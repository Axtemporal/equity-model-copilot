"""Reverse DCF / break-even solver (backlog item — "what does the screen price imply?").

Not a discrete scenario: the inversion of the model. Given a market price, it back-solves the
single assumption that reconciles the DCF to that price, holding the rest fixed — and, per
assumption, how far it can deteriorate before the implied value falls to the price (upside → 0).

It reads the FCFF stream and the EV→equity bridge straight off the recalculated Valuation tab
(so it inherits exactly the model's DCF), then solves in closed form / by bisection in Python —
no spreadsheet circularity, no extra dependency. Valuation-parameter inversions (WACC, terminal
g, a uniform FCFF haircut) are exact and fast because the FCFF path is independent of them.
Inverting operational premises (revenue growth, margin) would require re-running the three
statements per iteration — left as a follow-up; flagged in the report.

Usage:
    python -m engine.reverse_dcf <model.xlsx> <market_price_per_share>
"""
from __future__ import annotations

import sys
from dataclasses import dataclass

from engine.harness.recalc import recalc_workbook


# ─── extraction ─────────────────────────────────────────────────────────────

@dataclass
class DcfInputs:
    fcff: list[float]      # explicit-period FCFF, annual, in order
    bridge: float          # net debt + leases + minority (already signed; added to EV → equity)
    shares: float
    wacc: float            # the model's current WACC
    g: float               # the model's current terminal growth
    nopat_last: float      # year-N NOPAT (terminal value is rebuilt from this, not from FCFF[-1])
    troic: float           # terminal ROIC (stable phase) — sets the terminal reinvestment rate
    ev: float              # the model's current enterprise value (for reference)
    price: float           # the model's current implied value per share


def _sheet(calc, name: str):
    for s in calc.sheetnames:
        if s.upper() == name.upper():
            return calc[s]
    raise KeyError(f"sheet {name!r} not found (have {calc.sheetnames})")


def _row(ws, needle: str) -> int | None:
    for r in range(1, ws.max_row + 1):
        v = ws.cell(r, 2).value
        if isinstance(v, str) and needle.lower() in v.lower():
            return r
    return None


def _val(ws, needle: str, col: int = 4) -> float:
    r = _row(ws, needle)
    v = ws.cell(r, col).value if r else None
    return float(v) if isinstance(v, (int, float)) else 0.0


def _last_numeric(ws, needle: str, start_col: int = 4) -> float:
    """Last contiguous numeric value on the row matching `needle` (the year-N column)."""
    r = _row(ws, needle)
    if not r:
        return 0.0
    last, c = 0.0, start_col
    while True:
        cell = ws.cell(r, c).value
        if isinstance(cell, (int, float)):
            last = float(cell); c += 1
        else:
            break
    return last


def extract_dcf_inputs(model_path: str, *, backend: str = "formulas") -> DcfInputs:
    calc, _ = recalc_workbook(model_path, backend=backend)
    v = _sheet(calc, "Valuation")
    # FCFF row: read contiguous numeric forecast columns starting at column 4 (D).
    fr = _row(v, "(=) FCFF")
    fcff: list[float] = []
    c = 4
    while fr:
        cell = v.cell(fr, c).value
        if isinstance(cell, (int, float)):
            fcff.append(float(cell)); c += 1
        else:
            break
    bridge = _val(v, "(−) Net debt") + _val(v, "(−) Lease liabilities") + _val(v, "(−) Minority interest")
    return DcfInputs(
        fcff=fcff,
        bridge=bridge,
        shares=_val(v, "Shares outstanding"),
        wacc=_val(v, "(=) WACC"),
        g=_val(v, "Terminal growth"),
        nopat_last=_last_numeric(v, "NOPAT"),
        troic=_val(v, "Terminal ROIC"),
        ev=_val(v, "(=) Enterprise value"),
        price=_val(v, "Implied value per share"),
    )


# ─── the DCF (mirrors the Valuation tab exactly) ─────────────────────────────

def enterprise_value(fcff: list[float], wacc: float, g: float,
                     *, nopat_last: float, troic: float, scale: float = 1.0) -> float:
    n = len(fcff)
    pv = sum(cf * scale / (1 + wacc) ** (t + 1) for t, cf in enumerate(fcff))
    # Terminal value rebuilt from NOPAT with a consistent reinvestment rate (g ÷ ROIC),
    # matching the Valuation tab. The uniform haircut `scale` hits terminal cash too.
    reinv = g / troic if troic else 0.0
    tfcff = nopat_last * scale * (1 + g) * (1 - reinv)
    tv = tfcff / (wacc - g) if wacc > g else float("inf")
    return pv + tv / (1 + wacc) ** n


def value_per_share(inp: DcfInputs, wacc: float, g: float, fcff_scale: float = 1.0) -> float:
    ev = enterprise_value(inp.fcff, wacc, g, nopat_last=inp.nopat_last,
                          troic=inp.troic, scale=fcff_scale)
    if inp.shares == 0:
        return 0.0
    return (ev + inp.bridge) / inp.shares


# ─── solvers ─────────────────────────────────────────────────────────────────

def _bisect(f, lo: float, hi: float, target: float, *, tol: float = 1e-7, iters: int = 200):
    """Solve f(x)=target on [lo,hi] assuming f is monotonic. Returns None if not bracketed."""
    flo, fhi = f(lo) - target, f(hi) - target
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if (flo > 0) == (fhi > 0):
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def implied_wacc(inp: DcfInputs, market: float) -> float | None:
    # value falls as WACC rises → monotonic decreasing
    return _bisect(lambda w: value_per_share(inp, w, inp.g), inp.g + 1e-4, 1.0, market)


def implied_g(inp: DcfInputs, market: float) -> float | None:
    # value rises with g (g < WACC) → monotonic increasing
    return _bisect(lambda gg: value_per_share(inp, inp.wacc, gg), -0.5, inp.wacc - 1e-4, market)


def implied_fcff_scale(inp: DcfInputs, market: float) -> float | None:
    # equity is linear in a uniform FCFF scale: solve in closed form
    ev0 = enterprise_value(inp.fcff, inp.wacc, inp.g, nopat_last=inp.nopat_last, troic=inp.troic)
    if ev0 == 0:
        return None
    return (market * inp.shares - inp.bridge) / ev0


# ─── report ──────────────────────────────────────────────────────────────────

def reverse_report(model_path: str, market: float, *, backend: str = "formulas") -> str:
    inp = extract_dcf_inputs(model_path, backend=backend)
    iw = implied_wacc(inp, market)
    ig = implied_g(inp, market)
    isc = implied_fcff_scale(inp, market)
    pct = lambda x: f"{x*100:.2f}%" if isinstance(x, (int, float)) else "—"
    lines = [
        "REVERSE DCF / BREAK-EVEN",
        f"  Model implied value/share : {inp.price:.2f}",
        f"  Market (screen) price      : {market:.2f}",
        f"  Upside at current premises : {(inp.price/market-1)*100:+.1f}%" if market else "  (no market price)",
        "",
        "  What the screen price implies (holding everything else at the base case):",
        f"    Implied WACC               : {pct(iw)}   (base {pct(inp.wacc)})",
        f"    Implied terminal growth g  : {pct(ig)}   (base {pct(inp.g)})",
        f"    Implied FCFF level         : {pct(isc) if isc is None else f'{isc*100:.1f}% of base'}"
        + (f"  -> cash flows can fall {(1-isc)*100:.1f}% before upside zeros" if isinstance(isc, float) and isc <= 1 else ""),
        "",
        "  Note: revenue-growth / margin inversions need a model re-run per iteration (follow-up).",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("usage: python -m engine.reverse_dcf <model.xlsx> <market_price_per_share>")
    print(reverse_report(sys.argv[1], float(sys.argv[2])))

"""Single base template + input introspection + sector knowledge location.

Architecture (the build flow, defined 2026-06-17 — see planejamento §16):
  1. user provides financial + operational inputs
  2. identify the company (input title) and sector (signal heuristic; ask if unsure)
  3. introspect the operational tab — what drivers/sections the company discloses
  4. locate the sector method card in knowledge/sector_modeling_rules/sectors/<slug>.md
  5. the engine renders base.yaml + an operational layer ASSEMBLED from (3),
     grounded in (4)

There are NO per-sector template files. Sector knowledge lives in the method cards
(knowledge/sector_modeling_rules/) and is the single source of sector truth.
`base.yaml` is the only template — the universal three-statement + schedules scaffold.

Usage in build_model.py:
    from template_loader import analyze_input, BuildDiagnostics

    an = analyze_input(fin, op, orow, ohdr, hist_q, sector="oil_and_gas")
    diag = BuildDiagnostics()
    diag.log_analysis(an)
    # ... render the model using an.op_row(label), an.assets, an.schedules ...
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field
from pathlib import Path

ROOT          = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
# Method cards live in the sectors/ subfolder of the 3-layer llm-wiki
# (sources/ raw · sectors/ by-sector cards · wiki/ by-concept articles).
CARDS_DIR     = ROOT / "knowledge" / "sector_modeling_rules" / "sectors"

# The operational INPUT template contract — how the user fills "Input Operational".
# This describes the input FORMAT, not sector economics (those live in the method
# cards). Stage 2 generalizes introspection to arbitrary input shapes.
ASSET_SECTION_HEADER = "PRODUCTION BY ASSET"
ASSET_SETUP_HEADER   = "Asset 1 name"
LIFT_SECTION         = "LIFTING COST BY ASSET"
CAPEX_SECTION        = "CAPEX BY ASSET"
ASSET_MAX_SLOTS      = 8

# Bootstrap sector-identification heuristic: distinctive operational labels per sector.
# This is a deterministic fallback; the AI layer does the real identification by reading
# the input + card. Returns None when no signal matches → the caller asks the user.
SECTOR_SIGNALS = {
    "oil_and_gas": ["Brent average", "Sales volume", ASSET_SECTION_HEADER],
    "telecom":     ["ARPU total", "Total lines", "ARPU TIM Live"],
}


# ─── base.yaml loading ────────────────────────────────────────────────────────

def load_base_template() -> dict:
    path = TEMPLATES_DIR / "base.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ─── data classes ─────────────────────────────────────────────────────────────

@dataclass
class AssetInfo:
    idx: int           # 0-based slot index
    name: str
    prod_row: int
    lift_row: int | None
    capex_row: int | None


@dataclass
class InputAnalysis:
    """Everything the engine learned about this specific input + its sector."""
    company: str                                  # from the input title
    sector: str | None                            # identified or provided slug
    card_path: Path | None                        # method card, if it exists
    card_exists: bool
    assets: list[AssetInfo] = field(default_factory=list)
    op_labels: dict[str, int] = field(default_factory=dict)   # label -> row (operational tab)
    op_sections: dict[str, int] = field(default_factory=dict) # SECTION HEADER -> row
    schedules: dict[str, bool] = field(default_factory=dict)  # from base.yaml
    max_slots: int = ASSET_MAX_SLOTS

    def op_row(self, label: str) -> int | None:
        """Row of an operational input by its exact label, or None if absent."""
        return self.op_labels.get(label)

    def has_op(self, label: str) -> bool:
        return label in self.op_labels


# ─── identification ───────────────────────────────────────────────────────────

def identify_company(fin_sheet) -> str:
    return (fin_sheet["B1"].value or "Unknown").strip()


def identify_sector(op_labels: dict[str, int], sector: str | None = None) -> str | None:
    """Return the sector slug. If `sector` is given, trust it. Otherwise match
    distinctive operational labels. Returns None when ambiguous → caller asks."""
    if sector:
        return sector
    for slug, signals in SECTOR_SIGNALS.items():
        if sum(1 for s in signals if s in op_labels) >= 2:
            return slug
    return None


def locate_card(sector: str | None) -> tuple[Path | None, bool]:
    if not sector:
        return None, False
    path = CARDS_DIR / f"{sector}.md"
    return path, path.exists()


# ─── introspection ────────────────────────────────────────────────────────────

def introspect_operational(orow: dict) -> tuple[dict, dict]:
    """Split the operational label→row map into (all labels, section headers).
    Section headers are detected as ALL-CAPS labels (the input template convention)."""
    sections = {lbl: r for lbl, r in orow.items()
                if lbl.isupper() and len(lbl) > 3}
    return dict(orow), sections


def scan_assets(op_sheet, orow, ohdr, hist_q) -> list[AssetInfo]:
    """Detect active per-asset slots: rows below the production section header that
    have at least one historical value. Generic over the input template contract."""
    assets: list[AssetInfo] = []
    if ASSET_SECTION_HEADER not in orow or ASSET_SETUP_HEADER not in orow:
        return assets
    prod0  = orow[ASSET_SECTION_HEADER]
    setup0 = orow[ASSET_SETUP_HEADER]
    for i in range(ASSET_MAX_SLOTS):
        rr = prod0 + 1 + i
        has_data = any(
            op_sheet.cell(row=rr, column=ohdr.get(q, 0)).value is not None
            for q in hist_q
        )
        if has_data:
            assets.append(AssetInfo(
                idx=i,
                name=(op_sheet.cell(row=setup0 + i, column=3).value or f"Asset {i + 1}"),
                prod_row=rr,
                lift_row=(orow[LIFT_SECTION]  + 1 + i) if LIFT_SECTION  in orow else None,
                capex_row=(orow[CAPEX_SECTION] + 1 + i) if CAPEX_SECTION in orow else None,
            ))
    return assets


# ─── the single entry point ───────────────────────────────────────────────────

def analyze_input(fin_sheet, op_sheet, orow, ohdr, hist_q, sector: str | None = None) -> InputAnalysis:
    """Run the read-and-understand stages (2-4 of the flow) against a real input."""
    base = load_base_template()
    op_labels, op_sections = introspect_operational(orow)

    company    = identify_company(fin_sheet)
    sector_id  = identify_sector(op_labels, sector)
    card, ok   = locate_card(sector_id)
    assets     = scan_assets(op_sheet, orow, ohdr, hist_q)
    schedules  = {name: bool(cfg.get("enabled", False))
                  for name, cfg in base.get("schedules", {}).items()}

    return InputAnalysis(
        company=company,
        sector=sector_id,
        card_path=card,
        card_exists=ok,
        assets=assets,
        op_labels=op_labels,
        op_sections=op_sections,
        schedules=schedules,
        max_slots=ASSET_MAX_SLOTS,
    )


# ─── diagnostic log ───────────────────────────────────────────────────────────

class BuildDiagnostics:
    """Collects build-time observations and writes them to a text file.
    Diagnostic output only — not part of the model or the app."""

    def __init__(self):
        self._lines: list[str] = []

    def log(self, msg: str = ""):
        self._lines.append(msg)

    def log_header(self, input_path: str, output_path: str):
        self.log("=" * 60)
        self.log("BUILD DIAGNOSTIC LOG")
        self.log("=" * 60)
        self.log(f"Input  : {input_path}")
        self.log(f"Output : {output_path}")
        self.log()

    def log_analysis(self, an: InputAnalysis):
        self.log("IDENTIFICATION")
        self.log(f"  Company : {an.company}")
        self.log(f"  Sector  : {an.sector or '(unidentified — ask the user)'}")
        if an.sector:
            tag = "found" if an.card_exists else "MISSING"
            self.log(f"  Card    : {an.card_path.name if an.card_path else '-'}  [{tag}]")
        self.log()

        self.log("ASSET DETECTION")
        if an.assets:
            for a in an.assets:
                parts = [f"  [{a.idx + 1}] {a.name:<24}  prod_row={a.prod_row}"]
                if a.lift_row:
                    parts.append(f"  lift_row={a.lift_row}")
                if a.capex_row:
                    parts.append(f"  capex_row={a.capex_row}")
                self.log("".join(parts))
        else:
            self.log("  (none — per-asset section absent or no historical data)")
        self.log()

        self.log("OPERATIONAL SECTIONS DISCLOSED")
        for sec, row in an.op_sections.items():
            self.log(f"  - {sec}  (row {row})")
        self.log()

        self.log("SCHEDULES (from base.yaml)")
        for name, enabled in an.schedules.items():
            self.log(f"  [{'on' if enabled else '- '}] {name}")
        self.log()

    def write(self, path: str) -> str:
        Path(path).write_text("\n".join(self._lines), encoding="utf-8")
        return path

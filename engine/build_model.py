"""Engine v0: reads the filled input workbook and builds the integrated model.

The model is written as a copy of the input + new tabs (Cover, Premises,
Operational Model, IS, BS, CF, Schedules), so the input tabs stay inside the
final file and all history on the model tabs is a formula linking the input
(green). Projection: quarterly through the end of the year after the last
historical quarter, then annual through year 10. Assumptions live in the
Premises tab (blue, auto-seeded from the last historical value) and are the
model's only editable cells. No circularity: no revolver in v0 (cash can go
negative; the balance check still closes).

Usage: python engine/build_model.py <filled_input.xlsx> <output_model.xlsx>
"""

import shutil
import sys
from openpyxl import load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

FONT = "Arial"
BLUE = Font(name=FONT, size=10, color="0000FF")
BLACK = Font(name=FONT, size=10, color="000000")
GREEN = Font(name=FONT, size=10, color="006100")
BOLD = Font(name=FONT, size=10, bold=True)
TITLE = Font(name=FONT, size=14, bold=True)
SUB = Font(name=FONT, size=9, italic=True, color="595959")
WHITE_BOLD = Font(name=FONT, size=10, bold=True, color="FFFFFF")
NAVY = PatternFill("solid", start_color="1F3864")
GRAY_Y = PatternFill("solid", start_color="EDEDED")
PROJ_FILL = PatternFill("solid", start_color="FFF7E6")   # marks projection columns
THIN_BOT = Border(bottom=Side(style="thin", color="9DC3E6"))
NUM_MN = '#,##0;(#,##0);"-"'
NUM_1D = '#,##0.0;(#,##0.0);"-"'
NUM_2D = '#,##0.00;(#,##0.00);"-"'
PCT = '0.0%;(0.0%);"-"'
FIRST_COL = 4
HDR = 5
PROJ_YEARS_ANNUAL = 8        # annual years beyond the quarterly block (through year 10)

L = get_column_letter


# --------------------------------------------------------------------- input parsing
def header_map(ws):
    return {ws.cell(row=HDR, column=c).value: c
            for c in range(FIRST_COL, ws.max_column + 1)
            if ws.cell(row=HDR, column=c).value}


def label_rows(ws):
    out = {}
    for r in range(HDR + 1, ws.max_row + 1):
        v = ws.cell(row=r, column=2).value
        if isinstance(v, str) and v.strip() and v not in out:
            out[v.strip()] = r
    return out


def q_seq(label):  # '3Q24' -> (2024, 3)
    return 2000 + int(label[2:]), int(label[0])


def detect_history(fin):
    hdr = header_map(fin)
    rev_row = label_rows(fin)["(=) Net revenue"]
    filled = [p for p, c in hdr.items()
              if "Q" in p and fin.cell(row=rev_row, column=c).value is not None]
    filled.sort(key=q_seq)
    if not filled:
        raise SystemExit("input has no filled quarter on the Net revenue line")
    return filled


# --------------------------------------------------------------------- timeline
def build_timeline(hist_quarters):
    """List of model periods: dicts {label, kind, year, q}.

    kind: QH historical quarter | QP projected quarter | YB year closing a block
          of 4 quarters | YS pure annual year (no quarters)
    """
    first_y = q_seq(hist_quarters[0])[0]
    last_y, last_q = q_seq(hist_quarters[-1])
    proj_end_y = last_y + 1
    tl = []
    for y in range(first_y, proj_end_y + 1):
        for q in range(1, 5):
            lbl = f"{q}Q{str(y)[2:]}"
            if (y, q) <= (last_y, last_q):
                if lbl in hist_quarters or True:   # quarter inside the historical range
                    kind = "QH" if lbl in hist_quarters else "QP"
                    tl.append(dict(label=lbl, kind=kind, year=y, q=q))
            else:
                tl.append(dict(label=lbl, kind="QP", year=y, q=q))
        tl.append(dict(label=str(y), kind="YB", year=y, q=None))
    for y in range(proj_end_y + 1, proj_end_y + 1 + PROJ_YEARS_ANNUAL):
        tl.append(dict(label=str(y), kind="YS", year=y, q=None))
    for i, p in enumerate(tl):
        p["col"] = FIRST_COL + i
    return tl


def block_cols(tl, yb):       # columns of the 4 quarters of year YB
    return [p["col"] for p in tl if p["q"] and p["year"] == yb["year"]]


def prev_period(tl, i):
    """Previous period in the real sequence (quarters chain skipping YB; YS chains to YB/YS)."""
    p = tl[i]
    if p["kind"] in ("QH", "QP"):
        for j in range(i - 1, -1, -1):
            if tl[j]["q"]:
                return tl[j]
        return None
    for j in range(i - 1, -1, -1):
        if tl[j]["kind"] in ("YB", "YS"):
            return tl[j]
    return None


def yoy_col(tl, i):
    p = tl[i]
    for j in range(len(tl)):
        t = tl[j]
        if p["q"] and t["q"] == p["q"] and t["year"] == p["year"] - 1:
            return t["col"]
        if not p["q"] and not t["q"] and t["year"] == p["year"] - 1:
            return t["col"]
    return None


# --------------------------------------------------------------------- writing
def sheet_shell(wb, name, purpose, tl, tab_color="305496"):
    ws = wb.create_sheet(name)
    ws.sheet_properties.tabColor = tab_color
    ws["B1"] = wb["Input Financials"]["B1"].value or "Model"
    ws["B1"].font = TITLE
    ws["B2"], ws["B2"].font = purpose, SUB
    ws["B3"] = "History = link to the input (green). Projection = formulas driven by the Premises tab."
    ws["B3"].font = SUB
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 10
    ws.freeze_panes = f"{L(FIRST_COL)}{HDR + 1}"
    for p in tl:
        c = ws.cell(row=HDR, column=p["col"], value=p["label"])
        c.font, c.border = BOLD, THIN_BOT
        c.alignment = Alignment(horizontal="center")
        if not p["q"]:
            c.fill = GRAY_Y
        elif p["kind"] == "QP":
            c.fill = PROJ_FILL
        ws.column_dimensions[L(p["col"])].width = 9.5
    ws.cell(row=HDR, column=2, value="Line item").font = BOLD
    ws.cell(row=HDR, column=3, value="Unit").font = BOLD
    return ws


def section(ws, row, text, tl):
    ws.cell(row=row, column=2, value=text).font = WHITE_BOLD
    for col in range(2, FIRST_COL + len(tl)):
        ws.cell(row=row, column=col).fill = NAVY
    return row + 1


class Line:
    """One model line: history links the input; projection uses per-column-type functions."""

    def __init__(self, ws, row, label, unit, fmt=NUM_MN):
        self.ws, self.row = ws, row
        ws.cell(row=row, column=2, value=label).font = BLACK
        ws.cell(row=row, column=3, value=unit).font = SUB

    def fill(self, tl, hist=None, qp=None, yb="sum", ys=None):
        for i, p in enumerate(tl):
            cell = self.ws.cell(row=self.row, column=p["col"])
            cell.number_format = self.fmt if hasattr(self, "fmt") else NUM_MN
            if not p["q"]:
                cell.fill = GRAY_Y
            elif p["kind"] == "QP":
                cell.fill = PROJ_FILL
            r = self.row
            if p["kind"] == "QH":
                if hist:
                    cell.value, cell.font = hist(p), GREEN
            elif p["kind"] == "QP":
                if qp:
                    cell.value, cell.font = qp(p, i), BLACK
            elif p["kind"] == "YB":
                bc = block_cols(tl, p)
                if yb == "sum":
                    cell.value = f"=SUM({L(bc[0])}{r}:{L(bc[-1])}{r})"
                elif yb == "eop":
                    cell.value = f"={L(bc[-1])}{r}"
                elif yb == "avg":
                    cell.value = f'=IFERROR(AVERAGE({L(bc[0])}{r}:{L(bc[-1])}{r}),"-")'
                elif callable(yb):
                    cell.value = yb(p, i)
                cell.font = BLACK
            elif p["kind"] == "YS":
                if ys:
                    cell.value, cell.font = ys(p, i), BLACK
        return self


def add_line(ws, row, label, unit, fmt, tl, **kw):
    ln = Line(ws, row, label, unit)
    ln.fmt = fmt
    ln.fill(tl, **kw)
    return row + 1


# --------------------------------------------------------------------- assumptions
def seed_premises(wb, tl, fin, op, assets, seeds):
    proj = [p for p in tl if p["kind"] in ("QP", "YS")]
    ws = wb.create_sheet("Premises")
    ws.sheet_properties.tabColor = "BF8F00"
    ws["B1"], ws["B1"].font = "Premises — projection assumptions (blue cells)", TITLE
    ws["B2"] = ("Auto-seed = last historical value ('seed' method, to be replaced in the "
                "line-by-line session). Annual years use the annualized quarterly seed where it makes sense.")
    ws["B2"].font = SUB
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 10
    ws.freeze_panes = f"D{HDR + 1}"
    cols = {}
    for k, p in enumerate(proj):
        c = ws.cell(row=HDR, column=FIRST_COL + k, value=p["label"])
        c.font, c.fill = BOLD, PROJ_FILL
        c.alignment = Alignment(horizontal="center")
        ws.column_dimensions[L(FIRST_COL + k)].width = 9.5
        cols[p["label"]] = FIRST_COL + k
    ws.cell(row=HDR, column=2, value="Premise").font = BOLD
    ws.cell(row=HDR, column=3, value="Unit").font = BOLD

    rows = {}
    r = HDR + 2
    for key, label, unit, fmt, qval, mult_y in seeds:
        ws.cell(row=r, column=2, value=label).font = BLACK
        ws.cell(row=r, column=3, value=unit).font = SUB
        for p in proj:
            c = ws.cell(row=r, column=cols[p["label"]])
            c.value = round(qval * (mult_y if p["kind"] == "YS" else 1), 6)
            c.font, c.number_format = BLUE, fmt
        ws.cell(row=r, column=2).comment = Comment(
            "Auto-seeded from the last historical value. Replace in the assumption session "
            "(method, source and rationale in the Assumptions tab).", "engine")
        rows[key] = r
        r += 1
    return ws, rows, cols


def prem(ws_name, rows, cols):
    def ref(key, p):
        return f"='{ws_name}'!{L(cols[p['label']])}{rows[key]}"
    def raw(key, p):
        return f"'{ws_name}'!{L(cols[p['label']])}{rows[key]}"
    return ref, raw


# --------------------------------------------------------------------- main
def main(input_path, out_path):
    shutil.copy(input_path, out_path)
    wb = load_workbook(out_path)
    fin, op = wb["Input Financials"], wb["Input Operational"]
    fhdr, ohdr = header_map(fin), header_map(op)
    frow, orow = label_rows(fin), label_rows(op)

    hist_q = detect_history(fin)
    tl = build_timeline(hist_q)
    last = hist_q[-1]
    lc_f, lc_o = fhdr[last], ohdr[last]

    # active assets = production rows with at least some historical data
    prod0 = frow_sec = orow["PRODUCTION BY ASSET"]
    setup0 = orow["Asset 1 name"]
    assets = []
    for i in range(8):
        rr = prod0 + 1 + i
        if any(op.cell(row=rr, column=ohdr[q]).value is not None for q in hist_q):
            assets.append(dict(idx=i, name=op.cell(row=setup0 + i, column=3).value,
                               prod_row=rr, lift_row=orow["LIFTING COST BY ASSET"] + 1 + i,
                               capex_row=orow["CAPEX BY ASSET"] + 1 + i))

    g = lambda ws, rr, cc: ws.cell(row=rr, column=cc).value or 0
    total_prod = sum(g(op, a["prod_row"], lc_o) for a in assets)
    lift_w = (sum(g(op, a["prod_row"], lc_o) * g(op, a["lift_row"], lc_o) for a in assets)
              / total_prod if total_prod else 0)
    rev_l = g(fin, frow["(=) Net revenue"], lc_f)
    vol_l = g(op, orow["Sales volume"], lc_o)
    seeds = [("brent", "Brent average", "USD/bbl", NUM_1D, g(op, orow["Brent average"], lc_o), 1),
             ("disc", "Realized premium (discount) to Brent", "USD/bbl", NUM_1D,
              g(op, orow["Realized price"], lc_o) - g(op, orow["Brent average"], lc_o), 1),
             ("lift", "Lifting cost (weighted avg)", "USD/boe", NUM_1D, lift_w, 1),
             ("roy", "Royalties (% of revenue)", "%", PCT,
              g(fin := fin, frow["(=) Net revenue"], lc_f) and
              (g(op, orow["Royalties and government take"], lc_o) / rev_l if rev_l else 0.1), 1),
             ("depl", "Depletion rate", "USD/boe", NUM_1D,
              (g(fin, frow["memo: (+) Depreciation, depletion & amortization"], lc_f) / vol_l * 1000)
              if vol_l else 8.0, 1),
             ("ga", "G&A (% of revenue)", "%", PCT,
              -g(fin, frow["(-) General & administrative expenses"], lc_f) / rev_l if rev_l else 0.04, 1),
             ("expl", "Exploration expenses (per period)", "USD mn", NUM_MN,
              g(fin, frow["(-) Exploration expenses"], lc_f), 4),
             ("finres", "Financial result (per period)", "USD mn", NUM_MN,
              g(fin, frow["(+/-) Financial result"], lc_f), 4),
             ("tax", "Effective tax rate (% of EBT)", "%", PCT,
              -g(fin, frow["(-) Income taxes"], lc_f) / g(fin, frow["(=) EBT"], lc_f)
              if g(fin, frow["(=) EBT"], lc_f) else 0.25, 1),
             ("payout", "Dividend payout (% of NI)", "%", PCT, 0.0, 1),
             ("days", "Days in period", "days", NUM_1D, 91.25, 4)]
    for a in assets:
        seeds.insert(0, (f"prod{a['idx']}", f"Production — {a['name']}", "kboe/d", NUM_1D,
                         g(op, a["prod_row"], lc_o), 1))
        seeds.append((f"capex{a['idx']}", f"Capex — {a['name']} (per period)", "USD mn", NUM_MN,
                      g(op, a["capex_row"], lc_o), 4))

    pws, prows, pcols = seed_premises(wb, tl, fin, op, assets, seeds)
    P, Praw = prem("Premises", prows, pcols)

    # ---------------------------------------------------------- Operational Model
    om = sheet_shell(wb, "Operational Model", "Operational drivers → financial lines", tl)
    r = HDR + 2
    r = section(om, r, "PRODUCTION (kboe/d)", tl)
    om_prod = {}
    for a in assets:
        om_prod[a["idx"]] = r
        r = add_line(om, r, a["name"], "kboe/d", NUM_1D, tl,
                     hist=lambda p, a=a: f"='Input Operational'!{L(ohdr[p['label']])}{a['prod_row']}",
                     qp=lambda p, i, a=a: P(f"prod{a['idx']}", p),
                     yb="avg", ys=lambda p, i, a=a: P(f"prod{a['idx']}", p))
    row_tprod = r
    r = add_line(om, r, "(=) Total production", "kboe/d", NUM_1D, tl,
                 hist=lambda p: f"=SUM({L(p['col'])}{min(om_prod.values())}:{L(p['col'])}{max(om_prod.values())})",
                 qp=lambda p, i: f"=SUM({L(p['col'])}{min(om_prod.values())}:{L(p['col'])}{max(om_prod.values())})",
                 yb="avg",
                 ys=lambda p, i: f"=SUM({L(p['col'])}{min(om_prod.values())}:{L(p['col'])}{max(om_prod.values())})")
    r += 1
    r = section(om, r, "VOLUMES AND PRICES", tl)
    row_vol = r
    r = add_line(om, r, "Sales volume", "kboe", NUM_MN, tl,
                 hist=lambda p: f"='Input Operational'!{L(ohdr[p['label']])}{orow['Sales volume']}",
                 qp=lambda p, i: f"={L(p['col'])}{row_tprod}*{Praw('days', p)}",
                 yb="sum",
                 ys=lambda p, i: f"={L(p['col'])}{row_tprod}*{Praw('days', p)}")
    row_brent = r
    r = add_line(om, r, "Brent average", "USD/bbl", NUM_1D, tl,
                 hist=lambda p: f"='Input Operational'!{L(ohdr[p['label']])}{orow['Brent average']}",
                 qp=lambda p, i: P("brent", p), yb="avg", ys=lambda p, i: P("brent", p))
    row_real = r
    r = add_line(om, r, "Realized price", "USD/boe", NUM_1D, tl,
                 hist=lambda p: f"='Input Operational'!{L(ohdr[p['label']])}{orow['Realized price']}",
                 qp=lambda p, i: f"={L(p['col'])}{row_brent}+{Praw('disc', p)}",
                 yb="avg",
                 ys=lambda p, i: f"={L(p['col'])}{row_brent}+{Praw('disc', p)}")
    r += 1
    r = section(om, r, "REVENUE AND COST BUILD (USD mn)", tl)
    row_rev = r
    rev_f = lambda p, i: f"={L(p['col'])}{row_vol}*{L(p['col'])}{row_real}/1000"
    r = add_line(om, r, "(=) Revenue build (volume × price)", "USD mn", NUM_MN, tl,
                 hist=lambda p: f"='Input Financials'!{L(fhdr[p['label']])}{frow['(=) Net revenue']}",
                 qp=rev_f, yb="sum", ys=rev_f)
    row_liftc = r
    lift_f = lambda p, i: f"=-{L(p['col'])}{row_vol}*{Praw('lift', p)}/1000"
    r = add_line(om, r, "(-) Lifting cost", "USD mn", NUM_MN, tl, qp=lift_f, yb="sum", ys=lift_f)
    row_royc = r
    roy_f = lambda p, i: f"=-{L(p['col'])}{row_rev}*{Praw('roy', p)}"
    r = add_line(om, r, "(-) Royalties", "USD mn", NUM_MN, tl, qp=roy_f, yb="sum", ys=roy_f)
    row_depl = r
    depl_f = lambda p, i: f"=-{L(p['col'])}{row_vol}*{Praw('depl', p)}/1000"
    r = add_line(om, r, "(-) Depletion (DD&A)", "USD mn", NUM_MN, tl,
                 hist=lambda p: f"=-'Input Financials'!{L(fhdr[p['label']])}{frow['memo: (+) Depreciation, depletion & amortization']}",
                 qp=depl_f, yb="sum", ys=depl_f)
    row_capext = r
    cap_f = lambda p, i: "=" + "+".join(Praw(f"capex{a['idx']}", p) for a in assets)
    r = add_line(om, r, "(=) Total capex", "USD mn", NUM_MN, tl,
                 hist=lambda p: f"='Input Operational'!{L(ohdr[p['label']])}{orow['CAPEX BY ASSET'] + 9}",
                 qp=cap_f, yb="sum", ys=cap_f)

    OM = "Operational Model"

    # ---------------------------------------------------------- Schedules
    sc = sheet_shell(wb, "Schedules", "Roll-forwards: PP&E, retained earnings, cash", tl)
    r = HDR + 2
    rows_sc = {}
    def corkscrew(r, name, bop_seed, plus, minus, fmt=NUM_MN):
        r = section(sc, r, name, tl)
        rb, rp, rm, re_ = r, r + 1, r + 2, r + 3
        def bop(p, i):
            pv = prev_period(tl, i)
            if pv is None or (pv["kind"] == "QH"):
                return bop_seed(p)
            if p["kind"] == "YB":
                bc = block_cols(tl, p)
                return f"={L(bc[0])}{rb}"
            return f"={L(pv['col'])}{re_}"
        add_line(sc, rb, "BOP", "USD mn", fmt, tl,
                 hist=lambda p: None, qp=bop, yb=bop, ys=bop)
        add_line(sc, rp, "(+) additions", "USD mn", fmt, tl, qp=plus, yb="sum", ys=plus)
        add_line(sc, rm, "(-) reductions", "USD mn", fmt, tl, qp=minus, yb="sum", ys=minus)
        eop = lambda p, i: f"=SUM({L(p['col'])}{rb}:{L(p['col'])}{rm})"
        def eop_yb(p, i):
            bc = block_cols(tl, p)
            return f"={L(bc[-1])}{re_}"
        add_line(sc, re_, "(=) EOP", "USD mn", fmt, tl, qp=eop, yb=eop_yb, ys=eop)
        return re_ + 2, dict(bop=rb, plus=rp, minus=rm, eop=re_)

    seed_ppe = lambda p: f"='Input Financials'!{L(fhdr[last])}{frow['PP&E']}"
    r, rows_sc["ppe"] = corkscrew(
        r, "PP&E ROLL-FORWARD", seed_ppe,
        plus=lambda p, i: f"='{OM}'!{L(p['col'])}{row_capext}",
        minus=lambda p, i: f"='{OM}'!{L(p['col'])}{row_depl}")
    seed_re = lambda p: f"='Input Financials'!{L(fhdr[last])}{frow['Retained earnings (accumulated)']}"
    NI_REF = {}   # filled later (IS); a deferred-callback placeholder won't work: IS comes later.
    # Order: build IS before RE/cash? RE needs NI; IS only needs OM. So: IS now.

    # ---------------------------------------------------------- IS
    is_ = sheet_shell(wb, "IS", "Integrated income statement", tl)
    ri = HDR + 2
    ri = section(is_, ri, "INCOME STATEMENT", tl)
    rows_is = {}
    def is_line(label, unit, fmt, **kw):
        nonlocal ri
        rows_is[label] = ri
        ri = add_line(is_, ri, label, unit, fmt, tl, **kw)
    hist_fin = lambda lbl: (lambda p: f"='Input Financials'!{L(fhdr[p['label']])}{frow[lbl]}")
    is_line("(=) Net revenue", "USD mn", NUM_MN, hist=hist_fin("(=) Net revenue"),
            qp=lambda p, i: f"='{OM}'!{L(p['col'])}{row_rev}", yb="sum",
            ys=lambda p, i: f"='{OM}'!{L(p['col'])}{row_rev}")
    ryoy = ri
    def yoy_f(target_row):
        def f(p, i):
            pc = yoy_col(tl, i)
            return (f'=IFERROR({L(p["col"])}{target_row}/{L(pc)}{target_row}-1,"-")' if pc else None)
        return f
    ri = add_line(is_, ri, "% YoY", "%", PCT, tl,
                  hist=lambda p: yoy_f(rows_is["(=) Net revenue"])(p, [t["label"] for t in tl].index(p["label"])),
                  qp=yoy_f(rows_is["(=) Net revenue"]), yb=yoy_f(rows_is["(=) Net revenue"]),
                  ys=yoy_f(rows_is["(=) Net revenue"]))
    cogs_f = lambda p, i: (f"='{OM}'!{L(p['col'])}{row_liftc}+'{OM}'!{L(p['col'])}{row_royc}"
                           f"+'{OM}'!{L(p['col'])}{row_depl}")
    is_line("(-) Cost of goods sold", "USD mn", NUM_MN, hist=hist_fin("(-) Cost of goods sold"),
            qp=cogs_f, yb="sum", ys=cogs_f)
    gp_f = lambda p, i: f"={L(p['col'])}{rows_is['(=) Net revenue']}+{L(p['col'])}{rows_is['(-) Cost of goods sold']}"
    is_line("(=) Gross profit", "USD mn", NUM_MN, hist=hist_fin("(=) Gross profit"),
            qp=gp_f, yb="sum", ys=gp_f)
    ga_f = lambda p, i: f"=-{L(p['col'])}{rows_is['(=) Net revenue']}*{Praw('ga', p)}"
    is_line("(-) General & administrative expenses", "USD mn", NUM_MN,
            hist=hist_fin("(-) General & administrative expenses"), qp=ga_f, yb="sum", ys=ga_f)
    is_line("(-) Exploration expenses", "USD mn", NUM_MN, hist=hist_fin("(-) Exploration expenses"),
            qp=lambda p, i: P("expl", p), yb="sum", ys=lambda p, i: P("expl", p))
    is_line("(+/-) Other operating income (expenses)", "USD mn", NUM_MN,
            hist=hist_fin("(+/-) Other operating income (expenses)"),
            qp=lambda p, i: "=0", yb="sum", ys=lambda p, i: "=0")
    ebit_f = lambda p, i: (f"=SUM({L(p['col'])}{rows_is['(=) Gross profit']},"
                           f"{L(p['col'])}{rows_is['(-) General & administrative expenses']},"
                           f"{L(p['col'])}{rows_is['(-) Exploration expenses']},"
                           f"{L(p['col'])}{rows_is['(+/-) Other operating income (expenses)']})")
    is_line("(=) EBIT", "USD mn", NUM_MN, hist=hist_fin("(=) EBIT"), qp=ebit_f, yb="sum", ys=ebit_f)
    is_line("(+/-) Financial result", "USD mn", NUM_MN, hist=hist_fin("(+/-) Financial result"),
            qp=lambda p, i: P("finres", p), yb="sum", ys=lambda p, i: P("finres", p))
    ebt_f = lambda p, i: (f"={L(p['col'])}{rows_is['(=) EBIT']}+{L(p['col'])}{rows_is['(+/-) Financial result']}")
    is_line("(=) EBT", "USD mn", NUM_MN, hist=hist_fin("(=) EBT"), qp=ebt_f, yb="sum", ys=ebt_f)
    tax_f = lambda p, i: f"=-MAX({L(p['col'])}{rows_is['(=) EBT']},0)*{Praw('tax', p)}"
    is_line("(-) Income taxes", "USD mn", NUM_MN, hist=hist_fin("(-) Income taxes"),
            qp=tax_f, yb="sum", ys=tax_f)
    ni_f = lambda p, i: f"={L(p['col'])}{rows_is['(=) EBT']}+{L(p['col'])}{rows_is['(-) Income taxes']}"
    is_line("(=) Net income", "USD mn", NUM_MN, hist=hist_fin("(=) Net income"),
            qp=ni_f, yb="sum", ys=ni_f)
    da_f = lambda p, i: f"=-'{OM}'!{L(p['col'])}{row_depl}"
    is_line("memo: (+) DD&A", "USD mn", NUM_MN,
            hist=hist_fin("memo: (+) Depreciation, depletion & amortization"),
            qp=da_f, yb="sum", ys=da_f)
    ebitda_f = lambda p, i: f"={L(p['col'])}{rows_is['(=) EBIT']}+{L(p['col'])}{rows_is['memo: (+) DD&A']}"
    is_line("memo: (=) EBITDA", "USD mn", NUM_MN,
            hist=lambda p: f"={L(p['col'])}{rows_is['(=) EBIT']}+{L(p['col'])}{rows_is['memo: (+) DD&A']}",
            qp=ebitda_f, yb="sum", ys=ebitda_f)
    mg_f = lambda p, i: (f'=IFERROR({L(p["col"])}{rows_is["memo: (=) EBITDA"]}'
                         f'/{L(p["col"])}{rows_is["(=) Net revenue"]},"-")')
    ri = add_line(is_, ri, "EBITDA margin", "%", PCT, tl,
                  hist=lambda p: mg_f(p, 0), qp=mg_f, yb=mg_f, ys=mg_f)
    NI_ROW = rows_is["(=) Net income)"] if "(=) Net income)" in rows_is else rows_is["(=) Net income"]

    # ---------------------------------------------------------- Schedules (RE and cash)
    r, rows_sc["re"] = corkscrew(
        r, "RETAINED EARNINGS ROLL-FORWARD", seed_re,
        plus=lambda p, i: f"=IS!{L(p['col'])}{NI_ROW}",
        minus=lambda p, i: f"=-IS!{L(p['col'])}{NI_ROW}*{Praw('payout', p)}")

    # ---------------------------------------------------------- CF
    cf = sheet_shell(wb, "CF", "Cash flow: reconciliation", tl)
    rc = HDR + 2
    rc = section(cf, rc, "CASH FLOW STATEMENT", tl)
    rows_cf = {}
    def cf_line(label, src_label, qp=None, ys=None, yb="sum"):
        nonlocal rc
        rows_cf[label] = rc
        rc = add_line(cf, rc, label, "USD mn", NUM_MN, tl,
                      hist=hist_fin(src_label) if src_label else None,
                      qp=qp, yb=yb, ys=ys if ys else qp)
    cf_line("(=) Net income", "(=) Net income (CF basis)",
            qp=lambda p, i: f"=IS!{L(p['col'])}{NI_ROW}")
    cf_line("(+) D&A", "(+) D&A and non-cash items",
            qp=lambda p, i: f"=IS!{L(p['col'])}{rows_is['memo: (+) DD&A']}")
    cf_line("(+/-) Working capital changes", "(+/-) Working capital changes",
            qp=lambda p, i: "=0")
    cfo_f = lambda p, i: (f"=SUM({L(p['col'])}{rows_cf['(=) Net income']}:"
                          f"{L(p['col'])}{rows_cf['(+/-) Working capital changes']})")
    cf_line("(=) Cash from operations", "(=) Cash from operations", qp=cfo_f)
    cf_line("(-) Capex", "(-) Capex", qp=lambda p, i: f"=-'{OM}'!{L(p['col'])}{row_capext}")
    cfi_f = lambda p, i: f"={L(p['col'])}{rows_cf['(-) Capex']}"
    cf_line("(=) Cash from investing", "(=) Cash from investing", qp=cfi_f)
    cf_line("(-) Dividends", "(-) Dividends and buybacks",
            qp=lambda p, i: f"=-IS!{L(p['col'])}{NI_ROW}*{Praw('payout', p)}")
    cff_f = lambda p, i: f"={L(p['col'])}{rows_cf['(-) Dividends']}"
    cf_line("(=) Cash from financing", "(=) Cash from financing", qp=cff_f)
    dch_f = lambda p, i: (f"={L(p['col'])}{rows_cf['(=) Cash from operations']}"
                          f"+{L(p['col'])}{rows_cf['(=) Cash from investing']}"
                          f"+{L(p['col'])}{rows_cf['(=) Cash from financing']}")
    cf_line("(=) Net change in cash", "(=) Net change in cash", qp=dch_f)

    r, rows_sc["cash"] = corkscrew(
        r, "CASH ROLL-FORWARD", lambda p: f"='Input Financials'!{L(fhdr[last])}{frow['Cash and equivalents']}",
        plus=lambda p, i: f"=CF!{L(p['col'])}{rows_cf['(=) Net change in cash']}",
        minus=lambda p, i: "=0")

    def cash_line(label, key):
        nonlocal rc
        rows_cf[label] = rc
        def yb_cash(p, i):
            bc = block_cols(tl, p)
            cidx = bc[0] if key == "bop" else bc[-1]
            return f"={L(cidx)}{rows_cf[label]}"
        rc = add_line(cf, rc, label, "USD mn", NUM_MN, tl,
                      hist=hist_fin("Cash — beginning of period" if key == "bop" else "Cash — end of period"),
                      qp=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['cash'][key]}",
                      yb=yb_cash,
                      ys=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['cash'][key]}")
    cash_line("Cash — beginning of period", "bop")
    cash_line("Cash — end of period", "eop")

    # ---------------------------------------------------------- BS
    bs = sheet_shell(wb, "BS", "Integrated balance sheet", tl)
    rb_ = HDR + 2
    rb_ = section(bs, rb_, "BALANCE SHEET", tl)
    rows_bs = {}
    def bs_line(label, qp=None, ys=None):
        nonlocal rb_
        rows_bs[label] = rb_
        flat_q = lambda p, i: f"={L(prev_period(tl, i)['col'])}{rows_bs[label]}"
        rb_ = add_line(bs, rb_, label, "USD mn", NUM_MN, tl,
                       hist=hist_fin(label), qp=qp or flat_q, yb="eop", ys=ys or qp or flat_q)
    bs_line("Cash and equivalents",
            qp=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['cash']['eop']}",
            ys=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['cash']['eop']}")
    for lbl in ["Short-term investments", "Trade receivables", "Inventories", "Other current assets"]:
        bs_line(lbl)
    tca_f = lambda p, i: (f"=SUM({L(p['col'])}{rows_bs['Cash and equivalents']}:"
                          f"{L(p['col'])}{rows_bs['Other current assets']})")
    bs_line("(=) Total current assets", qp=tca_f, ys=tca_f)
    bs_line("PP&E", qp=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['ppe']['eop']}",
            ys=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['ppe']['eop']}")
    for lbl in ["Intangible assets and goodwill", "Right-of-use assets",
                "Deferred tax assets", "Other non-current assets"]:
        bs_line(lbl)
    tnca_f = lambda p, i: (f"=SUM({L(p['col'])}{rows_bs['PP&E']}:"
                           f"{L(p['col'])}{rows_bs['Other non-current assets']})")
    bs_line("(=) Total non-current assets", qp=tnca_f, ys=tnca_f)
    ta_f = lambda p, i: (f"={L(p['col'])}{rows_bs['(=) Total current assets']}"
                         f"+{L(p['col'])}{rows_bs['(=) Total non-current assets']}")
    bs_line("(=) Total assets", qp=ta_f, ys=ta_f)
    for lbl in ["Trade payables", "Loans and financing (current)", "Lease liabilities (current)",
                "Other current liabilities"]:
        bs_line(lbl)
    tcl_f = lambda p, i: (f"=SUM({L(p['col'])}{rows_bs['Trade payables']}:"
                          f"{L(p['col'])}{rows_bs['Other current liabilities']})")
    bs_line("(=) Total current liabilities", qp=tcl_f, ys=tcl_f)
    for lbl in ["Loans and financing (non-current)", "Lease liabilities (non-current)",
                "Provisions (incl. asset retirement obligation)", "Deferred tax liabilities",
                "Other non-current liabilities"]:
        bs_line(lbl)
    tl_f = lambda p, i: (f"={L(p['col'])}{rows_bs['(=) Total current liabilities']}"
                         f"+SUM({L(p['col'])}{rows_bs['Loans and financing (non-current)']}:"
                         f"{L(p['col'])}{rows_bs['Other non-current liabilities']})")
    bs_line("(=) Total liabilities", qp=tl_f, ys=tl_f)
    bs_line("Share capital and reserves")
    bs_line("Retained earnings (accumulated)",
            qp=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['re']['eop']}",
            ys=lambda p, i: f"=Schedules!{L(p['col'])}{rows_sc['re']['eop']}")
    eq_f = lambda p, i: (f"={L(p['col'])}{rows_bs['Share capital and reserves']}"
                         f"+{L(p['col'])}{rows_bs['Retained earnings (accumulated)']}")
    bs_line("(=) Equity attributable to shareholders", qp=eq_f, ys=eq_f)
    bs_line("Minority interest (equity)")
    teq_f = lambda p, i: (f"={L(p['col'])}{rows_bs['(=) Equity attributable to shareholders']}"
                          f"+{L(p['col'])}{rows_bs['Minority interest (equity)']}")
    bs_line("(=) Total equity", qp=teq_f, ys=teq_f)
    chk_f = lambda p, i: (f"={L(p['col'])}{rows_bs['(=) Total assets']}"
                          f"-{L(p['col'])}{rows_bs['(=) Total liabilities']}"
                          f"-{L(p['col'])}{rows_bs['(=) Total equity']}")
    rows_bs["check"] = rb_
    rb_ = add_line(bs, rb_, "Balance check (= 0)", "USD mn", NUM_2D, tl,
                   hist=lambda p: chk_f(p, 0), qp=chk_f, yb=chk_f, ys=chk_f)

    # ---------------------------------------------------------- Cover
    cov = wb.create_sheet("Cover", 0)
    cov.sheet_properties.tabColor = "1F3864"
    cov.column_dimensions["B"].width = 100
    notes = [
        (fin["B1"].value, TITLE),
        ("Model generated by engine/build_model.py (engine v0). History linked to the input tabs; "
         "projections driven by the Premises tab (auto-seeds to be replaced in the assumption session).", SUB),
        ("", None),
        (f"History: {hist_q[0]} to {hist_q[-1]}. Projection: quarterly through 4Q{str(q_seq(hist_q[-1])[0] + 1)[2:]}, "
         f"annual through {q_seq(hist_q[-1])[0] + 1 + PROJ_YEARS_ANNUAL}.", None),
        ("Known v0 limitations: no revolver (cash can go negative), constant working capital, "
         "constant debt, no scenarios. See docs/project_specification.md.", None),
        ("Blue = input/assumption | Black = formula | Green = link between tabs | Cream fill = projection.", None),
        ("This file may contain synthetic test data; check the title of the input tabs.", None),
    ]
    for k, (txt, f) in enumerate(notes, start=2):
        c = cov.cell(row=k, column=2, value=txt)
        if f:
            c.font = f
        c.alignment = Alignment(wrap_text=True, vertical="top")

    order = ["Cover", "IS", "BS", "CF", "Operational Model", "Schedules", "Premises",
             "Assumptions", "Input Financials", "Input Operational", "README"]
    wb._sheets = [wb[n] for n in order if n in wb.sheetnames] + \
                 [ws for ws in wb._sheets if ws.title not in order]
    wb.save(out_path)
    print(f"OK: {out_path} | hist {hist_q[0]}..{hist_q[-1]} | {len(assets)} assets | "
          f"{len(tl)} period columns")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

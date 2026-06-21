---
title: Sector authoring guide — how to make a NEW sector modelable, cold
slug: _sector_page_guide
audience: a Claude chat starting cold, asked to add a sector to this system
status: draft
extends:
  - _schema.md            # the card contract — DO NOT duplicate it, reference it
  - wiki/_schema.md        # the concept-article contract (where a wiki exists)
last_reviewed: 2026-06-20
---

# Sector authoring guide

This guide teaches a Claude chat, starting with no prior context, how to make a **brand-new sector** modelable by this system — any sector: a bank, a utility, a retailer, a miner, a hospital chain, an airline, a software company. The system is **sector-agnostic by construction**: a sector enters as *data and prose* (a method card + a machine schema + an operational recipe), and only occasionally as *code* (a dedicated build function).

> **Framing — read this first.** Oil & Gas and Telecom are the only two sectors that have a dedicated build engine today. They are used in this guide **only as labelled examples** of two contrasting archetypes (bottom-up volume×price vs. margin-down-from-EBITDA). **They are not targets, not defaults, and not the shape your sector must take.** When you see an `EXAMPLE (O&G)` or `EXAMPLE (telecom)` block, read it as "here is one concrete instantiation of the pattern", then design *your* sector from its own economics.

This guide is a **supplement** to [`_schema.md`](_schema.md) (the card contract) and the wiki concept contract. It does **not** restate the 7-section card structure — `_schema.md` owns that. It adds only the buildable + machine artifacts the card schema does not cover, and tells you how everything plugs into the engine.

> **Line numbers drift.** Every `build_model.py:NNN` (and similar) reference below was verified on 2026-06-20, but any edit to the source silently invalidates the offset. **Trust the symbol, not the number** — each citation also names a function/branch/label you can relocate with a grep (e.g. `grep -n "def corkscrew" engine/build_model.py`, `grep -n "if og:" engine/build_model.py`). If a cited line shows something different, re-grep the named symbol before believing the guide.

---

## 0. The one thing you must internalise: prose does not build the model — and Path B is **not** "free for any sector"

There are **two independent things** you can ship for a sector, and they do completely different jobs:

1. **The method card** (`sectors/<slug>.md`) — prose. It grounds the *assumption conversation*. The engine reads it through exactly one function, `sector_knowledge.card_excerpt()`, which keyword-scores the card's markdown sections against the line item being discussed and injects a slice into the proposal prompt. **`build_model.py` never imports `sector_knowledge`.** A perfect card produces a richer conversation and the *same* model.

2. **The build path** — code. The actual rows, formulas, and statement wiring are produced by a Python build function. Today there are exactly two build paths, dispatched by one line in `engine/build_model.py` (`grep -n "og = " build_model.py`, currently `:533`):

   ```python
   og = (an.sector == 'oil_and_gas') and bool(an.assets)
   ```

   - **Path A — bottom-up** (volume × price, per asset): fires *only* for the literal slug `oil_and_gas` with assets (`if og:` branch, `build_model.py:556-586,675-745`).
   - **Path B — generic top-down** (revenue-growth × margin): the `else:` branch — everything else (`build_model.py:587-615,747-792`).
   - Telecom is a **third, separate script** (`build_model_telecom.py`) — not dispatched from `main()` at all; it is a standalone fork of the whole pipeline.

The machine schema (`<slug>.delta.yaml`) sits *between* these: it declares **which input labels must exist** and lets the validator prove "the engine will not KeyError". It does **not** emit statements.

**The dangerous half-truth this guide used to tell you:** that Path B is "zero code, available today" for any new sector that just carries the universal base labels, and that a missing label fails *silently to a 0-seed*. **That is wrong for the financial statements.** The shared statement builder (the IS/BS/CF/Schedules code, `build_model.py:855-1162`) runs for *every* sector and reads its history through `hist_fin(lbl)` = a bare `frow[lbl]` dict subscript (`build_model.py:878`) — **not** the safe `gf()` reader. It hard-reads, by exact string, a set of labels that are **NOT** in `UNIVERSAL_BASE_FINANCIAL` — they are exactly the O&G financial delta. **A genuinely new sector built on "universal base + extras only" will hard-CRASH with `KeyError`, not "balance at 0 for free."**

So the real failure model has **two** distinct cases (§7 makes this precise):

| Read mechanism | Where | Missing-label behaviour |
|---|---|---|
| `gf(label, default)` | premise *seeds* (DSO, tax, gross-margin, G&A, …) | **silent**: returns the default → an economically empty model that still balances at 0 |
| `frow[label]` / `hist_fin(label)` | every IS/BS/CF/schedule *statement* line | **loud**: `KeyError`, the build crashes |

**Consequences for you:**
- Decide *up front* which build path your sector takes (§5), and be honest about the resulting **coverage tier** (§9).
- A Tier-B sector's delta is **effectively NOT optional** — Path B hard-reads the non-base financial labels in §7.2, so you must declare them (or the build crashes). Do not believe any claim in older notes that "the delta is optional for Tier B."
- Do not imply the card drives the build. Do not tell the next Claude "just write a delta and you're done."

---

## 1. What knowledge you need before writing anything (the operational layer)

Model the sector's *economics*, not its accounting forms. Before drafting, you must be able to answer all of the following from **public sources** (filings, regulator data, sector reports, company releases/transcripts — never the proprietary `Example models/` or `Knowledge Base/` archives, and never pasted source prose):

1. **The revenue identity.** How does "revenue = price × volume" actually decompose here? Write it as an explicit equation. Examples of the *shape* (not your answer):
   - A retailer: `revenue = stores × sales/m² × m²/store`, or `same-store-sales growth × store count + new-store contribution`.
   - A bank: `net interest income = average earning assets × NIM` + `fee income`; this sector likely needs its own builder (see §5).
   - A utility: `revenue = regulated asset base × allowed return + volume × tariff`.
   - A miner: `revenue = volume sold × realized price per tonne`, by commodity.
   - A hospital/health insurer: `revenue = members × premium`; cost driven by `sinistralidade` (loss ratio).
2. **The driver tree under each term** — what disaggregates volume and price, and to what granularity the *typical company in this sector discloses* (per asset? per business unit? per product family? per segment? consolidated only?). The system's differentiator is that the operational structure **auto-adapts to the granularity the company actually discloses** — so capture the *full* tree and note which levels are usually visible.
3. **Mandatory KPIs & regulatory disclosures** — the metrics the market and the Brazilian regulator for this sector expect (ANP, ANS, ANEEL, Anatel, CVM, BACEN, SUSEP, …). Define each and how it is computed. Keep BR-specific terms (CFEM, JCP, sinistralidade) in Portuguese with a gloss, per `_schema.md`.
4. **Units** for every driver (kt, m³, lines, members, MWh, R$/unit, %, days) — you will need the unit and number format for every premise (§3). **Per CLAUDE.md, line labels are English and figures use each company's reporting currency.** The generic Path B currently labels every premise unit `USD mn` / `USD/...` regardless of reporting currency (`build_model.py:599-615`) — a known generic-path artifact, not a licence to bake USD into a non-USD reporter.
5. **The public sources you actually read** — each load-bearing claim must carry a `> source:` callout pointing to an ID in [`_sources.md`](_sources.md), with a confidence tag. If you cannot source a driver, tag it `⚠️ to-verify` — **never fabricate a citation** (§8).

This is §1–§3 of the card. Distil, do not copy. Encode **method, not numbers**: "spread per route × utilization", never a 2026 spot price baked in as a value.

---

## 2. How to organise the OPERATIONAL part of the Excel

The operational section lives on a tab the engine calls **"Operational Model"**. Its layout is **label-driven**, so the typographic conventions below are load-bearing, not cosmetic.

### 2.1 Section headers vs. driver lines — casing IS the API

`introspect_operational()` (`template_loader.py:124-129`) classifies a row purely by its text:

- **ALL-CAPS string, length > 3 ⇒ a SECTION HEADER.**
- **Anything else ⇒ a driver line** (it gets surfaced/projected).

So:

- Write section headers in **ALL CAPS** (`PRODUCTION BY ASSET`, `VOLUMES`, `PRICING`, `SUBSCRIBERS`).
- Write driver labels in **mixed case** (`Realized price`, `Total lines`, `Same-store sales growth`).
- **Gotcha:** a driver accidentally typed in caps becomes an invisible "section"; a section typed in Title Case becomes a projected driver line. This is the single most common authoring error.

### 2.2 What is an input vs. a computed line

- **History columns (QH)** of every operational line: a **green link** pulling the actual from the `Input Operational` (or `Input Financials`) tab. History is *never typed* into the model — always linked by formula (project rule).
- **Projection columns (QP / YS):** a **black formula** computing the value from premises and other rows.
- **Premise cells** (the only **blue**, editable cells) live exclusively on the **Premises** tab — never inline on an operational row.

### 2.3 The granularity-adaptation contract

The engine adapts to disclosed granularity in two different ways depending on build path:

- **Generic path (Path B):** every non-section operational row is surfaced as a **flat-projected memo line** (history link + carry-forward), and that is *all* — **disclosed drivers are NOT wired to revenue** (`build_model.py:747-765`, comment "not yet wired to revenue — Stage 3"). In Path B the disclosed driver tree is **decorative**: revenue is still `rev_growth × margin` off the financials. Organise the tab so a human can read the drivers, but do not expect them to move the model.
- **Bottom-up path (Path A):** per-group introspection via `scan_assets()` reads named slots. **This machinery is hard-coded to O&G's three section headers** (`PRODUCTION BY ASSET`, `LIFTING COST BY ASSET`, `CAPEX BY ASSET`) and `Asset 1 name`, reading names from column C, max 8 slots (`template_loader.py:39-43,132-154`). **A non-O&G bottom-up sector cannot reuse it** — it needs new introspection code in a new builder (§5).

### 2.4 Ordering

Group top-down: **drivers of volume → drivers of price → the revenue build line → the cost build lines → capex/D&A drivers.** Put each group under an ALL-CAPS header. The revenue build line is the hinge between this tab and the income statement (§4), so make it explicit and singular.

---

## 3. The formula each operational line should have (per-line spec)

The engine sets **font colour by the *provenance* of the number, automatically** — colour is the source-of-truth signal, enforced by the engine, not chosen by you:

| Colour | Meaning | Where |
|---|---|---|
| **Blue** | hardcoded input / approved assumption — the only editable cells | Premises tab only |
| **Black** | a formula computing from other cells (same tab or Premises) | projected quarters (QP), pure-annual (YS), year-close aggregations (YB) |
| **Green** | a link pulling a historical actual from the Input tab (or a cross-tab link) | history quarters (QH) |
| Red | external link | (not used in operational build) |

(`build_model.py:29-42` defines `BLUE/BLACK/GREEN` and the `NUM_MN/NUM_1D/NUM_2D/PCT` formats.)

### 3.0 The period / timeline ABI (you cannot write a correct formula without this)

Every example formula below — and every Tier-A builder — is written against one data structure: the **timeline** `tl`, a list of period dicts built by `build_timeline()` (`build_model.py:83-106`). Internalise it or the lambdas are not reproducible:

- **`tl` is a list of dicts**, one per model column, each: `{"label", "kind", "year", "q", "col"}`.
  - `label` — the column header text (`"1Q22"`, `"2022"`).
  - `kind` — one of **four** values:
    - **`QH`** historical quarter (history; green link to Input).
    - **`QP`** projected quarter.
    - **`YB`** the annual column that *closes* a 4-quarter block (aggregates its own quarters).
    - **`YS`** a pure-annual year (years 3–10; no quarters under it — projected like QP).
  - `q` — quarter number `1..4`, or `None` for YB/YS columns (so `p["q"]` is a truthiness test for "is this a quarter").
  - `col` — the openpyxl 1-based column index of this period (`FIRST_COL + i`).
- **Helpers** (use verbatim; all in `build_model.py`):
  - `prev_period(tl, i)` (`:113-124`) — the previous period *in the real sequence*: quarters chain skipping YB columns; YS/YB chain to the prior YB/YS. Returns `None` at the start.
  - `block_cols(tl, yb)` (`:109-110`) — the four quarter `col`s belonging to a YB year (used for sum/avg/eop aggregation).
  - `yoy_col(tl, i)` (`:127-132`) — the `col` of the same quarter one year earlier, or `None`.

### 3.1 The four period kinds — never one blanket formula, and the `add_line` signature

Every line is created by **`add_line(ws, row, label, unit, fmt, tl, hist=None, qp=None, yb="sum", ys=None)`** (`build_model.py:212-216`, which wraps `Line.fill`, `:180-209`). Each callback has a fixed contract:

- **`hist(p)`** — receives **only the period dict** `p`; returns the QH formula (a **green link** to the Input tab). `None` ⇒ projection-only line.
- **`qp(p, i)`** — receives `(period dict, index)`; the QP **black formula** from premises and other rows.
- **`yb`** — the YB aggregator: the string `"sum"` (flows), `"avg"` (rates/prices/per-unit), `"eop"` (stocks/balances), **or** a callable `yb(p, i)`. YB columns are **not re-projected** — they aggregate their own four quarters.
- **`ys(p, i)`** — receives `(period dict, index)`; the YS formula, normally identical to `qp`.

> **Gotcha:** summing a price, or averaging a flow, in YB corrupts the annual figure even though the balance check still passes. Match the aggregator to the line type.

### 3.2 The hard formula rules (mandatory — see CLAUDE.md "Spreadsheet conventions")

1. **Sign convention 1, baked into the formula and announced by the label prefix.** Revenues/inflows positive, costs/outflows negative. A cost line must *compute* a negative (`=-{vol}*{rate}`), so subtotals are plain additions (`EBIT = SUM(gross profit, G&A, …)`, each term already signed). The label prefix must agree with the sign the formula produces: `(=)` subtotal/result, `(-)` cost/deduction, `(+)` addition, `(+/-)` signed-either-way.
2. **No constant embedded in a formula.** Any number that is a *judgement* (growth, margin, price, premium/discount, per-unit cost, days, payout, tax rate, a unit conversion that is really an assumption) **must be a Premises row** referenced by formula. The *only* literals tolerated are non-judgement structural/unit constants — e.g. the `/1000` that converts (units × price) to millions, or the `0` floor inside `MAX/MIN`. **If unsure whether a number is structural or a judgement, treat it as a judgement and give it a premise cell.**
3. **No nested IF.** Use `MIN`/`MAX`/flag cells. Caps and floors: `=MAX(0, x)`, `=MIN(cap, x)`. Taxes only on positive EBT: `=-MAX(EBT,0)*Praw(tax)`. Division safety: `IFERROR(expr, 0)` for value lines feeding subtotals (an `IFERROR(...,"-")` string can poison a downstream `SUM`; reserve `"-"` for display-only ratios). Any sector threshold (price floor, capacity cap, take-or-pay) → `MIN`/`MAX` against a premise cell holding the threshold, or a `0/1` flag premise multiplied in.
4. **No named ranges, no macros, no hidden rows.** All references are explicit A1-style cross-tab refs (`IS!D12`, `'Operational Model'!E7`).
5. **No circularity (MVP).** Anything accruing on a balance references the **beginning-of-period (BOP)** cell of that balance's corkscrew, never the EOP/same-period cell: `debt interest = -Praw(debt_rate) * <debt BOP cell>`. Roll-forwards use the corkscrew pattern **BOP / (+) additions / (−) reductions / (=) EOP**, with BOP(t) = EOP(t−1) (`corkscrew()`, `build_model.py:798-818`). Revolver interest is deliberately omitted to avoid the cash→interest→cash loop; do not reintroduce it.

### 3.3 Premise referencing mechanics (use verbatim)

- `P(key, period)` → a self-contained cell formula `='Premises'!<col><row>` (the whole cell *is* the premise).
- `Praw(key, period)` → the bare reference `Premises!<col><row>` for embedding inside a larger formula, e.g. `=-{vol}*Praw(lift)/1000`. (`prem()` returns the `P`/`Praw` pair, `build_model.py:259-264`.)

A premise row is created by a **seed tuple** in the `seeds` list (`seed_premises()`, `build_model.py:220-256`):

```
(key, label, unit, number_format, seed_value_expr, annual_multiplier)
```

- **`number_format`**: `PCT` | `NUM_1D` | `NUM_2D` | `NUM_MN`.
- **`seed_value_expr`**: how the seed is **back-solved from the last historical actual** (e.g. `royalties% = government take ÷ revenue`; `DSO = AR ÷ revenue × 91.25`; `depletion rate = D&A ÷ volume × 1000`). Method, not a typed number.
- **`annual_multiplier`**: `1` for a rate/price/margin (same per period when annualised) — `4` for a per-quarter **flow** that must be ×4 to annualise (capex, exploration, lease amounts, `days` 91.25→365). **Omitting this makes annual projections 4× wrong.**

> **Path-B seeds are back-solved from O&G-delta financial lines (and silently default if absent).** The generic seed block (`build_model.py:587-615`) computes `gross_margin` from `(=) Gross profit` (via `gf`, defaults to `0.30`), `ga` from `(-) General & administrative expenses` (defaults `0.04`), `tax` from `(=) EBT` + `(-) Income taxes` (defaults `0.25`), `depr` from `memo: (+) Depreciation, depletion & amortization`. These reads are the **safe `gf()`** kind — a missing label silently falls to the default and you get an economically empty model that still balances. So even where Path B does *not* crash, those lines must be on the input tab to get meaningful seeds, even though they are not in the universal base.

### 3.4 The per-line spec template (fill one of these per operational line)

Specify each operational line as a small table mirroring an `add_line()` call:

| Field | What to write |
|---|---|
| **Label** | text with the correct `(=)`/`(-)`/`(+)`/`(+/-)` prefix |
| **Unit / format** | e.g. `R$/m³` / `NUM_2D` |
| **History (QH)** | green link to which `Input Operational`/`Input Financials` row (the `hist=` callback), or `none` if projection-only |
| **Projection (QP)** | the `qp=` black formula in terms of other Operational-Model rows and `Praw('<key>')`, producing the sign the label promises |
| **Year-block (YB)** | `sum` \| `avg` \| `eop` |
| **Pure-annual (YS)** | normally identical to QP |
| **Premises consumed** | each premise key with unit / format / seed expr / annual multiplier |
| **Downstream** | which financial/statement line this feeds (§4) |

> **EXAMPLE — O&G lifting-cost line (imitate the *shape*, not the sector).** Label `(-) Lifting cost` / `NUM_MN`; QH `none` (projection-only cost); QP/YS `=-{sales_volume_cell}*Praw(lift)/1000` (negative; `/1000` is the unit constant, allowed); YB `sum`; premise `lift` = "Lifting cost (weighted avg)", `USD/boe`, `NUM_1D`, seed = production-weighted lifting cost of last actual, mult `1`; downstream → IS `(-) Cost of goods sold`. (`build_model.py:567,726-727`.)

> **EXAMPLE — generic top-down (what any new sector gets through Path B).** Revenue: `(=) Revenue`, QH green link to `Input Financials` `(=) Net revenue`, QP/YS `=<prev rev col><row>*(1+Praw(rev_growth))`, YB `sum`. Cost: `(-) Cost of goods sold (ex-D&A)` = `=-<rev cell>*(1-Praw(gross_margin))`. Capex (Damodaran sales-to-capital): `=Praw(depr)+(<rev_t>-<rev_t-1>)/Praw(sales_to_capital)`. (`build_model.py:768-791`.) **Note this is the operational layer only — the financial statements still hard-read the labels in §7.2, so "Path B" is never "no financial schema".**

> **Generic-path artifact to flag:** the generic seed block still plants an O&G-shaped `expl` / `(-) Exploration expenses` premise and the IS unconditionally builds an `(-) Exploration expenses` row (`build_model.py:610,906`). In a non-O&G model this surfaces as a dormant Exploration line at 0. Note it as a known artifact to clean up when a builder is added; do not let it confuse the sector's statements.

---

## 4. What changes in the 3 STATEMENTS for the sector

The statements are wired by **row handles**, not labels. The operational section returns handles (`row_rev`, `row_cogs`, `row_depl`, `row_capext`, and the O&G triple `row_liftc`/`row_royc`) and the IS/BS/CF/Schedules/Valuation consume them by sheet-qualified cell refs. **This row-handle interface is the implicit ABI** between the operational section and the rest of the engine. (`build_model.py:768-792`; IS COGS branch `if og:` `:892-899`; PP&E corkscrew additions=capex / reductions=depletion in `corkscrew`, `:798-818`.)

> **The ABI is a contract WITHIN one `main()`, not across engines.** O&G (Path A) and the generic (Path B) branches share the *same* downstream IS/BS/CF/Valuation, so they must both expose the same handles. The unused handles are set to `None` per path: O&G sets `row_cogs = None` (`:745`); the generic branch sets `row_liftc = row_royc = None` (`:792`). The IS COGS formula then **branches on `og`** (`:892-897`) to pick which handles to read. The **only** Tier-A precedent, telecom, does NOT plug into this — `build_model_telecom.py` forks the *entire* pipeline into a standalone script and reuses none of the shared `is_line`/`corkscrew`/`add_valuation_tab` machinery. So decide which model your builder follows (§5/§10.3): **plug into `build_model.main()`** (then you owe the exact ABI *and* a new `og`-style dispatch branch + a COGS branch) **or fork like telecom** (then you reimplement downstream and the ABI is only advisory).

What is genuinely sector-specific:

1. **Revenue identity into the IS.** Path B: `(=) Net revenue` grows by `rev_growth`. A bottom-up/multi-stream sector instead sums its driver-built segment lines into net revenue — and that requires a builder (§5).
2. **The cost / EBIT direction.** Two archetypes:
   - **Expense-up-to-EBIT** (O&G style): COGS reconstructed from operational cost rows; `GP − G&A − … = EBIT`; `EBITDA = EBIT + DD&A` as a derived memo.
   - **Margin-down-from-EBITDA** (telecom style): keys off a disclosed-EBITDA margin premise (`opex ex-D&A = -rev × (1 − margin)`), `EBITDA = rev + opex`, `EBIT = EBITDA − D&A`.
   State which one your sector uses — it dictates which IS rows exist and the formula *direction*.
3. **D&A and capex drivers.** Specify the D&A driver (unit-of-production rate? % of PP&E? flat per-period?) and the capex driver (per-asset? sales-to-capital? flat?), and which schedule rows they feed.
4. **Sector-specific lines that appear or stay dormant.** Enumerate which extra lines your statements carry (e.g. a regulated-asset-base roll-forward, a loss-provision schedule, a spectrum/intangible amortisation block) and which base lines you leave at zero. **Beware:** the shared IS already builds an `(+/-) Other operating income (expenses)` row whose generic formula subtracts the lease-depreciation premise (`build_model.py:908-911`), and an ARO accretion term inside the financial result (`:917-919`) — for *every* sector, O&G or not. They are harmless at a 0 seed but present and not removable without code (§6).
5. **Working capital & financial result.** State whether WC is **days-driven** (full DSO/inv-days/DPO schedule feeding BS+CF) or **frozen** (change = 0); whether debt is **dynamic with a revolver/cash-sweep plug** or **held flat**; and how financial result is assembled (`debt int + lease int − ARO accretion + other`, `:917-919`, or a single flat net premise). These choices change the BS plug behaviour and the CF reconciliation.
6. **The balance check must stay 0 in every column** (`Balance check (= 0)` line, `build_model.py:1157-1162`), verified by the recalculation harness. Any new line that writes a BS/CF row must show how it reconciles. A line only the IS or the Valuation tab reads does not threaten the check.

### 4.1 Compliance invariants the harness ENFORCES on a Valuation tab (Tier-A: read this)

If your builder emits a Valuation tab, the harness (`engine/harness/invariants.py`) enforces two **FAIL-severity** compliance invariants — they fail the build, not just warn:

- **`inv_valuation_disclaimer`** (`invariants.py:361-383`): any sheet that prints a cell starting with the exact label **`(=) Implied value per share`** MUST also carry a cell containing **"not a price target"** or **"not a recommendation"**. The engine emits both today (`build_model.py:441-442,476`). **Two traps:** (a) emit the disclaimer string **verbatim** adjacent to per-share output, or the build FAILs; (b) the check triggers *only* on the exact `(=) Implied value per share` label — a divergently-spelled per-share line **silently EVADES** the check, which is a compliance hole, not a feature. Use the canonical label.
- **`inv_assumptions_provenance`** (`invariants.py:386-407`): every row on the Assumptions tab with status `Aprovada` must carry a method (col 8) and source (col 9) — the build-time mirror of `assumptions.approve()` (§8).

### 4.2 IFRS / accounting rules to encode (card §4)

Cite the standard for each. Common sector overlays: revenue recognition timing (IFRS 15 — contra-revenue, variable consideration), capitalisation vs. expensing (IAS 38 software/R&D; IFRS 6 exploration; IAS 16 PP&E), depletion/UoP, fair value (IAS 41 biological assets; financial instruments), leases (**IFRS 16** — RoU + lease-liability twin roll-forwards; report both **EBITDA and EBITDA-AL**; in the EV→equity bridge leases count as debt; FCFF deducts lease payments), provisions/decommissioning (IAS 37 — ARO), and BR taxation (JCP, effective rate). Note IFRS-vs-US-GAAP divergence where it matters. **Every accounting claim carries a `> source:` + confidence tag.**

---

## 5. Which build path — and the decision rule

This is the most important design decision. Decide it explicitly in card §5 and state *why*.

**Use the generic top-down path (Path B) when** the sector's economics are honestly "revenue grows at a rate, costs are a margin." Provide a card + the canonical input labels **including the §7.2 financial extras** and you get a balancing three-statement + Valuation model with no new code; the disclosed drivers appear as memo lines. This is the **happy path** — aim a new sector here first. **It is "no new build function", NOT "no financial schema":** the §7.2 labels are still mandatory or the build crashes (§0/§7).

**You need a dedicated builder (a new `build_model_<slug>.py`, the telecom precedent) when** the revenue identity is **multi-stream, roll-forward-based, or margin-down-from-EBITDA** — anything Path B's single-line `rev_growth × margin` gets economically wrong. Signals you need a builder:

- revenue must **sum several driver-built segment lines** (subscribers × ARPU per segment; volume × price per commodity; members × premium);
- a **stock corkscrew drives revenue** (subscriber base, regulated asset base, loan book);
- the cost build is **margin-down-from-disclosed-EBITDA**;
- the sector needs a **schedule that does not exist** in `base.yaml` (see §6) — e.g. a loss-provision roll-forward, a spectrum-amortisation block separate from PP&E.

**Per-asset bottom-up (Path A)** is *O&G-specific code*. Do not assume a new bottom-up sector can reuse it — `scan_assets`, the per-asset capex-total offset (`capex_header + max_slots + 1`, `build_model.py:740`), and the consolidated Brent/Realized/Sales-volume labels are all O&G-shaped. A different per-asset sector needs its own introspection + builder.

> **EXAMPLE — telecom (separate-engine precedent).** Card demands subscriber-corkscrew × ARPU by segment + service-vs-handset split + EBITDA-AL. This cannot run through Path B, so it lives in `build_model_telecom.py` with its own seeds and its own financial labels (`(=) EBITDA (as disclosed)`, `(-) Operating expenses (ex-D&A)`, segment memo revenues, its own cash-bridge lines). It is invoked as a standalone script — **adding a delta does not auto-route a sector to a custom engine; that wiring is a separate manual step (§11).**

---

## 6. Which schedules apply (and the base.yaml reality)

`templates/base.yaml` is the **only** template (no per-sector YAML exists; `oil_and_gas.yaml` was deleted). It ships five schedules:

| Schedule | base.yaml flag | Premises (ids) |
|---|---|---|
| `working_capital` | **enabled** | `dso, invdays, ocadays, dpo, ocldays` |
| `debt` | **enabled** | `debt_draw, debt_repay, debt_rate, debt_curr_pct, other_finres, min_cash` |
| `leases` | **enabled** | `lease_add, lease_depr_amt, lease_princ_amt, lease_rate, lease_curr_pct` |
| `aro` | **disabled** [†] | `aro_accr, aro_settle` |
| `hedge` | **disabled** | (none defined) |

> [†] **"disabled" in base.yaml ≠ absent from the build.** The ARO and lease premises are seeded **unconditionally for every sector** (`build_model.py:655-667`), the ARO roll-forward is built unconditionally (`corkscrew` for ASSET RETIREMENT OBLIGATION, `:859-864`), the IS subtracts `aro_accr` in the financial result and `lease_depr_amt` in "Other operating income (expenses)" for every sector (`:908-919`), and the BS reads `Provisions (incl. asset retirement obligation)` by subscript (`:860,1137` → KeyError if absent). So a Tier-B non-O&G sector **inherits** an ARO accretion term, a lease-depreciation "other operating" term, and a hard-required `Provisions (incl. asset retirement obligation)` input line — harmless at a 0 seed but present, and not removable without code. The `aro: disabled` flag controls neither the seeding nor the wiring today.

> **The base.yaml comments are stale.** The "sector YAML opts in" / "extends: base" comments describe a per-sector-YAML design that no longer exists. In code the `enabled` flags are read **globally** (`template_loader.py:166-167`). **A sector cannot turn a schedule on/off via data**, and cannot add a sector-specific schedule without editing `build_model.py`. So:
> - In card §5 you may **describe** the schedules your sector needs (including ones that don't exist yet — e.g. a regulated-asset-base or loss-provision roll-forward).
> - But state plainly that adding such a schedule is a **code change**, not a data change, and list which of the 5 base schedules apply vs. which the sector needs that **don't exist yet**.

When you do seed a base schedule, map your sector premises onto its ids and give each a seed back-solved from history (DSO from AR, DPO from payables, cost-of-debt from interest÷debt, etc.).

---

## 7. The input labels the build reads by exact string — and the TWO failure modes

The build reads lines by **exact string match**. **There are two different readers, with opposite failure behaviour** (§0). Get this right — it is the most load-bearing cold-start fact in the guide.

### 7.1 Reader A — `gf(label, default)`: missing ⇒ **silent default** (an empty-but-balancing model)

`gf()` (`build_model.py:551-554`) returns `default` (usually 0 or an economic fallback) when the label is absent. This covers the **premise seeds**: `gross_margin`, `ga`, `tax`, `depr`, the WC days, the debt/lease seeds (`:587-660`). A renamed/missing seed label does **not** crash — the model just seeds to a default and balances at 0. **There is no validator that the operational build is non-trivial**, so for these lines *silence* is the failure mode: carry them or get an economically empty model.

### 7.2 Reader B — `frow[label]` / `hist_fin(label)`: missing ⇒ **hard `KeyError`**

`hist_fin(lbl)` (`build_model.py:878`) is `frow[lbl]` — a bare dict subscript that **raises `KeyError`** if the label is absent. The shared statement builder (IS/BS/CF/schedules, `:855-1162`) hard-reads, by exact string, this set of **non-base** financial labels for **every** sector, O&G or not:

| Hard-read label (NOT in the universal base) | Read at (symbol / line) |
|---|---|
| `(-) Cost of goods sold` | IS history `hist_fin`, `:898`; WC `cogs_base`, `:623` |
| `(=) Gross profit` | IS history, `:901`; seed `gp_l`, `:594` |
| `(-) General & administrative expenses` | IS history, `:905`; seed `ga`, `:609` |
| `(-) Exploration expenses` | IS history, `:906` |
| `(+/-) Other operating income (expenses)` | IS history, `:910` |
| `(+/-) Financial result` | IS history, `:920`; debt seed `finres_q`, `:637` |
| `memo: (+) Depreciation, depletion & amortization` | IS DD&A history, `:932`; seeds `:595,604`; OM D&A `:780` |
| `Provisions (incl. asset retirement obligation)` | ARO seed `:860`; BS line `:1137` |
| `Minority interest (equity)` | BS line `:1153` |
| `Cash — beginning of period` | CF `cash_line`, `:1080` |
| `Cash — end of period` | CF `cash_line`, `:1080` |
| `(-) Capex` | **optional** — read only `if "(-) Capex" in frow` (`:789-790`) |

**The first nine are EXACTLY the `oil_and_gas.delta.yaml` financial list.** The two `Cash — …` lines are read by the shared CF code but currently live only in `telecom.delta.yaml`. **Every Tier-B sector MUST carry all of these on its input tab (and declare them in its delta), except `(-) Capex` which is optional.** Absent ⇒ `KeyError`, not a silent 0. This is why a Tier-B delta is **not optional**.

### 7.3 The universal base (already shared — never re-list it in a delta)

`UNIVERSAL_BASE_FINANCIAL` (`canonical_schema.py:40-70`) is shared by every sector and lives **only** in `canonical_schema.py`:

- IS base (5): `(=) Net revenue`, `(=) EBIT`, `(=) EBT`, `(-) Income taxes`, `(=) Net income`.
- BS base (20): `Cash and equivalents`, `Short-term investments`, `Trade receivables`, `Inventories`, `Other current assets`, `PP&E`, `Intangible assets and goodwill`, `Right-of-use assets`, `Deferred tax assets`, `Other non-current assets`, `Trade payables`, `Other current liabilities`, `Loans and financing (current)`, `Loans and financing (non-current)`, `Lease liabilities (current)`, `Lease liabilities (non-current)`, `Deferred tax liabilities`, `Other non-current liabilities`, `Share capital and reserves`, `Retained earnings (accumulated)`.

> **Do NOT re-list any base line in your delta** — `test_required_labels_is_base_plus_delta` asserts `fin − base == set(delta-financial)` exactly, so a duplicated base line **fails the test**.

### 7.4 What the Valuation / EV→equity bridge reads (built rows vs. input labels — don't confuse them)

The Valuation tab reads the BS **rows the engine itself BUILDS** from `rows_bs` (`add_valuation_tab`, `build_model.py:387-432`): `(=) Total equity`, `Cash and equivalents`, `Short-term investments`, `PP&E`, the loans/lease lines, etc. Those are **always present because the engine builds them** — they are NOT extra *input* requirements, and `(=) Total equity` is an **engine-COMPUTED** line (`:1156`), not an input label at all. The only genuine extra-*input* requirement the bridge ultimately needs is `Minority interest (equity)` — which the build reads from the input at `:1153` and the Valuation reads as a built row at `:431`. `Minority interest (equity)` is **not** in the base; it is a delta line (currently only O&G's). A sector with minorities must declare it in its **own** delta to keep the EV→equity bridge intact.

### 7.5 Structural input

`STRUCTURAL = ['memo: Shares outstanding (EOP)']` (`canonical_schema.py:75`) is the per-share-value input. It is **defined but not yet hard-required**; the build reads it best-effort via `gf(..., 0.0)` (`:1166`) and the Valuation falls back to a seed. Declare it for the sector (capital-structure / valuation input), and note it is currently optional. In the role classifier a `STRUCTURAL` item maps to the `CAPITAL_STRUCTURE` role (§ appendix).

---

## 8. Provenance & public-source discipline (anti-hallucination — non-negotiable)

This is an engine invariant, not a courtesy. `assumptions.approve()` raises `AssumptionProvenanceError` without all three of `method`, `source`, `source_date`; `proposals.py` requires `source` in its input schema; and the harness re-checks it at build time via `inv_assumptions_provenance` (§4.1). **A card claim with no `> source:` can never become an approvable premise.**

- **Three-tier confidence (reuse exactly, per `_schema.md`):** ✅ **Verified** (adversarial deep-research, vote ≥ 2-0 vs. primary/strong-secondary source) · 🟡 **Seed** (single-source or reputable-but-unverified; confirm before hardcoding) · ⚠️ **To-verify** (practitioner/textbook knowledge, not yet sourced — **never present as verified, never attach a fabricated citation**; these *are* the round-N research agenda). Roll them up in the `coverage:` front-matter (`verified | partial | seed-only`) and tag inline where claims diverge.
- **Method, not numbers** — doubly enforced (the card schema forbids hardcoded figures *and* the engine treats premises as cells). Point-in-time figures appear only as **dated illustrations with provenance**, never as values to hardcode.
- **Distillation, not copying.** Paraphrase. Never quote the proprietary archives. Public sources only.
- **No investment advice / no target price (MVP compliance)** — and this is build-enforced, not just prose: see `inv_valuation_disclaimer` (§4.1).
- ⚠️ drivers are allowed in the card as the research agenda, but **cannot be silently promoted** into the model as approved.

> **EXAMPLE — the honesty model (tech/SaaS card).** It flags that only the IAS 38 R&D/software-capitalisation rule is ✅ verified and labels the entire ARR/MRR/NRR/CAC/LTV driver tree ⚠️ "no citation." That is the correct way to author a card that is mostly a research gap — **without fabricating sources.**

---

## 9. Coverage tier — and how to be honest about it

The deterministic gate (`sector_coverage.py`) classifies every sector:

- **Tier A (full):** card **+** delta **+** a dedicated builder. `BUILDERS = {oil_and_gas, telecom}` — and that set is **code**, not data.
- **Tier B (partial):** card exists, but no dedicated builder → the generic top-down Path B model (with the §7.2 financial labels carried).
- **Tier C (none):** no card → **blocked** at Fase 1 intake, with the list of what *is* modelable.

**You cannot make a sector Tier A by authoring prose + YAML alone.** Tier A requires a builder. Authoring a card + delta lands you at **Tier B**, and that is a perfectly good, honest outcome for a sector with simple top-down economics. State plainly in card §7 where the sector lands and exactly what is missing to reach A (the builder, and which schedules/labels it would need). **Overclaiming coverage is a compliance failure** that mirrors the ⚠️/🟡 discipline.

> **EXAMPLE — fuel-distribution (honest Tier B).** Verified-core card (gross profit off volume(m³) × R$/m³ by product, recurring-vs-reported margin, inventory-effect line, price-aware WC) but **no builder yet**. Correct declaration: "the card grounds premises; the delta carries the §7.2 financial labels so Path B builds; reaching Tier A needs a builder for the inventory-effect / R$-per-m³ build." Do not pretend the card alone models it.

---

## 10. The exact artifacts a sector must ship

### 10.1 The method card — `sectors/<slug>.md`

Follow [`_schema.md`](_schema.md) **exactly**: YAML front-matter (`sector`, `slug`, `pilots_examples`, `coverage`, `key_standards`, `status: draft`) + the **7 mandatory sections in order** (Core thesis / Operational drivers with explicit revenue identity / KPIs & regulatory disclosures / Peculiar accounting / Model structure adaptation / Pitfalls incl. REFUTED claims / Confidence & open questions). **Do not restate `_schema.md` here and do not re-derive those 7 sections — reference the schema and keep them exactly as it defines.**

Card discipline that matters for the engine:

- `card_excerpt()` (`sector_knowledge.py:61-86`) splits on markdown `#{1,6}` headings and **keyword-scores** each section against the premise line item, returning the intro head (~900 chars) + top sections within a **2600-char budget**. Therefore:
  - every buildable/driver section must be a **real markdown heading** to be retrievable;
  - make headings **rich in the driver vocabulary** that will appear as premise line items (so scoring matches);
  - keep sections **terse** — a long prose recipe defeats retrieval and blows the budget.
- The card **links to** the delta (`templates/sectors/<slug>.delta.yaml`) and the operational recipe; it **never duplicates** the delta YAML in prose (`_schema.md` and the delta headers both forbid it).
- Make §2's revenue identity **render-able:** write it as an explicit equation and tag each driver as a **PREMISE** (own blue cell), a **FORMULA** (derived), or a disclosed **HISTORICAL driver**. Force yourself to state the build path and why (§5).
- Use cross-links `[[sibling_slug]]` / `[[concept-slug]]` — slugs must actually exist.

### 10.2 The machine delta — `templates/sectors/<slug>.delta.yaml`

The file has **two top-level keys** (verify against `oil_and_gas.delta.yaml` / `telecom.delta.yaml`):

```yaml
signals:                       # >=2 present in the operational tab => sector auto-detected
  - "<distinctive operational label 1>"
  - "<distinctive operational label 2>"
required:
  Input Financials:
    - "<extra financial labels ONLY — never a base line>"
  Input Operational:
    - "<every operational label the build reads + any ALL-CAPS section headers it introspects>"
```

- **`signals:`** — the detection labels. They are read **from the delta** via `canonical_schema.detection_signals()` / `signals_by_sector()` (`canonical_schema.py:93-100`) and consumed by `template_loader.identify_sector` (`:99-112`, needs **≥ 2** present). **There is no `SECTOR_SIGNALS` dict in `template_loader.py`** — older notes that say so are wrong; signals live in the delta YAML.
- The children of `required:` are the **exact sheet-name constants** `Input Financials` and `Input Operational` (`cs.FINANCIALS` / `cs.OPERATIONAL` — any other key like `Financials` or `IS` is **silently ignored**), each a YAML list of label strings.

Rules:

- **Financial list = sector EXTRAS only** (base lives in `canonical_schema.py`). Re-listing a base line fails `test_required_labels_is_base_plus_delta`. **For a Tier-B sector, "extras" must include the §7.2 hard-read labels** (the nine O&G-shaped financial lines), because the shared statement code reads them for every sector — that is the whole point of §0/§7.2. The fastest correct delta for a new Tier-B sector is "the §7.2 financial extras + your operational labels."
- **Operational list = ALL of them** (operational has no universal base).
- **Labels are byte-for-byte the column-B text the build looks up** via `frow[...]`/`orow[...]`. Sign prefixes (`(=)`,`(-)`,`(+/-)`), the `memo: ` prefix, casing, ampersands, spacing — all matter.
- **How to derive the list:**
  - **Tier B (no builder of your own):** you are **NOT writing a build function** — your sector rides the shared generic path. So do **not** "grep your build function" (you have none). The labels you must satisfy come from the **shared** code in `build_model.py`: the `is_line`/`cf_line`/`bs_line`/`corkscrew` calls (`:855-1162`) and the generic seed/operational blocks (`:587-639,746-792`). The concrete answer is already enumerated for you in **§7.2** — copy that list. Do not invent fresh spellings.
  - **Tier A (you write `build_model_<slug>.py`):** grep *your* build function for every `frow['...']` / `hist_fin('...')` / `orow['...']` key that is **not** in `UNIVERSAL_BASE_FINANCIAL`, and list exactly those.
- **Divergent spellings are intentional — preserve them, don't unify.** The same economic concept gets a different spelling per sector precisely so the delta can diverge (e.g. O&G `(+/-) Financial result` vs. telecom `(+/-) Net financial result`; O&G `memo: (+) Depreciation, depletion & amortization` vs. telecom `(-) Depreciation & amortization`). Match the spelling **the build that runs for your sector** actually reads; **never invent a fresh spelling.**
- **Reported aggregates the build keys off** (`(=) EBITDA (as disclosed)`, `EBITDA-AL`, `Net debt`) are intentionally classified `REPORTED_CHECK` by `role_classifier` **even when required**. Do **not** remove them from the delta to "make the role consistent" — telecom legitimately requires `(=) EBITDA (as disclosed)` as an input it divides by margin, yet intake-tags it reported-check. The split is by design.
- **For a bottom-up sector**, the ALL-CAPS **section headers** are legitimate `Input Operational` entries (they are hard-read via `orow[HEADER]`), but remember `scan_assets` is hardwired to the O&G header names — a different bottom-up layout needs its own introspection code, not just delta entries.

### 10.3 The operational/statement build recipe

If Tier B: the recipe is the per-line spec tables (§3.4) describing how the generic path's premises/labels apply — no new code, but write the recipe so the next person can audit it. Confirm the §7.2 financial labels are carried.

If Tier A: the recipe is the **build function** (`build_model_<slug>.py`). State first which integration model you follow (§4 box):
- **plug into `build_model.main()`** — then (a) read the delta's labels, (b) build the operational section exposing the **row-handle ABI** (§4), (c) add an `og`-style dispatch branch and a matching COGS branch, (d) wire IS/BS/CF/Schedules/Valuation, (e) keep the **balance check at 0**; or
- **fork like telecom** — a standalone script that reimplements the downstream; the ABI is then advisory.
Either way: emit the canonical `(=) Implied value per share` label + the verbatim disclaimer (§4.1), and ship a **synthetic input workbook** + a **test** proving no KeyError (§11 step 6).

---

## 11. Wiring a new sector end-to-end (these files move together)

Adding one artifact in isolation breaks the contract tests and/or leaves the sector unreachable. To make a sector **runnable**, not just declared:

1. **`templates/sectors/<slug>.delta.yaml`** — the machine schema (§10.2): `signals:` (≥ 2 distinctive operational labels) + `required:` (financial extras incl. the §7.2 hard-reads; all operational labels). The slug in the filename **must** match the card slug. The set of sectors is **disk-driven**: `canonical_schema.known_sectors()` returns whatever `*.delta.yaml` files exist (`:120-126`) — **adding the file is what registers the sector**; there is no `SECTORS` list to edit in code. (Note: the contract test `test_known_sectors_have_deltas` and a couple of older tests reference a `cs.SECTORS` symbol that is **not** defined in the current `canonical_schema.py` — treat `known_sectors()` as the real API and re-verify the test names before relying on them.)
2. **The card** — `sectors/<slug>.md` (§10.1), same slug.
3. **The three detectors must agree on the canonical slug** (guarded by `tests/test_slug_concordance.py`): `validator.detect_sector`, `sector_knowledge.detect_sector_from_input`, and `template_loader.identify_sector` must all return the *same* slug for your synth input. `identify_sector` is data-driven off your `signals:`; **but `validator.detect_sector` is NOT** — see step 5.
4. **Slug discipline:** wherever a slug appears, use the `canonical_schema` constant or the disk-derived slug — **never write a slug string literal twice** (the `oil_and_gas` vs. `oil_gas` bug is why). If you add a convenience ref like `OIL_AND_GAS`/`TELECOM`, mirror that style.
5. **Make the sector REACHABLE through the documented tooling.** This is the step prior versions of this guide omitted, and without it your sector is unrunnable via the harness pipeline:
   - **`engine/harness/pipeline.py`** routes **only** `oil_and_gas` → `build_model` and `telecom` → `build_model_telecom`, and **`raise ValueError(f"unknown sector: …")` for anything else** (`:34-39`); its CLI `--sector` is `choices=[None, OIL_AND_GAS, TELECOM]` (`:69`). To reach your sector through the pipeline you must extend that dispatch (route unknown/new sectors to `build_model.main()` for Path B, or to your builder for Tier A) **and** widen the `--sector choices`.
   - **`engine/harness/validator.py:detect_sector`** (`:35-44`) recognises only `PRODUCTION BY ASSET`→O&G and `Total lines`→telecom, returning `None` otherwise → `assert_valid_input` raises `InputValidationError` **before** the build. Teach it a signal for your sector (or fall back to `signals_by_sector()` / honour an explicit `--sector`).
   - **Until both edits land, your Tier-B sector runs ONLY via the direct `build_model` entrypoint with an explicit slug** (see §12 step 6), never via `python -m engine.harness.pipeline`.
6. **(Tier A only) the builder** — `build_model_<slug>.py`, and add the slug to `sector_coverage.BUILDERS`. Note: today only `oil_and_gas` is dispatched from `build_model.main()`; telecom is standalone. **Auto-dispatch wiring is the manual step in #5** — a delta does not route a sector to a custom engine.
7. **A synthetic input + a test:**
   - register a new **`synth_inputs_<slug>` fixture** in `tests/conftest.py` (the existing `synth_inputs` is O&G-only, `:19-21`); the sample workbook's `Input Financials`/`Input Operational` column-B labels must be a **superset** of `required_labels(slug)`;
   - add a test mirroring `test_synth_input_satisfies_oil_and_gas_required` (`tests/test_canonical_schema.py:39-51`) **and** a build-it test asserting no `KeyError`.
   - **Caveat that breaks the naive test:** `required_labels(slug)` (base + delta) is **necessary but NOT sufficient** for a Path-B sector — the shared statement code reads the §7.2 O&G-shaped labels too. If your delta omits them, a synth workbook that satisfies `required_labels(slug)` will **pass the label test but the build will still `KeyError`**. Make the synth workbook (and the delta) carry the §7.2 labels, or the test gives false assurance.

The contract guard is `tests/test_canonical_schema.py` (the per-sector spelling-present/other-absent tests, the base-plus-delta test, the synth-input superset test) plus `tests/test_slug_concordance.py`. Run them after every change.

---

## 12. Worked mini-example — a generic Tier-B sector (illustrative, not a target)

Take a simple consumer-goods manufacturer whose economics honestly are "revenue grows, costs are a margin." Aim it at **Path B** (no new build function — but a real delta and the §7.2 financial labels).

1. **Knowledge (§1):** revenue identity `revenue = volume (units) × ASP`; drivers = volume growth and ASP/mix; KPIs = gross margin, capacity utilisation; units = kt, R$/kg. Source each driver.
2. **Card (§10.1):** 7 sections per `_schema.md`. §2 states the identity and tags `volume growth`, `gross margin`, `ASP` as PREMISES; §5 states **"build path = generic top-down (Path B); the disclosed volume/ASP drivers surface as memo lines and are not yet wired to revenue — Stage 3."** §7 declares **Tier B** and lists "a builder to wire volume×ASP" as the path to A.
3. **Input tab — carry the canonical base AND the §7.2 hard-reads verbatim,** or the build crashes (`KeyError`) / silent-0s:
   - universal base (already shared): `(=) Net revenue`, `(=) EBIT`, `(=) EBT`, `(-) Income taxes`, `(=) Net income`, the 20 BS lines.
   - **the §7.2 financial extras the shared statement code hard-reads** (all nine + the two cash lines): `(=) Gross profit`, `(-) Cost of goods sold`, `(-) General & administrative expenses`, `(-) Exploration expenses` (dormant for this sector, still required), `(+/-) Other operating income (expenses)`, `(+/-) Financial result`, `memo: (+) Depreciation, depletion & amortization`, `Provisions (incl. asset retirement obligation)`, `Minority interest (equity)`, `Cash — beginning of period`, `Cash — end of period`. (`(-) Capex` is optional via `if "(-) Capex" in frow`.)
   - disclosed drivers (`Sales volume (kt)`, `Average selling price`) sit under ALL-CAPS headers (`VOLUMES`, `PRICING`) as mixed-case driver lines.
4. **Delta (§10.2) — required, not optional.** `Input Financials:` lists exactly the §7.2 extras above (never a base line). `Input Operational:` lists the headers + drivers (`VOLUMES`, `Sales volume (kt)`, `PRICING`, `Average selling price`). `signals:` lists ≥ 2 of the operational labels (e.g. `Sales volume (kt)`, `Average selling price`).
5. **Premises:** the generic seeds (`rev_growth`, `gross_margin`, `depr`, `sales_to_capital`, `ga`, `tax`, `payout`, the WC days, debt/lease) apply as-is — but note `gross_margin`/`ga`/`tax` are **back-solved from** `(=) Gross profit` / `(-) General & administrative expenses` / `(=) EBT`+`(-) Income taxes` via `gf()` and silently default if those lines are absent (§3.3). Map any sector judgement to one of these or note it needs a builder.
6. **Validate & run:**
   - run `pytest tests/test_canonical_schema.py tests/test_slug_concordance.py` (plus the synth-input + no-KeyError test you added per §11 step 7);
   - **run the build.** Path B is reached by the direct entrypoint with an explicit slug:
     ```
     <python> -m engine.build_model <input.xlsx> <output.xlsx> <slug>
     ```
     (`build_model.main(input, output, sector)`, `:503,1212-1215` — accepts any slug and takes the `else:`/Path B branch.) **`python -m engine.harness.pipeline` will NOT work for a new sector** until you make the §11 step-5 edits — it `raise ValueError("unknown sector: …")`.
   - then verify the built model with the harness: `<python> -m engine.harness <output.xlsx>` (verifies an already-built workbook; balance check = 0 every column, ties, no error cells).

Result: a balancing three-statement model with a Valuation tab, honestly declared Tier B. Wiring volume×ASP into revenue is the documented step to Tier A.

> **Environment preflight (this machine).** Recalc needs the **`formulas`** backend; the harness verification skips/fails without it. And on this machine **`python` / `python3` are not on PATH** — use the Anaconda full path (see MEMORY.md) for every command above, substituted for `<python>`. Run **`<python> -m engine.check_env`** first: it proves the recalc backend actually computes a cross-sheet formula (not merely imports). The pipeline points you here on a recalc failure (`pipeline.py:87`).

---

## 13. Recommended process for the authoring Claude

1. **Read sources** (public only) and the existing exemplar cards for *shape*. Read [`_schema.md`](_schema.md), this guide, and the two delta files.
2. **Distil** the revenue identity, driver tree, KPIs, accounting rules, pitfalls — method not numbers, every claim sourced and confidence-tagged.
3. **Decide the build path** (§5) and the **coverage tier** (§9) — honestly.
4. **Write the card** per `_schema.md` (§10.1) — retrieval-friendly headings, links to the delta, REFUTED claims as "do NOT encode."
5. **Declare the delta** (§10.2) — `signals:` + `required:`; financial extras **including the §7.2 hard-reads** (Tier B) or your build function's non-base reads (Tier A); exact spellings; sheet keys `Input Financials`/`Input Operational`; reported aggregates kept if read. For Tier B copy the §7.2 list — do **not** grep a build function you aren't writing.
6. **Specify the operational recipe** (§3.4 per-line tables) — and, for Tier A, the build function (state plug-in vs. fork; expose the row-handle ABI; emit the `(=) Implied value per share` label + disclaimer; hold the balance check at 0).
7. **Wire it** (§11) — delta + card + slug concordance across the three detectors + the pipeline/validator edits that make it reachable (+ builder + `BUILDERS` for Tier A), one slug everywhere.
8. **Validate against the engine** — `tests/test_canonical_schema.py` + `tests/test_slug_concordance.py` + your synth-input/no-KeyError test, then build with `build_model <input> <output> <slug>` and verify with the harness. The model must balance and not KeyError before you call the sector done. Use the Anaconda python; run `check_env` first.

---

## 14. Integration checklist (definition of done)

- [ ] Card `sectors/<slug>.md` follows `_schema.md` (front-matter + 7 sections in order); headings are retrieval-friendly; links to the delta; no delta YAML duplicated in prose.
- [ ] Every load-bearing claim has a `> source:` + confidence tag; ⚠️ drivers are the research agenda, never fabricated citations; no numbers hardcoded (method only); no investment advice/target price.
- [ ] Delta `templates/sectors/<slug>.delta.yaml`: `signals:` has **≥ 2 distinctive operational labels**; sheet keys are exactly `Input Financials` / `Input Operational`; financial list = extras only (no base line re-listed) **and includes the §7.2 hard-read labels** (Tier B) or the builder's non-base reads (Tier A); operational list = all operational labels + any ALL-CAPS headers; labels byte-for-byte match the build's reads; divergent spellings preserved; reported aggregates kept if read.
- [ ] Slug is **one canonical family**: identical across card filename, delta filename, and every detector; the three detectors (`validator.detect_sector`, `sector_knowledge.detect_sector_from_input`, `template_loader.identify_sector`) agree (`test_slug_concordance.py`).
- [ ] Input tab carries the universal base **and** the §7.2 financial labels **verbatim** (else KeyError or silent 0-seed); operational headers ALL-CAPS, drivers mixed-case.
- [ ] Build path and coverage **tier** declared honestly in card §5/§7; if Tier B, the gap to Tier A is named.
- [ ] **Reachability wired:** `harness/pipeline.py` dispatch + `--sector` choices extended for the new slug; `harness/validator.py:detect_sector` teaches a signal (or falls back). If not yet done, the model is runnable **only** via `build_model <input> <output> <slug>` — note that explicitly.
- [ ] (Tier A) `build_model_<slug>.py` states plug-in-vs-fork; exposes the row-handle ABI (if plugging in) or reimplements downstream (if forking); emits `(=) Implied value per share` + the verbatim no-target-price disclaimer (`inv_valuation_disclaimer`); approved assumptions carry method+source (`inv_assumptions_provenance`); keeps the **balance check = 0** every column; added to `BUILDERS`.
- [ ] `synth_inputs_<slug>` fixture in `tests/conftest.py` (labels ⊇ `required_labels(slug)` **and** the §7.2 labels) + a test proving no KeyError.
- [ ] `tests/test_canonical_schema.py` + `tests/test_slug_concordance.py` pass; **`check_env` green** (recalc backend); the build runs (`build_model <input> <output> <slug>`) and the harness reports the balance check = 0 in every column. Use the Anaconda python path on this machine.

---

### Engine reference (where each rule lives)

> Line numbers verified 2026-06-20; **re-grep the named symbol if an offset looks wrong** (see the note under the title).

- Build-path gate: `og = ...` in `build_model.py:533` (`grep -n "og = "`) · Stage-3 hole comment: `:529-532`
- Path-A `if og:` branch (O&G bottom-up): `build_model.py:556-586,675-745` · Path-B `else:` branch (generic top-down): `:587-615,747-792`
- Two readers: safe seed reader `gf()` `:551-554` (silent default) vs. statement reader `hist_fin()` = `frow[...]` `:878` (KeyError) · §7.2 hard-read labels: IS `:892-933`, BS `:1137,1153`, CF cash `:1080`, WC `:623`, seeds/debt `:594-637`
- `build_timeline` (tl shape, kinds): `:83-106` · `block_cols`: `:109-110` · `prev_period`: `:113-124` · `yoy_col`: `:127-132`
- `Line`/`add_line`/`fill` (period kinds + signature): `:172-216` · fonts/formats: `:29-42` · `prem()` P/Praw: `:259-264` · `seed_premises`: `:220-256` · `corkscrew`: `:798-818` · ARO roll-forward (built unconditionally): `:859-864` · balance check: `:1157-1162`
- `main(input, out, sector=None)` (Path-B entrypoint): `:503`; CLI `python -m engine.build_model <input> <output> [slug]`: `:1212-1215`
- Valuation tab + disclaimer + `(=) Implied value per share` label: `add_valuation_tab` `:268`, label/disclaimer `:441-442,476`
- Operational introspection (ALL-CAPS headers): `template_loader.py:124-129` · per-asset scan (O&G-only): `:132-154` · asset headers/constants: `:39-43` · `identify_sector` (data-driven, ≥2 signals): `:99-112` · `locate_card`: `:115-119`
- Canonical schema (base + delta + slugs + `known_sectors` + `signals_by_sector` + `normalize`): `engine/canonical_schema.py` (base `:40-70`, STRUCTURAL `:75`, `signals` `:93-100`, `required_labels` `:107-117`, `known_sectors` `:120-126`)
- Coverage gate / tiers (card+delta → A, card-only → B, none → C; no hardcoded builder list): `engine/sector_coverage.py`
- Card excerpt retrieval: `engine/sector_knowledge.py:61-86`
- Provenance invariant (runtime + build-time): `engine/assumptions.py` (`approve()`), `engine/proposals.py`, `engine/harness/invariants.py:386-407` (`inv_assumptions_provenance`)
- Compliance disclaimer invariant (FAIL): `engine/harness/invariants.py:361-383` (`inv_valuation_disclaimer`)
- Role classifier — real roles `STATEMENT / CAPITAL_STRUCTURE / REPORTED_CHECK / OPERATIONAL_RAW / CONTEXTUAL` (no `STRUCTURAL` role; a `STRUCTURAL` input item maps to `CAPITAL_STRUCTURE`): `engine/role_classifier.py:14-44`
- Harness pipeline (builder by naming convention — `_select_builder`: `build_model_<slug>.py` if it exists, else the default engine; no sector branches): `engine/harness/pipeline.py` · input validator `detect_sector` (data-driven — delegates to `identify_sector`): `engine/harness/validator.py` · verify-only entrypoint: `python -m engine.harness <model.xlsx>` · env preflight: `python -m engine.check_env`
- Schedules + common premises (flags read globally; stale per-sector comments): `templates/base.yaml`, read at `template_loader.py:166-167`
- Exemplar deltas (with `signals:`): `templates/sectors/oil_and_gas.delta.yaml`, `templates/sectors/telecom.delta.yaml`
- Separate-engine precedent (forks the pipeline; not dispatched from `main()`): `engine/build_model_telecom.py`
- Contract guards: `tests/test_canonical_schema.py`, `tests/test_slug_concordance.py`; synth fixture `tests/conftest.py:19-21`
- Card contract (do not duplicate): [`_schema.md`](_schema.md) · sources registry: [`_sources.md`](_sources.md)

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

---

## 0. The one thing you must internalise: prose does not build the model

There are **two independent things** you can ship for a sector, and they do completely different jobs:

1. **The method card** (`sectors/<slug>.md`) — prose. It grounds the *assumption conversation*. The engine reads it through exactly one function, `sector_knowledge.card_excerpt()`, which keyword-scores the card's markdown sections against the line item being discussed and injects a slice into the proposal prompt. **`build_model.py` never imports `sector_knowledge`.** A perfect card produces a richer conversation and the *same* model.

2. **The build path** — code. The actual rows, formulas, and statement wiring are produced by a Python build function. Today there are exactly two build paths, and the dispatch is one line in `engine/build_model.py`:

   ```python
   og = (an.sector == 'oil_and_gas') and bool(an.assets)
   ```

   - **Path A — bottom-up** (volume × price, per asset): fires *only* for the literal slug `oil_and_gas` with assets. (`build_model.py:675-745`.)
   - **Path B — generic top-down** (revenue-growth × margin): everything else. (`build_model.py:747-792`.)
   - Telecom is a **third, separate script** (`build_model_telecom.py`) — not dispatched from `main()` at all; it is run standalone.

The machine schema (`<slug>.delta.yaml`) sits *between* these: it declares **which input labels must exist** and lets the validator prove "the engine will not KeyError". It does **not** emit statements. **A sector with a delta but no builder validates and produces nothing custom — it falls into Path B.**

**Consequence for you:** decide *up front* which build path your sector takes (§5), and be honest about the resulting **coverage tier** (§9). Do not imply the card drives the build. Do not tell the next Claude "just write a delta and you're done."

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
4. **Units** for every driver (kt, m³, lines, members, MWh, R$/unit, %, days) — you will need the unit and number format for every premise (§3).
5. **The public sources you actually read** — each load-bearing claim must carry a `> source:` callout pointing to an ID in [`_sources.md`](_sources.md), with a confidence tag. If you cannot source a driver, tag it `⚠️ to-verify` — **never fabricate a citation** (§8).

This is §1–§3 of the card. Distil, do not copy. Encode **method, not numbers**: "spread per route × utilization", never a 2026 spot price baked in as a value.

---

## 2. How to organise the OPERATIONAL part of the Excel

The operational section lives on a tab the engine calls **"Operational Model"**. Its layout is **label-driven**, so the typographic conventions below are load-bearing, not cosmetic.

### 2.1 Section headers vs. driver lines — casing IS the API

`introspect_operational()` (`template_loader.py:122-127`) classifies a row purely by its text:

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

- **Generic path (Path B):** every non-section operational row is surfaced as a **flat-projected memo line** (history link + carry-forward), and that is *all* — **disclosed drivers are NOT wired to revenue** (`build_model.py:750-751,754-765`, comment "not yet wired to revenue — Stage 3"). In Path B the disclosed driver tree is **decorative**: revenue is still `rev_growth × margin` off the financials. Organise the tab so a human can read the drivers, but do not expect them to move the model.
- **Bottom-up path (Path A):** per-group introspection via `scan_assets()` reads named slots. **This machinery is hard-coded to O&G's three section headers** (`PRODUCTION BY ASSET`, `LIFTING COST BY ASSET`, `CAPEX BY ASSET`) and `Asset 1 name`, reading names from column C, max 8 slots (`template_loader.py:39-43,130-152`). **A non-O&G bottom-up sector cannot reuse it** — it needs new introspection code in a new builder (§5).

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

(`build_model.py:29-43` defines `BLUE/BLACK/GREEN` and the `NUM_MN/NUM_1D/NUM_2D/PCT` formats.)

### 3.1 The four period kinds — never one blanket formula

Every line is specified across the engine's four column kinds (`Line.fill(hist=, qp=, yb=, ys=)`, `build_model.py:172-216`):

- **QH** (historical quarter) → **green link** to the Input tab.
- **QP** (projected quarter) → **black formula** from premises.
- **YB** (year that closes a 4-quarter block) → **aggregation of its own four quarter columns** — `sum` for flows, `avg` for rates/prices/per-unit, `eop` for stocks/balances. YB years are **not re-projected**.
- **YS** (pure annual year, years 3–10) → the **same** projection formula as QP, evaluated on the annual column.

> **Gotcha:** summing a price, or averaging a flow, in YB corrupts the annual figure even though the balance check still passes. Match the aggregator to the line type.

### 3.2 The hard formula rules (mandatory — see CLAUDE.md "Spreadsheet conventions")

1. **Sign convention 1, baked into the formula and announced by the label prefix.** Revenues/inflows positive, costs/outflows negative. A cost line must *compute* a negative (`=-{vol}*{rate}`), so subtotals are plain additions (`EBIT = SUM(gross profit, G&A, …)`, each term already signed). The label prefix must agree with the sign the formula produces: `(=)` subtotal/result, `(-)` cost/deduction, `(+)` addition, `(+/-)` signed-either-way.
2. **No constant embedded in a formula.** Any number that is a *judgement* (growth, margin, price, premium/discount, per-unit cost, days, payout, tax rate, a unit conversion that is really an assumption) **must be a Premises row** referenced by formula. The *only* literals tolerated are non-judgement structural/unit constants — e.g. the `/1000` that converts (units × price) to millions, or the `0` floor inside `MAX/MIN`. **If unsure whether a number is structural or a judgement, treat it as a judgement and give it a premise cell.**
3. **No nested IF.** Use `MIN`/`MAX`/flag cells. Caps and floors: `=MAX(0, x)`, `=MIN(cap, x)`. Taxes only on positive EBT: `=-MAX(EBT,0)*Praw(tax)`. Division safety: `IFERROR(expr, 0)` for value lines feeding subtotals (an `IFERROR(...,"-")` string can poison a downstream `SUM`; reserve `"-"` for display-only ratios). Any sector threshold (price floor, capacity cap, take-or-pay) → `MIN`/`MAX` against a premise cell holding the threshold, or a `0/1` flag premise multiplied in.
4. **No named ranges, no macros, no hidden rows.** All references are explicit A1-style cross-tab refs (`IS!D12`, `'Operational Model'!E7`).
5. **No circularity (MVP).** Anything accruing on a balance references the **beginning-of-period (BOP)** cell of that balance's corkscrew, never the EOP/same-period cell: `debt interest = -Praw(debt_rate) * <debt BOP cell>`. Roll-forwards use the corkscrew pattern **BOP / (+) additions / (−) reductions / (=) EOP**, with BOP(t) = EOP(t−1) (`corkscrew()`, `build_model.py:798-818`). Revolver interest is deliberately omitted to avoid the cash→interest→cash loop; do not reintroduce it.

### 3.3 Premise referencing mechanics (use verbatim)

- `P(key, period)` → a self-contained cell formula `='Premises'!<col><row>` (the whole cell *is* the premise).
- `Praw(key, period)` → the bare reference `Premises!<col><row>` for embedding inside a larger formula, e.g. `=-{vol}*Praw(lift)/1000`.

A premise row is created by a **seed tuple** in the `seeds` list (`seed_premises()`, `build_model.py:220-256`):

```
(key, label, unit, number_format, seed_value_expr, annual_multiplier)
```

- **`number_format`**: `PCT` | `NUM_1D` | `NUM_2D` | `NUM_MN`.
- **`seed_value_expr`**: how the seed is **back-solved from the last historical actual** (e.g. `royalties% = government take ÷ revenue`; `DSO = AR ÷ revenue × 91.25`; `depletion rate = D&A ÷ volume × 1000`). Method, not a typed number.
- **`annual_multiplier`**: `1` for a rate/price/margin (same per period when annualised) — `4` for a per-quarter **flow** that must be ×4 to annualise (capex, exploration, lease amounts, `days` 91.25→365). **Omitting this makes annual projections 4× wrong.**

### 3.4 The per-line spec template (fill one of these per operational line)

Specify each operational line as a small table mirroring an `add_line()` call:

| Field | What to write |
|---|---|
| **Label** | text with the correct `(=)`/`(-)`/`(+)`/`(+/-)` prefix |
| **Unit / format** | e.g. `R$/m³` / `NUM_2D` |
| **History (QH)** | green link to which `Input Operational`/`Input Financials` row, or `none` if projection-only |
| **Projection (QP)** | the black formula in terms of other Operational-Model rows and `Praw('<key>')`, producing the sign the label promises |
| **Year-block (YB)** | `sum` \| `avg` \| `eop` |
| **Pure-annual (YS)** | normally identical to QP |
| **Premises consumed** | each premise key with unit / format / seed expr / annual multiplier |
| **Downstream** | which financial/statement line this feeds (§4) |

> **EXAMPLE — O&G lifting-cost line (imitate the *shape*, not the sector).** Label `(-) Lifting cost` / `NUM_MN`; QH `none` (projection-only cost); QP/YS `=-{sales_volume_cell}*Praw(lift)/1000` (negative; `/1000` is the unit constant, allowed); YB `sum`; premise `lift` = "Lifting cost (weighted avg)", `USD/boe`, `NUM_1D`, seed = production-weighted lifting cost of last actual, mult `1`; downstream → IS `(-) Cost of goods sold`. (`build_model.py:726-727,567`.)

> **EXAMPLE — generic top-down (what any new sector gets with zero code change).** Revenue: `(=) Revenue`, QH green link to `Input Financials` `(=) Net revenue`, QP/YS `={prev_rev_cell}*(1+Praw(rev_growth))`, YB `sum`. Cost: `(-) Cost of goods sold (ex-D&A)` = `=-{rev_cell}*(1-Praw(gross_margin))`. Capex (Damodaran sales-to-capital): `=Praw(depr)+({rev_t}-{rev_t-1})/Praw(sales_to_capital)`. (`build_model.py:769-791`.)

---

## 4. What changes in the 3 STATEMENTS for the sector

The statements are wired by **row handles**, not labels. The operational section returns handles (`row_rev`, `row_cogs` / the O&G triple `row_liftc`/`row_royc`/`row_depl`, `row_depl`, `row_capext`) and the IS/BS/CF/Schedules/Valuation consume them by sheet-qualified cell refs. **This row-handle interface is the implicit ABI** between the operational section and the rest of the engine: any new build function must expose the same handles so the downstream statements keep balancing. (`build_model.py:768-792`; IS COGS branch `:892-899`; CF capex `:1012`; PP&E corkscrew additions=capex / reductions=depletion `:822-824`.)

What is genuinely sector-specific:

1. **Revenue identity into the IS.** Path B: `(=) Net revenue` grows by `rev_growth`. A bottom-up/multi-stream sector instead sums its driver-built segment lines into net revenue — and that requires a builder (§5).
2. **The cost / EBIT direction.** Two archetypes:
   - **Expense-up-to-EBIT** (O&G style): COGS reconstructed from operational cost rows; `GP − G&A − … = EBIT`; `EBITDA = EBIT + DD&A` as a derived memo.
   - **Margin-down-from-EBITDA** (telecom style): keys off a disclosed-EBITDA margin premise (`opex ex-D&A = -rev × (1 − margin)`), `EBITDA = rev + opex`, `EBIT = EBITDA − D&A`.
   State which one your sector uses — it dictates which IS rows exist and the formula *direction*.
3. **D&A and capex drivers.** Specify the D&A driver (unit-of-production rate? % of PP&E? flat per-period?) and the capex driver (per-asset? sales-to-capital? flat?), and which schedule rows they feed.
4. **Sector-specific lines that appear or stay dormant.** Enumerate which extra lines your statements carry (e.g. a regulated-asset-base roll-forward, a loss-provision schedule, a spectrum/intangible amortisation block) and which base lines you leave at zero. The generic build leaves disclosed drivers as memo lines only.
5. **Working capital & financial result.** State whether WC is **days-driven** (full DSO/inv-days/DPO schedule feeding BS+CF) or **frozen** (change = 0); whether debt is **dynamic with a revolver/cash-sweep plug** or **held flat**; and how financial result is assembled (`debt int + lease int − ARO accretion + other`, or a single flat net premise). These choices change the BS plug behaviour and the CF reconciliation.
6. **The balance check must stay 0 in every column** (`build_model.py:1157-1162`), verified by the recalculation harness. Any new line that writes a BS/CF row must show how it reconciles. A line only the IS or the Valuation tab reads does not threaten the check.

### 4.1 IFRS / accounting rules to encode (card §4)

Cite the standard for each. Common sector overlays: revenue recognition timing (IFRS 15 — contra-revenue, variable consideration), capitalisation vs. expensing (IAS 38 software/R&D; IFRS 6 exploration; IAS 16 PP&E), depletion/UoP, fair value (IAS 41 biological assets; financial instruments), leases (**IFRS 16** — RoU + lease-liability twin roll-forwards; report both **EBITDA and EBITDA-AL**; in the EV→equity bridge leases count as debt; FCFF deducts lease payments), provisions/decommissioning (IAS 37 — ARO), and BR taxation (JCP, effective rate). Note IFRS-vs-US-GAAP divergence where it matters. **Every accounting claim carries a `> source:` + confidence tag.**

---

## 5. Which build path — and the decision rule

This is the most important design decision. Decide it explicitly in card §5 and state *why*.

**Use the generic top-down path (Path B) — zero code, available today — when** the sector's economics are honestly "revenue grows at a rate, costs are a margin." Provide a card + canonical input labels and you get a balancing model for free; the disclosed drivers appear as memo lines. This is the **happy path** — aim a new sector here first.

**You need a dedicated builder (a new `build_model_<slug>.py`, the telecom precedent) when** the revenue identity is **multi-stream, roll-forward-based, or margin-down-from-EBITDA** — anything Path B's single-line `rev_growth × margin` gets economically wrong. Signals you need a builder:

- revenue must **sum several driver-built segment lines** (subscribers × ARPU per segment; volume × price per commodity; members × premium);
- a **stock corkscrew drives revenue** (subscriber base, regulated asset base, loan book);
- the cost build is **margin-down-from-disclosed-EBITDA**;
- the sector needs a **schedule that does not exist** in `base.yaml` (see §6) — e.g. a loss-provision roll-forward, a spectrum-amortisation block separate from PP&E.

**Per-asset bottom-up (Path A)** is *O&G-specific code*. Do not assume a new bottom-up sector can reuse it — `scan_assets`, the per-asset capex-total offset (`capex_header + max_slots + 1`, `build_model.py:738-740`), and the consolidated Brent/Realized/Sales-volume labels are all O&G-shaped. A different per-asset sector needs its own introspection + builder.

> **EXAMPLE — telecom (separate-engine precedent).** Card demands subscriber-corkscrew × ARPU by segment + service-vs-handset split + EBITDA-AL. This cannot run through Path B, so it lives in `build_model_telecom.py` with its own seeds and its own financial labels (`(=) EBITDA (as disclosed)`, `(-) Operating expenses (ex-D&A)`, segment memo revenues). It is invoked as a standalone script — **adding a delta does not auto-route a sector to a custom engine; that wiring is a separate manual step.**

---

## 6. Which schedules apply (and the base.yaml reality)

`templates/base.yaml` is the **only** template (no per-sector YAML exists; `oil_and_gas.yaml` was deleted). It ships five schedules:

| Schedule | Default | Premises (ids) |
|---|---|---|
| `working_capital` | **enabled** | `dso, invdays, ocadays, dpo, ocldays` |
| `debt` | **enabled** | `debt_draw, debt_repay, debt_rate, debt_curr_pct, other_finres, min_cash` |
| `leases` | **enabled** | `lease_add, lease_depr_amt, lease_princ_amt, lease_rate, lease_curr_pct` |
| `aro` | **disabled** | `aro_accr, aro_settle` |
| `hedge` | **disabled** | (none defined) |

> **Critical contradiction to flag honestly.** The base.yaml comments ("sector YAML opts in", "extends: base") are **stale** — no sector YAML exists. In code today the `enabled` flags are read **globally** (`template_loader.py:166-167`), and the ARO/lease premises are appended **unconditionally for every sector** (`build_model.py:641-667`). **A sector cannot turn a schedule on/off via data today**, and cannot add a sector-specific schedule without editing `build_model.py`. So:
> - In card §5 you may **describe** the schedules your sector needs (including ones that don't exist yet — e.g. a regulated-asset-base or loss-provision roll-forward).
> - But state plainly that adding such a schedule is a **code change**, not a data change, and list which of the 5 base schedules apply vs. which the sector needs that **don't exist yet**.

When you do seed a base schedule, map your sector premises onto its ids and give each a seed back-solved from history (DSO from AR, DPO from payables, cost-of-debt from interest÷debt, etc.).

---

## 7. The canonical input labels the build reads by exact string

The build reads financial and operational lines by **exact string match** (`gf(label)` / `frow[...]` / `orow[...]`). A renamed or mis-prefixed label does **not** error loudly — `gf()` returns its default and `g()` coerces `None→0`, so the line is **silently seeded 0** and the model balances at 0 but is economically empty (`build_model.py:549,551-554`). **There is no validator that the operational build is non-trivial** — silence is the failure mode. Therefore the per-sector input tab MUST carry the canonical labels **verbatim**.

### 7.1 The universal base (already shared — never re-list it)

`UNIVERSAL_BASE_FINANCIAL` (`canonical_schema.py:39-68`) is shared by every sector and lives **only** in `canonical_schema.py`:

- IS base: `(=) Net revenue`, `(=) EBIT`, `(=) EBT`, `(-) Income taxes`, `(=) Net income`.
- BS base (20 lines): `Cash and equivalents`, `Short-term investments`, `Trade receivables`, `Inventories`, `Other current assets`, `PP&E`, `Intangible assets and goodwill`, `Right-of-use assets`, `Deferred tax assets`, `Other non-current assets`, `Trade payables`, `Other current liabilities`, `Loans and financing (current)`, `Loans and financing (non-current)`, `Lease liabilities (current)`, `Lease liabilities (non-current)`, `Deferred tax liabilities`, `Other non-current liabilities`, `Share capital and reserves`, `Retained earnings (accumulated)`.

The Valuation/ROIC/EV→equity bridge depends on a **fixed subset of these BS labels** (`(=) Total equity`, `Cash and equivalents`, `Short-term investments`, `Minority interest (equity)`, `PP&E`). A sector that doesn't carry those exact lines breaks the bridge even if the operational layer builds fine.

> **Do NOT re-list any base line in your delta** — `test_required_labels_is_base_plus_delta` asserts `fin − base == set(delta-financial)` exactly, so a duplicated base line **fails the test**.

### 7.2 Structural input

`STRUCTURAL = ['memo: Shares outstanding (EOP)']` (`canonical_schema.py:73`) is the per-share-value input. It is **defined but not yet hard-required**; the build reads it best-effort and falls back to a 1000-share seed. Declare it for the sector (capital-structure / valuation input), and note it is currently optional.

---

## 8. Provenance & public-source discipline (anti-hallucination — non-negotiable)

This is an engine invariant, not a courtesy. `assumptions.approve()` raises `AssumptionProvenanceError` without all three of `method`, `source`, `source_date`; `proposals.py` requires `source` in its input schema. **A card claim with no `> source:` can never become an approvable premise.**

- **Three-tier confidence (reuse exactly, per `_schema.md`):** ✅ **Verified** (adversarial deep-research, vote ≥ 2-0 vs. primary/strong-secondary source) · 🟡 **Seed** (single-source or reputable-but-unverified; confirm before hardcoding) · ⚠️ **To-verify** (practitioner/textbook knowledge, not yet sourced — **never present as verified, never attach a fabricated citation**; these *are* the round-N research agenda). Roll them up in the `coverage:` front-matter (`verified | partial | seed-only`) and tag inline where claims diverge.
- **Method, not numbers** — doubly enforced (the card schema forbids hardcoded figures *and* the engine treats premises as cells). Point-in-time figures appear only as **dated illustrations with provenance**, never as values to hardcode.
- **Distillation, not copying.** Paraphrase. Never quote the proprietary archives. Public sources only.
- **No investment advice / no target price** (MVP compliance).
- ⚠️ drivers are allowed in the card as the research agenda, but **cannot be silently promoted** into the model as approved.

> **EXAMPLE — the honesty model (tech/SaaS card).** It flags that only the IAS 38 R&D/software-capitalisation rule is ✅ verified and labels the entire ARR/MRR/NRR/CAC/LTV driver tree ⚠️ "no citation." That is the correct way to author a card that is mostly a research gap — **without fabricating sources.**

---

## 9. Coverage tier — and how to be honest about it

The deterministic gate (`sector_coverage.py`) classifies every sector:

- **Tier A (full):** card **+** delta **+** a dedicated builder. `BUILDERS = {oil_and_gas, telecom}` — and that set is **code**, not data.
- **Tier B (partial):** card exists, but no delta and/or only the generic top-down builder → lower-fidelity Path B model.
- **Tier C (none):** no card → **blocked** at Fase 1 intake, with the list of what *is* modelable.

**You cannot make a sector Tier A by authoring prose + YAML alone.** Tier A requires a builder. Authoring a card + delta lands you at **Tier B**, and that is a perfectly good, honest outcome for a sector with simple top-down economics. State plainly in card §7 where the sector lands and exactly what is missing to reach A (the builder, and which schedules/labels it would need). **Overclaiming coverage is a compliance failure** that mirrors the ⚠️/🟡 discipline.

> **EXAMPLE — fuel-distribution (honest Tier B).** Verified-core card (gross profit off volume(m³) × R$/m³ by product, recurring-vs-reported margin, inventory-effect line, price-aware WC) but **no delta/builder yet**. Correct declaration: "the card grounds premises; reaching Tier A needs the delta + a builder for the inventory-effect / R$-per-m³ build." Do not pretend the card alone models it.

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

A single top-level key `required:` whose children are the **exact sheet-name constants** `Input Financials` and `Input Operational` (`cs.FINANCIALS` / `cs.OPERATIONAL` — any other key like `Financials` or `IS` is **silently ignored**), each a YAML list of label strings:

```yaml
required:
  Input Financials:
    - "<extra financial labels ONLY — never a base line>"
  Input Operational:
    - "<every operational label the build reads + any ALL-CAPS section headers it introspects>"
```

Rules:

- **Financial list = sector EXTRAS only** (base lives in `canonical_schema.py`). Re-listing a base line fails `test_required_labels_is_base_plus_delta`.
- **Operational list = ALL of them** (operational has no universal base).
- **Labels are byte-for-byte the column-B text the build looks up** via `frow[...]`/`orow[...]`. Sign prefixes (`(=)`,`(-)`,`(+/-)`), the `memo: ` prefix, casing, ampersands, spacing — all matter. Derive the list by grepping your build function for every `frow['...']` / `orow['...']` key that is **not** in `UNIVERSAL_BASE_FINANCIAL`, and list exactly those.
- **Divergent spellings are intentional — preserve them, don't unify.** The same economic concept gets a different spelling per sector precisely so the delta can diverge (e.g. O&G `(+/-) Financial result` vs. telecom `(+/-) Net financial result`; O&G `memo: (+) Depreciation, depletion & amortization` vs. telecom `(-) Depreciation & amortization`). Match the spelling **your** build function actually reads; **never invent a fresh spelling.**
- **Reported aggregates the build keys off** (`(=) EBITDA (as disclosed)`, `EBITDA-AL`, `Net debt`) are intentionally classified `REPORTED_CHECK` by `role_classifier` **even when required**. Do **not** remove them from the delta to "make the role consistent" — telecom legitimately requires `(=) EBITDA (as disclosed)` as an input it divides by margin, yet intake-tags it reported-check. The split is by design.
- **For a bottom-up sector**, the ALL-CAPS **section headers** are legitimate `Input Operational` entries (they are hard-read via `orow[HEADER]`), but remember `scan_assets` is hardwired to the O&G header names — a different bottom-up layout needs its own introspection code, not just delta entries.

### 10.3 The operational/statement build recipe

If Tier B: the recipe is the per-line spec tables (§3.4) describing how the generic path's premises/labels apply — no new code, but write the recipe so the next person can audit it.

If Tier A: the recipe is the **build function** (`build_model_<slug>.py`) that (a) reads the delta's labels, (b) builds the operational section exposing the **row-handle ABI** (§4), (c) wires IS/BS/CF/Schedules/Valuation, (d) keeps the **balance check at 0**, plus a **synthetic input workbook** and a **test** proving no KeyError.

---

## 11. Wiring a new sector end-to-end (these files move together)

Adding one artifact in isolation breaks the contract tests. To make a sector **reachable**, not just declared:

1. **`canonical_schema.py`** — add the slug constant + the `SECTORS` tuple entry. (`test_known_sectors_have_deltas` asserts `known_sectors() == SECTORS`, so a delta file with no constant — or a constant with no delta — **fails**.) Import the constant everywhere; **never write the slug string literal again** (the `oil_and_gas` vs. `oil_gas` bug is why).
2. **`templates/sectors/<slug>.delta.yaml`** — the machine schema (§10.2). Slug in the filename **must** match the front-matter slug and the constant (guarded by `test_slug_concordance.py`).
3. **`template_loader.py` → `SECTOR_SIGNALS`** — register **≥ 2 distinctive operational labels** so `identify_sector()` (needs ≥ 2 hits) can auto-route. Without it the sector is **undetectable**, the build prints "could not identify the sector," and falls to the generic path **even if a card exists**; the user must then pass the slug explicitly.
4. **The card** — `sectors/<slug>.md` (§10.1), same slug.
5. **(Tier A only) the builder** — `build_model_<slug>.py`, and add the slug to `sector_coverage.BUILDERS`. Note: today only `oil_and_gas` is dispatched from `build_model.main()`; telecom is standalone. **Auto-dispatch wiring is a separate manual step** — a delta does not route a sector to a custom engine.
6. **A synthetic input + a test** — a sample workbook whose `Input Financials`/`Input Operational` column-B labels are a **superset** of `required_labels(slug)`, plus a test mirroring `test_synth_input_satisfies_<sector>_required` and proving the build does not KeyError. **The validator passing does NOT prove the engine won't KeyError unless a synth-input test mirrors the build's reads.**

The contract guard is `tests/test_canonical_schema.py` (`test_known_sectors_have_deltas`, `test_required_labels_is_base_plus_delta`, the per-sector spelling-present/other-absent tests, the synth-input superset test). Run it after every change.

---

## 12. Worked mini-example — a generic Tier-B sector (illustrative, not a target)

Take a simple consumer-goods manufacturer whose economics honestly are "revenue grows, costs are a margin." Aim it at **Path B** with **zero code change**.

1. **Knowledge (§1):** revenue identity `revenue = volume (units) × ASP`; drivers = volume growth and ASP/mix; KPIs = gross margin, capacity utilisation; units = kt, R$/kg. Source each driver.
2. **Card (§10.1):** 7 sections per `_schema.md`. §2 states the identity and tags `volume growth`, `gross margin`, `ASP` as PREMISES; §5 states **"build path = generic top-down (Path B); the disclosed volume/ASP drivers surface as memo lines and are not yet wired to revenue — Stage 3."** §7 declares **Tier B** and lists "delta + builder needed to wire volume×ASP" as the path to A.
3. **Input tab:** carries the canonical financial labels **verbatim** (`(=) Net revenue`, `(=) Gross profit`, `(-) Cost of goods sold`, `(-) General & administrative expenses`, `(=) EBT`, `(-) Income taxes`, the WC lines, the debt/lease lines) so Path B seeds correctly. Disclosed drivers (`Sales volume (kt)`, `Average selling price`) sit under ALL-CAPS headers (`VOLUMES`, `PRICING`) as mixed-case driver lines.
4. **Delta (§10.2):** optional for Tier B. If you add one to formalise the operational labels, list **only** the extras (e.g. `VOLUMES`, `Sales volume (kt)`, `PRICING`, `Average selling price`) under `Input Operational`; add nothing to `Input Financials` that is already in the base.
5. **Premises:** the generic seeds (`rev_growth`, `gross_margin`, `depr`, `sales_to_capital`, `ga`, `tax`, `payout`, the WC days, debt/lease) apply as-is; map any sector judgement to one of these or note it needs a builder.
6. **Validate (§11):** add the slug + SECTOR_SIGNALS (≥ 2 of the operational labels) + (if delta) the constant; run `tests/test_canonical_schema.py`; run the harness end-to-end (`python -m engine.harness.pipeline <input> <output>`) and confirm the balance check = 0 in every column.

Result: a balancing three-statement model with a Valuation tab, honestly declared Tier B. Wiring volume×ASP into revenue is the documented step to Tier A.

---

## 13. Recommended process for the authoring Claude

1. **Read sources** (public only) and the existing exemplar cards for *shape*. Read [`_schema.md`](_schema.md), this guide, and the two delta files.
2. **Distil** the revenue identity, driver tree, KPIs, accounting rules, pitfalls — method not numbers, every claim sourced and confidence-tagged.
3. **Decide the build path** (§5) and the **coverage tier** (§9) — honestly.
4. **Write the card** per `_schema.md` (§10.1) — retrieval-friendly headings, links to the delta, REFUTED claims as "do NOT encode."
5. **Declare the delta** (§10.2) — extras only, exact spellings, sheet keys `Input Financials`/`Input Operational`, reported aggregates kept if the build reads them.
6. **Specify the operational recipe** (§3.4 per-line tables) — and, for Tier A, the build function exposing the row-handle ABI (§4) with the balance check held at 0.
7. **Wire it** (§11) — slug constant + delta + SECTOR_SIGNALS (+ builder + BUILDERS for Tier A), one slug across all of them.
8. **Validate against the engine** — `tests/test_canonical_schema.py` + a synth-input test + the recalculation harness. The model must balance and not KeyError before you call the sector done.

---

## 14. Integration checklist (definition of done)

- [ ] Card `sectors/<slug>.md` follows `_schema.md` (front-matter + 7 sections in order); headings are retrieval-friendly; links to the delta; no delta YAML duplicated in prose.
- [ ] Every load-bearing claim has a `> source:` + confidence tag; ⚠️ drivers are the research agenda, never fabricated citations; no numbers hardcoded (method only); no investment advice/target price.
- [ ] Delta `templates/sectors/<slug>.delta.yaml`: sheet keys are exactly `Input Financials` / `Input Operational`; financial list = extras only (no base line re-listed); operational list = all operational labels + any ALL-CAPS headers; labels byte-for-byte match the build's reads; divergent spellings preserved; reported aggregates kept if read.
- [ ] Slug is **one canonical family**: identical across card filename, delta filename, `canonical_schema.SECTORS`/constant, `SECTOR_SIGNALS`, and (Tier A) `BUILDERS`.
- [ ] `SECTOR_SIGNALS` has **≥ 2 distinctive operational labels** for auto-detection.
- [ ] Input tab carries the canonical financial base labels **verbatim** (else silent 0-seed); operational headers ALL-CAPS, drivers mixed-case.
- [ ] Build path and coverage **tier** declared honestly in card §5/§7; if Tier B, the gap to Tier A is named.
- [ ] (Tier A) `build_model_<slug>.py` exposes the row-handle ABI, wires IS/BS/CF/Schedules/Valuation, keeps the **balance check = 0** every column; added to `BUILDERS`; dispatch/auto-routing wired or its manual status noted.
- [ ] Synthetic input workbook (column-B labels ⊇ `required_labels(slug)`) + a test proving no KeyError.
- [ ] `tests/test_canonical_schema.py` passes; harness runs end-to-end and the balance check is 0 in every column.

---

### Engine reference (where each rule lives)

- Build-path gate: `engine/build_model.py:533` · Stage-3 hole comment: `:531-532`
- O&G bottom-up seeds/build: `build_model.py:556-586,675-745` · generic top-down: `:587-615,747-792`
- Label readers (silent-0 fallback): `build_model.py:545-554` · IS COGS branch (row-handle ABI): `:892-899`
- `Line`/`add_line`/`fill` (period kinds): `:172-216` · fonts/formats: `:29-43` · `prem()` P/Praw: `:259-264` · `seed_premises`: `:220-256` · `corkscrew`: `:798-818` · interest-on-BOP: `:826-856` · tax/revolver MIN-MAX: `:924,1060-1063` · balance check: `:1157-1162`
- Operational introspection (ALL-CAPS headers): `template_loader.py:122-127` · per-asset scan (O&G-only): `:130-152` · asset headers/constants: `:39-43` · `SECTOR_SIGNALS`/`identify_sector`: `:48-51,102-110` · `locate_card`: `:113-117`
- Canonical schema (base + delta + slugs + normalize): `engine/canonical_schema.py`
- Coverage gate / tiers / `BUILDERS`: `engine/sector_coverage.py`
- Card excerpt retrieval: `engine/sector_knowledge.py:61-86`
- Provenance invariant: `engine/assumptions.py` (`approve()`), `engine/proposals.py`
- Role classifier (STATEMENT / OPERATIONAL_RAW / REPORTED_CHECK / STRUCTURAL): `engine/role_classifier.py`
- Schedules + common premises: `templates/base.yaml`
- Exemplar deltas: `templates/sectors/oil_and_gas.delta.yaml`, `templates/sectors/telecom.delta.yaml`
- Separate-engine precedent: `engine/build_model_telecom.py`
- Contract guard: `tests/test_canonical_schema.py`
- Card contract (do not duplicate): [`_schema.md`](_schema.md) · sources registry: [`_sources.md`](_sources.md)

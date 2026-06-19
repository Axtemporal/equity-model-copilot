# Calibration Notes and Knowledge Map

**Date:** June 10, 2026
**Inputs:** 4 market models (`Example models` folder) + licensed training library (`Knowledge Base` folder)
**Purpose:** engineering reference for the Python engine and for the AI assumption layer

---

## 1. What each reference model teaches

### Model A (mining, multi-asset) ⭐ primary reference for structure and aesthetics (user's declared preference)

- **Per-asset granularity:** one tab per mine plus a Corporate tab, consolidating into the Model tab and breaking out valuation as SOTP. This is the design to emulate whenever a company discloses results by asset.
- **Asset-tab pattern:** header with the relevant macro linked from `Macro Assumptions` (FX, inflation for the countries where the mine operates), then a summarized P&L for the asset (Net Revenues down to Net Income with local formulas), then detailed operational sections (production, costs) feeding the summary bottom-up.
- **Centralized macro:** a single `Macro Assumptions` tab (years 2018A onward), referenced by every other tab. Validates the concept of shared macro assumptions.
- **Sign convention 1:** revenues positive, costs negative, subtotals via plain SUM, labels prefixed `(=)`, `(-)`, `(+)`.
- **Colors:** blue hardcode, black formula, green link between tabs (the classic convention used in full).
- **Explicit units** in a dedicated column next to the label (USD mn, USD th, %).

### Model B (telecom, international sell-side) — reference for the Input → Operational → Statements architecture

- Exactly the flow this project wants: an `Inputs` tab with raw data as published (operational KPIs + revenue breakdown), an `OPERATIONAL` tab deriving calculated KPIs (net adds, ARPU, market share, QoQ) pulled from Inputs, and `IS`/`BS`/`CF` tabs that are 100% formula (zero hardcode in the IS), with separate `CAPEX` and `DEBT` schedules and dedicated `VALUATION` and `MACRO` tabs.
- Even the IS line labels are formulas (`=Inputs!A33`), guaranteeing naming consistency.
- Quarterly columns with a year row above (1Q13, 2Q13... grouped by year).

### Model C (telecom) — reference for a compact single-tab model

- A single `Full Model` tab: Macro block at the top, IS with driver lines interleaved (% YoY, % of net revenue, % of handset revenue), revenue built bottom-up by segment in sections further down (the line above references the detail section).
- Demonstrates the driver-below-the-line style that makes assumptions easy to read in context.

### Model D (telecom) — declared anti-reference by the user

- Heavy structure: a 752-row `Input` tab, tabs extending to 16 thousand columns (Input, Model, Time), a dense Control Panel with price objective and IRRs. Functional, but opaque and hard to audit. (Note: dynamic lookups such as INDEX/MATCH in place of direct links, seen in Model B, also go on the avoid list, even though that model gets the tab architecture right.)

## 2. Declared product preferences (June 10, 2026)

- **Aesthetics and clarity:** follow the Model A standard. Avoid the Model D style.
- **Columns:** quarters and years together on the same tab, interleaved: `1Q22, 2Q22, 3Q22, 4Q22, 2022, 1Q23...`. The year closes out the block of four quarters. (Engineering note: the generator must treat the annual column as a SUM/aggregation of the 4 quarters to its left, and line formulas must be aware of the column type.)
- **Model history always linked to the input tab**, never typed into the model tab.
- **The 3 statements automatically interlinked** by the engine: NI → retained earnings, D&A and capex → PP&E roll-forward, CF as a pure balance sheet reconciliation, cash and revolver as plugs, balance check in every column.

## 3. Distilled from the licensed training library (what becomes engine rules)

### Construction rules (from the best-practices guide)

1. Colors: blue input, black formula, green link between tabs, red external link. Generous comments citing the source on every assumption and hardcode.
2. Sign convention 1 (income +, expense −), same as Model A. Decision adopted.
3. Never embed a constant inside a formula (no partial inputs). Every assumption in its own cell.
4. One row, one consistent calculation from left to right. History on the left, projections on the right.
5. Schedules as roll-forwards (corkscrew): beginning balance + flows = ending balance, for PP&E, debt, equity, working capital.
6. No calculations on the balance sheet: the balance sheet only receives links from schedules.
7. Simple formulas; avoid nested IFs (use MIN/MAX/boolean flags); avoid named ranges; avoid referencing multiple tabs inside a single formula (import the line first, as Model A does with macro).
8. Circularity: avoid by default by charging interest on the beginning debt balance; if average balance is used, require iterative calculation plus a documented circuit breaker. For the MVP: beginning balance, no circularity.
9. No macros (except for printing). No hidden rows (use grouping instead).
10. Error checks aggregated in a panel: balance check, sum of quarters = year, depreciation ≤ PP&E, debt amortization ≤ outstanding balance. Direct calculation rather than plugs wherever possible (except the canonical plugs, cash/revolver).
11. Cover page with company, purpose, currency, units and date; company name at the top of every tab; tabs flowing left to right.

### Per-line projection methods (becomes the AI layer's "method card" library)

**Income statement (from the income statement guide):**

| Line | Default method | Override/alternative |
|---|---|---|
| Revenue | aggregate % growth | price × volume by segment (preferred when operational data exists; the case for our pilots) |
| COGS | % of revenue (gross margin) | unit cost × volume when operational data is available |
| SG&A and other opex | % of revenue, straight-line margin | explicit margin-change thesis (news, guidance) |
| D&A | from the PP&E roll-forward (schedule), never directly on the income statement | % of historical capex |
| SBC | % of revenue | straight-line |
| Net financial result | rate × beginning debt/cash balance (no circularity) | rate × average balance (requires circuit breaker) |
| Other non-operating items | straight-line | zero if non-recurring |
| Income tax (IR/CSLL) | prior year's effective rate | marginal rate with adjustments (tax-loss carryforwards, JCP) |
| Shares and EPS | constant share count | buyback/issuance schedule |

**Balance sheet (from the balance sheet projections guide):**

| Line | Default method | Override |
|---|---|---|
| Accounts receivable | grows with revenue | explicit DSO |
| Inventories | grow with COGS | inventory turnover |
| Prepaid expenses | grow with SG&A (or revenue) | straight-line |
| Other current assets | grow with revenue | straight-line if non-operating |
| Accounts payable | grows with COGS | days payable outstanding (DPO) |
| Provisions/accruals | grow with SG&A | straight-line |
| Deferred revenue | grows with revenue | specific thesis |
| Taxes payable | grow with income tax expense | straight-line |
| PP&E | roll-forward: BOP + capex − depreciation − disposals | depreciation waterfall |
| Intangibles | roll-forward with purchases and amortization | no new purchases if history is immaterial |
| Goodwill | straight-line (no projected impairment) | |
| Deferred taxes | grow with revenue | straight-line |
| Other non-current items | straight-line | |
| LT debt | constant, or growing with NI (refinancing, not contractual amortization) | contractual schedule if the thesis is deleveraging |
| Common stock/APIC | constant + SBC | issuance schedule |
| Treasury stock | straight-line of historical buybacks | guidance |
| Retained earnings | roll-forward: BOP + NI − dividends (historical payout) | stated dividend policy |
| OCI | straight-line | |
| Cash and revolver | model plugs | |

**Cash flow:** pure reconciliation — every line referenced from elsewhere in the model, nothing typed in. The balance sheet debugging routine (checking the cash impact line by line) becomes part of the generator's QA checklist.

### Dynamic schedules: working capital, leases (IFRS-16), debt and revolver (distilled June 15, 2026)

Replaces the engine's current static treatment (WC change hardcoded `=0`; debt, leases and financial result frozen flat). All four reference models (A–D) independently converge on the same working-capital and interest mechanics, which is what validates them as market standard.

**Working capital — days-driven (all of Models A–D).**
- Receivables = `DSO × Revenue / days_in_period`; Inventories = `inventory_days × cost_base / days_in_period`; Payables = `DPO × cost_base / days_in_period`.
- `cost_base` = COGS (for commodity producers, the lifting/production cost; Model A uses COGS gross of D&A).
- Each days premise is seeded by **inverting the reported historical balance** (`DSO_hist = AR/Revenue × days`), set once then drifted/held flat — every premise in its own cell.
- **Critical mechanic (all models):** the cash-flow "change in working capital" line is computed from the period-over-period deltas of the balance-sheet WC lines, **not** from the schedule subtotal. This keeps the CF tied to the BS and makes the balance check self-enforcing (it fixes the tautological close).
- Sector variation: telecom splits payables into suppliers / taxes payable / labour / other, each with its own days premise (B, C, D); O&G/mining uses the AR/Inv/AP triad (A). Quarterly base may be an LTM (trailing-4Q) sum (C).

**Leases (IFRS-16) — full treatment only in Model C; D shows the reporting layout; A/B are partial (the gap to close).**
- Twin roll-forwards linked by one additions driver: Right-of-use asset `EOP = BOP + additions − depreciation` (additions = % of revenue/capex); Lease liability `EOP = BOP + additions − principal repayment` (same additions figure).
- Lease interest: **primary = `discount_rate × lease_liability_BOP`; fallback = `% of revenue`** when the rate is not disclosed/derivable (flag per company; the method used is recorded in the Assumptions log).
- P&L: lease depreciation → D&A; lease interest → financial result (separate line). Report both **EBITDA** and **EBITDA-AL = EBITDA − lease depreciation − lease interest**. Split lease liability EOP into current/non-current by a % premise.
- EV→equity bridge convention is decided at **v2 (the Valuation tab)**: the closed decision states both "leases count as debt in the bridge" and "FCFF deducts lease payments" — applying both double-counts, so one convention must be picked (the after-lease view — FCFF deducts payments, net debt ex-lease — is the coherent default). The three-statement roll-forward built now is identical either way.

**Debt — all models use interest on the opening balance (no circularity); none builds a real tranche schedule.**
- Roll-forward `Debt EOP = BOP + draws − repayments`, split ST/LT. Interest = `rate × debt_BOP` (strictly opening; if a non-zero issuance plug is active, reference BOP explicitly, not EOP, to stay non-circular).
- MVP: a single indexer + spread per debt block (e.g. spread over CDI/Selic), **structured to accept per-tranche decomposition later** (backlog item 6: weighted-average Kd → WACC by formula). FX: separate BRL vs foreign-currency debt, revalue the foreign portion at period-end FX, isolate the non-cash FX revaluation so the CF adds it back (B). Seed the forward cost-of-debt premise from the historical implied rate (`interest / prior balance`). Optional: gate interest accrual on an activity flag (`IF production/revenue > 0`) for depleting resource assets (A).

**Revolver / cash sweep — simple, non-circular (our improvement; no reference model demonstrates it — all let cash go negative).** Per spec "cash/revolver as plugs" and backlog item 2.
- Minimum-cash premise. `cash_available = Cash_BOP + CFO + CFI + CFF(ex-revolver)`. Draw = `MAX(0, minimum − cash_available)`; Sweep = `MIN(revolver_BOP, MAX(0, cash_available − minimum))`. Revolver `EOP = BOP + draw − sweep`; revolver interest = `rate × revolver_BOP` (opening → no circularity). All via MIN/MAX, no nested IF.
- Reading: the revolver balance is a **financing-need signal** — a growing revolver flags that the modeled plan does not self-fund. It is an estimate (assumes credit available at the modeled rate), logged with method, never reported data.

**ARO / decommissioning — O&G-specific (built into the O&G engine; an optional schedule for other sectors).**
- Roll-forward of the asset-retirement obligation: `ARO EOP = BOP + new ARO (capitalized into PP&E) + accretion − settlements`. Accretion = `discount_rate × ARO_BOP`, charged through the financial result (the unwinding of the discount). On initial recognition the ARO is capitalized into PP&E (asset side) and booked as a provision (liability side); it is settled in cash only at end of field life. Acquiring a field means assuming its ARO. The discount rate is a labeled premise.

### Data-gathering process (PIB guide, adapted to Brazil)

A Brazilian Public Information Book per company: earnings release + IR results center, ITR/DFP and FRE filings with the CVM, call transcript, institutional presentation, guidance, news from the last 6 months, consensus when available. Becomes the checklist for the manual input phase and for the AI's searches.

### Course manuals (future reference)

- `Financial-Statement-Modeling-Course-Manual` (155 pp., complete Apple case study): detail reference for when the three-statement engine is under construction.
- `DCF_Modeling` (157 pp.): theoretical foundation for v2 (valuation). Covers equity vs. enterprise value, WACC, perpetuity.
- Banking kit (webinar + Bank_BS_IS spreadsheets): hold for when the banking sector enters the roadmap.
- Shipping/maritime materials: example of sector-specific operational modeling (vessel depreciation, charter revenue), inspiration for a sector template.

## 4. Copyright (repository rule)

The training library is paid and licensed, and the example models are proprietary to the firms that produced them. **None of it may go into the public repository.** Rules:

1. `Example models/` and `Knowledge Base/` go into `.gitignore` from the very first commit.
2. The distilled knowledge (this document, method cards, engine rules) is a paraphrase of standard market methods and may be published.
3. Never reproduce literal text, screenshots, or structure from these materials in the repo.

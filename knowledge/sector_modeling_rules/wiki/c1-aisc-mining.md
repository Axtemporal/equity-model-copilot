---
concept: c1-aisc-mining
title: C1 Cash Cost & AISC
theme: sector-kpi
applies_to: [metals_mining]
confidence: seed
status: draft
---

# C1 Cash Cost & AISC

**What it is.** The mining cost stack used to judge competitiveness and survival —
**C1 cash cost** (direct per-tonne operating cost), **AISC** (all-in sustaining cost,
adding sustaining capex and overheads), and the asset's **position on the global cost
curve** — together with **grade/teor** and **strip ratio** as the physical drivers
underneath, plus **provisional pricing** on the revenue side.

## Core idea

A miner is a price-taker on its output, so what decides survival through the cycle is
**where its assets sit on the global cost curve**. The cost metrics make that explicit:

- **C1 cash cost (US$/t)** — direct cash cost of production (mining, processing, site
  G&A), the headline operating-cost metric. 🟡 (definition standard; not source-verified)
- **AISC (all-in sustaining cost)** ✅ — a non-GAAP metric (defined by the World Gold
  Council and applied across mining) that **adds to cash operating cost**: **sustaining
  capital expenditure, corporate G&A, share-based remuneration, and reclamation/inventory
  adjustments**, with **by-product/co-product revenues credited against operating cost**.
  It **excludes** non-sustaining (growth/major-project) capital, impairments, one-time
  severance, M&A costs, and financing/interest. It separates the cost of *maintaining*
  production from *growth* spending.
- **Cost-curve position** — rank against global supply; low-cost assets survive the
  trough that shuts high-cost ones. 🟡

Physical drivers feed the cost: **grade/teor** (e.g. % Fe) drives both the price premium
and processing economics, and the **strip ratio** (waste : ore) drives mining cost. 🟡

## Applies to sectors

- **Metals & mining** — directly; the cost stack is the margin driver beneath the
  reserve-bounded production schedule ([[reserve-based-nav]]).
- Pairs with **steel** as the downstream customer (iron ore) — see the realized-price
  logic in that card.

## Mechanics / formulas

- `Cash margin/t = realized price/t − C1 cash cost/t`; `all-in margin/t = realized
  price/t − AISC/t`.
- **AISC** = cash operating cost + sustaining capex + corporate G&A + share-based
  remuneration + reclamation/inventory adjustments − by-product credits. ✅
- Realized price = reference index (e.g. 62% Fe Platts/MB for iron ore; LME for
  copper/nickel) **± grade premium/penalty**. 🟡
- **Provisional pricing** ✅ — many iron-ore and copper sales are invoiced at a
  **provisional price at delivery**, then the receivable is **re-measured at fair value
  through profit or loss** (the price-adjustment feature is an **embedded derivative**)
  until the **contractual pricing period** — generally **later than the shipment/
  revenue-recognition date** — sets the final price; the mark-to-market changes are
  booked into **sales revenue**. This is the precise true-up mechanic to model.

## Modeling implications

- Build a **C1 / AISC cost block per asset**, with grade and strip ratio as inputs;
  separate **sustaining vs growth capex** so AISC isn't polluted by expansion projects.
- Add a **provisional-pricing true-up line** on revenue, carrying the open receivable at
  fair value until the pricing period closes — expect revenue volatility from price moves
  between shipment and final pricing.
- Normalize cost-curve position through the cycle ([[mid-cycle-normalization]]) rather
  than capitalizing a trough or peak.

## Pitfalls & nuances

- **Do NOT blend growth capex into AISC** — AISC is sustaining only; non-sustaining
  project capital, impairments, M&A and financing are excluded by definition.
- **Do NOT ignore provisional-pricing true-ups** — they move reported revenue between
  the shipment date and the later pricing date (embedded-derivative re-measurement).
- **Do NOT ignore CFEM** ([[cfem-royalty]]) — model it between gross and net revenue.
- 🟡 **Still to verify (round 4):** the **C1** definition specifically, grade/strip
  economics, and the cost-curve framing were not reached before the session limit — only
  **AISC** and **provisional pricing** were 3-0 verified this round.

## Related concepts

- [[jorc-resources-and-reserves]] — the reserve base the cost stack mines
- [[reserve-based-nav]] — the per-asset valuation the cost feeds
- [[cfem-royalty]] — the Brazilian mining royalty in the cost/revenue stack
- [[mid-cycle-normalization]] — normalizing cost-curve position through the cycle

## Provenance
- Method cards: [[metals_mining]]
- Sources: [WGC-AISC — World Gold Council, All-in costs / AISC definition](https://www.gold.org/about-gold/gold-supply/responsible-gold/all-in-costs) (AISC inclusions/exclusions, 3-0); [VALE-20F-2022 — Vale Form 20-F 2022 (SEC)](https://www.sec.gov/Archives/edgar/data/0000917851/000129281423001516/valeform20f_2022.htm) (provisional pricing as embedded derivative at FVTPL into sales revenue, 3-0); [XP-METALS-2025 — XP Investimentos, Metals & Mining Brazil outlook (Oct 2025)] for the BR realized-price framing
- Confidence: 🟡 seed overall — **AISC ✅ (3-0)** and **provisional pricing ✅ (3-0)** verified round 3; C1 / grade / strip / cost-curve remain round-4 gaps (not reached before session limit).

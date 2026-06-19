---
concept: inventory-effect-fuel
title: The Inventory Effect (cost-flow lag)
theme: driver-pattern
applies_to: [fuel_distribution]
confidence: verified
status: draft
---

# The Inventory Effect (cost-flow lag)

**What it is.** In a fuel distributor, weighted-average-cost inventory accounting makes
**COGS lag spot fuel prices**, so when prices move the reported margin picks up a
non-cash **holding gain (rising prices) or loss (falling prices)** — the "inventory
effect" — which materially distorts reported net income and must be stripped to read a
**recurring margin**.

## Core idea

Under [[ias-2-inventory-costing]], fuel is carried at weighted-average cost. The COGS
booked against a sale reflects the **average of past purchase costs**, not today's spot.
So:

- **Spot rises** → COGS understates replacement cost → reported margin **overstated** by
  a holding gain.
- **Spot falls** → COGS overstates replacement cost → reported margin **understated** by
  a holding loss.

This is **non-recurring** and **non-cash in substance** (it reverses as inventory turns),
yet it lands squarely in reported net income. In Brazil it is driven largely by **import
parity opening/closing** — when domestic prices diverge from import-parity, the gap feeds
through the inventory position.

## Applies to sectors

- **Fuel distribution** — the canonical case; the effect can swing reported net income by
  a large fraction quarter to quarter.
- The same cost-flow-lag mechanism exists in **petrochemicals** and **steel** (average-
  cost inventory), but it is most material — and most explicitly disclosed — in fuel
  distribution.

## Mechanics / formulas

- `Reported margin = recurring margin + inventory effect (+ asset/tax gains)`
- `Recurring margin` strips (i) the inventory effect and (ii) one-off asset-sale / tax
  gains.
- The inventory effect ≈ `(average cost − replacement/spot cost) × volume sold` over the
  period, with sign following the price move.

## Modeling implications

- Present **both** a reported and a **recurring (ex-inventory-effect, ex-asset/tax-gain)
  margin** — the copilot should default to this split for any fuel distributor.
- Model the inventory-effect line **tied to fuel-price/parity moves**, feeding both margin
  and net income, and flag it **explicitly non-recurring**; reverse it in the cash-flow
  reconciliation.
- Pair with a **price-aware working-capital schedule** — a deliberate inventory build
  consumes cash that reverses next quarter (~45-day normalization), not a flat % of
  revenue.

## Pitfalls & nuances

- **Do NOT treat the inventory effect as recurring margin** — strip it (and asset/tax
  gains).
- **REFUTED — do NOT confuse this with an IAS 2 lower-of-cost-and-NRV writedown** (3-0
  refuted). LCNRV only bites when selling price falls **below** cost; the recurring
  inventory gain/loss is the **weighted-average cost-flow lag**, a separate mechanism. See
  [[ias-2-inventory-costing]].
- **Do NOT model working capital as a flat % of revenue** — it is inventory-positioning
  and price-driven, mean-reverting within ~a quarter.

## Related concepts

- [[ias-2-inventory-costing]] — the accounting mechanism (cost-flow lag vs LCNRV)
- [[r-per-m3-fuel]] — why profitability is measured per m³, recurring vs reported
- [[spread-based-revenue]] — the distributor's underlying margin logic
- [[mid-cycle-normalization]] — normalizing through commodity-price swings

## Provenance
- Method cards: [[fuel_distribution]]
- Sources: [VIBRA-2Q25 — Vibra Energia 2Q25 conference call transcript (Aug 2025)](https://api.mziq.com); [IAS-2 (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/)
- Confidence: ✅ verified (round 2, 3-0). Figures point-in-time; encode method only.

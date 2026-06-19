---
concept: ias-2-inventory-costing
title: IAS 2 — Inventory Costing
theme: accounting-standard
applies_to: [fuel_distribution, petrochemicals, steel, agri_inputs]
confidence: verified
status: draft
---

# IAS 2 — Inventory Costing

**What it is.** IAS 2 permits only **FIFO or weighted-average cost** for inventory (LIFO
is prohibited), which means that when input prices move, the **average cost recorded in
COGS lags the spot price** — producing non-cash holding gains and losses in reported
margin — and it keeps the separate **lower-of-cost-and-net-realizable-value (LCNRV)**
writedown as a distinct mechanism that only bites when selling price falls below cost.

## Core idea

Two mechanisms live inside IAS 2 and are routinely confused:

1. **Cost-flow lag (weighted-average cost).** Because inventory is carried at a rolling
   weighted-average cost, the COGS recognized this period reflects an average of past
   purchase costs, not today's spot. When spot rises, COGS understates replacement cost
   → a **holding gain**; when spot falls, COGS overstates it → a **holding loss**. This
   is the recurring "inventory effect" in price-volatile commodity businesses. See
   [[inventory-effect-fuel]].
2. **LCNRV writedown.** Separately, inventory must be written down when its net
   realizable value (expected selling price − costs to complete/sell) falls **below**
   carrying cost. This only triggers in a genuine loss situation (selling below cost),
   not on every price move.

LIFO is banned under IFRS, so the US-GAAP "LIFO reserve" framing does not apply.

## Applies to sectors

- **Fuel distribution** — the canonical case: weighted-average cost makes COGS lag spot
  fuel prices, and the inventory effect materially distorts net income. See
  [[inventory-effect-fuel]] and [[r-per-m3-fuel]].
- **Petrochemicals** — average-cost inventory can create price-driven gains/losses that
  distort a single quarter's spread.
- **Steel** — raw-material (iron ore, coking coal, scrap) and finished-steel inventory at
  average cost create timing effects in COGS.
- **Agri-inputs** — input and grain inventory at cost; grain taken as barter introduces
  commodity-price exposure on the balance sheet.

## Mechanics / formulas

- Weighted-average cost: `unit cost = total cost of goods available ÷ units available`,
  re-struck as new purchases arrive; COGS uses this rolling average, not spot.
- LCNRV: `carrying value = min(cost, net realizable value)`; the writedown is recognized
  only when NRV < cost.

## Modeling implications

- For price-volatile inventory, model a **recurring margin** that strips the cost-flow-lag
  inventory effect, alongside the reported margin — the copilot should present both.
- Treat the inventory effect as **explicitly non-recurring** and reverse it in the
  cash-flow reconciliation.
- Do not build an LCNRV writedown into the recurring inventory-effect line — model it
  only in a genuine sub-cost scenario.

## Pitfalls & nuances

- **REFUTED — do NOT encode:** attributing recurring fuel-distribution inventory
  gains/losses to the **LCNRV writedown**. That failed verification (3-0). The recurring
  effect is the **weighted-average cost-flow lag**; LCNRV is a separate mechanism that
  only applies below cost. Keep the two distinct.
- Do not import a US-GAAP LIFO framing — LIFO is prohibited under IAS 2.

## Related concepts

- [[inventory-effect-fuel]] — the cost-flow lag in the fuel sector, in depth
- [[r-per-m3-fuel]] — why the effect must be stripped to read fuel profitability
- [[ias-41-biological-assets]] — where harvested produce hands off into IAS 2 at deemed cost
- [[mid-cycle-normalization]] — the cyclical-price problem behind inventory swings

## Provenance
- Method cards: [[fuel_distribution]], [[petrochemicals]], [[steel]], [[agri_inputs]]
- Sources: [IAS-2 — Inventories (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/); [VIBRA-2Q25 — Vibra Energia 2Q25 conference call transcript (Aug 2025)](https://api.mziq.com)
- Confidence: ✅ verified (round 2, 3-0; LCNRV-vs-cost-flow-lag distinction 3-0 refuted)

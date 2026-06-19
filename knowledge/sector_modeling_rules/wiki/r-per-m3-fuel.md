---
concept: r-per-m3-fuel
title: R$/m³ — Fuel Distribution Profitability
theme: sector-kpi
applies_to: [fuel_distribution]
confidence: verified
status: draft
---

# R$/m³ — Fuel Distribution Profitability

**What it is.** A fuel distributor's profitability is measured as **margin per cubic
metre (R$/m³)** — gross profit (or EBITDA) divided by volume — **not** as a percentage of
revenue, because revenue is dominated by pass-through fuel cost that makes percentage
margins meaningless; and it is reported **recurring vs reported** to strip the inventory
effect and one-off gains.

## Core idea

A distributor buys fuel and resells it at a thin spread over a huge, volatile,
pass-through cost. Revenue therefore swings with fuel prices independently of how the
business is actually doing, and a "% gross margin on revenue" is noise. The meaningful
unit is **per cubic metre sold**:

`Margin per m³ = gross profit (or EBITDA) ÷ volume (m³)`

modeled **by product** (gasoline, diesel S10/S500, hydrous/anhydrous ethanol, jet fuel/
QAV). And because the [[inventory-effect-fuel]] cost-flow lag plus one-off asset/tax gains
distort the reported figure, the distributor reports a **recurring margin** beside the
reported one.

## Applies to sectors

- **Fuel distribution** — directly; the headline KPI.
- The "measure per physical unit, not % of pass-through revenue" principle echoes the
  spread logic in [[spread-based-revenue]].

## Mechanics / formulas

- `Gross profit ≈ volume (m³) × margin per m³`, by product and channel (retail network
  vs B2B/TRR/aviation).
- `Recurring margin = reported margin − inventory effect − asset/tax gains` (see
  [[inventory-effect-fuel]]).

## Modeling implications

- **Drive gross profit off volume × R$/m³ by product**; carry revenue as a large
  low-signal pass-through line.
- Show a **recurring-margin line (ex-inventory-effect, ex-asset/tax gains)** beside
  reported — the copilot defaults to this.
- Volume = total fuel demand (GDP/fleet-linked) × **market share**; posto count and
  same-store throughput; B2B vs retail split.

## Pitfalls & nuances

- **Do NOT use % gross margin on revenue** — the pass-through makes it meaningless; use
  R$/m³.
- **Do NOT treat the inventory effect as recurring margin** — strip it (and asset/tax
  gains).
- ⚠️ Margin-per-m³ benchmarks per product and per peer (Raízen, Ultrapar) are a round-3
  gap — round-2 evidence is Vibra-centric.

## Related concepts

- [[inventory-effect-fuel]] — the distortion stripped to get the recurring margin
- [[ias-2-inventory-costing]] — the accounting behind the inventory effect
- [[spread-based-revenue]] — the per-physical-unit margin logic
- [[ebitda-al-ifrs16]] — lease-adjusted profitability for the station/terminal base

## Provenance
- Method cards: [[fuel_distribution]]
- Sources: [VIBRA-2Q25 — Vibra Energia 2Q25 conference call transcript (Aug 2025)](https://api.mziq.com)
- Confidence: ✅ verified (round 2, 3-0). Figures point-in-time; encode method only.

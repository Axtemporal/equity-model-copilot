---
concept: spread-based-revenue
title: Spread-Based Revenue Modeling
theme: driver-pattern
applies_to: [petrochemicals, fuel_distribution]
confidence: verified
status: draft
---

# Spread-Based Revenue Modeling

**What it is.** For processors and converters whose economics hinge on the gap between
an output price and an input cost, the revenue/margin build replaces the generic
"price × volume" with **spread × volume**, where **spread = product price − feedstock
cost**, defined **per production route** and multiplied by **capacity × utilization**.

## Core idea

A petrochemical cracker or a fuel distributor does not control its absolute output price
— both ends move with commodity markets. What it earns is the **spread** between them.
Modeling the output price alone (or worse, a percentage margin on a huge pass-through
revenue) misses the actual driver and produces nonsense margins when both ends move
together.

So the build becomes:

- **Spread (US$/t or R$/m³)** = product price − feedstock cost, defined **per route /
  product**, because different feedstocks give structurally different spreads.
- **Volume** = **capacity × utilization (operating) rate** per product per site.
- **EBITDA** = spread × volume, summed across routes/products.

## Applies to sectors

- **Petrochemicals** — the textbook case. Spreads are defined per production route:
  - **PE-Naphtha** (Brazil — naphtha-fed polyethylene)
  - **PE-Ethane** (Mexico — ethane-fed; the most cost-competitive feedstock)
  - **PP-Propylene** (US / Europe)
  The spread **replaces the price** component; volume remains capacity × utilization.
- **Fuel distribution** — a spread-like logic at the distributor level: profitability is
  the **margin per cubic metre (R$/m³)**, not a % of pass-through revenue. See
  [[r-per-m3-fuel]] and [[inventory-effect-fuel]].

## Mechanics / formulas

- `Spread_route = product price_route − feedstock cost_route`
- `Volume_product = capacity_product × utilization rate`
- `EBITDA ≈ Σ_routes (Spread_route × Volume_route) − fixed cost`
- Integrated producers need **multi-feedstock / multi-product** spreads (see below);
  non-integrated units collapse to a **single input-to-output spread**.

## Modeling implications

- **Adapt to the integration level** (a textbook "self-adapting granularity" case):
  - **Non-integrated unit** → model one input-to-output spread (e.g. USA PP − Propylene).
  - **Integrated unit** (Braskem Brazil) → multi-feedstock/multi-product, because a large
    share of revenue is non-resin by-products and ethylene is largely naphtha-based; one
    spread line cannot capture it.
- Model **capacity per product per site (kty)**; the template collapses to the grain the
  issuer discloses.
- Value on **normalized mid-cycle spreads** ([[mid-cycle-normalization]]), not spot.

## Pitfalls & nuances

- **Do NOT use a single product price** — use the route spread (price − feedstock).
- **Do NOT collapse an integrated producer to one spread** — by-products and mixed
  feedstock require multi-product structure.
- **Do NOT value on spot/near-term spread** at a cycle peak or trough — normalize.
- **Do NOT hardcode a bank's dated spread deck** — encode the method; spreads drift.

## Related concepts

- [[mid-cycle-normalization]] — valuing the cyclical spread on a through-cycle basis
- [[inventory-effect-fuel]] — the cost-flow lag that distorts a single period's spread
- [[r-per-m3-fuel]] — the fuel-distribution analogue of a spread metric
- [[ias-2-inventory-costing]] — why average-cost inventory adds spread noise

## Provenance
- Method cards: [[petrochemicals]], [[fuel_distribution]]
- Sources: [XP-PETCHEM-2023 — XP Investimentos, Petrochemicals initiation (Sep 2023)]; [IBIQ-CRACKER — ethylene cracker economics](https://ibinterviewquestions.com/guides/energy-investment-banking/petrochemicals-ethylene-cracker-economics-ethane)
- Confidence: ✅ verified (3-0 / 2-0). Numbers point-in-time; encode method only.

---
concept: mid-cycle-normalization
title: Mid-Cycle / Normalized Earnings
theme: driver-pattern
applies_to: [petrochemicals, steel, metals_mining, pulp_paper]
confidence: verified
status: draft
---

# Mid-Cycle / Normalized Earnings

**What it is.** Deeply cyclical commodity processors are valued on **normalized
mid-cycle earnings** — margins/spreads set at a through-cycle average in a **separate
assumption block**, not on spot or trough/peak figures — because a snapshot at any one
point in the cycle systematically mis-states through-cycle earning power.

## Core idea

A petrochemical, steel, mining or pulp business earns a margin that swings violently with
the commodity cycle. Valuing it on the **current** spread is a trap:

- Near a **trough**, spot EBITDA is depressed; near-term multiples look expensive and the
  business looks worse than it is.
- Near a **peak**, spot EBITDA is inflated; multiples look cheap and the business looks
  better than it is.

The discipline is to value on **normalized mid-cycle margins/spreads** — a through-cycle
average, ideally in **real (CPI-adjusted)** terms — held in a **separate mid-cycle
assumption block** distinct from the near-term forecast. The explicit forecast carries
the next few years; the **terminal/normalized value** uses mid-cycle economics.

## Applies to sectors

- **Petrochemicals** — value on EV / normalized EBITDA at real mid-cycle spreads (see
  [[spread-based-revenue]]).
- **Steel** — normalize realized price (index + premium) and the metallic spread through
  the cycle.
- **Metals & mining** — normalize commodity price and cost-curve position
  ([[c1-aisc-mining]]) rather than capitalizing a peak.
- **Pulp & paper** — normalize the China CIF pulp price × FX through the cycle.

## Mechanics / formulas

- `Normalized EBITDA = mid-cycle spread/margin × normalized volume (capacity × through-
  cycle utilization)`.
- Valuation: apply a through-cycle multiple to normalized EBITDA, or use normalized
  margins in the DCF terminal year; keep mid-cycle assumptions in their own block so they
  are auditable and toggleable.

## Modeling implications

- Build a **separate mid-cycle block** (real mid-cycle spreads/prices, normalized
  utilization) feeding the terminal value, distinct from the spot-anchored near-term
  forecast.
- Pair with **EBITDA-AL** ([[ebitda-al-ifrs16]]) for lease consistency.
- The copilot should never propose a valuation off a single trough/peak quarter for these
  sectors.

## Pitfalls & nuances

- **Do NOT value on spot/near-term EBITDA** at a cycle extreme — normalize.
- **Do NOT hardcode a bank's dated spread/price deck or exit multiple** — encode the
  normalization method; the numbers drift.
- Distinguish a **cyclical** swing (normalize through it) from a **structural** shift
  (re-base the mid-cycle) — getting this wrong over- or under-normalizes.

## Related concepts

- [[spread-based-revenue]] — the spread that gets normalized (petchem/fuel)
- [[c1-aisc-mining]] — cost-curve position normalized through the cycle
- [[ebitda-al-ifrs16]] — the lease-consistent profitability metric to normalize
- [[inventory-effect-fuel]] — the related single-period distortion from price swings

## Provenance
- Method cards: [[petrochemicals]], [[steel]], [[metals_mining]], [[pulp_paper]]
- Sources: [XP-PETCHEM-2023 — XP Investimentos, Petrochemicals initiation (Sep 2023)]; corroborated by Damodaran, *Valuing Cyclical and Commodity Companies*
- Confidence: ✅ verified (2-0). Numbers point-in-time; encode method only.

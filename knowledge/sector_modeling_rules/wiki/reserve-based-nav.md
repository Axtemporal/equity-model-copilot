---
concept: reserve-based-nav
title: Reserve-Based NAV / DCF
theme: driver-pattern
applies_to: [oil_and_gas, metals_mining]
confidence: seed
status: draft
---

# Reserve-Based NAV / DCF

**What it is.** For extractive companies, value is built **per asset** as the risked,
discounted cash flow of a **production schedule bounded by certified reserves** — a
sum-of-the-parts net asset value (NAV) whose terminal point is **asset exhaustion**, not
a perpetuity-growth tail — with a consolidated FCFF DCF kept as a cross-check.

## Core idea

An E&P company or a miner cannot be valued on a Gordon-growth perpetuity, because its
output is **finite**: barrels and tonnes run out. The native method is a **NAV / SOTP**:

1. For **each field/mine**, run a reserve roll-forward (opening − production ± revisions
   ± acquisitions = closing) that caps cumulative production at recoverable reserves.
2. Drive a **production/decline curve** off that reserve base.
3. Price output at a realized price (benchmark ± differential/premium) net of per-unit
   cost ([[c1-aisc-mining]] for mining; netback/lifting cost for O&G).
4. Discount each asset's cash-flow profile; **terminal value = exhaustion + retirement
   obligation (ARO)**, not a growing perpetuity.
5. **Sum the parts**, risk contingent/prospective barrels down or out, and bridge to
   equity.

## Applies to sectors

- **Oil & Gas (E&P)** — NAV on the **2P reserve case** ([[spe-prms-reserve-categories]]),
  one tab per producing asset.
- **Metals & mining** — the same structure on JORC reserves
  ([[jorc-resources-and-reserves]]), one tab per mine; **Inferred resources excluded**
  from the reserve-backed schedule.

## Mechanics / formulas

- Production bounded: `cumulative production ≤ recoverable reserves (2P / Probable+Proved)`.
- Asset value: `Σ_t (production_t × (realized price_t − unit cost_t) − capex_t − taxes_t)
  / (1+r)^t`, terminating at exhaustion + ARO.
- Corporate value = `Σ assets − net debt (incl. leases) ± non-operating items`.

## Modeling implications

- **One tab per producing asset/field/mine**, consolidating into Corporate — mirrors the
  reference multi-asset structure.
- Self-adapting granularity: if the issuer discloses only at cluster/basin level, the
  template collapses to that grain rather than forcing per-well/per-pit detail.
- Depletion runs on [[uop-depletion]], tied to the same reserve base.

## Pitfalls & nuances

- **Do NOT model perpetual production growth** — bound and decline against reserves.
- **Do NOT use a Gordon-growth terminal value** — the tail is exhaustion + ARO.
- **Do NOT include unrisked contingent/prospective resources** (O&G) or **Inferred
  resources** (mining) in the base mine plan.
- **Open question for the spec/copilot:** should the default be **NAV (per-asset risked
  SOTP)** or a **consolidated FCFF DCF**? DCF is the v2 deliverable per the spec; NAV is
  the sector-native answer. Flagged on both extractive cards — resolve with the user.

## Related concepts

- [[spe-prms-reserve-categories]] — the O&G reserve base NAV runs on
- [[jorc-resources-and-reserves]] — the mining reserve base
- [[uop-depletion]] — depletion over the same reserve base
- [[ev-2p-reserves]] — the reserve multiple cross-check
- [[c1-aisc-mining]] — the per-tonne cost in the mining NAV

## Provenance
- Method cards: [[oil_and_gas]], [[metals_mining]]
- Sources: [SPE-PRMS-2007 (SPE)](https://www.spe.org/industry/docs/PRMS-Guide-for-Non-Technical-Users-2007.pdf); [JORC-2012 (JORC)](https://www.jorc.org/docs/JORC_code_2012.pdf); [CFI-EV2P](https://corporatefinanceinstitute.com/resources/valuation/ev-2p-ratio)
- Confidence: 🟡 seed — reserve logic ✅ verified; NAV-vs-DCF default is an open spec question

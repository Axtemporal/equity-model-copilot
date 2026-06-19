---
concept: ev-2p-reserves
title: EV/2P Reserve Multiple
theme: sector-kpi
applies_to: [oil_and_gas]
confidence: seed
status: draft
---

# EV/2P Reserve Multiple

**What it is.** EV/2P expresses an E&P company's enterprise value **per barrel of 2P
(Proved + Probable) reserves**, giving a reserve-based valuation cross-check that asks
"what is the market paying per recoverable barrel?" — a complement to, not a substitute
for, the reserve-based NAV/DCF.

## Core idea

Because an E&P company's value is fundamentally the value of its recoverable barrels, a
natural multiple normalizes enterprise value by the reserve base:

`EV/2P = Enterprise Value ÷ 2P reserves (boe)`

It lets you compare what the market pays per barrel across companies and against
transaction comps, sidestepping the year-to-year noise in earnings. **EV/1P** is the
more conservative analogue on proved-only reserves.

It is a **cross-check**, not the primary method — the reserve-based NAV
([[reserve-based-nav]]) captures decline, cost, and timing that a flat per-barrel
multiple cannot.

## Applies to sectors

- **Oil & Gas (E&P)** — directly, on the 2P base ([[spe-prms-reserve-categories]]).
- The mining analogue is an EV-per-resource/reserve or EV/EBITDA cross-check, but the
  per-reserve multiple is most standardized in O&G.

## Mechanics / formulas

- `EV/2P = EV ÷ 2P reserves`; `EV/1P = EV ÷ 1P reserves`.
- Use a consistent reserve definition across the comp set — mixing SEC proved (1P) with
  analyst 2P breaks comparability ([[spe-prms-reserve-categories]]).

## Modeling implications

- Surface EV/2P (and EV/1P) in the Valuation tab as a **multiple cross-check** beside the
  NAV/DCF, never as the headline output.
- Keep the reserve base used explicit and consistent with the rest of the model.

## Pitfalls & nuances

- 🟡 A per-barrel multiple ignores **decline, cost structure, and timing** — two
  companies at the same EV/2P can have very different economics; always anchor on the
  NAV/DCF.
- Do not mix reserve definitions across the comp set.
- No target price / recommendation — present as an analytical cross-check with a
  disclaimer (project compliance).

## Related concepts

- [[spe-prms-reserve-categories]] — the 2P base the multiple uses
- [[reserve-based-nav]] — the primary method this cross-checks
- [[uop-depletion]] — why a flat multiple misses decline economics

## Provenance
- Method cards: [[oil_and_gas]]
- Sources: [CFI-EV2P — EV/2P ratio (Corporate Finance Institute)](https://corporatefinanceinstitute.com/resources/valuation/ev-2p-ratio); reserve base from [SPE-PRMS-2007 (SPE)](https://www.spe.org/industry/docs/PRMS-Guide-for-Non-Technical-Users-2007.pdf)
- Confidence: 🟡 seed (multiple is standard; treat as cross-check only)

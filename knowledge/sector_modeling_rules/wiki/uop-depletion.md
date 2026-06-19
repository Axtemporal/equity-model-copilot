---
concept: uop-depletion
title: Units-of-Production Depletion
theme: driver-pattern
applies_to: [oil_and_gas, metals_mining]
confidence: verified
status: draft
---

# Units-of-Production Depletion

**What it is.** Producing extractive assets are amortized **not straight-line but
pro-rata to production over the reserve base** — each period's DD&A is the capitalized
cost times the fraction of recoverable reserves produced — and **which reserve basis is
used (proved developed, 1P, or 2P) is an accounting-policy choice the issuer makes and
must apply consistently**, so it must be read per company, never assumed.

## Core idea

A straight-line depreciation of a producing oilfield or mine would misstate the cost of
extraction, because the economic life is measured in **barrels/tonnes remaining**, not
years. Units-of-production (UoP) ties the charge to physical depletion: produce more this
period, depletion is higher; revise reserves up, the rate per unit falls. Under IFRS,
**UoP is the preferred amortization method** for upstream producing assets precisely
because it reflects the pattern of consumption of the reserves' economic benefits;
straight-line is acceptable only when the asset is consumed by passage of time or the
result is not materially different.

The pivotal nuance — and the answer to a question the copilot had left open — is that
**IFRS does not prescribe the reserve basis**. Entities may deplete over **proved
developed** reserves, **total proved (1P)**, or **proved-plus-probable (2P)**; it is an
**accounting-policy choice applied consistently**. So depleting over 1P gives a higher
per-unit rate than over 2P, and the model must identify the issuer's stated basis rather
than impose one.

## Applies to sectors

- **Oil & Gas (E&P)** — producing fields amortize on UoP over the chosen reserve base;
  the rate shifts with revisions and with the disclosed basis. See
  [[spe-prms-reserve-categories]].
- **Metals & mining** — mines amortize on UoP over JORC reserves, parallel to O&G. See
  [[jorc-resources-and-reserves]].

## Mechanics / formulas

- `DD&A_period = amortizable cost × (period production ÷ recoverable reserves on the chosen basis)`
- Equivalently, a depletion **rate per unit** = amortizable cost ÷ recoverable reserves,
  applied to production.
- **Consistency rule:** if a **non-developed** basis is used (total proved or 2P), the
  amortizable cost must be **grossed up to include estimated future development costs**
  needed to access the undeveloped reserves — so numerator (cost) and denominator
  (reserves) cover the same barrels. ✅
- Reserve revisions re-strike the rate prospectively.

## Modeling implications

- The depletion schedule reads from the **same reserve roll-forward** that bounds
  production ([[reserve-based-nav]]) — link, never hardcode a straight-line %.
- **Identify the issuer's reserve basis first** (proved developed / 1P / 2P); if it is a
  non-developed basis, add the future-development-cost gross-up to the depletable base.
- Capitalized E&E reclassified under [[ifrs-6-ee-capitalization]] enters the depletable
  base.

## ARO / decommissioning interaction

The decommissioning / asset-retirement obligation (ARO) is measured at the **present
value of expected future decommissioning cash flows** (IAS 37.45) and **capitalized into
the asset cost** when the obligation arises (IAS 16.16(c)), then depreciated over the
asset life — typically on the **same UoP basis**. Critically, the subsequent **accretion
(unwinding of the discount) is a finance expense**, *not* part of operating/depletion
cost — keep the two charges distinct in the model. ✅

## Pitfalls & nuances

- **Do NOT depreciate producing extractive assets straight-line** — use UoP over reserves.
- **Do NOT assume a single reserve basis** — it is a per-issuer accounting-policy choice
  (proved developed vs 1P vs 2P); read the disclosure.
- **Do NOT mix bases between numerator and denominator** — a non-developed basis requires
  grossing up the cost for future development.
- **Do NOT fold ARO accretion into operating cost** — it is a finance expense, separate
  from UoP depletion.

## Related concepts

- [[reserve-based-nav]] — the reserve base that also bounds production
- [[spe-prms-reserve-categories]] — the O&G reserve basis options (1P vs 2P)
- [[jorc-resources-and-reserves]] — the mining reserve base
- [[ifrs-6-ee-capitalization]] — what enters the depletable asset base

## Provenance
- Method cards: [[oil_and_gas]], [[metals_mining]]
- Sources: [PWC-OG — Financial reporting in the oil and gas industry (PwC)](https://www.pwc.com/id/en/publications/assets/eumpublications/financial-reporting-in-the-oil-and-gas-industry.pdf) (UoP as policy choice; non-developed gross-up; UoP as preferred method; ARO measurement/accretion — IAS 37.45, IAS 16.16(c)); reserve framing from [SPE-PRMS-2007 (SPE)](https://www.spe.org/industry/docs/PRMS-Guide-for-Non-Technical-Users-2007.pdf) and [JORC-2012 (JORC)](https://www.jorc.org/docs/JORC_code_2012.pdf)
- Confidence: ✅ verified (round 3, 3-0 on UoP basis-is-a-choice, non-developed gross-up, UoP-preferred, ARO measurement+accretion). The specific *Brazilian* government-take royalty formulas remain a round-4 gap (abstention-killed on session limit, not refuted).

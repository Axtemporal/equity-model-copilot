---
sector: Tech / B2B software (SaaS)
slug: tech_saas
pilots_examples: (no BR pilot yet) — global SaaS comps
coverage: partial
key_standards: IAS 38 / ASC 730, IFRS 15 / ASC 606
status: draft
---

# Tech / SaaS — sector method card

## 1. Core thesis
A SaaS company is a **recurring-revenue** engine: model the **ARR base as a
roll-forward** (new + expansion − contraction − churn) and judge it on **retention
(NRR)** and **unit economics (CAC/LTV, rule of 40)** rather than a single growth rate.
**Honesty note:** of all the SaaS-specific items, **only the R&D/software
capitalization rule was verified** in this research — the operating metrics below are
**textbook but ⚠️ not yet sourced** and form the round-2 agenda.

## 2. Operational drivers (the revenue build) — ⚠️ to-verify skeleton
All items here are standard SaaS practice but **were not returned/verified** by the
research; tagged ⚠️, **no citation**:
- **ARR / MRR roll-forward** ⚠️ — closing ARR = opening ARR + new + expansion −
  contraction − churned (a "corkscrew" on recurring revenue). Revenue derives from the
  ARR base, not the other way around.
- **Retention** ⚠️ — gross revenue churn vs **Net Revenue Retention (NRR / net dollar
  retention)**; NRR > 100% means expansion outweighs churn. Track **logo churn**
  separately.
- **Unit economics** ⚠️ — **CAC**, **LTV**, **LTV/CAC**, **CAC payback period**, magic
  number / sales efficiency.
- **Growth-vs-profitability** ⚠️ — **Rule of 40**: revenue growth % + FCF/EBITDA
  margin % ≥ 40.
- **Cohort modeling** ⚠️ — retention/expansion by signing cohort is the rigorous way to
  project NRR and the ARR roll-forward.

## 3. Mandatory KPIs & disclosures — ⚠️ to-verify
ARR/MRR, NRR/gross churn, logo churn, CAC/LTV, rule-of-40, **RPO (remaining performance
obligations)** and **deferred revenue** as forward-bookings indicators, **billings**
(≠ revenue), SBC as a % of revenue. ⚠️

## 4. Peculiar accounting / normative rules
- **R&D / software capitalization** ✅ — **IAS 38**: research expensed; development
  capitalized **only if all six criteria** met (technical feasibility, intention to
  complete, ability to use/sell, probable future economic benefits, adequate resources,
  reliable measurement). **US GAAP ASC 730**: R&D expensed as incurred (with separate
  **ASC 350-40** rules for internal-use software). The model **must read the issuer's
  framework and policy** — the capitalization choice materially changes reported margins
  and the asset base.
  > source: [KPMG-RD-2025] — verified ✅ (3-0).
- **Revenue recognition (IFRS 15 / ASC 606)** ✅ — a performance obligation satisfied
  **over time** (services) vs at a point in time (goods); a subscription is over-time, so
  it is recognized **ratably over the contract term** → a **deferred-revenue** liability +
  RPO; **billings ≠ revenue** within a period. The five-step model applies.
  > source: [IFRS-15] (over-time vs point-in-time + five-step model) — verified ✅ (3-0).
- **Capitalized commissions** (IFRS 15 / ASC 340-40) and high **SBC** materiality. ⚠️

## 5. Model structure adaptation
- **Drive the P&L off the ARR roll-forward**, with a deferred-revenue schedule
  converting bookings/billings into recognized revenue over time.
- **Cohort retention table** feeding NRR; CAC/LTV block; rule-of-40 check. ⚠️
- **Capitalized-software schedule** (per the issuer's IAS 38 / ASC 350-40 policy) with
  amortization, plus a clear view of SBC. ✅ (the capitalization rule) / ⚠️ (mechanics).

## 6. Modeling pitfalls
- **Do NOT equate billings/bookings with revenue** — subscription revenue is recognized
  over the term; the gap sits in deferred revenue/RPO.
- **Do NOT ignore SBC** — it is often large and distorts GAAP vs adjusted margins.
- **Do NOT assume a capitalization policy** — IAS 38 vs ASC 730 differ; read the issuer.
- **Do NOT project a flat churn/NRR** — model by cohort.

## 7. Confidence & open questions
- ✅ **Verified:** IAS 38 vs ASC 730 R&D/software capitalization divergence — the **only**
  verified SaaS item.
- ⚠️ **To verify (round 2 — this sector is largely a research gap):** ARR/MRR
  roll-forward conventions, NRR/churn definitions, CAC/LTV and rule-of-40 benchmarks,
  cohort method, IFRS 15 deferred-revenue/RPO mechanics, capitalized-commission rules.
- Shares R&D capitalization + software deferred revenue with [[auto]].

---
sector: Education / for-profit post-secondary
slug: education
pilots_examples: Cogna (Kroton), Yduqs (Estácio), Ânima, Cruzeiro do Sul
coverage: to-verify
key_standards: IFRS 15, government programs (FIES / PROUNI), MEC regulation
status: draft
---

# Education (for-profit post-secondary) — sector method card

## 1. Core thesis
An education company is a **student-base roll-forward**: revenue = **base de alunos ×
ticket médio (net mensalidade)**, where the base grows by **captação** (intake) and
shrinks by **evasão** (dropout). Two structural forces dominate the thesis — the **mix
shift to EAD** (digital, high-margin, capex-light) and **government programs
(FIES/PROUNI)** that drive affordability, intake, receivables and tax. **Honesty note:**
only the IFRS 15 tuition-recognition item is a (fetched, unverified) 🟡 seed; the
operating drivers are **⚠️ standard but not yet sourced** — a priority round-2 target.

## 2. Operational drivers (the revenue build)
- **Revenue = student base × average net ticket** ⚠️ — base de alunos (matrículas) ×
  **ticket médio** (mensalidade líquida, net of discounts/scholarships).
- **Base roll-forward (corkscrew)** ⚠️ — opening base + **captação** (new enrollments
  each entry cycle) − graduations − **evasão** (dropout/churn) = closing base.
- **Intake ramp / maturation** ⚠️ — a new campus or course matures over several years
  (the student **safra**/cohort); model a cohort ramp, not a flat base.
- **Presencial vs EAD/DL** ⚠️ — *ensino a distância* (digital) is much **higher-margin
  and capex-light/scalable** than on-campus; model as **separate segments** with
  different ticket, churn, and margin. The **mix shift to EAD** is the dominant industry
  thesis.

## 3. Mandatory KPIs & disclosures — ⚠️ to-verify
- Student base by modality (presencial / EAD); intake (captação); evasão / churn. ⚠️
- Ticket médio (gross vs net of scholarships/discounts), by modality. ⚠️
- FIES/PROUNI share of base; FIES receivables. ⚠️
- PCLD (*provisão para créditos de liquidação duvidosa* — bad-debt provision) — material. ⚠️
- Deferred revenue. 🟡

## 4. Peculiar accounting / normative rules
- **Tuition revenue recognition (IFRS 15)** ✅ — under IFRS 15 a performance obligation is
  satisfied **over time** (typically services) vs **at a point in time** (goods); tuition
  is an over-time service, so it is recognized **over the term** as delivered, giving rise
  to **deferred revenue** (fees billed/collected ahead of delivery); **billings ≠ revenue**
  within a term. The five-step model applies.
  > source: [IFRS-15] (over-time vs point-in-time + five-step model) — verified ✅ (3-0),
  > and the IFRS Foundation's tuition agenda decision concludes tuition is recognized
  > over time. Nuance 🟡: the *specific* "IFRIC concluded over time" claim was killed 2-1
  > on quote-precision, but the underlying over-time treatment is confirmed by the general
  > IFRS 15 finding — encode over-time/deferred revenue with confidence.
- **Discounts/scholarships as contra-revenue** ⚠️ — gross vs net ticket; heavy
  promotional discounting is standard, so the gap between list and net mensalidade is
  large.
- **Government programs** ⚠️ — **FIES** (federal student loan — affects affordability and
  intake, and creates **FIES receivables** with collection/repurchase risk); **PROUNI**
  (scholarships granted in exchange for **tax exemption** — affects the effective tax
  rate and fills seats). Model their effect on intake, ticket realization, receivables,
  and tax.
- **Bad debt / PCLD** ⚠️ — a material P&L and working-capital line for this sector.

## 5. Model structure adaptation — ⚠️ to-verify
- **Separate engines for presencial and EAD** (different ticket, churn, margin, capex).
- **Cohort/safra base roll-forward** feeding revenue, with intake ramp and evasão. ⚠️
- **FIES/PROUNI overlay** — intake & receivables effect (FIES), tax effect (PROUNI). ⚠️
- **Deferred-revenue schedule** (tuition recognized over the term). 🟡
- **MEC regulation** ⚠️ — accreditation, course caps, and the scarcity value of
  **vagas de medicina** (medicine seats — high-ticket, the Yduqs/Ânima premium thesis).

## 6. Modeling pitfalls — ⚠️ to-verify
- **Do NOT use gross ticket** — model net of scholarships/discounts.
- **Do NOT model one homogeneous base** — presencial and EAD differ in ticket, churn,
  and margin; the mix shift is the story.
- **Do NOT ignore FIES receivables / PCLD** — collection risk and bad debt are material.
- **Do NOT treat captação as flat** — it is cyclical (entry cycles) and ramps by cohort.

## 7. Confidence & open questions
- ✅ **Verified (round 2):** IFRS 15 five-step model and over-time-vs-point-in-time
  recognition → tuition recognized over the term → deferred revenue (billings ≠ revenue).
- ⚠️ **To verify (round 3 — operating drivers are still a research gap):** ticket/base/
  captação/evasão benchmarks; presencial vs EAD margin and capex; FIES/PROUNI mechanics
  and receivables/tax impact; PCLD levels; MEC regulation and vagas-de-medicina economics.
- Regulated-BR-service, roll-up M&A, and deferred-revenue parallels with [[healthcare]];
  EAD recurring-revenue / cohort parallels with [[tech_saas]].

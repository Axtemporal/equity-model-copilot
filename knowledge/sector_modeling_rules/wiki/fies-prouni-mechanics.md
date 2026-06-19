---
concept: fies-prouni-mechanics
title: FIES & PROUNI — Education Financing
theme: brazil-specific
applies_to: [education]
confidence: to-verify
status: draft
---

# FIES & PROUNI — Education Financing

**What it is.** Two Brazilian federal programmes that drive for-profit education
economics — **FIES** (a federal student loan that funds tuition, boosting affordability
and intake while creating **FIES receivables** with collection/repurchase risk) and
**PROUNI** (scholarships granted in exchange for a **corporate tax exemption**, filling
seats and lowering the effective tax rate) — both of which must be modeled for their
effect on intake, ticket realization, receivables, and tax.

## Core idea

A for-profit education company's student base and cash quality are shaped heavily by
public financing:

- **FIES** — the government lends students the tuition. It **raises affordability and
  intake** (captação), but the institution carries **FIES receivables** with collection
  and repurchase risk; program contraction directly shrinks the addressable base.
- **PROUNI** — the government grants scholarships, and in exchange the institution gets a
  **tax exemption**. It **fills otherwise-empty seats** and **lowers the effective tax
  rate** ([[jcp-effective-tax]]), at the cost of zero/low ticket on those seats.

Both interact with the **student-base roll-forward** (captação − evasão − graduations) and
with **net ticket** (gross mensalidade less scholarships/discounts).

## Applies to sectors

- **Education (for-profit post-secondary)** — directly.
- The student-base corkscrew parallels the SaaS [[arr-roll-forward]]; the regulated-BR-
  service overlay parallels healthcare's [[mlr-sinistralidade]] sector.

## Mechanics / formulas

- `Net ticket = gross mensalidade − scholarships/discounts (incl. PROUNI seats)`.
- `Student base (corkscrew) = opening + captação − graduations − evasão = closing`.
- FIES adds a **receivables + PCLD (bad-debt provision)** schedule; PROUNI adds a **tax-
  exemption** reconciling item to the effective rate.

## Modeling implications

- Model **separate engines for presencial and EAD** (different ticket, churn, margin,
  capex); EAD is higher-margin and capex-light — the mix shift is the dominant thesis.
- Overlay **FIES** (intake + receivables/PCLD effect) and **PROUNI** (tax effect) on the
  base roll-forward.
- Build a **deferred-revenue schedule** (tuition recognized over the term — see
  [[ifrs-15-performance-obligations]]).

## Pitfalls & nuances

- ⚠️ **To-verify (round 3).** FIES/PROUNI mechanics, receivables/tax impact, PCLD levels,
  and MEC regulation (incl. scarce **vagas de medicina**) are standard but **not yet
  source-verified** — the IFRS 15 tuition recognition is the only ✅ education item.
- **Do NOT use gross ticket** — model net of scholarships/discounts.
- **Do NOT ignore FIES receivables / PCLD** — collection risk and bad debt are material.
- **Do NOT treat captação as flat** — it is cyclical (entry cycles) and ramps by cohort.

## Related concepts

- [[ifrs-15-performance-obligations]] — over-time tuition recognition / deferred revenue
- [[jcp-effective-tax]] — PROUNI's tax exemption is an effective-rate lever
- [[arr-roll-forward]] — the analogous recurring-base corkscrew (SaaS)
- [[mlr-sinistralidade]] — the parallel regulated-BR-service overlay (healthcare)

## Provenance
- Method cards: [[education]]
- Sources: Brazilian education-financing programmes (FIES/PROUNI, MEC); accounting basis from [IFRS-15 (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/) — operating/program mechanics are a round-3 gap
- Confidence: ⚠️ to-verify (round-3 agenda; IFRS 15 tuition recognition is the only ✅ item)

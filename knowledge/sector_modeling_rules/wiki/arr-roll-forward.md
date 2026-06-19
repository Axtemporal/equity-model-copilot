---
concept: arr-roll-forward
title: ARR / MRR Roll-Forward
theme: driver-pattern
applies_to: [tech_saas]
confidence: seed
status: draft
---

# ARR / MRR Roll-Forward

**What it is.** A SaaS company's revenue is driven off a **recurring-revenue base
modeled as a roll-forward (corkscrew)** — closing ARR = opening ARR + new + expansion −
contraction − churn — so revenue **derives from the ARR base**, not the other way around,
and the base is judged on retention rather than a single growth rate.

## Core idea

Subscription revenue is sticky and cumulative: most of next period's revenue is already
locked in by the existing base. Modeling it as a single growth-rate line throws away the
structure that actually drives it. The **corkscrew** makes the dynamics explicit:

```
Closing ARR = Opening ARR
            + New ARR (new logos)
            + Expansion ARR (upsell/cross-sell to existing)
            − Contraction ARR (downgrades)
            − Churned ARR (lost logos)
```

Recognized revenue then derives from the ARR base over time (under
[[ifrs-15-performance-obligations]], a subscription is an over-time obligation → revenue
ratable, with a deferred-revenue liability and RPO). **Billings ≠ revenue** in a period.

## Applies to sectors

- **Tech / SaaS** — directly; the corkscrew is the spine of the model.
- The **cohort/base roll-forward** structure parallels education's student-base
  roll-forward ([[fies-prouni-mechanics]] sector) — captação/evasão is the same corkscrew
  on students.

## Mechanics / formulas

- ARR roll-forward as above; **MRR** is the monthly analogue (ARR ÷ 12 ≈ MRR for clean
  annual contracts).
- Retention metrics fall straight out of the corkscrew components — see
  [[saas-unit-economics]] for NRR, gross/logo churn, etc.
- Revenue: derived from the average ARR base over the period, net of the deferred-revenue
  timing.

## Modeling implications

- **Drive the P&L off the ARR roll-forward**, with a **deferred-revenue schedule**
  converting bookings/billings into recognized revenue over time.
- Feed a **cohort retention table** into NRR rather than projecting a flat churn/NRR.
- Keep **billings, bookings, and revenue** as distinct lines; the gaps are deferred
  revenue / RPO.

## Pitfalls & nuances

- **Do NOT equate billings/bookings with revenue** — the gap sits in deferred revenue /
  RPO.
- **Do NOT project a flat churn/NRR** — model by cohort; retention varies sharply by
  signing cohort.
- 🟡 The roll-forward conventions are standard SaaS practice but were **not yet
  source-verified** in the research (a round-3 gap) — the IFRS 15 deferred-revenue
  mechanics underneath are ✅ verified.

## Related concepts

- [[saas-unit-economics]] — the retention/efficiency metrics layered on the base
- [[ifrs-15-performance-obligations]] — why subscription revenue is over-time / deferred
- [[ias-38-rd-capitalization]] — the cost side (capitalized vs expensed development)

## Provenance
- Method cards: [[tech_saas]]
- Sources: [IFRS-15 (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/) for the deferred-revenue mechanics; roll-forward conventions are standard SaaS practice (round-3 verification gap)
- Confidence: 🟡 seed (deferred-revenue mechanics ✅; corkscrew conventions to-verify)

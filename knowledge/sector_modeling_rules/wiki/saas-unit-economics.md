---
concept: saas-unit-economics
title: SaaS Unit Economics
theme: sector-kpi
applies_to: [tech_saas]
confidence: to-verify
status: draft
---

# SaaS Unit Economics

**What it is.** The set of metrics used to judge a SaaS business on **retention and
efficiency** rather than headline growth — **NRR, gross/logo churn, CAC, LTV, LTV/CAC,
CAC payback, and the Rule of 40** — layered on the ARR roll-forward and ideally measured
by **signing cohort**.

## Core idea

A SaaS company can grow revenue while quietly destroying value if it churns customers or
overspends to acquire them. Unit economics make that visible by interrogating the
[[arr-roll-forward]] components:

- **Net Revenue Retention (NRR)** — revenue this year from last year's cohort ÷ last
  year's revenue from that cohort. **NRR > 100%** means expansion outweighs churn — the
  base grows with zero new logos.
- **Gross revenue churn** and **logo churn** — tracked separately; logo churn can be high
  while NRR stays >100% if survivors expand.
- **CAC** (customer acquisition cost), **LTV** (lifetime value), **LTV/CAC**, and **CAC
  payback period** — the efficiency of the growth engine.
- **Rule of 40** — `revenue growth % + FCF/EBITDA margin % ≥ 40` as a growth-vs-
  profitability balance test.
- **Cohort retention** — retention/expansion by signing cohort, the rigorous basis for
  projecting NRR and the ARR roll-forward.

## Applies to sectors

- **Tech / SaaS** — directly.
- The retention/cohort logic informs any **recurring-revenue** business, including
  education's EAD/student cohorts ([[fies-prouni-mechanics]] sector).

## Mechanics / formulas

- `NRR = (starting cohort ARR + expansion − contraction − churn) ÷ starting cohort ARR`
- `LTV/CAC` and `CAC payback = CAC ÷ (gross-margin-adjusted monthly recurring revenue per
  customer)`
- `Rule of 40 = revenue growth % + profitability margin %`

## Modeling implications

- Feed a **cohort retention table** into NRR rather than a flat churn assumption.
- Add a **CAC/LTV block** and a **Rule-of-40 check** alongside the ARR roll-forward.
- Watch **SBC** (stock-based comp) materiality — it distorts GAAP vs adjusted margins and
  interacts with the Rule-of-40 profitability term.

## Pitfalls & nuances

- ⚠️ **Entire article is to-verify (round 3).** These are standard SaaS conventions but
  were **not source-verified** in the research — only the underlying IAS 38 / IFRS 15
  accounting was confirmed. Treat the definitions as textbook-standard pending a research
  round.
- **Do NOT project a flat churn/NRR** — model by cohort.
- **Do NOT ignore SBC** — often large; distorts margins and the Rule of 40.

## Related concepts

- [[arr-roll-forward]] — the recurring-revenue base these metrics interrogate
- [[ifrs-15-performance-obligations]] — the revenue-recognition basis (deferred revenue/RPO)
- [[ias-38-rd-capitalization]] — the cost side (capitalized vs expensed development)

## Provenance
- Method cards: [[tech_saas]]
- Sources: standard SaaS practitioner conventions (round-3 verification gap); accounting basis from [IFRS-15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/) and [KPMG-RD-2025](https://kpmg.com/us/en/articles/2025/rd-costs-ifrs-accounting-standards-us-gaap.html)
- Confidence: ⚠️ to-verify (round-3 agenda; the only verified SaaS items are IAS 38 and IFRS 15)

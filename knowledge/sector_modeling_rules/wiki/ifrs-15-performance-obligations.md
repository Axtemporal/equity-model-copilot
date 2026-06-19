---
concept: ifrs-15-performance-obligations
title: IFRS 15 — Over-time vs Point-in-time Recognition
theme: accounting-standard
applies_to: [education, tech_saas, auto]
confidence: verified
status: draft
---

# IFRS 15 — Over-time vs Point-in-time Recognition

**What it is.** IFRS 15's five-step model recognizes revenue when a **performance
obligation** is satisfied — **over time** for obligations the customer consumes as
delivered (most services: tuition, SaaS subscriptions) or **at a point in time** for
obligations transferred at a moment (most goods: a vehicle at OEM-to-dealer transfer) —
which determines when revenue hits the P&L, what sits in deferred revenue, and how
incentives are treated.

## Core idea

The whole standard turns on **when control transfers**. Run the five steps — identify
the contract, identify the performance obligations, determine the transaction price,
allocate it to the obligations, recognize revenue as each is satisfied — and the pivotal
question is whether each obligation is satisfied **over time** or **at a point in time**:

- **Over time** — the customer simultaneously receives and consumes the benefit (a
  subscription, a term of tuition, a service contract). Revenue is recognized **ratably
  over the period**, and amounts billed/collected ahead of delivery sit in a **deferred-
  revenue** liability. **Billings ≠ revenue** within a period.
- **Point in time** — control transfers at a moment (a manufactured good). Revenue is
  recognized then.

The **transaction price** is net of **variable consideration** — which is why cash
incentives paid to customers are **contra-revenue**, not marketing expense.

## Applies to sectors

- **Education** — tuition is an **over-time service**: recognized over the term →
  deferred revenue when fees are billed ahead. See [[fies-prouni-mechanics]] for the
  financing overlay.
- **Tech / SaaS** — a subscription is **over-time** → deferred revenue + remaining
  performance obligations (RPO); billings lead revenue. See [[arr-roll-forward]] and
  [[saas-unit-economics]].
- **Auto / OEM** — vehicle sales are **point-in-time at OEM-to-dealer control transfer**
  (the dealer, not the consumer, is the customer); **cash incentives are contra-
  revenue**; software/FSD obligations may be over-time (deferred).

## Mechanics / formulas

- Over-time: `Revenue_period = transaction price × (obligation satisfied this period)`;
  unrecognized billed amount → deferred revenue liability.
- Point-in-time: full transaction price recognized at control transfer.
- Contra-revenue: `Net revenue = gross price − cash incentives` (variable consideration
  if contingent; fixed discount if not). A distinct good/service bought from the customer
  is a separate purchase, not contra-revenue.

## Modeling implications

- For over-time issuers, build a **deferred-revenue schedule** converting
  bookings/billings into recognized revenue, and **never equate billings with revenue**.
- For point-in-time issuers (auto), set revenue timing at the **wholesale (OEM-to-dealer)
  sale**, and **net incentives against revenue** rather than expensing them.
- The copilot should classify each major revenue stream over-time vs point-in-time before
  proposing a revenue build.

## Pitfalls & nuances

- **Do NOT recognize an automaker's revenue at the consumer sale** — it is at OEM-to-
  dealer transfer; consignment that withholds control defers it.
- **Do NOT classify customer incentives as opex** — they are contra-revenue.
- **Do NOT equate SaaS/tuition billings with revenue** — the gap sits in deferred
  revenue / RPO.
- Nuance: the IFRS Foundation's tuition agenda decision concludes tuition is recognized
  over time; the *specific* "IFRIC concluded over time" wording was challenged on
  quote-precision, but the over-time treatment itself is solid via the general IFRS 15
  principle.

## Related concepts

- [[arr-roll-forward]] — the SaaS recurring-revenue build behind deferred revenue
- [[saas-unit-economics]] — the metrics layered on subscription revenue
- [[fies-prouni-mechanics]] — education financing affecting the transaction price
- [[ias-38-rd-capitalization]] — the other standard recurring across tech/auto

## Provenance
- Method cards: [[education]], [[tech_saas]], [[auto]]
- Sources: [IFRS-15 — Revenue from Contracts with Customers (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/); [EY-AUTO-IFRS15 — Applying IFRS, automotive (EY, 2020)](https://www.ey.com/en_gl/technical/ifrs-technical-resources/applying-ifrs-the-revenue-recognition-standard-automotive-industry); [IFRS-15-TUITION — tuition agenda decision (IFRS Foundation, 2025)](https://www.ifrs.org/projects/completed-projects/2025/recognition-of-revenue-from-tuition-fees-ifrs-15/)
- Confidence: ✅ verified (3-0; tuition-specific wording 🟡 2-1 on quote-precision)

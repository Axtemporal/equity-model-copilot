---
concept: ifrs-6-ee-capitalization
title: IFRS 6 — Exploration & Evaluation Capitalization
theme: accounting-standard
applies_to: [oil_and_gas, metals_mining]
confidence: verified
status: draft
---

# IFRS 6 — Exploration & Evaluation Capitalization

**What it is.** IFRS 6 grants extractive issuers (oil & gas and mining) an
**accounting-policy exemption** for exploration & evaluation (E&E) costs: each company
sets its own recognition and measurement policy — most visibly the **successful-efforts
vs full-cost** choice — so the model must **read each issuer's stated policy** rather
than assume one uniform treatment.

## Core idea

Before reserves are proven, an extractive company spends heavily searching for and
appraising deposits. Normal asset-recognition rules struggle here because the future
economic benefit is genuinely uncertain. IFRS 6 sidesteps the problem with an explicit
**exemption**: issuers may keep their pre-existing E&E policy on adoption and apply
judgment, so two otherwise-comparable companies can capitalize very different amounts:

- **Successful-efforts** — capitalize only costs tied to successful discoveries; expense
  dry holes / unsuccessful exploration.
- **Full-cost** — capitalize essentially all exploration cost into a cost pool,
  regardless of individual outcome.

E&E is the cost bucket capitalized **before reserves are proven**; once commercial
viability is established it **reclassifies** into IAS 16 (PP&E) or IAS 38 (intangibles)
and begins to deplete via [[uop-depletion]].

## Applies to sectors

- **Oil & Gas (E&P)** — the successful-efforts/full-cost choice materially changes
  capitalized assets, DD&A, and reported margins. See [[spe-prms-reserve-categories]].
- **Metals & mining** — same exemption; issuers set their own exploration capitalization
  policy. See [[jorc-resources-and-reserves]].

This is the one accounting overlay genuinely shared across both extractive cards, which
is why it sits in one article they both link to.

## Mechanics / formulas

- E&E costs → capitalized under the issuer's chosen policy → held until commercial
  viability → **reclassified** to IAS 16 / IAS 38 → depleted on a units-of-production
  basis over the reserve base.
- Impairment testing applies to E&E assets under IFRS 6's specific indicators (e.g.
  expiry of exploration rights, no further budgeted activity).

## Modeling implications

- The copilot must **not assume a single E&E treatment**. When proposing capex and DD&A
  assumptions for an extractive issuer, it should first identify the stated E&E policy
  (successful-efforts vs full-cost) and model accordingly.
- The capitalized E&E asset and its later reclassification feed the depletion schedule —
  link, don't hardcode.

## Pitfalls & nuances

- **Do NOT assume one E&E policy across companies** — IFRS 6 lets them differ; comparing
  capitalized exploration across peers without normalizing for the policy is misleading.
- Watch the adoption grandfathering — a company may carry a legacy policy that diverges
  from current practice.

## Related concepts

- [[spe-prms-reserve-categories]] — what gets proven (O&G reserves)
- [[jorc-resources-and-reserves]] — what gets proven (mining reserves)
- [[uop-depletion]] — how the reclassified asset depletes
- [[reserve-based-nav]] — the valuation the capitalized base feeds

## Provenance
- Method cards: [[oil_and_gas]], [[metals_mining]]
- Sources: [IFRS-6 — Exploration for and Evaluation of Mineral Resources (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-6-exploration-for-and-evaluation-of-mineral-resources/) (para 7)
- Confidence: ✅ verified (3-0)

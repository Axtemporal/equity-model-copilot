---
concept: ifrs-16-leases
title: IFRS 16 — Leases, EBITDA-AL & the EV Bridge
theme: accounting-standard
applies_to: [oil_and_gas, fuel_distribution, petrochemicals, steel, pulp_paper, healthcare, education, tech_saas, auto, agriculture, agri_inputs, metals_mining]
confidence: seed
status: draft
---

# IFRS 16 — Leases, EBITDA-AL & the EV Bridge

**What it is.** IFRS 16 puts almost all leases on the balance sheet as a **right-of-use
(RoU) asset** and a **lease liability**, which lifts reported EBITDA (rent leaves opex,
replaced by depreciation + interest) — so the project reports both **EBITDA and
EBITDA-AL** (after-lease), counts **leases as debt** in the EV→equity bridge, and has
**FCFF deduct lease payments**.

## Core idea

Pre-IFRS-16, operating-lease rent was a single opex line. IFRS 16 capitalizes the lease:

- A **right-of-use asset** (depreciated) and a **lease liability** (unwound with interest)
  appear on the balance sheet.
- The old rent expense splits into **depreciation** (above EBITDA) + **interest** (below
  EBITDA). Mechanically this **raises EBITDA** versus the pre-standard view.

That EBITDA lift is why a second metric is needed to compare like-for-like and to avoid
double-counting lease obligations in valuation.

## Project decisions (closed)

Per the spec's third-round decisions:

- **Report both EBITDA and EBITDA-AL** (EBITDA after leases). See [[ebitda-al-ifrs16]].
- In the **EV→equity bridge, leases count as debt** (the lease liability is part of net
  debt).
- **FCFF deducts lease payments**, consistent with the telecom guidance — so the cash
  flow and the bridge treat leases consistently and the lease obligation is not
  double-counted.

## Applies to sectors

Effectively **all** sectors carry leases, but it bites hardest where leasing is
structural — fuel distribution (stations, terminals), healthcare (hospital real estate),
education (campuses), retail-style ag-inputs distribution. For lease-light extractive and
heavy-industrial issuers it is smaller but still reported both ways for consistency.

## Mechanics / formulas

- `EBITDA-AL = EBITDA − depreciation of RoU assets − ...` (the after-lease metric that
  neutralizes the IFRS-16 EBITDA lift; exact construction in [[ebitda-al-ifrs16]]).
- Lease liability roll-forward: opening + new leases + interest accretion − payments =
  closing.
- EV→equity bridge: `Equity value = EV − net debt − lease liability + non-operating
  assets` (leases inside net debt).

## Modeling implications

- The engine maintains **RoU + lease-liability roll-forwards** (already implemented for
  O&G; see the build status) and surfaces **EBITDA and EBITDA-AL** side by side.
- The Valuation tab's bridge treats the **lease liability as debt**, and **FCFF deducts
  lease payments** — never both add leases to debt *and* ignore the payment in FCFF
  (double-count) nor omit both.

## Pitfalls & nuances

- **Do NOT compare a post-IFRS-16 EBITDA with a pre-standard or US-GAAP figure** without
  reconciling — the standard lifts EBITDA.
- **Do NOT double-count leases** — if the lease liability is in net debt, FCFF must
  deduct lease payments (the project's consistent treatment).
- 🟡 This article encodes the project's *decisions*; sector-specific EBITDA-AL mechanics
  per issuer are still a to-verify gap on several cards.

## Related concepts

- [[ebitda-al-ifrs16]] — the after-lease profitability metric in depth
- [[reserve-based-nav]] — the EV→equity bridge where leases sit as debt
- [[mid-cycle-normalization]] — EBITDA-AL feeds cyclical normalized multiples

## Provenance
- Method cards: cross-cutting (all); explicit on [[petrochemicals]], [[steel]], [[pulp_paper]]
- Sources: project spec (`docs/project_specification.md`, third-round decisions); [IFRS 16 Leases (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/)
- Confidence: 🟡 seed (project decision encoded; per-sector mechanics to verify)

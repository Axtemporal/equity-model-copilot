---
concept: ebitda-al-ifrs16
title: EBITDA-AL (after-lease EBITDA)
theme: sector-kpi
applies_to: [oil_and_gas, fuel_distribution, petrochemicals, steel, pulp_paper, healthcare, education, tech_saas, auto]
confidence: seed
status: draft
---

# EBITDA-AL (after-lease EBITDA)

**What it is.** EBITDA-AL ("EBITDA after leases") is the profitability metric that
**neutralizes the EBITDA lift created by IFRS 16** — it deducts the lease-related
depreciation/interest that IFRS 16 moved out of opex — so margins are comparable across
issuers and time, and so the lease obligation is treated consistently in valuation.

## Core idea

IFRS 16 capitalized operating leases, splitting old rent into depreciation + interest and
**mechanically raising EBITDA** ([[ifrs-16-leases]]). That makes a post-standard EBITDA
non-comparable with pre-standard or US-GAAP figures and risks double-counting leases in
valuation. **EBITDA-AL** strips the lift back out, restoring a rent-equivalent view.

The project's spec (third-round decisions) requires **reporting both EBITDA and
EBITDA-AL**, treating **leases as debt** in the EV→equity bridge, and having **FCFF deduct
lease payments** — a single consistent treatment.

## Applies to sectors

Universal, but it matters most where leasing is structural: **fuel distribution**
(stations/terminals), **healthcare** (hospital real estate), **education** (campuses),
and **telecom** (towers/sites) — the lease-heavy sectors where the EBITDA lift is large.
For lease-light extractive/heavy-industry issuers it is smaller but still reported both
ways for consistency.

## Mechanics / formulas

- Conceptually: `EBITDA-AL = EBITDA − (depreciation of right-of-use assets + lease
  interest)`, i.e. EBITDA reduced back toward a cash-rent basis.
- In valuation: the **lease liability sits in net debt** in the EV→equity bridge, and
  **FCFF deducts lease payments** — never both ignore the payment and add the liability
  (double-count) nor omit both.

## Modeling implications

- Surface **EBITDA and EBITDA-AL side by side** in the model output (the engine maintains
  the RoU + lease-liability roll-forwards that make this possible).
- Use **EBITDA-AL** for cross-sector and historical comparisons and for cyclical
  normalization ([[mid-cycle-normalization]]); use the bridge treatment for the Valuation
  tab.

## Pitfalls & nuances

- **Do NOT compare a post-IFRS-16 EBITDA with a pre-standard / US-GAAP EBITDA** — use
  EBITDA-AL to reconcile.
- **Do NOT double-count leases** — if the lease liability is in net debt, FCFF must deduct
  lease payments.
- 🟡 Exact EBITDA-AL construction per issuer (which lease lines, how disclosed) is a
  to-verify gap on several cards.

## Related concepts

- [[ifrs-16-leases]] — the standard and the project's lease decisions
- [[mid-cycle-normalization]] — normalize EBITDA-AL, not raw EBITDA, for cyclicals
- [[reserve-based-nav]] — the EV→equity bridge where leases sit as debt

## Provenance
- Method cards: cross-cutting; explicit on [[petrochemicals]], [[steel]], [[pulp_paper]]
- Sources: project spec (`docs/project_specification.md`, third-round decisions); [IFRS 16 (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/)
- Confidence: 🟡 seed (project decision encoded; per-issuer construction to verify)

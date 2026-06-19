---
concept: jcp-effective-tax
title: JCP & Effective Tax Rate (Brazil)
theme: brazil-specific
applies_to: [oil_and_gas, fuel_distribution, petrochemicals, steel, pulp_paper, healthcare, education, agriculture, agri_inputs, metals_mining]
confidence: to-verify
status: draft
---

# JCP & Effective Tax Rate (Brazil)

**What it is.** **Juros sobre capital próprio (JCP)** — "interest on equity" — is a
Brazilian distribution mechanism that is **tax-deductible for the paying company** (within
limits), so it lowers the **effective tax rate** below the ~34% statutory IRPJ+CSLL rate
and blurs the line between a dividend and an interest expense; the project spec calls for a
**dedicated method card** on JCP and effective-tax mechanics.

## Core idea

Unlike an ordinary dividend, JCP is deductible against taxable income for the company that
pays it (subject to caps tied to equity and to a reference interest rate, historically the
TJLP), creating a **tax shield on a distribution**. The economic effects:

- The paying company's **effective tax rate falls** below the ~34% statutory combination
  of IRPJ (25%) + CSLL (9%).
- The recipient is taxed on JCP (historically withholding), so JCP is a
  distribution-plus-tax-planning tool, not free money.
- Because JCP is partly a financing-flavored line, it must be modeled where it actually
  affects the **tax line and the distribution policy**, not buried.

Other Brazilian features that move the effective rate: **PROUNI** tax exemption for
qualifying education companies ([[fies-prouni-mechanics]]), SUDENE/SUDAM regional
incentives, and Lucro Real vs Lucro Presumido regimes.

## Applies to sectors

Cross-cutting across all Brazilian issuers, since JCP and the effective-rate drivers are a
tax-structure feature, not a sector-operational one. Education is a special case via
PROUNI ([[fies-prouni-mechanics]]).

## Mechanics / formulas

- JCP deduction is capped (broadly) by a reference rate applied to adjusted equity and by
  a proportion of profit/retained earnings — model the cap, not a free deduction.
- `Effective tax rate = tax expense ÷ pre-tax income`, reconciled from the ~34% statutory
  rate down for JCP deductibility and incentives, up for non-deductibles.

## Modeling implications

- Model JCP as a **tax-deductible distribution**: it reduces the tax line and is part of
  the cash-return policy — surface it in both places.
- Build an **effective-tax-rate reconciliation** from statutory ~34% to the modeled
  effective rate, with JCP and incentives as explicit reconciling items, rather than
  hardcoding a flat rate.

## Pitfalls & nuances

- ⚠️ **Entire article is to-verify (round 3).** The JCP/effective-tax mechanics here are
  standard Brazilian-tax knowledge but **not yet source-verified** in the research — a
  dedicated method card is the spec's plan.
- **Do NOT model a flat 34% rate** for a JCP-paying company — the effective rate is
  structurally lower.
- JCP caps and rules have been subject to legislative change — confirm current rules when
  the card is built.

## Related concepts

- [[fies-prouni-mechanics]] — PROUNI tax exemption, the education-specific effective-rate lever
- [[ebitda-al-ifrs16]] — separate metric, but both shape the path from EBITDA to net income/FCFF

## Provenance
- Method cards: cross-cutting (spec calls for a dedicated JCP/effective-tax card)
- Sources: project spec (`docs/project_specification.md`, third-round decisions — JCP/effective tax dedicated card); Brazilian tax law (IRPJ/CSLL, Lei 9.249/95) — round-3 verification gap
- Confidence: ⚠️ to-verify (round-3 agenda; spec-mandated dedicated card)

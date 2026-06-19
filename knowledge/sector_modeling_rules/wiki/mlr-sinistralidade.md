---
concept: mlr-sinistralidade
title: MLR / Sinistralidade
theme: sector-kpi
applies_to: [healthcare]
confidence: seed
status: draft
---

# MLR / Sinistralidade

**What it is.** **Sinistralidade** (the Brazilian analogue of the **medical loss ratio,
MLR**) is the share of health-plan premiums spent on medical claims — the **core margin
driver for health plans/operadoras** — where a lower ratio means more premium retained as
margin, and where verticalization (owning the hospitals) is the structural lever to
lower it.

## Core idea

A health plan collects premiums and pays claims. The single number that gates its margin
is the ratio of claims to premiums:

`Sinistralidade ≈ claims (sinistros) ÷ premiums (receita de contraprestações)`

(The US MLR is the same idea: premiums spent on claims + quality improvement.) A rising
sinistralidade compresses margin directly; medical inflation pushes it up, and pricing
power is constrained by **ANS** readjustment caps on individual plans. The structural
counter-lever is **verticalization** — owning hospitals/clinics so that a plan's claims
are partly internal cost rather than third-party payouts (the Hapvida/GNDI thesis).

## Applies to sectors

- **Healthcare (health plans/operadoras)** — the swing factor for plan margins.
- The hospital and diagnostics sub-verticals have different drivers (beds × occupancy ×
  ticket; exam volume × ticket); a **verticalized** operator links the plan and hospital
  engines (intra-group claims net out).

## Mechanics / formulas

- `Plan gross margin ≈ 1 − sinistralidade − admin ratio`.
- Verticalization: a portion of claims becomes internal hospital cost → effective
  sinistralidade falls if the owned network is utilized efficiently.

## Modeling implications

- Model **lives (beneficiaries) × premium per life** for revenue, with **sinistralidade**
  as the explicit margin gate and an **admin ratio** alongside.
- For a verticalized group, **link the plan and hospital engines** so own-hospital claims
  net out — do not model it as a pure plan or pure hospital.
- Keep **M&A/roll-up explicit** (goodwill/PPA, IFRS 3) and **out of organic** base-case
  revenue — consolidation is a structural growth driver in Brazilian supplementary health.

## Pitfalls & nuances

- 🟡 Sinistralidade as the core KPI is a **seed** (US MLR definition confirmed; the BR
  analogue and ANS specifics are a round-3 gap).
- **Do NOT ignore ANS price caps** — regulated individual-plan readjustments constrain
  pricing power.
- **Do NOT treat a verticalized operator as a pure plan** — link the engines.

## Related concepts

- [[fies-prouni-mechanics]] — the parallel regulated-BR-service overlay (education)
- [[ifrs-15-performance-obligations]] — plan premiums earned over the coverage period
- [[healthcare]] — the full sector card (M&A roll-up, sub-verticals)

## Provenance
- Method cards: [[healthcare]]
- Sources: [NAIC-MLR — Medical Loss Ratio (NAIC)](https://content.naic.org/insurance-topics/medical-loss-ratio); [PMC-SAUDE-2024 — BMC Health Services Research, BR supplementary-health consolidation (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11483984/)
- Confidence: 🟡 seed (MLR definition confirmed; BR sinistralidade + ANS to verify round 3)

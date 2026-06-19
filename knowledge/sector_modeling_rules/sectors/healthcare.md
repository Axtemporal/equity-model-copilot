---
sector: Healthcare — hospitals, health plans, diagnostics
slug: healthcare
pilots_examples: Rede D'Or, Hapvida, Fleury, Hospital Care
coverage: partial
key_standards: IFRS 15, IFRS 3 (business combinations), ANS regulation
status: draft
---

# Healthcare — sector method card

## 1. Core thesis
Brazilian supplementary health is a **consolidation story**: **M&A/roll-up** is a
structural growth driver that must be modeled **explicitly** (scenario + goodwill/PPA),
not buried in organic growth. Within it, three sub-verticals have different drivers —
**hospitals** (beds × occupancy × ticket), **health plans/operadoras** (lives × premium,
gated by **sinistralidade**), **diagnostics** (exam volume × ticket). The M&A driver is
verified; the operating KPIs and ANS regulation are ⚠️ not yet sourced.

## 2. Operational drivers (the revenue build), by sub-vertical
- **Hospitals** ⚠️ — revenue ≈ **beds (operational) × occupancy rate × ticket médio**
  (avg revenue per admission); watch **ALOS** (average length of stay) and a
  **bed ramp/maturation curve** for new hospitals; payer mix.
- **Health plans / operadoras** ⚠️ — **lives (beneficiaries) × premium per life**; margin
  gated by **sinistralidade** (claims ÷ premiums — the Brazilian analogue of the
  **MLR**); admin ratio; **verticalization** (owning hospitals lowers claims cost — the
  Hapvida/GNDI thesis).
- **Diagnostics (Fleury)** ⚠️ — **exam/test volume × ticket per exam**; units / PSCs
  (patient service centers); B2B vs B2C mix.

## 3. Mandatory KPIs & disclosures
- **Sinistralidade / MLR** — the core margin driver for health plans (premiums spent on
  claims + quality improvement). 🟡
  > source: [NAIC-MLR] — seed 🟡 (US MLR definition; the BR sinistralidade analogue).
- Hospitals: beds, occupancy, ticket médio, ALOS. ⚠️
- Plans: beneficiaries, premium/life, sinistralidade, admin ratio. ⚠️
- Diagnostics: exam volume, ticket, units. ⚠️
- M&A pipeline / goodwill & PPA. ✅

## 4. Peculiar accounting / normative rules
- **M&A intensity & IFRS 3** ✅ — consolidation is a **structural growth driver** in
  Brazilian supplementary health (~494 transactions 2018-2022, peak ~165 in 2021; Rede
  D'Or top acquirer ~46 operations; Hapvida beneficiaries +250% over 2011-2022). It is
  best modeled via **scenario / roll-up assumptions and goodwill/PPA mechanics (IFRS 3)**,
  **not baked into base-case organic revenue**. Medical inflation (~14%, illustrative)
  accelerates consolidation.
  > source: [PMC-SAUDE-2024] — verified ✅ (3-0). Numbers are dated illustrations.
- **Relative valuation (EV/EBITDA) predominates** over DCF for these deals; the market is
  highly concentrated (Hapvida, Bradesco Saúde, GNDI, Amil, SulAmérica). 🟡
- **ANS regulation** ⚠️ — annual price-readjustment caps for individual plans; solvency/
  capital requirements; regulatory risk. Material and **unverified** — confirm in round 2.
- **Revenue recognition (IFRS 15)** ⚠️ — plan premiums earned over the coverage period;
  hospital/diagnostic services at point of delivery; payer disallowances (glosas). ⚠️

## 5. Model structure adaptation
- **Separate engines per sub-vertical** (hospital / plan / diagnostic), since drivers and
  margins differ; a verticalized group (Hapvida) needs the plan and hospital engines
  linked (intra-group claims).
- **Explicit M&A/roll-up block** with goodwill, PPA, and a scenario toggle — kept
  **out of organic** base-case revenue. ✅
- **Sinistralidade** as the plan-margin driver; bed-ramp curves for hospitals. 🟡/⚠️

## 6. Modeling pitfalls
- **Do NOT bury M&A in organic growth** — model acquisitions explicitly with goodwill/PPA.
- **Do NOT ignore sinistralidade** — it is the swing factor for plan margins.
- **Do NOT ignore ANS price caps** — regulated individual-plan readjustments constrain
  pricing power.
- **Do NOT treat a verticalized operator as a pure plan or pure hospital** — link the
  engines (own-hospital claims net out).

## 7. Confidence & open questions
- ✅ **Verified:** M&A/consolidation as a structural driver; model via scenario +
  goodwill/PPA, not organic.
- 🟡 **Seed:** sinistralidade/MLR as the core plan KPI; EV/EBITDA-based valuation; market
  concentration.
- ⚠️ **To verify (round 2):** hospital KPIs (beds, occupancy, ticket, ALOS); plan
  mechanics (premium/life, sinistralidade benchmarks, verticalization economics);
  diagnostics KPIs; **ANS regulation** (readjustment caps, solvency); glosas.
- Regulated-BR-service and roll-up parallels with [[education]].

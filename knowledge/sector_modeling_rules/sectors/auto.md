---
sector: Auto / OEM manufacturers
slug: auto
pilots_examples: Tesla (user reference model); legacy OEMs
coverage: partial
key_standards: IFRS 15, IAS 38 / ASC 730, IAS 16
status: draft
---

# Auto / OEM manufacturers — sector method card

## 1. Core thesis
An automaker's operating model is **units × ASP** at a **gross-margin-per-vehicle**,
against **lumpy, capacity-driven plant capex**; but the two things that break the
generic model are **revenue timing** (recognized at the **OEM-to-dealer** sale, not the
consumer sale, with incentives as **contra-revenue**) and **high-margin side lines**
(regulatory credits, software) that must be split out. The unit-economics drivers are
standard but ⚠️ not yet sourced here; the revenue-recognition rules below are verified.

## 2. Operational drivers (the revenue build)
- **Revenue = units sold × ASP**, modeled per model line / region, at a **gross margin
  per vehicle**. ⚠️ (standard, not sourced here).
- **Regulatory credits** (e.g. Tesla ZEV/emission credits) — near-100% gross margin,
  lumpy, and **declining** as competitors electrify; model as a **separate high-margin
  line**, never blended into auto revenue. ⚠️
- Energy / services / software (FSD) as separate segments with their own recognition. ⚠️

## 3. Mandatory KPIs & disclosures
- Units delivered/produced by model & region; ASP; gross margin per vehicle (ex-credits). ⚠️
- Production capacity & utilization per plant. ⚠️
- Regulatory-credit revenue (disclosed separately). ⚠️
- Deferred revenue for software/FSD; RPO. ⚠️

## 4. Peculiar accounting / normative rules (verified core)
- **Revenue recognition — point-in-time at OEM-to-dealer control transfer** ✅ — the
  **dealer (not the end consumer) is the customer**; revenue is recognized when control
  transfers to the dealer (vehicles made available / released to the carrier),
  requiring case-by-case analysis of dealership agreements against IFRS 15.38's **five
  non-determinative control indicators**. **Consignment** arrangements where the dealer
  does not obtain control **defer** revenue. So the operating model's revenue timing is
  the **wholesale (OEM-to-dealer)** sale.
  > source: [EY-AUTO-IFRS15] — verified ✅ (3-0).
- **Incentives are contra-revenue** ✅ — cash sales incentives (rebates, bonuses) paid to
  dealers/customers **reduce the transaction price** → **contra-revenue** (variable
  consideration if it varies; a fixed discount if not contingent), **NOT** a
  marketing/opex expense. The model must **net incentives against revenue**. Carve-out:
  payment for a distinct good/service from the customer is a separate purchase.
  > source: [EY-AUTO-IFRS15] — verified ✅ (2-0).
- **R&D / development capitalization** ✅ — **IAS 38**: research expensed, development
  capitalized only if all six criteria met; **US GAAP ASC 730**: R&D expensed as
  incurred. Read the issuer's framework (**Tesla = US GAAP / ASC 730**) to model
  capitalized development and amortization.
  > source: [KPMG-RD-2025] — verified ✅ (3-0).

## 5. Model structure adaptation
- **Volume × ASP × margin per model/region**, with **regulatory credits and software as
  separate lines/segments** (different margins and recognition).
- **Capex as a step-function** — gigafactory/plant capex is **lumpy and capacity-driven**
  (a new plant is a discrete event), **not** a smooth % of revenue. Model capacity
  additions explicitly and tie depreciation to the plant roll-forward. ⚠️
- Deferred-revenue schedule for software/FSD recognized over time. ⚠️

## 6. Modeling pitfalls
- **Do NOT recognize revenue at the consumer sale** — it is at the OEM-to-dealer transfer.
- **Do NOT classify customer incentives as opex** — they are contra-revenue.
- **Do NOT blend regulatory credits into auto gross margin** — they are a separate,
  high-margin, declining line; blending overstates core auto profitability.
- **Do NOT model gigafactory capex as a flat % of revenue** — it is lumpy and
  capacity-driven.

## 7. Confidence & open questions
- ✅ **Verified:** IFRS 15 point-in-time OEM-to-dealer recognition; incentives as
  contra-revenue; IAS 38 vs ASC 730 R&D capitalization.
- ⚠️ **To verify (round 2):** units × ASP × margin-per-vehicle benchmarks; capacity
  utilization; gigafactory capex step-function sizing; regulatory-credit trajectory;
  software/FSD deferred-revenue mechanics.
- **GitHub reference (low/dated value):** [REPO-JWOLBERG] jwolberg/Equity-Valuation-Model
  has two **2019** Tesla Excel models — generic three-statement + WACC + competitive
  analysis, **no license (all rights reserved → do not copy)**, no documented
  auto-specific driver tree. Treat as a **structure-only** reference, not a source of
  rules.
- Shares software/deferred-revenue + R&D capitalization with [[tech_saas]].

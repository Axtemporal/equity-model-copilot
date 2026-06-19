---
sector: Pulp & paper
slug: pulp_paper
pilots_examples: Suzano, Klabin, Irani
coverage: partial
key_standards: IAS 41, IAS 16, IAS 2, IFRS 16
status: draft
---

# Pulp & paper — sector method card

## 1. Core thesis
A market-pulp producer is a **USD commodity** play: value is driven by the **net China
CIF pulp price × BRL/USD FX**, against a **cash cost per tonne** that is heavily
**oil-linked**, modeled **per business unit** (market pulp vs paper) in tonnes ×
utilization × EBITDA/t. The **planted forest** is an **IAS 41 biological asset** whose
fair-value swings are non-cash and must be isolated. The accounting is verified; the
operating drivers are a single-source **seed**.

## 2. Operational drivers (the revenue/margin build) — 🟡 seed
From a single research source ([XP-PULP-2022], Dec 2022, **not re-verified**); numbers
are dated illustrations — encode the **method**:
- **Primary value drivers: net China CIF pulp price (BHKP/BEKP hardwood, US$/t) ×
  BRL/USD FX** — **pulp price is the larger lever**. 🟡
- Model **per business unit** (market pulp vs paper): **capacity (tonnes) × utilization
  rate × EBITDA/tonne**. 🟡
- **Cash cost per tonne** is the core cost metric and is heavily **oil-linked**
  (~50% of cash cost oil-related via chemicals/inputs) → a **Brent assumption feeds
  cash cost**. 🟡
- **FX is structural**: revenue ~100% USD-linked vs costs partly BRL → a leveraged
  long-USD exposure; model revenue-side and cost-side FX sensitivity **separately**. 🟡
> source: [XP-PULP-2022] — seed 🟡 (single source, not re-confirmed).

## 3. Mandatory KPIs & disclosures
- Net pulp price (China CIF BHKP), BRL/USD, by BU. 🟡
- Capacity (tonnes), utilization, sales volume, EBITDA/tonne. 🟡
- Cash cost per tonne (and its oil linkage). 🟡
- Biological-asset fair value & P&L impact (IAS 41). ✅
- EBITDA vs EBITDA-AL (IFRS 16). ⚠️

## 4. Peculiar accounting / normative rules (verified core)
- **IAS 41 — planted forests at fair value** ✅ — biological assets at **fair value less
  costs to sell**, with changes in **P&L** → a **non-cash line to isolate** from
  operating EBITDA.
  > source: [IAS-41] — verified ✅ (3-0).
- **Critical classification** ✅ — **eucalyptus planted for pulp is harvested whole
  (felled = consumed)**, so it is a **CONSUMABLE biological asset that STAYS UNDER
  IAS 41 at fair value**. The **June 2014 bearer-plant carve-out to IAS 16 does NOT
  apply** (bearer plants bear produce repeatedly without being felled; pulp eucalyptus
  is cut down). Do **not** route pulp forests to IAS 16 depreciation.
  > source: [IAS-41-BP-2014] — verified ✅ (3-0).
- **Inventory (IAS 2)** and **IFRS 16** leases as elsewhere. ⚠️

## 5. Model structure adaptation
- **Per-BU engine** (market pulp vs paper): tonnes × utilization × (price − cash cost/t),
  with **separate FX sensitivity on revenue vs cost**.
- **Brent → cash cost** linkage block (chemicals/inputs). 🟡
- **Separate IAS 41 fair-value line** for the forest, excluded from operating EBITDA. ✅
- **New-capacity ramp curves** for projects coming online; forestry as a possible
  land/NAV component. ⚠️

## 6. Modeling pitfalls
- **Do NOT depreciate pulp eucalyptus under IAS 16** — it is a consumable IAS 41 asset.
- **Do NOT leave forest fair-value swings in operating EBITDA** — isolate the non-cash line.
- **Do NOT net FX** — revenue (USD) and cost (partly BRL) have different sensitivities;
  model them separately.
- **Do NOT hardcode XP's dated price/FX/Brent deck** — it is a single-source 2022 seed;
  encode the method, confirm the numbers.

## 7. Confidence & open questions
- ✅ **Verified:** IAS 41 fair-value forest accounting; consumable-vs-bearer
  classification (pulp eucalyptus stays IAS 41).
- 🟡 **Seed (single source, confirm):** pulp price × FX as primary drivers; per-BU tonnes
  × utilization × EBITDA/t; oil-linked cash cost; structural USD/BRL asymmetry.
- ⚠️ **To verify (round 2):** pulp cycle position; integrated vs market-pulp economics;
  capacity-ramp curves; wood cost & logistics; energy self-generation (black liquor).
- Shares IAS 41 with [[agriculture]]; shares cyclical USD-commodity + FX with
  [[petrochemicals]] and [[steel]].

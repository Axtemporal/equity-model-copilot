---
sector: Agricultural inputs / insumos agrícolas
slug: agri_inputs
pilots_examples: 3tentos (pilot); Nutrien (disclosure benchmark); fertilizers, crop protection, seeds
coverage: verified core
key_standards: IAS 2, IFRS 15
status: draft
---

# Agricultural inputs (insumos agrícolas) — sector method card

## 1. Core thesis
The business splits into **upstream nutrient production** (commodity economics — tonnes
× price − cash cost) and **downstream retail/distribution** (a working-capital-heavy,
**seasonal** ag-services business). Model the two **separately**, and treat working
capital as a first-class, season-driven driver. **Caveat:** the verified evidence below
is from a **global producer (Nutrien)**; a Brazilian distributor like **3tentos** adds
barter/originação and resale dynamics that are ⚠️ not yet sourced.

## 2. Operational drivers (the revenue/margin build)
- **Segment first** ✅ — Nutrien reports four segments: **Retail** (Ag Solutions =
  distribution/ag-services, downstream), **Potash**, **Nitrogen**, **Phosphate**
  (upstream, differentiated by chemical nutrient K/N/P), each with adjusted EBITDA.
  > source: [NUTRIEN-FY2024] — verified ✅ (3-0).
- **Upstream build** ✅ — revenue = **volume (tonnes) × net selling price**;
  margin = **net selling price − cash cost per tonne**. Issuers disclose tonnage, avg
  net selling price/t, and controllable cash cost of production/t.
  > source: [NUTRIEN-FY2024] — verified ✅ (3-0). Dated illustration: Potash FY24
  > ~13,886 kt at ~US$215/t net, ~US$54/t controllable cash cost — **do not hardcode**.
- **Downstream/retail build** ✅ — a **working-capital-intensive, seasonal** business;
  model with a **working-capital-to-sales** driver (an **average** ratio, not a
  year-end snapshot) tied to the crop-application calendar.
  > source: [NUTRIEN-FY2024] — verified ✅ (2-1). Illustration: Nutrien Retail adjusted
  > avg WC/sales ~20%.

## 3. Mandatory KPIs & disclosures
- Segment revenue & adjusted EBITDA (Retail / Potash / Nitrogen / Phosphate). ✅
- Per-nutrient: volume (t), net selling price/t, cash cost/t, gross margin/t. ✅
- Working-capital-to-sales (average). ✅
- For a BR distributor: originação volumes, resale margin, grain inventory. ⚠️

## 4. Peculiar accounting / normative rules
- **Inventory (IAS 2)** — input inventory at cost; for a distributor taking grain as
  payment, **grain inventory introduces commodity-price exposure** on the balance sheet. ⚠️
- **Revenue recognition (IFRS 15)** — distribution revenue at delivery; barter/exchange
  transactions need careful gross-vs-net treatment. ⚠️
- Seasonality means quarter-end balances are not representative — use average ratios. ✅

## 5. Model structure adaptation
- **Two engines:** an upstream commodity engine (tonnes × price − cash cost/t per
  nutrient) and a downstream retail engine (sales × margin, with a heavy WC schedule).
- **Brazilian distributor (3tentos) overlay** ⚠️ — three interlocking businesses:
  **input retail** + **grain origination (originação/barter)** + **industrialization**
  (e.g. soy crushing / biodiesel). Barter means inputs are paid for in grain →
  the model needs a grain-inventory + commodity-price-exposure line and farmer **credit
  risk**; revenue mixes **resale spreads** on third-party inputs with own-industrial
  margin. FX hits imported fertilizer cost.
- Self-adapting granularity: collapse to the segment grain the issuer discloses.

## 6. Modeling pitfalls
- **Do NOT model as one consolidated line** — upstream commodity and downstream retail
  have different drivers and margins.
- **Do NOT use year-end working capital** — it is seasonal; use an average WC-to-sales.
- **Do NOT ignore barter/originação for a BR distributor** — it puts grain price risk on
  the input seller's balance sheet (a 3tentos-specific exposure not present at Nutrien).
- **Do NOT confuse a global producer's economics with a distributor's** — margin
  structure differs (production margin vs resale spread).

## 7. Confidence & open questions
- ✅ **Verified:** four-segment split; upstream tonnes × net price − cash cost/t;
  seasonal WC-to-sales driver — **all from Nutrien (global producer).**
- ⚠️ **To verify (round 2, 3tentos-specific):** barter/originação mechanics and grain
  inventory accounting; resale spread benchmarks; the three-business model integration;
  Brazilian safra/safrinha seasonality; farmer credit risk / PCLD; FX on imports.
- Customer is the farmer — see [[agriculture]]; distribution/WC parallels with
  [[fuel_distribution]].

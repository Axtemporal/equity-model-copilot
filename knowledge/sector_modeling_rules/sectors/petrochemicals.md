---
sector: Petrochemicals
slug: petrochemicals
pilots_examples: Braskem, Unipar
coverage: verified
key_standards: IFRS 15, IAS 2, IFRS 16
status: draft
---

# Petrochemicals — sector method card

## 1. Core thesis
A petrochemical producer's earnings are driven by the **spread** between its product
price and its feedstock cost, not by an absolute price — and that spread is deeply
**cyclical**. So the model is built around **per-route spreads × capacity utilization**,
and the company is valued on **normalized mid-cycle earnings**, never on spot/trough
EBITDA. Spot earnings near a trough look cheap on near-term multiples but understate
(or overstate) through-cycle power.

## 2. Operational drivers (the revenue/margin build)
Replace generic price×volume with a spread-and-utilization build:

- **Spread (US$/t)** = product price − feedstock cost, defined **per production route**:
  - **PE-Naphtha** (Brazil — naphtha-fed polyethylene)
  - **PE-Ethane** (Mexico — ethane-fed; the most cost-competitive feedstock)
  - **PP-Propylene** (US / Europe)
- The **spread replaces the PRICE** component; **volume is still capacity × utilization
  (operating) rate** per product per site.
- **Revenue/EBITDA** is then spread × volume, summed across routes/products.
> source: [XP-PETCHEM-2023] — verified ✅ (3-0). Dated illustration only: XP Brazil
> PE-Naphtha ~US$250/t in 2H23 rising to ~US$400/t (real) from 2025 — **do not hardcode**.

## 3. Mandatory KPIs & disclosures
- **Reference spreads (US$/t) per route** — the headline driver the market tracks. ✅
- **Capacity (kty) per product per site** and **utilization / operating rate**. ✅
- **Normalized / mid-cycle EBITDA** and through-cycle EV/EBITDA. ✅
- Feedstock mix (naphtha vs gas/ethane) and integration ratio. ⚠️
- EBITDA and **EBITDA-AL** (IFRS 16) per the project's lease decision. ⚠️

## 4. Peculiar accounting / normative rules
- **Cyclical-commodity valuation** ✅ — value on **normalized/mid-cycle EBITDA at real
  (CPI-adjusted) mid-cycle spreads**, kept in a **separate mid-cycle assumption block**
  distinct from the near-term forecast. (Corroborated by Damodaran, *Valuing Cyclical
  and Commodity Companies*, and industrials IB primers.)
  > source: [XP-PETCHEM-2023] — verified ✅ (2-0). Illustration: XP valued on
  > EV/normalized-2030 EBITDA, normalization assumed from ~2025.
- **Inventory (IAS 2)** — like fuel distribution, average-cost inventory can create
  price-driven inventory gains/losses that distort a single quarter's margin. ⚠️
- **IFRS 16 leases** — report EBITDA and EBITDA-AL; leases in the EV→equity bridge per
  the spec. ⚠️
- Revenue recognition (IFRS 15) at control transfer on bulk shipments. ⚠️

## 5. Model structure adaptation
**Adapt to each business unit's INTEGRATION level** ✅ — this is a textbook case of the
project's "self-adapting granularity" differential:
- **Non-integrated unit** → model as a **single input-to-output spread** (e.g. USA PP
  minus Propylene; Mexico PE minus Ethylene).
- **Integrated unit** (Braskem Brazil) → **multi-feedstock / multi-product** structure,
  because ~30–40% of revenue is **non-resin by-products** and ~60% of ethylene is
  naphtha-based. One spread line cannot capture it.
- Model **capacity per product per site (kty)**; the template collapses to the grain the
  issuer discloses.
> source: [XP-PETCHEM-2023] — verified ✅ (3-0).

## 6. Modeling pitfalls
- **Do NOT use a single product price** — use the route spread (price − feedstock).
- **Do NOT value on spot/near-term EBITDA** at a cycle trough or peak — use normalized
  mid-cycle spreads in a separate block.
- **Do NOT collapse an integrated producer to one spread** — by-products and mixed
  feedstock require multi-product structure.
- **Do NOT hardcode a bank's dated spread/price deck or exit multiple** — encode the
  method; the numbers drift.

## 7. Confidence & open questions
- ✅ **Verified:** per-route spreads × utilization; normalized mid-cycle valuation;
  integration-level model adaptation.
- ⚠️ **To verify (round 2):** exact feedstock-cost linkage to oil/naphtha; FX split
  (USD-linked product prices vs partly-BRL cost for Braskem); inventory-effect
  reporting; IFRS 16 EBITDA-AL mechanics for this sector.
- Shares the **cyclical USD-commodity + FX** problem with [[steel]] and [[pulp_paper]];
  feedstock ties to [[oil_and_gas]].

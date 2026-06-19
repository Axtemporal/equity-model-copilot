---
sector: Fuel distribution / distribuição de combustíveis
slug: fuel_distribution
pilots_examples: Vibra (BR), Raízen (Shell BR), Ultrapar/Ipiranga
coverage: verified core
key_standards: IAS 2 (inventory), IFRS 15, ANP regulation
status: draft
---

# Fuel distribution (distribuição de combustíveis) — sector method card

## 1. Core thesis
A fuel distributor is a **thin-margin, high-volume logistics** business: profitability is
measured as **margin per cubic metre (R$/m³)**, **not** as a % of a huge pass-through
revenue. The two things that break the generic model are the **inventory effect**
(weighted-average-cost accounting makes COGS lag spot prices, creating non-recurring
holding gains/losses) and **large, price-sensitive working capital** driven by inventory
positioning. Always separate a **recurring margin** from the **reported margin**.

## 2. Operational drivers (the gross-profit build)
- **Profit measured in R$/m³, not % of revenue** ✅ — model gross profit as
  **volume (m³) × margin per m³**, by product (gasoline, diesel S10/S500, hydrous/anhydrous
  ethanol, jet fuel / QAV). Revenue is dominated by pass-through fuel cost, so revenue and
  % margins mislead.
  > source: [VIBRA-2Q25] — verified ✅ (3-0). Dated illustration: Vibra 2Q25 reported
  > adjusted EBITDA margin R$143/m³, recurring ~R$161/m³ — **method, not the number**.
- **Reported vs recurring margin** ✅ — the recurring margin **strips out** (i) asset-sale
  /tax gains and (ii) the **inventory effect**. Model and present **both**.
  > source: [VIBRA-2Q25] — verified ✅ (3-0).
- **Volume** ⚠️ — total fuel demand (GDP/fleet-linked) × **market share**; posto (station)
  count and same-store throughput; B2B (TRR, aviation, large fleets) vs retail split.

## 3. Mandatory KPIs & disclosures
- **Margin per m³** (reported and recurring/ex-inventory) — the headline KPI. ✅
- Volume (m³) by product and channel (retail network vs B2B). ⚠️
- Inventory effect (R$/m³ and R$ on net income). ✅
- Working capital and net debt (both swing with fuel price). ✅
- Station/posto count; same-store volume. ⚠️

## 4. Peculiar accounting / normative rules
- **Inventory effect via weighted-average cost (IAS 2)** ✅ — IAS 2 permits only **FIFO or
  weighted-average cost** (LIFO prohibited); distributors carry **weighted-average cost**,
  so when fuel prices move the **average cost LAGS spot**, producing **holding gains**
  (rising prices) or **losses** (falling prices) in reported margin/net income.
  > source: [IAS-2] — verified ✅ (3-0).
- **Isolate the inventory effect** ✅ — it **materially distorts reported net income**, so
  strip it to read recurring profitability (illustration: Vibra 2Q25 adjusted net income
  R$493mn reported vs ~R$1bn ex-inventory effect; driven by import **parity open→closed**).
  > source: [VIBRA-2Q25] — verified ✅ (3-0).
- **⚠️ Do NOT attribute inventory losses to the IAS 2 lower-of-cost-and-NRV writedown** ✅
  (verified as a refutation) — LCNRV is a *separate* mechanism that only bites when selling
  price falls **below** carrying cost (negative margin). The recurring inventory
  gain/loss is the **cost-flow lag** under weighted-average cost, **not** an NRV writedown.
  Keep the two distinct.
  > source: refuted claim, [IAS-2] — verified ✅ (3-0 refuted).
- **ANP regulation** ⚠️ — biofuel blend mandates (anhydrous ethanol in gasoline; biodiesel
  in diesel), informal-market competition, **ICMS** monofásico regime.
- **Revenue recognition (IFRS 15)** at delivery; gross-vs-net for pass-through fuel. ⚠️

## 5. Model structure adaptation
- **Drive gross profit off volume × R$/m³ by product**; carry revenue as a large
  low-signal pass-through. Show a **recurring-margin line (ex-inventory-effect, ex-asset/
  tax gains)** beside reported.
- **Inventory-effect line** tied to fuel-price/parity moves, feeding both margin and net
  income — explicitly non-recurring. ✅
- **Price-aware working-capital schedule** ✅ — WC is dominated by **inventory positioning**
  (holding above/below plan vs import parity); a deliberate build consumes cash that
  **reverses next quarter** (~45-day normalization). Do not model WC as a flat % of
  revenue.
  > source: [VIBRA-2Q25] — verified ✅ (3-0).

## 6. Modeling pitfalls
- **Do NOT use % gross margin on revenue** — the pass-through makes it meaningless; use R$/m³.
- **Do NOT treat the inventory effect as recurring margin** — strip it (and asset/tax gains).
- **Do NOT confuse the inventory cost-flow lag with an IAS 2 NRV writedown** — different
  mechanisms (verified).
- **Do NOT model working capital as a flat % of revenue** — it is inventory-positioning and
  price-driven, and mean-reverts within ~a quarter.
- **Do NOT ignore blend mandates / ICMS monofásico** — they shift volumes and margins.

## 7. Confidence & open questions
- ✅ **Verified (round 2):** R$/m³ recurring-vs-reported margin; inventory effect distorts
  net income (isolate it); IAS 2 weighted-average-cost mechanism (and the LCNRV
  distinction); inventory-positioning working capital. Core mechanics now solid.
- ⚠️ **To verify (round 3):** margin-per-m³ benchmarks per product and per peer (Raízen,
  Ultrapar) — round-2 evidence is Vibra-centric; ANP blend-mandate and ICMS monofásico
  mechanics; B2B vs retail margin split; volume/market-share drivers.
- Upstream supplier link to [[oil_and_gas]]; distribution/WC parallels with [[agri_inputs]].

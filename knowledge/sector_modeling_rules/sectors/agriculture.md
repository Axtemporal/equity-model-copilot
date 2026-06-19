---
sector: Agriculture / row-crop producers
slug: agriculture
pilots_examples: SLC Agrícola, BrasilAgro (soybean, corn, cotton)
coverage: verified core
key_standards: IAS 41, IAS 16, IAS 2
status: draft
---

# Agriculture (row-crop producers) — sector method card

## 1. Core thesis
A crop producer's reported earnings carry **non-cash fair-value swings** from
**IAS 41 biological assets** that must be **isolated from operating results**, and its
operating value is driven by **area × yield × price** plus the often-separate value of
**owned farmland**. The accounting (fair value through P&L) is the peculiarity that
breaks the generic model; the operating build (hectares × yield) is standard but not yet
sourced here.

## 2. Operational drivers (the revenue build)
- **Revenue ≈ hectares planted × yield (t/ha) × price per crop**, per crop (soy, corn,
  cotton), with the **safra calendar** driving timing. ⚠️ (standard, not sourced here).
- **Land** is a distinct value lever: SLC **owns** and **leases** land; owned farmland
  appreciation is a **real-estate-like NAV component often valued separately** from the
  farming operation. ⚠️
- Input costs link to [[agri_inputs]]; commodity price + FX (CBOT/B3 soybean in USD)
  and hedging drive realized price. ⚠️

## 3. Mandatory KPIs & disclosures
- Hectares planted by crop; yield (t/ha = produtividade); production (t). ⚠️
- Realized price per crop; hedge position. ⚠️
- Biological-asset fair value and its P&L impact (IAS 41 disclosure). ✅
- Owned vs leased area; land carrying value / appraised value. ⚠️

## 4. Peculiar accounting / normative rules (the core of this card)
- **IAS 41 — biological assets at fair value** ✅ — biological assets **and agricultural
  produce at harvest** are measured at **fair value less costs to sell (FVLCTS)**,
  distinct from cost-based IAS 2 inventory, and **fair-value changes flow through profit
  or loss (never OCI)**. This injects **non-cash earnings volatility** the model **must
  isolate** from operating EBIT/EBITDA. Harvest FVLCTS becomes the **deemed cost** for
  IAS 2 inventory thereafter. Note the **IAS 41.30 cost-model carve-out** (used when
  fair value is not reliably measurable).
  > source: [IAS-41] — verified ✅ (3-0).
- **Consumable vs bearer biological assets** ✅ — **annual row crops (soy, corn, cotton)
  are CONSUMABLE biological assets** (harvested whole) → they **stay under IAS 41 at
  FVLCTS**. The **June 2014 bearer-plant carve-out to IAS 16 does NOT apply** to them
  (bearer plants — grape vines, rubber trees, oil palms, tea bushes, fruit trees — bear
  produce repeatedly for >1 period and are depreciated under IAS 16; the produce growing
  on them stays IAS 41). State this distinction so the engine routes annual crops to
  IAS 41 and any perennial/orchard assets to IAS 16.
  > source: [IAS-41-BP-2014] — verified ✅ (3-0).

## 5. Model structure adaptation
- **Operating P&L on a cash/cost basis** with a **separate, clearly-labeled IAS 41
  fair-value line** (gain/loss on biological assets) excluded from operating EBITDA — so
  the analyst sees real margin, not mark-to-market noise.
- **Per-crop operating build** (hectares × yield × price − cost/ha), adapting to the
  crops and farms the issuer discloses.
- **Land as a separate NAV block** (owned farmland at cost or appraised value), distinct
  from the farming DCF — a sum-of-the-parts where land can dominate. ⚠️

## 6. Modeling pitfalls
- **Do NOT leave IAS 41 fair-value swings inside operating EBITDA** — they are non-cash
  and volatile; isolate them.
- **Do NOT apply the bearer-plant/IAS 16 treatment to annual row crops** — those are
  consumable IAS 41 assets.
- **Do NOT ignore owned land value** — for SLC it can be a large part of NAV, valued
  separately from operations.
- **Do NOT model flat yields** — yield varies with weather/safra; price and FX are
  volatile and often hedged.

## 7. Confidence & open questions
- ✅ **Verified:** IAS 41 FVLCTS + P&L recognition; consumable-vs-bearer split (row
  crops stay IAS 41).
- ⚠️ **To verify (round 2):** hectares × yield × price operating benchmarks; farmland
  valuation method and owned-vs-leased split; hedging treatment; how SLC reports the
  land NAV vs operating value.
- Shares IAS 41 with [[pulp_paper]] (planted forests); input cost links to [[agri_inputs]].

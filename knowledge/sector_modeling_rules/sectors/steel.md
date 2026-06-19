---
sector: Steel / Siderurgia
slug: steel
pilots_examples: Gerdau, CSN, Usiminas
coverage: verified
key_standards: IAS 2, IFRS, IFRS 16
status: draft
---

# Steel (Siderurgia) — sector method card

## 1. Core thesis
Steel revenue is not "one domestic price × tonnes." Realized prices **systematically
diverge** from any single reference, and demand/supply only make sense **decomposed by
product family** with imports explicitly in the balance. Build the model as
**volume by product family** (from an apparent-demand identity) × **realized price =
reference index + premium**, with **import penetration** as the key pricing-power lever.

## 2. Operational drivers (the revenue build)
- **Volume by product family** ✅ — split **flat** (HRC, CRC, galvanized, pre-painted)
  vs **long** (rebar, wire rod). Build **apparent demand = domestic sales + imports
  (− exports)** per family. Import penetration differs sharply by family (illustrative
  Sep'25: flat ~22% vs long ~12% of apparent demand).
  > source: [XP-METALS-2025] — verified ✅ (3-0).
- **Realized price = reference index (Platts) + price premium** ✅ — realized unit
  revenue diverges from the reference, so model an index plus a structural premium
  (Brazilian domestic flat steel carries a ~20–25% premium; illustrative quarterly
  diffs ~ −1.3 to +9.5 p.p. across Gerdau/Usiminas/CSN). **Do not** use the bare
  reference index as realized price.
  > source: [XP-METALS-2025] — verified ✅ (2-0).
- **Import penetration & import price parity** (domestic vs landed imported price incl.
  taxes) drive domestic pricing power; antidumping investigations shift import flows. ✅

## 3. Mandatory KPIs & disclosures
- Volumes (kt) by product family: production, domestic sales, exports, imports,
  apparent demand. ✅
- Import penetration (%) and import price parity (%) per family. ✅
- Realized price/t vs reference index; price premium. ✅
- Capacity utilization; metallic spread; cost/t. ⚠️

## 4. Peculiar accounting / normative rules
- **Inventory (IAS 2)** — raw-material (iron ore, coking coal, scrap) and finished-steel
  inventory at average cost; price moves create timing effects in COGS. ⚠️
- **IFRS 16** — EBITDA vs EBITDA-AL per the spec. ⚠️
- Vertical-integration accounting (own iron ore/coke transferred at cost) affects
  segment margins. ⚠️

## 5. Model structure adaptation
- **Volume tables per product family** feeding an apparent-demand block (production +
  imports − exports), then realized price = index + premium per family.
- **Metallic spread** view (steel price − metallic/raw-material cost) as the margin
  driver; **vertical integration** (Gerdau/CSN own iron ore & coke vs Usiminas) modeled
  as a cost advantage. ⚠️
- Capacity & utilization per plant; product mix shift (flat vs long, value-added). ⚠️

## 6. Modeling pitfalls
- **Do NOT use a single domestic price** — realized price = reference + premium, per
  product.
- **Do NOT model steel as one homogeneous tonne** — flat vs long differ in demand,
  imports, and pricing power.
- **Do NOT ignore imports** — apparent demand and import penetration are central.
- **REFUTED — do NOT encode:** "EV/EBITDA at 3–5x is THE valuation anchor for Brazilian
  steel." This failed verification (0-2). EV/EBITDA is **a cross-check**, not the
  defining method (use FCFF DCF as the primary per the spec, with multiples as a sanity
  check).
  > source: refuted claim, see [`_sources.md`](../_sources.md).

## 7. Confidence & open questions
- ✅ **Verified:** volume by product family + apparent-demand identity; realized price =
  index + premium; import penetration as a pricing driver.
- ⚠️ **To verify (round 2):** metallic-spread definitions per issuer; capacity
  utilization; vertical-integration cost economics (iron ore/coke); mix effects; IFRS 16
  treatment.
- Raw material links to [[metals_mining]] (iron ore); cyclical-commodity valuation
  parallels [[petrochemicals]].

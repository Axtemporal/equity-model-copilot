---
sector: Metals & mining
slug: metals_mining
pilots_examples: Vale (iron ore, nickel, copper), CSN Mineração, CBA
coverage: verified core
key_standards: JORC / CRIRSCO, IFRS 6, CFEM (royalty)
status: draft
---

# Metals & mining — sector method card

## 1. Core thesis
A miner, like an E&P company, is worth the **certified reserves** it can mine, priced at
a commodity reference net of a **per-tonne cash cost** whose position on the **global
cost curve** decides who survives the trough. Build it **per asset (per mine)** on a
**reserve-bounded production schedule × (reference price ± grade premium) − C1 cash
cost**. The reserves logic closely mirrors [[oil_and_gas]]; the cost-curve and pricing
mechanics are ⚠️ not yet sourced here.

## 2. Operational drivers (the revenue/margin build)
- **Production (Mt)** = reserve-bounded mine schedule (parallel to O&G). ⚠️
- **Realized price** — iron ore at a **62% Fe reference index** (Platts/MB) **± quality
  premium/penalty**; copper/nickel on **LME**. **Provisional pricing** ✅ — shipments
  are invoiced at a **provisional price at delivery**, the receivable re-measured at
  **fair value through P&L** (an embedded derivative) until the contractual **pricing
  period** (generally *later* than the shipment date) sets the final price, with MTM
  changes booked to **sales revenue**. Model an explicit true-up line.
  > source: [VALE-20F-2022] — verified ✅ (round 3, 3-0).
- **C1 cash cost (US$/t)** 🟡 — the core operating-cost metric; plus **AISC** ✅ (all-in
  sustaining cost = cash cost + sustaining capex + corporate G&A + share-based remun. +
  reclamation/inventory adj. − by-product credits; **excludes** growth capex,
  impairments, M&A, financing). **Cost-curve position** drives survival and margin. 🟡
  > source: AISC per [WGC-AISC] — verified ✅ (round 3, 3-0); C1/cost-curve still 🟡.
- **Grade / teor** (e.g. % Fe) drives the price premium and processing economics;
  **strip ratio** (waste:ore) drives mining cost. ⚠️

## 3. Mandatory KPIs & disclosures
- Reserves & resources by confidence tier (JORC/CRIRSCO). ✅
- Production (Mt) by mineral/asset; grade/teor; strip ratio. ⚠️
- C1 cash cost, AISC, cost-curve position. ⚠️
- Realized price vs reference index; provisional-pricing adjustments. ⚠️
- CFEM and other royalties. ⚠️

## 4. Peculiar accounting / normative rules
- **Reserves vs resources (JORC / CRIRSCO)** ✅ — non-additive confidence tiers:
  **Mineral Resources** (Inferred / Indicated / Measured, increasing confidence) vs
  **Ore Reserves** (Probable / Proved). **Value reserves (not resources)**, weighted by
  confidence tier. Mirrors the O&G reserves-vs-resources logic.
  > source: [JORC-2012] — verified ✅ (round 2, 2-0 / 3-0).
- **Resource→Reserve conversion mapping** ✅ — encode the exact paths:
  **Indicated → Probable only**; **Measured → Proved** (high confidence in Modifying
  Factors) **or Probable** (where Modifying Factors carry uncertainty). **Proved Ore
  Reserve** = the economically mineable part of a Measured Resource (highest confidence);
  **Probable** = the economically mineable part of an Indicated (or sometimes Measured)
  Resource — this is the basis for the **2P (Proved + Probable)** tier in valuation.
  > source: [JORC-2012] — verified ✅ (3-0 / 2-0).
- **Modifying Factors** ✅ — Ore Reserves are a *modified subset* of Indicated/Measured
  Resources, converted via the **Modifying Factors**: mining, processing, metallurgical,
  infrastructure, economic, marketing, legal, environmental, social and governmental
  ("not restricted to"). These are what turn a geological resource into a mineable
  reserve usable in a mine plan / DCF/NAV.
  > source: [JORC-2012] — verified ✅ (2-0).
- **Inferred Resources** ✅ — **must NOT be converted to an Ore Reserve** (no direct link
  to Proved or Probable). **Exclude Inferred from the mineable / reserve-backed
  production and DCF base.** (Nuance from verification: resources may still carry option
  value in *some* NAV approaches, but never in the base mine plan — keep them out of the
  reserve-backed schedule.)
  > source: [JORC-2012] — verified ✅ (survived 2-1; one voter flagged "exclude from ANY
  > base" as slight overreach — hence the option-value nuance).
- **IFRS 6 — E&E accounting-policy exemption** ✅ — applies to mining too: issuers set
  their own exploration & evaluation capitalization policy, so the model must **read each
  issuer's stated policy** rather than assume one treatment.
  > source: [IFRS-6] — verified ✅ (3-0).
- **UoP depletion** over the reserve base (parallel to O&G). ⚠️
- **CFEM** (*Compensação Financeira pela Exploração de Recursos Minerais* — Brazilian
  mining royalty) ✅ — constitutionally mandated (Art. 20 §1º, CF/1988); base = **gross
  sale revenue minus commercialization taxes**; rate **by mineral** (iron ore **3.5%**;
  bauxite/manganese/niobium/rock salt 3%; diamond/other 2%; gold 1.5%; aggregates 1%;
  **4% cap**). Model **between gross revenue and net**, per-mineral rate, not flat opex.
  > source: [ANM-CFEM] — verified ✅ (round 3, 3-0). See [[cfem-royalty]] wiki article.

## 5. Model structure adaptation
- **One tab per mine + Corporate, consolidating in SOTP** — matches the reference
  "Model A" multi-asset mining structure; each asset has a reserve roll-forward,
  production schedule, grade, cash cost, and realized price.
- **Reserve roll-forward (corkscrew):** opening − production ± revisions ±
  acquisitions/discoveries = closing; production reads from this and never exceeds
  reserves.
- **Cost-curve / C1 block** per asset; **provisional-pricing true-up** line on revenue. ⚠️
- Self-adapting granularity: collapse to the asset grain the issuer discloses.

## 6. Modeling pitfalls
- **Do NOT count Inferred Resources** in a mineable/DCF schedule — value reserves only.
- **Do NOT confuse resources with reserves** — they are non-additive, different-confidence
  inventories.
- **Do NOT model perpetual production** — bound it by the reserve base, with UoP depletion.
- **Do NOT ignore provisional-pricing true-ups or CFEM** — both move reported
  revenue/net realization.

## 7. Confidence & open questions
- ✅ **Verified:** IFRS 6 E&E policy exemption (transversal with O&G); JORC/CRIRSCO
  resources-vs-reserves, the conversion mapping (Indicated→Probable, Measured→Proved/
  Probable), Modifying Factors, and the Inferred-exclusion rule (round 2). **AISC
  definition** (inclusions/exclusions), **provisional pricing** (embedded derivative at
  FVTPL into sales revenue), and **CFEM** (constitutional basis, iron-ore 3.5% + rate
  table + 4% cap, base = gross revenue − commercialization taxes) — all round 3, 3-0.
  **UoP depletion** is an accounting-policy choice of basis (see [[oil_and_gas]] / the
  [[uop-depletion]] wiki).
- 🟡 / ⚠️ **To verify (round 4):** **C1 cash cost** definition specifically; grade &
  strip-ratio economics; cost-curve framing; iron-ore reference index + premium detail;
  finer CFEM post-2018 base mechanics (abstention-killed on the session limit, not
  refuted).
- Reserves/UoP/per-asset parallel with [[oil_and_gas]]; downstream customer is [[steel]]
  (iron ore).

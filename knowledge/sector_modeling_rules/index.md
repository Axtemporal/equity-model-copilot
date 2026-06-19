# Sector modeling rules (method cards)

How each sector must behave in the model **beyond** the generic three-statement +
projection + DCF framework: the operational drivers that replace generic
"revenue = price × volume", the mandatory KPIs/disclosures, the peculiar accounting
treatments, how the operational structure adapts, and the common pitfalls.

These cards are sector overlays on the per-line method library in
[`docs/calibration_and_knowledge_notes.md`](../../docs/calibration_and_knowledge_notes.md).
They are the **single source of sector truth**: the engine has no per-sector template
files. The copilot reads the card to understand a sector's revenue identity, drivers and
structure adaptation, then assembles the operational layer on top of the single
universal `base.yaml` — grounded in the card, never in model memory.

**Three folders (llm-wiki, CLAUDE.md decision #9).** The knowledge base is organized in
three layers, with this `index.md` + `_schema.md` + `_sources.md` as the entry point:

- [`sources/`](sources/README.md) — **layer 1**, the immutable raw material (releases,
  transcripts, research), one subfolder per sector; you add to it, the AI reads but never
  edits it; gitignored for copyright.
- [`sectors/`](sectors/) — the 12 **by-sector method cards** (the *by-sector* view), one
  per sector.
- [`wiki/`](wiki/index.md) — **layer 2**, the *by-concept* view: 25 cross-linked concept
  articles (accounting standards, operational driver patterns, sector KPIs,
  Brazil-specific rules), each governing one or more sectors.

**Two views, same knowledge.** Enter from a card in [`sectors/`](sectors/) and click
through to a concept, or browse the [`wiki/`](wiki/index.md) by theme. The assumption
session consults the wiki to ground a proposal in a verifiable concept (itself grounded
in `sources/`) before proposing a premise.

See [`_schema.md`](_schema.md) for the card contract and [`_sources.md`](_sources.md)
for the bibliography + confidence tiers. Every claim is tagged ✅ verified / 🟡 seed /
⚠️ to-verify; **method over numbers** — point-in-time figures are dated illustrations,
never hardcode them.

## Provenance of this batch

Built from deep-research runs with adversarial 3-vote verification: **round 1**
(2026-06-16, 23/25 claims confirmed) covered the extractive/commodity/accounting core;
**round 2** (2026-06-17, partial — credits ran out mid-run, results recovered from the
workflow journal) closed fuel-distribution mechanics, mining JORC reserves, and IFRS 15
over-time recognition. Coverage is still **uneven** — the remaining ⚠️ items (SaaS unit
economics, healthcare operating KPIs, mining cost/pricing, pulp & paper drivers,
education operating drivers, O&G NAV/UoP, JCP) are the round-3 agenda.

## Cards

### Extractive / reserve-based
- [`oil_and_gas.md`](sectors/oil_and_gas.md) — E&P: SPE-PRMS 1P/2P/3P, reserves vs resources, IFRS 6 E&E, UoP depletion, NAV vs DCF — **verified core** ✅
- [`metals_mining.md`](sectors/metals_mining.md) — Vale-type: JORC/CRIRSCO resources vs reserves (verified), C1 cash cost, grade, cost curve, CFEM (gaps) — **verified core** ✅

### Commodity / cyclical processors
- [`petrochemicals.md`](sectors/petrochemicals.md) — Braskem-type: per-route spreads, capacity × utilization, normalized mid-cycle EBITDA, integration — **verified** ✅
- [`steel.md`](sectors/steel.md) — Gerdau/CSN/Usiminas: reference index + premium, volume by product family, apparent demand, import penetration — **verified** ✅
- [`pulp_paper.md`](sectors/pulp_paper.md) — Suzano/Klabin: China CIF pulp × FX, per-BU tonnes × utilization, oil-linked cash cost, IAS 41 forest assets — **partial** 🟡
- [`fuel_distribution.md`](sectors/fuel_distribution.md) — Vibra/Raízen/Ultrapar: margin per m³ (recurring vs reported), inventory effect (IAS 2 weighted-avg cost), inventory-positioning working capital — **verified core** ✅

### Agribusiness
- [`agri_inputs.md`](sectors/agri_inputs.md) — 3tentos/Nutrien: segment by nutrient, volume × net price − cash cost/t, WC seasonality, barter/originação — **verified core** ✅
- [`agriculture.md`](sectors/agriculture.md) — SLC Agrícola: IAS 41 biological assets at fair value, bearer-plant split, hectares × yield, land — **verified core** ✅

### Services (regulated, KPI-driven)
- [`healthcare.md`](sectors/healthcare.md) — Rede D'Or/Hapvida/Fleury: beds/occupancy/ticket, sinistralidade (MLR), ANS, M&A roll-up — **partial** 🟡
- [`education.md`](sectors/education.md) — Cogna/Yduqs/Ânima: IFRS 15 over-time tuition / deferred revenue (verified); student base, ticket, evasão, FIES/PROUNI, EAD vs presencial (gaps) — **partial** 🟡

### Recurring / capital-intensive manufacturing
- [`tech_saas.md`](sectors/tech_saas.md) — SaaS: ARR/MRR, churn, NRR, CAC/LTV, rule-of-40, software capitalization (IAS 38) — **partial** 🟡
- [`auto.md`](sectors/auto.md) — Tesla-type OEM: units × ASP, gross margin/vehicle, capacity & gigafactory capex, IFRS 15 timing, incentives contra-revenue, regulatory credits — **partial** 🟡

## Cross-cutting accounting overlays (reference)
The accounting standards that recur across cards: **IFRS 6** (E&E capitalization,
O&G + mining), **IAS 41 / IAS 16 bearer plants** (agriculture + forestry), **IAS 38
vs ASC 730** (R&D/software capitalization), **IFRS 15** (point-in-time vs over-time
revenue, contra-revenue incentives, deferred tuition). Project decisions on **IFRS 16
EBITDA-AL** and **JCP / effective tax** live in the spec and a dedicated method card.

## Status & agenda
- [x] Round 1 — research + verified cards (extractive, petchem, steel, agri, accounting)
- [x] Round 2 (partial, 2026-06-17, recovered from journal after credits ran out) —
  **closed:** fuel distribution core (R$/m³, inventory effect, IAS 2 weighted-avg cost),
  mining JORC reserves (conversion mapping, Modifying Factors, Inferred exclusion),
  IFRS 15 over-time tuition + SaaS subscription / deferred revenue
- [ ] Round 3 — SaaS unit economics (ARR/MRR/NRR/CAC/LTV/rule-of-40); healthcare operating
  KPIs (beds, occupancy, sinistralidade, ANS); mining cost/pricing (C1, AISC, grade,
  CFEM, provisional pricing); pulp & paper operating drivers (still 🟡); education
  operating drivers; O&G depletion/UoP + NAV-vs-DCF default; Brazilian JCP/effective tax
- [x] ~~Wire each card into its `/templates/<sector>.yaml`~~ — **dropped (2026-06-17).** No
  per-sector templates: the card is consumed by the AI layer and the operational layer is
  assembled on the single `base.yaml`. See `planejamento_camadas_de_melhoria.md` §16.

## Compliance
Public sources only. Methods and KPIs described, never turned into a recommendation
or target price. No verbatim copying of the proprietary `Example models/` or
`Knowledge Base/` archives — distillation with provenance only.

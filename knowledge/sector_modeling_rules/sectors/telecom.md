---
sector: Telecom — mobile & fixed (Brazilian telecommunications)
slug: telecom
pilots_examples: TIM Brasil (pilot), Vivo/Telefônica Brasil, Claro/América Móvil
coverage: partial
key_standards: IFRS 15, IFRS 16, IAS 38 (spectrum/licence intangibles), Anatel regulation
status: draft
---

# Telecom (mobile & fixed) — sector method card

## 1. Core thesis
A telecom operator is a **subscriber × ARPU recurring-revenue** business riding on a
**heavy fixed-asset + lease base** (towers, sites, backhaul, spectrum). The generic
"revenue = price × volume" frame breaks in two ways. First, **service revenue is a
roll-forward of a subscriber base** (net adds, churn, mix migration) multiplied by a
**slowly-repricing ARPU** — not a free-floating growth rate — and it must be modeled
**separately from low-margin, volatile, seasonal handset/product revenue**, which is a
different animal entirely. Second, **IFRS 16 is structurally large** here (the lease base
is core infrastructure), so reported EBITDA is meaningfully lifted and **EBITDA-AL is the
honest profitability metric**. Build the model around a **per-segment subscriber/ARPU
build + an EBITDA-margin-driven cost structure + a capex/spectrum-intensity block**, and
always read EBITDA next to EBITDA-AL.

## 2. Operational drivers (the revenue build)
Split revenue into **service revenue** (recurring, high-margin) and **handset/product
revenue** (one-off, low-margin, seasonal) — never blend them.

- **Service revenue = subscribers × ARPU, BY SEGMENT** ⚠️ — model each segment as a
  base × per-unit price, summed to corporate:
  - **Mobile postpaid** (incl. control/híbrido) — the value engine: higher ARPU, lower
    churn, contract-bound.
  - **Mobile prepaid** — lower ARPU, higher churn, recharge-driven; the migration *source*.
  - **Fixed broadband / FTTH** (e.g. "TIM Live") — home connections × broadband ARPU; the
    growth front.
  - **Legacy fixed voice / DTH** — declining; model as run-off, not growth.
- **Subscriber roll-forward (corkscrew)** ⚠️ — `closing subs = opening subs + gross adds −
  disconnects`, or equivalently opening + **net adds**; net adds = gross adds − churn. Run
  one corkscrew per segment. This is the subscriber analogue of an [[arr-roll-forward]].
- **Churn** ⚠️ — monthly % of base disconnecting; prepaid churn ≫ postpaid churn. Churn
  drives both the base roll-forward and the cost of retention/SAC.
- **Prepaid → postpaid mix migration** ⚠️ — a deliberate, value-accretive shift: each
  migrated line *leaves* the prepaid base and *enters* postpaid at a higher ARPU. Model as
  a transfer between the two corkscrews, not as independent growth — it inflates postpaid
  net adds while shrinking prepaid.
- **ARPU trajectory** ⚠️ — `ARPU = service revenue ÷ average subscribers` per segment.
  Project as **carried-over ARPU + repricing**, where repricing is typically **IPCA-linked**
  (inflation pass-through on the base) plus mix and "more-for-more" upsell, partly offset by
  competitive/down-trading pressure. Do NOT project ARPU as a flat % growth divorced from
  inflation and mix.
- **TIM Live / FTTH home connections** ⚠️ — homes passed × penetration → connected homes
  (the fixed-broadband subscriber base); broadband ARPU on top. Capex-led; ties to the
  network/capex block below.
- **Data usage** ⚠️ — GB/user is the demand backdrop that *justifies* postpaid ARPU and
  upsell, but revenue is recognized on the plan (subscription), not metered per GB —
  model usage as a driver of plan mix/ARPU, not as a billable volume.
- **Handset / product revenue** ⚠️ — devices sold (often bundled with a plan): **low
  gross margin, volatile, seasonal** (4Q/launch peaks). Keep it a **distinct revenue and
  margin line** so it doesn't distort blended ARPU or service-revenue margins. Its
  recognition interacts with IFRS 15 bundling (§4).

> source: telecom operating-driver tree (subscribers × ARPU by segment, net adds/churn,
> prepaid→postpaid migration, IPCA-linked repricing, handset-vs-service split) is
> industry-standard practitioner knowledge ⚠️ **not yet sourced in this research** — round-N
> agenda; confirm exact line/segment definitions against the issuer's release. Accounting
> overlays in §4 ARE sourced at the standard level.

## 3. Mandatory KPIs & regulatory disclosures
- **ARPU per segment** (mobile postpaid, prepaid, fixed/broadband) — the headline KPI; the
  market reads ARPU trajectory as the pricing-power signal. ⚠️
- **Subscriber base & net adds** by segment; **postpaid vs prepaid mix** (postpaid % of
  base is a quality indicator). ⚠️
- **Churn** (monthly %, by segment). ⚠️
- **EBITDA AND EBITDA-AL** with margins — report **both**, because IFRS 16 lifts EBITDA and
  telecom's lease base is large; EBITDA-AL is the like-for-like metric. ✅ (project decision)
  See [[ebitda-al-ifrs16]] and [[ifrs-16-leases]].
- **Capex / capex intensity** (capex ÷ net revenue) — telecom is capital-intensive; track
  it explicitly. ⚠️
- **Operating Free Cash Flow** (EBITDA − capex − leases), the cash-conversion read. ⚠️
- **FTTH homes passed / connected / penetration** for the fixed-broadband build. ⚠️
- **Anatel** (the Brazilian telecom regulator) disclosures: spectrum holdings, coverage/
  quality obligations, licence terms. ⚠️ Brazilian-specific.

## 4. Peculiar accounting / normative rules
- **IFRS 16 leases — structurally large** ✅ (standard-level) — telecom's **towers, rooftop
  sites, backhaul/fibre and real estate** are mostly leased, so the RoU asset + lease
  liability are **material**, and IFRS 16 **lifts reported EBITDA** more than in most
  sectors (rent leaves opex; depreciation + interest replace it). Therefore: **report
  EBITDA and EBITDA-AL**, count the **lease liability as debt in the EV→equity bridge**, and
  have **FCFF deduct lease payments** — the project's single consistent treatment.
  Tower-lease sale-and-leaseback structures (operators sell towers to towercos and lease
  back) further enlarge the lease liability — do not net them away.
  > source: [IFRS-16] (standard); project spec third-round decisions; the telecom
  > towers/sites lease-base framing is cross-linked in [[ifrs-16-leases]] / [[ebitda-al-ifrs16]].
  > ✅ at the standard/decision level; per-issuer EBITDA-AL construction ⚠️ to-verify.
- **IFRS 15 — bundled handset + service contracts** ✅ (standard-level) — a postpaid plan
  that bundles a subsidized handset with a service term is a **single contract with multiple
  performance obligations**: the **handset (point-in-time, at delivery)** and the **service
  (over time, ratably over the term)**. The total transaction price is **allocated across
  obligations by standalone selling price**, so a subsidized device recognizes **more handset
  revenue up front than cash collected**, creating a **contract asset** (unbilled receivable)
  that unwinds as the customer pays over the term. Connection/activation fees are usually
  not a separate obligation (recognized over the service period). **Do not recognize the
  whole bundle as service revenue, and do not push all device revenue to the cash-collection
  schedule** — follow the five-step allocation.
  > source: [IFRS-15] (five-step model; over-time vs point-in-time; allocation by SSP;
  > contract assets) — ✅ verified at the standard level (round 2, 3-0). Telecom-specific
  > application (bundle allocation, contract-asset mechanics per issuer) ⚠️ to-verify.
  > See [[ifrs-15-performance-obligations]].
- **Spectrum / licence intangibles (IAS 38)** ⚠️ — spectrum licences acquired at Anatel
  auctions are **intangible assets**, capitalized at cost and **amortized straight-line over
  the licence term** (the finite useful life), not over physical-asset life. Renewal fees
  and coverage obligations attached to the licence may be capitalized or expensed per the
  award terms — read the issuer's policy. Keep spectrum amortization on its **own schedule**,
  separate from network PP&E depreciation, because the term (and therefore the amortization
  horizon) differs.
  > source: [IAS-38] (intangible recognition + finite-life amortization, the general
  > principle behind spectrum-licence treatment) ⚠️ telecom-specific spectrum treatment not
  > yet adversarially verified in this research — round-N agenda.
- **Capex vs spectrum capex** ⚠️ — separate **network capex** (RAN, fibre, core; into PP&E,
  depreciated) from **spectrum capex** (auction outlays; into intangibles, amortized over
  the licence term). 5G rollout is a multi-year network-capex wave layered on top of the
  spectrum purchase. Do not lump them into one line — the schedules differ.

## 5. Model structure adaptation
- **Two revenue blocks, never one:** (1) a **service-revenue block** = per-segment
  subscriber corkscrew × ARPU (mobile postpaid / prepaid / fixed broadband / legacy
  run-off), with the **prepaid→postpaid migration as an explicit transfer** between
  corkscrews; (2) a **handset/product block** with its own (low) margin and seasonality.
- **EBITDA-margin-driven cost build keyed off disclosed EBITDA** ⚠️ — telecom opex is
  modeled top-down as **opex ex-D&A → EBITDA margin** (calibrated to disclosed EBITDA and
  EBITDA-AL), rather than bottom-up cost-by-cost, because the disclosed EBITDA margin is the
  reliable anchor. Carry **D&A split into network-PP&E depreciation, RoU depreciation, and
  spectrum amortization** below EBITDA. This is the generic top-down build the engine
  already supports (revenue growth × margin + disclosed drivers), specialized to telecom.
- **Two capex/intangible schedules:** **network capex → PP&E → depreciation**, and
  **spectrum → intangibles → amortization over licence term**, kept separate.
- **Lease block (IFRS 16):** RoU + lease-liability roll-forwards (opening + new leases +
  interest accretion − payments = closing), surfacing **EBITDA and EBITDA-AL side by side**;
  the lease liability flows into net debt in the valuation bridge.
- **Self-adapting granularity (the differential):** if the issuer discloses ARPU/subs only
  at "mobile total" or "fixed total", the template **collapses segments to the disclosed
  grain** rather than forcing a postpaid/prepaid split that the issuer doesn't report; if it
  discloses TIM-Live/FTTH connections, build the fixed block out.

## 6. Modeling pitfalls
- **Do NOT conflate service revenue with handset/product revenue** — they have opposite
  margin profiles, different seasonality, and different recognition (over-time vs
  point-in-time). Blending them corrupts ARPU and service-margin trends.
- **Do NOT compare telecom EBITDA across issuers/time without EBITDA-AL** — the lease base
  is large, so IFRS 16 lifts EBITDA materially; reconcile via EBITDA-AL ([[ebitda-al-ifrs16]]).
- **Do NOT ignore the IFRS-16 lease base** — towers/sites/backhaul leases are core
  infrastructure here; omitting them understates net debt and overstates equity value.
- **Do NOT amortize spectrum like network PP&E** — spectrum is an IAS 38 intangible
  amortized **over the licence term**; keep its schedule separate from physical depreciation.
- **Do NOT recognize the whole bundled plan as service revenue (or all device revenue on the
  cash schedule)** — IFRS 15 allocates the transaction price across the handset (point-in-time)
  and service (over-time) obligations by standalone selling price, creating a contract asset.
- **Do NOT project ARPU as flat % growth** — anchor repricing to **IPCA** plus mix
  migration and upsell, net of competitive pressure.
- **Do NOT model prepaid→postpaid migration as net new subscribers** — it is a *transfer*;
  the line leaves prepaid and enters postpaid (no net base growth from migration alone).
- **Do NOT ignore Anatel** — spectrum auctions (the spectrum-capex trigger), coverage/quality
  obligations, and licence terms shape both capex timing and the amortization horizon.

## 7. Confidence & open questions
- ✅ **Verified (standard level only):** the **accounting overlays** lean on already-verified
  standards — **IFRS 16** (leases on balance sheet, EBITDA lift → EBITDA-AL, leases-as-debt
  bridge: project decision + standard), **IFRS 15** (five-step model, over-time service vs
  point-in-time handset, allocation by SSP, contract assets: round-2 3-0 at the standard
  level), and **IAS 38** (finite-life intangible amortization, the principle behind spectrum
  licences). The *telecom-specific application* of each is ⚠️ not yet adversarially verified.
- ⚠️ **To verify (round-N agenda — this sector is a new research gap, like SaaS was):** the
  entire **operating-driver tree** (subscribers × ARPU by segment, net-adds/churn
  conventions, prepaid→postpaid migration mechanics, IPCA-linked repricing, FTTH
  homes-passed/penetration, capex intensity benchmarks); **spectrum-licence accounting**
  specifics (capitalization of renewal fees/coverage obligations, amortization basis per
  issuer); per-issuer **EBITDA-AL construction**; **Anatel** spectrum-auction and
  coverage-obligation mechanics. No telecom source is yet in [`_sources.md`](../_sources.md)
  — the operating drivers above carry **no citation** and must not be presented as verified.
- **Cross-links:** [[ifrs-16-leases]] and [[ebitda-al-ifrs16]] (the lease-heavy core of
  telecom valuation); [[ifrs-15-performance-obligations]] (bundled handset+service);
  [[arr-roll-forward]] (the recurring-base corkscrew analogue); [[mid-cycle-normalization]]
  is **not** apt here (telecom is recurring, not cyclical). Consistency check against
  [[fuel_distribution]] / [[tech_saas]] for the "report a clean recurring metric, separate the
  volatile one" pattern.

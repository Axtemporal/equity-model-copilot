# Sector Modeling Rules — LLM Wiki

The **concept-oriented** knowledge base for how a model must behave **beyond** the
generic three-statement + projection + DCF framework, per sector. One article per
concept, cross-linked, with provenance and a confidence tier on every article. This is
the navigable companion to the *by-sector* method cards (`../sectors/oil_and_gas.md …
../sectors/auto.md`) and the bibliography (`../_sources.md`).

It mirrors the sibling [`../../damodaran_corporate_life_cycle/wiki/`](../../damodaran_corporate_life_cycle/wiki/index.md)
— same llm-wiki contract (CLAUDE.md decision #9), two deltas: the cross-cutting axis is
**sector** (not life-cycle stage), and every article carries a **confidence tier**
(✅ verified / 🟡 seed / ⚠️ to-verify) because the claims came from adversarial deep-
research, not a single book.

**How to read it.** Pick the concept you need and follow its cross-links; or enter from a
[method card](../index.md) and click through to the concept. Every article leads with a
one-sentence definition, explains the concept, says which sectors it governs and what it
changes in the model, and ends with provenance. The article contract is in
[`_schema.md`](_schema.md); the canonical concept list in [`_concepts.md`](_concepts.md).

**Three layers.** This `wiki/` (layer 2, distilled articles) sits on top of
[`../sources/`](../sources/README.md) (layer 1 — the raw material drop zone: releases,
transcripts, research; you add to it, the AI reads it but never edits it; gitignored for
copyright) and the maintenance rules in [`_schema.md`](_schema.md) (layer 3). Articles
distil from `sources/` and cite it in their Provenance block.

> Compliance: methods and KPIs are described, never turned into a recommendation or
> target price; all content is distilled (no verbatim copying of the proprietary
> archives); sources are public. **Method over numbers** — any figure is a dated
> illustration, never a value to hardcode.

---

## 🧾 Accounting standards (cross-sector overlays)
- [[ias-41-biological-assets]] — biological assets at fair value through P&L ✅
- [[ias-41-bearer-plants]] — the bearer-plant carve-out; why row crops & pulp eucalyptus stay IAS 41 ✅
- [[spe-prms-reserve-categories]] — O&G reserves: 1P/2P/3P, reserves vs resources ✅
- [[jorc-resources-and-reserves]] — mining: resources vs reserves, conversion mapping, Modifying Factors ✅
- [[ifrs-6-ee-capitalization]] — the exploration & evaluation accounting-policy exemption ✅
- [[ifrs-15-performance-obligations]] — over-time vs point-in-time revenue; contra-revenue ✅
- [[ias-2-inventory-costing]] — FIFO/weighted-average; cost-flow lag vs LCNRV ✅
- [[ias-38-rd-capitalization]] — IAS 38 vs ASC 730 R&D/software capitalization ✅
- [[ifrs-16-leases]] — leases on balance sheet, EBITDA-AL, the EV bridge 🟡

## ⚙️ Operational driver patterns (replacing generic price × volume)
- [[spread-based-revenue]] — spread = product price − feedstock cost, per route ✅
- [[reserve-based-nav]] — reserve-bounded per-asset NAV/DCF; the NAV-vs-DCF question 🟡
- [[uop-depletion]] — units-of-production depletion over the reserve base; basis is a policy choice; ARO ✅
- [[inventory-effect-fuel]] — the weighted-average cost-flow lag; recurring vs reported ✅
- [[arr-roll-forward]] — the SaaS recurring-revenue corkscrew 🟡
- [[biological-assets-in-model]] — isolating the IAS 41 fair-value line ✅
- [[mid-cycle-normalization]] — valuing cyclicals on normalized mid-cycle earnings ✅

## 📊 Sector KPIs & disclosures
- [[ev-2p-reserves]] — enterprise value per barrel of 2P reserves 🟡
- [[ebitda-al-ifrs16]] — after-lease EBITDA, the IFRS-16-adjusted metric 🟡
- [[saas-unit-economics]] — NRR, churn, CAC/LTV, Rule of 40, cohorts ⚠️
- [[c1-aisc-mining]] — C1 cash cost, AISC (✅), provisional pricing (✅), cost curve, grade 🟡
- [[mlr-sinistralidade]] — medical loss ratio as the health-plan margin gate 🟡
- [[r-per-m3-fuel]] — fuel-distribution profitability per cubic metre ✅

## 🇧🇷 Brazil-specific rules
- [[jcp-effective-tax]] — JCP (interest on equity) & the effective tax rate ⚠️
- [[cfem-royalty]] — the Brazilian mining royalty in the revenue bridge (iron ore 3.5%) ✅
- [[fies-prouni-mechanics]] — FIES & PROUNI education financing ⚠️

---

## Provenance & status
Built from deep-research runs with adversarial 3-vote verification (round 1, 2026-06-16;
round 2, 2026-06-17, partial; round 3, 2026-06-17, partial — all recovered from the
workflow output/journal when the session limit hit mid-run). This wiki distils the 12
method cards into 25 concept articles. Coverage is **uneven by design** — the confidence
tier on each article is honest:

- **✅ verified (15):** the accounting core (IAS 41, bearer plants, SPE-PRMS, JORC,
  IFRS 6, IFRS 15, IAS 2, IAS 38), the verified driver patterns (spreads, the inventory
  effect, the IAS 41 model split, mid-cycle normalization, R$/m³), and — added round 3 —
  **UoP depletion** (basis is a policy choice; ARO interaction) and **CFEM** (iron-ore
  3.5%, base, 4% cap).
- **🟡 seed (7):** IFRS 16 / EBITDA-AL (project decision encoded), reserve-based NAV
  (logic verified, NAV-vs-DCF default open), the ARR corkscrew, EV/2P, sinistralidade,
  and **C1/AISC** (AISC ✅ + provisional pricing ✅ this round; C1/grade/strip still open).
- **⚠️ to-verify (3):** the round-4 research agenda — SaaS unit economics, JCP/effective
  tax, FIES/PROUNI. (Healthcare, education, pulp operating drivers also remain gaps inside
  partially-verified articles.)

**Round 3 (2026-06-17):** 11 claims confirmed 3-0, **0 genuinely refuted** — the ~14
unconfirmed verdicts were **0-0/1-0 abstentions** when the session limit hit, not
refutations (same failure mode as round 1), so they carry to round 4. Closed: O&G UoP +
ARO; mining AISC + provisional pricing + CFEM. See `../_sources.md` for the round-4
agenda (Brazilian O&G royalty formulas, NAV method, C1 cash cost, SaaS/healthcare/
education/pulp operating drivers, JCP).

Future rounds upgrade the ⚠️/🟡 articles; update the article frontmatter, the inline
tag, and [`_concepts.md`](_concepts.md) together.

*25 concept articles · provenance via method card + hyperlink + confidence tier · built
per CLAUDE.md decision #9 (the three-layer llm-wiki pattern).*

---
sector: Oil & Gas — Exploration & Production (E&P)
slug: oil_and_gas
pilots_examples: Prio (pilot), PetroReconcavo, Brava, Petrobras (E&P segment)
coverage: verified
key_standards: SPE-PRMS, SEC reserves, IFRS 6
status: draft
---

# Oil & Gas (E&P) — sector method card

## 1. Core thesis
An E&P company's value is the value of barrels it can commercially produce, so the
model is not "revenue = price × volume" floating freely — it is a **production
schedule bounded by certified reserves**, priced at a realized oil/gas price net of
costs, and exhausted through decline. Reserves certification (how many barrels, at
what confidence) is the upstream constraint that everything else hangs from, and the
reserve base also drives depletion (DD&A) and the terminal value. Build the model
around the **2P reserve case and a production/decline profile**, not a perpetual
growth rate.

## 2. Operational drivers (the revenue build)
Replace the generic revenue line with a per-asset (per-field/cluster) build:

- **Production (boe/d or kbbl)** = opening reserve base run down a **decline/production
  curve**, capped so cumulative production never exceeds the recoverable reserve case.
- **Realized price** = benchmark (Brent for BR offshore) **± differential/quality
  discount** per stream (oil vs gas vs NGL priced separately).
- **Revenue** = production × realized price, **per field**, summed to corporate.
- **Netback** = realized price − royalties − production (lifting) cost − transport,
  per boe — the per-barrel margin that drives field economics.
- **Lifting cost (US$/boe)** is the core opex driver; project per field, watch the
  per-barrel cost *rise* as fields mature and volumes decline (fixed cost / falling
  boe).

> source: [SPE-PRMS-2007] for the reserve→production logic; netback/lifting-cost
> framing is industry-standard practitioner knowledge ⚠️ (confirm exact line
> definitions against the issuer's release in round 2).

## 3. Mandatory KPIs & reserve disclosures
- **Reserve categories (SPE-PRMS)** ✅ — `1P = Proved`, `2P = Proved + Probable`,
  `3P = Proved + Probable + Possible`. **2P is the standard "best estimate" base case
  for NAV/DCF.** Categories are additive only *within committed / in-development
  projects*. PRMS warns against naively summing categories of different risk in
  probabilistic portfolio aggregation.
  > source: [SPE-PRMS-2007] p.4 — verified 3-0.
- **Reserves vs Resources** ✅ — **Reserves** are commercially recoverable *with a firm
  development intent (typically within ~5 years)*. **Contingent Resources** are
  discovered but not yet commercial; **Prospective Resources** are undiscovered. Risk
  or exclude contingent/prospective barrels from a base-case reserve NAV (PRMS gives
  the risking mechanics: chance of development `Pd`, chance of discovery `Pg`).
  > source: [SPE-PRMS-2007] — verified 3-0.
- **SEC reserves** differ from PRMS/2P: SEC recognizes **proved (1P) only**, priced at
  a trailing 12-month average. A US-listed/20-F filer's "proved reserves" are a
  *conservative* subset — do not equate SEC proved with the analyst 2P base case. 🟡
- **Other standard KPIs:** reserve life (**R/P** = reserves ÷ annual production),
  **reserve replacement ratio**, finding & development cost, lifting cost/boe,
  netback/boe. ⚠️ (confirm definitions per issuer.)
- **Common reserve-based multiple:** **EV/2P** (and EV/1P). 🟡 [CFI-EV2P]

## 4. Peculiar accounting / normative rules
- **IFRS 6 — Exploration & Evaluation (E&E)** ✅ — grants O&G (and mining) an
  *accounting-policy exemption*: issuers set their own E&E recognition/measurement
  policy (the **successful-efforts vs full-cost** choice) and may keep pre-existing
  policy on adoption. **E&E is NOT uniform across companies — the model must read each
  issuer's stated policy, not assume one treatment.** E&E is the cost bucket
  capitalized before reserves are proven; it reclassifies into IAS 16 / IAS 38 once
  commercial viability is established.
  > source: [IFRS-6] para 7 — verified 3-0.
- **Depletion by unit-of-production (UoP)** ✅ — producing assets are amortized not
  straight-line but **pro-rata to production over the reserve base**: `DD&A = amortizable
  cost × (period production ÷ recoverable reserves)`. **The reserve basis is an
  accounting-policy CHOICE** (proved developed / total proved 1P / proved-plus-probable
  2P), applied consistently — **read it per issuer, do not assume**. If a **non-developed
  basis** (1P/2P) is used, the amortizable cost is **grossed up for estimated future
  development costs** so numerator and denominator cover the same barrels. UoP is the
  IFRS-preferred method (reflects consumption of the reserves' benefits).
  > source: [PWC-OG] — verified ✅ (round 3, 3-0). Resolves the open "which basis"
  > question: there is no single mandated basis — read the disclosure.
- **Decommissioning / asset retirement obligation (ARO)** ✅ — measured at the **PV of
  expected future decommissioning cash flows** (IAS 37.45), **capitalized into the asset
  cost** (IAS 16.16(c)), and depreciated over asset life (typically same UoP basis). The
  **accretion (unwinding of the discount) is a FINANCE expense**, *not* operating/
  depletion cost — keep distinct. Material for late-life fields (Prio's revitalization
  thesis).
  > source: [PWC-OG] — verified ✅ (round 3, 3-0).
- **Government take** — royalties + special participation (Brazil) sit between gross
  revenue and netback; model as a function of price/production, not a flat %. ⚠️

## 5. Model structure adaptation
- **One tab per producing asset/field** (mirrors reference Model A's per-mine
  structure), each with: reserve roll-forward, production/decline curve, realized
  price, lifting cost, netback; consolidating into Corporate.
- **Reserve roll-forward (corkscrew):** opening reserves − production ± revisions ±
  acquisitions/discoveries = closing reserves; production schedule reads from this.
- **Valuation: NAV (risked sum-of-the-parts of discounted per-field cash flows over
  the production profile) is the E&P-native method**, distinct from a single
  perpetuity-growth FCFF DCF. The terminal value is field exhaustion + ARO, not a
  Gordon-growth tail. Keep a consolidated FCFF DCF as a cross-check. *(NAV-vs-DCF
  default for the copilot is an open question — see §7.)*
- Self-adapting granularity: if the issuer discloses only at cluster/basin level, the
  template collapses to that grain rather than forcing per-well detail.

## 6. Modeling pitfalls
- **Do NOT model perpetual production growth** — barrels are finite; production must be
  bounded by, and decline against, the certified reserve case.
- **Do NOT mix reserve definitions** — SEC proved (1P) ≠ analyst 2P base case ≠ 3P
  upside. Pick one base (2P) and show 1P/3P as the downside/upside band.
- **Do NOT count contingent/prospective resources in the base case unrisked.**
- **Do NOT assume a single E&E policy** across companies (IFRS 6 lets them differ).
- **REFUTED — do NOT encode:** the framing of PRMS as "two independent axes with
  Reserves a strict subset of Resources, every barrel tagged on both dimensions." This
  failed verification; use the simple 1P/2P/3P + Reserves-vs-Resources framing above.
  > source: refuted claim, see [`_sources.md`](../_sources.md).

## 7. Confidence & open questions
- ✅ **Verified:** SPE-PRMS 1P/2P/3P and 2P-as-base-case; Reserves vs Resources;
  IFRS 6 E&E policy exemption. **UoP depletion** — basis is an accounting-policy choice
  (proved developed / 1P / 2P), non-developed basis requires the future-development
  gross-up, UoP is IFRS-preferred (round 3, 3-0). **ARO** — PV (IAS 37.45), capitalized
  (IAS 16.16(c)), accretion is a finance expense distinct from depletion (round 3, 3-0).
- ⚠️ **To verify (round 4):** netback/lifting-cost line definitions per Brazilian
  issuer; Brazilian royalty & special-participation formulas and the oil reference price
  (Preço Mínimo) — these were **abstention-killed on the session limit, not refuted**, so
  they carry over.
- **Open question for the user/spec (still open):** should the copilot default to **NAV
  (per-field risked SOTP)** or a **consolidated FCFF DCF** for E&P? (DCF is v2 per the
  spec; NAV is the sector-native answer.) The round-3 NAV-method claims (per-reserve-
  category SOTP; probability-weighting 2P/3P via reserve credits) were abstention-killed,
  so the decision is unchanged pending round 4. See [[metals_mining]] for the parallel
  reserves-vs-resources logic.

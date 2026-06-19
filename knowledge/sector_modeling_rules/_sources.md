# Sources — Sector modeling rules

Bibliography for the sector method cards. Built from a deep-research run
(fan-out web search → fetch → 3-vote adversarial verification → synthesis,
two passes on 2026-06-16). Each card's `> source:` callouts point to an ID here.

**Quality tiers** as classified by the research: *primary* (standards body,
issuer filing, peer-reviewed), *secondary* (reputable practitioner/educator),
*unreliable/blog* (used cautiously or filtered out).

## Standards & accounting (primary)

- **[SPE-PRMS-2007]** SPE, *Petroleum Resources Management System — Guide for
  Non-Technical Users* (2007). <https://www.spe.org/industry/docs/PRMS-Guide-for-Non-Technical-Users-2007.pdf>
  — reserve categories 1P/2P/3P, Reserves vs Resources, risking mechanics. ✅ verified (3-0).
- **[IFRS-6]** IFRS Foundation, *IFRS 6 Exploration for and Evaluation of Mineral
  Resources*. <https://www.ifrs.org/issued-standards/list-of-standards/ifrs-6-exploration-for-and-evaluation-of-mineral-resources/>
  — E&E accounting-policy exemption. ✅ verified (3-0).
- **[IAS-41]** IFRS Foundation, *IAS 41 Agriculture*.
  <https://www.ifrs.org/issued-standards/list-of-standards/ias-41-agriculture/>
  — biological assets at fair value less costs to sell, P&L recognition. ✅ verified (3-0).
- **[IAS-41-BP-2014]** IFRS Foundation, *Agriculture: Bearer Plants — Amendments
  to IAS 16 and IAS 41* (June 2014).
  <https://www.ifrs.org/content/dam/ifrs/project/agriculture-bearer-plants/final-agriculture-bearer-plants-june-2014-website.pdf>
  — bearer plants moved to IAS 16; produce stays IAS 41. ✅ verified (3-0).
- **[KPMG-RD-2025]** KPMG, *R&D costs: IFRS Accounting Standards vs US GAAP* (2025).
  <https://kpmg.com/us/en/articles/2025/rd-costs-ifrs-accounting-standards-us-gaap.html>
  — IAS 38 (research expensed, development capitalized if 6 criteria) vs ASC 730
  (R&D expensed). ✅ verified (3-0).
- **[EY-AUTO-IFRS15]** EY, *Applying IFRS — the revenue recognition standard:
  automotive industry* (July 2020).
  <https://www.ey.com/en_gl/technical/ifrs-technical-resources/applying-ifrs-the-revenue-recognition-standard-automotive-industry>
  — point-in-time recognition at OEM-to-dealer transfer; incentives as
  contra-revenue. ✅ verified (3-0 / 2-0).
- **[IFRS-15-TUITION]** IFRS Foundation, *Recognition of Revenue from Tuition Fees
  (IFRS 15)* (2025 agenda decision).
  <https://www.ifrs.org/projects/completed-projects/2025/recognition-of-revenue-from-tuition-fees-ifrs-15/>
  — concludes tuition is recognized **over time**. 🟡 the specific "IFRIC concluded over
  time" claim was killed 2-1 on quote-precision, but the over-time treatment itself is
  ✅ via [IFRS-15] (general over-time-vs-point-in-time principle).
- **[JORC-2012]** JORC, *Australasian Code for Reporting of Exploration Results,
  Mineral Resources and Ore Reserves (2012)*. <https://www.jorc.org/docs/JORC_code_2012.pdf>
  — Mineral Resources vs Ore Reserves; conversion mapping (Indicated→Probable,
  Measured→Proved/Probable); Modifying Factors; Inferred not convertible to reserves.
  ✅ verified (round 2, 2-0 / 3-0; corroborated by Geoscience Australia, SciELO).
- **[IAS-2]** IFRS Foundation, *IAS 2 Inventories*.
  <https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/>
  — only FIFO or weighted-average cost (LIFO prohibited); weighted-avg cost lags spot →
  inventory holding gains/losses (the fuel-distribution mechanism); lower-of-cost-and-NRV
  is a *separate* mechanism. ✅ verified (round 2, 3-0).
- **[IFRS-15]** IFRS Foundation, *IFRS 15 Revenue from Contracts with Customers*.
  <https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/>
  — five-step model; performance obligation satisfied over time (services: tuition, SaaS
  subscriptions) vs point in time (goods). ✅ verified (round 2, 3-0).

## Equity research & issuer filings (primary/secondary)

- **[XP-PETCHEM-2023]** XP Investimentos, *Initiation of Coverage — Petrochemicals
  (Braskem / Unipar)* (Sep 10 2023). S3-hosted PDF (see run transcript).
  — per-route spreads (PE-Naphtha, PE-Ethane, PP-Propylene), normalized mid-cycle
  EBITDA valuation, integrated vs non-integrated modeling. ✅ verified (3-0 / 2-0).
  *Numbers are point-in-time; encode method only.*
- **[XP-METALS-2025]** XP Investimentos, *Metals & Mining Brazil Outlook* (Oct 20
  2025). S3-hosted PDF. — steel realized-price = reference index + premium;
  volume by product family; apparent demand identity; import penetration.
  ✅ verified (2-0 / 3-0). *Numbers point-in-time.*
- **[XP-PULP-2022]** XP Investimentos, *Initiation — Suzano + update Klabin/Irani*
  (Dec 2022). S3-hosted PDF. — pulp price (China CIF BHKP/BEKP) × FX as primary
  drivers, per-BU tonnes × utilization × EBITDA/t, oil-linked cash cost. 🟡 seed
  (round-1, single source).
- **[NUTRIEN-FY2024]** Nutrien Ltd, *Q4 and Full-Year 2024 Results* press release.
  <https://www.nutrien.com/news/press-releases/nutrien-reports-fourth-quarter-and-full-year-2024-results-1717>
  — four reportable segments; volume × net price − cash cost/tonne; working-capital
  -to-sales seasonality. ✅ verified (3-0 / 2-1).
- **[VIBRA-2Q25]** Vibra Energia S.A., *2Q25 Conference Call Transcript* (Aug 12 2025,
  official MZ IR file system, api.mziq.com). — fuel distribution measured in R$/m³;
  recurring vs reported margin (strip inventory effect + asset/tax gains); inventory
  effect distorts net income; inventory-positioning working capital reversing ~45 days.
  ✅ verified (round 2, 3-0). *Figures are point-in-time; encode method only.*

## Healthcare (primary/secondary)

- **[PMC-SAUDE-2024]** *BMC Health Services Research*, study on Brazilian
  supplementary-health consolidation (PMC11483984, 2024).
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483984/>
  — M&A intensity (494 deals 2018-2022), concentration, Rede D'Or/Hapvida.
  ✅ verified (3-0). 🟡 (round-1) concentration indices.
- **[NAIC-MLR]** NAIC, *Medical Loss Ratio*.
  <https://content.naic.org/insurance-topics/medical-loss-ratio>
  — MLR definition (the US analogue of sinistralidade). 🟡 seed (round-1).

## Practitioner guides (secondary)

- **[CFI-EV2P]** Corporate Finance Institute, *EV/2P ratio*.
  <https://corporatefinanceinstitute.com/resources/valuation/ev-2p-ratio> — reserve-based multiple.
- **[IBIQ-CRACKER]** IB Interview Questions, *Petrochemicals / ethylene cracker
  economics*. <https://ibinterviewquestions.com/guides/energy-investment-banking/petrochemicals-ethylene-cracker-economics-ethane>
- **[CPDBOX-IAS41]** CPDbox, *How to measure fair value in agriculture (IAS 41 / IFRS 13)*.
  <https://www.cpdbox.com/how-to-measure-fair-value-in-agriculture-ias-41-and-ifrs-13/>
- **[ACCA-IAS41]** ACCA, *IAS 41* technical article.
  <https://www.accaglobal.com/gb/en/student/exam-support-resources/dipifr-study-resources/technical-articles/ias-41.html>

## GitHub repos cited by the user (assessed, low relevance)

- **[REPO-JWOLBERG]** jwolberg/Equity-Valuation-Model.
  <https://github.com/jwolberg/Equity-Valuation-Model> — two Tesla Excel models
  (2019), generic three-statement + WACC + competitive analysis. **No license =
  all rights reserved → do not copy.** Vintage, no documented auto-specific driver
  tree. Structure reference only.
- **[REPO-WYATTM94]** wyattm94/Equity-Valuation-Modelling-in-Excel.
  <https://github.com/wyattm94/Equity-Valuation-Modelling-in-Excel> — sector-agnostic
  Excel/VBA, single-case → probability-weighted DCF (multi-scenario). **No license.**
  Relevant only as a *scenario-method* reference for the bull/base/bear v2 work, not
  for any sector.

## Refuted in research (do NOT encode)

- PRMS as "two independent axes with Reserves a strict subset of Resources, every
  barrel tagged on both" — refuted (1-0 against, abstentions). Use the simple
  1P/2P/3P + Reserves-vs-Resources framing from [SPE-PRMS-2007] instead.
- "EV/EBITDA at 3-5x is THE valuation anchor for Brazilian steel" — refuted (0-2).
  EV/EBITDA is *a* cross-check, not the defining method.
- "The IAS 2 lower-of-cost-and-NRV writedown is THE mechanism behind fuel-distribution
  inventory losses" — refuted (3-0, round 2). LCNRV only bites when selling price falls
  *below* carrying cost; the recurring inventory gain/loss is the **weighted-average
  cost-flow lag** (a separate mechanism). Keep the two distinct — see [[fuel_distribution]].

## Round-2 results (2026-06-17, partial — credits ran out mid-run)

Recovered from the workflow journal (24 verdicts: ~10 confirmed, 2 killed). **Closed:**
fuel distribution core mechanics (R$/m³ recurring-vs-reported margin, inventory effect,
IAS 2 weighted-avg cost, inventory-positioning WC) ✅; metals & mining JORC reserves
(conversion mapping, Modifying Factors, Inferred exclusion) ✅; IFRS 15 over-time
recognition for education tuition + SaaS subscriptions (deferred revenue) ✅.

## Round-3 sources (2026-06-17)

- **[PWC-OG]** PwC, *Financial reporting in the oil and gas industry* (IFRS).
  <https://www.pwc.com/id/en/publications/assets/eumpublications/financial-reporting-in-the-oil-and-gas-industry.pdf>
  — UoP reserve basis is an **accounting-policy choice** (proved developed / 1P / 2P),
  applied consistently; non-developed basis requires grossing up the amortizable cost for
  future development; UoP is the IFRS-preferred method; ARO measured at PV (IAS 37.45),
  capitalized (IAS 16.16(c)), accretion as finance expense. ✅ verified (round 3, 3-0).
- **[WGC-AISC]** World Gold Council, *All-in costs / AISC guidance*.
  <https://www.gold.org/about-gold/gold-supply/responsible-gold/all-in-costs>
  — AISC = cash operating cost + sustaining capex + corporate G&A + share-based remun. +
  reclamation/inventory adj., net of by-product credits; **excludes** non-sustaining
  capital, impairments, severance, M&A, financing. ✅ verified (round 3, 3-0).
- **[VALE-20F-2022]** Vale S.A., *Form 20-F 2022* (SEC).
  <https://www.sec.gov/Archives/edgar/data/0000917851/000129281423001516/valeform20f_2022.htm>
  — provisional pricing: provisional invoice at delivery, receivable re-measured at
  **fair value through P&L** (embedded derivative) until the contractual pricing period
  (generally later than shipment) sets the final price; MTM into **sales revenue**.
  ✅ verified (round 3, 3-0). *Figures point-in-time; encode method only.*
- **[ANM-CFEM]** ANM, *Perguntas frequentes — CFEM* (gov.br).
  <https://www.gov.br/anm/pt-br/acesso-a-informacao/perguntas-frequentes/contribuicao-financeira-pela-exploracao-mineral-2013-cfem>
  — CFEM constitutionally mandated (Art. 20 §1º, CF/1988); base = gross sale revenue minus
  commercialization taxes; rates by mineral (iron ore **3.5%**; bauxite/manganese/niobium/
  rock salt 3%; diamond/other 2%; gold 1.5%; aggregates 1%; **4% cap**). ✅ verified
  (round 3, 3-0).

## Round-3 results (2026-06-17, partial — session limit hit mid-verify)

113 agents, 30 sources → 116 claims → 25 verified → **11 confirmed (3-0), 0 genuinely
refuted**. The synthesis step and ~14 verdicts died as **0-0 / 1-0 abstentions** when the
session limit hit (resets 6:30am SP) — these are **NOT refutations**, just not reached
(same failure mode as round 1). **Closed (✅):** O&G **UoP depletion** (basis = policy
choice; non-developed gross-up; UoP-preferred) + **ARO** (PV/IAS 37.45, capitalized/
IAS 16.16(c), accretion = finance expense); mining **AISC** definition + **provisional
pricing** (embedded derivative at FVTPL) + **CFEM** (constitutional basis, iron-ore 3.5%
+ rate table + 4% cap, base = gross − commercialization taxes).

## Remaining coverage gaps (round-4 agenda)

**Abstention-killed this round (not refuted — carry over):** Brazilian O&G royalty &
special-participation formulas + oil reference price (Preço Mínimo); finer CFEM post-2018
base mechanics (transport/insurance deductibility, ANM rate-reduction discretion); O&G
**NAV method** (per-reserve-category SOTP; probability-weighting 2P/3P via reserve
credits) → the **NAV-vs-DCF default** stays open. **Not reached at all:** mining **C1
cash cost** definition specifically, grade/strip economics, cost-curve framing; **SaaS
unit economics** (ARR/MRR, NRR, CAC/LTV, rule-of-40, cohort); **healthcare** operating
KPIs (beds, occupancy, ticket, sinistralidade, ANS, glosas, verticalization); **education**
operating drivers (ticket, evasão, FIES/PROUNI, EAD vs presencial, PCLD, MEC); **pulp &
paper** operating drivers (still 🟡 single-source); **Brazilian JCP / effective-tax**
mechanics. Several reputable sources were *fetched* for these (wallstreetprep NRR,
Rule-of-40 wiki, Metrópoles FIES/evasão, Exame ANS, fastmarkets/XP pulp, etc.) but their
claims were never verified — candidates to harvest as 🟡 seeds or re-verify in round 4.

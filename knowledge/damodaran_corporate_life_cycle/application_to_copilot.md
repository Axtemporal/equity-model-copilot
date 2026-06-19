---
title: Applying the Life Cycle to the Modeling Copilot
type: synthesis/application
status: draft
---

# Applying the Life Cycle to the Modeling Copilot

This note translates Damodaran's life-cycle thinking (synthesised in
[[00_framework_lifecycle]]) into concrete guidance for **this** project: a
Brazilian-equity three-statement + DCF modeling copilot whose AI proposes
assumptions line by line for user approval. It is written against the project's
existing **method-card library** in `docs/calibration_and_knowledge_notes.md`
(§3, "Per-line projection methods" and "Dynamic schedules") and the closed
decisions in `docs/project_specification.md` (integrated IFRS three-statement
engine; FCFF DCF + WACC Valuation tab with multiples, bull/base/bear scenarios,
target price under disclaimer; quarterly + annual interleaved columns; Kd from the
debt schedule feeds WACC by formula; IFRS-16 leases-as-debt in the EV→equity
bridge; assumptions persisted by the Assumptions log; pilots Prio (Oil & Gas) and
3tentos (agri inputs)).

The core move: **the copilot runs a life-cycle classification step *before*
proposing assumptions, then uses the stage to choose, per line, between the
method-card's default and override methods** — and to set valuation, WACC, and
scenario width. The method cards already encode the *menu* of methods; the life
cycle tells the AI *which item on the menu to pick and why*.

---

## 1. The life-cycle classification step (run first, every session)

Per [[cap_01_unifying_theory]] §7 ("stage first, model second") and
[[cap_03_measures_determinants]] §7, the copilot should classify the company on the
six stages *from its disclosed financials* before the line-by-line session — and
write the result, with evidence, to the Assumptions log as the session's first
entry (method + source, per compliance).

### 1.1 Inputs to read (already in the Input Financials / Operational tabs)
Compute, from the keyed historicals (use the most recent 3–5 years where available):
- **Revenue growth** — 3–5y CAGR and the latest YoY (and the *absolute* ΔRevenue,
  not just %, per [[cap_11_valuing_high_growth]] §2.4).
- **Operating margin** — level *and trajectory* (rising / stable / falling); margin
  sign is the key disambiguator between stages that share a growth level
  ([[cap_03_measures_determinants]] §3.1).
- **Reinvestment intensity** — capex + acquisitions − D&A + ΔNWC, scaled to
  revenue; and its *sign* (positive = investing; negative = divesting).
- **FCF sign** — FCFF and FCFE (the engine already computes the components).
- **Cash-return behaviour** — dividends + buybacks vs. FCFE, and payout ratio.
- **Cash-flow-statement sign pattern** — operating/investing/financing signs, for
  the Mauboussin cross-check ([[cap_14_investment_philosophies]] §6.5).

### 1.2 Rule-of-thumb thresholds (Brazil-calibrated, seed values — drift per sector)
Match the *combination* (the fingerprint), not any single metric. These are
starting thresholds for the classifier; the `_sector.md` file should refine them
per sector against the Damodaran by-industry growth/margin distributions.

| Signal | Start-up | Young Growth | High Growth | Mature Growth | Mature Stable | Decline |
|---|---|---|---|---|---|---|
| Real revenue growth (CAGR) | NA / pre-revenue | > ~25% | ~15–25% | ~5–15% | ~0–5% (≈ GDP+inflation) | < 0 over 3–5y, esp. ex-cycle |
| Operating margin | very negative | negative, flat/worse | negative→improving | positive, rising | positive, stable | positive falling / negative |
| Reinvestment (% rev) | very high | very high | high, stable | high, declining | low (≈ maintenance) | **negative** (divesting) |
| FCFF / FCFE sign | very negative | very negative | negative→turning | positive, growing | positive, high | positive (high, from drawdown) |
| Cash returned | none (raising equity) | none | minimal | dividends/buybacks begin | high payout | high payout + buybacks |

Two guards, both required before committing a label:
- **Growth × margin 2×2 sanity check** ([[cap_03_measures_determinants]] §3.2):
  high growth + negative margin ⇒ young growth; high growth + high margin ⇒
  superstar/mature-growth winner; low/neg growth + high margin ⇒ cash cow; low/neg
  growth + neg margin ⇒ distressed. Flag if the proposed stage contradicts the 2×2.
- **3-part decline diagnostic** ([[cap_02_basics]] §2.7) before ever labelling a
  firm "declining": (a) is the revenue drop a 5–10y *trend* or a 1–2y blip;
  (b) is it macro/**cyclical** (critical for Prio — a Brent downturn is not
  decline) or structural; (c) does an un-paid-down debt load risk tipping it into
  distress? This is essential for Brazilian cyclicals and commodity names.

### 1.3 Transition detection
If the firm is at or just past a gate (recent IPO/SEO, an announced/closed LBO or
take-private, a new VC round, a large divestiture/spin-off, an activist on the
register), switch the relevant model section into **transition mode**: a discrete
step-change in cash/share-count/debt at the transition period, not a smooth trend
([[cap_04_transitions]] §7, [[00_framework_lifecycle]] §2). For mature/declining
pilots, an **activist appearing** is the trigger to add the status-quo-vs-
restructured (value-of-control) view ([[cap_12_valuing_mature]] §2.8).

### 1.4 Outputs of the step
(1) a stage label with the metric evidence; (2) the **dominant decision** to weight
the session toward (investment / financing / cash-return —
[[00_framework_lifecycle]] §4.1); (3) the **scenario width** prior (wider for young
/ high-uncertainty, tighter for mature — [[cap_14_investment_philosophies]] §7);
(4) a **management-stage-fit** note (CEO archetype vs. stage; flag mismatch ≥ 1
stage — [[cap_18_managing]] §2.4, §7); (5) for O&G/agri, whether the decline-looking
signal is actually **cyclical** (suppresses the decline template). All logged.

---

## 2. STAGE → per-line projection method (deltas to the existing method cards)

The tables below are read as **overrides on `docs/calibration_and_knowledge_notes.md`
§3**. "Default" / method names refer to the existing cards; the entry says *which to
pick per stage and why*. Where a stage needs a method the cards don't yet have, it
is flagged as a new card. Nothing here changes the engine's arithmetic or the
"no constant in a formula / every premise in its own cell" rule — it only steers
*which* sourced premise the AI proposes.

### 2.1 Revenue
Method card: default = aggregate % growth; override = price × volume by segment.

| Stage | Pick | Why |
|---|---|---|
| Start-up / Young Growth | **New top-down card: `Revenue = TAM × market share`, glide to steady state** (not in the cards yet) | No history to extrapolate; value is built from a story. Make TAM and share their own sourced cells; auto-compute **implied market share** and flag if implausible vs. competition (big-market-delusion guard) ([[cap_10_valuing_young]] §3, [[cap_11_valuing_high_growth]] §2.10). |
| High Growth | **price × volume by segment**, with an explicit **growth fade** time profile | Operational data exists (the pilots' case); fade % toward the sector mature rate, year-specific, never flat ([[cap_11_valuing_high_growth]] §2.4). Sanity-check ΔRevenue in absolute terms, not just %. |
| Mature Growth / Mature Stable | **price × volume by segment** (or aggregate % ≈ GDP+inflation) | Growth ≈ economy; spend effort elsewhere ([[cap_12_valuing_mature]] §2.1). |
| Decline | **aggregate % growth, set NEGATIVE** | Negative growth is real and correct, not an error; tie to `g = Reinvestment rate × ROIC` so a negative reinvestment rate and negative-but-bounded terminal g stay consistent ([[cap_13_valuing_declining]] §3.1). |

For user/subscriber-driven young firms, additionally expose the **user-economics
layer** `Value = PV(existing users) + PV(new users) − PV(corporate drag)` with
explicit renewal/churn and CAC, as a parallel pricing cross-check
([[cap_15_investing_youth]] §6.1) — labelled pricing, never intrinsic value.

### 2.2 COGS / margins
Method card: default = % of revenue (gross margin); override = unit cost × volume.

| Stage | Pick | Why |
|---|---|---|
| Young / High Growth | **unit cost × volume** + a **margin glide path** from today's (often negative) level to a *target* margin benchmarked on an efficient mature peer | Current margin is depressed by up-front fixed costs and growth-spend mingled with opex; model the *path*, not the frozen current margin ([[cap_11_valuing_high_growth]] §2.5, [[cap_10_valuing_young]] §2.5). Separate growth-spend from cost-to-serve. |
| Mature | **% of revenue / unit cost × volume**, roughly held | Margins are settled; small efficiency gains can still lift earnings growth above revenue growth ([[cap_12_valuing_mature]] §2.1). |
| Decline | **margin converging DOWN to (or below) the sector average** | Pricing power erodes and the firm cuts its own prices to defend volume ([[cap_13_valuing_declining]] §3.6, the BB&B retail-average convergence). Do **not** auto-assume mean reversion to past highs under disruption ([[cap_03_measures_determinants]] §2.17). |

### 2.3 D&A
Method card: default = from the PP&E roll-forward (schedule). **Keep this at every
stage** — it is an accounting identity, not a stage choice. The only stage effect
is via capex (next row): heavy capex early lifts future D&A; divestitures in
decline shrink the asset base and D&A.

### 2.4 Reinvestment / capex
Method card: PP&E roll-forward `BOP + capex − depreciation − disposals`.

| Stage | Pick | Why |
|---|---|---|
| Young / High Growth | **size reinvestment off ΔRevenue via a sales-to-capital ratio** (`Reinvestment = ΔRevenue / sales-to-capital`), high early, declining over time — feed it into the capex line | More robust than projecting capex independently for a scaling firm; keeps growth and capital internally consistent ([[cap_11_valuing_high_growth]] §2.6, [[cap_10_valuing_young]] §3). Expect deeply negative early FCFF (modeled, not an error). |
| Mature | **capex toward maintenance**; treat **acquisitions as a reinvestment (capex) line**, policed by ROIC vs. WACC | As firms mature, acquisitions become the growth engine and must be modeled like capex, not a free add-on; flag value destruction when implied ROIC < WACC (the Unilever sales-to-capital lesson) ([[cap_12_valuing_mature]] §2.3, §3). |
| Decline | **negative reinvestment** — model **divestiture cash inflows** in place of capex | Existing assets earn below the cost of capital, so shrinking *adds* value; cash flows exceed earnings ([[cap_13_valuing_declining]] §2.2). Default decline policy = minimize reinvestment, deleverage before payout ([[cap_17_investing_old_age]] §7). |

### 2.5 Working capital
Method card: days-driven (DSO / inventory-days / DPO), each premise inverted from
reported history, then drifted/held; CF "change in WC" computed from BS deltas.

- **Keep the days-driven cards at every stage** — they are the market standard the
  reference models converge on. The stage effect is on the *driver level*: in
  **high growth**, working capital *builds* aggressively (a real cash drag that
  keeps FCFE negative even when NI turns positive — [[cap_08_cash_return]] §2.2), so
  do not let WC default to flat; in **mature**, hold days flat unless there is a
  thesis; in **decline**, WC *releases* cash as the business shrinks (a source, not
  a use). Surface DSO/DPO/turnover as the dynamic premises the engine already plans
  (backlog item 3).

### 2.6 Debt / financing
Method cards: LT debt roll-forward, interest on opening balance (no circularity);
revolver/cash-sweep; weighted-average Kd → WACC by formula (backlog item 6).

| Stage | Pick | Why |
|---|---|---|
| Start-up / Young Growth | **near-zero debt; fund with equity / equity hybrids (convertibles, warrants)** | Intangible/growth assets + volatile earnings + no taxable income ⇒ ~no debt capacity; reject the "debt is cheaper" illusion; **gate the tax shield on actual taxable income** (NOLs ⇒ no shield — the Tesla 7-year case) ([[cap_07_financing]] §2.4, §3.4). |
| High Growth | **building capacity; convertibles** matched to growth | Fixed payments still dangerous; convertibles carry low coupons + equity option ([[cap_07_financing]] §2.8). |
| Mature Growth / Mature Stable | **use the rising-to-peak debt capacity; conventional straight debt matched to assets** | Stable earnings maximize the interest tax shield; this is where the **financing decision dominates** — interrogate the debt schedule hardest ([[cap_07_financing]] §2.9, [[cap_12_valuing_mature]] §7). Run the **synthetic-rating Kd loop** (coverage → rating → spread) and an optimal-leverage/WACC×g view. |
| Decline | **wind debt DOWN from peak; deleverage before payout** | Debt taken on when healthy becomes a crushing burden against falling earnings — "the wrong edge of the leverage sword"; a rising D/E feeds *both* a higher Kd *and* the distress probability ([[cap_13_valuing_declining]] §2.1, §7). |

Apply the **matching principle** (currency, maturity, fixed/floating) at every
stage ([[cap_07_financing]] §2.8): for Prio (commodity producer), commodity-linked
or hedged debt is the textbook match; separate BRL vs. foreign-currency debt and
revalue at period-end FX (the existing card). Per [[cap_20_serenity]] §3, treat the
fundamental optimum as a **ceiling** and keep deliberate **buffer debt capacity**
for cyclical/commodity names — model leverage *below* the theoretical max.

### 2.7 Dividends / buybacks
Method card: retained-earnings roll-forward `BOP + NI − dividends`; treasury stock /
buyback schedule. The framework's headline: **cash return is a residual, computed
from FCFE, never a target** ([[cap_08_cash_return]] §7).

| Stage | Pick | Why |
|---|---|---|
| Start-up → High Growth | **default zero (or negative) cash return; flag any modeled dividend as a red flag** | FCFE is negative (reinvestment + losses); these firms *raise*, not return ([[cap_08_cash_return]] §2.2). |
| Mature Growth → Mature Stable | **positive payout; spend effort on the dividend-vs-buyback / JCP split and sustainability vs. FCFE** | Cash-return decision switches on; benchmark payout against FCFE and the `divfcfe` industry average; flag *both* dysfunctions — payout > FCFE (sticky-dividend drawdown, esp. commodity names in a downturn) and payout ≪ FCFE (hoarding) ([[cap_08_cash_return]] §7). Dividends and buybacks are value-equivalent in form — don't credit EPS accretion as value. |
| Decline | **high payout from drawdown/divestiture**; in a "walking-dead" firm treat surplus cash as a **liability** (it funds value-destroying reinvestment), not a cushion | Markets discount trapped cash at low-growth/high-debt firms; force it out ([[cap_08_cash_return]] §2.9, [[cap_19_fighting_aging]] §7). |

### 2.8 Tax
Method card: default = prior-year effective rate; override = marginal rate with
adjustments (NOLs, JCP). Keep this card; the stage effects are:
- **Young / loss-making:** no interest tax shield until taxable income exists;
  carry NOLs explicitly ([[cap_07_financing]] §3.4).
- **Mature/profitable:** use the marginal rate for the shield (only on debt up to
  the point interest < taxable income; the shield caps out beyond that —
  [[cap_07_financing]] §3.3).
- **All Brazilian firms:** route through the dedicated **JCP / effective-rate method
  card** (the project's closed decision) — JCP is a deductible distribution that
  blends financing and tax, so it belongs in both the Kd/WACC logic and the payout
  split.

### 2.9 Shares / EPS
Method card: default = constant count; override = buyback/issuance schedule. Stage
effect: young/high-growth firms have **step-changes** at transitions (VC rounds,
IPO/SEO dilution, SBC) — roll SBC and successive rounds forward, never ignore them
([[cap_02_basics]] §7, [[cap_04_transitions]] §7). Mature firms reduce count via
buybacks. This is the existing shares-outstanding input (backlog item 4).

---

## 3. Stage-specific VALUATION guidance (the Valuation tab)

The Valuation tab is an FCFF DCF + WACC + multiples + bull/base/bear, with a
target price under disclaimer. The same machinery is **re-weighted** by stage
([[cap_09_valuation_101]] §7); below is what changes per stage.

### 3.1 Which approach leads, and the terminal-value treatment
| Stage | Lead approach | Terminal value | Pricing cross-check |
|---|---|---|---|
| Start-up / Young | **Story-driven FCFF DCF** with explicit **failure probability** (§3.2); intrinsic is back-loaded | Standard perpetuity capped at economy growth, but most value sits in it — expect it | EV/TAM, EV/user, EV/forward-sales — **labelled pricing, never intrinsic** ([[cap_10_valuing_young]] §7) |
| High Growth | **FCFF DCF with year-specific WACC, growth fade, margin convergence** | **Dominates (80–100%+) — normal, not a flaw**; surface the year-5/10 base-year inputs that drive it; keep stable-phase **ROC > WACC** spread explicit; for tech-like firms compress the window (≤10y) and steepen decay | PEG / forward-PE peer cross-check + a **breakeven** view (solve for margin×revenue implied by price) ([[cap_11_valuing_high_growth]] §7) |
| Mature | **FCFF DCF (near-term cash flows dominate)** + **status-quo vs. restructured (value of control)** + **SOTP** for octopuses | Standard; stable growth ≤ economy; **don't lock sub-optimal margins/ROC into perpetuity** | **EV/EBITDA** emphasis (capital-structure-neutral; survives to divisional level for SOTP); pick the multiple *before* seeing its answer ([[cap_12_valuing_mature]] §7) |
| Decline | **DCF with negative growth + negative reinvestment + distress blend**; **liquidation/SOTP as a floor**; **equity-as-option** for deeply distressed | Negative terminal g is legitimate (enlarges `r − g`); add the asset-liquidation premium when assets are worth more sold ([[cap_13_valuing_declining]] §3.1) | P/E, EV/liquidation; never read a low EV/Sales or P/B as a bargain without controlling for growth/margin/distress (the BB&B trap) |

### 3.2 Failure / distress probability (the input mature models skip)
- **Young firms** ([[cap_10_valuing_young]] §2.5): keep the cost of capital near a
  diversified/mature level (resist VC-style 50%+ target rates) and add an
  **explicit probability of failure** with a failure value (cash on hand or asset
  haircut): `Equity value = going-concern value × p_survival + failure value ×
  p_failure`. Set p_failure from the cash-burn **runway** (cash ÷ burn rate) and
  quality of capital access ([[cap_10_valuing_young]] §6.2).
- **Declining firms** ([[cap_13_valuing_declining]] §3.3–3.4): estimate a
  **cumulative probability of distress** over the horizon (from the company's
  rating, backed out of its bond price via Solver, or a probit) and apply the same
  blend with a distress-sale value (a fraction of book or of going-concern value,
  *never* the full DCF). A rising D/E and a deteriorating rating must feed *both*
  Kd and p_distress. For deeply distressed names add the **equity-as-option**
  overlay (S = firm assets, K = face debt, t = debt duration, σ = asset vol) so a
  pure DCF doesn't wrongly zero out equity — with a clear analytical disclaimer.

### 3.3 Growth fade & margin convergence (high-growth) and value-per-user (young)
For high-growth pilots, **force three convergences over the horizon, all
year-specific**: revenue growth *fades* toward the sector mature rate, operating
margin *climbs* to a defensible steady state, WACC *declines* toward the sector
average ([[cap_11_valuing_high_growth]] §7). Always translate the revenue path into
an **implied market share** and stress it (big-market-delusion guard). For
user-driven young firms, run the **value-per-user** model alongside the FCFF DCF and
reconcile the gap ([[cap_15_investing_youth]] §7) — both labelled, neither alone
trusted.

### 3.4 How WACC should evolve
WACC is a **built-up, dynamic, sourced** number, never a typed constant
([[cap_06_investing]] §7): cost of equity = Rf + β×ERP; after-tax Kd =
(Rf + default spread)×(1 − marginal t), wired from the debt schedule's
weighted-average cost (the synthetic-rating loop, backlog item 6). Let it **drift
down and β toward 1 as a young/high-growth firm matures** (age gradient: young
≈ 9–9.6% → mature ≈ 7–8%); let it **rise again in distress** as D/E and earnings
volatility climb. Estimate Rf and ERP in the **currency of the cash flows** and the
ERP by **where the firm does business** — relevant for Brazilian pilots with
USD-denominated commodity revenue (Prio) ([[cap_06_investing]] §2.5,
[[cap_12_valuing_mature]] §2.4). Don't over-engineer the discount rate — the
cross-firm spread is narrow (~5–10%); spend effort on cash flows
([[cap_06_investing]] §7). Keep **discrete risks (failure, distress) OUT of the
discount rate** — handle them with the probability blends (§3.2) and scenarios.

### 3.5 Bull / base / bear ↔ stage uncertainty
Scenario *width* should scale with stage uncertainty, not be a uniform haircut
([[cap_14_investment_philosophies]] §7, [[cap_16_investing_middle_age]] §7,
[[cap_20_serenity]] §3): **widest for start-up/young** (the AI should treat a single
point value skeptically and lean on the spread / a Monte-Carlo layer on the ~6 key
inputs — revenue growth, target margin, sales-to-capital, Ke, Kd, failure prob),
**tightest for mature**. The bull/bear cases are **structured, justified
deviations** from base (the AI proposes them as such): for mature firms the
**restructured (value-of-control)** case is a natural bull and the **status-quo /
zombie** case a natural bear; for declining firms an **acceptance/soft-landing**
case (deliberate shrinkage, margin expansion on a smaller base, rising cash return)
often *raises* value vs. a doomed growth-chasing case and makes a clean bull-vs-bear
contrast ([[cap_19_fighting_aging]] §7).

---

## 4. The two pilots

### 4.1 Prio (Oil & Gas)
**Likely stage: high-growth / mature *cyclical* producer.** Rapid production growth
via acquired/redeveloped fields, scaling toward maturity, but with **commodity-
cyclical** revenue (Brent × volume × FX) that can *look* like decline in a price
downturn without being structural decline. Implications:
- **Run the 3-part decline diagnostic religiously** ([[cap_02_basics]] §2.7): a
  Brent-driven revenue fall is cyclical, *not* the decline template — suppress
  negative-growth/divestiture defaults unless reserves are genuinely depleting.
- Revenue = **production by field × realization price vs. Brent × FX** (the sector
  template); size reinvestment (field development capex) off the growth via
  sales-to-capital; gate interest accrual / depletion on an activity flag for
  depleting fields (the existing O&G card option).
- **Buffer debt capacity** is a feature, not conservatism — an oil-price collapse
  is the canonical macro failure trigger ([[cap_20_serenity]] §3); model leverage
  below the optimum. Prefer **commodity-linked / hedged debt** (matching principle)
  and reflect this in the weighted-average Kd → WACC.
- Management premium is **small** — a Brent-driven business is macro-driven, so the
  CEO archetype/quality adjustment should be muted ([[cap_18_managing]] §2.2, §7).
- O&G is in Damodaran's **"bad business"** set (many firms earn ROIC < WACC), so
  the **ROIC − WACC excess-return spread** is the headline value test
  ([[cap_06_investing]] §7, [[cap_11_valuing_high_growth]] §4.3); growth only adds
  value if the spread is positive. Add a **reserve-depletion / negative-terminal-
  growth** option to the terminal value for a finite resource base.

### 4.2 3tentos (agri inputs)
**Likely stage: young growth → high growth** (multi-segment: input retail,
industrial, grains). Real, scaling revenue with margins still climbing; value rests
on the growth path. Implications:
- Revenue = **price × volume by segment** with an explicit **growth fade** and
  **crop-seasonality** profile; size reinvestment (store/plant build-out) off
  ΔRevenue via sales-to-capital ([[cap_11_valuing_high_growth]] §7).
- **Margin glide path** to a defensible steady state benchmarked on a mature agri-
  inputs peer; separate growth-spend (expansion) from cost-to-serve.
- **Working capital is a major cash drag** for a growing agri-distribution business
  (inventory + receivables build with seasonality) — do **not** let WC default to
  flat; use days-driven premises with seasonal awareness ([[cap_08_cash_return]] §2.2).
- Debt: building capacity; commodity/FX exposure (grain prices, USD) ⇒ apply the
  matching principle and separate BRL vs. foreign-currency debt.
- Valuation leads with **FCFF DCF (growth fade + margin convergence + year-specific
  WACC)**; cross-check with EV/sales and EV/EBITDA against B3 and international
  agri-inputs peers; surface the **implied market share** of each segment's growth
  and stress it against competition.

### 4.3 Coverage-consistency note
Because the project flags divergences between same-sector companies, the classifier
output (stage, growth/margin fingerprint, WACC build, terminal assumptions) should
be comparable across coverage — e.g. two O&G names should not carry wildly
different stable-phase ROC or terminal growth without a sourced reason
([[cap_06_investing]] §7). Shared sector drivers (Brent, FX, sector growth) live in
`_sector.md` and feed every model by formula.

---

## 5. Compliance reminder (carry through every output)

The life-cycle framing **reinforces**, never relaxes, the project's compliance core:
- **Every estimate carries method + source + date** and is logged in the
  Assumptions tab; never present an estimate (TAM, target margin, failure
  probability, restructured-case uplift, value-per-user) as reported data
  ([[cap_01_unifying_theory]] §7, [[cap_10_valuing_young]] §7).
- **No recommendations, no buy/sell, no target-price framing beyond the analytical
  disclaimer.** Value ≠ price: the DCF produces *value*, multiples produce *price*;
  present the gap as an analytical observation with the §2.11 humility framing
  (you / the market / both may be wrong), never a signal — the pricing game can
  reward value destruction ([[cap_09_valuation_101]] §7, [[cap_11_valuing_high_growth]] §2.11).
- **Describe, don't advise.** The value-of-control, activist-lever, and management-
  mismatch readouts are analytical observations about *where value is trapped*, not
  activism recommendations ([[cap_16_investing_middle_age]] §7, [[cap_18_managing]] §7).
- **Guard against overreach and the AI's own bias** ([[cap_01_unifying_theory]] §7,
  [[cap_20_serenity]] §2.3): don't over-fit a company to one elegant story or
  factor; flag when an assumption is stretched past its evidence; keep the feedback
  loop open (invite dissenting input in the approve/re-apply workflow); default to
  ranges/scenarios over false precision; respect base rates over hero/turnaround
  narratives.
- **Public sources only**, and the proprietary `Example models/` / `Knowledge Base/`
  material stays gitignored and is never copied into code or docs.

---

See [[00_framework_lifecycle]] for the unifying theory and the master table this
note operationalises, and the per-chapter notes `[[cap_01_unifying_theory]] …
[[cap_20_serenity]]` for the underlying evidence and method derivations.

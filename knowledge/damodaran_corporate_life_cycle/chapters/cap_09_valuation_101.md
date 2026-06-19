---
chapter: 9
title: Valuation and Pricing 101
block: Valuation
slides: reference/damodaran_clc/pdf/Ch9.pdf
status: draft
---

# Ch 9 — Valuation and Pricing 101

## 1. Core thesis

Chapter 9 is the foundations chapter for the book's Valuation block: it lays out
the machinery that the four stage-specific valuation chapters
([[cap_10_valuing_young]], [[cap_11_valuing_high_growth]],
[[cap_12_valuing_mature]], [[cap_13_valuing_declining]]) will then re-weight for
each life-cycle phase. Damodaran's central organizing claim is that **value and
price are two different things, estimated by two different processes, driven by
two different sets of forces** — and that conflating them is the root of most
analytical confusion. *Value* (intrinsic value) is what a business is worth based
on its expected cash flows, their growth, and their risk; it is estimated by
**discounted cash flow (DCF)** analysis. *Price* is what the market will pay
today; it is estimated by **relative valuation / pricing** (multiples and
comparables) and is driven by mood, momentum, liquidity, and incremental news.
Both are legitimate, but they answer different questions. The chapter then sets
out the four DCF inputs that every intrinsic valuation reduces to — **cash flows
from existing assets, the value of growth, the risk/discount rate, and a terminal
value** that imposes closure on an infinite-life going concern — and shows that
the *same* identity (value = present value of expected cash flows, adjusted for
risk) holds across the life cycle, even though the cash-flow path, the dependence
on terminal value, and the balance between **narrative and numbers** shift
dramatically as a firm ages. This is the operational restatement of the Chapter 1
invariant ([[cap_01_unifying_theory]]): one model, re-weighted inputs.

> source: Ch9.pdf p.1–15 (slide deck, primary); valuesurvey.pdf; multiples.pdf

## 2. Key concepts & frameworks

### 2.1 Value vs. price — the master distinction
Damodaran insists on never using "value" and "price" interchangeably. The **value
process** asks what an asset is intrinsically worth from its fundamentals (cash
flows, growth, risk) and is the domain of DCF. The **pricing process** asks what
the market will pay right now and is the domain of multiples. The two can diverge
widely for the same asset at the same moment because they respond to different
drivers; the gap ("the gap" on the Pricing slide) is the source of both
investment opportunity and risk. The pricing process can reward firms that
destroy value and punish firms that follow financial first principles — which is
freeing to recognize, because it makes the analyst's implicit assumptions
explicit. Applies across all life-cycle stages, but the *relative weight* an
investor puts on each shifts by stage (price-heavy for the youngest and the
oldest firms; value-heavy in the middle).
> source: Ch9.pdf p.12–13; Jan-2018 and Jan-2019 data-update blogs (§6)

### 2.2 Intrinsic value: the basics
Intrinsic value is the present value of expected future cash flows, discounted at
a **risk-adjusted discount rate** that also embeds the time value of money.
Putting this into practice means grappling with three things at once: how to
*define* the cash flows, how to *incorporate risk* into the discount rate, and
how to handle the *time value of money* across the forecast. The deck's headline
formula (§3.1) is just the present-value identity applied to a stream of expected
cash flows. Universal across the life cycle.
> source: Ch9.pdf p.2

### 2.3 Equity valuation vs. firm (enterprise) valuation
There are two consistent levels at which to run a DCF, and mixing them is a
classic error:
- **Firm / business valuation** discounts cash flows to *all* claim holders —
  free cash flow to the firm (FCFF), which is *pre-debt-payment* and *after*
  reinvestment — at the **cost of capital** (the blended after-tax cost of debt
  and equity, weighted by use). The present value is the value of the *entire
  firm* (operating assets); subtract net debt to reach equity.
- **Equity valuation** discounts cash flows to equity only — free cash flow to
  equity (FCFE), which is *after* debt payments and reinvestment — at the **cost
  of equity**. The present value is the value of equity directly.
Done consistently, both routes give the same equity value; you can always bridge
from firm value to equity value by netting out all non-equity claims. The firm
approach is preferred when leverage is expected to change materially over time
(debt cash flows need not be modeled explicitly), at the cost of needing debt
ratios and rates for the WACC. Relevant at every stage, but the firm approach is
especially useful for young/high-growth firms whose capital structure is in flux.
> source: Ch9.pdf p.3; valuesurvey.pdf p.7–8, p.25–30

### 2.4 The four DCF inputs (value drivers)
Damodaran's "Intrinsic Value: Key Questions" / "Value Drivers" slides decompose
every DCF into four questions, mapped to four inputs:
1. **Cash flows from existing assets** — *What are the cash flows from assets in
   place?* Base earnings reflecting the earning power of existing assets, net of
   taxes and the reinvestment needed just to sustain them.
2. **Value of growth** — *What is the value added (or destroyed) by growth?*
   Future cash flows reflect how fast earnings grow (a positive) net of how much
   the firm must reinvest to generate that growth (a negative). Expected cash flow
   in year t = expected earnings − reinvestment needed for growth. Growth only
   creates value when it earns **excess returns** (return on capital above the
   cost of capital).
3. **Risk in the cash flows** — *How risky are the cash flows?* Captured in the
   discount rate: a **beta** in the cost of equity and a **default spread** in the
   cost of debt; riskier cash flows are discounted at higher rates.
4. **Steady state / terminal value** — *When does the firm become mature (the
   "roadblock"), and what then?* The length of the growth period comes from the
   strength and sustainability of competitive advantages; beyond it, assume a
   constant growth rate forever and apply closure via a terminal value.
> source: Ch9.pdf p.5–6 (read as images)

### 2.5 A parsimonious valuation structure
The deck offers a compact "value tree" linking the value of a business down
through its operational drivers: **revenue growth** (a function of the size of
the accessible market and market share), **operating margins** (pricing power and
cost efficiency), and **growth/investment efficiency** (how much reinvestment a
unit of growth requires) combine into expected FCFF (= revenues × operating
margin × (1 − tax) − reinvestment); this is discounted at a risk-adjusted rate
built from the **cost of equity** (rate of return equity investors demand) and
the **cost of debt** (cost of borrowing, after tax), with **failure probability**
as a survival overlay for fragile (especially young) firms. The point is that a
sound DCF need not be elaborate — a handful of well-chosen drivers carries the
value.
> source: Ch9.pdf p.7 (read as image)

### 2.6 Value = story + numbers
A good valuation marries a **narrative** (a coherent story about the business)
with **numbers** (projections that translate the story into value). Each side has
appeal and danger: numbers give a sense of precision and objectivity but, divorced
from a story, can be manipulated and are not anchored; stories are memorable and
emotionally resonant but, unconnected to numbers, drift into fairy tales and
unrealistic valuations. The discipline is the feedback loop — every story input
must show up as a number, and every number must trace back to a story element.
The "Connecting Story Pieces to Value Inputs" slide makes this concrete: a
*big-market* narrative drives the total-market number; *networking / winner-take-
all* narratives drive market share; *strong, sustainable competitive advantage*
shows up as a combination of high share and high margins; *tax breaks* show up as
a lower tax rate; *easy scaling* shows up as low reinvestment for growth; and a
*low-risk* narrative shows up as a lower discount rate. Especially load-bearing
for young/high-growth firms, where the story dominates.
> source: Ch9.pdf p.8–9 (read as images); DCF Myth 2 blog (§6)

### 2.7 Intrinsic value across the life cycle
The intrinsic-value identity is *constant* across the life cycle, but it plays out
through very different cash-flow paths and a changing reliance on terminal value:
- **Young companies** building business models show negative cash flows in the
  early years, turning positive only as they approach high growth, then growing
  fast before settling into stability. A *much larger* share of their value sits
  in later-year cash flows and the terminal value.
- **Mature companies** more often show positive cash flows immediately, but with
  far less growth ahead — a larger share of value is in near-term cash flows.
- **Declining companies** may show *shrinking* cash flows over time as the
  business gets smaller.
The "Narrative vs Numbers Across the Life Cycle" matrix overlays the six stages on
the revenue (red) and earnings (green) curves and grades each stage by
narrative-vs-numbers mix and by how wide investor disagreement is:

| Stage | Narrative vs. numbers | Narrative driver | Narrative differences |
|---|---|---|---|
| Start-up | All narrative | How big is the narrative? | Unconstrained, large differences |
| Young growth | Mostly narrative | How plausible is the narrative? | (constraints begin to bind) |
| High growth | Narrative + numbers | How profitable is the narrative? | Constraints mount as numbers build up |
| Mature growth | Numbers + narrative | How sustainable is the narrative? | Differences narrow as history deepens |
| Mature stable | Mostly numbers | How happy is the narrative? | Constrained |
| Decline | All numbers | — | Narrow differences |

> source: Ch9.pdf p.10–11 (read as images)

### 2.8 Pricing: the relative-valuation framework
The "Pricing" slide mirrors the value slide but on the price side. **Tools for
the gap** (deciding whether a gap exists and will close) include intrinsic DCF on
the value side and behavioral finance / charting / technical indicators on the
price side. Intrinsic value is driven by cash flows (adjusted for risk), growth,
quality of growth, and cash-flow quality; **price** is driven by market mood and
momentum, liquidity, and surface stories about fundamentals. Relative valuation
gives up on estimating intrinsic value and instead trusts that the market gets
pricing right *on average* across comparable assets, even if it errs on
individual names.
> source: Ch9.pdf p.12; valuesurvey.pdf p.57–59; multiples.pdf p.1–2

### 2.9 Price drivers (the four behavioral forces)
Market price is set largely by **mood and momentum** (panic, fear, greed);
**liquidity and trading ease** (the price can move even when value does not, as
liquidity changes); **incremental information** (since you make money on price
*changes*, the focus is on news/rumor/gossip measured against expectations, not on
price *levels*); and **group think / the herd** (pricing is partly a guess about
what other investors will do). These are the forces that make price diverge from
value and that the value-oriented analyst must distinguish from fundamentals.
> source: Ch9.pdf p.13 (read as image)

### 2.10 Pricing mechanics — the four steps to using multiples
Using multiples soundly (and detecting their misuse) follows four steps, mirrored
in the "Pricing Mechanics" slide:
1. **Pick a multiple / define it consistently and uniformly.** Numerator is an
   *equity* value (price, market cap) or a *firm* value (enterprise value = market
   value of equity + debt − cash). Denominator must match: equity numerator →
   equity denominator (EPS, net income, book value of equity); firm numerator →
   firm denominator (revenues, EBIT, EBITDA, book value of capital). A consistent
   multiple matches numerator and denominator (PE, EV/EBITDA); an inconsistent one
   (e.g., price/EBITDA — equity over firm) mis-ranks levered vs. unlevered firms.
   Measure it *uniformly* (same trailing/forward convention, same accounting
   standards) across the comparison group.
2. **Make a timing choice.** Most recent annual (last 10-K), trailing (last four
   quarters), or forward (next year's expected) figure.
3. **Choose the peer group / comparables.** A "narrow vs. broad" sector choice;
   companies of similar size; same country/region/global; or other criteria. A
   true comparable is any firm with similar cash flows, growth, and risk — *not*
   necessarily the same industry.
4. **Tell a story / control for differences.** Adjust for differences in **risk**
   (higher risk → lower multiple), **growth** (higher growth → higher multiple),
   and **quality of growth** (higher return on capital/equity → higher multiple),
   via subjective adjustments, modified multiples (e.g., PEG), or regressions.
> source: Ch9.pdf p.14 (read as image); multiples.pdf p.5–21

### 2.11 Pricing across the life cycle
The "Pricing Across the Life Cycle" matrix shows that the *pricing-vs-valuing*
balance is U-shaped: pricing dominates at the start-up and decline ends (where
intrinsic DCF is hardest), value dominates in the middle. The pricing *metric*
also rotates with age, tracking whatever the market currently fixates on:

| Stage | Pricing vs. valuing | Pricing measures | Pricing metrics | Peer group |
|---|---|---|---|---|
| Start-up | Mostly pricing | Potential market, capital access | EV/TAM, users, EV/subscribers | Young companies that have raised VC funding |
| Young growth | (pricing→value) | Revenue growth, margins | EV/Forward sales, EV/Sales | Young companies from same or public recently |
| High growth | Mostly value | Revenue growth, operating margins | EV/Sales | Young companies in sector |
| Mature growth | (value) | Earnings growth | PEG, Forward PE | High-growth companies in sector |
| Mature stable | (value→pricing) | Earnings stability | PE, EV/EBITDA | Other mature companies in sector |
| Decline | Pricing | Other-people's-firms, sometimes book value | PE, EV/Liquidation value | Declining companies in sector |

> source: Ch9.pdf p.15 (read as image)

## 3. Metrics, formulas & rules of thumb

### 3.1 The DCF identity (general)
Value = sum over t of E(CF_t) / (1 + r)^t, where E(CF_t) is the expected cash flow
in period t and r is the risk-adjusted discount rate. This is the master formula;
everything else is a way of estimating CF and r.
> source: Ch9.pdf p.2

### 3.2 Terminal value and closure
A going concern can in theory last forever; to impose closure, assume cash flows
beyond an explicit forecast horizon grow at a constant rate g forever and
capitalize them:

`Value of business today = Σ_{t=1..n} E(CF_t)/(1+r)^t  +  [E(CF_{n+1})/(r − g)]/(1+r)^n`

The first term is the present value of cash flows in the explicit forecast period
(n years); the second is the present value of the **terminal value** — itself a
stable-growth perpetuity, the value of the business at the end of year n assuming
constant growth thereafter. Constraint: the perpetual growth rate **cannot exceed
the growth rate of the economy** (nominal g if r is nominal), because no firm can
outgrow the economy forever. Young firms draw a far larger fraction of their value
from this terminal piece than mature firms do.
> source: Ch9.pdf p.4, p.10; valuesurvey.pdf p.11, p.27–28

### 3.3 FCFF vs. FCFE (cash-flow definitions)
- **FCFF (free cash flow to the firm)** = after-tax operating income (EBIT × (1 −
  tax)) − (capital expenditures − depreciation) − change in non-cash working
  capital. Pre-debt, after reinvestment. Discounted at the **cost of capital
  (WACC)**.
- **FCFE (free cash flow to equity)** = net income + depreciation − capital
  expenditures − change in non-cash working capital − (new debt issued − debt
  repayments). After debt, after reinvestment. Discounted at the **cost of
  equity**. (The dividend discount model is the special case where FCFE is proxied
  by actual dividends.)
> source: valuesurvey.pdf p.20, p.26; Ch9.pdf p.3

### 3.4 Stable-growth (perpetuity) values
- Firm: `Value of firm = FCFF_1 / (WACC − g)`
- Equity (FCFE): `Value of equity = FCFE_1 / (Cost of equity − g)`
- Equity (dividends, Gordon growth): `Value of equity = DPS_1 / (Cost of equity − g)`

All require g ≤ economy growth and inputs (reinvestment, risk) consistent with a
mature firm.
> source: valuesurvey.pdf p.11, p.22, p.27

### 3.5 The main multiples and their DCF-derived drivers
Every multiple is implicitly a function of the same three things that drive DCF —
**cash-flow generating potential, growth, and risk** — plus, for some, a quality
variable. Dividing a stable-growth model by the relevant denominator yields the
fundamentals (the "companion variable" is the dominant one):

| Multiple | Type | Formula (stable growth) | Key drivers / companion variable |
|---|---|---|---|
| **PE** (price / earnings) | Equity | `Payout × (1+g) / (k_e − g)` | Growth (companion), risk, payout |
| **PBV** (price / book equity) | Equity | `ROE × Payout × (1+g) / (k_e − g)` | **ROE** (companion), growth, risk, payout |
| **PS** (price / sales) | Equity | `Net margin × Payout × (1+g) / (k_e − g)` | **Net margin** (companion), growth, risk, payout |
| **EV/EBITDA** (and EV/EBIT) | Firm | derived from `1/(WACC − g)` adjusted for tax/reinvestment | Reinvestment rate, ROC, tax rate, growth, risk |
| **EV/FCFF** | Firm | `1 / (WACC − g)` | WACC, g |
| **EV/Sales** | Firm | analogous | Operating margin, reinvestment, growth, risk |

PE variants matter: **current PE** (most recent fiscal-year EPS), **trailing PE**
(last four quarters), **forward PE** (next year's expected EPS); in a rising-
earnings environment forward < trailing < current, so the variant chosen reveals
the analyst's bias. The **PEG ratio** (PE ÷ expected growth) is a "modified
multiple" that controls for the companion variable but assumes a linear PE-growth
relationship and equal risk across firms.
> source: multiples.pdf p.12–14, p.18; valuesurvey.pdf p.62–70

### 3.6 Consistency and distribution rules of thumb
- **Consistency test:** numerator and denominator must both be equity or both be
  firm values; price/EBITDA fails this.
- **Distribution test:** multiples are bounded below at zero but unbounded above,
  so their distributions are right-skewed; the **median** is far more
  representative than the mean, and percentiles (10th/25th/75th/90th) define what
  "cheap" or "expensive" means *relative to the market*. Absolute multiple
  thresholds are meaningless without the distribution.
- **Selection-bias test:** firms with negative earnings drop out of PE samples,
  biasing the average **upward**; fixes are to adjust down, to compute an
  aggregate PE (Σ market cap / Σ net income), or to use the **earnings yield**
  (E/P), which is computable even for loss-makers.
- **Determinants test:** know which fundamentals drive the multiple and how
  non-linearly they do so before judging cheap vs. expensive.
> source: multiples.pdf p.5–11, p.12–15; Jan-2019 blog (§6)

## 4. Examples & cases

Chapter 9's slide deck is deliberately framework-first and names few companies,
but the supplementary readings and papers supply the concrete cases:
- **Amazon** (DCF Myth 2 blog) — different narratives (optimistic, base,
  pessimistic) produced a valuation range of roughly $32 to $468 per share,
  illustrating that the *story*, not the modeling mechanics, drives the answer.
- **Uber vs. Coca-Cola** (DCF Myth 2 blog) — Uber's value is narrative-dominated
  with a wide range; Coca-Cola's is numbers-dominated and tight — the life-cycle
  narrative/numbers shift in action.
- **Cisco and data-networking peers** (multiples.pdf p.17–20) — a worked
  comparable-firms case: a simple PE comparison calls Cisco overvalued (PE 133.76
  vs. peer average 115.31), the PEG adjustment still calls it slightly overvalued
  (implied PE 120.82), but a sector regression of PE on beta and growth
  (PE = 35.08 − 65.73·Beta + 573.10·Growth, R² = 93.6%) predicts 144.79 and calls
  it ~7.6% undervalued — showing how controlling for more fundamentals flips the
  conclusion.
- **Specialty retailers** (multiples.pdf p.10–11) — the negative-earnings
  selection bias: average PE > aggregate PE > median PE.
- **Cross-market pricing** (Jan-2018 / Jan-2019 blogs) — China and India the most
  expensive markets on PE/EV-EBITDA; Russia and Eastern Europe the cheapest;
  software and healthcare richly priced, utilities and energy cheap — used to show
  that "cheap" stocks usually deserve their low multiples (weak growth, high risk,
  low ROC).
> source: DCF Myth 2 blog; multiples.pdf p.10–20; Jan-2018/Jan-2019 blogs

## 5. Data & tools

Damodaran's companion data and spreadsheets for this chapter (catalog only; raw
data not copied, per the copyright rule):
- **uValue.xls** — valuation-input industry averages (US) and a Global version:
  by-industry inputs needed to run a DCF or sanity-check multiples (growth,
  margins, reinvestment, costs of capital, multiple levels).
  `pages.stern.nyu.edu/~adamodar/pc/datasets/uValue.xls`
- **fcffsimpleginzu.xlsx** — the "simple FCFF ginzu" model: a ready-made
  firm-level DCF (FCFF discounted at WACC, with terminal value) — the canonical
  template for the intrinsic-value identity in §3.
  `pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx`
- **divginzu.xlsx** — dividend / FCFE discount model: the equity-side DCF
  counterpart.
  `pages.stern.nyu.edu/~adamodar/pc/divginzu.xlsx`
- **eqmult.xls** — equity-multiples tool: computes/derives PE, PBV, PS and their
  fundamental drivers for relative valuation.
  `pages.stern.nyu.edu/~adamodar/pc/eqmult.xls`

(All under `pages.stern.nyu.edu/~adamodar/`; URLs are best-known canonical paths
and should be confirmed live before use.)

## 6. Supplementary readings — distilled

### 6.1 Paper — "Valuation Approaches and Metrics: A Survey of the Theory and Evidence" (valuesurvey)
*Read in full as local text.* Damodaran's 2006 academic survey of the entire
valuation field, the theoretical backbone of this chapter. It classifies valuation
into four families: **DCF** (value = PV of expected cash flows), **liquidation /
accounting** (asset/book-value based), **relative** (multiples and comparables),
and **contingent-claim / real options**. The DCF section is exhaustive: it traces
the intellectual history (Fisher, Williams, Gordon), distinguishes **equity
valuation** (FCFE/dividends at cost of equity) from **firm valuation** (FCFF at
WACC), and covers four DCF variants that *all converge under consistent
assumptions* — risk-adjusted-discount-rate models, **certainty-equivalent**
models (adjust cash flows for risk, discount at the risk-free rate), **excess-
return / EVA** models (value = capital invested + PV of excess returns), and
**adjusted present value (APV)** (unlevered value + PV of tax shields − expected
bankruptcy costs). The relative-valuation section establishes that *every multiple
is a disguised DCF*: dividing a stable-growth model by earnings, book value, or
sales yields PE, PBV, and PS as functions of growth, risk, payout, and (for the
latter two) ROE and margin. It catalogs how to control for differences across
comparables (subjective adjustment, modified multiples like PEG, sector/market
regressions) and surveys the empirical evidence (forecast-EPS multiples price best;
multiples and DCF give similar values cross-sectionally but DCF dominates over
time). What it adds beyond the slides: the rigorous proof that all DCF variants and
relative valuation share one root, plus the academic evidence base and the
emerging-market / young-company estimation challenges that motivate the
stage-specific chapters.
> source: reference/damodaran_clc/text/valuesurvey.txt (full)

### 6.2 Paper — "Relative Valuation" / Pricing First Principles (multiples)
*Read in full as local text.* The applied companion to §6.1, this is Damodaran's
practitioner chapter on multiples. It argues relative valuation is *popular*
(faster, fewer explicit assumptions, easier to sell, closer to market price) but
*dangerous* (the same ease lets analysts ignore risk/growth/cash-flow drivers,
import the market's mispricing, and manipulate via biased multiple/peer choices).
Its core contribution is the **four-step discipline** for using multiples
(definitional/consistency/uniformity tests; descriptional/distribution tests;
analytical/determinants tests; application/comparable-firm tests — §2.10) and the
formal derivation of each multiple's fundamentals from a DCF model, including the
**companion variable** (growth for PE, ROE for PBV, margin for PS). It works the
Cisco/data-networking case three ways (raw PE, PEG, regression) and the
specialty-retailer negative-earnings bias case. Adds beyond the slides: the
explicit consistency rule (equity-over-equity, firm-over-firm), the skew/median/
percentile statistics of multiples, and the selection-bias fixes (aggregate PE,
earnings yield).
> source: reference/damodaran_clc/text/multiples.txt (full)

### 6.3 Blog — "Discounted Cashflow Valuations (DCF): Academic Exercise, Sales Pitch or Investing Tool?" (Feb 2015)
*Read in full via WebFetch.* Damodaran defends DCF as a *practical investor tool*,
not an academic abstraction. DCF rests on one descriptive principle — value =
risk- and time-adjusted expected cash flows — and needs neither advanced math nor
faith in modern portfolio theory. He blames the bad reputation on DCF's own
proponents (over-complicated models, using DCF as a sales pitch to justify
predetermined conclusions, sanitizing genuine uncertainty) and on critics who
confuse input disagreements (e.g., over beta) with flaws in the method. He lists
ten "myths" (perfect data required; terminal-value dominance invalidates the
result; uncertainty makes DCF useless for start-ups; intrinsic value should never
change) and concludes DCF works when the analyst embraces uncertainty, keeps it
simple, and stays transparent. Adds beyond the slides: the explicit framing of the
myths the stage chapters then dismantle.
> source: https://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html

### 6.4 Blog — "DCF Myth 2: A DCF is an exercise in modeling and number crunching" (Aug 2015)
*Read in full via WebFetch.* The source of the chapter's "Value = Story + Numbers"
slide. The myth is that DCF is pure technical modeling; Damodaran's rebuttal is
that "the test of a valuation is not in the inputs or the modeling, but in the
story underlying the numbers" and how well that story holds up. He splits
valuation into a narrative hemisphere (a coherent business story) and a numbers
hemisphere (projections that discipline the story), illustrated by Amazon
($32–$468/share across narratives) and the Uber-vs-Coke contrast. The narrative/
numbers balance shifts with the life cycle (story-heavy for young firms,
numbers-heavy for mature). Practical takeaways: strengthen your weaker side
(storyteller vs. cruncher), track narrative consistency against management actions,
and watch for "bar-mitzvah moments" when the market's focus flips from narrative
credibility to delivered numbers. Adds beyond the slides: the operational advice
for keeping story and numbers in a feedback loop.
> source: https://aswathdamodaran.blogspot.com/2015/08/dcf-myth-2-dcf-is-exercise-in-modeling.html

### 6.5 Blog — "Reacting to Earnings Reports: Pricing Metrics and Market Reactions" (Aug 2014)
*Read in full via WebFetch.* A case study in the value-vs-price divide applied to
earnings season. Investors care about *value*; traders care about *price*, which
is why markets fixate on a single metric (an EPS beat) and a stock can jump even
as fundamentals deteriorate. Markets run an "earnings game": analysts set
expectations on a metric, firms try to beat them, and the price reacts to the
beat/miss — not to the full valuation. Which metric "matters" rotates with the
life cycle (user growth / capital access for start-ups; user counts and engagement
for mid-stage names like Twitter/Snapchat; earnings for mature Google/Apple).
Three dangers of metric fixation: incomplete pictures (one metric ignores growth
efficiency, risk, profitability), tunnel vision, and game-playing (once a metric
is known to move the price, firms manage accounting to hit it). Adds beyond the
slides: a real-world demonstration of the price-driver forces (incremental
information vs. expectations).
> source: https://aswathdamodaran.blogspot.com/2014/08/reacting-to-earnings-reports-pricing.html

### 6.6 Blog — "January 2018 Data Update 10: The Price is Right!" (Feb 2018)
*Read in full via WebFetch (correct URL: .../2018/02/january-2018-data-update-10-price-is.html).*
The data-update articulation of the master distinction: stop using "value" and
"price" interchangeably — they can differ for the same asset at the same moment
and are driven by different forces (value by cash flows/growth/risk; price by
sentiment/momentum/liquidity). The distinction is *freeing* because it surfaces
your assumptions and shows the pricing game can reward value destruction and
punish first-principles behavior. Lays out the four-step pricing process (find
comparables, pick the metric level, pick the scaling variable, control for
differences) and reports global pricing data: China most expensive (PE,
EV/EBITDA), then India; Eastern Europe/Russia cheapest; software and healthcare
richly priced, utilities and energy cheap. Adds beyond the slides: live
cross-country/sector multiple data to calibrate what "expensive" means.
> source: http://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-10-price-is.html

### 6.7 Blog — "January 2019 Data Update 9: The Pricing Game" (Feb 2019)
*Read in full via WebFetch.* Restates the value/price split (intrinsic value from
cash flows/growth/risk vs. price from supply-demand/momentum/"animal spirits") and
the four-step pricing process, then offers five pricing propositions: (1) absolute
multiple rules don't work in a relative market — calibrate to the distribution
(US PE ran 6.09 at the bottom decile to 53.70 at the top); (2) global markets share
asymmetric-distribution patterns despite different levels (China median PE 20.63
vs. Russia 9.40), reflecting fundamentals not irrationality; (3) book-value
metrics are overrated — sub-book stocks usually have low ROE or are in declining,
capital-heavy sectors; (4) cheap stocks usually deserve it (low multiples ↔ weak
growth, high risk, poor ROC), not hidden bargains; (5) pricing reflects what
markets actually value (users/subscribers for revenue-less young firms), a
pragmatic adaptation. Adds beyond the slides: the explicit "distribution context
over mechanical screen" rule and concrete decile data.
> source: https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-9-pricing-game.html

## 7. Takeaways for valuation & modeling

For an equity analyst building standardized models (raw material for
[[application_to_copilot]]):

1. **Build the model as the four DCF inputs, explicitly.** Every projection tab
   should resolve to (i) cash flows from existing assets, (ii) the value of growth
   = growth net of the reinvestment it requires, (iii) risk in the discount rate
   (beta in cost of equity, default spread in cost of debt), and (iv) a terminal
   value with a clearly stated, economy-capped perpetual growth rate. The Valuation
   tab's FCFF + WACC + terminal-value structure (project decision of 10/06/2026) is
   exactly this identity; keep the four inputs as labeled, source-tagged
   assumptions.

2. **Keep equity vs. firm valuation consistent — never mix levels.** Discount FCFF
   at WACC to firm value, then bridge to equity by subtracting net debt (and, per
   IFRS-16 guidance, leases) and adding non-operating assets; or discount FCFE at
   cost of equity directly. The EV→equity bridge components (backlog item 4) are
   the netting step §2.3 requires. The firm approach suits the pilots when leverage
   is expected to shift.

3. **Tie every assumption to a story, and every story to a number.** Operationalize
   "Value = Story + Numbers": each proposed assumption (market size → revenue;
   moat → margin/share; scalability → reinvestment; risk → discount rate) should
   carry the narrative justification the copilot already requires (method, source,
   rationale). This is the modeling discipline that prevents both spreadsheet-only
   over-precision and story-only fantasy.

4. **Weight estimation effort and metric choice by life-cycle stage.** Young/high-
   growth pilots → spend effort on revenue growth, margin path, and terminal value
   (value is back-loaded, terminal-value-heavy, narrative-dominated, and judged on
   EV/Sales-type pricing); mature pilots → near-term cash flows, reinvestment, and
   earnings-based multiples (PE, EV/EBITDA). This is the §2.7 / §2.11 rotation made
   actionable for the sector sessions.

5. **Treat multiples as cross-checks, defined and applied correctly.** When the
   Valuation tab reports multiples alongside the DCF, enforce the four-step
   discipline: consistent multiple (equity-over-equity, firm-over-firm — never
   price/EBITDA), uniform timing/accounting, peers chosen on similar growth/risk/
   cash flows (not just industry), and the right companion variable (growth for PE,
   ROE for PBV, margin for PS). Use medians and percentiles, not means, and prefer
   earnings yield / aggregate PE where loss-makers would bias the sample.

6. **Distinguish value from price in every output, per compliance.** The DCF
   produces *value*; multiples produce *price*. Label the target-price/multiples
   output as a pricing estimate with its disclaimer (never a recommendation, per
   the MVP rule), and present the value-vs-price gap as an analytical observation,
   not a buy/sell signal. The pricing process can reward value destruction — so a
   gap is information about market mood, not automatically an opportunity.

> source: synthesis of Ch9.pdf p.1–15 + valuesurvey + multiples + blogs (§6)

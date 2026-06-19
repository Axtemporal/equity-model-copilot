---
chapter: 10
title: Valuing Young and Start-up Businesses
block: Valuation
slides: reference/damodaran_clc/pdf/Ch10.pdf
status: draft
---

# Ch 10 — Valuing Young and Start-up Businesses

## 1. Core thesis

This is the first valuation chapter aimed at the left edge of the life-cycle
curve from [[cap_01_unifying_theory]] — companies that have no operating
history, no (or negative) earnings, negligible revenues, and no clean set of
publicly traded comparables. Damodaran's central argument is that the *absence of
data does not require a new valuation model*: the same intrinsic-value identity
(value = expected cash flows discounted for their risk) still holds, but you must
build the inputs **top-down from a story** rather than bottom-up from history.
The recommended workflow is to tell a coherent, disciplined narrative about the
business, run it through a feasibility filter ("the 3P test": is it Possible,
Plausible, Probable?), translate the story piece by piece into the handful of
inputs that actually drive value (revenue growth from total addressable market ×
market share, a target operating margin, reinvestment via a sales-to-capital
ratio), then go from operating value to per-share equity value while explicitly
charging for **failure risk** (the real chance the firm never reaches steady
state). He contrasts this disciplined intrinsic approach with the venture-capital
"pricing" shortcut — a short forecast cut off with an exit multiple, discounted
at an arbitrarily high target return — which he calls forward pricing dressed up
as valuation, with no honest connection to the firm's actual risk. The chapter's
running case is the 2021 Zomato IPO; add-on sections cover Monte Carlo simulation
for uncertainty, the optionality/value-per-user premium often claimed for
platform companies, and why relative ("pricing") approaches are especially
treacherous for young firms.

> source: Ch10.pdf p.1–25 (slide deck, primary)

## 2. Key concepts & frameworks

### 2.1 The young-company challenge (what breaks)
Young firms break the standard valuation toolkit on every front at once. Cash
flows from existing assets are non-existent or negative; the value added by
growth assets is hard to estimate because there is no track record to extrapolate
from; the different claims on equity (multiple VC rounds, preferred stock,
options) muddy the value-of-equity-per-share calculation; the limited historical
data on earnings and market prices makes *risk* hard to measure; and there is a
"substantial likelihood that the firm may not make it" — a going-concern
question that mature-company models simply assume away. Damodaran frames these as
the four questions every valuation must answer (cash flows from existing assets,
value added by growth, riskiness of those cash flows, when/whether the firm
matures) — all of which are hardest precisely at this stage.
> source: Ch10.pdf p.2

### 2.2 The VC "pricing" response — and its perils
The dominant market response is the venture-capital method, which Damodaran
classifies as *pricing*, not valuation. Mechanically: take an operating metric
(revenue, earnings, users) in a future "exit" year, multiply by a peer-group or
comparable-company multiple to get a forward value, then discount that single
future value back to today at a **target rate of return**. Those target rates are
steep and decline as the firm de-risks toward exit:

| Stage of development | Typical target rate of return |
|---|---|
| Start-up | 50%–70% |
| First stage | 40%–60% |
| Second stage | 35%–50% |
| Bridge / IPO | 25%–35% |

His critique has three prongs: (1) it dodges the hard work of estimating
long-term operating detail by cutting the forecast off prematurely and leaning on
whatever comparables trade at *today*; (2) the target rate is sloppy — it is
supposed to bundle both operating risk and failure risk, but there is no
transparent mapping of how either is built into the number; (3) the net result is
really a pricing exercise in disguise — a forward exit value pulled back at an
inflated required return that is disconnected from the firm's genuine risk, rather
than a true valuation. This sets up the chapter's preference for an intrinsic,
story-driven alternative.
> source: Ch10.pdf p.3–4

### 2.3 Step 1 — Tell a story (intrinsic value starts with narrative)
Because the numbers can't come from history, they must come from a disciplined
story. Damodaran lays out the *components* a good story must address, each of
which later maps to a value input: the product/service and the need it meets;
total potential market size; competition and competitive advantages; expected
market share and profit margins; past financials (if any) and growth trends; unit
economics of the business; access to capital (private vs. public); probability of
success; founder and management capabilities; capital intensity of the business;
and reinvestment needs for growth. The instruction is to "frame a story for the
business that reflects everything you have learned about the business" — the story
is the connective tissue that keeps the eventual spreadsheet internally
consistent. This is the chapter's version of his broader "narrative and numbers"
discipline (see §6.5).
> source: Ch10.pdf p.5

### 2.4 Step 2 — The 3P test (Possible → Plausible → Probable)
Before a story is allowed to become a valuation, it is filtered through three
escalating feasibility hurdles:

- **Possible** (the weakest test): could this happen *at all*, even if everything
  breaks the firm's way? Almost any story is possible; "it is not a fairy tale."
- **Plausible** (stronger): can you make a reasoned argument, with tangible
  evidence it is *already starting to happen*, that this could occur? You need
  some product/market evidence, not just imagination.
- **Probable** (strongest): can you back the story up with *specifics* that
  convert it into valuation inputs, converting uncertainty into your
  expectations? Probable stories produce a *product* (successful financial
  results) you can model.

The test is a guard against both the "fairy tale" valuation (a possible-only
story priced as if certain) and against analyst over-attachment to a favorite
narrative. Only probable elements should drive base-case numbers.
> source: Ch10.pdf p.6

### 2.5 Step 3 — Story pieces → value inputs
Each narrative element is translated into a specific model input, and the chapter
shows the explicit chain that builds free cash flow to the firm:

- **Revenue growth** comes from two routes: a **top-down** approach (total
  potential market × expected market share, then revenue = market share × market
  size) or a **bottom-up** approach (build revenue from existing capacity/units;
  more reliable when the firm already has some operating base). For idea-stage
  firms the top-down TAM route is usually the only option.
- **Operating margin** is a *target* margin the firm is expected to reach as it
  matures (set by reference to a more efficient/mature peer or the steady-state
  economics of the model), with a glide path from today's (often negative) margin
  to that target.
- **Reinvestment** is driven by a **sales-to-capital ratio** (how many dollars of
  revenue each dollar of invested capital generates), distinguishing internal
  reinvestment (the firm builds capacity) from external reinvestment
  (acquisitions). This converts the revenue path into the capital the firm must
  sink in to support it.
- These three feed **"Cash flow to future years"** rolling from one year to the
  next, which is the operating side of value.
- The discount rate has two pieces: a **cost of capital** reflecting operating
  risk (industry, geography, where the firm is in the life cycle, market risk of
  the marginal investor) and, *separately*, **failure risk** (probability the firm
  fails × what investors recover if it does — e.g. cash on hand or a fraction of
  going-concern value).

The key structural point: failure risk is pulled *out* of the discount rate and
handled as a separate probability, so the cost of capital stays honest (close to
a diversified mature-company cost of capital) rather than being inflated to a VC
target rate to "cover" the chance of death.
> source: Ch10.pdf p.7

### 2.6 Step 4A — Value the business: the three key indicators
Damodaran distils the whole exercise to three things the analyst must get right:

1. **Cash-flow patterns.** Expected cash flows embody the revenue-growth, margin
   and reinvestment assumptions. A high-growth firm with negative margins that
   are slow to turn positive will post negative earnings early; layering in the
   reinvestment needed to *deliver* the growth makes early cash flows even *more*
   negative. The shape (deep early negatives → improving → positive at maturity)
   is expected, not a red flag, *if* the story supports the turn.
2. **Discount-rate check.** Because operating and failure risk are separated, the
   cost of capital should reflect only operating risk — and so will often look
   *much lower* than VC target rates, closer to the cost of capital of
   established public companies, especially if the marginal investor is
   diversified. Seeing a 9%–11% cost of capital instead of a 50% target rate is a
   feature, not a bug.
3. **Failure risk.** This input captures the genuine likelihood that many young
   firms don't make it — either they run out of cash and lose access to fresh
   capital, or the business model never reaches profitability. It must be an
   explicit number, not buried in the discount rate.

> source: Ch10.pdf p.8, p.10 (Step 4A key indicators)

### 2.7 Step 4B — From business value to equity value per share
Going from the operating business to a per-share number requires a multi-step
bridge that is more involved for young firms than for mature ones:

1. Discount forecast-period cash flows at the cost of capital.
2. Estimate a **terminal value** at the end of the explicit forecast (assuming a
   constant stable growth and a terminal cost of capital), then discount it back
   → this gives **value of business as a going concern** (PV of forecast cash
   flows + PV of terminal value).
3. Adjust for **failure**: value-of-business-adjusted-for-failure =
   (going-concern value × probability of survival) + (failure value × probability
   of failure), where failure value is typically cash on hand or a haircut to
   asset/going-concern value.
4. **Add cash and non-operating assets** → value of business with cash & non-op
   assets.
5. **Subtract debt** and other contractual/minority claims (debt + minority
   interests in consolidated subsidiaries) → **value of equity**.
6. If valuing equity in a *publicly traded* firm, *add back* the value of any
   options (the option overhang), or for option grants run an option-pricing model
   on them.
7. **Divide by share count** → value of equity in common shares ÷ number of shares
   = intrinsic value per share. For restricted shares or shares contingent on
   vesting, adjust the count for vesting probability.

> source: Ch10.pdf p.9 (Step 4B)

### 2.8 Step 5 — Keep the feedback loop open
A behavioral safeguard: when you build a story, convert it to inputs and a value,
it is easy to develop blind spots and get attached to your own narrative. The
final step is to deliberately seek feedback from people who *think least like you*
and who may know the business better, and — rather than getting defensive —
incorporate what you learn back into the story. This is the antidote to the
over-attachment risk flagged in the 3P test and reinforces the "you're definitely
wrong, just try to be less wrong than everyone else" stance from the CFA talk
(§6.5).
> source: Ch10.pdf p.12

### 2.9 Add-on 1 — Monte Carlo simulation
Rather than a single point estimate, run the valuation as a simulation to surface
the distribution of value. The recommended procedure: (1) identify the few
**"probabilistic" variables** that actually move value (don't try to randomize
dozens of inputs — focus on the handful with real leverage, typically revenue
growth, target margin, sales-to-capital); (2) **define probability
distributions** for them using a mix of historical data, industry averages and
common sense; (3) **check for correlation** across inputs — if two are strongly
correlated, either vary only the higher-impact one or build the correlation
explicitly into the simulation (which needs more sophisticated tooling); (4) **run
the simulation**, drawing one outcome per distribution per trial and recomputing
value, repeating many times (with diminishing marginal information from each extra
trial). The output is a value-per-share distribution and percentile table, which
makes the *uncertainty* itself a deliverable rather than something hidden behind a
single number.
> source: Ch10.pdf p.19–20

### 2.10 Add-on 2 — Optionality (and its limits)
Young companies carry an *upside* from uncertainty: if the product wins broader
acceptance than expected, the firm can use that success to enter businesses that
look non-viable (or aren't even contemplated) today. This "optionality" justifies
a *premium* over the base intrinsic value, and the premium grows as uncertainty
rises. But Damodaran is careful about its weight: the premium depends not just on
the *number* of users/subscribers but on how *loyal* they are, how *intense* their
usage is, and especially whether the platform accumulates **proprietary data** on
those users that becomes a competitive advantage in adjacent businesses (data
others lack is worth more than data everyone has). Even when optionality is real,
*attaching a number* to it is "one of the most difficult tasks in investment," so
any premium should be modest unless user characteristics genuinely support it.
> source: Ch10.pdf p.21–22

### 2.11 Pricing (relative valuation) for young firms — why it's hard
The chapter closes by explaining why the relative-valuation/"pricing" route is
especially fraught for young companies, broken into three classic problems:

- **Standardized price (the scalar).** A pricing metric must be positive (most
  young firms have negative earnings, so P/E is out) and closely tied to value.
  Workarounds: use an *operating metric* you can observe and that plausibly leads
  to revenue/profit (users, GMV/gross order value), or *forecast* the financials
  and price off the forecasted scalar instead of the trailing one.
- **Peer-group assembly.** For private start-ups, "comparables" are themselves
  private, so the only pricing available comes from their last VC round — often
  stale and misleading. Once the firm is public, define the business *broadly* and
  loosen the "similar firm" criteria to get enough peers, even pulling in
  companies from other markets/sectors.
- **Controlling for differences.** Outside of revenue growth, young firms' margins
  and reinvestment measures are unreliable and shifting, so you can't easily
  normalize across peers. To reverse-engineer what the market is pricing in, use
  statistical tools (regressions) to find correlations between observed market
  prices and observable variables.

> source: Ch10.pdf p.23–24

## 3. Metrics, formulas & rules of thumb

The chapter's distinctive contribution is a connected chain of inputs. Written
out, the **TAM → revenue → margin → sales-to-capital → survival** workflow plus
the value-per-user logic:

**1. Revenue from the market (top-down).**
- `Revenue (steady state) = Total addressable market (TAM) × Market share`
- TAM is itself sized from a story (e.g., penetration scaling with per-capita
  income and internet access). Revenue in interim years is interpolated along a
  growth path from today's base to the steady-state level.

**2. Operating profit from a target margin.**
- `EBIT = Revenue × Target pre-tax operating margin`, where the margin glides from
  today's (often negative) level to a maturity target benchmarked on an efficient
  peer or the model's steady-state unit economics.

**3. Reinvestment from a sales-to-capital ratio.**
- `Reinvestment in a year = Δ Revenue ÷ Sales-to-capital ratio`
- A *higher* sales-to-capital ratio means *less* capital needed per dollar of new
  revenue (capital-light); the ratio is usually high early (rebound / low base)
  and settles to a lower steady-state level as the firm scales.

**4. Free cash flow to the firm.**
- `FCFF = EBIT × (1 − tax rate) − Reinvestment`
- Early FCFF is typically deeply negative (negative EBIT *and* heavy
  reinvestment); the turn to positive FCFF is the modeled payoff of the story.

**5. Discount rate — operating risk only.**
- Cost of capital reflects industry/geography/market risk for a (often
  diversified) marginal investor — expect numbers near established-company costs
  of capital, *not* VC target rates. Failure is handled separately (below).

**6. Terminal value.**
- `TV = FCFF(terminal+1) ÷ (terminal cost of capital − stable growth g)`, with g
  capped at the growth rate of the economy/risk-free rate.

**7. Survival/failure adjustment (the input that mature models skip).**
- `Value of equity (adjusted) = (Going-concern equity value × p_survival) +
  (Failure value × p_failure)`, where `p_survival = 1 − p_failure` and failure
  value is often cash on hand or a haircut to asset value. Probability of failure
  is an *explicit* input (Zomato base case: 10%).

**8. Per-share value bridge.**
- `Equity value = Business going-concern value (failure-adjusted) + cash &
  non-op assets − debt − minority interests (+ option value adjustments)`; then
  `÷ shares (vesting-adjusted) = value per share`.

**9. Value-per-user / pricing scalars (relative route).**
- `EV/User = Enterprise value ÷ number of users (or subscribers)`; analogously
  `EV/GOV` (gross order value/gross bookings), `EV/Revenues`, `EV/Gross income`.
  Useful only as a *pricing* cross-check; a "forward" version uses the forecast
  scalar (e.g. 2030 EV/user) to strip out current-stage distortion. The premium
  any user base deserves rises with loyalty, usage intensity, and proprietary
  data — not raw user count.

**Rules of thumb:**
- *Separate operating risk from failure risk.* Don't inflate the discount rate to
  a 50%–70% VC target to "cover" the chance of death — model death explicitly.
- *Few variables, not dozens.* Value is driven by ~6 inputs: revenue growth,
  target operating margin, sales-to-capital, cost of equity, cost of debt, failure
  probability (the CFA "keep it simple" list, §6.5). Simulate those.
- *Margins follow revenue; reinvestment makes early cash flows worse before they
  get better* — the canonical young-company FCFF shape.
- *Negative-earnings firms can still be valued* — but diagnose *why* they lose
  money (temporary growth-stage losses vs. structural model failure) before
  assuming a turn (§6.4).

> source: Ch10.pdf p.7–9, p.14–18, p.25

## 4. Examples & cases

### 4.1 Zomato (2021 IPO) — the running case
Indian online food-delivery and restaurant-discovery platform; Damodaran values
it ahead of its July 2021 IPO. Revenue model has four legs: **transaction fees**
(Zomato keeps ~20–25% of total order value), **advertising** (listed restaurants
pay for visibility), **subscription** (~1.5 million members getting discounts),
and **HyperPure** (B2B restaurant raw-materials supply). The base-case story: the
Indian food-delivery market grows as prosperity and internet access rise; network
effects concentrate the market into a few dominant players with Zomato among them;
as a capital-light intermediary with strong unit economics it earns high margins
at maturity and grows mostly through acquisitions; operating risk is "average" but,
as a money-loser, there is a non-trivial-but-modest failure chance, cushioned by
the post-IPO cash balance.

Base-case inputs translated from that story (slide deck figures):
- **TAM:** total online food-delivery market grows to ~**$25 billion** in a decade
  (the per-capita-income scaling table runs the Chinese/US-penetration scenarios
  up to ~$21.7bn at 100% of China's per-capita-GDP penetration; the base assumes
  $25bn).
- **Market share:** Zomato to ~**40%** in steady state.
- **Target pre-tax operating margin:** trends toward **35%** at maturity (the
  accompanying blog uses 30% — see §6.1; the slide deck states 35%).
- **Reinvestment / sales-to-capital:** ~**Rs 5** of revenue per rupee of capital
  next year (COVID rebound), **Rs 3** in years 2–5, settling at **Rs 2.5**
  thereafter; reinvestment mostly acquisitions + technology.
- **Cost of capital:** ~**10.25%** (rupee) early, easing to ~**9%** in steady
  state, reflecting Indian macro exposure.
- **Probability of failure:** **10%** (size + post-IPO cash buffer keep it low,
  but it is still burning cash and dependent on future capital).
- **Intrinsic value:** ~**₹43/share** (slide deck; the blog states ₹41) versus an
  IPO price around ₹72–75 — i.e., Damodaran judged the IPO pricing rich relative
  to the base-case intrinsic value.

A Monte Carlo simulation on the Zomato story (varying growth in the Indian market,
Zomato's market share, and pre-tax margin) produces a value-per-share
distribution and percentile table — used to show how wide the honest uncertainty
band is, not to manufacture a single "right" number.
> source: Ch10.pdf p.9–18, p.20

### 4.2 Zomato optionality verdict
Applying the optionality test (§2.10) to Zomato: it has the *large numbers* but
falls short on *intensity* (users engage only when ordering food) and *proprietary
data* (engagement is narrow). Any platform expansion is likely to stay
food-adjacent (e.g., grocery), which limits option value. Conclusion: any premium
over the ~₹43 intrinsic value for "user base + optionality" should be **small**,
given those user characteristics.
> source: Ch10.pdf p.21–22

### 4.3 Zomato vs. DoorDash — the pricing comparison
A pricing table contrasts Zomato (2020 actual and a 2030 forecast) with DoorDash
(2020 and 2030 forecast) on current and forward multiples, illustrating how
relative multiples whipsaw for young firms:

| Metric (US$ unless noted) | DoorDash 2020 | DoorDash 2030F | Zomato 2020 | Zomato 2030F |
|---|---|---|---|---|
| Market cap | $57,860 | — | $8,600 | — |
| Enterprise value | $53,640 | — | $7,500 | — |
| Gross bookings (GOV) | $18,897 | $72,072 | $1,264 | $10,038 |
| Revenues | $3,601 | $9,009 | $266 | $2,208 |
| Gross income | $1,864 | $4,955 | $140 | $1,325 |
| EBIT | −$412 | $1,802 | −$64 | $773 |
| Platform users (m) | 20 | 50 | 40 | 200 |
| EV/GOV (current → forward) | 2.84 → 0.74 | | 5.93 → 0.75 | |
| EV/Revenues (current → forward) | 14.90 → 5.95 | | 28.20 → 3.40 | |
| EV/Gross income (current → fwd) | 28.78 → 10.83 | | 53.57 → 5.66 | |
| EV/User (current → forward) | $2,682 → $1,072.80 | | $187.50 → $37.50 | |

The takeaway: on **EV/User** Zomato looks far *cheaper* than DoorDash, but on
**EV/Revenues** it looks far *more expensive* — the same two companies rank
opposite ways depending on the scalar, which is exactly why pricing young firms by
a single multiple is unreliable, and why forward (forecast-based) scalars differ
so sharply from current ones.
> source: Ch10.pdf p.25

## 5. Data & tools

- **Revenue (price-to-sales) multiples by industry** — Damodaran's by-industry
  EV/Sales and Price/Sales datasets, the natural pricing scalar when young firms
  have no earnings:
  - US: `psdata.xls` — <https://pages.stern.nyu.edu/~adamodar/pc/datasets/psdata.xls>
  - Global: `psdataGlobal.xls` (same `/datasets/` path).
  (Cataloged by URL only; raw industry data not copied here.)
- **Zomato IPO valuation model** — the full spreadsheet behind the chapter's case,
  implementing the TAM → revenue → margin → sales-to-capital → failure-adjusted
  DCF and the Monte Carlo layer:
  <https://pages.stern.nyu.edu/~adamodar/pc/blog/ZomatoIPO.xlsx>
  (companion to the Zomato IPO blog, §6.1). A direct template for the copilot's
  young-company valuation tab.
- Webcast for the chapter: <https://youtu.be/i80avS70k8E>.

## 6. Supplementary readings — distilled

### 6.1 Blog — "The Zomato IPO: A Bet on Big Markets and Brilliant Managers?" (Jul 2021)
*Read in full via WebFetch.* The narrative backbone of the chapter's case. Damodaran
walks the same TAM → market share → margin → sales-to-capital → failure-risk chain
in prose: Indian food-delivery TAM ~$25bn in a decade (upside ~$40bn), Zomato to
~40% share, a **30%** pre-tax target margin (note: the *slide deck* states 35% —
the blog and deck differ slightly), a capital-light sales-to-capital path, a
rupee cost of capital incorporating Indian country risk, and a 10% failure
probability — yielding an intrinsic value of ~**₹41/share** (deck: ₹43) against an
IPO price of ₹72–75, so he judged the IPO **overpriced**. He stresses that the
EV/user-vs-EV/revenue contradiction (cheaper than DoorDash on one, dearer on the
other) shows how comparables can be cherry-picked, and frames any investment as a
*joint* bet on the company, the sector and the country — he'd buy on price
weakness, not at the IPO. *Adds beyond the slides:* the explicit "bet on a
company + sector + country" framing and the candid acknowledgment that plausible
stories could justify >₹100, underscoring the uncertainty band.
> source: https://aswathdamodaran.blogspot.com/2021/07/the-zomato-ipo-bet-on-big-markets-and.html

### 6.2 Blog — "The Bonfire of Venture Capital: The Good, the Bad and the Ugly Side of Cash Burn!" (Aug 2016)
*Read in full via WebFetch.* The deep dive on the chapter's **failure-risk** input.
Damodaran defines cash burn as persistent negative free cash flow and operationalizes
it with two metrics: the **cash burn rate** (cash consumed per period) and **cash
runway** (months until reserves run out = cash ÷ burn rate; e.g., $1bn at −$500m/yr
= 2 years). He splits cash burn into: the **good/benign** case (a money-*making*
business showing negative cash flows only because of large, *discretionary*
reinvestment — manageable, because spend can be throttled if capital tightens, and
margins/reinvestment improve as growth scales); the **bad** case (margins
deteriorating despite scaling — "venture capital hell," cash flows negative
indefinitely); and the **ugly** case (a money-*losing* firm that *also* reinvests
very little — burning cash with no growth payoff). Cash burn destroys value through
three channels: **dilution** (equity raised to fund burn cuts existing stakes),
**lost growth** (when capital dries up, reinvestment is slashed), and **distress**
(inability to fund operations risks liquidation and loss of going-concern value).
The decisive variable is **access to capital**: a cash-burning firm depends on open
capital markets to survive, so large cash balances and strong capital relationships
lower failure risk. *Adds beyond the slides:* the runway math and the
good/bad/ugly taxonomy give a concrete, defensible way to *set* the failure
probability number the deck treats as a single input.
> source: https://aswathdamodaran.blogspot.com/2016/08/the-bonfire-of-venture-capital-good-bad.html

### 6.3 Reading — "The Dark Side of Valuation: Firms with No Earnings, No History and No Comparables" (SSRN 1297075 / Stern WP 99-022)
*Full text fetched as PDF (text auto-extraction partial; distilled from the
extracted summary + verified SSRN/Semantic Scholar abstract).* The intellectual
ancestor of the chapter. Thesis: standard DCF is easy with positive earnings, long
history and many comparables; this paper handles the cases where one or more is
missing, insisting the *fundamentals of valuation still apply*. It first treats
firms with **negative earnings**, arguing the fix depends on *why* they lose
money — temporary/cyclical or growth-stage losses warrant normalizing toward
achievable margins, whereas structural (broken-model) losses may imply zero or
negative equity value. For **young firms with negligible revenue**, it replaces
absent history with industry benchmarks: project *when* the firm reaches
industry-average margins, then back out the required growth path. Its signature
contribution is making **survival probability explicit** — young unprofitable
firms face real bankruptcy risk that standard discount rates don't capture, so
adjust cash flows/value for the chance the firm survives to profitability. *Adds
beyond the slides:* the typology of *reasons* for negative earnings (which
determines whether a turn is even modelable) and the original case for separating
survival risk from the discount rate.
> source: https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/HighGrow.pdf (SSRN abstract_id=1297075)

### 6.4 Reading — "Valuing Young, Start-up and Growth Companies: Estimation Issues and Valuation Challenges" (SSRN 1418687, 2009)
*Abstract + Damodaran's own paper-page description obtained (full-text PDF would
not auto-extract — distilled abstract-only, cross-checked against the overlapping
slide content and §6.3).* The formal monograph version of the chapter's method.
Abstract: young companies are hard to value because some are idea/start-up
businesses with little/no revenue and operating losses, even profitable ones have
short histories and depend on private (owner + VC) capital, and standard
techniques for cash flows, growth and discount rates "either do not work or yield
unrealistic numbers" — and crucially, the reality that *most young companies do
not survive* must enter the valuation. Damodaran's description: "How do you value
a young or start-up business with little to show in terms of operating
performance?... we examine ways in which we can adapt valuation approaches to
account for the absence of historical information and the possibility that many of
the young firms we value will not make it through to success." The paper's
estimation issues map one-to-one onto the chapter: revenue (top-down from market),
target margins, reinvestment/sales-to-capital, an operating-risk-only discount
rate, an explicit survival/failure adjustment, and the equity-claims/dilution
problem (multiple share classes, options) in getting to per-share value. *Adds
beyond the slides:* the systematic, paper-length treatment of *each* estimation
issue and the dilution/multiple-claims mechanics that the deck only gestures at in
the Step 4B bridge.
> source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1418687 (abstract; Stern page <https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/younggrowth.pdf>)

### 6.5 Reading — "Tell Me a Story: Aswath Damodaran on Valuing Young Companies" (CFA Institute Enterprising Investor, May 2022)
*Read in full via WebFetch (followed 301 redirect to rpc.cfainstitute.org).* The
"narrative and numbers" discipline behind Step 1. Core line: "a good valuation is
a marriage between stories and numbers... every number in your valuation has to
have a story attached to it." It frames uncertainty as the real enemy — three
axes (estimation vs. **economic**, with ~90% of valuation uncertainty being
economic and unavoidable; **micro** (firm-level, dominant for young firms) vs.
**macro**; **continuous** vs. **discrete/catastrophic**) — and warns against the
*unhealthy* coping responses (paralysis, denial, stale rules, outsourcing to
consultants). Its prescriptions reinforce the chapter: (1) build a coherent
narrative; (2) **keep it simple** — value hinges on ~6 inputs: revenue growth,
operating margin, sales-to-invested-capital, cost of equity, cost of debt, failure
probability; (3) use **Monte Carlo** distributions, not point estimates. It flags
classic DCF errors (ignoring economics in terminal value, growing faster than the
economy forever, over-tuning the discount rate when ~80% of global firms' cost of
capital sits between 4.5%–10%, and cramming failure risk into the discount rate).
Memorable: "you're definitely wrong" — aim to be *less wrong than everybody else*,
correct errors, and solicit dissenting views (the feedback loop of Step 5).
*Adds beyond the slides:* the taxonomy of uncertainty and of unhealthy responses,
and the explicit "6 inputs" minimalism.
> source: https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/tell-me-a-story-aswath-damodaran-on-valuing-young-companies (Stern PDF backup: <https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/narrativeandnumbers.pdf>)

## 7. Takeaways for valuation & modeling

For an equity analyst building standardized models (raw material for
[[application_to_copilot]]):

1. **Drive young-company revenue top-down from TAM × market share, not from
   history.** The copilot's young/idea-stage path should ask for (a) total
   addressable market with a sizing story and source, (b) a steady-state market
   share, and (c) a glide path to steady state — never extrapolate a one- or
   two-year revenue history. Make the TAM and share *assumptions in their own
   cells* with method + source (project compliance), because they dominate value.

2. **Set a target operating margin and converge to it; expect (and explain) early
   losses.** Model margin as a glide from today's (often negative) level to a
   maturity target benchmarked on an efficient peer, and let early FCFF be deeply
   negative because reinvestment to fund growth compounds the EBIT losses. The
   assumption layer should flag that the negative early earnings are *modeled*, not
   an error, and tie the turn date to the story.

3. **Reinvest via a sales-to-capital ratio, declining over time.** Add a
   sales-to-capital input (revenue per dollar of invested capital), typically high
   early and settling lower, with `Reinvestment = ΔRevenue ÷ sales-to-capital`.
   This is the young-company analogue of the mature-firm capex/working-capital
   schedules and keeps growth and capital internally consistent.

4. **Separate operating risk from failure risk — never bury death in the discount
   rate.** Keep the cost of capital near a diversified-investor / mature-company
   level (resist VC-style 50%+ target rates) and add an *explicit* probability of
   failure with a failure value (cash on hand or asset haircut), folding it into
   the equity bridge as a survival-weighted average. Set the failure probability
   using the cash-burn runway logic from §6.2 (cash ÷ burn rate, plus quality of
   capital access). This is a concrete extension to the copilot's Valuation tab for
   pre-profit names.

5. **Build the full equity bridge for messy cap tables.** For young firms the
   business-to-per-share bridge must handle cash & non-operating assets, debt,
   minority interests, option overhang, and vesting-adjusted share counts — more
   than the standard mature-firm EV→equity bridge. The copilot should expose these
   bridge components as inputs (consistent with the project's EV→equity bridge
   backlog item).

6. **Treat relative/pricing multiples as a cross-check only, with forward
   scalars.** When earnings are negative, fall back to EV/Sales, EV/GOV or EV/User
   for *pricing*, but flag their unreliability (the DoorDash-vs-Zomato reversal)
   and prefer *forecast-based* (forward) scalars. Never present a young-company
   pricing multiple as the valuation — it is a sanity check on the intrinsic
   number, never a substitute (and never a recommendation, per compliance).

7. **Surface uncertainty explicitly (simulation) and keep a feedback loop.** Where
   feasible, run the ~6 key inputs through a Monte Carlo layer and report a
   value-per-share distribution/percentiles rather than a single point — and design
   the assumption-approval flow to invite dissenting input (Step 5) so the model
   doesn't ossify around one story. Optionality premia (platform/user-base) should
   be small unless loyalty, usage intensity and proprietary data justify them.

> source: synthesis of Ch10.pdf p.5–25 + blogs (§6.1–6.2) + readings (§6.3–6.5)

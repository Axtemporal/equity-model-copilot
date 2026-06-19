---
chapter: 13
title: Valuing Declining Businesses
block: Valuation
slides: reference/damodaran_clc/pdf/Ch13.pdf
status: draft
---

# Ch 13 — Valuing Declining Businesses

## 1. Core thesis

This chapter takes valuation to the far end of the life-cycle arc [[cap_01_unifying_theory]]:
the firm whose revenues are flat or shrinking, whose margins are compressing, and
that often carries a debt load taken on in healthier days. Damodaran's central
argument is that the **going-concern assumption baked into conventional DCF and
relative valuation systematically overstates the value of declining and,
especially, distressed firms**, because both methods implicitly assume the firm
survives to reach a stable, ever-growing terminal state. For a declining firm the
correct picture is the inverse of the growth story analysts are trained on:
**negative revenue growth, margins falling toward (or below) the industry average,
negative reinvestment (divestitures that bring cash *in*), and cash flows that
exceed earnings.** On top of that, a meaningful subset of these firms faces a real
probability of *not making it* — distress that truncates the cash flows long before
the terminal year. The chapter therefore does two things: (1) it builds the
declining-firm DCF on a **story** about *why* the business is shrinking and *how
management will respond* (denial, desperation, acceptance, reinvention), translating
that story into negative-growth inputs; and (2) it layers on the machinery to handle
distress — estimating a **cumulative probability of failure**, blending the
going-concern value with a **distress-sale / liquidation value**, and recognizing
that in deeply distressed firms **equity behaves like an out-of-the-money call
option** on the firm's assets and retains value even when the firm is technically
insolvent. It also introduces **sum-of-the-parts (disaggregated) valuation** as the
natural tool for the divestiture-heavy, multi-business declining firm.

> source: Ch13.pdf p.1–10, p.27; eqnotes/distress.pdf p.1–2; papers/NewDistress.pdf (abstract)

## 2. Key concepts & frameworks

### 2.1 The six tell-tale signs of a declining firm
Damodaran opens by cataloguing the operating and financial fingerprints of decline,
which together define the valuation problem:
- **Stagnant or declining revenues** — the most telling sign is an inability to grow
  the top line over long stretches *even in good times*; revenues that grow below
  inflation are real (inflation-adjusted) shrinkage.
- **Shrinking or negative margins** — falling pricing power, compounded by the firm
  cutting its own prices to defend volume, drags operating margins down.
- **Asset divestitures** — because existing assets are often worth more to *someone
  else* (who can redeploy them better), declining firms sell assets far more
  frequently than younger firms.
- **Interspersed with growth acquisitions** — paradoxically, some declining firms
  *buy* growth, often out of desperation ("defensive mergers").
- **Big payouts (dividends + buybacks)** — with little to reinvest in, low-debt
  declining firms return large amounts of cash, sometimes paying out *more than they
  earn*.
- **The wrong edge of the leverage sword** — debt taken on when the firm was healthy
  becomes a crushing burden against stagnant/declining earnings, exposing the firm
  to distress.

Applies squarely to the **decline** stage (and the late-mature → decline transition).
> source: Ch13.pdf p.2

### 2.2 Why decline is economically rational — earning below the cost of capital
In many declining firms, existing assets — even if accounting-profitable — earn a
return **below the cost of capital**. The mechanical consequence: discounting their
cash flows back at the cost of capital yields a value *less than the capital invested*
in them. The rational response is then to **shrink** — divest or liquidate the
assets that destroy value — and a sensible management does exactly that. Two
counter-intuitive facts follow that "analysts trained at healthy companies" resist:
**negative growth rates** and **cash flows that exceed earnings** (because
divestitures are negative reinvestment that releases cash). Decline is not a modeling
error to be smoothed away; for a bad business it is the *value-maximizing* path.
> source: Ch13.pdf p.3–4; eqnotes blog "No light at the end of the tunnel" (§6.2)

### 2.3 Divestitures break the historical data
Because declining firms divest mid-period, the historical record becomes
discontinuous and harder to forecast from:
- All operating numbers (revenues, margins, reinvestment) are *contaminated* — the
  full-year figure mixes results from before and after a divestiture.
- **Risk parameters** estimated from market data (betas from past prices/returns) are
  distorted when a chunk of the business is sold partway through the estimation
  window.
The practical upshot: don't extrapolate naïvely from reported history; identify which
assets will go, model the operating effect of their departure, and — critically —
estimate the **proceeds** received, because a divestiture by itself is value-neutral;
value turns on price received vs. value given up.
> source: Ch13.pdf p.3; NewDistress.pdf p.4–5

### 2.4 Feedback loops: payouts, divestitures and distress move the discount rate
The declining firm's actions change the very inputs used to value it, so the model
cannot treat weights and rates as static:
- **Large dividends/buybacks** shrink the market value of equity (lower price,
  fewer shares). If debt isn't repaid proportionately, the **debt ratio rises**,
  pushing up the cost of debt, cost of equity, and WACC.
- **Divestitures and acquisitions** change the firm's operating risk → its beta and
  cost of capital shift over the forecast.
- **Distress itself** raises both costs: default risk pushes the cost of debt up
  (ratings can fall to junk), and a climbing D/E pushes the cost of equity up as
  earnings volatility rises.
> source: Ch13.pdf p.5

### 2.5 Valuation starts with a story — and a diagnosis
A declining-firm valuation begins with a *narrative grounded in reality*: a shrinking
market, intensifying competition for what's left, and survival worries. The first
move is a **diagnosis** of *why* the market/revenues are shrinking — causes range
from social/health costs (tobacco), to an aging customer base, to outside disruption.
The story must then incorporate **how management will respond**, which Damodaran
sorts into four archetypes (§2.6). Listening to management's own turnaround plans
"can easily lead to fairy tales," so the analyst must run a **3P / fairy-tale test**:
is the plan *possible, plausible, and probable*, and is *this* management team and
resource base capable of delivering it? Three factors govern that judgment:
- **Company-specific vs. sector decline** — easier to engineer a turnaround when the
  problem is the company's, not the whole industry's.
- **Competitive context** — easier when most peers are healthy and only a few firms
  are declining, than when the entire sector is fighting decline at once.
- **Management history & capabilities/resources** — even a plausible plan needs the
  team, capital, infrastructure and people to execute.
> source: Ch13.pdf p.7–8

### 2.6 The four management responses to decline (the central typology)
This is the chapter's organizing framework: each response implies a *different*
trajectory for revenue growth, profitability, reinvestment and risk, and therefore a
different set of valuation inputs. From the slide matrix (p.9):

| Response | Revenue growth | Profitability | Reinvestment | Risk |
|---|---|---|---|---|
| **Denial** (refuses to face decline; blames temporary factors) | Negative | Long-term decline | Continue status quo in existing business | Stable operating risk **+ increased failure risk** |
| **Desperation** (tries everything — buys growth companies, chases the disruptors) | Positive *blips* from acquisitions/investments | May see short-term boosts but fades to long-term decline | Significant, unpredictable reinvestment (acquisitions) | **Volatile** operating risk + increased failure risk |
| **Acceptance** (accepts life-cycle position; adopts age-appropriate policies) | Negative | Short-term decline, then **stability** | **Negative** (divestitures) | Stable operating risk + **stable** failure risk |
| **Reinvention** (rediscovers core competencies; enters new business/markets) | Positive, but may take time to unfold | Decline near-term, then **rises** to new-business margins | Negative in existing business, **positive in new** business(es) | **Melded** operating risk reflecting the new business |

How each maps to value (p.10):
- **Denial** → declining revenues + compressing margins → long-term earnings/cash-flow
  decline → either **distress (equity worth nothing)** or a "bad business" terminal
  value where equity is worth very little.
- **Acceptance** → short-term shrinkage and margin compression, then a **steady-state
  terminal value** for a *smaller but healthier* firm — or a **liquidation value** if
  that pays more.
- **Desperation** → no predictable pattern; temporary surges from acquisitions fade
  and are more than offset by the reinvestment cost — "value destruction on steroids."
- **Reinvention** → no short-term reprieve, but *if it works*, growth/margins/
  reinvestment migrate toward the new business profile over time.

The analyst should also price in the chance the chosen path changes: new
CEO/board breaks the denial path (re-assess); **activist investors** can push back on
desperate management; and acceptance/reinvention paths "take a long time," so there's
always a risk investors lose faith and the firm abandons them before they pay off.
> source: Ch13.pdf p.7, p.9–11 (p.9 read as image)

### 2.7 Why distress matters — truncation risk
Distress is the wild card that separates "declining" from "dying." Its source varies:
for some firms it's **too much debt** (failure to make debt payments → bankruptcy/
liquidation/reorganization); for others it's the **inability to meet operating
expenses**. When distress hits, the firm's life *terminates* and all cash flows
beyond that point are lost. In DCF terms, distress **truncates the cash flows before
the firm ever reaches the terminal "nirvana"** — which is precisely why a going-concern
DCF, which assumes the firm always survives to stable growth, overstates value.
Damodaran rebuts the "purist DCF defense" (with unlimited capital access no
worth-more-as-going-concern firm is ever liquidated): capital access is *not*
unlimited, especially for troubled firms in stressed markets (Enron, Kmart), and
distress sales rarely fetch fair value because of the need to liquidate quickly.
> source: Ch13.pdf p.10; eqnotes/distress.pdf p.23–25; NewDistress.pdf p.6–8

### 2.8 Relative valuation traps for declining firms
Pricing a declining firm against peers is hazardous in predictable ways:
- If the firm is an **outlier in a healthy sector**, it will *look cheap* — it trades
  at lower multiples — but that's the market correctly penalizing weaker growth,
  thinner profitability and higher risk. You must explicitly **control for those
  fundamental differences**, not declare a bargain.
- If the **whole sector is declining**, you must control for the *degree* of decline
  across firms.
- **Forward multiples** sidestep some current-loss problems but reintroduce the
  distress problem — they only work if you assume guaranteed survival (no default).
- **Book value as a liquidation proxy is dangerous**: in a bad business, buyers won't
  pay book value for assets whose underlying economics are poor — so book-scaled
  multiples again make declining firms look like false bargains.

Scaling choices for the multiple (p.16): **price/book or EV/invested-capital**
(market value vs. accounting capital invested), **EV/replacement cost** (what it would
cost to replicate the assets), or **forward operating numbers** (scale to *future*
estimates, as with start-ups — useful if you believe the firm can stabilize/turn
around). Peer-group choice (p.17): either assemble *other declining/distressed firms*
(only works if many firms are troubled at once, and risks lumping together different
degrees of distress) **or** compare to *healthy peers* and explicitly collect and
control for revenue growth, profitability and reinvestment. The pricing should reflect
**operating performance** (growth, margins), **distress** (forced-liquidation risk),
and **management response** (denial/desperate management should price lower than
acceptance/purposeful management).
> source: Ch13.pdf p.15–18

### 2.9 Equity as an option in deeply distressed firms ("basket-case equities")
For a money-losing, heavily indebted firm, equity is **not** worthless. With limited
liability, equity is a **residual claim** on the firm's assets after debt is paid —
mathematically a **call option** on the firm's asset value, struck at the **face value
of debt**, expiring when the debt comes due. Even when the firm value sits *below* the
face value of debt (the firm "owes more than it owns"), the equity option retains value
from two sources: (1) the **time premium** — the time until the bonds mature, during
which asset value might recover above the debt — and (2) the chance the assets rise
above the debt face value before maturity, exactly as a deep-out-of-the-money traded
option commands value. Three implications:
- **Risk becomes an ally.** Because option value rises with the volatility of the
  underlying, *more uncertainty in firm value raises equity value* in a distressed
  firm — the opposite of the healthy-firm intuition.
- This explains why stock in Chapter-11 / effectively-bankrupt firms still trades at
  a positive price.
- **Debt–equity agency conflict.** The option lens explains why equity holders and
  lenders diverge on how to run the business — equity (the option holder) wants more
  risk, lenders want less — and the conflict *worsens* as operations deteriorate and
  leverage rises (risk-shifting / asset-substitution).
> source: Ch13.pdf p.26–27 (p.26 read as image); eqnotes/distress.pdf p.46–63

### 2.10 Aggregated vs. disaggregated (sum-of-the-parts) valuation
DCF is **additive**: a multi-business firm can be valued either *aggregated* (sum the
cash flows across businesses, discount at a value-weighted blended rate) or
*disaggregated* (value each business with its *own* cash flows and discount rate, then
sum). In theory both give the same answer. Aggregated valuation dominates in practice
because (a) investors buy whole companies, not parts, and (b) disclosure is at the
whole-company level. But **disaggregated / SOTP** is the right tool for the
divestiture-heavy declining firm, for four reasons:
- **Fundamental differences** — assign each business its own risk/growth/cash-flow
  profile instead of forcing one blended profile.
- **Growth differences** — a blended bottom-up beta must *change over time* if
  segments grow at different rates; valuing separately avoids that mess.
- **Transactional reasons** — you often need the value of just the *part* being sold
  or spun off (acute when a firm is being broken up).
- **Management reasons** — valuing each division separately lets you monitor and
  improve divisional performance.

SOTP procedure (p.22): tell a story for *each part* (stand-alone management) → run the
3P test on each part → convert each part's story to inputs, value each part, **sum,
then net out the value drag from unallocated corporate costs** → add cash/cross-holdings
and net out debt to reach equity value. The pricing analogue (p.23): pick a scalar and
a peer group *per part*, control for differences per part, price each part and
aggregate.
> source: Ch13.pdf p.20–23 (p.22–23 read as images)

### 2.11 Liquidation value vs. going-concern value
SOTP-by-liquidation can yield a *different* (often lower) number than a conventional
going-concern pricing, for three reasons:
- The proceeds from **selling individual assets to the highest bidders** can exceed
  the going-concern value when assets are worth more redeployed elsewhere.
- A **forced** liquidation (debt coming due, distress) draws **discounted prices** —
  buyers smell the urgent need for cash and extract bargains.
- Liquidation triggers **tax consequences**, especially selling old, low/zero
  book-value assets (taxable gains).

Cautions on estimating liquidation value: assets with **business entanglements**
can't be valued individually; the **faster** the forced sale, the **deeper** the
discount to fair value; and **it is almost never appropriate to treat book value as
liquidation value**. For most *healthy* firms, going-concern value trumps liquidation;
for declining/distressed firms, the analyst should check whether liquidation pays more.
> source: Ch13.pdf p.24–25

## 3. Metrics, formulas & rules of thumb

This chapter (and its companion distress notes) is unusually formula-rich. Below are
the load-bearing relationships, written so the modeling layer can implement them.

### 3.1 Negative growth, divestitures and terminal value
- **Negative growth is real and common.** Damodaran's data: ~40% of ~46,814 firms had
  declining revenues in 2015; ~25% had a negative revenue CAGR over 2006–2015; with
  sector concentration (Oil/Gas 79.2% negative in 2015, Steel 73.2%, Publishing
  53.8%). Perpetual growth is mathematically impossible — "the global marketplace is
  not big enough to accommodate ever-expanding behemoths." (blog §6.4)
- **Reinvestment ↔ growth identity holds with a negative sign.** The standard
  `g = Reinvestment Rate × ROIC` still applies; for a shrinking firm the *reinvestment
  rate is negative* (net divestiture = cash inflow). Worked example: with g = −5% and
  ROIC = 7.5%, Reinvestment Rate = g/ROIC = −66.67% (i.e., the firm releases cash
  equal to 66.67% of after-tax operating income each year). (blog §6.4)
- **Terminal value with negative growth (no liquidation premium):**
  `TV = FCFF_(n+1) / (r − g)`, and a *negative g enlarges the denominator*, so it is
  perfectly well-defined. Example: $100M after-tax operating income, r = 10%, g = −5%
  → `TV = 100 / (0.10 − (−0.05)) = $666.67M`. (blog §6.4)
- **Terminal value with an asset-liquidation premium** (assets fetch more sold than
  retained, here ROIC on divested assets ≈ 7.5% modeled as releasing value): the same
  case rises to **≈ $1,111.33M**. The rule: *as long as you can get more for divesting
  assets than for keeping them as continuing investments, liquidating raises terminal
  value.* (blog §6.4)
- **Decision rule:** if **ROIC < cost of capital**, negative growth (shrinking) *adds*
  value; growth *destroys* it. The healthy-firm intuition is inverted.

### 3.2 The going-concern firm value template (declining DCF)
`FCFF = Revenue × Operating Margin × (1 − t) − Reinvestment`, where for a declining
firm Revenue trends down, margin converges to (or below) the industry average,
Reinvestment is **negative** (divestiture cash inflows), and the discount rate
*migrates over time* as the debt ratio normalizes from its distressed high toward a
target (e.g., the Global Crossing case runs WACC and debt ratio down across the
forecast as the firm is "nursed back to health"). Standard build:
`Value of operating assets (PV of FCFF + PV of TV) + cash & non-op assets = Firm value;
− debt = Equity value; − equity options = value of equity in common stock.`
> source: eqnotes/distress.pdf p.3–4, p.30–31

### 3.3 Estimating the cumulative probability of distress
Three methods (estimate it **cumulatively over the DCF horizon**, often 10 years):

**(a) From the bond rating** — map the rating to a historical cumulative default
probability. Selected figures from Damodaran's table (cumulative probability of
distress):

| Rating | 5-year | 10-year |
|---|---|---|
| AAA / AA | 0.03% | 0.03% |
| A | 0.18% | 0.25% |
| BBB | 0.19% | 0.40% |
| B | 1.35% | 2.42% |
| CCC/CC | 2.50% | 4.27% |
| C and below | 9.27%+ | 16.89% → up to ~87% for the lowest tiers |

(The BB&B case in this chapter uses a **23.74% failure probability** off a Moody's
**B1** rating; the eqnotes Global Crossing case derives ~76.63% — see below.)

**(b) Back it out of the bond price** — solve for the annual default probability
(π_distress) that makes the bond's promised coupons and principal, each multiplied by
the survival probability `(1 − π)^t`, discounted at the riskfree rate, equal the
observed market price. Global Crossing example: a 12% coupon, 8-year bond trading at
$653 with a 5% riskfree rate solves to an **annual default probability ≈ 13.53%**.
Cumulative survival over 10 years = `(1 − 0.1353)^10 = 23.37%`, so **cumulative
probability of distress = 1 − 0.2337 = 76.63%**. (Use Excel Solver in practice.)

**(c) Statistical / probit model** — build an indicator (1 = went bankrupt, 0 =
survived) and regress it on beginning-of-period financials, e.g.
`Distress Dummy = a + b·(Debt/Capital) + c·(Operating Margin)` to predict the
probability of distress out of sample.
> source: eqnotes/distress.pdf p.32–35

### 3.4 Incorporating distress into value (the blend)
- **Expected-cash-flow adjustment (period by period):**
  `Expected CF_t = CF_t × (1 − Probability of distress_t)`.
- **Going-concern-plus-distress blend (the headline formula):**
  `Value of Equity = DCF equity value × (1 − Prob. distress) + Distress-sale equity
  value × Prob. distress`.
  Global Crossing worked example: going-concern equity = $3.22/share, distress sale
  value of equity = $0 (25% of $14,531M book capital = $3,633M < $7,647M book debt, so
  nothing left for equity), cumulative distress = 76.63% →
  `Value = 3.22 × (1 − 0.7663) + 0 × 0.7663 = $0.75/share`.
- **Distress-sale value** is estimated as a **percent of book value** (lower in a bad
  economy / when peers are also distressed) **or** as a **percent of the going-concern
  DCF value** — *never* as the full PV of expected cash flows (if it were, distress
  wouldn't matter).
- **Relative-valuation analogue:** `Distress-adjusted value = Healthy-peer relative
  value × (1 − Prob. distress) + Distress sale proceeds × Prob. distress`. Or adjust
  the multiple by rating — Damodaran's telecom example: Value/Book Capital of 1.70 (A)
  → 1.61 (BBB) → 1.18 (BB) → 1.06 (B) → 0.88 (CCC) → 0.61 (CC).
- **Adjusted Present Value (APV):** `Firm Value = Unlevered firm value + Tax benefit of
  debt − Expected bankruptcy cost`, where `Tax Benefit ≈ tax rate × Debt` and
  `Expected Bankruptcy Cost = (Unlevered firm value − Distress sale value) × Prob.
  distress`.
> source: eqnotes/distress.pdf p.28–29, p.36–43

### 3.5 Equity as a call option (Black–Scholes parameters)
Map the firm onto an option:

| Option input | Firm-valuation analogue |
|---|---|
| Underlying asset value S | Value of the firm's assets |
| Strike price K | **Face value of outstanding debt** |
| Time to expiry t | Life / weighted duration of the debt |
| Variance σ² | Variance in firm value |
| Riskless rate r | Treasury rate matching the option life |

Payoff to equity on liquidation = `V − D if V > D, else 0` (limited liability).
**Worked example:** S = $100M, σ = 40% (σ² = 0.16), K = $80M zero-coupon debt, t = 10y,
r = 10% → Black–Scholes call (equity) = `100·N(d1) − 80·e^(−0.10·10)·N(d2)` with
d1 = 1.5994, d2 = 0.3345 → **equity ≈ $75.94M**; debt = 100 − 75.94 = $24.06M; implied
debt rate = `(80/24.06)^(1/10) − 1 = 12.77%`. **Troubled case:** drop S to $50M
(firm owes more than it owns) → equity *still* worth **≈ $30.44M** (d1 = 1.0515,
d2 = −0.2135). **Varig case:** S = $1,099M, K = $1,391M face debt, t = 2.09y weighted
duration, σ = 32.44%, r = 15% → equity ≈ **$239M** even though face debt far exceeds
firm value. *Higher variance → higher equity value* (risk is the equity holder's
friend in distress).
Real-world input notes: estimate firm value and its variance by cumulating market
values of debt + equity (or FCFF/WACC on the assets); estimate firm-value variance via
`σ²_firm = w_e²σ_e² + w_d²σ_d² + 2·w_e·w_d·ρ_ed·σ_e·σ_d` (use similarly-rated bonds or
the industry average if not traded); for debt life use the face-value-weighted duration.
> source: eqnotes/distress.pdf p.46–62

### 3.6 The Bed Bath & Beyond (2022) input set — a clean declining-firm template
The chapter's anchor case translates the "acceptance/soft-landing" story into numbers:
- **Revenue:** −10% in year 1, then −5% per year for four years, returning to positive
  growth only in year 9 (negative-then-stabilize trajectory).
- **Operating margin:** converges to the **US retail average of 5.54%** (well below
  BB&B's double-digit heyday margins).
- **Reinvestment:** none (firm is shrinking); instead, **cash inflows from store
  shutdowns/divestitures** augment operating cash flow, available to return to
  shareholders or pay down debt.
- **Risk / leverage:** lease debt falls as stores close; as profitability returns the
  firm pays down debt to manageable levels — but rated **B1 (well below investment
  grade)**, so a **23.74% probability of failure** is applied.
- **Terminal state:** a *soft landing* — if it survives the decade, a smaller niche
  business with stable growth, earning ROIC near the mature-retail average.
- The pricing-table reality check (p.19): BB&B at the time had Market Cap $698M,
  EV $3,867M, EV/Sales 0.52 (peer median 0.97, average 1.26), with **−12.70% forward
  revenue growth and a −5.24% operating margin** vs. peers at +5.98% growth / 8.69%
  margin — i.e., it *looks* cheap on EV/Sales only because of its far worse
  fundamentals and distress risk.
> source: Ch13.pdf p.13, p.19 (read as image); tool BB&B2022.xlsx

## 4. Examples & cases

- **Bed Bath & Beyond (2022)** — the chapter's primary intrinsic-valuation case
  (acceptance / soft-landing story); demonstrates negative-then-recovering revenue,
  margin convergence to the retail average, divestiture cash inflows, a B1 rating →
  23.74% failure probability, and why a low EV/Sales multiple is a fundamentals/distress
  artifact, not a bargain. (Ch13.pdf p.12–14, p.19; tool BB&B2022.xlsx)
- **Global Crossing (Nov 2001)** — the eqnotes distress anchor: current revenue
  $3,804M, operating margin −49.82%, going-concern equity $3.22/share, B− rating /
  8% default spread, distress probability backed out of its bond (annual 13.53% →
  cumulative 76.63%), distress-sale equity = $0 → distress-adjusted value $0.75/share.
  Illustrates the full going-concern-plus-distress blend. (eqnotes/distress.pdf
  p.31–37, p.44)
- **Varig (Brazilian airline, 1999)** — equity-as-option case: EBIT −$134M, book equity
  $29M, $1,391M face debt (2.09y weighted duration) > firm value $1,099M, yet equity
  ≈ $239M via Black–Scholes. Shows insolvent-on-paper equity retaining option value.
  (eqnotes/distress.pdf p.60–62)
- **Yahoo (2015)** — "end-game" holding-company case (from the supplementary blog):
  ~$46B SOTP dominated by Alibaba (~$32B) and Yahoo Japan (~$8.4B) stakes, with the
  core operating business <10% of value; the prescription is *accept decline* — sell
  the operating business, return cash, run as a closed-end fund — rather than
  desperation bets ("Steve Jobs syndrome"). Live illustration of SOTP + management
  response. (blog §6.3)
- **Telecom distressed peer set (SAVVIS, Level 3, Williams Communications, RCN,
  Metromedia Fiber, etc.)** — used to show how to build and rating-adjust a
  comparable group when many sector firms are distressed at once. (eqnotes/distress.pdf
  p.41–42)
- **Enron, Kmart** — named as large-cap firms that *did* default, rebutting the claim
  that big exchange-listed firms can't fail. (eqnotes/distress.pdf p.24)
- **Automobiles, REITs/homebuilding, airlines (leases capitalized), 169 diversified
  firms** — Damodaran's "bad business" exemplars: sectors with persistent negative
  excess returns (ROIC < WACC) over 2005–2014. (blog §6.2)

> source: Ch13.pdf p.12–19; eqnotes/distress.pdf p.31–62; blogs §6.2–6.3

## 5. Data & tools

- **Book-value-multiples dataset (`pbvdata.xls`)** — Damodaran's by-industry dataset
  for ~100+ US sectors (Global variant `pbvdataGlobal.xls`). Columns: Industry name,
  Number of firms, **PBV** (market value of equity / book value of equity), **ROE**
  (return to equity investors), **EV/Invested Capital**, and **ROIC** (return to all
  capital providers). The tie to this chapter: PBV and EV/IC are the *liquidation-
  /book-anchored* multiples Damodaran warns against using naïvely for declining firms,
  and ROE vs. cost of equity / ROIC vs. cost of capital is the diagnostic for whether a
  business is "bad" (earning below its cost of capital). URL:
  `https://pages.stern.nyu.edu/~adamodar/pc/datasets/pbvdata.xls`. (Catalog only — raw
  data not copied; a 51.5KB `.xls` was fetched to confirm the column structure.)
- **Bed, Bath & Beyond valuation tool (`BB&B2022.xlsx`)** — the live declining-firm DCF
  model behind the chapter case: revenue decline schedule, margin convergence to the
  5.54% retail average, divestiture cash inflows in place of reinvestment, the going-
  concern DCF, the 23.74% failure-probability adjustment, and the distress-adjusted
  per-share value. URL:
  `https://pages.stern.nyu.edu/~adamodar/pc/blog/BB&B2022.xlsx`. (Catalog only.)
- **Companion distress papers (full text fetched locally):**
  `eqnotes/distress.pdf` ("Valuing Equity in Firms in Distress") and
  `papers/NewDistress.pdf` ("Valuing Distressed and Declining Companies") on
  `pages.stern.nyu.edu/~adamodar/` — the source of the probability-of-distress tables,
  the blend formula, and the equity-as-option machinery distilled above.

## 6. Supplementary readings — distilled

### 6.1 Reading — "Valuing Declining and Distressed Companies" (Damodaran, SSRN 1428022)
*The SSRN abstract page and PDF both returned HTTP 403; the Substack reproduction is a
preview only. Distilled instead from (a) the SSRN/Substack abstract, and (b) the
full-text companion paper `papers/NewDistress.pdf` ("Valuing Distressed and Declining
Companies"), which is the same author's treatment of the identical material and was read
in full.* The paper's thesis: the hardest firms to value sit at **both ends** of the
life cycle, and at the declining end the core problem is that **conventional, going-
concern DCF overstates value** because it ignores the probability of failure. It lays
out the five signs of decline (§2.1), argues that **divestitures create negative growth
and cash-flows-exceeding-earnings** that analysts must accept rather than smooth away,
and stresses that a divestiture is value-neutral except for the *price received vs.
value given up*. It then develops the distress correction: estimate a cumulative
probability of distress (ratings, bond prices, probit), blend the going-concern value
with a distress-sale value, and — for the most levered firms — treat **equity as an
option** whose value survives technical insolvency, noting that distressed-debt
renegotiations can re-cut the debt/equity-option/common-stock split "overnight." What it
adds beyond the slides: the *additivity argument for SOTP* in rigorous form, the warning
that distressed-firm betas computed from long historical windows are unreliable (and can
even fall during distress as the stock decouples from the market), and the explicit
statement that book values and earnings "can become meaningless" for these firms.
> source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1428022 (abstract; 403 on full PDF) + https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/NewDistress.pdf (full text) + https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/distress.pdf (full text)

### 6.2 Blog — "No Light at the End of the Tunnel: Investing in Bad Businesses" (Damodaran, May 2015)
*Read in full via WebFetch.* Defines a **bad business** by three conditions: most firms
in it earn ROIC below cost of capital, the underperformance is *persistent* across many
years, and there is *no delayed payoff* (unlike infrastructure that needs a long build
phase). Empirically (2005–2014) he flags automobiles, real estate (REITs, homebuilding,
building materials), wireless telecom, entertainment software, broadcasting, and
airlines (once leases are capitalized as debt) as bad businesses; 169 diversified firms
showed negative excess returns *every* year. The pivotal insight for valuation: in a bad
business **growth destroys value** — value is maximized by *minimizing reinvestment and
shrinking*, the opposite of management's instinct. He sorts corporate responses into
exit / retrench-and-return-cash / continue-unchanged (the most common and least
defensible) / aggressively transform, and the investor split into **passive** (must
price in value-destructive management) vs. **activist** (can force change; classic
targets are firms "in denial"). Closing lesson: *at the right price even a bad business
is investable; at the wrong price even a great one isn't* — and markets are quicker to
anoint disruption's winners than to reprice its losers. What it adds beyond the slides:
the rigorous *definition* of a bad business via persistent ROIC < WACC, the explicit
"growth destroys value" corollary, and the passive-vs-activist framing.
> source: https://aswathdamodaran.blogspot.com/2015/05/no-light-at-end-of-tunnel-investing-in.html

### 6.3 Blog — "The Yahoo Chronicles: Is this the end game?" (Damodaran, Dec 2015)
*Read in full via WebFetch.* A live "end-game" case for a declining tech firm. Yahoo —
having lost search to Google ("tech companies age in dog years"; a 20-year-old tech firm
is "geriatric") — was weighing selling its operating business and becoming a holding
company for its **Alibaba (~$32B) and Yahoo Japan (~$8.4B)** stakes. Damodaran's
**sum-of-the-parts** valued the whole at ~$46B, with the **core operating business worth
<10% of total value** (cash ~$5.9B, less ~$2.2B debt). The persistent ~28.9%
holding-company discount reflects tax/illiquidity drag on the cross-holdings. His
prescription is textbook **acceptance**: sell the operating business, return cash, run as
a closed-end fund — *not* a desperate, visionary acquisition gamble (the "Steve Jobs
syndrome" of CEOs chasing heroic status with shareholder capital). What it adds beyond
the slides: a concrete SOTP-with-cross-holdings worked case and a vivid illustration of
how **management response choice** (acceptance vs. desperation) drives end-game value.
> source: https://aswathdamodaran.blogspot.com/2015/12/the-yahoo-chronicles-is-this-end-game.html

### 6.4 Blog — "Myth 5.4: Negative Growth Rates Forever? Impossible!" (Damodaran, Nov 2016)
*Read in full via WebFetch. (Listed in `_sources.md` as "Negative growth rates forever?
Impossible!"; the actual title is "Myth 5.4: …".)* Attacks the analyst reflex that
terminal growth must be positive. Empirically negative growth is neither rare nor
unnatural (~40% of ~46,814 firms shrank in 2015; ~25% had a negative 2006–2015 revenue
CAGR; Oil/Gas 79.2%, Steel 73.2%, Publishing 53.8% negative in 2015). Perpetual growth
is *impossible* — the global market can't accommodate ever-expanding firms — so mature/
declining firms *should* carry negative terminal growth. The counter-intuitive payoff:
**shrinking can raise value when assets are worth more divested than retained.** The math
(distilled in §3.1): the reinvestment identity `g = Reinvestment Rate × ROIC` runs with a
negative reinvestment rate (−66.67% at g = −5%, ROIC = 7.5%); a −5% terminal growth gives
`TV = 100/(0.10 − (−0.05)) = $666.67M`, rising to ≈$1,111.33M once asset-liquidation
proceeds are credited. The governing rule: *if ROIC < cost of capital, negative growth
increases value.* What it adds beyond the slides: the empirical prevalence of negative
growth, the explicit liquidation-premium terminal-value math, and the formal statement
that negative reinvestment rates are legitimate, not modeling errors.
> source: https://aswathdamodaran.blogspot.com/2016/11/myth-54-negative-growth-rates-forever.html

## 7. Takeaways for valuation & modeling

For the copilot building standardized models of late-life-cycle Brazilian equities
(raw material for [[application_to_copilot]]):

1. **Flip the default trajectory for declining firms.** When a company is classified as
   declining (revenue flat/shrinking, margins compressing, ROIC < WACC), the engine's
   seed assumptions should *invert* the growth-firm template: negative revenue growth,
   operating margins converging *down* toward the sector average, **negative
   reinvestment** (divestiture cash inflows), and **cash flows that exceed earnings**.
   These are correct, not anomalies, and the assumption-proposal layer should explain
   them rather than flag them as errors. Tie terminal growth to the `g = Reinv × ROIC`
   identity so a negative reinvestment rate and a negative-but-bounded terminal g are
   internally consistent.

2. **Make the "management response" a first-class model input.** Add a
   denial / desperation / acceptance / reinvention selector (§2.6) that drives the
   whole forecast shape (growth path, margin path, reinvestment sign, risk profile) and
   forces an explicit, sourced story. Run a **3P test** (possible/plausible/probable) on
   any management turnaround narrative before letting it lift the numbers — this is the
   compliance-aligned guard against "fairy tale" valuations.

3. **Build a distress/failure-probability module and blend it in.** Estimate a
   cumulative probability of distress over the forecast horizon (from the company's
   rating, from its bond price via Solver, or from a probit) and apply the headline
   blend: `Equity value = going-concern DCF × (1 − P_distress) + distress-sale equity
   value × P_distress`. Estimate distress-sale value as a *fraction of book value or
   of going-concern value* — never the full DCF. This directly extends the project's
   Valuation tab and its debt-schedule-driven Kd: a rising D/E and a deteriorating
   rating must feed *both* the cost of debt *and* the distress probability.

4. **Treat liquidation value as a floor and a check, not book value.** For asset-heavy
   declining firms, compute a liquidation/SOTP value and compare it to the going-concern
   value; the higher of the two (net of forced-sale discounts and liquidation taxes)
   anchors the valuation. Never equate book value with liquidation value, and never read
   a low EV/Sales or P/B multiple as a bargain without controlling for growth, margins
   and distress (the BB&B EV/Sales trap, §3.6).

5. **Support sum-of-the-parts for divestiture-heavy and multi-business firms.** Because
   DCF is additive, let the engine value segments separately (own story, own risk/growth/
   cash-flow profile, own peer group), sum them, then **net out unallocated corporate
   costs** and the EV→equity bridge (cash, cross-holdings, debt, leases-as-debt per the
   project's IFRS 16 rule). This is the right machinery for end-game holding-company
   cases (Yahoo) and for pricing a part that is about to be sold/spun off.

6. **Carry an equity-as-option overlay for deeply distressed names.** When face value of
   debt exceeds firm value, a pure DCF can wrongly zero out equity. Add a Black–Scholes
   overlay (S = firm asset value, K = face value of debt, t = debt duration, σ = asset
   volatility) so the model recognizes equity's residual option value — and surface the
   *risk-helps-equity* and *debt–equity agency* implications, with a clear disclaimer
   that this is an analytical estimate, never a recommendation.

> source: synthesis of Ch13.pdf p.2–27 + eqnotes/distress.pdf + NewDistress.pdf + blogs §6.2–6.4

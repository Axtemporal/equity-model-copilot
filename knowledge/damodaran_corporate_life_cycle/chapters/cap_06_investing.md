---
chapter: 6
title: Investing across the Life Cycle (The Investment Decision)
block: Corporate Finance
slides: reference/damodaran_clc/pdf/Ch6.pdf
status: draft
---

# Ch 6 — Investing across the Life Cycle (The Investment Decision)

## 1. Core thesis

This chapter is the corporate-finance "investment decision" chapter of the
book: how a business decides *where to put scarce capital* and how that decision
shifts as the firm ages. Damodaran's spine is simple and unchanging — an
investment is good only if it earns more than its **hurdle rate** (the cost of
capital), i.e. it generates **excess returns** (ROIC > cost of capital, or
equivalently positive NPV / IRR above the hurdle). What *changes* across the
life cycle is not the rule but the *terrain*: the dominant decision tool, the
hardest input to estimate, the most common mistake, and the type of investment a
firm actually faces. Young firms live or die by the investment decision (it is
their whole story), face huge uncertainty about whether the business model even
works, and lean on growth/real-option arguments; mature firms have stabilized
returns and must guard against the opposite error — pouring capital into growth
that earns less than the cost of capital and therefore *destroys* value; declining
firms should be divesting and liquidating, not reinvesting. The chapter's
sobering empirical backdrop, threaded through the data slides and the 2024
profitability blog, is that **most firms globally do not clear their hurdle rate**
— roughly 80% earn returns below their cost of capital — so "grow at all costs"
is, on the evidence, more likely to destroy value than create it. This is the
investment-decision face of the life-cycle scaffold introduced in
[[cap_01_unifying_theory]] and built on the corporate-finance first principles of
[[cap_05_corpfin_101]].

> source: Ch6.pdf p.1–20 (slide deck, primary; text sparse — read as images);
> blog "Data Update 5 for 2024: Profitability"; paper costofcapital.pdf

## 2. Key concepts & frameworks

### 2.1 The investment process — what feeds the decision
The opening framework lays out the analyst's task: to decide whether to make an
investment, you forecast the project's expected earnings and cash flows and
discount them at the hurdle rate to see whether the business can at least break
even on a value basis. The inputs that feed that forecast come from several
buckets, each of which is also (not coincidentally) an input to one of the risk
measures later in the chapter: **past projects** (use the earnings history of
similar past investments), **industry norms** (profitability/returns of other
firms in the business), **market information** (consumer behaviour, market size),
**price data** (what the market pays / will pay), **debt history** (the cost of
borrowing), and **earnings variability** (use accounting-earnings volatility as a
risk proxy). The point is that the investment decision is an evidence-gathering
exercise, and the same evidence stream is reused to estimate the discount rate.
> source: Ch6.pdf p.2

### 2.2 The hurdle rate = the cost of capital
Damodaran maps the firm's balance sheet to make the hurdle rate concrete. On the
asset side sit **assets in place** (expected value of investments already made)
and **growth assets** (expected value added by future investments). On the
liability side sit **debt** (borrowed money) and **equity** (owners' funds). The
**cost of capital** is the blended cost of funding the *whole* business — a
weights-based average of the cost of debt and cost of equity — and it is the rate
new investments must beat. The cost of debt is the interest rate the firm would
pay on long-term borrowing today, adjusted for default risk; the cost of equity
is the rate of return equity investors require given the riskiness of the firm's
operations. This is the same number the companion paper calls the "Swiss Army
knife of finance" (see §6) — it is simultaneously a hurdle rate (investing), an
optimizing target (financing), a divining rod for cash return (dividends), and a
discount rate (valuation). Applies to every stage, but the *level* drifts down as
firms mature (see §3, age-decile table).
> source: Ch6.pdf p.3; costofcapital.pdf p.1–3

### 2.3 Cost of debt (pre- and post-tax)
Built from three pieces and a tax shield:
**After-tax cost of debt = (Risk-free rate + Default spread) × (1 − tax rate).**
The risk-free rate is the long-term government rate in the currency of analysis;
the default spread is what lenders charge to reflect the firm's *current* default
risk (use the company's standing today, not when it borrowed); the (1 − t) factor
captures the tax deductibility of interest. Two cautions carried from the cost-of-
capital paper: keep it **current** (today's risk-free rate and today's rating) and
**currency-consistent** (estimate the cost of debt in the currency of the cash
flows). Note the project tie-in flagged in the CLAUDE.md build backlog: the debt
schedule's weighted-average cost (tranches, indexers, spreads) should feed the
WACC by formula, never a typed standalone number.
> source: Ch6.pdf p.4; costofcapital.pdf p.24

### 2.4 Cost of equity
Damodaran's standard build: **Cost of equity = Risk-free rate + (Relative risk
measure × Equity risk premium).** The risk-free rate is the same long-term rate
used for debt; the relative risk measure is the asset's risk relative to the
average (a beta in the CAPM, but Damodaran is agnostic about the exact measure —
see §3.6); the equity risk premium is the price of equity risk in the markets the
firm operates in. The three inputs each get their own slide: risk-free rate
(2.5), default spreads (the bond-market price of risk), and the equity risk
premium (the equity-market price of risk).
> source: Ch6.pdf p.5

### 2.5 Inputs — risk-free rate, default spreads, ERP, by country
Three data slides drive home that the price-of-risk inputs are observable,
time-varying, and geography-dependent:
- **Risk-free rate** varies by *currency*, driven almost entirely by expected
  inflation; estimate it as a default-free long-term government rate, or net the
  sovereign default spread out of a risky government bond rate. (Figure: risk-free
  rates by currency, July 2022.)
- **Default spreads** (the price of risk in the *bond* market) by rating, and how
  they move over time (2015–2022 chart) — a warning against frozen costs of
  capital.
- **Equity risk premium** (the price of risk in the *equity* market): the
  *implied* ERP backed out of current index level and expected cash flows is
  preferred to a backward-looking historical premium. (Figure: implied ERP time
  series; July 1, 2022 implied ERP ≈ 6.01% over the risk-free rate.)
- **ERP by country** (July 2022 world map): a company's ERP should reflect *where
  it does business*, not merely where it is incorporated — relevant for Brazilian
  pilots whose revenue mix may straddle currencies/countries.
> source: Ch6.pdf p.6–9

### 2.6 Relative risk (beta) and its life-cycle drivers
The beta slide decomposes relative equity risk into three drivers, and — unusually
for a CAPM discussion — annotates each with *life-cycle implications*:
- **Business risk (nature of product/service):** the more discretionary the
  product, the higher the beta. *Life-cycle note:* young firms tend to be riskier
  here because their product and market are unproven; risk falls as the business
  matures and demand stabilizes.
- **Operating leverage (fixed-cost structure):** the greater the proportion of
  fixed costs, the higher the beta, because earnings swing more for a given
  revenue swing. *Life-cycle note:* young firms often carry higher fixed costs
  (relative to revenue) and so higher operating leverage; this should ease with
  scale.
- **Financial leverage (debt):** more debt magnifies business risk into equity
  risk, raising the levered beta. *Life-cycle note:* young firms borrow little, so
  this driver is small early and grows as firms mature and lever up (consistent
  with the financing-decision rotation in [[cap_07_financing]]).
The takeaway: a firm's beta is not a fixed trait — it should *decline* over the
life cycle as the business de-risks, and a forecast should let it drift toward 1.
> source: Ch6.pdf p.10

### 2.7 Investment decision rule #1 — accounting returns (ROIC / ROE)
The first decision rule compares an *accounting* return to the hurdle rate.
- **Return on invested capital (ROIC):** after-tax operating income ÷ invested
  capital, compared to the **cost of capital**. Invested capital = book value of
  equity + book value of debt − cash & marketable securities (capital actually
  tied up in operations).
- **Return on equity (ROE):** net income ÷ book value of equity, compared to the
  **cost of equity**.
A firm creates value when ROIC > cost of capital (or ROE > cost of equity); the
*spread* is the excess return / economic profit. The slide explicitly walks the
balance-sheet mapping: operating assets generate the operating income for ROIC;
cash & marketable securities are stripped out; cumulated retained earnings sit in
book equity for ROE. This is the chapter's bridge to the EVA / excess-return data
(see §3.2 and §5) and to the supplementary ROIC paper (§6).
> source: Ch6.pdf p.14

### 2.8 Investment decision rule #2 — discounted cash flow (NPV / IRR)
The cash-flow rules:
- **Net present value (NPV):** sum of the present values of a project's expected
  cash flows over its life, discounted at the hurdle rate. NPV > 0 → the project
  earns more than its hurdle rate → accept; NPV < 0 → reject. NPV is an *absolute*
  (currency) value.
- **Internal rate of return (IRR):** the discount rate that sets the project's
  aggregate PV of cash flows to zero. IRR > hurdle rate → accept. IRR is a
  *percentage* value.
The slide also catalogs the classic NPV-vs-IRR frictions (see §3.4): absolute vs
percentage bias, multiple IRRs when cash-flow signs flip more than once, and the
reinvestment-rate assumption (NPV reinvests intermediate flows at the hurdle rate,
IRR at the project's own IRR). Damodaran's lean is toward NPV.
> source: Ch6.pdf p.16–17; Ch6.txt p.16–17

### 2.9 Investment decision rule #3 — real options
The third rule recognizes that static NPV/ROIC can *undervalue* projects that
carry embedded flexibility — chiefly the **option to expand**. The expansion
payoff diagram is a call option: if the PV of expected cash flows from future
expansion stays below the cost of expansion, you do not expand and lose only the
initial outlay; if it exceeds the cost, you expand and capture the upside. So a
project with negative stand-alone NPV can still be worth taking if it buys a
valuable option to enter a large, uncertain market later. Damodaran's caution
(echoed across the chapter): real options are *notoriously hard to value*
(underlying asset not traded, long-dated, early exercise common), and the
argument is easily abused to justify investments that fail financial muster. Even
without a precise value, the logic tells you *when* the option is most valuable —
big target market, high uncertainty about its size and your ability to enter —
which is exactly the situation of **young firms entering large markets**, so the
real-options rule maps most naturally to the early life cycle.
> source: Ch6.pdf p.18–19; Ch6.txt p.19; realopt.pdf (full paper, §6)

### 2.10 The empirical reality — most firms don't clear the hurdle
A recurring, deliberately uncomfortable theme: when Damodaran computes ROIC vs
cost of capital across the global universe, **more than half (and in the 2024
update, ~80%) of firms earn returns below their cost of capital.** Growth, in
aggregate, is more likely to destroy value than create it. This reframes the
investment decision as primarily a *discipline against over-investment*, not a
hunt for projects to fund — especially important for mature and declining firms
(see the "Decline and Denial" case, §4 and §6).
> source: Ch6.pdf p.11–13; costofcapital.pdf p.5–6; blog "Data Update 5 for 2024"

## 3. Metrics, formulas & rules of thumb

### 3.1 Cost of capital (the hurdle rate)
```
Cost of capital = Cost of equity × E/(D+E)  +  After-tax cost of debt × D/(D+E)
Cost of equity      = Rf + (Relative risk measure × ERP)        [CAPM: relative risk = β]
After-tax cost of debt = (Rf + Default spread) × (1 − marginal tax rate)
```
- Use **market-value** weights for D and E (book weights break down — ~10% of US
  firms have negative book equity).
- Use a **long-term** Rf in the **currency of the cash flows**; differences in Rf
  across currencies are mostly expected-inflation differences and wash out if
  cash-flow inflation is matched.
- Keep the cost of debt **current** (today's rating, today's Rf), not the historical
  book interest rate.
- **Marginal**, not effective, tax rate for the shield — and only if the firm is
  actually making money (no shield while in operating losses).
- The cost of capital is a **dynamic** number: it should fall over a young firm's
  forecast as it matures (see age-decile table 3.7).

### 3.2 Excess return / economic profit / EVA
```
Excess return (spread)      = ROIC − Cost of capital
Economic profit / EVA       = (ROIC − Cost of capital) × Invested capital
Equity excess return        = ROE  − Cost of equity
```
Value is created only when the spread is positive. **Growth multiplies value when
the spread is positive and destroys value when it is negative.** This is the
single most load-bearing idea in the chapter for valuation.

### 3.3 Accounting returns
```
ROIC = After-tax operating income / Invested capital
       After-tax operating income = EBIT × (1 − tax rate)  [NOPAT]
       Invested capital = BV equity + BV debt − Cash & marketable securities
ROE  = Net income / Book value of equity
```
Measurement adjustments (from the ROIC paper, §6): capitalize R&D and operating
leases (move them into invested capital and operating income), strip one-time
charges out of operating income, net out cash, and use beginning-of-period or
average book value consistently. Unadjusted accounting returns are noisy and can
mislead — tech ROICs look inflated mainly because R&D is expensed not capitalized.

### 3.4 NPV vs IRR
```
NPV = Σ [ E(CFt) / (1 + hurdle rate)^t ]  − Initial investment      → accept if NPV > 0
IRR = the rate r such that Σ [ E(CFt) / (1 + r)^t ] = 0             → accept if IRR > hurdle
```
| Dimension | NPV | IRR |
|---|---|---|
| Output type | Absolute (currency) — biases toward big-capital projects | Percentage — biases toward small-capital projects |
| Uniqueness | One value per project | Multiple IRRs possible if cash-flow signs flip >1× |
| Reinvestment of interim cash | At the hurdle rate (realistic) | At the project's own IRR (optimistic) |
Damodaran prefers NPV; the reinvestment assumption is the deciding flaw of IRR.

### 3.5 Real-option logic (the option to expand)
A negative-NPV project can be worth taking if it embeds a valuable option:
```
Value with option = Static NPV (often < 0) + Value of the embedded real option
```
The expansion option is a **call**: underlying = PV of cash flows from future
expansion (S); strike = cost of expansion (K); life = window in which the option
can be exercised; volatility = uncertainty about the expansion's value. Value
rises with market size and with uncertainty. Three "is this option real?" tests
(from realopt.pdf, §6): (1) is the first investment a prerequisite for the second?
(2) does it confer an exclusive/competitive right? (3) is the competitive
advantage sustainable? Only excess-return-generating, sustainable advantages give
the option value.

### 3.6 Relative-risk alternatives (when you dislike beta)
From the cost-of-capital paper: if you reject the diversified-marginal-investor
assumption or price-based betas, substitutes include the **total beta**
(σ_stock / σ_market) and **relative standard deviation** (σ_stock / avg σ across
stocks) for undiversified owners (private firms), **accounting/earnings betas**,
**accounting-ratio** risk proxies (e.g. debt/EBITDA), or **sector-average betas**
to kill single-regression noise. Total beta is the practical tool for valuing
private businesses — directly relevant if a pilot is closely held.

### 3.7 Cost of capital and accounting returns by age decile (rules of thumb)
The chapter's own data slides give the life-cycle gradient (US, July 2022):

| | Youngest decile | Top (oldest) decile |
|---|---|---|
| Avg age (yrs) | ~5 | ~140 |
| Cost of capital (median) | ~9.3% | ~7.0% |
| Cost of capital range (low/high quartile) | ~8.7% / ~9.6% | ~6.7% / ~8.9% |
| ROIC (median) | deeply **negative** (≈ −75% to −58% in youngest deciles) | positive (≈ low-to-mid single digits / ~5% median) |
| % of firms with negative returns | very high (~47% capital, ~74% equity in youngest) | much lower (~23% capital, ~8.6% equity in oldest) |

Rules of thumb: **cost of capital falls with age** (young ≈ 9–9.6%, market median
≈ 8%, old ≈ 7%); **ROIC rises from deeply negative to modestly positive with
age**; even at the oldest deciles the *median* spread (ROIC − cost of capital) is
thin or negative — value creation is hard at every age. The full-market cost-of-
capital distribution is tight: ~80% of US firms between ~5.2% and ~10%, median
~8% — so (per costofcapital.pdf Lesson 1) errors in *cash flows* matter far more
than errors in the discount rate.
> source: Ch6.pdf p.7–9, p.11–15; costofcapital.pdf p.27

## 4. Examples & cases

- **Young firm entering a large market (real-options archetype):** the canonical
  use of the option-to-expand rule — accept a negative-NPV beachhead because it
  buys the option to enter a big, uncertain market. The chapter ties this to why
  growth/real-option arguments cluster in the early life cycle. (Ch6.pdf p.19)
- **BlackBerry — denial in decline:** a declining firm whose management kept
  acting like a growth/mature company; the eventual go-private signals *acceptance*
  of decline (orderly wind-down) rather than value-destroying reinvestment.
  (blog "Decline and Denial", §6)
- **Microsoft as a "value trap" (2013 framing):** looked cheap on multiples, but
  decades of R&D on failed ventures implied continued growth spending below the
  cost of capital — cheap is a trap if the firm keeps reinvesting at a negative
  spread. (blog "Decline and Denial", §6)
- **COVID through the life-cycle lens:** young/high-growth firms gained value
  (risk capital returned), capital-intensive mature sectors — energy, utilities,
  financials — suffered; explains growth's outperformance over value in 2020.
  (blog "A Viral Market Update X", §6)
- **Real-option worked examples (from the paper):** Avonex/Biogen patent valued as
  a call (option value ≈ $907m vs static NPV ≈ $547m); gold-mine and offshore-oil-
  reserve options (positive option value despite negative static NPV); Home Depot
  France store (option to expand turns −20m FF into +17.9m FF); Eurotunnel equity
  valued as a deep-out-of-the-money call on the firm. (realopt.pdf, §6)

> source: Ch6.pdf p.18–20; realopt.pdf; blogs (§6)

## 5. Data & tools

Catalog only — raw `.xls` data is **not** copied into the repo (per `_sources.md`).
All under `https://pages.stern.nyu.edu/~adamodar/`.

- **Cost of capital by industry** — US `.../wacc.xls`, Global `.../waccGlobal.xls`.
  Industry-average costs of capital; useful as a sanity anchor for a pilot's WACC.
- **Return on capital by industry** — US `.../mgnroc.xls`, Global
  `.../mgnrocGlobal.xls`. Margins and ROIC by industry.
- **Excess returns by industry** — US `.../EVA.xls`, Global `.../EVAGlobal.xls`.
  ROIC − cost of capital (economic profit) by industry — the direct value-creation
  read.
- **Tools (under `.../pc/`):**
  - `wacccalculator.xlsx` — builds a cost of capital from Rf, ERP, beta, default
    spread, tax rate, and D/E weights.
  - `returncalculator.xls` — computes ROIC/ROE with the standard accounting
    adjustments (R&D, leases, cash).
  - `expand.xls` — values the option to expand (real-option calculator).

## 6. Supplementary readings — distilled

### 6.1 Paper (full text, local) — "The Promise and Peril of Real Options" (realopt.pdf)
*Read in full from the local PDF.* A long, applied treatment of real options in
corporate finance. It first reviews option basics (call/put payoffs, the six
determinants of option value, binomial and Black-Scholes models) and the *caveats*
that make real options harder than listed options: the underlying asset is not
traded (no clean replicating portfolio), price paths aren't continuous, variance
isn't constant or known, and exercise isn't instantaneous. It then values three
project options — the **option to delay** (a patent or undeveloped reserve as a
call; e.g. Biogen's Avonex patent worth ~$907m as an option vs ~$547m static NPV;
gold-mine and oil-reserve illustrations), the **option to expand** (Home Depot
France: a −20m FF store justified by a +37.9m FF expansion option), and the
**option to abandon** (a put). It extends to **equity as a call option** on a
levered firm (Eurotunnel: equity worth ~£122m despite deeply negative book equity)
and to financing applications (bondholder–stockholder conflict, security design,
the value of financial flexibility). The disciplining contribution: three tests
for whether an option is real and valuable — (1) is the first investment a
prerequisite for the second, (2) does it confer an exclusive/competitive right,
(3) is the advantage sustainable — because value comes only from *sustainable
excess returns*, not from cash flows per se. **Adds beyond the slides:** the full
valuation machinery and the rigor needed to stop "real options" from becoming a
rhetorical excuse for negative-NPV investments — exactly the abuse the chapter
warns about.
> source: reference/damodaran_clc/text/realopt.txt (full)

### 6.2 Paper (full text, local) — "The Cost of Capital: The Swiss Army Knife of Finance" (costofcapital.pdf)
*Read in full from the local PDF.* The definitive companion to the hurdle-rate
slides. The cost of capital is one number used in four roles: hurdle rate
(investing), optimizer (capital structure — the mix that minimizes it maximizes
value), divining rod (dividends — return cash if no project beats it), and
discount rate (valuation). Mechanics: weighted average of cost of equity and
after-tax cost of debt at **market-value** weights. Inputs covered in depth —
**risk-free rate** (long-term, currency-specific, inflation-driven; don't
normalize), **equity risk premium** (prefer the implied/forward ERP to historical;
estimate by *where a company does business*; rule of thumb: ERP ≈ 2× the Baa
default spread), **default spreads** (current rating, currency-consistent),
**relative risk** (beta and its many substitutes — total beta, relative σ,
accounting/sector betas — for when you distrust beta), and **debt weight/cost**
(market not book; marginal tax rate; tax shield only if profitable; dynamic
weights that rise as a firm matures). Four lessons close it: (1) cash-flow errors
dwarf discount-rate errors — the cross-firm cost-of-capital spread is small
(~80% of US firms between 5.2% and 10%, median ~8%); (2) the cost of capital is
not a receptacle for fears (use probabilities/decision trees for discrete risks
like FDA failure); (3) widespread ≠ justified (the small-cap premium has been
"missing in action" since 1981); (4) watch for agenda-driven discount rates.
**Adds beyond the slides:** the estimation craft and the explicit warning that
discount-rate fiddling is where bias enters valuations.
> source: reference/damodaran_clc/text/costofcapital.txt (full)

### 6.3 Blog — "A Viral Market Update X: A Corporate Life Cycle Perspective" (Jun 2020)
*Read in full via WebFetch.* Damodaran reads the COVID market shock through the
life cycle: after an initial freeze, risk capital returned and **young/high-growth
firms gained value**, while **capital-intensive mature sectors** (energy,
utilities, financials) suffered lasting damage — the highest-revenue-growth firms
rose, the lowest fell. This explains why growth investing beat value in 2020, but
he cautions that the recovery was atypical, so naïvely extrapolating either the
crash or the rebound is dangerous. **Adds beyond the slides:** a real-time demo
that the *same shock* hits different life-cycle stages in opposite directions,
which is precisely why the investment decision (and risk) must be stage-aware.
> source: https://aswathdamodaran.blogspot.com/2020/06/a-viral-market-update-x-corporate-life.html

### 6.4 Blog — "Earnings and Cash Flows: A Primer on Free Cash Flow" (Oct 2022)
*Read in full via WebFetch (correct URL has hyphens:
.../2022/10/earnings-and-cash-flows-primer-on-free.html).* Damodaran warns that
"free cash flow" is one of finance's most abused terms because definitions vary.
Two clean measures:
```
FCFF = EBIT × (1 − t) − Reinvestment              [pre-debt; serves all capital providers]
FCFE = Net income + non-cash items − Reinvestment + Net debt issuances   [equity only]
Reinvestment = (Capex + acquisitions) − D&A + ΔNon-cash working capital
```
He stresses **not** adding back stock-based compensation (it is genuine
dilution). FCF has three uses: explain the past, forecast (after normalizing
extraordinary items) for intrinsic valuation, and underpin pricing multiples.
**Life-cycle pattern:** young firms typically show **negative FCFE** (heavy
reinvestment + thin/negative profits), mature firms generate **large positive
FCFE**, and declining firms can show **elevated FCFE** from asset sales — which is
exactly why dividend/buyback capacity tracks FCFE across the cycle. **Adds beyond
the slides:** the earnings→cash-flow bridge that turns the chapter's return
metrics into the cash flows the Valuation tab discounts; connects to
[[cap_09_valuation_101]] and the cash-return logic of [[cap_08_cash_return]].
> source: https://aswathdamodaran.blogspot.com/2022/10/earnings-and-cash-flows-primer-on-free.html

### 6.5 Blog — "Decline and Denial: Blackberry End game and Microsoft as a Value Trap" (Sep 2013)
*Read in full via WebFetch (correct URL: .../2013/09/decline-and-denial-requiem-for.html).*
Businesses age like people; mature and declining firms must eventually *accept*
decline rather than chase value-destructive growth. Management typically cycles
through anger → denial (expensive turnarounds) → acceptance. **"Growth can be
value-destructive if it is expensive"**: a cheap-looking mature firm becomes a
*value trap* when it keeps reinvesting at returns below the cost of capital
(Microsoft's history of R&D on failed ventures is the cautionary case; BlackBerry's
go-private signals acceptance/orderly wind-down). The investing lesson: declining
firms create value by **returning cash and managing assets efficiently**, not by
reinvesting at a negative spread. **Adds beyond the slides:** the behavioural
/managerial half of the over-investment problem — why the empirically common
failure to clear the hurdle persists, and how it manifests as a value trap.
> source: https://aswathdamodaran.blogspot.com/2013/09/decline-and-denial-requiem-for.html

### 6.6 Blog — "Data Update 5 for 2024: Profitability" (Jan 2024)
*Read in full via WebFetch (.../2024/01/data-update-5-for-2024-profitability.html).*
Profitability is measured by margins (gross/operating/net/EBITDA, chosen by
life-cycle stage) and by **ROIC vs cost of capital**. The headline: **~80% of
global firms earned returns below their cost of capital in 2023** — "there is not
a single sector or region where a majority of firms earn more than their hurdle
rates" — i.e. widespread value destruction. Tech shows the highest accounting
ROIC (inflated by expensing rather than capitalizing R&D); financials make the
largest absolute profits; US firms outperform Chinese/SE-Asian peers. **Adds
beyond the slides:** the up-to-date, quantified backbone for the chapter's
"growth usually destroys value" thesis and the case for treating the investment
decision as a discipline against over-investment.
> source: https://aswathdamodaran.blogspot.com/2024/01/data-update-5-for-2024-profitability.html

### 6.7 Reading — Morgan Stanley / Counterpoint Global, "ROIC and the Investment Process" (Mauboussin & Callahan)
*Read via WebFetch of the Marcellus mirror; the primary morganstanley.com PDF
returned HTTP 403.* ROIC = NOPAT ÷ invested capital; value is created only when
ROIC > cost of capital (a dollar invested becomes worth more than a dollar). ROIC
decomposes into **invested-capital turnover** (sales/capital) × **NOPAT margin**
(profit/sales), mapping to cost-leadership vs differentiation strategies; firms
with durable superior returns tend to win on margin (differentiation). On
persistence: market-wide ROICs mean-revert toward the cost of capital
(competition), but some sectors show strong persistence from moats. Crucially,
**changes in ROIC, not the absolute level, drive shareholder returns** — bottom-to-
top-quintile movers earned ~33% TSR, top-to-bottom ~−11% — because markets already
price current quality and reward *improvement*. **Adds beyond the slides:** the
turnover×margin decomposition, the empirical fade/persistence evidence, and the
investing edge in spotting improving ROIC.
> source: https://marcellus.in/story/roic-and-the-investment-process/ (mirror;
> primary https://www.morganstanley.com/im/publication/insights/articles/article_roicandtheinvestmentprocess.pdf — 403)

### 6.8 Reading — HBR, "Making Real Options Really Work" (van Putten & MacMillan, Dec 2004)
*Abstract/intro only — the full HBR article is paywalled (timed out / partial
fetch); distilled from the accessible introduction and corroborating sources.*
Real options struggle to catch on because CFOs fear they over-value risky projects
and encourage over-investment — but firms relying on DCF *alone* under-value
projects and under-invest in promising but uncertain ones. The fix is **not to
choose** between DCF and real options: a project's value should combine a DCF base
case with the option value of the upside. The article's distinctive critique: as
usually applied, real options price only the **revenue** uncertainty and ignore
**cost** uncertainty — a discipline that, once added, keeps the method honest.
**Adds beyond the slides:** a managerial recipe for integrating (not substituting)
real options into capital budgeting, reinforcing Damodaran's "value it, don't just
assert it" stance.
> source: https://hbr.org/2004/12/making-real-options-really-work (paywalled; intro + corroborating summaries)

### 6.9 Reading — Damodaran, "Return on Capital (ROC), ROIC and ROE: Measurement and Implications" (SSRN 1105499)
*Read in full from the Damodaran-hosted PDF (the SSRN abstract page returned 403).*
The methods paper behind the accounting-return slide. ROIC = after-tax operating
income (NOPAT) ÷ invested capital, where invested capital = BV equity + BV debt −
cash; ROE = net income ÷ BV equity. Core measurement issues: treat **operating
leases as debt**, **capitalize R&D** (move it into invested capital and operating
income), **strip one-time/unusual charges**, **net out cash**, and use **consistent
book-value timing**. The conceptual payoff is the **excess return = ROIC − cost of
capital**: when positive, expansion creates value; when negative, growth destroys
value *despite* rising revenues and earnings — so sustainable competitive
advantage, not speed of growth, is the value driver. **Adds beyond the slides:**
the precise adjustments needed to make accounting ROIC/ROE economically meaningful
— directly usable in the copilot's returns calculations.
> source: https://ssrn.com/abstract=1105499 (abstract 403; full text via
> pages.stern.nyu.edu/~adamodar/ returnmeasures.pdf)

## 7. Takeaways for valuation & modeling

For an equity analyst building standardized models, Chapter 6 yields these
actionable principles (raw material for [[application_to_copilot]]):

1. **Make ROIC − cost of capital the headline value test in the model.** Compute
   ROIC = NOPAT / invested capital (invested capital = BV equity + BV debt − cash)
   and compare it to the WACC every period. The *spread* — not growth, not margin
   in isolation — is what tells the model whether projected reinvestment creates or
   destroys value. Surface it explicitly in the Valuation tab as economic profit /
   EVA.

2. **Treat the hurdle rate as a built-up, dynamic, sourced number — never a typed
   constant.** Cost of equity = Rf + β×ERP; after-tax cost of debt =
   (Rf + default spread)×(1 − marginal t); WACC at market-value weights. Per the
   build backlog, wire Kd from the debt schedule's weighted-average cost. Let the
   WACC *drift down* and beta *toward 1* as a young pilot matures (age-decile
   gradient: young ≈ 9–9.6% → mature ≈ 7–8%).

3. **Don't over-engineer the discount rate; spend the effort on cash flows.** The
   cross-firm cost-of-capital spread is narrow (~5–10%, median ~8%); the big
   valuation errors come from revenue, margin, and reinvestment forecasts. Keep
   discrete risks (project failure, distress) out of the discount rate — handle
   them with scenarios/probabilities (ties to the bull/base/bear scenario design).

4. **Bake in the "growth ≠ value" discipline.** Default the model to *flag*
   negative-spread growth: if projected ROIC < WACC, more capex/reinvestment lowers
   value. For mature/declining pilots, the value lever is cash return and asset
   efficiency, not reinvestment — guard against the "value trap" pattern.

5. **Use NPV-style logic, and reserve real options for genuine, sustainable
   optionality.** Prefer NPV over IRR (reinvestment assumption). Where a young-firm
   pilot has a real option to expand into a large, uncertain market, value it
   separately and add it — but apply the three tests (prerequisite? exclusive
   right? sustainable advantage?) and never let a real-option narrative paper over
   a negative-NPV core. Account for *cost* uncertainty too, not just revenue.

6. **Apply accounting adjustments before trusting reported returns.** Capitalize
   R&D and operating leases, strip one-time charges, net out cash, and use
   consistent book-value timing — otherwise ROIC is noisy and cross-company
   comparisons (e.g. coverage-consistency checks across same-sector pilots)
   mislead. For closely held pilots, consider total beta for the cost of equity.

> source: synthesis of Ch6.pdf p.2–20 + realopt.pdf + costofcapital.pdf + SSRN
> 1105499 + Morgan Stanley ROIC + blogs (§6)

---
chapter: 11
title: Valuing High Growth Businesses
block: Valuation
slides: reference/damodaran_clc/pdf/Ch11.pdf
status: draft
---

# Ch 11 — Valuing High Growth Businesses

## 1. Core thesis

High-growth businesses are firms that have cleared the start-up and product-test
gates of [[cap_10_valuing_young]] — they have real, scaling revenues and
often the beginnings of profitability — but whose value still rests
overwhelmingly on a *future* that has not yet arrived. The central argument of
the chapter is that valuing these firms is an exercise in **disciplined
narrative under a binding arithmetic constraint**: you can tell an optimistic
story about scalability, margins, and reinvestment, but every piece of that
story must be forced through a consistent, time-varying valuation engine so the
pieces do not contradict one another. Three things must be made to *converge to
maturity over the forecast horizon*: revenue growth must fade as the firm gets
bigger (scale and competition guarantee it), operating margins must climb from
depressed or negative levels toward a sustainable mature level, and the cost of
capital (and the risk it encodes) must drift down from growth-firm highs toward
the sector's mature average. Reinvestment is the price paid for the growth and
must be sized to it via a sales-to-capital ratio. Because cash flows are low or
negative early and large late, the **terminal value dominates** — often 80–100%+
of total value — which is a feature of the firm's life-cycle position, not a flaw
in DCF. The chapter's recurring cautionary theme is the **big market delusion**:
when a market is advertised as enormous, entrepreneurs and investors collectively
assign market shares that sum to far more than 100%, and the whole cohort of
firms gets overpriced together until the inevitable correction. The running case
is Damodaran's valuation of **Tesla in November 2021**, with **Airbnb (Dec 2020)**
as the supplementary tool. This note sits between young-firm valuation
[[cap_10_valuing_young]] and mature-firm valuation
[[cap_12_valuing_mature]] in the life-cycle arc [[00_framework_lifecycle]].

> source: Ch11.pdf p.1–13, p.21 (Tesla valuation); synthesis

## 2. Key concepts & frameworks

### 2.1 The high-growth phase on the life-cycle curve
The opening diagram places the high-growth phase on the standard
revenue/earnings curve: revenues are still rising steeply, earnings are crossing
from negative into positive, and free cash flow to the firm (FCFF) is still
depressed because reinvestment is heavy. The slide arrays the stages —
idea/start-up/young/high-growth companies — and marks the high-growth firm as one
that is "growing rapidly," "becoming profitable," and "scaling up the business,"
with FCFF lagging both revenues and earnings. The visual point is that a
high-growth firm lives in the steep, ambiguous middle of the curve where small
changes in assumptions swing value dramatically.
> source: Ch11.pdf p.2 (diagram, read as image)

### 2.2 What changes versus valuing a young/start-up firm
Relative to a true start-up, a high-growth firm has **more financial history and
a corporate-governance structure** to lean on. The narrative still centers on
*potential*, but more weight now goes to the actual track record — which can cut
both ways: a strong record (real revenue growth and emerging profitability) lets
you raise your story, while a weak one forces you to **scale the story back**.
The story for a high-growth firm specifically concerns the **business model**
and how it plays out along three axes: **scalability (growth), profitability
(margins), and reinvestment (growth efficiency)**.
> source: Ch11.pdf p.5

### 2.3 The three estimation battlegrounds and their biases
Damodaran isolates where the hard, bias-prone judgments live:
- **Revenues / scaling.** The biggest questions arise here because you are
  assuming revenues can be scaled up. Discipline it by checking **market size**
  and the **implied market share** your growth assumptions require, against
  **potential competition**. (This is the hook into the big-market-delusion
  warning in §2.9.)
- **Operating margins.** Positive profit trend lines breed over-optimism about
  the steady-state margin; temper it with **unit economics** rather than
  extrapolation.
- **Reinvestment / growth efficiency.** The hardest to pin down, because
  historical reinvestment is volatile and is **obscured by stock-funded
  acquisitions and investments**. Look to **industry averages** and the
  **business model** for clues rather than trusting noisy historicals.
> source: Ch11.pdf p.5–6

### 2.4 Revenue growth must fade as the firm scales
A growth firm, if the forecasts come true, gets larger — and growth rates *fall*
mechanically as the base grows. Three tools discipline the fade:
1. **Look at absolute revenue changes, not just percentages.** A constant 40%
   growth rate on a much larger base implies an absolute dollar increase that may
   be implausibly large; checking the dollar change is a sanity test.
2. **Trend lines.** Examine the firm's own past year-by-year growth rates to see
   how growth decayed as the company's size rose.
3. **Sector data.** Anchor the long-run rate on the revenue growth of **more
   mature firms in the same business** — that is roughly where this firm is
   heading. (Ties to the by-industry growth datasets in
   [[cap_03_measures_determinants]].)
> source: Ch11.pdf p.7

### 2.5 Margin convergence to a sustainable level
The most common starting point is a **current margin that is negative or too low**
relative to the sustainable long-run margin, for three structural reasons:
1. **Up-front fixed costs** incurred early, with the revenue/growth payoff
   arriving later.
2. **Growth expenses mingled with operating expenses** — money spent to *generate*
   future growth is booked as if it were the cost of *running* the current
   business; as the firm matures this contamination shrinks and reported margins
   rise.
3. **A lag between expenses and the revenues they create.**
The less common case is a **current margin that is too high** and will fall — most
likely for a firm with a **niche product in a small market**; as it grows beyond
the niche, competition compresses the margin. Either way, the modeling task is to
project a *path* from today's margin to a defensible steady-state margin, not to
freeze the current margin.
> source: Ch11.pdf p.8

### 2.6 Reinvestment sized by the sales-to-capital ratio
Because margins (and therefore earnings-based reinvestment metrics) are moving,
Damodaran reuses the young-firm road map: tie reinvestment to **revenue change**
through a **sales-to-capital ratio** rather than to noisy capex/working-capital
figures.

`Reinvestment_t = (Change in Revenues_t) / (Sales-to-Capital ratio)`

The sales-to-capital ratio is estimated from the **company's own data** (more
stable than year-to-year net capex or working-capital swings) blended with
**sector averages**. A **lag** between spending and the revenue it produces can be
modeled by using a *future* period's revenue change to size the *current*
period's reinvestment.
> source: Ch11.pdf p.9

### 2.7 Risk and cost of capital evolve year by year
The key to keeping a growth valuation internally consistent is to **let the
discount rate move over time** in step with the growth and margin path. A growth
firm should carry **high costs of equity and debt while revenue growth is at its
peak**, and those costs should **decline as growth moderates and margins
improve**. As earnings rise and growth falls, the firm flips from cash-consuming
to cash-generating, gaining the capacity to pay dividends and service debt — which
in turn justifies a higher debt ratio and a lower cost of capital. The
prescription: the cost of capital should be a **year-specific number** that keeps
pace with every other forecast change, not a single static rate applied to the
whole horizon. This is the mechanical embodiment of the life-cycle idea that risk
falls as a firm ages, picked up again in [[cap_12_valuing_mature]].
> source: Ch11.pdf p.10

### 2.8 Putting the firm into stable growth (the terminal transition)
Two rules govern the move to the terminal phase:
- **Do not wait too long.** Scale and competition lower growth quickly even at the
  best companies; growth periods longer than **ten years** — especially at high
  rates — are rare, achieved by only a handful of firms historically.
- **Give the firm the characteristics of a stable-growth firm** once it gets
  there: lower costs of debt and equity, a higher debt ratio, and — critically —
  a chosen **return on capital** for the stable phase. Some analysts set
  stable-phase ROC equal to the cost of capital (implying no excess returns, i.e.
  no value added by growth); Damodaran prefers to **preserve some company-specific
  flexibility** so a firm with a durable moat can still earn above its cost of
  capital in perpetuity.
> source: Ch11.pdf p.11

### 2.9 Terminal value dominance is normal, not a DCF flaw
Because growth-firm cash flows are low/negative early and high late, the
**terminal value is a very high proportion of total value — 80%, 90%, even >100%**.
Critics use this to attack DCF, arguing high-growth assumptions get "drowned out"
by terminal assumptions. Damodaran's rebuttal: the **base-year inputs for the
terminal calculation** (year-5 or year-10 earnings and cash flows) are themselves
*determined by* the high-growth-phase assumptions. Change the growth-phase story
and the terminal value changes dramatically — exactly as it should. The high
terminal share is a property of the firm's place in the life cycle, not evidence
that the DCF ignores the growth years.
> source: Ch11.pdf p.12

### 2.10 The big market delusion
The chapter's signature trap (developed fully in the Cornell–Damodaran paper,
§6.3): a market advertised as **huge and scalable** attracts many entrants, and
both **entrepreneurs and their financiers** (VC and public-equity investors), each
overconfident, assign their firm a large slice of that market. Summed across all
the contenders, the **implied market shares far exceed 100%**, so the entire
cohort is collectively overpriced. The discipline against it is exactly the
revenue check in §2.3 — translate your growth assumption into an *implied market
share*, then ask whether it is plausible once rivals are also taking share. The
inevitable correction returns the cohort to earth. This is why "the market is
big" is the single most dangerous phrase in a high-growth narrative.
> source: Ch11.pdf p.5–6; SSRN 3501688 (§6.3)

### 2.11 When your value diverges sharply from price
When a DCF value differs greatly from the market price (either direction), pause
and weigh three explanations honestly: (1) **you are wrong** — your growth,
margin, or reinvestment inputs are off and the consensus is right; (2) **the
market is wrong** — mood and momentum have detached price from intrinsic value;
or (3) **both are wrong, but one is less wrong** — neither side has a crystal ball.
The healthy default is humility: assume the market may be seeing something you
are missing, re-examine and tweak the data, but accept that even after honest
revision your value may still legitimately differ from price.
> source: Ch11.pdf p.13

### 2.12 Relative valuation for high-growth firms
Standard PE makes high-growth firms look expensive. Two repairs are common
(§3 details the formulas): **forward multiples** (scale price to *expected*
earnings five or ten years out, then compare across the peer group), and
**growth-adjusted multiples**, chiefly the **PEG ratio** (PE divided by the
expected growth rate). Both are partial fixes; the chapter treats them as
cross-checks on an intrinsic valuation, not substitutes for it.
> source: Ch11.pdf p.22

### 2.13 Add-ons: the value of growth and reverse (breakeven) DCF
Two closing tools:
- **Value of growth.** Growth is *not* an unalloyed good — it is a **trade-off**.
  To grow, a firm reinvests now (denying dividends/buybacks to investors today)
  in exchange for higher earnings later. Growth adds value only if what the firm
  **harvests** as future growth exceeds what it **reinvests** to get it — i.e. only
  if the return on the reinvested capital beats the cost of capital. Growth at or
  below the cost of capital destroys or merely transfers value.
- **Breakeven / reverse-engineered valuation.** Instead of computing a value, back
  out what the *market* is assuming: (a) hold all else constant and solve for the
  single variable (growth, revenue, or risk) that makes value equal the current
  price — clean but artificial, since it isolates one of many linked inputs; (b)
  better, pick **two or three** critical inputs and map the *combinations* that
  reproduce the market price; (c) translate the market price back into the
  **story** it implies, and test how the value moves as you change that story.
> source: Ch11.pdf p.25, p.28

## 3. Metrics, formulas & rules of thumb

| Item | Formula / rule | How it shifts across the life cycle |
|---|---|---|
| **Reinvestment** | `Reinvestment_t = ΔRevenues_t / (Sales-to-Capital ratio)` | Heavy in high growth (large ΔRevenues); shrinks as growth fades toward maturity |
| **Sales-to-capital ratio** | Revenues generated per $1 of invested capital; estimate from firm data blended with sector average; lag-adjust by using a future ΔRevenue | More stable than capex/WC; converges to sector norm as firm matures |
| **Implied market share** | (Projected firm revenue) ÷ (Total addressable market) | Must stay plausible; summed across all entrants it cannot exceed 100% (big-market-delusion check) |
| **Absolute revenue change test** | ΔRevenues = Rev_t − Rev_{t−1} (in $) | A stable % growth implies a *rising* $ change as the base grows — sanity-check the dollars, not the percent |
| **Year-specific cost of capital** | WACC_t set per year, high early → declining as growth moderates and debt capacity rises | High in high growth; falls toward sector-average WACC in maturity (see [[cap_06_investing]] WACC datasets) |
| **Stable-growth ROC** | Chosen for terminal phase; either = cost of capital (no excess return) or kept above it (durable moat) | Excess return (ROC − WACC) is the only thing that makes terminal growth add value |
| **Value of growth** | Positive only if ROC on reinvested capital > cost of capital | Growth-phase reinvestment must out-earn its cost or it destroys value |
| **Terminal value share** | TV ÷ total DCF value, typically 80–100%+ for growth firms | Highest for young/high-growth firms; falls as more value comes from near-term cash flows in maturity |
| **Forward multiple** | Price ÷ *expected* EPS in year 5 or 10 (peer-group comparison) | Normalizes the high near-term PE of growth firms |
| **PEG ratio** | `PEG = PE ratio ÷ expected growth rate (%)` | Adjusts PE for growth; lower PEG = cheaper per unit of growth; breaks down when growth is volatile or near-zero |

**Rules of thumb.** (1) Force growth to fade — sustained >10-year high growth is
rare. (2) Make margins, growth, and the discount rate converge to mature levels
together, year by year. (3) Always convert a revenue forecast into an implied
market share and test it against competition. (4) Expect terminal value to be the
bulk of value; do not treat that as a modeling error. (5) Growth without
excess returns (ROC > WACC) is not value.

> source: Ch11.pdf p.7–12, p.22, p.25, p.28

## 4. Examples & cases

### 4.1 Tesla — November 2021 (the running case)
The chapter's spine is a full intrinsic valuation of Tesla at its late-2021 peak,
when "the market led in" — Tesla's market cap had run to roughly **$1.03 trillion**
by Nov-2021, after a **+158%** move in 2021 alone (the slide tabulates the
market-cap climb from ~$2.8B in Nov-2010 to >$1T in Nov-2021). Damodaran rebuilds
the value from a story translated into the three battlegrounds:
- **Revenues / scaling.** Tesla grossed ~**$46B** in revenue over the twelve months
  to Sep-2021. Damodaran's story scales revenues toward roughly **$400B by 2032**,
  which he frames against the global auto market — implying Tesla becomes one of
  the largest auto companies in the world, taking on the order of **~3% of global
  auto sales** (the slide notes the worldwide auto market was ~$2.2 trillion with
  ~75 million vehicles sold). The explicit market-share check is the
  big-market-delusion discipline in action.
- **Margins.** Tesla's pre-tax operating margin had risen to ~**13–16%** by
  2020/2021Q3; the story takes the steady-state operating margin to roughly
  **19%**, well above the auto-sector weighted-average of ~**12.5%** but justified
  by software/brand premium.
- **Reinvestment.** Sized via a sales-to-capital ratio (~**2.5**, in line with the
  auto-sector ~2.53), so the ~$350B of incremental revenue requires a
  correspondingly large but efficient reinvestment.
- **Risk.** Initial cost of capital ~**9.99%** (Tesla funded ~90% with equity;
  the slide flags a blend reflecting auto vs. tech classification — auto median
  WACC ~5.95%, tech ~7.5%), declining over time as Tesla matures.
- **Result.** The DCF produced a value-per-share **far below** the ~$1T market
  price, i.e. the market was pricing in a story even more aggressive than
  Damodaran's already-bullish one. The **breakeven** slides invert this: a grid of
  target operating margin (12%–28%) × revenue scenario (e.g. "1300/Toyota-like,"
  "1400/50% auto," "800/30% auto," "1000/40% auto") shows which *combinations* of
  margin and revenue would be needed to justify the then-current price — most
  cells fall short, with shaded cells marking the few that exceed the market cap.
> source: Ch11.pdf p.14–21, p.28 (read as images)

### 4.2 Tesla relative valuation — auto pricing and auto PEG
To cross-check, Damodaran prices Tesla against an auto peer group (Toyota, VW,
Daimler, GM, Ford, Honda, Stellantis, BMW, Renault, Nissan, Hyundai, Kia, Tata,
Maruti, BYD, etc.) on PE and on a **PEG basis** (PE ÷ expected net-income growth).
The peer-group average PE and PEG are far below Tesla's, so even on a
growth-adjusted multiple Tesla looks richly priced versus the auto sector — a
relative-valuation confirmation of the intrinsic-DCF conclusion. The point of
showing both is methodological: intrinsic and relative approaches should be run
together and reconciled, not treated as rivals.
> source: Ch11.pdf p.23–24 (read as images)

### 4.3 Excess returns across global firms — which industries add value via growth
A global data slide tabulates, by region and by industry, the share of firms
earning **ROIC above their cost of capital** (positive excess returns) versus
below. It segments **"good businesses"** (high % of firms with excess returns —
e.g. tobacco, retail/building supply, beverages, certain software and computer
services, ~60–80% positive) from **"bad businesses"** (mostly value-destroying —
e.g. drugs/biotech, precious metals, metals & mining, hotels/gaming,
oil/gas production, where only ~30–45% earn excess returns). The lesson reinforces
§2.13: growth only creates value where firms can earn above their cost of capital,
and that capacity is heavily industry-dependent.
> source: Ch11.pdf p.26–27 (read as images)

### 4.4 Airbnb — December 2020 (supplementary tool)
Used as the worked spreadsheet (AirbnbIPO.xlsx, §5). Damodaran valued Airbnb at
its IPO at roughly **$36B equity (~$54/share)**, on assumptions of: gross
bookings recovering slowly in 2021 (revenue below 2019, −10% margin) then growing
~**25%/yr** 2022–2025, reaching **>$150B gross bookings by 2031**; take-rate
rising from ~12–13% to ~14%; **target operating margin ~25%** by 2031 (below
Booking.com's 35% but above hotels); **sales-to-capital ~2.0** (vs. Booking.com
1.91); **cost of capital 6.5% rising to 7.23%**; and a **10% failure
probability**. He explicitly attacked Airbnb's **$3.4 trillion TAM** claim —
calling the **$1.4 trillion "experiences"** slice "more fictional than even
aspirational" — a textbook big-market-delusion critique. Sensitivity: a $60B
market cap would require ~$200B gross bookings and ~35% margins by 2031. He would
not short it (momentum can override fundamentals), illustrating §2.11's
price-vs-value humility.
> source: SSRN/blog (§6.4); Ch11.pdf p.5–6 (TAM discipline)

## 5. Data & tools

- **PE and PEG ratios by industry** — US: `pedata.xls`; Global: `pedataGlobal.xls`
  (`pages.stern.nyu.edu/~adamodar/`). Industry-average PE, expected growth, and
  the resulting PEG used to anchor relative valuation of high-growth firms and to
  judge whether a firm's PEG is high or low for its sector. *(Catalog only —
  industry data, not copied.)*
- **Excess-returns / ROIC datasets** — the by-industry ROIC-vs-WACC "good vs. bad
  business" data behind §4.3 (`EVA.xls`, `mgnroc.xls`; see
  [[cap_06_investing]]).
- **Tool — Airbnb IPO valuation:** `AirbnbIPO.xlsx`
  (`pages.stern.nyu.edu/~adamodar/pc/blog/AirbnbIPO.xlsx`) — a full FCFF growth-firm
  model demonstrating the year-by-year fade of growth, margin convergence to ~25%,
  sales-to-capital reinvestment (~2.0), a rising cost of capital, and a failure
  probability — the template for valuing any scaling platform. *(Not downloaded
  locally; catalog-only.)*
- **Companion blog:** "The Sharing Economy Comes Home: An IPO of Airbnb"
  (`aswathdamodaran.blogspot.com/2020/12/the-sharing-economy-come-home-ipo-of.html`)
  walks through the spreadsheet's assumptions.
- The general-purpose `fcffsimpleginzu.xlsx` from [[cap_09_valuation_101]] is the
  underlying engine these case spreadsheets specialize.

## 6. Supplementary readings — distilled

### 6.1 Blog — "Interest Rates, Earnings Growth and Equity Value: Investment Implications" (Damodaran, Mar 2021)
*Read in full via WebFetch.* Damodaran argues the effect of rising rates on stocks
depends entirely on **why** rates are rising. Mechanically, a higher risk-free
rate raises the discount rate and lowers present values (the **direct effect**);
but rate moves also signal fundamentals (the **indirect effect**) — a
**real-growth-driven** rate rise boosts revenues, margins, and reinvestment
efficiency, often offsetting the discount-rate hit, whereas an **inflation-driven**
rise hurts margins (for firms lacking pricing power) and lifts risk premiums.
Crucially for this chapter, he shows **high-growth firms are far more sensitive to
rate changes than mature value firms**: because most of a growth firm's value sits
in distant cash flows (a long "duration"), a given rate rise compresses its PE far
more than a low-growth firm's — the "growth premium" in PE shrinks as rates rise.
He values the S&P 500 under benign/neutral/malignant growth-vs-rate scenarios
(intrinsic value ~3,919 in the benign case) and links the early-2021 value/growth
rotation (energy up, tech down) to this logic. **Adds beyond the slides:** the
explicit duration/interest-rate channel explaining *why* growth firms' year-specific
discount rates and terminal assumptions matter so much, and why a rate regime
shift can re-rate the whole growth cohort.
> source: https://aswathdamodaran.blogspot.com/2021/03/rates-growth-and-value-investment.html

### 6.2 Blog — "The Aging of the Tech Sector: The Pricing Divergence of Young and Old Tech Companies" (Damodaran, Feb 2015)
*Read in full via WebFetch.* Damodaran rejects a blanket "tech bubble," arguing
"tech" is no longer a single category: of ~2,816 US tech firms in Feb-2015, ~41%
were 25+ years old, so the sector spans baby/young/middle-aged/old tech. Pricing
diverges by **age, not just sector** — young tech traded at ~**4.34× revenues**
vs. ~**2.44×** for the oldest tech, yet young *non-tech* firms actually grew
faster than young tech, and old tech was often *more* profitable and *cheaper*
than old non-tech (a possible value pocket). Tech firms show far higher
volatility but lower leverage at every age. His prescriptions: (1) "truth in
labeling" — reclassify tech-using-but-not-tech firms (Tesla, Uber) into their real
sectors; (2) age-classify rather than sector-classify; (3) recognize mispricing
is largely a *youth* effect (Shake Shack, a non-tech, spiked too); (4) because
tech life cycles are **compressed** ("aging in dog years"), use **finite-life
terminal models with steeper multiple compression**, not perpetual high growth.
**Adds beyond the slides:** empirical backing for §2.4/§2.8 — growth and pricing
multiples really do compress with age, and the compression is faster in tech, so
the "don't wait too long to put the firm into stable growth" rule is even more
binding for technology firms.
> source: https://aswathdamodaran.blogspot.com/2015/02/the-aging-of-tech-sector-pricing.html

### 6.3 Reading — "The Big Market Delusion: Valuation and Investment Implications" (Cornell & Damodaran, *Financial Analysts Journal* 76(2), 2020; SSRN 3501688)
*Abstract + FAJ overview read via WebFetch; the SSRN/FAJ full PDF returned 403 and
the authors' Cornell Capital page exposes only the abstract — distilled from the
abstract, the journal overview, and the slide treatment.* The paper formalizes the
trap in §2.10: when a market is advertised as **big and scalable**, the "big market
promise" of easily scaled, highly profitable revenue draws in many entrants, and
**overconfidence among both entrepreneurs and their financiers** (VCs and public
investors) leads each to claim a large share — so the **collective valuation of all
the contenders exceeds any realistic value of the market itself** (implied shares
sum past 100%). Initial overpricing is therefore a *systematic* feature of such
markets, followed by an **inevitable correction** back to earth. Three case studies
illustrate the arc at different stages: **dot-com retail** (1990s — correction
largely complete), **online advertising** (mid-unwind), and the **cannabis market**
(delusion just beginning). **Investment implication for an analyst:** when valuing a
single high-growth firm in a "hot" market, do not value it in isolation — anchor the
revenue forecast to a *defensible* market share net of competition, and treat the
crowd's enthusiasm as a reason for *more* skepticism, not less. **Adds beyond the
slides:** the rigorous argument and named historical episodes that justify the
revenue/market-share discipline the chapter prescribes.
> source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3501688 (full PDF 403 — distilled from abstract + https://www.tandfonline.com/doi/abs/10.1080/0015198X.2020.1730655 overview + Ch11.pdf p.5–6)

### 6.4 Reading — "Growth Investing: Betting on the Future?" (Damodaran, 2012; SSRN 2118966)
*Distilled from the CFA Institute "Enterprising Investor" review of the paper
(read via WebFetch); the SSRN page itself was not directly fetched.* Damodaran
surveys growth investing — buying companies whose value rests on *future*
expansion (typically younger, smaller firms) — versus value investing (mature,
under-priced firms with existing assets). He sorts growth strategies into
**activist** (venture capital / private equity: strong in some periods but weaker
risk-adjusted long-run returns, requiring diversification and clean exits) and
**passive** (small-cap investing; **IPO** investing — strong early, weak long-run,
best used as a supplement; and **screens** — naive high-PE/high-growth screens
underperform, and **PEG** screens are limited by the difficulty of forecasting
growth and by PEG's linear assumption). The evidence: growth investing tends to
**beat value in periods of slow aggregate earnings growth** (when scarce growth
commands a premium) and **when the yield curve is flat or inverted**, but over long
horizons **value screens (low PE, low price-to-book) dominate**; active growth
managers add more over passive than active value managers do. **Adds beyond the
slides:** the empirical reality check on §2.13 / §2.12 — betting on future growth
pays only selectively and regime-dependently, which is why the chapter insists
growth be *forced through* a valuation that prices its cost, rather than assumed to
be self-justifying.
> source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2118966 (SSRN page not fetched — distilled from https://rpc.cfainstitute.org/blogs/enterprising-investor/2012/how-does-growth-investing-measure-up)

## 7. Takeaways for valuation & modeling

For the copilot building standardized models of high-growth Brazilian equities,
Chapter 11 yields these actionable principles (raw material for
[[application_to_copilot]]):

1. **Force three convergences over the projection horizon.** Revenue growth must
   *fade* toward the sector's mature rate, operating margin must *climb* from its
   current (possibly negative) level to a defensible steady state, and the cost of
   capital must *decline* from a growth-firm high toward the sector WACC — and all
   three must be **year-specific, not flat**. The Valuation tab should expose each
   as its own time series of assumption cells (per the "no constants in formulas"
   rule), with the fade/climb/decline visibly converging.

2. **Size reinvestment off ΔRevenue via a sales-to-capital ratio, not off noisy
   capex.** Implement `Reinvestment_t = ΔRevenues_t / (Sales-to-Capital)`, seed the
   ratio from company history blended with a sector average (a `_sector.md` shared
   assumption), and offer a lead/lag toggle (size current reinvestment off a future
   revenue change). This is more robust than projecting capex and working capital
   independently for a scaling firm.

3. **Translate every revenue forecast into an implied market share and stress it.**
   Before accepting a growth path, the assumption session should auto-compute
   implied market share against a stated TAM and flag it if it is implausible once
   competitors' shares are added — the engine's built-in defense against the **big
   market delusion**. Tag the TAM with its source/date; treat vendor "TAM" claims
   as suspect.

4. **Expect and explain terminal-value dominance.** The model should report the
   terminal-value share of total value and *not* warn on a high (80–100%+) figure
   for a growth firm — instead surface the year-5/10 base-year inputs that drive it,
   since those are where the growth-phase story actually lives. Keep the
   stable-phase **ROC vs. WACC** spread as an explicit, defensible input (growth
   adds value only when ROC > WACC).

5. **Cap and justify the high-growth window; converge fast for "tech-like" firms.**
   Default to a high-growth window of **≤10 years** and, for technology-style
   businesses, compress it further and steepen multiple decay (the "aging in dog
   years" finding). The assumption layer should make the analyst justify any
   high-growth period that runs long.

6. **Run intrinsic and relative valuation together, and reverse-engineer the
   price.** Pair the FCFF DCF with a **forward-multiple / PEG** peer cross-check,
   and add a **breakeven** view that solves for the margin × revenue (and risk)
   combinations implied by the market price. Surface the price-vs-value gap with
   the §2.11 humility framing (you / market / both wrong) rather than as a buy/sell
   signal — consistent with the project's no-recommendation compliance rule.

> source: synthesis of Ch11.pdf p.5–13, p.22, p.25, p.28 + blogs (§6.1–6.2) + papers (§6.3–6.4)

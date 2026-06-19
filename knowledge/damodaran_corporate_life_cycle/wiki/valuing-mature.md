---
concept: valuing-mature
title: Valuing Mature Firms
theme: Valuing mature & declining firms
status: draft
---

# Valuing Mature Firms

**What it is.** Valuing a firm whose growth story is largely written — revenues near the economy's growth rate, settled margins, falling reinvestment needs — so that value is dominated by assets already in place and by three *policy* choices the firm controls (financing mix, cash return, and how well existing assets are managed) rather than by growth assumptions.

## Core idea

A mature business throws off more cash than it can productively redeploy, so intrinsic value becomes far less sensitive to growth and far more sensitive to the firm's financing, payout, and operating efficiency. The same DCF machinery from [[dcf-foundations]] still applies, but the analyst's effort shifts: stop debating top-line growth and instead interrogate the debt schedule (which feeds [[cost-of-capital]]), the dividend/buyback policy ([[cash-return-dividends-buybacks]]), and whether existing assets earn above their cost of capital ([[roic-and-excess-returns]]).

The pivot of the chapter is that a mature firm run sub-optimally carries a separable **value of control** — the gap between its value as currently run and its value if restructured. That makes the mature-firm valuation naturally a *two-case* exercise: a status-quo run and a restructured run. The same heterogeneity that clusters in maturity (multi-business conglomerates, multinationals) calls for [[sum-of-the-parts-octopus]] valuation, and the slow erosion of incumbents calls for a disruption stress-test.

## Across the life cycle

- **Young / high growth:** value lives in future bets and the terminal block; near-term cash flows are small or negative. See [[valuing-high-growth]] and [[terminal-value]].
- **Mature (this concept):** near-term cash flows are large and dominate value; the terminal piece is a smaller fraction, and the growth story is an *extension of history* — past revenue growth, margins, and reinvestment — rather than a new narrative. Because settled risk profiles have long price histories, historical risk-parameter estimates (beta) are more defensible here than for young firms.
- **Decline:** the picture inverts toward negative growth and distress. See [[valuing-declining-and-distressed]].

## Mechanics / formulas

**Status-quo vs. restructured DCF.** Run the *same* FCFF DCF twice with two assumption sets and compare value per share. The levers that move from status quo to restructured are the operating margin, the sales-to-capital ratio (capital efficiency of growth), and the cost of capital (financing mix) — the operational form of the [[value-of-control]] idea. In the chapter's running case, the gap is roughly a one-third uplift.

**Acquisitions = reinvestment.** Mature firms often buy growth. Treat acquisition spend exactly like capex on the reinvestment line, and credit it with value only when the implied ROC exceeds the cost of capital. `Reinvestment = ΔRevenue ÷ Sales-to-capital`, so a higher sales-to-capital ratio means more capital-efficient growth and higher FCFF.

**Terminal value discipline.** Stable growth must sit at or below the economy's growth rate (the risk-free rate is a practical ceiling), and the firm must *behave* like a stable firm — average risk and reinvestment, not frozen-high inputs. Critically, **do not lock today's sub-optimal margins or ROC into perpetuity** if a fix is plausible; doing so undervalues a poorly run firm by assuming bad practice continues forever. See [[terminal-value]].

**Pricing with EV/EBITDA.** For mature and multi-business firms, enterprise-value multiples (EV/EBITDA, EV/EBIT, EV/Revenues, EV/Capital) are preferred because they are capital-structure-neutral — vital when mature firms carry heavy and varied debt — and because EBITDA/operating income survive to the *divisional* level for SOTP even when net income/EPS do not. Choose the multiple *before* seeing each one's answer to fight bias, control comps for growth, margin, ROC, [[moat]], and disruption exposure, and clean cross-country accounting differences. See [[valuation-multiples]].

## Pitfalls & nuances

- **Extrapolating reported earnings off sub-optimal management.** If a management change is plausible, valuing existing assets off *reported* earnings undervalues them — you are implicitly assuming bad management forever (the seed of [[value-of-control]]).
- **Managed earnings.** Long, stable histories give management both incentive and accounting discretion to smooth reported numbers; the analyst must look through that.
- **Freezing today's practice into the terminal value** — the most expensive terminal-value mistake for a poorly run mature firm.
- **Under-weighting disruption.** A price-to-value gap that *widens* (price drifts down, not up toward your estimate) is a warning to raise the probability of failure or haircut margins, not to declare a bargain.
- **Blending heterogeneous segments.** Consolidated averages silently misprice a genuinely multi-business firm; use [[sum-of-the-parts-octopus]].

## Related concepts

- [[value-of-control]] — the status-quo vs. restructured gap, the central mature-firm adjustment
- [[sum-of-the-parts-octopus]] — valuing the multi-business / multinational mature firm by segment
- [[valuing-declining-and-distressed]] — the next stage, where growth turns negative
- [[terminal-value]] — where mature-firm inputs must look genuinely mature
- [[valuation-multiples]] — EV/EBITDA and the EV family for mature-firm pricing
- [[roic-and-excess-returns]] — the test for whether assets-in-place create value
- [[cash-return-dividends-buybacks]] — the payout policy that dominates mature-firm value
- [[cost-of-capital]] — the financing-mix lever, fed by the debt schedule
- [[moat]] — what lets a mature firm keep earning excess returns
- [[activist-investing]] — the trigger that raises the probability of control

## Provenance
- Chapter notes: [[cap_12_valuing_mature]]
- Sources: [Valuing Mature Businesses (Ch12 slides, CLC companion site)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/CLC.htm); [Divergence in the Drug Businesses: Pharmaceuticals and Biotechnology (Nov 2015)](https://aswathdamodaran.blogspot.com/2015/11/divergence-in-drug-businesses.html); [EV multiples by industry (vebitda.xls)](https://pages.stern.nyu.edu/~adamodar/pc/datasets/vebitda.xls); [Unilever valuation (Unilever2022.xlsx)](https://pages.stern.nyu.edu/~adamodar/pc/blog/Unilever2022.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch12.txt

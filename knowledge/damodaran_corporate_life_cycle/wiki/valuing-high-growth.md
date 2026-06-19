---
concept: valuing-high-growth
title: Valuing High-Growth Firms
theme: Valuing young & high-growth firms
status: draft
---

# Valuing High-Growth Firms

**What it is.** Valuing a firm whose value still rests on a future not yet arrived, by forcing an optimistic story through a time-varying arithmetic engine in which three things must *converge to maturity over the horizon* — revenue growth fades, operating margin climbs to a sustainable level, and the cost of capital declines toward the sector average — with reinvestment sized to the growth and the terminal value, normally, dominating total value.

## Core idea
A high-growth firm has cleared the start-up and product-test gates of [[valuing-young-and-startups]]: it has real, scaling revenues and often emerging profitability, plus enough financial history and a governance structure to lean on. The narrative still centres on *potential*, but now it must address the **business model** along three axes — scalability (growth), profitability (margins) and reinvestment (growth efficiency) — and each piece must be forced through a consistent valuation so the pieces do not contradict one another.

The hard, bias-prone judgements live in three estimation battlegrounds: **revenues** (the biggest questions, because you are assuming revenue can be scaled — discipline it with market size and implied share, see [[big-market-delusion]]); **margins** (positive trend lines breed over-optimism; temper with unit economics); and **reinvestment** (the hardest, because historical reinvestment is volatile and obscured by stock-funded acquisitions — look to industry averages and the business model). The defining discipline of the chapter is making everything *converge together, year by year* — and accepting that the terminal value will carry most of the value, which is a property of the firm's position on [[corporate-lifecycle]], not a DCF flaw.

## Across the life cycle
This sits between [[valuing-young-and-startups]] (left) and [[valuing-mature]] (right) on the arc. The whole exercise is *about* the transition: the firm is being modeled into stable growth over the horizon, so revenue growth, margins and risk are all moving from growth-firm levels toward mature ones. For technology businesses the [[compressed-lifecycle-tech]] finding bites — growth and multiples compress faster ("aging in dog years"), so the high-growth window should be shorter and the multiple decay steeper, and naïve perpetual growth in terminal value over-values fast-aging tech.

## Mechanics / formulas
**The three forced convergences (all year-specific, never flat):**

1. **Revenue growth must fade.** As the base grows, percentage growth falls mechanically. Discipline it three ways: check *absolute* dollar revenue changes (a constant 40% on a big base may imply an implausible dollar increase); read the firm's own trend lines; and anchor the long-run rate on mature firms in the same business.
2. **Margins converge to a sustainable level.** Usually the current margin is too *low* (up-front fixed costs, growth-spend booked as operating cost, lag between spend and the revenue it creates) and must rise; less often it is too *high* (a niche product in a small market) and falls as competition arrives. Project a *path*, not the frozen current margin.
3. **The cost of capital declines year by year.** Carry high costs of equity and debt while growth peaks, then let them fall as growth moderates, earnings rise, the firm flips from cash-consuming to cash-generating, and debt capacity rises — a [[cost-of-capital]] that is a year-specific time series, not one static rate.

**Reinvestment via sales-to-capital** (shared with [[valuing-young-and-startups]]):

```
Reinvestment_t = ΔRevenues_t ÷ Sales-to-Capital ratio
```

Estimate the ratio from the company's own data (more stable than year-to-year capex/working-capital swings) blended with sector averages; a lag between spending and the revenue it produces can be modeled by sizing the current period's reinvestment off a *future* period's revenue change.

**The terminal transition.** Don't wait too long — sustained high growth beyond ~10 years is rare. Give the firm stable-growth characteristics (lower Ke/Kd, higher debt ratio) and choose a stable-phase **return on capital**: setting ROC equal to the cost of capital implies no excess returns (growth adds no value), so Damodaran prefers to preserve some flexibility for a durable moat. Because cash flows are low/negative early and high late, the **terminal value is typically 80–100%+ of total value** — and that is correct: the year-5/10 base-year inputs feeding the terminal calculation are themselves *set by* the high-growth-phase story, so changing the story changes terminal value exactly as it should (see [[terminal-value]] and [[fcff]]).

**Value of growth.** Growth is a trade-off, not a free good: it adds value only if the return on reinvested capital beats the cost of capital. Growth at or below the cost of capital destroys or merely transfers value (see [[roic-and-excess-returns]]).

**Relative cross-checks.** Standard P/E makes growth firms look expensive; repair with **forward multiples** (price ÷ expected EPS five or ten years out) and the **PEG ratio** (P/E ÷ expected growth %). Both are partial — cross-checks on the intrinsic value, never substitutes (see [[valuation-multiples]]).

## Pitfalls & nuances
- **Flat assumptions.** Holding growth, margin or WACC constant breaks internal consistency; all three must move together.
- **Attacking terminal-value dominance.** A high terminal share is a feature of the life-cycle position; surface the base-year inputs that drive it rather than warning on the percentage.
- **Trusting noisy historicals for reinvestment.** Stock-funded deals corrupt reported reinvestment; size it off ΔRevenue.
- **Skipping the implied-market-share check.** Always convert the revenue forecast into an implied share and stress it against competitors — the defence against the [[big-market-delusion]].
- **Growth without excess returns.** If stable-phase ROC ≤ WACC, the growth you modeled adds nothing.
- **Value far from price.** Weigh honestly that you may be wrong, the market may be wrong, or both — present the gap with humility, never as a buy/sell signal (compliance).

## Related concepts
- [[valuing-young-and-startups]] — the prior stage; shares the sales-to-capital reinvestment logic
- [[big-market-delusion]] — the implied-market-share discipline that polices the revenue forecast
- [[valuing-mature]] — the destination the three convergences aim at
- [[compressed-lifecycle-tech]] — why tech firms must converge faster with steeper multiple decay
- [[terminal-value]] — why it dominates here, and the r−g engine behind it
- [[cost-of-capital]] — the year-specific WACC that must decline over the horizon
- [[fcff]] — the firm-level cash flow being projected and discounted
- [[roic-and-excess-returns]] — growth only creates value when ROC > WACC
- [[valuation-multiples]] — forward multiples and PEG as relative cross-checks
- [[moat]] — what justifies a stable-phase ROC above the cost of capital

## Provenance
- Chapter notes: [[cap_11_valuing_high_growth]]
- Sources: [Interest Rates, Earnings Growth and Equity Value](https://aswathdamodaran.blogspot.com/2021/03/rates-growth-and-value-investment.html), [The Aging of the Tech Sector](https://aswathdamodaran.blogspot.com/2015/02/the-aging-of-tech-sector-pricing.html), [The Big Market Delusion (Cornell & Damodaran, SSRN 3501688)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3501688), [Growth Investing: Betting on the Future? (SSRN 2118966)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2118966), [Airbnb IPO valuation model](https://pages.stern.nyu.edu/~adamodar/pc/blog/AirbnbIPO.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch11.txt

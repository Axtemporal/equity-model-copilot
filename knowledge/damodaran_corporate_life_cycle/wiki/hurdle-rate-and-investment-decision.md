---
concept: hurdle-rate-and-investment-decision
title: The Investment Decision & Hurdle Rate
theme: Corporate finance: investing & cost of capital
status: draft
---

# The Investment Decision & Hurdle Rate

**What it is.** The first principle of corporate finance: invest only in assets whose expected return clears a risk-adjusted hurdle rate — the cost of capital — measured by discounting the investment's own cash flows (NPV/IRR) or by comparing its accounting return to that hurdle.

## Core idea

To decide whether to make an investment, you forecast its expected earnings and cash flows and discount them at the **hurdle rate** to see whether the business can at least break even on a value basis. That hurdle rate *is* the [[cost-of-capital]] — the blended cost of funding the whole business. An investment creates value only if it earns more than this rate; the excess is the firm's economic profit, the subject of [[roic-and-excess-returns]].

Two design rules govern the hurdle rate. It should reflect the risk of *the investment itself*, not the average risk of the firm taking it, and it should use a debt ratio appropriate to *that investment's* cash flows. And only **undiversifiable (macro) risk** earns a premium — firm-specific (micro) shocks wash out across a diversified portfolio and so do not raise the hurdle rate.

The investment decision is an **evidence-gathering exercise**: the forecast draws on past similar projects, industry norms, market and price data, debt history, and earnings variability — and (not by accident) the same evidence stream feeds the discount-rate estimate.

This is the **dominant decision when firms are young**: a start-up's entire value lives in future investments, so getting the investment decision right is its whole story. It matters at every stage, but in maturity the live question shifts to financing and in decline to cash return — the rotation described in [[corporate-finance-first-principles]] and [[corporate-lifecycle]].

## Across the life cycle

- **Young / high-growth firms** live or die by the investment decision. Their hurdle rate is *highest* (young US firms ≈ 9–9.6% median cost of capital) and their accounting returns are *deeply negative* — the youngest deciles show median ROIC of roughly −58% to −75%, and a large share of firms earn negative returns. The whole game is whether projected investments will eventually clear the hurdle. Real-option arguments (the option to expand into a large, uncertain market) cluster here — see [[real-options]].
- **Mature firms** have stabilized returns; the danger inverts. The temptation is to pour capital into growth that earns *less* than the cost of capital and therefore destroys value. Here the investment decision is mostly a *discipline against over-investment*.
- **Declining firms** should be *divesting and liquidating*, not reinvesting; the value-creating move is returning cash, not funding negative-spread projects (the "value trap" pattern).

The empirical backdrop is sobering: roughly **80% of firms globally earn returns below their cost of capital**, so "grow at all costs" is, on the evidence, more likely to destroy value than create it.

## Mechanics / formulas

Two families of decision rule, both judged against the hurdle rate.

**Cash-flow rules (Damodaran's preference):**

```
NPV = Σ [ E(CF_t) / (1 + hurdle rate)^t ] − Initial investment   → accept if NPV > 0
IRR = the rate r such that Σ [ E(CF_t) / (1 + r)^t ] = 0          → accept if IRR > hurdle
```

| Dimension | NPV | IRR |
|---|---|---|
| Output | Absolute (currency) — biases toward big-capital projects | Percentage — biases toward small-capital projects |
| Uniqueness | One value | Multiple IRRs possible if cash-flow signs flip more than once |
| Reinvestment of interim cash | At the hurdle rate (realistic) | At the project's own IRR (optimistic) |

Damodaran **prefers NPV**; the unrealistic reinvestment assumption is IRR's deciding flaw.

**Accounting rules (compare to the matching hurdle):**

```
ROIC = After-tax operating income (NOPAT) / Invested capital   → vs. cost of capital
ROE  = Net income / Book value of equity                       → vs. cost of equity
```

A third rule recognizes embedded flexibility: a project with negative stand-alone NPV can still be worth taking if it buys a valuable **option to expand**. That logic — and its abuse — is the domain of [[real-options]].

## Pitfalls & nuances

- **The hurdle belongs to the project, not the firm.** Use the investment's own risk and an appropriate financing mix, not the company average.
- **Prefer NPV to IRR.** IRR's reinvestment assumption (and its multiple-root problem) can flip rankings; NPV reinvests at the hurdle rate, which is realistic.
- **Don't inflate the hurdle rate to express fear.** Discrete risks (project failure, regulatory denial) belong in probabilities/scenarios, not a fudged discount rate.
- **Accounting returns are noisy.** Capitalize R&D and operating leases, strip one-time charges, and net out cash before trusting ROIC/ROE — see [[roic-and-excess-returns]].
- **Spend effort on cash flows, not the discount rate.** The cross-firm cost-of-capital spread is narrow (~5–10%, median ~8%); the big valuation errors come from revenue, margin, and reinvestment forecasts.
- **Growth ≠ value.** More capex only creates value when the investment's return exceeds the hurdle; below it, growth destroys value despite rising revenues.

## Related concepts

- [[cost-of-capital]] — the hurdle rate's construction and how it drifts with maturity
- [[roic-and-excess-returns]] — the accounting-return version of the same value test
- [[real-options]] — when embedded flexibility justifies a negative-NPV beachhead
- [[corporate-finance-first-principles]] — the investment decision as one of the three
- [[corporate-lifecycle]] — why this decision dominates when firms are young
- [[fcff]] — the cash flows the firm-level NPV discounts
- [[uncertainty-in-valuation]] — where discrete risks belong (not the hurdle rate)

## Provenance

- Chapter notes: [[cap_06_investing]], [[cap_05_corpfin_101]]
- Sources: [Data Update 5 for 2024: Profitability (Jan 2024)](https://aswathdamodaran.blogspot.com/2024/01/data-update-5-for-2024-profitability.html), [The Cost of Capital: The Swiss Army Knife of Finance](https://pages.stern.nyu.edu/~adamodar/) (costofcapital.pdf, local), [Decline and Denial: Blackberry End game and Microsoft as a Value Trap (Sep 2013)](https://aswathdamodaran.blogspot.com/2013/09/decline-and-denial-requiem-for.html)
- Raw (gitignored): reference/damodaran_clc/text/Ch6.txt, reference/damodaran_clc/text/Ch5.txt

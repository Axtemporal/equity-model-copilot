---
concept: corporate-finance-first-principles
title: Corporate Finance First Principles
theme: Corporate finance: investing & cost of capital
status: draft
---

# Corporate Finance First Principles

**What it is.** Corporate finance is not a grab-bag of accounting ratios or deal-making techniques but a single governing logic: every business faces just three decisions — where to invest, how to finance, and what to do with the cash — all subordinated to one objective, maximizing the value of the business.

## Core idea

Damodaran reduces the whole discipline to **one objective and three decisions**, and insists the same skeleton applies to every firm — public or private, large or small, young or old. The objective is to **maximize the value of the business**, which in his framing operationalizes as maximizing long-term owner/shareholder value. He defends this against a pure *stakeholder* objective on two grounds: making managers accountable to everyone makes them accountable to no one (it leaves the business rudderless when stakeholder interests genuinely collide), and it dissolves accountability. The objective is "not perfect," but it gives a usable decision rule that the three decisions can serve.

The three decisions are:

- **The investment decision** — put money only into assets that earn a return above a risk-adjusted hurdle rate. This is the domain of [[hurdle-rate-and-investment-decision]] and the value test of [[roic-and-excess-returns]].
- **The financing decision** — find the right *mix* of debt and equity (the [[capital-structure-tradeoff]]) and the right *kind* of debt, matched to the assets it funds.
- **The cash-return (dividend) decision** — if the firm cannot find investments that beat the hurdle, return the residual cash to owners, as dividends or buybacks ([[cash-return-dividends-buybacks]]).

The decisions stack as a **residual ordering**: first take every good investment, then choose the financing mix that minimizes the hurdle rate, and only *then* pay out whatever cash is left over. What is "left over" is [[fcfe]] — the firm's *potential* dividends, distinct from what it actually pays.

All three decisions are made under uncertainty. Damodaran sorts that uncertainty into three orthogonal pairs — *estimation vs. economic*, *micro vs. macro*, *discrete vs. continuous* — because the right response differs by type (research cures estimation noise but not economic noise; managers move only the micro component). That triage is the subject of [[uncertainty-in-valuation]].

## Across the life cycle

The principles never change, but **the emphasis rotates with age** — this is the corporate-finance face of the whole [[corporate-lifecycle]] scaffold and the heart of [[acting-your-age-serenity]]:

| Stage | Investing policy | Financing policy | Cash-return policy |
|---|---|---|---|
| Start-up / young growth | New product development, build/test the market | Equity / VC; debt only if assets allow | None — cash burn, equity infusions |
| High growth | Scale up production | Equity, building debt capacity | Beginnings of cash flow |
| Mature growth | Add capacity + new products | Use the rising debt capacity | Cash buildup; returns begin |
| Mature stable | Maintain capacity + acquisitions | Use peak debt capacity | Peak cash returns |
| Decline | Reduce/divest capacity | Wind debt down from peak | Return cash from drawdown/divestiture |

So the **dominant decision rotates: investment (young) → financing (mature) → cash-return (decline)**. The practical reading for an analyst is *which model section deserves the most scrutiny* at each stage. **Mismatched policy destroys value** — a young firm loading up on debt, or a declining firm hoarding cash instead of returning it.

## Mechanics / formulas

The three decisions, written as rules:

```
1. Investment: accept iff  expected return > hurdle rate
   (hurdle rate reflects the INVESTMENT's risk + an appropriate financing mix,
    not the firm's average risk)

2. Financing: choose the debt/equity mix that MINIMIZES the hurdle rate
   (= maximizes value); match the debt's currency/maturity/cash-flow profile
   to the assets it funds

3. Cash return (residual): payout = FCFE not reinvested above the hurdle
   FCFE = Net Income − (Cap-Ex − D&A) − ΔNon-cash WC + (New Debt − Debt Repaid)
```

Two design rules govern the investment decision: the hurdle rate is a property of the *project* (its risk and its appropriate leverage), not of the firm taking it; and the return must be measured on actual cash flows, time-weighted (when they arrive, not just their total). Damodaran's clear preference is the time-weighted cash-flow measures (NPV/IRR) over accounting returns — see [[hurdle-rate-and-investment-decision]].

The **debt trade-off** in one line: debt's biggest plus is the tax shield (interest is deductible; cash to equity is not); its biggest minus is default/bankruptcy risk. So firms with large, stable, predictable earnings and low distress risk can carry more debt; fragile firms should lean to equity.

## Pitfalls & nuances

- **Don't confuse the firm's risk with the project's risk.** The hurdle rate belongs to the investment, with leverage appropriate to *that* investment's cash flows.
- **Only undiversifiable (macro) risk earns a premium** in the hurdle rate; firm-specific (micro) risk diversifies away and should not inflate the discount rate.
- **The residual ordering is strict.** Returning cash before exhausting value-creating investments, or reinvesting at a negative spread instead of paying out, both destroy value.
- **Don't bury discrete risks in the discount rate.** Handle catastrophic, low-probability risks with probabilities/scenarios, not a fudged hurdle rate.
- **"Maximize value" is a discipline, not a slogan.** Because roughly 80% of firms earn below their cost of capital, the investment decision is more often a guard against over-investment than a hunt for projects to fund.

## Related concepts

- [[hurdle-rate-and-investment-decision]] — the investment decision in detail (NPV/IRR above the hurdle)
- [[cost-of-capital]] — the hurdle rate's construction and how it fades with maturity
- [[roic-and-excess-returns]] — the value test that all three decisions ultimately serve
- [[capital-structure-tradeoff]] — the financing-mix decision (tax shield vs. distress)
- [[cash-return-dividends-buybacks]] — the cash-return decision and how to return cash
- [[fcfe]] — "potential dividends," the residual the cash-return decision distributes
- [[uncertainty-in-valuation]] — the noise every decision is made under, and how to triage it
- [[corporate-lifecycle]] — the arc along which the decision emphasis rotates
- [[acting-your-age-serenity]] — why matching policy to stage is the through-line

## Provenance

- Chapter notes: [[cap_05_corpfin_101]], [[cap_01_unifying_theory]]
- Sources: [Corporate Finance 101: A Big Picture, Applied Class (Jan 2016)](https://aswathdamodaran.blogspot.com/2016/01/corporate-finance-101-big-picture.html), [Online Corporate Finance class page (Stern)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastcfonline.htm), [Living with Noise: Investing and Valuation in the Face of Uncertainty](https://pages.stern.nyu.edu/~adamodar/pdfiles/country/NoiseMotleyFool.pdf) (SSRN 2323621)
- Raw (gitignored): reference/damodaran_clc/text/Ch5.txt, reference/damodaran_clc/text/Ch1.txt

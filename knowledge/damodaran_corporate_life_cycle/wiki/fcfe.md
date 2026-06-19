---
concept: fcfe
title: Free Cash Flow to Equity (FCFE)
theme: Corporate finance: financing & cash return
status: draft
---

# Free Cash Flow to Equity (FCFE)

**What it is.** The cash a firm *could* return to its equity holders after meeting reinvestment needs and settling debt flows — the "potential dividend" — computed from net income by adding back non-cash charges, subtracting net reinvestment, and adding net debt issued; its sign flips from negative to positive as a firm ages.

## Core idea

FCFE is the ceiling on what equity holders can be paid without impairing the business or its target capital structure. It is the residual cash *available* to equity, which is why the cash-return decision (see [[cash-return-dividends-buybacks]]) is framed as choosing how much of FCFE actually to distribute. The distinction between **potential** dividends (FCFE — what the firm *could* pay) and **actual** dividends (what it *does* pay) is the heart of cash-return analysis: the gap between them is what builds or drains the cash balance.

Crucially, FCFE is *not* net income. A firm can be profitable on paper yet have deeply negative FCFE because capex, working-capital builds, and debt repayment consume the earnings — Tesla had negative FCFE for years through its high-growth phase even while scaling. Reported profitability does not equal distributable cash.

## Across the life cycle

Because FCFE nets reinvestment and debt flows against earnings, its trajectory mirrors the life-cycle curve — and its **sign** is the headline signal:

- **Start-up / young growth.** Net income negative or thin, reinvestment heavy → FCFE **negative**. These firms consume cash and must raise it (equity, sometimes debt); they cannot return cash.
- **High growth.** Even as net income turns positive, large capex and working-capital builds keep FCFE negative or near zero. Profitability ≠ distributable cash yet.
- **Mature growth → mature stable.** Reinvestment needs fall faster than earnings → FCFE turns solidly **positive** and grows. This is where the cash-return decision switches on.
- **Decline.** With little to reinvest and assets being run down or divested, FCFE can be **very large** relative to earnings — returning cash becomes the central managerial task.

Damodaran's age-decile data make the arc concrete: the youngest deciles show negative FCFE; the oldest show the largest FCFE and the highest payout. Cash return scales up monotonically with age because FCFE does.

## Mechanics / formulas

The FCFE waterfall — the "potential dividend":

```
  Net income
+ Depreciation & amortization        (non-cash add-back)
− Capital expenditures & acquisitions (net capex)
− Increase in non-cash working capital
+ Net debt issued (new borrowings − debt repaid)
─────────────────────────────────────────────────
= Free Cash Flow to Equity (FCFE)
```

An equivalent compact form, and the **FCFE-before-debt** intermediate the worked examples use:

```
FCFE = Net income − (Capex − D&A) − ΔNon-cash WC + (New debt − Debt repaid)

FCFE before debt = Net income + D&A − Net capex − ΔNon-cash WC   (± divestitures)
FCFE             = FCFE before debt + Net debt raised
```

**Reading the lines.** The `(Capex − D&A)` term is *net* reinvestment in long-term assets; the working-capital term captures cash tied up in growth; the net-debt term means a firm growing its debt (toward its [[debt-capacity-by-stage]]) adds to FCFE, while one deleveraging subtracts from it. The debt and divestiture lines can dominate the result — a mature firm's FCFE can be swollen by net debt raised or asset sales well beyond its net income.

**Link to the cash balance.** Because `Δ Cash = FCFE − cash returned`, FCFE is the flow that, net of payout, accumulates into the balance-sheet stock of cash (see [[value-of-cash]]).

## Pitfalls & nuances

- **FCFE is equity-level, FCFF is firm-level.** FCFE is *after* interest and net debt flows and is discounted at the cost of equity; [[fcff]] is before financing flows and discounted at WACC. Mixing the two — e.g. discounting FCFE at WACC — double-counts the financing effect.
- **Profit is not cash.** The single most common error is treating net income as distributable. Always run the full waterfall.
- **Negative FCFE is normal for young firms, not a defect.** It signals a firm in the investing-dominant stage that should be *raising* capital, not returning it. A modeled dividend on negative FCFE is a red flag.
- **Net debt issued is a policy choice, bounded by capacity.** It should follow the target capital structure and the firm's debt capacity, not be tuned to manufacture a positive FCFE.
- **Model it, never hardcode it.** FCFE should be computed from the linked income statement, capex/working-capital schedule, and debt schedule — consistent with "no constant embedded in a formula."

## Related concepts

- [[cash-return-dividends-buybacks]] — the decision of how much of FCFE to actually distribute
- [[value-of-cash]] — where un-returned FCFE accumulates and how the market prices it
- [[fcff]] — the firm-level counterpart, discounted at WACC
- [[dcf-foundations]] — FCFE is the cash-flow input to an equity-side DCF
- [[corporate-finance-first-principles]] — FCFE as the residual after invest + finance
- [[debt-capacity-by-stage]] — net debt issued, a waterfall line, is bounded by capacity
- [[roic-and-excess-returns]] — reinvestment in the waterfall only adds value above the cost of capital

## Provenance

- Chapter notes: [[cap_08_cash_return]], [[cap_05_corpfin_101]]
- Sources: [Damodaran, "Data Update 7 for 2023: Dividends, Buybacks and Cashflows"](https://aswathdamodaran.blogspot.com/2023/03/data-update-7-for-2023-dividends.html), [Damodaran, "January 2017 Data Update 9: Dividends and Buybacks"](https://aswathdamodaran.blogspot.com/2017/02/january-2017-data-update-9-dividends.html), [dividend policy tool (dividends.xlsx)](https://pages.stern.nyu.edu/~adamodar/pc/dividends.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch8.txt, reference/damodaran_clc/text/Ch5.txt

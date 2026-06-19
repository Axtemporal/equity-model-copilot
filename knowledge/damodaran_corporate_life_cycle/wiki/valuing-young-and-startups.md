---
concept: valuing-young-and-startups
title: Valuing Young & Start-up Firms
theme: Valuing young & high-growth firms
status: draft
---

# Valuing Young & Start-up Firms

**What it is.** A discipline for valuing companies with no operating history, negligible (or negative) earnings and no clean comparables by building every input *top-down from a story* — TAM → market share → target margin → sales-to-capital reinvestment → a failure-adjusted DCF — rather than extrapolating a non-existent past.

## Core idea
The absence of data does not justify abandoning intrinsic valuation. The same identity holds — value equals expected cash flows discounted for their risk — but the inputs must come from a coherent narrative instead of from history. Damodaran's workflow is: (1) tell a disciplined story about the business; (2) filter it through a feasibility test before letting it become numbers; (3) translate each story element into the handful of inputs that actually move value; (4) value the business and bridge to per-share equity, charging *explicitly* for the real chance the firm never reaches steady state; (5) keep a feedback loop open to fight your own attachment to the story.

He contrasts this with the venture-capital shortcut — a short forecast cut off with an exit multiple, discounted at an arbitrarily high "target return" of 50–70% — which he classifies as forward *pricing* dressed up as valuation (see [[intrinsic-vs-relative-valuation]] and [[pricing-game-vs-value-game]]). The VC target rate is supposed to bundle operating risk *and* failure risk, but with no transparent mapping of either; the intrinsic method instead keeps the cost of capital honest and handles death separately.

## Across the life cycle
This is the framework for the far-left edge of [[corporate-lifecycle]] — idea-stage and start-up firms. As the firm clears the product-test and scaling gates it becomes a [[valuing-high-growth]] case: a real revenue base lets you lean more on track record and less on pure story, the convergence mechanics take over, and failure risk shrinks. For user-driven platforms, [[value-per-user]] supplies a parallel, disaggregated cross-check. The method is *stage-specific by construction* — it exists precisely because mature-firm models break when there is nothing to extrapolate.

## Mechanics / formulas
The distinctive contribution is a *connected chain* of inputs:

1. **Revenue (top-down).** `Steady-state revenue = TAM × market share`. TAM is itself sized from a story (e.g. penetration scaling with per-capita income and connectivity); interim-year revenue is interpolated along a growth path from today's base to that steady state. The bottom-up alternative (build from existing capacity/units) is more reliable but usually unavailable at idea stage.
2. **Operating profit.** `EBIT = Revenue × target pre-tax operating margin`, where the margin *glides* from today's (often negative) level to a maturity target benchmarked on an efficient peer — see [[valuing-high-growth]] for the convergence logic.
3. **Reinvestment.** `Reinvestment_t = ΔRevenue_t ÷ sales-to-capital ratio`. A higher ratio means less capital per new dollar of revenue (capital-light); the ratio is typically high early and settles lower as the firm scales.
4. **Free cash flow.** `FCFF = EBIT × (1 − tax) − Reinvestment` (see [[fcff]]). Early FCFF is usually deeply negative — negative EBIT *and* heavy reinvestment — and the modeled turn to positive is the payoff of the story, not a red flag.
5. **Discount rate — operating risk only.** Keep the cost of capital near a diversified-investor / mature-company level (often 9–11%), *not* a VC target rate. Failure is pulled out and handled separately (see [[failure-probability]]). This is the single most important structural choice: do not inflate the discount rate to "cover" the chance of death.
6. **Terminal value.** `TV = FCFF(terminal+1) ÷ (terminal cost of capital − g)`, with `g` capped at the growth rate of the economy (see [[terminal-value]]).
7. **Survival adjustment.** `Equity value (adjusted) = going-concern value × p_survive + failure value × p_fail`, where failure value is typically cash on hand or an asset haircut.
8. **Per-share bridge.** Going-concern (failure-adjusted) value + cash & non-operating assets − debt − minority interests (± option overhang) ÷ vesting-adjusted shares.

**Three things to get right** (Damodaran's "key indicators"): the cash-flow *shape* (deep early negatives → improving → positive), a discount rate that looks *low* versus VC rates (a feature), and an *explicit* failure probability. Value hinges on roughly six inputs — revenue growth, target margin, sales-to-capital, cost of equity, cost of debt, failure probability — so surface and stress those, ideally through a [[uncertainty-in-valuation]] simulation, rather than randomising dozens.

## Pitfalls & nuances
- **Burying failure in the discount rate.** The cardinal error. Resist VC 50–70% rates; model death as a probability with a recovery value.
- **Freezing the current margin.** Early margins are depressed by up-front fixed costs and growth-spend mingled with operating costs; project the *path*, not the snapshot.
- **Treating the story as certain.** Run it through the feasibility filter (Possible → Plausible → Probable) and let only *probable* elements drive the base case; almost any story is *possible*.
- **Relative valuation as a substitute.** With negative earnings, P/E is out; falling back on EV/Sales, EV/GOV or EV/user is *pricing*, treacherous for young firms (the same two companies can rank opposite ways on different scalars), and a cross-check only — never the valuation, and never a recommendation.
- **Over-attachment.** Deliberately seek dissent from people who think least like you and fold it back in; you are "definitely wrong" — aim to be less wrong.
- **Optionality.** A platform's upside premium should be *modest* unless user loyalty, usage intensity and proprietary data genuinely support it — see [[real-options]] and [[value-per-user]].

## Related concepts
- [[failure-probability]] — the explicit survival-weighted blend that completes the equity bridge here
- [[valuing-high-growth]] — the next stage; growth fade, margin convergence and year-specific WACC
- [[value-per-user]] — the disaggregated cross-check for subscriber/user-driven young firms
- [[narrative-to-numbers]] — the "tell a story, then price it" discipline behind step 1
- [[dcf-foundations]] — the underlying intrinsic-value identity this adapts
- [[fcff]] — the firm-level cash flow being projected
- [[terminal-value]] — where most young-firm value sits
- [[uncertainty-in-valuation]] — simulating the ~6 key inputs instead of a single point
- [[big-market-delusion]] — the trap when the TAM × share story is over-optimistic
- [[pricing-game-vs-value-game]] — why the VC "target rate" method is pricing, not valuation

## Provenance
- Chapter notes: [[cap_10_valuing_young]]
- Sources: [The Zomato IPO: A Bet on Big Markets and Brilliant Managers?](https://aswathdamodaran.blogspot.com/2021/07/the-zomato-ipo-bet-on-big-markets-and.html), [The Bonfire of Venture Capital](https://aswathdamodaran.blogspot.com/2016/08/the-bonfire-of-venture-capital-good-bad.html), [The Dark Side of Valuation: Firms with No Earnings, No History and No Comparables (SSRN 1297075)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/HighGrow.pdf), [Valuing Young, Start-up and Growth Companies (SSRN 1418687)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1418687), [Tell Me a Story: Aswath Damodaran on Valuing Young Companies (CFA Institute)](https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/tell-me-a-story-aswath-damodaran-on-valuing-young-companies), [Zomato IPO valuation model](https://pages.stern.nyu.edu/~adamodar/pc/blog/ZomatoIPO.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch10.txt

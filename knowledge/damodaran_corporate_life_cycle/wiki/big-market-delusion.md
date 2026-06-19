---
concept: big-market-delusion
title: The Big Market Delusion
theme: Valuing young & high-growth firms
status: draft
---

# The Big Market Delusion

**What it is.** The systematic over-pricing that arises when a market is advertised as huge and scalable, drawing in many entrants who each — egged on by overconfident financiers — assume a large slice of the *same* market, so that the implied market shares summed across all of them far exceed 100% and the whole cohort is collectively overvalued until an inevitable correction.

## Core idea
"The market is big" is the single most dangerous phrase in a high-growth narrative. When a "big market promise" of easily scaled, highly profitable revenue is on offer, it attracts a crowd of contenders, and **both entrepreneurs and their financiers** (VCs and public-equity investors), each overconfident, assign their own firm a large share. The error is not in any single valuation — it is in the *aggregation*. Value each firm in isolation and every story looks defensible; add up the revenues all the contenders are implicitly forecasting and you find them claiming, in total, more of the market than exists. Initial over-pricing is therefore a *structural feature* of hot, big-TAM markets, not a coincidence, and it is followed by a correction back to earth.

The discipline against it is simple to state and easy to skip: translate your revenue forecast into an **implied market share**, then ask whether that share is plausible once rivals are *also* taking share. This is the same revenue check that anchors [[valuing-high-growth]] — and the reason a vendor-supplied "TAM" should be treated as a marketing number, not a fact.

## Across the life cycle
The delusion lives at the young / high-growth end of [[corporate-lifecycle]], where value rests on a future market rather than current cash flows, and where [[valuing-young-and-startups]] builds revenue top-down from TAM × share. The correction tends to recur in waves with named historical episodes at different stages of unwinding — dot-com retail (correction largely complete), online advertising (mid-unwind) and the cannabis market (delusion just beginning). For the analyst, the practical lesson is contrarian: the crowd's enthusiasm about a "hot" market is a reason for *more* skepticism, not less, and a single firm in such a market should never be valued in isolation from the implied collective share.

## Mechanics / formulas
**The implied-market-share check (the core discipline):**

```
Implied market share = Projected firm revenue ÷ Total addressable market (TAM)
```

Run it for *every* serious contender and sum:

```
Σ (implied shares across all contenders)  must be ≤ 100%
```

If the sum blows past 100%, the cohort is collectively pricing in an impossible market, and your own firm's forecast is almost certainly too high. The fixes:

- **Net out competition.** Anchor the revenue forecast to a *defensible* share after rivals take theirs, not a share that only works if everyone else fails.
- **Stress the TAM itself.** Vendor TAM claims are often inflated (a famous case split a headline "$3.4 trillion" market and labelled the "$1.4 trillion experiences" slice "more fictional than even aspirational"). Tag the TAM with its source and date and treat it as suspect.
- **Reverse the question.** Use a breakeven / reverse-DCF (see [[valuation-multiples]] and [[uncertainty-in-valuation]]): solve for the revenue, share or margin the *market price* is implying, then ask whether that share is plausible against competition.

## Pitfalls & nuances
- **Valuing in isolation.** A defensible standalone story can still be part of a collectively impossible market — always aggregate the implied shares.
- **Taking TAM at face value.** "TAM" is frequently the most aggressive number in a pitch; size it from a story with a source, don't import it.
- **Reading enthusiasm as confirmation.** In hot markets, broad agreement is a warning, not validation — the [[pricing-game-vs-value-game]] can keep a whole cohort overpriced for a while.
- **Forgetting the correction is *when*, not *if*.** Structural over-pricing in big-TAM markets reliably reverts; the timing is the only open question.
- **Compliance.** Flagging an implausible implied share is an analytical observation, not a short recommendation.

## Related concepts
- [[valuing-high-growth]] — where the implied-share check is a core modeling discipline
- [[valuing-young-and-startups]] — builds revenue from TAM × share, the very inputs this stresses
- [[uncertainty-in-valuation]] — scenarios and reverse-DCF to test the implied share against price
- [[narrative-to-numbers]] — "the market is big" is the story that most needs disciplining into numbers
- [[pricing-game-vs-value-game]] — why a whole cohort can stay overpriced before the correction
- [[valuation-multiples]] — EV/Sales and reverse-engineered multiples used to back out the implied share
- [[moat]] — a defensible share net of competition depends on a real competitive advantage

## Provenance
- Chapter notes: [[cap_11_valuing_high_growth]]
- Sources: [The Big Market Delusion: Valuation and Investment Implications (Cornell & Damodaran, FAJ 76(2), 2020; SSRN 3501688)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3501688), [FAJ article overview](https://www.tandfonline.com/doi/abs/10.1080/0015198X.2020.1730655), [The Sharing Economy Comes Home: An IPO of Airbnb](https://aswathdamodaran.blogspot.com/2020/12/the-sharing-economy-come-home-ipo-of.html), [Airbnb IPO valuation model](https://pages.stern.nyu.edu/~adamodar/pc/blog/AirbnbIPO.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch11.txt

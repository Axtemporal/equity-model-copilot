---
concept: failure-probability
title: Failure / Survival Probability
theme: Valuing young & high-growth firms
status: draft
---

# Failure / Survival Probability

**What it is.** An *explicit* probability that a young firm never reaches steady state — folded into value as a survival-weighted blend (`equity = going-concern value × p_survive + failure value × p_fail`) rather than being hidden inside an inflated discount rate.

## Core idea
Mature-company valuation quietly assumes the firm survives. Young, cash-burning firms break that assumption: there is a "substantial likelihood the firm may not make it." Damodaran's fix is to keep the cost of capital honest (reflecting *operating* risk only, near a diversified-investor level) and to charge for the chance of death *separately*, as a probability with an associated recovery value. This is the structural move that distinguishes the intrinsic [[valuing-young-and-startups]] method from the venture-capital habit of jamming both operating risk and failure risk into a single 50–70% "target return" with no transparent mapping of either.

The survival-weighted blend is a probability tree collapsed to two branches: with probability `p_survive` the firm reaches its modeled going-concern value; with probability `p_fail = 1 − p_survive` it is worth only its failure value (cash on hand, or a haircut to asset / going-concern value). The expected value is the weighted average.

## Across the life cycle
Failure probability is largest at the [[corporate-lifecycle]] start-up edge and falls as the firm clears each gate — a [[valuing-high-growth]] firm with a real revenue base and a cash buffer carries a much smaller probability, and a mature firm's is negligible (which is why mature DCFs omit it). The *declining*-firm analogue is **distress probability** — same blend mechanics, but driven by leverage and a deteriorating rating rather than cash burn — covered in [[distress-probability]] and [[valuing-declining-and-distressed]]. The decisive variable throughout is **access to capital**: a firm dependent on open capital markets to fund losses is far more fragile than one with a large cash balance and strong financing relationships.

## Mechanics / formulas
**The survival-weighted blend (the headline identity):**

```
Equity value (failure-adjusted)
  = (going-concern equity value × p_survive) + (failure value × p_fail)
  where p_survive = 1 − p_fail
```

Failure value is usually cash on hand, or a fraction of asset / going-concern value. The probability is an *input in its own cell* with method and source — not a plug.

**Setting the probability from cash burn (the runway logic):**

- `Cash burn rate` = cash consumed per period (persistent negative free cash flow).
- `Cash runway = cash reserves ÷ burn rate` — e.g. $1bn of cash at a −$500m/yr burn implies a ~2-year runway. A short runway plus weak capital access argues for a higher `p_fail`.

**The good / bad / ugly taxonomy** (how to read the burn before setting the number):

- **Good (benign):** a money-*making* business showing negative cash flow only because of large, *discretionary* reinvestment — throttleable if capital tightens; margins and reinvestment improve as growth scales. Lower `p_fail`.
- **Bad:** margins *deteriorating* despite scaling ("venture-capital hell") — cash flows negative indefinitely. Higher `p_fail`.
- **Ugly:** a money-*losing* firm that also reinvests very little — burning cash with no growth payoff. Highest `p_fail`.

Cash burn destroys value through three channels even short of failure: **dilution** (equity raised to fund burn cuts existing stakes), **lost growth** (when capital dries up, reinvestment is slashed), and **distress** (inability to fund operations risks liquidation and loss of going-concern value).

## Pitfalls & nuances
- **The cardinal error: cramming failure into the discount rate.** A VC-style 50%+ rate is an opaque catch-all; separate it so the cost of capital reflects only operating risk and the death risk is visible and defensible.
- **Treating failure value as zero by reflex.** Cash on hand and saleable assets give real recovery; the failure branch is rarely worth nothing.
- **Ignoring capital access.** Two firms with identical burn can carry very different `p_fail` depending on cash balance and the quality of their financing relationships.
- **False precision on the probability.** It is a judgement; pair it with [[uncertainty-in-valuation]] scenarios rather than presenting a single point as fact (compliance: label method and source, never present an estimate as data).
- **Double-counting.** If a discrete failure event is in the probability blend, do not *also* lift the discount rate for it — pick one home for each risk.

## Related concepts
- [[valuing-young-and-startups]] — the parent method this completes; the failure adjustment is its step 4
- [[distress-probability]] — the declining-firm cousin (leverage/rating-driven rather than burn-driven)
- [[valuing-declining-and-distressed]] — where the same survival-weighted blend reappears at the right edge of the arc
- [[cost-of-capital]] — kept honest precisely *because* failure is handled separately here
- [[fcfe]] — its sign (the cash-burn the runway measures) is what drives the probability
- [[uncertainty-in-valuation]] — ranges and simulation around the probability instead of a single point
- [[terminal-value]] — the going-concern value that the survival branch weights

## Provenance
- Chapter notes: [[cap_10_valuing_young]]
- Sources: [The Bonfire of Venture Capital: The Good, the Bad and the Ugly Side of Cash Burn!](https://aswathdamodaran.blogspot.com/2016/08/the-bonfire-of-venture-capital-good-bad.html), [The Zomato IPO: A Bet on Big Markets and Brilliant Managers?](https://aswathdamodaran.blogspot.com/2021/07/the-zomato-ipo-bet-on-big-markets-and.html), [The Dark Side of Valuation: Firms with No Earnings, No History and No Comparables (SSRN 1297075)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/HighGrow.pdf), [Valuing Young, Start-up and Growth Companies (SSRN 1418687)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1418687)
- Raw (gitignored): reference/damodaran_clc/text/Ch10.txt

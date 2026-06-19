---
concept: intrinsic-vs-relative-valuation
title: Intrinsic vs Relative Valuation (Value vs Price)
theme: Valuation foundations
status: draft
---

# Intrinsic vs Relative Valuation (Value vs Price)

**What it is.** The master distinction of valuation: *value* (what a business is intrinsically worth from its expected cash flows, growth and risk, estimated by discounted cash flow) and *price* (what the market will pay for it today, estimated by multiples and comparables) are two different things, produced by two different processes, driven by two different sets of forces — and conflating them is the root of most analytical confusion.

## Core idea

Damodaran's rule is to never use "value" and "price" interchangeably. They answer different questions and obey different drivers:

- **The value game** asks *what is this asset worth?* It is the domain of **intrinsic valuation / DCF**: value is the present value of expected future cash flows, discounted at a risk-adjusted rate. Its drivers are fundamentals — cash flows, the quality and quantity of growth, and risk. See [[dcf-foundations]].
- **The pricing game** asks *what will the market pay right now?* It is the domain of **relative valuation**: a number scaled to an observable metric (earnings, sales, book value, users) and benchmarked against comparable assets. Its drivers are behavioural — mood and momentum, liquidity, incremental news measured against expectations, and herd behaviour. See [[valuation-multiples]] and [[pricing-game-vs-value-game]].

Relative valuation does *not* try to estimate intrinsic worth at all; it trusts the market to price comparable assets right *on average*, even when it errs on individual names. The two numbers can diverge widely for the same asset at the same moment because they respond to different inputs. That gap is the source of both opportunity and risk — but it is *information about market mood*, not automatically a signal. The pricing game can reward firms that destroy value and punish firms that follow [[corporate-finance-first-principles]], which is precisely why the analyst must keep the two processes separate and explicit.

## Across the life cycle

Both processes apply at every stage, but the *weight* a rational analyst puts on each is **U-shaped** across the life cycle, and the pricing *metric* rotates with age:

- **Start-up / young:** pricing dominates — intrinsic DCF is hardest when there is no history. The market prices off potential market, capital access and users (EV/TAM, EV/subscribers, EV/forward sales). See [[valuing-young-and-startups]].
- **High growth → mature:** value dominates in the middle of the arc, where cash flows and history give DCF the most traction; metrics shift from EV/Sales toward PEG, forward PE.
- **Mature stable → decline:** pricing reasserts itself at the old end — PE, EV/EBITDA, and at the extreme book value or EV/liquidation value. See [[valuing-mature]] and [[valuing-declining-and-distressed]].

## Mechanics / formulas

There is no single formula — the distinction is procedural — but the two routes reduce to:

- **Intrinsic value** = Σ E(CF_t) / (1 + r)^t — fundamentals in, value out (the DCF identity; see [[dcf-foundations]]).
- **Price** = (chosen multiple) × (the firm's scaling metric), where the multiple is read off a peer group — comparables in, price out (see [[valuation-multiples]]).

The discipline that keeps them honest: run *both*, label each output for what it is, and treat the value-vs-price gap as an observation. When the gap is large, weigh three explanations honestly — you are wrong, the market is wrong, or both are wrong but one less so — and default to humility rather than to a trade.

## Pitfalls & nuances

- **Calling a pricing number a "value."** A target price from multiples is a *pricing* estimate, not intrinsic worth; presenting it as value imports the market's mispricing.
- **Assuming the gap is always an opportunity.** Price can stay detached from value for long stretches; momentum can override fundamentals indefinitely.
- **Mixing the two inside one model** — e.g. anchoring a DCF terminal value to a current trading multiple — quietly smuggles the pricing game into the value game.
- **Compliance:** the gap is analytical information about market sentiment, never a buy/sell recommendation.

## Related concepts

- [[dcf-foundations]] — the engine of the value game (the four inputs)
- [[valuation-multiples]] — the engine of the pricing game (multiples and their drivers)
- [[pricing-game-vs-value-game]] — momentum/multiples vs intrinsic value across stages
- [[narrative-to-numbers]] — the story+numbers discipline that anchors intrinsic value
- [[uncertainty-in-valuation]] — why an honest value still legitimately differs from price
- [[corporate-finance-first-principles]] — the first principles the pricing game can reward firms for ignoring

## Provenance
- Chapter notes: [[cap_09_valuation_101]]
- Sources: [Discounted Cashflow Valuations (DCF): Academic Exercise, Sales Pitch or Investing Tool?](https://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html); [January 2018 Data Update 10: The Price is Right!](http://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-10-price-is.html); [January 2019 Data Update 9: The Pricing Game](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-9-pricing-game.html); local papers valuesurvey.pdf, multiples.pdf
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt

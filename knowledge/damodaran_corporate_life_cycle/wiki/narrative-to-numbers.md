---
concept: narrative-to-numbers
title: Narrative to Numbers
theme: Valuation foundations
status: draft
---

# Narrative to Numbers

**What it is.** The discipline that a valuation is a marriage of a *story* (a coherent narrative about the business) and *numbers* (projections that translate the story into value): every assumption must trace back to a story element, and every story element must show up as a number, kept in a feedback loop so neither side drifts free of the other.

## Core idea

Value = story + numbers. Each half has its own appeal and its own failure mode:

- **Numbers** give a sense of precision and objectivity, but divorced from a story they are unanchored — they can be manipulated to justify a predetermined answer and have nothing to discipline them.
- **Stories** are memorable and emotionally resonant, but unconnected to numbers they drift into fairy tales and indefensible valuations.

The test of a valuation, Damodaran insists, is not in the inputs or the modelling mechanics but in the *story underlying the numbers* and how well that story holds up. The cure for each side's weakness is the other side: force every narrative claim through the arithmetic of a [[dcf-foundations|DCF]], and require every input cell to carry a narrative justification. A useful split is the storyteller vs the number-cruncher — most analysts lean one way, and the practical advice is to strengthen the weaker side and keep the two hemispheres in conversation.

## The story → input mapping

The connective tissue is an explicit chain from narrative claim to value driver:

| Story element | Value input it drives |
|---|---|
| Big market | Total addressable market → revenue level |
| Networking / winner-take-all | Market share |
| Strong, sustainable competitive advantage (a [[moat]]) | High share **and** high operating margin |
| Easy scaling | Low reinvestment per unit of growth (high sales-to-capital) |
| Tax breaks | Lower effective tax rate |
| Low risk | Lower discount rate (see [[cost-of-capital]]) |

Each row is bidirectional: a number with no story above it is unanchored; a story element with no number below it is untested.

## Across the life cycle

The narrative/numbers balance shifts systematically with age, and so does how widely investors disagree:

| Stage | Narrative vs numbers | The narrative question | Disagreement |
|---|---|---|---|
| Start-up | All narrative | How *big* is the story? | Huge, unconstrained |
| Young growth | Mostly narrative | How *plausible*? | Narrowing |
| High growth | Narrative + numbers | How *profitable*? | Constraints mount |
| Mature growth | Numbers + narrative | How *sustainable*? | Narrowing further |
| Mature stable | Mostly numbers | How *happy*? | Constrained |
| Decline | All numbers | — | Narrow |

For a young firm, the story is filtered through the **3P test** — is it *Possible*, *Plausible*, *Probable*? — and only probable elements may drive base-case numbers (see [[valuing-young-and-startups]]). Concrete illustrations of the shift: Amazon valued across optimistic/base/pessimistic narratives spanned roughly $32 to $468 per share — the *story*, not the modelling, drove the answer; Uber's value is narrative-dominated and wide, Coca-Cola's numbers-dominated and tight.

## Mechanics / discipline

Not a formula but a process:

1. Write a coherent business story addressing market, competition, margins, scaling, capital access and survival.
2. Map each story element to its value input (the table above).
3. Run the inputs through the DCF and read off the value.
4. Check both directions: every input has a story; every story claim has a number.
5. Track narrative *consistency* against management actions over time, and watch for "bar-mitzvah moments" when the market's focus flips from narrative credibility to delivered numbers.
6. Keep a **feedback loop**: solicit dissent from people who think least like you and fold it back into the story, rather than getting attached to your own narrative.

## Pitfalls & nuances

- **Numbers-only over-precision** — a polished model with no story is the easiest kind to manipulate.
- **Story-only fantasy** — an inspiring narrative with no numerical discipline produces fairy-tale valuations.
- **The big-market trap.** "The market is big" is the most dangerous phrase in a growth narrative; translate it into an *implied market share* and test plausibility (see [[big-market-delusion]]).
- **Over-attachment.** The feedback loop exists because analysts develop blind spots around their own stories; "you're definitely wrong — aim to be less wrong than everyone else."

## Related concepts

- [[dcf-foundations]] — the numbers engine the story is forced through
- [[valuing-young-and-startups]] — where the story dominates and the 3P test applies
- [[uncertainty-in-valuation]] — ranges and scenarios as honest expressions of a contested story
- [[big-market-delusion]] — the discipline against an untested "big market" story
- [[moat]] — the narrative element behind high share and margins
- [[cost-of-capital]] — the "low-risk" story shows up here
- [[intrinsic-vs-relative-valuation]] — the value game where story+numbers lives

## Provenance
- Chapter notes: [[cap_09_valuation_101]], [[cap_10_valuing_young]]
- Sources: [DCF Myth 2: A DCF is an exercise in modeling and number crunching (Aug 2015)](https://aswathdamodaran.blogspot.com/2015/08/dcf-myth-2-dcf-is-exercise-in-modeling.html); [Tell Me a Story: Aswath Damodaran on Valuing Young Companies (CFA Institute)](https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/tell-me-a-story-aswath-damodaran-on-valuing-young-companies)
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt, reference/damodaran_clc/text/Ch10.txt

---
chapter: 4
title: Transitions
block: Lead In
slides: reference/damodaran_clc/pdf/Ch4.pdf
status: draft
---

# Ch 4 — Transitions

## 1. Core thesis

The earlier chapters treated the life cycle as a *map of states* (start-up, young
growth, high growth, mature growth, mature stable, decline). Chapter 4 zooms into
the **moments between the states** — the transitions a firm must pass through to
move from one stage to the next — and argues that each transition is simultaneously
a **financial event** (how the firm raises or returns capital), an **operating
event** (what the business has to prove), and a **governance event** (who owns and
controls it, and how that ownership changes hands). Damodaran organizes the whole
chapter around four concrete capital-market mechanisms that *are* the transitions
for most companies: **(1) venture-capital financing** that carries a young firm
from idea to scalable business; **(2) the initial public offering (IPO)** that
takes a private firm public; **(3) seasoned equity offerings (SEOs)** by which an
already-public firm raises more equity; and **(4) private equity / LBOs and
activist buyouts** that can take a mature or declining public firm back into
private (or differently-controlled) hands. The recurring message is that the
*plumbing* of each transition — pre-/post-money pricing, VC protections,
underpricing, issuance costs, leverage — has its own economics and frictions, and
that the institutions that intermediate these transitions (VCs, investment bankers,
PE general partners) are themselves being disrupted. This chapter is the hinge
between the descriptive life-cycle arc of [[cap_01_unifying_theory]],
[[cap_02_basics]], [[cap_03_measures_determinants]] and the corporate-finance,
valuation and investing blocks that follow, because every transition is where the
investment, financing and cash-return decisions actually get made.

> source: Ch4.pdf p.1–2 (deck, primary); transition table p.2

## 2. Key concepts & frameworks

### 2.1 The transitions overlaid on the life-cycle curve
The chapter's opening diagram redraws the familiar revenue (green) / earnings
(red) curves and marks the six **transition gates** as vertical lines on the time
axis — the same milestones introduced in Ch.1 but now treated as the chapter's
subject rather than scenery:

- **The Lightbulb (idea) Moment** — entering start-up.
- **The Product Test** — start-up → young growth (does the idea become a product?).
- **The Bar Mitzvah** — young growth → high growth (does usage convert to a real,
  monetizable business? see §2.2 and the Twitter blog in §6.1).
- **The Scaling-up Test** — high growth → mature growth (can it scale profitably?).
- **The Midlife Crisis** — mature growth → mature stable.
- **The End Game** — mature stable → decline.

Below the curve, a three-row matrix classifies what changes at each stage along
three dimensions — and this matrix is the conceptual spine of the chapter:

| Growth stage | Financial transition | Operating transition | Governance transition |
|---|---|---|---|
| **Start-up** | Outside (VC / PE) funding | Idea → product | Sole founder → angel investors (capital) |
| **Young growth** | Going public (IPO) | Product → business | Established VC (more operating input) |
| **High growth** | Equity as "currency" (using shares to acquire/pay) | Small → large | Public investors (growth); founders firmly in control |
| **Mature growth** | Cash return & debt initiation | Growth on scale | Public investors (more conventional); founder control wavers |
| **Mature stable** | Seasoned financing (SEOs, refinancing) | Playing defense | Public investors (index funds, pension funds); founders / activists |
| **Decline** | Spin-offs & divestitures | Scaling down | Activist investors, vulture investors |

The table makes the chapter's thesis operational: as a firm ages, its *financing
act* migrates from VC → IPO → using equity as currency → initiating debt and cash
return → seasoned/refinancing → divestiture; its *operating act* migrates from
proving the idea to scaling to defending to shrinking; and its *ownership* migrates
from founder/angels → VCs → public growth investors → institutional investors →
activists and vultures. Applies across all stages by construction.

> source: Ch4.pdf p.2 (transition curve + 3-row matrix; read as zoomed image)

### 2.2 Transition 1 — Young-business financing via venture capital
The first deep-dive (slides 3–7) covers how young firms raise the outside capital
that the start-up/young-growth rows of the matrix call for. VC financing is
organized in **rounds**, each with a name and a purpose:

- **Pre-Seed & Seed** — usually the first capital a start-up raises; it funds the
  work of converting an *idea into a product*.
- **Series A** — funding of much greater magnitude than seed, for firms further
  along the idea-to-product transition.
- **Series B** — for businesses that are generally working on developing the
  business model and already have user/customer activity.
- **Series C** — for businesses that have a working business model and are
  *producing results* but need capital to **scale up**.

Four supporting concepts govern how these rounds work:

- **VC Terms** — in return for capital, VCs receive an ownership share of the firm,
  set by the *pricing* of the round.
- **VC Pricing** — VCs price young firms off **activity metrics** (users,
  downloads, subscribers) or multiples of *forward* revenues/earnings, because
  trailing earnings are usually negative or non-existent (this is the pricing-vs-
  valuation distinction Damodaran stresses throughout the book — see §3).
- **VC Rounds** — a growing firm can raise multiple rounds, each at a *different*
  (usually higher) price as it de-risks.
- **VC Up & Down Rounds** — a new round priced *higher* than the prior one is an
  **up round**; priced *lower* is a **down round**. Down rounds can retroactively
  alter the terms of earlier rounds (via the protections in §2.3).

> source: Ch4.pdf p.3 (VC stages + terms boxes), p.5 text

### 2.3 Pre-money vs. post-money, and VC downside protections
Two refinements VCs use:

- **Pre-money vs. post-money pricing.** *Pre-money* is the firm's pricing **before**
  the VC's cash goes in; *post-money* is the pricing **after** the infusion. The
  relation is mechanical but judgment-laden: if you start from an existing pricing,
  **post-money = pre-money + capital infused**; conversely, the VC's own pricing of
  the deal is usually treated as a *post-money* figure, and **pre-money =
  post-money − capital provided**. Which estimate you call which matters because the
  founder's retained ownership percentage falls out of it.
- **VC protections.** Because VCs want upside but fear the downside, many deals
  embed contractual protection against ownership loss — most importantly,
  mechanisms (e.g., anti-dilution / ratchet provisions) that **re-adjust earlier
  VCs' ownership shares when a later down round prices the firm lower**, shifting
  the dilution pain onto founders and unprotected holders rather than the protected
  VC. This is the governance teeth behind the "down rounds can alter prior terms"
  point in §2.2.

> source: Ch4.pdf p.5 (text slide, "With Special Features")

### 2.4 The VC pricing-and-target-return mechanism
Slide 4 lays out, as a flow chart, exactly *how* a VC arrives at a price today
("pricing today") for a firm with little or no current revenue:

1. **Today** — the firm is a young company/start-up with a product or idea but no
   (or trivial) revenue.
2. **Exit Year (Year n)** — the VC forecasts revenues or earnings in some future
   exit year and applies a **multiple** (based on what acquirers/markets pay for
   comparable companies *today*) to get an **estimated exit pricing**:
   *Pricing in year n = (Revenues in year n) × Multiple.*
3. **Target Rate of Return** — the VC discounts that exit pricing back to today at
   a high **target rate of return** (or, equivalently, computes the IRR implied by
   investing today and exiting at the year-n value and compares it to the target).
4. The VC also flags **worries/concerns**: many young firms don't make it, and
   cash burn forces further equity infusions (and dilution).

The slide then gives the *levers* and their direction:
- To get a **lower** pricing today: project lower year-n revenues/earnings, use a
  lower exit multiple, and/or use a **higher** target return.
- To get a **higher** pricing today: project higher revenues/earnings, use a higher
  multiple, and/or use a **lower** target return.

This is the practical engine behind "VC pricing" and a clean illustration of
Damodaran's pricing-vs-valuation distinction: it is a *relative* (multiple-based)
exercise discounted at a hurdle rate, not an intrinsic DCF.

> source: Ch4.pdf p.4 (flow chart; read as zoomed image)

### 2.5 How VC has evolved (the four trends)
Slides 6–7 chart VC funding over time and name four structural trends:

- **Funding over time / cyclicality.** VC capital scaled in the 1990s, fell sharply
  after the dot-com bust (the deck notes capital fell from ~$100bn in 2000 to ~$40bn
  by 2002–03), was hit again by the 2008 crisis, and then surged — with the unicorn
  era seeing VC- and M&A-funded "unicorns" (private firms valued > $1bn) numbering in
  the hundreds by the early 2020s (the deck cites > $1bn-plus exits in the hundreds).
  Takeaway: **VC is intensely cyclical and tied to the macro/market cycle.**
- **Globalization.** Historically U.S.-centered, VC is now globally accessible,
  though access still varies by geography.
- **Investor make-up.** Once purely institutional, VC has opened to individual and
  retail investors, enabled by technology (platforms, syndication).
- **Corporate venture capital (CVC).** CVC flows have risen over two decades for two
  reasons: (i) in health care and tech, mature companies find it **more efficient to
  invest in promising young companies than to spend the same money on internal R&D**;
  and (ii) the cash-rich winners of those sectors have unprecedented balance-sheet
  cash to deploy across many start-ups.

> source: Ch4.pdf p.6 (chart, read as image), p.7 (text slide "And Trends")

### 2.6 Transition 2 — Going public (the IPO) and its costs
Slide 8 frames the IPO decision: ambitious firms consider going public when **public
markets offer better pricing terms** and the **need for liquidity** (for founders,
VCs and employees to cash out) is higher. But going public carries at least two
costs that must be weighed:

1. **Heavier disclosure** — public-market information-disclosure requirements are
   far more onerous than for private firms.
2. **Short-termism / expectations treadmill** — the pressure to **match or beat
   investor expectations** every quarter (or half-year) on metrics like user
   numbers, revenues and earnings adds management stress and can, in some cases,
   drive decisions that damage the firm long-term.

> source: Ch4.pdf p.8 (text slide, "2. Public Equity — Initial Public Offerings")

### 2.7 The three going-public routes
Slides 9–11 contrast three mechanisms for going public, each as a process diagram:

- **The banker-led IPO (Figure 4.6).** The traditional route. The *issuing company*
  chooses to go public, picks a lead investment banker who assembles a **syndicate**,
  files a prospectus stating how much it will raise and how it will use the
  proceeds, then bankers set a preliminary price, test it with investors, fix the
  final offering price and share count, run a **roadshow**, and on the offering date
  the shares start trading at a market-clearing price; post-offering the bankers
  provide after-market support. The *banker's role* spans **timing** (finding the
  window), **filing & offering details** (writing the prospectus, sizing the
  offer), **pricing** (framing the metric/peer group and gauging demand, fine-tuning
  to keep issuer and investors "happy"), **selling/marketing**, a **price guarantee**
  (if the market opens below the offer price, deliver the guaranteed price), and
  **after-market support** (buying shares if needed; favorable research). Each of
  these claimed services is exactly what the "Disrupting the IPO" critique (§6.2)
  attacks.
- **The direct listing (Figure 4.7).** The firm goes public **without bankers /
  underwriting**: it files a prospectus (history + story + prospects), managers run
  a roadshow, and shares start trading at a market-set clearing price. Its
  **limitations**: it *still takes too long* (cutting bankers doesn't shorten the
  pre-IPO timeline); a *disclosure drag* (a full prospectus with all legal/
  regulatory requirements is still needed); *market skepticism* for low-profile
  names that lack a "trusted" underwriter's affirmation; and *capital restrictions*
  — historically the cash raised could not be held to fund future needs (i.e.,
  classic direct listings raised **no fresh capital**, only enabled existing holders
  to sell). Suits large, well-known firms (Spotify, Slack).
- **The SPAC route (Figure 4.8).** A **Special Purpose Acquisition Company** raises
  capital in its own IPO ("blank check"), finds a target, provides target financials
  + story for SPAC-shareholder approval, negotiates the merger price and any
  additional **PIPE** capital, and then the combined entity trades publicly.
  *Pluses*: **timing advantage** (the SPAC is already cash-ready, so the deal can
  move when the window is open), **expert "due diligence"** (sponsors specialize in
  the target's business, in principle improving pricing), **investor outsourcing
  with escape hatches** (SPAC investors outsource diligence but can opt out before
  the deal closes), and **capital access** (targets keep capital raised and can tap
  additional capital). *Minuses*: **costly** (benefits must be large enough to cover
  subsidizing the sponsor's promote and deal costs); **disclosure concerns** (claims
  about targets that wouldn't meet regular-IPO standards); **sponsor self-dealing**
  (sponsors control the process and have incentives to do *any* deal); and a
  structural **investor-vs-issuer** conflict (deals good for the issuer on timing/
  price can be bad for the SPAC's own investors).

> source: Ch4.pdf p.9 (Fig 4.6 banker IPO), p.10 (Fig 4.7 direct listing), p.11 (Fig 4.8 SPAC); all read as zoomed images

### 2.8 IPO trends over time
Slides 12–13 chart IPO **volume** (number of offerings and aggregate proceeds) and
the **characteristics** of the companies going public. The narrative arc Damodaran
draws: IPO activity is **cyclical** (waves tied to bull markets and hot sectors),
and over recent decades the **typical IPO company has changed** — firms come public
**older, larger, and more often unprofitable**, with revenues rising over the period
but profitability of the IPO cohort drifting *down* (the red profitability line
falls while the revenue bars rise on Fig 4.10). This is the empirical counterpart to
the life-cycle point that firms now stay private longer (financed by ever-larger VC
rounds) and only go public well into high/mature growth. Cross-link the staying-
private-longer dynamic to [[cap_02_basics]] and [[cap_03_measures_determinants]].

> source: Ch4.pdf p.12 (IPO volume chart), p.13 (Fig 4.10 IPO revenues vs. profitability)

### 2.9 Transition 3 — Seasoned equity offerings (SEOs)
Slides 14–16 treat the *already-public* firm raising **more** equity. The framing
chart (Fig 4.11) contrasts **external vs. internal financing** at U.S. firms: mature
firms fund most of their needs internally, with external equity issuance a smaller,
cyclical slice. The chapter's analytical payload here is **issuance costs**:

- **Cost by issue size (Fig 4.12).** Issuance costs (as a % of proceeds) for both
  debt and equity **fall sharply with issue size** — small issues are
  disproportionately expensive (a fixed-cost / economies-of-scale effect), and
  **equity issues cost more than debt issues** at every size band.
- **Cost by offering method (Fig 4.13).** Comparing **general (underwritten) cash
  offers, rights offerings (with/without standby underwriting), and pure rights
  issues**, the *pure rights issue* is the **cheapest** way to raise equity, yet
  U.S. firms overwhelmingly use the more expensive underwritten cash offer — a
  standing puzzle ("the rights-offering paradox"). This feeds Damodaran's "right
  offering route?" question: the cheapest method is underused for institutional/
  agency reasons.

> source: Ch4.pdf p.14 (Fig 4.11 external vs internal), p.15 (Fig 4.12 cost by size), p.16 (Fig 4.13 cost by method)

### 2.10 Transition 4 — Private equity, LBOs and activist targeting
Slides 17–20 cover the **reverse** transition: taking a mature/declining public
firm private (or shaking up its control).

- **Typical PE targets (Fig 4.9 / 4.14).** PE buyers prefer **mature or declining**
  public companies that have **predictable cash flows and are under-levered**
  relative to what their EBITDA could support — i.e., firms whose cash flows can
  service a lot of new debt. The deck's bar charts show acquisition targets cluster
  in particular EBITDA/percentile bands (cash-flow-rich, debt-capacity-rich names).
- **The PE process (Fig 4.15).** Two pie charts make it vivid. *Before*: a mature/
  declining public company is ~96% public, with a sliver held by insiders. *After*:
  the firm's capital is reconstituted as roughly **Insiders 15% / PE LP equity 20%
  / PE GP equity 25% / Borrowed (debt) 40%** — i.e., the general partners raise
  equity from limited partners, **borrow the rest** (the L in LBO), buy out the
  public holders, and **get key managers to buy in as equity investors** in the
  newly "privatized" company (aligning management incentives).
- **The PE timeline (Fig … / p.19).** Three steps and their risks: (1) a *"Public"
  company is acquired* with a mix of debt and equity and taken private — risks:
  **wrong target** and **paying too high a price**; (2) it is *run as a private
  company* with changes to asset mix and operations, while PE investors supply
  "management" and "strategic" input and collect **management fees and residual cash
  payouts** — risks: the business model fails or the economy weakens, **asset sales
  disappoint**, or there is **too much debt**; (3) the *"fixed" company is taken back
  public or sold* to a public company, with PE selling its equity stake at market
  prices — risk: **market/sector weakness leads to poor exit values.** The whole
  model lives or dies on the exit.
- **PE trends (p.20).** Three: **bigger deals** (more capital flowing in → bigger
  buyouts), **globalization** (PE, like VC and IPOs, has gone from a mostly-U.S.
  phenomenon to global), and **flexibility on leverage** (early buyouts were almost
  always leveraged — hence "LBO" — but PE now varies its debt use rather than
  always maximizing it).

Activist investors and vulture investors (the decline-row of the §2.1 matrix) are
the milder cousins of the full buyout: they take stakes in mature/declining public
firms to force changes in capital allocation, cash return, or strategy.

> source: Ch4.pdf p.17 (Fig 4.9/4.14 targets), p.18 (Fig 4.15 PE process pies), p.19 (PE timeline), p.20 (PE trends text + value chart)

## 3. Metrics, formulas & rules of thumb

- **Post-money / pre-money identity.**
  `Post-money pricing = Pre-money pricing + Capital infused`, and equivalently
  `Pre-money pricing = Post-money pricing − Capital provided`.
  Founder's retained ownership ≈ `Pre-money / Post-money`; the new investor's stake
  ≈ `Capital infused / Post-money`. (Ch4.pdf p.5)
- **VC exit-and-discount pricing.** Forecast exit-year metric, apply a market
  multiple, discount at a target return:
  `Pricing today = (Revenuesₙ × Exit multiple) / (1 + target return)ⁿ`, or compare
  the **IRR** from `(invest today → exit value in year n)` to the target return.
  Levers: lower price ← lower forecast / lower multiple / **higher** target return;
  higher price ← the reverse. (Ch4.pdf p.4)
- **Up round vs. down round.** A round priced above (below) the prior round is an
  up (down) round; down rounds can trigger anti-dilution protections that reprice
  prior rounds. (Ch4.pdf p.3, p.5)
- **IPO underpricing rule of thumb.** The median IPO pops ~**15%** on day one
  (banker-led model); extreme examples cited in the companion blog: Beyond Meat
  +84%, Zoom +72% (Zoom's pop ≈ $250–300m "left on the table"). Underwriting
  **gross spreads run ~3–8% of proceeds**, higher for smaller deals. (Blog §6.2;
  Ritter data §5)
- **Issuance-cost rules of thumb.** Issuance cost (% of proceeds) **falls with
  issue size** and is **higher for equity than for debt**; **pure rights issues are
  the cheapest** equity-raising method, underwritten cash offers among the dearest.
  (Ch4.pdf p.15–16)
- **PE post-buyout capital mix (illustrative).** ≈ **Debt 40% / GP equity 25% / LP
  equity 20% / management 15%** — i.e., majority equity but with leverage the
  defining feature; target firms chosen for **stable cash flow + spare debt
  capacity**. (Ch4.pdf p.18)
- **First-day return categories / underwriter reputation** are tabulated in Ritter's
  datasets (§5) and serve as empirical benchmarks for any IPO assumption.

> source: Ch4.pdf p.3–6, p.15–16, p.18; blog §6.2; Ritter §5

## 4. Examples & cases

- **Twitter** — Damodaran's worked "Bar Mitzvah" case: a social-media firm forced to
  shift from being valued on *user growth* to being valued on *monetization*. He
  judged its ~$41.85 (Nov 2014) price to require improbable revenue (CFO Anthony
  Noto projected ~$14bn by 2024, vs. Damodaran's implied ~$30–40bn break-even), and
  criticized management for tailoring its story to equity analysts and leaning on
  "adjusted EBITDA." Illustrates the young-growth → high-growth scaling-up gate.
  (Blog §6.1)
- **Beyond Meat (+84%), Zoom (+72%)** — extreme IPO-day pops illustrating
  underpricing and the wealth transfer from issuers to flippers. (Blog §6.2)
- **Uber** — its IPO generated ~$105m in banker fees (≈70% to Morgan Stanley);
  Damodaran's example of fee economics and a household-name issuer whose brand
  exceeded its underwriters'. (Blog §6.2)
- **WeWork** — the 2019 failed IPO; the archetype of banker mispricing, where the
  price was set first and investors hunted for afterward. (Blog §6.2)
- **Spotify, Slack** — direct-listing pioneers; large, well-known firms that skipped
  underwriting. (Slides p.10; blog §6.2)
- **Google** — auction-IPO reference (an alternative the market largely declined to
  adopt). (Blog §6.2)
- **Toys "R" Us** — recurring PE cautionary tale in the wider literature: a 2005 LBO
  loaded the firm with ~$5.3bn of debt, ending in bankruptcy and ~31,000 job losses
  — the "too much debt / poor exit" risks of the PE timeline made concrete. (NYT-PE
  theme via §6.5)
- **Unicorns** — private firms valued > $1bn; the deck uses their proliferation in
  the late-2010s/early-2020s to show firms staying private longer on ever-larger VC
  rounds. (Slides p.6)

> source: Ch4.pdf p.4, p.6, p.10; blogs §6.1–6.2; §6.5

## 5. Data & tools

Chapter 4 is institution/mechanism-focused; its quantitative backbone lives in two
external datasets rather than a Damodaran industry `.xls`:

- **Jay Ritter's IPO data** (Univ. of Florida, Warrington) —
  <https://site.warrington.ufl.edu/ritter/ipo-data/>. The canonical empirical source
  for IPO **volume** and **underpricing** (first-day returns) 1975–present: annual
  IPO counts and proceeds, average/median first-day returns, first-day-return
  categories by offer-price revision, long-run post-IPO returns (through 2012),
  founding dates (1975–2025), VC-backed vs. non-VC IPOs, SPAC and direct-listing
  tabs, underwriter-reputation rankings (1980–2025), gross spreads, dual-class
  tallies, SEO data (1970–2015), and cross-country underpricing for 55 countries
  (incl. **Brazil**). Catalog only; raw Excel not copied.
- **NVCA Yearbook** (National Venture Capital Association) —
  <https://nvca.org/nvca-yearbook/>. Annual U.S. VC industry statistics: number of
  active firms, deal counts and dollars invested (e.g., 2023: 3,417 firms, 13,608
  deals, **$170.6bn** invested; **$66.9bn** raised across 474 funds; ~$311.6bn dry
  powder; ~$1.21tn AUM; first-time financings down to $7.8bn), by stage
  (seed/early/late) and by exit channel (IPO / M&A). The empirical source for §2.2
  and §2.5's VC-funding trends.
- **NYT "Private Equity" topic** — <https://www.nytimes.com/topic/subject/private-equity>
  (paywalled; not fetched). Ongoing journalistic coverage of LBOs, take-privates,
  fees, debt loading and bankruptcies — the qualitative counterweight to the PE
  process diagrams.

No dedicated Damodaran tool spreadsheet is tied to Ch.4 (the VC/IPO valuation
spreadsheets surface in [[cap_10_valuing_young]] and [[cap_11_valuing_high_growth]]).

## 6. Supplementary readings — distilled

### 6.1 Blog — "Twitter's Bar Mitzvah! Is social media coming of age?" (Nov 2014)
*Read in full via WebFetch.* Damodaran uses the "Bar Mitzvah" metaphor for the
moment a young-growth company is forced to **grow up**: markets stop rewarding
surface growth (user/subscriber counts) and start demanding *operating substance* —
evidence that **usage converts to revenue and revenue to profit**, with "numbers
driving narrative" rather than the reverse. Twitter is his case: at ~$41.85
(Nov 2014) the price implied break-even revenues far above CFO Anthony Noto's
~$14bn-by-2024 guidance (Damodaran's math implied ~$30–40bn). He flags three
monetization headwinds for social media — uncertain ad effectiveness, a *finite*
online-ad market (projected $209–323bn by ~2023, shared across all players), and
competition that increasingly takes share from rivals rather than expanding the pie
— and criticizes the CFO for pitching to equity analysts and dressing up "adjusted
EBITDA." **What it adds beyond the slides:** it puts flesh on the abstract "Bar
Mitzvah / scaling-up" transition gate and shows the *volatility* a stock suffers
while investors argue over old vs. new metrics during the crossover. Cross-link
[[cap_02_basics]], [[cap_10_valuing_young]].
> source: https://aswathdamodaran.blogspot.com/2014/11/twitter-bar-mitzvah-is-social-media.html

### 6.2 Blog — "Disrupting the IPO Process: Challenging the Banker-run Model" (Oct 2019)
*Read in full via WebFetch.* A frontal attack on the **banker-led IPO**. The core
claim: market conditions have eroded the value of the six services bankers claim to
provide, while their costs persist. Underpricing transfers wealth from issuers to
first-day flippers — median first-day pop ~15%, extremes like Beyond Meat (+84%) and
Zoom (+72%, ≈$250–300m left on the table) — on top of **3–8% gross spreads** (Uber:
~$105m of fees, ~70% to Morgan Stanley). He dismantles each banker service —
**timing** (no one times markets; 2019's IPO stumbles proved it), **prospectus**
(boilerplate), **pricing** (WeWork as the disaster case; price set first, investors
sought after), **marketing** (post-2008 banks lack credibility; issuers like Uber
out-brand their underwriters), the **price guarantee** (hollow when the price is
deliberately set 15–20% low), and **after-market support** (infeasible for
multi-billion-dollar deals). Alternatives: **direct listings** (Spotify, Slack — no
underwriting, no lock-up, no artificial underpricing, but no fresh capital and only
for big names) and **auctions** (Google — underused). Recommendations: cash-rich,
high-profile firms should direct-list; if using bankers, tie fees to pricing
quality; investors should pick the value or the pricing game and stay flexible.
**What it adds beyond the slides:** it supplies the *critique* behind the three-route
comparison in §2.7 — the slides describe the routes neutrally; the blog argues *why*
the banker model is being disrupted. Cross-link [[cap_06_investing]].
> source: https://aswathdamodaran.blogspot.com/2019/10/disrupting-ipo-process-challenging.html

### 6.3 Reading — "Disrupting the Disruptors? The 'Going Public Process' in Transition" (Damodaran, SSRN 3892419, Jul 2021)
*Abstract-only — SSRN returned HTTP 403 on both the abstract page and the short
link; full text not retrieved; authorship/title/date confirmed via web search.* This
is Damodaran's own **academic formalization of the §6.2 blog**: a paper-length
treatment of how the going-public process is in transition, arguing that the
traditional banker-intermediated IPO is being challenged by **direct listings,
SPACs, and broader retail access**, and re-examining the empirical case on IPO
**underpricing**, banker fees, and the (dis)value of underwriter services across the
changing market structure. **What it adds beyond the slides:** it is the scholarly
backbone for the IPO-route material in §2.6–2.8, with the same thesis as the blog
but with citations and data; treat the §6.2 distillation as the faithful proxy until
the full PDF can be retrieved from SSRN's download button.
> source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3892419 (403 — abstract not fetchable; distilled from confirmed metadata + the parallel §6.2 blog)

### 6.4 Reading — NVCA Yearbook (National Venture Capital Association)
*Page read via WebFetch; underlying yearbook is a downloadable PDF, not parsed in
full.* The yearbook is the authoritative annual statistical portrait of U.S. venture
capital: industry size, capital invested, fundraising, deal counts, stage mix
(seed/early/late) and exits (IPOs and M&A). Headline 2023 figures (2024 edition):
3,417 active firms; 13,608 deals; **$170.6bn invested**; **$66.9bn raised** across
474 funds; record ~$311.6bn dry powder; ~$1.21tn AUM; first-time financings down to
$7.8bn (lowest since 2017) with insider-led rounds at decade highs (a caution
signal). **What it adds beyond the slides:** it converts §2.2/§2.5's qualitative VC
narrative into hard, current numbers — the empirical base for any VC-funding or exit
assumption, and direct evidence of the cyclicality and "stay-private-longer" trends.
> source: https://nvca.org/nvca-yearbook/

### 6.5 Reading — NYT "Private Equity" topic page
*Not retrieved — nytimes.com is blocked to this agent (WebFetch + WebSearch both
refused the domain); themes distilled from secondary coverage and the chapter's own
PE slides.* The NYT topic hub aggregates ongoing journalism on private equity, whose
recurring themes are the standard critiques: **leveraged buyouts** funded mostly by
debt (~70% borrowed), **fees and asset-stripping** that drain target companies,
**elevated bankruptcy risk** for PE-owned firms (multiple studies cited put default
rates well above non-PE peers), and **harm to workers and pensions** (Toys "R" Us:
~$5.3bn LBO debt → bankruptcy → ~31,000 jobs). **What it adds beyond the slides:**
it is the *critical* counterweight to Damodaran's neutral PE-process diagrams (§2.10)
— the slides explain *how* PE works; this coverage documents *when and why it goes
wrong* (the "too much debt / wrong target / poor exit" risks the timeline lists).
> source: https://www.nytimes.com/topic/subject/private-equity (domain blocked — distilled from secondary sources incl. pestakeholder.org, PBS NewsHour, U.S. Senate JEC report)

## 7. Takeaways for valuation & modeling

For an equity analyst building standardized models (raw material for
[[application_to_copilot]]):

1. **Model the transition, not just the state.** A firm sitting at a gate (about to
   IPO, just IPO'd, an LBO target) is mid-transition, and its near-term financials
   are dominated by the *mechanics* of that transition — fresh equity in (IPO/SEO),
   a debt load slammed on (LBO), dilution from a new VC round. The copilot's
   life-cycle classifier (from [[cap_01_unifying_theory]]) should detect a pending
   or recent transition and switch the relevant model section into "transition mode"
   (e.g., add the IPO cash injection and share-count jump; re-lever the balance
   sheet for a buyout).

2. **Pricing vs. valuation for young/transitioning firms.** Where a firm is priced
   off VC-style multiples of forward revenue/users discounted at a high target
   return, the model should make that *pricing* logic explicit and **separate** from
   any intrinsic DCF — and tag every such input with method + source (compliance
   rule). Do not present a VC-style relative price as an intrinsic value.

3. **Capital-structure & share-count discontinuities are forecast events.** IPOs and
   SEOs raise the share count and the cash balance; LBOs/take-privates raise debt and
   cut the float; down rounds and anti-dilution provisions reshuffle ownership. These
   are step-changes, not smooth trends — the debt schedule, share-count line and
   equity/cash plugs must handle a discrete jump at the transition period rather than
   interpolating through it. (Direct tie-in to backlog items 2 and 4 — dynamic debt
   and shares-outstanding inputs.)

4. **Issuance and underpricing are real costs to net out.** When a model assumes the
   firm funds itself with new equity or debt, deduct **issuance costs** (higher for
   equity, higher for small issues; cheapest via rights issues) and, for IPOs, the
   **underpricing discount** (~15% median day-one pop) — the firm nets the offer
   price, not the post-pop market price. These belong in their own assumption cells,
   sourced to Ritter/empirical data, never buried in a formula.

5. **LBO/PE lens for mature, cash-rich, under-levered firms.** A mature firm with
   stable cash flow and spare debt capacity is a structural buyout candidate; an LBO
   "stress test" (can the cash flows service ~40%+ debt and still exit?) is a useful
   sanity check on a mature-firm valuation and on its optimal capital structure — and
   the PE-timeline risks (wrong target, too high a price, too much debt, weak exit)
   double as a downside-scenario checklist. Feeds the bull/base/bear scenario design
   for mature pilots.

6. **"Stay private longer" reshapes the comparable set.** Because firms now IPO older,
   larger and often unprofitable, the public comparable universe for a young company
   is sparse and biased — be explicit that early-stage assumptions lean on private/VC
   data (NVCA, Ritter VC-backed tabs) rather than clean public comps, and flag the
   resulting uncertainty rather than over-fitting to a thin peer group.

> source: synthesis of Ch4.pdf p.2–20 + blogs §6.1–6.2 + readings §6.3–6.5

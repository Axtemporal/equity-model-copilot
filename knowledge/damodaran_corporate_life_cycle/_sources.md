# Sources — Damodaran "The Corporate Life Cycle"

Master bibliography for the knowledge base, organized by chapter. Origin page:
<https://pages.stern.nyu.edu/~adamodar/New_Home_Page/CLC.htm> (companion site to
the book *The Corporate Life Cycle: Business, Investment, and Management
Implications*, Aswath Damodaran, Penguin/Portfolio, 2024).

**Local raw material** (gitignored, under `reference/damodaran_clc/`):
- `pdf/ChNN.pdf` — slide decks. `text/ChNN.txt` — extracted text. `img/ChNN/pNN.png` — page renders (use when text extraction is sparse, e.g. Ch4–Ch9).
- `pdf/{realopt,costofcapital,valuesurvey,multiples}.pdf` + matching `.txt` — Damodaran papers downloaded in full.
- Datasets (`.xls`) are **not** downloaded — cataloged here by URL (raw industry data, not prose to distill).

Blog posts and external readings are HTML → fetch live with WebFetch. SSRN links
are abstract pages (abstract is fetchable; full PDF may require the SSRN
download button — note "abstract-only" if full text is unavailable).

---

## Block: The Lead In

### Ch1 — A Search for a Unifying Theory
- Slides: `pdf/Ch1.pdf` · webcast: <https://youtu.be/vg6H9248onQ>
- Blog: "A Return to Teaching: The Spring 2023 Edition" (Dec 2022)
- Readings: Adizes Corporate Lifecycle article · "Business Life Cycle: Five Stages" (Corporate Finance Institute)

### Ch2 — The Basics of the Corporate Life Cycle
- Slides: `pdf/Ch2.pdf` · webcast: <https://youtu.be/2sC-szm7tfE>
- Blogs: "A Viral Market Update XIII: The Strong (FANGAM) get stronger!" (Aug 2020) · "Back to Earth or Temporary Setback? Revisiting the FANGAM stocks" (Feb 2022)
- Readings: "Research: The average age of a successful start-up founder is 45" (HBR, Jul 2018)
- Data: New business formations US <https://www.census.gov/econ/bfs/data.html> · Failure rates US businesses <https://www.bls.gov/bdm/bdmage.htm>

### Ch3 — Measures and Determinants
- Slides: `pdf/Ch3.pdf` · webcast: <https://youtu.be/x7dbavHECfc>
- Blog: "Aging in Dog Years: The Short, Glorious Life of a Successful Tech Company" (Dec 2015) <https://aswathdamodaran.blogspot.com/2015/12/aging-in-dog-years-short-glorious-life.html>
- Readings: "Why Japan is home to the world's oldest businesses" (Nov 2023) · "Kongo Gumi: The Enduring Legacy of Japan's Oldest Company" (Oct 2023)
- Data: Historical growth rates by industry — US <https://pages.stern.nyu.edu/~adamodar/pc/datasets/histgr.xls> / Global <.../histgrGlobal.xls> · Operating margins — US <.../margin.xls> / Global <.../marginGlobal.xls>

### Ch4 — Transitions
- Slides: `pdf/Ch4.pdf` · webcast: <https://youtu.be/erRg4CL13VM>
- Blogs: "Twitter's Bar Mitzvah: Is social media coming of age?" (Nov 2014) · "Disrupting the IPO Process: Challenging the Banker-run Model" (Oct 2019)
- Readings: National Venture Capital Yearbook <https://nvca.org/nvca-yearbook/> · NYT private equity topic <https://www.nytimes.com/topic/subject/private-equity> · "Disrupting the Disruptors? The Going Public Process in Transition" SSRN 3892419
- Data: Jay Ritter's IPO data <https://site.warrington.ufl.edu/ritter/ipo-data/>

## Block: Corporate Finance

### Ch5 — Corporate Finance 101: A Life Cycle Perspective
- Slides: `pdf/Ch5.pdf` (image-heavy — use `img/Ch5/`) · webcast: <https://youtu.be/dkstj88dw1E>
- Blogs: "Corporate Finance 101: A Big Picture, Applied Class" (Jan 2016) · "Data Update 5 for 2022: The Bottom Line" (Feb 2022)
- Readings: "Living with noise: Investing and Valuation in the face of uncertainty" SSRN 2323621 · Online corp finance class <https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastcfonline.htm>

### Ch6 — Investing across the Life Cycle
- Slides: `pdf/Ch6.pdf` (image-heavy — use `img/Ch6/`) · webcast: <https://youtu.be/Tf-VW0XiQtM>
- Blogs: "A Viral Market Update X: A Corporate Life Cycle Perspective" (Jun 2020) · "Earnings and Cashflows: A Primer on Free Cash Flow" (Oct 2022) · "Decline and Denial: Blackberry End game and Microsoft as a Value Trap" (Sep 2013) · "Data Update 5 for 2024: Profitability" (Jan 2024)
- Papers (full local): `pdf/realopt.pdf` ("The Promise and Peril of Real Options") · `pdf/costofcapital.pdf` ("Cost of capital: The Swiss Army Knife of Finance")
- Readings: Morgan Stanley "ROIC and the Investment Process" <https://www.morganstanley.com/im/publication/insights/articles/article_roicandtheinvestmentprocess.pdf> · HBR "Making real options really work" <https://hbr.org/2004/12/making-real-options-really-work> · "Return on capital, ROIC and ROE" SSRN 1105499
- Data: Cost of capital — US <.../wacc.xls> / Global <.../waccGlobal.xls> · Return on capital — US <.../mgnroc.xls> / Global <.../mgnrocGlobal.xls> · Excess returns — US <.../EVA.xls> / Global <.../EVAGlobal.xls>
- Tools: wacccalculator.xlsx · returncalculator.xls · expand.xls (all under <https://pages.stern.nyu.edu/~adamodar/pc/>)

### Ch7 — Financing across the Life Cycle
- Slides: `pdf/Ch7.pdf` · webcast: <https://youtu.be/loRxUyfqMEk>
- Blogs: "A Viral Market Update XI: A Flexibility Premium" (Jul 2020) *(corrected: post is "XI", verified live)* · "A Tesla 2017 Update: A Disruptive Force and a Debt Puzzle" (Aug 2017)
- Readings: Graham "How big are the tax benefits of debt?" <https://people.duke.edu/~jgraham/HowBigFinalJF.pdf> · NY Fed "The Indirect Costs of the Lehman Bankruptcy" · "Financing Innovations and Capital Structure Choices" SSRN 1297066
- Data: Marginal tax rate by country <.../countrytaxrates.xlsx> · Debt fundamentals — US <.../dbtfund.xls> / Global · Debt breakdown — US <.../debtdetails.xls> / Global
- Tools: capstru.xlsx

### Ch8 — Cash Return (Dividends and Buybacks) across the Life Cycle
- Slides: `pdf/Ch8.pdf` (text extraction failed — **use `img/Ch8/` images**) · webcast: <https://youtu.be/Aw_ljPKgFVw>
- Blogs: "The Walking Dead: Blackberry, Yahoo! and the Zombie Apocalypse" (Sep 2014) · "Jan 2017 Data Update 9: Dividends and Buybacks" (Feb 2017) · "Jan 2018 Data Update 9: Dividends, Stock Buybacks and Cash Holdings" (Feb 2018) · "Data Update 7 for 2023: Dividends, Buybacks and Cashflows" (Mar 2023)
- Readings: "Six Muddles about Stock Buybacks" (Economist) · McKinsey "Dividends versus Buybacks: Which creates more value?"
- Data: Dividend fundamentals — US <.../divfund.xls> / Global · Dividends and FCFE — US <.../divfcfe.xls> / Global
- Tools: dividends.xlsx · buybackcalculator.xls

## Block: Valuation

### Ch9 — Valuation 101
- Slides: `pdf/Ch9.pdf` (image-heavy — use `img/Ch9/`) · webcast: <https://youtu.be/EP-RSiVtwA0>
- Blogs: "Reacting to Earnings Reports: Pricing Metrics and Market Reactions" (Aug 2014) · "DCF Myth 2: A DCF is an exercise in modeling and number crunching" (Aug 2015) · "Jan 2018 Data Update: The Price is Right!" (Feb 2018) · "Jan 2019 Data Update 9: The Pricing Game" (Feb 2019)
- Papers (full local): `pdf/valuesurvey.pdf` ("A Survey of Valuation Approaches") · `pdf/multiples.pdf` ("Relative Valuation / Pricing First Principles")
- Readings: "Discounted cashflow valuations (DCF): Academic Exercise, Sales Pitch or Investing Tool" <https://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html>
- Data: Valuation inputs industry averages — US <.../uValue.xls> / Global
- Tools: fcffsimpleginzu.xlsx · divginzu.xlsx · eqmult.xls

### Ch10 — Valuing Young and Start-up Businesses
- Slides: `pdf/Ch10.pdf` · webcast: <https://youtu.be/i80avS70k8E>
- Blogs: "Risk Capital and Markets: A Temporary Retreat or Long Term Pull Back?" (Jul 2022) · "The Bonfire of Venture Capital: The Good, the Bad and the Ugly Side of Cash Burn!" (Aug 2016)
- Readings: "The Dark Side of Valuation: Valuing firms with no earnings, no history and no comparables" SSRN 1297075 · "Valuing Young, Start-up and Growth Companies" SSRN 1418687 · "Tell me a story" (CFA Institute)
- Data: Revenue multiples by industry — US <.../psdata.xls> / Global
- Tools: Zomato IPO valuation <https://pages.stern.nyu.edu/~adamodar/pc/blog/ZomatoIPO.xlsx> + blog <https://aswathdamodaran.blogspot.com/2021/07/the-zomato-ipo-bet-on-big-markets-and.html>

### Ch11 — Valuing High Growth Businesses
- Slides: `pdf/Ch11.pdf` · webcast: <https://youtu.be/rioTguFIH3U>
- Blogs: "Interest Rates, Earnings Growth and Equity Value" (Mar 2021) · "The Aging of the Tech Sector: The Pricing Divergence of Young and Old Tech Companies" (Feb 2015)
- Readings: "The Big Market Delusion: Valuation and Investment Implications" SSRN 3501688 · "Growth Investing: Betting on the future?" SSRN 2118966
- Data: PE and PEG ratio by industry — US <.../pedata.xls> / Global
- Tools: Airbnb IPO valuation <https://pages.stern.nyu.edu/~adamodar/pc/blog/AirbnbIPO.xlsx> + blog <https://aswathdamodaran.blogspot.com/2020/12/the-sharing-economy-come-home-ipo-of.html>

### Ch12 — Valuing Mature Businesses
- Slides: `pdf/Ch12.pdf` · webcast: <https://youtu.be/rioTguFIH3U>
- Blogs: "The Difference Makers: Key Person(s) Valuation" (Dec 2023) · "Divergence in the Drug Businesses: Pharmaceuticals and Biotechnology" (Nov 2015)
- Readings: "The Octopus: Valuing Multi-business, Multi-national Companies" SSRN 1609795
- Data: EV multiples by industry — US <.../vebitda.xls> / Global
- Tools: Unilever valuation <https://pages.stern.nyu.edu/~adamodar/pc/blog/Unilever2022.xlsx>

### Ch13 — Valuing Declining Businesses
- Slides: `pdf/Ch13.pdf` · webcast: <https://youtu.be/mpx-__Trhak>
- Blogs: "Myth 5.4: Negative Growth Rates Forever? Impossible!" (Nov 2016) · "No light at the end of the tunnel: Investing in bad businesses" (May 2015) · "The Yahoo Chronicles: Is this the end game?" (Dec 2015)
- Readings: "Valuing declining and distressed companies" SSRN 1428022
- Data: Book value multiples by industry — US <.../pbvdata.xls> / Global
- Tools: Bed, Bath and Beyond valuation <https://pages.stern.nyu.edu/~adamodar/pc/blog/BB&B2022.xlsx>

## Block: Investing

### Ch14 — Investment Philosophies 101
- Slides: `pdf/Ch14.pdf` · webcast: <https://youtu.be/u8_J1Z4Mt2w>
- Blogs: "The secret to investment success: Self awareness?" (Nov 2010) · "Active investing: Seeking the elusive edge" (Dec 2016) · "The Search for Investment Serenity: The Look Back Test" (Apr 2015) · "Active Investing: Rest in peace or Resurgent force" (Dec 2016)
- Readings: "The Importance of an Investment Philosophy" (Investors Podcast) · Morgan Stanley "Trading Stages in the Company Life Cycle" <https://www.morganstanley.com/im/publication/insights/articles/article_tradingstagesinthecompanylifecycle.pdf>
- Data: SPIVA Scorecard <https://www.spglobal.com/spdji/en/research-insights/spiva/>

### Ch15 — Investing in Youth (Young and Growth Businesses)
- Slides: `pdf/Ch15.pdf` · webcast: <https://youtu.be/9vMxyAL1dB0>
- Blog: "The Compressed Tech Life Cycle: The Investor Challenge" (Dec 2015)
- Readings: "Going to Pieces: Valuing Users, Subscribers and Customers" SSRN 3175652 · Peter Lynch approach (CSULB) · "How to invest like Peter Lynch" (Motley Fool) · "Growth vs Value Investing" (Forbes)
- Data: Pitchbook VC indices <https://pitchbook.com/news/articles/pitchbook-private-market-indexes>

### Ch16 — Investing in Middle Age (Mature Businesses)
- Slides: `pdf/Ch16.pdf` · webcast: <https://youtu.be/Oax7apxhUP8>
- Blogs: "Value Investing I: The Back Story" · "Value Investing II: A Lost Decade" · "Value Investing III: Rebirth, Requiem or Reincarnation?" (all Oct 2020)
- Readings: "Value Investing: Investing for Grown-ups?" SSRN 2042657 · Berkshire Hathaway shareholder letters <https://www.berkshirehathaway.com/letters/letters.html>

### Ch17 — Investing in Old Age (Shrinking and Declining Businesses)
- Slides: `pdf/Ch17.pdf` · webcast: <https://youtu.be/tBXho7i8_8Q>
- Blogs: "The GE End Game: Bataan Death March or Turnaround Play?" (Nov 2018) · "Private Equity: Hero or Villain" (Jan 2012)
- Readings: "The Anatomy of a LBO: Leverage, Control and Value" SSRN 1162862

## Block: Management

### Ch18 — Managing across the Life Cycle
- Slides: `pdf/Ch18.pdf` · webcast: <https://youtu.be/V1UcOCHTmFM>
- Blogs: "The Compressed Tech Life Cycle: The Managerial Challenge" (Dec 2015) · "Managing across the Corporate Life Cycle" (Dec 2021) · "META Lesson 1: Corporate Governance" (Nov 2022)
- Readings: McKinsey "The mindsets and practices of excellent CEOs" · Yale "Triumph and Disaster: Best and Worst CEOs of 2023" · CEO Magazine "Lessons from history's worst CEOs"
- Data: Comparably best CEOs <https://www.comparably.com/awards/winners/best-ceo-2023-large>

### Ch19 — Fighting Aging
- Slides: `pdf/Ch19.pdf` · webcast: <https://youtu.be/PHlERmgzSHM>
- Blogs: "Rebirth and Reincarnation: Escaping the corporate death spiral" (Sep 2013) · "Walmart's India Gambit: Growth Rebirth or Costly Facelift?" (May 2018)
- Readings: "The Apple Comeback" (Inc) · "Six Biggest Comeback Stories" (Think Business) · "Lessons from Microsoft's Startling Comeback" (Economist) · McKinsey "Leading companies out of crisis: Ten Tips"

### Ch20 — In Search of Serenity
- Slides: `pdf/Ch20.pdf` · webcast: <https://youtu.be/7s3-Xb2gnTY>
- Blogs: "Aging in Dog Years" (Dec 2015) <https://aswathdamodaran.blogspot.com/2015/12/aging-in-dog-years-short-glorious-life.html> · "How a company can act its age" (Oslo Business Forum)
- Readings: "In Silicon Valley, you can forget aging gracefully" (Time)

---

## Add-on resources (whole book)
- Exercises: `CLC/CLCExercises.htm` · Glossary: `glossary.htm` · Updated data: `data.html` · Spreadsheets index: `spreadsh.htm`
- YouTube playlist: <https://www.youtube.com/playlist?list=PLUkh9m2BorqkjTKRzLN9Cx0vIlPvo4Ivw>
- Book corrections: `littlebook2/LBV2corrections.html`

## Note on blog URLs
Where a full blogspot URL is not listed above, fetch by searching the exact
title restricted to `aswathdamodaran.blogspot.com`. All Damodaran blog posts live
on that domain; data-update and "viral market update" posts follow the
`/YYYY/MM/slug.html` pattern.

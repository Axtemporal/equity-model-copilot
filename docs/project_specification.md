# AI-Assisted Financial Modeling System

**Status:** specification v0.2 (decisions closed in a clarification session)
**Date:** June 10, 2026
**Context:** personal open-source library of tools for Brazilian equity research. Solo work, public sources only, no proprietary employer data, no investment recommendations.

---

## One-line summary

A modeling copilot that turns the analyst's manual inputs into standardized Excel models (IFRS statements + sector-specific operational modeling), with the AI proposing assumptions line by line for user approval, and a structure that adapts to the granularity each company discloses.

---

## 1. Closed decisions (June 10, 2026)

| Topic | Decision |
|---|---|
| Architecture | Hybrid. Python engine in the repo (sector templates, validations, .xlsx generator with real formulas). The AI layer runs via Claude. **The interface is Claude Code itself (terminal/PowerShell) driving the engine as a toolkit — no GUI** (decision of June 18, 2026; see §11). |
| MVP scope | Historicals + projections: integrated IFRS three-statement model and an operational tab connected to the financials. The Valuation tab (DCF/WACC) is specified (see §4 and the third-round decisions) but not yet coded — backlog item 6. |
| Pilot sectors | Oil & Gas (pilot company: Prio) and agricultural inputs (pilot company: 3tentos). |
| Data entry | Manually keyed in by the user on the input tabs. Sector and regulatory data (e.g., ANP) are delivered ready-to-use by the user, not collected by the system. |
| Granularity | Self-adapting structure: the operational tab builds itself around the data the company discloses (by field, asset, segment, or consolidated). This is the project's core differentiator. |
| Periodicity | Quarterly + annual for the financials. Operational data accepts monthly series, converted to quarterly in the model. |
| Historical window | 10 years or since the IPO, whichever is shorter. |
| Assumption workflow | The AI proposes line by line with method, source, and rationale. Nothing enters the model without user approval. |
| Assumption log | Dedicated log tab (line, value, method, source, date, status) + a short cell comment pointing to the log. |
| AI sources | Web search allowed (news, peers, public sector data), always citing the source and date of every piece of information used in an assumption. |
| Peers | The AI collects and the user validates. Models of other companies in the library also serve as cross-references (assumptions that can be aligned across models). |
| Language | English, international standard (Net revenue, COGS, EBITDA, working capital). |
| Currency | Each company's reporting currency (to be confirmed during each company's setup; no conversion in the MVP). |

---

## 2. Architecture principle (non-negotiable, carried over from v0.1)

**The LLM reasons, the code calculates.**

All arithmetic (the linkage between income statement, balance sheet, and cash flow statement; ratios; sensitivities; the future DCF) lives in deterministic code or in spreadsheet formulas. The AI reads, flags, suggests methods, finds data in public sources, and explains the reasoning. It never does the math.

```
[AI layer: reasoning]                 [Code layer: calculation]
detect gaps                           model formulas
propose assumptions line by line ---> ratios, sensitivities
find data in public sources           balance check
explain and document assumptions      .xlsx generation
```

Rationale: documented evidence of LLM arithmetic errors in financial contexts (arXiv, July 2025; confirm the exact reference before citing publicly).

---

## 3. Core product workflow (line-by-line modeling session)

**Definitive workflow (set by the user on the evening of June 10, 2026):**

1. The user downloads the repo from GitHub into a folder, connects Claude Code (via the Claude app or PowerShell), and adds the inputs to a folder.
2. The project reads the inputs, converts them into the ideal format for the input tabs, flags what is missing, and runs public research on the company to point out possible typing/unit errors and suggest data the user has not used. Correction is never automatic: the system flags, the user decides.
3. Once the input is ready, the line-by-line session interface opens, starting with the OPERATIONAL DATA. For each line: what the driver is, news, arguments and divergent viewpoints, and 2-3 assumption suggestions (e.g., +3%, +5%, +10%), each anchored in a well-grounded perspective. The user can enter whatever value they want, by quarter and by year. The time profile is discussed explicitly: a single assumption for all periods, or short-term growth with stabilization (e.g., after 5 years), fade, convergence.
4. After the operational section, FINANCIALS: first the structural discussions (debt, acquisitions, organic vs. inorganic growth, how to finance it), which parameterize several lines; then line by line through the three statements.
5. Finally, VALUATION: building the WACC assumption by assumption, multiples, scenarios, target price.
6. Deliverable: a complete model with all tabs integrated with one another and the input tabs included inside the file.

Details closed on the same date: the raw inputs are the user's own spreadsheets with hard data (financial: the three statements, debt and the like; plus operational), in free-form layout, which the system interprets and converts into the template with user verification (no PDFs in the MVP). This project's ingestion acts as a reviewer and helper (format, gaps, complements suggested via public research), never as a collector; the separate collector project continues to exist for anyone who prefers to receive the template already filled in. The session is sequential with resumption: fixed order of operational → structural → statements → valuation, with pause, resume, and the ability to revisit lines already closed.

Original context of the concept:

1. The user keys the historical data (financial and operational) into the input tabs.
2. The system builds the structure: standardized IFRS statements + an operational tab adapted to the disclosed granularity.
3. The guided session begins: for each projectable line, the user and the AI discuss and close an assumption. Format defined in testing (June 10, 2026): each line presented with history and drivers, 2-3 assumption alternatives with pros and cons, and the step-by-step reasoning leading up to the recommendation; only then the decision. Never a bare approve/reject question. The AI proposes based on logic and accounting identities, the company's own historical ratios, peer comparison, growth perception, guidance, and company-specific news affecting the line (e.g., a cost-pressure news item affecting opex).
4. Each approved assumption is recorded in the log with method, source, date, and rationale.
5. At the end, the system generates the complete Excel file: working formulas, input tabs included in the file, cell comments, and the assumptions log.

Two-phase implementation:

- **Phase A (MVP):** the workflow runs in Cowork (chat) using the repo's Python engine. Same logic, no dedicated UI.
- **Phase B (June 2026):** public GitHub repository. The user clones it into a local folder, drops files into the inputs folder, and opens **Claude Code in the repo** — this is the interface. Each line and assumption is worked through in conversation, with Claude Code driving the Python engine (build, log, harness) as a toolkit, until the final Excel file is generated. A Streamlit prototype on the Claude Agent SDK was built first and then discarded (June 18, 2026): the rerun model fought a stateful, latency-heavy approval workflow, and the SDK bridge (Python calling Claude) became redundant once Claude Code is the orchestrator. The engine also runs bare from PowerShell for scripted use.

---

## 4. Standard workbook structure

| Tab | Contents |
|---|---|
| README | Instructions, disclaimers, color and label legend. |
| Input Financials | Manual entry of historicals (quarterly), in the reporting currency. |
| Input Operational | Structure adapted to the company; accepts monthly columns where it makes sense (conversion to quarterly by formula). |
| Assumptions | Assumptions log: line, value, method, source, date, status (approved/pending). |
| IS / BS / CF | Standardized IFRS statements (income statement by function, current/non-current balance sheet, indirect cash flow statement), all by formula linked to the inputs. |
| Operational Model | Operational drivers connected to the financial lines (e.g., production × realization price = revenue). |
| Schedules | Capex/D&A, debt, working capital. |
| Peers | Comparable-company metrics collected by the AI and validated by the user. |
| Valuation | Decision of June 10, 2026 (evening), pulled forward from v2 at the user's request: DCF (FCFF, Gordon growth and exit multiple), WACC block with assumptions and sources, multiples (EV/EBITDA, P/E, FCF yield), target price with disclaimer (analytical output, not a recommendation), bull/base/bear scenarios, summary of main financial and operational data and of the assumptions. Engine prerequisites: revolver, dynamic working capital, shares outstanding, and the EV→equity bridge (incl. IFRS 16 lease treatment). |

Conventions: blue = manual input, black = formula, green = link between tabs, visual highlight for any estimate generated with AI assistance. Sign convention 1 (revenues positive, expenses negative). Balance check (assets = liabilities + equity) in every column.

Layout decisions calibrated against the market reference models (June 10, 2026, details in `calibration_and_knowledge_notes.md`):

- Columns with interleaved quarters and years: 1Q22, 2Q22, 3Q22, 4Q22, 2022, 1Q23... The year closes out each block of four quarters.
- Primary reference for clarity, reasoning structure, and aesthetics: Model A from the local library, including its design of one tab per asset consolidating into the Model tab. Anti-reference: Model D (dense, tabs with 16 thousand columns, hard to audit).
- Historicals on the model tabs always linked by formula to the input tab.
- The three statements automatically interlinked by the engine: NI → retained earnings, roll-forward schedules (PP&E, debt, equity), cash flow as a pure reconciliation, cash and revolver as plugs.

---

## 5. AI layer (four functions)

1. **Detect gaps:** compare the inputs against the sector schema, list what is missing, and classify by criticality (blocks the model, affects a secondary metric, estimable).
2. **Propose assumptions line by line:** the workflow of section 3, using the methods of section 6.
3. **Estimate missing lines:** when the company does not disclose, suggest a method, point to an alternative public source, and label the result as an estimate.
4. **Sensitivity and value drivers:** run via code, ranking which inputs move the result the most so the analyst can focus their attention.

## 6. Estimation and assumption methods

- The company's own historical ratios
- Peer benchmarking (B3 and, where it makes sense, international) and cross-referencing with other models in the library
- Accounting identity or plug
- Top-down from sector or macro data
- Alternative public sources: footnotes to the financial statements, FRE, ITR/DFP filings, sector regulators (ANP for O&G; CONAB/USDA as candidates for agribusiness), always delivered or validated by the user
- Company-specific news affecting individual lines (via web search, with source and date recorded)
- Statistical/regression, used with caution (small samples)

Limitations that must remain visible in the product: estimation error propagates through the three-statement model; some lines only support a range, not a point estimate; every estimate labeled with method and source, never presented as a reported number.

---

## 7. Sector templates

**Oil & Gas (pilot: Prio).** Production by field (boe/d), lifting cost, realization price vs. Brent, capex, reserves (1P/2P/3P), FX. ANP data comes in as a cross-check, delivered by the user. A good test of asset-level granularity.

**Agricultural inputs (pilot: 3tentos).** Multi-segment structure (input retail, industrial, grains), volumes and margins by segment, crop seasonality, commodity prices, FX. Exact drivers to be detailed when the template is built. A good test of incomplete disclosure and of a multi-segment company.

Extensible later: mining (per mine/operation), retail, utilities, etc. Banks are out of scope for now (their statements depart from the industrial IFRS template).

## 8. Alignment across models

With more than one company in the library, shared macro and commodity assumptions (Brent, USDBRL, soybean, diesel) live in a central file referenced by the models, ensuring coverage consistency. Peer models in the same coverage serve as sanity checks for one another.

---

## 9. Compliance (non-negotiable, carried over from v0.1)

- Every estimate marked as an estimate, with method and source, never as a reported number.
- No investment recommendation under any circumstance.
- Public sources only.
- Visual labels separating reported data, the analyst's assumption, and an AI-assisted estimate.
- Framing for professional use: CNPI, APIMEC, CVM Resolution 20.

---

## 10. Roadmap

**MVP (Phase A):**
1. Python engine: IFRS statement schema, O&G template, .xlsx generator with real formulas and a balance check.
2. End-to-end Prio model: manual input → statements + operational → line-by-line assumption session → final Excel.
3. 3tentos next, validating the engine's generalization to another sector and a multi-segment structure.

Status (June 2026): the O&G engine builds the three interlinked statements with **dynamic schedules** — days-driven working capital, a debt schedule (interest on the opening balance), IFRS-16 leases (right-of-use + lease-liability roll-forwards), a simple non-circular revolver (keeps cash ≥ a minimum via MIN/MAX), and ARO/decommissioning — with the balance check at zero in every column, verified automatically by a recalculation harness (openpyxl writes formulas but does not compute them; the harness recalculates the workbook and asserts the invariants). Approved assumptions persist on rebuild (the Assumptions log is the source of truth). The interface is Claude Code driving the engine as a toolkit (the Streamlit prototype was removed on June 18, 2026); the line-by-line assumption session and four-agent panel are being redesigned for that format. Pending: the telecom engine is one step behind O&G (schedules still frozen); the declarative YAML template is written but not yet consumed by the engine; the full Valuation tab (DCF/WACC) is specified but not coded.

**Evolution:**
- Input-collector project (the user's separate repo): gathers public data and delivers the filled input workbook.
- Full DCF with automatic sensitivity and value-driver ranking (the Valuation tab).
- Scenarios (base/bull/bear).
- Central shared-macro assumptions file.
- Reference-Form reader connection (notes and the FRE feed estimates).
- New sectors (mining a natural candidate for the per-mine granularity question).

## 11. Closed decisions, second round (June 10, 2026)

- **Projection horizon:** quarterly through the end of next year, annual through year 10.
- **Pilot order:** Prio first, then 3tentos.
- **Base/bull/bear scenarios:** v2.

**Interface — decided (June 18, 2026):** the interface is **Claude Code itself** (terminal/PowerShell), driving the engine as a toolkit/CLI. The Streamlit + Agent SDK prototype was built and then discarded; this supersedes the earlier "Phase B bridge = Agent SDK" decision (neither Agent SDK nor MCP — the bridge is Claude Code). Consequence: deterministic guardrails (method+source gate, sanity bounds, harness, YAML log + cell comments) must be enforced by the engine as invariants, not left to the conversation. (LangChain/LangGraph were evaluated and discarded — keeping a plain Python engine driven by Claude Code.) Still open: the Python package name, and confirming each pilot's reporting currency on the first input.

## 12. Stack and engineering

- Python: pandas, numpy, openpyxl (real formulas, never static values where a formula belongs)
- Declarative sector templates (YAML/JSON): lines, operational → financial mapping, granularity rules
- Reasoning layer: Claude, via Claude Code driving the engine as a toolkit (the interface; no GUI, no Python→Claude SDK bridge)
- Suggested repo structure: `/engine` (package), `/templates` (sectors), `/inputs` (per-company input sheets), `/models` (.xlsx outputs), `/knowledge` (per-line projection method cards distilled from the training library), `/reference` (market models and the training library, necessarily gitignored for copyright), README, requirements.txt, .gitignore, engine tests
- Retry, cache and logging wherever there is an external source; everything versioned

## 13. Sources and references

- CVM (ITR, DFP, FRE, explanatory notes), B3, BCB
- ANP (O&G operational data, delivered by the user); CONAB/USDA as candidates for agribusiness
- Anthropic's `creating-financial-models` skill as an engineering reference for the calculation engine
- Evidence of LLM arithmetic limitations in finance: arXiv, July 2025 (confirm the exact reference before any public citation)
- Compliance: CNPI, APIMEC, CVM Resolution 20
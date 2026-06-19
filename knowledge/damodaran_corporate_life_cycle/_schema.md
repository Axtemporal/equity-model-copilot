# Note schema — Damodaran "Corporate Life Cycle" knowledge base

This file defines the **mandatory structure** every chapter note (`cap_NN_<slug>.md`)
must follow, so the 20 notes are homogeneous and machine-navigable. It is a
maintenance contract, not content.

## Conventions

- **Language:** English (technical valuation terms kept as market-standard).
- **Distillation, not copying:** paraphrase Damodaran's ideas in our own words.
  Never paste slide text, paragraphs, or tables verbatim. Numbers/examples may be
  cited as facts with provenance, but prose must be rewritten.
- **Provenance is mandatory:** every claim traces to a source. Use the
  `> source:` callout under each major section pointing to the slide deck +
  page(s), paper, or blog URL it came from.
- **Cross-links:** link sibling notes with `[[cap_NN_slug]]` and the synthesis
  notes `[[00_framework_lifecycle]]` / `[[application_to_copilot]]`.
- **No investment advice:** describe Damodaran's frameworks; never turn them into
  a recommendation. (Project compliance rule.)

## Required sections (in order)

```markdown
---
chapter: NN
title: <chapter title>
block: <Lead In | Corporate Finance | Valuation | Investing | Management>
slides: reference/damodaran_clc/pdf/ChNN.pdf
status: draft
---

# Ch NN — <Title>

## 1. Core thesis
One-paragraph statement of what this chapter argues and where it sits in the
life-cycle arc.

## 2. Key concepts & frameworks
Bullet/sub-section per concept. Define each, give Damodaran's logic, note the
life-cycle stage(s) it applies to.
> source: ChNN.pdf p.X–Y

## 3. Metrics, formulas & rules of thumb
Every metric or formula the chapter introduces, written out, with how it is
computed and how it shifts across the life cycle. Tables welcome.
> source: ...

## 4. Examples & cases
Companies/cases Damodaran uses, with the point each illustrates.
> source: ...

## 5. Data & tools
The Damodaran datasets (.xls by industry) and tool spreadsheets tied to this
chapter — name, what they contain, URL. (Catalog only; raw data not copied.)

## 6. Supplementary readings — distilled
For EACH blog post / paper / external reading mapped to this chapter in
`_sources.md`: 2–5 sentence distillation of its argument + what it adds beyond
the slides. Mark whether read in full or abstract-only.
> source: <url>

## 7. Takeaways for valuation & modeling
The 3–6 most actionable points for an equity analyst building a model — the raw
material the synthesis note will lift into `[[application_to_copilot]]`.
```

## Length
No artificial cap. A chapter with 30 slides + 4 blogs + 2 papers should produce
a substantial note. Completeness over brevity — do not cut corners.

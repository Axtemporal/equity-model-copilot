# Wiki article contract (LLM wiki)

This wiki is the **concept-oriented** view of the Damodaran Corporate Life Cycle
knowledge base (the chapter notes `cap_01…cap_20` are the complementary
*by-chapter* view). It follows the three-layer "llm-wiki" pattern from the
project's CLAUDE.md decision #9: one concept per file, heavily cross-linked,
provenance on every article, with `index.md` as the entry point.

## Rules every article must follow

1. **One concept per file.** Filename = the concept slug from `_concepts.md`
   (e.g. `wacc.md`, `terminal-value.md`). Never invent a slug — use the registry.
2. **English.** Market-standard technical terms kept in English.
3. **Distillation, not copying.** Paraphrase. Never paste verbatim from the
   source material. (Project copyright rule.)
4. **Cross-link liberally** with `[[slug]]` — but ONLY slugs that exist in
   `_concepts.md`. A wiki is its link graph; aim for 4–10 outbound links each.
5. **Provenance is mandatory.** Every article ends with a Provenance block that
   points to (a) the chapter note(s) `[[cap_NN_slug]]`, (b) the original
   source(s) as markdown hyperlinks (URLs from `../_sources.md`), and (c) the
   local raw text when relevant (`reference/damodaran_clc/text/ChNN.txt`,
   gitignored). No re-fetched source markdown exists — provenance is by hyperlink.
6. **No investment advice.** Describe frameworks; never turn them into a
   recommendation. (Project compliance rule.)
7. **Lead with the definition.** First line after the title is a bold one-sentence
   "what it is", so the article is useful even read alone.

## Required structure

```markdown
---
concept: <slug>
title: <Concept Title>
theme: <one of the themes in _concepts.md>
status: draft
---

# <Concept Title>

**What it is.** One-sentence definition.

## Core idea
The essential explanation in our own words.

## Across the life cycle
How this concept changes / when it matters by stage (start-up → decline).
Omit only if genuinely stage-invariant (say so).

## Mechanics / formulas
Formulas, computation, rules of thumb (when applicable).

## Pitfalls & nuances
Common mistakes, Damodaran's caveats, where it breaks.

## Related concepts
- [[slug]] — one line on the relationship
- ...

## Provenance
- Chapter notes: [[cap_NN_slug]], ...
- Sources: [Title](url), ...
- Raw (gitignored): reference/damodaran_clc/text/ChNN.txt
```

## Length
Concept articles are focused — typically 60–200 lines. Depth over padding;
completeness over brevity, but stay on the single concept and push tangents to
their own article via a cross-link.

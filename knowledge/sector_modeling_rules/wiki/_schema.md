# Wiki article contract (sector LLM wiki)

This wiki is the **concept-oriented** view of the sector modeling-rules knowledge
base (the per-sector method cards `sectors/oil_and_gas.md … sectors/auto.md` are the complementary
*by-sector* view). It follows the three-layer "llm-wiki" pattern from the project's
CLAUDE.md decision #9: one concept per file, heavily cross-linked, provenance on
every article, with `index.md` as the entry point.

It mirrors the sibling wiki `../../damodaran_corporate_life_cycle/wiki/` — same
contract, two deltas: the cross-cutting axis is **sector**, not life-cycle stage,
and every article carries a **confidence tier** (✅/🟡/⚠️) because the underlying
claims came from adversarial deep-research, not a single authoritative book.

## Rules every article must follow

1. **One concept per file.** Filename = the concept slug from `_concepts.md`
   (e.g. `ias-41-biological-assets.md`, `arr-roll-forward.md`). Never invent a
   slug — use the registry.
2. **English.** Market-standard technical terms kept in English; Brazilian-specific
   terms (CFEM, JCP, sinistralidade) kept in Portuguese with a gloss.
3. **Distillation, not copying.** Paraphrase. Never paste verbatim from the source
   material, and never quote the proprietary `Example models/` or `Knowledge Base/`
   archives. (Project copyright rule.)
4. **Method over numbers.** Encode the *method*, not point-in-time figures. Any
   number is a dated illustration, never a value to hardcode.
5. **Cross-link liberally** with `[[slug]]` — but ONLY slugs that exist in
   `_concepts.md`. A wiki is its link graph; aim for 4–10 outbound links each.
   Cross-links may also point to the per-sector method cards by filename
   (e.g. `[[fuel_distribution]]`) and to the sibling Damodaran wiki concepts.
6. **Provenance is mandatory.** Every article ends with a Provenance block that
   points to (a) the method card(s) it overlays, (b) the original source(s) as
   markdown hyperlinks (IDs + URLs from `../_sources.md`), and (c) the article's
   confidence tier with the verification vote when known.
7. **No investment advice.** Describe modeling methods and KPIs; never turn them
   into a recommendation or target price. (Project compliance rule.)
8. **Lead with the definition.** First line after the title is a bold one-sentence
   "what it is", so the article is useful even read alone.

## Confidence tiers (carried from the deep-research)

- ✅ **verified** — confirmed by adversarial 3-vote verification (≥2-0) against a
  primary or strong secondary source.
- 🟡 **seed** — single reputable source, or verified-in-principle but not yet
  corroborated.
- ⚠️ **to-verify** — standard practice / textbook knowledge with no source attached
  yet; a round-N research gap.

Tag at the article level in frontmatter (`confidence:`) and inline on individual
claims where they diverge from the article's overall tier.

## Required structure

```markdown
---
concept: <slug>
title: <Concept Title>
theme: accounting-standard | driver-pattern | sector-kpi | brazil-specific
applies_to: [oil_and_gas, metals_mining, ...]   # sectors this concept governs
confidence: verified | seed | to-verify
status: draft
---

# <Concept Title>

**What it is.** One-sentence definition.

## Core idea
The essential explanation in our own words.

## Applies to sectors
Which sectors this governs and how each one uses it (the analogue of the
Damodaran wiki's "Across the life cycle"). Omit only if genuinely universal.

## Mechanics / formulas
Formulas, computation, rules of thumb (when applicable).

## Modeling implications
What changes in the model / the assumption proposals when this concept applies —
the bridge from theory to the copilot's behaviour.

## Pitfalls & nuances
Common mistakes, caveats, where it breaks. Include any **refuted** framings here
as explicit "do NOT encode" notes.

## Related concepts
- [[slug]] — one line on the relationship
- ...

## Provenance
- Method cards: [[oil_and_gas]], ...
- Sources: [ID — Title](url), ...
- Confidence: ✅/🟡/⚠️ (verification vote, round)
```

## Length
Concept articles are focused — typically 60–200 lines. Depth over padding;
completeness over brevity, but stay on the single concept and push tangents to
their own article via a cross-link.

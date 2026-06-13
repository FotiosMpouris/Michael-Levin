# Wiki Schema — Michael Levin Research

## Purpose
A focused knowledge base for Michael Levin's research and related topics:
bioelectricity, morphogenetics, xenobots, cognitive biology, developmental biology,
regeneration, collective intelligence, and the platonic space of minds.

## Three Layers
1. **raw/** — Immutable source material (transcripts, papers, notes). Never modify.
2. **Wiki pages** — Agent-owned. Entities, concepts, comparisons, queries.
3. **This schema** — Conventions and rules.

## Page Types

### entities/
Researchers, labs, organisms, technologies mentioned in sources.
Filename: `entities/{name-slug}.md`

### concepts/
Scientific ideas, frameworks, hypotheses, research directions.
Filename: `concepts/{concept-slug}.md`
Examples: bioelectricity, morphogenetic-fields, xenobots, cognitive-lightcone, basal-cognition

### comparisons/
Side-by-side analyses (e.g., top-down vs bottom-up approaches to morphogenesis)
Filename: `comparisons/{subject-vs-subject}.md`

### queries/
Saved answers to important questions filed back from conversations.
Filename: `queries/{question-slug}.md`

## Conventions
- All pages use [[wikilinks]] for cross-references
- Frontmatter is YAML between --- delimiters
- Each page has a ## Sources section
- Tag taxonomy: #bioelectricity #morphogenesis #xenobots #cognition #regeneration #collective-intelligence #neuroscience #philosophy

## Operations
Same as main wiki — see ~/workspace/wiki/SCHEMA.md for ingest/query/lint details.
After any wiki write: `cd ~/workspace/wikis/michael-levin && git add -A && git commit -m "..." && git push`

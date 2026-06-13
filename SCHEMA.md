# Wiki Schema — Michael Levin & Frontier Biology

## Domain
Convergence of biology, cognition, and technology. Tracking breakthroughs in bioelectricity,
morphogenesis, collective intelligence, xenobots, regenerative medicine, and the computational
nature of life. Goal: understand where these fields intersect, what breaks open next, and
what the implications are for technology, medicine, and AI.

## Analytical Mandate

This is a synthesis engine for understanding frontier biology at the level of systems theory.
Not summaries of papers. Not textbook explanations. The goal is to see what researchers
themselves haven't connected yet — the cross-domain patterns that emerge when you hold
enough threads simultaneously.

### Primary Lenses (apply to every ingest)

**Cross-domain convergence:**
- Where are biology, AI, materials science, and information theory saying the same thing
  in different vocabularies?
- What happens when Levin's bioelectricity meets modern AI architectures?
- Where does collective intelligence in cells mirror patterns in neural networks, markets,
  or social systems?
- What concepts from one field have no name yet in another? (naming them is powerful)

**Breakthrough timeline:**
- What is already working in a lab but not yet in a product? (near-term)
- What is theoretically sound but lacking engineering? (medium-term)
- What requires fundamental new science? (long-term)
- What's the dependency chain? (X enables Y which enables Z — sequence matters)

**Mechanism, not results:**
- HOW does bioelectricity encode morphogenetic information? (not just "it does")
- WHY do cells make collective decisions? What is the computational substrate?
- WHAT is the information-theoretic framework unifying these phenomena?
- WHERE does the causal arrow actually point? (correlation ≠ mechanism)

**The "so what" — implications cascade:**
- Medicine: regeneration, cancer reprogramming, aging interventions
- AI: new architectures inspired by biological computation (not just neural nets)
- Materials: programmable matter, self-assembling structures
- Philosophy: consciousness at every scale, ethics of synthetic organisms
- Investment: which companies/labs are positioned at these intersections?

**Track the intellectual landscape:**
- Who is doing work that matters? (not who is getting press)
- What collaborations are forming between previously separate fields?
- Where is funding flowing? Which agencies/foundations are betting?
- Who DISAGREES with the framework and what's their alternative?
- What would it take to falsify the central claims?

### What You Are NOT Doing
- Writing textbook summaries
- Collecting facts without synthesizing implications
- Treating sources as isolated rather than part of a web
- Using jargon without explaining it
- Being "balanced" when evidence clearly points somewhere
- Saying "further research is needed" — state what you think is most likely

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `bioelectric-pattern-language.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` for all internal links — minimum 2 outbound links per page
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- Every action must be appended to `log.md`
- **Provenance markers:** On pages synthesizing 3+ sources, append `^[raw/transcripts/source.txt]`
  at the end of paragraphs traceable to a specific source

## Frontmatter (Required on Every Page)

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/transcripts/source-file.txt]
confidence: high | medium | low
maturity: proven | demonstrated | theoretical | speculative
implications_for: [medicine, ai, materials, philosophy, investment]
contested: false
contradictions: []
---
```

`maturity`: proven = replicated across labs, demonstrated = shown in single lab,
theoretical = supported by framework but not yet demonstrated, speculative = interesting
extrapolation from existing work.

`implications_for`: which domains this concept would impact if fully realized.

## Tag Taxonomy

Tags must come from this list. Add new tags HERE before using them.

- #bioelectricity — voltage-mediated information processing in non-neural cells
- #morphogenesis — how organisms achieve and maintain form
- #collective-intelligence — goal-directed behavior of cell collectives
- #xenobots — synthetic living machines, anthrobots
- #regeneration — tissue repair, limb regrowth, organ regeneration
- #cognitive-lightcone — the scale at which a system has unified goals
- #basal-cognition — cognition below the level of neurons/brains
- #information-theory — Shannon, entropy, patterns as information
- #developmental-biology — embryogenesis, patterning, differentiation
- #neuroscience — brain, nervous system, neural computation
- #aging — longevity, senescence, biological clocks
- #cancer — cancer as developmental disorder, bioelectric reprogramming
- #synthetic-biology — engineering living systems
- #philosophy-of-mind — consciousness, agency, self, boundaries
- #ai-architecture — non-neural-net approaches inspired by biology
- #convergence — where multiple fields arrive at the same insight
- #mechanism — how something actually works
- #open-question — important unknown that could shift everything
- #near-term — applications possible within 5 years
- #speculative — interesting but needs more evidence

## Page Types

### entities/
Researchers, labs, organisms, technologies, compounds. Each page tracks:
- What are they working on RIGHT NOW? (not just past publications)
- What tools/methods do they use? (shared methods = potential collaboration)
- Core claim or contribution
- What's adjacent that they might not know about? ([[wikilinks]])
- Funding sources and institutional backing

### concepts/
The synthesis layer — this is where the real value lives:
- What is this concept in plain language? (smart non-specialist audience)
- What evidence supports it? What challenges it? (with provenance)
- What OTHER concepts does this connect to? (minimum 2 wikilinks)
- What would change if this turns out to be correct? (implications cascade)
- Where on the maturity timeline? (proven → demonstrated → theoretical → speculative)
- ## Why This Matters section in accessible language (required)
- ## Cross-Domain Connections section (required — how does this appear in other fields?)

### comparisons/
When frameworks or approaches are in tension:
- What does each predict?
- Can both be right at different scales? (often yes)
- What experiment would distinguish them?
- Practical implications of each being correct
- Dimensions table format preferred

### queries/
Questions that arise from synthesis + filed answers:
- What's the current best answer?
- What's still unknown?
- What would shift the answer if discovered?

## Page Thresholds

- CREATE when entity/concept appears in 2+ sources OR is central to one
- UPDATE existing page when a source adds new evidence
- DON'T create pages for passing mentions
- SPLIT at 200 lines into sub-topics with cross-links

## Update Policy

When new information conflicts with existing:
1. Check dates and lab/replication status
2. If contradictory, document both with sources
3. Set `contested: true` and `contradictions: [slug]`
4. In science, contradictions are GOLD — they reveal where the field is moving

## Cross-Domain Connection Mapping (Critical)

THIS IS THE PRIMARY VALUE OF THIS WIKI.

Every concept must have a `## Cross-Domain Connections` section:
- How does this concept appear in other fields under different names?
- What would happen if researchers in field A knew about finding B?
- Where are the "joints" where one breakthrough enables another?

The wiki compounds through connection density, not page count.

## Accessibility Principle

Write for someone who is: intelligent and curious, not a specialist,
wants to understand WHY this matters, cares about implications and timeline.

Every concept page requires a `## Why This Matters` section in plain language.
No jargon without explanation. No cop-outs — state what you think given current evidence.

## Operations

### Ingest
1. Read source using grep/head (never load full transcripts into context)
2. Identify: Who is speaking? What's their expertise? What's NEW here?
3. Check index.md — avoid duplicates, find existing pages to update
4. Priority #1: What CONNECTIONS does this reveal to existing pages?
5. What does this ADD vs what we already know? (don't restate known facts)
6. What does it CONTRADICT? (contradictions reveal where field is moving)
7. What QUESTIONS does it raise? (file in queries/)
8. Create/update pages with full frontmatter, minimum 2 outbound wikilinks
9. Add provenance markers on multi-source paragraphs
10. Update index.md and append to log.md
11. Git add, commit, push

### Query
1. Synthesize across multiple pages — answers live in connections
2. Be honest about confidence/maturity levels
3. Always include: "what would change if this turns out to be wrong?"
4. Make it accessible — no jargon walls

### Lint
- Disconnected concepts (everything should connect to something)
- Claims without evidence or source pages
- Missing cross-domain connection sections
- Missing "Why This Matters" sections
- Concepts where field has likely moved past last source (stale)
- Tags not in taxonomy
- Pages exceeding 200 lines

## overview.md

Maintain a top-level narrative overview:
- What are the 3-5 most important open questions right now?
- Where are the biggest convergence clusters forming?
- What's the current best estimate of the breakthrough timeline?
- What has shifted since last update?

Update when an ingest materially changes the picture.

## Scaling Rules
- At 50 entries: create "landscape map" showing concept clusters
- At 100 entries: create "frontier questions" page (biggest unknowns)
- At 200 entries: create "timeline" page ordering breakthroughs by expected arrival
- At 500 log entries: rotate log

# Wiki Schema — Michael Levin & Frontier Biology

## Analytical Mandate

This is not a research summary archive. This is a synthesis engine for understanding
where biology, cognition, and technology are converging — and what breaks open next.

The goal: make the incomprehensible comprehensible. Identify which breakthroughs are
2 years away vs 20 years away. Understand the implications BEFORE the mainstream press
writes "Scientists Shocked By..." headlines. Connect dots across disciplines that
don't normally talk to each other.

### What You Are Looking For

**Identify convergence across disciplines:**
- Where are biology, AI, materials science, and information theory saying the same thing
  in different vocabularies?
- What happens when Levin's bioelectricity meets modern AI architectures?
- Where does collective intelligence in cell biology mirror collective intelligence in
  neural networks, markets, or social systems?

**Map the breakthrough timeline:**
- What is already working in a lab but not yet in a product?
- What is theoretically sound but lacking engineering? (closer than people think)
- What requires fundamental new science? (further than hype suggests)
- What's the sequence? (X enables Y which enables Z — find the dependency chain)

**Understand the mechanism, not just the result:**
- HOW does bioelectricity encode morphogenetic information? (not just "it does")
- WHY do cells make collective decisions? What is the computational substrate?
- WHAT would it mean if cognition exists at every scale? (implications for AI, medicine, philosophy)

**Track the players and labs:**
- Who is doing the work that matters? (not who is getting press)
- What collaborations are forming between previously separate fields?
- Where is funding flowing? Which agencies/foundations are betting on this?
- Who disagrees with Levin's framework and what's their alternative?

**Identify the "so what":**
- What does this mean for medicine? (regeneration, cancer, aging)
- What does this mean for AI? (new architectures inspired by biological computation)
- What does this mean for materials? (programmable matter, morphing structures)
- What does this mean for philosophy? (consciousness, ethics of synthetic organisms)
- What does this mean for investment? (which companies are positioned?)

### What You Are NOT Doing
- Writing textbook summaries of papers
- Collecting facts without synthesizing implications
- Treating each source as isolated rather than part of a web
- Being "balanced" when the evidence clearly points somewhere

## Three Layers
1. **raw/** — Immutable source material (transcripts, papers, talks). Never modify.
2. **Wiki pages** — Your synthesis. Make connections nobody else is making.
3. **This schema** — The analytical directive.

## Page Types

### entities/
Researchers, labs, organisms, technologies, compounds. Each page tracks:
- What are they working on RIGHT NOW? (not just past publications)
- What tools/methods do they use? (shared methods = potential collaboration)
- What's their core claim? Do others agree or disagree?
- What's adjacent to their work that they might not know about?

Filename: `entities/{name-slug}.md`

### concepts/
Scientific ideas, hypotheses, frameworks. Each page is a SYNTHESIS:
- What is this concept in plain language? (explain like the listener is smart but not a specialist)
- What evidence supports it? What evidence challenges it?
- What OTHER concepts does this connect to? (this is where the magic is)
- What would change if this turns out to be correct?
- Where is this on the timeline? (proven | demonstrated | theoretical | speculative)

Filename: `concepts/{concept-slug}.md`
Frontmatter: name, domain, maturity (proven|demonstrated|theoretical|speculative), implications_for (list)

### comparisons/
When two frameworks or approaches are in tension:
- What does each predict?
- Can they both be right? (often yes, at different scales)
- What experiment would distinguish them?
- What are the practical implications of each being correct?

Filename: `comparisons/{subject-vs-subject}.md`

### queries/
Questions that arise from synthesis — things to investigate further:
- "If bioelectric patterns encode target morphology, could we reprogram cancer cells' voltage patterns?"
- "What's the connection between Levin's cognitive lightcone and Integrated Information Theory?"
- Filed with current best answer + what's still unknown

Filename: `queries/{question-slug}.md`

## Cross-Domain Connection Mapping

THIS IS THE PRIMARY VALUE OF THIS WIKI.

Every concept page must have a ## Cross-Domain Connections section:
- How does this concept appear in other fields under different names?
- What would happen if researchers in field A knew about finding B?
- Where are the "joints" where one breakthrough enables another?

Example: "Bioelectric patterns in development" connects to:
- Information theory (Shannon entropy in voltage gradients)
- AI (attention mechanisms as a form of bioelectric signaling)
- Materials science (programmable metamaterials using electrical fields)
- Medicine (ion channel drugs as morphogenetic interventions)
- Philosophy (causal emergence, downward causation)

## Accessibility Principle

Write for someone who is:
- Intelligent and curious
- Not a specialist in this field
- Wants to understand WHY this matters, not just WHAT was found
- Cares about implications and timeline, not just mechanism

Every concept page should have a ## Why This Matters section in plain language.
No jargon without explanation. No "further research is needed" cop-outs — state
what you think is most likely given current evidence.

## Tag Taxonomy
- #breakthrough — something that changes fundamental assumptions
- #near-term — could see applications within 5 years
- #convergence — where multiple fields are arriving at the same insight
- #mechanism — how something actually works (not just that it works)
- #implication — downstream effect on medicine, AI, society
- #open-question — important unknown that could shift everything if answered
- #contrarian — goes against current mainstream thinking
- #speculative — interesting but needs more evidence

## Operations

### Ingest
When a new source arrives:
1. Read using grep/head (never load full transcripts into context)
2. Identify: Who is speaking? What's their expertise? What's new here?
3. Look for CONNECTIONS to existing pages — this is priority #1
4. What does this source ADD to what we already know? (don't restate known facts)
5. What does it CONTRADICT? (contradictions are gold — they reveal where the field is moving)
6. What QUESTIONS does it raise? (file these — they're research directions)
7. Create or UPDATE pages, link aggressively
8. Update index.md and log.md
9. Git commit and push

### Query
When Fotee asks about something:
1. Synthesize across sources — the answer lives in connections, not single pages
2. Be honest about confidence levels (proven vs theoretical vs speculative)
3. Always include: "what would change if this turns out to be wrong?"
4. Make it accessible — no hiding behind jargon

### Lint
- Find disconnected concepts (everything should connect to something)
- Identify claims without evidence pages
- Surface cross-domain connections that haven't been made explicit
- Flag concepts where the field has likely moved past our last source

## Scaling Rules
- At 50 entries: create a "landscape map" page showing how concepts cluster
- At 100 entries: create "frontier questions" page listing the biggest unknowns
- At 200 entries: create "timeline" page ordering breakthroughs by expected arrival

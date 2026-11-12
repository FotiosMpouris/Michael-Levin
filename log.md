# Wiki Log — Michael Levin

## 2026-06-15

**Ingest:** "Mind May Be Older Than the Brain" — Philosophy Everyday, LCqJKGnRcbA

**Created entities:**
- michael-levin (researcher profile, current work at Tufts)
- xenobots-anthrobots (synthetic organisms, demonstrated learning/self-replication)

**Created concepts:**
- cognitive-lightcone (goal-scale framework for intelligence scaling)
- bioelectric-pattern-language (how voltage encodes morphogenetic info)
- basal-cognition (continuum theory of mind across all scales)
- morphogenetic-field (pattern space where organism form is specified)
- platonic-space (speculative framework for Levin's ideas on abstract patterns)

**Created queries:**
- 2026-06-15-morphogenetic-templates (CRITICAL: where are templates stored?)
- 2026-06-15-xenobot-cognition (what cognitive capacities do xenobots have?)
- 2026-06-15-embodiment-potential (why does embodiment unlock behavioral potential?)

**Key findings:**

1. **Template Problem (CRITICAL):** Levin emphasizes this repeatedly — if regenerating tissues "know" the correct morphology, where is that information stored? DNA is necessary but insufficient. Bioelectric patterns are the leading hypothesis, but the mechanism is still unknown. This is the keystone question.

2. **Bioelectricity as Computational Substrate:** Not just biophysics "noise" — actual information encoding. Voltage gradients are how cells represent morphogenetic goals and coordinate at scale. Testable: manipulate bioelectricity → change morphology, DNA unchanged.

3. **Cognitive Glue Mechanisms:** Gap junctions create "mind meld" effects where cells can't distinguish their own memories from collective memories. This expands cognitive lightcone by enabling spatial/temporal integration.

4. **Xenobots as Proof of Concept:** Same frog cells in novel configuration → novel morphology. Demonstrates: form is not hard-coded in DNA; cells can self-organize around bioelectric patterns. Learning demonstrated; other cognitive abilities still being tested.

5. **Platonic Space Hypothesis:** Most speculative but most ambitious. Claims biological systems access abstract mathematical patterns with causal power. Explains "unexpected" behaviors that can't be attributed to design, evolution, or learning alone.

6. **Continuous Spectrum of Mind:** Rejects binary "minded/non-minded" categories. Intelligence is about goal-scale, not substrate or presence of neurons. Single cells have basal cognition pursuing homeostatic goals.

**Connections to note:**
- Bioelectricity ↔ Morphogenesis ↔ Regeneration ↔ Development (unified by pattern-space framework)
- Cognitive Glue ↔ Neural Integration ↔ Collective Intelligence (scaling laws)
- Basal Cognition ↔ Embodied Cognition ↔ Relational Ontology (philosophy of mind shift)
- Platonic Space ↔ Emergent Behavior ↔ AI Capability (theoretical implications)

**Next priorities:**
- Empirical resolution of template problem (likely 2-5 years)
- Xenobot cognitive tests (ongoing, results in 1-3 years)
- Bioelectric mechanism clarification (medium-term)
- Embodied AI experiments (could inform both biology and AI)

**Confidence levels:**
- Bioelectric effects: HIGH (demonstrated in multiple labs)
- Cognitive lightcone framework: MEDIUM (theoretical, useful, not yet universally adopted)
- Basal cognition: MEDIUM-HIGH (philosophically interesting, empirically supported but challenged)
- Platonic space: LOW (speculative, needs formalization and testing)
- Xenobot cognition: MEDIUM (learning demonstrated, full profile unknown)

**Maturity assessment:**
- Bioelectric pattern control: DEMONSTRATED (lab-proven)
- Morphogenetic field model: THEORETICAL (well-supported but incompletely understood)
- Regenerative medicine applications: NEAR-TERM (animal trials ongoing, hoping for FDA soon)
- Xenobot/anthropot applications: SPECULATIVE (cognitive status unclear, ethical framework needed)

---

## Ingest Statistics

| Category | Count | Status |
|----------|-------|--------|
| Entities | 2 | new |
| Concepts | 5 | new |
| Queries | 3 | new |
| Pages | 10 | new |

**Transcript analysis:** 2303 lines, ~82 minutes of content. Key sections: 
- Intro/overview (0-5 min)
- Mind continuum argument (5-12 min)
- Cognitive lightcone definition (13-16 min)
- Bioelectric glue mechanisms (16-20 min)
- Xenobots/anthrobots demonstration (21-35 min)
- Platonic space hypothesis (42-54 min)
- Embodied algorithms (59-64 min)
- Regenerative medicine applications (77-82 min)

## 2026-10-15 — channel ingest + companies tracker
- Pulled YouTube auto-captions (yt-dlp, en-orig) for the 10 most recent videos on @drmichaellevin; transcripts in raw/transcripts/.
- Added videos/ (10 pages), topics/ (8 hub pages), whats-new.md, vision.md, companies/companies-tracker.md.
- All quotes verified as exact substrings of the caption transcripts. Company links checked 2026-10-15.
- Public site built from this repo with site/build.py and published on here.now.

## [2026-10-16] update | Michael Levin profile page rebuilt
- entities/michael-levin.md rewritten from lab site, 7 peer-reviewed papers (DOIs checked on Crossref), blog, X; evidence labels (Confirmed / His words / Our reading). Typos fixed, broken [[xenobots]] link fixed.
- Nav link added; site/check.py deterministic checks added. Republished (anonymous, 24h) at https://inner-breeze-5fr8.here.now/ because the 10/15 publish expired and the saved here.now API key was rejected.

## [2026-10-16] redesign | Morphospace public site
- New home: "Latest from Levin" feed (feed/latest.json, 39 dated items from YouTube, Crossref, X, thoughtforms.life), then topics, papers, companies, profile. New identity, self-hosted fonts (OFL).
- Personal material removed from public pages; vision.md moved to the private notes. check.py now blocks any personal name, future-dated items and dead feed links.
- feed/refresh.py + feed/UPDATE.md for the Thursday routine.

## [2026-10-22] weekly refresh
- Feed: 2 videos (SiTlGdMKQNo Jian Shu guest talk, YxmSCElKdm0 "New Bodies, Unconventional Minds", both 2026-10-17), 1 preprint (Clofilium in colorectal cancer, 2026-10-19), 2 X posts (cell trainer platform 2026-10-21, Venn poll 2026-10-22). whats-new.md updated.
- YouTube blocked yt-dlp (bot check / 429), so no captions and no video pages this week; refresh.py now falls back to the channel RSS for dates and titles. check.py: ERRORS 0. Published to inner-breeze-5fr8 (version 01M5HWVWW27QBPQ2BNT9B5DMMR).

## [2026-10-29] weekly refresh
- Feed: 4 videos (Lior Nissim 10/29, Benjamin De Bari-Cheung 10/28, Debanik Bhattacharjee 10/26, Chris Fields 10/25), 1 preprint (Xenopus limb/brain transcription, 10/24), 1 peer-reviewed paper (nanofluidic reservoir computing, 10/23), 5 X posts (10/23 to 10/26). whats-new.md, index.md and topic hubs updated.
- Captions pulled with the vaulted-cookie yt-dlp method for all 8 videos missing pages (4 new plus SiTlGdMKQNo, YxmSCElKdm0, P803O6opd3o, YXXYM3Z4fV0); 8 video pages written, every quote checked word for word against the captions. Transcripts in raw/transcripts/. Companies tracker unchanged (YxmSCElKdm0 repeats the "four companies" licensing disclosure already noted).
- check.py --links: ERRORS 0. Published to inner-breeze-5fr8 (version 01M63XT3Z373ND3H6J8FBRTZGS). The box lacks the `file` utility (apt mirror returned 500), so publish.sh ran with a fallback shim returning application/octet-stream for unknown extensions only.

## [2026-11-05] weekly refresh
- Feed: 3 videos (Narcis Marincat "Is consciousness popularity?" 11/5, "Thoughts as Thinkers ... within & without us" 10/31, Conversation #1 with Martin Šolc 10/30), 2 preprints (topoietic model of collective morphogenesis, 11/4; enteroendocrine L-cells, 11/4), 1 blog post (Interactive MindMap, 11/4), 3 X posts (11/1 to 11/4). Fixed HTML italics in the topoietic preprint title from Crossref. Skipped one 11/5 X post that is media-only with no words to quote.
- Captions pulled with the vaulted-cookie yt-dlp method for all 3 videos; 3 video pages written, every quote checked word for word against the captions. Transcripts in raw/transcripts/. whats-new.md, index.md and topic hubs updated. Companies tracker: added the 10/31 "three or four companies" licensing disclosure.
- check.py --links: ERRORS 0. Published to inner-breeze-5fr8 (version 01M6P1SH3SK4AQE8VTGGJ6KJG2), authenticated, first try, using the same /tmp/fileshim fallback for the missing `file` utility.

## [2026-11-12] weekly refresh
- Feed: 2 videos (Glanzman "Evidence for intracellular memory storage and its implications for AI" 11/11, Siegelmann "Super Turing Computing" 11/6), 1 X post ("A beautiful animal" 11/12). No new Crossref papers or blog posts. Skipped X posts that are only a link or nature photography (11/5 and 11/6 link-only posts, 11/10 and 11/11 #naturephotography).
- Captions pulled with the vaulted-cookie yt-dlp method for both videos; 2 video pages written, quotes checked word for word against the captions. Transcripts in raw/transcripts/. whats-new.md, index.md and topic hubs updated. Companies tracker: no change.
- check.py --links: ERRORS 0 (one transient error on first run, clean on rerun). Published to inner-breeze-5fr8 (version 01M782YMWKB7WTGD8D42VJEE51), authenticated, first try, using the /tmp/fileshim fallback for the missing `file` utility.

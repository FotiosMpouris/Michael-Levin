---
title: "Deep Learning in Biology"
created: 2026-10-15
updated: 2026-10-15
type: video
video_id: S-seCBLDFsw
published: 2026-10-15
tags: [#video, #ai-and-biology]
sources: [raw/transcripts/2026-10-15-S-seCBLDFsw.txt]
---

# Deep Learning in Biology

- **Date published:** 2026-10-15
- **Speakers:** Dr. Edo Dotan (guest talk to the Levin lab)
- **Format:** Guest talk
- **Watch:** https://www.youtube.com/watch?v=S-seCBLDFsw
- **Topics:** [[ai-and-biology|AI and biology]]

## In one paragraph

Edo Dotan, a bioinformatics PhD working between natural-language processing and biology, explains how the language-model recipe carries over to DNA and protein sequences, and presents a system that reads a protein sequence and writes a plain-English description of what it does.

## Main ideas (plain words)

- Biology is largely written in sequences (DNA, proteins), so architectures built for text transfer well. The hard difference: in English we know the grammar; in biology the rules exist but we do not know them, and checking an answer can take weeks of lab work.
- Tokenization matters. Learned tokenizers (instead of one letter per nucleotide or amino acid) cut sequence length and, in his tests, also raised accuracy — one tokenizer cut tokens by about 3x and improved accuracy by more than 20% on a dataset.
- The protein-to-text system is a pipeline, not one model: a generator writes several candidate descriptions, validator models predict simple properties (location in the cell, enzyme or not), and an external LLM acts as judge to reject descriptions that do not fit.
- It beats BLAST-style similarity search for proteins with no close relatives in the database, but loses when a close match exists. Practical rule: run BLAST first; use the model when nothing is found.
- Masking experiments show the model learned real biology on its own (for insulin it keyed on the A and B chains) without being told where the important regions are.

## Why it matters

This is the AI side of Levin's program: if machine models can translate the 'language' of molecules into human language, the same move may later work on bioelectric patterns. It also sits next to Levin's stated goal of talking to gene regulatory networks in English (see the Bohórquez/Serruya conversation).

## Key quotes (word for word from YouTube's auto-generated captions)

Quotes are copied exactly from the captions, including filler words and caption errors. Timestamps are to the nearest minute.

> "in English the the rules are known okay you can teach them in school but in biology they are rules but we don't know them"  
> — [9 min](https://www.youtube.com/watch?v=S-seCBLDFsw&t=540s)

> "if you are training a transformer and I think you should probably at least check or verify your tokenizer because the simplest you know one token per nucleotide or amino acid is not always the best solution"  
> — [22 min](https://www.youtube.com/watch?v=S-seCBLDFsw&t=1320s)

> "So if you have unknown protein that is doesn't have any heat in any database so you can use this kind of system"  
> — [43 min](https://www.youtube.com/watch?v=S-seCBLDFsw&t=2580s)

## Related

[[whats-new|What's new]] · [[companies-tracker|Companies tracker]] · [[vision|Connections to Fotios's vision]] · transcript: `raw/transcripts/2026-10-15-S-seCBLDFsw.txt`

# Writing Notes: Ch12 NLP Part 2 — Sections 4–7

**Date:** 2026-03-13
**Agent:** Research+Writer (Sonnet)
**Status:** COMPLETE — written to ch12-nlp-voice-assistants.tex

---

## Card Count

- Section 4 (LLMs/GenAI): 13 cards across 5 subsections
- Section 5 (Applications): 8 cards across 5 subsections
- Section 6 (Challenges): 6 cards across 3 subsections
- Section 7 (Further Reading): 1 card

**Total: 28 cards**

---

## Structure

### 4.1 Pre-training and Fine-tuning (3 cards)
1. Pre-training Objectives (raster multicolumn=3) — MLM vs causal LM
2. Transfer Learning (raster multicolumn=3) — what transfers, why it works
3. Fine-tuning Strategies (raster multicolumn=6) — SFT, few-shot, zero-shot table

### 4.2 BERT (3 cards)
4. BERT Architecture (raster multicolumn=3) — bidirectional encoder, inputs, sizes
5. Pre-training: MLM and NSP (raster multicolumn=3) — masking procedure, NSP
6. Fine-tuning BERT (raster multicolumn=6) — CLS token, tasks, results

### 4.3 GPT Family (3 cards)
7. GPT Architecture (raster multicolumn=3) — decoder-only, causal attention
8. GPT Evolution and Scaling (raster multicolumn=3) — GPT-1/2/3/4, scaling laws
9. Emergent Abilities (raster multicolumn=6) — capabilities at scale, examples

### 4.4 Prompt Engineering (2 cards)
10. Prompting Strategies (raster multicolumn=3) — zero/few-shot, CoT
11. System Prompts and Templates (raster multicolumn=3) — structure, best practices

### 4.5 RAG (2 cards)
12. RAG: Motivation and Pipeline (raster multicolumn=6) — diagram-like description
13. Vector Databases and Chunking (raster multicolumn=6) — implementation details

### 5.1 Machine Translation (1 card)
14. Machine Translation (raster multicolumn=3)

### 5.2 Information Extraction (2 cards)
15. NER and Sentiment Analysis (raster multicolumn=3)
16. Summarization and QA (raster multicolumn=3)

### 5.3 Chatbots and Voice Assistants (2 cards)
17. Task-Oriented Dialogue (raster multicolumn=3)
18. Open-Domain Chatbots (raster multicolumn=3)

### 5.4 NLP in Education (1 card)
19. NLP in Education (raster multicolumn=3)

### 5.5 NLP for Accessibility (2 cards)
20. Text Simplification (raster multicolumn=3)
21. Captioning and Speech Accessibility (raster multicolumn=3)

### 6.1 Data Quality and Bias (2 cards)
22. Training Data Bias (raster multicolumn=3)
23. Fairness and Representation (raster multicolumn=3)

### 6.2 Domain and Language Adaptation (2 cards)
24. Multilingual Models (raster multicolumn=3)
25. Domain Shift and Low-Resource Languages (raster multicolumn=3)

### 6.3 Explainability and Safety (2 cards)
26. Hallucination (raster multicolumn=3)
27. Alignment and RLHF (raster multicolumn=3) [also TikZ skipped — no significant diagram value]

### Section 7: Further Reading (1 card)
28. Recommended Sources for NLP and Generative AI (raster multicolumn=6)

---

## Notes on Style Compliance
- All citations use `\textsuperscript{\cite[][p.~XX]{key}}` format
- Titles with commas use `title={...}` braced form
- No `\subsubsection` used — only `\subsection` with `tcbitemize` cards
- Table in Section 4.1 uses `tblr` environment
- No TikZ diagrams (none would significantly aid understanding here beyond what prose+table conveys)
- raster multicolumn=3 for half-width, =6 for full-width

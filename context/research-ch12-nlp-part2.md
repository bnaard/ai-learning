# Research Notes: Ch12 NLP Part 2 — Generative AI/LLMs, Applications, Challenges

**Date:** 2026-03-13
**Agent:** Research+Writer (Sonnet)
**Task:** Sections 4–7 of Ch12

---

## Sources Consulted

1. **Dhamani et al. (2024) — Introduction to Generative AI** (`dhamaniIntroductionGenerativeAI2024`)
   - Ch1: Evolution of NLP, attention, transformers, BERT/GPT history
   - Key: fine-tuning defined as "taking a model trained on a large dataset and then tuning or tweaking it" (p.9)
   - LLMs trained on self-supervised objectives: predict next token given context
   - BERT: 100M+ parameters, BooksCorpus + Wikipedia, bidirectional encoder
   - GPT-1 (2018): generative pre-training on internet data, then fine-tuned
   - GPT-3 (2020): massive scale, few-shot capability
   - Applications: QA (extractive, open-book generative, closed-book generative), content generation, coding, conversation

2. **Farris, Biderman & Raff (2025) — How Large Language Models Work** (`farrisHowLargeLanguage2025`)
   - Ch1: LLMs as GPT = Generative Pretrained Transformer; scaling is key (bigger data + more params)
   - Ch2: Tokenization — subword tokens, vocabulary, normalization→segmentation→mapping
   - Ch3: Transformer architecture: word embedding → positional embedding → transformer layers (L times) → unembedding → sampling → decoding
   - Ch4: Learning = gradient descent + reward functions; LLMs learn to mimic human text via cross-entropy loss on next-token prediction; RLHF
   - Ch5: Fine-tuning — supervised fine-tuning (SFT), RLHF; RAG (p.82): combines LLM embeddings with retrieval to customize behavior without retraining
   - Ch7: Few-shot learning, emergent abilities, misconceptions about LLMs

3. **Devlin et al. (2019) — BERT** (`devlinBERTPretrainingDeep2019`)
   - BERT = Bidirectional Encoder Representations from Transformers
   - Pre-training tasks: (1) MLM: 15% of tokens masked, predict masked token; (2) NSP: binary classification of sentence pairs
   - Architecture: BERT_BASE (L=12, H=768, A=12, 110M params), BERT_LARGE (L=24, H=1024, A=16, 340M params)
   - [CLS] token: first token in every sequence; final hidden state used for classification
   - Fine-tuning: add one output layer; plug in task-specific inputs/outputs; fine-tune all parameters end-to-end
   - SOTA on GLUE, SQuAD 1.1/2.0, SWAG, CoNLL NER
   - Pre-training data: BooksCorpus (800M words) + English Wikipedia (2500M words)

4. **Raschka (2025) — Build a Large Language Model (From Scratch)** (`raschkaBuildLargeLanguage2025`)
   - Three stages: (1) data prep + architecture, (2) pre-training, (3) fine-tuning (classifier or instruction following)
   - GPT architecture: decoder-only, autoregressive, causal attention mask
   - BPE tokenization; sliding window data sampling
   - Pre-training loss: cross-entropy on next-token prediction
   - Fine-tuning for classification: add classification head
   - Instruction fine-tuning: (instruction, input, output) triplets; LoRA for parameter-efficient fine-tuning

---

## Key Concepts

### Section 4: LLMs and Generative AI

**4.1 Pre-training and Fine-tuning**
- Pre-training on large unlabeled corpus with self-supervised objective (MLM or causal LM)
- Transfer learning: pre-trained representations transfer to downstream tasks
- Fine-tuning: adapt with labeled data; adds one output layer
- Few-shot: examples in prompt; zero-shot: task instruction only; chain-of-thought: "think step by step"

**4.2 BERT**
- Bidirectional encoder — conditions on both left AND right context at every layer
- MLM: 15% tokens masked; NSP: predict if B follows A
- [CLS] token = aggregate sequence representation for classification; [SEP] separates sentences
- Input = token embedding + segment embedding + position embedding
- BERT_BASE: 110M params, 12 layers; BERT_LARGE: 340M params, 24 layers

**4.3 GPT Family**
- Decoder-only transformer: causal (left-to-right) attention, autoregressive generation
- GPT-1 (2018) → GPT-2 (2019, 1.5B) → GPT-3 (2020, 175B) → GPT-4 (2023, multimodal)
- Scaling laws: performance scales with compute, data, and parameters
- Emergent abilities: capabilities not present at small scale, appearing at large scale

**4.4 Prompt Engineering**
- Zero-shot: task description only; few-shot: k=1..8 examples in context
- Chain-of-thought (CoT): "think step by step" → improved multi-step reasoning
- System prompts: pre-pended instructions shape behavior (persona, format, restrictions)

**4.5 RAG (Retrieval-Augmented Generation)**
- Problem: LLMs have knowledge cutoff and hallucinate facts
- RAG pipeline: (1) embed query → (2) vector similarity search → (3) retrieve top-k chunks → (4) LLM generates with context
- Vector databases (FAISS, Pinecone, Weaviate) store document embeddings
- Chunking: split documents into fixed-size or semantic chunks

### Section 5: Applications (concise)
- Machine Translation: seq2seq + attention → transformer-based (Google NMT)
- NER, sentiment, summarization, QA
- Chatbots: task-oriented (slot filling) vs open-domain (GPT-based)
- NLP in Education: automated grading, tutoring
- NLP for Accessibility: text simplification, captioning

### Section 6: Challenges
- Data/Bias: training data reflects societal biases; representation disparity
- Domain/Language: low-resource languages, domain shift, multilingual models
- Safety: hallucination, alignment, RLHF, interpretability

---

## BibTeX Keys Confirmed
- `dhamaniIntroductionGenerativeAI2024`
- `farrisHowLargeLanguage2025`
- `bahreeGenerativeAIAction2024`
- `raschkaBuildLargeLanguage2025`
- `devlinBERTPretrainingDeep2019`
- `vaswaniAttentionAllYou2023`
- `anticPythonNaturalLanguage2021`
- `bengioNeuralProbabilisticLanguage`

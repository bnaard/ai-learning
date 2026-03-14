# Research Notes: Ch12 NLP and Generative AI — Sections 1–3

**Date:** 2026-03-13
**Agent:** Research+Writer (Sonnet 4.6)
**Sources:** Farris et al. (2025), Dhamani et al. (2024), Devlin et al. (2019), Vaswani et al. (2023), Fleuret (Little Book of DL)

---

## Section 1: NLP Foundations

### 1.1 What is NLP?
- NLP = building machines to manipulate human language to accomplish useful tasks (Dhamani ch.1 p.3)
- Intersects computer science and linguistics
- First imagined use of computers was machine translation (1940s)
- Turing test (1950): machine indistinguishable from human in text conversation — early NLP benchmark
- ELIZA (1966, Weizenbaum/MIT): rule-based pattern-matching chatbot
- Transition 1990s: rule-based → statistical methods (better on translation, POS tagging)
- 2006: Google Translate — first commercially successful NLP system
- 2013: Word2Vec (Google) — dense word embeddings
- 2017: Transformer (Vaswani et al.) — dominant architecture
- 2018: GPT-1 (OpenAI), BERT (Google) — pre-trained LLMs
- Core challenges: ambiguity (lexical, syntactic), context-dependence, language variety, sarcasm/pragmatics

### 1.2 Linguistic Building Blocks
- **Morphology**: study of word forms — inflection (run/ran), derivation (happy/happiness), compounding
- **Syntax**: grammatical structure — parse trees, constituency vs dependency parsing
- **Semantics**: meaning of words and sentences — word sense disambiguation, compositionality
- **Pragmatics**: language use in context — speaker intent, discourse, indirect speech
- **Prosody** (for speech): rhythm, stress, intonation patterns that modify meaning

### 1.3 Tokenization
Source: Farris et al. ch.2 (pp.14–28)

- **Token**: smallest unit of text an LLM processes — "atom" of language (p.15)
- Tokenization pipeline (4 steps, p.17):
  1. Receive text as string
  2. Normalize string (lowercase, remove punctuation, Unicode normalization)
  3. Segment string into tokens
  4. Map each token to a unique integer ID
- **Word tokenization**: split on whitespace — simple but fails for compound words, languages without spaces (Chinese), punctuation
- **Byte Pair Encoding (BPE)** (Farris p.20–22):
  - Start with individual characters as vocabulary
  - Iteratively merge most frequent adjacent pairs into subword tokens
  - Continues until vocabulary reaches target size
  - Used by GPT/tiktoken; also WordPiece (BERT), SentencePiece (multilingual)
  - "loquacious" → lo + qu + acious
  - Common words get single tokens; rare words decompose into subwords
- **Why subword tokenization dominates**:
  - Handles OOV (out-of-vocabulary) words by decomposition
  - Vocabulary size manageable (GPT-3: 50,257 tokens)
  - Works across multiple languages
  - Captures morphological structure (un + happy + ness)
- **Vocabulary**: complete set of unique tokens seen during training
- Trade-off: larger vocabulary → richer representation but larger model
- Token != word: "I'm running" = 3 tokens; "I'm runnin" = 4 tokens (BPE is greedy, p.23)

### 1.4 Evaluation of NLP Systems
- **Perplexity**: PP = exp(-(1/N) Σ log P(wᵢ|context)) — lower = better LM
- **BLEU**: n-gram precision between hypothesis and reference — machine translation
- **ROUGE**: recall-based overlap — summarization (ROUGE-N, ROUGE-L)
- **F1**: harmonic mean of precision/recall — NER, QA, classification
- **GLUE/SuperGLUE**: multi-task NLU benchmarks; BERT_LARGE scores 82.1 (Devlin p.5)
- **Human evaluation**: gold standard for fluency and coherence; expensive

---

## Section 2: Text Processing and Representation

### 2.1 Word Vectors and Embeddings
- **Bag-of-Words**: document as word frequency vector — ignores order
- **TF-IDF**: TF × log(N/df) — downweights common words
- **Word2Vec** (Mikolov et al. 2013): CBOW (predict center from context) / Skip-gram (predict context from center); 300-dim vectors; "king - man + woman ≈ queen" (Farris p.36)
- **GloVe** (Pennington et al. 2014): global co-occurrence statistics
- Static embeddings: same vector regardless of context ("bank" = financial vs river)
- **Contextual embeddings**: ELMo (biLSTM), then BERT — word representation depends on full sentence context

### 2.2 Statistical and Classical NLP
- **N-gram LM**: P(wₙ|w₁..wₙ₋₁) ≈ P(wₙ|wₙ₋ₙ₊₁..wₙ₋₁) — Markov assumption
- Bengio et al. (2003): neural probabilistic language model — first neural n-gram model
- **Naive Bayes**: P(class|doc) ∝ P(class) × ΠP(wᵢ|class) — fast text classification
- **HMM** (Hidden Markov Model): for POS tagging — hidden states (POS tags) emit observed words
- **CRF** (Conditional Random Field): discriminative sequence model; better than HMM for NER

### 2.3 RNN-Based Approaches
- LSTM/GRU: gated RNNs that handle long-range dependencies
- **Seq2seq** (Sutskever et al. 2014): encoder → context vector → decoder; for MT, summarization
- **Bahdanau Attention** (2014): decoder attends to all encoder hidden states
  - cₜ = Σ αₜᵢ hᵢ; αₜᵢ = softmax(score(sₜ₋₁, hᵢ))
- Limitation: sequential, hard to parallelize → superseded by transformers

### 2.4 Transformer-Based NLP
- Vaswani et al. (2017): self-attention replaces recurrence entirely
- att(K,Q,V) = softmax(QKᵀ/√D) V — see Ch.6 for full derivation
- Encoder-only (BERT): bidirectional context; best for classification/NER/QA
- Decoder-only (GPT): causal/autoregressive; best for generation
- Encoder-decoder (T5, mT5): seq2seq tasks like translation
- **BERT** (Devlin et al. 2019):
  - Pre-training: Masked LM (predict 15% masked tokens) + Next Sentence Prediction
  - WordPiece vocab 30k; BERT_BASE: 110M params; BERT_LARGE: 340M params
  - Fine-tuning: single additional output layer for downstream tasks
  - GLUE: 82.1 (LARGE) vs 74.0 (pre-BERT SOTA), SQuAD F1: 93.2
- **GPT family**:
  - GPT-1 (2018): pre-train on BooksCorpus, fine-tune on tasks
  - GPT-3 (2020): 175B params, few-shot in-context learning without fine-tuning
  - GPT-4 (2023): multimodal, best-in-class benchmark performance

---

## Section 3: Speech Processing

### 3.1 ASR
- Classical: acoustic model (HMM-GMM) + language model (n-gram) + pronunciation lexicon
- Bayes combination: P(word|audio) ∝ P(audio|word) × P(word)
- MFCC features (Mel-Frequency Cepstral Coefficients) as acoustic features
- **CTC** (Graves et al. 2006): end-to-end — aligns audio to text without pre-segmentation; allows blank tokens
- **Whisper** (Radford et al., OpenAI 2022): transformer encoder-decoder; 680k hours training; multilingual; end-to-end (no separate acoustic model)

### 3.2 TTS
- **Concatenative**: stitch diphones/units from database — high quality, inflexible
- **Parametric (HMM-based)**: model vocal tract parameters — flexible, robotic quality
- **WaveNet** (van den Oord et al., DeepMind 2016): dilated causal CNN; generates raw audio sample-by-sample; very high quality
- **Tacotron 2** (Google 2018): seq2seq text → mel spectrogram, then WaveNet vocoder
- Modern: FastSpeech (transformer, non-autoregressive), diffusion vocoders

---

## BibTeX Keys Confirmed
- `farrisHowLargeLanguage2025`
- `dhamaniIntroductionGenerativeAI2024`
- `devlinBERTPretrainingDeep2019`
- `vaswaniAttentionAllYou2023`
- `fleuretLittleBookDeep`
- `bengioNeuralProbabilisticLanguage`
- `openaiGPT4TechnicalReport2023`

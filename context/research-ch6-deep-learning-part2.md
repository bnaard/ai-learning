# Research Notes: Ch6 Deep Learning — Sections 4–6
**Date:** 2026-03-13
**Sources:** Fleuret (Little Book of Deep Learning, pp. 73–99, 124–126), Vaswani et al. 2023 (Attention Is All You Need), Dhamani & Engler (Introduction to Generative AI, 2024)

---

## Section 4: Alternative Training Methods

### 4.1 Attention Mechanism (Fleuret §4.8, pp. 73–79; Vaswani et al. 2017)
- Attention layers aggregate features across entire input tensor without locality constraints
- Attention operator att(Q, K, V): Q = queries, K = keys, V = values
- Attention(Q,K,V) = softmax(QK^T / √d_k) V
- Scaling factor 1/√d_k prevents softmax saturation
- Causal masking: upper-diagonal set to −∞ before softmax
- Multi-Head Attention adds learned projection matrices
- Self-attention: Q = K = V from same sequence; Cross-attention: Q from one, K/V from another

### 4.2 Transformer Architecture (Vaswani et al. 2017; Fleuret §5.3)
- Why transformers replaced RNNs: O(1) sequential ops vs O(n) for RNNs; parallelizable
- Encoder: N=6 layers; multi-head self-attention + FFN; residual + LayerNorm
- Decoder: N=6 layers; masked self-attention + cross-attention + FFN
- Positional encoding: sinusoidal PE(pos,2i) = sin(pos/10000^(2i/d))
- GPT: decoder-only, causal, autoregressive
- BERT: encoder-only, bidirectional, masked LM

### 4.3–4.5 Feedback Alignment, Synthetic Gradients, DNI
- Feedback alignment: replace W^T with fixed random B
- Synthetic gradients: DNI module predicts gradient without full backward pass
- Decoupled interfaces: removes update and forward locking

## Section 5: Further Network Architectures

### 5.1 GANs (Goodfellow et al. 2014, Fleuret p.125)
- Generator G(z) vs Discriminator D(x); minimax game
- Mode collapse, training instability

### 5.2 Autoencoders + VAE (Fleuret p.125)
- Encoder → bottleneck → decoder; MSE reconstruction loss
- VAE: reparameterization trick; ELBO loss with KL term

### 5.3 RBMs — Energy-based, contrastive divergence CD-k
### 5.4 Capsule Networks — Dynamic routing, equivariance
### 5.5 Spiking Networks — LIF model, neuromorphic hardware

## BibTeX Keys
- `fleuretLittleBookDeep`, `vaswaniAttentionAllYou2023`, `dhamaniIntroductionGenerativeAI2024`
- `farrisHowLargeLanguage2025`, `devlinBERTPretrainingDeep2019`
- `krieselBriefIntroductionNeural2007`, `fischerVorlesungGrundlagenNeuronale2024`

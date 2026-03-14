# Project Progress Tracker

## Last Updated: 2026-03-14 - Ch19 Visualization COMPLETE

## Current Phase: Phase 2 — Content Production (Ch8 Functional Security or Ch18b Visualization next)

### Document Analysis Summary
The document has 20 chapter files. Content completeness:

| Chapter | Status | Completeness |
|---------|--------|-------------|
| **1. Introduction to AI & DA** | **DONE** | **~95% (content complete, latest commit)** |
| **2. Mathematical Foundations** | **DONE** | **~95% (content complete, latest commit)** |
| **3. Programming Foundations** | **DONE** | **~95% (content complete, latest commit)** |
| **4. Data Analytics Foundations** | **DONE** | **~95% (content complete, latest commit)** |
| **5. Machine Learning** | **DONE** | **~95% (52 cards, 8 sections, 8 TikZ diagrams, Further Reading)** |
| **6. Deep Learning** | **DONE** | **~95% (49 cards, 6 sections, 20 subsections, 4 TikZ diagrams, Further Reading)** |
| **7. Reinforcement Learning** | **DONE** | **~95% (~59 cards, 7 sections, 2 TikZ diagrams, Further Reading)** |
| 8. Functional Security | Stub | ~0% (outline only) |
| **9. Computer Vision** | **DONE** | **~95% (Sec 1-2: 24 cards; Sec 3-6: ~34 cards, 7 sections, Further Reading)** |
| **10. AI in FinTech** | **DONE** | **~95% (~40 cards, 6 sections, 17 subsections, Further Reading)** |
| **11. AI in Healthcare** | **DONE** | **~95% (~40 cards, 6 sections, 14 subsections, 21 new bib entries, Further Reading)** |
| **12. NLP & Generative AI** | **DONE** | **~95% (51 cards: all 7 sections complete, Further Reading)** |
| **13. Industrial AI** | **DONE** | **~95% (40 cards, 6 sections, 15 subsections, 20 new bib entries, Further Reading)** |
| **14. AI in Supply Chain** | **DONE** | **~95% (~38 cards, 6 sections, 15 subsections, 15 new bib entries, Further Reading)** |
| **15. Multi-Agent Systems** | **DONE** | **~95% (~40 cards, 8 sections, 16 subsections, 6 new bib entries, Further Reading)** |
| **16. AI in E-Commerce, Marketing** | **DONE** | **~95% (~43 cards, 4 sections, 14 subsections, 11 new bib entries, Further Reading)** |
| **19. Visualization** | **DONE** | **~95% (38 cards, 5 sections, 10 subsections, 1 TikZ, Further Reading)** |
| 17-18, 20. Various | Empty/Stub | ~0% |

### Ch5 Machine Learning — Completed Structure
- 5.1 Introduction to ML (5 subsections, 9 cards)
  - What is ML?, Supervised/Unsupervised, Regression/Classification, RL overview, Model Eval & Overfitting
- 5.2 Clustering (5 subsections, 17 cards)
  - Intro, K-Means, EM/GMM, DBSCAN, Hierarchical
- 5.3 Regression (5 subsections, 7 cards)
  - Linear/Nonlinear, Logistic, Quantile, Multivariate, Lasso/Ridge
- 5.4 Support Vector Machines (3 subsections, 5 cards)
  - Intro (margin, soft-margin), Classification (kernel trick), Regression (SVR)
- 5.5 Decision Trees & Ensemble Methods (5 subsections, 7 cards)
  - Intro, Classification, Regression, Random Forests, Gradient Boosting
- 5.6 Nearest Neighbor Methods (2 subsections, 3 cards)
  - k-NN, Distance Metrics
- 5.7 Genetic Algorithms (2 subsections, 4 cards)
  - Intro (terminology, lifecycle, operators), Applications
- 5.8 Further Reading (1 card with \fullcite references)

### Task Queue

#### Phase 1: Analysis & Planning (COMPLETE)
- [x] All planning tasks completed (see previous sessions)
- [x] Ch5 structure revision approved
- [x] Ch2/Ch6/Ch12 structural additions: APPROVED by author

#### Phase 2: Core Content (IN PROGRESS)
- [x] Ch 1: Introduction — COMPLETE (latest commit)
- [x] Ch 2: Mathematical Foundations — COMPLETE (latest commit)
- [x] Ch 3: Programming Foundations — COMPLETE (latest commit)
- [x] Ch 4: Data Analytics Foundations — COMPLETE (latest commit)
- [x] Ch 5: Machine Learning — COMPLETE (52 cards, 8 sections, 25 subsections)
- [x] Ch 6: Deep Learning — COMPLETE (49 cards, 6 sections, 20 subsections, 4 TikZ diagrams)
- [x] Ch 7: Reinforcement Learning — COMPLETE (~59 cards, 7 sections: Intro, MDP, Bandits, Q-Learning/DRL, RL Approaches, Inference & Causality, Further Reading)
- [x] Ch 12: NLP & Generative AI — COMPLETE (~51 cards, 7 sections: NLP Foundations, Text Processing, Speech Processing, LLMs/GenAI, Applications, Challenges, Further Reading)
- [ ] Ch 9-16: Domain applications

#### Phase 3: Integration & Polish (PLANNED)
- Cross-reference consistency
- Bibliography cleanup
- Build verification

### Ch6 Deep Learning — Completed Structure
- 6.1 Introduction to NN & DL (3 subsections, 8 cards)
  - Biological Brain, Perceptron & MLPs, Activation Functions
- 6.2 Network Architectures (3 subsections, 8 cards)
  - Feed-Forward Networks, Convolutional Networks, RNNs/LSTMs
- 6.3 Neural Network Training (5 subsections, 12 cards)
  - Forward Pass & Loss Functions, Weight Initialization, Backprop & GD, Training Loop, Regularization
- 6.4 Alternative Training Methods (5 subsections, 11 cards)
  - Attention, Transformer Architecture (5 cards + TikZ), Feedback Alignment, Synthetic Gradients, Decoupled Interfaces
- 6.5 Further Network Architectures (5 subsections, 9 cards)
  - GANs, Autoencoders/VAE, RBMs, Capsule Networks, Spiking Networks
- 6.6 Further Reading (1 card with \fullcite references)

### Ch7 Reinforcement Learning — Completed Structure (ALL Sections)
- 7.1 Introduction to RL (5 cards, 1 TikZ)
  - What is RL?, Reward Hypothesis, Agent-Environment Loop (TikZ), Core Components, RL vs Supervised/Unsupervised
- 7.2 Markov Decision Processes (9 cards, 1 TikZ)
  - Markov Property, MDP Definition, Discounted Return G_t, Value Functions, Bellman Equations, Value Iteration, MDP State Diagram (TikZ), Policy Types, MCMC
- 7.3 Bandit Problems (4 cards)
  - Multi-Armed Bandit, ε-greedy, UCB, Thompson Sampling
- 7.4 Q-Learning and Deep RL (9 cards)
  - TD Learning, SARSA vs Q-Learning, DQN, Experience Replay, Double Q-Learning, Sparse Rewards, Hierarchical RL, Value vs Policy-Based, Actor-Critic
- 7.5 RL Approaches (11 cards)
  - Model-Free RL, Q-Learning Update, SARSA, REINFORCE; Model-Based RL, Dyna-Q, World Models/MPC; Exploration-Exploitation, ε-Greedy, UCB, Curiosity-Driven
- 7.6 Inference and Causality (20 cards)
  - Bayesian Inference, Bayesian vs Frequentist, Bayesian Networks (wide), Probabilistic Modelling, Conditional Independence
  - Correlation vs Causation, Granger Causality, DAGs, Fork/Chain/Collider, D-Separation (wide)
  - Seeing vs Doing, Confounders, Counterfactuals, Causal Inference vs RCTs
  - Backdoor Criterion, Front-Door Criterion, Three Rules of Do-Calculus (wide)
  - Simpson's Paradox, Collider Bias/Berkson, Mediation Fallacy, Missing Values (Causal View)
- 7.7 Further Reading (1 wide card, 9 fullcite references)

### Ch12 NLP & Generative AI — Completed Structure
- 12.1 NLP Foundations (sections 1–3, ~23 cards — written by prior agent)
  - NLP overview, text processing pipeline, speech processing and ASR
- 12.2 Large Language Models and Generative AI (13 cards, 5 subsections)
  - Pre-training and Fine-tuning, BERT Architecture, GPT Family, Prompt Engineering, RAG
- 12.3 Application Scenarios (10 cards, 5 subsections)
  - Machine Translation, Information Extraction, Chatbots/Voice Assistants, NLP in Education, NLP for Accessibility
- 12.4 Challenges in NLP (6 cards, 3 subsections)
  - Data Quality and Bias, Domain and Language Adaptation, Explainability and Safety
- 12.5 Further Reading (1 wide card, 8 fullcite references)

### Active Assignments
| Agent | Task | Status | Started |
|-------|------|--------|---------|
| Coordinator | Plan next chapter (Ch9 CV or other) | READY | Now |
| Research+Writer | Ch12 NLP/GenAI sections 1–3 | COMPLETE | 2026-03-13 |
| Research+Writer | Ch12 NLP/GenAI sections 4–7 (LLMs, Applications, Challenges, Further Reading) | COMPLETE | 2026-03-13 |

### Author Decisions Log
- Priority: Tier 1-4 approved as proposed
- Depth: "One thing to grasp per box", denser only where it makes sense
- TikZ: Only where they significantly aid understanding
- Literature: Merge inline lists → one big bib section; add "Further Reading" per chapter
- Excluded: IT Law, Startup, Scientific Writing. Visualization KEPT.
- Language: Use all sources; content always in English
- Structure changes: Must be proposed and confirmed by author
- Ch5 revised structure: APPROVED and IMPLEMENTED
- Ch2/Ch6/Ch12 structural additions for NN-from-scratch & LLM paths: APPROVED

### Key Decisions
- Content depth: Core concepts + key formulas, not full derivations
- Style: Match existing tcbitemize card format
- Citations: bibtex superscript style as in existing content
- Priority: ML → DL → Math → RL → DA → Programming → NLP/GenAI

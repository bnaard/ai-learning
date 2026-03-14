# Research Notes: Ch10 — AI in FinTech

## Date: 2026-03-14
## Researcher: Research+Writer Agent (Sonnet)

---

## Primary Sources

### Jansen, Stefan (2020). *Machine Learning for Algorithmic Trading*, 2nd ed. Packt. [jansenMachineLearningAlgorithmic2020]

Key content extracted:
- **Ch1 (pp.1–6)**: Rise of ML in investment industry; electronic trading evolution; HFT (55% of US equity volume, 40% in Europe); factor investing — CAPM, Fama-French factors; information ratio formula IR ≈ IC × √N; EMH and anomalies (value, size, momentum)
- **Ch4 (pp.82–84)**: Alpha factors: momentum (12-1 month return), value (P/B), quality (ROE), volatility, size; engineering from alternative data (NLP sentiment, satellite imagery)
- **Ch5 (pp.121–142)**: Portfolio optimization: Markowitz mean-variance frontier formula; Sharpe ratio; Black-Litterman Bayesian update formula; risk parity; hierarchical risk parity
- **Ch6 (pp.148–149)**: ML workflow for finance: supervised/unsupervised/RL; cross-validation challenges with financial time series
- **Ch7 (pp.173–219)**: Linear models for return forecasting; Fama-French factor models; ridge/lasso regularization
- **Ch8 (pp.221–254)**: Backtesting; look-ahead bias; survivorship bias; walk-forward validation; deflated Sharpe ratio
- **Ch11 (pp.327–364)**: Random forests for long-short strategy; feature importance; bootstrap aggregation
- **Ch12 (pp.365–406)**: Gradient boosting (XGBoost, LightGBM, CatBoost); SHAP values for interpretability
- **Ch14 (pp.439–462)**: NLP for finance: bag-of-words, sentiment analysis, Twitter/Yelp data
- **Ch17 (pp.513–549)**: Deep learning for trading; NN architecture optimization for long-short signals
- **Ch19 (pp.591–624)**: RNNs/LSTMs for multivariate time series and sentiment in SEC filings
- **Ch22 (pp.679–711)**: Deep RL for trading; MDP formulation; DQN; OpenAI Gym trading environment; Q-learning algorithm
- **Ch23 (pp.713–723)**: Conclusions: domain expertise critical; backtesting overfitting risks

### Kardell, Christopher & Brouwer, Mark (2025). *Build Financial Software with Generative AI (From Scratch)*. Manning. [kardellBuildFinancialSoftware2025]

Key content extracted:
- **Preface (pp.xii–xiii)**: Core banking software definition; ACH as primary payment infrastructure; Python/Java/COBOL in FinTech
- **Ch1 (pp.3–28)**: FinTech ecosystem; ACH dashboard project; generative AI as development aid (ChatGPT, Copilot for code); privacy/security considerations; GenAI for code generation, test writing, syntax help
- **Ch2 (pp.29–62)**: ACH file structure — file header (type 1), batch header (type 5), entry detail (type 6), addenda (type 7), batch control (type 8), file trailer (type 9); parsing ACH with Python
- **Ch11 (pp.355–392)**: IAT (International ACH Transactions); OFAC scanning; sanctions list; fuzzy matching in PostgreSQL for name screening
- **Ch12 (pp.393–404)**: Future directions — asynchronous processing, multi-tenancy, continuous integration, mobile front-ends, service charges

---

## Domain Knowledge (General / Widely Established)

### FinTech Definitions and Ecosystem
- FinTech = Financial Technology; term gained currency post-2008 crisis
- Neo-banks: Revolut (founded 2015, UK), N26 (Germany), Chime (USA), Monzo (UK)
- Open Banking: PSD2 (EU, 2018); AISPs and PISPs; UK Open Banking (2018); Australia CDR; USA exploring rulemaking
- ACH: US payment network processing ~30 billion transactions/year (Nacha 2023)

### Credit Scoring
- FICO model: payment history (35%), amounts owed (30%), length of history (15%), new credit (10%), mix (10%)
- Alternative data for credit: transaction cash flows, mobile metadata, psychometric scoring
- Fairness: ECOA disparate impact; GDPR Art.22; EU AI Act high-risk classification
- SHAP for credit explanation: widely used in industry compliance

### Fraud Detection
- Global card fraud losses: $33.8bn (Nilson Report 2022)
- Insurance fraud cost: ~$80bn/year US (Coalition Against Insurance Fraud)
- Wirecard collapse: June 2020; €1.9bn missing; EY audit failure; largest German financial fraud
- Class imbalance: SMOTE (Chawla et al. 2002); cost-sensitive learning; precision-recall curve optimization
- Real-time scoring: sub-100ms constraint; Redis for feature store; model serving via REST API

### Portfolio Theory and Robo-Advisory
- Markowitz MPT (1952): efficient frontier, mean-variance optimization
- Sharpe ratio (1966): risk-adjusted return metric
- Black-Litterman (1990): Bayesian blend of market equilibrium and investor views — addresses estimation error instability
- First robo-advisors: Betterment (2010), Wealthfront (2011)
- Market sizes: robo-advisory AUM ~$2.5 trillion globally (Statista 2023)
- Tax-loss harvesting: wash-sale rule 30-day window; Wealthfront claims 1.55–2.99% return improvement

### Regulation
- MiFID II (2018): algorithm registration, kill-switch, stress-testing, best execution
- EU AI Act (2024): credit scoring = high-risk; logging, transparency, human oversight required
- GDPR Art.22: right to explanation for automated decisions
- US FCRA: adverse action notice citing specific denial reasons

### Future Trends
- CBDCs: 130+ countries exploring (BIS 2023); programmable money use cases
- DeFi: TVL peaked ~$180bn in 2021; smart contract automation of financial services
- Embedded finance: Shopify Capital, Uber Money, BNPL integration
- ESG/sustainable finance: satellite + NLP for environmental monitoring; NGFS climate scenarios

---

## Bibliography Keys Available in references.bib
- `jansenMachineLearningAlgorithmic2020` — confirmed present
- `kardellBuildFinancialSoftware2025` — confirmed present

## Missing References (not in bib)
The books listed in the original chapter stub literature section (Arslanian, Boobier, Tatsat, Sironi, Narang, etc.) are NOT in references.bib. Only jansenMachineLearningAlgorithmic2020 and kardellBuildFinancialSoftware2025 are available as verified bib keys. All cards in the chapter use only these two keys as citations.

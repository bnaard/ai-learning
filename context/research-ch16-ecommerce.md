# Research Notes: Ch16 — AI in E-Commerce, Marketing and Demand Forecasting

## Date: 2026-03-14

## Primary Sources Used
- `leskovecMiningMassiveDatasets2014` — Leskovec, Rajaraman, Ullman (2014): Mining of Massive Datasets, 2nd ed., Cambridge UP.
  - Ch 9: Recommendation Systems — user-based CF, item-based CF, matrix factorisation, cosine similarity, RMSE
  - Ch 6: Frequent Itemsets — Apriori algorithm, anti-monotone property, support/confidence/lift formulas, FP-Growth
- `laudonECommerce2020` — Laudon & Traver (2020): E-Commerce 2020--2021: Business, Technology, Society, 16th ed., Pearson.
  - E-commerce AI landscape, programmatic advertising (RTB, DSP, SSP), pricing theory, price elasticity, Bayesian pricing, dynamic pricing ethics, dark patterns, GDPR
- `chaffeyDigitalBusinessECommerce2019` — Chaffey (2019): Digital Business and E-Commerce Management, 7th ed., Pearson.
  - IoT in retail, chatbots, voice search, visual search, marketing mix (4Ps), customer journey attribution, RFM segmentation, SEO/SEM, churn prediction, CLV, A/B testing, closed-loop marketing
- `aggarwalRecommenderSystems2016` — Aggarwal (2016): Recommender Systems: The Textbook, Springer.
  - History (Netflix Prize, Amazon), user-item matrix, feedback types, personalisation levels, evaluation metrics, neighbourhood CF, matrix factorisation biases, ALS for implicit feedback, cold-start problem, large-scale two-stage architecture, multi-stakeholder recommenders
- `jannachRecommenderSystemsIntroduction2010` — Jannach et al. (2010): Recommender Systems: An Introduction, Cambridge UP.
  - Levels of personalisation, hybrid approaches (weighted, switching, cascade, feature augmentation, meta-level)
- `korenMatrixFactorizationTechniques2009` — Koren, Bell, Volinsky (2009): Matrix Factorization Techniques for Recommender Systems, IEEE Computer.
  - SVD model with biases, ALS, implicit feedback confidence matrix
- `rendleBPRBayesianPersonalized2009` — Rendle et al. (2009): BPR: Bayesian Personalized Ranking from Implicit Feedback.
  - Pairwise ranking loss, model-agnostic application of BPR
- `rendleFactorizationMachines2010` — Rendle (2010): Factorization Machines, ICDM.
  - FM formula, pairwise interaction terms, unification of MF and content-based
- `chengWideDeepLearning2016` — Cheng et al. (2016): Wide & Deep Learning for Recommender Systems.
  - Wide (memorisation) + Deep (generalisation) architecture
- `heNeuralCollaborativeFiltering2017` — He et al. (2017): Neural Collaborative Filtering.
  - MLP replacing inner product in MF, NCF formula
- `liFaissLibraryEfficient2019` — Johnson, Douze, Jégou (2019): Billion-Scale Similarity Search with GPUs.
  - FAISS, IVF, HNSW, Product Quantisation
- `suttonReinforcementLearningIntroduction2018` — Sutton & Barto (2018): Reinforcement Learning: An Introduction.
  - MAB (epsilon-greedy, UCB, Thompson Sampling) for campaign optimisation; RL-based recommenders as MDP
- `itgovernanceprivacyteamEUGDPR2020` — IT Governance Privacy Team (2020): EU GDPR Implementation Guide.
  - Lawful basis, data minimisation, right to explanation, data portability for e-commerce
- `hyndmanForecastingPrinciples2021` — Hyndman & Athanasopoulos (2021): Forecasting: Principles and Practice.
  - Forecasting methods hierarchy: ARIMA, ETS, ML, deep learning
- `wickDemandForecastingIndividual2021` — Wick et al. (2021): Demand Forecasting with ML.
  - Demand estimation with ML; confounding in elasticity estimation
- `pearlCausalInferenceStatistics2016` — Pearl et al. (2016): Causal Inference in Statistics: A Primer.
  - Causal recommenders, exposure bias, IPS correction

## Key Concepts Synthesised

### Section 1: AI in E-Commerce
- **Data flywheel**: virtuous cycle of users → data → better models → more users
- **Long tail**: niche catalogue items collectively dominate in digital; recommenders make long tail accessible
- **Programmatic advertising**: RTB millisecond auctions; CTR/CVR prediction models
- **IoT retail**: RFID, CV cameras, beacons; cashierless checkout (Amazon Go)
- **Voice search**: conversational queries, single-result responses, position-1 criticality
- **Visual search**: CNN embedding + ANN retrieval pipeline
- **Price elasticity**: ε = ∂lnQ/∂lnP; elastic vs. inelastic
- **Bayesian optimal pricing**: posterior over demand params; Thompson Sampling for price A/B
- **RL pricing**: MDP formulation; surge pricing fairness concerns
- **Double ML**: causal price coefficient estimation from observational data
- **GDPR in e-commerce**: consent, minimisation, right to explanation, portability
- **Dark patterns**: prohibited by EU Digital Services Act 2022

### Section 2: Marketing Analytics
- **4Ps + 4Cs**: product, price, place, promotion + customer, cost, convenience, communication
- **Attribution models**: last-click, first-click, linear, data-driven (Shapley values)
- **RFM segmentation**: Recency-Frequency-Monetary scoring 1-5; champions = 555
- **Association rules**: support, confidence, lift formulas; lift > 1 = genuine association
- **Apriori**: anti-monotone pruning; FP-Growth improves with FP-tree
- **SEO signals**: relevance (BERT), authority (PageRank), UX (Core Web Vitals)
- **Churn prediction**: binary classification; survival models; SHAP explainability
- **CLV**: DCF formula with retention probability; Pareto/NBD for non-contractual
- **Sales forecasting**: ARIMA → ETS → ML (XGBoost) → DeepAR/N-BEATS/TFT
- **Propensity models**: P(action|features); uplift modelling = causal incremental effect
- **A/B testing**: randomised; MDE = f(σ/δ)²; pitfalls: peeking, novelty, interactions
- **MAB**: ε-greedy, UCB formula, Thompson Sampling; minimise regret during experiment
- **Upselling/cross-selling**: association rules + CF
- **Closed-loop automation vs. human-in-the-loop**: trade-off between scale and oversight

### Section 3: Recommender Systems
- **History**: GroupLens (1994), Amazon item-based (1998), Netflix Prize (2006-2009)
- **User-item matrix**: R ∈ R^(m×n); explicit vs. implicit feedback
- **Personalisation levels**: non-personalised → segment → collaborative → content-based → hybrid
- **Evaluation**: RMSE/MAE (rating), Precision@k, Recall@k, NDCG@k, Diversity, Coverage; online A/B for business impact
- **User-based CF**: rating prediction with weighted neighbour average; cosine/Pearson similarity
- **Item-based CF**: pre-computed item-item similarities; stable, scalable
- **Matrix factorisation (SVD)**: R ≈ PQ^T; biases; SGD optimisation with L2 regularisation
- **ALS**: confidence matrix c_ui = 1 + α·count_ui; closed-form solution; parallelisable
- **BPR**: pairwise ranking loss over (u, i+, j-) triples; σ(r̂_ui+ - r̂_uj-); model-agnostic
- **Content-based**: TF-IDF/BERT text; CNN image features; user profile as weighted item feature average
- **Factorisation Machines**: FM formula with pairwise interaction via <v_i, v_j>; unifies MF + content
- **Hybrid**: weighted, switching, cascade, feature augmentation, meta-level
- **Cold-start**: onboarding quiz; content-based fallback; exploration budget for new items
- **Two-stage retrieval**: retrieval (ANN, ~100 candidates) → ranking (Wide&Deep/transformer)
- **Two-tower model**: user tower + item tower; inner product as retrieval score
- **FAISS**: IVF (Voronoi partitions), HNSW (graph, O(log n)), PQ (compression)
- **Wide & Deep**: wide linear (memorisation) + deep MLP (generalisation)
- **NCF**: MLP replaces inner product; formula ŷ = σ(h^T · MLP([p_u || q_i]))
- **RL recommenders**: MDP formulation; avoids filter bubbles via diversity rewards
- **Causal recommenders**: exposure bias; IPS re-weighting
- **Multi-stakeholder**: user satisfaction + producer exposure fairness + platform revenue; Pareto-optimal re-ranking

## New Bibliography Entries Added
1. `aggarwalRecommenderSystems2016` — Aggarwal (2016): Recommender Systems: The Textbook, Springer
2. `jannachRecommenderSystemsIntroduction2010` — Jannach et al. (2010): Recommender Systems: An Introduction, Cambridge UP
3. `ricciRecommenderSystemsHandbook2015` — Ricci et al. (2015): Recommender Systems Handbook, 2nd ed., Springer
4. `rendleBPRBayesianPersonalized2009` — Rendle et al. (2009): BPR, UAI 2009
5. `rendleFactorizationMachines2010` — Rendle (2010): Factorization Machines, ICDM 2010
6. `chengWideDeepLearning2016` — Cheng et al. (2016): Wide & Deep Learning, RecSys workshop
7. `heNeuralCollaborativeFiltering2017` — He et al. (2017): Neural Collaborative Filtering, WWW 2017
8. `korenMatrixFactorizationTechniques2009` — Koren et al. (2009): Matrix Factorization Techniques, IEEE Computer
9. `liFaissLibraryEfficient2019` — Johnson et al. (2019): Billion-Scale Similarity Search (FAISS), IEEE Trans. Big Data
10. `chaffeyDigitalBusinessECommerce2019` — Chaffey (2019): Digital Business and E-Commerce Management, 7th ed., Pearson
11. `laudonECommerce2020` — Laudon & Traver (2020): E-Commerce 2020-2021, 16th ed., Pearson

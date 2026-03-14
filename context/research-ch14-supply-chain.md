# Research Notes: Chapter 14 — AI in Supply Chain Management

## Date
2026-03-14

## Knowledge Sources Used
- No primary PDF books available for this chapter
- General knowledge of operations research and supply chain management
- Bibliography scan of `bibliography/references.bib` for relevant existing keys

## Bibtex Keys Added to references.bib
All entries appended after `astarPathPlanning1968` at line 5354:

| Key | Source |
|-----|--------|
| `chopraSupplyChainManagement2019` | Chopra & Meindl, Pearson 7th ed. |
| `vandeputInventoryOptimization2020` | Vandeput, De Gruyter |
| `hyndmanForecastingPrinciples2021` | Hyndman & Athanasopoulos, OTexts 3rd ed. |
| `hillierIntroductionOperationsResearch2020` | Hillier & Lieberman, McGraw-Hill 11th ed. |
| `banBigDataNewsvendor2019` | Ban & Rudin, Oper. Res. 67(1):90–108 |
| `bertsimasPredictivePrescriptiveAnalytics2020` | Bertsimas & Kallus, Mgmt Sci 66(3) |
| `huberDataDrivenNewsvendor2019` | Huber et al., EJOR 278(3) |
| `limTemporalFusionTransformers2021` | Lim et al., IJF 37(4) |
| `wickDemandForecastingIndividual2021` | Wick et al., SN OR Forum 2 |
| `nahmiasOptimalOrderingPolicies1973` | Nahmias & Pierskalla, NRL Quarterly |
| `harrisHowManyParts1913` | Harris, Factory Magazine 1913 |
| `galliherDynamicsContinuousReview1959` | Galliher, Morse & Simond, OR 7(3) |
| `scarfBayesSolutionsStatistical1959` | Scarf, Ann. Math. Statist. 30(2) |
| `rasulMultivariateProbabilisticTime2021` | Rasul et al., arXiv 2002.06103 |
| `porteusFundamentationsStochasticInventory2002` | Porteus, Stanford UP |

## Pre-existing Keys Used
- `peixeiroTimeSeriesForecasting2026` — time series foundation models
- `bocewiczDigitalTwinManufacturing2021` — digital twin manufacturing
- `panJobShopSchedulingRL2021` — dynamic VRP with deep RL (Zhao et al.)
- `laviollaCNNDefectDetection2019` — CNN defect/counterfeit detection

## Key Concepts by Section

### Section 1: Fundamentals
- Supply chain vs. network: upstream tiers (Tier-1, Tier-2), downstream channels
- SCOR model: Plan, Source, Make, Deliver, Return
- Bullwhip effect (Lee et al., 1997): demand amplification; causes: forecast updating, batching, price fluctuation, rationing
- Supply Chain 4.0: IoT/RFID, big data, AI/ML, cloud, autonomous robots
- Blockchain: immutable ledger, anti-counterfeiting, smart contracts
- Digital twins: real-time replica, what-if simulation, IoT-fed feedback loop

### Section 2: Demand Forecasting
- SES: y_{t+1} = alpha*y_t + (1-alpha)*y_hat_t
- Holt-Winters: level + trend + seasonal; ETS state-space framework, AIC model selection
- ARIMA(p,d,q): AR + differencing + MA; SARIMA for seasonal data
- BSTS: Kalman filter; spike-and-slab priors for covariate selection
- LSTM: forget/input/output gates; captures long-range temporal dependencies
- XGBoost/LightGBM: tabular features (calendar, price, promotions), no stationarity assumption
- TFT: variable selection network, LSTM encoder-decoder, temporal self-attention, quantile regression
- Probabilistic forecasting: quantile regression, normalising flows, conformal prediction, Bayesian NNs

### Section 3: Newsvendor
- Critical ratio: CR = cu/(cu+co); Q* = CR-quantile of F
- Cost: E[C(Q)] = co*E[(Q-D)^+] + cu*E[(D-Q)^+]
- Demand models: Normal, Poisson, Negative Binomial, log-normal
- Censored demand: EM/MLE with censoring; ignoring censoring underestimates mean
- Ban & Rudin 2019: weighted empirical quantile regression; data-driven
- Bertsimas & Kallus 2020: prescriptive analytics for general stochastic programs

### Section 4: Inventory
- EOQ: TC(Q) = lambda*K/Q + Q*h/2; Q* = sqrt(2*lambda*K/h)
- Square root robustness: 30% param error → ~14% Q error
- EOQ extensions: quantity discounts, backordering, POQ, joint replenishment
- Continuous review (s,Q): s = mu_L + z_alpha * sigma_L
- Periodic review (s,S): optimal under fixed ordering costs (Scarf 1959)
- Type I service level: P(no stockout per cycle) = F(s)
- Type II (fill rate): fraction of demand satisfied from stock
- Safety stock: SS = z_alpha * sqrt(L*sigma_d^2 + mu_d^2*sigma_L^2)
- Perishable inventory: FIFO/LIFO, ML neural policies with shelf-life state variable
- MOQ: integer programming or round-up heuristics
- Multi-echelon: Clark-Scarf decomposition for serial systems

### Section 5: Strategic/Operational
- Uncapacitated FLP: binary y_j (open/close), fractional x_ij (allocation); branch-and-bound or Benders
- Robust / stochastic network design for disruption resilience
- ML supplier scoring: on-time delivery, defect rate, ESG, financial ratios
- Spend analytics: NLP into UNSPSC taxonomy, entity resolution, Pareto 80/20
- CVRP: Clarke-Wright savings, LKH metaheuristic, neural combinatorial optimisation
- Dynamic routing RL: Actor-Critic (PPO/A3C), state = (positions, orders, time windows)
- Last-mile: ETA regression, stop sequencing, drone routing, crowdsourcing, micro-fulfillment
- S&OP: 5-step process; hierarchical reconciliation; digital twin what-if; bias detection

### Section 6: Transparency & Risk
- Visibility: predictive ETA (gradient boosting), order peak prediction (LSTM/Prophet), anomaly detection
- Churn analytics: RFM segmentation; gradient boost / survival models; SHAP for explainability
- Procurement fraud: Isolation Forest, Autoencoder, graph analysis, Benford's Law, NLP
- Counterfeit: CNN image classifiers; blockchain digital product passports; serialisation mandates
- Data challenges: silos, censoring, cold-start, organisational inertia
- Governance: human-in-the-loop, audit trails, SaaS accessibility, continual retraining

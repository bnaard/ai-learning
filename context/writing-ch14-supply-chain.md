# Writing Summary: Chapter 14 — AI in Supply Chain Management

## Date
2026-03-14

## Status
COMPLETE — all stubs replaced with full card content.

## Files Modified
- `/workspace/ai and data analytics/chapters/ch14-supply-chain.tex` — full chapter written
- `/workspace/bibliography/references.bib` — 15 new bibtex entries added (supply chain references)
- `/workspace/context/research-ch14-supply-chain.md` — research notes written

## Chapter Structure Written

### Section 1: Supply Chain Management Fundamentals (3 subsections, 7 cards)
- **14.1.1 Supply Chain Concepts**: supply chain vs network, SCOR (Plan/Source/Make/Deliver/Return), bullwhip effect
- **14.1.2 Supply Chain 4.0**: SC4.0 digital transformation (IoT/RFID/AI/cloud/robots), blockchain for traceability, digital twins
- **14.1.3 AI Techniques**: overview table (ML, LP/MIP, RL, RPA, Multi-Agent)

### Section 2: Demand Forecasting (3 subsections, 8 cards)
- **14.2.1 Traditional Methods**: SES formula, Holt-Winters/ETS, ARIMA(p,d,q), BSTS/Kalman filter
- **14.2.2 ML-Based Forecasting**: LSTMs (gates), gradient boosting (XGBoost/LightGBM), TFT (full architecture), probabilistic forecasting
- **14.2.3 Newsvendor Problem**: classic critical ratio, demand models + censoring, Ban & Rudin data-driven approach

### Section 3: Inventory Management (3 subsections, 6 cards)
- **14.3.1 EOQ**: Harris formula derivation, assumptions and extensions
- **14.3.2 Inventory Policies**: (s,Q) continuous review with reorder point, (s,S) periodic review, service levels table + safety stock formula
- **14.3.3 Advanced Topics**: perishable inventory, MOQ + multi-echelon

### Section 4: Strategic and Operational AI Applications (4 subsections, 8 cards)
- **14.4.1 Network Design**: facility location ILP formulation, robust/stochastic resilience
- **14.4.2 Supplier Selection and Procurement**: ML supplier scoring, spend analytics + NLP classification
- **14.4.3 Route Optimisation**: CVRP formulation + solution methods, dynamic RL routing, last-mile delivery applications
- **14.4.4 S&OP**: 5-step process, AI applications (consensus forecasting, digital twin, bias detection)

### Section 5: Transparency and Risk (3 subsections, 6 cards)
- **14.5.1 Visibility**: real-time tracking + order prediction, customer/churn analytics
- **14.5.2 Fraud and Risk**: anomaly detection in procurement, counterfeit detection + blockchain
- **14.5.3 Challenges**: data quality/organisational challenges, trust/accountability/accessibility

### Section 6: Further Reading (1 card, full width)
8 references with descriptions covering all major sources.

## Card Count
Total: approximately 38 cards across 6 sections.

## Key Formulas Included
1. SES: $\hat{y}_{t+1} = \alpha y_t + (1-\alpha)\hat{y}_t$
2. Holt-Winters: $\hat{y}_{t+h} = \ell_t + hb_t + s_{t+h-m}$
3. ARIMA components (AR, MA equations)
4. Newsvendor cost function and critical ratio: $F(Q^*) = c_u/(c_u+c_o)$
5. EOQ: $Q^* = \sqrt{2\lambda K/h}$
6. Reorder point: $s = \mu_L + z_\alpha \sigma_L$
7. Safety stock: $\text{SS} = z_\alpha\sqrt{L\sigma_d^2 + \mu_d^2\sigma_L^2}$
8. Facility location ILP (objective + constraints)

## Style Compliance Notes
- All cards use `\begin{tcbitemize}[skin=sectionraster]` with `\tcbitem[title=..., raster multicolumn=3|6]`
- Citations follow `\textsuperscript{\cite[][p.~XX]{key}}` format
- Tables use `tblr` environment with `\hline` rows
- Titles with commas/special chars braced: e.g. `title={Supply Chain 4.0: Digital Transformation}`
- No `\subsubsection` used (only `\subsection`)
- English throughout
- One concept per card maintained

## Issues Fixed
- Removed stray `\end{parameter}` inside equation environment in facility location card

## Bibtex Keys Added
See research notes for full list of 15 new entries.

# Writing Summary: Ch16 — AI in E-Commerce, Marketing and Demand Forecasting

## Date: 2026-03-14

## Output File
`/workspace/ai and data analytics/chapters/ch16-ecommerce-marketing.tex`

## Card Count
- **Section 1 (AI in E-Commerce)**: 10 cards
  - 1.1 Application Areas: 4 cards (E-Commerce AI Landscape, Programmatic Advertising, IoT in Retail, The Long Tail)
  - 1.2 Virtual Assistants and Search: 3 cards (NLP-Powered Chatbots, Voice Search, Visual Product Search)
  - 1.3 Dynamic Pricing: 4 cards (Pricing Theory Foundations, Bayesian Optimal Pricing, RL-Based Dynamic Pricing, Demand Elasticity Measurement)
  - 1.4 Ethics and Regulation: 2 cards (GDPR in E-Commerce, Algorithmic Fairness and Dark Patterns)
- **Section 2 (Marketing Analytics)**: 12 cards
  - 2.1 Foundations: 2 cards (Marketing Mix 4Ps, Customer Journey and Attribution)
  - 2.2 Descriptive Analytics: 4 cards (RFM Customer Segmentation, Market Basket Analysis, Apriori Algorithm, SEO and Search Analytics)
  - 2.3 Predictive Analytics: 4 cards (Customer Churn Prediction, CLV, Sales Forecasting, Propensity Models)
  - 2.4 Prescriptive Analytics: 4 cards (A/B Testing, Multi-Armed Bandits, Upselling/Cross-selling, Closed-Loop vs Human-in-the-Loop)
- **Section 3 (Recommender Systems)**: 18 cards
  - 3.1 Foundations: 4 cards (History and Impact, User-Item Matrix and Feedback, Levels of Personalisation, Evaluation Metrics)
  - 3.2 Collaborative Filtering: 5 cards (User-Based CF, Item-Based CF, Matrix Factorisation, ALS, BPR)
  - 3.3 Content-Based Filtering: 2 cards (Feature Extraction, Factorisation Machines)
  - 3.4 Hybrid Systems: 2 cards (Hybrid Approaches, Cold-Start Problem)
  - 3.5 Large-Scale and Modern: 5 cards (Two-Stage Retrieval, ANN/FAISS, Wide&Deep/NCF, RL and Causal, Multi-Stakeholder)
- **Section 4 (Further Reading)**: 1 itemize block, 10 references

**Total: ~43 cards** (exceeds 40-45 target; Recommender Systems has 18 for desired depth)

## Key Formulas Included
- Price elasticity: ε = ∂lnQ/∂lnP
- Bayesian optimal price: argmax_p [p · E_θ[Q(p,θ)]]
- Association rules: support, confidence, lift
- CLV discounted cash flow
- Cosine similarity
- User-based CF: weighted neighbour prediction
- Item-based CF: similarity-weighted rating
- Matrix factorisation: R ≈ PQ^T + biases; SGD loss with L2 regularisation
- BPR pairwise loss: -sum log σ(r̂_ui+ - r̂_uj-)
- Factorisation Machine formula with pairwise interaction terms
- NCF: ŷ = σ(h^T · MLP([p_u || q_i]))

## TikZ Diagrams
None included (the two-stage retrieval pipeline is described inline; visual search pipeline uses inline LaTeX notation). The chapter content is formula-dense enough without TikZ.

## Style Decisions
- All cards use `raster multicolumn=3` (half-width) or `raster multicolumn=6` (full-width) as required
- `raster multicolumn=6` used for: Visual Product Search (pipeline diagram), BPR (key insight + formula), Two-Stage Retrieval (two-stage explanation)
- Tables use `tblr` environment (Programmatic Advertising, User-Item Matrix, Evaluation Metrics)
- Titles with commas/special chars braced (e.g., `title={NLP-Powered Chatbots}`)
- No `\subsubsection` — only `\subsection`
- All old `\subsubsection` stubs removed; section titles merged into logical subsections
- Citations use `\textsuperscript{\cite[][p.~XX]{key}}` format throughout

## Bibliography Changes
Added 11 new entries to `/workspace/bibliography/references.bib` in section `% ===== E-Commerce, Marketing and Recommender Systems References (added for Ch16) =====`:
- `aggarwalRecommenderSystems2016`
- `jannachRecommenderSystemsIntroduction2010`
- `ricciRecommenderSystemsHandbook2015`
- `rendleBPRBayesianPersonalized2009`
- `rendleFactorizationMachines2010`
- `chengWideDeepLearning2016`
- `heNeuralCollaborativeFiltering2017`
- `korenMatrixFactorizationTechniques2009`
- `liFaissLibraryEfficient2019`
- `chaffeyDigitalBusinessECommerce2019`
- `laudonECommerce2020`

## Coverage vs. Original Stub Structure
| Original stub | Written content |
|---|---|
| Application Areas (Retail, Entertainment, Advertising, IoT) | Merged into 4 cards in Sec 1.1 |
| Virtual Assistants (NLP, DL, Chatbots, Voice) | 2 cards in Sec 1.2 |
| Visual Search | 1 full-width card in Sec 1.2 |
| Dynamic Pricing (theory, elasticity, Bayesian, RL) | 4 cards in Sec 1.3 |
| Regulatory Requirements & Ethics | 2 cards in Sec 1.4 |
| Case Studies | Merged into application area cards (examples cited inline) |
| Marketing Foundations | 2 cards in Sec 2.1 |
| Descriptive Methods (BI, Brand, RFM, Basket, SEO) | 4 cards in Sec 2.2 |
| Predictive Methods (Churn, CLV, Forecasting, SEO-optim.) | 4 cards in Sec 2.3 |
| Prescriptive Methods (Pricing, Upsell, A/B, Targeting) | 4 cards in Sec 2.4 |
| Perspectives (Closed-loop, Omnichannel) | Covered in Sec 2.4 last card |
| Recommender System Foundations | 4 cards in Sec 3.1 |
| Collaborative Filtering | 5 cards in Sec 3.2 |
| Content-based Filtering | 2 cards in Sec 3.3 |
| Hybrid Recommenders | 2 cards in Sec 3.4 |
| Large-Scale Recommenders | 5 cards in Sec 3.5 |
| Literature (inline) | Converted to \fullcite Further Reading section |

## Quality Notes
- "One concept per card" maintained throughout
- All formulas in `equation` environments
- Scientific but accessible tone consistent with other chapters
- Key business context provided (Netflix 80% viewing, Amazon 35% revenue) to motivate each technique
- Causal/RL perspectives integrated where pedagogically appropriate

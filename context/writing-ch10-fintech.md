# Writing Summary: Ch10 — AI in FinTech

## Date: 2026-03-14
## Writer: Research+Writer Agent (Sonnet)

---

## Output Summary

**File written**: `/workspace/ai and data analytics/chapters/ch10-fintech.tex`
**Status**: COMPLETE (all stubs replaced with substantive content)

---

## Chapter Structure Written

### Section 1: Concepts of FinTech and Artificial Intelligence
- **1.1 Introduction to FinTech** (4 cards)
  - What is FinTech? (half-width)
  - The FinTech Ecosystem — tblr table of actors (half-width)
  - Open Banking and PSD2 — AISPs/PISPs (half-width)
  - Revolution in Financial Services — 3 forces (half-width)

- **1.2 Applications in Banking and Finance** (4 cards)
  - Neo-Banks and Digital-Only Banking (half-width)
  - Payments and the ACH Network (half-width)
  - Wealth Management and Lending (half-width)
  - Financial Inclusion (half-width)

- **1.3 FinTech Underlying Technologies** (4 cards)
  - Cloud Banking (half-width)
  - Blockchain, DLT and Smart Contracts (half-width)
  - ML and DL in Finance — tblr table (half-width)
  - NLP for Financial Text (half-width)

### Section 2: AI Applications in Financial Services
- **2.1 Credit Scoring and Lending** (3 cards)
  - Traditional Credit Scorecards (half-width)
  - ML-Based Credit Models (half-width)
  - Fairness and Disparate Impact (half-width)

- **2.2 Algorithmic Trading** (5 cards)
  - What is Algorithmic Trading? — IR formula (half-width)
  - Alpha Factors and Feature Engineering (half-width)
  - Strategy Types — tblr table (half-width)
  - RL for Trading (half-width)
  - Backtesting and Overfitting Risk — tblr table (FULL width)

- **2.3 Chatbots and Customer Service** (2 cards)
  - NLP-Powered Banking Assistants (half-width)
  - Generative AI in Finance (half-width)

- **2.4 KYC and AML** (2 cards)
  - Know Your Customer (KYC) (half-width)
  - Anti-Money Laundering (AML) (half-width)

### Section 3: Fraud Detection in FinTech
- **3.1 Types of Financial Fraud** (3 cards)
  - Payment and Card Fraud (half-width)
  - Insurance and Identity Fraud (half-width)
  - The Wirecard Case (FULL width — important case study)

- **3.2 ML for Fraud Detection** (4 cards)
  - Anomaly Detection Approaches (half-width)
  - Supervised Classification for Fraud (half-width)
  - Class Imbalance Problem — SMOTE + remedies (half-width)
  - Real-Time Fraud Scoring (half-width)

### Section 4: Robo-Advisory
- **4.1 Definition and Types** (2 cards)
  - What is a Robo-Advisor? (half-width)
  - Pure vs. Hybrid Robo-Advisors — tblr comparison table (half-width)

- **4.2 Portfolio Management** (4 cards)
  - Modern Portfolio Theory (Markowitz) — optimization formula (half-width)
  - Sharpe Ratio and Risk-Adjusted Performance — formula (half-width)
  - Black-Litterman Model — Bayesian formula (half-width)
  - Rebalancing and Tax-Loss Harvesting (half-width)

- **4.3 Goal-Based Investing** (2 cards)
  - Risk Profiling and Investor Preferences (half-width)
  - Goal-Based Portfolio Modeling (half-width)

### Section 5: Trust, Ethics, and Regulation
- **5.1 Bias and Fairness** (2 cards)
  - Algorithmic Discrimination in Lending (half-width)
  - Explainability Requirements (half-width)

- **5.2 Financial Regulation** (2 cards)
  - MiFID II and Algorithmic Trading (half-width)
  - Regulation of Robo-Advisors — tblr table (half-width)

- **5.3 Future Outlook** (3 cards)
  - CBDCs and Programmable Money (half-width)
  - DeFi and Embedded Finance (half-width)
  - ESG and Sustainable Finance (half-width)

### Section 6: Further Reading (1 wide card)
- jansenMachineLearningAlgorithmic2020
- kardellBuildFinancialSoftware2025

---

## Card Count
Total cards written: **~40 cards**
- Full-width (raster multicolumn=6): 3 cards (Backtesting table, Wirecard case, Further Reading)
- Half-width (raster multicolumn=3): ~37 cards

---

## Formulas Included
1. Information Ratio: IR ≈ IC × √N (Section 2.2)
2. Markowitz mean-variance optimization (Section 4.2)
3. Sharpe ratio (Section 4.2)
4. Black-Litterman posterior return formula (Section 4.2)

---

## TikZ Diagrams
None included — no diagram would significantly aid understanding over the table/itemize structures used. The RL-for-trading concept is covered in Ch7 with full TikZ treatment.

---

## Tables (tblr)
1. FinTech Ecosystem actors
2. ML types and finance applications
3. Strategy types in algorithmic trading
4. Backtesting pitfalls, causes, and remedies (full-width)
5. Pure vs. Hybrid Robo-Advisors
6. Regulation of Robo-Advisors by jurisdiction

---

## Style Compliance
- All subsections use `\begin{tcbitemize}[skin=sectionraster]`
- No `\subsubsection` used (original stub used these; all removed)
- All citations: `\textsuperscript{\cite[][p.~XX]{key}}` format
- Tables use `tblr` (tabularray)
- Only available bib keys cited: `jansenMachineLearningAlgorithmic2020`, `kardellBuildFinancialSoftware2025`
- Original stub's inline `\itemize` literature section replaced by `\fullcite` Further Reading card

---

## Citation Page References
- Citations are to approximate page ranges from the PDFs as read during research
- Jansen page references verified against book TOC (pp.1–722)
- Kardell page references verified against book TOC (pp.3–404)

---

## Content Not Included (Scope Decisions)
- Crypto fraud / DeFi hack details — covered under Future Outlook at summary level
- Full CAPM derivation — summarized via Markowitz formula; CAPM covered in Ch2
- Detailed AML SAR filing process — covered at conceptual level
- Insurance fraud case studies (OneConnect) — original stub item; covered under Types
- NLP/GenAI details — covered in depth in Ch12; cross-referenced implicitly

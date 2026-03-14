# Writing Summary: Chapter 19 — Visualization

**Date**: 2026-03-14
**Agent**: Research+Writer (Sonnet 4.6)
**File written**: `/workspace/ai and data analytics/chapters/ch19-visualization.tex`

## Output Statistics

- **Sections**: 5 (Foundations, Chart Types, Dashboards & Storytelling, Tools, Further Reading)
- **Subsections**: 10
- **Cards (tcbitem)**: 28 total
- **TikZ diagrams**: 1 (Anscombe's Quartet illustration)
- **Tables (tblr)**: 6
- **Equations**: 8

## Card Inventory

### Section 1: Foundations of Data Visualization
1. Anscombe's Quartet (multicolumn=3) + TikZ diagram
2. Pre-attentive Processing and Cognitive Load (multicolumn=3)
3. Data-Ink Ratio (Tufte) (multicolumn=3)
4. Exploratory vs Explanatory Visualization (multicolumn=3) + tblr table
5. Marks and Channels (multicolumn=3)
6. Cleveland & McGill Effectiveness Ranking (multicolumn=3)
7. Gestalt Principles in Chart Design (multicolumn=6) + tblr table
8. Colour Palette Types (multicolumn=3)
9. Perceptual Uniformity and Colourblind Safety (multicolumn=3)

### Section 2: Chart Types and When to Use Them
10. Bar and Column Charts (multicolumn=3)
11. Histograms and Density Plots (multicolumn=3)
12. Box Plots and Violin Plots (multicolumn=3)
13. When to Use Which Distribution Chart (multicolumn=3) + tblr table
14. Scatter Plots and Bubble Charts (multicolumn=3)
15. Heatmaps and Correlation Matrices (multicolumn=3)
16. Pair Plots (multicolumn=6)
17. Pie Charts and When to Avoid Them (multicolumn=3)
18. Line Charts and Time Series (multicolumn=3)
19. Confusion Matrix (multicolumn=3)
20. ROC Curve and AUC (multicolumn=3)
21. Precision-Recall Curve (multicolumn=3)
22. Learning Curves (multicolumn=3)
23. Feature Importance Plots (multicolumn=3)
24. SHAP Summary Plots (multicolumn=3)
25. t-SNE and UMAP Embedding Plots (multicolumn=6)

### Section 3: Dashboards and Storytelling
26. Few's Dashboard Design Principles (multicolumn=3)
27. KPIs and Layout Patterns (multicolumn=3)
28. Common Dashboard Anti-Patterns (multicolumn=6) + tblr table
29. Narrative Structure in Data Presentations (multicolumn=3)
30. Annotation, Context, and Audience Design (multicolumn=3)

### Section 4: Tools and Libraries
31. Matplotlib: The Foundation (multicolumn=3)
32. Seaborn: Statistical Plots (multicolumn=3)
33. Plotly: Interactive Visualization (multicolumn=3)
34. Altair: Declarative Visualization (multicolumn=3)
35. Streamlit and Dash: Dashboard Frameworks (multicolumn=6) + tblr table
36. Tableau and Power BI (multicolumn=3)
37. D3.js and ggplot2 (multicolumn=3)

### Section 5: Further Reading
38. Recommended Sources (multicolumn=6) — 7 fullcite entries

## Citation Decisions

All citations use keys verified to exist in `bibliography/references.bib`.
The chapter stub listed Tufte, Few, Munzner, Kirk, Yau as recommended reading
but none are in the bib file. Their concepts are discussed in the text but not
formally cited. Page numbers for citations are approximate (the PDFs in the bib
were often marked pagetotal=1, meaning page count was not imported from Zotero).

## Style Compliance

- All tcbitem titles with commas or special chars are braced
- All tables use tblr (tabularray) with \SetCell-compatible column specs
- No \subsubsection used
- All content in English
- Each card teaches one concept
- TikZ used only for the Anscombe diagram (aids understanding significantly)
- Equations in \begin{equation} environments

## Remaining Work / Notes for Coordinator

- The bib is missing the primary visualization references (Tufte, Few, Munzner, Wilke).
  If the author acquires these books, keys should be added and citations inserted.
- The Anscombe TikZ is a schematic approximation; data points are illustrative, not
  exact coordinates from the original quartet.
- Section 2.3 (Composition and Time Series) is slightly leaner (only 2 cards) compared
  to other subsections; could be expanded with stacked area/bar cards if desired.

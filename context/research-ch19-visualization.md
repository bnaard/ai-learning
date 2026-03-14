# Research Notes: Chapter 19 — Visualization

**Date**: 2026-03-14
**Agent**: Research+Writer (Sonnet 4.6)

## Knowledge Sources Used

### Bibliography keys confirmed in references.bib
- `loducaDataStorytellingAltair2024` — Data Storytelling with Altair and AI (Manning, 2024)
- `jansenHandbuchInfografik1999` — Handbuch der Infografik (Springer, 1999)
- `molinHandsonDataAnalysis2021` — Hands-on Data Analysis with Pandas (Packt, 2021)
- `brucePracticalStatisticsData2017` — Practical Statistics for Data Scientists (O'Reilly, 2017)
- `downeyThinkStatsExploratory2015` — Think Stats: Exploratory Data Analysis (O'Reilly, 2015)
- `raschkaPythonMachineLearning2015` — Python Machine Learning (Packt, 2015)
- `jansenMachineLearningAlgorithmic2020` — ML for Algorithmic Trading (Packt, 2020)

### Notable absences (not in bib)
- Tufte "The Visual Display of Quantitative Information" — NOT found in bib
- Few "Now You See It" / "Information Dashboard Design" — NOT found in bib
- Munzner "Visualization Analysis and Design" — NOT found in bib
- Wilke "Fundamentals of Data Visualization" — NOT found in bib
- Kirk "Data Visualization" — NOT found in bib
- Yau "Data Points" — NOT found in bib

These are listed in the chapter's inline literature stub but are not in references.bib.
Decision: Use available bib keys only; do not manufacture citations for missing keys.

## Key Concepts Researched

### Foundations
- Anscombe's Quartet (1973): canonical argument for always plotting data
- Pre-attentive attributes: colour, luminance, size, orientation, motion, position
- Cognitive load theory: extraneous vs intrinsic vs germane load
- Tufte's data-ink ratio: maximize proportion of ink encoding data
- Exploratory vs explanatory visualization dichotomy

### Visual Encoding
- Marks: points, lines, areas, bars, glyphs
- Channels: position, length, angle, area, colour hue, luminance, saturation, shape
- Cleveland & McGill (1984) accuracy ranking: position > length > angle > area > colour
- Gestalt principles: proximity, similarity, closure, continuity, figure/ground, common fate

### Colour
- Sequential palettes for ordered data (luminance monotonic)
- Diverging palettes for data with meaningful midpoint
- Categorical palettes for nominal groups (distinct hues, similar luminance)
- Viridis family: perceptually uniform AND colourblind-safe
- ColorBrewer: web tool with colourblind-safe markers
- ~8% of males have red-green colour deficiency

### Chart Types
- Bar charts: always zero baseline; sort by value
- Histograms: bin width rules (Sturges, Scott, Freedman-Diaconis)
- KDE: bandwidth h for continuous smoothing
- Box plots: Q1/median/Q3/whiskers (1.5 x IQR)/outliers
- Violin plots: KDE mirrored -- reveals multimodality
- Scatter plots: best for bivariate quantitative relationships
- Bubble charts: weak -- area is 5th in encoding accuracy
- Heatmaps: colour for matrices; diverging palette for correlation
- Pair plots (SPLOM): all pairwise scatter + diagonal univariate
- Pie charts: avoid for >3 slices; Cleveland-McGill: angle is step 4
- Line charts: temporal ordering; direct labels; reference lines

### ML-Specific Visualizations
- Confusion matrix: TN/FP/FN/TP; normalize by row for class-wise error
- ROC curve: TPR vs FPR at every threshold; AUC in [0.5, 1]
- Precision-Recall curve: better for imbalanced data than ROC
- Learning curves: bias vs variance diagnosis
- Feature importance: impurity-based (biased), permutation (model-agnostic)
- SHAP summary plot: phi_j values per sample; colour = feature value
- t-SNE: KL divergence minimization; inter-cluster distances not meaningful
- UMAP: faster, better global structure, supports projection

### Dashboard Design
- Few's principles: single screen, at-a-glance, context, 5-second test
- KPIs: F-pattern (top-left first) and Z-pattern layouts
- Anti-patterns: 3-D charts, dual y-axes, gauges, auto-animation, inconsistent colour

### Storytelling
- Narrative arc: Setup -> Conflict -> Resolution -> Call to Action
- Annotation: direct labels, headline annotations, event markers
- Audience-aware design: technical vs executive vs public

### Python Tools
- Matplotlib: Figure/Axes/Artist model; pyplot vs OO interface
- Seaborn: high-level statistical plots; tidy data; FacetGrid
- Plotly: interactive HTML; plotly.express vs graph_objects
- Altair: declarative Vega-Lite; composable; linked brushing
- Streamlit: re-run model; rapid prototyping
- Dash: callback model; production dashboards
- D3.js: lowest-level JavaScript primitives
- ggplot2/plotnine: Grammar of Graphics (Wilkinson)

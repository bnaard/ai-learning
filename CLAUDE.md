# AI & Data Analytics Learning Cards - Project Guide

## Project Overview
A comprehensive LaTeX document (`ai and data analytics/ai-dataanalytics-cards.tex`) serving as a learning reference for AI and Data Analytics. The document uses a "card-based" layout with `tcolorbox` and `tcbitemize` environments to present bite-sized learning content.

## Document Structure
- **Format**: LaTeX (extreport class, 8pt, A4, two-column multicol layout)
- **Engine**: LuaLaTeX or XeLaTeX (uses fontspec)
- **Bibliography**: biblatex with biber backend, numeric style (`bibliography/references.bib`)
- **Main color**: LimeGreen-based theme
- **Style**: `sectionraster` skin for content cards, `sectionboxskin` for sections

## Chapters (13 total)
1. Introduction to AI and Data Analytics (partial content)
2. Mathematical Foundations (partial - vectors done, rest stubs)
3. Programming Foundations (all stubs)
4. Data Analytics Foundations (all stubs)
5. Machine Learning (intro done, rest stubs with \lipsum placeholders)
6. Deep Learning (all stubs with \lipsum)
7. Reinforcement Learning (stubs with \lipsum)
8. Functional Security in AI Systems (all stubs)
9. Foundational Computer Vision (stubs with \lipsum)
10. AI in FinTech (stubs with \lipsum)
11. AI in Healthcare and Medical Imaging (stubs with \lipsum)
12. NLP and Generative AI (stubs)
13. AI in Business (Recommender Systems, Marketing Analytics)
14. International IT Law (stubs)
15. Start-up / Visualization / Scientific Writing (empty stubs)

## Content Style Guidelines
- Each section uses `\begin{tcbitemize}[skin=sectionraster]` with `\tcbitem[title=..., raster multicolumn=6]`
- Content is concise, educational, with key formulas in `equation` environments
- Citations use `\textsuperscript{\cite[][p.XX]{bibtexkey}}` format
- Diagrams use TikZ with predefined flowchart styles
- Stub sections use either `\lipsum` placeholders or enumerated topic outlines
- Tables use `tblr` (tabularray) environment
- Tone: Scientific but accessible, "deep enough for background, not all formulas derived"

## Way of Working

### Team Structure
- **Coordinator** (Claude Opus): Orchestrates work, challenges quality, manages progress
- **Research Agent**: Investigates knowledge sources, extracts key concepts, finds references
- **Writer Agent** (Sonnet): Produces LaTeX content matching document style, formatting

### Workflow
1. Research agent reads relevant knowledge PDFs and does web research for a section
2. Research agent documents findings in `context/research-{topic}.md`
3. Writer agent takes research notes + style guide and produces LaTeX content
4. Writer agent documents output in `context/writing-{topic}.md`
5. Coordinator reviews, challenges, and integrates into main .tex file
6. All agents update `context/PROGRESS.md` after each task

### Key Rules
- **References**: All content must cite sources using bibtex keys from `bibliography/references.bib`
- **New references**: Add to references.bib if not already present
- **Style consistency**: Match existing card-based tcbitemize format exactly
- **Depth**: Core concepts + key formulas, not full derivations
- **Token conservation**: Use Sonnet model for writing tasks; research agents should summarize, not dump raw text
- **Resilience**: Document progress every 3-4 minutes or after each subtask in context/PROGRESS.md
- **Priority**: Start with chapters that have the most structure (outlines) already defined

## Knowledge Sources
- Primary: Books in `./knowledge/Knowledge ML and AI/` and `./knowledge/Knowledge Data Mining/`
- Secondary: Internet research
- Bibliography: `bibliography/references.bib` (large Zotero export, ~400+ entries)

## File Paths
- Main doc: `ai and data analytics/ai-dataanalytics-cards.tex`
- Bibliography: `bibliography/references.bib`
- Flowchart styles: `shapes/flowchart_styles.tex`
- Config: `config/textwrap.yaml`
- Progress tracking: `context/PROGRESS.md`
- Research notes: `context/research-*.md`
- Writing notes: `context/writing-*.md`

# Writing Summary: Chapter 13 — Industrial AI

**Date**: 2026-03-14
**Agent**: Research+Writer (Sonnet)
**Status**: COMPLETE

## Output

Full LaTeX chapter written to:
`/workspace/ai and data analytics/chapters/ch13-industrial-ai.tex`

## Card Count

| Section | Subsection | Cards |
|---------|-----------|-------|
| 1: Smart Factory & Industry 4.0 | 1.1 Industry 4.0 | 2 |
| 1: Smart Factory & Industry 4.0 | Key Technologies | 4 |
| **Section 1 total** | | **6** |
| 2: AI for Manufacturing | Predictive Maintenance | 3 |
| 2: AI for Manufacturing | Quality Control | 3 |
| 2: AI for Manufacturing | Generative Design | 2 |
| 2: AI for Manufacturing | Planning & Scheduling | 2 |
| **Section 2 total** | | **10** |
| 3: Industrial Automation | Discrete Event Systems | 6 |
| 3: Industrial Automation | Simulation and Control | 3 |
| 3: Industrial Automation | Applications | 2 |
| **Section 3 total** | | **11** |
| 4: Robotics | Robot Types | 2 |
| 4: Robotics | Kinematics & Motion | 4 |
| 4: Robotics | Robot Architectures | 3 |
| **Section 4 total** | | **9** |
| 5: Supply Chain | AI for Supply Chain | 3 |
| **Section 5 total** | | **3** |
| 6: Further Reading | | 1 (full list) |
| **TOTAL** | | **40** |

## Structure Changes vs Original Outline

The original stub had 3 sections with heavy use of `\subsubsection` (not permitted by style guide). The new chapter:
- Restructures into 6 logical sections per the task specification
- Eliminates all `\subsubsection` levels
- Replaces all `\lipsum` placeholders with real content
- Adds 20 new bibliography entries covering all cited works
- Literature section converted from `itemize` list to proper `\section{Further Reading}` with `\fullcite` format

## Scope Decisions

1. **Dynamics omitted**: The original outline had a full "Fundamentals of Robot Dynamics" subsection (Lagrange, Newton formulations). Omitted to keep within ~40 card target and maintain "one concept per card" principle. The kinematics + motion planning cards provide sufficient background for a learning reference.

2. **Supply Chain kept brief**: Per task specification, Ch14 covers supply chain in depth. Section 5 has 3 cards covering demand forecasting, EOQ, and VRP — enough context without overlap.

3. **DES consolidated**: Original had 7 subsections in Industrial Automation. Consolidated to 3 subsections (DES theory, Simulation+Control, Applications) with 11 cards total — covers the same ground more efficiently.

4. **Timed models**: Rather than a standalone subsection, timed models (timed automata, stochastic Petri nets, M/M/1) consolidated into one card in the DES section.

## Style Compliance

- All `\tcbitem` entries use `raster multicolumn=3` (half) or `raster multicolumn=6` (full)
- Titles containing commas are braced: e.g. `title={Card Title, with comma}`
- Citations use `\textsuperscript{\cite[][p.~XX]{key}}` format throughout
- Equations in `\begin{equation}` environments
- No `\subsubsection` used anywhere
- No TikZ diagrams (none deemed essential enough to add)
- `tblr` not needed (no tables in this chapter — tabular data better expressed as itemize lists here)
- English throughout

## Bibliography Notes

20 new entries added to `bibliography/references.bib`. All entries use Zotero/biblatex conventions consistent with the existing file (using `date =` not `year =`, `journaltitle =` not `journal =`, `location =` not `address =`).

Key entry names follow the existing `authorTitleKeyword YYYY` pattern used throughout the bibliography.

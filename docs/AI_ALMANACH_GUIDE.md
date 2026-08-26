# AI Almanach authoring guide

## Purpose

The AI Almanach is a 22-chapter, A4 LaTeX learning reference for AI, machine
learning, data science, intelligent systems, and their application domains. It
is designed for engineering learners who need conceptual models, mathematical
mechanisms, worked reasoning, operational failure modes, and evidence they can
use to make defensible decisions.

The main document is `ai almanach/ai-almanach.tex`. Chapter sources live in
`ai almanach/chapters/`, and the bibliography is
`bibliography/references.bib`.

## Build and preview

Build only inside the development container:

```sh
aibox-latex-build ai-almanach
```

The compiled PDF is `ai almanach/out/ai-almanach.pdf`. Open the live preview
at `http://127.0.0.1:8766/documents/ai-almanach/`.

The document uses LuaLaTeX, `biblatex` with Biber, `tcolorbox`, `tabularray`,
TikZ, `caption`, and `hyperref`.

## Curriculum

The book contains these learning strands:

1. Orientation, mathematics, programming, data, machine learning, and deep
   learning.
2. Evaluation and MLOps, reinforcement learning, trustworthy AI, computer
   vision, NLP, and practical LLM engineering.
3. Finance, healthcare, industrial AI, supply chains, multi-agent systems,
   commerce, law, and visualization.
4. AI venture building and scientific writing with reproducible
   communication.

The course-coverage map in
`ai almanach/appendices/course-coverage-map.tex` is the auditable curriculum
index. Update it when a new learning outcome changes the book's scope.

## Repeated chapter pattern

Every chapter is included with `\almanachinputchapter`. This wrapper creates a
consistent learning sequence:

1. A side-by-side chapter compass with an essential question, an observable
   learning outcome, reading guidance, and a four-stage roadmap figure.
2. Concept cards that introduce one coherent idea at a time.
3. Formal mechanisms, equations, diagrams, comparison tables, and worked
   examples close to the text they explain.
4. A chapter-specific engineering deep dive that covers a modern concern or
   an important failure boundary.
5. A synthesis with evidence checks and retrieval prompts.

This pattern combines constructive alignment, signaling and spatial
contiguity, worked examples, and retrieval practice. Do not remove the opening
or synthesis from an individual chapter merely to save space.

## Layout and card composition

- The page uses comfortable A4 margins and a six-column `tcolorbox` raster.
- Prefer paired `raster multicolumn=3` cards for concepts that compare or
  complete one another.
- Use `raster multicolumn=6` for equations, diagrams, long examples, tables,
  and any card that would otherwise leave an empty half-row.
- Keep the text that interprets a visual beside or immediately above it. Avoid
  decorative images that duplicate the prose.
- Use the shared `sectionraster` and `sectionboxskin` styles. Do not create a
  chapter-local visual language unless the information genuinely requires a
  new semantic component.
- A card should have one teaching purpose, but it may contain definition,
  mechanism, example, and caveat when those parts form one reasoning unit.

## Figures and tables

Every pedagogically meaningful visual must have a concise caption and stable
label. Every table must also have a caption and stable label. Captions are not
optional even when the object is inside a `tcolorbox` and cannot float.

Use a normal `figure` or `table` environment when floats are safe. Inside
cards, use `\captionof{figure}` or `\captionof{table}`. Captions must explain
the takeaway, not merely name the object. Labels use `fig:` or `tab:` and must
be unique.

Run the inline-object audit before release:

```sh
python3 scripts/almanach_caption_audit.py
```

The `--fix` option can add captions to legacy inline `tblr` and TikZ blocks,
but the generated captions still require editorial review.

## Content quality

Core explanations should answer these questions where relevant:

- What problem does the concept solve, and what is the non-AI baseline?
- What are its inputs, outputs, assumptions, and dimensions?
- How does the mechanism work, including the decisive equation or algorithm?
- Which worked example demonstrates the reasoning rather than only the
  result?
- How can the method fail through leakage, shift, bias, unsafe interaction,
  poor calibration, or metric mismatch?
- Which evidence would justify adoption, release, monitoring, or rejection?
- What remains uncertain, time-sensitive, or outside the chapter's scope?

Use precise, accessible English. State constraints and counterexamples rather
than presenting a method as universally applicable. Time-sensitive legal,
product, and benchmark claims require a date and a primary source.

## Sources

Prefer peer-reviewed papers, standards, official documentation, and
authoritative textbooks. Add complete BibTeX entries to
`bibliography/references.bib` and cite the source at the claim it supports.
Further-reading sections should point to the most useful sources rather than
repeat the full bibliography.

## File map

- Main document and shared visual system:
  `ai almanach/ai-almanach.tex`
- Chapter-specific modern extensions:
  `ai almanach/chapters/cross-cutting-deep-dives.tex`
- Chapters: `ai almanach/chapters/ch*.tex`
- Front matter: `ai almanach/frontmatter/`
- Curriculum map: `ai almanach/appendices/course-coverage-map.tex`
- Bibliography: `bibliography/references.bib`
- Shared flowchart styles: `shapes/flowchart_styles.tex`
- Caption audit: `scripts/almanach_caption_audit.py`

Chapter files contain content only; the preamble and document environment stay
in the main file. Keep generated files under `ai almanach/out/`.

# AI and Data Analytics Learning Cards

This repository contains a card-based LaTeX learning reference for AI and
data analytics. It is written for beginners who want a structured overview of
the mathematics, programming, data, machine-learning, and applied topics that
support practical AI work.

## Status

The project is a work in progress. The document has twenty chapter files, but
several chapters still contain outlines, placeholders, or incomplete sections.
It should be treated as a learning draft rather than a finished textbook,
course, or production reference. See [STATUS.md](STATUS.md) for the current
maintenance and maturity policy.

## Build

The maintained entry point is
`ai and data analytics/ai-dataanalytics-cards.tex`. It uses LuaLaTeX or
XeLaTeX, `latexmk`, `biber`, the TeX packages in the preamble, and installed
fonts such as FreeSans and FreeMono.

From the repository root:

```sh
cd "ai and data analytics"
latexmk -lualatex -shell-escape -interaction=nonstopmode \
  -file-line-error ai-dataanalytics-cards.tex
test -s ai-dataanalytics-cards.pdf
```

The separate mathematics deck can be built similarly:

```sh
cd math
latexmk -lualatex -shell-escape -interaction=nonstopmode \
  -file-line-error math-learning-cards.tex
```

The build uses `minted` and SVG conversion, so `-shell-escape` is required.
Only build reviewed sources in an isolated workspace; generated PDFs and
LaTeX intermediates are ignored and must not be committed.

## Provenance and boundaries

The chapter sources are maintained in
`ai and data analytics/chapters/`. `bibliography/references.bib` is a Zotero
export containing bibliographic metadata; it does not redistribute the
referenced books or papers. Research notes and generated-content expectations
are documented in the maintainer notes and summarized in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Automation policy

This project intentionally does not use GitHub Actions or checked-in workflow
files. Local builds and human review are the verification process; pull
requests do not receive an automated GitHub CI status check.

## Contributing, security, and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing chapters and
[SECURITY.md](SECURITY.md) before reporting a concern. The source is released
under the [MIT License](LICENSE). AI assistance is disclosed in the document;
contributors remain responsible for checking factual accuracy, citations, and
licensing before publication.

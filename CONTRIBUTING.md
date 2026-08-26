# Contributing

This is a structured learning publication. Before making a substantial
chapter or section change, open an issue describing the learning objective and
the intended audience. Small corrections, citation fixes, and build-documentation
updates can go directly into a pull request.

Follow the existing card-based LaTeX style. New factual material should cite
a key from `bibliography/references.bib`; add a source when no suitable key
exists. Mark unfinished work clearly rather than presenting a placeholder as
finished content.

Run the relevant local `latexmk` build when the toolchain is available and
describe the result. Do not commit PDFs, LaTeX intermediates, minted output,
or failed-build diagnostics.

This repository intentionally has no GitHub Actions or workflow files. Local
builds, citation review, and human review are the verification process.

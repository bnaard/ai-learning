---
apiVersion: processkit.projectious.work/v2
kind: DecisionRecord
metadata:
  id: DEC-20260826_1751-FluentMelody-ai-almanach-v3-depth-first-didactic
  created: '2026-08-26T17:51:58+00:00'
spec:
  title: 'AI Almanach v3: depth-first didactic rebuild, no page limit'
  state: accepted
  decision: |
    Rebuild the remaining 15 bare chapters of the AI Almanach v3 one at a time to the full didactic standard established by the Chapter 6 rebuild, rather than adding minimal scaffolding book-wide first. Accept unbounded page growth (Chapter 6 went 14 -> 26 pages; book-wide this implies roughly 600+ pages).

    Rollout order (dependency- and value-ordered, not chapter-numeric):
    W1 Ch2 Mathematical Foundations, then Ch5 Machine Learning
    W2 Ch12 NLP and Voice Assistants
    W3 Ch7 Reinforcement Learning, Ch9 Computer Vision
    W4 Ch3 Programming Foundations, Ch4 Data and Analytics
    W5 Ch1 Introduction, then application chapters 10, 11, 13-18

    Cross-cutting jobs folded in along the way: add \label{ch:...} to all 22 chapters so cross-references resolve, and sweep converter-generated captions book-wide using scripts/almanach_caption_audit.py.
  context: |
    A structural review of ai almanach v3 (309 pp at the time) found that the eight didactic environments defined in preamble.tex (plainlanguage, engineernote, workedexample, checkpoint, practicallab, cautionbox, learningobjectives, didacticnote) were used in only 7 of 22 chapters, and the 15 without them included every core learning chapter: Machine Learning, Deep Learning, Reinforcement Learning, Computer Vision and NLP. The whole book contained 5 worked examples and 6 practical labs. Sourcing was already strong (547 bib entries, 850+ citations, zero undefined references), and the front matter was complete, so the gap was didactic apparatus and illustration density (152 tables vs 44 hand-authored figures), not content coverage or scholarship.

    Chapter 6 (Deep Learning) was rebuilt in this session as the reference implementation: 0 -> 52 didactic elements, 3 -> 25 figures, 16 worked examples with real numbers, 27 primary BibTeX entries added to replace textbook-mediated attributions, Attention/Transformers moved out of the mis-titled "Alternative Training Methods" section, and the non-inverted dropout description corrected. Book builds clean at 325 pp with zero undefined references and zero overfull boxes in Ch6.
  rationale: |
    Depth-first was chosen over breadth-first because each finished chapter is immediately usable for learning, whereas a minimal-scaffolding pass would leave every chapter half-done and require a second full pass anyway. The owner's stated goal is to learn from the book to succeed professionally in AI, so usable-now beats uniformly-improved-later. No page limit was chosen because the owner explicitly set no size constraint and completeness is the stated objective; rationing worked examples would reintroduce the exact deficiency the review identified.

    Order is driven by dependency and by concentration of the owner's stated interests: Ch2 is the mathematical gateway for a mixed-background audience that needs math rehearsals, Ch5 is the largest chapter in the book (64 KB) with zero scaffolding, and Ch12 sits between the rebuilt Ch6 and the already-strong Ch12b, making it the weak link on the LLM-engineering path the owner cares most about.
  alternatives:
  - option: Breadth-first, then deepen
    why_rejected: Adds minimum scaffolding to all 15 chapters first, then a second
      pass for worked examples, figures and labs. Improves the whole book sooner but
      leaves no chapter at usable depth for a long time and requires touching every
      chapter twice.
  - option: Learning-path first (Ch2, Ch5, Ch12, Ch12b only)
    why_rejected: Fastest route to the LLM-engineering material the owner's career
      depends on, but abandons the completeness goal that motivated the almanach and
      leaves the eight application chapters permanently below standard.
  - option: Cap the book at ~450 pages
    why_rejected: Would require rationing worked examples and figures to the highest-value
      concepts per chapter, reintroducing the exact deficiency the review identified.
      The owner explicitly set no size limit.
  - option: Split into two volumes (Foundations Ch1-9, Applications Ch10-20)
    why_rejected: Keeps each volume readable but adds a build target and cross-referencing
      work. Deferred rather than dismissed; revisit if the single volume becomes unwieldy
      past roughly 600 pages.
  consequences: |
    Positive: each completed chapter is immediately usable; the Ch6 template makes later chapters faster and more consistent; primary-source citations strengthen the book's scholarly claim.

    Negative / accepted costs: the book will roughly double in length, so a future volume split may become necessary (explicitly declined for now); 15 chapters remain below standard for an extended period, so the book is uneven until the rollout completes; each chapter costs roughly one full working pass.

    Operational: builds must not be run directly into /workspace. That path is a virtiofs mount from the macOS host which silently truncates large files (the PDF was observed shrinking 1,769,987 -> 1,612,170 -> 403,998 bytes), corrupting the .aux and PDF and producing LaTeX errors unrelated to the source. Build into container-local storage and copy back with byte-count verification. Note also that -outdir is a latexmk flag, not a lualatex flag; direct lualatex invocations need -output-directory.
  decided_at: '2026-08-26T17:51:58+00:00'
---

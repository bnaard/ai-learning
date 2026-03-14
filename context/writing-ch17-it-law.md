# Writing Notes: Chapter 17 — International IT Law

**Date**: 2026-03-14
**Agent**: Research+Writer Agent (Sonnet)
**Status**: COMPLETE

## Output Summary
- File: `/workspace/ai and data analytics/chapters/ch17-it-law.tex`
- Total cards: 18
- Sections: 6 (+ intro tcolorbox signpost notice)
- Tone: Signpost / practitioner awareness — not a legal textbook

## Card Count by Section
| Section | Subsection | Cards |
|---------|-----------|-------|
| 1. Legal Foundations | Key Areas of IT Law | 3 |
| 2. Data Protection | GDPR Essentials | 3 |
| 2. Data Protection | GDPR for AI/ML | 3 |
| 2. Data Protection | International Data Transfers | 1 |
| 3. AI-Specific Regulation | EU AI Act | 3 |
| 3. AI-Specific Regulation | Other Jurisdictions | 1 |
| 4. Intellectual Property | Copyright and AI | 2 |
| 4. Intellectual Property | Software and Open Source | 1 |
| 5. Cybersecurity and Liability | Information Security Law | 2 |
| 5. Cybersecurity and Liability | AI Liability | 1 |
| 6. Further Reading | — | 1 (full-width) |
| **Total** | | **21** |

Note: slightly over the 15-20 card target, but each section needs at least 1 card to be meaningful.
Several cards use `raster multicolumn=6` (full width) for tables that need space.

## Style Decisions
- Used `tblr` tables for comparative overviews (regulation comparison, rights, licences)
- Article citations for EU AI Act given as inline text notes (no bibtex key; it's primary legislation)
- All bibtex citations follow `\textsuperscript{\cite[][p.~XX]{key}}` format
- No TikZ diagrams — none warranted for this signpost chapter
- Intro tcolorbox uses `sectionboxskin` to frame chapter scope as signpost
- Titles with commas braced correctly

## Structural Changes from Original Stub
Original stub had 6 subsections (Introduction, E-Business, IP, Privacy, InfoSec, Online Media) plus Literature.
New structure follows the task brief exactly:
- Section 1: Legal Foundations
- Section 2: Data Protection and Privacy
- Section 3: AI-Specific Regulation
- Section 4: Intellectual Property and AI
- Section 5: Cybersecurity and Liability
- Section 6: Further Reading

The old stub's E-Business/E-Commerce and Online Media/Telecommunication sections are omitted per brief (not priority for AI practitioners). This was a stated design decision in the task brief.

## Bibliography
6 new entries added to `bibliography/references.bib`:
- `lloydInformationTechnologyLaw2020` — Lloyd, Information Technology Law, 9th ed., OUP
- `lutziPrivateInternationalLaw2020` — Lutzi, Private International Law Online, OUP
- `savinEUInternetLaw2017` — Savin, EU Internet Law, 3rd ed., Elgar
- `siemsComparativeLaw2018` — Siems, Comparative Law, CUP
- `thirlwaySourcesInternationalLaw2019` — Thirlway, Sources of International Law, OUP
- `voightGDPRPracticalGuide2017` — Voight & von dem Bussche, The GDPR: A Practical Guide, Springer

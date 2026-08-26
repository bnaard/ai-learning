#!/usr/bin/env python3
"""Audit or caption inline AI Almanach tables and TikZ diagrams.

The book intentionally uses tables and figures inside tcolorbox cards, where
normal floats are not valid. In fix mode this script adds ``captionof`` entries
and stable labels to uncaptioned inline ``tblr`` and ``tikzpicture`` blocks.
Formal ``table`` and ``figure`` environments remain untouched.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "ai almanach" / "chapters"

HEADING_RE = re.compile(
    r"\\(?:chapter|section|subsection)\*?\{([^{}]+)\}"
)
CARD_RE = re.compile(
    r"\\tcbitem\[.*?title\s*=\s*(?:\{([^{}]*)\}|([^,\]]+))"
)


def sentence(text: str) -> str:
    """Return a compact caption fragment while preserving safe TeX."""
    value = " ".join(text.split()).strip()
    if not value:
        return "Engineering reference"
    return value if value[-1] in ".?!" else value + "."


def next_lines_contain(lines: list[str], start: int, needle: str) -> bool:
    """Look through nearby wrappers for an existing caption."""
    window = "".join(lines[start : start + 6])
    return needle in window or "\\caption{" in window


def caption_file(path: Path, fix: bool) -> tuple[int, int]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    output: list[str] = []
    heading = "Chapter reference"
    card = ""
    figure_depth = 0
    table_depth = 0
    table_number = 0
    figure_number = 0
    missing_tables = 0
    missing_figures = 0
    pending_after_wrapper: list[str] = []

    for index, line in enumerate(lines):
        heading_match = HEADING_RE.search(line)
        if heading_match:
            heading = heading_match.group(1)
            card = ""

        card_match = CARD_RE.search(line)
        if card_match:
            card = (card_match.group(1) or card_match.group(2) or "").strip()

        if "\\begin{figure" in line:
            figure_depth += 1
        if "\\begin{table" in line:
            table_depth += 1

        output.append(line)

        if pending_after_wrapper and line.strip() == "}":
            output.extend(pending_after_wrapper)
            pending_after_wrapper = []

        if "\\end{tblr}" in line and table_depth == 0:
            table_number += 1
            if not next_lines_contain(lines, index + 1, "\\captionof{table}"):
                missing_tables += 1
                if fix:
                    context = card if card else heading
                    caption_lines = [
                        "\\captionof{table}{"
                        + sentence(f"{heading}: {context}")
                        + "}\n",
                        (
                            f"\\label{{tab:{path.stem}-inline-"
                            f"{table_number:02d}}}\n"
                        ),
                    ]
                    closes_wrapper = (
                        index + 1 < len(lines)
                        and lines[index + 1].strip() == "}"
                    )
                    if closes_wrapper:
                        pending_after_wrapper.extend(caption_lines)
                    else:
                        output.extend(caption_lines)

        if "\\end{tikzpicture}" in line and figure_depth == 0:
            figure_number += 1
            if not next_lines_contain(lines, index + 1, "\\captionof{figure}"):
                missing_figures += 1
                if fix:
                    context = card if card else heading
                    caption_lines = [
                        "\\captionof{figure}{"
                        + sentence(f"{heading}: {context}")
                        + "}\n",
                        (
                            f"\\label{{fig:{path.stem}-inline-"
                            f"{figure_number:02d}}}\n"
                        ),
                    ]
                    closes_wrapper = (
                        index + 1 < len(lines)
                        and lines[index + 1].strip() == "}"
                    )
                    if closes_wrapper:
                        pending_after_wrapper.extend(caption_lines)
                    else:
                        output.extend(caption_lines)

        if "\\end{figure" in line:
            figure_depth = max(0, figure_depth - 1)
        if "\\end{table" in line:
            table_depth = max(0, table_depth - 1)

    if fix and output != lines:
        path.write_text("".join(output), encoding="utf-8")

    return missing_tables, missing_figures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fix",
        action="store_true",
        help="add captions and labels to uncaptioned inline blocks",
    )
    args = parser.parse_args()

    total_tables = 0
    total_figures = 0
    paths = sorted(CHAPTER_DIR.glob("ch*.tex"))
    paths.append(
        ROOT / "ai almanach" / "appendices" / "course-coverage-map.tex"
    )

    for path in paths:
        missing_tables, missing_figures = caption_file(path, args.fix)
        total_tables += missing_tables
        total_figures += missing_figures
        if missing_tables or missing_figures:
            action = "captioned" if args.fix else "missing"
            print(
                f"{path.relative_to(ROOT)}: {action} "
                f"{missing_tables} table(s), {missing_figures} figure(s)"
            )

    if args.fix:
        print(
            f"Captioned {total_tables} inline table(s) and "
            f"{total_figures} inline figure(s)."
        )
        return 0

    if total_tables or total_figures:
        print(
            f"Missing captions: {total_tables} inline table(s), "
            f"{total_figures} inline figure(s)."
        )
        return 1

    print("All inline tables and TikZ figures have captions and labels.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

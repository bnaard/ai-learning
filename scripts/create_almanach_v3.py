#!/usr/bin/env python3
"""Create semantic AI Almanach v3 chapter sources from the v2 content.

The conversion deliberately preserves subject matter, equations, tables,
citations, and TikZ pictures while discarding the v2 card/raster layer.
Generated chapters use only semantic v3 environments and normal LaTeX
hierarchy.  Run this script only when intentionally regenerating v3 sources.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "ai almanach"
V3 = ROOT / "ai almanach v3"

CHAPTERS = [
    ("orientation", "ch01-introduction.tex"),
    ("mathematics", "ch02-mathematical-foundations.tex"),
    ("programming", "ch03-programming-foundations.tex"),
    ("data-analytics", "ch04-data-analytics.tex"),
    ("machine-learning", "ch05-machine-learning.tex"),
    ("deep-learning", "ch06-deep-learning.tex"),
    ("evaluation-mlops", "ch06b-evaluation-mlops.tex"),
    ("reinforcement-learning", "ch07-reinforcement-learning.tex"),
    ("trustworthy-ai", "ch08-functional-security.tex"),
    ("computer-vision", "ch09-computer-vision.tex"),
    ("nlp-generative-ai", "ch12-nlp-voice-assistants.tex"),
    ("practical-llm-engineering", "ch12b-practical-llm-engineering.tex"),
    ("fintech", "ch10-fintech.tex"),
    ("healthcare", "ch11-healthcare.tex"),
    ("industrial-ai", "ch13-industrial-ai.tex"),
    ("supply-chain", "ch14-supply-chain.tex"),
    ("multi-agent-systems", "ch15-multi-agent-systems.tex"),
    ("commerce-marketing", "ch16-ecommerce-marketing.tex"),
    ("it-law", "ch17-it-law.tex"),
    ("visualization", "ch18-visualization.tex"),
    ("startup", "ch19-startup.tex"),
    ("scientific-writing", "ch20-scientific-writing.tex"),
]

LEADS = {
    "orientation": (
        "How do intelligent systems turn goals and data into defensible "
        "decisions?",
        ("Frame", "Represent", "Learn", "Evaluate"),
    ),
    "mathematics": (
        "Which mathematical objects make learning, uncertainty, and "
        "optimisation precise?",
        ("Objects", "Transform", "Estimate", "Optimise"),
    ),
    "programming": (
        "How does an analytical idea become reproducible, testable software?",
        ("Specify", "Implement", "Test", "Maintain"),
    ),
    "data-analytics": (
        "How does raw data become trustworthy evidence for a decision?",
        ("Acquire", "Clean", "Explore", "Govern"),
    ),
    "machine-learning": (
        "How can a model learn patterns that generalise beyond its examples?",
        ("Frame", "Baseline", "Fit", "Diagnose"),
    ),
    "deep-learning": (
        "How do layered differentiable models learn representations at scale?",
        ("Represent", "Differentiate", "Optimise", "Scale"),
    ),
    "evaluation-mlops": (
        "What evidence shows that a learned system remains useful after "
        "release?",
        ("Contract", "Test", "Release", "Monitor"),
    ),
    "reinforcement-learning": (
        "How should an agent learn when its actions change later observations?",
        ("Model", "Act", "Update", "Evaluate"),
    ),
    "trustworthy-ai": (
        "What evidence justifies trust within a stated operating boundary?",
        ("Scope", "Threats", "Controls", "Assure"),
    ),
    "computer-vision": (
        "How do pixels and geometry become testable statements about a scene?",
        ("Sense", "Represent", "Infer", "Stress-test"),
    ),
    "nlp-generative-ai": (
        "How can language systems be evaluated rather than merely admired?",
        ("Tokenise", "Represent", "Generate", "Evaluate"),
    ),
    "practical-llm-engineering": (
        "Which mechanisms and trade-offs appear in a small LLM experiment?",
        ("Trace", "Adapt", "Benchmark", "Deploy"),
    ),
    "fintech": (
        "How can AI support financial decisions under asymmetric risk?",
        ("Onboard", "Assess", "Transact", "Govern"),
    ),
    "healthcare": (
        "How can AI improve a workflow without confusing scores with benefit?",
        ("Need", "Evidence", "Integrate", "Monitor"),
    ),
    "industrial-ai": (
        "How do predictions become safe, timely actions in physical systems?",
        ("Sense", "Model", "Control", "Verify"),
    ),
    "supply-chain": (
        "How can uncertain demand and constrained resources be coordinated?",
        ("Observe", "Forecast", "Optimise", "Recover"),
    ),
    "multi-agent-systems": (
        "How can autonomous components coordinate without losing control?",
        ("Architect", "Communicate", "Coordinate", "Verify"),
    ),
    "commerce-marketing": (
        "How can personalisation create value without harmful feedback loops?",
        ("Discover", "Recommend", "Experiment", "Govern"),
    ),
    "it-law": (
        "Which duties attach to an AI system, its data, and its operators?",
        ("Classify", "Identify", "Document", "Reassess"),
    ),
    "visualization": (
        "How can a visual make evidence clearer without overstating it?",
        ("Question", "Encode", "Compare", "Explain"),
    ),
    "startup": (
        "How can an AI venture test problem, feasibility, and economics?",
        ("Problem", "Experiment", "Economics", "Scale"),
    ),
    "scientific-writing": (
        "How can a technical claim become traceable and reproducible?",
        ("Claim", "Method", "Evidence", "Revise"),
    ),
}


def extract_title(line: str, key: str = "title") -> str:
    """Extract a possibly braced tcolorbox option value."""
    marker = f"{key}="
    start = line.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    while start < len(line) and line[start].isspace():
        start += 1
    if start >= len(line):
        return ""
    if line[start] != "{":
        end = start
        while end < len(line) and line[end] not in ",]":
            end += 1
        return line[start:end].strip()
    depth = 0
    for end in range(start, len(line)):
        char = line[end]
        if char == "{" and (end == 0 or line[end - 1] != "\\"):
            depth += 1
        elif char == "}" and (end == 0 or line[end - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return line[start + 1 : end].strip()
    return ""


def extract_deep_dives() -> dict[str, str]:
    """Read balanced macro bodies from the v2 deep-dive registry."""
    source = (V2 / "chapters" / "cross-cutting-deep-dives.tex").read_text()
    pattern = re.compile(
        r"\\expandafter\\def\\csname almanachdeepdive@"
        r"([^\\]+)\\endcsname\s*\{"
    )
    result: dict[str, str] = {}
    for match in pattern.finditer(source):
        depth = 1
        cursor = match.end()
        comment = False
        while cursor < len(source) and depth:
            char = source[cursor]
            escaped = cursor > 0 and source[cursor - 1] == "\\"
            if char == "\n":
                comment = False
            elif char == "%" and not escaped:
                comment = True
            elif not comment and char == "{" and not escaped:
                depth += 1
            elif not comment and char == "}" and not escaped:
                depth -= 1
            cursor += 1
        result[match.group(1)] = source[match.end() : cursor - 1]
    return result


def transform(source: str) -> str:
    """Replace v2 presentation commands with semantic v3 markup."""
    lines = source.splitlines(keepends=True)
    output: list[str] = []
    raster_stack: list[bool] = []
    raster_scaled: list[bool] = []
    scaled_next_raster = False
    skip_next_closing_brace = False
    listing_options = False
    item_options = False
    direct_box = False

    for index, line in enumerate(lines):
        stripped = line.strip()
        next_line = lines[index + 1].strip() if index + 1 < len(lines) else ""

        if skip_next_closing_brace:
            if not stripped or stripped.startswith("%"):
                continue
            if stripped == "}":
                skip_next_closing_brace = False
                continue
            skip_next_closing_brace = False

        if item_options:
            if "]" in stripped:
                item_options = False
            continue

        if re.match(r"\\scalebox\{[^}]+\}\{$", stripped) and (
            "\\begin{tcbitemize}" in next_line
        ):
            scaled_next_raster = True
            continue

        if "\\begin{tcbitemize}" in line:
            raster_stack.append(False)
            raster_scaled.append(scaled_next_raster)
            scaled_next_raster = False
            continue

        if stripped.startswith("\\tcbitem"):
            if not raster_stack:
                raise RuntimeError("tcbitem outside tcbitemize")
            if raster_stack[-1]:
                output.append("\\end{v3topic}\n")
            title = extract_title(line)
            output.append(f"\\begin{{v3topic}}{{{title}}}\n")
            raster_stack[-1] = True
            item_options = "]" not in stripped
            continue

        if "\\end{tcbitemize}" in line:
            if not raster_stack:
                raise RuntimeError("unbalanced tcbitemize")
            if raster_stack.pop():
                output.append("\\end{v3topic}\n")
            skip_next_closing_brace = raster_scaled.pop()
            continue

        if stripped == "\\tcblower":
            output.append("\\visualseparator\n")
            continue

        if stripped.startswith("\\tcbsubtitle"):
            match = re.search(r"\{([^{}]+)\}\s*$", stripped)
            title = match.group(1) if match else ""
            output.append(f"\\topicline{{{title}}}\n")
            continue

        if stripped.startswith("\\begin{tcolorbox}"):
            title = extract_title(line) or "Context"
            output.append(f"\\begin{{v3aside}}[{title}]\n")
            direct_box = True
            continue

        if stripped == "\\end{tcolorbox}" and direct_box:
            output.append("\\end{v3aside}\n")
            direct_box = False
            continue

        if stripped.startswith("\\begin{tcblisting}"):
            listing_options = True
            output.append("\\begin{lstlisting}[language=json]\n")
            continue

        if listing_options:
            if stripped == "}" or stripped.endswith("}}"):
                listing_options = False
            continue

        if stripped == "\\end{tcblisting}":
            output.append("\\end{lstlisting}\n")
            continue

        output.append(line)

    while raster_stack:
        if raster_stack.pop():
            output.append("\\end{v3topic}\n")

    return "".join(output)


def insert_before_reading(chapter: str, addition: str) -> str:
    """Insert added semantic material before a chapter reading list."""
    marker = re.search(
        r"(?m)^\\section\{(?:Further Reading|Literature)\}", chapter
    )
    if marker:
        return (
            chapter[: marker.start()]
            + addition
            + "\n"
            + chapter[marker.start() :]
        )
    return chapter + "\n" + addition


def add_chapter_lead(chapter: str, slug: str) -> str:
    """Place the new prose-and-roadmap opening after the chapter command."""
    question, stages = LEADS[slug]
    lead = (
        "\n\\chapterlead"
        f"{{{question}}}"
        f"{{{stages[0]}}}{{{stages[1]}}}"
        f"{{{stages[2]}}}{{{stages[3]}}}"
        f"{{{slug}}}\n"
    )
    match = re.search(r"(?m)^\s*\\chapter\{.*\}\s*$", chapter)
    if not match:
        raise RuntimeError(f"chapter command missing for {slug}")
    return chapter[: match.end()] + lead + chapter[match.end() :]


def main() -> int:
    deep_dives = extract_deep_dives()
    chapter_dir = V3 / "chapters"
    chapter_dir.mkdir(parents=True, exist_ok=True)

    for slug, filename in CHAPTERS:
        source = (V2 / "chapters" / filename).read_text(encoding="utf-8")
        chapter = transform(source)
        chapter = add_chapter_lead(chapter, slug)
        deep_dive = transform(deep_dives.get(slug, ""))
        review = (
            "\\chapterreview"
            f"{{{LEADS[slug][1][0]}}}"
            f"{{{LEADS[slug][1][1]}}}"
            f"{{{LEADS[slug][1][2]}}}"
            f"{{{LEADS[slug][1][3]}}}\n"
        )
        chapter = insert_before_reading(chapter, deep_dive + "\n" + review)
        header = (
            "% Generated semantic source for AI Almanach v3.\n"
            "% Edit v3 directly after initial generation; do not overwrite\n"
            "% editorial changes by rerunning the converter casually.\n\n"
        )
        (chapter_dir / filename).write_text(
            header + chapter.lstrip(), encoding="utf-8"
        )

    print(f"Generated {len(CHAPTERS)} semantic chapters in {chapter_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

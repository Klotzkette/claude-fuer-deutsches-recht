#!/usr/bin/env python3
"""Prüft elementare Markdown-Strukturen ohne gerenderte Codeblöcke anzufassen."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
EMPTY_HEADING = re.compile(r"^\s{0,3}#{1,6}\s*$")
EMPTY_LINK = re.compile(r"!?\[[^]\n]+]\(\s*\)")
EMPTY_BULLET = re.compile(r"^\s{0,3}[-*+]\s*$")
EMPTY_NUMBERED_ITEM = re.compile(r"^\s{0,3}[1-9][0-9]?\.\s*$")
TABLE_SEPARATOR = re.compile(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
COMMAND_HEADING = re.compile(r"^/[a-z0-9-]+:[a-z0-9-]+(?: Thema: [a-z0-9-]+)?$")
PROMISED_SECTION = re.compile(
    r"(?:Rechtsprechung|Leitentscheidungen?|Leits[aä]tze?|"
    r"Quellen(?:regel|anker| und Updates)?|Disclaimer)",
    re.IGNORECASE,
)
SOURCE_RULE_MARKERS = (
    "Rechtsprechung live prüfen",
    "Keine Entscheidung aus Modellwissen",
    "Keine Kommentar-, Handbuch- oder Aufsatzfundstellen",
    "Quellenregel: Literatur nur mit Nutzerquelle",
)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in REPO.rglob("*.md")
        if ".git" not in path.parts and path.is_file()
    )


def inspect(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    problems: list[str] = []
    outside_fence: list[bool] = []
    fence_marker: str | None = None

    for number, line in enumerate(lines, start=1):
        match = FENCE.match(line)
        if match:
            marker = match.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            outside_fence.append(False)
            continue
        outside = fence_marker is None
        outside_fence.append(outside)
        if not outside:
            continue
        if EMPTY_HEADING.fullmatch(line):
            problems.append(f"{number}: leere Überschrift")
        if EMPTY_LINK.search(line):
            problems.append(f"{number}: Markdown-Link ohne Ziel")
        if EMPTY_BULLET.fullmatch(line):
            problems.append(f"{number}: leerer Listenpunkt")
        if EMPTY_NUMBERED_ITEM.fullmatch(line):
            problems.append(f"{number}: leerer nummerierter Listenpunkt")
        if (
            number > 1
            and outside_fence[number - 2]
            and line == lines[number - 2]
            and any(marker in line for marker in SOURCE_RULE_MARKERS)
        ):
            problems.append(f"{number}: unmittelbar doppelte Quellenregel")

    if fence_marker is not None:
        problems.append(f"{len(lines)}: nicht geschlossener Codeblock")

    headings: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        if not outside_fence[index]:
            continue
        match = HEADING.fullmatch(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2)))
    for position, (start, level, title) in enumerate(headings):
        # Ein nackter Skillaufruf ist ein Bedienbeispiel. Ein Bestandteil wie
        # 'quellen' im Slug verspricht keinen eigenen Quellenabschnitt.
        if COMMAND_HEADING.fullmatch(title):
            continue
        if not PROMISED_SECTION.search(title):
            continue
        if position + 1 < len(headings):
            end, next_level, _ = headings[position + 1]
            if next_level > level:
                continue
        else:
            end = len(lines)
        section = "\n".join(lines[start + 1 : end])
        section = re.sub(r"<!--.*?-->", "", section, flags=re.DOTALL)
        if not section.strip():
            problems.append(f"{start + 1}: inhaltsloser Fachabschnitt {title!r}")

    index = 0
    while index < len(lines):
        if not outside_fence[index] or not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        start = index
        while (
            index < len(lines)
            and outside_fence[index]
            and lines[index].lstrip().startswith("|")
        ):
            index += 1
        block = lines[start:index]
        if len(block) == 1:
            problems.append(f"{start + 1}: verwaiste Tabellenzeile")
        elif not TABLE_SEPARATOR.fullmatch(block[1]):
            problems.append(f"{start + 2}: Tabellen-Kopftrenner fehlt oder ist ungültig")
    return problems


def main() -> int:
    failures: list[str] = []
    files = markdown_files()
    for path in files:
        for problem in inspect(path):
            failures.append(f"{path.relative_to(REPO)}:{problem}")
    if failures:
        for failure in failures[:200]:
            print(failure, file=sys.stderr)
        if len(failures) > 200:
            print(f"... {len(failures) - 200} weitere Fehler", file=sys.stderr)
        print(
            f"validate-markdown-structure: {len(failures)} Fehler in {len(files)} Dateien",
            file=sys.stderr,
        )
        return 1
    print(f"validate-markdown-structure OK ({len(files)} Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

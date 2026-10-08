#!/usr/bin/env python3
"""Erzeugt eine strenge Baseline-Rubric fuer neue Testakten.

Die Baseline ersetzt keine fallbezogenen Checks. Sie verhindert aber, dass
eine neu angelegte Akte ohne pruefbare Mindeststruktur in den Eval-Lauf kommt.
Bestehende Rubrics werden niemals ueberschrieben.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "testakten"
SKIP_DIRS = {"megaprompts"}
KNOWN_PLUGINS = {
    "vergabestelle-behoerden",
    "bieter-unternehmen",
    "konkurrenten-rechtsschutz",
}

TEMPLATE = '''# Automatisierte Mindestpruefung; fallbezogene Checks ergaenzen.
name: "{name}"
plugin: "{plugin}"

checks:
  - id: r01-readme
    check_type: file_exists
    description: "Fallbeschreibung vorhanden"
    path: "README.md"

  - id: r02-gesamt-pdf
    check_type: file_exists
    description: "Gesamt-PDF vorhanden"
    path: "gesamt-pdf/{slug}_gesamt.pdf"

  - id: r03-aktenstuecke
    check_type: file_count
    description: "Mindestens drei Markdown-Aktenstuecke vorhanden"
    glob: "[0-9]*.md"
    min: 3

  - id: r04-einzel-pdfs
    check_type: file_count
    description: "Mindestens drei gerenderte Einzel-PDFs vorhanden"
    glob: "einzel-pdf/*.pdf"
    min: 3

  - id: r05-fiktionshinweis
    check_type: text_contains
    description: "Fiktionshinweis in der Fallbeschreibung vorhanden"
    path: "README.md"
    contains: "fiktiv"

  - id: r06-rechtsanker
    check_type: regex_match
    description: "Mindestens ein konkreter Normenanker vorhanden"
    path: "README.md"
    pattern: "§\\s*[0-9]+"

  - id: r07-fachpruefung
    check_type: human_review
    description: "Rechtsstand, Chronologie und Rollenlogik fallbezogen pruefen"
    note: "Vor Freigabe mindestens drei weitere automatisierte Fallchecks ergaenzen."
'''


def discover_plugin(readme: Path) -> str:
    """Ermittelt die Rolle aus expliziten Plugin-Nennungen im Akten-README."""
    if not readme.is_file():
        return "rollenverbund"
    text = readme.read_text(encoding="utf-8", errors="ignore")
    found = {
        match
        for match in re.findall(r"`([a-z][a-z0-9-]+)`", text)
        if match in KNOWN_PLUGINS
    }
    return next(iter(found)) if len(found) == 1 else "rollenverbund"


def main() -> int:
    created = 0
    existing = 0
    for directory in sorted(TESTAKTEN.iterdir()):
        if not directory.is_dir() or directory.name in SKIP_DIRS:
            continue
        rubric = directory / "rubric.yaml"
        if rubric.exists():
            existing += 1
            continue
        rubric.write_text(
            TEMPLATE.format(
                name=directory.name.replace("-", " ").title(),
                plugin=discover_plugin(directory / "README.md"),
                slug=directory.name,
            ),
            encoding="utf-8",
        )
        created += 1
    print(f"Default-Rubrics erzeugt: {created}; vorhanden gelassen: {existing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

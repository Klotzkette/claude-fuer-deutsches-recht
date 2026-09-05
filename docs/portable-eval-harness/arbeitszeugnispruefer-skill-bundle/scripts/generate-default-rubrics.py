#!/usr/bin/env python3
"""generate-default-rubrics.py - erzeugt fuer alle Testakten ohne rubric.yaml
eine Baseline-Pass/Fail-Rubric mit Standard-Checks. Bestehende rubric.yaml
werden NICHT ueberschrieben.

Standard-Checks:
- README vorhanden
- Gesamt-PDF vorhanden
- mindestens 1 Markdown-Aktenstueck
- Quellenhygiene-Markierung (Skill-Verweis oder keine erkennbare Halluzination)
"""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "fixtures"

TEMPLATE = '''# Auto-generierte Baseline-Rubric (v301).
# Manuelle Anpassung empfohlen - mindestens 3 weitere fall-spezifische
# Pass/Fail-Checks hinzufuegen (BAG-Az., Frist-Erwaehnung, spezifische Anlage).

name: "{name}"
plugin: "{plugin}"

checks:
  - id: r01-readme-vorhanden
    check_type: file_exists
    description: "README.md vorhanden"
    path: "README.md"

  - id: r02-gesamt-pdf-vorhanden
    check_type: file_exists
    description: "Gesamt-PDF gebaut"
    path: "gesamt-pdf/{slug}_gesamt.pdf"

  - id: r03-mindestens-3-aktenstuecke
    check_type: file_count
    description: "mindestens 3 Markdown-Aktenstuecke"
    glob: "*.md"
    min: 3

  - id: r04-fachspezifischer-check-zu-ergaenzen
    check_type: human_review
    description: "Fachspezifischer Pass/Fail-Check fuer dieses Mandat fehlt - manuell ergaenzen"
    note: "Beispiel: Vor jeder Schriftsatz-Ausgabe muss BAG-Az. live verifiziert werden"
'''


def discover_plugin(testakte_md: Path) -> str:
    """Aus der README oder Testakten-Index das primary plugin raten."""
    import re
    if testakte_md.is_file():
        text = testakte_md.read_text(encoding="utf-8", errors="ignore")
        # Suche `plugin-name` in backticks
        m = re.search(r'Plugin\s+`([a-z][a-z0-9\-]+)`', text)
        if m:
            return m.group(1)
    return "tbd"


def main() -> int:
    created = 0
    existing = 0
    for d in sorted(TESTAKTEN.iterdir()):
        if not d.is_dir():
            continue
        rubric = d / "rubric.yaml"
        if rubric.exists():
            existing += 1
            continue
        readme = d / "README.md"
        plugin = discover_plugin(readme)
        name = d.name.replace("-", " ").title()
        rubric.write_text(
            TEMPLATE.format(name=name, plugin=plugin, slug=d.name),
            encoding="utf-8",
        )
        created += 1
    print(f"Default-Rubrics erzeugt: {created}; vorhanden gelassen: {existing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

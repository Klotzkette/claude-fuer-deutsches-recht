#!/usr/bin/env python3
"""
Entfernt den frueher autogenerierten '<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->'-
Block aus allen Plugin-READMEs. Plugin-READMEs erhalten ihre Testakten-Auflistung
inzwischen ausschliesslich aus 'scripts/inject-plugin-sofort-download-section.py'.

Dieses Skript dient nur noch der Bereinigung: Wenn ein alter Block irgendwo
zurueckkehrt (z. B. durch Wiedereinspielen alter Skripte), entfernt der Aufruf
ihn idempotent. Es wird NICHTS injiziert.
"""

from __future__ import annotations

import re
from pathlib import Path

BEGIN = "<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->"
END = "<!-- END TESTAKTEN-SECTION (auto-generated) -->"
REPO = Path(__file__).resolve().parent.parent

PATTERN = re.compile(
    r"\n*" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*",
    re.DOTALL,
)


def clean_readme(readme: Path) -> bool:
    txt = readme.read_text(encoding="utf-8")
    if BEGIN not in txt:
        return False
    new = PATTERN.sub("\n\n", txt)
    new = re.sub(r"\n{3,}", "\n\n", new)
    if new == txt:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    removed = 0
    for readme in sorted(REPO.glob("*/README.md")):
        # testakten/-Ordner ausschliessen
        if readme.parts[-2] == "testakten":
            continue
        if clean_readme(readme):
            removed += 1
            print(f"  RM  {readme.relative_to(REPO)}")
    print(f"\nFertig: {removed} Plugin-READMEs bereinigt.")


if __name__ == "__main__":
    main()

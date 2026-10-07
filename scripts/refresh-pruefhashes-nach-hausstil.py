#!/usr/bin/env python3
"""Zieht die Pruefhashes in quality/evals nach, wenn sich geprufte Dateien seit dem letzten Commit
ausschliesslich mechanisch geaendert haben (Hausstil-Phrase, Formatblock). Reihenfolge bei einem
Standardwechsel: inject-ausformulierungspflicht.py, apply-hausstil.py, dieses Skript,
audit-hausstil.py, dann committen. Mit --check wird nur gelistet.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hausstil as hs  # noqa: E402
import pruefhashes  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=hs.REPO, help="Repository-Wurzel (Standard: dieses Repo)")
    parser.add_argument("--check", action="store_true", help="nur anstehende Aenderungen listen, nichts schreiben")
    parser.add_argument("--datum", default=date.today().isoformat(), help="Datum des Aenderungseintrags (JJJJ-MM-TT)")
    argumente = parser.parse_args(argv)
    repo = argumente.repo.resolve()
    stil = hs.lade_hausstil(repo / hs.QUELLDATEI)
    bilanz = pruefhashes.nachziehen(repo, stil, argumente.datum, schreiben=not argumente.check)

    for meldung in bilanz.gemeldet:
        print(meldung)
    for ort in bilanz.aktualisiert:
        print(ort)
    verb = "anstehend" if argumente.check else "aktualisiert"
    print(f"{verb}={len(bilanz.aktualisiert)} unveraendert={bilanz.unveraendert} gemeldet={len(bilanz.gemeldet)}")
    if argumente.check and bilanz.aktualisiert:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

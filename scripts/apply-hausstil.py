#!/usr/bin/env python3
"""Bringt freie Schriftangaben in Skills, Prompts, References und Eval-Rubriken auf die
kanonische Phrase aus hausstil.json. Schnellstart- und Hauptproblem-Prompts (*-schnellstart.md,
*-hauptproblem.md und ihre TXT-Kopien) erhalten wegen ihrer Bytegrenze die Kurzform ohne
Schriftnamen. Idempotent. Zeilenenden bleiben, wie sie sind; eine Datei, die kein UTF-8 ist,
wird gemeldet und uebersprungen. Mit --check wird nur gelistet.
Reihenfolge bei einem Standardwechsel: inject-ausformulierungspflicht.py, dann dieses
Skript, dann audit-hausstil.py.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hausstil as hs  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=hs.REPO, help="Repository-Wurzel (Standard: dieses Repo)")
    parser.add_argument("--check", action="store_true", help="nur anstehende Aenderungen listen, nichts schreiben")
    argumente = parser.parse_args(argv)
    repo = argumente.repo.resolve()
    stil = hs.lade_hausstil(repo / "hausstil.json")
    geaendert = []
    uebersprungen = []
    geprueft = 0
    for pfad in hs.repo_textdateien(repo, hs.ENDUNGEN_ANWENDEN):
        if pfad == hs.QUELLDATEI or hs.ist_ausgenommen(pfad, stil):
            continue
        datei = repo / pfad
        # Bytes statt Text, damit CRLF-Zeilenenden nicht stillschweigend zu LF werden.
        try:
            alt = datei.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            uebersprungen.append(pfad)
            continue
        geprueft += 1
        neu = hs.ersetze_schriftangaben(alt, stil)
        if pfad.endswith(hs.KURZFORM_ENDUNGEN):
            neu = hs.kurzform(neu, stil)
        if neu == alt:
            continue
        geaendert.append(pfad)
        if not argumente.check:
            datei.write_bytes(neu.encode("utf-8"))

    for pfad in uebersprungen:
        print(f"{pfad}: keine UTF-8-Datei, übersprungen")
    for pfad in geaendert:
        print(pfad)
    verb = "anstehend" if argumente.check else "geschrieben"
    print(f"geprueft={geprueft} {verb}={len(geaendert)} uebersprungen={len(uebersprungen)} "
          f"phrase={hs.kanonische_phrase(stil)!r}")
    if argumente.check and geaendert:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Stellt sicher, dass für jede Vorlagen-Markdown eine gleichnamige <slug>.md.zip
existiert und ihren Inhalt unverändert enthält.

Der Download-Block jeder Vorlagen-README verweist auf diese ZIP, weil GitHub
.md-Dateien als text/plain ausliefert und Browser sie inline anzeigen. Die ZIP
gewährleistet einen verlässlichen Direkt-Download.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import md_in, vorlagenordner  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def pruefe_zip(md: Path) -> list[str]:
    fehler: list[str] = []
    zip_pfad = md.with_suffix(".md.zip")
    if not zip_pfad.is_file():
        fehler.append(f"{zip_pfad.relative_to(REPO)}: ZIP fehlt zu {md.name}")
        return fehler
    try:
        with zipfile.ZipFile(zip_pfad) as z:
            namen = z.namelist()
            if namen != [md.name]:
                fehler.append(
                    f"{zip_pfad.relative_to(REPO)}: erwartete genau einen Eintrag '{md.name}', "
                    f"enthielt {namen}"
                )
                return fehler
            inhalt = z.read(md.name)
    except zipfile.BadZipFile as exc:
        fehler.append(f"{zip_pfad.relative_to(REPO)}: ZIP-Datei nicht lesbar ({exc})")
        return fehler
    if inhalt != md.read_bytes():
        fehler.append(
            f"{zip_pfad.relative_to(REPO)}: Inhalt weicht von {md.name} ab — bitte mit "
            f"scripts/build-md-zips.py neu erzeugen"
        )
    return fehler


def main() -> int:
    fehler: list[str] = []
    untersucht = 0
    for ordner in vorlagenordner(REPO):
        md = md_in(ordner)
        if md is None:
            continue
        untersucht += 1
        fehler.extend(pruefe_zip(md))
    if fehler:
        print(f"check-md-zip-integrity FEHLER ({len(fehler)} Probleme):")
        for f in fehler:
            print(f"  {f}")
        return 1
    print(f"check-md-zip-integrity OK ({untersucht} Vorlagen, ZIP synchron)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

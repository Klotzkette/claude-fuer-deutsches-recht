#!/usr/bin/env python3
"""Erzeugt für jede Vorlagen-Markdown eine gleichnamige <slug>.md.zip im selben
Ordner.

Hintergrund: GitHub serviert .md-Dateien mit Content-Type: text/plain, was
Browser dazu bringt, sie inline anzuzeigen statt herunterzuladen. ZIP-Dateien
werden dagegen mit application/zip ausgeliefert und vom Browser zuverlässig
zum Download angeboten.

Pro Vorlage entsteht eine deterministische ZIP, die genau die Markdown-Datei
enthält. Zeitstempel werden auf 2026-01-01 gesetzt, damit die ZIPs bei
unverändertem Inhalt byte-identisch bleiben (reproduzierbar).
"""
from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

# Importiert die kanonische Vorlagensuche.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import md_in, vorlagenordner  # type: ignore  # noqa: E402
from _atomar import bytes_atomar_schreiben  # type: ignore  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def build_zip(md_pfad: Path) -> bool:
    """Schreibt <slug>.md.zip neben <slug>.md. Gibt True zurück, wenn die ZIP
    neu erzeugt oder ersetzt wurde."""
    zip_pfad = md_pfad.with_suffix(".md.zip")
    inhalt = md_pfad.read_bytes()
    # Deterministischer Zeitstempel (Y, M, D, h, m, s)
    zeit = (2026, 1, 1, 0, 0, 0)
    neu = zipfile.ZipInfo(md_pfad.name, date_time=zeit)
    neu.compress_type = zipfile.ZIP_DEFLATED
    neu.external_attr = (0o644 & 0xFFFF) << 16

    # Zielinhalt erzeugen.
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr(neu, inhalt)
    zielbytes = puffer.getvalue()

    if zip_pfad.is_file() and zip_pfad.read_bytes() == zielbytes:
        return False
    def pruefen(temp_pfad: Path) -> None:
        with zipfile.ZipFile(temp_pfad, "r") as archiv:
            if archiv.testzip() is not None:
                raise RuntimeError(f"CRC-Fehler in neuer Markdown-ZIP: {zip_pfad}")
            if archiv.namelist() != [md_pfad.name]:
                raise RuntimeError(f"Falscher Inhalt in neuer Markdown-ZIP: {zip_pfad}")
            if archiv.read(md_pfad.name) != inhalt:
                raise RuntimeError(f"Markdown-ZIP weicht von der Quelle ab: {zip_pfad}")

    bytes_atomar_schreiben(zip_pfad, zielbytes, pruefen=pruefen)
    return True


def main() -> int:
    geschrieben = 0
    untersucht = 0
    for ordner in vorlagenordner(REPO):
        md = md_in(ordner)
        if md is None:
            continue
        untersucht += 1
        if build_zip(md):
            geschrieben += 1
    print(f"build-md-zips OK ({untersucht} Vorlagen, {geschrieben} ZIPs aktualisiert)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

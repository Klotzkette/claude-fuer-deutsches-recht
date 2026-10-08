#!/usr/bin/env python3
"""Prüft, dass keine ODT-Fassung den Fließtext in eine enge, zentrierte
Spalte zwingt.

Hintergrund: Pandocs `multiline_tables`/`simple_tables` deuten die `---`-
Trennlinien zwischen Abschnitten fälschlich als Tabellenränder und packen
ganze Rubrum- oder Vertragstexte in eine einspaltige, mittig zentrierte
Tabelle. Das sieht im Dokument aus wie eine schmale Kolumne in der Blattmitte.

Repo-Regel: Niemals eine enge, zentrierte Spalte im Dokument — weder im
Rubrum noch im Body. Body-Text gehört in normale Absätze über die volle
Satzbreite, nicht in eine einspaltige Tabelle.

Der Check meldet einen Fehler, wenn eine `<table:table>` einspaltig ist und
nennenswert Fließtext enthält, oder wenn in einer Tabellenzelle wörtliche
Markdown-Marken (`##`, Aufzählungs-`- `) auftauchen — beides sind sichere
Zeichen für fälschlich tabellierten Body-Text.
"""
from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

TABLE_RE = re.compile(r"<table:table\b[^>]*>(.*?)</table:table>", re.S)
COL_RE = re.compile(r"<table:table-column\b")
TAG_RE = re.compile(r"<[^>]+>")

# Schwellen: ab so viel Zelltext gilt eine einspaltige Tabelle als
# fälschlich tabellierter Body.
EINSPALTIG_MAX_ZEICHEN = 200


def zelltext(table_xml: str) -> str:
    text = TAG_RE.sub(" ", table_xml)
    text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return re.sub(r"\s+", " ", text).strip()


def pruefe_odt(path: Path) -> list[str]:
    fehler: list[str] = []
    try:
        with zipfile.ZipFile(path, "r") as zf:
            content = zf.read("content.xml").decode("utf-8", errors="ignore")
    except (zipfile.BadZipFile, KeyError):
        return [f"{path.relative_to(REPO)}: content.xml nicht lesbar"]

    for tbl in TABLE_RE.finditer(content):
        body = tbl.group(1)
        spalten = len(COL_RE.findall(body))
        text = zelltext(body)
        # 1) wörtliche Markdown-Überschrift in einer Zelle → Body falsch tabelliert
        if re.search(r"(^|\s)#{2,4}\s", text):
            fehler.append(
                f"{path.relative_to(REPO)}: Tabellenzelle enthält wörtliche "
                f"Markdown-Überschrift (Body in Tabelle): {text[:60]!r}"
            )
            break
        # 2) einspaltige Tabelle mit viel Fließtext → enge zentrierte Spalte
        if spalten <= 1 and len(text) > EINSPALTIG_MAX_ZEICHEN:
            fehler.append(
                f"{path.relative_to(REPO)}: einspaltige Tabelle mit "
                f"{len(text)} Zeichen Fließtext (enge zentrierte Spalte): {text[:60]!r}"
            )
            break
    return fehler


def odt_dateien() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "*/*.odt"],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    return [REPO / line for line in result.stdout.splitlines()]


def main() -> int:
    fehler: list[str] = []
    n = 0
    for odt in odt_dateien():
        if " 2." in odt.name:  # Dubletten-Schutz
            continue
        n += 1
        fehler.extend(pruefe_odt(odt))

    if fehler:
        print("check-odt-spaltenlayout: FEHLER (enge zentrierte Spalte / Body in Tabelle)")
        for e in fehler[:200]:
            print(" -", e)
        if len(fehler) > 200:
            print(f" ... ({len(fehler) - 200} weitere)")
        return 1
    print(f"check-odt-spaltenlayout OK ({n} ODT-Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Prüft alle sprechend benannten ODT-Dateien auf Integrität und Basislayout."""
from __future__ import annotations

import importlib.util
import re
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"

spec = importlib.util.spec_from_file_location(
    "md_to_odt_integrity",
    SCRIPTS / "md-to-odt.py",
)
if spec is None or spec.loader is None:
    raise RuntimeError("md-to-odt.py konnte nicht geladen werden")
md_to_odt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md_to_odt)

SEITENPROFILE = {
    "A4-Hochformat": (
        'style:print-orientation="portrait"',
        'fo:page-width="21cm"',
        'fo:page-height="29.7cm"',
        'fo:margin-left="2.5cm"',
        'fo:margin-right="2.5cm"',
    ),
    "A4-Querformat für breite Tabellen": (
        'style:print-orientation="landscape"',
        'fo:page-width="29.7cm"',
        'fo:page-height="21cm"',
        'fo:margin-left="2cm"',
        'fo:margin-right="2cm"',
    ),
}


def odt_files() -> list[Path]:
    candidates = [*REPO.glob("*/*/*.odt"), *REPO.glob("*.odt")]
    return sorted(
        (
            p
            for p in candidates
            if " 2." not in p.name and " 2." not in str(p.relative_to(REPO))
        ),
        key=lambda p: str(p.relative_to(REPO)),
    )


def pruefe_erstseitenhinweis(styles: str) -> list[str]:
    errors: list[str] = []
    if styles.count("<style:footer-first") != 1:
        errors.append("Dokument enthält nicht genau eine Erstseiten-Fußzeile")
    match = re.search(
        r'<style:footer-first\b[^>]*>[\s\S]*?</style:footer-first>',
        styles,
    )
    if match is None:
        return ["Erstseiten-Fußzeile fehlt"]
    first_footer = match.group(0)
    for notice in (
        md_to_odt.FIRST_PAGE_NOTICE_DE,
        md_to_odt.FIRST_PAGE_NOTICE_EN,
    ):
        if notice not in first_footer:
            errors.append(f"Erstseitenhinweis fehlt: {notice}")
        if styles.count(notice) != 1:
            errors.append(f"Erstseitenhinweis steht nicht genau einmal im Dokument: {notice}")
    if f'text:style-name="{md_to_odt.FIRST_PAGE_NOTICE_STYLE}"' not in first_footer:
        errors.append("Erstseitenhinweis verwendet nicht den verbindlichen Fußzeilenstil")
    return errors


def check_one(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        with zipfile.ZipFile(path, "r") as zf:
            names = set(zf.namelist())
            for required in ("mimetype", "content.xml", "styles.xml"):
                if required not in names:
                    errors.append(f"{required} fehlt")
            if errors:
                return errors
            content = zf.read("content.xml").decode("utf-8", errors="ignore")
            styles = zf.read("styles.xml").decode("utf-8", errors="ignore")
    except zipfile.BadZipFile:
        return ["keine gültige ODT-ZIP-Datei"]

    if "<office:text" not in content or len(content) < 1000:
        errors.append("content.xml wirkt leer oder beschädigt")
    if not any(
        all(merkmal in styles for merkmal in merkmale)
        for merkmale in SEITENPROFILE.values()
    ):
        errors.append(
            "kein zulässiges Seitenprofil: erwartet A4-Hochformat mit 2,5 cm "
            "Seitenrändern oder A4-Querformat mit 2 cm seitlichen Rändern"
        )
    markdown = path.with_suffix(".md")
    if markdown.is_file():
        erwartet_querformat = md_to_odt.needs_landscape_layout(
            markdown.read_text(encoding="utf-8")
        )
        ist_querformat = 'style:print-orientation="landscape"' in styles
        if erwartet_querformat != ist_querformat:
            erwartet = "A4-Querformat" if erwartet_querformat else "A4-Hochformat"
            errors.append(
                f"Seitenprofil ist nicht quellensynchron; erwartet {erwartet}"
            )
    for needle in (
        'fo:margin-top="2.5cm"',
        'fo:margin-bottom="2.5cm"',
        "Times New Roman",
        "11pt",
        'fo:line-height="121%"',
        'fo:margin-bottom="0.095in"',
        'fo:margin-top="0.26in"',
        'fo:line-height="114%"',
        "<style:footer>",
        "<style:footer-first",
        "<text:page-number",
        'fo:text-align="end"',
    ):
        if needle not in styles:
            errors.append(f"Layoutmerkmal fehlt: {needle}")
    if 'style:font-name="Arial"' in styles:
        errors.append("Überschriftenstil nutzt noch Arial statt Times New Roman")
    errors.extend(pruefe_erstseitenhinweis(styles))
    return errors


def main() -> int:
    errors: list[tuple[Path, list[str]]] = []
    files = odt_files()
    for path in files:
        result = check_one(path)
        if result:
            errors.append((path, result))

    if errors:
        print("check-odt-integrity: FEHLER")
        for path, problems in errors:
            print(f" - {path.relative_to(REPO)}")
            for problem in problems:
                print(f"   - {problem}")
        return 1

    print(f"check-odt-integrity OK ({len(files)} ODT-Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

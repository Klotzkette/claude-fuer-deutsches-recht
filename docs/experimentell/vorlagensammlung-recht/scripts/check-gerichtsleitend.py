#!/usr/bin/env python3
"""Prueft den Sonderbereich `vorlagen-gerichtsleitend/`.

Diese Dateien sind bewusst Markdown-only: echte deutsche Umlaute im
Fliesstext, eckige Platzhalter, keine spitzen Klammern, Paragraphenzeichen
im Mustertext, keine geraden Anfuehrungszeichen, keine Komma-Zahlen und
keine ODT-/ZIP-Pflicht. Warnhinweis-Bloecke duerfen "Paragraf" ausschreiben,
damit sie sich sichtbar vom Tenor- und Verfuegungstext absetzen.

Der Bereich deckt richterliche Schriftvorlagen ab und seit v3.3.0 auch
staatsanwaltschaftliche und amtsanwaltschaftliche Vorlagen. Plugin- und
Skill-Querverweise auf andere Repos sind seit v3.3.1 verboten; die
Vorlagen stehen fuer sich.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "vorlagen-gerichtsleitend"

EXPECTED_FOLDERS = {
    "ag-zivil": (5, 10),
    "ag-straf": (5, 10),
    "ag-insolvenz-restrukturierung": (5, 10),
    "ag-handelsregister": (5, 10),
    "familiengericht": (5, 10),
    "lg-zivilkammer": (5, 10),
    "lg-strafkammer": (5, 10),
    "verwaltungsgericht": (5, 10),
    "finanzgericht": (5, 10),
    "sozialgericht": (5, 10),
    "arbeitsgericht": (5, 10),
    "bverfg-kammer": (5, 10),
    "staatsanwaltschaft-ermittlungsverfahren": (5, 10),
    "staatsanwaltschaft-abschlussentscheidung": (5, 10),
    "staatsanwaltschaft-hauptverhandlung": (5, 10),
    "staatsanwaltschaft-rechtsmittel-vollstreckung": (5, 10),
    "amtsanwaltschaft": (5, 10),
    "strafvollstreckungskammer-beschwerdegericht": (5, 10),
}

REQUIRED_SECTIONS = [
    "## Anwendungsbereich",
    "## Pflichtangaben",
    "## Mustertext mit Platzhaltern",
    "## Hinweise zur Verwendung",
]

# Plugin- und Skill-Verweise auf andere Repos sind seit v3.3.1 verboten.
# Der Sonderbereich steht eigenstaendig; verwandte Skills oder Plugins
# leben in `claude-fuer-deutsches-recht`, nicht hier.
FORBIDDEN_CROSS_LINK_MARKERS = (
    "_GERICHTE_EXPERIMENTAL",
    "## Korrespondierendes Plugin",
    "Korrespondierendes Plugin und Skill",
    "claude-fuer-deutsches-recht",
    "claude-f\u00fcr-deutsches-recht",
)

# Die Anker-Sektion darf den Lueckenlisten-Begriff mit echtem Umlaut oder in
# ASCII-Schreibung tragen; aeltere Vorlagen nutzen die ASCII-Variante.
ANKER_SECTION_VARIANTS = (
    "## Anker-Rechtsprechung und Lückenliste",
    "## Anker-Rechtsprechung und Lueckenliste",
)

# Schlussmarkierung am Ende des Mustertextes. Richterliche Vorlagen tragen die
# richterliche, staatsanwaltschaftliche und amtsanwaltschaftliche Vorlagen die
# staatsanwaltschaftliche Variante.
FINAL_MARKERS = (
    "Vorschlag zur richterlichen Prüfung. Kein automatisierter Letztentscheid. "
    "Aktengeheimnis und Datenschutz wahren.",
    "Vorschlag zur staatsanwaltschaftlichen Prüfung. Kein automatisierter Letztentscheid. "
    "Aktengeheimnis und Datenschutz wahren.",
)

SLUG_RE = re.compile(r"^[a-z0-9-]{1,64}$")
DECIMAL_COMMA_RE = re.compile(r"\d,\d")
FORBIDDEN_WORD_RE = re.compile(r"\b(?:scrape|scraping|crawl|crawling)\b", re.I)
# Im INDEX zählen nur Links der Form <bereich>/<vorlage>.md als Vorlagen.
# Navigationslinks auf README.md bleiben davon bewusst unberührt.
INDEX_LINK_RE = re.compile(r"\]\(([a-z0-9-]+/[a-z0-9-]+\.md)\)")


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def ohne_eigene_downloadziele(text: str) -> str:
    """Nur vorhandene Dateien dieser Kopie sind keine Plugin-Querverweise."""
    prefix = (
        "https://github.com/Klotzkette/claude-fuer-deutsches-recht/"
        "raw/main/docs/experimentell/vorlagensammlung-recht/"
    )

    def ersetzen(match: re.Match[str]) -> str:
        ziel = (REPO / match.group(1)).resolve()
        if ziel.is_relative_to(REPO.resolve()) and ziel.is_file():
            return "download:" + match.group(1)
        return match.group(0)

    return re.sub(re.escape(prefix) + r"([A-Za-z0-9_./-]+)", ersetzen, text)


def pruefe_text(path: Path, text: str, is_template: bool) -> list[str]:
    errors: list[str] = []
    for nr, line in enumerate(text.splitlines(), start=1):
        klammertiefe = 0
        for zeichen in line:
            if zeichen == "[":
                klammertiefe += 1
                if klammertiefe > 1:
                    errors.append(f"{rel(path)}:{nr}: verschachtelter Platzhalter verboten")
                    break
            elif zeichen == "]" and klammertiefe:
                klammertiefe -= 1
        if "<" in line or ">" in line:
            errors.append(f"{rel(path)}:{nr}: spitze Klammer verboten")
        if '"' in line:
            errors.append(f"{rel(path)}:{nr}: doppelte Anfuehrungszeichen vermeiden")
        if DECIMAL_COMMA_RE.search(line):
            errors.append(f"{rel(path)}:{nr}: Komma-Zahl verboten")
        if FORBIDDEN_WORD_RE.search(line):
            errors.append(f"{rel(path)}:{nr}: verbotene Abruf-/Crawl-Sprache")
    if is_template:
        if not text.startswith("# "):
            errors.append(f"{rel(path)}: Titelzeile '# ...' fehlt")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{rel(path)}: Pflichtabschnitt fehlt: {section}")
        if not any(variant in text for variant in ANKER_SECTION_VARIANTS):
            errors.append(
                f"{rel(path)}: Pflichtabschnitt fehlt: ## Anker-Rechtsprechung und Lückenliste"
            )
        if not any(marker in text for marker in FINAL_MARKERS):
            errors.append(f"{rel(path)}: Pflichtmarkierung am Mustertextende fehlt")
        if not re.search(r"\[[^\]]+\]", text):
            errors.append(f"{rel(path)}: keine eckigen Platzhalter gefunden")
    querverweise = ohne_eigene_downloadziele(text)
    for marker in FORBIDDEN_CROSS_LINK_MARKERS:
        if marker in querverweise:
            errors.append(
                f"{rel(path)}: Plugin-/Skill-Querverweis verboten ('{marker}')"
            )
    return errors


def main() -> int:
    errors: list[str] = []
    if not ROOT.is_dir():
        print("check-gerichtsleitend: FEHLER")
        print(" - vorlagen-gerichtsleitend/: Ordner fehlt")
        return 1

    for required in ("README.md", "INDEX.md"):
        if not (ROOT / required).is_file():
            errors.append(f"vorlagen-gerichtsleitend/{required}: Datei fehlt")

    vorhandene = {p.name for p in ROOT.iterdir() if p.is_dir()}
    for name in sorted(set(EXPECTED_FOLDERS) - vorhandene):
        errors.append(f"vorlagen-gerichtsleitend/{name}/: Gerichtsbarkeit fehlt")
    for name in sorted(vorhandene - set(EXPECTED_FOLDERS)):
        errors.append(f"vorlagen-gerichtsleitend/{name}/: unerwarteter Unterordner")

    templates: list[Path] = []
    for folder, (minimum, maximum) in sorted(EXPECTED_FOLDERS.items()):
        base = ROOT / folder
        if not base.is_dir():
            continue
        readme = base / "README.md"
        if not readme.is_file():
            errors.append(f"{rel(readme)}: Datei fehlt")
        files = sorted(p for p in base.glob("*.md") if p.name != "README.md")
        if not minimum <= len(files) <= maximum:
            errors.append(
                f"{rel(base)}: erwartete {minimum}-{maximum} Vorlagen, gefunden {len(files)}"
            )
        for file in files:
            if not SLUG_RE.fullmatch(file.stem):
                errors.append(f"{rel(file)}: Slug unzulaessig oder laenger als 64 Zeichen")
            templates.append(file)

    for file in sorted(ROOT.rglob("*.md")):
        text = file.read_text(encoding="utf-8")
        is_template = file.parent != ROOT and file.name != "README.md"
        errors.extend(pruefe_text(file, text, is_template))

    index = ROOT / "INDEX.md"
    if index.is_file():
        indexed = set(INDEX_LINK_RE.findall(index.read_text(encoding="utf-8")))
        expected = {p.relative_to(ROOT).as_posix() for p in templates}
        for missing in sorted(expected - indexed):
            errors.append(f"vorlagen-gerichtsleitend/INDEX.md: Vorlage fehlt im Index: {missing}")
        for extra in sorted(indexed - expected):
            errors.append(f"vorlagen-gerichtsleitend/INDEX.md: Linkziel ist keine Vorlage: {extra}")

    downloads = REPO / "DOWNLOADS.md"
    if not downloads.is_file():
        errors.append("DOWNLOADS.md: Datei fehlt")
    else:
        download_text = downloads.read_text(encoding="utf-8")
        for folder in sorted(EXPECTED_FOLDERS):
            readme = ROOT / folder / "README.md"
            if readme.is_file():
                ziel = f"../../DOWNLOADS.md#sonder-{folder}"
                if ziel not in readme.read_text(encoding="utf-8"):
                    errors.append(f"{rel(readme)}: bereichsspezifischer Downloadlink fehlt")
        for template in templates:
            ziel = template.relative_to(REPO).as_posix()
            if f"]({ziel})" not in download_text:
                errors.append(f"DOWNLOADS.md: Vorschau fehlt für {ziel}")
            raw = (
                "https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/"
                f"{ziel}"
            )
            if raw not in download_text:
                errors.append(f"DOWNLOADS.md: Direktdownload fehlt für {ziel}")

    if errors:
        print(f"check-gerichtsleitend: FEHLER ({len(errors)} Probleme):")
        for error in errors[:200]:
            print(" -", error)
        if len(errors) > 200:
            print(f" - ... weitere {len(errors) - 200} Probleme")
        return 1
    print(
        "check-gerichtsleitend OK "
        f"({len(templates)} Vorlagen, {len(EXPECTED_FOLDERS)} Gerichtsbarkeiten)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Gemeinsamer Filter fuer Testakten-Exportdateien.

Die Repo-README und redaktionelle Uebersichten sind fuer GitHub wichtig, sollen
aber nicht in den Arbeitsmaterial-Dump gelangen. Gesamt-PDFs und Testakten-ZIPs
muessen wie eine Anwaltsakte aufgehen: Aktenstuecke, Anlagen, Mails, Tabellen,
Bilder und Original-PDFs, aber weder Markdown noch Vorfuehr- oder
Download-Hinweise.
"""

from __future__ import annotations

from functools import lru_cache
from html import unescape
from pathlib import Path
import re
import zipfile

TEXT_EXTS = {".md", ".txt", ".csv", ".eml"}
CONTENT_SCAN_EXTS = TEXT_EXTS | {".docx", ".xlsx", ".odt", ".json", ".xml", ".yaml", ".yml"}

META_MARKERS = (
    "demonstrationsakte",
    "demonstrations-testakte",
    "demonstrationszweck",
    "plugin-test",
    "plugin-testing",
    "plugin-testsystem",
    "plugin demonstration",
    "plugin-demonstration",
    "demo-akte",
    "vorfuehrziel",
    "vorführziel",
    "testzweck",
    "ausschließlich testzwecken",
    "ausschliesslich testzwecken",
    "nur zu testzwecken",
    "diese akte eignet sich",
    "direkt-download",
    "download der akte",
    "github-release",
)

META_NAME_PARTS = (
    "readme",
    "qualitaetsstandard",
    "qualitätsstandard",
    "direkt-download",
    "download",
    "loesungspfad",
    "lösungspfad",
    "pflichtanker",
    "streitstoff-liste",
    "streitstoffliste",
    "musterloesung",
    "musterlösung",
    "loesungsskizze",
    "lösungsskizze",
    "erwartungshorizont",
    "pruefervermerk",
    "prüfervermerk",
    "red-team",
    "red_team",
    "redteam",
    "finalcheck",
    "antwortmatrix",
    "anspruchsmatrix",
    "rechenhinweise",
    "kandidatenloesung",
    "kandidatenlösung",
    "loesungsliste",
    "lösungsliste",
    "eigene-stellungnahme-loesung",
    "eigene-stellungnahme-lösung",
    "beschlussentwurf_loesung",
    "beschlussentwurf_lösung",
    "aufgabenloesungsansatz",
    "aufgabenlösungsansatz",
    "klageraster",
    "kurzvotum",
    "quality_gate",
    "quality-gate",
    "qualitaetsgate",
    "qualitätsgate",
    "pruefraster",
    "prüfraster",
    "pruefvermerk",
    "prüfvermerk",
    "rechtsprechungsanalyse",
    "rechtsanalyse",
    "rechtsgutachten",
    "chronologie_arbeitsstand",
    "klagestrategie",
    "beratungsmemo",
    "beratervermerk",
    "antwortstrategie",
    "strategie_und_vergleichskorridor",
    "gesamtstrategie",
    "kanzleistrategie",
    "strategiememorandum",
    "verhandlungsstrategie",
    "prozessstrategie",
    "anwaltsstrategie",
    "rechtsanwalt_position",
    "testamentsauslegungs_vermerk",
    "bewertung_bildrechte_nachlass",
    "interne_risikoampel",
    "intern_berechnung",
    "intern_monatsraster",
    "kanzleinotizen_intern",
    "gerichtliche_route",
    "zieloutput_checkliste",
    "schutzschirmantrag_vorbereitung",
    "sachwalter_eigenverwaltung_notiz",
    "arbeitsvermerk",
    "prueffragen-fuer-erstgespraech",
    "prüffragen-für-erstgespräch",
    "entwurf_naechstes_schreiben",
    "entwurf-naechstes-schreiben",
    "99_arbeitsstand",
    "clean_entwurf_checkliste",
    "dozenten_uebersicht",
    "dozenten-uebersicht",
    "notiz_vergleich_krisenstadien",
)

META_EXACT_NAMES = {
    "02-fristen-kosten-risiken.csv",
    "02-fristen-risiken-dashboard.csv",
    "07-chronologie-und-aktenstand.docx",
    "08-gutachtenstand.docx",
    "09-gegenschreiben-oder-behoerde.docx",
    "10-entwurf-stellungnahme.docx",
    "11-besprechungsprotokoll.docx",
    "13-beweis-und-fristenlog.csv",
    "90-ergaenzende-korrespondenz-und-vollvermerke.docx",
    "91_fristsachen_belege_offene_punkte_2026-07-06.csv",
}

CONTENT_MARKER_NAME_PARTS = META_NAME_PARTS + (
    "hinweis",
    "hinweise",
    "info",
    "index",
    "meta",
    "uebersicht",
    "übersicht",
)

EXPORT_BLOCKING_CONTENT_MARKERS = (
    "musterlösung",
    "musterloesung",
    "lösungsskizze",
    "loesungsskizze",
    "antwortmatrix",
    "erwartungshorizont",
    "prüferhinweis",
    "prueferhinweis",
    "[fragment",
    "fragmentarisch",
    "lorem ipsum",
    "inhalt folgt",
    "hier würde der inhalt",
    "hier wuerde der inhalt",
    "platzhalter",
    "fiktives beispieldokument",
    "fiktive lernakte",
    "fiktive testakte",
    "dieses dokument ist fiktiv",
    "ausschließlich zu übungszwecken",
    "ausschliesslich zu uebungszwecken",
    "für testzwecke",
    "fuer testzwecke",
    "alle daten fiktiv",
    "testakte zum plugin",
    "testakte:",
    "[az fiktiv]",
    "nur als fragment",
    "fragment statt vollständigem dokument",
    "fragment statt vollstaendigem dokument",
)

PLACEHOLDER_PATTERN = re.compile(
    r"\[\s*(?:\.{3}|datum(?:[^\]]{0,80})?|date(?:[^\]]{0,80})?)\s*\]",
    re.IGNORECASE,
)

INITIAL_OVERVIEW_PARTS = (
    "aktenuebersicht",
    "aktenübersicht",
    "akte-uebersicht",
    "akte-übersicht",
    "soforttriage",
)

def _xml_text(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="ignore")
    text = re.sub(r"<[^>]+>", " ", text)
    return unescape(re.sub(r"\s+", " ", text))


@lru_cache(maxsize=16_384)
def _safe_text(path: Path, limit: int = 160_000) -> str:
    try:
        suffix = path.suffix.lower()
        if suffix in {".docx", ".xlsx", ".odt"} and zipfile.is_zipfile(path):
            member_prefixes = {
                ".docx": ("word/document.xml", "word/header", "word/footer"),
                ".xlsx": ("xl/sharedStrings.xml", "xl/worksheets/"),
                ".odt": ("content.xml",),
            }[suffix]
            chunks: list[str] = []
            consumed = 0
            with zipfile.ZipFile(path) as archive:
                for name in archive.namelist():
                    if not any(name == prefix or name.startswith(prefix) for prefix in member_prefixes):
                        continue
                    raw = archive.read(name)
                    chunks.append(_xml_text(raw[: max(0, limit - consumed)]))
                    consumed += len(raw)
                    if consumed >= limit:
                        break
            return " ".join(chunks).lower()
        with path.open("rb") as fh:
            return fh.read(limit).decode("utf-8", errors="ignore").lower()
    except Exception:
        return ""


def _contains_blocking_export_content(path: Path, *, allow_template_fields: bool = False) -> bool:
    if path.suffix.lower() not in CONTENT_SCAN_EXTS:
        return False
    if "formatvorlagen-paradebeispiele" in path.parts:
        return False
    text = _safe_text(path)
    markers = (marker for marker in EXPORT_BLOCKING_CONTENT_MARKERS
               if not (allow_template_fields and marker == 'platzhalter'))
    return any(marker in text for marker in markers) or (
        not allow_template_fields and bool(PLACEHOLDER_PATTERN.search(text))
    )


def _is_initial_overview(path: Path, testakte_dir: Path) -> bool:
    try:
        rel = path.relative_to(testakte_dir)
    except ValueError:
        return False
    if len(rel.parts) != 1:
        return False
    stem = path.stem.lower()
    compact = stem.replace("_", "-")
    starts_as_front_piece = compact.startswith(("00-", "01-", "00.", "01."))
    return starts_as_front_piece and any(part in stem for part in INITIAL_OVERVIEW_PARTS)


def is_allowed_markdown_aktenstueck(path: Path, testakte_dir: Path) -> bool:
    """Markdown ist als exportiertes Aktenstueck ausnahmslos unzulaessig."""
    return False


def is_export_meta_file(path: Path, testakte_dir: Path) -> bool:
    """True, wenn die Datei nicht in PDF/ZIP-Arbeitsmaterial gehoert."""
    name = path.name.lower()
    stem = path.stem.lower()
    if name in META_EXACT_NAMES:
        return True
    if name == "readme.md":
        return True
    if is_allowed_markdown_aktenstueck(path, testakte_dir):
        return False
    if any(part in stem for part in META_NAME_PARTS):
        return True
    relative = path.relative_to(testakte_dir)
    requested_template = (
        testakte_dir.name == 'bauwirtschaft-hildesheim-lebensakte'
        and relative.parts[0] == '12_Wordvorlagen'
        and path.suffix.lower() == '.docx'
    )
    if _contains_blocking_export_content(path, allow_template_fields=requested_template):
        return True
    if _is_initial_overview(path, testakte_dir):
        return True
    if path.suffix.lower() in TEXT_EXTS and any(part in stem for part in CONTENT_MARKER_NAME_PARTS):
        text = _safe_text(path)
        if any(marker in text for marker in META_MARKERS):
            return True
    return False


def include_in_working_dump(path: Path, testakte_dir: Path, *, include_gesamt_pdf: bool = False) -> bool:
    """Export-Entscheidung fuer eine einzelne Datei innerhalb einer Testakte."""
    if not path.is_file():
        return False
    try:
        rel = path.relative_to(testakte_dir)
    except ValueError:
        return False
    if any(part.startswith(".") for part in rel.parts):
        return False
    if "__pycache__" in rel.parts or path.name == ".DS_Store":
        return False
    if path.name.lower() == "rubric.yaml":
        return False
    if path.suffix.lower() == ".md":
        return False
    if path.suffix.lower() == ".py" and path.stem.lower().startswith("build_"):
        return False
    if "gesamt-pdf" in rel.parts:
        return include_gesamt_pdf and path.name == f"{testakte_dir.name}_gesamt.pdf"
    if is_export_meta_file(path, testakte_dir):
        return False
    return True

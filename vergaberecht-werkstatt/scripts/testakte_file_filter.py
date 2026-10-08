#!/usr/bin/env python3
"""Gemeinsamer Filter fuer Testakten-Exportdateien.

Die Repo-README und redaktionelle Uebersichten sind fuer GitHub wichtig, sollen
aber nicht in die Akten-PDFs und den internen Quellenbestand gelangen. Der
Filter steuert die Sammlung fuer Einzel- und Gesamt-PDFs. Die flachen
Release-ZIPs kuratiert `build-testakten-release-zips.py` gesondert.
"""

from __future__ import annotations

from pathlib import Path

TEXT_EXTS = {".md", ".txt", ".csv", ".eml"}

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
)

INITIAL_OVERVIEW_PARTS = (
    "aktenuebersicht",
    "aktenübersicht",
    "akte-uebersicht",
    "akte-übersicht",
    "soforttriage",
)


def _safe_text(path: Path, limit: int = 80_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit].lower()
    except Exception:
        return ""


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


def is_export_meta_file(path: Path, testakte_dir: Path) -> bool:
    """True, wenn die Datei nicht in PDF/ZIP-Arbeitsmaterial gehoert."""
    name = path.name.lower()
    stem = path.stem.lower()
    if name == "readme.md":
        return True
    if any(part in stem for part in META_NAME_PARTS):
        return True
    if _is_initial_overview(path, testakte_dir):
        return True
    if path.suffix.lower() in TEXT_EXTS:
        text = _safe_text(path)
        if any(marker in text for marker in META_MARKERS):
            return True
    return False


def include_in_working_dump(
    path: Path,
    testakte_dir: Path,
    *,
    include_gesamt_pdf: bool = False,
    include_einzel_pdf: bool = False,
    include_markdown: bool = True,
) -> bool:
    """Export-Entscheidung fuer eine einzelne Datei innerhalb einer Testakte.

    include_markdown=False steht fuer Aufrufer zur Verfuegung, die nur
    Arbeitsformate sammeln. Das Release-ZIP verwendet einen eigenen strengeren
    Export: flach und ausschliesslich DOCX, XLSX sowie PDF.
    """
    if not path.is_file():
        return False
    if not include_markdown and path.suffix.lower() == ".md":
        return False
    try:
        rel = path.relative_to(testakte_dir)
    except ValueError:
        return False
    if any(part.startswith(".") for part in rel.parts):
        return False
    if "__pycache__" in rel.parts or path.name == ".DS_Store":
        return False
    if any(part.endswith(" 2") for part in rel.parts):
        return False
    if "gesamt-pdf" in rel.parts:
        return include_gesamt_pdf and path.name == f"{testakte_dir.name}_gesamt.pdf"
    if "einzel-pdf" in rel.parts:
        return include_einzel_pdf and path.suffix.lower() == ".pdf"
    if is_export_meta_file(path, testakte_dir):
        return False
    return True

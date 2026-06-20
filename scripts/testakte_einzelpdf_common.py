#!/usr/bin/env python3
"""Gemeinsame Definitionen fuer die Testakten-Einzel-PDF-ZIPs.

Die Einzel-PDF-ZIPs liefern jede Unterlage einer Testakte als eigene PDF-Datei
(im Gegensatz zum Gesamt-PDF, das alles in ein Dokument zusammenfasst). Builder
und Validator teilen sich hier dieselbe Auswahl- und Benennungslogik, damit die
erzeugten ZIPs und die Pruefung garantiert deckungsgleich sind.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from testakte_file_filter import include_in_working_dump

# Dokumente, die in eine eigene PDF gerendert werden.
RENDER_EXTS = {"md", "txt", "eml", "csv", "xlsx", "docx", "odt"}
# Bilder werden in eine PDF-Seite eingebettet.
IMAGE_EXTS = {"jpg", "jpeg", "png"}
# PDFs werden unveraendert uebernommen (Original-Layout bleibt erhalten).
COPY_EXTS = {"pdf"}

# Reine Konfigurations-/Metadaten-Formate sind keine "Unterlagen" und werden
# nicht in PDFs umgewandelt (z. B. rubric.yaml, *.json, *.ics).
DOCUMENT_EXTS = RENDER_EXTS | IMAGE_EXTS | COPY_EXTS


def ext_of(path: Path) -> str:
    return path.suffix.lower().lstrip(".")


def is_einzelpdf_document(path: Path, testakte_dir: Path) -> bool:
    """True, wenn die Datei als eigene PDF in das Einzel-PDF-ZIP gehoert."""
    if not include_in_working_dump(path, testakte_dir, include_gesamt_pdf=False):
        return False
    return ext_of(path) in DOCUMENT_EXTS


def iter_documents(testakte_dir: Path):
    for path in sorted(
        testakte_dir.rglob("*"),
        key=lambda p: str(p.relative_to(testakte_dir)).lower(),
    ):
        if is_einzelpdf_document(path, testakte_dir):
            yield path


def _clean_arcname(path: Path, testakte_dir: Path) -> str:
    rel = path.relative_to(testakte_dir)
    out_rel = rel if ext_of(path) == "pdf" else rel.with_suffix(".pdf")
    return (Path(testakte_dir.name) / out_rel).as_posix()


def _qualified_arcname(path: Path, testakte_dir: Path) -> str:
    """Behaelt die Originalendung im Namen, um Kollisionen aufzuloesen
    (z. B. ``vertrag.odt`` -> ``vertrag.odt.pdf`` neben ``vertrag.docx.pdf``)."""
    rel = path.relative_to(testakte_dir)
    out_rel = rel.with_name(rel.name + ".pdf")
    return (Path(testakte_dir.name) / out_rel).as_posix()


def document_arcname_pairs(testakte_dir: Path) -> list[tuple[Path, str]]:
    """Liefert (Quelldatei, ZIP-PDF-Pfad)-Paare mit kollisionsfreien Namen.

    Mehrere Dokumente mit gleichem Stamm (z. B. dasselbe Muster als .odt, .docx
    und .md) erhalten ihre Originalendung als Teil des PDF-Namens, damit im ZIP
    keine doppelten Eintraege entstehen. Original-PDFs behalten ihren Namen.
    """
    docs = list(iter_documents(testakte_dir))
    clean = {p: _clean_arcname(p, testakte_dir) for p in docs}
    collisions = {name for name, n in Counter(clean.values()).items() if n > 1}
    pairs: list[tuple[Path, str]] = []
    for p in docs:
        name = clean[p]
        if name in collisions and ext_of(p) != "pdf":
            name = _qualified_arcname(p, testakte_dir)
        pairs.append((p, name))
    return pairs


def expected_arcnames(testakte_dir: Path) -> list[str]:
    return [name for _, name in document_arcname_pairs(testakte_dir)]

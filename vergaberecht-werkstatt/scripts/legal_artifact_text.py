#!/usr/bin/env python3
"""Liest Rechtstext aus Office- und PDF-Artefakten ohne Pflichtpakete.

DOCX, XLSX und PPTX sind ZIP-basierte OOXML-Container. Fuer die
Rechtsstandsvalidatoren genuegt eine direkte, schnelle XML-Auswertung. PDF
wird bevorzugt mit ``pdftotext`` gelesen; wenn das Programm fehlt, wird
``pypdf`` nur bei Bedarf importiert.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import re
import shutil
import subprocess
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile


BINARY_LEGAL_SUFFIXES = {".docx", ".xlsx", ".pptx", ".pdf"}
DERIVED_ARTIFACT_DIRS = {"einzel-pdf", "gesamt-pdf", "scan-pdf"}
NON_PROJECT_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".cache", "dist"}
_NATURAL_NUMBER_RE = re.compile(r"(\d+)")


def binary_legal_files(root: Path, skip_parts: set[str]) -> list[Path]:
    """Findet primaere Rechtsartefakte, aber keine abgeleiteten PDF-Kopien."""
    excluded = skip_parts | DERIVED_ARTIFACT_DIRS | NON_PROJECT_DIRS
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in BINARY_LEGAL_SUFFIXES
        and not excluded.intersection(path.relative_to(root).parts)
    )


def _natural_key(value: str) -> list[str | int]:
    return [int(part) if part.isdigit() else part for part in _NATURAL_NUMBER_RE.split(value)]


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _xml_text(data: bytes, text_tags: set[str], break_tags: set[str] | None = None) -> str:
    """Extrahiert Text anhand lokaler XML-Namen und erhaelt grobe Grenzen."""
    break_tags = break_tags or set()
    root = ET.fromstring(data)
    chunks: list[str] = []
    for element in root.iter():
        name = _local_name(element.tag)
        if name in text_tags and element.text:
            chunks.append(element.text)
        elif name in break_tags:
            chunks.append("\n")
    return " ".join(part.strip() for part in chunks if part.strip())


def _docx_text(path: Path) -> str:
    prefixes = (
        "word/document.xml",
        "word/header",
        "word/footer",
        "word/footnotes.xml",
        "word/endnotes.xml",
        "word/comments.xml",
    )
    with ZipFile(path) as archive:
        names = [name for name in archive.namelist() if any(name.startswith(prefix) for prefix in prefixes)]
        names.sort(key=_natural_key)
        chunks = [
            _xml_text(archive.read(name), {"t", "instrText"}, {"p", "tr", "br", "tab"})
            for name in names
            if name.endswith(".xml")
        ]
    return "\n".join(chunk for chunk in chunks if chunk)


def _shared_strings(archive: ZipFile) -> list[str]:
    name = "xl/sharedStrings.xml"
    if name not in archive.namelist():
        return []
    root = ET.fromstring(archive.read(name))
    return [
        "".join(node.text or "" for node in item.iter() if _local_name(node.tag) == "t")
        for item in root
        if _local_name(item.tag) == "si"
    ]


def _xlsx_text(path: Path) -> str:
    with ZipFile(path) as archive:
        shared = _shared_strings(archive)
        sheets = sorted(
            (
                name
                for name in archive.namelist()
                if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name)
            ),
            key=_natural_key,
        )
        chunks: list[str] = []
        for name in sheets:
            root = ET.fromstring(archive.read(name))
            for cell in (node for node in root.iter() if _local_name(node.tag) == "c"):
                cell_type = cell.attrib.get("t", "")
                values = [node.text or "" for node in cell.iter() if _local_name(node.tag) == "v"]
                inline = [node.text or "" for node in cell.iter() if _local_name(node.tag) == "t"]
                formulas = [node.text or "" for node in cell.iter() if _local_name(node.tag) == "f"]
                if cell_type == "s" and values:
                    try:
                        chunks.append(shared[int(values[0])])
                    except (IndexError, ValueError):
                        chunks.append(values[0])
                else:
                    chunks.extend(inline or values)
                chunks.extend(f"={formula}" for formula in formulas if formula)
    return "\n".join(chunk for chunk in chunks if chunk)


def _pptx_text(path: Path) -> str:
    prefixes = ("ppt/slides/slide", "ppt/notesSlides/notesSlide")
    with ZipFile(path) as archive:
        names = sorted(
            (
                name
                for name in archive.namelist()
                if name.endswith(".xml") and any(name.startswith(prefix) for prefix in prefixes)
            ),
            key=_natural_key,
        )
        chunks = [_xml_text(archive.read(name), {"t"}, {"p", "br"}) for name in names]
    return "\n".join(chunk for chunk in chunks if chunk)


def _pdf_text(path: Path) -> str:
    executable = shutil.which("pdftotext")
    if executable:
        proc = subprocess.run(
            [executable, "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if proc.returncode == 0:
            return proc.stdout
        raise RuntimeError(f"pdftotext scheiterte fuer {path}: {proc.stderr.strip()}")

    try:
        from pypdf import PdfReader
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "PDF-Pruefung braucht entweder das Programm 'pdftotext' oder das optionale Paket 'pypdf'."
        ) from exc
    return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)


@lru_cache(maxsize=256)
def _read_cached(path_value: str, size: int, mtime_ns: int) -> str:
    del size, mtime_ns  # Teil des Cache-Schluessels; der Dateipfad allein waere nicht sicher.
    path = Path(path_value)
    suffix = path.suffix.lower()
    try:
        if suffix == ".docx":
            text = _docx_text(path)
        elif suffix == ".xlsx":
            text = _xlsx_text(path)
        elif suffix == ".pptx":
            text = _pptx_text(path)
        elif suffix == ".pdf":
            text = _pdf_text(path)
        else:
            raise ValueError(f"Nicht unterstuetztes Rechtsartefakt: {path}")
    except (BadZipFile, ET.ParseError) as exc:
        raise RuntimeError(f"Beschaedigtes oder unlesbares Rechtsartefakt: {path}") from exc
    if not text.strip():
        raise RuntimeError(f"Rechtsartefakt enthaelt keinen auslesbaren Text: {path}")
    return text


def read_binary_legal_text(path: Path) -> str:
    """Liest Text und verwirft den Cache automatisch nach Dateiaenderungen."""
    resolved = path.resolve()
    stat = resolved.stat()
    return _read_cached(str(resolved), stat.st_size, stat.st_mtime_ns)

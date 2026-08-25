#!/usr/bin/env python3
"""Validiert die Release-Artefakte fuer pluginlokale testakte-Ordner."""

from __future__ import annotations

import io
import json
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader

from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_notice_errors
from testakte_einzelpdf_common import expected_arcnames
from testakte_zip_common import working_dump_expected_arcnames, working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
A4_WIDTH = 595.2755905511812
A4_HEIGHT = 841.8897637795277


def fail(message: str) -> None:
    print(f"validate-plugin-testakte-assets failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def check_pdf(path: Path) -> None:
    if not path.is_file():
        fail(f"{path.relative_to(REPO)} fehlt")
    data = path.read_bytes()
    if len(data) < 1024 or not data.startswith(b"%PDF") or b"%%EOF" not in data[-4096:]:
        fail(f"{path.relative_to(REPO)} ist kein plausibles PDF")
    for problem in pdf_notice_errors(data, exactly_once=True):
        fail(f"{path.relative_to(REPO)}: {problem}")


def check_zip(
    path: Path,
    *,
    expected: list[str] | None = None,
    suffix: str | None = None,
    require_notice: bool = False,
) -> list[str]:
    if not path.is_file() or path.stat().st_size <= 0:
        fail(f"{path}: ZIP fehlt oder ist leer")
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                fail(f"{path}: defekter ZIP-Eintrag {bad}")
            names = [n.replace("\\", "/") for n in archive.namelist() if not n.endswith("/")]
            if not names:
                fail(f"{path}: ZIP ohne Dateien")
            for name in names:
                if "/" in name:
                    fail(f"{path}: Unterordner im ZIP: {name}")
                if name.lower().endswith(".md"):
                    fail(f"{path}: Markdown-Datei im Akten-ZIP: {name}")
                if suffix and not name.lower().endswith(suffix):
                    fail(f"{path}: unerwarteter Dateityp: {name}")
                if suffix == ".pdf":
                    data = archive.read(name)
                    try:
                        pages = list(PdfReader(io.BytesIO(data)).pages)
                    except Exception as exc:
                        fail(f"{path}: PDF nicht lesbar {name}: {exc}")
                    if not pages:
                        fail(f"{path}: PDF ohne Seite: {name}")
                    for problem in pdf_notice_errors(data, exactly_once=True):
                        fail(f"{path}: {name}: {problem}")
                    for page_number, page in enumerate(pages, start=1):
                        width = float(page.mediabox.width)
                        height = float(page.mediabox.height)
                        portrait = abs(width - A4_WIDTH) < 1 and abs(height - A4_HEIGHT) < 1
                        landscape = abs(width - A4_HEIGHT) < 1 and abs(height - A4_WIDTH) < 1
                        if not (portrait or landscape):
                            fail(
                                f"{path}: {name}, Seite {page_number} ist nicht A4 "
                                f"({width:.1f} x {height:.1f} pt)"
                            )
            if require_notice:
                notice_names = [name for name in names if name.casefold() == NOTICE_FILENAME.casefold()]
                if notice_names != [NOTICE_FILENAME]:
                    fail(f"{path}: {NOTICE_FILENAME} fehlt oder ist nicht eindeutig")
                if names[0] != NOTICE_FILENAME:
                    fail(f"{path}: {NOTICE_FILENAME} muss der erste ZIP-Eintrag sein")
                for problem in notice_text_errors(archive.read(NOTICE_FILENAME)):
                    fail(f"{path}: {problem}")
            if len({name.casefold() for name in names}) != len(names):
                fail(f"{path}: kollidierende Dateinamen")
            if expected is not None and sorted(names) != sorted(expected):
                fail(f"{path}: Inhalt weicht vom Aktenbestand ab")
            return names
    except zipfile.BadZipFile as exc:
        fail(f"{path}: kein gueltiges ZIP: {exc}")


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "dist"
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    checked_gesamt_pdfs: set[Path] = set()
    for path in sorted(REPO.rglob("*.pdf"), key=lambda item: str(item).lower()):
        try:
            rel = path.relative_to(REPO)
        except ValueError:
            continue
        if "testakten" in rel.parts or "testakte" not in rel.parts or "gesamt-pdf" not in rel.parts:
            continue
        check_pdf(path)
        checked_gesamt_pdfs.add(path.resolve())
    count = 0
    source_archives: list[str] = []
    pdf_archives: list[str] = []
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        testakte = directory / "testakte"
        if not testakte.is_dir():
            continue
        source_pairs = working_dump_flat_pairs(testakte, include_gesamt_pdf=False)
        pdf_expected = expected_arcnames(testakte)
        if not source_pairs and not pdf_expected:
            stale = [
                dist / f"{name}-testakte.zip",
                dist / f"{name}-testakte-einzelpdfs.zip",
            ]
            if any(path.exists() for path in stale):
                fail(f"{name}: veraltetes Release-Asset fuer nicht exportfaehige Dokumentation")
            continue
        if not source_pairs or not pdf_expected:
            fail(f"{name}: Quell- und Einzel-PDF-Auswahl sind inkonsistent")
        count += 1
        gesamt_pdf = testakte / "gesamt-pdf" / "testakte_gesamt.pdf"
        if gesamt_pdf.resolve() not in checked_gesamt_pdfs:
            check_pdf(gesamt_pdf)
        source_name = f"{name}-testakte.zip"
        pdf_name = f"{name}-testakte-einzelpdfs.zip"
        source_expected = working_dump_expected_arcnames(
            testakte,
            include_gesamt_pdf=True,
        )
        check_zip(
            dist / source_name,
            expected=source_expected,
            require_notice=True,
        )
        check_zip(
            dist / pdf_name,
            expected=pdf_expected,
            suffix=".pdf",
        )
        source_archives.append(source_name)
        pdf_archives.append(pdf_name)
    check_zip(
        dist / "alle-pluginlokalen-testakten.zip",
        expected=source_archives,
        suffix=".zip",
    )
    check_zip(
        dist / "alle-pluginlokalen-testakten-einzelpdfs.zip",
        expected=pdf_archives,
        suffix=".zip",
    )
    print(f"validate-plugin-testakte-assets OK ({count} pluginlokale Testakten)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

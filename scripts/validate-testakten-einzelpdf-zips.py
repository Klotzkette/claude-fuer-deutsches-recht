#!/usr/bin/env python3
"""Validiert die Einzel-PDF-ZIPs der Testakten vor dem Release.

Spiegelt die Auswahl- und Benennungslogik des Builders (testakte_einzelpdf_common)
und prueft fuer jede Testakte mit renderbaren Unterlagen, dass das ZIP existiert,
intakt ist und genau die erwarteten PDF-Eintraege enthaelt. Zusaetzlich wird das
Sammel-ZIP geprueft. Nach dem Dist-Verzeichnis koennen optional konkrete
Testakten-Namen angegeben werden; dann wird ein gezielter Teilbestand geprueft.
"""

from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader

from testakte_einzelpdf_common import expected_arcnames
from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_content_errors

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
A4_WIDTH = 595.2755905511812
A4_HEIGHT = 841.8897637795277


def fail(message: str) -> None:
    print(f"validate-testakten-einzelpdf-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def zip_entries(zip_path: Path, *, expected_suffix: str) -> list[str]:
    if not zip_path.exists():
        fail(f"{zip_path}: missing ZIP")
    if zip_path.stat().st_size <= 0:
        fail(f"{zip_path}: empty ZIP")
    try:
        with zipfile.ZipFile(zip_path) as archive:
            if any(info.is_dir() for info in archive.infolist()):
                fail(f"{zip_path}: Verzeichniseintrag im ZIP")
            if archive.testzip() is not None:
                fail(f"{zip_path}: beschädigter ZIP-Eintrag")
            names = [n.replace("\\", "/") for n in archive.namelist() if not n.endswith("/")]
            if not names or names[0] != NOTICE_FILENAME:
                fail(f"{zip_path}: {NOTICE_FILENAME} muss der erste ZIP-Eintrag sein")
            for problem in notice_text_errors(archive.read(NOTICE_FILENAME)):
                fail(f"{zip_path}: {problem}")
            for n in names:
                if "/" in n:
                    fail(f"{zip_path}: Unterordner im ZIP: {n}")
                if n != NOTICE_FILENAME and not n.lower().endswith(expected_suffix):
                    fail(f"{zip_path}: unerwarteter Dateityp {n}")
                parts = Path(n).parts
                if Path(n).is_absolute() or ".." in parts:
                    fail(f"{zip_path}: unsafe member path {n}")
            for info in archive.infolist():
                if info.filename.endswith("/"):
                    continue
                if info.file_size <= 0:
                    fail(f"{zip_path}: empty member {info.filename}")
                if info.flag_bits & 0x1:
                    fail(f"{zip_path}: encrypted member {info.filename}")
                if expected_suffix == ".pdf" and info.filename != NOTICE_FILENAME:
                    data = archive.read(info)
                    if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-2048:]:
                        fail(f"{zip_path}: member is not a complete PDF: {info.filename}")
                    try:
                        reader = PdfReader(io.BytesIO(data))
                        pages = list(reader.pages)
                    except Exception as exc:
                        fail(f"{zip_path}: PDF nicht lesbar {info.filename}: {exc}")
                    if not pages:
                        fail(f"{zip_path}: PDF ohne Seite: {info.filename}")
                    for notice_problem in pdf_content_errors(data):
                        fail(f"{zip_path}: {info.filename}: {notice_problem}")
                    for page_number, page in enumerate(pages, start=1):
                        width = float(page.mediabox.width)
                        height = float(page.mediabox.height)
                        is_portrait = (
                            abs(width - A4_WIDTH) < 1 and abs(height - A4_HEIGHT) < 1
                        )
                        is_landscape = (
                            abs(width - A4_HEIGHT) < 1 and abs(height - A4_WIDTH) < 1
                        )
                        if not (is_portrait or is_landscape):
                            fail(
                                f"{zip_path}: {info.filename}, Seite {page_number} "
                                f"ist nicht A4 ({width:.1f} x {height:.1f} pt)"
                            )
            if len({name.casefold() for name in names}) != len(names):
                fail(f"{zip_path}: Dateinamen kollidieren ohne Beachtung der Grossschreibung")
            return sorted(names)
    except zipfile.BadZipFile as exc:
        fail(f"{zip_path}: invalid ZIP: {exc}")


def assert_same(label: str, expected: list[str], actual: list[str]) -> None:
    expected_set, actual_set = set(expected), set(actual)
    missing = sorted(expected_set - actual_set)
    extra = sorted(actual_set - expected_set)
    if missing or extra:
        details = []
        if missing:
            details.append(f"missing={missing[:10]}")
        if extra:
            details.append(f"extra={extra[:10]}")
        fail(f"{label}: entry mismatch ({'; '.join(details)})")
    if len(actual) != len(actual_set):
        fail(f"{label}: duplicate ZIP entries detected")


def main() -> None:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "dist"
    targets = set(sys.argv[2:])
    all_dirs = sorted((d for d in TESTAKTEN.iterdir() if d.is_dir()), key=lambda p: p.name)
    dirs = all_dirs
    if targets:
        missing_targets = sorted(targets - {d.name for d in dirs})
        if missing_targets:
            fail(f"unknown testakten: {missing_targets}")
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        fail("no testakten directories found")

    combined_expected = [
        f"testakte-{d.name}-einzelpdfs.zip"
        for d in all_dirs
        if expected_arcnames(d)
    ]
    zip_count = 0
    total_pdfs = 0

    for testakte_dir in dirs:
        expected = expected_arcnames(testakte_dir)
        if not expected:
            # Ordner ohne renderbare Unterlagen bekommen bewusst kein ZIP.
            if (dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip").exists():
                fail(f"{testakte_dir.name}: unexpected einzelpdf ZIP for empty akte")
            continue
        actual = zip_entries(
            dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip",
            expected_suffix=".pdf",
        )
        assert_same(f"testakte-{testakte_dir.name}-einzelpdfs.zip", [NOTICE_FILENAME, *expected], actual)
        zip_count += 1
        total_pdfs += len(expected)

    combined_actual = zip_entries(
        dist / "alle-testakten-einzelpdfs.zip",
        expected_suffix=".zip",
    )
    assert_same("alle-testakten-einzelpdfs.zip", [NOTICE_FILENAME, *combined_expected], combined_actual)

    print(
        "validate-testakten-einzelpdf-zips OK "
        f"({zip_count} Einzel-PDF-ZIPs, {total_pdfs} PDFs)"
    )


if __name__ == "__main__":
    main()

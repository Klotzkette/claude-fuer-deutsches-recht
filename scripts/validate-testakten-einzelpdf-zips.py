#!/usr/bin/env python3
"""Validiert die Einzel-PDF-ZIPs der Testakten vor dem Release.

Spiegelt die Auswahl- und Benennungslogik des Builders (testakte_einzelpdf_common)
und prueft fuer jede Testakte mit renderbaren Unterlagen, dass das ZIP existiert,
intakt ist und genau die erwarteten PDF-Eintraege enthaelt. Zusaetzlich wird das
Sammel-ZIP geprueft.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from testakte_einzelpdf_common import expected_arcnames

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"


def fail(message: str) -> None:
    print(f"validate-testakten-einzelpdf-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def zip_entries(zip_path: Path) -> list[str]:
    if not zip_path.exists():
        fail(f"{zip_path}: missing ZIP")
    if zip_path.stat().st_size <= 0:
        fail(f"{zip_path}: empty ZIP")
    try:
        with zipfile.ZipFile(zip_path) as archive:
            bad = archive.testzip()
            if bad is not None:
                fail(f"{zip_path}: corrupt member {bad}")
            names = [n.replace("\\", "/") for n in archive.namelist() if not n.endswith("/")]
            for n in names:
                if not n.lower().endswith(".pdf"):
                    fail(f"{zip_path}: non-PDF entry {n}")
            for info in archive.infolist():
                if not info.filename.endswith("/") and info.file_size <= 0:
                    fail(f"{zip_path}: empty member {info.filename}")
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
    dirs = sorted((d for d in TESTAKTEN.iterdir() if d.is_dir()), key=lambda p: p.name)
    if not dirs:
        fail("no testakten directories found")

    combined_expected: list[str] = []
    zip_count = 0
    total_pdfs = 0

    for testakte_dir in dirs:
        expected = expected_arcnames(testakte_dir)
        if not expected:
            # Ordner ohne renderbare Unterlagen bekommen bewusst kein ZIP.
            if (dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip").exists():
                fail(f"{testakte_dir.name}: unexpected einzelpdf ZIP for empty akte")
            continue
        actual = zip_entries(dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip")
        assert_same(f"testakte-{testakte_dir.name}-einzelpdfs.zip", expected, actual)
        combined_expected.extend(expected)
        zip_count += 1
        total_pdfs += len(expected)

    combined_actual = zip_entries(dist / "alle-testakten-einzelpdfs.zip")
    assert_same("alle-testakten-einzelpdfs.zip", combined_expected, combined_actual)

    print(
        "validate-testakten-einzelpdf-zips OK "
        f"({zip_count} Einzel-PDF-ZIPs, {total_pdfs} PDFs)"
    )


if __name__ == "__main__":
    main()

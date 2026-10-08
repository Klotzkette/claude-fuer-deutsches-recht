#!/usr/bin/env python3
"""Validiert flache Testakten-ZIPs aus Word, Excel und PDF.

Jeder Dateiname liegt auf der ZIP-Oberflaeche. Markdown, Verzeichnisse und
andere Dateitypen sind releaseblockierend. Das Gesamt-ZIP verwendet den
Testakten-Slug als Dateipraefix, bleibt aber ebenfalls vollstaendig flach.
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

from testakte_notices import README_NOTICE, is_internal_file

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}
ALLOWED_SUFFIXES = {".docx", ".xlsx", ".pdf"}


def fail(message: str) -> None:
    print(f"validate-testakten-release-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def expected_entries(testakte_dir: Path, *, combined: bool = False) -> list[str]:
    entries: list[str] = []
    for dirname, suffix in (("docx", ".docx"), ("xlsx", ".xlsx"), ("einzel-pdf", ".pdf")):
        directory = testakte_dir / dirname
        if directory.is_dir():
            entries.extend(path.name for path in directory.glob(f"*{suffix}") if path.is_file() and not is_internal_file(path.name))
    for dirname, prefix in (("scan-pdf", "Scan__"), ("pdfs", "Original__")):
        directory = testakte_dir / dirname
        if directory.is_dir():
            entries.extend(f"{prefix}{path.name}" for path in directory.glob("*.pdf") if path.is_file() and not is_internal_file(path.name))
    if combined:
        entries = [f"{testakte_dir.name}__{name}" for name in entries]
    entries.sort(key=lambda name: (Path(name).suffix.lower(), name.casefold(), name))
    if not entries:
        fail(f"{testakte_dir}: keine exportfähige Word-, Excel- oder PDF-Datei")
    return entries


def zip_entries(zip_path: Path) -> list[str]:
    if not zip_path.exists():
        fail(f"{zip_path}: missing ZIP")
    if zip_path.stat().st_size <= 0:
        fail(f"{zip_path}: empty ZIP")
    try:
        with zipfile.ZipFile(zip_path) as archive:
            if "README.txt" not in archive.namelist():
                fail(f"{zip_path}: README.txt fehlt")
            if archive.namelist()[0] != "README.txt":
                fail(f"{zip_path}: README.txt muss der erste Eintrag sein")
            if any(name.endswith("_gesamt.pdf") or name.endswith("00_Gesamtakte.pdf") for name in archive.namelist()):
                fail(f"{zip_path}: Gesamt-PDF muss separat ausgeliefert werden")
            if not archive.read("README.txt").decode("utf-8").startswith(README_NOTICE):
                fail(f"{zip_path}: Pflichtwarnhinweis fehlt")
            if any(name.endswith("/") for name in archive.namelist()):
                fail(f"{zip_path}: Verzeichniseintrag unzulaessig")
            bad = archive.testzip()
            if bad is not None:
                fail(f"{zip_path}: corrupt member {bad}")
            return sorted(name.replace("\\", "/") for name in archive.namelist() if not name.endswith("/"))
    except zipfile.BadZipFile as exc:
        fail(f"{zip_path}: invalid ZIP: {exc}")


def assert_same(label: str, expected: list[str], actual: list[str]) -> None:
    expected_set = set(expected)
    actual_set = set(actual)
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
    folded = [name.casefold() for name in actual]
    if len(folded) != len(set(folded)):
        fail(f"{label}: case-insensitive duplicate ZIP entries detected")
    nested = [name for name in actual if "/" in name or "\\" in name]
    if nested:
        fail(f"{label}: Unterordner sind unzulässig: {nested[:10]}")
    wrong = [
        name for name in actual
        if name != "README.txt" and (
            Path(name).suffix.lower() not in ALLOWED_SUFFIXES or is_internal_file(name)
        )
    ]
    if wrong:
        fail(f"{label}: nur DOCX, XLSX und PDF zulässig: {wrong[:10]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist_dir", nargs="?", type=Path, default=REPO_ROOT / "dist")
    args = parser.parse_args()
    dist = args.dist_dir.resolve()
    dirs = sorted(
        (d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS),
        key=lambda p: p.name,
    )
    if not dirs:
        fail("no testakten directories found")

    combined_expected: list[str] = []
    empty_dirs: list[str] = []
    gesamt_pdf_count = 0

    for testakte_dir in dirs:
        entries = expected_entries(testakte_dir)
        if not entries:
            empty_dirs.append(testakte_dir.name)
            continue
        actual = zip_entries(dist / f"testakte-{testakte_dir.name}.zip")
        assert_same(f"testakte-{testakte_dir.name}.zip", entries + ["README.txt"], actual)
        pdf_entries = [
            name for name in entries
            if name.endswith(".pdf") and name != "00_Gesamtakte.pdf"
        ]
        pdf_zip = dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip"
        assert_same(pdf_zip.name, pdf_entries + ["README.txt"], zip_entries(pdf_zip))
        overall_name = f"{testakte_dir.name}_gesamt.pdf"
        overall_asset = dist / overall_name
        if not overall_asset.is_file() or overall_asset.read_bytes() != (testakte_dir / "gesamt-pdf" / overall_name).read_bytes():
            fail(f"{overall_asset}: Gesamt-PDF fehlt oder weicht von der Quelle ab")
        gesamt_pdf_count += 1
        suffixes = {Path(name).suffix.lower() for name in actual}
        missing_formats = sorted(ALLOWED_SUFFIXES - suffixes)
        if missing_formats:
            fail(f"testakte-{testakte_dir.name}.zip: Dateitypen fehlen: {missing_formats}")

    if empty_dirs:
        fail(f"testakten without exportable files: {empty_dirs[:20]}")

    combined_expected = [
        name
        for testakte_dir in dirs
        for name in expected_entries(testakte_dir, combined=True)
    ]
    combined_actual = zip_entries(dist / "testakten-vergaberecht-werkstatt.zip")
    assert_same("testakten-vergaberecht-werkstatt.zip", combined_expected + ["README.txt"], combined_actual)

    print(
        "validate-testakten-release-zips OK "
        f"({len(dirs)} testakte ZIPs, {len(combined_expected)} files, {gesamt_pdf_count} Gesamt-PDFs)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

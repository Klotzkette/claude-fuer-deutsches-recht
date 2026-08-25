#!/usr/bin/env python3
"""Validate release ZIPs for testakten before publishing.

The release builder strips Markdown/download/meta files from testakten ZIPs
and adds the mandatory bilingual README.txt. This validator mirrors that
contract and verifies the individual and combined archives. After the dist
directory, optional testakte names limit validation to a targeted build.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors
from testakte_zip_common import working_dump_expected_arcnames

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {
    "megaprompts",
}


def fail(message: str) -> None:
    print(f"validate-testakten-release-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def expected_entries(testakte_dir: Path) -> list[str]:
    return working_dump_expected_arcnames(testakte_dir, include_gesamt_pdf=True)


def zip_entries(zip_path: Path, *, require_notice: bool) -> list[str]:
    if not zip_path.exists():
        fail(f"{zip_path}: missing ZIP")
    if zip_path.stat().st_size <= 0:
        fail(f"{zip_path}: empty ZIP")
    try:
        with zipfile.ZipFile(zip_path) as archive:
            bad = archive.testzip()
            if bad is not None:
                fail(f"{zip_path}: corrupt member {bad}")
            names = [name.replace("\\", "/") for name in archive.namelist() if not name.endswith("/")]
            for name in names:
                if "/" in name:
                    fail(f"{zip_path}: Unterordner im ZIP: {name}")
                if name.lower().endswith(".md"):
                    fail(f"{zip_path}: Markdown-Datei im Akten-ZIP: {name}")
            if require_notice:
                notice_names = [name for name in names if name.casefold() == NOTICE_FILENAME.casefold()]
                if notice_names != [NOTICE_FILENAME]:
                    fail(f"{zip_path}: {NOTICE_FILENAME} fehlt oder ist nicht eindeutig")
                if names[0] != NOTICE_FILENAME:
                    fail(f"{zip_path}: {NOTICE_FILENAME} muss der erste ZIP-Eintrag sein")
                for problem in notice_text_errors(archive.read(NOTICE_FILENAME)):
                    fail(f"{zip_path}: {problem}")
            if len({name.casefold() for name in names}) != len(names):
                fail(f"{zip_path}: Dateinamen kollidieren ohne Beachtung der Grossschreibung")
            return sorted(names)
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


def main() -> None:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "dist"
    targets = set(sys.argv[2:])
    all_dirs = sorted(
        (d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS),
        key=lambda p: p.name,
    )
    dirs = all_dirs
    if targets:
        missing_targets = sorted(targets - {d.name for d in dirs})
        if missing_targets:
            fail(f"unknown testakten: {missing_targets}")
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        fail("no testakten directories found")

    empty_dirs: list[str] = []
    gesamt_pdf_count = 0
    individual_archives = [
        f"testakte-{d.name}.zip"
        for d in all_dirs
        if expected_entries(d)
    ]

    for testakte_dir in dirs:
        entries = expected_entries(testakte_dir)
        if not entries:
            empty_dirs.append(testakte_dir.name)
            continue
        if f"{testakte_dir.name}_gesamt.pdf" in entries:
            gesamt_pdf_count += 1
        actual = zip_entries(
            dist / f"testakte-{testakte_dir.name}.zip",
            require_notice=True,
        )
        assert_same(f"testakte-{testakte_dir.name}.zip", entries, actual)
    if empty_dirs:
        fail(f"testakten without exportable files: {empty_dirs[:20]}")

    combined_actual = zip_entries(dist / "alle-testakten.zip", require_notice=False)
    assert_same("alle-testakten.zip", individual_archives, combined_actual)
    if any(not name.lower().endswith(".zip") for name in combined_actual):
        fail("alle-testakten.zip: enthaelt andere Dateien als Einzel-ZIPs")

    print(
        "validate-testakten-release-zips OK "
        f"({len(dirs)} flache Testakten-ZIPs, {sum(len(expected_entries(d)) for d in dirs)} Dateien, "
        f"{gesamt_pdf_count} Gesamt-PDFs)"
    )


if __name__ == "__main__":
    main()

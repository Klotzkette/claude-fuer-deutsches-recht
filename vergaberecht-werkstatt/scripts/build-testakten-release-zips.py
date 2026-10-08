#!/usr/bin/env python3
"""Baut flache Testakten-ZIPs fuer Releases.

Jedes ZIP enthaelt Word-, Excel- und PDF-Dateien sowie README.txt auf seiner
obersten Ebene. Markdown und technische Quellformate bleiben im Repository;
ihre lesbaren Einzel-PDFs liegen im Release-Paket. Das Gesamt-ZIP bleibt
ebenfalls flach und praefigiert Dateinamen mit dem Testakten-Slug.

Eine Testakte ohne mindestens eine echte Arbeitsdatei bricht den Build ab.
Damit kann kein scheinbar erfolgreiches, aber nur aus einer README bestehendes
Akten-ZIP entstehen.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from reproducible_zip import write_archive
from testakte_notices import README_NOTICE, is_internal_file
REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}


ALLOWED_SUFFIXES = {".docx", ".xlsx", ".pdf"}


def iter_export_files(testakte_dir: Path):
    """Liefert genau die kuratierten Lebenslage-Dateien fuer ein flaches ZIP."""
    files = []
    for dirname, suffix in (("docx", ".docx"), ("xlsx", ".xlsx"), ("einzel-pdf", ".pdf")):
        directory = testakte_dir / dirname
        if directory.is_dir():
            files.extend(path for path in directory.glob(f"*{suffix}") if path.is_file())
    for dirname in ("scan-pdf", "pdfs"):
        directory = testakte_dir / dirname
        if directory.is_dir():
            files.extend(path for path in directory.glob("*.pdf") if path.is_file())
    files = [path for path in files if not is_internal_file(path.name)]
    files.sort(key=lambda path: (path.suffix.lower(), path.name.casefold(), path.name))
    if not files:
        raise RuntimeError(f"{testakte_dir}: keine exportfähige Word-, Excel- oder PDF-Datei")
    yield from files


def flat_archive_name(path: Path, *, gesamt: bool = False) -> str:
    if gesamt:
        return "00_Gesamtakte.pdf"
    if path.parent.name == "scan-pdf":
        return f"Scan__{path.name}"
    if path.parent.name == "pdfs":
        return f"Original__{path.name}"
    return path.name


def testakte_members(testakte_dir: Path, *, combined: bool = False) -> list[tuple[Path, str]]:
    members: list[tuple[Path, str]] = []
    seen: set[str] = set()
    for path in iter_export_files(testakte_dir):
        is_gesamt = path.parent.name == "gesamt-pdf"
        filename = flat_archive_name(path, gesamt=is_gesamt)
        if combined:
            filename = f"{testakte_dir.name}__{filename}"
        folded = filename.casefold()
        if folded in seen:
            raise RuntimeError(f"{testakte_dir}: doppelter flacher ZIP-Name: {filename}")
        if Path(filename).suffix.lower() not in ALLOWED_SUFFIXES:
            raise RuntimeError(f"{testakte_dir}: unzulässiges Release-Format: {filename}")
        seen.add(folded)
        members.append((path, filename))
    return members


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}.zip"
    count = write_archive(out, testakte_members(testakte_dir) + [warning_member()])
    return out, count


def warning_member() -> tuple[Path, str]:
    readme = TESTAKTEN / "README.txt"
    if not readme.read_text(encoding="utf-8").startswith(README_NOTICE):
        raise ValueError("testakten/README.txt: Pflichtwarnhinweis fehlt")
    return readme, "README.txt"


def build_individual_pdfs(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    members = [
        member for member in testakte_members(testakte_dir)
        if member[0].suffix.lower() == ".pdf" and member[1] != "00_Gesamtakte.pdf"
    ]
    if not members:
        raise RuntimeError(f"{testakte_dir}: keine Einzel-PDFs vorhanden")
    output = dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip"
    count = write_archive(output, members + [warning_member()])
    return output, count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", type=Path, default=REPO_ROOT / "dist")
    args = parser.parse_args()
    dist = args.output_dir.resolve()
    dist.mkdir(parents=True, exist_ok=True)
    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    if not dirs:
        parser.error("keine Testakten gefunden")

    total_files = 0
    for d in dirs:
        out, count = build_single(d, dist)
        if count == 0:
            raise SystemExit(f"{d}: keine exportfaehigen Dateien")
        total_files += count
        print(f"Baue {out.name}: {count} Dateien")
        pdf_zip, pdf_count = build_individual_pdfs(d, dist)
        print(f"Baue {pdf_zip.name}: {pdf_count} Dateien")
        gesamt = d / "gesamt-pdf" / f"{d.name}_gesamt.pdf"
        if not gesamt.is_file():
            raise RuntimeError(f"{d}: Gesamt-PDF fehlt")
        shutil.copyfile(gesamt, dist / gesamt.name)

    all_out = dist / "testakten-vergaberecht-werkstatt.zip"
    all_members = [member for d in dirs for member in testakte_members(d, combined=True)]
    all_count = write_archive(all_out, all_members + [warning_member()])
    print(f"Baue {all_out.name}: {all_count} Dateien aus {len(dirs)} Testakten")
    print(f"Fertig: {len(dirs)} Einzel-ZIPs, {total_files} Dateien")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

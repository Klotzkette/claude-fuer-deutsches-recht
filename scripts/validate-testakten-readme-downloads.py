#!/usr/bin/env python3
"""Prüft die Downloadhinweise der zentralen Testakten.

Jede nutzerseitige Akte unter testakten/<slug>/ braucht im README den
autogenerierten Downloadblock mit Gesamt-PDF, Akten-ZIP und Einzel-PDF-ZIP.
Zusätzlich muss die zentrale testakten/README.md dieselben drei Ziele je Akte
aufführen. Der Check läuft ohne externe Abhängigkeiten und eignet sich damit
als frühes Release-Gate. Auf Root-, Index-, Akten- und Plugin-Seiten muss der
unveränderte DE/EN-Warnhinweis unmittelbar vor jeder Downloadgruppe stehen.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from testakte_download_notices import (
    download_group_starts,
    download_readmes,
    is_case_readme,
    missing_notice_positions,
)

ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = ROOT / "testakten"
OVERVIEW = TESTAKTEN / "README.md"
REPO_SLUG = "Klotzkette/" + "cla" + "ude-fuer-deutsches-recht"

BEGIN_MARKER = "<!-- BEGIN gesamt-pdf-section (autogen) -->"
END_MARKER = "<!-- END gesamt-pdf-section (autogen) -->"

# Hilfsmaterial-Ordner ohne vollständige Aktenstruktur.
SKIP_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}

EXPECTED_LABELS = (
    "Gesamt-PDF",
    "Akten-ZIP",
    "Einzel-PDF-ZIP",
)
TREE_FILE_PATTERN = re.compile(
    r"^[\s│]*(?:├──|└──)\s+"
    r"(?P<path>.+?\.(?:csv|docx|eml|ics|jpeg|jpg|json|odt|pdf|png|rtf|"
    r"tsv|txt|xlsm|xlsx|xml))"
    r"(?=\s{2,}|\s+(?:#|<-|←|—)|$)",
    re.IGNORECASE,
)
TABLE_FILE_PATTERN = re.compile(
    r"^\s*\|\s*`"
    r"(?P<path>[^`]+?\.(?:csv|docx|eml|ics|jpeg|jpg|json|odt|pdf|png|rtf|"
    r"tsv|txt|xlsm|xlsx|xml))"
    r"`\s*\|",
    re.IGNORECASE,
)


def fs_path(path: Path) -> Path:
    """Return a Windows long-path-safe Path without changing display paths."""
    if sys.platform != "win32":
        return path
    resolved = str(path.resolve())
    if resolved.startswith("\\\\?\\"):
        return Path(resolved)
    if resolved.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + resolved[2:])
    return Path("\\\\?\\" + resolved)


def path_exists(path: Path) -> bool:
    return fs_path(path).exists()


def read_text(path: Path) -> str:
    return fs_path(path).read_text(encoding="utf-8", errors="replace")


def release_url(slug: str, suffix: str = "") -> str:
    return (
        f"https://github.com/{REPO_SLUG}/"
        f"releases/latest/download/testakte-{slug}{suffix}.zip"
    )


def expected_targets(slug: str) -> tuple[str, str, str]:
    return (
        f"gesamt-pdf/{slug}_gesamt.pdf",
        release_url(slug),
        release_url(slug, "-einzelpdfs"),
    )


def validate_file_reference(
    slug: str,
    directory: Path,
    raw_path: str,
    line_number: int,
    errors: list[str],
) -> None:
    """Prüft einen relativen README-Dateieintrag gegen den Aktenbestand."""
    reference = Path(raw_path)
    if reference.is_absolute() or ".." in reference.parts:
        errors.append(
            f"{slug}: README-Zeile {line_number} enthält unsicheren Pfad {raw_path}"
        )
        return
    if any(char in raw_path for char in "*?["):
        found = any(path.is_file() for path in directory.glob(raw_path))
    elif len(reference.parts) > 1:
        found = path_exists(directory / reference)
    else:
        found = any(
            path.is_file() and path.name == reference.name
            for path in directory.rglob(reference.name)
        )
    if not found:
        errors.append(
            f"{slug}: README-Zeile {line_number} nennt fehlende Datei {raw_path}"
        )


def validate_readme_file_references(
    slug: str,
    directory: Path,
    text: str,
    errors: list[str],
) -> None:
    """Prüft Dateieinträge in README-Baumansichten und Dateitabellen."""
    for line_number, line in enumerate(text.splitlines(), start=1):
        matches = [
            match
            for pattern in (TREE_FILE_PATTERN, TABLE_FILE_PATTERN)
            if (match := pattern.match(line))
        ]
        if not matches:
            continue
        validate_file_reference(
            slug,
            directory,
            matches[0].group("path").strip(),
            line_number,
            errors,
        )


def validate_local_readme(slug: str, directory: Path, errors: list[str]) -> int:
    readme = directory / "README.md"
    if not path_exists(readme):
        errors.append(f"{slug}: README.md fehlt")
        return 0

    text = read_text(readme)
    validate_download_notices(slug, text, errors, case_readme=True)
    validate_readme_file_references(slug, directory, text, errors)
    begin_count = text.count(BEGIN_MARKER)
    end_count = text.count(END_MARKER)
    if begin_count != 1 or end_count != 1:
        errors.append(
            f"{slug}: Downloadblock-Marker unklar "
            f"({BEGIN_MARKER}: {begin_count}, {END_MARKER}: {end_count})"
        )
        block = text
    else:
        begin = text.index(BEGIN_MARKER)
        end = text.index(END_MARKER)
        if begin > end:
            errors.append(f"{slug}: Downloadblock-Ende steht vor dem Anfang")
            block = text
        else:
            block = text[begin:end]

    hits = 0
    for label in EXPECTED_LABELS:
        if label not in block:
            errors.append(f"{slug}: README-Downloadblock nennt {label} nicht")
        else:
            hits += 1

    for target in expected_targets(slug):
        if target not in block:
            errors.append(f"{slug}: README-Downloadblock verlinkt {target} nicht")
        else:
            hits += 1

    return hits


def validate_download_notices(
    label: str, text: str, errors: list[str], *, case_readme: bool = False
) -> int:
    for position in missing_notice_positions(text, case_readme=case_readme):
        line = text.count("\n", 0, position) + 1
        errors.append(
            f"{label}: unveränderter DE/EN-Hinweis fehlt unmittelbar vor "
            f"Downloadgruppe in Zeile {line}"
        )
    return len(download_group_starts(text, case_readme=case_readme))


def validate_overview(slug: str, overview: str, errors: list[str]) -> int:
    hits = 0
    overview_targets = (
        f"./{slug}/gesamt-pdf/{slug}_gesamt.pdf",
        release_url(slug),
        release_url(slug, "-einzelpdfs"),
    )
    for target in overview_targets:
        if target not in overview:
            errors.append(f"{slug}: zentrale Übersicht verlinkt {target} nicht")
        else:
            hits += 1
    return hits


def main() -> int:
    errors: list[str] = []
    if not path_exists(OVERVIEW):
        print("validate-testakten-readme-downloads: testakten/README.md fehlt", file=sys.stderr)
        return 1

    overview = read_text(OVERVIEW)
    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    checked_links = 0
    for directory in dirs:
        slug = directory.name
        checked_links += validate_local_readme(slug, directory, errors)
        checked_links += validate_overview(slug, overview, errors)

    central_readmes = {directory / "README.md" for directory in dirs}
    checked_groups = 0
    for readme in download_readmes(ROOT):
        if readme in central_readmes:
            continue
        checked_groups += validate_download_notices(
            readme.relative_to(ROOT).as_posix(), read_text(readme), errors,
            case_readme=is_case_readme(readme, ROOT),
        )

    if errors:
        print("validate-testakten-readme-downloads: FEHLER", file=sys.stderr)
        for err in errors[:80]:
            print(f" - {err}", file=sys.stderr)
        if len(errors) > 80:
            print(f" - ... {len(errors) - 80} weitere Fehler", file=sys.stderr)
        return 1

    print(
        f"validate-testakten-readme-downloads OK ({len(dirs)} Akten, "
        f"{checked_links} Treffer, {checked_groups} weitere Downloadgruppen)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

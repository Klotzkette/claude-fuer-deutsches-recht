#!/usr/bin/env python3
"""Gemeinsame flache und kollisionssichere ZIP-Benennung fuer Testakten."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

from testakte_file_filter import include_in_working_dump
from testakte_disclaimer import NOTICE_FILENAME


MAX_ARCHIVE_NAME = 220


def _shorten(name: str, identity: str) -> str:
    """Begrenzt sehr lange Namen, ohne Endung oder Eindeutigkeit zu verlieren."""
    if len(name) <= MAX_ARCHIVE_NAME:
        return name
    suffix = "".join(Path(name).suffixes[-2:]) or Path(name).suffix
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:10]
    room = MAX_ARCHIVE_NAME - len(suffix) - len(digest) - 2
    return f"{name[:room]}__{digest}{suffix}"


def flatten_relative_path(relative: Path) -> str:
    """Bildet einen relativen Pfad auf genau einen ZIP-Dateinamen ab."""
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise ValueError(f"unsicherer relativer Pfad: {relative}")
    if any(part in {"", "."} for part in relative.parts):
        raise ValueError(f"ungueltiger relativer Pfad: {relative}")
    name = "__".join(relative.parts).replace("/", "__").replace("\\", "__")
    return _shorten(name, relative.as_posix())


def flat_archive_pairs(
    items: Iterable[tuple[Path, Path]],
) -> list[tuple[Path, str]]:
    """Erzeugt flache, auch auf Windows kollisionsfreie Archivnamen."""
    pairs: list[tuple[Path, str]] = []
    used: set[str] = set()
    for source, desired_relative in items:
        name = flatten_relative_path(desired_relative)
        key = name.casefold()
        if key in used:
            path = Path(name)
            suffix = "".join(path.suffixes[-2:]) or path.suffix
            stem = name[: -len(suffix)] if suffix else name
            digest = hashlib.sha256(desired_relative.as_posix().encode("utf-8")).hexdigest()[:10]
            name = _shorten(f"{stem}__{digest}{suffix}", desired_relative.as_posix())
            key = name.casefold()
        counter = 2
        base = name
        while key in used:
            path = Path(base)
            suffix = "".join(path.suffixes[-2:]) or path.suffix
            stem = base[: -len(suffix)] if suffix else base
            name = _shorten(
                f"{stem}__{counter}{suffix}",
                f"{desired_relative.as_posix()}:{counter}",
            )
            key = name.casefold()
            counter += 1
        used.add(key)
        pairs.append((source, name))
    return pairs


def working_dump_flat_pairs(
    testakte_dir: Path,
    *,
    include_gesamt_pdf: bool,
) -> list[tuple[Path, str]]:
    """Liefert alle exportierten Originaldateien mit flachen ZIP-Namen."""
    items: list[tuple[Path, Path]] = []
    for path in sorted(
        testakte_dir.rglob("*"),
        key=lambda candidate: str(candidate.relative_to(testakte_dir)).lower(),
    ):
        if not include_in_working_dump(
            path,
            testakte_dir,
            include_gesamt_pdf=include_gesamt_pdf,
        ):
            continue
        relative = path.relative_to(testakte_dir)
        if relative.parts[0] == "gesamt-pdf":
            relative = Path(path.name)
        items.append((path, relative))
    return flat_archive_pairs(items)


def working_dump_expected_arcnames(
    testakte_dir: Path,
    *,
    include_gesamt_pdf: bool,
) -> list[str]:
    """Liefert den vollstaendigen Inhalt eines Originalformat-ZIPs."""
    names = [
        arcname
        for _, arcname in working_dump_flat_pairs(
            testakte_dir,
            include_gesamt_pdf=include_gesamt_pdf,
        )
    ]
    if NOTICE_FILENAME.casefold() in {name.casefold() for name in names}:
        raise ValueError(f"reservierter ZIP-Dateiname kollidiert: {NOTICE_FILENAME}")
    return [NOTICE_FILENAME, *names]

#!/usr/bin/env python3
"""Kollisionssichere ZIP-Benennung, einschließlich bestellter Projektordner."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

from testakte_file_filter import include_in_working_dump
from testakte_disclaimer import NOTICE_FILENAME


MAX_ARCHIVE_NAME = 220
# Diese Fassung wurde ausdrücklich als vollständige Projektordner-Akte bestellt.
# Bestehende Testakten behalten ihre flachen Archive.
STRUCTURED_TESTAKTEN = frozenset({'bauwirtschaft-hildesheim-lebensakte'})


def preserves_directories(testakte_dir: Path) -> bool:
    return testakte_dir.name in STRUCTURED_TESTAKTEN


def safe_archive_name(name: str, *, allow_directories: bool) -> bool:
    """Portable relative ZIP-Pfade ohne Traversal, Laufwerk oder Steuerzeichen."""
    if not name or any(character in name for character in '\\:*?<>|"') or name.startswith('/'):
        return False
    if any(ord(character) < 32 for character in name):
        return False
    parts = name.split('/')
    if any(part in {'', '.', '..'} or part.endswith((' ', '.')) for part in parts):
        return False
    if not allow_directories and len(parts) != 1:
        return False
    reserved = {'con', 'prn', 'aux', 'nul', *(f'com{i}' for i in range(1, 10)), *(f'lpt{i}' for i in range(1, 10))}
    return all(part.split('.')[0].casefold() not in reserved for part in parts)


def structured_archive_pairs(items: Iterable[tuple[Path, Path]]) -> list[tuple[Path, str]]:
    pairs = []
    used = set()
    for source, relative in items:
        name = relative.as_posix()
        if not safe_archive_name(name, allow_directories=True) or len(name) > MAX_ARCHIVE_NAME:
            raise ValueError(f'unsicherer oder zu langer Projektaktenpfad: {name}')
        if name.casefold() in used:
            raise ValueError(f'kollidierender Projektaktenpfad: {name}')
        used.add(name.casefold())
        pairs.append((source, name))
    return pairs


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


def _working_dump_items(
    testakte_dir: Path,
    *,
    include_gesamt_pdf: bool,
) -> list[tuple[Path, Path]]:
    """Liefert alle exportierten Originaldateien mit ihrem relativen Pfad."""
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
    return items


def working_dump_flat_pairs(testakte_dir: Path, *, include_gesamt_pdf: bool) -> list[tuple[Path, str]]:
    return flat_archive_pairs(_working_dump_items(testakte_dir, include_gesamt_pdf=include_gesamt_pdf))


def working_dump_archive_pairs(testakte_dir: Path, *, include_gesamt_pdf: bool) -> list[tuple[Path, str]]:
    items = _working_dump_items(testakte_dir, include_gesamt_pdf=include_gesamt_pdf)
    return structured_archive_pairs(items) if preserves_directories(testakte_dir) else flat_archive_pairs(items)


def working_dump_expected_arcnames(
    testakte_dir: Path,
    *,
    include_gesamt_pdf: bool,
) -> list[str]:
    """Liefert den vollstaendigen Inhalt eines Originalformat-ZIPs."""
    names = [
        arcname
        for _, arcname in working_dump_archive_pairs(
            testakte_dir,
            include_gesamt_pdf=include_gesamt_pdf,
        )
    ]
    if NOTICE_FILENAME.casefold() in {name.casefold() for name in names}:
        raise ValueError(f"reservierter ZIP-Dateiname kollidiert: {NOTICE_FILENAME}")
    return [NOTICE_FILENAME, *names]

#!/usr/bin/env python3
"""Erzeugt atomare, byte-stabile ZIP-Archive fuer Release-Artefakte."""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import stat
import tempfile
import unicodedata
import zipfile
from collections.abc import Callable, Iterable
from pathlib import Path, PurePosixPath


FIXED_ZIP_TIME = (2020, 1, 1, 0, 0, 0)
COPY_CHUNK_SIZE = 1024 * 1024
ALREADY_COMPRESSED_SUFFIXES = {
    ".7z",
    ".docx",
    ".gz",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".pptx",
    ".xlsx",
    ".zip",
}
ExcludePredicate = Callable[[PurePosixPath], bool]
ArchiveMember = tuple[Path, str]


def _normalise_arcname(value: str) -> str:
    if "\x00" in value:
        raise ValueError(f"unzulaessiger ZIP-Pfad: {value!r}")
    name = unicodedata.normalize("NFC", value.replace("\\", "/"))
    if name.startswith("/") or re.match(r"^[A-Za-z]:", name):
        raise ValueError(f"unzulaessiger ZIP-Pfad: {value!r}")
    path = PurePosixPath(name)
    parts = path.parts
    if not name or name.endswith("/") or ".." in parts:
        raise ValueError(f"unzulaessiger ZIP-Pfad: {value!r}")
    normalized = path.as_posix()
    if normalized in {"", "."}:
        raise ValueError(f"unzulaessiger ZIP-Pfad: {value!r}")
    return normalized


def _zip_info(arcname: str, source: Path) -> zipfile.ZipInfo:
    executable = bool(source.stat().st_mode & 0o111)
    permissions = 0o755 if executable else 0o644
    info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | permissions) << 16
    info.compress_type = (
        zipfile.ZIP_STORED
        if source.suffix.casefold() in ALREADY_COMPRESSED_SUFFIXES
        else zipfile.ZIP_DEFLATED
    )
    return info


def _stream_member(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    """Kopiert einen Eintrag speicherschonend und erkennt parallele Änderungen."""
    before = source.stat()
    written = 0
    info = _zip_info(arcname, source)
    with source.open("rb") as source_handle, archive.open(
        info, "w", force_zip64=True
    ) as target_handle:
        while chunk := source_handle.read(COPY_CHUNK_SIZE):
            target_handle.write(chunk)
            written += len(chunk)
    after = source.stat()
    if (
        written != before.st_size
        or after.st_size != before.st_size
        or after.st_mtime_ns != before.st_mtime_ns
    ):
        raise RuntimeError(f"Quelldatei waehrend ZIP-Bau geaendert: {source}")


def write_archive(output: Path, members: Iterable[ArchiveMember]) -> int:
    """Schreibt Dateien sortiert, mit festen Metadaten und atomarem Austausch."""
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    prepared: list[ArchiveMember] = []
    names: set[str] = set()
    for source, raw_arcname in members:
        if source.is_symlink():
            raise ValueError(f"Symlink nicht als Release-Datei zulaessig: {source}")
        source = source.resolve()
        if not source.is_file():
            raise FileNotFoundError(source)
        if source == output:
            raise ValueError("Ausgabe-ZIP darf nicht zugleich Quelldatei sein")
        arcname = _normalise_arcname(raw_arcname)
        collision_key = unicodedata.normalize("NFC", arcname).casefold()
        if collision_key in names:
            raise ValueError(f"doppelter oder kollidierender ZIP-Eintrag: {arcname}")
        names.add(collision_key)
        prepared.append((source, arcname))
    if not prepared:
        raise ValueError("kein ZIP-Eintrag vorhanden")
    prepared.sort(key=lambda item: (item[1] != "README.txt", item[1].casefold(), item[1]))

    descriptor, temp_name = tempfile.mkstemp(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent
    )
    os.close(descriptor)
    temp_path = Path(temp_name)
    try:
        with zipfile.ZipFile(
            temp_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=6,
        ) as archive:
            for source, arcname in prepared:
                _stream_member(archive, source, arcname)
        os.chmod(temp_path, 0o644)
        os.replace(temp_path, output)
    finally:
        temp_path.unlink(missing_ok=True)
    return len(prepared)


def tree_members(
    root: Path,
    *,
    exclude: ExcludePredicate | None = None,
) -> list[ArchiveMember]:
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)
    members: list[ArchiveMember] = []
    for source in root.rglob("*"):
        if not source.is_file():
            continue
        relative = PurePosixPath(source.relative_to(root).as_posix())
        if exclude and exclude(relative):
            continue
        members.append((source, relative.as_posix()))
    return members


def archive_tree(
    output: Path,
    root: Path,
    *,
    exclude: ExcludePredicate | None = None,
) -> int:
    root = root.resolve()
    output = output.resolve()
    try:
        output.relative_to(root)
    except ValueError:
        pass
    else:
        raise ValueError("Ausgabe-ZIP darf nicht innerhalb des Quellbaums liegen")
    return write_archive(output, tree_members(root, exclude=exclude))


def _pattern_excluder(patterns: list[str]) -> ExcludePredicate:
    def excluded(relative: PurePosixPath) -> bool:
        value = relative.as_posix()
        for pattern in patterns:
            if fnmatch.fnmatchcase(value, pattern):
                return True
            if pattern.startswith("**/") and fnmatch.fnmatchcase(value, pattern[3:]):
                return True
        return False

    return excluded


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Erzeugt ein reproduzierbares ZIP aus einem Verzeichnisbaum."
    )
    parser.add_argument("output", type=Path)
    parser.add_argument("root", type=Path)
    parser.add_argument("--exclude", action="append", default=[], metavar="GLOB")
    args = parser.parse_args()

    count = archive_tree(
        args.output,
        args.root,
        exclude=_pattern_excluder(args.exclude),
    )
    if count == 0:
        parser.error(f"{args.root}: keine Dateien fuer das ZIP gefunden")
    print(f"{args.output}: {count} Dateien")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

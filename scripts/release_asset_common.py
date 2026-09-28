#!/usr/bin/env python3
"""Gemeinsame Auswahl und Prüfsummenlogik für Release-Dateien."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from release_routing import check_asset_limit


SPECIAL_ASSETS = {"marketplace.json", "checksums-sha256.txt"}
ASSET_SUFFIXES = {".zip", ".md"}
CHECKSUM_RE = re.compile(r"^([0-9a-f]{64})  ([^/\\]+)$")


def is_release_asset(path: Path) -> bool:
    return (
        path.is_file()
        and not path.is_symlink()
        and (path.suffix.lower() in ASSET_SUFFIXES or path.name in SPECIAL_ASSETS)
    )


def release_assets(dist: Path, *, include_checksums: bool = True) -> list[Path]:
    assets = sorted(
        (path for path in dist.iterdir() if is_release_asset(path)),
        key=lambda path: path.name,
    )
    if not include_checksums:
        assets = [path for path in assets if path.name != "checksums-sha256.txt"]
    return assets


def sha256_file(path: Path, *, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def write_checksums(dist: Path) -> int:
    assets = release_assets(dist, include_checksums=False)
    if not assets:
        raise ValueError(f"No release assets in {dist}")
    target = dist / "checksums-sha256.txt"
    temporary = target.with_name(f".{target.name}.tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for path in assets:
            handle.write(f"{sha256_file(path)}  {path.name}\n")
    temporary.replace(target)
    return len(assets)


def read_checksums(path: Path) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = CHECKSUM_RE.fullmatch(raw_line)
        if not match:
            raise ValueError(f"{path}:{line_number}: ungültige Prüfsummenzeile")
        digest, name = match.groups()
        if name in checksums:
            raise ValueError(f"{path}:{line_number}: doppelter Dateiname {name}")
        checksums[name] = digest
    if not checksums:
        raise ValueError(f"{path}: keine Prüfsummen enthalten")
    return checksums


def expected_asset_metadata(dist: Path) -> dict[str, dict[str, int | str]]:
    """Liest Hashes aus der frisch erzeugten Liste und Größen vom Dateisystem."""
    checksum_path = dist / "checksums-sha256.txt"
    checksums = read_checksums(checksum_path)
    assets = release_assets(dist)
    names = {path.name for path in assets}
    check_asset_limit(names)
    expected_checksum_names = names - {checksum_path.name}
    missing = expected_checksum_names - set(checksums)
    extra = set(checksums) - expected_checksum_names
    if missing or extra:
        raise ValueError(
            f"Prüfsummenbestand weicht ab: fehlend={sorted(missing)[:10]}, "
            f"überzählig={sorted(extra)[:10]}"
        )
    metadata: dict[str, dict[str, int | str]] = {}
    checksum_mtime = checksum_path.stat().st_mtime_ns
    for path in assets:
        if path != checksum_path and path.stat().st_mtime_ns > checksum_mtime:
            raise ValueError(
                f"{path.name}: neuer als checksums-sha256.txt; Prüfsummen erneut erzeugen"
            )
        digest = sha256_file(path) if path == checksum_path else checksums[path.name]
        metadata[path.name] = {
            "size": path.stat().st_size,
            "digest": f"sha256:{digest}",
        }
    return metadata

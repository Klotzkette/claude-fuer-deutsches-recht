#!/usr/bin/env python3
"""Build and verify the Arbeitszeugnisprüfer component from this checkout."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

from prompt_profiles import PROMPT_SUFFIXES
from release_routing import validate_plugin_version

ROOT = Path(__file__).resolve().parents[1]
NAME = "arbeitszeugnispruefer"
PLUGIN = ROOT / NAME
PROMPT_ASSETS = tuple(f"{NAME}-{suffix}.md" for suffix in ("werkstatt", "schnellstart"))
CHECKSUM_ASSET = "checksums-sha256.txt"
PAYLOAD_ASSETS = frozenset((f"{NAME}.zip", *PROMPT_ASSETS))
RELEASE_ASSETS = PAYLOAD_ASSETS | {CHECKSUM_ASSET}


def checked_manifest() -> dict:
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entry = next(item for item in marketplace["plugins"] if item["name"] == NAME)
    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    if entry["version"] != manifest["version"]:
        raise ValueError("Marketplace and plugin component versions differ")
    validate_plugin_version(entry, marketplace["version"], root=ROOT)
    return manifest


def source_files() -> list[Path]:
    return [
        path for path in sorted(PLUGIN.rglob("*"))
        if path.is_file() and not path.is_symlink()
        and "__pycache__" not in path.parts and path.suffix != ".pyc"
        and path.name != ".DS_Store" and path.relative_to(PLUGIN).as_posix() != "CLAUDE.md"
        and not path.name.endswith(PROMPT_SUFFIXES)
    ]


def validate_assets(destination: Path) -> None:
    """Check the complete release, including downloads excluded from the ZIP."""
    if not destination.is_dir():
        raise ValueError(f"Release directory is missing: {destination}")
    actual = {path.name for path in destination.iterdir()}
    if actual != RELEASE_ASSETS:
        raise ValueError(f"Release asset inventory differs: {sorted(actual ^ RELEASE_ASSETS)}")
    for name in RELEASE_ASSETS:
        path = destination / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Release asset is not a regular file: {name}")
    for name in PROMPT_ASSETS:
        if (destination / name).read_bytes() != (PLUGIN / name).read_bytes():
            raise ValueError(f"Prompt asset differs from the source checkout: {name}")

    checksums = {}
    for line in (destination / CHECKSUM_ASSET).read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            raise ValueError("Malformed release checksum entry")
        digest, name = match.groups()
        if name not in PAYLOAD_ASSETS or name in checksums:
            raise ValueError(f"Unexpected or duplicate release checksum entry: {name}")
        checksums[name] = digest
    if set(checksums) != PAYLOAD_ASSETS:
        raise ValueError("Release checksum inventory is incomplete")
    for name, digest in checksums.items():
        if hashlib.sha256((destination / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Release checksum differs: {name}")


def validate_bundle(destination: Path, version: str) -> None:
    validate_assets(destination)
    spec = importlib.util.spec_from_file_location("release_zip_validator", ROOT / "scripts/validate-release-zips.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.validate_plugin_zip(destination, NAME, version)
    module.validate_focus_skill(destination / f"{NAME}.zip", PLUGIN, ROOT / "quality/evals" / f"{NAME}.json")
    with zipfile.ZipFile(destination / f"{NAME}.zip") as archive:
        expected = {path.relative_to(PLUGIN).as_posix(): path for path in source_files()}
        if set(archive.namelist()) != set(expected):
            raise ValueError("ZIP inventory differs from the source inventory")
        for name, path in expected.items():
            if archive.read(name) != path.read_bytes():
                raise ValueError(f"ZIP content differs: {name}")
        if "references/arbeitszeugnis-handbuch.md" not in expected:
            raise ValueError("The installed plugin must include the complete handbook reference")
    print(f"Verified {len(expected)} packed files against the source checkout.")


def verify_remote(destination: Path, tag: str) -> None:
    validate_assets(destination)
    with tempfile.TemporaryDirectory(prefix="zeugnis-release-verify-") as folder:
        subprocess.run(["gh", "release", "download", tag, "--repo", "Klotzkette/claude-fuer-deutsches-recht", "--dir", folder], check=True)
        target = Path(folder)
        validate_assets(target)
        for name in sorted(RELEASE_ASSETS):
            if (destination / name).read_bytes() != (target / name).read_bytes():
                raise ValueError(f"Remote asset differs: {name}")
        print(f"Verified {len(RELEASE_ASSETS)} downloaded release assets byte for byte.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--verify-release", metavar="TAG", help="Verify existing local and remote assets without rebuilding")
    args = parser.parse_args()
    destination = args.destination.resolve()
    if not args.verify_release and destination.is_relative_to(PLUGIN.resolve()):
        raise ValueError("Build destination must be outside the plugin directory")
    manifest = checked_manifest()
    if args.verify_release:
        if args.verify_release != f"{NAME}-v{manifest['version']}":
            raise ValueError("Release tag does not match the checked component version")
        validate_bundle(destination, manifest["version"])
        verify_remote(destination, args.verify_release)
        return

    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Build destination must be empty; existing assets are never overwritten")
    with zipfile.ZipFile(destination / f"{NAME}.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in source_files():
            item = zipfile.ZipInfo(path.relative_to(PLUGIN).as_posix(), (2026, 10, 8, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            archive.writestr(item, path.read_bytes())
    for name in PROMPT_ASSETS:
        source = PLUGIN / name
        shutil.copyfile(source, destination / source.name)
    checksums = "".join(
        f"{hashlib.sha256((destination / name).read_bytes()).hexdigest()}  {name}\n"
        for name in sorted(PAYLOAD_ASSETS)
    )
    (destination / CHECKSUM_ASSET).write_text(checksums, encoding="utf-8")
    validate_bundle(destination, manifest["version"])
    print(json.dumps({"version": manifest["version"], "assets": len(RELEASE_ASSETS), "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

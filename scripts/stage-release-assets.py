#!/usr/bin/env python3
"""Partition the completed dist without changing its files or aggregate ZIPs."""

from __future__ import annotations

import argparse
import errno
import json
import os
import shutil
import zipfile
from pathlib import Path

from release_asset_common import release_assets, write_checksums
from release_routing import (
    CONFIG, ROOT, check_asset_limit, companion_asset_names, companion_cases,
    companion_tag, marketplace_version,
)


def check_companion_bundles(dist: Path, slugs: tuple[str, ...]) -> None:
    expected = {
        "alle-testakten.zip": {f"testakte-{slug}.zip" for slug in slugs},
        "alle-testakten-einzelpdfs.zip": {f"testakte-{slug}-einzelpdfs.zip" for slug in slugs},
        "alles-komplettpaket.zip": {f"testakten/{name}" for name in companion_asset_names(slugs)},
    }
    for name, members in expected.items():
        with zipfile.ZipFile(dist / name) as archive:
            missing = members - set(archive.namelist())
        if missing:
            raise ValueError(f"Incomplete aggregate {name}: {sorted(missing)}")


def stage_assets(dist: Path, staging: Path, slugs: tuple[str, ...]) -> dict[str, int]:
    dist, staging = dist.resolve(), staging.resolve()
    if dist == staging or dist in staging.parents or staging in dist.parents:
        raise ValueError("dist and staging must be separate, non-nested directories")
    if staging.exists():
        raise ValueError(f"Staging must be a new directory: {staging}")
    assets = {path.name: path for path in release_assets(dist, include_checksums=False)}
    companion = companion_asset_names(slugs)
    missing = companion - assets.keys()
    if missing:
        raise ValueError(f"Configured companion ZIPs missing: {sorted(missing)}")
    groups = {"main": set(assets) - companion}
    if not groups["main"]:
        raise ValueError("No main release assets")
    if companion:
        groups["companion"] = companion
    for names in groups.values():
        check_asset_limit(names | {"checksums-sha256.txt"})
    if companion:
        check_companion_bundles(dist, slugs)

    staging.mkdir(parents=True)
    for group, names in groups.items():
        target = staging / group
        target.mkdir()
        for name in sorted(names):
            # Packaging is finished. Hardlinks avoid duplicating the large bundles.
            try:
                os.link(assets[name], target / name)
            except OSError as exc:
                if exc.errno != errno.EXDEV:
                    raise
                shutil.copy2(assets[name], target / name)
        write_checksums(target)
    return {group: len(names) + 1 for group, names in groups.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path)
    parser.add_argument("staging", type=Path)
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    slugs = companion_cases(args.config, args.root)
    tag = companion_tag(marketplace_version(args.root)) if slugs else ""
    counts = stage_assets(args.dist, args.staging, slugs)
    print(json.dumps({"assets": counts, "companion_tag": tag}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

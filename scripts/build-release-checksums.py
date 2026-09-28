#!/usr/bin/env python3
"""Erzeugt streamend SHA-256-Prüfsummen für alle Release-Dateien."""

from __future__ import annotations

import argparse
from pathlib import Path

from release_asset_common import write_checksums


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    args = parser.parse_args()
    if not args.dist.is_dir():
        parser.error(f"kein Verzeichnis: {args.dist}")
    try:
        count = write_checksums(args.dist)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"build-release-checksums OK ({count} Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

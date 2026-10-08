#!/usr/bin/env python3
"""Vergleicht hochgeladene Assets bytegenau vor der Veröffentlichung."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

tag, source = sys.argv[1:]
source = Path(source)
with tempfile.TemporaryDirectory(prefix="betreuung-release-") as scratch:
    subprocess.run(["gh", "release", "download", tag, "--dir", scratch], check=True)
    target = Path(scratch)
    expected = {p.name for p in source.iterdir() if p.is_file()}
    actual = {p.name for p in target.iterdir() if p.is_file()}
    if expected != actual:
        raise SystemExit(f"Assetliste weicht ab: {expected ^ actual}")
    for name in sorted(expected):
        if hashlib.sha256((source / name).read_bytes()).digest() != hashlib.sha256((target / name).read_bytes()).digest():
            raise SystemExit(f"Prüfsumme weicht ab: {name}")
    print(f"{len(expected)} Assets bytegenau geprüft.")

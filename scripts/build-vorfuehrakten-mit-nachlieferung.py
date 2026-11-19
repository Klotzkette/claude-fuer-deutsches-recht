#!/usr/bin/env python3
"""Vier häufig heruntergeladene Originalakten um die weitere Korrespondenz ergänzen."""
import argparse
import hashlib
import json
import shutil
import tempfile
import urllib.request
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from testakte_disclaimer import NOTICE_BYTES

QUELLEN = Path(__file__).resolve().parents[1] / "docs/workshops/vorfuehrakten-nachlieferungen"


def build(slug, source, dist, cache):
    basis = cache / (slug + ".zip")
    if not basis.exists():
        with urllib.request.urlopen(source["source"], timeout=90) as response, basis.open("wb") as f:
            shutil.copyfileobj(response, f)
    if hashlib.sha256(basis.read_bytes()).hexdigest() != source["sha256"]:
        raise ValueError(f"{slug}: Basisarchiv hat eine andere Prüfsumme")
    additional = {"Nachlieferung/" + p.name: p for p in (QUELLEN / slug).iterdir() if p.is_file()}
    output = dist / (slug + "-mit-nachtrag.zip")
    with ZipFile(basis) as old, ZipFile(output, "w") as new:
        members = old.namelist()
        if len(set(members)) != len(members) or set(members) & additional.keys():
            raise ValueError(f"{slug}: doppelte Archivpfade")
        if not old.read("README.txt").startswith(NOTICE_BYTES):
            raise ValueError(f"{slug}: Notice fehlt")
        for item in old.infolist():
            new.writestr(item, old.read(item))
        for name, path in sorted(additional.items()):
            info = ZipInfo(name, date_time=(2026, 11, 19, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            new.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED)
    with ZipFile(basis) as old, ZipFile(output) as new:
        if (new.testzip() is not None or set(new.namelist()) != set(old.namelist()) | additional.keys()
                or any(new.read(path) != old.read(path) for path in old.namelist())
                or any(new.read(name) != p.read_bytes() for name, p in additional.items())):
            raise ValueError(f"{slug}: Aktenbestand inkonsistent")
    print(output.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--basis", type=Path, help="Optionaler Cache für veröffentlichte Original-ZIPs")
    args = parser.parse_args()
    args.dist.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        cache = args.basis or Path(tmp)
        cache.mkdir(parents=True, exist_ok=True)
        for case, record in json.loads((QUELLEN / "basis.json").read_text()).items():
            build(case, record, args.dist, cache)

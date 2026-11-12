#!/usr/bin/env python3
"""Baut und prüft die Originalformat-ZIPs der Sammlung mit Grundakten."""

import argparse
from hashlib import file_digest
import importlib.util
import json
from pathlib import Path
from zipfile import ZipFile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_grundakte import FOLDER, selection
from testakte_zip_common import working_dump_archive_pairs


ROOT = Path(__file__).resolve().parents[1]
TAG = "grundakten-sammlung-v1.0.0"
SOURCES = ROOT / "scripts/data/testakten-grundakten-eingangsbestand.json"
INVENTORY = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
GROUPS = ("A–B", "C–K", "L–Z")
COMPONENT_CASES = {"bauunternehmer-einkauf-brandschutztueren-krimpfort"}


def load_script(stem):
    path = ROOT / "scripts" / f"{stem}.py"
    spec = importlib.util.spec_from_file_location(stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    with path.open("rb") as source:
        return file_digest(source, "sha256").hexdigest()


def cases_by_group():
    cases = set(json.loads(SOURCES.read_text(encoding="utf-8"))) - COMPONENT_CASES
    if not cases <= selection()["central"].keys():
        raise ValueError("Fall im Release ohne Grundaktenauswahl.")
    groups = {}
    for bounds in GROUPS:
        first, last = bounds.lower().split("–")
        groups[f"Grundakten_{first.upper()}-{last.upper()}.zip"] = sorted(
            case for case in cases if first <= case[0] <= last
        )
    if sum(map(len, groups.values())) != len(cases):
        raise ValueError("Mindestens eine Grundakte hat keinen Platz im Sammelpaket.")
    return groups


def archive_name(slug):
    return f"testakte-{slug}.zip"


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein.")
    dist.mkdir(parents=True, exist_ok=True)
    builder = load_script("build-testakten-release-zips")
    for bundle, slugs in cases_by_group().items():
        for slug in slugs:
            builder.build_single(ROOT / "testakten" / slug, dist)
        with ZipFile(dist / bundle, "x") as archive:
            builder.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
            for slug in slugs:
                filename = archive_name(slug)
                builder.write_file(archive, dist / filename, filename)
    inventory = inspect(dist)
    (dist / INVENTORY).write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dist / CHECKSUMS).write_text(
        "".join(f"{digest(path)}  {path.name}\n" for path in sorted(dist.iterdir())), encoding="ascii"
    )
    show(inventory)


def inspect(dist):
    checker = load_script("validate-testakten-release-zips")
    result = {"tag": TAG, "bundles": {}, "cases": {}}
    for bundle, slugs in cases_by_group().items():
        names = [NOTICE_FILENAME, *(archive_name(slug) for slug in slugs)]
        with ZipFile(dist / bundle) as package:
            if package.namelist() != names or package.read(NOTICE_FILENAME) != NOTICE_BYTES:
                raise ValueError(f"Abweichender Paketbestand: {bundle}")
            for slug in slugs:
                filename = archive_name(slug)
                case_path = dist / filename
                case_dir = ROOT / "testakten" / slug
                pairs = working_dump_archive_pairs(case_dir, include_gesamt_pdf=False)
                intake = sum(name.startswith(f"{FOLDER}/") for _, name in pairs)
                if intake != len(selection()["central"][slug]):
                    raise ValueError(f"Abweichende Grundakte: {slug}")
                checker.assert_same(filename, [NOTICE_FILENAME, *(name for _, name in pairs)],
                                    checker.zip_entries(case_path, require_notice=True, allow_directories=True))
                with ZipFile(case_path) as archive:
                    for source, member in pairs:
                        if archive.read(member) != source.read_bytes():
                            raise ValueError(f"Abweichendes Original: {slug}/{member}")
                sha = digest(case_path)
                with package.open(filename) as nested:
                    if file_digest(nested, "sha256").hexdigest() != sha:
                        raise ValueError(f"Abweichende Kopie im Sammelpaket: {filename}")
                result["cases"][slug] = {"bundle": bundle, "documents": len(pairs),
                                         "intake": intake, "sha256": sha}
        result["bundles"][bundle] = {"cases": len(slugs), "sha256": digest(dist / bundle)}
    return result


def show(report):
    print(f"{TAG}: {len(report['cases'])} Grundakten, "
          f"{sum(case['intake'] for case in report['cases'].values())} Eingangsunterlagen, "
          f"{len(report['bundles'])} Sammel-ZIPs.")


def verify(dist):
    hashes = dict(line.split("  ", 1)[::-1] for line in (dist / CHECKSUMS).read_text(encoding="ascii").splitlines())
    expected = {INVENTORY}
    for bundle, cases in cases_by_group().items():
        expected.add(bundle)
        expected.update(archive_name(case) for case in cases)
    if hashes.keys() != expected or {path.name for path in dist.iterdir()} != expected | {CHECKSUMS}:
        raise ValueError("Dateiliste und Prüfsummenliste stimmen nicht überein.")
    for name, sha in hashes.items():
        if digest(dist / name) != sha:
            raise ValueError(f"Prüfsummenabweichung: {name}")
    report = inspect(dist)
    if report != json.loads((dist / INVENTORY).read_text(encoding="utf-8")):
        raise ValueError("Abweichendes Release-Inventar.")
    show(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    (verify if args.verify else build)(args.dist.resolve())

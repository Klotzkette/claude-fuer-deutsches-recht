#!/usr/bin/env python3
"""Aktuelles bAV-Plugin und alle vier Arbeitsakten prüfen, ohne Release-Freigabe.

Die Paketversion folgt dem aktuellen Marketplace. Akten, Renderinventar und
Byteprüfungen bleiben dieselben wie beim historischen Komponentenrelease;
dessen feste Version, Scope, Routen und Publisher werden nicht überschrieben.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from bav_konzern_verify import verify_inventory
from release_asset_common import sha256_file
from release_routing import validate_plugin_version
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

spec = importlib.util.spec_from_file_location("bav_historical_release", Path(__file__).with_name("build-bav-konzern-release.py"))
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)
Q = H.Q
ROOT = H.ROOT
REPORT = "checkout-pruefung.json"
PURPOSE = "current-checkout-validation-only"


def expected_names():
    return (H.expected_names() - {H.REPORT, H.CHECKSUMS}) | {REPORT}


def current_version(root):
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = [row for row in market["plugins"] if row["name"] == H.PLUGIN]
    if len(entries) != 1:
        raise ValueError("Genau ein bAV-Marketplace-Eintrag erforderlich")
    entry = entries[0]
    directory = root / H.PLUGIN
    if (root / entry["source"]).resolve() != directory or directory.is_symlink() or not directory.is_dir():
        raise ValueError("Aktuelle bAV-Pluginquelle stimmt nicht")
    validate_plugin_version(entry, market["version"], root=root)
    return entry["version"]


def inspect(dist, root):
    version = current_version(root)
    if {p.name for p in dist.iterdir()} - {REPORT} != expected_names() - {REPORT}:
        raise ValueError("Checkout-Prüfbestand ist unvollständig oder überzählig")
    if any(not p.is_file() or p.is_symlink() for p in dist.iterdir()):
        raise ValueError("Checkout-Prüfbestand darf nur reguläre Dateien enthalten")
    files = Q.source_files(root, root / H.PLUGIN)
    manifests = Q.check_manifests(files, H.PLUGIN, version)
    skills = Q.verify_reachability(files)
    if len(skills) != 10:
        raise ValueError("Genau zehn auswählbare bAV-Skills erforderlich")
    chapters = H.verify_chapters(files, skills, root)
    plugin_hashes = Q.verify_zip(dist / f"{H.PLUGIN}.zip", files)
    Q.CHECKS.validate_plugin_zip(dist, H.PLUGIN, version)
    Q.CHECKS.validate_skill_sources(dist / f"{H.PLUGIN}.zip", root / H.PLUGIN)
    Q.CHECKS.validate_focus_skill(dist / f"{H.PLUGIN}.zip", root / H.PLUGIN,
                                root / "quality/evals" / f"{H.PLUGIN}.json")
    for filename in H.PROMPTS:
        if (dist / filename).read_bytes() != (root / H.PLUGIN / filename).read_bytes():
            raise ValueError(f"Abweichender Prompt: {filename}")
    # Keine bloße Existenzprüfung: alle ursprünglichen Quelldateien, Generatoren,
    # Fixtures und jedes PDF-Mitglied bleiben an das Renderinventar gebunden.
    verify_inventory(root)
    cases = {slug: H.case_evidence(dist, slug, root) for slug in H.CASES}
    H.verified_archive(dist / H.BUNDLE,
                       [(dist / H.names(slug)[0], H.names(slug)[0]) for slug in H.CASES], notice=True)
    return {"schema_version": 1, "purpose": PURPOSE, "plugin_name": H.PLUGIN, "version": version,
            "plugin": {"skills": skills, "chapters": chapters, "manifests": manifests, "files": plugin_hashes},
            "prompts": {name: sha256_file(dist / name) for name in H.PROMPTS}, "cases": cases,
            "render_inventory_sha256": sha256_file(root / H.PLUGIN / "testakten/pruefung/bestand.json"),
            "artifacts": {name: sha256_file(dist / name) for name in sorted(expected_names() - {REPORT})}}


def validate(dist, root=ROOT, *, expected_commit=None):
    root, dist = root.resolve(), dist.resolve()
    state = Q.checkout_state(root, expected_commit)
    if {p.name for p in dist.iterdir()} != expected_names():
        raise ValueError("Checkout-Prüfbestand benötigt exakt 17 Dateien")
    report = json.loads((dist / REPORT).read_text())
    if report != {**inspect(dist, root), "source_state": state}:
        raise ValueError("Checkout-Prüfnachweis stimmt nicht mit den aktuellen Quellen überein")
    return report


def build(dist, root=ROOT, *, expected_commit=None):
    root, dist = root.resolve(), dist.resolve()
    if dist.is_relative_to(root):
        raise ValueError("Checkout-Prüfziel muss außerhalb des Quellrepositories liegen")
    state = Q.checkout_state(root, expected_commit)
    current_version(root)
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Checkout-Prüfziel muss leer sein")
    Q.write_zip(dist / f"{H.PLUGIN}.zip", Q.source_files(root, root / H.PLUGIN))
    for filename in H.PROMPTS:
        shutil.copyfile(root / H.PLUGIN / filename, dist / filename)
    for slug in H.CASES:
        _, singles, combined = H.names(slug)
        H.NATIVE.build_single(root / "testakten" / slug, dist)
        shutil.copyfile(root / H.PLUGIN / "testakten/downloads" / singles, dist / singles)
        shutil.copyfile(root / "testakten" / slug / "gesamt-pdf" / combined, dist / combined)
    with ZipFile(dist / H.BUNDLE, "x") as archive:
        H.NATIVE.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for slug in H.CASES:
            name = H.names(slug)[0]
            H.NATIVE.write_file(archive, dist / name, name)
    report = {**inspect(dist, root), "source_state": state}
    (dist / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return validate(dist, root, expected_commit=expected_commit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--expected-commit")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = (validate if args.verify else build)(args.dist, expected_commit=args.expected_commit)
    print(f"bAV {result['version']}: aktuelles Plugin, zwei Prompts und vier Arbeitsakten vollständig geprüft; keine Release-Freigabe")


if __name__ == "__main__":
    main()

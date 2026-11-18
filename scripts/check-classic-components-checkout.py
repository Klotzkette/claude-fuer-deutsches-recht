#!/usr/bin/env python3
"""Prüfbau für CISG, Sanktionen und Kündigungsschutz am aktuellen Checkout.

Kein Veröffentlichungsnachweis: historische Builder und Releaseverträge bleiben
unverändert. Vorhandene Akten, Prompts und PDFs werden ausschließlich kopiert.
Die fachlichen Source-/Aktenprüfungen laufen zusätzlich im jeweiligen Workflow.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import shutil

from release_asset_common import read_checksums, sha256_file
from release_routing import validate_plugin_version

ROOT = Path(__file__).resolve().parents[1]
PURPOSE = "current-checkout-validation-only"
REPORT = "checkout-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
COMPONENTS = {
    "cisg": (("un-kaufrecht-cisg",), "cisg-akten.json", 3, 11),
    "sanktionen": (("eu-sanktionspruefer", "us-sanktionspruefer"), "sanktionen-akten.json", 4, 10),
    "kuendigungsschutz": (("arbeitsrecht-kuendigungsschutzklagewerkstatt",), "kuendigungsschutz-akten.json", 3, 11),
}

spec = importlib.util.spec_from_file_location("classic_checkout_packages", Path(__file__).with_name("build-skill-quality-release.py"))
PACKAGES = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PACKAGES)


def source(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or "\\" in relative:
        raise ValueError(f"Ungültiger Quellpfad: {relative}")
    target = root / path
    if (not target.is_file() or any((root / Path(*path.parts[:i])).is_symlink()
                                   for i in range(1, len(path.parts) + 1))
            or not target.resolve().is_relative_to(root.resolve())):
        raise ValueError(f"Quelldatei fehlt oder ist kein regulärer Checkoutinhalt: {relative}")
    return target


def collect(root: Path, component: str):
    names, dataset, case_count, skill_count = COMPONENTS[component]
    market_path = source(root, ".claude-plugin/marketplace.json")
    market = json.loads(market_path.read_text())
    copies, plugins = {}, {}
    inputs = {".claude-plugin/marketplace.json": sha256_file(market_path)}

    def copy(relative, asset=None):
        path = source(root, relative)
        asset = asset or path.name
        if Path(asset).name != asset or asset in copies or asset in {REPORT, CHECKSUMS}:
            raise ValueError(f"Doppeltes oder ungültiges Begleitasset: {asset}")
        copies[asset] = path

    def data(relative):
        path = source(root, relative)
        inputs[relative] = sha256_file(path)
        return json.loads(path.read_text())

    for name in names:
        matches = [row for row in market["plugins"] if row["name"] == name]
        if len(matches) != 1 or matches[0]["source"] != "./" + name:
            raise ValueError(f"Eindeutige Marketplacequelle fehlt: {name}")
        entry = matches[0]
        validate_plugin_version(entry, market["version"], root=root)
        files = PACKAGES.source_files(root, root / name)
        manifests = PACKAGES.check_manifests(files, name, entry["version"])
        if set(manifests) != set(PACKAGES.MANIFESTS):
            raise ValueError(f"Drei vorhandene Pluginmanifeste erforderlich: {name}")
        skills = PACKAGES.verify_reachability(files)
        if len(skills) != skill_count:
            raise ValueError(f"{name}: {skill_count} aktive Fach-/Hauptskills erforderlich")
        plugins[name] = {"files": files, "version": entry["version"], "manifests": manifests, "skills": skills}
        for kind in ("werkstatt", "schnellstart", "hauptproblem"):
            copy(f"{name}/{name}-{kind}.md")
        for relative in skills:
            copy(f"{name}/{relative}", f"{name}-{Path(relative).parent.name}.md")

    cases = data("scripts/data/" + dataset)
    if len(cases) != case_count or len({case["slug"] for case in cases}) != case_count:
        raise ValueError(f"{component}: vollständiger eindeutiger Aktenbestand erforderlich")
    if component == "sanktionen" and any(sum(case.get("plugin") == name for case in cases) != 2 for name in names):
        raise ValueError("Zwei Sanktionsakten je Plugin erforderlich")
    for case in cases:
        slug = case["slug"]
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Ungültige Aktenkennung")
        name = case["plugin"] if component == "sanktionen" else names[0]
        if name not in names:
            raise ValueError("Aktenzuordnung außerhalb der Komponente")
        copy(f"testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf")
        folder = "downloads" if component == "sanktionen" else "testakte/downloads"
        for suffix in ("", "-einzelpdfs"):
            copy(f"{name}/{folder}/testakte-{slug}{suffix}.zip")

    if component == "kuendigungsschutz":
        name = names[0]
        seewerk = data(f"{name}/testakte/pruefung/seewerk-bestand.json")
        if len(seewerk) != 2 or len({case["slug"] for case in seewerk}) != 2:
            raise ValueError("Zwei getrennte Seewerk-Fassungen erforderlich")
        for case in seewerk:
            slug = case["slug"]
            for filename in (slug + "_gesamt.pdf", *(f"testakte-{slug}{suffix}.zip" for suffix in ("", "-einzelpdfs", "-anlagen-k1-k14"))):
                copy(f"{name}/testakte/downloads/{filename}")
        for filename in ("mandantengespraech-seewerk.md", "seewerk-quellen-und-grenzen.md"):
            copy(f"{name}/referentenmaterial/{filename}")
        copy(f"{name}/testakte/downloads/testakte-arbeitsrecht-muster-uferwerk-berufung-einzelpdfs.zip")
    return plugins, copies, inputs


def inventory(root, component, plugins, copies, inputs):
    return {
        "schema_version": 1, "purpose": PURPOSE, "component": component,
        "inputs": inputs,
        "plugins": {name: {"version": row["version"], "manifests": row["manifests"],
                           "active_skills": row["skills"],
                           "files": {relative: sha256_file(path) for relative, path in row["files"].items()}}
                    for name, row in plugins.items()},
        "copied_assets": {name: {"source": path.relative_to(root).as_posix(), "sha256": sha256_file(path), "size": path.stat().st_size}
                          for name, path in copies.items()},
    }


def expected_names(plugins, copies):
    return set(copies) | {name + suffix for name in plugins for suffix in (".zip", "-portable.zip")} | {REPORT, CHECKSUMS}


def verify(root: Path, component: str, dist: Path):
    plugins, copies, inputs = collect(root, component)
    expected = expected_names(plugins, copies)
    if ({path.name for path in dist.iterdir()} != expected
            or any(not path.is_file() or path.is_symlink() for path in dist.iterdir())):
        raise ValueError("Prüfbestand enthält fehlende, zusätzliche oder unzulässige Dateien")
    report = json.loads((dist / REPORT).read_text())
    if report != inventory(root, component, plugins, copies, inputs):
        raise ValueError("Prüfbericht stimmt nicht mit den aktuellen Quellenbindungen überein")
    for name, row in plugins.items():
        for suffix, prefix in ((".zip", ""), ("-portable.zip", name + "/")):
            PACKAGES.verify_zip(dist / (name + suffix), row["files"], prefix)
    for name, path in copies.items():
        if (dist / name).read_bytes() != path.read_bytes():
            raise ValueError(f"Begleitasset weicht vom aktuellen Quellstand ab: {name}")
    checksums = read_checksums(dist / CHECKSUMS)
    if set(checksums) != expected - {CHECKSUMS}:
        raise ValueError("Prüfsummenbestand ist nicht vollständig und exakt")
    for name, digest in checksums.items():
        if sha256_file(dist / name) != digest:
            raise ValueError(f"Prüfsumme stimmt nicht: {name}")
    return report


def build(root: Path, component: str, dist: Path):
    root, dist = root.resolve(), dist.resolve()
    if dist == root or root in dist.parents or dist in root.parents:
        raise ValueError("Prüfausgabe muss außerhalb des Quellrepositorys liegen")
    if dist.exists() and (not dist.is_dir() or any(dist.iterdir())):
        raise ValueError("Prüfausgabe muss ein leeres Verzeichnis sein")
    plugins, copies, inputs = collect(root, component)
    report = inventory(root, component, plugins, copies, inputs)
    dist.mkdir(parents=True, exist_ok=True)
    for name, row in plugins.items():
        PACKAGES.write_zip(dist / (name + ".zip"), row["files"])
        PACKAGES.write_zip(dist / (name + "-portable.zip"), row["files"], name + "/")
    for name, path in copies.items():
        shutil.copyfile(path, dist / name)
    (dist / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    (dist / CHECKSUMS).write_text("".join(f"{sha256_file(path)}  {path.name}\n" for path in sorted(dist.iterdir())))
    return verify(root, component, dist)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("component", choices=COMPONENTS)
    parser.add_argument("--dist", required=True, type=Path)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    (verify if args.verify else build)(ROOT, args.component, args.dist)
    print(f"{args.component}: aktueller Checkout bytegenau geprüft; kein Release-Tag und keine Veröffentlichung.")

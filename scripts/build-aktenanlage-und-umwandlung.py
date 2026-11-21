#!/usr/bin/env python3
"""Baut und prüft die beiden Kursmappen und die vier zugehörigen Installationspakete."""

import argparse
import hashlib
import json
import re
import subprocess
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from akteneingang.ausgabe import archive
from akteneingang.fallausgaben import case_files
from akteneingang.fallpruefung import check, inspect_case
from akteneingang.quellen import ROOT
from package_readme import render_readme
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, NOTICE_MARKDOWN

VERSION = "445.36.10"
TAG = "fachaufnahme-v" + VERSION
URL = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/" + TAG
SUITES = {"aktenanleger": 5, "umwandlungssteuerrecht": 3}
PLUGINS = (*SUITES, "geldwaeschebeauftragter", "geldwaeschepraevention-aml-kyc")


def save_or_check(path, data, write):
    if write:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    else:
        check(path.read_bytes() == data, "Abweichung zum Aktenstand: " + str(path))


def dossiers(plugin, write):
    suite = ROOT / plugin / "testakten"
    proof = suite / "aktenbestand.json"
    old = {} if write else json.loads(proof.read_text())
    sources = sorted((ROOT / "scripts/data" / plugin).glob("*.json"))
    check(len(sources) == SUITES[plugin], "Unerwartete Fallzahl für " + plugin)
    bundle = {NOTICE_FILENAME: NOTICE_BYTES + "\nZuerst je Fall die Grundakte öffnen. Nachreichungen und Arbeitsvorlagen getrennt verwenden.\n".encode()}
    report, payload = {}, {}
    rows = ["# Die Übungsakten", "", "Öffnen Sie zuerst die Grundakte im Originalformat. Führen Sie die Bearbeitung mit den späteren Unterlagen im Ordner Nachreichungen fort. Bearbeitbare Muster stehen unter Vorlagen.", "",
            NOTICE_MARKDOWN, "", f"[Alle {len(sources)} Akten als ZIP]({URL}/{plugin}-testakten.zip)", "",
            "| Fall | Ausgangslage |", "| --- | --- |"]
    for source in sources:
        case = json.loads(source.read_text())
        slug = source.stem
        check(case["id"] == slug and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug), str(source))
        assets, report[slug] = case_files(case, suite, write, old.get(slug), source=source,
                                           prefix="testakte-", overview="Zur Fallauswahl")
        native, _ = inspect_case(case, None, suite=suite, prefix="testakte-")
        bundle.update({slug + "/" + name: data for name, data in native.items()})
        payload.update(assets)
        rows.append(f"| [{case['titel']}]({slug}/README.md) | {case['einstieg']} |")
    save_or_check(proof, (json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode(), write)
    save_or_check(suite / "README.md", ("\n".join(rows) + "\n").encode(), write)
    payload[plugin + "-testakten.zip"] = archive(bundle)
    return payload


def packages(commit):
    spec = spec_from_file_location("quality_release", ROOT / "scripts/build-skill-quality-release.py")
    quality = module_from_spec(spec)
    spec.loader.exec_module(quality)
    payload = {}
    for name in PLUGINS:
        directory = ROOT / name
        files = quality.source_files(ROOT, directory)
        quality.check_manifests(files, name, VERSION)
        reachable = quality.verify_reachability(files)
        check(name not in SUITES or len(reachable) == 8, "Acht Skills erforderlich: " + name)
        readme = render_readme(ROOT, directory, files, commit)
        payload[name + ".zip"] = archive({n: readme if n == "README.md" else p.read_bytes() for n, p in files.items()})
        for kind in ("werkstatt", "schnellstart", "hauptproblem"):
            md = directory / f"{name}-{kind}.md"
            if not md.exists() and kind == "hauptproblem":
                continue
            payload[md.name] = md.read_bytes()
            txt = md.with_suffix(".txt")
            if txt.exists():
                check(txt.read_bytes() == payload[md.name], "Text-/Markdown-Abweichung: " + name)
                payload[txt.name] = txt.read_bytes()
    return payload


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    group = cli.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-cases", action="store_true", help="Beide Fallserien aus ihren Fachquellen setzen")
    group.add_argument("--dist", type=Path, help="Leerer Ordner für den Freigabebau")
    group.add_argument("--verify", type=Path, help="Alle Dateien eines fertigen Pakets inhaltlich abgleichen")
    cli.add_argument("--commit", help="Vollständiger Commit für beständige Quellenlinks")
    args = cli.parse_args()
    payload = {}
    for plugin in SUITES:
        payload.update(dossiers(plugin, args.write_cases))
    if args.write_cases:
        return
    commit = args.commit or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    check(re.fullmatch("[0-9a-f]{40}", commit), "Ungültiger Commit")
    payload.update(packages(commit))
    payload["checksums-sha256.txt"] = "".join(f"{hashlib.sha256(blob).hexdigest()}  {name}\n" for name, blob in sorted(payload.items())).encode()
    if args.verify:
        check(set(payload) == {p.name for p in args.verify.iterdir()}, "Falscher Releaseumfang")
        for name, expected in payload.items():
            path = args.verify / name
            check(path.is_file() and not path.is_symlink() and path.read_bytes() == expected, name + " weicht ab")
    else:
        args.dist.mkdir(parents=True, exist_ok=True)
        check(not any(args.dist.iterdir()), "Ausgabeverzeichnis muss leer sein")
        for name, blob in payload.items():
            (args.dist / name).write_bytes(blob)
    print(f"{len(PLUGINS)} Plugins, {sum(SUITES.values())} Originalakten, {len(payload)} Freigabedateien geprüft.")


if __name__ == "__main__":
    main()

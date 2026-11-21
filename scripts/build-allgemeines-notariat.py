#!/usr/bin/env python3
"""Baut die sieben Amtsgeschäfte, ihre Druckfassungen und die gemeinsame Notariatsmappe."""

import argparse
import json
import re
import subprocess
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from akteneingang.fallausgaben import case_files
from akteneingang.ausgabe import archive
from akteneingang.quellen import ROOT, Sources, digest, members
from package_readme import render_readme
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

PLUGIN = "allgemeines-notariat"
BASE = ROOT / PLUGIN
DATA = ROOT / "scripts/data"
CASES = (
    "wohnung-stuttgart",
    "hofuebergabe-tuebingen",
    "testament-luebeck",
    "vorsorgevollmacht-bonn",
    "erbausschlagung-kassel",
    "vereinsvorstand-jena",
    "anteilskauf-osnabrueck",
)


def stored_cases():
    return json.loads((DATA / "notariat-bestandsakten.json").read_text())


def installable(commit):
    spec = spec_from_file_location(
        "skillrelease", ROOT / "scripts/build-skill-quality-release.py"
    )
    q = module_from_spec(spec)
    spec.loader.exec_module(q)
    files = q.source_files(ROOT, BASE)
    q.check_manifests(files, PLUGIN, "1.0.0")
    if len(q.verify_reachability(files)) != 10:
        raise ValueError("Zehn erreichbare Skills erforderlich")
    readme = render_readme(ROOT, BASE, files, commit)
    return archive(
        {
            name: readme if name == "README.md" else path.read_bytes()
            for name, path in files.items()
        }
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-cases",
        action="store_true",
        help="Sieben Falldossiers im Repository aus der Redaktion setzen",
    )
    parser.add_argument(
        "--dist", type=Path, help="Leeres Ziel für die vollständige Kursausgabe"
    )
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--local-index", type=Path)
    parser.add_argument(
        "--commit",
        help="Git-Commit für beständige Quellenlinks im installierbaren Paket",
    )
    args = parser.parse_args()
    if not args.dist and not args.write_cases:
        parser.error("--dist oder --write-cases erforderlich")
    if args.dist and args.dist.exists() and any(args.dist.iterdir()):
        parser.error("Ausgabeordner muss leer sein")
    payload = {}
    collected = {
        NOTICE_FILENAME: NOTICE_BYTES
        + "\nÖffnen Sie einen Fallordner. Jede Akte enthält die Grundakte zur ersten Sichtung. Bei den sieben Amtsgeschäften folgen Nachreichungen und Vorlagen in getrennten Unterordnern.\n".encode()
    }
    stock = stored_cases()
    stats = {}
    proof = BASE / "testakten/aktenbestand.json"
    old = {} if args.write_cases else json.loads(proof.read_text())
    if not args.write_cases and set(old) != set(CASES):
        raise ValueError("Unvollständiger Fallnachweis")
    for slug in CASES:
        case = json.loads((DATA / PLUGIN / (slug + ".json")).read_text())
        if case["id"] != slug:
            raise ValueError(slug)
        assets, stats[slug] = case_files(
            case, BASE / "testakten", args.write_cases, old.get(slug),
            source=DATA / PLUGIN / (slug + ".json"), prefix="testakte-notariat-",
            overview="Alle Fälle des allgemeinen Notariats",
        )
        payload.update(assets)
        for name, blob in members(assets["testakte-notariat-" + slug + ".zip"]).items():
            collected["Amtsgeschaefte/" + slug + "/" + name] = blob
    if args.write_cases:
        proof.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")
    if not args.dist:
        return
    sources = Sources(args.cache, args.local_index)
    for slug, row in stock.items():
        original = members(sources.read(row))
        if not original[NOTICE_FILENAME].startswith(NOTICE_BYTES) or not any(
            n.startswith("Grundakte/") for n in original
        ):
            raise ValueError("Bestandsakte ohne belegten Eingang: " + slug)
        for name, blob in original.items():
            collected["Weitere_Notariatsakten/" + slug + "/" + name] = blob
    payload[PLUGIN + "-alle-testakten.zip"] = archive(collected)
    commit = (
        args.commit
        or subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    )
    if not re.fullmatch("[0-9a-f]{40}", commit):
        raise ValueError("Vollständiger Git-Commit erforderlich")
    payload[PLUGIN + ".zip"] = installable(commit)
    for kind in ("werkstatt", "schnellstart"):
        for ext in ("md", "txt"):
            path = BASE / (PLUGIN + "-" + kind + "." + ext)
            payload[path.name] = path.read_bytes()
    payload["aktenbestand.json"] = (
        json.dumps(
            {"neue_faelle": stats, "bestandsakten": stock}, ensure_ascii=False, indent=2
        )
        + "\n"
    ).encode()
    payload["checksums-sha256.txt"] = "".join(
        f"{digest(v)}  {k}\n" for k, v in sorted(payload.items())
    ).encode()
    args.dist.mkdir(parents=True, exist_ok=True)
    for name, blob in payload.items():
        (args.dist / name).write_bytes(blob)
    print(
        f"{len(stats)} Amtsgeschäfte, {len(stock)} Bestandsakten, {len(payload)} Dateien"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Aktiviert genau eine geprüfte Plugin-Ausgabe nach dem Abgleich ihrer öffentlichen Dateien."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

from package_edition import EDITION, activate_routes

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "qualitaetsrunde-v445.36.13": Path("vergaberecht-werkstatt/vergabestelle-behoerden"),
    "qualitaetsrunde-v445.36.14": Path("patentrecht"),
    "qualitaetsrunde-v445.36.15": Path("vergaberecht-werkstatt/vergabestelle-behoerden"),
}


def metadata_changes(root, scope, report):
    plugin, = scope["plugins"]
    name, version = plugin["name"], scope["version"]
    source_path = SOURCES[scope["tag"]]
    predecessor = plugin["previous_release"]
    if name != source_path.name or not BUILDER.SLUG.fullmatch(name) or not set(predecessor["manifests"]) <= set(BUILDER.MANIFESTS):
        raise ValueError("Unzulässiger Plugin- oder Manifestname im Freigabeplan")
    asset = name + ".zip"
    proof = report["plugins"][name]["archives"][asset]
    digest = hashlib.sha256(json.dumps(scope, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if (report["scope_sha256"] != digest or report["version"] != version
            or report["plugins"][name]["source"] != "./" + source_path.as_posix()):
        raise ValueError("Öffentliche Ausgabe und registrierter Plugin-Scope weichen ab")
    if set(report["prompts"]) != set(plugin["prompts"]):
        raise ValueError("Öffentlicher Promptbestand weicht vom Freigabeplan ab")
    for filename in plugin["prompts"]:
        if (not re.fullmatch(re.escape(name) + r"-(?:werkstatt|schnellstart|hauptproblem)\.(?:md|txt)", filename)
                or hashlib.sha256((root / source_path / filename).read_bytes()).hexdigest() != report["prompts"][filename]):
            raise ValueError(f"{filename}: lokaler Prompt weicht vom veröffentlichten Stand ab")
    updates = {}
    market_filename = Path(".claude-plugin/marketplace.json")
    markets = {market_filename: "./" + source_path.as_posix()}
    if source_path.parent != Path("."):
        markets[source_path.parent / market_filename] = "./" + name
    for relative, source in markets.items():
        path = root / relative
        market = json.loads(path.read_bytes())
        entry, = (p for p in market["plugins"] if p["name"] == name)
        if entry["source"] != source or entry["version"] not in (predecessor["version"], version):
            raise ValueError(f"{relative}: Unerwarteter Quell- oder Versionsstand")
        entry["version"] = version
        updates[path] = (json.dumps(market, ensure_ascii=False, indent=2) + "\n").encode()
    for member, old_hash in predecessor["manifests"].items():
        path = root / source_path / member
        obj = json.loads(path.read_bytes())
        target = BUILDER.versioned_manifest(obj, version)
        allowed = {old_hash, hashlib.sha256(target).hexdigest()}
        if (obj["name"] != name or hashlib.sha256(path.read_bytes()).hexdigest() not in allowed
                or hashlib.sha256(target).hexdigest() != proof[member]):
            raise ValueError(f"{member}: Manifest des veröffentlichten Pakets weicht ab")
        updates[path] = target
    path = root / f"scripts/data/{EDITION}.json"
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    successors = data["nachfolger"]
    if asset in successors:
        previous = successors[asset]["tag"]
        if previous not in (predecessor["tag"], scope["tag"]):
            raise ValueError(f"{EDITION}: unerwartete Nachfolge für {asset}")
        successors[asset]["tag"] = scope["tag"]
    else:
        if predecessor["tag"] != f"{EDITION}-v{predecessor['version']}":
            raise ValueError(f"{EDITION}: Vorgängereintrag für {asset} fehlt")
        successors[asset] = {"ausgabeversion": predecessor["version"], "tag": scope["tag"]}
    # Preserve historical group rows and their hand-formatted representation.
    start = text.index('  "nachfolger": {')
    lines = ["    " + json.dumps(key) + ": " + json.dumps(row, ensure_ascii=False)
             for key, row in successors.items()]
    updated = text[:start] + '  "nachfolger": {\n' + ",\n".join(lines) + "\n  }\n}\n"
    if json.loads(updated) != data:
        raise ValueError(f"{EDITION}: unerwartetes Format im Ausgabenplan")
    updates[path] = updated.encode()
    return updates


def main(default_tag=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", choices=sorted(SOURCES), default=default_tag, required=default_tag is None)
    parser.add_argument("--expected-commit", required=True, help="Vollständiger veröffentlichter Quellcommit")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-f0-9]{40}", args.expected_commit):
        parser.error("Vollständiger 40-stelliger Git-Commit erwartet")
    subprocess.run(["git", "merge-base", "--is-ancestor", args.expected_commit, "HEAD"], cwd=ROOT, check=True)
    scope_path = Path(f"scripts/data/{args.tag}-scope.json")
    scope = json.loads((ROOT / scope_path).read_bytes())
    recorded = subprocess.check_output(["git", "show", f"{args.expected_commit}:{scope_path}"], cwd=ROOT)
    if scope != json.loads(recorded) or scope["tag"] != args.tag:
        raise ValueError("Lokaler Ausgabeplan weicht vom freigegebenen Quellcommit ab")
    plugin, = scope["plugins"]
    routes = {plugin["name"] + ".zip": (plugin["previous_release"]["tag"], scope["tag"])}
    publisher = BUILDER.load_module("publish-skill-quality-release.py")
    verifier = BUILDER.load_module("paketpflege.py")
    # Prompt snapshots are public release assets. Pages also serves their editable Markdown source.
    public_assets = {**routes, **{name: (None, scope["tag"]) for name in plugin["prompts"]}}
    reports = verifier.verify_public(publisher, public_assets, [scope["tag"]], args.expected_commit)
    updates = metadata_changes(ROOT, scope, reports[scope["tag"]])
    activate_routes(ROOT, routes)
    for path, contents in updates.items():
        if path.read_bytes() != contents:
            path.write_bytes(contents)
    generators = ["scripts/generate-root-plugin-catalog.py", "scripts/generate-skills-md.py"]
    if SOURCES[scope["tag"]].parent != Path("."):
        generators.append("vergaberecht-werkstatt/scripts/generate-skills-md.py")
    for generator in generators:
        subprocess.run([sys.executable, str(ROOT / generator)], cwd=ROOT, check=True)
    print(f"{scope['tag']}: Öffentliche Dateien bestätigt und lokale Kataloge aktualisiert.")


spec = importlib.util.spec_from_file_location("release_builder", ROOT / "scripts/build-skill-quality-release.py")
BUILDER = importlib.util.module_from_spec(spec)
spec.loader.exec_module(BUILDER)
if __name__ == "__main__":
    main()

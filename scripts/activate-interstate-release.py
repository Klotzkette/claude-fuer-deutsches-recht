#!/usr/bin/env python3
"""Aktiviert den Desktop-Download nach dem Abgleich der öffentlichen Interstate-Ausgabe."""
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
SCOPE = Path("scripts/data/qualitaetsrunde-v445.36.13-scope.json")
COMPONENT = Path("vergaberecht-werkstatt")


def metadata_changes(root, scope, report):
    plugin, = scope["plugins"]
    name, version = plugin["name"], scope["version"]
    predecessor = plugin["previous_release"]
    if not BUILDER.SLUG.fullmatch(name) or not set(predecessor["manifests"]) <= set(BUILDER.MANIFESTS):
        raise ValueError("Unzulässiger Plugin- oder Manifestname im Freigabeplan")
    asset = name + ".zip"
    proof = report["plugins"][name]["archives"][asset]
    digest = hashlib.sha256(json.dumps(scope, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if (report["scope_sha256"] != digest or report["version"] != version
            or report["plugins"][name]["source"] != f"./{COMPONENT}/{name}"):
        raise ValueError("Öffentliche Ausgabe und registrierter Vergabestellen-Scope weichen ab")
    updates = {}
    for relative, source in ((Path(".claude-plugin/marketplace.json"), f"./{COMPONENT}/{name}"),
                             (COMPONENT / ".claude-plugin/marketplace.json", "./" + name)):
        path = root / relative
        market = json.loads(path.read_bytes())
        entry, = (p for p in market["plugins"] if p["name"] == name)
        if entry["source"] != source or entry["version"] not in (predecessor["version"], version):
            raise ValueError(f"{relative}: Unerwarteter Quell- oder Versionsstand")
        entry["version"] = version
        updates[path] = (json.dumps(market, ensure_ascii=False, indent=2) + "\n").encode()
    for member, old_hash in predecessor["manifests"].items():
        path = root / COMPONENT / name / member
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
    previous = data["nachfolger"][asset]["tag"]
    if previous not in (predecessor["tag"], scope["tag"]):
        raise ValueError(f"{EDITION}: unerwartete Nachfolge für {asset}")
    data["nachfolger"][asset]["tag"] = scope["tag"]
    updated = text.replace(f'"tag": "{previous}"', f'"tag": "{scope["tag"]}"')
    if json.loads(updated) != data:
        raise ValueError(f"{EDITION}: mehrdeutige Änderung im Ausgabenplan")
    updates[path] = updated.encode()
    return updates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True, help="Vollständiger veröffentlichter Quellcommit")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-f0-9]{40}", args.expected_commit):
        parser.error("Vollständiger 40-stelliger Git-Commit erwartet")
    subprocess.run(["git", "merge-base", "--is-ancestor", args.expected_commit, "HEAD"], cwd=ROOT, check=True)
    scope = json.loads((ROOT / SCOPE).read_bytes())
    recorded = subprocess.check_output(["git", "show", f"{args.expected_commit}:{SCOPE}"], cwd=ROOT)
    if scope != json.loads(recorded):
        raise ValueError("Lokaler Ausgabeplan weicht vom freigegebenen Quellcommit ab")
    plugin, = scope["plugins"]
    routes = {plugin["name"] + ".zip": (plugin["previous_release"]["tag"], scope["tag"])}
    publisher = BUILDER.load_module("publish-skill-quality-release.py")
    verifier = BUILDER.load_module("paketpflege.py")
    reports = verifier.verify_public(publisher, routes, [scope["tag"]], args.expected_commit)
    updates = metadata_changes(ROOT, scope, reports[scope["tag"]])
    activate_routes(ROOT, routes)
    for path, contents in updates.items():
        if path.read_bytes() != contents:
            path.write_bytes(contents)
    for generator in ("scripts/generate-root-plugin-catalog.py", "scripts/generate-skills-md.py",
                      "vergaberecht-werkstatt/scripts/generate-skills-md.py"):
        subprocess.run([sys.executable, str(ROOT / generator)], cwd=ROOT, check=True)
    print(f"{scope['tag']}: Öffentliche Dateien bestätigt und lokale Kataloge aktualisiert.")


spec = importlib.util.spec_from_file_location("release_builder", ROOT / "scripts/build-skill-quality-release.py")
BUILDER = importlib.util.module_from_spec(spec)
spec.loader.exec_module(BUILDER)
if __name__ == "__main__":
    main()

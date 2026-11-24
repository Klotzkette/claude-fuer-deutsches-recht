#!/usr/bin/env python3
"""Schaltet die 25 Paare vollständiger Arbeitsakten nach Prüfung des öffentlichen Releases um."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

from akteneingang.verweise import FACHTAG, fachpfade
from package_edition import activate_routes
from release_routing import RELEASE_BASE, REPOSITORY

ROOT = Path(__file__).resolve().parents[1]
BUILDER = importlib.import_module("build-insolvenz-arbeitsvorlagen-release")
TAG = BUILDER.TAG


def activate_verified(root, sources):
    routes = {name: (row["tag"], TAG) for name, row in sources.items()}
    # Bis zur ersten expliziten Zuordnung bilden verweise.links die URL dieser Fachakten mit FACHTAG.
    fallback_tags = {
        f"lebensakte-{path.removeprefix('testakten/')}.zip": FACHTAG
        for path in fachpfade() if path.startswith("testakten/")
    }
    return activate_routes(root, routes, fallback_tags=fallback_tags,
                           extra_documents={"docs/grundakten-lebenswelt/Fachakten.md"})


def public_files(dist, expected, commit):
    public = importlib.import_module("validate-public-downloads")
    publisher = importlib.import_module("publish-release-assets")
    metadata = public.public_assets(TAG, public.github_cli_json)
    if publisher.tag_commit(REPOSITORY, TAG) != commit or metadata.keys() != expected:
        raise ValueError(f"{TAG}: Quellcommit oder öffentlicher Assetbestand weicht ab")

    def download(name):
        asset = metadata[name]
        if asset.get("state") != "uploaded" or not asset.get("size"):
            raise ValueError(f"{name}: öffentliche Datei fehlt oder ist leer")
        request = Request(f"{RELEASE_BASE}/download/{TAG}/{name}", headers={"User-Agent": "Insolvenz-Aktenabgleich"})
        digest = hashlib.sha256()
        target = dist / name
        with urlopen(request, timeout=60) as source, target.open("wb") as output:
            while block := source.read(1024 * 1024):
                output.write(block)
                digest.update(block)
        if target.stat().st_size != asset["size"] or f"sha256:{digest.hexdigest()}" != asset.get("digest"):
            raise ValueError(f"{name}: öffentlicher Download weicht von den GitHub-Metadaten ab")

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(download, sorted(expected)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True, help="Vollständiger veröffentlichter Quellcommit")
    parser.add_argument("--cache", type=Path, help="Vorhandener Cache der historischen Originalarchive")
    args = parser.parse_args()
    commit = args.expected_commit
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        parser.error("Vollständige Commit-SHA mit 40 Stellen erforderlich")
    subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT, check=True)
    recorded = subprocess.check_output(["git", "show", f"{commit}:{BUILDER.SOURCES_FILE}"], cwd=ROOT)
    if recorded != (ROOT / BUILDER.SOURCES_FILE).read_bytes():
        raise ValueError("Lokaler Quellenbestand weicht vom veröffentlichten Quellcommit ab")
    sources, _, _ = BUILDER.scope_files(ROOT)
    expected = set(sources) | {BUILDER.FORMS.COLLECTION.name, BUILDER.INVENTORY, BUILDER.CHECKSUMS}
    with TemporaryDirectory(prefix="insolvenz-arbeitsvorlagen-") as directory:
        dist = Path(directory) / "release"
        dist.mkdir()
        public_files(dist, expected, commit)
        edition = BUILDER.Edition(args.cache or Path(directory) / "quellen", offline=False)
        edition.validate_assets(dist, BUILDER.SCOPE, ROOT, expected_commit=commit)
    changed = activate_verified(ROOT, sources)
    print(f"{TAG}: {len(expected)} öffentliche Dateien bestätigt, {changed} Katalog- und Routingdateien aktualisiert.")


if __name__ == "__main__":
    main()

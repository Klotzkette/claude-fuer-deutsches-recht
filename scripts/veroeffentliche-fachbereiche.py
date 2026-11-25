#!/usr/bin/env python3
"""Prüft und veröffentlicht die Pakete für Insolvenzrecht und Betriebsvereinbarungen."""
import argparse
import importlib
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from release_asset_common import write_checksums, sha256_file
from release_routing import REPOSITORY

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = importlib.import_module("publish-skill-quality-release")
INSOLVENZ = importlib.import_module("build-insolvenz-fachpakete")
COPILOT = "testakte-betriebsvereinbarung-copilot-maschinenbau-kassel"
AUSGABEN = {
    "betriebsvereinbarungen-v1.0.0": "Betriebsvereinbarungen und die Copilot-Pilotakte",
    INSOLVENZ.TAG: "Fachbereich Insolvenzrecht",
}


def stage(tag, dist, root):
    if tag == INSOLVENZ.TAG:
        source = root / "Fachbereiche/Insolvenzrecht"
        subprocess.run([sys.executable, "scripts/insolvenz-fachbereich-pakete.py"], cwd=root, check=True)
        files = sorted(source.glob("*.zip"))
        if len(files) != 16:
            raise ValueError("Für den Insolvenz-Fachbereich werden 16 native Pakete benötigt.")
        for plugin in INSOLVENZ.PLUGINS:
            (dist / f"{plugin}-portable.zip").write_bytes(INSOLVENZ.package(plugin, root, portable=True))
    else:
        source = root / "docs/downloads"
        subprocess.run([sys.executable, "scripts/build-betriebsvereinbarungen.py", "--check"], cwd=root, check=True)
        files = [source / name for name in ("betriebsvereinbarungen.zip", COPILOT + ".zip", COPILOT + "-einzelpdfs.zip")]
    for path in files:
        shutil.copyfile(path, dist / path.name)
    write_checksums(dist)


def hashes(directory):
    return {p.name: sha256_file(p) for p in directory.iterdir() if p.is_file()}


class Edition:
    checkout_state = staticmethod(PUBLISHER.B.checkout_state)

    @staticmethod
    def validate_assets(dist, scope, root, *, expected_commit):
        Edition.checkout_state(root, expected_commit)
        with TemporaryDirectory() as temporary:
            other = Path(temporary)
            stage(scope["tag"], other, root)
            if hashes(dist) != hashes(other):
                raise ValueError("Paketnamen oder Inhalt weichen vom geprüften Quellstand ab.")

    @staticmethod
    def verify_download(dist, scope, root, repo, expected_commit):
        with TemporaryDirectory() as temporary:
            other = Path(temporary)
            subprocess.run(["gh", "release", "download", scope["tag"], "--repo", repo, "--dir", str(other)],
                           cwd=root, check=True, timeout=900)
            if hashes(dist) != hashes(other):
                raise ValueError("Der GitHub-Download stimmt nicht mit der geprüften Ausgabe überein.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", choices=AUSGABEN, required=True)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    Edition.checkout_state(ROOT, args.expected_commit)
    tag = args.tag
    scope = {"tag": tag, "version": tag.rsplit("-v", 1)[-1], "title": AUSGABEN[tag]}
    with TemporaryDirectory() as temporary:
        dist = Path(temporary)
        stage(tag, dist, ROOT)
        if args.publish:
            existing = PUBLISHER.P.companion_release(REPOSITORY, tag)
            if existing and not existing["isDraft"]:
                if PUBLISHER.P.tag_commit(REPOSITORY, tag) != args.expected_commit:
                    raise ValueError("Der veröffentlichte Tag gehört zu einem anderen Commit.")
                Edition.verify_download(dist, scope, ROOT, REPOSITORY, args.expected_commit)
            else:
                PUBLISHER.publish(dist, scope, args.expected_commit, REPOSITORY, builder=Edition)
        print(f"{tag}: {len(hashes(dist))} Dateien einschließlich SHA-256-Liste geprüft.")


if __name__ == "__main__":
    main()

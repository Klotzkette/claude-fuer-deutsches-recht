#!/usr/bin/env python3
"""Baut die lokalen Release-Dateien; veroeffentlicht nichts im Netz."""

import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

from public_release import COMPONENT, PROMPT_SUFFIXES, RELEASE_TAG, ROOT
from reproducible_zip import tree_members, write_archive


def run(script: str, *args: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", nargs="?", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output == ROOT or ROOT.is_relative_to(output):
        parser.error("Ausgabe muss ein separates Build-Verzeichnis sein")
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        parser.error("Ausgabe muss leer sein; fuer jeden Build ein frisches Verzeichnis verwenden")

    run("sync-public-entrypoints.py", "--check")
    run("validate-public-integration.py")
    for script in ("build-plugin-release-zips.py", "build-testakten-release-zips.py", "build-skills-markdown-bundles.py"):
        run(script, str(output))

    for role in PROMPT_SUFFIXES:
        shutil.copyfile(ROOT / "unified-mini-prompts" / f"{role}.md", output / f"{role}-unified-mini-prompt.md")
    for pattern in ("vergaberecht-arbeitsprompt-*.md", "vergaberecht-kurzprompt-*.md"):
        for prompt in ROOT.glob(pattern):
            shutil.copyfile(prompt, output / prompt.name)
    write_archive(output / "alle-plugins-megazip.zip", [
        (output / f"{role}.zip", f"{role}.zip") for role in PROMPT_SUFFIXES
    ])

    members = [(ROOT / "testakten/README.txt", "README.txt")]
    # Die vollstaendige Quellkopie ist vom bereinigten Arbeits-ZIP getrennt.
    source_members = tree_members(ROOT, exclude=lambda p: (
        p.parts[0] in {"dist", ".git", ".venv"} or "__pycache__" in p.parts
        or p.suffix == ".pyc" or p.name == ".DS_Store"
        or (ROOT / p).is_relative_to(output)
    ))
    members += [(path, f"{COMPONENT}/{name}") for path, name in source_members]
    write_archive(output / "alles-komplettpaket.zip", members)

    checksums = []
    for path in sorted(output.iterdir()):
        if path.is_file():
            with path.open("rb") as handle:
                digest = hashlib.file_digest(handle, "sha256").hexdigest()
            checksums.append(f"{digest}  {path.name}\n")
    (output / "checksums-sha256.txt").write_text("".join(checksums), encoding="utf-8")
    run("validate-release-zips.py", str(output))
    run("validate-testakten-release-zips.py", str(output))
    print(f"{RELEASE_TAG}: {len(checksums) + 1} Dateien in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

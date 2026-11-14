#!/usr/bin/env python3
"""Baut und verifiziert das eigenständige Insolvenzrecht-Hauptplugin."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

from prompt_profiles import PROMPT_SUFFIXES
from release_routing import validate_plugin_version

ROOT = Path(__file__).resolve().parents[1]
NAME = "insolvenzrecht"
PLUGIN = ROOT / NAME
PROMPTS = tuple(f"{NAME}-{kind}.md" for kind in ("werkstatt", "schnellstart", "hauptproblem"))
INVENTORY = "quellenabgleich.json"
CHECKSUMS = "checksums-sha256.txt"
PAYLOAD = frozenset((f"{NAME}.zip", *PROMPTS, INVENTORY))
ASSETS = PAYLOAD | {CHECKSUMS}
REPOSITORY = "Klotzkette/claude-fuer-deutsches-recht"
FACHMODULE_SPEC = importlib.util.spec_from_file_location(
    "insolvenzrecht_fachmodule", ROOT / "scripts/build-insolvenzrecht-fachmodule.py")
FACHMODULE = importlib.util.module_from_spec(FACHMODULE_SPEC)
FACHMODULE_SPEC.loader.exec_module(FACHMODULE)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def version() -> str:
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entry = next(p for p in marketplace["plugins"] if p["name"] == NAME)
    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    if entry["version"] != manifest["version"]:
        raise ValueError("Marketplace und Pluginversion weichen ab.")
    validate_plugin_version(entry, marketplace["version"], root=ROOT)
    return manifest["version"]


def sources() -> dict[str, Path]:
    result = {}
    for path in sorted(PLUGIN.rglob("*")):
        relative = path.relative_to(PLUGIN)
        if {"__pycache__", ".git", ".venv", "testakten", "testakte"}.intersection(relative.parts):
            continue
        if path.name in {".DS_Store", "CLAUDE.md"} or path.suffix == ".pyc" or path.name.endswith(PROMPT_SUFFIXES):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink im Paket: {path}")
        if path.is_file():
            result[relative.as_posix()] = path
    for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if name not in result and (ROOT / name).is_file():
            result[name] = ROOT / name
    return result


def source_inventory(files: dict[str, Path]) -> dict:
    return {
        "schema_version": 1,
        "plugin": NAME,
        "version": version(),
        "tag": f"{NAME}-v{version()}",
        "files": {name: {"sha256": digest(path.read_bytes()), "bytes": path.stat().st_size}
                  for name, path in sorted(files.items())},
        "prompts": {name: digest((PLUGIN / name).read_bytes()) for name in PROMPTS},
    }


def verify(destination: Path) -> None:
    if not destination.is_dir() or {p.name for p in destination.iterdir()} != ASSETS:
        raise ValueError("Release muss genau sechs Dateien enthalten.")
    for name in ASSETS:
        if not (destination / name).is_file() or (destination / name).is_symlink():
            raise ValueError(f"Ungültige Releasedatei: {name}")
    recorded = {}
    for line in (destination / CHECKSUMS).read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match or match[2] not in PAYLOAD or match[2] in recorded:
            raise ValueError("Ungültiges Prüfsummenverzeichnis.")
        recorded[match[2]] = match[1]
    if set(recorded) != PAYLOAD:
        raise ValueError("Unvollständiges Prüfsummenverzeichnis.")
    for name, expected in recorded.items():
        if digest((destination / name).read_bytes()) != expected:
            raise ValueError(f"Prüfsumme weicht ab: {name}")
    # Auch außerhalb der CI dürfen veraltete Importe nicht neu gehasht und
    # damit scheinbar gültig gebaut werden. Ein Abgleich pro Releaseprüfung.
    import_errors = FACHMODULE.check_tree(
        PLUGIN / "references/fachmodule", FACHMODULE.generate(root=ROOT))
    if import_errors:
        raise ValueError("Fachmodule weichen von den Originalquellen ab:\n" + "\n".join(import_errors[:30]))
    files = sources()
    if json.loads((destination / INVENTORY).read_text()) != source_inventory(files):
        raise ValueError("Quelleninventar weicht vom Checkout ab.")
    for name in PROMPTS:
        if (destination / name).read_bytes() != (PLUGIN / name).read_bytes():
            raise ValueError(f"Prompt weicht ab: {name}")
    with zipfile.ZipFile(destination / f"{NAME}.zip") as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(files):
            raise ValueError("ZIP-Dateiliste weicht von den Paketquellen ab.")
        for name, path in files.items():
            if archive.read(name) != path.read_bytes():
                raise ValueError(f"ZIP-Datei weicht ab: {name}")
        if "references/fachmodule/INDEX.md" not in files:
            raise ValueError("Lokale Fachmodule fehlen.")
    spec = importlib.util.spec_from_file_location("zip_check", ROOT / "scripts/validate-release-zips.py")
    checks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checks)
    checks.validate_plugin_zip(destination, NAME, version())
    checks.validate_skill_sources(destination / f"{NAME}.zip", PLUGIN)
    checks.validate_focus_skill(destination / f"{NAME}.zip", PLUGIN, ROOT / "quality/evals/insolvenzrecht.json")
    print(f"Verifiziert: {len(ASSETS)} Releasedateien, {len(files)} paketlokale Dateien.")


def build(destination: Path) -> None:
    if destination.is_relative_to(PLUGIN.resolve()):
        raise ValueError("Ausgabeziel muss außerhalb des Plugins liegen.")
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Ausgabeziel muss leer sein; kein Überschreiben.")
    files = sources()
    with zipfile.ZipFile(destination / f"{NAME}.zip", "x", zipfile.ZIP_DEFLATED) as archive:
        for name, path in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 11, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    for name in PROMPTS:
        shutil.copyfile(PLUGIN / name, destination / name)
    (destination / INVENTORY).write_text(json.dumps(source_inventory(files), ensure_ascii=False, indent=2) + "\n")
    (destination / CHECKSUMS).write_text("".join(
        f"{digest((destination / name).read_bytes())}  {name}\n" for name in sorted(PAYLOAD)))
    verify(destination)


def verify_remote_tag(tag: str) -> None:
    """Binde die verifizierten Assets an genau den geprüften Git-Commit."""
    expected = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    def remote_object(endpoint: str) -> dict:
        return json.loads(subprocess.check_output(
            ["gh", "api", f"repos/{REPOSITORY}/{endpoint}", "--jq", ".object"],
            cwd=ROOT, text=True))
    actual = remote_object(f"git/ref/tags/{tag}")
    visited = set()
    while actual.get("type") == "tag":
        if actual["sha"] in visited:
            raise ValueError(f"Zyklische Tagreferenz: {tag}")
        visited.add(actual["sha"])
        actual = remote_object(f"git/tags/{actual['sha']}")
    if actual.get("type") != "commit" or actual.get("sha") != expected:
        raise ValueError(f"Release-Tag zeigt nicht auf den geprüften Checkout: {tag}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="Vorhandenes Release nur prüfen")
    parser.add_argument("--verify-release", metavar="TAG", help="Auch alle GitHub-Downloads vergleichen")
    args = parser.parse_args()
    destination = args.dist.resolve()
    if args.check or args.verify_release:
        verify(destination)
    else:
        build(destination)
    if args.verify_release:
        if args.verify_release != f"{NAME}-v{version()}":
            raise ValueError("Tag stimmt nicht mit der Paketversion überein.")
        verify_remote_tag(args.verify_release)
        with tempfile.TemporaryDirectory(prefix="insolvenzrecht-download-") as temp:
            subprocess.run(["gh", "release", "download", args.verify_release, "--repo", REPOSITORY, "--dir", temp], check=True)
            downloaded = Path(temp)
            verify(downloaded)
            for name in sorted(ASSETS):
                if (downloaded / name).read_bytes() != (destination / name).read_bytes():
                    raise ValueError(f"Download weicht ab: {name}")
            verify_remote_tag(args.verify_release)
            print("Alle sechs GitHub-Downloads byteidentisch zum geprüften lokalen Release.")


if __name__ == "__main__":
    main()

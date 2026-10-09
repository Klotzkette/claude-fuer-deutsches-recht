#!/usr/bin/env python3
"""Begrenztes Reparaturrelease mit reproduzierbaren Paketen und Quellenabgleich."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import zipfile

from prompt_profiles import PROMPT_SUFFIXES
from release_routing import scoped_asset_url, validate_plugin_version

ROOT = Path(__file__).resolve().parents[1]
VERSION = "445.35.1"
TAG = f"kompatibilitaet-v{VERSION}"
PLUGINS = (
    "bauvergabe-bieter", "bauvergabe-rechtsschutz", "bauvergabe-unterlagen",
    "bauvergabe-verfahren", "bieter-unternehmen", "grundstuecksrecherche",
    "rechtsabteilung-forderungsmanagement-immobilienunternehmen",
    "schriftsatzwerkstatt-bea", "vergabestelle-behoerden",
)
WEBSITE = "grundstuecksrecherche-website.zip"
SKIP_PARTS = {"__pycache__", ".git", ".venv", "node_modules", "testakte", "testakten"}

spec = importlib.util.spec_from_file_location("release_checks", ROOT / "scripts/validate-release-zips.py")
CHECKS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECKS)


def packaged(name: str) -> bool:
    path = Path(name)
    return (not SKIP_PARTS.intersection(path.parts) and name != "CLAUDE.md"
            and path.name != ".DS_Store" and path.suffix != ".pyc"
            and not path.name.endswith(PROMPT_SUFFIXES))


def sources(root: Path, directory: Path) -> dict[str, Path]:
    listing = subprocess.check_output(
        ["git", "ls-files", "-z", "--", directory.relative_to(root).as_posix()], cwd=root, timeout=30)
    result = {}
    for relative in listing.decode("utf-8").split("\0"):
        if not relative:
            continue
        path = root / relative
        name = path.relative_to(directory).as_posix()
        if not packaged(name):
            continue
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(directory.resolve()):
            raise ValueError(f"Keine reguläre Quelldatei: {relative}")
        result[name] = path
    for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if name not in result:
            for parent in directory.parents:
                if not parent.is_relative_to(root.resolve()):
                    break
                candidate = parent / name
                if candidate.is_file() and not candidate.is_symlink():
                    result[name] = candidate
                    break
    if ".claude-plugin/plugin.json" not in result or not any(n.endswith("/SKILL.md") for n in result):
        raise ValueError(f"Manifest oder Skills fehlen: {directory}")
    return result


def write_zip(target: Path, files: dict[str, Path]) -> None:
    with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, path in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def verify_zip(target: Path, files: dict[str, Path]) -> dict[str, str]:
    with zipfile.ZipFile(target) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(files):
            raise ValueError(f"Paketdateiliste weicht ab: {target.name}")
        hashes = {}
        for name, path in sorted(files.items()):
            data = archive.read(name)
            if data != path.read_bytes():
                raise ValueError(f"Paketinhalt weicht ab: {target.name}/{name}")
            hashes[name] = hashlib.sha256(data).hexdigest()
        return hashes


def build(dist: Path, root: Path = ROOT) -> None:
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Paketverzeichnis muss leer sein; keine vorhandenen Artefakte überschreiben.")
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    entries = {p["name"]: p for p in market["plugins"]}
    report = {"schema_version": 1, "tag": TAG, "version": VERSION,
              "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True, timeout=30).strip(),
              "plugins": {}}
    for name in PLUGINS:
        entry = entries[name]
        if entry["version"] != VERSION:
            raise ValueError(f"Unerwartete Paketversion: {name}")
        validate_plugin_version(entry, market["version"], root=root)
        if not (scoped_asset_url(f"{name}.zip", root=root) or "").endswith(f"/{TAG}/{name}.zip"):
            raise ValueError(f"Paketroute fehlt: {name}")
        directory = (root / entry["source"]).resolve()
        if not directory.is_relative_to(root.resolve()):
            raise ValueError(f"Pluginquelle außerhalb des Repositorys: {name}")
        files = sources(root, directory)
        target = dist / f"{name}.zip"
        write_zip(target, files)
        CHECKS.validate_plugin_zip(dist, name, VERSION)
        CHECKS.validate_skill_sources(target, directory)
        CHECKS.validate_focus_skill(target, directory, root / "quality/evals" / f"{name}.json")
        report["plugins"][name] = {"source": entry["source"], "files": verify_zip(target, files)}
    if not (scoped_asset_url(WEBSITE, root=root) or "").endswith(f"/{TAG}/{WEBSITE}"):
        raise ValueError("Website-Route fehlt")
    subprocess.run([sys.executable, str(root / "grundstuecksrecherche/app/portable.py"), str(dist / WEBSITE)],
                   check=True, timeout=120)
    with zipfile.ZipFile(dist / WEBSITE) as archive:
        if "index.html" not in archive.namelist():
            raise ValueError("Website-Einstieg fehlt")
        bundle = archive.read("portable-bundle.js").decode("utf-8")
        data = json.loads(bundle.removeprefix("window.PORTABLE_BUNDLE=").strip().removesuffix(";"))
        if data["case"] is not None:
            raise ValueError("Website darf keine Vorgangsdaten ausliefern")
    (dist / "quellenabgleich.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checksums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in sorted(dist.iterdir()))
    (dist / "checksums-sha256.txt").write_text(checksums, encoding="utf-8")
    print(f"{TAG}: {len(PLUGINS)} Plugin-ZIPs, Website-ZIP und zwei Prüfnachweise erstellt.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    args = parser.parse_args()
    build(args.dist.resolve())

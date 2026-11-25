#!/usr/bin/env python3
"""Baut die beiden zusammengeführten Fachplugins und prüft jedes Archivmitglied gegen seinen Quelltext."""
import argparse
import importlib
import io
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

from package_readme import render_readme

ROOT = Path(__file__).resolve().parents[1]
TAG = "insolvenz-fachbereich-v445.36.10"
VERSION = "445.36.10"
PLUGINS = ("fachanwalt-insolvenz-sanierungsrecht", "insolvenzforderungen-checker")
builder = importlib.import_module("build-skill-quality-release")


def package(plugin, root=ROOT, *, portable=False):
    directory = root / plugin
    files = builder.source_files(root, directory)
    builder.check_manifests(files, plugin, VERSION)
    builder.verify_reachability(files)
    prefix = plugin + "/" if portable else ""
    archive = io.BytesIO()
    with ZipFile(archive, "w") as output:
        for name, source in sorted(files.items()):
            data = (render_readme(root, directory, files, None, name=name, release_tag=TAG)
                    if source.name == "README.md" else source.read_bytes())
            info = ZipInfo(prefix + name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            mode = 0o755 if source.stat().st_mode & 0o111 else 0o644
            info.external_attr = (0o100000 | mode) << 16
            info.compress_type = ZIP_STORED
            output.writestr(info, data)
    return archive.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    parser.add_argument("--verify", action="store_true", help="Vorhandene Pakete bytegenau mit dem Neubau vergleichen")
    parser.add_argument("--portable", action="store_true", help="Portable ZIPs mit umschließendem Pluginordner bearbeiten")
    args = parser.parse_args()
    if not args.verify:
        args.dist.mkdir(parents=True, exist_ok=True)
    for plugin in PLUGINS:
        data = package(plugin, portable=args.portable)
        suffix = "-portable" if args.portable else ""
        target = args.dist / f"{plugin}{suffix}.zip"
        if args.verify:
            if not target.is_file() or target.read_bytes() != data:
                raise SystemExit(f"Fachpaket weicht vom Quellenstand ab: {target}")
        else:
            target.write_bytes(data)
        print(plugin, len(data), "Bytes")


if __name__ == "__main__":
    main()

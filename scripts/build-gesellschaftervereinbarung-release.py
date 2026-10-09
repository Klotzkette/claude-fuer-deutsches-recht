#!/usr/bin/env python3
"""Baut und kontrolliert das abgegrenzte Beteiligungsvertrags-Release."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import zipfile
from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
NAME = "gesellschaftervereinbarung"
CASE = "gesellschaftervereinbarung-drohnenfriseur-berlin"
PROMPTS = [
    f"{NAME}-{kind}.md" for kind in ("werkstatt", "schnellstart", "hauptproblem")
]
DOCS = [
    "01_Term_Sheet_SkyFade.docx",
    "02_Gesellschaftervereinbarung_Ausfuellfassung.docx",
]


def module(filename):
    spec = importlib.util.spec_from_file_location(
        filename.replace("-", "_"), ROOT / "scripts" / filename
    )
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    dist.mkdir(parents=True, exist_ok=True)
    plugin = ROOT / NAME
    manifests = [
        json.loads((plugin / p).read_text())
        for p in (
            "plugin.json",
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
        )
    ]
    if (
        len({(m["name"], m["version"], m["description"]) for m in manifests}) != 1
        or manifests[0]["version"] != "1.1.0"
    ):
        raise ValueError("Manifeste stimmen nicht überein")
    if len(list((plugin / "skills").glob("*/SKILL.md"))) != 11:
        raise ValueError("Elf Skills erforderlich")
    for name in PROMPTS[1:]:
        data = (plugin / name).read_bytes()
        if len(data) > 7500 or len(data.decode()) > 7500:
            raise ValueError("Kompaktprompt überschreitet die Grenze")
    sources = [
        p for p in sorted(plugin.rglob("*")) if p.is_file() and p.name not in PROMPTS
    ]
    if any(
        p.is_symlink() or "__pycache__" in p.parts or p.suffix == ".pyc"
        for p in sources
    ):
        raise ValueError("Unerwartete Paketdatei")
    for portable in (False, True):
        prefix = f"{NAME}/" if portable else ""
        target = dist / f"{NAME}{'-portable' if portable else ''}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            for source in sources + [ROOT / "LICENSE"]:
                relative = (
                    source.relative_to(plugin).as_posix()
                    if source != ROOT / "LICENSE"
                    else "LICENSE"
                )
                info = zipfile.ZipInfo(prefix + relative, (2026, 10, 9, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, source.read_bytes())
        with zipfile.ZipFile(target) as z:
            for source in sources:
                if (
                    z.read(prefix + source.relative_to(plugin).as_posix())
                    != source.read_bytes()
                ):
                    raise ValueError("Paketinhalt weicht ab")
    for name in PROMPTS:
        shutil.copyfile(plugin / name, dist / name)
    directory = ROOT / "testakten" / CASE
    module("build-testakten-release-zips.py").build_single(directory, dist)
    module("build-testakten-einzelpdf-zips.py").build_single(directory, dist)
    shutil.copyfile(
        directory / "gesamt-pdf" / f"{CASE}_gesamt.pdf", dist / f"{CASE}_gesamt.pdf"
    )
    for name in DOCS:
        shutil.copyfile(directory / name, dist / name)
    for source in dist.glob("*.zip"):
        with zipfile.ZipFile(source) as z:
            if z.testzip():
                raise ValueError("ZIP beschädigt")
            if source.name.startswith("testakte-"):
                if any(
                    "/" in name or name.lower().endswith(".md") for name in z.namelist()
                ):
                    raise ValueError("Akten-ZIP ist nicht flach oder enthält Markdown")
                if not z.read("README.txt").startswith(NOTICE_BYTES):
                    raise ValueError("Warnhinweis fehlt")
    names = sorted(p.name for p in dist.iterdir())
    if len(names) != 10:
        raise ValueError(f"Unerwarteter Assetumfang: {names}")
    (dist / "checksums-sha256.txt").write_text(
        "".join(
            f"{hashlib.sha256((dist/name).read_bytes()).hexdigest()}  {name}\n"
            for name in names
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {"version": "1.1.0", "assets": len(names) + 1, "destination": str(dist)}
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    build(parser.parse_args().dist)

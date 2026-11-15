#!/usr/bin/env python3
"""Reproduzierbare native bAV-Konzernakten aus getrennten Falldaten.

Office-Binärdateien erstellt der gebündelte Artifact-Tool-Runtime.
Alle Pfade können für einen isolierten Kontrollbuild umgeleitet werden.
Die Gesamt-PDF-/Release-ZIP-Builder bleiben die zentralen Repository-Werkzeuge.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile
import io
import re
import uuid
import xml.etree.ElementTree as ET

from bav_konzern_render import (register_fonts, safe_path, pdf, docx, text_file,
                                csv_file, screenshot, email_file)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/bav-konzern-faelle"
RUNTIME = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies"


def source_cases(slugs=()):
    cases = [json.loads(p.read_text()) for p in sorted(DATA.glob("*.json"))]
    return [c for c in cases if not slugs or c["slug"] in slugs]


def stable_office_container(path):
    """Verpackungszeitstempel ändern keine Fachdatei und keine MIME-Anlage."""
    source = io.BytesIO(path.read_bytes())
    target = io.BytesIO()
    with zipfile.ZipFile(source) as old, zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as new:
        identities = {}
        for name in sorted(old.namelist()):
            if name.endswith(".rels"):
                tree = ET.fromstring(old.read(name))
                for relation in tree:
                    identifier = relation.get("Id", "")
                    if re.fullmatch(r"R[0-9a-f]{16}", identifier):
                        key = name + "|" + relation.get("Type", "") + "|" + relation.get("Target", "")
                        identities[identifier] = "rId" + hashlib.sha256(key.encode()).hexdigest()[:16]
            if name.endswith(".xml"):
                text = old.read(name).decode("utf-8")
                for index, identifier in enumerate(re.findall(r'<a16:creationId id="(\{[^}]+\})"', text)):
                    identities[identifier] = "{" + str(uuid.uuid5(uuid.NAMESPACE_URL, path.name + "/" + name + "/" + str(index))).upper() + "}"
        for name in sorted(old.namelist()):
            data = old.read(name)
            if name.endswith((".xml", ".rels")):
                text = data.decode("utf-8")
                for original, stable in identities.items():
                    text = text.replace('"' + original + '"', '"' + stable + '"')
                stable_slide_id = str(int(hashlib.sha256((path.name + name).encode()).hexdigest()[:8], 16))
                text = re.sub(r'(<p14:creationId val=")\d+("[^>]*>)', lambda m: m[1] + stable_slide_id + m[2], text)
                data = text.encode("utf-8")
            if name == "docProps/core.xml":
                text = data.decode("utf-8")
                text = re.sub(r"(<dcterms:(?:created|modified)\b[^>]*>)[^<]*(</dcterms:(?:created|modified)>)", r"\g<1>2026-11-15T00:00:00Z\g<2>", text)
                data = text.encode("utf-8")
            info = zipfile.ZipInfo(name, (2026, 11, 15, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            new.writestr(info, data)
    path.write_bytes(target.getvalue())


def historical_archive(case_dir, destination):
    """Einmaliger byteidentischer Auditbestand vor Ablösung des Altmandats."""
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / (case_dir.name + "-vor-2026-11-15.zip")
    if archive.exists():
        return
    files = sorted(p for p in case_dir.rglob("*") if p.is_file())
    if not files:
        return
    records = []
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as out:
        for p in files:
            data = p.read_bytes()
            relative = p.relative_to(case_dir).as_posix()
            zi = zipfile.ZipInfo(relative, (2026, 11, 15, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            out.writestr(zi, data)
            records.append({"path": relative, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    archive.with_suffix(".json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*")
    parser.add_argument("--output", type=Path, default=ROOT / "testakten")
    parser.add_argument("--qa", type=Path, default=ROOT.parent / "tmp/bav-konzern-2026-11-15/qa")
    parser.add_argument("--archive-old", action="store_true")
    parser.add_argument("--skip-office", action="store_true", help="Nur für gezielte PDF-/Textkorrektur; kein vollständiger Build")
    args = parser.parse_args()
    cases = source_cases(args.slugs)
    if not cases:
        raise SystemExit("Keine Falldaten gefunden")
    register_fonts(Path(os.environ.get("BAV_FONT_DIR", "/System/Library/Fonts/Supplemental")))
    args.output.mkdir(parents=True, exist_ok=True)
    args.qa.mkdir(parents=True, exist_ok=True)
    for case in cases:
        base = args.output / case["slug"]
        if args.archive_old and case["slug"] == "bav-strategie-konzern-meissner-rheinwerk-ag":
            historical_archive(base, ROOT / "quality/bav-konzern-2026-11-15/historischer-bestand")
        base.mkdir(parents=True, exist_ok=True)
        for item in case.get("documents", []):
            path = safe_path(base, item["path"])
            function = {".pdf": pdf, ".docx": docx, ".txt": text_file, ".csv": csv_file, ".png": screenshot}.get(path.suffix.lower())
            if function:
                function(path, item, case)
            elif path.suffix.lower() != ".eml":
                raise ValueError(f"Unbekanntes Dokumentformat {path}")
    if not args.skip_office:
        with tempfile.TemporaryDirectory(prefix="bav-artifacts-") as temp:
            temp = Path(temp)
            (temp / "node_modules").symlink_to(RUNTIME / "node/node_modules", target_is_directory=True)
            script = temp / "build.mjs"
            shutil.copyfile(ROOT / "scripts/bav_konzern_office.mjs", script)
            fixture = temp / "cases.json"
            fixture.write_text(json.dumps(cases, ensure_ascii=False))
            env = dict(os.environ, RUNTIME_NODE_MODULES=str(RUNTIME / "node/node_modules"),
                       RUNTIME_NODE=str(RUNTIME / "node/bin/node"))
            subprocess.run([str(RUNTIME / "node/bin/node"), str(script), str(fixture), str(args.output.resolve()), str(args.qa.resolve())], check=True, env=env)
    inventory = []
    for case in cases:
        base = args.output / case["slug"]
        for group in ("documents", "workbooks", "slides"):
            for item in case.get(group, []):
                path = base / item["path"]
                if path.suffix.lower() in {".docx", ".xlsx", ".pptx"}:
                    stable_office_container(path)
        for item in case.get("documents", []):
            if Path(item["path"]).suffix.lower() == ".eml":
                email_file(safe_path(base, item["path"]), item, case, base)
        paths = [x["path"] for group in ("documents", "workbooks", "slides") for x in case.get(group, [])]
        records = [{"path": r, "bytes": (base / r).stat().st_size,
                    "sha256": hashlib.sha256((base / r).read_bytes()).hexdigest()} for r in sorted(paths)]
        inventory.append({"slug": case["slug"], "native_documents": len(records), "files": records})
        print(f"{case['slug']}: {len(records)} native Aktenstücke")
    (args.qa / "native-inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()

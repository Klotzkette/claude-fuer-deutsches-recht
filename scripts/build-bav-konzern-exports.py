#!/usr/bin/env python3
"""Lokaler qualifizierter Satz: zentrale Konverter, gebundene Einzel-/Gesamt-PDFs.

Nur nach nativer Erzeugung ausführen. Der Release nutzt anschließend unveränderte
Quellen. Das Inventar wird hier aus tatsächlichen Bytes erzeugt, nicht redigiert.
"""
from __future__ import annotations
import argparse
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import zipfile

from pypdf import PdfReader, PdfWriter
from bav_konzern_verify import GENERATOR_PATHS, INVENTORY, pdf_facts, sha
from bav_konzern_render import register_fonts, workbook_pdf
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import render_office_batch, normalize_pdf
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies"
DOCX_SKILL = Path.home() / ".codex/plugins/cache/openai-primary-runtime/documents/26.1111.10934/skills/documents"


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S = load("build-testakten-einzelpdf-zips.py")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*")
    parser.add_argument("--qa", type=Path, default=ROOT.parent / "tmp/bav-konzern-2026-11-15/qa")
    parser.add_argument("--reuse", action="store_true", help="Nur unveränderte Sourcehash-geprüfte Office-Satzstände wiederverwenden")
    args = parser.parse_args()
    register_fonts(Path(os.environ.get("BAV_FONT_DIR", "/System/Library/Fonts/Supplemental")))
    os.environ["SOFFICE"] = str(RUNTIME / "bin/override/soffice")
    os.environ["TMPDIR"] = "/private/tmp" if Path("/private/tmp").is_dir() else "/tmp"
    destination = ROOT / "bav-strategie-konzern/testakten/downloads"
    destination.mkdir(parents=True, exist_ok=True)
    inventory_path = ROOT / INVENTORY
    previous = json.loads(inventory_path.read_text()) if inventory_path.exists() else {"cases": []}
    cases = {c["slug"]: c for c in previous["cases"]}
    for fixture_path in sorted((ROOT / "scripts/data/bav-konzern-faelle").glob("*.json")):
        fixture = json.loads(fixture_path.read_text())
        slug = fixture["slug"]
        if args.slugs and slug not in args.slugs:
            continue
        directory = ROOT / "testakten" / slug
        qa = args.qa.resolve() / slug / "pdf-render"
        qa.mkdir(parents=True, exist_ok=True)
        pairs = document_arcname_pairs(directory)
        cache = {}
        for source, name in pairs:
            if source.suffix.lower() != ".docx":
                continue
            out = qa / (source.stem + "-word")
            receipt = out / "source-sha256.txt"
            rendered = out / (source.stem + ".pdf")
            digest = sha(source.read_bytes())
            if not (args.reuse and receipt.exists() and receipt.read_text() == digest and rendered.exists()):
                subprocess.run([str(RUNTIME / "python/bin/python3"), str(DOCX_SKILL / "render_docx.py"), str(source),
                                "--output_dir", str(out), "--emit_pdf"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                receipt.write_text(digest)
            cache[source] = normalize_pdf(rendered.read_bytes(), source.name)
        cache.update(render_office_batch([p for p, _ in pairs if p.suffix.lower() == ".pptx"]))
        cache.update({p: workbook_pdf(p) for p, _ in pairs if p.suffix.lower() == ".xlsx"})
        for source, _ in pairs:
            if source.suffix.lower() in {".docx", ".xlsx", ".pptx"} and source not in cache:
                raise RuntimeError(f"Native Office-Lesefassung fehlt: {source}")
        archive_path = destination / f"testakte-{slug}-einzelpdfs.zip"
        combined = PdfWriter()
        members = []
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
            S.write_pdf(archive, NOTICE_FILENAME, NOTICE_BYTES)
            for source, name in pairs:
                data = S.render_document_pdf(source, directory, cache)
                S.write_pdf(archive, name, data)
                members.append({"path": name, **pdf_facts(data)})
                target = qa / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                combined.append(PdfReader(io.BytesIO(data)), outline_item=name, import_outline=False)
        combined.add_metadata({"/Title": fixture["title"], "/Author": fixture["client"], "/CreationDate": "D:20261115000000Z"})
        total_path = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        total_path.parent.mkdir(parents=True, exist_ok=True)
        with total_path.open("wb") as stream:
            combined.write(stream)
        cases[slug] = {"slug": slug, "fixture": {"path": str(fixture_path.relative_to(ROOT)), "sha256": sha(fixture_path.read_bytes())},
                       "sources": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p.read_bytes())} for p, _ in working_dump_archive_pairs(directory, include_gesamt_pdf=False)],
                       "pdf_zip": {"path": str(archive_path.relative_to(ROOT)), "sha256": sha(archive_path.read_bytes()), "members": members},
                       "gesamt_pdf": {"path": str(total_path.relative_to(ROOT)), **pdf_facts(total_path.read_bytes())}}
        print(f"{slug}: {len(members)} Einzel-PDFs, {len(combined.pages)} Seiten")
    inventory = {"schema_version": 1, "generators": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in GENERATOR_PATHS], "cases": list(cases.values())}
    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

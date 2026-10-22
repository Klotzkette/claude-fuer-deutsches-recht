#!/usr/bin/env python3
"""Baut das Komponentenrelease für den Insolvenzbericht-Ersteller 1.0.0."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import zipfile

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate

from prompt_profiles import PROMPT_SUFFIXES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import office_binary, valid_office_container


ROOT = Path(__file__).resolve().parents[1]
NAME = "insolvenzverwaltung-berichtsersteller"
VERSION = "1.0.0"
TAG = f"{NAME}-v{VERSION}"
KINDS = ("werkstatt", "schnellstart")
CASES = (
    "insolvenzverwaltung-mainbogen-laborsoftware-wuerzburg",
    "insolvenzverwaltung-nordlicht-handels-kiel",
    "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren",
)


def module(filename: str):
    path = ROOT / "scripts" / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    result = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(result)
    return result


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def asset_names() -> set[str]:
    names = {f"{NAME}.zip", f"{NAME}-portable.zip", "checksums-sha256.txt", "quellenabgleich.json"}
    names.update(f"{NAME}-{kind}.{suffix}" for kind in KINDS for suffix in ("md", "txt", "pdf"))
    for case in CASES:
        names.update((f"testakte-{case}.zip", f"testakte-{case}-einzelpdfs.zip", f"{case}_gesamt.pdf"))
    return names


def plugin_sources() -> list[Path]:
    plugin = ROOT / NAME
    result = []
    for path in sorted(plugin.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symbolischer Link nicht zulässig: {path}")
        if not path.is_file():
            continue
        if path.name in {".DS_Store", "CLAUDE.md"} or path.suffix == ".pyc" or "__pycache__" in path.parts:
            continue
        if path.name.endswith(PROMPT_SUFFIXES):
            continue
        if path.suffix.lower() in {".pdf", ".docx", ".xlsx", ".eml"} or "testakten" in path.parts:
            raise ValueError(f"Akteninhalt gehört nicht ins Plugin-ZIP: {path}")
        result.append(path)
    return result


def register_fonts():
    candidates = (
        (Path("/System/Library/Fonts/Supplemental"), ("Times New Roman.ttf", "Times New Roman Bold.ttf"), "Times New Roman"),
        (Path("/usr/share/fonts/truetype/liberation2"), ("LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf"), "Liberation Serif (Ersatz für Times New Roman)"),
    )
    for directory, files, label in candidates:
        if all((directory / file).is_file() for file in files):
            for name, file in zip(("BER-Regular", "BER-Bold"), files):
                pdfmetrics.registerFont(TTFont(name, str(directory / file)))
            pdfmetrics.registerFontFamily("BER-Regular", normal="BER-Regular", bold="BER-Bold", italic="BER-Regular", boldItalic="BER-Bold")
            return label
    raise RuntimeError("Times New Roman oder Liberation Serif fehlt")


def render_prompt(source: Path, target: Path) -> dict:
    render = module("build-testakte-gesamt-pdf.py")
    font_label = register_fonts()
    render.FONT_REG, render.FONT_BOLD = "BER-Regular", "BER-Bold"
    for style in (render.s_body, render.s_meta):
        style.fontName, style.fontSize, style.leading = "BER-Regular", 11, 14.3
    for style in (render.s_h1, render.s_h2, render.s_h3):
        style.fontName = "BER-Bold"
        style.keepWithNext = True
    markdown = re.sub(r"\[([^\]]+)\]\((https?://[^ )]+)\)", r"\1 (\2)", source.read_text(encoding="utf-8"))
    flow = render.md_to_flowables(markdown)

    def footer(canvas, document):
        canvas.setFont("BER-Regular", 8)
        canvas.drawString(50, 27, f"Insolvenzverwaltung Zwischen- und Schlussbericht-Ersteller {VERSION} | {font_label} 11 pt")
        canvas.drawRightString(A4[0] - 50, 27, str(document.page))

    doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=48, bottomMargin=50, invariant=1, title=source.stem, author="Klotzkette", subject=f"{font_label} 11 pt")
    doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    pages = len(PdfReader(target).pages)
    if not pages:
        raise ValueError(f"Leere Prompt-Lesefassung: {source}")
    return {"source": source.relative_to(ROOT).as_posix(), "source_sha256": sha(source), "pdf_sha256": sha(target), "pages": pages, "font": font_label}


def write_zip(target: Path, portable: bool) -> None:
    plugin = ROOT / NAME
    sources = plugin_sources()
    prefix = f"{NAME}/" if portable else ""
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as archive:
        for source in [*sources, ROOT / "LICENSE"]:
            relative = source.relative_to(plugin).as_posix() if source != ROOT / "LICENSE" else "LICENSE"
            info = zipfile.ZipInfo(prefix + relative, (2026, 10, 22, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())


def build(destination: Path) -> dict:
    if not office_binary():
        raise RuntimeError("LibreOffice fehlt; Office-Unterlagen dürfen nicht nur textuell exportiert werden.")
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein.")
    plugin = ROOT / NAME
    manifests = [json.loads((plugin / relative).read_text()) for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    if {(m["name"], m["version"]) for m in manifests} != {(NAME, VERSION)}:
        raise ValueError("Manifeststände stimmen nicht überein.")
    if len(list((plugin / "skills").glob("*/SKILL.md"))) != 11:
        raise ValueError("Genau zehn Fachskills und ein Hauptskill erforderlich.")

    report = {"schema_version": 1, "plugin": NAME, "version": VERSION, "tag": TAG, "prompts": {}, "cases": {}}
    for kind in KINDS:
        source = plugin / f"{NAME}-{kind}.md"
        twin = source.with_suffix(".txt")
        if source.read_bytes() != twin.read_bytes():
            raise ValueError(f"Promptfassungen weichen ab: {kind}")
        if kind == "schnellstart" and source.stat().st_size > 7500:
            raise ValueError("Mini-Prompt überschreitet 7.500 UTF-8-Bytes")
        for path in (source, twin):
            shutil.copyfile(path, destination / path.name)
        report["prompts"][kind] = render_prompt(source, destination / source.with_suffix(".pdf").name)

    write_zip(destination / f"{NAME}.zip", False)
    write_zip(destination / f"{NAME}-portable.zip", True)
    individual = module("build-testakten-einzelpdf-zips.py")
    originals = module("build-testakten-release-zips.py")
    for case in CASES:
        directory = ROOT / "testakten" / case
        pairs = document_arcname_pairs(directory)
        if len(pairs) < 30:
            raise ValueError(f"Testakte zu klein: {case} ({len(pairs)} Dokumente)")
        for source, _ in pairs:
            if source.suffix.lower() in {".docx", ".xlsx", ".odt"} and not valid_office_container(source):
                raise ValueError(f"Ungültiges natives Office-Dokument: {source}")
        individual_path, count = individual.build_single(directory, destination)
        writer = PdfWriter()
        with zipfile.ZipFile(individual_path) as archive:
            for source, arcname in pairs:
                writer.append(io.BytesIO(archive.read(arcname)), outline_item=source.relative_to(directory).as_posix())
        combined = directory / "gesamt-pdf" / f"{case}_gesamt.pdf"
        combined.parent.mkdir(parents=True, exist_ok=True)
        writer.add_metadata({"/Title": f"Testakte {case}", "/Author": "Fiktive Testakte"})
        writer.write(combined)
        originals.build_single(directory, destination)
        shutil.copyfile(combined, destination / combined.name)
        report["cases"][case] = {"documents": count, "pages": len(PdfReader(combined).pages), "sha256": sha(combined)}

    (destination / "quellenabgleich.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    actual_without_checksums = {p.name for p in destination.iterdir()}
    expected_without_checksums = asset_names() - {"checksums-sha256.txt"}
    if actual_without_checksums != expected_without_checksums:
        raise ValueError(f"Assetliste weicht ab: {actual_without_checksums ^ expected_without_checksums}")
    (destination / "checksums-sha256.txt").write_text("".join(f"{sha(destination / name)}  {name}\n" for name in sorted(actual_without_checksums)), encoding="utf-8")
    if {p.name for p in destination.iterdir()} != asset_names():
        raise ValueError("Endgültige Assetliste weicht ab")
    proof = ROOT / "quality" / NAME / "release-pakete.json"
    proof.parent.mkdir(parents=True, exist_ok=True)
    proof.write_text(json.dumps({**report, "assets": {p.name: {"sha256": sha(p), "size": p.stat().st_size} for p in sorted(destination.iterdir())}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.dist.resolve()), ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""Baut elf Skills, drei Promptpaare und drei geprüfte PDF-Lesefassungen."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import zipfile

import pdfplumber
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate

from prompt_profiles import PROMPT_SUFFIXES

ROOT = Path(__file__).resolve().parents[1]
NAME = "ki-halluzinationsreduzierer"
VERSION = "1.1.0"
TAG = f"{NAME}-v{VERSION}"
KINDS = ("werkstatt", "schnellstart", "hauptproblem")
SKIP_PARTS = {".git", ".venv", "node_modules", "__pycache__", "testakte", "testakten"}
FONT_REG, FONT_BOLD = "Halluzinationspruefer-Regular", "Halluzinationspruefer-Bold"


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def asset_names():
    return {f"{NAME}{suffix}.zip" for suffix in ("", "-portable")} | {
        f"{NAME}-{kind}.{ext}" for kind in KINDS for ext in ("md", "txt", "pdf")
    } | {"quellenabgleich.json", "checksums-sha256.txt"}


def plugin_sources():
    directory = ROOT / NAME
    files = {}
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if path.is_symlink():
            raise ValueError(f"Symbolischer Link ist kein Releaseinhalt: {path}")
        if SKIP_PARTS.intersection(relative.parts) or path.name in {".DS_Store", "CLAUDE.md"}:
            continue
        if path.suffix == ".pyc" or path.name.endswith(PROMPT_SUFFIXES):
            continue
        if path.is_file():
            if path.suffix.lower() in {".pdf", ".docx", ".xlsx", ".eml"}:
                raise ValueError(f"Akten- oder Lesefassungsdatei im Plugin: {path}")
            files[relative.as_posix()] = path
    for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if name not in files and (ROOT / name).is_file():
            files[name] = ROOT / name
    return files


def visible_markdown(source):
    # Langadressen werden mit ausgegeben; Markdown-Linksyntax entfällt.
    text = re.sub(r"\[([^\]]+)\]\(([^ )]+)\)", r"\1 (\2)", source)
    # Auch kurze Codebezeichner bleiben in der tatsächlichen Grundschrift.
    return re.sub(r"`([^`]+)`", r"\1", text)


def words(text):
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "-", text)
    return Counter(re.findall(r"[\w§]+(?:-[\w§]+)*", text.casefold()))


def prose_without_urls(source, rendered):
    for url in re.findall(r"https?://[^\s)]+", source):
        wrapped = r"\s*".join(re.escape(character) for character in url)
        rendered, count = re.subn(wrapped, "", rendered, count=1)
        if count != 1:
            raise ValueError(f"URL im PDF nicht vollständig: {url}")
        source = source.replace(url, "", 1)
    return source, rendered


def inspect_pdf(source, target):
    """Prüft Glyphen, Seitenbegrenzung und vollständigen Wortbestand ohne Fußzeilen."""
    text_parts = []
    character_count = 0
    with pdfplumber.open(target) as document:
        if not document.pages:
            raise ValueError(f"Leere PDF-Lesefassung: {target}")
        for number, page in enumerate(document.pages, 1):
            if not page.chars:
                raise ValueError(f"Leere PDF-Seite: {target.name}, Seite {number}")
            for character in page.chars:
                value = character.get("text", "")
                if "\ufffd" in value or "\x00" in value or "(cid:" in value:
                    raise ValueError(f"Nicht lesbare Glyphe: {target.name}, Seite {number}: {value!r}")
                if (character["x0"] < -0.5 or character["x1"] > page.width + 0.5
                        or character["top"] < -0.5 or character["bottom"] > page.height + 0.5):
                    raise ValueError(f"Text außerhalb der Seite: {target.name}, Seite {number}")
            character_count += len(page.chars)
            # Fußzeilen dürfen fehlende Wörter des eigentlichen Textes nicht ersetzen.
            text_parts.append(page.crop((0, 0, page.width, page.height - 42)).extract_text() or "")
        page_count = len(document.pages)
    source_text = visible_markdown(source.read_text(encoding="utf-8"))
    left, right = prose_without_urls(source_text, "\n".join(text_parts))
    missing = words(left) - words(right)
    if missing:
        raise ValueError(f"Wörter fehlen in {target.name}: {dict(missing)}")
    return {"pages": page_count, "characters": character_count,
            "source_words": sum(words(left).values()), "missing_words": 0,
            "bounds_checked": True, "glyphs_checked": True}


def register_fonts():
    candidates = (
        (Path("/System/Library/Fonts/Supplemental"),
         ("Times New Roman.ttf", "Times New Roman Bold.ttf"), "Times New Roman"),
        (Path("/usr/share/fonts/truetype/liberation2"),
         ("LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf"),
         "Liberation Serif (Ersatz für Times New Roman)"),
    )
    for directory, filenames, label in candidates:
        if all((directory / filename).is_file() for filename in filenames):
            for name, filename in zip((FONT_REG, FONT_BOLD), filenames):
                pdfmetrics.registerFont(TTFont(name, str(directory / filename)))
            pdfmetrics.registerFontFamily(FONT_REG, normal=FONT_REG, bold=FONT_BOLD,
                                          italic=FONT_REG, boldItalic=FONT_BOLD)
            return label
    raise RuntimeError("Times New Roman und Liberation Serif fehlen; kein stiller Schriftwechsel.")


def render_prompt(source, target):
    render = module("build-testakte-gesamt-pdf.py")
    label = register_fonts()
    markdown = visible_markdown(source.read_text(encoding="utf-8"))
    for name in (FONT_REG, FONT_BOLD):
        supported = pdfmetrics.getFont(name).face.charToGlyph
        missing = sorted({character for character in markdown if not character.isspace()
                          and ord(character) not in supported})
        if missing:
            raise ValueError(f"Schrift {name} enthält nicht alle Glyphen: {missing}")
    render.FONT_REG, render.FONT_BOLD = FONT_REG, FONT_BOLD
    for style in (render.s_body, render.s_meta):
        style.fontName, style.fontSize, style.leading = FONT_REG, 11, 14.3
    for style in (render.s_h1, render.s_h2, render.s_h3):
        style.fontName, style.keepWithNext = FONT_BOLD, True

    def footer(canvas, document):
        canvas.setFont(FONT_REG, 7.5)
        canvas.drawString(55, 27, f"KI-Halluzinationsreduzierer {VERSION} | {label} 11 pt")
        canvas.drawRightString(A4[0] - 55, 27, str(document.page))

    document = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=55, rightMargin=55,
                                 topMargin=50, bottomMargin=50, invariant=1,
                                 title=source.stem, author="Klotzkette", subject=f"{label} 11 pt")
    document.build(render.md_to_flowables(markdown), onFirstPage=footer, onLaterPages=footer)
    result = inspect_pdf(source, target)
    result.update({"source": source.relative_to(ROOT).as_posix(), "source_sha256": sha(source),
                   "sha256": sha(target), "font": label, "font_size": 11})
    return result


def build(dist):
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein; keine vorhandenen Assets überschreiben.")
    plugin = ROOT / NAME
    for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        manifest = json.loads((plugin / relative).read_text(encoding="utf-8"))
        if (manifest["name"], manifest["version"]) != (NAME, VERSION):
            raise ValueError(f"Manifestname oder Version stimmt nicht: {relative}")
    if len(list((plugin / "skills").glob("*/SKILL.md"))) != 11:
        raise ValueError("Dieses Release benötigt genau elf Skills.")
    report = {"schema_version": 1, "tag": TAG, "plugin": NAME, "version": VERSION,
              "files": {}, "prompts": {}, "pdfs": {}}
    files = plugin_sources()
    for portable in (False, True):
        prefix = f"{NAME}/" if portable else ""
        target = dist / f'{NAME}{"-portable" if portable else ""}.zip'
        with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as archive:
            for relative, path in files.items():
                info = zipfile.ZipInfo(prefix + relative, (2026, 10, 18, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(target) as archive:
            if set(archive.namelist()) != {prefix + name for name in files}:
                raise ValueError("Dateiliste im Plugin-ZIP weicht ab.")
            for relative, path in files.items():
                if archive.read(prefix + relative) != path.read_bytes():
                    raise ValueError(f"Quellenabweichung im ZIP: {relative}")
    report["files"] = {relative: sha(path) for relative, path in files.items()}
    for kind in KINDS:
        source = plugin / f"{NAME}-{kind}.md"
        twin = source.with_suffix(".txt")
        if source.read_bytes() != twin.read_bytes():
            raise ValueError(f"MD/TXT weichen ab: {kind}")
        data = source.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        if kind != "werkstatt" and len(data) > 7500:
            raise ValueError(f"Kompaktprompt überschreitet 7.500 UTF-8-Bytes einschließlich CRLF: {kind}")
        for path in (source, twin):
            shutil.copyfile(path, dist / path.name)
            report["prompts"][path.name] = sha(path)
        pdfname = source.with_suffix(".pdf").name
        report["pdfs"][pdfname] = render_prompt(source, dist / pdfname)
    (dist / "quellenabgleich.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dist / "checksums-sha256.txt").write_text("".join(
        f"{sha(path)}  {path.name}\n" for path in sorted(dist.iterdir())), encoding="utf-8")
    if {path.name for path in dist.iterdir()} != asset_names() or len(asset_names()) != 13:
        raise ValueError("Das Release muss genau die vorgesehenen dreizehn Assets enthalten.")
    print(json.dumps({"tag": TAG, "assets": len(asset_names()), "dist": str(dist),
                      "pdfs": report["pdfs"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    build(parser.parse_args().dist.resolve())

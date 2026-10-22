#!/usr/bin/env python3
"""Baut Insolvenzanfechtung, Fachanwalts-Ergänzung und fünf vollständige Übungsakten."""
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
NAME = "insolvenzanfechtung"
VERSION = "1.1.0"
TAG = f"{NAME}-v{VERSION}"
KINDS = ("werkstatt", "schnellstart", "hauptproblem")
SKIP_PARTS = {".git", ".venv", "node_modules", "__pycache__", "testakte", "testakten", "prompts"}
FONT_REG, FONT_BOLD = "Anfechtungspruefer-Regular", "Anfechtungspruefer-Bold"


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


PARENT = "fachanwalt-insolvenz-sanierungsrecht"
PARENT_VERSION = "445.35.4"
CASES = ("fintech-darlehen-vertragsuebernahme-bremen", "insolvenzanfechtung-blechliebe-bamberg", "insolvenzanfechtung-faltenwurf-fuerth", "insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln", "insolvenzanfechtung-veedelwende-zession-koeln")
PROOF = ROOT / "quality/insolvenzanfechtung/release-pakete.json"


def prompt_sources():
    return [ROOT / NAME / f"{NAME}-{kind}.md" for kind in KINDS] + [
        ROOT / PARENT / "prompts/insolvenzanfechtung" / f"insolvenzanfechtung-{kind}.md"
        for kind in ("werkstatt", "schnellstart")]


def prompt_asset(source):
    return f"{PARENT}-{source.name}" if PARENT in source.parts else source.name


def asset_names():
    return {f"{name}{suffix}.zip" for name in (NAME, PARENT) for suffix in ("", "-portable")} | {
        str(Path(prompt_asset(source)).with_suffix("." + ext)) for source in prompt_sources() for ext in ("md", "txt", "pdf")
    } | {name for slug in CASES for name in (f"testakte-{slug}.zip", f"testakte-{slug}-einzelpdfs.zip", f"{slug}_gesamt.pdf")} | {"quellenabgleich.json", "checksums-sha256.txt"}


def plugin_sources(name):
    directory = ROOT / name
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
    for filename in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if filename not in files and (ROOT / filename).is_file():
            files[filename] = ROOT / filename
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
        (Path("/usr/share/fonts/truetype/liberation"),
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

    if "werkstatt" not in source.name:
        # Kurze Prompts ohne nahezu leere Schlussseite; Grundschrift unverändert.
        render.s_body.spaceAfter = 5
        render.s_body.leading = 14
        render.s_h1.spaceBefore, render.s_h1.spaceAfter = 12, 6
        render.s_h2.spaceBefore, render.s_h2.spaceAfter = 8, 5

    def footer(canvas, document):
        canvas.setFont(FONT_REG, 7.5)
        canvas.drawString(55, 27, f"Insolvenzanfechtung {VERSION} | {label} 11 pt")
        canvas.drawRightString(A4[0] - 55, 27, str(document.page))

    document = SimpleDocTemplate(str(target), pagesize=A4,
                                 leftMargin=55 if "werkstatt" in source.name else 50,
                                 rightMargin=55 if "werkstatt" in source.name else 50,
                                 topMargin=50, bottomMargin=50, invariant=1,
                                 title=source.stem, author="Klotzkette", subject=f"{label} 11 pt")
    document.build(render.md_to_flowables(markdown), onFirstPage=footer, onLaterPages=footer)
    result = inspect_pdf(source, target)
    result.update({"source": source.relative_to(ROOT).as_posix(), "source_sha256": sha(source),
                   "sha256": sha(target), "font": label, "font_size": 11})
    return result


def published_proof_status(actual, candidate=False):
    expected = json.loads(PROOF.read_text(encoding="utf-8"))
    if actual == expected:
        return "matching_release"
    if (candidate
            and all(actual.get(key) == expected.get(key) for key in ("version", "release", "plugins"))
            and set(actual.get("assets", {})) == set(expected.get("assets", {}))):
        return "source_candidate_not_published"
    raise ValueError("Fachanwalts-Paket stimmt nicht mit dem Routingnachweis überein.")


def build(dist, case_assets, write_proof=False, candidate=False):
    if write_proof and candidate:
        raise ValueError("Quellkandidat darf keinen Veröffentlichungsnachweis ändern.")
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein.")
    report = {"schema_version": 1, "tag": TAG, "plugin": NAME, "version": VERSION,
              "plugins": {}, "prompts": {}, "pdfs": {}, "cases": {}}
    for name, version in ((NAME, VERSION), (PARENT, PARENT_VERSION)):
        directory = ROOT / name
        for relative in (("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json") if name == NAME else (".claude-plugin/plugin.json",)):
            manifest = json.loads((directory / relative).read_text(encoding="utf-8"))
            if (manifest["name"], manifest["version"]) != (name, version):
                raise ValueError(f"Manifeststand falsch: {name}/{relative}")
        if name == NAME and len(list((directory / "skills").glob("*/SKILL.md"))) != 11:
            raise ValueError("Zehn Fachskills und ein Hauptskill erforderlich.")
        files = plugin_sources(name)
        report["plugins"][name] = {"version": version, "files": {rel: sha(path) for rel, path in files.items()}}
        for portable in (False, True):
            prefix = f"{name}/" if portable else ""
            target = dist / f'{name}{"-portable" if portable else ""}.zip'
            with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as archive:
                for relative, path in files.items():
                    info = zipfile.ZipInfo(prefix + relative, (2026, 10, 22, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes())
            with zipfile.ZipFile(target) as archive:
                if set(archive.namelist()) != {prefix + rel for rel in files}:
                    raise ValueError("Dateiliste im Plugin-ZIP weicht ab.")
                for relative, path in files.items():
                    if archive.read(prefix + relative) != path.read_bytes():
                        raise ValueError(f"Quellenabweichung: {relative}")
    for source in prompt_sources():
        twin = source.with_suffix(".txt")
        if source.read_bytes() != twin.read_bytes():
            raise ValueError(f"MD/TXT weichen ab: {source}")
        data = source.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        if "werkstatt" not in source.name and len(data) > 7500:
            raise ValueError(f"Kompaktprompt über 7.500 UTF-8-Bytes: {source}")
        for path in (source, twin):
            target = dist / prompt_asset(path)
            shutil.copyfile(path, target)
            report["prompts"][target.name] = sha(path)
        target = dist / str(Path(prompt_asset(source)).with_suffix(".pdf"))
        report["pdfs"][target.name] = render_prompt(source, target)
    for slug in CASES:
        names = (f"testakte-{slug}.zip", f"testakte-{slug}-einzelpdfs.zip", f"{slug}_gesamt.pdf")
        for name in names:
            source = case_assets / name
            if not source.is_file():
                raise ValueError(f"Aktenasset fehlt: {source}")
            shutil.copyfile(source, dist / name)
            report["cases"][name] = sha(source)
    proof = {"version": PARENT_VERSION, "release": TAG, "plugins": [{"name": PARENT}],
             "assets": {f"{PARENT}.zip": sha(dist / f"{PARENT}.zip")}}
    if write_proof:
        PROOF.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        routing_path = ROOT / "scripts/scoped-release-package-versions.json"
        routing = json.loads(routing_path.read_text(encoding="utf-8"))
        routing["assets"][f"{PARENT}.zip"] = {
            "tag": TAG, "version": PARENT_VERSION,
            "sha256": proof["assets"][f"{PARENT}.zip"],
            "evidence": PROOF.relative_to(ROOT).as_posix(),
        }
        routing_path.write_text(json.dumps(routing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        report["published_proof_status"] = published_proof_status(proof, candidate)
    (dist / "quellenabgleich.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dist / "checksums-sha256.txt").write_text("".join(f"{sha(path)}  {path.name}\n" for path in sorted(dist.iterdir())), encoding="utf-8")
    if {path.name for path in dist.iterdir()} != asset_names():
        raise ValueError("Releaseumfang weicht ab.")
    print(json.dumps({"tag": TAG, "assets": len(asset_names()), "pdfs": report["pdfs"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--case-assets", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write-proof", action="store_true")
    mode.add_argument("--candidate", action="store_true", help="Quellkandidat ohne Änderung veröffentlichter Paketnachweise")
    args = parser.parse_args()
    build(args.dist.resolve(), args.case_assets.resolve(), args.write_proof, args.candidate)

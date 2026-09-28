#!/usr/bin/env python3
"""Erzeugt ausschließlich die formatierten Mainzer Originalunterlagen."""

from __future__ import annotations

import argparse
import csv
from email import policy
from email.parser import BytesParser
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import shutil
import sys
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "testakten/ki-transparenz-kanzlei-kommunikation-mainz"
FIXTURE = ROOT / "scripts/fixtures/ki-transparenz-mainz"
from akten_build_runtime import serif_font_path
from testakte_office_pdf import office_binary


def document_blocks(spec):
    yield "title", spec["title"]
    for key, label in (("author", "Von"), ("recipient", "An"), ("date", "Datum"), ("reference", "Bezug")):
        yield "meta", f"{label}: {spec[key]}"
    for section in spec["sections"]:
        yield "heading", section["heading"]
        for text in section["paragraphs"]:
            yield "body", text


def create_docx(spec, path):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin = sec.bottom_margin = Inches(0.8)
    sec.left_margin = sec.right_margin = Inches(0.85)
    sec.footer_distance = Inches(0.35)
    for style in doc.styles:
        if style.type == 1:
            style.font.name = "Times New Roman"
            style.font.size = Pt(11)
            style.font.color.rgb = RGBColor(0, 0, 0)
            for element in style.element.iter():
                for attr in list(element.attrib):
                    if "theme" in attr.lower():
                        del element.attrib[attr]
            for border in list(style.element.iter(qn("w:pBdr"))):
                border.getparent().remove(border)
    normal = doc.styles["Normal"].paragraph_format
    normal.space_after = Pt(7)
    normal.line_spacing = 1.1
    normal.widow_control = True
    for name in ("Title", "Heading 1"):
        style = doc.styles[name]
        style.font.bold = True
        style.paragraph_format.space_before = Pt(10)
        style.paragraph_format.space_after = Pt(8)
        style.paragraph_format.keep_with_next = True
    for kind, text in document_blocks(spec):
        paragraph = doc.add_paragraph(text, "Title" if kind == "title" else "Heading 1" if kind == "heading" else "Normal")
        if spec["file"].startswith("05_") and kind == "heading" and text.startswith("3."):
            paragraph.paragraph_format.page_break_before = True
        if kind == "meta":
            paragraph.paragraph_format.space_after = Pt(3)
            paragraph.paragraph_format.keep_with_next = True
    footer = sec.footer.paragraphs[0]
    footer.alignment = 2
    footer.add_run("Seite ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    doc.core_properties.author = spec["author"]
    doc.core_properties.title = spec["title"]
    doc.core_properties.last_modified_by = spec["author"]
    doc.save(path)


def pdf_styles():
    pdfmetrics.registerFont(TTFont("MainzTNR", str(serif_font_path())))
    pdfmetrics.registerFont(TTFont("MainzTNRBold", str(serif_font_path(True))))
    return {
        "body": ParagraphStyle("Body", fontName="MainzTNR", fontSize=11, leading=13.2, spaceAfter=8),
        "meta": ParagraphStyle("Meta", fontName="MainzTNR", fontSize=11, leading=13.2, spaceAfter=3),
        "title": ParagraphStyle("Title", fontName="MainzTNRBold", fontSize=11, leading=14, spaceAfter=12, keepWithNext=True),
        "heading": ParagraphStyle("Heading", fontName="MainzTNRBold", fontSize=11, leading=14, spaceBefore=10, spaceAfter=8, keepWithNext=True),
    }


def write_pdf(path, blocks, image_path=None):
    styles = pdf_styles()
    story = [PageBreak() if kind == "break" else Paragraph(escape(text).replace("\n", "<br/>"), styles[kind]) for kind, text in blocks]
    if image_path:
        story.extend([PageBreak(), Paragraph("3. Vergleichsansicht MZ Schulweg 07B", styles["heading"]),
                      Paragraph("Oben Raumstand ohne Gesprächsteilnehmende. Unten bearbeitete Fassung zur Auswahl. Lieferung vom 24. September 2026.", styles["body"]),
                      Spacer(1, 6), Image(str(image_path), width=400, height=540)])

    def footer(canvas, doc):
        canvas.setFont("MainzTNR", 11)
        canvas.drawRightString(letter[0] - 61.2, 25, f"Seite {doc.page}")

    SimpleDocTemplate(str(path), pagesize=letter, leftMargin=61.2, rightMargin=61.2,
                      topMargin=48, bottomMargin=48, title=path.stem,
                      author="Seidel und Kühn", pageCompression=1).build(story, onFirstPage=footer, onLaterPages=footer)


def native_preview(path, output):
    if path.suffix == ".eml":
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        blocks = [("title", str(message["Subject"]))]
        blocks += [("meta", f"{label}: {message[key]}") for key, label in
                   (("From", "Von"), ("To", "An"), ("Cc", "Kopie"), ("Date", "Datum")) if message[key]]
        blocks += [("body", p.replace("\n", " ")) for p in message.get_content().strip().split("\n\n")]
    elif path.suffix == ".csv":
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter=";"))
        blocks = [("title", "Systeminventar vom 25. September 2026")]
        for row in rows:
            blocks.append(("heading", f"{row['kennung']} {row['produkt']} {row['version']}"))
            blocks += [("body", f"{key}: {value}") for key, value in row.items() if key not in {"kennung", "produkt", "version"}]
    else:
        blocks = [("body", text) for text in path.read_text(encoding="utf-8").split("\n\n") if text.strip()]
        if path.name.startswith("08_"):
            index = next(i for i, (_, text) in enumerate(blocks) if text.startswith("3. Beobachtungen"))
            blocks.insert(index, ("break", ""))
    write_pdf(output, blocks)


def render_all(qa_dir):
    renderer = Path(os.environ.get("AKTEN_DOCX_RENDERER", "")).expanduser()
    office = office_binary()
    rasterizer = shutil.which("pdftoppm")
    if not renderer.is_file() or not office or not rasterizer:
        raise RuntimeError("Für --qa-dir AKTEN_DOCX_RENDERER auf render_docx.py setzen sowie LibreOffice und pdftoppm bereitstellen")
    qa_dir.mkdir(parents=True, exist_ok=True)
    module_spec = importlib.util.spec_from_file_location("mainz_render_docx", renderer)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module._resolve_soffice = lambda: office
    result = []
    for path in sorted(CASE.glob("[0-9][0-9]_*")):
        target = qa_dir / path.stem
        target.mkdir(exist_ok=True)
        if path.suffix == ".docx":
            sys.argv = [str(renderer), str(path), "--output_dir", str(target), "--dpi", "130", "--emit_pdf"]
            module.main()
        else:
            pdf = path
            if path.suffix != ".pdf":
                pdf = target / (path.stem + ".pdf")
                native_preview(path, pdf)
            subprocess.run([rasterizer, "-png", "-r", "130", str(pdf), str(target / "page")], check=True, timeout=180)
        result.append({"file": path.name, "pages": len(list(target.glob("page-*.png")))})
    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qa-dir", type=Path)
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()
    if args.render_only and not args.qa_dir:
        parser.error("--render-only benötigt --qa-dir")
    if not args.render_only:
        specs = json.loads((FIXTURE / "documents.json").read_text(encoding="utf-8"))["documents"]
        for spec in specs:
            name = spec["file"]
            if Path(name).name != name or Path(name).suffix not in {".docx", ".pdf"}:
                raise ValueError(f"Ungültiger Aktenpfad: {name}")
            target = CASE / name
            if target.suffix == ".docx":
                create_docx(spec, target)
            else:
                write_pdf(target, document_blocks(spec), FIXTURE / "bildvergleich.png" if name.startswith("10_") else None)
    if args.qa_dir:
        if args.qa_dir.resolve().is_relative_to(ROOT.resolve()):
            parser.error("QA-Ausgaben müssen außerhalb des Repositorys liegen")
        render_all(args.qa_dir)


if __name__ == "__main__":
    main()

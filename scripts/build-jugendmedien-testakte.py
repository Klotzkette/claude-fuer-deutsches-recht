#!/usr/bin/env python3
"""Build the fictional Wolkenwerft intake, later evidence and blank templates.

Run with the document-capable Python runtime and licensed Times New Roman TTFs.
Validation deliberately uses only the standard library so CI can check the
intake boundary without access to the licensed rendering fonts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import textwrap
import zipfile
from datetime import datetime, timezone
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from pathlib import Path, PurePosixPath
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "scripts/data/jugendmedien-wolkenwerft.json"
DEFAULT_OUTPUT = ROOT / "jugendmedienschutz-und-medienangebote/testakte"
FOLDERS = {
    "G": "01_Grundakte_ohne_Loesung",
    "N": "02_Nachreichungen",
    "V": "03_Vorlagen",
}
ARCHIVE_NAME = "testakte-jugendmedien-wolkenwerft-originaldateien.zip"
PDF_NAME = "testakte-jugendmedien-wolkenwerft-gesamt.pdf"
XLSX_NAME = "V05_Leere_Arbeitsmatrix.xlsx"
FIXED_TIME = datetime(2026, 11, 18, 12, 0, tzinfo=timezone.utc)


def validate_documents(payload: dict) -> None:
    """Reject a lost, duplicated, misplaced or unsafe source document."""
    if not isinstance(payload, dict) or not isinstance(payload.get("case"), dict):
        raise ValueError("Missing case metadata")
    documents = payload.get("documents")
    if not isinstance(documents, list):
        raise ValueError("Missing documents")
    expected = {f"G{i:02d}" for i in range(1, 26)}
    expected |= {f"N{i:02d}" for i in range(1, 5)}
    expected |= {f"V{i:02d}" for i in range(1, 5)}
    ids, paths = set(), set()
    for item in documents:
        ident = item.get("id", "")
        if ident not in expected or ident in ids:
            raise ValueError(f"Unexpected or duplicate document ID: {ident}")
        ids.add(ident)
        if item.get("folder") != FOLDERS[ident[0]]:
            raise ValueError(f"Wrong intake/follow-up/template folder: {ident}")
        name = item.get("filename", "")
        if not name or PurePosixPath(name).name != name or "\\" in name:
            raise ValueError(f"Unsafe filename: {name}")
        fmt = item.get("format")
        if fmt not in {"docx", "pdf", "eml", "txt", "csv", "json"}:
            raise ValueError(f"Unsupported format: {fmt}")
        if not name.startswith(ident + "_") or not name.endswith("." + fmt):
            raise ValueError(f"Filename and document identity differ: {name}")
        path = item["folder"] + "/" + name
        if path in paths:
            raise ValueError(f"Duplicate output path: {path}")
        paths.add(path)
        paragraphs = item.get("paragraphs")
        if not isinstance(paragraphs, list) or not paragraphs or any(
            not isinstance(p, str) or not p.strip() for p in paragraphs
        ):
            raise ValueError(f"Missing document text: {ident}")
        for field in ("sender", "recipient", "date", "title"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"Missing {field}: {ident}")
        datetime.fromisoformat(item["date"])
        if fmt == "csv":
            if not item.get("columns") or not isinstance(item.get("rows"), list):
                raise ValueError(f"Missing table: {ident}")
            if any(len(row) != len(item["columns"]) for row in item["rows"]):
                raise ValueError(f"Uneven table rows: {ident}")
        if fmt == "json":
            if json.loads(item.get("nativeText", "")) != item.get("data"):
                raise ValueError(f"JSON body and source differ: {ident}")
    if ids != expected:
        raise ValueError(f"Missing document IDs: {sorted(expected - ids)}")


def normalize_office_zip(path: Path) -> None:
    """Stable container timestamps, without changing document contents."""
    with zipfile.ZipFile(path) as src:
        members = {name: src.read(name) for name in src.namelist()}
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as dst:
        for name, content in sorted(members.items()):
            info = zipfile.ZipInfo(name, (2026, 11, 18, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            dst.writestr(info, content)


def create_docx(item: dict, output: Path) -> None:
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2.8), Cm(2.2)
    section.left_margin = section.right_margin = Cm(2.2)
    section.header_distance = section.footer_distance = Cm(1.1)
    normal = doc.styles["Normal"]
    normal.font.name, normal.font.size = "Times New Roman", Pt(11)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.line_spacing = 1.17
    normal.paragraph_format.space_after = Pt(8)
    # The bundled base template contains theme fonts and a blue Title border.
    # Explicitly clear those inherited slots; setting font.name alone leaves
    # LibreOffice free to use the major theme font instead of Times New Roman.
    for style in doc.styles:
        if style.type not in (1, 2):
            continue
        style.font.name = "Times New Roman"
        rpr = style.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is not None:
            for attribute in list(fonts.attrib):
                if "theme" in attribute.lower():
                    del fonts.attrib[attribute]
            for slot in ("ascii", "hAnsi", "eastAsia", "cs"):
                fonts.set(qn("w:" + slot), "Times New Roman")
        for border in list(style.element.iter(qn("w:pBdr"))):
            border.getparent().remove(border)
    for name, size in (("Title", 20), ("Heading 1", 14), ("Heading 2", 12)):
        style = doc.styles[name]
        style.font.name, style.font.size = "Times New Roman", Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = Pt(10)
        style.paragraph_format.space_after = Pt(5)
    head = section.header.paragraphs[0]
    head.text = "ARBEITSVORLAGE  /  INSELATLAS" if item["id"].startswith("V") else "WOLKENWERFT  /  INSELATLAS"
    head.runs[0].font.size = Pt(10)
    head.runs[0].font.bold = True
    head.runs[0].font.color.rgb = RGBColor(0, 0, 0)
    footer = section.footer.paragraphs[0]
    footer.text = f"{item['id']}  ·  Fiktive Schulungsakte  ·  Seite "
    footer.runs[0].font.size = Pt(9)
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    doc.add_paragraph(item["title"], "Title")
    meta = doc.add_paragraph(f"{item['id']}  ·  {item['date']}  ·  {item['sender']}")
    meta.paragraph_format.space_after = Pt(14)
    for p in item["paragraphs"]:
        lines = p.splitlines()
        if re.match(r"^\d+\. ", lines[0]) and len(lines) > 1:
            doc.add_paragraph(lines[0], "Heading 2")
            doc.add_paragraph("\n".join(lines[1:]))
        else:
            doc.add_paragraph(p)
    # The blank matrix is supplied as an editable spreadsheet. A seven-column
    # prose form in portrait Word would make the otherwise spacious form cramped.
    doc.core_properties.title = item["title"]
    doc.core_properties.author = item["sender"]
    doc.core_properties.created = doc.core_properties.modified = FIXED_TIME
    doc.save(output)
    normalize_office_zip(output)


def register_fonts(font_dir: Path) -> None:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    names = {
        "WWTimes": "Times New Roman.ttf",
        "WWTimes-Bold": "Times New Roman Bold.ttf",
        "WWTimes-Italic": "Times New Roman Italic.ttf",
        "WWTimes-BoldItalic": "Times New Roman Bold Italic.ttf",
    }
    missing = [str(font_dir / name) for name in names.values() if not (font_dir / name).is_file()]
    if missing:
        raise RuntimeError("Licensed Times New Roman TTFs missing; set UFERWERK_FONT_DIR: " + ", ".join(missing))
    for registered, filename in names.items():
        pdfmetrics.registerFont(TTFont(registered, str(font_dir / filename)))
    pdfmetrics.registerFontFamily("WWTimes", normal="WWTimes", bold="WWTimes-Bold", italic="WWTimes-Italic", boldItalic="WWTimes-BoldItalic")


def create_pdf(item: dict, output: Path) -> None:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    is_table = item["format"] == "csv"
    page_size = landscape(A4) if is_table else A4
    body = ParagraphStyle("body", fontName="WWTimes", fontSize=11, leading=15.3, spaceAfter=9, allowWidows=0, allowOrphans=0)
    heading = ParagraphStyle("heading", parent=body, fontName="WWTimes-Bold", fontSize=12, leading=15, spaceBefore=7, spaceAfter=5, keepWithNext=True)
    title = ParagraphStyle("title", parent=body, fontName="WWTimes-Bold", fontSize=20, leading=23, spaceAfter=11, keepWithNext=True)
    meta = ParagraphStyle("meta", parent=body, fontSize=9.5, leading=12, spaceAfter=13)
    small = ParagraphStyle("cell", parent=body, fontSize=8.5, leading=10.5, spaceAfter=0)
    code = ParagraphStyle("code", parent=body, fontName="Courier", fontSize=8, leading=9.5, spaceAfter=0)
    page_w, page_h = page_size

    def stationery(c, d):
        c.saveState()
        c.setFillColor(colors.HexColor("#124C5B"))
        c.rect(22*mm, page_h-18*mm, 5*mm, 5*mm, fill=1, stroke=0)
        c.setFillColor(colors.black)
        c.setFont("WWTimes-Bold", 10)
        brand = "VERFAHRENSKORRESPONDENZ  /  FIKTIVE SCHULUNGSUNTERLAGE" if item["id"] == "N03" else "WOLKENWERFT  /  INSELATLAS"
        c.drawString(30*mm, page_h-16.3*mm, brand)
        c.setFont("WWTimes", 8.5)
        c.drawString(22*mm, 12*mm, f"{item['id']}  ·  Fiktive Schulungsakte")
        c.drawRightString(page_w-22*mm, 12*mm, f"Seite {d.page}")
        c.restoreState()

    flow = [Paragraph(escape(item["title"]), title), Paragraph(escape(f"{item['id']}  ·  {item['date']}  ·  {item['sender']}"), meta)]
    if item["format"] == "eml":
        flow += [Paragraph(escape("An: " + item["recipient"]), meta)]
    for p in item["paragraphs"]:
        lines = p.splitlines()
        if re.match(r"^\d+\. ", lines[0]) and len(lines) > 1:
            flow.append(Paragraph(escape(lines[0]), heading))
            flow.append(Paragraph(escape("\n".join(lines[1:])).replace("\n", "<br/>"), body))
        else:
            flow.append(Paragraph(escape(p).replace("\n", "<br/>"), body))
    if is_table:
        table_data = [[Paragraph(escape(str(v)).replace("_", " "), small) for v in row] for row in [item["columns"], *item["rows"]]]
        weights = {
            "G20": [35, 95, 115, 55, 65, 85, 135, 133],
            "G21": [90, 120, 95, 220, 45, 148],
            "G25": [35, 70, 60, 140, 150, 140, 50, 73],
        }.get(item["id"], [1] * len(item["columns"]))
        widths = [(page_w-44*mm)*weight/sum(weights) for weight in weights]
        table = Table(table_data, colWidths=widths, repeatRows=1, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#DFEAF0")),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F5F7F8")]),
            ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#D9D9D9")),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
            ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ]))
        flow.append(table)
    elif item["format"] == "json":
        flow.append(Spacer(1,8))
        for line in item["nativeText"].splitlines():
            for wrapped in textwrap.wrap(line, width=92, replace_whitespace=False, drop_whitespace=False) or [""]:
                flow.append(Paragraph(escape(wrapped).replace(" ", "&#160;"), code))
    document = SimpleDocTemplate(str(output), pagesize=page_size, leftMargin=22*mm, rightMargin=22*mm, topMargin=29*mm, bottomMargin=22*mm, title=item["title"], author=item["sender"])
    def stable_canvas(*args, **kwargs):
        kwargs["invariant"] = 1
        return canvas.Canvas(*args, **kwargs)

    document.build(flow, onFirstPage=stationery, onLaterPages=stationery, canvasmaker=stable_canvas)


def write_native(item: dict, output: Path) -> None:
    fmt = item["format"]
    output.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "docx":
        create_docx(item, output)
    elif fmt == "pdf":
        create_pdf(item, output)
    elif fmt == "eml":
        msg = EmailMessage(policy=SMTP)
        msg["From"], msg["To"] = item["sender"], item["recipient"]
        msg["Date"] = format_datetime(datetime.fromisoformat(item["sentAt"]))
        msg["Subject"], msg["Message-ID"] = item["title"], item["messageId"]
        msg.set_content("\n\n".join(item["paragraphs"]), charset="utf-8")
        output.write_bytes(msg.as_bytes())
    elif fmt == "csv":
        with output.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream, delimiter=";", lineterminator="\n")
            writer.writerow(item["columns"])
            writer.writerows(item["rows"])
    else:
        output.write_text(item.get("nativeText") or "\n\n".join(item["paragraphs"]), encoding="utf-8")


def validate_docx_pdf_fonts(path: Path) -> list[str]:
    """Inspect actual embedded PDF fonts; Word's declared font is not proof."""
    from pypdf import PdfReader

    fonts = set()
    for page in PdfReader(path).pages:
        resources = page.get("/Resources")
        if resources is None:
            continue
        font_map = resources.get_object().get("/Font")
        if font_map is None:
            continue
        for ref in font_map.get_object().values():
            font = ref.get_object()
            name = str(font.get("/BaseFont", ""))
            if "TimesNewRoman" not in name:
                raise ValueError(f"Unexpected font substitution in {path.name}: {name}")
            descriptor = font.get("/FontDescriptor")
            if descriptor is None and font.get("/DescendantFonts"):
                descriptor = font["/DescendantFonts"][0].get_object().get("/FontDescriptor")
            if descriptor is None or not any(k in descriptor.get_object() for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                raise ValueError(f"Times New Roman is not embedded in {path.name}: {name}")
            fonts.add(name)
    if not fonts:
        raise ValueError("No fonts found in rendered DOCX: " + str(path))
    return sorted(fonts)


def build(output: Path, font_dir: Path, xlsx_source: Path | None = None, docx_renderer: Path | None = None, qa_dir: Path | None = None) -> dict:
    from pypdf import PdfReader, PdfWriter
    from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN

    payload = json.loads(FIXTURE.read_text())
    validate_documents(payload)
    register_fonts(font_dir)
    if docx_renderer is None:
        candidates = sorted((Path.home() / ".codex/plugins/cache/openai-primary-runtime/documents").glob("*/skills/documents/render_docx.py"))
        if not candidates:
            raise RuntimeError("Set --docx-renderer to the bundled documents/render_docx.py; native Word files must be rendered")
        docx_renderer = candidates[-1]
    if not docx_renderer.is_file():
        raise RuntimeError("Bundled DOCX renderer is unavailable: " + str(docx_renderer))
    qa_dir = qa_dir or ROOT.parent / "tmp/jugendmedien-qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    font_config = qa_dir / "fontconfig.xml"
    font_config.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>' + escape(str(font_dir.resolve())) + '</dir><cachedir>' + escape(str((qa_dir / "fontcache").resolve())) + '</cachedir></fontconfig>')
    render_env = os.environ.copy()
    render_env["FONTCONFIG_FILE"] = str(font_config.resolve())
    render_env["SAL_FONTPATH"] = str(font_dir.resolve())
    output.mkdir(parents=True, exist_ok=True)
    downloads = output / "downloads"
    downloads.mkdir(exist_ok=True)
    reading = output / "lesefassung"
    reading.mkdir(exist_ok=True)
    originals, pdfs = [], []
    for item in payload["documents"]:
        native = output / item["folder"] / item["filename"]
        write_native(item, native)
        originals.append(native)
        pdf = reading / (Path(item["filename"]).stem + ".pdf")
        if item["format"] == "pdf":
            pdf.write_bytes(native.read_bytes())
        elif item["format"] == "docx":
            render_dir = qa_dir / item["id"]
            subprocess.run([sys.executable, str(docx_renderer), str(native), "--output_dir", str(render_dir), "--emit_pdf"], check=True, env=render_env)
            rendered_pdf = render_dir / (native.stem + ".pdf")
            if not rendered_pdf.is_file():
                raise RuntimeError("DOCX rendering did not produce a PDF: " + str(native))
            validate_docx_pdf_fonts(rendered_pdf)
            pdf.write_bytes(rendered_pdf.read_bytes())
        else:
            create_pdf(item, pdf)
        pdfs.append((item, pdf))
    xlsx = output / FOLDERS["V"] / XLSX_NAME
    if xlsx_source:
        content = xlsx_source.read_bytes()
        xlsx.write_bytes(content)
    elif not xlsx.is_file():
        raise RuntimeError("Build the blank XLSX with scripts/build-jugendmedien-vorlage.mjs --output " + str(xlsx))
    with zipfile.ZipFile(xlsx) as book:
        if "xl/workbook.xml" not in book.namelist():
            raise ValueError("The blank workbook is not an XLSX")
    normalize_office_zip(xlsx)
    originals.append(xlsx)
    archive = downloads / ARCHIVE_NAME
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        info = zipfile.ZipInfo("README.txt", (2026,11,18,12,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, NOTICE_BYTES + ("\n\n" + payload["case"]["fictionNotice"] + "\n\n01_Grundakte_ohne_Loesung: Bearbeitungsbeginn 18.11.2026.\n02_Nachreichungen: spaeter separat oeffnen.\n03_Vorlagen: leere Arbeitsmittel.\nDie Gesamt-PDF-Lesefassung ist bewusst nicht Bestandteil dieses ZIP.\n").encode("utf-8"))
        for path in originals:
            info = zipfile.ZipInfo(path.relative_to(output).as_posix(), (2026,11,18,12,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, path.read_bytes())
    writer = PdfWriter()
    pdf_inventory = []
    page = 0
    for item, pdf in pdfs:
        reader = PdfReader(pdf)
        writer.append(reader, import_outline=False)
        writer.add_outline_item(f"{item['id']} {item['title']}", page)
        pdf_inventory.append({"id": item["id"], "file": pdf.relative_to(output).as_posix(), "pages": len(reader.pages), "first_page": page+1, "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()})
        page += len(reader.pages)
    writer.add_metadata({"/Title": payload["case"]["title"], "/Author": "Fiktive Akte Wolkenwerft", "/CreationDate": "D:20261118120000Z"})
    total = downloads / PDF_NAME
    with total.open("wb") as stream:
        writer.write(stream)
    inventory = {"case": payload["case"]["title"], "source": "scripts/data/jugendmedien-wolkenwerft.json", "source_sha256": hashlib.sha256(FIXTURE.read_bytes()).hexdigest(), "original_count": len(originals), "grundakte_count": 25, "nachreichungen_count": 4, "vorlagen_count": 5, "pdf_documents": len(pdfs), "pages": page, "originals": [{"file": p.relative_to(output).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size} for p in originals], "pdfs": pdf_inventory, "downloads": [{"file": p.relative_to(output).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size} for p in (archive,total)]}
    (output / "bestand.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2)+"\n")
    (output / "README.md").write_text(f"""# Wolkenwerft und das Browsergame Inselatlas

Die Akte beginnt am 18. November 2026 bei der Beratung einer Freiburger Spielefirma. Vor der öffentlichen Beta müssen widersprüchliche Altersangaben, geteilte Links, KI-Szenen, Gruppenkommunikation und organisatorische Lücken aus unterschiedlichen Unterlagen zusammengeführt werden. Eine fertige Lösung gehört nicht zur Akte.

Öffnen Sie zunächst nur `01_Grundakte_ohne_Loesung`. Die 25 Originaldateien umfassen ausführliche Geschäftsunterlagen, Vertrags- und Produktentwürfe, acht E-Mails sowie technische Exporte. Die vier Nachreichungen enthalten spätere Beschwerden, Produktänderungen, eine fiktive Aufsichtsanfrage und weitere Beteiligungsangaben. Fünf leere Vorlagen unterstützen die eigene Bearbeitung.

{NOTICE_MARKDOWN}

| Fassung | Download |
| --- | --- |
| 34 Originaldateien in drei getrennten Ordnern | [Lebensnahe Akte als ZIP](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/jugendmedienschutz-und-medienangebote/testakte/downloads/{ARCHIVE_NAME}) |
| Vollständige Lesefassung mit {page} Seiten, einschließlich Nachreichungen | [Gesamt-PDF](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/jugendmedienschutz-und-medienangebote/testakte/downloads/{PDF_NAME}) |

Das ZIP enthält keine Gesamt-PDF und keine rechtliche Musterlösung. Die Lesefassung enthält die 33 textlichen Dokumente; die zusätzliche leere Excel-Arbeitsmatrix liegt ausschließlich als bearbeitbare Datei im Vorlagenordner. Öffnen Sie die Nachreichungen erst, nachdem Sie den Anfangsstand selbst bearbeitet haben.

Alle Personen, Unternehmen, Ereignisse und Kommunikationsadressen sind fiktiv. Das Aufsichtsschreiben ist ausdrücklich ein Übungsdokument und keine echte Behördenpost. Technische Kennungen sind keine Zugangsdaten zu realen Diensten. Eine Anfrage bei einer Selbstkontrolle ist im Fall noch keine Mitgliedschaft; 1,8 Millionen Seitenaufrufe sind noch keine ermittelte Zahl aktiver Empfänger.

[Zum Plugin](../README.md) · [Dateibestand und Prüfsummen](bestand.json)
""", encoding="utf-8")
    return inventory


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--font-dir", type=Path, default=Path(os.environ.get("UFERWERK_FONT_DIR", "/System/Library/Fonts/Supplemental")))
    parser.add_argument("--xlsx-source", type=Path)
    parser.add_argument("--docx-renderer", type=Path)
    parser.add_argument("--qa-dir", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.validate_only:
        validate_documents(json.loads(FIXTURE.read_text()))
        print("Wolkenwerft: 33 source documents and intake boundaries valid")
        return
    inv = build(args.output, args.font_dir, args.xlsx_source, args.docx_renderer, args.qa_dir)
    print(json.dumps({k: inv[k] for k in ("original_count", "grundakte_count", "nachreichungen_count", "vorlagen_count", "pdf_documents", "pages", "downloads")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

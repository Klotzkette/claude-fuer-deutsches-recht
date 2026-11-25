#!/usr/bin/env python3
"""Baut die bearbeitbaren Insolvenzvorlagen und das gemeinsame Download-ZIP."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from akteneingang.ausgabe import archive
from akteneingang.dokumente import office_bytes
from testakte_disclaimer import NOTICE_TEXT, NOTICE_FILENAME


ROOT = Path(__file__).resolve().parents[1]
SOURCES = Path("scripts/data/insolvenz-arbeitsvorlagen")
COLLECTION = Path("docs/downloads/insolvenz-arbeitsvorlagen.zip")
PLUGIN_README = Path("fachanwalt-insolvenz-sanierungsrecht/README.md")
GENERAL = "asset-purchase-agreement-blanko"
CROSS_REFERENCE = "fintech-darlehen-vertragsuebernahme-bremen"
FONT = "Times New Roman"
INK, ACCENT, PALE = "192C35", "285262", "E4EEF0"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
PLACEHOLDER = re.compile(r"(\[[^\[\]\n]+\])")


def case_list(root):
    """Die verlinkten Akten der Plugin-Tabelle in redaktioneller Reihenfolge."""
    text = (root / PLUGIN_README).read_text(encoding="utf-8")
    heading = "## Zugeordnete Testakten"
    _, found, after = text.partition(heading + "\n")
    if not found:
        raise ValueError("Abschnitt zur Testaktenzuordnung fehlt in der Plugin-README.")
    section = after.partition("\n## ")[0]
    rows = re.findall(r"^\| \[([^\]]+)\]\(\.\./testakten/([a-z0-9-]+)/README\.md\)", section, re.M)
    # Die Editionsdateien begrenzen den unveränderten Kreis der Blankovorlagen.
    sources = {path.stem for path in (root / SOURCES / "faelle").glob("*.json")}
    rows = [(title, slug) for title, slug in rows if slug in sources and slug != CROSS_REFERENCE]
    if {slug for _, slug in rows} | {CROSS_REFERENCE} != sources or len(rows) != 24 or len({slug for _, slug in rows}) != 24:
        raise ValueError("Die Zuordnungstabelle muss 24 eindeutige Insolvenztestakten enthalten.")
    if f"../testakten/{CROSS_REFERENCE}/README.md" not in text or CROSS_REFERENCE in {s for _, s in rows}:
        raise ValueError("Der gesonderte Querverweis auf die Bremer Darlehensakte fehlt.")
    return [(slug, re.sub(r"^\d+\.\s*", "", title)) for title, slug in rows] + [
        (CROSS_REFERENCE, "Bremer Darlehensverfahren und Vertragsübernahme")]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def filename(spec):
    slug, kind = spec["slug"], spec.get("format", "docx")
    if not SLUG.fullmatch(slug) or kind not in {"docx", "xlsx"}:
        raise ValueError(f"Ungültiger Vorlagenname oder Dateityp: {slug!r}, {kind!r}")
    return f"{slug}.{kind}"


def add_text(paragraph, content):
    for part in PLACEHOLDER.split(content):
        if part:
            run = paragraph.add_run(part)
            if PLACEHOLDER.fullmatch(part):
                run.font.color.rgb = RGBColor.from_string(ACCENT)


def word_table(doc, headers, count):
    if not headers or len(set(headers)) != len(headers) or not 1 <= count <= 100:
        raise ValueError(f"Ungültige Eingabetabelle: {headers!r}, {count!r}")
    table = doc.add_table(rows=count + 1, cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    # Lange Fachwörter in schmalen Spalten am Seitenrand vermeiden.
    available = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    weights = [10 + max(len(word) for word in label.split()) for label in headers]
    widths = [round(available * weight / sum(weights)) for weight in weights]
    for column, width in zip(table.columns, widths):
        column.width = width
    for i, row in enumerate(table.rows):
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        row.height = Cm(0.65)
        if i == 0:
            row._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
        for j, cell in enumerate(row.cells):
            cell.width = widths[j]
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_after = Pt(2)
            paragraph.paragraph_format.space_before = Pt(2)
            paragraph.paragraph_format.keep_with_next = i < (count if count <= 6 else 2)
            if i == 0:
                shade = OxmlElement("w:shd")
                shade.set(qn("w:fill"), PALE)
                cell._tc.get_or_add_tcPr().append(shade)
                paragraph.add_run(headers[j]).bold = True


def word_document(spec):
    doc = Document()
    doc.core_properties.title = spec["titel"]
    doc.core_properties.subject = "Ausfüllbare Arbeitsvorlage"
    doc.core_properties.author = "Klotzkette"
    doc.core_properties.comments = ""
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.left_margin, section.right_margin = Cm(2.3), Cm(2.0)
    section.top_margin, section.bottom_margin = Cm(2.0), Cm(2.1)
    section.header_distance, section.footer_distance = Cm(0.8), Cm(0.9)
    for item in ("Normal", "Heading 1", "Title", "Footer"):
        style = doc.styles[item]
        style.font.name, style.font.size = FONT, Pt(11)
        style.font.color.rgb = RGBColor.from_string(INK)
        fonts = style.element.get_or_add_rPr().rFonts
        for script in ("ascii", "hAnsi", "eastAsia", "cs"):
            fonts.attrib.pop(qn("w:" + script + "Theme"), None)
            fonts.set(qn("w:" + script), FONT)
    normal = doc.styles["Normal"].paragraph_format
    normal.space_after, normal.line_spacing = Pt(4), 1.08
    normal.widow_control = True
    title = doc.styles["Title"]
    title.font.bold = True
    title.paragraph_format.keep_with_next = True
    title.paragraph_format.space_after = Pt(8)
    heading = doc.styles["Heading 1"]
    heading.font.bold = True
    heading.paragraph_format.keep_with_next = True
    heading.paragraph_format.space_before, heading.paragraph_format.space_after = Pt(8), Pt(6)
    doc.add_paragraph(spec["titel"], "Title")
    add_text(doc.add_paragraph(), spec["zweck"])
    for number, block in enumerate(spec["abschnitte"], 1):
        name = block["titel"]
        if name == "Abschluss" and doc.paragraphs:
            # Ein Unterschriftsblock bleibt bei mindestens einem sachlichen Absatz.
            preceding = doc.paragraphs[-1].paragraph_format
            preceding.keep_together = preceding.keep_with_next = True
        if not re.match(r"^\d+(?:\.\d+)*\.?\s+", name):
            name = f"{number} {name}"
        doc.add_paragraph(name, "Heading 1")
        paragraphs = block.get("absaetze", [])
        for index, paragraph in enumerate(paragraphs):
            item = doc.add_paragraph()
            add_text(item, paragraph)
            if block["titel"] == "Abschluss" and len(paragraphs) <= 5:
                item.paragraph_format.space_after = Pt(1)
                item.paragraph_format.keep_with_next = index + 1 < len(paragraphs)
            if "spalten" in block and (len(paragraphs) <= 2 or index + 1 == len(paragraphs)):
                item.paragraph_format.keep_with_next = True
                item.paragraph_format.keep_together = True
        if "spalten" in block:
            word_table(doc, block["spalten"], block.get("zeilen", 3))
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.add_run("Seite ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    return office_bytes(doc)


def spreadsheet(spec):
    book = Workbook()
    book.remove(book.active)
    book.properties.title, book.properties.subject, book.properties.creator = spec["titel"], spec["zweck"], "Klotzkette"
    border = Border(bottom=Side(style="hair", color="BBC9CC"))
    for sheet in spec["blaetter"]:
        name, columns = sheet["titel"], sheet["spalten"]
        if not name or len(name) > 31 or name.casefold() in {n.casefold() for n in book.sheetnames}:
            raise ValueError(f"Ungültiger Blattname: {name!r}")
        formulas, formats = sheet.get("formeln", {}), sheet.get("formate", {})
        if len(columns) < 2 or len(set(columns)) != len(columns) or (formulas.keys() | formats.keys()) - set(columns):
            raise ValueError(f"Mehrdeutige oder unbekannte Spalten in {name}")
        count = sheet.get("zeilen", 15)
        if not 1 <= count <= 1000:
            raise ValueError(f"Ungültige Anzahl Eingabezeilen in {name}")
        ws = book.create_sheet(name)
        end = get_column_letter(len(columns))
        ws.sheet_view.showGridLines = False
        ws.freeze_panes = "A5"
        for row, value in ((1, spec["titel"]), (2, spec["zweck"])):
            ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=len(columns))
            cell = ws.cell(row, 1, value)
            cell.font = Font(name=FONT, size=14 if row == 1 else 11, bold=row == 1, color=INK)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        ws.row_dimensions[1].height, ws.row_dimensions[2].height = 32, 48
        ws.row_dimensions[4].height = 40
        for col, label in enumerate(columns, 1):
            header = ws.cell(4, col, label)
            header.font = Font(name=FONT, size=11, bold=True, color="FFFFFF")
            header.fill = PatternFill("solid", fgColor=ACCENT)
            header.alignment = Alignment(wrap_text=True, vertical="center")
            ws.column_dimensions[get_column_letter(col)].width = min(38, max(18, len(label) * 0.82))
            for row in range(5, 5 + count):
                cell = ws.cell(row, col)
                if label in formulas:
                    formula = formulas[label]
                    if not formula.startswith("="):
                        raise ValueError(f"Excel-Formel fehlt für {name}/{label}")
                    cell.value = formula.format(r=row)
                    cell.fill = PatternFill("solid", fgColor=PALE)
                cell.font = Font(name=FONT, size=11, color=INK)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                cell.number_format = formats.get(label, "General")
                cell.border = border
        for row in range(5, 5 + count):
            ws.row_dimensions[row].height = 24
        ws.auto_filter.ref = f"A4:{end}{4 + count}"
        ws.print_title_rows = "1:4"
        ws.page_margins.left = ws.page_margins.right = 0.35
        ws.page_margins.top = ws.page_margins.bottom = 0.48
        ws.page_margins.header = ws.page_margins.footer = 0.22
        ws.page_setup.orientation, ws.page_setup.paperSize = "landscape", ws.PAPERSIZE_A4
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
        ws.oddFooter.right.text = "Seite &P / &N"
    return office_bytes(book)


def build_outputs(root):
    sources = root / SOURCES
    general = read_json(sources / "asset-deal.json")
    general_name = GENERAL + ".docx"
    if filename(general) != general_name:
        raise ValueError("Der Dateiname des gemeinsamen APA muss erhalten bleiben.")
    common = word_document(general)
    titles = case_list(root)
    files = list((sources / "faelle").glob("*.json"))
    cases = {p.stem for p in files}
    expected = {slug for slug, _ in titles}
    if cases != expected:
        raise ValueError(f"Fachvorlagen fehlen: {sorted(expected - cases)}; unerwartete Akten: {sorted(cases - expected)}")
    outputs = {}
    members = {f"Gemeinsam/{general_name}": common}
    guide = [NOTICE_TEXT.rstrip(), "", "ARBEITSVORLAGEN FÜR INSOLVENZAKTEN", "",
             "Die gemeinsame Vertragsvorlage steht unter Gemeinsam/. Die Fachvorlagen stehen unter Akten/.",
             "Für eine Akte den gemeinsamen Vertrag und die unten genannten Dateien in einen Arbeitsordner kopieren.",
             "In Word die Angaben in eckigen Klammern ersetzen und Tabellen bearbeiten.",
             "In Excel die freien Zellen befüllen. Farblich hinterlegte Rechenfelder enthalten Formeln.",
             "Die Datei SHA256SUMS.txt enthält die Prüfsummen der Vorlagen und dieses Inhaltsverzeichnisses.",
             "", f"Gemeinsamer Vertrag: Gemeinsam/{general_name}", "", "AKTENVERZEICHNIS"]
    for number, (slug, title) in enumerate(titles, 1):
        folder = Path("testakten") / slug / "Arbeitsvorlagen"
        outputs[folder / general_name] = common
        specs = read_json(sources / "faelle" / (slug + ".json"))
        specs = specs if isinstance(specs, list) else [specs]
        if not specs:
            raise ValueError(f"{slug}: Fachvorlage fehlt")
        guide.extend(["", f"{number}. {title}"])
        for spec in specs:
            name = filename(spec)
            if folder / name in outputs:
                raise ValueError(f"{slug}: doppelte Vorlage {name}")
            data = spreadsheet(spec) if name.endswith(".xlsx") else word_document(spec)
            outputs[folder / name] = data
            relative = f"Akten/{slug}/{name}"
            members[relative] = data
            guide.extend([spec["titel"], relative])
    index = ("\n".join(guide) + "\n").encode("utf-8")
    collection = {NOTICE_FILENAME: index, **members}
    collection["SHA256SUMS.txt"] = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n" for name, data in sorted(collection.items())
    ).encode("utf-8")
    outputs[COLLECTION] = archive(collection)
    return outputs


def publish(root, outputs, check):
    errors = []
    for folder in {path.parent for path in outputs if path.parent.name == "Arbeitsvorlagen"}:
        if (root / folder).exists():
            errors.extend(f"Unerwartete Vorlage: {file.relative_to(root)}" for file in (root / folder).iterdir()
                          if file.relative_to(root) not in outputs)
    if errors and not check:
        raise ValueError("\n".join(errors))
    for relative, data in outputs.items():
        path = root / relative
        if path.is_file() and path.read_bytes() == data:
            continue
        if check:
            errors.append(f"Fehlt oder weicht von der Quelle ab: {relative}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
            temporary.write(data)
        os.chmod(temporary.name, 0o644)
        os.replace(temporary.name, path)
    if errors:
        raise ValueError("\n".join(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Vorhandene Dateien ohne Schreibzugriff vergleichen.")
    args = parser.parse_args()
    try:
        outputs = build_outputs(ROOT)
        publish(ROOT, outputs, args.check)
    except (KeyError, ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(f"{len(outputs) - 1} Arbeitsvorlagen und ein Sammel-ZIP {'geprüft' if args.check else 'bereitgestellt'}.")


if __name__ == "__main__":
    main()

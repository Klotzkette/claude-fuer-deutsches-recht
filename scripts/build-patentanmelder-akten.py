#!/usr/bin/env python3
"""Baut die drei Übungsakten für Patentanmeldungen samt getrennter Auswertung."""
import argparse
from importlib import import_module
import io
import json
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.graphics import renderPDF, renderSVG
from reportlab.graphics.shapes import Circle, Drawing, Line, PolyLine, Rect, String
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from akteneingang.ausgabe import archive
from akteneingang.quellen import safe_member
from aktenarbeit_einstiege import mit_verweisen
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, NOTICE_MARKDOWN

# Reuse the native Word/Excel/mail and searchable reading formats already shipped with Interstate.
forms = import_module("build-interstate-testakten")
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/patentanmelder"
FOLDER = ROOT / "patentrecht/Patentanmelder"
COLLECTION = ROOT / "docs/downloads/patentanmelder-werkstatt-testakten.zip"
PHASES = ("Grundakte", "Nachreichungen")
CONTACT_NOTE = ("<!-- reserved-example-contacts -->\n"
                "Die E-Mail-Adressen mit der Endung `.example` sind fiktive Kontakte der Übung.")
INK = colors.HexColor("#1D333A")
TEAL = colors.HexColor("#205D63")
MUTED = colors.HexColor("#53666C")
PALE = colors.HexColor("#C9D7D8")


def figure(doc, case):
    """Render the same labelled, editable vector geometry to SVG and a single A4 PDF."""
    shape = doc["figur"]
    refs = shape["bezugszeichen"]
    if not shape["linien"] or not refs or len({str(r[0]) for r in refs}) != len(refs):
        raise ValueError(f'{doc["datei"]}: Geometrie und eindeutige Bezugszeichen werden benötigt')
    for x, y in (point for line in shape["linien"] for point in line):
        if not (0 <= x <= 700 and 0 <= y <= 360):
            raise ValueError(f'{doc["datei"]}: Punkt außerhalb der Zeichenfläche')
    for _, _, x, y, tx, ty in refs:
        if not (0 <= min(x, tx) <= max(x, tx) <= 700 and 0 <= min(y, ty) <= max(y, ty) <= 360):
            raise ValueError(f'{doc["datei"]}: Bezugszeichen außerhalb der Zeichenfläche')
    title = simpleSplit(doc["titel"], "Helvetica-Bold", 20, 690)
    parties = simpleSplit(f'{doc["von"]}   ·   An {doc["an"]}', "Helvetica", 10, 700)
    notes = [simpleSplit(t, "Helvetica", 12, 692) for t in doc["text"]]
    header = 48 + 24 * len(title) + 12 * len(parties)
    legend_y = header + 380
    legend = []
    for i in range(0, len(refs), 2):
        row = [(str(number), simpleSplit(label, "Helvetica", 12, 290))
               for number, label, *_ in refs[i:i+2]]
        legend.append(row)
    legend_height = sum(max(len(lines) for _, lines in row) * 16 + 8 for row in legend)
    height = legend_y + 51 + legend_height + sum(15 * len(lines) + 6 for lines in notes)
    sheet = Drawing(756, height)

    def caption(x, y, text, font="Helvetica", size=12, color=INK, align="start"):
        sheet.add(String(x, height - y, text, fontName=font, fontSize=size, fillColor=color, textAnchor=align))

    caption(28, 26, f'{case["zeichen"]}   ·   {forms.german_date(doc)}', size=10, color=MUTED)
    caption(728, 26, "TECHNISCHE ZEICHNUNG", size=10, color=MUTED, align="end")
    for i, line in enumerate(title):
        caption(28, 59 + 24 * i, line, "Helvetica-Bold", 20, TEAL)
    for i, line in enumerate(parties):
        caption(28, header - 9 - 12 * (len(parties)-1-i), line, size=10, color=MUTED)
    sheet.add(Rect(28, height-header-360, 700, 360, strokeColor=PALE, strokeWidth=0.8, fillColor=None))
    for line in shape["linien"]:
        points = [a for x, y in line for a in (28+x, height-header-y)]
        sheet.add(PolyLine(points, strokeColor=INK, strokeWidth=2.2, fillColor=None))
    for x, y, radius in shape.get("kreise", []):
        if radius <= 0 or x-radius < 0 or x+radius > 700 or y-radius < 0 or y+radius > 360:
            raise ValueError(f'{doc["datei"]}: ungültiger Kreis')
        sheet.add(Circle(28+x, height-header-y, radius, strokeColor=INK, strokeWidth=2, fillColor=None))
    for number, _, x, y, tx, ty in refs:
        sheet.add(Line(28+x, height-header-y, 28+tx, height-header-ty, strokeColor=TEAL, strokeWidth=0.9))
        sheet.add(Circle(28+tx, height-header-ty, 11, fillColor=colors.white, strokeColor=TEAL, strokeWidth=0.9))
        caption(28+tx, header+ty+4, str(number), "Helvetica-Bold", 11, TEAL, "middle")
    caption(28, legend_y, "BEZUGSZEICHEN", "Helvetica-Bold", 10, TEAL)
    cursor = legend_y + 23
    for row in legend:
        for i, (number, lines) in enumerate(row):
            x = 28 + i * 358
            caption(x, cursor, number, "Helvetica-Bold", 12, TEAL)
            for j, line in enumerate(lines):
                caption(x+32, cursor+16*j, line)
        cursor += max(len(lines) for _, lines in row) * 16 + 8
    for lines in notes:
        for line in lines:
            caption(28, cursor+8, line)
            cursor += 15
        cursor += 6
    svg = renderSVG.drawToString(sheet)
    svg = svg.replace("<title>...</title>", f'<title>{escape(doc["titel"])}</title>', 1)
    svg = svg.replace("<desc>...</desc>", f'<desc>{escape(" ".join(doc["text"]))}</desc>', 1)
    page = A4 if sheet.height > 1.1 * sheet.width else landscape(A4)
    out = io.BytesIO()
    canvas = Canvas(out, pagesize=page, invariant=1)
    canvas.setTitle(doc["titel"])
    canvas.setAuthor(doc["von"])
    canvas.setSubject("Technische Zeichnung")
    scale = min((page[0]-32)/sheet.width, (page[1]-32)/sheet.height)
    canvas.translate((page[0]-scale*sheet.width)/2, page[1]-16-scale*sheet.height)
    canvas.scale(scale, scale)
    renderPDF.draw(sheet, canvas, 0, 0)
    canvas.showPage()
    canvas.save()
    return svg.encode("utf-8"), out.getvalue()


def brief(case, title, sections, label):
    """A4 case cover and teaching notes. The solution is a separate PDF."""
    out = io.BytesIO()
    pdf = SimpleDocTemplate(out, pagesize=A4, leftMargin=53, rightMargin=53, topMargin=65,
                            bottomMargin=51, invariant=1, title=title, author="Patentanmelder-Werkstatt")
    heading = ParagraphStyle("Titel", fontName="Times-Bold", fontSize=23, leading=27,
                             textColor=TEAL, spaceAfter=18, keepWithNext=True)
    sub = ParagraphStyle("Abschnitt", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
                         textColor=TEAL, spaceBefore=9, spaceAfter=5, keepWithNext=True)
    story = [Paragraph(escape(title), heading)]
    for name, text in sections:
        story.append(Paragraph(escape(name), sub))
        story.extend(forms.paragraph(p, size=11, leading=15) for p in text)

    def furniture(c, page):
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 9)
        c.drawString(53, 803, case["zeichen"])
        c.drawRightString(A4[0]-53, 803, label)
        c.setStrokeColor(PALE)
        c.line(53, 793, A4[0]-53, 793)
        c.line(53, 38, A4[0]-53, 38)
        c.drawRightString(A4[0]-53, 25, f"Blatt {page.page}")

    pdf.build(story, onFirstPage=furniture, onLaterPages=furniture)
    return out.getvalue()


def case_files(case, slug):
    stem = "testakte-" + slug
    combined = f"gesamt-pdf/{stem}_gesamt.pdf"
    original_zip = f"downloads/{stem}.zip"
    single_zip = f"downloads/{stem}-einzelpdfs.zip"
    answer = "Auswertung/Erwartungshorizont.pdf"
    guide = [f'# {case["titel"]}', "", f'**{case["zeichen"]}**', "", case["einstieg"], "",
             "## Erste Bearbeitung", "", case["auftrag"], "", "## Downloads", "", CONTACT_NOTE, "",
             NOTICE_MARKDOWN, "", "| Gesamtakte | Originalunterlagen | Einzel-PDFs | Nachbesprechung |",
             "| --- | --- | --- | --- |",
             f"| [Gesamt-PDF mit Lesezeichen]({combined}) | [Originalformat-ZIP]({original_zip}) | "
             f"[Einzel-PDF-ZIP]({single_zip}) | [Erwartungshorizont]({answer}) |"]
    originals, singles = {}, {}
    writer = PdfWriter()
    cover = brief(case, case["titel"], [("Ausgangslage", [case["einstieg"]]),
                  ("Arbeitsauftrag", [case["auftrag"]]),
                  ("Unterlagen", ["Bearbeiten Sie zuerst die Grundakte. Öffnen Sie die Nachreichungen "
                                  "nach Ihrer ersten Einschätzung. Über die PDF-Lesezeichen gelangen Sie zu "
                                  "den einzelnen Unterlagen beider Bearbeitungsstände."])], "Arbeitsakte")
    writer.append(PdfReader(io.BytesIO(cover)), import_outline=False)
    writer.add_outline_item(title="Einstieg und Arbeitsauftrag", page_number=0)
    docs = case["dokumente"]
    if {d["phase"] for d in docs} != set(PHASES):
        raise ValueError(f"{slug}: Grundakte und Nachreichungen erforderlich")
    for phase in PHASES:
        guide.extend(["", f"## {phase}", ""])
        if phase == "Nachreichungen":
            guide.extend([case["nachreichung"], ""])
        guide.extend(["| Datum | Unterlage | Format |", "| --- | --- | --- |"])
        parent = None
        for doc in (d for d in docs if d["phase"] == phase):
            name = safe_member(doc["datei"])
            key = f"{phase}/{name}"
            single = phase + "__" + Path(name).stem + ".pdf"
            if "/" in name or key in originals or single in singles:
                raise ValueError(f"{slug}: ungültiger oder doppelter Aktenpfad {key}")
            if Path(name).suffix == ".svg":
                native, pdf = figure(doc, case)
            else:
                native = forms.native(doc, case, key, None)
                pdf = forms.reading(doc, case, key, None)
            originals[key], singles[single] = native, pdf
            page = len(writer.pages)
            writer.append(PdfReader(io.BytesIO(pdf)), import_outline=False)
            if parent is None:
                parent = writer.add_outline_item(title=phase, page_number=page)
            writer.add_outline_item(title=doc["titel"], page_number=page, parent=parent)
            label = doc["titel"].replace("|", "\\|")
            guide.append(f'| {forms.german_date(doc)} | [{label}]({quote(key)}) | {Path(name).suffix[1:].upper()} |')
    guide.extend(["", "## Rechtsquellen", ""])
    guide.extend(f"- [{name}]({url})" for name, url in case["quellen"])
    guide.extend(["", "[Alle Patentanmelder-Akten](../README.md)", ""])
    out = io.BytesIO()
    writer.add_metadata({"/Title": case["titel"], "/Subject": case["zeichen"]})
    writer.write(out)
    writer.close()
    expectations = [(s["titel"], s["text"]) for s in case["erwartung"]]
    if not expectations:
        raise ValueError(f"{slug}: Erwartungshorizont fehlt")
    solution = brief(case, case["titel"], expectations, "Erwartungshorizont")
    files = {**originals, original_zip: archive({NOTICE_FILENAME: NOTICE_BYTES, **originals}),
             single_zip: archive({NOTICE_FILENAME: NOTICE_BYTES, **singles}), combined: out.getvalue(),
             answer: solution, "README.md": mit_verweisen("\n".join(guide), (FOLDER / slug / "README.md").relative_to(ROOT), ["patentanmelder-" + slug]).encode()}
    return files


def write_or_check(path, data, check):
    if path.is_file() and path.read_bytes() == data:
        return
    if check:
        raise ValueError(f"Fehlend oder abweichend: {path.relative_to(ROOT)}")
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Alle gelieferten Dateien byteweise neu prüfen")
    args = parser.parse_args()
    sources = sorted(DATA.glob("*.json"))
    if [s.stem[:3] for s in sources] != ["01-", "02-", "03-"]:
        parser.error("Die Quellen zu den drei Akten 01 bis 03 werden benötigt.")
    index = ["# Werkstatt für Patentanmelder", "",
             "Bearbeiten Sie jeden Fall in zwei Runden. Die Grundakte enthält die erste Fassung und ihre "
             "Belege. Die Nachreichungen ergänzen den Sachverhalt. Den Erwartungshorizont finden Sie auf "
             "der jeweiligen Fallseite unter „Nachbesprechung“.", "", "## Fallauswahl", "",
             "| Fall | Einstieg |", "| --- | --- |"]
    package = {NOTICE_FILENAME: NOTICE_BYTES}
    manual = ["", "Werkstatt für Patentanmelder", "",
              "Beginnen Sie mit der Grundakte und bearbeiten Sie die Nachreichungen in einer zweiten Runde. "
              "Auswertung/Erwartungshorizont.pdf dient der anschließenden Besprechung."]
    for source in sources:
        slug = source.stem
        case = json.loads(source.read_bytes())
        files = case_files(case, slug)
        folder = FOLDER / slug
        unexpected = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()} - files.keys()
        if unexpected:
            raise ValueError(f"{slug}: zusätzliche Dateien {sorted(unexpected)}")
        for rel, content in files.items():
            write_or_check(folder / rel, content, args.check)
            if rel.startswith((*PHASES, "gesamt-pdf/", "Auswertung/")) or rel.endswith("-einzelpdfs.zip"):
                package[f"{slug}/{rel}"] = content
        index.append(f'| [{case["titel"]}]({slug}/README.md) | {case["einstieg"].replace("|", "&#124;")} |')
        manual.extend(["", f'{slug} · {case["titel"]}', case["zeichen"], "", case["einstieg"], "",
                       case["auftrag"], "", case["nachreichung"], "", "Rechtsquellen"])
        manual.extend(f"{label} · {url}" for label, url in case["quellen"])
        print(f'{slug}: {len(case["dokumente"])} Aktenstücke')
    target = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/" + COLLECTION.relative_to(ROOT).as_posix()
    index.extend(["", "## Sammlung herunterladen", "", NOTICE_MARKDOWN, "",
                  f"[Alle drei Akten mit Auswertung als ZIP]({target})", "", "[Zum Plugin Patentrecht](../README.md)", ""])
    package[NOTICE_FILENAME] += ("\n".join(manual) + "\n").encode()
    write_or_check(FOLDER / "README.md", "\n".join(index).encode(), args.check)
    write_or_check(COLLECTION, archive(package), args.check)
    print(COLLECTION.relative_to(ROOT))


if __name__ == "__main__":
    main()

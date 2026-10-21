#!/usr/bin/env python3
"""Rendert vier einzeln redigierte Sanktionsakten in drei deckungsgleichen Formaten."""

from collections import Counter
from datetime import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/sanktionen-akten.json"
TAG = "sanktionen-eu-us-v1.0.0"
BASE = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}"
PLUGINS = ("eu-sanktionspruefer", "us-sanktionspruefer")
CASES = {
    "sanktionen-eu-zwirnmark-beteiligung": PLUGINS[0],
    "sanktionen-eu-faltenfels-mandat": PLUGINS[0],
    "sanktionen-us-klingelgau-eigentum": PLUGINS[1],
    "sanktionen-us-sonnenquast-namensgleichheit": PLUGINS[1],
}


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def validate_data(cases):
    if len(cases) != 4 or {case["slug"]: case["plugin"] for case in cases} != CASES:
        raise ValueError("Vier bestimmte Akten mit eindeutiger EU-/US-Zuordnung erforderlich")
    for case in cases:
        files = case["files"]
        names = [item["name"] for item in files]
        if len(files) != 12 or len(set(names)) != 12 or len({Path(n).stem for n in names}) != 12:
            raise ValueError(f"Zwölf kollisionsfreie Originale erforderlich: {case['slug']}")
        if Counter(Path(name).suffix for name in names) != {".docx": 5, ".eml": 4, ".csv": 2, ".txt": 1}:
            raise ValueError(f"Originalformate stimmen nicht: {case['slug']}")
        if not any(item.get("attachments") for item in files):
            raise ValueError("Mindestens eine echte Mailanlage erforderlich")
        listed = []
        for item in files:
            name = item["name"]
            if not re.fullmatch(r"[0-9]{2}_[A-Za-z0-9_]+\.(docx|eml|csv|txt)", name):
                raise ValueError(f"Ungültiger Originalname: {name}")
            date = item["date"][:10]
            parsed = datetime.strptime(date, "%Y-%m-%d" if "-" in date else "%d.%m.%Y").date()
            if parsed.isoformat() > "2026-10-21":
                raise ValueError(f"Dokument nach Aktenstichtag: {name}")
            if Path(name).suffix == ".csv":
                rows = item["rows"]
                if len(rows) < 7 or any(len(row) != len(rows[0]) for row in rows):
                    raise ValueError(f"Tabellenzeilen oder Spalten inkonsistent: {name}")
            else:
                minimum = {".docx": 1000, ".eml": 450, ".txt": 650}[Path(name).suffix]
                if len(item["body"]) < minimum:
                    raise ValueError(f"Unvollständiges Aktenstück: {name}")
                if "KEIN RECHTSAKT" in item["body"]:
                    listed.append(item)
                if "§" in item["body"]:
                    raise ValueError(f"Paragraf ausschreiben: {name}")
            if Path(name).suffix == ".eml":
                if datetime.fromisoformat(item["date"]).utcoffset() is None:
                    raise ValueError(f"Mail ohne Zeitzone: {name}")
                for address in re.findall(r"[\w.+-]+@[^\s>]+", item["author"] + " " + item["to"] + " " + item.get("cc", "")):
                    if not address.endswith(".example"):
                        raise ValueError(f"Nicht reservierte Mailadresse: {address}")
                for attachment in item.get("attachments", []):
                    source = next((value for value in files if value["name"] == attachment), None)
                    if source is None or not attachment.endswith(".docx"):
                        raise ValueError(f"Fehlende Mailanlage: {attachment}")
                    if datetime.strptime(source["date"], "%d.%m.%Y").date() > parsed:
                        raise ValueError(f"Mailanlage aus der Zukunft: {name}/{attachment}")
                if item.get("reply_to") and item["reply_to"] not in names:
                    raise ValueError(f"Mailbezug fehlt: {name}")
        if not listed or any("NOT A LEGAL ACT" not in item["body"] for item in listed):
            raise ValueError("Erfundener Listungsbeschluss ohne zweisprachige Fiktionskennzeichnung")


def download_table(case, local=False):
    slug = case["slug"]
    pdf = f"gesamt-pdf/{slug}_gesamt.pdf" if local else f"{BASE}/{slug}_gesamt.pdf"
    return f"""{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamtakte]({pdf}) |
| Einzel-PDF-ZIP / Individual PDFs | [Einzelne Unterlagen]({BASE}/testakte-{slug}-einzelpdfs.zip) |
| Akten-ZIP / Native documents | [DOCX, EML, CSV und TXT]({BASE}/testakte-{slug}.zip) |"""


def render_table_pdf(item, slug, renderer):
    widths = {
        "10_Anteile.csv": [135, 50, 120, 80, 60, 235],
        "11_Auftragspositionen.csv": [55, 190, 55, 90, 100, 220],
        "10_Zeiterfassung.csv": [80, 175, 55, 75, 85, 240],
        "11_Lieferkalkulation.csv": [55, 190, 55, 90, 100, 220],
        "10_Ownership.csv": [150, 55, 75, 55, 240, 135],
        "11_Order_Lines.csv": [92, 165, 55, 65, 75, 75, 200],
        "10_Spendeneingaenge.csv": [85, 65, 160, 90, 90, 220],
        "11_Kontaktablage.csv": [125, 100, 80, 145, 160, 140],
    }[item["name"]]
    body = ParagraphStyle("TableBody", fontName="CISGTimes", fontSize=10, leading=13)
    numeric = ParagraphStyle("TableNumber", parent=body, alignment=TA_RIGHT)
    heading = ParagraphStyle("TableHeading", parent=body, fontName="CISGTimes-Bold")
    title = ParagraphStyle("TableTitle", parent=heading, fontSize=15, leading=18, spaceAfter=12)
    rows = []
    for index, row in enumerate(item["rows"]):
        cells = []
        for cell in row:
            style = heading if index == 0 else numeric if re.fullmatch(r"\d+(?:,\d+)?", cell) else body
            cells.append(Paragraph(escape(cell), style))
        rows.append(cells)
    table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8edf0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f7f7")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9d9d9")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    flow = [Paragraph(escape(item["author"]), body), Spacer(1, 7),
            Paragraph(escape(item["title"]), title),
            Paragraph(escape(item["date"] + " | " + item["name"]), body), Spacer(1, 9),
            Paragraph(escape(item["body"]), body), Spacer(1, 15), table]
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4), leftMargin=40, rightMargin=40,
                            topMargin=40, bottomMargin=40, title=item["title"], author="Klotzkette")

    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont("CISGTimes", 8)
        canvas.drawString(40, 23, slug)
        canvas.drawRightString(landscape(A4)[0] - 40, 23, f"Seite {document.page}")
        canvas.restoreState()

    doc.build(flow, onFirstPage=footer, onLaterPages=footer, canvasmaker=renderer.G.invariant_canvas)
    return buffer.getvalue()


def build():
    cases = json.loads(DATA.read_text(encoding="utf-8"))
    validate_data(cases)
    shared = module("build-cisg-akten")
    basis = shared.load_renderer()
    basis.STAMP = datetime(2026, 10, 21, 8)
    renderer = basis.module("build-testakten-einzelpdf-zips")
    shared.configure_text_fonts(renderer)
    report = []
    for case in cases:
        slug, plugin = case["slug"], case["plugin"]
        directory = ROOT / "testakten" / slug
        downloads = ROOT / plugin / "downloads"
        directory.mkdir(parents=True, exist_ok=True)
        downloads.mkdir(parents=True, exist_ok=True)
        paths = [directory / item["name"] for item in case["files"]]
        for mail_pass in (False, True):
            for path, item in zip(paths, case["files"]):
                if (path.suffix == ".eml") == mail_pass:
                    basis.write_original(path, item, slug)
                    if mail_pass:
                        shared.enrich_mail(path, item, slug)
        cache = render_office_batch(paths)
        missing = [p.name for p in paths if p.suffix == ".docx" and p not in cache]
        if missing:
            raise RuntimeError(f"Layoutgetreues Office-PDF fehlt, kein Textfallback: {missing}")
        notice = NOTICE_BYTES + ("\nAlle Personen, Unternehmen, Staaten, Organisationen und Listungen sind erfunden. "
                                 "Die Listungsdokumente sind keine Rechtsakte und dürfen nicht in echte Prüfungen übernommen werden.\n"
                                 "All parties, countries, organisations and designations are fictional. "
                                 "The designation documents have no legal effect and must not be used for real screening.\n").encode()
        originals, singles = {"README.txt": notice}, {"README.txt": notice}
        writer, documents = PdfWriter(), []
        for path, item in zip(paths, case["files"]):
            pdf = render_table_pdf(item, slug, renderer) if path.suffix == ".csv" else renderer.render_document_pdf(path, directory, cache)
            reader = PdfReader(io.BytesIO(pdf))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if not text.strip() or "Diese Testakte wurde mit KI" in text:
                raise ValueError(f"Leeres PDF oder allgemeiner Warntext im PDF: {path.name}")
            if "KEIN RECHTSAKT" in item.get("body", "") and "KEIN RECHTSAKT" not in text:
                raise ValueError(f"Fiktionskennzeichnung im Listungs-PDF verloren: {path.name}")
            start = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
            writer.add_outline_item(path.name, start)
            originals[path.name] = path.read_bytes()
            singles[path.stem + ".pdf"] = pdf
            documents.append({"file": path.name, "pages": len(reader.pages), "start_page": start + 1,
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        writer.add_metadata({"/Title": case["title"], "/Author": "Klotzkette",
                             "/CreationDate": "D:20261021080000Z", "/ModDate": "D:20261021080000Z"})
        total = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        total.parent.mkdir(exist_ok=True)
        with total.open("wb") as stream:
            writer.write(stream)
        for suffix, entries in (("", originals), ("-einzelpdfs", singles)):
            (downloads / f"testakte-{slug}{suffix}.zip").write_bytes(basis.archive_bytes(entries))
        rows = "\n".join(f"| [{item['name']}]({item['name']}) | {item['title']} | {doc['pages']} |"
                         for item, doc in zip(case["files"], documents))
        (directory / "README.md").write_text(f"""# 1. {case['title']}

{case['summary']}

[Alle Akten](../README.md) · [Repository](../../README.md) · [Download-Index](../../ASSET_INDEX.md)

## 1.1. Benutzung und Einordnung

Zwölf eigenständige Geschäftsunterlagen mit {len(writer.pages)} PDF-Seiten, Stand 21.10.2026. Fünf Word-Dokumente, vier E-Mails mit echten MIME-Anlagen, zwei Datentabellen und ein Gesprächsauszug bilden denselben Bestand in drei Formaten ab. Keine Musterlösung und keine vorweggenommene rechtliche Bewertung.

<!-- reserved-example-contacts -->

Sämtliche Personen, Unternehmen, Länder, Vereinigungen, Kontakte und Listungen sind erfunden. Auch die angeblichen EU- oder US-Listungsbeschlüsse sind ausdrücklich erfundene Schulungsdokumente ohne Rechtswirkung. Sie haben keine echten Amtsblatt-, Register- oder Behördenkennungen. Niemals in produktive Trefferlisten übernehmen. Reservierte .example-Adressen sind nicht erreichbar. Die rechtlichen Prüfkriterien stehen getrennt im Plugin; ein erfundener Listenstand belegt keine reale Sanktion.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{download_table(case, local=True)}

<!-- END gesamt-pdf-section (autogen) -->

Beide ZIPs sind flach. Im Original-ZIP liegen nur die zwölf Originalunterlagen und README.txt, kein Markdown und kein zusätzliches Gesamt-PDF. Das Einzel-PDF-ZIP enthält genau ein PDF je Original und README.txt. Mehrseitige Dokumente bleiben zusammen. E-Mail-Anlagen sind zusätzlich als Original enthalten und werden nicht doppelt als PDF gezählt. Der allgemeine Warnhinweis steht auf dieser Downloadseite und in den ZIP-READMEs; die Fiktionskennzeichnung der erfundenen Listungsdokumente bleibt dagegen auch im PDF erhalten.

## 1.3. Unterlagen

| Datei | Gegenstand | Seiten |
| --- | --- | ---: |
{rows}

## 1.4. English Guide

Twelve separate business records, four email messages with actual attachments, two data tables and a conversation extract. All parties, countries and designations are invented. The conspicuously marked designation records are not EU or US legal acts. Do not import them into real screening systems. Choose the combined reading PDF or either flat archive; there is no answer key.

[Zum Plugin](../../{plugin}/README.md) · [Weitere Akten dieses Plugins](../../{plugin}/testakte/README.md). Downloadstand `{TAG}`.
""", encoding="utf-8")
        report.append({"slug": slug, "documents": len(paths), "pages": len(writer.pages), "files": documents})
        print(f"{slug}: {len(paths)} Originale, {len(writer.pages)} Seiten", flush=True)
    for plugin in PLUGINS:
        own = [case for case in cases if case["plugin"] == plugin]
        sections = "\n\n".join(f"## 1.{i}. {case['title']}\n\n{case['summary']}\n\n"
                                  f"[Unterlagenverzeichnis](../../testakten/{case['slug']}/README.md)\n\n"
                                  + download_table(case) for i, case in enumerate(own, 1))
        (ROOT / plugin / "testakte/README.md").write_text(f"""# 1. Sanktionsprüfung mit erfundenen Geschäftsunterlagen

Zwei eigenständige Akten für Unternehmen und Kanzleien, mit jeweils zwölf Originalen. Alle Personen, Staaten und Listungen sind frei erfunden. Die Listungsdokumente tragen eine auffällige Kennzeichnung und sind keine echten Rechtsakte. Keine Musterlösung und keine Einordnung der Fantasienamen als reale Sanktionierte. Aktenstand 21.10.2026.

[Plugin](../README.md) · [Alle Akten](../../testakten/README.md) · [Repository](../../README.md) · [Download-Index](../../ASSET_INDEX.md)

<!-- reserved-example-contacts -->

Originalformat-ZIP und Einzel-PDF-ZIP sind flach; README.txt enthält den zweisprachigen Warnhinweis. Die PDFs enthalten keinen allgemeinen Warnvorspann, wohl aber die inhaltlich erforderliche Kennzeichnung erfundener Listungsdokumente.

English: Fictional compliance training records, never evidence of an actual designation. The two flat archives and combined PDF contain the same source documents. All contact domains are reserved examples. No answer key is included.

{sections}
""", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()

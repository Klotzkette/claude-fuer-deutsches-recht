#!/usr/bin/env python3
"""Baut drei redaktionelle CISG-Akten mit den bestehenden Aktenrenderern."""

from collections import Counter
from datetime import datetime
from email import policy
from email.parser import BytesParser
from email.utils import format_datetime, getaddresses
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table
from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/cisg-akten.json"
TARGET = ROOT / "un-kaufrecht-cisg/testakte"
TAG = "un-kaufrecht-cisg-v1.0.0"
BASE = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}"
CUTOFF = "2026-10-18"
SLUGS = {
    "cisg-klauselkollision-pumpen-bremen-lyon",
    "cisg-transportschaden-sensoren-ulm-turin",
    "cisg-maschinenlieferung-nachbesserung-leipzig-brno",
}


def load_renderer():
    path = ROOT / "scripts/build-untersuchungshaft-akten.py"
    spec = importlib.util.spec_from_file_location("cisg_basis", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.STAMP = datetime(2026, 10, 18, 8)
    return module


def validate_data(cases):
    if {case["slug"] for case in cases} != SLUGS or len(cases) != 3:
        raise ValueError("Genau die drei beauftragten Akten sind erforderlich")
    for case in cases:
        files = case["files"]
        names = [item["name"] for item in files]
        if len(files) != 16 or len(set(names)) != 16:
            raise ValueError(f"{case['slug']}: 16 eindeutige Originale erforderlich")
        if len({Path(name).stem for name in names}) != 16:
            raise ValueError("Kollision der Einzel-PDF-Namen")
        if not any(item.get("attachments") for item in files):
            raise ValueError("Echte MIME-Anlage fehlt")
        for item in files:
            name = item["name"]
            suffix = Path(name).suffix
            if not re.fullmatch(r"[0-9]{2}_[A-Za-z0-9_]+\.(docx|eml|csv|txt)", name):
                raise ValueError(f"Ungültiger Dateiname: {name}")
            date = item["date"][:10]
            parsed = datetime.strptime(date, "%Y-%m-%d" if "-" in date else "%d.%m.%Y")
            if parsed.date().isoformat() > CUTOFF:
                raise ValueError(f"Dokument nach Aktenstichtag: {name}")
            if suffix == ".csv":
                rows = item["rows"]
                if len(rows) < 7 or any(len(row) != len(rows[0]) for row in rows):
                    raise ValueError(f"CSV zu kurz oder inkonsistent: {name}")
            elif not item.get("body", "").strip():
                raise ValueError(f"Leeres Dokument: {name}")
            for attachment in item.get("attachments", []):
                if attachment not in names or not attachment.endswith(".docx"):
                    raise ValueError(f"Fehlende Anlage: {attachment}")
                source = next(value for value in files if value["name"] == attachment)
                if datetime.strptime(source["date"], "%d.%m.%Y").date() > parsed.date():
                    raise ValueError(f"Anlage erst nach Maildatum entstanden: {name}/{attachment}")
            if suffix == ".eml":
                date = datetime.fromisoformat(item["date"])
                if date.utcoffset() is None:
                    raise ValueError(f"Zeitzone fehlt: {name}")
                for _, address in getaddresses([item["author"], item["to"], item.get("cc", "")]):
                    if not address.endswith(".example"):
                        raise ValueError(f"Nicht reservierte Mailadresse: {address}")


def configure_text_fonts(renderer):
    directory = Path(os.environ.get("CISG_FONT_DIR", "/System/Library/Fonts/Supplemental"))
    for variant, filename in (("", "Times New Roman.ttf"), ("-Bold", "Times New Roman Bold.ttf"),
                              ("-Italic", "Times New Roman Italic.ttf"),
                              ("-BoldItalic", "Times New Roman Bold Italic.ttf")):
        pdfmetrics.registerFont(TTFont("CISGTimes" + variant, str(directory / filename)))
    pdfmetrics.registerFontFamily("CISGTimes", normal="CISGTimes", bold="CISGTimes-Bold",
                                  italic="CISGTimes-Italic", boldItalic="CISGTimes-BoldItalic")
    pdfmetrics.registerFont(TTFont("AktenLatin", str(directory / "Times New Roman.ttf")))
    renderer.G.FONT_REG, renderer.G.FONT_BOLD = "CISGTimes", "CISGTimes-Bold"
    for value in vars(renderer.G).values():
        if isinstance(value, ParagraphStyle):
            value.fontName = "CISGTimes-Bold" if "Bold" in value.fontName else "CISGTimes"
    for style in (renderer.G.s_body, renderer.G.s_meta, renderer.G.s_record):
        style.fontSize, style.leading = 11, 14
    for style in (renderer.G.s_meta, renderer.G.s_record):
        style.textColor = HexColor("#222222")
    original_csv = renderer.G.csv_to_flowables

    def csv_with_timestamp_column(path):
        flowables = original_csv(path)
        for table in flowables:
            if isinstance(table, Table) and len(table._argW) == 5:
                # Geometrie vor dem ersten Layoutlauf; Inhalt und Stil kommen vom Bestandsrenderer.
                width = sum(table._argW)
                table._argW = table._colWidths = [118] + [(width - 118) / 4] * 4
        return flowables

    renderer.G.csv_to_flowables = csv_with_timestamp_column


def enrich_mail(path, item, slug):
    mail = BytesParser(policy=policy.SMTP).parsebytes(path.read_bytes())
    sender = getaddresses([item["author"]])[0][1]
    recipient = getaddresses([item["to"]])[0][1]
    mail["Reply-To"] = item["author"]
    mail["Return-Path"] = f"<{sender}>"
    mail["Received"] = (
        f"from mail.{sender.split('@')[1]} by mx.{recipient.split('@')[1]} "
        f"with ESMTPS id {slug.split('-')[1]}-{path.stem[:2]}; "
        f"{format_datetime(datetime.fromisoformat(item['date']))}"
    )
    if item.get("cc"):
        mail["Cc"] = item["cc"]
    if item.get("reply_to"):
        reference = f"<{slug}-{Path(item['reply_to']).stem}@akten.example>"
        mail["In-Reply-To"] = reference
        mail["References"] = reference
    if item.get("attachments"):
        mail["X-Attachments"] = ", ".join(item["attachments"])
    path.write_bytes(mail.as_bytes(policy=policy.SMTP.clone(max_line_length=998)))
    parsed = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    for header in ("From", "To", "Date", "Subject", "Message-ID", "MIME-Version", "Content-Type", "Received"):
        if not parsed[header]:
            raise ValueError(f"{path.name}: Header {header} fehlt")
    actual = {part.get_filename(): part.get_payload(decode=True) for part in parsed.iter_attachments()}
    expected = {name: (path.parent / name).read_bytes() for name in item.get("attachments", [])}
    if actual != expected or parsed.defects:
        raise ValueError(f"{path.name}: MIME-Anlagen beschädigt")


def download_table(case, local=False):
    slug = case["slug"]
    total = f"gesamt-pdf/{slug}_gesamt.pdf" if local else f"{BASE}/{slug}_gesamt.pdf"
    return f"""{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Gesamtakte]({total}) |
| Einzel-PDF-ZIP | [Einzelne Unterlagen]({BASE}/testakte-{slug}-einzelpdfs.zip) |
| Akten-ZIP | [DOCX, EML, CSV und TXT]({BASE}/testakte-{slug}.zip) |"""


def build():
    cases = json.loads(DATA.read_text(encoding="utf-8"))
    validate_data(cases)
    basis = load_renderer()
    renderer = basis.module("build-testakten-einzelpdf-zips")
    configure_text_fonts(renderer)
    downloads = TARGET / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    report = []
    for case in cases:
        slug = case["slug"]
        directory = ROOT / "testakten" / slug
        directory.mkdir(parents=True, exist_ok=True)
        paths = [directory / item["name"] for item in case["files"]]
        # Anlagen entstehen vor ihren E-Mails, unabhängig von der Lesereihenfolge.
        for mail_pass in (False, True):
            for path, item in zip(paths, case["files"]):
                if (path.suffix == ".eml") == mail_pass:
                    basis.write_original(path, item, slug)
                    if mail_pass:
                        enrich_mail(path, item, slug)
        cache = render_office_batch(paths)
        missing = [p.name for p in paths if p.suffix == ".docx" and p not in cache]
        if missing:
            raise RuntimeError(f"Kein Office-PDF, kein Textfallback zulässig: {missing}")
        originals = {"README.txt": NOTICE_BYTES}
        singles = {"README.txt": NOTICE_BYTES}
        writer = PdfWriter()
        documents = []
        for path, item in zip(paths, case["files"]):
            pdf = renderer.render_document_pdf(path, directory, cache)
            reader = PdfReader(io.BytesIO(pdf))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if not text.strip() or "Diese Testakte wurde mit KI" in text or "This test case file was generated" in text:
                raise ValueError(f"Leeres PDF oder unzulässiger Warntext: {path.name}")
            if item.get("contract") and len(reader.pages) < 2:
                raise ValueError(f"Vertrag ist nicht mehrseitig: {path.name}")
            start = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
            writer.add_outline_item(path.name, start)
            originals[path.name] = path.read_bytes()
            singles[path.stem + ".pdf"] = pdf
            documents.append({"file": path.name, "pages": len(reader.pages), "start_page": start + 1,
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        writer.add_metadata({"/Title": case["title"], "/Author": "Klotzkette",
                             "/CreationDate": "D:20261018080000Z", "/ModDate": "D:20261018080000Z"})
        total = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        total.parent.mkdir(exist_ok=True)
        with total.open("wb") as stream:
            writer.write(stream)
        (downloads / total.name).write_bytes(total.read_bytes())
        for suffix, entries in (("", originals), ("-einzelpdfs", singles)):
            (downloads / f"testakte-{slug}{suffix}.zip").write_bytes(basis.archive_bytes(entries))
        rows = "\n".join(f"| `{item['name']}` | {item['title']} | {doc['pages']} |" for item, doc in zip(case["files"], documents))
        counts = Counter(path.suffix for path in paths)
        readme = f"""# 1. {case['title']}

{case['summary']}

[Alle Akten](../README.md) · [Repository](../../README.md) · [Download-Index](../../ASSET_INDEX.md)

## 1.1. Benutzung und Bestand

Für die anwaltliche Bearbeitung internationaler Warenkäufe. Lesen Sie die Unterlagen in ihrer Dateireihenfolge oder öffnen Sie die Originale für die eigene Aktenaufbereitung. Aktenstand: 18.10.2026. Der Bestand umfasst 16 eigenständige Dokumente mit {len(writer.pages)} PDF-Seiten: {counts['.docx']} DOCX, {counts['.eml']} EML, eine CSV und einen Chat-Export als TXT. Es gibt keine Lösung und keine Aufgabenmatrix.

<!-- reserved-example-contacts -->

Alle Parteien, Personen, Geschäftsadressen, Vorgangsnummern und Kontaktadressen sind erfunden. Orte dienen als geografischer Rahmen. E-Mail-Adressen verwenden reservierte .example-Domains.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{download_table(case, local=True)}

<!-- END gesamt-pdf-section (autogen) -->

Beide ZIPs sind flach und enthalten eine UTF-8-README.txt mit dem zweisprachigen Pflicht-Hinweis. Das Original-ZIP enthält nur die 16 Originalunterlagen und README.txt, weder Markdown noch das Gesamt-PDF. Das Einzel-PDF-ZIP enthält genau ein PDF je Original. Mehrseitige Dokumente bleiben zusammen. MIME-Anhänge sind zusätzlich als eigenständige Originale enthalten und werden nicht doppelt als PDF gezählt. Die PDFs selbst enthalten keine Warntexte.

## 1.3. Unterlagen

| Datei | Gegenstand | Seiten |
| --- | --- | ---: |
{rows}

Downloadstand für Pluginversion 1.0.0 und Release-Tag `{TAG}`. [Weitere CISG-Akten](../../un-kaufrecht-cisg/testakte/README.md).
"""
        (directory / "README.md").write_text(readme, encoding="utf-8")
        report.append({"slug": slug, "documents": 16, "pages": len(writer.pages), "files": documents})
        print(f"{slug}: 16 Dokumente, {len(writer.pages)} Seiten", flush=True)
    sections = "\n\n".join(f"## 1.{index}. {case['title']}\n\n{case['summary']}\n\n"
                              f"[Bestandsverzeichnis](../../testakten/{case['slug']}/README.md)\n\n"
                              + download_table(case) for index, case in enumerate(cases, 1))
    (TARGET / "README.md").write_text(f"""# 1. CISG Arbeitsakten

Drei internationale Warenkäufe für die anwaltliche Arbeit mit dem UN-Kaufrecht. Die Akten lassen sich als Gesamt-PDF lesen oder als einzelne Originaldateien bearbeiten. Jede Akte enthält 16 selbstständige Unterlagen, einschließlich mehrseitiger Verträge, echter E-Mail-Anhänge und betrieblicher Aufzeichnungen. Keine Lösung, keine Aufgabenmatrix und keine anwaltliche oder gerichtliche Ergebnisvorgabe.

Aktenstand 18.10.2026. Downloadstand für Pluginversion 1.0.0; sämtliche Release-Downloads verwenden `{TAG}`. Lokale Release-Dateien liegen in `downloads/`. Die Veröffentlichung dieses Tags ist nicht Bestandteil des Aktenbuilds.

<!-- reserved-example-contacts -->

Alle Parteien und Kontakte sind erfunden; die Kontaktadressen verwenden reservierte .example-Domains. Beide ZIP-Varianten sind flach. Das Originalformat-ZIP enthält DOCX, EML, CSV, TXT und README.txt; das Einzel-PDF-ZIP enthält ein PDF je Original sowie README.txt. Beide README.txt beginnen mit dem zweisprachigen Pflicht-Hinweis. Die PDFs enthalten keine Warntexte.

{sections}
""", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()

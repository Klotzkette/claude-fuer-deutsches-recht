#!/usr/bin/env python3
"""Orchestriert ausschließlich die drei redaktionell verfassten Kündigungsakten."""

from collections import Counter
from datetime import date, datetime, timedelta
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

from docx import Document
from docx.shared import Pt
from pypdf import PdfReader, PdfWriter
from reportlab.platypus import Table

from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN, pdf_content_errors
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/kuendigungsschutz-akten.json"
TARGET = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte"
TAG = "arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.0.0"
BASE = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}"
CUTOFF = date(2026, 10, 22)
SLUGS = (
    "arbeitsrecht-kuendigung-betriebsbedingt-leipzig",
    "arbeitsrecht-verdachtskuendigung-bonn",
    "arbeitsrecht-kuendigung-schwangerschaft-augsburg",
)


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


def item_date(item):
    value = item["date"]
    return datetime.fromisoformat(value).date() if "T" in value else datetime.strptime(value, "%d.%m.%Y").date()


def validate_data(cases):
    if tuple(case["slug"] for case in cases) != SLUGS:
        raise ValueError("Nur die drei festgelegten Akten in ihrer Lesereihenfolge sind zulässig")
    for case in cases:
        if not date.fromisoformat(case["access_date"]) <= CUTOFF < date.fromisoformat(case["access_date"]) + timedelta(days=21):
            raise ValueError("Zugang und Aktenstichtag passen nicht zusammen")
        files = case["files"]
        names = [item["name"] for item in files]
        if len(files) != 12 or len(set(Path(name).stem for name in names)) != 12:
            raise ValueError("Je Akte sind zwölf eindeutig benannte Originale erforderlich")
        if Counter(Path(name).suffix for name in names) != Counter({".docx": 8, ".eml": 2, ".csv": 1, ".txt": 1}):
            raise ValueError("Der festgelegte Originalformatmix fehlt")
        if sum(bool(item.get("contract")) for item in files) != 1:
            raise ValueError("Genau ein ausführlicher Arbeitsvertrag ist erforderlich")
        for item in files:
            if not re.fullmatch(r"\d{2}_[A-Za-z0-9_]+\.(docx|eml|csv|txt)", item["name"]):
                raise ValueError(item["name"])
            if item_date(item) > CUTOFF:
                raise ValueError("Dokument nach dem Aktenstichtag")
            if item["name"].endswith(".csv"):
                rows = item["rows"]
                if len(rows) < 5 or any(len(row) != 5 for row in rows):
                    raise ValueError("Entgeltkonto braucht mindestens vier vollständige Datenzeilen")
                for row in rows[1:]:
                    values = [int(value.replace(",", "")) for value in row[1:]]
                    if values[0] + values[1] - values[2] != values[3]:
                        raise ValueError("Entgeltkonto ist rechnerisch inkonsistent")
            elif len(item["body"]) < (5500 if item.get("contract") else 600):
                raise ValueError(f"Original nicht ausformuliert: {item['name']}")
            if item["name"].endswith(".eml"):
                if datetime.fromisoformat(item["date"]).utcoffset() is None:
                    raise ValueError("Maildatum ohne Zeitzone")
                for _, address in getaddresses([item[key] for key in ("author", "to", "cc") if item.get(key)]):
                    if not address.endswith(".example"):
                        raise ValueError("Nicht reservierte Kontaktadresse")
            for attachment in item.get("attachments", []):
                source = next((other for other in files if other["name"] == attachment), None)
                if source is None or not attachment.endswith(".docx") or item_date(source) > item_date(item):
                    raise ValueError("Fehlende oder zeitlich unpassende MIME-Anlage")
        if not any(item.get("attachments") for item in files):
            raise ValueError("Echte Mailanlage fehlt")


def clean_office_metadata(path, item):
    document = Document(path)
    if item.get("contract"):
        document.styles["Heading 1"].paragraph_format.space_before = Pt(12)
    document.core_properties.author = "Klotzkette"
    document.core_properties.last_modified_by = document.core_properties.author
    document.core_properties.comments = ""
    document.core_properties.created = document.core_properties.modified = datetime.combine(item_date(item), datetime.min.time())
    content = io.BytesIO()
    document.save(content)
    with zipfile.ZipFile(content) as source:
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as target:
            for name in sorted(source.namelist()):
                info = zipfile.ZipInfo(name, (2026, 10, 22, 8, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                target.writestr(info, source.read(name))
        path.write_bytes(output.getvalue())


def download_table(case, central=False):
    slug = case["slug"]
    prefix = BASE + "/" if central else "downloads/"
    total = f"gesamt-pdf/{slug}_gesamt.pdf" if central else prefix + f"{slug}_gesamt.pdf"
    return f"""{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Gesamtakte mit Lesezeichen]({total}) |
| Einzel-PDF-ZIP | [Zwölf einzelne PDF-Unterlagen]({prefix}testakte-{slug}-einzelpdfs.zip) |
| Akten-ZIP | [Originalformate DOCX, EML, CSV und TXT]({prefix}testakte-{slug}.zip) |"""


def configure_office_fonts():
    directory = Path(os.environ.get("CISG_FONT_DIR", "/System/Library/Fonts/Supplemental"))
    if not (directory / "Times New Roman.ttf").is_file():
        raise RuntimeError("Times New Roman fehlt; keine unbemerkte Ersatzschrift zulässig")
    workspace = tempfile.TemporaryDirectory(prefix="kuendigungsschutz-fonts-")
    config = ET.Element("fontconfig")
    ET.SubElement(config, "dir").text = str(directory)
    ET.SubElement(config, "cachedir").text = str(Path(workspace.name) / "fontcache")
    ET.indent(config, space="  ")
    path = Path(workspace.name) / "fonts.conf"
    ET.ElementTree(config).write(path, encoding="utf-8", xml_declaration=True)
    os.environ["FONTCONFIG_FILE"] = str(path)
    return workspace


def validate_outputs(cases, report):
    notices = module("testakte_download_notices")
    zipcheck = module("validate-testakten-einzelpdf-zips")
    quality = module("validate-testakten-dokumentqualitaet")
    csvcheck = module("validate-testakten-csv")
    for case, result in zip(cases, report):
        directory = ROOT / "testakten" / case["slug"]
        readme = (directory / "README.md").read_text(encoding="utf-8")
        if notices.missing_notice_positions(readme):
            raise ValueError("Hinweis steht nicht unmittelbar vor der Downloadgruppe")
        paths = [directory / item["name"] for item in case["files"]]
        mails = {path.name: BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                 for path in paths if path.suffix == ".eml"}
        for item in case["files"]:
            if item["name"] in mails:
                mail = mails[item["name"]]
                actual = {part.get_filename(): part.get_payload(decode=True) for part in mail.iter_attachments()}
                expected = {name: (directory / name).read_bytes() for name in item.get("attachments", [])}
                if mail.defects or actual != expected:
                    raise ValueError("MIME-Anlage stimmt nicht mit ihrem eigenständigen Original überein")
            if item.get("reply_to"):
                reference = str(mails[item["reply_to"]]["Message-ID"])
                if any(str(mails[item["name"]][header]) != reference for header in ("In-Reply-To", "References")):
                    raise ValueError("Antwort-Mail referenziert nicht die identische Message-ID")
        for path in paths:
            recorded = next(item for item in result["files"] if item["file"] == path.name)
            if hashlib.sha256(path.read_bytes()).hexdigest() != recorded["sha256"]:
                raise ValueError("Original weicht vom Bestandsbericht ab")
            if path.suffix == ".docx" and Document(path).core_properties.author != "Klotzkette":
                raise ValueError("Dokumentautor weicht vom vereinbarten Metadatenstandard ab")
            text = quality.export_text(path)
            errors = quality.export_meta_errors(text, path) + quality.language_prose_errors(text, path)
            if path.suffix == ".eml":
                errors += quality.eml_quality_errors(path)
            if path.suffix == ".csv":
                errors += csvcheck.validate_file(path)
            if errors:
                raise ValueError(f"{path.name}: {errors}")
        for suffix in ("", "-einzelpdfs"):
            path = TARGET / "downloads" / f"testakte-{case['slug']}{suffix}.zip"
            with zipfile.ZipFile(path) as archive:
                expected = {"README.txt", *(p.stem + ".pdf" if suffix else p.name for p in paths)}
                if archive.namelist()[0] != "README.txt" or set(archive.namelist()) != expected or archive.testzip():
                    raise ValueError("ZIP-Inhalt stimmt nicht mit den zwölf Originalen überein")
                if archive.read("README.txt") != NOTICE_BYTES or any("/" in name or "\\" in name for name in expected):
                    raise ValueError("ZIP ist nicht flach oder der Hinweis wurde verändert")
                if not suffix:
                    for source in paths:
                        if archive.read(source.name) != source.read_bytes():
                            raise ValueError("Originalformat-ZIP verändert ein Original")
                else:
                    for source, recorded in zip(paths, result["files"]):
                        data = archive.read(source.stem + ".pdf")
                        if hashlib.sha256(data).hexdigest() != recorded["pdf_sha256"]:
                            raise ValueError("Einzel-PDF weicht vom Bestandsbericht ab")
            if suffix:
                zipcheck.zip_entries(path, expected_suffix=".pdf")
        total = directory / "gesamt-pdf" / f"{case['slug']}_gesamt.pdf"
        if pdf_content_errors(total.read_bytes()) or len(PdfReader(total).pages) != result["pages"]:
            raise ValueError("Gesamt-PDF fehlerhaft")
        if (TARGET / "downloads" / total.name).read_bytes() != total.read_bytes():
            raise ValueError("Gesamt-PDF-Asset weicht von der zentralen Lesefassung ab")
    for path in [TARGET / "README.md", *(ROOT / "testakten" / case["slug"] / "README.md" for case in cases)]:
        text = path.read_text(encoding="utf-8")
        if notices.missing_notice_positions(text):
            raise ValueError(f"Hinweisposition: {path}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in target:
                if not target.startswith(BASE + "/") or not (TARGET / "downloads" / target.rsplit("/", 1)[1]).is_file():
                    raise ValueError(f"Kein versionsgleicher Akten-Asset: {target}")
            elif not (path.parent / target).is_file():
                raise ValueError(f"Kein funktionierendes lokales Linkziel: {target}")


def build():
    cases = json.loads(DATA.read_text(encoding="utf-8"))
    validate_data(cases)
    if sys.argv[1:] == ["--check-only"]:
        report = json.loads((TARGET / "pruefung/bestand.json").read_text(encoding="utf-8"))
        validate_outputs(cases, report)
        print("Bestandsprüfung: 36 Originale, sechs flache ZIPs, lokale Links und versionsgleiche Assetpfade korrekt")
        return
    if sys.argv[1:]:
        raise SystemExit("Nur ohne Argumente oder mit --check-only aufrufen")
    cisg = module("build-cisg-akten")
    basis = cisg.load_renderer()
    basis.STAMP = datetime(2026, 10, 22, 8)
    renderer = basis.module("build-testakten-einzelpdf-zips")
    cisg.configure_text_fonts(renderer)
    # Keep the temporary font configuration alive for all Office conversions.
    font_workspace = configure_office_fonts()
    original_csv = renderer.G.csv_to_flowables

    def payroll_table(path):
        flowables = original_csv(path)
        for table in flowables:
            if isinstance(table, Table):
                table._argW = table._colWidths = [sum(table._argW) / 5] * 5
        return flowables

    renderer.G.csv_to_flowables = payroll_table
    archives = module("build-testakten-release-zips")
    downloads = TARGET / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    report = []
    for case in cases:
        directory = ROOT / "testakten" / case["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        paths = [directory / item["name"] for item in case["files"]]
        for mail_pass in (False, True):
            for path, item in zip(paths, case["files"]):
                if (path.suffix == ".eml") == mail_pass:
                    basis.write_original(path, item, case["slug"])
                    if path.suffix == ".docx":
                        clean_office_metadata(path, item)
                    if mail_pass:
                        cisg.enrich_mail(path, item, case["slug"])
        cache = render_office_batch(paths)
        if any(path not in cache for path in paths if path.suffix == ".docx"):
            raise RuntimeError("Native Office-Konvertierung fehlt; keine PDF-Imitation zulässig")
        for pdf in cache.values():
            for page in PdfReader(io.BytesIO(pdf)).pages:
                fonts = [str(font.get_object().get("/BaseFont", ""))
                         for font in page["/Resources"]["/Font"].values()]
                if any("TimesNewRoman" not in font for font in fonts):
                    raise RuntimeError("Office hat eine Ersatzschrift eingebettet")
        originals, singles = {}, {}
        writer = PdfWriter()
        documents = []
        for path, item in zip(paths, case["files"]):
            pdf = renderer.render_document_pdf(path, directory, cache)
            reader = PdfReader(io.BytesIO(pdf))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if pdf_content_errors(pdf) or not text.strip() or "\ufffd" in text:
                raise ValueError(f"PDF-Inhalt fehlerhaft: {path.name}")
            if item.get("contract") and len(reader.pages) < 2:
                raise ValueError("Arbeitsvertrag ist nicht mehrseitig")
            start = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
            writer.add_outline_item(item["title"], start)
            originals[path.name], singles[path.stem + ".pdf"] = path.read_bytes(), pdf
            documents.append({"file": path.name, "pages": len(reader.pages), "start_page": start + 1,
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                              "pdf_sha256": hashlib.sha256(pdf).hexdigest()})
        writer.add_metadata({"/Title": case["title"], "/Author": "Aktenbestand",
                             "/CreationDate": "D:20261022080000Z", "/ModDate": "D:20261022080000Z"})
        total = directory / "gesamt-pdf" / f"{case['slug']}_gesamt.pdf"
        total.parent.mkdir(exist_ok=True)
        with total.open("wb") as stream:
            writer.write(stream)
        (downloads / total.name).write_bytes(total.read_bytes())
        for suffix, entries in (("", originals), ("-einzelpdfs", singles)):
            with zipfile.ZipFile(downloads / f"testakte-{case['slug']}{suffix}.zip", "w") as archive:
                archives.write_bytes(archive, NOTICE_BYTES, "README.txt")
                for name, data in sorted(entries.items()):
                    archives.write_bytes(archive, data, name)
        rows = "\n".join(f"| [{item['name']}]({item['name']}) | {item['title']} | {doc['pages']} |"
                         for item, doc in zip(case["files"], documents))
        (directory / "README.md").write_text(f"""# 1. {case['title']}

{case['summary']}

## 1.1. Benutzung und Bestand

Für die anwaltliche Arbeit an Kündigungsschutzmandaten. Die Unterlagen sind in Dateireihenfolge lesbar oder in ihren Originalformaten bearbeitbar. Aktenstand: 22.10.2026. Zwölf Originale mit {len(writer.pages)} PDF-Seiten: acht DOCX, zwei EML, ein Entgeltkonto als CSV mit vier Datenzeilen und ein persönlicher Textvermerk. Der Arbeitsvertrag ist mehrseitig. Es sind keine Lösung, Bewertung, Musterklage oder redaktionellen Arbeitsaufträge beigelegt.

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Praxen, Geschäftsanschriften und Vorgangsnummern sind erfunden. Die Orte bilden nur den geografischen Rahmen. Kontaktadressen verwenden reservierte .example-Domains. Die medizinischen Angaben betreffen keine realen Patientinnen oder Patienten.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{download_table(case, central=True)}

<!-- END gesamt-pdf-section (autogen) -->

Beide ZIPs sind flach; README.txt steht zuerst und enthält den unveränderten zweisprachigen Hinweis. Das Originalformat-ZIP enthält ausschließlich die zwölf Originale und README.txt. Das Einzel-PDF-ZIP enthält ein PDF je Original und README.txt. Mailanlagen sind bytegleich zusätzlich als eigenständige Originale abgelegt und werden in der Lesefassung nicht doppelt gezählt. Die PDFs enthalten keine Warnhinweise. Die ZIP-Links gehören zum Komponentenrelease `{TAG}`. Die lokalen ZIPs und das Gesamt-PDF liegen auch im Plugin-Aktenregister bereit; die Veröffentlichung ist nicht Bestandteil dieses Builds.

## 1.3. Unterlagen

| Original | Gegenstand | PDF-Seiten |
| --- | --- | ---: |
{rows}

[Alle Fallakten](../README.md) · [Repository-Start](../../README.md) · [Download-Index](../../ASSET_INDEX.md) · [Plugin-Aktenregister](../../arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte/README.md)
""", encoding="utf-8")
        report.append({"slug": case["slug"], "documents": len(paths), "pages": len(writer.pages), "files": documents})
        print(f"{case['slug']}: {len(paths)} Originale, {len(writer.pages)} PDF-Seiten", flush=True)
    sections = "\n\n".join(f"## 1.{index}. {case['title']}\n\n{case['summary']}\n\n"
                              f"[Bestandsverzeichnis und Originale](../../testakten/{case['slug']}/README.md)\n\n"
                              + download_table(case) for index, case in enumerate(cases, 1))
    (TARGET / "README.md").write_text(f"""# 1. Kündigungsschutz Aktenregister

Drei kleine Arbeitsakten für die anwaltliche Bearbeitung von Kündigungsschutzmandaten. Öffnen Sie die Gesamtakte als PDF oder nutzen Sie die Einzel-PDFs und nativen Originale zur eigenen Aktenbearbeitung. Aktenstand: 22.10.2026. Jede Akte umfasst zwölf Originalunterlagen; die Sammlung umfasst {sum(result['pages'] for result in report)} PDF-Seiten. Eine große Akte ist nicht Teil dieses Bestands.

Die Arbeitsverträge sind vollständig ausformuliert und mehrseitig. E-Mails sind echte MIME-Dateien mit bytegleichen DOCX-Anlagen. Entgeltkonten enthalten jeweils vier monatliche Datenzeilen. Die Originale enthalten keine Lösung, Bewertung, Musterklage oder redaktionellen Arbeitsaufträge.

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Praxen, Anschriften und Vorgangsnummern sind erfunden; die Orte dienen als geografischer Rahmen. Kontaktadressen verwenden reservierte .example-Domains. Es werden keine realen Patientendaten verwendet. Beide ZIP-Varianten sind flach, ohne Markdown, mit README.txt als erstem Eintrag. Die PDFs enthalten keinen Warnhinweis. Alle folgenden Downloadlinks sind relativ und führen auf vorhandene lokale Dateien. Die neun Dateien in `downloads/` sind zugleich die Akten-Assets für den Komponentenrelease `{TAG}`; dessen Veröffentlichung ist nicht Bestandteil dieses Builds.

{sections}
""", encoding="utf-8")
    if (TARGET / "pruefung/seewerk-bestand.json").is_file():
        module("build-seewerk-akten").write_register()
    validate_outputs(cases, report)
    checks = TARGET / "pruefung"
    checks.mkdir(exist_ok=True)
    (checks / "bestand.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Struktur, MIME-Anlagen, Entgeltrechnungen, PDF-Inhalt, Hinweispositionen und lokale Links geprüft", flush=True)


if __name__ == "__main__":
    build()

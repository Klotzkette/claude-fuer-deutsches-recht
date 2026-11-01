#!/usr/bin/env python3
"""Baut die ausschließlich als PDF-ZIP bestellte Uferwerk-Berufungsakte.

Satz und gattungsspezifische Gestaltung: uferwerk_satz.py.
Satzquellen, Quellenledger und Teilnehmerpaket bleiben getrennt.
"""

from datetime import date
import hashlib
import json
from pathlib import Path
import re
import unicodedata
import zipfile
import argparse

from pypdf import PdfReader
from uferwerk_satz import build_pdf, register_fonts

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt"
FILENAME = "testakte-arbeitsrecht-muster-uferwerk-berufung-einzelpdfs.zip"
STAMP = (2026, 10, 30, 12, 0, 0)
NOTICE = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
    "Benutzung auf eigene Verantwortung und eigene Gefahr.\n\n"
    "This test case file was generated with AI and is an experiment. "
    "Use at your own responsibility and risk.\n\n"
)
SOURCES = [ROOT / "scripts/data" / ("uferwerk-" + part + ".json")
           for part in ("vorgeschichte", "prozess", "nachurteil")]
SUPPORTING_SOURCES = [ROOT / "scripts/uferwerk_satz.py", ROOT / "scripts/build-uferwerk-berufungsakte.py",
                      ROOT / "scripts/data/uferwerk-quellen-vertiefung.json"]
BRANDS = {"employee_firm", "employer_firm", "employer", "court", "agency", "client", "neutral"}


def slug(value):
    value = value.replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")[:100]


def load_documents():
    documents = []
    for source in SOURCES:
        documents.extend(json.loads(source.read_text(encoding="utf-8"))["documents"])
    ids = [item["id"] for item in documents]
    if len(ids) != len(set(ids)):
        raise ValueError("Doppelte Dokumentnummer")
    for item in documents:
        if item["brand"] not in BRANDS or not item.get("sections"):
            raise ValueError(item["id"] + ": Marke oder Inhalt fehlt")
        if date.fromisoformat(item["date"]) > date(2026, 10, 30):
            raise ValueError(item["id"] + ": Nach dem Aktenstichtag")
    return documents


def build(output, register_inventory=True):
    register_fonts()
    documents = load_documents()
    output.mkdir(parents=True, exist_ok=True)
    for path in output.glob("*.pdf"):
        raise ValueError("Satzordner enthält bereits PDFs: " + str(path))
    files = []
    for item in documents:
        filename = item["id"] + "_" + item["date"] + "_" + slug(item["title"]) + ".pdf"
        path = output / filename
        build_pdf(item, path)
        reader = PdfReader(path)
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        if "Diese Testakte wurde" in extracted or "Use at your own" in extracted:
            raise ValueError("Warntext gehört nicht in PDFs")
        files.append({"id": item["id"], "date": item["date"], "title": item["title"], "file": filename,
                      "pages": len(reader.pages), "characters": len(extracted),
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    index_rows = [[file["id"], date.fromisoformat(file["date"]).strftime("%d.%m.%Y"), file["title"], str(file["pages"])]
                  for file in files]
    index = {"id": "00", "date": "2026-10-30", "kind": "memo", "brand": "employee_firm",
             "title": "Aktenverzeichnis", "sender": "FALKENHORST & FLOW", "recipient": "Handakte F26-041LM",
             "reference": "Muster ./. Uferwerk Verlag GmbH / 7 Ca 87/26",
             "subject": "Unterlagenstand 30. Oktober 2026",
             "sections": [{"paragraphs": [
                 "Die Akte umfasst die vorvertraglichen Unterlagen, das Arbeitsverhältnis, den Personalabbau, "
                 "das erstinstanzliche Verfahren und die Korrespondenz nach dem Urteil. Die Nummern V, P und N "
                 "bezeichnen die Ablageabschnitte Vorgeschichte, Prozess und Nachurteil. Sie sind keine gerichtlichen Anlagennummern.",
                 "Die Berufungsschrift und die zugehörige Ausgangskontrolle befinden sich im Abschnitt N. "
                 "Ein zweitinstanzliches Aktenzeichen ist noch nicht mitgeteilt. Der weitere Bearbeitungsauftrag "
                 "ergibt sich aus dem Mandat und der Korrespondenz. Abweichende Angaben in Schriftsätzen und "
                 "Zeugenaussagen werden in den jeweiligen Dokumenten wiedergegeben; dieses Verzeichnis bewertet sie nicht."]},
                 {"table": {"headers": ["Nr.", "Datum", "Dokument", "Seiten"], "rows": index_rows,
                             "widths": [.07, .16, .68, .09]}}]}
    index_file = output / "00_Aktenverzeichnis.pdf"
    build_pdf(index, index_file)
    index_pages = len(PdfReader(index_file).pages)
    readme = NOTICE + (
        "Muster gegen Uferwerk Verlag GmbH - Berufungswerkstatt\n"
        "Aktenstand: 30. Oktober 2026. Workshop: 12. November 2026.\n\n"
        f"{len(documents)} Aktenunterlagen und ein Aktenverzeichnis; insgesamt "
        f"{sum(file['pages'] for file in files) + index_pages} PDF-Seiten.\n"
        "Das Paket enthält ausschließlich PDFs und diese README.txt. Es enthält keine Berufungsbegründung.\n"
        "Die Berufungseinlegung ist innerhalb der erfundenen Fallgeschichte bereits dokumentiert.\n"
        "Sämtliche Parteien, Personen, Vorgänge und Kommunikationsdaten sind erfunden. Die Gerichtsnamen "
        "und Gerichtsanschriften dienen der realistischen Verfahrensdarstellung. Die Aktenzeichen gehören "
        "zur Fallfiktion; die Dokumente sind keine echten gerichtlichen oder anwaltlichen Erklärungen.\n"
        "Die reservierte Domain .example wird ausschließlich für erfundene Kontakte verwendet.\n"
        "Vorgeschichte (V), erste Instanz (P), Nachurteil und Berufungseinlegung (N). "
        "Das Aktenverzeichnis nennt alle Unterlagen mit Datum und Seitenzahl.\n"
        "Datumsangaben in Dateinamen bezeichnen das Ablagedatum; ein später übermittelter Ausdruck kann "
        "einen älteren Vorgang enthalten. Gerichtliche Anlagenkürzel stehen in den Schriftsätzen; "
        "sie sind vom Ablagekennzeichen der PDF-Dateien zu unterscheiden.\n"
        "Rechtsstand der Prompt-Begleitung: 1. November 2026; die Fallunterlagen bilden den jeweiligen "
        "historischen Dokumentstand ab. Prozessbehauptungen und Urteilsbegründungen sind selbst zu prüfen.\n"
    )
    archive_path = output.parent / FILENAME
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for filename, data in [("README.txt", readme.encode("utf-8"))] + [
                (path.name, path.read_bytes()) for path in [index_file] + [output / file["file"] for file in files]]:
            info = zipfile.ZipInfo(filename, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    inventory = {"schema_version": 2, "case": "muster-uferwerk-berufung", "cutoff": "2026-10-30",
                 "source_date": "2026-11-01", "format": "pdf-zip-only-user-request",
                 "documents": len(documents), "index_pages": index_pages,
                 "pages": sum(file["pages"] for file in files) + index_pages,
                 "pdf_files": len(documents) + 1, "archive": FILENAME,
                 "archive_sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": files,
                 "sources": [{"path": path.relative_to(ROOT).as_posix(),
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in SOURCES],
                 "production_sources": [{"path": path.relative_to(ROOT).as_posix(),
                                         "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                                        for path in SUPPORTING_SOURCES]}
    if register_inventory:
        inventory_path = PLUGIN / "testakte/pruefung/uferwerk-bestand.json"
        inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: inventory[key] for key in ("documents", "pdf_files", "pages", "archive_sha256")}, ensure_ascii=False))
    print(archive_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Leerer Satzordner für temporäre Einzel-PDFs")
    parser.add_argument("--no-register", action="store_true", help="Bestandsnachweis nicht aktualisieren")
    args = parser.parse_args()
    build(args.output, register_inventory=not args.no_register)

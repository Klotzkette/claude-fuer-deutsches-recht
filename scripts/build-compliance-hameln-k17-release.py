#!/usr/bin/env python3
"""Baut die vier Arbeitsphasen von ME-37 und ersetzt K17 im Hamelner Sammel-ZIP."""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime
from email import policy
from email.parser import BytesParser
from hashlib import sha256
import importlib.util
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
SLUG = "compliance-hameln-schokolade-charge-k17"
CASE = ROOT / "testakten" / SLUG
TAG = "compliance-hameln-k17-v1.1.0"
BASE = "compliance-hameln-praxis-v1.0.0"
BUNDLE = "Hameln_Compliance_39_Praxisakten.zip"
BUNDLE_SHA256 = "92addd22ed81609796cba976f6877075654d654c9cfd606d58f801b77e7209f5"
NATIVE = f"testakte-{SLUG}.zip"
SINGLE = f"testakte-{SLUG}-einzelpdfs.zip"
COMBINED = f"{SLUG}_gesamt.pdf"
INVENTORY = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
ENTRY = "G00_Tageslage_0925.docx"
PHASES = {
    "Grundakte": 21,
    "Interne_Untersuchung": 11,
    "Zeugenbefragungen": 9,
    "Massnahmen_und_Auswertung": 12,
}


def script(stem):
    spec = importlib.util.spec_from_file_location(stem, ROOT / "scripts" / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(data):
    return sha256(data).hexdigest()


def case_sources():
    pairs = working_dump_archive_pairs(CASE, include_gesamt_pdf=False)
    named = {name: path for path, name in pairs}
    counts = Counter(name.split("/")[0] for name in named)
    if counts != PHASES or any(len(Path(name).parts) != 2 for name in named):
        raise ValueError(f"Unvollständige oder abweichende Aktenstruktur: {counts}")
    for phase in PHASES:
        expected = {p for p in (CASE / phase).iterdir() if p.is_file()}
        if expected != {path for name, path in named.items() if name.startswith(phase + "/")}:
            raise ValueError(f"Nicht exportierte Originale in {phase}.")
    baseline_path = ROOT / "scripts/data/compliance-hameln-k17-ausgangsstand.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    for filename, value in baseline.items():
        if digest(named[f"Grundakte/{filename}"].read_bytes()) != value:
            raise ValueError(f"Das Original der Erstlage wurde verändert: {filename}")
    return named


def csv_records(folder, filename):
    with (CASE / folder / filename).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def verify_facts(named):
    all_filenames = {path.name: path for path in named.values()}
    messages = {}
    cutoff = datetime.fromisoformat("2026-11-06T09:25:00+01:00")
    for name, path in named.items():
        if path.suffix != ".eml":
            continue
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        if message.defects or not all(message[field] for field in ("From", "To", "Date", "Subject", "Message-ID")):
            raise ValueError(f"Unvollständige E-Mail: {name}")
        mid = str(message["Message-ID"])
        if mid in messages:
            raise ValueError(f"Doppelte Nachrichtenkennung: {mid}")
        messages[mid] = message
        if name.startswith("Grundakte/") and message["Date"].datetime > cutoff:
            raise ValueError(f"Nachtrag in der Grundakte: {name}")
        for part in message.iter_attachments():
            filename = part.get_filename()
            if filename not in all_filenames or part.get_payload(decode=True) != all_filenames[filename].read_bytes():
                raise ValueError(f"Abweichende E-Mail-Anlage: {name}/{filename}")
    for message in messages.values():
        parent = messages.get(str(message.get("In-Reply-To")))
        if parent and parent["Date"].datetime > message["Date"].datetime:
            raise ValueError("E-Mail-Antwort ist älter als die Ursprungsnachricht.")

    hmi = csv_records("Interne_Untersuchung", "U03_HMI_Linienjournal_TERM_L3_02.csv")
    gateway = csv_records("Interne_Untersuchung", "U04_Fernwartung_Gateway_UTC.csv")
    transition = next(row for row in hmi if row["mes_beleg"] == "MES-50201")
    confirmation = next(row for row in hmi if row["mes_beleg"] == "MES-50202")
    closed = next(row for row in gateway if row["ereignis"] == "CLOSE")
    elapsed = datetime.fromisoformat(transition["zeit_lokal"]) - datetime.fromisoformat(closed["zeit_utc"])
    if (elapsed.total_seconds() != 617 or confirmation["wert_neu"] != "ACCEPT_OVERRIDE"
            or any(row["benutzerkennung"] or row["eingabeklasse"] != "INPUT_LOCAL"
                   for row in (transition, confirmation))):
        raise ValueError("Zeitkette oder Aussagegrenze der technischen Aufzeichnungen weicht ab.")
    initial = csv_records("Grundakte", "08_Lieferung_und_Bestandsmeldung_K17.csv")
    if (sum(int(row["Stück"]) for row in initial),
        sum(int(row["Weiter vorhanden laut Meldung"]) for row in initial),
        sum(int(row["Kassenabgang"]) for row in initial)) != (12000, 9600, 2400):
        raise ValueError("Mengenrechnung im Eingangsstand weicht ab.")
    later = csv_records("Massnahmen_und_Auswertung", "M09_Ruecklaufstand_K17_1111.csv")
    for row in later:
        sent, held, sold, returned, open_count = (
            int(row[key]) for key in ("Ausgeliefert", "Am 06.11. gesperrter Altbestand",
                                      "Kassenabgang vor Rückruf", "Kundenrückgaben bis Stichtag",
                                      "Nicht zurückgemeldete abgegebene Tafeln")
        )
        if sent != held + sold or sold != returned + open_count:
            raise ValueError(f"Rücklauf vermischt Bestände und Kassenabgänge: {row['Händler']}")
    if sum(int(row["Kundenrückgaben bis Stichtag"]) for row in later) != 346:
        raise ValueError("Rücklaufstand weicht ab.")


def ordered_pdfs():
    order = {phase: i for i, phase in enumerate(PHASES)}
    return sorted(document_arcname_pairs(CASE),
                  key=lambda pair: (order[pair[1].split("/")[0]], pair[0].name != ENTRY, pair[1]))


def combined_bytes(single_zip):
    writer = PdfWriter()
    writer.add_metadata({"/Title": "Die Tafel aus Charge K17", "/Subject": "Vorgang ME-37",
                         "/Author": "Hamelner Bruchkakao GmbH"})
    parents = {}
    with ZipFile(single_zip) as archive:
        for source, name in ordered_pdfs():
            phase = name.split("/")[0]
            start = len(writer.pages)
            for page in PdfReader(BytesIO(archive.read(name))).pages:
                writer.add_page(page)
            if phase not in parents:
                parents[phase] = writer.add_outline_item(phase.replace("_", " "), start)
            writer.add_outline_item(source.name, start, parent=parents[phase])
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    buffer = BytesIO()
    writer.write(buffer)
    return buffer.getvalue()


def check_workshop(path):
    if digest(path.read_bytes()) != BUNDLE_SHA256:
        raise ValueError(f"Das Referenzarchiv aus {BASE} stimmt nicht mit dem veröffentlichten Stand überein.")


def build_workshop(dist, previous, writer):
    check_workshop(previous)
    with ZipFile(previous) as old, ZipFile(dist / BUNDLE, "x") as new:
        for name in old.namelist():
            if name == NATIVE:
                writer.write_file(new, dist / NATIVE, name)
            else:
                writer.write_bytes(new, old.read(name), name)


def verify_workshop(dist, previous, archive_check):
    check_workshop(previous)
    path = dist / BUNDLE
    archive_check.zip_entries(path, require_notice=True)
    with ZipFile(previous) as old, ZipFile(path) as new:
        if old.namelist() != new.namelist() or sum(n.startswith("testakte-") and n.endswith(".zip") for n in new.namelist()) != 39:
            raise ValueError("Das Sammel-ZIP enthält nicht die 39 vorgesehenen Arbeitsakten.")
        for name in new.namelist():
            data = (dist / NATIVE).read_bytes() if name == NATIVE else old.read(name)
            if new.read(name) != data:
                raise ValueError(f"Falsche Arbeitsakte im Sammel-ZIP: {name}")


def inspect(dist, previous):
    named = case_sources()
    verify_facts(named)
    native_check = script("validate-testakten-release-zips")
    single_check = script("validate-testakten-einzelpdf-zips")
    native_check.assert_same(NATIVE, native_check.expected_entries(CASE),
                             native_check.zip_entries(dist / NATIVE, require_notice=True, allow_directories=True))
    single_check.assert_same(SINGLE, [NOTICE_FILENAME, *single_check.expected_arcnames(CASE)],
                             single_check.zip_entries(dist / SINGLE, expected_suffix=".pdf", allow_directories=True))
    with ZipFile(dist / NATIVE) as archive:
        for name, source in named.items():
            if archive.read(name) != source.read_bytes():
                raise ValueError(f"Quelldatei abweichend im ZIP: {name}")
    full = (dist / COMBINED).read_bytes()
    if pdf_content_errors(full) or full != (CASE / "gesamt-pdf" / COMBINED).read_bytes():
        raise ValueError("Die Lesefassung stimmt nicht mit dem geprüften Repository-PDF überein.")
    reader = PdfReader(BytesIO(full))
    if [item.title for item in reader.outline if not isinstance(item, list)] != [
            name.replace("_", " ") for name in PHASES]:
        raise ValueError("Die Lesefassung hat keine vollständigen Phasenlesezeichen.")
    headings = [item for group in reader.outline if isinstance(group, list) for item in group]
    offset = 0
    pairs = ordered_pdfs()
    if len(headings) != len(pairs):
        raise ValueError("Unterlagen oder Lesezeichen fehlen.")
    with ZipFile(dist / SINGLE) as archive:
        for heading, (source, name) in zip(headings, pairs, strict=True):
            if (heading.title, reader.get_destination_page_number(heading)) != (source.name, offset):
                raise ValueError(f"Dokumentenfolge weicht ab: {name}")
            for original in PdfReader(BytesIO(archive.read(name))).pages:
                if original.extract_text() != reader.pages[offset].extract_text():
                    raise ValueError(f"Einzel-PDF und Lesefassung weichen ab: {name}")
                offset += 1
    if offset != len(reader.pages):
        raise ValueError("Seitenzahl weicht ab.")
    verify_workshop(dist, previous, native_check)
    return {
        "tag": TAG, "basis": BASE, "phases": PHASES, "documents": len(named), "pages": offset,
        "source_sha256": {name: digest(source.read_bytes()) for name, source in named.items()},
        "assets": {name: digest((dist / name).read_bytes()) for name in (NATIVE, SINGLE, COMBINED, BUNDLE)},
    }


def build(dist, previous):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein.")
    dist.mkdir(parents=True, exist_ok=True)
    verify_facts(case_sources())
    native = script("build-testakten-release-zips")
    native.build_single(CASE, dist)
    script("build-testakten-einzelpdf-zips").build_single(CASE, dist)
    data = combined_bytes(dist / SINGLE)
    path = CASE / "gesamt-pdf" / COMBINED
    temporary = path.with_suffix(".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)
    (dist / COMBINED).write_bytes(data)
    build_workshop(dist, previous, native)
    report = inspect(dist, previous)
    (dist / INVENTORY).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dist / CHECKSUMS).write_text("".join(f"{digest(p.read_bytes())}  {p.name}\n"
                                         for p in sorted(dist.iterdir())), encoding="utf-8")


def verify(dist, previous):
    names = {path.name for path in dist.iterdir()}
    expected = {NATIVE, SINGLE, COMBINED, BUNDLE, INVENTORY, CHECKSUMS}
    if names != expected:
        raise ValueError("Unerwartete Release-Dateien.")
    recorded = dict(line.split("  ", 1)[::-1] for line in (dist / CHECKSUMS).read_text().splitlines())
    if recorded != {name: digest((dist / name).read_bytes()) for name in expected - {CHECKSUMS}}:
        raise ValueError("Dateiliste oder Prüfsumme weicht ab.")
    report = inspect(dist, previous)
    if report != json.loads((dist / INVENTORY).read_text()):
        raise ValueError("Release-Inventar weicht vom Archiv ab.")
    print(f"{TAG}: {report['documents']} Originale, {report['pages']} Seiten, 4 Ordner und 6 Release-Dateien geprüft.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--previous-workshop", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        build(args.dist.resolve(), args.previous_workshop.resolve())
    verify(args.dist.resolve(), args.previous_workshop.resolve())

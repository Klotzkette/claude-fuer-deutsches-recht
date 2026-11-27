#!/usr/bin/env python3
"""Baut die fünf ModeFuchs-Downloads aus der Arbeitsakte, Eingangspost und Nachlieferung."""
import argparse
import io
import json
from pathlib import Path
from runpy import run_path
from tempfile import TemporaryDirectory

from pypdf import PdfReader

from akteneingang.ausgabe import archive, build_from_documents
from akteneingang.quellen import digest, editorial, members
from testakte_einzelpdf_common import expected_arcnames
from testakte_zip_common import working_dump_archive_pairs
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_office_pdf import office_binary


ROOT = Path(__file__).resolve().parents[1]
SLUG = "inkasso-zahlungsklage-modefuchs"
KEY = "testakten/" + SLUG
CASE = ROOT / KEY
LATE = ROOT / "docs/workshops/vorfuehrakten-nachlieferungen" / SLUG
OUTPUT = ROOT / "docs/downloads/modefuchs"
SOURCE_ZIP = f"testakte-{SLUG}.zip"
SINGLE_ZIP = f"testakte-{SLUG}-einzelpdfs.zip"
LATE_ZIP = f"{SLUG}-mit-nachtrag.zip"
WORK_ZIP = f"lebensakte-{SLUG}.zip"
PRINT_ZIP = f"druckakte-{SLUG}.zip"
ASSETS = {SOURCE_ZIP, SINGLE_ZIP, LATE_ZIP, WORK_ZIP, PRINT_ZIP}
LATE_FILES = ("Begleitnachricht.eml", "Kontenblatt_1749.csv")


def build(stage):
    if not office_binary():
        raise ValueError("LibreOffice wird für den Briefkopf der Klageschrift und das Forderungskonto benötigt.")
    originals = run_path(str(ROOT / "scripts/build-testakten-release-zips.py"))
    prints = run_path(str(ROOT / "scripts/build-testakten-einzelpdf-zips.py"))
    source, _ = originals["build_single"](CASE, stage)
    individual, _ = prints["build_single"](CASE, stage)
    native = members(source.read_bytes())
    printed = members(individual.read_bytes())
    if native.pop(NOTICE_FILENAME) != NOTICE_BYTES or printed.pop(NOTICE_FILENAME) != NOTICE_BYTES:
        raise ValueError("Der Herkunftshinweis fehlt in einem Grundpaket.")

    # Beide späteren Belege gehören nur zu den Fassungen mit Nachlieferung.
    for filename in LATE_FILES:
        path = LATE / filename
        name = "Nachlieferung/" + path.name
        pdf_name = str(Path(name).with_suffix(".pdf")).replace("/", "__")
        if name in native or pdf_name in printed:
            raise ValueError(f"Nachlieferung bereits im Grundbestand: {path.name}")
        native[name] = path.read_bytes()
        printed[pdf_name] = prints["render_document_pdf"](path, LATE)

    (stage / LATE_ZIP).write_bytes(
        archive({NOTICE_FILENAME: NOTICE_BYTES, **native})
    )
    life, reading, combined, _, _ = build_from_documents(KEY, {}, editorial()[KEY], native, printed)
    (stage / WORK_ZIP).write_bytes(life)
    (stage / PRINT_ZIP).write_bytes(archive({
        NOTICE_FILENAME: NOTICE_BYTES,
        SLUG + "/Einzel-PDFs.zip": reading,
        SLUG + "/Gesamtakte.pdf": combined,
    }))


def documents(data, *, extended_notice=False):
    files = members(data)
    notice = files.pop(NOTICE_FILENAME)
    if (extended_notice and not notice.startswith(NOTICE_BYTES)) or (not extended_notice and notice != NOTICE_BYTES):
        raise ValueError("Der Herkunftshinweis im Download fehlt oder weicht ab.")
    return files


def inventory(directory):
    if {path.name for path in directory.glob("*.zip")} != ASSETS:
        raise ValueError("Der Downloadordner enthält eine fehlende oder nicht zugeordnete ZIP-Datei.")
    archives = {name: (directory / name).read_bytes() for name in sorted(ASSETS)}
    originals = {name: path.read_bytes() for path, name in working_dump_archive_pairs(CASE, include_gesamt_pdf=False)}
    if documents(archives[SOURCE_ZIP]) != originals:
        raise ValueError("Das Originalformat-ZIP weicht von den Arbeitsunterlagen ab.")
    single = documents(archives[SINGLE_ZIP])
    if set(single) != set(expected_arcnames(CASE)):
        raise ValueError("Das Einzel-PDF-ZIP enthält einen abweichenden Dokumentenbestand.")

    with_late = originals | {"Nachlieferung/" + name: (LATE / name).read_bytes() for name in LATE_FILES}
    if documents(archives[LATE_ZIP]) != with_late:
        raise ValueError("Die Akte mit Nachlieferung weicht vom Grundbestand oder der späteren Post ab.")
    work = documents(archives[WORK_ZIP], extended_notice=True)
    incoming = {name for name in work if name.startswith("Grundakte/00_Posteingang/")}
    article = editorial()[KEY]
    if len(incoming) != len(article["unterlagen"]) or {n: data for n, data in work.items() if n not in incoming} != with_late:
        raise ValueError("Die Vollakte enthält eine abweichende Eingangspost oder Arbeitsunterlage.")

    bundle = documents(archives[PRINT_ZIP])
    if set(bundle) != {SLUG + "/Einzel-PDFs.zip", SLUG + "/Gesamtakte.pdf"}:
        raise ValueError("Einzel-PDFs oder Gesamt-PDF fehlen in den Druckfassungen.")
    readings = documents(bundle[SLUG + "/Einzel-PDFs.zip"])
    later_pdfs = {str(Path(n).with_suffix(".pdf")).replace("/", "__") for n in incoming | (with_late.keys() - originals.keys())}
    if set(readings) != single.keys() | later_pdfs or any(readings[n] != data for n, data in single.items()):
        raise ValueError("Die Druckfassungen weichen von den Einzel-PDFs oder der späteren Post ab.")
    pages = [len(PdfReader(io.BytesIO(data)).pages) for data in readings.values()]
    if not all(pages) or len(PdfReader(io.BytesIO(bundle[SLUG + "/Gesamtakte.pdf"])).pages) != sum(pages):
        raise ValueError("Die Gesamtdruckfassung und die Einzeldokumente haben abweichenden Seitenumfang.")
    return {
        "eingangspost_sha256": digest(json.dumps(article, ensure_ascii=False, sort_keys=True).encode()),
        "downloads_sha256": {name: digest(data) for name, data in archives.items()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true", help="Veröffentlichte Paketbytes, Quelldateien und Druckbestand prüfen.")
    args = parser.parse_args()
    if args.check:
        expected = json.loads((args.dist / "bestand.json").read_bytes())
        if inventory(args.dist) != expected:
            raise ValueError("Download oder Eingangspost weichen vom gespeicherten Ausgabestand ab.")
    else:
        args.dist.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix="modefuchs-downloads-", dir=args.dist.parent) as folder:
            stage = Path(folder)
            build(stage)
            report = json.dumps(inventory(stage), ensure_ascii=False, indent=2) + "\n"
            (stage / "bestand.json").write_text(report, encoding="utf-8")
            for path in sorted(stage.iterdir()):
                path.replace(args.dist / path.name)
    print("ModeFuchs: fünf Downloads geprüft.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Baut und prüft die Originalformat-ZIPs mit Grundakte und die Pflege-Lesefassungen."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import csv
from hashlib import sha256
import importlib.util
from io import BytesIO, StringIO
import json
from pathlib import Path
from zipfile import ZipFile

from openpyxl import load_workbook
from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_grundakte import FOLDER, base_selection, check_intake_member
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import safe_archive_name, source_zip_includes_gesamt_pdf, working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
TAG = "grundakten-pflegerecht-v1.0.0"
PROJECT = ROOT / "projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/downloads"
TOMASIUS = "Testakte_Tomasius_2025_Grundakte.zip"
COLLECTION = "Grundakten_60_Testakten.zip"
CARE_COLLECTION = "Pflegerecht_5_Testakten_mit_Grundakte.zip"
ACCOUNT = "konto__mietkonto-fbl5n.xlsx"
ACCOUNT_EXTRACT = "Mietkonto_Buchungsauszug.csv"
CARE = (
    "berufskrankheit-asbest-schlosser-werft-bremen",
    "sozialrecht-elektrorollstuhl-koerner-oldenburg",
    "sozialrecht-pflegegrad-demenz-nachtwache-trier",
    "sozialrecht-rollstuhl-tannenberg",
    "sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge",
)
REFRESH_PDF = (
    *CARE,
    "betriebspruefung-und-selbstanzeige-marquardt-handelsvertretung-augsburg",
    "grundsteuer-rosenwinkel-bescheidkette",
    "sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026",
)
WORKSHOP = (
    "steuerrecht-freiburg-workshop-erechnung-xml",
    "steuerrecht-freiburg-workshop-gewerbesteuer-vollstreckung",
    "steuerrecht-freiburg-workshop-plattformmeldung",
)
FREIBURG = (
    "einkommensteuer-freiburg-arbeitszimmer-fortbildung",
    "steuerrecht-freiburg-anwachsung-werkhalle",
    "steuerrecht-freiburg-erbst-familienheim",
    "steuerrecht-freiburg-kst-servicewagen",
    "umsatzsteuer-basel-freiburg-leistungsort",
    *WORKSHOP,
)
FREIBURG_BUNDLES = {
    "Freiburg_Steuerwerkstatt_8_Testakten.zip": FREIBURG,
    "Freiburg_Workshop_3_Livefaelle.zip": WORKSHOP,
}
ODERKONTO = "Freiburg_Oderkonto_Akte_und_Vorlagen.zip"
ODERKONTO_SLUG = "steuerrecht-freiburg-oderkonto-schenkungsteuer"
TEMPLATES = ROOT / "quality/steuerrecht-freiburg/vorlagen"
CORE_TEMPLATES = ("Arbeitsbogen_Steuererklaerung.docx", "Aussetzung_der_Vollziehung.docx",
                  "Einspruch_Finanzamt.docx", "Klage_Finanzgericht.docx")


def load_script(stem):
    spec = importlib.util.spec_from_file_location(stem, ROOT / "scripts" / f"{stem}.py")
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
    return script


def case_zip(slug):
    return f"testakte-{slug}.zip"


def renamed_members(members, intake):
    if not intake or len(intake) != len(set(intake)) or set(intake) - members.keys():
        raise ValueError("Ungültige Auswahl der Eingangsunterlagen.")
    if any(name.startswith(FOLDER + "/") for name in members):
        raise ValueError("Der Ordner für die Eingangsunterlagen ist bereits vorhanden.")
    if NOTICE_FILENAME in intake:
        raise ValueError("Der verbindliche Hinweis gehört an die ZIP-Wurzel.")
    result = {}
    for name, data in members.items():
        if name in intake:
            check_intake_member(name, data)
            name = FOLDER + "/" + name
        result[name] = data
    return result


def csv_bytes(rows, *, bom=False):
    stream = StringIO(newline="")
    csv.writer(stream, delimiter=";", lineterminator="\n").writerows(rows)
    return stream.getvalue().encode("utf-8-sig" if bom else "utf-8")


def project_members(slug, record):
    with ZipFile(PROJECT / case_zip(slug)) as archive:
        if len(archive.namelist()) != len(set(archive.namelist())) or archive.testzip():
            raise ValueError(f"Fehler im Quellarchiv {slug}.")
        members = {name: archive.read(name) for name in archive.namelist()}
    result = renamed_members(members, record["intake"])
    workbook = load_workbook(BytesIO(members[ACCOUNT]), read_only=True, data_only=True)
    try:
        first, last = record["account_rows"]
        lines = list(workbook.worksheets[0].iter_rows(min_row=first, max_row=last, values_only=True))
        if not lines or not lines[0][0] or any(not line[0] for line in lines):
            raise ValueError(f"Unvollständiger Mietkontoauszug in {slug}.")
        width = max(i + 1 for line in lines for i, cell in enumerate(line) if cell is not None)
        result[f"{FOLDER}/{ACCOUNT_EXTRACT}"] = csv_bytes(line[:width] for line in lines)
    finally:
        workbook.close()
    return result


def tomasius_members(intake):
    base = load_script("build-tomasius-rom-status-release")
    legacy = base.legacy_builder().case_members()
    members = base.working_copy(legacy)
    base.verify_members(members, legacy)
    result = renamed_members(members, intake)
    description = (
        "\n\nGrundakte\n\nEntpacken Sie für die erste Bearbeitung nur Grundakte. Sie enthält die "
        "Rechnungen, Kontoauszüge, Verträge und Sachbelege zu Betrieb, Musikschule und Rom. "
        "Der Ausgangsbescheid zur Umsatzsteuer ist als mögliche Grundlage für den eigenen "
        "Einspruch enthalten. Die nachfolgenden Verfahrensdokumente liegen außerhalb von Grundakte.\n\n"
    )
    old_notice = result[NOTICE_FILENAME]
    result[NOTICE_FILENAME] = NOTICE_BYTES
    result["Ablagebeschreibung.txt"] = description.lstrip().encode() + old_notice[len(NOTICE_BYTES):].lstrip()
    result.pop("Dateibestand.csv")
    result["Dateibestand.csv"] = csv_bytes([
        ("Datei", "Bytes", "SHA256"),
        *((name, len(data), sha256(data).hexdigest()) for name, data in sorted(result.items())),
    ], bom=True)
    return result


def write_archive(path, members, writer):
    notice = members[NOTICE_FILENAME]
    if notice_text_errors(notice):
        raise ValueError(f"Pflichthinweis fehlerhaft: {path.name}")
    with ZipFile(path, "x") as archive:
        writer.write_bytes(archive, notice, NOTICE_FILENAME)
        for name, data in sorted(members.items()):
            if name != NOTICE_FILENAME:
                if not safe_archive_name(name, allow_directories=True):
                    raise ValueError(f"Unzulässiger Archivpfad: {name}")
                writer.write_bytes(archive, data, name)


def build_case_pdf(task):
    slug, dist = task
    directory = ROOT / "testakten" / slug
    singles = load_script("build-testakten-einzelpdf-zips")
    individual, count = singles.build_single(directory, dist)
    pairs = document_arcname_pairs(directory)
    if len(pairs) != count or count < 1:
        raise ValueError(f"Akte unvollständig: {slug}")
    combined = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    title = (directory / "README.md").read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
    writer = PdfWriter()
    writer.add_metadata({"/Title": title, "/Subject": "Sozialrechtliche Arbeitsakte"})
    with ZipFile(individual) as archive:
        for source, name in pairs:
            reader = PdfReader(BytesIO(archive.read(name)))
            first_page = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
            writer.add_outline_item(source.relative_to(directory).as_posix(), first_page)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    buffer = BytesIO()
    writer.write(buffer)
    data = buffer.getvalue()
    if pdf_content_errors(data):
        raise ValueError(f"Unzulässiger Hinweistext in {combined.name}.")
    temporary = combined.with_suffix(".tmp")
    temporary.write_bytes(data)
    temporary.replace(combined)
    (dist / combined.name).write_bytes(data)


def build(dist, jobs):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Das Ausgabeziel muss leer sein.")
    dist.mkdir(parents=True, exist_ok=True)
    config = base_selection()
    native = load_script("build-testakten-release-zips")
    for slug in config["central"]:
        native.build_single(ROOT / "testakten" / slug, dist)
    for slug, record in config["project"].items():
        write_archive(dist / case_zip(slug), project_members(slug, record), native)
    write_archive(dist / TOMASIUS, tomasius_members(config["tomasius"]), native)
    with ProcessPoolExecutor(max_workers=jobs) as executor:
        list(executor.map(build_case_pdf, ((slug, dist) for slug in REFRESH_PDF)))
    groups = {
        COLLECTION: [*(case_zip(slug) for slug in sorted(config["central"] | config["project"])), TOMASIUS],
        CARE_COLLECTION: [case_zip(slug) for slug in CARE],
        **{name: [case_zip(slug) for slug in slugs] for name, slugs in FREIBURG_BUNDLES.items()},
    }
    for filename, names in groups.items():
        with ZipFile(dist / filename, "x") as archive:
            native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
            for name in names:
                native.write_file(archive, dist / name, name)
            if filename in FREIBURG_BUNDLES:
                for name in CORE_TEMPLATES:
                    native.write_file(archive, TEMPLATES / name, name)
    with ZipFile(dist / case_zip(ODERKONTO_SLUG)) as base:
        members = {name: base.read(name) for name in base.namelist()}
    members.update({path.name: path.read_bytes() for path in TEMPLATES.glob("*.docx")})
    write_archive(dist / ODERKONTO, members, native)

    report = inspect_release(dist)
    inventory = dist / "release-bestand.json"
    inventory.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sums = dist / "checksums-sha256.txt"
    sums.write_text("".join(f"{sha256(p.read_bytes()).hexdigest()}  {p.name}\n"
                           for p in sorted(dist.iterdir())), encoding="utf-8")
    show(report)


def inspect_release(dist):
    config = base_selection()
    orig_check = load_script("validate-testakten-release-zips")
    pdf_check = load_script("validate-testakten-einzelpdf-zips")
    report = {"tag": TAG, "central": {}, "project": {}, "tomasius": {}, "pdfs": {}}
    for slug, intake in config["central"].items():
        folder = ROOT / "testakten" / slug
        pairs = working_dump_archive_pairs(folder, include_gesamt_pdf=source_zip_includes_gesamt_pdf(folder))
        path = dist / case_zip(slug)
        orig_check.assert_same(path.name, orig_check.expected_entries(folder),
                               orig_check.zip_entries(path, require_notice=True, allow_directories=True))
        with ZipFile(path) as archive:
            for source, name in pairs:
                if source.read_bytes() != archive.read(name):
                    raise ValueError(f"Quelldatei verändert: {name}")
            if sum(name.startswith(FOLDER + "/") for _, name in pairs) != len(intake):
                raise ValueError(f"Grundakte unvollständig: {slug}")
        report["central"][slug] = {"intake": len(intake), "documents": len(pairs)}
    for slug, record in config["project"].items():
        members = project_members(slug, record)
        check_members(dist / case_zip(slug), members)
        report["project"][slug] = {"intake": len(record["intake"]) + 1, "documents": len(members) - 1}
    tomasius = tomasius_members(config["tomasius"])
    check_members(dist / TOMASIUS, tomasius)
    report["tomasius"] = {"intake": len(config["tomasius"]), "documents": len(tomasius) - 2}
    for slug in REFRESH_PDF:
        directory = ROOT / "testakten" / slug
        path = dist / f"testakte-{slug}-einzelpdfs.zip"
        names = pdf_check.expected_arcnames(directory)
        pdf_check.assert_same(path.name, [NOTICE_FILENAME, *names], pdf_check.zip_entries(path, expected_suffix=".pdf"))
        combined = dist / f"{slug}_gesamt.pdf"
        if combined.read_bytes() != (directory / "gesamt-pdf" / combined.name).read_bytes() or pdf_content_errors(combined.read_bytes()):
            raise ValueError(f"Unstimmige Lesefassung: {combined.name}")
        reader = PdfReader(combined)
        expected = []
        page = 0
        with ZipFile(path) as archive:
            for source, name in document_arcname_pairs(directory):
                expected.append((source.relative_to(directory).as_posix(), page))
                page += len(PdfReader(BytesIO(archive.read(name))).pages)
        actual = [(item.title, reader.get_destination_page_number(item)) for item in reader.outline]
        if expected != actual or page != len(reader.pages):
            raise ValueError(f"Lesefassung und Einzel-PDFs weichen ab: {combined.name}")
        report["pdfs"][slug] = {"individual_pdfs": len(names), "pages": page}
    for name, slugs in FREIBURG_BUNDLES.items():
        members = {case_zip(slug): (dist / case_zip(slug)).read_bytes() for slug in slugs}
        members.update({template: (TEMPLATES / template).read_bytes() for template in CORE_TEMPLATES})
        check_members(dist / name, {NOTICE_FILENAME: NOTICE_BYTES, **members})
    with ZipFile(dist / case_zip(ODERKONTO_SLUG)) as archive:
        members = {name: archive.read(name) for name in archive.namelist()}
    members.update({p.name: p.read_bytes() for p in TEMPLATES.glob("*.docx")})
    check_members(dist / ODERKONTO, members)
    for name, cases in ((COLLECTION, [*(case_zip(slug) for slug in sorted(config["central"] | config["project"])), TOMASIUS]),
                        (CARE_COLLECTION, [case_zip(slug) for slug in CARE])):
        check_members(dist / name, {NOTICE_FILENAME: NOTICE_BYTES,
                                    **{asset: (dist / asset).read_bytes() for asset in cases}})
    report["assets"] = {path.name: sha256(path.read_bytes()).hexdigest() for path in sorted(dist.iterdir())
                        if path.name not in {"release-bestand.json", "checksums-sha256.txt"}}
    if len(report["assets"]) != 81:
        raise ValueError("Unerwartete Anzahl der Veröffentlichungsdateien.")
    return report


def check_members(path, expected):
    with ZipFile(path) as archive:
        names = archive.namelist()
        if (len(names) != len(set(names)) or set(names) != set(expected) or archive.testzip()
                or names[0] != NOTICE_FILENAME or notice_text_errors(archive.read(NOTICE_FILENAME))):
            raise ValueError(f"Archiv oder Hinweis weicht ab: {path.name}")
        for name, data in expected.items():
            if archive.read(name) != data or not safe_archive_name(name, allow_directories=True):
                raise ValueError(f"Abweichender Archivbestand: {path.name}/{name}")
            if name.startswith(FOLDER + "/"):
                check_intake_member(name, data)


def show(report):
    counts = [*report["central"].values(), *report["project"].values(), report["tomasius"]]
    print(f"{TAG}: {len(counts)} Grundakten, {sum(item['intake'] for item in counts)} "
          f"Eingangsunterlagen, {len(report['assets']) + 2} Release-Dateien.")


def verify(dist):
    sums = dict(line.split("  ", 1)[::-1] for line in (dist / "checksums-sha256.txt").read_text().splitlines())
    if set(sums) != {p.name for p in dist.iterdir()} - {"checksums-sha256.txt"}:
        raise ValueError("Dateiliste und Prüfsummenliste stimmen nicht überein.")
    for name, digest in sums.items():
        if sha256((dist / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Abweichende Prüfsumme: {name}")
    report = inspect_release(dist)
    if report != json.loads((dist / "release-bestand.json").read_text()):
        raise ValueError("Abweichendes Release-Inventar.")
    show(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    if args.verify:
        verify(args.dist.resolve())
    else:
        build(args.dist.resolve(), args.jobs)

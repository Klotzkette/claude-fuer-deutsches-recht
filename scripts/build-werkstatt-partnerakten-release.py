#!/usr/bin/env python3
"""Baut die aktuelle Neuralis-Ausgabe und prüft Downloads gegen den passenden Aktenstand."""
import argparse
import hashlib
import importlib.util
import io
import json
import shutil
from pathlib import Path
from zipfile import ZipFile

from pypdf import PdfReader

from akteneingang.partnerakte import fachbestand, fachdateien, release_fachakte

from release_asset_common import read_checksums, sha256_file, write_checksums
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
TAG = "werkstatt-partnerakten-v1.0.0"
CASES = {
    "neuralis-medtech-erlangen-gestaltungsakte": {
        "Grundakte": 10, "01_Bescheid_und_erste_Aenderung": 13, "02_Gestaltungsvorschlaege": 5,
    },
    "autohaus-boeblingen": {"Grundakte": 18, "Nachlieferung": 6},
}
NEURALIS_TAG = "neuralis-rechtsmacht-v1.1.0"
NEURALIS_CASES = {
    "neuralis-medtech-erlangen-gestaltungsakte": {
        "Grundakte": 13, "01_Bescheid_und_erste_Aenderung": 14, "02_Gestaltungsvorschlaege": 10,
    },
}
REPORT = "release-bestand.json"
SUMS = "checksums-sha256.txt"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def filenames(slug):
    return (f"testakte-{slug}.zip", f"testakte-{slug}-einzelpdfs.zip", f"{slug}_gesamt.pdf")


def require_members(archive, names):
    actual = archive.namelist()
    require(len(actual) == len(set(actual)) and set(actual) == {*names, NOTICE_FILENAME},
            f"{archive.filename}: abweichende oder doppelte Einträge")
    require(archive.testzip() is None and archive.read(NOTICE_FILENAME) == NOTICE_BYTES,
            f"{archive.filename}: Archivfehler oder falscher Herkunftshinweis")


def inspect_case(dist, slug, stages):
    case = ROOT / "testakten" / slug
    native_name, print_name, combined_name = filenames(slug)
    native = dict(working_dump_archive_pairs(case, include_gesamt_pdf=False))
    prints = dict(document_arcname_pairs(case))
    require(native.keys() == prints.keys(), f"{slug}: nicht jedes Original hat eine Lesefassung")
    combined_file = dist / combined_name
    require(combined_file.read_bytes() == (case / "gesamt-pdf" / combined_name).read_bytes(),
            f"{slug}: Gesamt-PDF weicht vom Repository ab")
    combined = PdfReader(combined_file)
    outline = combined.outline
    require(len(outline) == 2 * len(stages), f"{slug}: fehlende Aktenstufen in den Lesezeichen")
    details, page_number = [], 0
    with ZipFile(dist / native_name) as originals, ZipFile(dist / print_name) as readings:
        require_members(originals, native.values())
        require_members(readings, prints.values())
        for index, (stage, count) in enumerate(stages.items()):
            sources = sorted((path for path, name in native.items() if Path(name).parent == Path(stage)),
                             key=lambda path: prints[path].casefold())
            bookmark, children = outline[index * 2:index * 2 + 2]
            require(len(sources) == count and isinstance(children, list) and len(children) == count
                    and combined.get_destination_page_number(bookmark) == page_number,
                    f"{slug}/{stage}: Anzahl oder Leseziel der Stufe stimmt nicht")
            for source, child in zip(sources, children):
                name = native[source]
                require(originals.read(name) == source.read_bytes(), f"{name}: kein bytegleiches Original")
                printed = readings.read(prints[source])
                reader = PdfReader(io.BytesIO(printed))
                start = page_number
                require(bool(reader.pages) and combined.get_destination_page_number(child) == start,
                        f"{name}: falsches Dokumentenlesezeichen")
                for page in reader.pages:
                    require(page.extract_text().strip() and page.extract_text() == combined.pages[page_number].extract_text(),
                            f"{name}: fehlender oder abweichender Text auf Blatt {page_number + 1}")
                    page_number += 1
                details.append({"original": name, "sha256": sha256_file(source), "lesefassung": prints[source],
                                "pdf_sha256": hashlib.sha256(printed).hexdigest(), "erstes_blatt": start + 1,
                                "seiten": page_number - start})
    require(page_number == len(combined.pages) and len(details) == len(native), f"{slug}: unvollständiger Bestand")
    return {"aktenstaende": stages, "seiten": page_number, "dokumente": details,
            "downloads": {name: sha256_file(dist / name) for name in filenames(slug)}}


def inventory(dist, cases, tag):
    records = {slug: inspect_case(dist, slug, stages) for slug, stages in cases.items()}
    if tag == NEURALIS_TAG:
        for slug, record in records.items():
            record["fachausgabe"] = fachbestand(dist, slug, *filenames(slug)[:2])
    return {"release": tag, "akten": records}


def verify(dist, cases, tag):
    names = {REPORT, SUMS, *(name for slug in cases for name in filenames(slug))}
    if tag == NEURALIS_TAG:
        names.update(name for slug in cases for name in fachdateien(slug))
    require({p.name for p in dist.iterdir()} == names, "Abweichender Releasebestand")
    require(read_checksums(dist / SUMS) == {name: sha256_file(dist / name) for name in names - {SUMS}},
            "Prüfsummen weichen vom tatsächlichen Download ab")
    require(json.loads((dist / REPORT).read_text(encoding="utf-8")) == inventory(dist, cases, tag), "Abweichendes Inventar")


def load_builder(filename):
    spec = importlib.util.spec_from_file_location("partnerakten_" + filename, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(dist, cases, tag):
    dist.mkdir(parents=True, exist_ok=True)
    require(not any(dist.iterdir()), "Bitte ein leeres Ausgabeverzeichnis angeben")
    native = load_builder("build-testakten-release-zips.py")
    prints = load_builder("build-testakten-einzelpdf-zips.py")
    for slug in cases:
        case = ROOT / "testakten" / slug
        native.build_single(case, dist)
        prints.build_single(case, dist)
        shutil.copyfile(case / "gesamt-pdf" / filenames(slug)[2], dist / filenames(slug)[2])
        if tag == NEURALIS_TAG:
            release_fachakte(dist, slug, *filenames(slug)[:2])
    (dist / REPORT).write_text(json.dumps(inventory(dist, cases, tag), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_checksums(dist)
    verify(dist, cases, tag)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dist", type=Path, help="Release in einem leeren Ordner bauen")
    mode.add_argument("--verify", type=Path, help="Vorhandenen oder heruntergeladenen Release gegen den Checkout prüfen")
    profile = ap.add_mutually_exclusive_group()
    profile.add_argument("--neuralis", dest="tag", action="store_const", const=NEURALIS_TAG,
                         help="Aktuelle Neuralis-Ausgabe (Standard beim Bauen)")
    profile.add_argument("--partnerakten-v1", dest="tag", action="store_const", const=TAG,
                         help="Historische Partnerakten im passenden Checkout bauen oder prüfen")
    args = ap.parse_args()
    tag = args.tag or NEURALIS_TAG
    if args.verify:
        try:
            reported = json.loads((args.verify / REPORT).read_text(encoding="utf-8"))["release"]
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ap.error(f"{args.verify / REPORT}: kein lesbarer Release-Nachweis ({exc})")
        if reported not in (TAG, NEURALIS_TAG) or (args.tag and args.tag != reported):
            ap.error(f"Unbekannter oder abweichender Release-Stand im Nachweis: {reported!r}")
        tag = reported
    cases = NEURALIS_CASES if tag == NEURALIS_TAG else CASES
    if tag == TAG:
        slug = "neuralis-medtech-erlangen-gestaltungsakte"
        originals = document_arcname_pairs(ROOT / "testakten" / slug)
        if len(originals) != sum(CASES[slug].values()):
            ap.error("Der Partnerakten-Release enthält 28 Neuralis-Belege. "
                     f"Bitte im Checkout von Tag {TAG} den dortigen Builder mit "
                     f"{'--verify' if args.verify else '--dist'} aufrufen.")
    if args.verify:
        verify(args.verify, cases, tag)
    else:
        build(args.dist, cases, tag)
    print(f"{tag}: Originale, Lesefassungen, Leseziele und Prüfsummen geprüft.")

#!/usr/bin/env python3
"""Bündelt die sechs aktuellen Kündigungsakten mit Eingangspost und Druckfassungen."""
import argparse
import io
import json
from pathlib import Path
from runpy import run_path
from tempfile import TemporaryDirectory

from pypdf import PdfReader, PdfWriter

from akteneingang.ausgabe import archive, build_from_documents
from akteneingang.quellen import catalogs, digest, editorial, members
from akteneingang.vertiefung import fachauswahl
from release_routing import KUENDIGUNG_DOWNLOADS, KUENDIGUNG_PLUGIN_DOWNLOADS, KUENDIGUNG_ZENTRAL, UFERWERK
from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_EN, NOTICE_FILENAME
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
STOCK = ROOT / KUENDIGUNG_PLUGIN_DOWNLOADS
OUTPUT = ROOT / KUENDIGUNG_DOWNLOADS
WORKSHOP = run_path(str(ROOT / "scripts/build-arbeitsrecht-praxisnachtraege.py"))
SEE = WORKSHOP["SEE"]
SUPPLEMENTS = ("01_Anhoerung_Betriebsrat.docx", "02_Antwort_Betriebsrat.docx",
               "03_Klageschrift.docx", "04_Klageerwiderung.docx")


def entries(path):
    files = members(path.read_bytes())
    notice = files.pop(NOTICE_FILENAME)
    if not notice.startswith((NOTICE_BYTES, f"{NOTICE_DE}\n\n{NOTICE_EN}\n".encode())):
        raise ValueError(f"Herkunftshinweis fehlt in {path}")
    return files


def central_source(slug):
    pairs = working_dump_archive_pairs(ROOT / "testakten" / slug, include_gesamt_pdf=False)
    original = {name: path.read_bytes() for path, name in pairs}
    flat = {Path(name).name: data for name, data in original.items()}
    source = STOCK / f"testakte-{slug}.zip"
    if len(flat) != len(original) or flat != entries(source):
        raise ValueError(f"{slug}: Zentrale Einzeldateien und Originalformat-ZIP weichen ab")
    return original


def process_material(slug):
    docs = entries(STOCK / f"testakte-{slug}-prozessunterlagen.zip")
    reader = PdfReader(io.BytesIO(docs.pop("Prozessunterlagen.pdf")))
    if set(docs) != set(SUPPLEMENTS) or len(reader.outline) != len(SUPPLEMENTS):
        raise ValueError(f"{slug}: Vier abgrenzbare Prozessunterlagen erwartet")
    starts = [reader.get_destination_page_number(item) for item in reader.outline] + [len(reader.pages)]
    if starts[0] != 0 or starts != sorted(set(starts)):
        raise ValueError(f"{slug}: Die Lesezeichen bilden keine vier fortlaufenden Abschnitte")
    result = []
    for name, first, end in zip(SUPPLEMENTS, starts[:-1], starts[1:], strict=True):
        with PdfWriter() as writer:
            for page in reader.pages[first:end]:
                writer.add_page(page)
            output = io.BytesIO()
            writer.write(output)
        result.append((name, docs[name], output.getvalue()))
    return result


def extra_prints(items):
    render = run_path(str(ROOT / "scripts/build-testakten-einzelpdf-zips.py"))["render_document_pdf"]
    result = {}
    with TemporaryDirectory() as folder:
        # Ein fester relativer Fallpfad hält Kopf- und Fußzeilen reproduzierbar.
        case = Path(folder) / SEE
        for name, content in items.items():
            path = case / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            result[str(Path(name).with_suffix(".pdf")).replace("/", "__")] = render(path, case)
    return result


def build(dist, records, articles, keys):
    WORKSHOP["seewerk"](dist)
    WORKSHOP["uferwerk"](dist)
    for slug, key in keys.items():
        record = records[key]
        if slug == UFERWERK:
            native = entries(dist / f"{slug}-mit-nachtrag.zip")
            printed = dict(native)
        else:
            native = central_source(slug)
            (dist / f"testakte-{slug}.zip").write_bytes(archive({NOTICE_FILENAME: NOTICE_BYTES, **native}))
            printed = entries(STOCK / f"testakte-{slug}-einzelpdfs.zip")
            if slug == SEE:
                workshop = entries(dist / f"{slug}-mit-nachtrag.zip")
                later = {name: data for name, data in workshop.items() if name.startswith("Nachtrag/")}
                if {name: data for name, data in workshop.items() if name not in later} != native:
                    raise ValueError("Seewerk-Grundbestand und Nachtragsakte weichen ab")
                native.update(later)
                printed.update(extra_prints(later))
            for name, source, pdf in process_material(slug):
                if source not in native.values():
                    native["Prozessunterlagen/" + name] = source
                    printed["Prozessunterlagen__" + Path(name).with_suffix(".pdf").name] = pdf
        work, single, combined, _, _ = build_from_documents(key, record, articles[key], native, printed)
        (dist / f"lebensakte-{slug}.zip").write_bytes(work)
        (dist / f"druckakte-{slug}.zip").write_bytes(archive({
            NOTICE_FILENAME: NOTICE_BYTES,
            slug + "/Einzel-PDFs.zip": single,
            slug + "/Gesamtakte.pdf": combined,
        }))


def inventory(dist, records, articles, keys):
    expected = {f"{prefix}-{slug}.zip" for slug in keys for prefix in ("lebensakte", "druckakte")}
    expected.update(f"testakte-{slug}.zip" for slug in KUENDIGUNG_ZENTRAL)
    expected.update(f"{slug}-mit-nachtrag.zip" for slug in (UFERWERK, SEE))
    if {p.name for p in dist.glob("*.zip")} != expected:
        raise ValueError("Der Downloadbestand enthält fehlende oder unzugeordnete ZIPs.")
    evidence = {}
    for slug, key in keys.items():
        inputs = [STOCK / f"testakte-{slug}-einzelpdfs.zip"]
        native = entries(dist / f"lebensakte-{slug}.zip")
        pack = entries(dist / f"druckakte-{slug}.zip")
        if set(pack) != {slug + "/Einzel-PDFs.zip", slug + "/Gesamtakte.pdf"}:
            raise ValueError(f"{slug}: Unvollständiges Druckpaket")
        printed = members(pack[slug + "/Einzel-PDFs.zip"])
        if printed.pop(NOTICE_FILENAME) != NOTICE_BYTES:
            raise ValueError(f"{slug}: Herkunftshinweis der Einzel-PDFs fehlt")
        if slug in KUENDIGUNG_ZENTRAL:
            inputs.extend([STOCK / f"testakte-{slug}.zip", STOCK / f"testakte-{slug}-prozessunterlagen.zip"])
            original = central_source(slug)
            if entries(dist / f"testakte-{slug}.zip") != original:
                raise ValueError(f"{slug}: Akten-ZIP mit Grundakte weicht vom Quellbestand ab")
            required = list(original.values())
            for name, source, reading in process_material(slug):
                if source in original.values():
                    continue
                if native.get("Prozessunterlagen/" + name) != source:
                    raise ValueError(f"{slug}: {name} fehlt in der Verfahrensphase")
                part = "Prozessunterlagen__" + Path(name).with_suffix(".pdf").name
                expected_pages = [p.extract_text() for p in PdfReader(io.BytesIO(reading)).pages]
                actual_pages = [p.extract_text() for p in PdfReader(io.BytesIO(printed[part])).pages]
                if actual_pages != expected_pages:
                    raise ValueError(f"{slug}: Lesefassung für {name} weicht vom Prozesspaket ab")
        else:
            original = entries(inputs[0])
            required = list(original.values())
        if slug in (SEE, UFERWERK):
            late = entries(dist / f"{slug}-mit-nachtrag.zip")
            required.extend(late.values())
            source = WORKSHOP["SOURCE"]
            workshop_data = source / ("seewerk.json" if slug == SEE else "uferwerk.json")
            inputs.append(workshop_data)
            if slug == SEE:
                inputs.extend(source / item["attachment"] for item in json.loads(workshop_data.read_bytes()) if "attachment" in item)
            else:
                inputs.append(STOCK.parent / "pruefung/uferwerk-bestand.json")
                if not all(printed.get(name) == source for name, source in late.items()):
                    raise ValueError("Uferwerk-Nachtrag fehlt in den Einzeldruckfassungen")
        if not set(map(digest, required)) <= {digest(data) for data in native.values()}:
            raise ValueError(f"{slug}: Vollakte enthält abweichende Original-, Prozess- oder Nachtragsunterlagen")
        base_print = entries(inputs[0])
        if not all(printed.get(name) == data for name, data in base_print.items()):
            raise ValueError(f"{slug}: Einzel-PDFs der Basisakte sind im Druckpaket unvollständig")
        inbox = sum(name.startswith("Grundakte/00_Posteingang/") for name in native)
        if inbox != len(articles[key]["unterlagen"]):
            raise ValueError(f"{slug}: Fehlende Eingangspost")
        pages = sum(len(PdfReader(io.BytesIO(data)).pages) for data in printed.values())
        if len(PdfReader(io.BytesIO(pack[slug + "/Gesamtakte.pdf"])).pages) != pages:
            raise ValueError(f"{slug}: Seiten in Einzel-PDFs und Gesamt-PDF stimmen nicht überein")
        evidence[slug] = {
            "eingangspost": inbox, "originale": len(native), "einzelpdfs": len(printed), "seiten": pages,
            "quellen": {p.relative_to(ROOT).as_posix(): digest(p.read_bytes()) for p in inputs},
            "redaktion_sha256": digest(json.dumps([records[key].get("eingang"), articles[key]],
                                                  sort_keys=True, ensure_ascii=False).encode()),
        }
    return {"akten": evidence, "downloads": {name: digest((dist / name).read_bytes()) for name in sorted(expected)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records, articles, routes = fachauswahl(catalogs(), editorial())
    keys = {slug: key for key, (slug, _) in routes.items() if slug in KUENDIGUNG_ZENTRAL or slug == UFERWERK}
    if set(keys) != KUENDIGUNG_ZENTRAL | {UFERWERK}:
        raise ValueError("Fachredaktion für sechs Kündigungsakten erforderlich")
    if args.check:
        if inventory(args.dist, records, articles, keys) != json.loads((args.dist / "bestand.json").read_bytes()):
            raise ValueError("Quell- oder Downloadbestand weicht von den veröffentlichten Prüfsummen ab.")
    else:
        args.dist.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(dir=args.dist.parent, prefix="kuendigungsschutz-") as folder:
            stage = Path(folder)
            build(stage, records, articles, keys)
            report = inventory(stage, records, articles, keys)
            (stage / "bestand.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
            for path in sorted(stage.iterdir()):
                path.replace(args.dist / path.name)
    print("Sechs Kündigungsakten und 19 benannte Akten-, Druck- und Workshop-Downloads geprüft.")


if __name__ == "__main__":
    main()

"""Ergänzt die aktuelle Workshopakte um ihre redigierte Eingangspost und Arbeitsfassungen."""

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader

from .ausgabe import archive, build_from_documents
from .quellen import catalogs, digest, editorial, members
from .vertiefung import fachauswahl
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME


def fachmaterial(slug):
    key = "testakten/" + slug
    records, articles, _ = fachauswahl(catalogs(), {key: editorial()[key]})
    return key, records[key], articles[key]


def fachdateien(slug):
    return f"lebensakte-{slug}.zip", f"druckakte-{slug}.zip"


def release_fachakte(dist, slug, originals, einzelpdfs):
    key, record, article = fachmaterial(slug)
    native = members((dist / originals).read_bytes())
    native.pop(NOTICE_FILENAME)
    prints = members((dist / einzelpdfs).read_bytes())
    prints.pop(NOTICE_FILENAME)
    readings = {name.replace("/", "__"): data for name, data in prints.items()}
    official, single, combined, _, _ = build_from_documents(key, record, article, native, readings)
    life, printpack = fachdateien(slug)
    (dist / life).write_bytes(official)
    (dist / printpack).write_bytes(archive({
        NOTICE_FILENAME: NOTICE_BYTES,
        f"{slug}/Einzel-PDFs.zip": single,
        f"{slug}/Gesamtakte.pdf": combined,
    }))


def fachbestand(dist, slug, originals, einzelpdfs):
    life, printpack = fachdateien(slug)
    extended = members((dist / life).read_bytes())
    bundle = members((dist / printpack).read_bytes())
    if set(bundle) != {NOTICE_FILENAME, f"{slug}/Einzel-PDFs.zip", f"{slug}/Gesamtakte.pdf"}:
        raise ValueError("Abweichender Inhalt des Druckpakets")
    readings = members(bundle[f"{slug}/Einzel-PDFs.zip"])
    if (not extended.pop(NOTICE_FILENAME).startswith(NOTICE_BYTES)
            or bundle[NOTICE_FILENAME] != NOTICE_BYTES or readings.pop(NOTICE_FILENAME) != NOTICE_BYTES):
        raise ValueError("Fehlender Herkunftshinweis in der Fachausgabe")
    direct_native = members((dist / originals).read_bytes())
    direct_prints = members((dist / einzelpdfs).read_bytes())
    direct_native.pop(NOTICE_FILENAME)
    direct_prints.pop(NOTICE_FILENAME)
    for name, content in direct_native.items():
        if extended.get(name) != content:
            raise ValueError("Abweichendes Original in der Fachausgabe: " + name)
    for name, content in direct_prints.items():
        if readings.get(name.replace("/", "__")) != content:
            raise ValueError("Abweichende Einzellesefassung in der Fachausgabe: " + name)
    _, _, article = fachmaterial(slug)
    incoming = [n for n in extended if n.startswith("Grundakte/00_Posteingang/")]
    supplements = [n for n in extended if n.startswith("Grundakte/Arbeitsfassungen/")]
    expected_extra = len(article["unterlagen"]) + len(article["fortschreibungen"])
    if (len(incoming) != len(article["unterlagen"]) or len(supplements) != len(article["fortschreibungen"])
            or len(extended) != len(direct_native) + expected_extra):
        raise ValueError("Unvollständige Eingangspost oder Arbeitsfassungen")
    expected = {Path(name).with_suffix(".pdf").as_posix().replace("/", "__") for name in extended}
    if set(readings) != expected:
        raise ValueError("Abweichende Einzellesefassungen")
    combined = PdfReader(BytesIO(bundle[f"{slug}/Gesamtakte.pdf"]))
    pages = sum(len(PdfReader(BytesIO(data)).pages) for data in readings.values())
    if pages != len(combined.pages):
        raise ValueError("Abweichende Seitenzahl in der Gesamtdruckfassung")
    return {"aktenstuecke": len(extended), "eingangspost": len(incoming), "arbeitsfassungen": len(supplements),
            "druckseiten": pages, "downloads": {name: digest((dist / name).read_bytes()) for name in (life, printpack)}}

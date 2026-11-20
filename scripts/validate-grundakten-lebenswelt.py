#!/usr/bin/env python3
"""Liest die fertigen Archive unabhängig vom Satz und prüft Fallbezug, Erhalt und Druckausgaben."""

import argparse
import io
import json
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from email import policy
from email.parser import BytesParser
from pathlib import Path
from zipfile import ZipFile

from akteneingang.fassungspruefung import fachvergleich, veroeffentlichter_bestand
from akteneingang.quellen import ROOT, Sources, catalogs, digest, editorial, members
from akteneingang.vertiefung import fachauswahl
from akteneingang.verweise import routes
from docx import Document
from openpyxl import load_workbook
from PIL import Image
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(job):
    (
        _case,
        slug,
        group,
        record,
        article,
        index,
        dist,
        cache,
        local_index,
        prior,
        local,
    ) = job
    filename = "lebensakte-" + slug + ".zip"
    data = (dist / filename).read_bytes()
    require(digest(data) == index["original"]["sha256"], slug + " Originalhash")
    archive = members(data)
    require(
        archive.pop(NOTICE_FILENAME).startswith(NOTICE_BYTES),
        slug + " Herkunftshinweis",
    )
    incoming = {
        name: blob
        for name, blob in archive.items()
        if name.startswith("Grundakte/00_Posteingang/")
    }
    require(
        len(archive) == index["aktenstuecke"]
        and len(incoming) == index["eingangspost"] == len(article["unterlagen"]),
        slug + " Dokumentenzahl",
    )
    existing = {digest(blob) for name, blob in archive.items() if name not in incoming}
    sources = Sources(cache, local_index)
    if prior:
        fachvergleich(archive, article, prior, local, sources)
    for version in ("source", "praxis", "vertieft"):
        if version in record:
            old = members(sources.read(record[version]))
            for name, blob in old.items():
                if name == NOTICE_FILENAME or Path(name).name.lower().endswith(
                    ("_gesamt.pdf", "-gesamt.pdf")
                ):
                    continue
                require(
                    digest(blob) in existing, slug + " fehlende Altunterlage " + name
                )
    for name, blob in incoming.items():
        style = Path(name).suffix
        item = article["unterlagen"][int(Path(name).stem.split("_", 1)[0]) - 1]
        if style == ".eml":
            msg = BytesParser(policy=policy.default).parsebytes(blob)
            require(
                str(msg["Subject"]) == item["titel"]
                and item["text"][0] in msg.get_body().get_content(),
                slug + " E-Mail-Inhalt",
            )
            require(bool(msg["Date"]) or msg["X-Unsent"] == "1", slug + " Mailkopf")
        elif style == ".docx":
            require(
                item["text"][0]
                in [p.text for p in Document(io.BytesIO(blob)).paragraphs],
                slug + " Word-Absatz",
            )
        elif style == ".xlsx":
            wb = load_workbook(io.BytesIO(blob), read_only=True)
            require(
                wb.active["A1"].value == item["titel"] and wb.active.max_row >= 5,
                slug + " Tabelle",
            )
            wb.close()
        elif style == ".png":
            with Image.open(io.BytesIO(blob)) as image:
                require(
                    image.format == "PNG"
                    and image.width >= 600
                    and image.height >= 225,
                    slug + " Bildschirmfoto",
                )
                image.verify()
        elif style == ".pdf":
            require(bool(PdfReader(io.BytesIO(blob)).pages), slug + " Brief")
        else:
            raise ValueError(name)
    if record.get("nur_original"):
        require(not index["druck"], slug + " ZIP-Bestellung")
        return len(incoming), len(archive), 0
    with ZipFile(dist / group) as collection:
        require(collection.read(NOTICE_FILENAME) == NOTICE_BYTES, group + " Hinweis")
        pdfzip = collection.read(slug + "/Einzel-PDFs.zip")
        combined = collection.read(slug + "/Gesamtakte.pdf")
    require(
        digest(pdfzip) == index["druck"]["Einzel-PDFs.zip"]["sha256"]
        and digest(combined) == index["druck"]["Gesamtakte.pdf"]["sha256"],
        slug + " Druckhash",
    )
    files = members(pdfzip)
    require(
        files.pop(NOTICE_FILENAME).startswith(NOTICE_BYTES), slug + " PDF-ZIP-Hinweis"
    )
    require(
        all("/" not in n and n.lower().endswith(".pdf") for n in files),
        slug + " PDF-Ablage",
    )
    new = [
        (name, blob)
        for name, blob in files.items()
        if name.startswith("Grundakte__00_Posteingang__")
    ]
    require(len(new) == len(incoming), slug + " fehlende Einzellesefassung")
    all_pages = sum(
        len(PdfReader(io.BytesIO(blob), strict=False).pages) for blob in files.values()
    )
    unified = PdfReader(io.BytesIO(combined), strict=False)
    require(len(unified.pages) == all_pages, slug + " Blattzahl")
    for name, blob in new:
        text = " ".join(PdfReader(io.BytesIO(blob)).pages[0].extract_text().split())
        require(len(text) > 70, slug + " Erstbeleg unlesbar " + name)
    return len(incoming), len(archive), all_pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path)
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--local-index", type=Path)
    parser.add_argument("--jobs", type=int, default=3)
    parser.add_argument("--vertiefung", action="store_true")
    parser.add_argument(
        "--vorstand",
        type=Path,
        help="Lokale Kopie der geprüften Gesamtausgabe für den Vorher-Nachher-Vergleich",
    )
    args = parser.parse_args()
    catalog = catalogs()
    articles = editorial()
    mapping = routes(catalog)
    central = {
        str(p.relative_to(ROOT))
        for p in (ROOT / "testakten").iterdir()
        if p.is_dir()
        and p.name not in ("megaprompts", "formatvorlagen-paradebeispiele")
    }
    require(
        central == {k for k in catalog if k.startswith("testakten/")},
        "Zentralbestand unvollständig",
    )
    require(set(catalog) == set(articles), "Unvollständige Zuordnung")
    previous = {}
    if args.vertiefung:
        catalog, articles, mapping = fachauswahl(catalog, articles)
        previous = veroeffentlichter_bestand(args.vorstand)
    index = json.loads((args.dist / "release-bestand.json").read_text())
    require(set(index) == {s for s, g in mapping.values()}, "Fehlende Ausgabe")
    expected = (
        {"release-bestand.json"}
        | {v["original"]["datei"] for v in index.values()}
        | {v["lesepaket"] for v in index.values() if "lesepaket" in v}
    )
    checksum = {}
    for line in (args.dist / "checksums-sha256.txt").read_text().splitlines():
        sha, name = line.split("  ", 1)
        require(
            name not in checksum and Path(name).name == name,
            "Mehrdeutiger Release-Name",
        )
        checksum[name] = sha
    require(set(checksum) == expected, "Prüfsummenbestand")
    for name, sha in checksum.items():
        require(digest((args.dist / name).read_bytes()) == sha, name + " Dateihash")
    jobs = [
        (
            case,
            slug,
            group,
            catalog[case],
            articles[case],
            index[slug],
            args.dist,
            args.cache,
            args.local_index,
            previous[slug] if args.vertiefung else None,
            args.vorstand,
        )
        for case, (slug, group) in mapping.items()
    ]
    with ProcessPoolExecutor(args.jobs) as pool:
        totals = list(pool.map(verify, jobs))
    formats = Counter(
        doc["typ"] for row in articles.values() for doc in row["unterlagen"]
    )
    print(
        f"{len(totals)} vollständige Originalarchive, {sum(a for a, b, c in totals)} zusätzliche Eingangsbelege, {sum(b for a, b, c in totals)} Aktenstücke, {sum(c > 0 for a, b, c in totals)} Druckfassungen, {sum(c for a, b, c in totals)} Seiten."
    )
    print(dict(formats))


if __name__ == "__main__":
    main()

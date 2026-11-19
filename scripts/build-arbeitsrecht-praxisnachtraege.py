#!/usr/bin/env python3
"""Baut die zwei vollständigen Workshopfassungen aus den historischen Akten und sechs neuen Belegen."""
import argparse
from email import policy
from email.message import EmailMessage
from io import BytesIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from pypdf import PdfReader

from testakte_zip_common import working_dump_archive_pairs
from uferwerk_satz import build_pdf, register_fonts


ROOT = Path(__file__).resolve().parents[1]
STOCK = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte/downloads"
SOURCE = ROOT / "docs/workshops/arbeitsrecht-praxisnachtraege/quellen"
SEE = "arbeitsrecht-muster-seewerk-lebensakte-radolfzell"
UFER = "arbeitsrecht-muster-uferwerk-berufung"


def write_package(dist, slug, members):
    target = dist / f"{slug}-mit-nachtrag.zip"
    with TemporaryDirectory(dir=dist) as scratch:
        temp = Path(scratch) / target.name
        with ZipFile(temp, "w") as archive:
            for name, data in members.items():
                info = ZipInfo(name, (2026, 11, 19, 12, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        with ZipFile(temp) as result:
            if result.testzip() or result.namelist() != list(members):
                raise ValueError(f"Archivprüfung fehlgeschlagen: {slug}")
        temp.replace(target)
    print(f"{target} ({len(members)-1} Aktenstücke)")


def seewerk(dist):
    with ZipFile(STOCK / f"testakte-{SEE}.zip") as old:
        members = {"README.txt": old.read("README.txt") + (
            "\nSeewerk | Montag, 23. November 2026\n\n"
            "22 Eingangsbelege stehen in Grundakte/. Die weiteren 22 ursprünglichen "
            "Unterlagen stehen im Hauptverzeichnis. Nachtrag/ enthält die drei im "
            "Laufe des Mandatstages nachgereichten Unterlagen E17 bis E19. "
            "Die CSV ist lose und als identische E-Mail-Anlage verfügbar.\n"
        ).encode()}
        pairs = working_dump_archive_pairs(ROOT / "testakten" / SEE, include_gesamt_pdf=False)
        if (len(pairs) != 44 or sum(name.startswith("Grundakte/") for _, name in pairs) != 22
                or {src.name for src, _ in pairs} != set(old.namelist()) - {"README.txt"}):
            raise ValueError("Grundbestand Seewerk prüfen.")
        for src, name in pairs:
            data = old.read(src.name)
            if data != src.read_bytes():
                raise ValueError(f"Zentrale Seewerk-Akte und Pluginbestand weichen ab: {src.name}")
            members[name] = data
    for item in json.loads((SOURCE / "seewerk.json").read_text()):
        msg = EmailMessage(policy=policy.SMTP)
        for header, field in (("From", "sender"), ("To", "recipient"), ("Date", "date"),
                              ("Message-ID", "id"), ("Subject", "subject")):
            msg[header] = item[field]
        msg.set_content(item["body"])
        if "attachment" in item:
            name = item["attachment"]
            data = (SOURCE / name).read_bytes()
            msg.add_attachment(data, maintype="text", subtype="csv", filename=name)
            msg.set_boundary("seewerk-20417-231126-wartungsfenster")
            members["Nachtrag/" + name] = data
        members["Nachtrag/" + item["filename"]] = msg.as_bytes()
    write_package(dist, SEE, members)


def uferwerk(dist):
    register_fonts()
    with ZipFile(STOCK / f"testakte-{UFER}-einzelpdfs.zip") as old:
        members = {name: old.read(name) for name in old.namelist()}
    if len(members) != 95 or any("/" in name for name in members):
        raise ValueError("Historischen Uferwerk-Bestand prüfen.")
    items = json.loads((SOURCE / "uferwerk.json").read_text())
    readme = members["README.txt"].decode().replace("93 Aktenunterlagen", "Grundbestand: 93 Aktenunterlagen", 1)
    with TemporaryDirectory() as scratch:
        for item in items:
            name = item["filename"]
            if name in members:
                raise ValueError(f"Doppelte Uferwerk-Unterlage: {name}")
            path = Path(scratch) / name
            build_pdf(item, path)
            data = path.read_bytes()
            reader = PdfReader(BytesIO(data))
            if len(reader.pages) != 1 or "per beA" in reader.pages[0].extract_text():
                raise ValueError(f"Satz oder Versandvermerk prüfen: {name}")
            members[name] = data
    index = "\n".join(f"{item['id']}   {item['title']} (1 Seite)" for item in items)
    members["README.txt"] = (readme + "\nArbeitsfassung mit Nachtrag | 30. Oktober 2026\n"
                             "Das PDF-Aktenverzeichnis dokumentiert den Grundbestand. "
                             "Am Nachmittag gehen folgende Unterlagen zur Handakte ein:\n" + index +
                             "\nGesamtumfang: 97 PDFs, 188 Seiten.\n").encode()
    write_package(dist, UFER, members)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--dist", type=Path, required=True)
    dist = args.parse_args().dist
    dist.mkdir(parents=True, exist_ok=True)
    seewerk(dist)
    uferwerk(dist)

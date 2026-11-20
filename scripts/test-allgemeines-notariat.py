#!/usr/bin/env python3
"""Prüft die tatsächlichen Aktenstücke, ihre Ablage, Mailanlagen, vollständigen PDF-Ausgaben und Kursmappe."""

import argparse
import io
import json
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path

from akteneingang.dokumente import simple
from akteneingang.quellen import ROOT, Sources, digest, members
from docx import Document
from openpyxl import load_workbook
from PIL import Image
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_FILENAME


def check(condition, message):
    if not condition:
        raise ValueError(message)


def normalize(text):
    return " ".join(text.split())


def inspect_case(case, dist):
    slug = case["id"]
    name = "testakte-notariat-" + slug
    folder = ROOT / "allgemeines-notariat/testakten" / slug
    paths = [
        folder / "downloads" / (name + ".zip"),
        folder / "downloads" / (name + "-einzelpdfs.zip"),
        folder / "gesamt-pdf" / (name + "_gesamt.pdf"),
    ]
    native, printset = [members(p.read_bytes()) for p in paths[:2]]
    notice = native.pop(NOTICE_FILENAME)
    check(
        notice.startswith(NOTICE_BYTES)
        and printset.pop(NOTICE_FILENAME) == NOTICE_BYTES,
        slug + " ZIP-Hinweise",
    )
    doclist = case["unterlagen"]
    combined = PdfReader(paths[2])
    numpages = 0
    check(len(native) == len(printset) == len(doclist), slug + " Zahl der Originale")
    mails = {}
    names = []
    for i, d in enumerate(doclist, 1):
        stem = f"{i:02d}_" + simple(d["titel"])[:82].rstrip("-")
        ext = {
            "eml": "eml",
            "brief": "pdf",
            "tabelle": "xlsx",
            "notiz": "docx",
            "chat": "png",
        }[d["typ"]]
        key = f"{d['ordner']}/{stem}.{ext}"
        names.append(key)
        b = native[key]
        printed = PdfReader(io.BytesIO(printset[d["ordner"] + "__" + stem + ".pdf"]))
        text = normalize(" ".join(p.extract_text() for p in printed.pages))
        check(
            NOTICE_DE not in text and normalize(d["titel"]) in text,
            slug + " PDF-Betreff " + stem,
        )
        for p in printed.pages:
            check(
                normalize(p.extract_text())
                == normalize(combined.pages[numpages].extract_text()),
                slug + " veränderte Gesamtseite " + stem,
            )
            numpages += 1
        if ext == "eml":
            m = BytesParser(policy=policy.default).parsebytes(b)
            mails[i] = m
            check(
                str(m["Subject"]) == d["titel"]
                and parsedate_to_datetime(str(m["Date"])).date().isoformat()
                == d["datum"],
                slug + " Mailkopf " + stem,
            )
            check(
                normalize(m.get_body(preferencelist=("plain",)).get_content())
                == normalize(" ".join(d["text"])),
                slug + " Mailtext " + stem,
            )
            attachments = list(m.iter_attachments())
            check(
                len(attachments) == int("anlage_nr" in d), slug + " Anlagenzahl " + stem
            )
            if "antwort_auf" in d:
                parent = mails[d["antwort_auf"]]
                check(
                    m["In-Reply-To"] == parent["Message-ID"]
                    and parent["Message-ID"] in m["References"]
                    and parsedate_to_datetime(str(m["Date"]))
                    > parsedate_to_datetime(str(parent["Date"])),
                    slug + " Thread " + stem,
                )
        elif ext == "xlsx":
            wb = load_workbook(io.BytesIO(b), read_only=True)
            rows = list(wb.active.values)
            check(
                all(
                    [
                        str(x).strip() if x is not None else ""
                        for x in data[: len(line.split("|"))]
                    ]
                    == [c.strip() for c in line.split("|")]
                    for data, line in zip(rows[3:], d["text"], strict=True)
                ),
                slug + " Excel " + stem,
            )
            wb.close()
        elif ext == "docx":
            paragraphs = [p.text for p in Document(io.BytesIO(b)).paragraphs]
            check(all(t in paragraphs for t in d["text"]), slug + " Word " + stem)
        elif ext == "png":
            with Image.open(io.BytesIO(b)) as image:
                image.verify()
        else:
            check(
                len(PdfReader(io.BytesIO(b)).pages) == len(printed.pages),
                slug + " Originalbrief " + stem,
            )
    check(numpages == len(combined.pages), slug + " Gesamtblattzahl")
    for i, m in mails.items():
        n = doclist[i - 1].get("anlage_nr")
        if n:
            attachment = next(m.iter_attachments())
            check(
                attachment.get_payload(decode=True) == native[names[n - 1]]
                and attachment.get_filename() == Path(names[n - 1]).name,
                slug + " falsche Anlage",
            )
    if dist:
        for p in paths:
            check((dist / p.name).read_bytes() == p.read_bytes(), p.name + " Release")
    return {**native, NOTICE_FILENAME: notice}, numpages


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--dist", type=Path)
    cli.add_argument("--cache", type=Path)
    cli.add_argument("--local-index", type=Path)
    args = cli.parse_args()
    dist = args.dist
    master = {}
    if dist:
        checks = {
            n: h
            for h, n in (
                r.split("  ", 1)
                for r in (dist / "checksums-sha256.txt").read_text().splitlines()
            )
        }
        check(
            len(checks) == 28
            and set(checks)
            == {p.name for p in dist.iterdir()} - {"checksums-sha256.txt"},
            "Releaseumfang",
        )
        for name, h in checks.items():
            check(digest((dist / name).read_bytes()) == h, name + " Prüfsumme")
        master = members(
            (dist / "allgemeines-notariat-alle-testakten.zip").read_bytes()
        )
        check(master.pop(NOTICE_FILENAME).startswith(NOTICE_BYTES), "Kursmappenhinweis")
        plugin = members((dist / "allgemeines-notariat.zip").read_bytes())
        for n in (
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
            "plugin.json",
        ):
            check(
                json.loads(plugin[n])["name"] == "allgemeines-notariat", "Paketmanifest"
            )
        check(
            len([p for p in plugin if p.endswith("/SKILL.md")]) == 10
            and not any(p.startswith("testakten/") for p in plugin),
            "Installationsumfang",
        )
    data = ROOT / "scripts/data"
    cases = sorted((data / "allgemeines-notariat").glob("*.json"))
    check(len(cases) == 7, "Fallzahl")
    total = pages = 0
    for source in cases:
        case = json.loads(source.read_text())
        files, count = inspect_case(case, dist)
        total += len(files) - 1
        pages += count
        if dist:
            for name, b in files.items():
                check(
                    master.pop("Amtsgeschaefte/" + case["id"] + "/" + name) == b, name
                )
    if dist:
        passed = Sources(args.cache, args.local_index)
        stock = json.loads((data / "notariat-bestandsakten.json").read_text())
        check(len(stock) == 13, "Bestandsaktenzahl")
        for key, record in stock.items():
            for name, b in members(passed.read(record)).items():
                check(
                    master.pop("Weitere_Notariatsakten/" + key + "/" + name) == b, name
                )
        check(not master, "Fremddateien in der Kursmappe")
    print(
        f"Sieben Amtsgeschäfte: {total} Arbeitsunterlagen, {pages} PDF-Seiten, alle Nachrichten, Anlagen und Arbeitsvorlagen geprüft."
    )
    if dist:
        print(
            "13 mitgelieferte Bestandsakten byteweise abgeglichen, 29 Freigabedateien geprüft."
        )


if __name__ == "__main__":
    main()

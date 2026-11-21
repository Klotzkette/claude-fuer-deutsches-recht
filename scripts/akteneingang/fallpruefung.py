"""Prüft die geöffneten Originale, Nachrichtenketten und jede Seite der Lesefassungen."""
import io
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path

from akteneingang.dokumente import simple
from akteneingang.quellen import members
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


def inspect_case(case, dist, *, suite, prefix):
    slug = case["id"]
    name = prefix + slug
    folder = suite / slug
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
            numeric = set(d.get("zahlenspalten", []))
            for index, (actual, line) in enumerate(zip(rows[3:], d["text"], strict=True)):
                for col, expected in enumerate(line.split("|"), 1):
                    value = actual[col - 1]
                    expected = expected.strip()
                    if index and col in numeric:
                        check(type(value) in {int, float} and Decimal(str(value)) == Decimal(expected.replace(",", ".")),
                              slug + " Excel-Zahlenwert " + stem)
                    else:
                        check((str(value).strip() if value is not None else "") == expected, slug + " Excel-Zelle " + stem)
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

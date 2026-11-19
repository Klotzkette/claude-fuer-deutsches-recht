#!/usr/bin/env python3
"""Baut Originalakten mit vier Belegnachträgen aus den angegebenen, SHA-gebundenen Ausgaben."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from io import BytesIO, StringIO
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_EN

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/testakten-praxisnachtraege-2026-11.json"
ANNEX = ROOT / "docs/testakten-praxisnachtraege"
INTAKE = "Praxisnachtrag/Grundakte/"
FOLLOWUP = "Praxisnachtrag/Nachlieferung/"
INK = "#203A46"
TEAL = "#27776F"


def table_csv(rows):
    buf = StringIO(newline="")
    csv.writer(buf, delimiter=";", lineterminator="\r\n").writerows(rows)
    return buf.getvalue().encode("utf-8-sig")


def pdf(
    title,
    sender,
    moment,
    *,
    paragraphs=(),
    rows=(),
    category="Aktenvermerk",
    recipient="",
):
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=79,
        bottomMargin=58,
        title=title,
        author=sender,
    )

    def para(value, font="Times-Roman", size=11, leading=15, colour=INK):
        return Paragraph(
            escape(value),
            ParagraphStyle(
                "body",
                fontName=font,
                fontSize=size,
                leading=leading,
                textColor=colors.HexColor(colour),
            ),
        )

    def furniture(c, _):
        c.setFillColor(colors.HexColor(TEAL))
        c.rect(54, 786, 42, 3, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(54, 774, category.upper())
        c.setStrokeColor(colors.HexColor("#B7CAC6"))
        c.line(54, 45, 541, 45)
        c.setFont("Helvetica", 8)
        c.drawString(54, 31, moment.strftime("%d.%m.%Y"))
        c.drawRightString(541, 31, f"Blatt {c.getPageNumber()}")

    story = [
        para(sender, "Helvetica-Bold", 10),
        Spacer(1, 6),
        para(title, "Times-Bold", 19, 23),
        Spacer(1, 8),
        para(moment.strftime("%d.%m.%Y · %H:%M Uhr (%z)"), "Helvetica", 9),
    ]
    if recipient:
        story.extend([Spacer(1, 4), para("An " + recipient, "Helvetica", 9)])
    story.append(Spacer(1, 19))
    for body in paragraphs:
        story.extend([para(body), Spacer(1, 11)])
    if rows:
        cells = [
            [
                para(
                    cell,
                    "Helvetica-Bold" if i == 0 else "Helvetica",
                    9,
                    13,
                    "#FFFFFF" if i == 0 else INK,
                )
                for cell in row
            ]
            for i, row in enumerate(rows)
        ]
        tab = Table(
            cells, colWidths=[doc.width / len(rows[0])] * len(rows[0]), repeatRows=1
        )
        tab.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(INK)),
                    (
                        "ROWBACKGROUNDS",
                        (0, 1),
                        (-1, -1),
                        [colors.HexColor("#ECF3F1"), colors.white],
                    ),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )
        story.append(tab)
    doc.build(
        story,
        onFirstPage=furniture,
        onLaterPages=furniture,
        canvasmaker=lambda *a, **kw: Canvas(*a, **{**kw, "invariant": 1}),
    )
    return buf.getvalue()


def archive_member(z, name, data):
    info = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    z.writestr(info, data)


def write_archive(target, records):
    with ZipFile(target, "w") as z:
        for name, data in records:
            archive_member(z, name, data)


def new_members(case, slug):
    received = datetime.fromisoformat(case["received"])
    later = datetime.fromisoformat(case["later"])
    if received >= later:
        raise ValueError(f"{slug}: Zeitstände verwechselt")
    msg = EmailMessage(policy=SMTP)
    msg["From"], msg["To"] = case["sender"], case["recipient"]
    msg["Subject"], msg["Date"] = case["subject"], format_datetime(received)
    msg["Message-ID"] = f"<praxis-{slug}@aktenpost.example>"
    msg.set_content(case["letter"])
    extract = table_csv(case["rows"])
    msg.add_attachment(
        extract, maintype="text", subtype="csv", filename="02_Betriebsauszug.csv"
    )
    stable_id = hashlib.sha256(slug.encode("utf-8")).hexdigest()[:16]
    msg.set_boundary(f"Aktenpost-{stable_id}")
    records = [
        (INTAKE + "01_Posteingang.eml", msg.as_bytes()),
        (INTAKE + "02_Betriebsauszug.csv", extract),
        (
            FOLLOWUP
            + "03_"
            + (
                "Aktenvermerk"
                if case["path"].startswith("testakten/notariat")
                else "Befund"
            )
            + ".pdf",
            pdf(
                case["heading"],
                case["office"],
                later,
                paragraphs=case["paragraphs"].split("\n\n"),
            ),
        ),
        (FOLLOWUP + "04_Registerauszug.csv", table_csv(case["second_rows"])),
    ]
    sheets = [
        pdf(
            case["subject"],
            case["sender"],
            received,
            recipient=case["recipient"],
            paragraphs=case["letter"].split("\n\n"),
            category="E-Mail",
        ),
        pdf(
            case["register"],
            case["sender"].split(" <")[0],
            received,
            rows=case["rows"],
            category="Datenauszug",
        ),
        records[2][1],
        pdf(
            case["second_register"],
            case["office"],
            later,
            rows=case["second_rows"],
            category="Datenauszug",
        ),
    ]
    return records, [
        (str(Path(n).with_suffix(".pdf")), s) for (n, _), s in zip(records, sheets)
    ]


def build(case, baselines, full_dir, annex_dir):
    slug = Path(case["path"]).name
    for filename in case["anchors"]:
        if not (ROOT / case["path"] / filename).is_file():
            raise ValueError(f"{slug}: Bezugsbeleg fehlt: {filename}")
    old = baselines / Path(urlsplit(case["baseline"]["url"]).path).name
    if hashlib.sha256(old.read_bytes()).hexdigest() != case["baseline"]["sha256"]:
        raise ValueError(
            f"{slug}: Quellarchiv stimmt nicht mit veröffentlichter Ausgabe überein"
        )
    originals, pdfs = new_members(case, slug)
    notice = (
        NOTICE_BYTES
        + (
            "\n"
            + case["title"]
            + "\n\n"
            + case["auftrag"]
            + "\n\nZuerst Praxisnachtrag/Grundakte, danach Praxisnachtrag/Nachlieferung öffnen.\n"
        ).encode()
    )
    with ZipFile(old) as base:
        names = base.namelist()
        previous_notice = base.read("README.txt").decode("utf-8-sig")
        if len(set(names)) != len(names) or not all(
            t in previous_notice for t in (NOTICE_DE, NOTICE_EN)
        ):
            raise ValueError(
                f"{slug}: Ausgangsarchiv nicht eindeutig oder ohne Herkunftshinweis"
            )
        if any(n.startswith("Praxisnachtrag/") for n in names):
            raise ValueError(f"{slug}: Nachtragsordner bereits vorhanden")
        full = full_dir / f"{slug}-mit-nachtrag.zip"
        tmp = full.with_suffix(".tmp")
        with ZipFile(tmp, "w") as target:
            for name in names:
                archive_member(target, name, base.read(name))
            for name, data in originals:
                archive_member(target, name, data)
        with ZipFile(tmp) as result:
            if (
                result.testzip()
                or set(result.namelist()) != set(names) | dict(originals).keys()
            ):
                raise ValueError(f"{slug}: Vollaktenbestand weicht ab")
            if any(result.read(n) != base.read(n) for n in names):
                raise ValueError(f"{slug}: Altbestand verändert")
        tmp.replace(full)
    write_archive(
        annex_dir / f"{slug}-nachtrag.zip", [("README.txt", notice), *originals]
    )
    write_archive(
        annex_dir / f"{slug}-nachtrag-einzelpdfs.zip", [("README.txt", notice), *pdfs]
    )
    combined = PdfWriter()
    for (name, raw), title in zip(
        pdfs,
        [case["subject"], case["register"], case["heading"], case["second_register"]],
    ):
        reader = PdfReader(BytesIO(raw))
        if len(reader.pages) != 1 or not reader.pages[0].extract_text().strip():
            raise ValueError(f"{slug}: Layout oder Inhalt prüfen: {name}")
        combined.append(reader, outline_item=title)
    combined.add_metadata({"/Title": case["title"] + " – Vier zusätzliche Aktenstücke"})
    with (annex_dir / f"{slug}-nachtrag.pdf").open("wb") as f:
        combined.write(f)
    return {
        "akte": slug,
        "dateien_vorher": len(names),
        "neue_aktenstuecke": len(originals),
        "vollakte_sha256": hashlib.sha256(full.read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baselines",
        type=Path,
        required=True,
        help="Ordner der veröffentlichten Original-ZIPs gemäß baseline.url der Quelldaten",
    )
    parser.add_argument(
        "--dist", type=Path, required=True, help="Zielordner für zwölf Vollakten"
    )
    parser.add_argument(
        "--annex",
        type=Path,
        default=ANNEX,
        help="Zielordner für Ergänzungspakete und deren Lesefassungen",
    )
    args = parser.parse_args()
    args.dist.mkdir(parents=True, exist_ok=True)
    args.annex.mkdir(parents=True, exist_ok=True)
    for case in json.loads(DATA.read_text(encoding="utf-8")):
        print(
            json.dumps(
                build(case, args.baselines, args.dist, args.annex), ensure_ascii=False
            )
        )


if __name__ == "__main__":
    main()

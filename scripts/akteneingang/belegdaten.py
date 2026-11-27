"""Datumsangaben, E-Mail-Felder und grundlegender Textsatz für fallgebundene Aktenbelege."""
import re
from datetime import date, datetime, time
from email.headerregistry import Address
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from akteneingang.dokumente import simple

SECTION_HEADING = re.compile(r"(?:§\s*)?\d+(?:\.\d+)*\s+[^\n.!?;:]{2,80}")


def german_date(doc):
    return date.fromisoformat(doc["datum"]).strftime("%d.%m.%Y")


def body(doc):
    return [doc["titel"], f'{german_date(doc)} · {doc["von"]} an {doc["an"]}', *doc["text"]]


def mail_time(doc):
    clock = time.fromisoformat(doc.get("uhrzeit", "09:00"))
    return datetime.combine(date.fromisoformat(doc["datum"]), clock, tzinfo=ZoneInfo("Europe/Berlin"))


def mail_address(doc, key, label):
    address = doc.get(key, simple(doc[label])[:48] + "@fallpost.example")
    return Address(display_name=doc[label], addr_spec=address)


def widths(rows):
    # Long descriptions need more space than dates or reference numbers.
    count = len(rows[0])
    return [max(12, min(55, max(len(str(r[c])) for r in rows) + 2)) for c in range(count)]


def paragraph(text, font="Times-Roman", size=11, leading=14.5, color="24333B", after=8, align=0):
    style = ParagraphStyle("Beleg", fontName=font, fontSize=size, leading=leading,
                           textColor=colors.HexColor("#" + color), spaceAfter=after, alignment=align,
                           allowOrphans=0, allowWidows=0)
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)

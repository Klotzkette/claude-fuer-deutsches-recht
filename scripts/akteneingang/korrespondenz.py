"""Setzt Antworten und echte E-Mail-Anlagen in der vollständigen Eingangspost."""

from __future__ import annotations

import mimetypes
from datetime import timedelta
from email import policy
from email.parser import BytesParser
from email.utils import format_datetime, parsedate_to_datetime

from .dokumente import render, sha, simple


def poststuecke(case, docs):
    ausgaben = []
    for nr, item in enumerate(docs, 1):
        name = item["titel"]
        kennung = f"{case}/{nr}/{name}"
        for feld, label in (
            ("antwort_auf", "_antworttitel"),
            ("anlage_nr", "_anlagetitel"),
        ):
            if feld in item:
                index = item[feld] - 1
                if not 0 <= index < len(docs):
                    raise ValueError("Fehlender Verweis: " + name)
                item = {**item, label: docs[index]["titel"]}
        ext, blob, pdf = render(item, kennung)
        stem = f"{nr:02d}_" + simple(name)[:82].rstrip("-")
        ausgaben.append([stem, ext, blob, pdf])
    for nr, item in enumerate(docs, 1):
        if not any(key in item for key in ("antwort_auf", "anlage_nr")):
            continue
        stem, ext, blob, pdf = ausgaben[nr - 1]
        if ext != "eml":
            raise ValueError(
                "Antwortbezug oder Anlage an Nicht-E-Mail: " + item["titel"]
            )
        message = BytesParser(policy=policy.SMTP).parsebytes(blob)
        if "antwort_auf" in item:
            i = item["antwort_auf"]
            if not 1 <= i < nr or ausgaben[i - 1][1] != "eml":
                raise ValueError("Nicht vorhandene Vorgängermail: " + item["titel"])
            parent = BytesParser(policy=policy.SMTP).parsebytes(ausgaben[i - 1][2])
            if not parent["Date"] and message["Date"]:
                raise ValueError("Antwort auf unversendeten Entwurf: " + item["titel"])
            if parent["Date"] and message["Date"]:
                before = parsedate_to_datetime(str(parent["Date"]))
                after = parsedate_to_datetime(str(message["Date"]))
                if after.date() < before.date():
                    raise ValueError("Antwort vor Anfrage: " + item["titel"])
                if before >= after:
                    message.replace_header(
                        "Date", format_datetime(before + timedelta(minutes=7 + nr))
                    )
            message["In-Reply-To"] = parent["Message-ID"]
            message["References"] = " ".join(
                filter(
                    None, [str(parent["References"] or ""), str(parent["Message-ID"])]
                )
            )
        if "anlage_nr" in item:
            i = item["anlage_nr"]
            if not 1 <= i <= len(docs) or i == nr:
                raise ValueError("Unbekannte Anlage: " + item["titel"])
            name, kind, attached, _ = ausgaben[i - 1]
            if kind == "eml":
                raise ValueError(
                    "Als Anlage nur den Sachbeleg einbetten: " + item["titel"]
                )
            mime = (
                mimetypes.guess_type(name + "." + kind)[0] or "application/octet-stream"
            )
            message.add_attachment(
                attached,
                maintype=mime.split("/")[0],
                subtype=mime.split("/")[1],
                filename=name + "." + kind,
            )
            message.set_boundary("Fallpost-" + sha((case + "/" + stem).encode())[:28])
        ausgaben[nr - 1][2] = message.as_bytes()
    return ausgaben

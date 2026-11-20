"""Vergleicht eine Fachfassung mit der veröffentlichten Grundakte einschließlich echter Mailanlagen."""

from __future__ import annotations

import io
import json
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.request import urlopen

from docx import Document
from openpyxl import load_workbook
from testakte_disclaimer import NOTICE_FILENAME

from .quellen import ROOT, URL, digest, members


def veroeffentlichter_bestand(vorstand):
    name = "release-bestand.json"
    proof = json.loads((ROOT / "docs/grundakten-lebenswelt/edition.json").read_text())
    base = URL + proof["tag"] + "/"
    if vorstand is None:
        with urlopen(base + name, timeout=90) as response:
            data = response.read()
    else:
        data = (vorstand / name).read_bytes()
    if digest(data) != proof["bestand_sha256"]:
        raise ValueError(
            "Ausgangsinventar stimmt nicht mit der veröffentlichten Edition überein"
        )
    return {
        k: {
            "url": base + r["original"]["datei"],
            "sha256": r["original"]["sha256"],
            "size": r["original"]["bytes"],
        }
        for k, r in json.loads(data).items()
    }


def fachvergleich(archive, article, prior, local, sources):
    if local:
        base = (local / prior["url"].split("/")[-1]).read_bytes()
        if digest(base) != prior["sha256"]:
            raise ValueError("Falsche historische Arbeitsakte")
    else:
        base = sources.read(prior)
    original = members(base)
    original.pop(NOTICE_FILENAME)

    def number(name):
        return int(Path(name).stem.split("_", 1)[0])

    first = "Grundakte/00_Posteingang/"
    for name, blob in original.items():
        if name.startswith(first) and article["unterlagen"][number(name) - 1].get(
            "_fachfassung"
        ):
            if name not in archive or archive[name] == blob:
                raise ValueError("Frühere Unterlage nicht fortgeschrieben: " + name)
        elif archive.get(name) != blob:
            raise ValueError("Ursprünglicher Beleg verändert: " + name)
    items = {number(n): (n, b) for n, b in archive.items() if n.startswith(first)}
    for i, doc in enumerate(article["unterlagen"], 1):
        if doc["typ"] != "eml":
            continue
        msg = BytesParser(policy=policy.default).parsebytes(items[i][1])
        for p in doc["text"]:
            if " ".join(p.split()) not in " ".join(
                msg.get_body(preferencelist=("plain",)).get_content().split()
            ):
                raise ValueError("Fehlender Mailabsatz: " + doc["titel"])
        if "antwort_auf" in doc:
            parent = BytesParser(policy=policy.default).parsebytes(
                items[doc["antwort_auf"]][1]
            )
            if (
                msg["In-Reply-To"] != parent["Message-ID"]
                or parent["Message-ID"] not in msg["References"]
            ):
                raise ValueError("Falsche Antwortzuordnung: " + doc["titel"])
            if (
                msg["Date"]
                and parent["Date"]
                and parsedate_to_datetime(str(msg["Date"]))
                <= parsedate_to_datetime(str(parent["Date"]))
            ):
                raise ValueError("Antwort vor der Ursprungsmail: " + doc["titel"])
        attachments = list(msg.iter_attachments())
        if "anlage_nr" in doc:
            name, blob = items[doc["anlage_nr"]]
            if (
                len(attachments) != 1
                or attachments[0].get_payload(decode=True) != blob
                or attachments[0].get_filename() != Path(name).name
            ):
                raise ValueError("Abweichende oder fehlende Anlage: " + doc["titel"])
    for item in article.get("fortschreibungen", []):
        path = Path(item["quelle"])
        if path.suffix == ".csv":
            path = path.with_suffix(".xlsx")
        blob = archive["Grundakte/Arbeitsfassungen/" + path.name]
        if path.suffix == ".docx":
            paragraphs = [p.text for p in Document(io.BytesIO(blob)).paragraphs]
            if not all(p in paragraphs for p in item["text"]):
                raise ValueError("Fehlender Wortlaut im Nachtrag: " + path.name)
        else:
            wb = load_workbook(io.BytesIO(blob), read_only=True)
            if wb["Rueckfragen"]["A1"].value != item["titel"] or len(wb.sheetnames) < 2:
                raise ValueError("Unvollständige Tabellenfassung: " + path.name)
            wb.close()

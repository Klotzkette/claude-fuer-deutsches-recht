#!/usr/bin/env python3
"""Prüft die PDF-ZIP-only-Berufungsakte, ihren Bestand und zentrale Übergaben."""

import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import unicodedata
from unittest.mock import patch
import zipfile

from pypdf import PdfReader
import pdfplumber
import uferwerk_satz

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt"
NOTICE = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
    "Benutzung auf eigene Verantwortung und eigene Gefahr.\n\n"
    "This test case file was generated with AI and is an experiment. "
    "Use at your own responsibility and risk.\n\n"
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_recipient_formatting(documents):
    """Prüft Versandvermerk und Adresssatz unabhängig von lokalen Schriftdateien."""
    by_id = {doc["id"]: doc for doc in documents}
    sty = {"body": object(), "small": object()}

    def recipient_calls(item):
        spec = uferwerk_satz.spec_for(item)
        require(spec["mode"] == "firm_letter", "Kanzleibriefprofil verloren: " + item["id"])
        with patch.object(uferwerk_satz, "_draw_paragraph") as draw:
            uferwerk_satz._recipient(None, item, spec, sty)
        return [call.args for call in draw.call_args_list]

    # P06 bittet im Text um künftige Zustellungen an das beA; das belegt
    # keinen Versandweg für dieses ausgehende Schreiben.
    for doc_id in ("N01", "N21", "P01", "P06"):
        calls = recipient_calls(by_id[doc_id])
        require(len(calls) == 1, "Unbelegter Versandvermerk: " + doc_id)
        require(calls[0][2:5] == (uferwerk_satz.LEFT, 728, 287), "Adresssatz verändert: " + doc_id)
        if doc_id in ("N01", "N21"):
            require(calls[0][1] == by_id[doc_id]["recipient"], "Mandantenanschrift verändert: " + doc_id)
        else:
            require("Arbeitsgericht Villingen-Schwenningen\nKammern Radolfzell" in calls[0][1],
                    "Gerichtsanschrift verändert: " + doc_id)

    # Lange Quellenangabe und bereits abgekürzter Vermerk müssen genau einmal
    # über der Anschrift erscheinen; die Quellenangabe gehört nicht in sie.
    for transmission in ("Über das besondere elektronische Anwaltspostfach", "per beA"):
        item = dict(by_id["N19"])
        item["recipient"] = by_id["N19"]["recipient"].replace(
            "Über das besondere elektronische Anwaltspostfach", transmission)
        calls = recipient_calls(item)
        require(len(calls) == 2 and calls[1][1:5] == ("per beA", uferwerk_satz.LEFT, 742, 200),
                "Ausdrücklicher beA-Versand fehlt oder ist doppelt: N19")
        require(calls[0][1] == by_id["N19"]["recipient"].rsplit("\n", 1)[0],
                "Versandvermerk nicht von Gerichtsanschrift getrennt: N19")


def check():
    inventory = json.loads((PLUGIN / "testakte/pruefung/uferwerk-bestand.json").read_text())
    archive_path = PLUGIN / "testakte/downloads" / inventory["archive"]
    require(hashlib.sha256(archive_path.read_bytes()).hexdigest() == inventory["archive_sha256"], "Archiv nicht synchron")
    require(inventory["format"] == "pdf-zip-only-user-request", "Ausdrückliche Formatwahl fehlt")
    documents = []
    for entry in inventory["sources"] + inventory["production_sources"]:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["sha256"],
                "PDF-Bestand nicht aus aktuellem Quellenstand: " + entry["path"])
    for part in ("vorgeschichte", "prozess", "nachurteil"):
        documents += json.loads((ROOT / "scripts/data" / ("uferwerk-" + part + ".json")).read_text())["documents"]
    by_id = {doc["id"]: doc for doc in documents}
    check_recipient_formatting(documents)
    require(len(by_id) == len(documents) == inventory["documents"], "Quellenbestand")
    require(len(documents) >= 80 and inventory["pages"] > 100, "Umfang bleibt hinter der bestellten Lebens- und Prozessakte zurück")
    pdf_texts = {}
    body_texts = {}
    recipient_texts = {}
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        require(archive.testzip() is None, "Beschädigtes ZIP")
        require(names[0] == "README.txt", "Hinweis zuerst an ZIP-Wurzel")
        readme = archive.read("README.txt").decode("utf-8")
        require(readme.startswith(NOTICE), "Pflichthinweis nicht wortgetreu")
        require(all("/" not in name and "\\" not in name for name in names), "ZIP muss flach sein")
        expected = {entry["file"] for entry in inventory["files"]} | {"00_Aktenverzeichnis.pdf", "README.txt"}
        require(set(names) == expected, "Fehlende oder zusätzliche Ausgabedateien")
        require(all(name.endswith(".pdf") or name == "README.txt" for name in names), "Unerwünschte Original-/Lösungsdatei")
        pages = 0
        for entry in inventory["files"]:
            payload = archive.read(entry["file"])
            require(payload.startswith(b"%PDF-"), "Falscher Dateityp")
            require(hashlib.sha256(payload).hexdigest() == entry["sha256"], "PDF-Prüfsumme: " + entry["id"])
            reader = PdfReader(BytesIO(payload))
            require(len(reader.pages) == entry["pages"], "Seitenzahl: " + entry["id"])
            content = "\n".join(page.extract_text() or "" for page in reader.pages)
            pdf_texts[entry["id"]] = content
            with pdfplumber.open(BytesIO(payload)) as layout:
                first = layout.pages[0]
                recipient_texts[entry["id"]] = first.crop((60, 85, first.width - 45, 220)).extract_text() or ""
                body_texts[entry["id"]] = "\n".join(
                    page.crop((60, 58, page.width - 45, page.height - 62)).extract_text(x_tolerance=2, y_tolerance=3) or ""
                    for page in layout.pages)

            pages += len(reader.pages)
            require(all((page.extract_text() or "").strip() for page in reader.pages), "Leere PDF-Seite")
            require("Diese Testakte wurde" not in content and "This test case file" not in content, "Hinweis im Aktenstück")
            require(not re.search(r"\[(?:Name|Datum|Betrag|Unterschrift|Adresse|einsetzen)\b", content, re.I), "Ungefülltes Muster")
            require("TimesNewRoman" in str(reader.pages[0]["/Resources"].get("/Font", {})) or
                    any("TimesNewRoman" in str(font.get_object().get("/BaseFont", ""))
                        for font in reader.pages[0]["/Resources"]["/Font"].values()), "Grundschrift fehlt")
        index = PdfReader(BytesIO(archive.read("00_Aktenverzeichnis.pdf")))
        require(pages + len(index.pages) == inventory["pages"], "Gesamtseitenzahl")
        index_text = "\n".join(page.extract_text() or "" for page in index.pages)
        require(all(entry["id"] in index_text for entry in inventory["files"]), "Aktenverzeichnis unvollständig")
    for doc in documents:
        if uferwerk_satz.spec_for(doc)["mode"] == "firm_letter":
            declared = any(line.strip().casefold() in ("über das besondere elektronische anwaltspostfach", "per bea")
                           for line in doc["recipient"].splitlines())
            require(recipient_texts[doc["id"]].count("per beA") == int(declared),
                    "PDF-Versandvermerk ohne passende Quellenangabe: " + doc["id"])
    require(recipient_texts["N19"].count("per beA") == 1, "Ausdrücklicher PDF-beA-Vermerk fehlt oder ist doppelt: N19")
    require("Über das besondere elektronische Anwaltspostfach" not in recipient_texts["N19"],
            "Langer Versandvermerk zusätzlich in PDF-Anschrift: N19")
    # Inhaltserhalt über den Satz hinweg: Absatztext darf durch Gattungsprofile
    # oder Umbrüche nicht verschwinden. Das gesondert gesetzte Rubrum wird
    # stattdessen anhand seiner entscheidenden Identitätsdaten geprüft.
    def normalize(text):
        return re.sub(r"[^a-zäöüß0-9]", "", unicodedata.normalize("NFKC", text).lower())
    for doc in documents:
        rendered = normalize(body_texts[doc["id"]])
        for section in doc["sections"]:
            for paragraph in section.get("paragraphs", []):
                if doc["kind"] == "email" and paragraph.startswith("Gesendet:"):
                    sent = re.match(r"Gesendet:\s*(.+?\b\d{2}:\d{2}(?:\s*Uhr)?)(.*)", paragraph, re.S)
                    if sent and sent[2].strip(" .\n"):
                        require(all(normalize(value) in rendered for value in sent.groups()), "Inline-Mailtext verloren: " + doc["id"])
                        continue
                if doc["id"] == "N10":
                    fields = re.match(r"Von: (.*?)\. An: (.*?)\. Betreff: (.*?)\. Text: (.*)", paragraph, re.S)
                    if fields:
                        require(all(normalize(value) in rendered for value in fields.groups()), "Mailfeld beim Satz verloren: N10")
                        continue
                require(normalize(paragraph) in rendered, "Absatz beim Satz verloren: " + doc["id"] + " / " + paragraph[:65])
    contract = by_id["V05"]
    require(len(contract["sections"]) == 20, "Vertragsgliederung verändert")
    require(sum(len(p.split()) for sec in contract["sections"] for p in sec.get("paragraphs", [])) >= 3500,
            "Vertragsvertiefung fehlt")
    for doc_id, minimum in {"P01": 12000, "P10": 14000, "P13": 18000, "P15": 13000, "P21": 11000, "P27": 65000}.items():
        require(sum(len(p) for sec in by_id[doc_id]["sections"] for p in sec.get("paragraphs", [])) >= minimum,
                "Bestellte Vertiefung fehlt: " + doc_id)
    ledger = json.loads((ROOT / "scripts/data/uferwerk-quellen-vertiefung.json").read_text())
    require(len([entry for entry in ledger if entry["type"] == "literatur"]) == 5, "Literaturledger unvollständig")
    require(all(entry.get("url") and entry.get("pinpoint") and entry.get("limit") and entry.get("license/access") for entry in ledger),
            "Quellenstatus oder Aussagegrenze fehlt")
    for doc in documents:
        content = " ".join(p for sec in doc["sections"] for p in sec.get("paragraphs", []))
        for reference, earliest in (("6 AZR 152/22", "2026-04-24"), ("6 AZR 157/22", "2026-04-28"), ("6 AZR 7/26", "2026-08-11")):
            if doc["date"] < earliest:
                require(not re.search(re.escape(reference) + r".{0,40}Rn\.", content),
                        "Volltextrandnummer vor Bereitstellung: " + doc["id"] + " / " + reference)
    for value in ("Lisa Muster", "Uferwerk Verlag GmbH", "Dr. Johanna Falkenhorst", "Caspar Finley von Knigge", "Hedwig Sky Pfefferle", "Ottokar Finn Leicht"):
        require(value in pdf_texts["P27"], "Unvollständiges Rubrum: " + value)
    require("1. Entscheidungsformel" in pdf_texts["P27"] and "2. Tatbestand" in pdf_texts["P27"] and "3. Entscheidungsgründe" in pdf_texts["P27"],
            "Urteilsaufbau nicht synchron")
    all_text = "\n".join(pdf_texts.values())
    require("Arbeitsgericht Konstanz" not in all_text, "Nicht existierendes Gericht")
    require("Kammern Radolfzell" in all_text and "Kammern Freiburg" in all_text, "Gerichtszuordnung fehlt")
    for value in ("Replik", "Duplik", "Triplik", "Zeuge", "Tatbestand", "Entscheidungsgründe", "Rechtsmittelbelehrung"):
        require(value.lower() in all_text.lower(), "Prozessbestandteil fehlt: " + value)
    require("16.11.2026" in pdf_texts["N18"] and "14.12.2026" in pdf_texts["N18"], "Unstimmige Fristen")
    appeal = re.sub(r"\s+", " ", pdf_texts["N19"])
    require("Berufung ein" in appeal and "gesonderten Schriftsatz vorbehalten" in appeal, "Nur fristwahrende Berufung erwartet")
    require("14. Oktober 2026" in appeal and "8. Oktober 2026" in appeal, "Angefochtenes Urteil/Zustellung fehlen")
    require(not any(re.search(r"Rechtsverletzung|fehlerhafte Beweiswürdigung|Berufungsbegründung", doc["title"], re.I)
                    for doc in documents), "Lösung oder Berufungsbegründung als Aktenstück")
    for doc_id in ("N05", "N06", "N09", "N13"):
        require(len(pdf_texts[doc_id]) > 1200, "Herkunft/Verfügbarkeit der neuen Belege zu knapp")
    require("14:10" in pdf_texts["N10"] and "16:20" in pdf_texts["N10"] and "08:32" in pdf_texts["N10"], "Anzeigen-/Konsultationssequenz unvollständig")
    judgment = next(doc for doc in documents if doc["kind"] == "judgment")
    require(next(file["pages"] for file in inventory["files"] if file["id"] == judgment["id"]) >= 7,
            "Urteil nicht vollständig genug")
    for rel in ("README.md", "testakte/README.md", "testakte/uferwerk-berufung/README.md"):
        page = (PLUGIN / rel).read_text()
        require(inventory["archive"] in page, "Download fehlt: " + rel)
        before = page.split(inventory["archive"], 1)[0]
        require("This test case file was generated with AI" in before[-800:], "Hinweis nicht unmittelbar vor Download: " + rel)
    print(f"Uferwerk: {len(documents)} Aktenstücke, {inventory['pdf_files']} PDFs, {inventory['pages']} Seiten; ZIP, Quellenbestand, Fristen und Prozessübergaben geprüft.")


if __name__ == "__main__":
    check()

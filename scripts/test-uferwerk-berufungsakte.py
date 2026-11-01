#!/usr/bin/env python3
"""Prüft die PDF-ZIP-only-Berufungsakte, ihren Bestand und zentrale Übergaben."""

import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import zipfile

from pypdf import PdfReader

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


def check():
    inventory = json.loads((PLUGIN / "testakte/pruefung/uferwerk-bestand.json").read_text())
    archive_path = PLUGIN / "testakte/downloads" / inventory["archive"]
    require(hashlib.sha256(archive_path.read_bytes()).hexdigest() == inventory["archive_sha256"], "Archiv nicht synchron")
    require(inventory["format"] == "pdf-zip-only-user-request", "Ausdrückliche Formatwahl fehlt")
    documents = []
    for entry in inventory["sources"]:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["sha256"],
                "PDF-Bestand nicht aus aktuellem Quellenstand: " + entry["path"])
    for part in ("vorgeschichte", "prozess", "nachurteil"):
        documents += json.loads((ROOT / "scripts/data" / ("uferwerk-" + part + ".json")).read_text())["documents"]
    by_id = {doc["id"]: doc for doc in documents}
    require(len(by_id) == len(documents) == inventory["documents"], "Quellenbestand")
    require(len(documents) >= 80 and inventory["pages"] > 100, "Umfang bleibt hinter der bestellten Lebens- und Prozessakte zurück")
    pdf_texts = {}
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

#!/usr/bin/env python3
"""Struktur, Belegpakete und rechtliche Verfahrensgrenzen reproduzierbar prüfen."""

import argparse
import csv
from email import policy
from email.parser import BytesParser
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

from docx import Document
from pypdf import PdfReader

from testakte_disclaimer import NOTICE_DE, NOTICE_EN, NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "untersuchungshaft"


def require(value, message):
    if not value:
        raise ValueError(message)


def pdf_pages(data):
    reader = PdfReader(io.BytesIO(data))
    require(bool(reader.pages), "Leeres PDF")
    pages = [re.sub(r"\s+", " ", p.extract_text()).strip() for p in reader.pages]
    for page in pages:
        require(len(page) > 30, "Leere oder verstümmelte PDF-Seite")
        require(NOTICE_DE not in page and NOTICE_EN not in page, "Warnseite in PDF")
    return pages


def check(dist=None):
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    require(len(skills) == 10, "Skillzahl")
    names = {p.parent.name for p in skills}
    for path in skills:
        text = path.read_text()
        require(text.startswith(f"---\nname: {path.parent.name}\n"), f"Frontmatter {path}")
        require("§" not in text and "**" not in text, f"Stil {path}")
        require(len(text.splitlines()) <= 500, f"Kontextbudget {path}")
        for number in range(1, 7):
            require(f"## 1.{number}." in text, f"Fachabschnitt {path}/{number}")
        for target in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", text):
            require(target in names, f"Toter Skillverweis {target}")
        for target in re.findall(r"`(\.\./[^`]+)`", text):
            require((path.parent / target).is_file(), f"Tote Referenz {path}/{target}")
    mini = (PLUGIN / "untersuchungshaft-schnellstart.md").read_text()
    require(max(len(mini), len(mini.encode()), len(mini.replace("\n", "\r\n"))) <= 7500, "Mini-Grenze")
    workshop = (PLUGIN / "untersuchungshaft-werkstatt.md").read_text()
    require(len(workshop.encode()) >= 25000, "Werkstattumfang")
    legal_guards = {
        "haftpruefung-muendlich-vorbereiten": ["117 Absatz 2", "118 Absatz 3", "118 Absatz 4", "zwei Wochen", "122 Absatz 3 Satz 4", "Ermessen"],
        "beschraenkungen-kontakt-pruefen": ["binnen drei Werktagen", "zur Genehmigung vorlegen"],
        "haftbeschwerde-begruenden": ["spätestens vor Ablauf von drei Tagen", "keine Einlegungsfrist", "310", "gewöhnliche E-Mail"],
        "vollzugsbedingungen-gerichtlich-pruefen": ["119a", "keine Ausschlussfrist", "Landesrecht", "keine Pflicht"],
        "jugendliche-heranwachsende-pruefen": ["unter 16", "109", "nicht pauschal", "Aufnahmezusage"],
        "haftdauer-beschleunigung-pruefen": ["Ruhen", "122a", "Sekundärvolltext", "keine starre"],
    }
    for slug, phrases in legal_guards.items():
        body = (PLUGIN / "skills" / slug / "SKILL.md").read_text()
        for phrase in phrases:
            require(phrase in body, f"Verfahrensgrenze fehlt: {slug}: {phrase}")
    cases = json.loads((ROOT / "scripts/data/untersuchungshaft-akten.json").read_text())
    require(len(cases) == 4, "Vier Akten erforderlich")
    total_pages = 0
    for case in cases:
        slug = case["slug"]
        require(len(slug) <= 64 and re.fullmatch(r"[a-z0-9-]+", slug), "Aktenslug")
        directory = ROOT / "testakten" / slug
        require(len(case["files"]) == 9, "Neun Originale je Akte")
        readme = (directory / "README.md").read_text()
        require(NOTICE_DE in readme and NOTICE_EN in readme, "Hinweis auf Downloadseite")
        originals = {}
        for item in case["files"]:
            path = directory / item["name"]
            require(path.name.isascii() and path.is_file(), f"Originalname {path}")
            data = path.read_bytes()
            originals[path.name] = data
            if path.suffix == ".docx":
                doc = Document(io.BytesIO(data))
                body = "\n".join(p.text for p in doc.paragraphs)
                require(len(body) >= 900 and item["title"] in body, f"Unvollständiges Word-Dokument {path}")
                require(doc.styles["Normal"].font.name == "Times New Roman", "Dokumentschrift")
            elif path.suffix == ".eml":
                mail = BytesParser(policy=policy.default).parsebytes(data)
                require(all(mail[h] for h in ("From", "To", "Date", "Subject", "Message-ID")), f"Mailheader {path}")
                body = mail.get_body(preferencelist=("plain",)).get_content()
                require(len(body) >= 500, f"Mailstummel {path}")
                attachments = {p.get_filename(): p.get_payload(decode=True) for p in mail.iter_attachments()}
                require(set(attachments) == set(item.get("attachments", [])), f"Mailanlagen fehlen: {path}")
                for name, payload in attachments.items():
                    require(payload == (directory / name).read_bytes(), f"Mailanlage veraltet: {name}")
            elif path.suffix == ".csv":
                body = data.decode("utf-8-sig")
                rows = list(csv.reader(io.StringIO(body), delimiter=";"))
                require(len(rows) >= 5 and len({len(r) for r in rows}) == 1, f"CSV-Struktur {path}")
            else:
                body = data.decode("utf-8")
            require("§" not in body, f"Paragrafenzeichen {path}")
            require(not any(word in body.casefold() for word in
                    ("musterlösung", "antwortmatrix", "lorem ipsum", "platzhalter", "testakte")), f"Metatext {path}")
        full = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        full_pages = pdf_pages(full.read_bytes())
        total_pages += len(full_pages)
        pdfzip = PLUGIN / "testakte/downloads" / f"testakte-{slug}-einzelpdfs.zip"
        with zipfile.ZipFile(pdfzip) as archive:
            expected = {Path(n).stem + ".pdf" for n in originals} | {"README.txt"}
            require(set(archive.namelist()) == expected, "Einzel-PDF-Zuordnung")
            require(archive.read("README.txt") == NOTICE_BYTES, "ZIP-Hinweis")
            separate_pages = []
            for name in originals:
                separate_pages += pdf_pages(archive.read(Path(name).stem + ".pdf"))
            require(separate_pages == full_pages, f"Gesamt-PDF nicht identisch mit Einzelbestand: {slug}")
            require(archive.testzip() is None, "ZIP defekt")
        with zipfile.ZipFile(PLUGIN / "testakte/downloads" / f"testakte-{slug}.zip") as archive:
            require(set(archive.namelist()) == set(originals) | {"README.txt", full.name}, "Original-ZIP Umfang")
            require(archive.read("README.txt") == NOTICE_BYTES, "Originalhinweis")
            for name, data in originals.items():
                require(archive.read(name) == data, f"Original weicht ab: {name}")
            require(archive.read(full.name) == full.read_bytes(), "Gesamt-PDF im Originalpaket veraltet")
    manifests = [json.loads((PLUGIN / p).read_text()) for p in
                 ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    require(len({(m["name"], m["version"], m["description"]) for m in manifests}) == 1, "Manifestkohärenz")
    require(manifests[0].get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Portables Manifestschema")
    entries = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
    require(len([x for x in entries if x["name"] == "untersuchungshaft"]) == 1, "Marketplacezuordnung")
    if dist:
        require(len(list(dist.iterdir())) == 27, "27 Release-Dateien")
        for portable in (False, True):
            prefix = "untersuchungshaft/" if portable else ""
            with zipfile.ZipFile(dist / f"untersuchungshaft{'-portable' if portable else ''}.zip") as archive:
                require(archive.testzip() is None, "PluginZIP defekt")
                require(sum(n.endswith("/SKILL.md") for n in archive.namelist()) == 10, "Paket-Skills")
                for name in archive.namelist():
                    relative = name.removeprefix(prefix)
                    source = ROOT / "LICENSE" if relative == "LICENSE" else PLUGIN / relative
                    require(source.is_file() and archive.read(name) == source.read_bytes(), f"Abweichendes Paket {name}")
                    require(not relative.endswith(("-werkstatt.md", "-schnellstart.md", ".pdf", ".zip", ".eml", ".docx")), "Zusatzmaterial im Plugin")
        for line in (dist / "checksums-sha256.txt").read_text().splitlines():
            digest, name = line.split("  ", 1)
            require(hashlib.sha256((dist / name).read_bytes()).hexdigest() == digest, f"Prüfsumme {name}")
        for path in skills:
            require((dist / f"untersuchungshaft-{path.parent.name}.md").read_bytes() == path.read_bytes(), "Skilldownload veraltet")
        for kind in ("werkstatt", "schnellstart"):
            name = f"untersuchungshaft-{kind}.md"
            require((dist / name).read_bytes() == (PLUGIN / name).read_bytes(), "Promptdownload veraltet")
        for case in cases:
            slug = case["slug"]
            name = f"{slug}_gesamt.pdf"
            require((dist / name).read_bytes() == (ROOT / "testakten" / slug / "gesamt-pdf" / name).read_bytes(), "PDF-Release veraltet")
            for suffix in ("", "-einzelpdfs"):
                name = f"testakte-{slug}{suffix}.zip"
                require((dist / name).read_bytes() == (PLUGIN / "testakte/downloads" / name).read_bytes(), "Aktenrelease veraltet")
    print(f"OK: 10 Skills, 4 Akten, 36 Originale, {total_pages} PDF-Seiten; Quellenstatus und Verfahrensgrenzen geprüft. Keine Modellbewertung.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    check(parser.parse_args().dist)

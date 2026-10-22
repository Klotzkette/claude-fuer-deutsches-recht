#!/usr/bin/env python3
"""Prüft Fachwege, Quellen, Paketgrenzen und die drei Kündigungsakten."""

import argparse
import csv
from datetime import date
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import zipfile

from docx import Document
from pypdf import PdfReader
import yaml

from testakte_disclaimer import NOTICE_DE, NOTICE_EN, NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
NAME = "arbeitsrecht-kuendigungsschutzklagewerkstatt"
PLUGIN = ROOT / NAME
SKILLS = {
    "frist-zugang-klageantrag", "arbeitgeber-schutzbereich-form",
    "betriebsbedingt-sozialauswahl", "krankheit-bem-pruefen",
    "verhalten-verdacht-aufklaeren", "sonderkuendigungsschutz-beteiligung",
    "massenentlassung-betriebsuebergang", "klage-erwiderung-beweisfuehrung",
    "guetetermin-vergleich-abfindung", "weiterbeschaeftigung-lohn-rechtsmittel",
    "kuendigungsschutzmandat-steuern",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def pdf_pages(data):
    reader = PdfReader(io.BytesIO(data))
    require(bool(reader.pages), "Leeres PDF")
    texts = [re.sub(r"\s+", " ", page.extract_text() or "").strip() for page in reader.pages]
    for text in texts:
        require(len(text) > 25, "Leere oder verstümmelte PDF-Seite")
        require(NOTICE_DE not in text and NOTICE_EN not in text, "Warntext gehört neben den Download")
    return texts


def check(dist=None):
    paths = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    require({path.parent.name for path in paths} == SKILLS, "Fachwege fehlen oder zusätzliche Wrapper-Skills")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        require(text.startswith("---\n"), "Frontmatter fehlt")
        front = yaml.safe_load(text.split("---", 2)[1])
        require(set(front) == {"name", "description"} and front["name"] == path.parent.name, str(path))
        require(80 <= len(front["description"]) <= 1024, "Beschreibungslänge")
        require(not re.search(r"\d,\d|[<>]", front["description"]), "Beschreibungsmuster")
        require("§" not in text and "**" not in text, "Skillstil")
        require("BAG" in text[:2400] and "Paragraf" in text[:2400], "Fachlicher Einstieg ohne Norm/Anker")
        for heading in range(1, 7):
            require(re.search(r"^## 1\." + str(heading) + r"(?:\.|\s)", text, re.M), f"Skillabschnitt fehlt: {path}")
        require(len(text) >= 3000 and len(text.splitlines()) <= 500, f"Skillumfang: {path}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "#")):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            require(resolved.is_relative_to(PLUGIN.resolve()) and resolved.is_file(), f"Ungepackte Referenz: {target}")
    prompts = {kind: PLUGIN / (NAME + "-" + kind + ".md")
               for kind in ("werkstatt", "schnellstart", "hauptproblem")}
    for kind, path in prompts.items():
        text = path.read_text(encoding="utf-8")
        require("§" not in text and "**" not in text, "Promptstil")
        require(all(re.match(r"^#{1,6} \d", line) for line in text.splitlines() if line.startswith("#")), "Dezimale Gliederung")
        require("KSchG" in text[:1800] and "2 AZR 68/24" in text[:1800], "Fachlicher Prompteinstieg")
        if kind != "werkstatt":
            require(max(len(text), len(text.encode()), len(text.replace("\n", "\r\n").encode())) <= 7500, "Kompaktgrenze")
        else:
            require(len(text.encode()) >= 30000, "Ausführliche Werkstatt fehlt")
        for case_number in ("6 AZR 157/22", "6 AZR 152/22", "6 AZR 7/26", "2 AZR 156/24", "2 AZR 426/18", "5 AZR 127/24"):
            require(case_number in text, f"Fachlicher Entscheidungsabgleich: {case_number}")
        require("Paragraf 46h ArbGG" in text, "Formfiktion für Prozesskündigung fehlt")
        require("Gesamtanrechnung" in text or "Gesamtberechnung" in text, "Anrechnung über Gesamtzeitraum fehlt")
    references = (PLUGIN / "references/rechtsprechung.md").read_text(encoding="utf-8")
    profile = json.loads((ROOT / "quality/evals" / (NAME + ".json")).read_text(encoding="utf-8"))
    module("quality_lab").validate_profile(profile, NAME, PLUGIN)
    require({case["target_skill"] for case in profile["cases"]} == SKILLS, "Prüffallabdeckung")
    for decision in profile["prompt_editorial_review"]["decisions"]:
        require(decision["url"] in references and decision["limit"], "Quellenzuordnung")
    download_checks = module("validate-testakten-readme-downloads")
    errors = []
    count = download_checks.validate_download_notices(NAME + "/README.md", (PLUGIN / "README.md").read_text(), errors)
    require(count == 3 and not errors, f"Downloadhinweise: {errors}")
    cases = json.loads((ROOT / "scripts/data/kuendigungsschutz-akten.json").read_text(encoding="utf-8"))
    module("build-kuendigungsschutz-akten").validate_data(cases)
    documents = pages = 0
    for case in cases:
        directory = ROOT / "testakten" / case["slug"]
        original_bytes = {}
        require(len(case["files"]) == 12, "Zwölf Dokumente je Akte")
        for item in case["files"]:
            path = directory / item["name"]
            data = path.read_bytes()
            original_bytes[path.name] = data
            if path.suffix == ".docx":
                doc = Document(io.BytesIO(data))
                body = "\n".join(paragraph.text for paragraph in doc.paragraphs)
                require(len(body) >= 600 and doc.styles["Normal"].font.name == "Times New Roman", "Word-Original verstümmelt")
                require(doc.core_properties.author == "Klotzkette", "Dokumentautor")
            elif path.suffix == ".eml":
                message = BytesParser(policy=policy.default).parsebytes(data)
                require(not message.defects and all(message[key] for key in ("From", "To", "Date", "Subject", "Message-ID")), "Mailheader")
                require(len(message.get_body(preferencelist=("plain",)).get_content()) >= 500, "Mailstummel")
                attachments = {part.get_filename(): part.get_payload(decode=True) for part in message.iter_attachments()}
                require(set(attachments) == set(item.get("attachments", [])), "MIME-Anlagenliste")
                for filename, payload in attachments.items():
                    require(payload == (directory / filename).read_bytes(), "Veraltete E-Mail-Anlage")
            elif path.suffix == ".csv":
                rows = list(csv.reader(io.StringIO(data.decode("utf-8-sig")), delimiter=";"))
                require(len(rows) >= 5 and len({len(row) for row in rows}) == 1, "CSV-Zeilen/Spalten")
            raw = (body if path.suffix == ".docx" else item.get("body", ""))
            require(not re.search(r"Lösungsmatrix|Musterlösung|Formathinweis|Lorem|TODO|§", raw, re.I), "Spoiler oder Rumpftext")
        base = PLUGIN / "testakte/downloads" / ("testakte-" + case["slug"])
        with zipfile.ZipFile(str(base) + ".zip") as archive:
            require(archive.testzip() is None, "Defektes Originalarchiv")
            require(set(archive.namelist()) == set(original_bytes) | {"README.txt"}, "Originalarchivinhalt")
            require(archive.read("README.txt") == NOTICE_BYTES, "Originalhinweis")
            require(all("/" not in name and not name.endswith(".md") for name in archive.namelist()), "Unterordner oder Markdown im Originalarchiv")
            for filename, data in original_bytes.items():
                require(archive.read(filename) == data, "Originalarchiv nicht synchron")
        individual_texts = []
        with zipfile.ZipFile(str(base) + "-einzelpdfs.zip") as archive:
            require(archive.testzip() is None and archive.read("README.txt") == NOTICE_BYTES, "PDF-Archiv/Hinweis")
            require(set(archive.namelist()) == {Path(name).stem + ".pdf" for name in original_bytes} | {"README.txt"}, "PDF je Original")
            for filename in original_bytes:
                pdf = archive.read(Path(filename).stem + ".pdf")
                text_pages = pdf_pages(pdf)
                item = next(item for item in case["files"] if item["name"] == filename)
                if item.get("contract"):
                    require(len(text_pages) >= 2, "Arbeitsvertrag nicht vollständig mehrseitig")
                individual_texts += text_pages
        total = directory / "gesamt-pdf" / (case["slug"] + "_gesamt.pdf")
        require(pdf_pages(total.read_bytes()) == individual_texts, "Gesamt-PDF und Einzel-PDFs divergieren")
        documents += len(original_bytes)
        pages += len(individual_texts)
    if dist:
        files = {path.name: path for path in dist.iterdir() if path.is_file()}
        require(len(files) == 26, "Releaseumfang")
        for line in files["checksums-sha256.txt"].read_text().splitlines():
            digest, filename = line.split("  ", 1)
            require(hashlib.sha256(files[filename].read_bytes()).hexdigest() == digest, "Prüfsumme")
        for portable in (False, True):
            prefix = NAME + "/" if portable else ""
            filename = NAME + ("-portable" if portable else "") + ".zip"
            with zipfile.ZipFile(files[filename]) as archive:
                members = archive.namelist()
                require(archive.testzip() is None, "Defektes Pluginarchiv")
                require(sum(name.endswith("/SKILL.md") for name in members) == 11, "Skillzahl im ZIP")
                require(all(not re.search(r"(^|/)(testakte|testakten|downloads)/|-(werkstatt|schnellstart|hauptproblem)\.md$", name) for name in members), "Begleitmaterial im installierbaren Paket")
                for member in members:
                    relative = member.removeprefix(prefix)
                    expected = ROOT / "LICENSE" if relative == "LICENSE" else PLUGIN / relative
                    require(archive.read(member) == expected.read_bytes(), "Pluginarchiv enthält veralteten Inhalt")
        for kind, path in prompts.items():
            require(files[path.name].read_bytes() == path.read_bytes(), "Promptrelease nicht synchron")
    print(f"Kündigungsschutzwerkstatt OK: elf Skills, drei Prompts, {documents} Originale, {pages} PDF-Seiten; keine behaupteten Modelltests.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    check(parser.parse_args().dist)

#!/usr/bin/env python3
"""Prüft Paketgrenzen, Fiktionskennzeichnung und Formatgleichheit der Sanktionsakten."""

import argparse
import csv
from datetime import datetime
from decimal import Decimal
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import tempfile
import zipfile

from docx import Document
from pypdf import PdfReader
import yaml
from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_EN
from testakte_zip_common import working_dump_flat_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ("eu-sanktionspruefer", "us-sanktionspruefer")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def pages(data):
    result = []
    for page in PdfReader(io.BytesIO(data)).pages:
        text = re.sub(r"\s+", " ", page.extract_text() or "").strip()
        require(len(text) > 30, "Leere oder verstümmelte PDF-Seite")
        require(NOTICE_DE not in text and NOTICE_EN not in text, "Allgemeiner Warntext gehört auf die Downloadseite")
        result.append(text)
    require(result, "Leeres PDF")
    return result


def check_plugins():
    catalog = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
    for name in PLUGINS:
        plugin = ROOT / name
        skills = sorted((plugin / "skills").glob("*/SKILL.md"))
        require(len(skills) == 10, f"Genau zehn Skills erforderlich: {name}")
        names = {path.parent.name for path in skills}
        for path in skills:
            body = path.read_text(encoding="utf-8")
            require(body.startswith("---\n"), f"Frontmatter fehlt: {path}")
            front = yaml.safe_load(body.split("---", 2)[1])
            require(set(front) == {"name", "description"} and front["name"] == path.parent.name, f"Skillidentität: {path}")
            require(80 <= len(front["description"]) <= 1024, f"Beschreibungslänge: {path}")
            require(len(body) >= 1800 and len(body.splitlines()) <= 500, f"Skillumfang: {path}")
            require("§" not in body and "**" not in body, f"Skillstil: {path}")
            for number in range(1, 7):
                require(f"## 1.{number}." in body, f"Abschnitt {number} fehlt: {path}")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
                if target.startswith(("https://", "#")):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                require(resolved.is_relative_to(plugin.resolve()) and resolved.is_file(), f"Referenz außerhalb des Pakets: {path}/{target}")
        manifests = [json.loads((plugin / relative).read_text()) for relative in
                     ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
        require(len({(v["name"], v["version"], v["description"]) for v in manifests}) == 1, f"Manifestkohärenz: {name}")
        require(manifests[0]["version"] == "1.0.0", "Falsche Komponentenversion")
        entry = [entry for entry in catalog if entry["name"] == name]
        require(len(entry) == 1 and entry[0]["version"] == "1.0.0" and
                entry[0]["description"] == manifests[0]["description"], f"Marketplaceabweichung: {name}")
        for kind in ("werkstatt", "schnellstart", "hauptproblem"):
            prompt = (plugin / f"{name}-{kind}.md").read_text(encoding="utf-8")
            require("§" not in prompt and "**" not in prompt, f"Promptstil: {name}/{kind}")
            require(all(re.match(r"^#{1,6} \d", line) for line in prompt.splitlines() if line.startswith("#")),
                    f"Dezimale Gliederung fehlt: {name}/{kind}")
            if kind != "werkstatt":
                require(max(len(prompt), len(prompt.encode()), len(prompt.replace("\n", "\r\n").encode())) <= 7500,
                        f"Kompaktbudget einschließlich UTF-8/CRLF: {name}/{kind}")
            else:
                require(18000 <= len(prompt.encode()) <= 1024 * 1024, f"Werkstattumfang: {name}")
        profile = json.loads((ROOT / "quality/evals" / f"{name}.json").read_text())
        module("quality_lab").validate_profile(profile, name, plugin)
        require({case["target_skill"] for case in profile["cases"]} == names, f"Individueller Prüffall pro Skill fehlt: {name}")
        reference_text = "\n".join(path.read_text() for path in (plugin / "references").glob("*.md"))
        for decision in profile["prompt_editorial_review"]["decisions"]:
            require(decision["url"] in reference_text and decision["application"] and decision["limit"],
                    f"Entscheidungsbeleg oder Aussagegrenze fehlt: {decision['citation']}")
        errors = []
        count = module("validate-testakten-readme-downloads").validate_download_notices(
            f"{name}/README.md", (plugin / "README.md").read_text(), errors)
        require(count == 2 and not errors, f"Plugin-Downloadhinweise: {errors}")
        require(not working_dump_flat_pairs(plugin / "testakte", include_gesamt_pdf=False),
                f"Downloadarchive dürfen nicht als zusätzliche lokale Akte gezählt oder verpackt werden: {name}")


def check_cases():
    cases = json.loads((ROOT / "scripts/data/sanktionen-akten.json").read_text(encoding="utf-8"))
    module("build-sanktionen-akten").validate_data(cases)
    check_case_arithmetic(cases)
    page_count = 0
    for case in cases:
        slug, plugin = case["slug"], ROOT / case["plugin"]
        directory = ROOT / "testakten" / slug
        require(re.fullmatch(r"[a-z0-9-]{1,64}", slug), "Ungültiger Aktenslug")
        errors = []
        require(module("validate-testakten-readme-downloads").validate_local_readme(slug, directory, errors) == 6 and not errors,
                f"Downloadhinweise: {slug}: {errors}")
        originals = {}
        for item in case["files"]:
            path = directory / item["name"]
            require(path.is_file() and path.parent == directory, f"Original fehlt: {path}")
            data = path.read_bytes()
            originals[path.name] = data
            if path.suffix == ".docx":
                doc = Document(io.BytesIO(data))
                body = "\n".join(p.text for p in doc.paragraphs)
                require(doc.styles["Normal"].font.name == "Times New Roman" and doc.styles["Normal"].font.size.pt == 11,
                        f"Schriftstandard: {path}")
                require(doc.core_properties.author == "Klotzkette", f"Dokumentautor: {path}")
                normalized = re.sub(r"\s+", " ", body)
                require(all(re.sub(r"\s+", " ", paragraph) in normalized for paragraph in item["body"].split("\n\n")),
                        f"Original stimmt nicht mit Quelle überein: {path}")
            elif path.suffix == ".eml":
                mail = BytesParser(policy=policy.default).parsebytes(data)
                require(all(mail[header] for header in ("From", "To", "Date", "Subject", "Message-ID", "Received", "MIME-Version")),
                        f"Mailheader unvollständig: {path}")
                require(not mail.defects, f"Mailformat defekt: {path}")
                body = mail.get_body(preferencelist=("plain",)).get_content()
                require(body.replace("\r\n", "\n").strip() == item["body"].strip(), f"Mailtext verändert: {path}")
                attached = {part.get_filename(): part.get_payload(decode=True) for part in mail.iter_attachments()}
                require(attached == {name: (directory / name).read_bytes() for name in item.get("attachments", [])},
                        f"Mailanhang fehlt oder ist veraltet: {path}")
                if item.get("reply_to"):
                    prior = BytesParser(policy=policy.default).parsebytes((directory / item["reply_to"]).read_bytes())
                    for header in ("In-Reply-To", "References"):
                        require(str(mail[header]) == str(prior["Message-ID"]), f"Mailbezug falsch: {path}")
                        require("=?" not in next(v for k, v in mail.raw_items() if k == header), f"Kennung falsch kodiert: {path}")
            elif path.suffix == ".csv":
                with path.open(encoding="utf-8-sig", newline="") as stream:
                    rows = list(csv.reader(stream, delimiter=";"))
                require(rows == [[str(cell) for cell in row] for row in item["rows"]], f"CSV nicht quellengleich: {path}")
                body = data.decode("utf-8-sig")
            else:
                body = data.decode("utf-8")
                require(item["body"] in body, f"Textoriginal verändert: {path}")
            require("§" not in body, f"Paragraf ausschreiben: {path}")
            require(not any(word in body.casefold() for word in ("musterlösung", "antwortmatrix", "lorem ipsum")),
                    f"Lösung oder Blindtext: {path}")
        require({name for _, name in working_dump_flat_pairs(directory, include_gesamt_pdf=False)} == set(originals),
                f"Zentraler Aktenexport würde andere Originale liefern: {slug}")
        full_pages = pages((directory / "gesamt-pdf" / f"{slug}_gesamt.pdf").read_bytes())
        page_count += len(full_pages)
        with zipfile.ZipFile(plugin / "downloads" / f"testakte-{slug}-einzelpdfs.zip") as archive:
            require(set(archive.namelist()) == {Path(name).stem + ".pdf" for name in originals} | {"README.txt"},
                    f"PDF-ZIP ist nicht flach oder enthält falsche Dokumente: {slug}")
            require(archive.testzip() is None and archive.read("README.txt").startswith(NOTICE_BYTES), "Archiv oder Hinweis defekt")
            separate = []
            for item in case["files"]:
                rendered = pages(archive.read(Path(item["name"]).stem + ".pdf"))
                if "KEIN RECHTSAKT" in item.get("body", ""):
                    require("KEIN RECHTSAKT" in rendered[0] and "NOT A LEGAL ACT" in rendered[0],
                            f"Erfundene Listung nicht auf erster PDF-Seite gekennzeichnet: {slug}")
                separate += rendered
            require(separate == full_pages, f"Gesamt-PDF und Einzel-PDFs widersprechen sich: {slug}")
        with zipfile.ZipFile(plugin / "downloads" / f"testakte-{slug}.zip") as archive:
            require(set(archive.namelist()) == set(originals) | {"README.txt"}, f"Original-ZIP enthält Ordner oder Markdown: {slug}")
            require(archive.testzip() is None and archive.read("README.txt").startswith(NOTICE_BYTES), "Archiv oder Hinweis defekt")
            require(all(archive.read(name) == value for name, value in originals.items()), f"Veraltete Originale: {slug}")
    return page_count


def check_case_arithmetic(cases):
    by_slug = {case["slug"]: {item["name"]: item for item in case["files"]} for case in cases}

    def number(value):
        return Decimal(value.replace(",", "."))

    def table(slug, name):
        return by_slug[slug][name]["rows"][1:]

    def amounts(slug, name, quantity, price, total):
        rows = table(slug, name)
        for row in rows:
            require(number(row[quantity]) * number(row[price]) == number(row[total]),
                    f"Menge, Einzelpreis und Betrag widersprechen sich: {slug}/{name}/{row[0]}")
        return sum(number(row[total]) for row in rows)

    eu = "sanktionen-eu-zwirnmark-beteiligung"
    shares = table(eu, "10_Anteile.csv")
    require([sum(number(row[col]) for row in shares) for col in (1, 2, 3, 4)] ==
            [1000, 100000, 100, 1000], "Gesellschafterkartei Zwirnmark nicht ausgeglichen")
    total = amounts(eu, "11_Auftragspositionen.csv", 2, 3, 4)
    require(total == 86400 and total * Decimal("0.3") == 25920 and total * Decimal("0.7") == 60480,
            "Auftrag, Anzahlung und Restbetrag Zwirnmark widersprechen sich")

    eu = "sanktionen-eu-faltenfels-mandat"
    fees = amounts(eu, "10_Zeiterfassung.csv", 2, 3, 4)
    require(sum(number(row[2]) for row in table(eu, "10_Zeiterfassung.csv")) == 12 and fees == 3600,
            "Zeitaufwand und Honorarbetrag Faltenfels widersprechen sich")
    goods = amounts(eu, "11_Lieferkalkulation.csv", 2, 3, 4)
    require(goods == 15000 and fees * Decimal("1.19") == 4284 and goods - 4284 == 10716,
            "Zahlungsbeträge Faltenfels widersprechen sich; Steueransatz bleibt ungeklärt")

    us = "sanktionen-us-klingelgau-eigentum"
    shares = table(us, "10_Ownership.csv")
    require([sum(number(row[col]) for row in shares) for col in (1, 2, 3)] == [1000, 100, 1000],
            "Gesellschafterkartei Klingelgau nicht ausgeglichen")
    rows = table(us, "11_Order_Lines.csv")
    for row in rows:
        require(number(row[2]) * number(row[4]) == number(row[5]), "Bestellposition Klingelgau widersprüchlich")
    require({currency: sum(number(row[5]) for row in rows if row[3] == currency)
             for currency in {row[3] for row in rows}} == {"USD": 48000, "EUR": 9600},
            "Währungen oder Einzelaufträge Klingelgau vermischt")

    us = "sanktionen-us-sonnenquast-namensgleichheit"
    balance = Decimal(0)
    for row in table(us, "10_Spendeneingaenge.csv"):
        balance += number(row[3])
        require(balance == number(row[4]), f"Laufender Spendenbestand falsch: {row[1]}")
    require(balance == 15000 and balance - 6000 == 9000, "Vormerkung und Buchbestand Sonnenquast widersprüchlich")


def check_dist(dist):
    require(len(list(dist.iterdir())) == 43, "43 Release-Dateien erforderlich")
    for plugin in PLUGINS:
        for portable in (False, True):
            prefix = plugin + "/" if portable else ""
            with zipfile.ZipFile(dist / f"{plugin}{'-portable' if portable else ''}.zip") as archive:
                require(archive.testzip() is None, "Defektes Plugin-ZIP")
                require(sum(name.endswith("/SKILL.md") for name in archive.namelist()) == 10, "Paket-Skillzahl")
                for name in archive.namelist():
                    require(not name.startswith("/") and ".." not in Path(name).parts, "Unsicherer Archivpfad")
                    relative = name.removeprefix(prefix)
                    source = ROOT / "LICENSE" if relative == "LICENSE" else ROOT / plugin / relative
                    require(source.is_file() and archive.read(name) == source.read_bytes(), f"Paketabweichung: {name}")
                    require(not relative.endswith(("-werkstatt.md", "-schnellstart.md", "-hauptproblem.md", ".pdf", ".zip", ".docx", ".eml")),
                            "Zusatzmaterial wird ungewollt installiert")
    for line in (dist / "checksums-sha256.txt").read_text().splitlines():
        digest, name = line.split("  ", 1)
        require(hashlib.sha256((dist / name).read_bytes()).hexdigest() == digest, f"Prüfsumme falsch: {name}")
    builder = module("build-sanktionen-release")
    with tempfile.TemporaryDirectory(prefix="sanktionen-rebuild-") as temporary:
        rebuilt = Path(temporary)
        builder.build(rebuilt)
        require(all(path.read_bytes() == (rebuilt / path.name).read_bytes() for path in dist.iterdir()), "Release nicht reproduzierbar")
        try:
            builder.build(rebuilt)
        except ValueError:
            pass
        else:
            raise ValueError("Builder überschreibt gefülltes Ausgabeverzeichnis")


def check(dist=None):
    check_plugins()
    count = check_cases()
    if dist:
        check_dist(dist)
    print(f"OK: 2 Plugins, 20 Skills, 6 Begleitprompts, 4 Akten, 48 Originale und {count} PDF-Seiten. Redaktionelle und technische Prüfung, kein Live-Modelltest.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    check(parser.parse_args().dist)

"""Plattformunabhängige, ausschließlich lesende Bindung von bAV-Quellen und PDFs."""
from __future__ import annotations
import hashlib
import io
import json
import re
from pathlib import Path
import zipfile

from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs

INVENTORY = "bav-strategie-konzern/testakten/pruefung/bestand.json"
GENERATOR_PATHS = (
    "scripts/build-bav-konzern-akten.py", "scripts/bav_konzern_render.py",
    "scripts/bav_konzern_office.mjs", "scripts/build-bav-konzern-exports.py",
    "scripts/build-testakten-einzelpdf-zips.py", "scripts/build-testakte-gesamt-pdf.py",
    "scripts/testakte_office_pdf.py", "scripts/testakte_einzelpdf_common.py",
)
EXPECTED_SLUGS = frozenset({"bav-strategie-konzern-meissner-rheinwerk-ag", "bav-carve-out-rheinbogen-automation",
                           "bav-rentnergesellschaft-rheinhafen-logistik", "bav-pensionskasse-niederrhein-verbund"})


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pdf_facts(data):
    reader = PdfReader(io.BytesIO(data))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return {"sha256": sha(data), "pages": len(reader.pages), "text_sha256": sha(text.encode())}


def checked_file(root, record):
    path = Path(record["path"])
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsicherer Inventarpfad {path}")
    file = root / path
    if not file.resolve().is_relative_to(root.resolve()) or any(p.is_symlink() for p in (file, *file.parents) if p != root.parent):
        raise ValueError(f"Quelle außerhalb des Checkouts oder Symlink: {path}")
    if not file.is_file():
        raise ValueError(f"Reguläre Quelle fehlt: {path}")
    data = file.read_bytes()
    if sha(data) != record["sha256"]:
        raise ValueError(f"Quellhash abweichend: {path}")
    return data


def verify_inventory(root: Path) -> dict:
    """Prüft exakten Quellbestand, Generatoren, Fixture und jeden PDF-Mitgliedsinhalt.

    Keine Satzschriften, LibreOffice, Netzverbindung oder Artefakt-Runtime nötig.
    Ein aktualisierter äußerer ZIP-Hash allein genügt ausdrücklich nicht.
    """
    root = Path(root).resolve()
    inventory = json.loads((root / INVENTORY).read_text())
    if inventory.get("schema_version") != 1 or len(inventory.get("cases", [])) != 4:
        raise ValueError("bAV-Inventar muss alle vier Fälle im Schema 1 enthalten")
    if {c["slug"] for c in inventory["cases"]} != EXPECTED_SLUGS:
        raise ValueError("Falsche oder doppelte bAV-Fallzuordnung")
    if {r["path"] for r in inventory["generators"]} != set(GENERATOR_PATHS):
        raise ValueError("Unvollständige Generatorbindung")
    if len(inventory["generators"]) != len(GENERATOR_PATHS):
        raise ValueError("Doppelte Generatorbindung")
    for record in inventory["generators"]:
        checked_file(root, record)
    for case in inventory["cases"]:
        slug = case["slug"]
        directory = root / "testakten" / slug
        if case["fixture"]["path"] != f"scripts/data/bav-konzern-faelle/{slug}.json":
            raise ValueError("Falscher Fixturepfad")
        fixture = json.loads(checked_file(root, case["fixture"]))
        if fixture["slug"] != slug:
            raise ValueError("Fixture gehört zu anderem Fall")
        expected = {str(p.relative_to(root)): p for p, _ in working_dump_archive_pairs(directory, include_gesamt_pdf=False)}
        if set(expected) != {r["path"] for r in case["sources"]}:
            raise ValueError(f"Nativer Bestand weicht ab: {slug}")
        if len(expected) != len(case["sources"]):
            raise ValueError("Doppelte native Quelle")
        fixture_items = [r for group in ("documents", "workbooks", "slides") for r in fixture.get(group, [])]
        fixture_paths = {str(directory.relative_to(root) / r["path"]) for r in fixture_items}
        if len(fixture_paths) != len(fixture_items):
            raise ValueError("Doppelte Fixturequelle")
        if fixture_paths != set(expected):
            raise ValueError(f"Fixture und native Auslieferung weichen ab: {slug}")
        for record in case["sources"]:
            checked_file(root, record)
        singles = case["pdf_zip"]
        if singles["path"] != f"bav-strategie-konzern/testakten/downloads/testakte-{slug}-einzelpdfs.zip":
            raise ValueError("PDF-ZIP-Pfad gehört nicht zum Fall")
        data = checked_file(root, singles)
        pairs = dict((n, p) for p, n in document_arcname_pairs(directory))
        records = {r["path"]: r for r in singles["members"]}
        if len(records) != len(singles["members"]):
            raise ValueError("Doppeltes PDF-Mitglied im Inventar")
        if set(records) != set(pairs):
            raise ValueError(f"Unvollständige PDF-Quellzuordnung: {slug}")
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            if len(z.namelist()) != len(set(z.namelist())) or set(z.namelist()) != {"README.txt", *pairs}:
                raise ValueError(f"PDF-ZIP-Bestand weicht ab: {slug}")
            if not z.read("README.txt").startswith(NOTICE_BYTES):
                raise ValueError("Pflichthinweis fehlt")
            for name, source in pairs.items():
                pdf = z.read(name)
                facts = pdf_facts(pdf)
                if facts != {k: records[name][k] for k in facts}:
                    raise ValueError(f"PDF-Inventar stimmt nicht: {slug}/{name}")
                if not facts["pages"]:
                    raise ValueError(f"Leere PDF: {name}")
                if source.suffix.lower() == ".pdf" and pdf != source.read_bytes():
                    raise ValueError(f"Original-PDF verändert: {name}")
        combined = case["gesamt_pdf"]
        if combined["path"] != f"testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf":
            raise ValueError("Gesamt-PDF-Pfad gehört nicht zum Fall")
        facts = pdf_facts(checked_file(root, combined))
        if facts != {k: combined[k] for k in facts} or facts["pages"] != sum(r["pages"] for r in records.values()):
            raise ValueError(f"Gesamt-PDF-Seiten/-Inhalt weichen ab: {slug}")
    return inventory

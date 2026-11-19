"""Druckfassungen und zweistufige PDF-Lesezeichen für die beiden Parallelakten."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import tempfile
import zipfile
from collections.abc import Iterator
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs

NEURALIS = "neuralis-medtech-erlangen-gestaltungsakte"
STAGES = {
    NEURALIS: {
        "Grundakte": "Grundakte · Juli 2023",
        "01_Bescheid_und_erste_Aenderung": "Bescheid und erste Satzungsänderung",
        "02_Gestaltungsvorschlaege": "Anwaltliche Gestaltungsvorschläge",
    },
    "autohaus-boeblingen": {
        "Grundakte": "Grundakte",
        "Nachlieferung": "Nachlieferung",
    },
}


def sources(case: Path) -> list[tuple[Path, str]]:
    """In jeder Stufe nach Aktenzeichen lesen, Grundakte stets zuerst."""
    stages = list(STAGES[case.name])
    pairs = document_arcname_pairs(case)
    found = {Path(name).parent.as_posix() for _, name in pairs}
    if found != set(stages):
        raise ValueError(f"{case.name}: unerwartete oder fehlende Aktenstufen: {found ^ set(stages)}")
    return sorted(pairs, key=lambda pair: (stages.index(Path(pair[1]).parent.name), pair[1]))


def checked_neuralis_prints(case: Path) -> Iterator[tuple[str, bytes]]:
    """Verknüpft jede native Quelle mit genau einer redaktionell geprüften Druckfassung."""
    repo = case.resolve().parent.parent
    workshop = repo / "docs/workshops/status-notariat"
    manifest = json.loads((workshop / "druckfassungen-sha256.json").read_text(encoding="utf-8"))
    pairs = sources(case)
    rows = {row["source"]: row for row in manifest}
    expected = {source.relative_to(case).as_posix() for source, _ in pairs}
    if len(rows) != len(manifest) or rows.keys() != expected:
        raise ValueError(f"{case.name}: Quellenliste weicht vom Aktenbestand ab: {rows.keys() ^ expected}")

    for source, member in pairs:
        relative = source.relative_to(case)
        row = rows[relative.as_posix()]
        directory = "gestaltung" if relative.parent.name == "02_Gestaltungsvorschlaege" else relative.parent.name
        print_path = (workshop / "lesefassungen" / directory / relative.with_suffix(".pdf").name).resolve()
        pdf = (repo / row["pdf"]).resolve()
        if pdf != print_path and not (source.suffix.lower() == ".pdf" and pdf == source.resolve()):
            raise ValueError(f"{relative}: Druckfassung gehört nicht zur Quelle: {row['pdf']}")
        native = source.read_bytes()
        data = pdf.read_bytes()
        if (hashlib.sha256(native).hexdigest() != row["source_sha256"]
                or hashlib.sha256(data).hexdigest() != row["pdf_sha256"]):
            raise ValueError(f"{relative}: Quelle oder Druckfassung seit Sichtprüfung geändert")
        if source.suffix.lower() == ".pdf" and native != data:
            raise ValueError(f"{relative}: Original-PDF und Druckfassung weichen ab")
        if not len(PdfReader(io.BytesIO(data)).pages):
            raise ValueError(f"{relative}: Druckfassung ohne Seiten")
        yield member, data


def build_release_pdf(case: Path) -> Path:
    """Dieselben Dokumentseiten wie im Einzel-PDF-Archiv, ohne Vorspann."""
    case = case.resolve()
    path = Path(__file__).with_name("build-testakten-einzelpdf-zips.py")
    spec = importlib.util.spec_from_file_location("gestufte_einzelpdfs", path)
    exporter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exporter)

    target = case / "gesamt-pdf" / f"{case.name}_gesamt.pdf"
    target.parent.mkdir(exist_ok=True)
    stages = STAGES[case.name]
    pairs = sources(case)
    writer = PdfWriter()
    parents = {}
    with tempfile.TemporaryDirectory(dir=target.parent) as scratch:
        archive, count = exporter.build_single(case, Path(scratch))
        with zipfile.ZipFile(archive) as individual:
            expected = {name for _, name in pairs} | {NOTICE_FILENAME}
            if (count != len(pairs) or set(individual.namelist()) != expected
                    or len(individual.namelist()) != len(expected)
                    or individual.read(NOTICE_FILENAME) != NOTICE_BYTES):
                raise ValueError(f"{case.name}: unerwarteter Inhalt im Einzel-PDF-Archiv")
            for _, name in pairs:
                stage = Path(name).parent.name
                first_page = len(writer.pages)
                writer.append(io.BytesIO(individual.read(name)), import_outline=False)
                if len(writer.pages) == first_page:
                    raise ValueError(f"{name}: keine Dokumentseiten")
                if stage not in parents:
                    parents[stage] = writer.add_outline_item(stages[stage], first_page)
                title = Path(name).stem.replace("_", " ")
                writer.add_outline_item(title, first_page, parent=parents[stage])
        writer.add_metadata({"/Title": f"Gesamtakte · {case.name}", "/Author": "Kanzleiakte"})
        output = Path(scratch) / target.name
        writer.write(output)
        output.replace(target)
    return target

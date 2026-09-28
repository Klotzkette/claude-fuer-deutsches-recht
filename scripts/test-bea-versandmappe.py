#!/usr/bin/env python3
"""End-to-End-Test für die lokale Anlagen- und Versandmappenproduktion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from types import ModuleType

from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from testakte_zip_common import working_dump_archive_pairs


REPO = Path(__file__).resolve().parent.parent
TOOL = (
    REPO
    / "anlagen-zu-schriftsaetzen"
    / "skills"
    / "anlagen-zu-schriftsaetzen"
    / "werkzeuge"
    / "build_anlagenkonvolut.py"
)


def load_tool() -> ModuleType:
    spec = importlib.util.spec_from_file_location("build_anlagenkonvolut", TOOL)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Werkzeug nicht ladbar: {TOOL}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_pdf(path: Path, title: str, pages: int) -> None:
    pdf = canvas.Canvas(str(path), pagesize=A4)
    _, height = A4
    for page in range(1, pages + 1):
        pdf.setFont("Helvetica-Bold", 15)
        pdf.drawString(56, height - 72, title)
        pdf.setFont("Helvetica", 11)
        pdf.drawString(56, height - 106, f"Seite {page} von {pages}")
        for row in range(8):
            pdf.drawString(
                56,
                height - 145 - row * 22,
                f"Ausformulierter Dokumentinhalt {row + 1} auf Seite {page}.",
            )
        pdf.showPage()
    pdf.save()


def check_modefuchs_eval_inputs() -> None:
    case_dir = REPO / "testakten" / "inkasso-zahlungsklage-modefuchs"
    profile = json.loads(
        (REPO / "quality" / "evals" / "bea-versand.json").read_text(encoding="utf-8")
    )
    cases = [
        case for case in profile["cases"]
        if case["id"] == "modefuchs-inhalt-statt-dateiname"
    ]
    if len(cases) != 1:
        raise AssertionError("Genau ein ModeFuchs-beA-Testfall erwartet")
    inputs = cases[0]["input_files"]
    expected = {
        path.relative_to(REPO).as_posix()
        for path, _ in working_dump_archive_pairs(case_dir, include_gesamt_pdf=False)
    }
    if len(expected) != 47 or len(inputs) != 47 or set(inputs) != expected:
        raise AssertionError(
            "beA-Eval muss genau die 47 kanonischen ModeFuchs-Arbeitsdateien nutzen; "
            f"Arbeitsbestand={len(expected)}, Eingaben={len(inputs)}, "
            f"fehlend={sorted(expected - set(inputs))}, "
            f"unerwartet={sorted(set(inputs) - expected)}"
        )
    hashes = json.loads(
        (REPO / "scripts" / "fixtures" / "modefuchs" / "originale-sha256.json")
        .read_text(encoding="utf-8")
    )
    originals = set((case_dir / "originale").glob("*.pdf"))
    if len(hashes) != 28 or {path.name for path in originals} != set(hashes):
        raise AssertionError("Genau die 28 erhaltenen ModeFuchs-Original-PDFs erwartet")
    for path in originals:
        if hashlib.sha256(path.read_bytes()).hexdigest() != hashes[path.name]:
            raise AssertionError(f"ModeFuchs-Original veraendert: {path.name}")


def main() -> int:
    check_modefuchs_eval_inputs()
    tool = load_tool()
    with tempfile.TemporaryDirectory(prefix="bea-versandmappe-test-") as tmp:
        root = Path(tmp)
        source = root / "eingang"
        target = root / "ausgang"
        source.mkdir()

        lead = source / "Hauptdokument.pdf"
        write_pdf(lead, "Klageerwiderung", 2)
        write_pdf(source / "Anlage_K-01_Kaufvertrag.pdf", "Kaufvertrag", 2)
        write_pdf(source / "Anlage_K-02_Mahnung.pdf", "Mahnung", 2)

        exit_code = tool.main(
            [
                "--eingang",
                str(source),
                "--ausgang",
                str(target),
                "--praefix",
                "K",
                "--hauptdokument",
                str(lead),
                "--dokumentart",
                "Klageerwiderung",
                "--profil",
                "berlin",
                "--datum",
                "20260711",
                "--gericht",
                "Landgericht Berlin II",
                "--aktenzeichen",
                "12 O 34/26",
                "--strict",
            ]
        )
        if exit_code != 0:
            raise AssertionError(f"Werkzeuglauf endete mit Status {exit_code}")

        shipping = target / "versandfertig"
        shipped = sorted(shipping.glob("*.pdf"))
        if len(shipped) != 3:
            raise AssertionError(f"Drei Versanddateien erwartet, erhalten: {shipped}")

        exhibits = [path for path in shipped if "AnlageK" in path.name]
        if len(exhibits) != 2:
            raise AssertionError(f"Zwei Anlagen erwartet, erhalten: {exhibits}")
        for exhibit in exhibits:
            if len(exhibit.name) > 60 or not exhibit.name.isascii():
                raise AssertionError(f"Dateinamensprofil verletzt: {exhibit.name}")
            reader = PdfReader(str(exhibit))
            if len(reader.pages) != 2:
                raise AssertionError(f"Seitenzahl verändert: {exhibit}")
            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                if "Anlage K" not in text:
                    raise AssertionError(
                        f"Anlagenstempel fehlt in {exhibit.name}, Seite {page_number}"
                    )

        manifest_path = target / "intern" / "Versandmanifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest["metadaten"]["dateien"] != 3:
            raise AssertionError("Manifest enthält eine falsche Dateizahl")
        if any(entry["befunde"] for entry in manifest["anlagen"]):
            raise AssertionError("Fehlerfreier Testlauf enthält unerwartete Befunde")

        preflight = (target / "intern" / "Preflight-Bericht.md").read_text(
            encoding="utf-8"
        )
        if "| STOP |" in preflight or "| WARNUNG |" in preflight:
            raise AssertionError("Preflight enthält unerwartete Stop- oder Warnbefunde")

    print(
        "test-bea-versandmappe OK (47 ModeFuchs-Arbeitsdateien, 28 Original-Hashes; "
        "3 Versanddateien, 4 gestempelte Anlagenseiten)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

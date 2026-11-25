#!/usr/bin/env python3
"""Baut Copilot-Verhandlungsakte, ausfüllbare Arbeitsvorlagen und Plugin-Paket."""
import argparse
import csv
import io
import json
from importlib import import_module
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from akteneingang.ausgabe import archive
from akteneingang.quellen import safe_member
from package_readme import render_readme
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_grundakte import check_intake_member

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "betriebsvereinbarungen"
CASE = "betriebsvereinbarung-copilot-maschinenbau-kassel"
RELEASE = "betriebsvereinbarungen-v1.0.0"
DOWNLOADS = ROOT / "docs/downloads"
PHASES = ("Grundakte", "Nachreichungen")
DOCUMENTS = import_module("build-interstate-testakten")
FORMS = import_module("build-insolvenz-arbeitsvorlagen")


def read_data(stem):
    return json.loads((ROOT / "scripts/data" / (stem + ".json")).read_bytes())


def render_forms():
    forms = {}
    for spec in read_data("betriebsvereinbarungen-arbeitsvorlagen"):
        name = FORMS.filename(spec)
        if name in forms:
            raise ValueError("Doppelte Vorlage: " + name)
        renderer = FORMS.spreadsheet if spec.get("format") == "xlsx" else FORMS.word_document
        forms[name] = renderer(spec)
    return forms


def report_csv(doc):
    """Schreibt je Datenzeile einen Satz mit einzeiligem Herkunftsvermerk."""
    table = doc["tabelle"]
    output = io.StringIO(newline="")
    writer = csv.writer(output, delimiter=";", lineterminator="\r\n")
    writer.writerow([*table[0], "Exportvermerk"])
    provenance = " · ".join(" ".join(text.splitlines()) for text in DOCUMENTS.body(doc))
    for index, row in enumerate(table[1:]):
        cells = [" ".join(value.splitlines()) if isinstance(value, str) else value for value in row]
        writer.writerow([*cells, provenance if index == 0 else ""])
    return output.getvalue().encode("utf-8-sig")


def render_case():
    case = read_data(CASE)
    native, printed = {}, {}
    writer = PdfWriter()
    parents = {}
    for doc in case["dokumente"]:
        phase, name = doc["phase"], safe_member(doc["datei"])
        member = f"{phase}/{name}"
        pdf_member = str(Path(member).with_suffix(".pdf"))
        if phase not in PHASES or "/" in name or member in native or pdf_member in printed:
            raise ValueError("Ungültiger Aktenpfad: " + member)
        native[member] = report_csv(doc) if name.endswith(".csv") else DOCUMENTS.native(doc, case, name, None)
        if phase == "Grundakte":
            check_intake_member(name, native[member])
        printed[pdf_member] = DOCUMENTS.reading(doc, case, name, None)
        page = len(writer.pages)
        writer.append(PdfReader(io.BytesIO(printed[pdf_member])), import_outline=False)
        if phase not in parents:
            parents[phase] = writer.add_outline_item(title=phase, page_number=page)
        writer.add_outline_item(title=doc["titel"], page_number=page, parent=parents[phase])
    if set(parents) != set(PHASES):
        raise ValueError("Grundakte und Nachreichungen sind beide erforderlich.")
    writer.add_metadata({"/Title": case["titel"], "/Subject": case["zeichen"]})
    combined = io.BytesIO()
    writer.write(combined)
    writer.close()
    return native, printed, combined.getvalue()


def create_package():
    plugin = ROOT / PLUGIN
    files = {}
    for folder in (".claude-plugin", ".codex-plugin", "skills", "references", "vorlagen"):
        for path in sorted((plugin / folder).rglob("*")):
            if path.is_file():
                files[path.relative_to(plugin).as_posix()] = path.read_bytes()
    files["plugin.json"] = (plugin / "plugin.json").read_bytes()
    files["README.md"] = render_readme(ROOT, plugin, [*files, "README.md"], None, release_tag=RELEASE)
    return archive(dict(sorted(files.items())))


def save(path, data, check):
    if path.is_file() and path.read_bytes() == data:
        return
    if check:
        raise ValueError("Datei fehlt oder weicht von der Quelle ab: " + str(path.relative_to(ROOT)))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Ausgaben mit dem Quellbestand vergleichen")
    args = parser.parse_args()
    folder = ROOT / "testakten" / CASE
    forms = render_forms()
    native, printed, pdf = render_case()
    for member, data in forms.items():
        save(ROOT / PLUGIN / "vorlagen" / member, data, args.check)
        native["Arbeitsvorlagen/" + member] = data
    for member, data in native.items():
        save(folder / member, data, args.check)
    for subdir in (*PHASES, "Arbeitsvorlagen"):
        expected = {name for name in native if name.startswith(subdir + "/")}
        actual = {p.relative_to(folder).as_posix() for p in (folder / subdir).rglob("*") if p.is_file()}
        if expected != actual:
            raise ValueError(f"Der Dateibaum in {subdir} weicht vom erklärten Aktenbestand ab.")
    save(folder / "gesamt-pdf" / (CASE + "_gesamt.pdf"), pdf, args.check)
    notice = {NOTICE_FILENAME: NOTICE_BYTES}
    save(DOWNLOADS / f"testakte-{CASE}.zip", archive({**notice, **native}), args.check)
    save(DOWNLOADS / f"testakte-{CASE}-einzelpdfs.zip", archive({**notice, **printed}), args.check)
    save(DOWNLOADS / (PLUGIN + ".zip"), create_package(), args.check)
    print(f"{len(printed)} Aktenstücke, {len(forms)} Arbeitsvorlagen und drei ZIP-Ausgaben geprüft.")


if __name__ == "__main__":
    main()

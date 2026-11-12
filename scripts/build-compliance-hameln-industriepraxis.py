#!/usr/bin/env python3
"""Baut ergänzende Industriebelege, Grundakten und das Hamelner Praxispaket."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from hashlib import sha256
from html import escape
import importlib.util
from io import BytesIO
import json
import mimetypes
from pathlib import Path
import re
from shutil import copyfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_grundakte import FOLDER, check_intake_member, selection
from testakte_zip_common import safe_archive_name, working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/compliance-hameln-industriepraxis.json"
INTAKE = DATA.with_name("testakten-grundakten-hameln.json")
TEMPLATES = ROOT / "quality/hameln-compliance/vorlagen"
TAG = "compliance-hameln-praxis-v1.1.0"
BUNDLE = "Hameln_Compliance_41_Praxisakten.zip"
K17 = "compliance-hameln-schokolade-charge-k17"
ENTRY = "00_Einstieg.pdf"
REGISTER_NACHLAUF = {
    "freigabe-personalassistent", "interview-und-transkript", "meldefrist-firmware",
    "meldung-nachtschicht", "offenes-fenster-fuer-stuecklisten", "personalscore-vor-start",
    "retrofit-beratung", "schriftsatz-version", "treffer-im-lieferantencheck",
    "vertriebspartner-marktstart", "wartungsvertrag-doppelbuchung", "wartungsvertrag-redline",
    "wirksamkeit-nachtest", "zweite-rechnung",
}


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def material():
    return json.loads(DATA.read_text(encoding="utf-8"))


def digest(data):
    return sha256(data).hexdigest()


def native_name(slug):
    return f"testakte-{slug}.zip"


def singles_name(slug):
    return f"testakte-{slug}-einzelpdfs.zip"


def combined_name(slug):
    return f"{slug}_gesamt.pdf"


def csv_document(path, doc):
    with path.open("w", newline="", encoding="utf-8") as output:
        csv.writer(output, lineterminator="\n").writerows([doc["columns"], *doc["rows"]])


def workbook(path, doc):
    book = Workbook()
    sheet = book.active
    sheet.title = "Buchungen" if "abruf" in path.name.lower() else "Register"
    sheet.append(doc["columns"])
    for row in doc["rows"]:
        sheet.append(row)
    for index, label in enumerate(doc["columns"], 1):
        data = [row[index - 1] for row in doc["rows"]]
        if label in {"Quote Förderung", "Davon EU"}:
            for cells in sheet.iter_rows(min_row=2, min_col=index, max_col=index):
                cells[0].number_format = "0%"
        elif "EUR" in label:
            for cells in sheet.iter_rows(min_row=2, min_col=index, max_col=index):
                cells[0].number_format = '#,##0.00'
        width = max(len(str(value)) for value in [label, *data])
        sheet.column_dimensions[get_column_letter(index)].width = max(13, min(35, width + 3))
    for row in sheet:
        sheet.row_dimensions[row[0].row].height = 30
        for cell in row:
            header = cell.row == 1
            cell.font = Font(name="Calibri", size=11, color="FFFFFF" if header else "162940", bold=header)
            cell.fill = PatternFill("solid", fgColor="204363" if header else
                                    ("EEF4F8" if cell.row % 2 == 0 else "FFFFFF"))
            cell.alignment = Alignment(vertical="center", wrap_text=True)
    sheet.freeze_panes = "B2"
    sheet.auto_filter.ref = sheet.dimensions
    sheet.sheet_view.showGridLines = False
    sheet.print_options.horizontalCentered = True
    sheet.print_title_rows = "1:1"
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.page_setup.fitToWidth = sheet.page_setup.fitToHeight = 1
    book.properties.creator = "Merrensteg Elektrosysteme SE"
    book.properties.title = doc["title"]
    # Save the same typed data and metadata on repeated builds.
    book.save(path)
    with ZipFile(path) as source:
        contents = {name: source.read(name) for name in source.namelist()}
    core = contents["docProps/core.xml"]
    contents["docProps/core.xml"] = re.sub(
        rb"(?<=\>)[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:]+Z(?=\<)",
        b"2026-11-11T10:00:00Z", core,
    )
    with ZipFile(path, "w") as target:
        for name, data in contents.items():
            target.writestr(ZipInfo(name, (2026, 11, 11, 10, 0, 0)), data, compress_type=ZIP_DEFLATED)


def word_document(path, case, doc, style, *, template=False):
    page = style.setup(case, template=template)
    page.add_paragraph(doc["title"], style="Title")
    page.add_paragraph(doc["office"], style="Subtitle")
    if template:
        for index, (heading, body) in enumerate(doc["body"], 1):
            style.heading(page, index, heading)
            style.addpara(page, body)
    else:
        for body in doc["body"]:
            style.addpara(page, body)
    page.core_properties.title = doc["title"]
    style.save(page, path)


class FixedCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "invariant": 1})


def pdf_document(path, case, doc):
    dark = HexColor("#183650")
    body = ParagraphStyle("Belegtext", fontName="Times-Roman", fontSize=11, leading=16,
                          spaceAfter=13, textColor=dark)
    title = ParagraphStyle("Belegtitel", parent=body, fontName="Times-Bold", fontSize=23,
                           leading=27, spaceAfter=18)
    office = ParagraphStyle("Belegkopf", parent=body, fontName="Helvetica", fontSize=9,
                            textColor=HexColor("#245C63"), spaceAfter=11)

    def frame(canvas, _document):
        width, height = A4
        canvas.setStrokeColor(HexColor("#245C63"))
        canvas.line(23 * mm, height - 25 * mm, width - 23 * mm, height - 25 * mm)
        canvas.setFillColor(dark)
        canvas.setFont("Helvetica", 9)
        canvas.drawString(23 * mm, 19 * mm, f"{case['nr']}  ·  {path.stem.split('_', 1)[0]}")
        canvas.drawRightString(width - 23 * mm, 19 * mm, f"Seite {canvas.getPageNumber()}")

    story = [Paragraph(escape(doc["office"]), office), Paragraph(escape(doc["title"]), title)]
    story += [Paragraph(escape(paragraph), body) for paragraph in doc["body"]]
    SimpleDocTemplate(str(path), pagesize=A4, title=doc["title"], leftMargin=23 * mm,
                      rightMargin=23 * mm, topMargin=34 * mm, bottomMargin=26 * mm).build(
                          story, onFirstPage=frame, onLaterPages=frame, canvasmaker=FixedCanvas)


def write_mail(path, case, doc):
    message = EmailMessage(policy=policy.SMTP)
    message["From"] = doc["sender"]
    message["To"] = doc["recipient"]
    message["Subject"] = f"{case['nr']} | {doc['title']}"
    message["Date"] = datetime.fromisoformat(doc["date"])
    message["Message-ID"] = f"<{case['nr'].lower()}.{path.stem.split('_', 1)[0]}.industrie@merrensteg.example>"
    message.set_content("\n\n".join(doc["body"]), charset="utf-8", cte="quoted-printable")
    for name in doc["attachments"]:
        typ = mimetypes.guess_type(name)[0] or "application/octet-stream"
        message.add_attachment((path.parent / name).read_bytes(), *typ.split("/", 1), filename=name)
    if doc["attachments"]:
        message.set_boundary(f"merrensteg-{case['nr'].lower()}-{path.stem.split('_', 1)[0]}")
    path.write_bytes(message.as_bytes())


def sources():
    style = module("build-compliance-hameln-vertiefung")
    for slug, case in material().items():
        directory = ROOT / "testakten" / slug
        directory.mkdir(exist_ok=True)
        for doc in case["documents"]:
            path = directory / doc["file"]
            if path.suffix == ".docx":
                word_document(path, case, doc, style)
            elif path.suffix == ".pdf":
                pdf_document(path, case, doc)
            elif path.suffix == ".eml":
                write_mail(path, case, doc)
            elif path.suffix == ".csv":
                csv_document(path, doc)
            elif path.suffix == ".xlsx":
                workbook(path, doc)
            else:
                raise ValueError(f"Unbekanntes Industriebelegformat {path.suffix}")
        if "template" in case:
            word_document(TEMPLATES / f"{slug}.docx", case, case["template"], style, template=True)
    prior = module("build-compliance-hameln-praxis")
    base = [case["slug"] for case in prior.cases() if case["slug"] != K17]
    intake = {}
    for slug in base:
        directory = ROOT / "testakten" / slug
        names = {path.name for path in directory.iterdir() if path.is_file()}
        if "01_Eingang.eml" in names:
            initial = {"01_Eingang.eml", "02_Sachgrundlage.docx"}
            if slug.removeprefix("compliance-hameln-") not in REGISTER_NACHLAUF:
                initial |= {"04_Datenregister.xlsx", "04a_Rohdaten.csv", "05_Registerauszug.png"}
        else:
            last = {"auskunft-mit-schwaerzungen": 3, "geschenk-geschaeftsfuehrung": 6,
                    "sicherheitsrelais-hinweis": 6}[slug.removeprefix("compliance-hameln-")]
            initial = {name for name in names if name[:2].isdigit() and 1 <= int(name[:2]) <= last}
        intake[slug] = initial
    for slug, case in material().items():
        intake.setdefault(slug, set()).update(doc["file"] for doc in case["documents"] if doc["ground"])
    INTAKE.write_text(json.dumps({slug: sorted(members) for slug, members in sorted(intake.items())},
                                 ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def checksummed(directory, name, inventory):
    data = (directory / name).read_bytes()
    if digest(data) != inventory["assets"][name]:
        raise ValueError(f"Datei weicht vom veröffentlichten Inventar ab: {name}")
    return data


def refresh_pdfs(case, dist, basis, basis_report, k17, k17_report, old):
    slug = case["slug"]
    combined = combined_name(slug)
    single = singles_name(slug)
    directory = ROOT / "testakten" / slug
    if slug == K17 or slug not in material():
        source, inventory = (k17, k17_report) if slug == K17 else (basis, basis_report)
        for name in (combined, single):
            (dist / name).write_bytes(checksummed(source, name, inventory))
        if (directory / "gesamt-pdf" / combined).read_bytes() != (dist / combined).read_bytes():
            raise ValueError(f"Gesamt-PDF des Basisstands weicht ab: {slug}")
        return
    singles = module("build-testakten-einzelpdf-zips")
    pairs = document_arcname_pairs(directory)
    previous = {}
    if old is not None:
        with ZipFile(BytesIO(checksummed(basis, single, basis_report))) as archive:
            previous = {name: archive.read(name) for name in archive.namelist()}
    writer = PdfWriter()
    writer.add_metadata({"/Title": case["title"], "/Author": "Merrensteg Elektrosysteme SE",
                         "/Subject": "Compliance-Arbeitsakte " + case["nr"]})
    with ZipFile(dist / single, "x") as archive:
        singles.write_pdf(archive, NOTICE_FILENAME, NOTICE_BYTES)
        for source, name in pairs:
            data = previous.get(name) if old and old["source_sha256"].get(source.name) == digest(source.read_bytes()) else None
            if data is None:
                data = singles.render_document_pdf(source, directory)
            if not data or pdf_content_errors(data):
                raise ValueError(f"Unbrauchbare PDF-Lesefassung: {slug}/{name}")
            singles.write_pdf(archive, name, data)
            first = len(writer.pages)
            for page in PdfReader(BytesIO(data)).pages:
                writer.add_page(page)
            writer.add_outline_item(source.name, first)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    local = directory / "gesamt-pdf" / combined
    local.parent.mkdir(exist_ok=True)
    with local.open("wb") as output:
        writer.write(output)
    copyfile(local, dist / combined)


def case_archive(dist, slug):
    return dist / native_name(slug)


def inspect_case(dist, slug):
    directory = ROOT / "testakten" / slug
    pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
    record = {}
    added = {entry["file"] for entry in material().get(slug, {}).get("documents", [])}
    with ZipFile(case_archive(dist, slug)) as archive:
        verify_notice(archive, directories=True)
        names = set(archive.namelist())
        if names != {NOTICE_FILENAME, *(name for _, name in pairs)}:
            raise ValueError(f"Abweichender Originalbestand: {slug}")
        sources_by_name = {source.name: source for source, _ in pairs}
        for path, name in pairs:
            data = archive.read(name)
            if path.read_bytes() != data:
                raise ValueError(f"Verändertes Original: {slug}/{name}")
            if name.startswith(FOLDER + "/"):
                check_intake_member(name, data)
            if path.name in added and path.suffix == ".eml":
                msg = BytesParser(policy=policy.default).parsebytes(data)
                if not all(msg[field] for field in ("From", "To", "Date", "Subject", "Message-ID")) or msg.defects:
                    raise ValueError(f"Unvollständiger Mailkopf: {name}")
                for attachment in msg.iter_attachments():
                    if attachment.get_payload(decode=True) != sources_by_name[attachment.get_filename()].read_bytes():
                        raise ValueError(f"Veränderte Mailanlage: {name}")
        if not added <= sources_by_name.keys():
            raise ValueError(f"Industriebelege fehlen im Originalarchiv: {slug}")
        record["grundakte"] = sum(name.startswith(FOLDER + "/") for name in names)
        if not record["grundakte"] or (slug != K17 and record["grundakte"] != len(selection()["central"][slug])):
            raise ValueError(f"Eingangsunterlagen fehlen: {slug}")
        record["documents"] = len(pairs)
        record["original_sha256"] = digest(case_archive(dist, slug).read_bytes())
    combined = PdfReader(dist / combined_name(slug))
    if pdf_content_errors((dist / combined_name(slug)).read_bytes()):
        raise ValueError(f"Unzulässiger PDF-Hinweis: {slug}")
    record["pages"] = len(combined.pages)
    pdf_pairs = (module("build-compliance-hameln-k17-release").ordered_pdfs()
                 if slug == K17 else document_arcname_pairs(directory))
    with ZipFile(dist / singles_name(slug)) as archive:
        verify_notice(archive, directories=slug == K17)
        if set(archive.namelist()) != {NOTICE_FILENAME, *(name for _, name in pdf_pairs)}:
            raise ValueError(f"Abweichender Einzel-PDF-Bestand: {slug}")
        page = 0
        marks = []
        for source, name in pdf_pairs:
            data = archive.read(name)
            if pdf_content_errors(data):
                raise ValueError(f"Unzulässiger PDF-Hinweis: {slug}/{name}")
            marks.append((source.name, page))
            page += len(PdfReader(BytesIO(data)).pages)
        outline = combined.outline
        if slug == K17:
            outline = [mark for chapter in outline if isinstance(chapter, list) for mark in chapter]
        if marks != [(mark.title, combined.get_destination_page_number(mark)) for mark in outline] or page != record["pages"]:
            raise ValueError(f"Abweichende Lesefassung: {slug}")
    return record


def verify_notice(archive, *, directories=False):
    names = archive.namelist()
    if (not names or names[0] != NOTICE_FILENAME or notice_text_errors(archive.read(NOTICE_FILENAME))
            or any(not safe_archive_name(name, allow_directories=directories) for name in names)
            or len({name.casefold() for name in names}) != len(names) or archive.testzip()):
        raise ValueError(f"Ungültiges Archiv: {archive.filename}")


def verify(dist):
    report = json.loads((dist / "release-bestand.json").read_text(encoding="utf-8"))
    checks = dict(line.split("  ", 1)[::-1] for line in (dist / "checksums-sha256.txt").read_text().splitlines())
    if (report["tag"] != TAG or len(report["cases"]) != 41
            or set(checks) != {p.name for p in dist.iterdir()} - {"checksums-sha256.txt"}
            or report["assets"] != {name: sha for name, sha in checks.items() if name != "release-bestand.json"}):
        raise ValueError("Release und Inventar stimmen nicht überein.")
    for name, sha in checks.items():
        if digest((dist / name).read_bytes()) != sha:
            raise ValueError(f"Abweichende Prüfsumme: {name}")
    with ZipFile(dist / BUNDLE) as bundle:
        verify_notice(bundle)
        for slug, entry in report["cases"].items():
            if inspect_case(dist, slug) != entry:
                raise ValueError(f"Abweichendes Akteninventar: {slug}")
            if digest(bundle.read(native_name(slug))) != entry["original_sha256"]:
                raise ValueError(f"Abweichender Aktenbestand im Sammel-ZIP: {slug}")
            template = template_path(slug)
            if template and bundle.read(template.name) != template.read_bytes():
                raise ValueError(f"Abweichende Word-Vorlage: {slug}")
    print(f"{TAG}: {len(report['cases'])} Fälle, "
          f"{sum(entry['grundakte'] for entry in report['cases'].values())} Eingangsunterlagen, "
          f"{len(checks) + 1} Release-Dateien.")


def template_path(slug):
    name = f"{slug}.docx"
    for folder in (TEMPLATES, ROOT / "compliance-abteilung-grosskonzern/templates"):
        path = folder / name
        if path.is_file():
            return path
    return None


def build(dist, basis, k17):
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Leeres Ausgabeziel erforderlich.")
    prior = module("build-compliance-hameln-praxis")
    basis_report = json.loads((basis / "release-bestand.json").read_text())
    k17_report = json.loads((k17 / "release-bestand.json").read_text())
    if basis_report["tag"] != prior.TAG or k17_report["tag"] != "compliance-hameln-k17-v1.1.0":
        raise ValueError("Falscher Basisstand für die PDF-Lesefassungen.")
    prior_by_slug = {case["slug"]: case for case in basis_report["cases"]}
    all_cases = prior.cases() + [
        {**case, "slug": slug} for slug, case in material().items() if slug not in prior_by_slug
    ]
    native = module("build-testakten-release-zips")
    for case in all_cases:
        slug = case["slug"]
        if slug != K17 and slug in prior_by_slug:
            directory = ROOT / "testakten" / slug
            for name, sha in prior_by_slug[slug]["source_sha256"].items():
                if digest((directory / name).read_bytes()) != sha:
                    raise ValueError(f"Historisches Original verändert: {slug}/{name}")
        refresh_pdfs(case, dist, basis, basis_report, k17, k17_report, prior_by_slug.get(slug))
        if slug == K17:
            case_archive(dist, slug).write_bytes(checksummed(k17, native_name(slug), k17_report))
        else:
            native.build_single(ROOT / "testakten" / slug, dist)
    records = {}
    with ZipFile(dist / BUNDLE, "x") as bundle:
        native.write_bytes(bundle, NOTICE_BYTES, NOTICE_FILENAME)
        for case in all_cases:
            slug = case["slug"]
            records[slug] = inspect_case(dist, slug)
            archive = case_archive(dist, slug)
            native.write_file(bundle, archive, archive.name)
            template = template_path(slug)
            if template:
                native.write_file(bundle, template, template.name)
    assets = {path.name: digest(path.read_bytes()) for path in sorted(dist.iterdir())}
    inventory = dist / "release-bestand.json"
    inventory.write_text(json.dumps({"tag": TAG, "cases": records, "assets": assets}, ensure_ascii=False,
                                    indent=2) + "\n", encoding="utf-8")
    assets[inventory.name] = digest(inventory.read_bytes())
    (dist / "checksums-sha256.txt").write_text(
        "".join(f"{sha}  {name}\n" for name, sha in sorted(assets.items())), encoding="utf-8"
    )
    verify(dist)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", action="store_true")
    parser.add_argument("--dist", type=Path)
    parser.add_argument("--basis", type=Path)
    parser.add_argument("--k17", type=Path)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.sources:
        sources()
    elif args.dist and args.verify:
        verify(args.dist.resolve())
    elif args.dist and args.basis and args.k17:
        build(args.dist.resolve(), args.basis.resolve(), args.k17.resolve())
    else:
        parser.error("Verwende --sources, --dist mit --verify oder --dist mit --basis und --k17.")

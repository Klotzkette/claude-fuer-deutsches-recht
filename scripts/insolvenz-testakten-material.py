#!/usr/bin/env python3
"""Baut und prüft gesonderte Vorlagen und Vergleichsunterlagen zu Insolvenztestakten."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from io import BytesIO
import json
from pathlib import Path
import re
import shutil
from tempfile import TemporaryDirectory
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from testakte_disclaimer import NOTICE_MARKDOWN, pdf_content_errors
from testakte_file_filter import INSOLVENZ_PRUEFMATERIAL, include_in_working_dump

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "testakten"
QUALITY = ROOT / "quality/insolvenz-testakten"
TEMPLATES = ROOT / "docs/experimentell/vorlagensammlung-recht"
BLANKS = {
    "insolvenzplan": TEMPLATES / "insolvenzrecht/insolvenzplan-darstellender-und-gestaltender-teil"
    / "insolvenzplan-darstellender-und-gestaltender-teil.odt",
    "restrukturierungsplan": TEMPLATES / "restrukturierungsrecht-starug/restrukturierungsplan-starug"
    / "restrukturierungsplan-starug.odt",
}
CLAIM_BASIS = TEMPLATES / "insolvenzrecht/klage-insolvenzanfechtung/klage-insolvenzanfechtung.md"
CLAIM_SOURCE = QUALITY / "klagevorlage.md"
CLAIM_TEMPLATE = "Insolvenzanfechtungsklage-Vorlage.docx"
OPINION = "Internes-Insolvenzanfechtungsgutachten.pdf"
BEGIN = "<!-- BEGIN pruefmaterial-insolvenz -->"
END = "<!-- END pruefmaterial-insolvenz -->"
EXTRA_CHALLENGES = {
    "fintech-darlehen-vertragsuebernahme-bremen",
    "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren",
    "insolvenzverwaltung-nordlicht-handels-kiel",
    "insolvenzverwaltung-mainbogen-laborsoftware-wuerzburg",
    "insolvenzrecht-forderungspruefung-mietkaution-berlin",
    "starug-schutzschirm-grossbach-druckguss-erfurt",
    "bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn",
    "insolvenzplan-starug-planwerkstatt-metallbau-hansa",
}


REQUIRED_PLANS = {
    "insolvenzplan-starug-planwerkstatt-metallbau-hansa": {"insolvenzplan", "restrukturierungsplan"},
    "insolvenzrecht-eigenverwaltung-schutzschirm-medtech-jena": {"insolvenzplan"},
    "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren": {"insolvenzplan"},
    "sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026": {"insolvenzplan"},
    "sanierungsgewinn-starug-plan-windenergie-pellbach-2026": {"restrukturierungsplan"},
    "starug-aufhebung-holding-duesseldorf-ix-zb-18-25": {"restrukturierungsplan"},
    "starug-schutzschirm-grossbach-druckguss-erfurt": {"restrukturierungsplan"},
    "krisenfrueherkennung-starug-vier-varianten": {"restrukturierungsplan"},
}


def load_script(filename):
    spec = importlib.util.spec_from_file_location(filename.removesuffix(".py"), ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_material():
    opinions = {path.stem: path for path in (QUALITY / "gutachten").glob("*.md")}
    required = EXTRA_CHALLENGES | {path.name for path in CASES.glob("insolvenzanfechtung-*") if path.is_dir()}
    if required - opinions.keys():
        raise ValueError(f"Gutachten fehlen für: {', '.join(sorted(required - opinions.keys()))}")

    plans = QUALITY / "plaene"
    plan_files = {}
    for path in sorted(plans.glob("*/*.md")):
        case = path.parent.name
        kind = path.stem.split("-", 1)[0]
        if kind not in BLANKS:
            raise ValueError(f"Unbekannte Planart: {path}")
        plan_files.setdefault(case, {})[path.stem + ".docx"] = path

    for case, kinds in REQUIRED_PLANS.items():
        actual = {name.split("-", 1)[0] for name in plan_files.get(case, {})}
        if case == "krisenfrueherkennung-starug-vier-varianten" and len(plan_files.get(case, {})) != 3:
            raise ValueError(f"Drei getrennte Planvarianten erforderlich: {case}")
        if kinds - actual:
            raise ValueError(f"Planentwurf fehlt: {case}: {', '.join(sorted(kinds - actual))}")
    material = {}
    for case in sorted(opinions.keys() | plan_files.keys()):
        if not (CASES / case / "README.md").is_file():
            raise ValueError(f"Unbekannte Testakte: {case}")
        entries = {}
        if case in opinions:
            entries.update({CLAIM_TEMPLATE: CLAIM_SOURCE, OPINION: opinions[case]})
        for filename, source in plan_files.get(case, {}).items():
            kind = source.stem.split("-", 1)[0]
            entries[kind + "-blanko.odt"] = BLANKS[kind]
            entries[filename] = source
        material[case] = entries
    return material


def evidence_snapshot(case):
    """Fingerabdruck der nativen Fallunterlagen und nicht ihrer Lesefassungen."""
    records = []
    for path in sorted(case.rglob("*")):
        rel = path.relative_to(case)
        if (not path.is_file() or INSOLVENZ_PRUEFMATERIAL in rel.parts
                or "gesamt-pdf" in rel.parts or any(part.startswith(".") for part in rel.parts)
                or path.name in {"README.md", "rubric.yaml"}):
            continue
        records.append([rel.as_posix(), digest(path)])
    encoded = json.dumps(records, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return {"dateien": len(records), "sha256": hashlib.sha256(encoded).hexdigest()}


def create_docx(converter, source, target):
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    converter.md_to_docx(source, target)
    document = Document(target)
    document.paragraphs[0].style = document.styles["Title"]
    for name in ("Title", "Normal", "Heading 1", "Heading 2", "Heading 3"):
        style = document.styles[name]
        style.font.name = "Times New Roman"
        style.font.color.rgb = RGBColor(0, 0, 0)
    title = document.styles["Title"]
    title.font.size = Pt(19)
    for border in title.element.xpath(".//w:pBdr"):
        border.getparent().remove(border)
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        document.styles[name].paragraph_format.space_after = Pt(5)
    document.styles["Normal"].paragraph_format.space_after = Pt(6)
    document.styles["Normal"].paragraph_format.line_spacing = 1.13
    for paragraph in document.paragraphs:
        previous = paragraph._p.getprevious()
        if previous is not None and previous.tag == qn("w:tbl"):
            paragraph.paragraph_format.space_before = Pt(6)
    for table in document.tables:
        if len(table.columns) == 7:
            table.autofit = False
            for index, column in enumerate(table.columns):
                column.width = Cm(4.48 if index == 0 else 1.92)
                for cell in column.cells:
                    cell.width = column.width
        properties = table._tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            border = OxmlElement(f"w:{edge}")
            for attr, value in (("val", "single"), ("sz", "4"), ("color", "D9D9D9")):
                border.set(qn(f"w:{attr}"), value)
            borders.append(border)
        properties.append(borders)
        margins = OxmlElement("w:tblCellMar")
        for edge in ("top", "bottom", "left", "right"):
            margin = OxmlElement(f"w:{edge}")
            margin.set(qn("w:w"), "90")
            margin.set(qn("w:type"), "dxa")
            margins.append(margin)
        properties.append(margins)
        table.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
        for cell in table.rows[0].cells:
            shade = OxmlElement("w:shd")
            shade.set(qn("w:fill"), "E8EDF1")
            cell._tc.get_or_add_tcPr().append(shade)
        for row in table.rows:
            row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    document.core_properties.title = document.paragraphs[0].text
    document.core_properties.author = "Klotzkette"
    stream = BytesIO()
    document.save(stream)
    with ZipFile(stream) as original, ZipFile(target, "w") as archive:
        for name in original.namelist():
            info = ZipInfo(name)
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, original.read(name))


def create_pdf(renderer, release, source, target):
    from reportlab.lib.pagesizes import A4
    from pypdf import PdfReader
    from reportlab.platypus import Paragraph, SimpleDocTemplate

    release.register_fonts()
    renderer.FONT_REG, renderer.FONT_BOLD = release.FONT_REG, release.FONT_BOLD
    renderer.s_body.fontName = release.FONT_REG
    renderer.s_body.fontSize, renderer.s_body.leading = 11, 14
    renderer.s_body.spaceAfter = 5
    for style in (renderer.s_h1, renderer.s_h2, renderer.s_h3):
        style.fontName, style.keepWithNext = release.FONT_BOLD, True
    original = source.read_text(encoding="utf-8")
    link_pattern = re.compile(r"\[([^]\n]+)\]\((https?://[^)\s]+)\)")
    links = {}

    def link_token(match):
        token = f"QUELLENLINK{len(links):04d}ENDE"
        links[token] = match.groups()
        return token

    markdown = link_pattern.sub(link_token, original)
    flowables = renderer.md_to_flowables(markdown)
    for index, flowable in enumerate(flowables):
        if isinstance(flowable, Paragraph) and "QUELLENLINK" in flowable.text:
            markup = flowable.text
            for token, (label, url) in links.items():
                href = escape(url, {'"': '&quot;'})
                markup = markup.replace(token, f'<link href="{href}">{escape(label)}</link>')
            flowables[index] = Paragraph(markup, flowable.style)
    document = SimpleDocTemplate(str(target), pagesize=A4, title=markdown.splitlines()[0][2:],
                                 author="Klotzkette", invariant=1, leftMargin=60, rightMargin=60,
                                 topMargin=49, bottomMargin=46)

    def footer(canvas, doc):
        canvas.setFont(release.FONT_REG, 8)
        canvas.drawString(60, 29, "Interne Fallprüfung")
        canvas.drawRightString(A4[0] - 60, 29, str(doc.page))

    document.build(flowables, onFirstPage=footer, onLaterPages=footer)
    uris = set()
    for page in PdfReader(target).pages:
        for reference in page.get("/Annots", []):
            action = reference.get_object().get("/A", {})
            if action.get("/URI"):
                uris.add(str(action["/URI"]))
    if uris != {url for _, url in links.values()}:
        raise ValueError(f"Quellenlinks im PDF weichen von der Vorlage ab: {source.name}")
    with TemporaryDirectory(prefix="gutachten-textkontrolle-") as temp:
        expected = Path(temp) / source.name
        expected.write_text(link_pattern.sub(r"\1", original), encoding="utf-8")
        release.inspect_pdf(expected, target)


def download_block(entries):
    labels = {CLAIM_TEMPLATE: "Klagevorlage (Word)", OPINION: "Internes Gutachten (PDF)",
              "insolvenzplan-blanko.odt": "Insolvenzplan (Blanko, ODT)",
              "restrukturierungsplan-blanko.odt": "StaRUG-Restrukturierungsplan (Blanko, ODT)"}
    lines = [BEGIN, "## Vorlagen und Vergleichsmaterial", "",
             "Für einen eigenständigen Testlauf verwenden Sie die Arbeitsakte und die Blankovorlagen. "
             "Ziehen Sie das Gutachten oder den fallbezogenen Plan erst beim Vergleich der Ergebnisse heran. "
             "Die Dateien in dieser Tabelle sind separat von den Aktenarchiven verfügbar.", "",
             NOTICE_MARKDOWN, "", "| Unterlage | Datei |", "| --- | --- |"]
    for name, source in entries.items():
        label = labels.get(name, source.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
                           if source.suffix == ".md" else name)
        lines.append(f"| {label.replace('|', '–')} | [Datei öffnen]({INSOLVENZ_PRUEFMATERIAL}/{name}) |")
    return "\n".join(lines + ["", END])


def update_readme(case, entries):
    path = case / "README.md"
    body = path.read_text(encoding="utf-8")
    block = download_block(entries)
    if BEGIN in body:
        body = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block, body, count=1, flags=re.S)
    else:
        body = body.rstrip() + "\n\n" + block + "\n"
    path.write_text(body, encoding="utf-8")


def inspect_material(material):
    from docx import Document

    unexpected = {path.parent.name for path in CASES.glob(f"*/{INSOLVENZ_PRUEFMATERIAL}")} - material.keys()
    if unexpected:
        raise ValueError(f"Prüfmaterial ohne Quellzuordnung: {', '.join(sorted(unexpected))}")
    result = {}
    for slug, entries in material.items():
        case = CASES / slug
        directory = case / INSOLVENZ_PRUEFMATERIAL
        if not directory.is_dir() or set(entries) != {path.name for path in directory.iterdir()}:
            raise ValueError(f"Unvollständiger oder unerwarteter Materialbestand: {slug}")
        readme = (case / "README.md").read_text(encoding="utf-8")
        readme = re.sub(r"^<!-- decimal-anchor -->.*\n\n?", "", readme, flags=re.M)
        readme = re.sub(r"^## (?:\d+\.)+ Vorlagen und Vergleichsmaterial$", "## Vorlagen und Vergleichsmaterial",
                        readme, flags=re.M)
        if download_block(entries) not in readme:
            raise ValueError(f"Downloadverzeichnis fehlt oder ist veraltet: {slug}")
        outputs = {}
        for name, source in entries.items():
            target = directory / name
            if include_in_working_dump(target, case):
                raise ValueError(f"Vergleichsmaterial landet im Arbeitsakten-Export: {target}")
            if target.suffix == ".odt" and digest(source) != digest(target):
                raise ValueError(f"Blankovorlage weicht vom Original ab: {target}")
            if target.suffix == ".docx":
                document = Document(target)
                body = "\n".join(p.text for p in document.paragraphs)
                if len(body) < 1000 or document.styles["Normal"].font.size.pt != 11:
                    raise ValueError(f"Unvollständige Word-Datei: {target}")
                if name == CLAIM_TEMPLATE and body.count("[") < 10:
                    raise ValueError(f"Ausfüllfelder fehlen: {target}")
            if target.suffix == ".pdf":
                errors = pdf_content_errors(target.read_bytes())
                if errors:
                    raise ValueError(f"{target}: {errors}")
            outputs[name] = {"sha256": digest(target), "quelle": source.relative_to(ROOT).as_posix(),
                             "quellen_sha256": digest(source)}
            if name == CLAIM_TEMPLATE:
                outputs[name]["vorlagenbasis_sha256"] = digest(CLAIM_BASIS)
        result[slug] = {"aktenstand": evidence_snapshot(case), "material": outputs}
    return result


def build(material):
    converter = load_script("convert-testakte-aktenstuecke-nativ.py")
    renderer = load_script("build-testakte-gesamt-pdf.py")
    release = load_script("build-insolvenzanfechtung-release.py")
    with TemporaryDirectory(prefix="insolvenz-material-") as temp:
        staging = Path(temp)
        template = staging / CLAIM_TEMPLATE
        create_docx(converter, CLAIM_SOURCE, template)
        for slug, entries in material.items():
            directory = staging / slug
            directory.mkdir()
            for name, source in entries.items():
                target = directory / name
                if name == CLAIM_TEMPLATE:
                    shutil.copyfile(template, target)
                elif target.suffix == ".odt":
                    shutil.copyfile(source, target)
                elif target.suffix == ".pdf":
                    create_pdf(renderer, release, source, target)
                else:
                    create_docx(converter, source, target)
        for slug, entries in material.items():
            case = CASES / slug
            directory = case / INSOLVENZ_PRUEFMATERIAL
            directory.mkdir(exist_ok=True)
            for name in entries:
                shutil.copyfile(staging / slug / name, directory / name)
            update_readme(case, entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Geprüfte Materialquellen setzen und Bestand erfassen")
    args = parser.parse_args()
    material = expected_material()
    manifest = QUALITY / "bestand.json"
    if args.build:
        build(material)
    actual = inspect_material(material)
    if args.build:
        manifest.write_text(json.dumps(actual, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        expected = json.loads(manifest.read_text(encoding="utf-8"))
        stale = [key for key in sorted(expected.keys() | actual.keys()) if expected.get(key) != actual.get(key)]
        if stale:
            raise SystemExit("Akten-, Vorlagen- oder Materialstand geändert. Fachlich abgleichen: " + ", ".join(stale))
    print(f"{len(actual)} Akten, {sum(len(row['material']) for row in actual.values())} Dateien geprüft.")


if __name__ == "__main__":
    main()

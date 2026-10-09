#!/usr/bin/env python3
"""Baut die individuell verfasste Berliner Beteiligungsakte."""

import argparse
import csv
import importlib.util
import json
from pathlib import Path
from copy import deepcopy
import zipfile
from lxml import etree
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data"
CASE = json.loads(
    (DATA / "gesellschaftervereinbarung-akte.json").read_text(encoding="utf-8")
)
HISTORY = json.loads(
    (DATA / "gesellschaftervereinbarung-vorgeschichte.json").read_text(encoding="utf-8")
)
for group in ("contacts", "documents", "emails", "raw"):
    CASE[group].extend(HISTORY.get(group, []))
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def render_docx(template, source, target):
    with zipfile.ZipFile(template) as archive:
        parts = {p: archive.read(p) for p in archive.namelist()}
    root = etree.fromstring(parts["word/document.xml"])
    body = root.find("w:body", NS)
    section = deepcopy(body.find("w:sectPr", NS))
    for child in list(body):
        body.remove(child)
    for block in source.read_text(encoding="utf-8").split("\n\n"):
        block = block.strip()
        if not block:
            continue
        style = "Normal"
        for prefix, chosen in (
            ("#### ", "Heading3"),
            ("### ", "Heading2"),
            ("## ", "Heading1"),
            ("# ", "Title"),
        ):
            if block.startswith(prefix):
                block, style = block[len(prefix) :], chosen
                break
        p = etree.SubElement(body, f"{{{W}}}p")
        pr = etree.SubElement(p, f"{{{W}}}pPr")
        etree.SubElement(pr, f"{{{W}}}pStyle").set(f"{{{W}}}val", style)
        etree.SubElement(pr, f"{{{W}}}widowControl")
        if style != "Normal":
            etree.SubElement(pr, f"{{{W}}}keepNext")
        if style == "Heading2" and block == "32.3 Vollständige Abschlussfelder":
            etree.SubElement(pr, f"{{{W}}}pageBreakBefore")
        run = etree.SubElement(p, f"{{{W}}}r")
        etree.SubElement(run, f"{{{W}}}t").text = block
    body.append(section)
    parts["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    styles = etree.fromstring(parts["word/styles.xml"])
    for identifier, size in (
        ("Normal", 22),
        ("Title", 22),
        ("Heading1", 22),
        ("Heading2", 22),
        ("Heading3", 22),
        ("Header", 22),
        ("Footer", 22),
    ):
        matches = styles.xpath(f'./w:style[@w:styleId="{identifier}"]', namespaces=NS)
        if matches:
            s = matches[0]
        else:
            s = etree.SubElement(styles, f"{{{W}}}style")
            s.set(f"{{{W}}}type", "paragraph")
            s.set(f"{{{W}}}styleId", identifier)
            etree.SubElement(s, f"{{{W}}}name").set(f"{{{W}}}val", identifier)
        for element in list(s):
            if element.tag in (f"{{{W}}}pPr", f"{{{W}}}rPr"):
                s.remove(element)
        pp = etree.SubElement(s, f"{{{W}}}pPr")
        if identifier.startswith("Heading"):
            etree.SubElement(pp, f"{{{W}}}outlineLvl").set(f"{{{W}}}val", str(int(identifier[-1]) - 1))
        spacing = etree.SubElement(pp, f"{{{W}}}spacing")
        spacing.set(f"{{{W}}}after", "150")
        spacing.set(f"{{{W}}}line", "264")
        spacing.set(f"{{{W}}}lineRule", "auto")
        if identifier != "Normal":
            spacing.set(f"{{{W}}}before", "180")
            etree.SubElement(pp, f"{{{W}}}keepNext")
        rp = etree.SubElement(s, f"{{{W}}}rPr")
        fonts = etree.SubElement(rp, f"{{{W}}}rFonts")
        for attr in ("ascii", "hAnsi", "cs", "eastAsia"):
            fonts.set(f"{{{W}}}{attr}", "Times New Roman")
        etree.SubElement(rp, f"{{{W}}}sz").set(f"{{{W}}}val", str(size))
        etree.SubElement(rp, f"{{{W}}}color").set(f"{{{W}}}val", "000000")
        if identifier != "Normal":
            etree.SubElement(rp, f"{{{W}}}b")
    parts["word/styles.xml"] = etree.tostring(
        styles, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    for name in list(parts):
        if name.startswith(("word/header", "word/footer")) and name.endswith(".xml"):
            part = etree.fromstring(parts[name].replace(b" (geplant)", b""))
            for run in part.findall(".//w:r", NS):
                properties = run.find("w:rPr", NS)
                if properties is None:
                    properties = etree.Element(f"{{{W}}}rPr")
                    run.insert(0, properties)
                for tag in ("rFonts", "sz", "szCs"):
                    for old in properties.findall(f"w:{tag}", NS):
                        properties.remove(old)
                fonts = etree.SubElement(properties, f"{{{W}}}rFonts")
                for attr in ("ascii", "hAnsi", "cs", "eastAsia"):
                    fonts.set(f"{{{W}}}{attr}", "Times New Roman")
                for tag in ("sz", "szCs"):
                    etree.SubElement(properties, f"{{{W}}}{tag}").set(f"{{{W}}}val", "22")
            parts[name] = etree.tostring(part, xml_declaration=True, encoding="UTF-8", standalone=True)
    core = etree.fromstring(parts["docProps/core.xml"])
    for node in core:
        if etree.QName(node).localname in {"creator", "lastModifiedBy"}:
            node.text = "Klotzkette"
    parts["docProps/core.xml"] = etree.tostring(
        core, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in parts.items():
            info = zipfile.ZipInfo(name, (2026, 10, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content)


def build(template_dir):
    spec = importlib.util.spec_from_file_location(
        "native", ROOT / "scripts/build-geldwaeschebeauftragter-akten.py"
    )
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    regular, bold = native.font_paths()
    pdfmetrics.registerFont(TTFont("AkteSerif", str(regular)))
    pdfmetrics.registerFont(TTFont("AkteSerifBold", str(bold)))
    directory = ROOT / "testakten" / CASE["slug"]
    directory.mkdir(parents=True, exist_ok=True)
    for item in CASE["documents"]:
        target = directory / item["path"]
        if item.get("source"):
            template = template_dir / (
                "term-sheet.docx" if item["id"] == "S01" else "vertrag.docx"
            )
            render_docx(template, DATA / item["source"], target)
        else:
            native.create_pdf(target, item)
    for item in CASE["emails"]:
        native.create_eml(directory, CASE, item)
    for item in CASE["raw"]:
        target = directory / item["path"]
        if target.suffix == ".csv":
            if len({len(row) for row in item["rows"]}) != 1:
                raise ValueError("Uneinheitliche CSV-Spalten")
            with target.open("w", encoding="utf-8", newline="") as handle:
                csv.writer(handle, delimiter=";", lineterminator="\n").writerows(
                    item["rows"]
                )
        else:
            target.write_text(item["text"], encoding="utf-8")
    paths = [
        item["path"] for group in ("documents", "emails", "raw") for item in CASE[group]
    ]
    paths.append("22_Kapital_und_Finanzierungsplan.xlsx")
    table = "\n".join(f"| [{p}]({p}) | {Path(p).suffix[1:].upper()} |" for p in paths)
    slug = CASE["slug"]
    release = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gesellschaftervereinbarung-v1.1.0"
    counts = {ext: sum(Path(p).suffix == ext for p in paths) for ext in (".docx", ".pdf", ".eml", ".csv", ".txt", ".xlsx")}
    (directory / "README.md").write_text(
        f"""# Drohnenfriseur Berlin – Gesellschaftervereinbarung

<!-- reserved-example-contacts -->

## 1 Fall und Unterlagen

Die Berliner SkyFade Robotics GmbH verhandelt eine Finanzierung über zehn Millionen Euro. Zwei Gründer, ein Business Angel, vier Investoren und die Gesellschaft stimmen Kapital, Mitspracherechte, Technologie und einen späteren Verkauf ab. Die Korrespondenz enthält verschiedene Verhandlungspositionen. Es gibt keine Musterlösung.

Die Akte umfasst {len(paths)} Originaldateien: {counts['.docx']} bearbeitbare Word-Dokumente, {counts['.pdf']} PDF-Unterlagen, {counts['.eml']} E-Mails mit echten Dateianhängen, {counts['.csv']} CSV-Dateien, {counts['.txt']} Textdateien und eine Excel-Arbeitsmappe. Die Vorgeschichte reicht von der Vorgründungsabrede über die UG, Softwareüberlassungen und Kapitalerhöhungen bis zur Frühfinanzierung, Gesellschafterdarlehen und einer Liquiditätsenge. Ein privater Darlehensgeber macht eine bislang nicht vollzogene Wandlungsabrede geltend.

Der ausführliche Vertragsentwurf ist eine fallbezogene Ausfüllfassung in Times New Roman 11 mit dezimaler Gliederung, vollständig formulierten Klauseln und ausfüllbaren Vertragsanlagen. Er ist keine beurkundete oder unterschriftsreife Endfassung. Das Term Sheet enthält Verhandlungspositionen; Anlagen, Vertretung und offene Entscheidungen müssen noch ergänzt werden. Die Excel-Arbeitsmappe unterscheidet historischen Bestand, geplante Runde, Darlehenszinsen und eine gesonderte Wandlungsrechnung. Eine Rechenvariante ist keine bereits vereinbarte Beteiligung.

Alle Personen, Unternehmen, Anschriften und Vorgänge sind erfunden. Kontaktadressen verwenden reservierte Beispieldomains. Keine Kontaktdaten zum tatsächlichen Versand verwenden. Der technische Fall enthält keine Betriebsfreigabe für einen Einsatz an Menschen.

Zugeordnetes Plugin: [Gesellschaftervereinbarung](../../gesellschaftervereinbarung/README.md).

## 2 Downloads

<!-- BEGIN gesamt-pdf-section (autogen) -->

{NOTICE_MARKDOWN}

| Gesamt-PDF | Einzel-PDF-ZIP | Akten-ZIP mit Originalformaten |
| --- | --- | --- |
| [Akte am Stück](gesamt-pdf/{slug}_gesamt.pdf) | [Einzelne PDFs]({release}/testakte-{slug}-einzelpdfs.zip) | [Word, Excel, PDF, E-Mail, CSV und Text]({release}/testakte-{slug}.zip) |

<!-- END gesamt-pdf-section (autogen) -->

Beide ZIPs sind flach und enthalten die zweisprachige README.txt. Das Originalformat-ZIP enthält zusätzlich die Gesamt-PDF als Lesefassung. Bei Auswertung der Einzeldateien diese Lesefassung nicht nochmals mitladen. E-Mail-Anhänge entsprechen den gesondert vorhandenen Originalen und sind nicht als zusätzliche Vorgänge zu zählen.

## 3 Einzeldateien

{NOTICE_MARKDOWN}

| Datei | Format |
| --- | --- |
{table}

## 4 English Overview

A fictional Berlin robotics company negotiates a two-stage equity financing. The file contains competing party positions, editable drafts, corporate records, technical limitations, correspondence and a formula-based capital workbook. It contains no answer key. Complete the open choices before treating any draft as executable. Choose one of the three editions above.

[Repository](../../README.md) · [Alle Akten](../README.md) · [Plugin](../../gesellschaftervereinbarung/README.md) · [Download-Index](../../ASSET_INDEX.md)
""",
        encoding="utf-8",
    )
    print(
        f"{slug}: {len(paths)} Originale einschließlich gesondert gebauter Arbeitsmappe"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=DATA / "gesellschaftervereinbarung-vorlagen",
    )
    build(parser.parse_args().template_dir)

#!/usr/bin/env python3
"""Baut die drei individuell verfassten AGB-Mandatsakten in Originalformaten."""
import csv
import importlib.util
import json
from pathlib import Path
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/agb-werkstatt-akten.json"
TAG = "agb-werkstatt-v1.0.0"


def load_renderer():
    spec = importlib.util.spec_from_file_location("agb_native", ROOT / "scripts/build-geldwaeschebeauftragter-akten.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build():
    renderer = load_renderer()
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    regular, bold = renderer.font_paths()
    pdfmetrics.registerFont(TTFont("AkteSerif", str(regular)))
    pdfmetrics.registerFont(TTFont("AkteSerifBold", str(bold)))
    for case in json.loads(DATA.read_text(encoding="utf-8"))["cases"]:
        directory = ROOT / "testakten" / case["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        paths = [item["path"] for group in ("documents", "emails", "raw") for item in case[group]]
        if len(paths) != len(set(paths)) or any(Path(p).name != p for p in paths):
            raise ValueError("Aktenpfade müssen eindeutig und flach sein")
        for item in case["documents"]:
            target = directory / item["path"]
            if target.suffix == ".pdf":
                renderer.create_pdf(target, item)
            elif target.suffix == ".docx":
                renderer.create_docx(target, item)
            else:
                raise ValueError(f"Nicht unterstütztes Dokumentformat: {target.name}")
        for item in case["emails"]:
            renderer.create_eml(directory, case, item)
        for item in case["raw"]:
            target = directory / item["path"]
            if target.suffix == ".csv":
                rows = item["rows"]
                if len(rows) < 5 or len({len(row) for row in rows}) != 1:
                    raise ValueError("Unvollständige CSV-Struktur")
                with target.open("w", encoding="utf-8", newline="") as handle:
                    csv.writer(handle, delimiter=";", lineterminator="\n").writerows(rows)
            elif target.suffix == ".txt":
                target.write_text(item["text"], encoding="utf-8")
            else:
                raise ValueError(f"Nicht unterstützte Rohdatei: {target.name}")
        slug = case["slug"]
        release = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}"
        overview = "\n".join(f"| `{p}` | {Path(p).suffix[1:].upper()} |" for p in sorted(paths))
        readme = f"""# {case['title']}

<!-- reserved-example-contacts -->

## 1 Akteninhalt

{case['summary']}

Zugeordnetes Plugin: [AGB-Werkstatt](../../agb-werkstatt/README.md). Die Unterlagen enthalten den Mandatsauftrag und Geschäftsvorgänge, aber keine Musterlösung. Personen und Unternehmen sind erfunden; Kontaktadressen verwenden reservierte Beispieldomains.

## 2 Downloads

<!-- BEGIN gesamt-pdf-section (autogen) -->

{NOTICE_MARKDOWN}

| Gesamt-PDF | Einzel-PDF-ZIP | Akten-ZIP |
| --- | --- | --- |
| [PDF](gesamt-pdf/{slug}_gesamt.pdf) | [ZIP]({release}/testakte-{slug}-einzelpdfs.zip) | [ZIP]({release}/testakte-{slug}.zip) |

<!-- END gesamt-pdf-section (autogen) -->

Wählen Sie eine Fassung je Arbeitsordner. Beide ZIPs sind flach und enthalten die zweisprachige README.txt. Die Originalakte enthält Word-Dokumente, PDFs, vollständige E-Mails mit Dateianhängen sowie CSV- und Textdateien; keine Markdown-Aktenstücke. In den PDFs steht der Hinweis nicht nochmals.

## 3 Einzelunterlagen

| Datei | Format |
| --- | --- |
{overview}

## 4 English Overview

A fictional German business mandate with original correspondence, draft terms, invoices and operational records. There is no solution key. Choose the combined PDF, individual PDF archive or mixed original-format archive; do not load all three together. Both archives contain the bilingual experimental-use notice.

[Alle Akten](../README.md) · [Plugin](../../agb-werkstatt/README.md) · [Download-Index](../../ASSET_INDEX.md) · [Repository](../../README.md)
"""
        (directory / "README.md").write_text(readme, encoding="utf-8")
        print(f"{slug}: {len(paths)} Originaldateien")


if __name__ == "__main__":
    build()

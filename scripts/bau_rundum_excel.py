"""Fallbezogene Excel-Unterlagen; Prüferwartungen bleiben außerhalb der Akten."""

import json
from pathlib import Path
import re
from readme_decimal_headings import normalize_decimal_headings

ROOT = Path(__file__).resolve().parents[1]
RELEASE = "bauwirtschaft-rundum-v445.33.3"


def specifications():
    result = []
    for part in ("basis", "vertiefung"):
        result.extend(json.loads((ROOT / "scripts" / f"bau_rundum_excel_{part}.json").read_text(encoding="utf-8")))
    return result


def extra_originals(slug):
    return [s["filename"] for s in specifications() if s["slug"] == slug]


def update_readmes():
    for spec in specifications():
        file = ROOT / "testakten" / spec["slug"] / "README.md"
        text = file.read_text(encoding="utf-8")
        from testakte_zip_common import working_dump_archive_pairs
        count = len(working_dump_archive_pairs(file.parent, include_gesamt_pdf=False))
        text = re.sub(r"\b\d+ eigenständige Original(unterlagen|dateien)", lambda m: f"{count} eigenständige Original{m[1]}", text)
        text = re.sub(r"bauwirtschaft-rundum-v\d+\.\d+\.\d+", RELEASE, text)
        inventory = re.search(r"^\| (?:Datei \| Format|Nr\. \| Datei \| Datum \| Inhalt) \|\n(?:\|[^\n]*\n)+", text, re.MULTILINE)
        if inventory is None:
            raise ValueError(f"{file}: Verzeichnis der Originalunterlagen fehlt.")
        if f"]({spec['filename']})" not in inventory[0]:
            if inventory[0].startswith("| Nr."):
                date = ".".join(reversed(spec["date"].split("-")))
                row = f"| {spec['filename'].split('_', 1)[0]} | [{spec['filename']}]({spec['filename']}) | {date} | {spec['title']} |\n"
            else:
                row = f"| [{spec['filename']}]({spec['filename']}) | XLSX |\n"
            text = text[:inventory.end()] + row + text[inventory.end():]
        start = "<!-- BEGIN excel-unterlagen -->"
        end = "<!-- END excel-unterlagen -->"
        block = (f"{start}\n\n"
                 f"## 1.5. Excel-Arbeitsmappe\n\n"
                 f"[{spec['title']}]({spec['filename']}) enthält "
                 f"{sum(len(s['rows']) for s in spec['sheets'])} Datenzeilen auf "
                 f"{len(spec['sheets'])} Tabellenblättern: "
                 + ", ".join(s["name"] for s in spec["sheets"]) + ". "
                 "Filter, Formeln und eingefrorene Kopfzeilen unterstützen den Belegabgleich. "
                 "Die Arbeitsmappe liegt auch im Originalformat-ZIP; ihre Tabellen sind in den beiden PDF-Fassungen enthalten. "
                 "Die Zahlenwerke sind Arbeitsstände der jeweiligen Projektbeteiligten und nicht ungeprüft zu übernehmen.\n\n"
                 f"[Excel-Datei direkt herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{RELEASE}/{spec['slug']}.xlsx).\n\n"
                 f"{end}")
        if start in text:
            before, rest = text.split(start, 1)
            _, after = rest.split(end, 1)
            text = before + block + after
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
        file.write_text(normalize_decimal_headings(text), encoding="utf-8")

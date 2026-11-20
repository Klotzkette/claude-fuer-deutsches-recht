#!/usr/bin/env python3
"""Erstellt den Fallkatalog und gleicht die Eingangslinks auf zentralen Fallseiten ab."""

import argparse

from akteneingang.quellen import ROOT, catalogs
from akteneingang.verweise import central_row, links, routes
from testakte_disclaimer import NOTICE_MARKDOWN

HEADER = """# Arbeitsakten mit Eingangspost

Wählen Sie den Fall über die Seitensuche. Entpacken Sie das **Arbeits-ZIP**. Öffnen Sie für die erste Bearbeitung den Ordner `Grundakte`. Unter `00_Posteingang` finden Sie die fallbezogenen Nachrichten, Belege und offenen Rückfragen. Die `README.txt` im ZIP nennt die Absender, Betreffzeilen und weitere Eingangsunterlagen. Für die nächste Runde können Sie den übrigen Aktenbestand hinzunehmen.

Die Druckpakete bündeln jeweils bis zu 15 Fallordner. Im angegebenen Fallordner liegen die durchsuchbare Gesamtakte und ein ZIP mit Einzel-PDFs. Die Steuerakte Tomasius ist auf Wunsch als Originalformat-ZIP erhältlich.
"""
FOOTER = """Die beiden Schweriner Vergabeakten teilen einen Sachverhalt und werden in ihrer jeweiligen Ablage geführt. Der Berliner Mietspiegel ist bei den [Arbeitshilfen für Immobilienfälle](../../projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/TESTAKTEN.md) verzeichnet.
"""


def title(key, slug):
    page = ROOT / key / "README.md"
    if page.is_file():
        for line in page.read_text().splitlines():
            if line.startswith("# "):
                name = line[2:].strip()
                if name.casefold() not in ("testakte", "testakten"):
                    return name.replace("|", "–")
                break
    return slug.replace("-", " ").capitalize()


def apply(path, content, check):
    if path.is_file() and path.read_text() == content:
        return
    if check:
        raise ValueError("Abweichender Katalog oder Downloadblock: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records = catalogs()
    targets = routes(records)
    lines = [HEADER]
    for central, heading in (
        (True, "Zentral geführte Akten"),
        (False, "Weitere Arbeitsakten und eigenständige Pluginfassungen"),
    ):
        lines += [
            "## " + heading,
            "",
            NOTICE_MARKDOWN,
            "",
            "| Fall | Fallordner im Druckpaket | Vollständige Akte | Lesefassungen |",
            "| --- | --- | --- | --- |",
        ]
        for key, (slug, part) in targets.items():
            if key.startswith("testakten/") != central:
                continue
            native, printpack = links(key)
            if records[key].get("nur_original"):
                printpack = "Originalformate"
            lines.append(f"| {title(key, slug)} | {slug} | {native} | {printpack} |")
            if central:
                file = ROOT / key / "README.md"
                text = file.read_text()
                begin = text.index("<!-- BEGIN gesamt-pdf-section (autogen) -->")
                start = text.index("| --- |", begin)
                end = text.index("\n", start)
                row = central_row(slug, 3 if text[start:end].count("|") == 4 else 2)
                if row not in text:
                    apply(file, text[:end] + "\n" + row + text[end:], args.check)
        lines += [""]
    lines.append(FOOTER)
    apply(ROOT / "docs/grundakten-lebenswelt/README.md", "\n".join(lines), args.check)


if __name__ == "__main__":
    main()

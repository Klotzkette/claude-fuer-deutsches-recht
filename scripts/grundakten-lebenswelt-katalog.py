#!/usr/bin/env python3
"""Erstellt den Fallkatalog und gleicht die Eingangslinks auf zentralen Fallseiten ab."""

import argparse

from akteneingang.quellen import ROOT, catalogs
from akteneingang.vertiefung import fachredaktion
from akteneingang.verweise import central_row, links, routes
from release_routing import case_asset_url
from testakte_disclaimer import NOTICE_MARKDOWN

HEADER = """# Arbeitsakten mit Eingangspost

Wählen Sie den Fall über die Seitensuche. Entpacken Sie das **Arbeits-ZIP**. Öffnen Sie für die erste Bearbeitung den Ordner `Grundakte`. Unter `00_Posteingang` finden Sie die fallbezogenen Nachrichten, Belege und offenen Rückfragen. Die `README.txt` im ZIP nennt die Absender, Betreffzeilen und weitere Eingangsunterlagen. Für die nächste Runde können Sie den übrigen Aktenbestand hinzunehmen.

Für die notarielle Praxis gibt es außerdem [sieben Amtsgeschäfte und dreizehn Bestandsakten](../../allgemeines-notariat/testakten/README.md). [Fünf Akten zur Aktenanlage](../../aktenanleger/testakten/README.md) und [drei zur steuerlichen Umwandlung](../../umwandlungssteuerrecht/testakten/README.md) enthalten jeweils eine Grundakte und spätere Nachreichungen.

Die [Fachauswahl nach Rechtsgebiet](Fachakten.md) erschließt die mehrstufige Eingangspost für die gemeinsame Bearbeitung im Kurs. Für die vertieften Fachakten führt „Druckfassungen dieses Falls“ direkt zum gewünschten Fall. Die nummerierten Druckpakete bündeln jeweils bis zu 15 Fallordner. Im angegebenen Ordner liegen die durchsuchbare Gesamtakte und ein ZIP mit Einzel-PDFs. Die Steuerakte Tomasius ist auf Wunsch als Originalformat-ZIP erhältlich.
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


def fachkatalog(records, check):
    themen = (
        "Sozialrecht",
        "Datenschutzrecht",
        "Gesellschaftsrecht",
        "Insolvenzrecht",
        "Kündigungsschutz und Arbeitsrecht",
    )
    alle = fachredaktion()
    gruppen = {name: [] for name in themen}
    for key, teile in alle.items():
        fachgebiete = set()
        for fach, record in teile:
            gebiete = record.get(
                "fachgebiete", ["Insolvenzrecht"] if fach == "insolvenz" else []
            )
            if not gebiete or set(gebiete) - set(themen):
                raise ValueError("Fachgebiet fehlt oder unklar: " + key)
            fachgebiete.update(gebiete)
        for gebiet in fachgebiete:
            gruppen[gebiet].append(key)
    neuralis_release = case_asset_url("neuralis-medtech-erlangen-gestaltungsakte").rsplit("/", 1)[0]
    lines = [
        "# Fachakten mit fortgeführter Eingangspost",
        "",
        f"Die Auswahl umfasst {len(alle)} eigenständige Akten. Fälle mit mehreren fachlichen Schwerpunkten erscheinen in den jeweiligen Abschnitten.",
        "",
        f"Der [Bestandsnachweis mit Prüfsummen](fachausgabe.json) gehört zur Sammelausgabe `grundakten-fachakten-v1.1.0`. Für die erweiterte Neuralis-Akte gelten der [Bestandsnachweis]({neuralis_release}/release-bestand.json) und die [Prüfsummen der Einzelausgabe]({neuralis_release}/checksums-sha256.txt).",
        "",
        "Öffnen Sie zunächst das Arbeits-ZIP des Falls. Unter `Grundakte/00_Posteingang` stehen der ausgebaute Erstkontakt, anschließende Nachrichten und die dazugehörigen Belege. Eine Antwort lässt sich über den Nachrichtenkopf ihrer Anfrage zuordnen. Wenn eine Datei mitgeschickt wurde, können Sie die Anlage direkt aus der E-Mail öffnen.",
        "",
        "In einzelnen Akten ist auch ein älteres Word-Dokument oder eine Tabelle als fortgeschriebene Arbeitskopie enthalten. Unter `Grundakte/Arbeitsfassungen` lässt sich etwa Heinz Körners ursprüngliche Wegeschilderung zusammen mit seiner späteren Präzisierung lesen. Die Druckmappe enthält die Gesamtakte und einzeln durchsuchbare PDFs. Die Steuerakte Tomasius steht als Originalformat-ZIP bereit.",
        "",
    ]
    lines += [
        " · ".join(f"[{name}](#{name.lower().replace(' ', '-')})" for name in themen),
        "",
    ]
    for gebiet, keys in gruppen.items():
        lines += [
            "## " + gebiet,
            "",
            NOTICE_MARKDOWN,
            "",
            "| Fall | Originalunterlagen | Lesefassungen |",
            "| --- | --- | --- |",
        ]
        for key in sorted(keys):
            slug = records[key].get("id", key.split("/")[-1])
            native, pdfs = links(key)
            if records[key].get("nur_original"):
                pdfs = "Originalformat-ZIP"
            lines.append(f"| {title(key, slug)} | {native} | {pdfs} |")
        lines += [""]
    apply(ROOT / "docs/grundakten-lebenswelt/Fachakten.md", "\n".join(lines), check)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records = catalogs()
    fachkatalog(records, args.check)
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
                previous = central_row(
                    slug, 3 if text[start:end].count("|") == 4 else 2, historisch=True
                )
                if row not in text:
                    if previous != row and text[end:].startswith(
                        "\n" + previous + "\n"
                    ):
                        updated = text[:end] + text[end:].replace(previous, row, 1)
                    else:
                        updated = text[:end] + "\n" + row + text[end:]
                    apply(file, updated, args.check)
        lines += [""]
    lines.append(FOOTER)
    apply(ROOT / "docs/grundakten-lebenswelt/README.md", "\n".join(lines), args.check)


if __name__ == "__main__":
    main()

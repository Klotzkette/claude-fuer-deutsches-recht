#!/usr/bin/env python3
"""Verständliche Einstiege zu den vier bAV-Arbeitsakten, getrennt von den Belegen."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/bav-konzern-faelle"
CASES = {
    "bav-strategie-konzern-meissner-rheinwerk-ag": (
        "Historische Versorgungsordnungen und Besitzstände im Harmonisierungsprojekt.",
        ["Welche Regelung gilt für welche Personengruppe, und welcher Originalbeleg trägt die Zuordnung?",
         "Wie unterscheiden sich Dienstzeitbegrenzung, Entgeltbegrenzung und ein neuer Beitragsbaustein?",
         "Welche Gremien sind für welchen Gegenstand zuständig, und welche Finanzdaten fehlen für die Entscheidung?"],
        "Nach dem Archivfund die betroffenen Zuordnungen und Berechnungsannahmen erneut prüfen. Geänderte Ergebnisse mit dem neuen Beleg und ihrer Auswirkung erläutern."),
    "bav-carve-out-rheinbogen-automation": (
        "Unternehmenskauf mit Beschäftigtenzuordnung, Altzusagen und gebundenem Treuhandvermögen.",
        ["Wie unterscheiden sich die vorgesehenen Transaktionsstrukturen für Arbeitgeber und Versorgungsschuldner?",
         "Welche Verpflichtungen, Vermögenswerte und Sicherheiten erfasst jede Vertragsanlage tatsächlich?",
         "Welche Bedingungen müssen vor einer verbindlichen Umsetzung geklärt oder vertraglich abgesichert werden?"],
        "Nachgereichte Personen-, Garantie- und Treuhandunterlagen gegen den ersten Vertragsentwurf halten. Betroffene Klauseln gezielt neu formulieren und verbleibende Lücken benennen."),
    "bav-rentnergesellschaft-rheinhafen-logistik": (
        "Rentnergesellschaft zwischen Anbieterangebot, Dotierung und langfristiger Leistungsfähigkeit.",
        ["Welche rechtliche Struktur wird angeboten und welche Verpflichtungen sollen übergehen?",
         "Wie unterscheiden sich Buchwert, Angebotspreis, verfügbare Mittel und belastbare Sicherheiten?",
         "Welche Finanzierungsszenarien und Vertragsregelungen benötigt eine vertretbare Geschäftsführungsentscheidung?"],
        "Die späteren Angaben zur Finanzierung mit der ursprünglichen Ausstattung und dem Zahlungsplan vergleichen. Die Entscheidungsvorlage auf die tatsächlich belegte Lage umstellen."),
    "bav-pensionskasse-niederrhein-verbund": (
        "Pensionskassenkürzung, unterschiedliche Zusagen und Rentenanpassung im Unternehmensverbund.",
        ["Welche Leistung wurde vom Arbeitgeber zugesagt, welche zahlt der Träger und welche Bestandteile sind unterschiedlich?",
         "Welche Zusage-, Übergangs- und Anpassungsregeln gelten für die jeweiligen Personengruppen?",
         "Welche Unterlagen ermöglichen eine nachvollziehbare Beschäftigtenantwort und eine zutreffende Zahlungsvorlage?"],
        "Neue Zusage- und Zahlungsbelege personengenau einarbeiten. Nur die betroffenen Beträge und Begründungen ändern und die bisherige Bearbeitung nachvollziehbar erhalten."),
}


def main():
    rows = []
    for slug, (short, questions, continuation) in CASES.items():
        case = json.loads((DATA / f"{slug}.json").read_text())
        directory = ROOT / "testakten" / slug
        directory.mkdir(parents=True, exist_ok=True)
        items = [r for group in ("documents", "workbooks", "slides") for r in case[group]]
        count = {folder: sum(r["path"].startswith(folder + "/") for r in items) for folder in ("Grundakte", "Fortsetzung")}
        formats = ", ".join(sorted({Path(r["path"]).suffix.upper().lstrip(".") for r in items}))
        lines = [f"# {case['title']}", "", case["story"], "",
                 "## 1. Die Situation bei Mandatseingang", "",
                 f"Sie begleiten **{case['client']}** aus Sicht der beratenden Kanzlei. {case['assignment']}", "",
                 "Beginnen Sie ausschließlich mit dem Ordner **Grundakte**. Er enthält die beim ersten Auftrag vorliegenden Unterlagen und Rohdaten. Eine bereits erstellte Klage, ein Gutachten mit Musterlösung oder eine fertige Entscheidungsvorlage wird für diesen Durchgang nicht vorausgesetzt.", "",
                 "## 2. Unterlagen und Bearbeitungsstände", "",
                 "| Ordner | Inhalt | Originaldateien |", "| --- | --- | ---: |",
                 f"| `Grundakte/` | Erster Auftrag, Verträge, Korrespondenzen, Daten und Projektunterlagen | {count['Grundakte']} |",
                 f"| `Fortsetzung/` | Später eingegangene Unterlagen für die erneute Prüfung | {count['Fortsetzung']} |", "",
                 f"Formate: {formats}. Die Tabellen enthalten bearbeitbare Daten; ausgewählte Einzelpersonen sind von den aggregierten Konzernbeständen zu unterscheiden. E-Mail-Anlagen bleiben in ihrem Nachrichtenkontext erhalten.", "",
                 "## 3. Erster Arbeitsauftrag", "",
                 "> Lesen Sie die Grundakte. Erstellen Sie zuerst eine kurze verständliche Darstellung des Unternehmens, des Vorhabens und der noch offenen Entscheidung. Ordnen Sie Tatsachen, Aussagen einzelner Beteiligter und fehlende Nachweise den konkreten Dateien zu. Bearbeiten Sie danach den erteilten Auftrag und liefern Sie das angeforderte Dokument vollständig ausformuliert. Rechnen Sie mit den belegten Eingaben; ergänzen Sie keine angeblich üblichen Marktpreise oder unbekannte versicherungsmathematische Werte.", "",
                 "Für die anschließende Diskussion:", "", *(f"- {q}" for q in questions), "",
                 "## 4. Zweiter Durchgang", "", continuation, "",
                 "Öffnen Sie dafür erst jetzt **Fortsetzung**. Die Gesamt-PDF enthält beide Bearbeitungsstände und eignet sich deshalb besonders für die Nachbesprechung. Das Originalformat-ZIP enthält weder diese Gesamt-PDF noch eine Musterlösung.", "",
                 "## 5. Rahmen der Übung", "",
                 "Mandatiert ist die fiktive Boutique **Kashiwara · Treuenfels Rechtsanwälte Partnerschaft mbB**, Am Rheinbogen 18, 51373 Leverkusen, mit Dr. Kashiwara Harunobu und Dr. Nora Treuenfels. Der Familienname steht zuerst; die Anrede lautet „Herr Dr. Kashiwara“. Unternehmen, Personen, Anschriften und Konditionen sind Übungsmaterial. Adressen unter `.example` sind reservierte Beispieldomains.", "",
                 "<!-- reserved-example-contacts -->", "",
                 "Die Modelle dienen der Strukturierung und Szenarioplanung. Sie ersetzen keine versicherungsmathematische Begutachtung oder Abschlussprüfung. Einzelfallbehauptungen in Nachrichten oder Vertragsentwürfen sind zu prüfen; sie werden durch ihre Aufnahme in die Akte nicht als rechtlich zutreffend bestätigt.", "",
                 "[Zum bAV-Plugin](../../bav-strategie-konzern/README.md) · [Alle Testakten](../README.md)", ""]
        readme = directory / "README.md"
        readme.write_text("\n".join(lines))
        rubric = {"name": case["title"], "plugin": "bav-strategie-konzern", "checks": [
            {"id": "arbeitsbestand", "check_type": "working_file_count", "description": "Der deklarierte Originalbestand ist vorhanden.", "min": len(items)},
            {"id": "gesamt-pdf", "check_type": "file_exists", "description": "Die getrennte Lesefassung ist vorhanden.", "path": f"gesamt-pdf/{slug}_gesamt.pdf"},
            *[{"id": f"fachpruefung-{i}", "check_type": "human_review", "description": question} for i, question in enumerate(questions, 1)],
            {"id": "fortsetzung", "check_type": "human_review", "description": continuation},
        ]}
        (directory / "rubric.yaml").write_text(yaml.safe_dump(rubric, allow_unicode=True, sort_keys=False))
        spec = importlib.util.spec_from_file_location("case_readme_downloads", ROOT / "scripts/inject-gesamt-pdf-section.py")
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        module.inject(readme, slug)
        from release_routing import case_asset_url
        rows.append(f"| [`{slug}/`](./{slug}/) | {short} Grundakte und spätere Fortsetzung; {len(items)} Originaldateien. | `bav-strategie-konzern` | [Gesamt-PDF](./{slug}/gesamt-pdf/{slug}_gesamt.pdf) · [`testakte-{slug}.zip`]({case_asset_url(slug, root=ROOT)}) · [`testakte-{slug}-einzelpdfs.zip`]({case_asset_url(slug, '-einzelpdfs', root=ROOT)}) |")
    index = ROOT / "testakten/README.md"
    old = index.read_text().splitlines()
    positions = [i for i, line in enumerate(old) if any(line.startswith(f"| [`{slug}/`]") for slug in CASES)]
    at = min(positions) if positions else next(i for i, line in enumerate(old) if line.startswith("| [`"))
    old = [line for i, line in enumerate(old) if i not in positions]
    old[at:at] = rows
    # Das zentrale Register bleibt alphabetisch nach Aktenordner sortiert.
    indices = [i for i, line in enumerate(old) if line.startswith("| [`") and "/`](./" in line]
    ordered = sorted((old[i] for i in indices), key=lambda line: line.split("`", 2)[1].lower())
    for i, line in zip(indices, ordered):
        old[i] = line
    index.write_text("\n".join(old) + "\n")
    print("Vier bAV-Akteneinstiege, Rubriken und zentrale Downloadzeilen aktualisiert")


if __name__ == "__main__":
    main()

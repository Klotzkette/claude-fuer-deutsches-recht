#!/usr/bin/env python3
"""Prüft Prompt-Vollständigkeit, Dezimalgliederung und kritische Fachrouten."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from themen_profile import EXACT_PROFILE_KEYS, profile_for  # noqa: E402


CRITICAL_ROUTES = dict(EXACT_PROFILE_KEYS)
# Fünf operative Zeugnisaufgaben plus vier Kontextfelder, ohne Füllrouten.
EXPECTED_ROUTE_COUNTS = {"arbeitszeugnisgenerator": 9}

PROMPT_ASSERTIONS: dict[str, dict[str, tuple[str, ...]]] = {
    "grosskanzlei-corporate-ma": {
        "required": ("V ZR 77/22", "C-746/21 P"),
        "forbidden": ("Das Arbeitsprodukt „Garantiekatalog-Zeile“",),
    },
    "arbeitszeugnisgenerator": {
        "required": ("8 AZB 25/25", "9 AZR 272/22", "9 AZR 584/13"),
        "forbidden": ("Elektronische Form ist ausgeschlossen",),
    },
    "fachanwalt-agrarrecht": {
        "required": ("54.000 EUR", "60 Prozent", "BLw 12/11", "LwVfG"),
        "forbidden": (
            "Dreiwochenfrist",
            "1,4-facher Einheitswert",
            "1,5-facher Einheitswert",
            "IV ZR 256/01",
            "10 W 47/20",
            "LwVG und HöfeVfO",
            "Abfindung, Schriftform und Landwirtschaftsgericht",
        ),
    },
    "fachanwalt-sportrecht": {
        "required": ("1 BvR 2103/16", "7 AZR 312/16"),
        "forbidden": ("Auskunft, Einkommen, Bedarf, Selbstbehalt",),
    },
    "juristische-presseberichterstattung": {
        "required": ("1 BvR 573/25", "VI ZR 1241/20"),
        "forbidden": ("Auskunft, Einkommen, Bedarf, Selbstbehalt",),
    },
    "jveg-kostenpruefer": {
        "required": ("JVEG Paragraf 1 und Paragraf 2", "JVEG Paragraf 4", "dreimonatige Ausschlussfrist"),
        "forbidden": ("Dreiwochenfrist",),
    },
    "schoeffen-handelsrichter-praxis": {
        "required": (
            "StPO Paragraf 240 Absatz 2",
            "StPO Paragraf 261",
            "StPO Paragraf 263",
            "Zweidrittelmehrheit",
            "DRiG Paragraf 43",
        ),
        "forbidden": ("(Geheimhaltung)", "Paragraf 76 GVG (Mitwirkung)"),
    },
}

GLOBAL_PROMPT_FORBIDDEN: tuple[str, ...] = (
    "Open" + "AI",
    "Chat" + "GPT",
    "Clau" + "de",
    "Per" + "plexity",
    "Copi" + "lot",
    "Indizien glaubhaft machen",
    "Paragraf 4 RVG — Vergütungsvereinbarung",
    "Paragraf 51b BRAO",
    "Paragraf 33 SGB XI: Pflegeheimbetreuung",
    "Paragraf 73 Absatz 5 SGB V: Wirtschaftlichkeitsgebot",
    "Paragraf 25h KWG – Anzeigepflichten bei Geldwäscheverdacht",
    "100 € Erstattungsdeckelung",
    "Paragraf 309 Nr. 7 Buchst;",
    "Paragraf 16a BNotO",
    "Schutzfrist 50 Jahre ab Entstehung",
    "Schutzfrist: 50 Jahre ab Aufnahme",
    "Briefkraftloserklärung ohne FamFG ermöglichen",
    "Antrag beim Amtsgericht (Paragraf 470 FamFG)",
    "Prüfschritte: Paragraf 5c IfSG nach Pandemienovelle",
    "Bei dinglich übertragener Lizenz kein Wahlrecht",
    "Paragraf 8 EnWG: Anschlusspflicht",
    "Paragraf 2 Nummer 5 AFIR-VO",
    "Übersetzung ist stets Bearbeitung",
    "5–10 Jahre Standardlizenz",
    "Pflichtbestandteil der Wirtschaftsprüfung (Paragraf 320 HGB)",
    "Entschädigung nach dem Verkehrswert; enteignungsrechtliche Entschädigung",
    "Paragrafen 148, 246 ZPO analog",
    "Cape Town Aircraft Protocol Art. XII",
    "Automatische Herausgabepflicht in Insolvenz nach 60 Tagen",
    "typisch 6-12 Monate Nach-Deckung",
    "Paragraf 93 II 3 AktG / analog GmbHG",
    "Paragraf 12 VVG Klagefrist",
    "Paragraf 12 VVG: 1 Monat",
    "Auswahlstichwort:",
    "Au. Output:",
    "Materienbezogene Arbeitsfelder",
    "Output: Ergebnisbaustein mit Risiko, Belegstelle und nächstem Schritt.",
    "ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt",
    "prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen",
    "routet Rolle, Frist, Unterlagen und Fachschritt",
    "erstellt Entwurf mit Antrag, Beweis und Anlagen",
    "prüft Ergebnis, Beweislast und Gegenposition",
    "prüft Frist, Form, Zuständigkeit und Eilbedarf",
    "ordnet Akte, Belege und Lücken",
    "rechnet Beträge, Schwellen und Varianten",
    "entwickelt Ziel, Vergleich und Eskalation",
    "ordnet Norm, Beweislast und Gegenargument",
    "Prüfprodukt mit Risiko und nächstem Schritt",
    "einsatzfertiges Arbeitsprodukt für",
    "P092",
    "Pflichtversto)",
    "Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung",
)

GENERIC_ROUTE_ASSIGNMENT_BITS: tuple[str, ...] = (
    "welches konkrete ziel soll erreicht oder verhindert werden",
    "wenn ein fachskill eindeutig passt",
    "streitige und unstreitige tatsachen trennen, lückentafel",
    "fristen und zuständigkeit sichern: rechtsbehelfsfrist",
    "einschlägige normen, zuständige stellen, verfahrensart",
    "nur einschlägige normen, verifizierte rechtsprechung",
    "arbeitsmodus: erst gesellschaftsform, organ, beschlussweg",
    "welche einheit ist betroffen und welches recht gilt wirklich",
    "arbeitsmodus: zuerst insolvenzgrund, frist, organpflicht",
    "verfahrensarbeit: zuständigkeit, form, frist, anhörung",
    "unsichere tatsachen als offen markieren und nicht durch modellwissen ersetzen",
    "rolle klären: antragstellende person, behörde, verband",
    "rechtsfrage, gewünschtes produkt, empfänger, frist und entscheidungsschwelle",
    "nächste handlung erzeugen: liefere bei bedarf nachreichungsschreiben",
    "hindernisse benennen: formuliere jedes hindernis konkret",
    "frage nur nach, wenn es die rechtliche weiche wirklich verändert",
    "datei, typ, datum, autor, fassung, signatur, dublette",
    "chronologie, beteiligte, dokumentfundstellen, unstreitige tatsachen",
    "arbeitsmodus: immer verwaltungsakt, frist, widerspruch",
    "welche frist, behörde, vertragspartei, kundengruppe",
    "prüfschritt: fristen, zustellung, rolle, zuständigkeit",
    "symptom: falsche zuständigkeit adressiert",
    "symptom: frist falsch berechnet oder übersehen",
    "form und zuständigkeit prüfen: trenne materielle rechtslage",
    "erstelle für entscheidungsvorlage eine entscheidungsreife fassung",
    "rechtsabteilungsfähige kurzentscheidung mit ampel",
    "fristen, zustellungen, aktenzeichen, anhörungen, mahnungen",
    "fristen, registerstand, veröffentlichungen, vertragslage",
    "beteiligte, rolle und kommunikationskanal klären",
    "bearbeite prozessuale kniffe und rechtsprechungsanker entlang",
    "er führt durch dokumentenmatrix",
    "ziel ist nicht ein abstrakter lexikontext",
    "nach parteien, regelungsziel, definitionen, leistung und gegenleistung",
    "als vollständigen melde- oder dokumentationsvorgang",
    "eine entscheidungsreife fassung mit rubrum oder adressat",
    "eine beweis- und zugriffsakte",
    "vom angegriffenen verfügungssatz oder antrag aus",
    "schriftbild: wenn ein schriftsatz",
    "arbeitsmodus: immer erst",
    "welche behörde handelt:",
    "welche behörde, welches gericht, welches register",
    "prüfachse: ordne den konkreten auftrag",
    "trenne sachverhalt, zuständigkeit, zustimmung",
    "transaktionsstruktur, datenraumfund, wertwirkung",
    "auslöser, zugang, fristart, beginn",
    "arbeite zuerst die tragende rechtsfrage heraus",
)

SOURCE_FORBIDDEN: tuple[tuple[Path, tuple[str, ...]], ...] = (
    (
        REPO / "fachanwalt-agrarrecht",
        (
            "1,4-facher Einheitswert",
            "1,5-facher Einheitswert",
            "1 4-facher Einheitswert",
            "1 5-facher Einheitswert",
            "10.000 EUR Einheitswert",
            "Bewirtschaftungspflicht § 17",
            "Altenteilsleistungen § 14 HöfeO",
            "rueckkaufrecht-30-jahre",
            "Rueckkaufrecht 30 Jahre",
            "Rückkaufrecht 30 Jahre",
            "Rueckkaufpreis = Wert bei Hofuebergang",
            "Wirtschaftswert ab 10.000 EUR",
            "Wirtschaftswert ≥ 10.000 EUR",
            "§ 13 LPachtVG",
            "HöfeO gilt nur in NW, NI, SH, HB",
            "Hofvermerk im Grundbuch Pflicht",
            "BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr",
            "Vorpachtrecht § 588 BGB",
            "Vorpacht / Vorpfand-Recht",
            "Vorpacht-Recht",
            "9 Jahre Standard-Laufzeit",
            "Vertrag verlaengert sich um 9 Jahre",
            "Pacht-Anpassung ohne 3-Jahres-Wartezeit",
            "Landwirtschaftsgericht beim Amtsgericht oder Landgericht je nach Streitwert",
            "4-facher Jahres-Pachtzins",
            "4-facher Jahrespachtzins",
            "Schriftform gewahrt (§ 585a BGB)?",
            "Verlaengerung Schriftform § 585a BGB",
            "LwVG",
            "§ 23 LwVfG",
            "Paragraf 23 LwVfG",
            "Pflichtiger Schlichtungsversuch",
            "Schlichtungsantrag nach § 23",
            "Wert bis 5.000 EUR",
            "§ 41 Abs. 1 ZPO",
            "LPachtVG §§ 2, 4, 13",
            "dreifacher Jahresmehrwert",
            "VwGO § 70 / SGG § 84",
        ),
    ),
    (
        REPO / "testakten" / "megaprompts" / "fachanwalt-agrarrecht.md",
        (
            "LwVG",
            "§ 23 LwVfG",
            "Paragraf 23 LwVfG",
            "Pflichtiger Schlichtungsversuch",
            "Schlichtungsantrag nach § 23",
        ),
    ),
    (
        REPO / "juristische-presseberichterstattung" / "skills",
        ("aktueller Suchanker zur Verdachtsberichterstattung",),
    ),
    (
        REPO / "schoeffen-handelsrichter-praxis" / "skills",
        (
            "§ 76 GVG (Mitwirkung)",
            "§ 263 StPO (Geheimhaltung)",
            "§ 43 DRiG (Eid)",
        ),
    ),
    (
        REPO / "notariat-alltag" / "skills",
        (
            "Briefkraftloserklärung ohne FamFG ermöglichen",
            "Antrag beim Amtsgericht (§ 470 FamFG)",
            "§ 16a BNotO (Videobeurkundung",
            "§ 12 BeurkG muss sie in öffentlich beglaubigter Form vorliegen",
            "Liste mindestens 3 Jahre alt ist oder der Berechtigte die Unrichtigkeit nicht kannte",
            "§ 50a EStG (beschränkte Steuerpflicht)",
            "§ 50a EStG: Einbehaltungspflicht des Käufers",
            "Paragraf 50a EStG: Einbehaltungspflicht des Käufers",
            "AO §§ 10–14 (Steuerliche Identifikation)",
        ),
    ),
    (
        REPO / "verlagsrecht-buchpreisbindung" / "skills",
        (
            "Schutzfrist 50 Jahre ab Entstehung",
            "Schutzfrist: 50 Jahre ab Aufnahme",
            "§ 79b UrhG (seit 2014): Öffentliche Einrichtungen dürfen verwaiste Werke",
            "OpenStreetMap: CC BY-SA 2.0",
            "Übersetzung ist stets Bearbeitung",
            "5–10 Jahre Standardlizenz",
            "VerlG § 35 | Übersetzungsrecht",
        ),
    ),
    (
        REPO
        / "fachanwalt-gewerblicher-rechtsschutz"
        / "skills"
        / "dpma-mehrparteien-konflikt-und-interessen"
        / "SKILL.md",
        (
            "§ 41 MarkenG | Widerspruch gegen Markeneintragung",
            "§ 55 MarkenG: Unterlassung",
            "§ 10 MarkenG (ältere Markenpolitik)",
            "§§ 148, 246 ZPO analog",
        ),
    ),
    (
        REPO / "steuerrecht-anwalt-und-berater" / "skills",
        (
            "Saldenabstimmung ist Pflichtbestandteil der Wirtschaftspruefung",
            "Saldenabstimmung ist Pflicht bei Wirtschaftspruefung",
            "§ 320 HGB — Prüfungspflicht; Abstimmung Pflicht für WP",
        ),
    ),
    (
        REPO / "luftrecht-flughafenrecht" / "skills",
        (
            "Cape Town Aircraft Protocol Art. XII",
            "ICAO-Register",
            "IDERA nicht im Cape-Town-Register eingetragen",
            "Aircraft Protocol Art. IX**: Rangverhältnis",
            "Art. 30 Aircraft Protocol",
            "Automatische Herausgabepflicht in Insolvenz nach 60 Tagen",
        ),
    ),
    (
        REPO / "fachanwalt-versicherungsrecht" / "skills",
        (
            "§ 12 VVG Klagefrist",
            "Paragraf 12 VVG Klagefrist",
            "typisch 6-12 Monate Nach-Deckung",
            "§ 93 II 3 AktG / analog GmbHG",
            "Selbstbehalt-Pflicht börsennotiert",
            "nur börsennotierte AG; GmbH vertraglich",
        ),
    ),
    (
        REPO / "patentrecht" / "skills",
        (
            "TT-GVO (EU) 316/2014:",
            "TT-GVO (EU 316/2014, Auflauf",
        ),
    ),
)

GLOBAL_MD_FORBIDDEN: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bVwG\b"), "VwG statt VwGO oder ausgeschriebenem Verwaltungsgericht"),
    (re.compile(r"\bLwVG\b"), "LwVG statt LwVfG"),
)

REQUIRED_WERKSTATT = (
    ("Rolle und Auftrag",),
    (
        "Rechtsprechungs-Fallkarte",
        "Quellen- und Deutungsfallkarte",
        "Prüf- und Evidenzfallkarte",
        "Produktions- und Übergabekarte",
        "Regelungs- und Vollzugsfallkarte",
        "Verfahrens- und Entscheidungsfallkarte",
    ),
    (
        "Normenanker, Tatbestandswichtigkeiten und Beweislast",
        "Quellenanker, Textstufe, Deutungslast und Wirkung",
        "Maßstäbe, Kernfragen, Evidenz und Folgerung",
        "Anforderungen, Qualitätsmerkmale, Nachweis und Ausgabe",
        "Rechtsanker, Regelungsmechanik, Nachweis und Vollzug",
        "Rechtsanker, Entscheidungsmerkmale, Beweislast und Tenorfolge",
    ),
    (
        "Rechtsprechungsanker, Quellenstatus und Rechtsfolgen",
        "Quellenstatus, Gegenlesarten und Rezeptionswirkung",
        "Quellen-, Rechtsprechungs- und Belastbarkeitsstatus",
        "Vorgaben, Quellenstatus und technische Folge",
        "Rechtsprechungsanker, Quellenstatus und Risikozuweisung",
        "Rechtsprechungsanker, Quellenstatus und Entscheidungswirkung",
    ),
    ("Outputvarianten und Empfängerwunsch",),
)
REQUIRED_SCHNELLSTART = (
    ("Schnellmodus", "Sofortstart nach Eingangslage"),
    ("Direktstart", "Fachlicher Direktstart"),
    ("Kernroute",),
    ("Fallkarte",),
    ("Anker",),
    ("Antwortform",),
    ("Stop",),
)


def protected_slugs() -> set[str]:
    path = REPO / "scripts" / "handkuratierte-prompts.txt"
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def marketplace_plugins() -> list[tuple[str, Path, str]]:
    marketplace = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugins: list[tuple[str, Path, str]] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source", "")
        if not isinstance(source, str) or not source.startswith("./"):
            raise ValueError(f"Ungültige Marketplace-Quelle: {source!r}")
        plugin_dir = REPO / source[2:]
        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        slug = manifest.get("name") or plugin_dir.name
        description = manifest.get("description", "")
        plugins.append((slug, plugin_dir, description))
    return plugins


def decimal_heading_problems(text: str) -> list[str]:
    problems: list[str] = []
    numbers: list[int] = []
    current_h2 = 0
    expected_h3 = 0
    for line in text.splitlines():
        if line.startswith("### "):
            match = re.match(r"^### (\d+)\.(\d+)\.\s+\S", line)
            if not match:
                problems.append(f"H3 nicht dezimal: {line[:100]}")
                continue
            major, minor = map(int, match.groups())
            expected_h3 += 1
            if major != current_h2 or minor != expected_h3:
                problems.append(
                    f"H3-Folge unpassend zu H2 {current_h2}: {line[:100]}"
                )
            continue
        if not line.startswith("## "):
            continue
        match = re.match(r"^## (\d+)\.\s+\S", line)
        if not match:
            problems.append(f"nicht dezimal: {line[:100]}")
            continue
        current_h2 = int(match.group(1))
        expected_h3 = 0
        numbers.append(current_h2)
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        problems.append(f"H2-Folge nicht lückenlos: {numbers}")
    return problems


def source_anchor_problems() -> list[str]:
    problems: list[str] = []
    for root, forbidden_bits in SOURCE_FORBIDDEN:
        files = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for path in files:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for bit in forbidden_bits:
                if bit in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: veralteter oder falscher Anker {bit!r}"
                    )
    for path in sorted(REPO.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, label in GLOBAL_MD_FORBIDDEN:
            if pattern.search(text):
                problems.append(
                    f"{path.relative_to(REPO)}: veraltete Gesetzesabkürzung {label}"
                )
    return problems


def main() -> int:
    plugins = marketplace_plugins()
    protected = protected_slugs()
    problems: list[str] = []
    profile_counts: Counter[str] = Counter()
    checked_files = 0

    slugs = [slug for slug, _plugin_dir, _description in plugins]
    if len(slugs) != len(set(slugs)):
        problems.append("Marketplace enthält doppelte Plugin-Slugs")

    for slug, plugin_dir, description in plugins:
        profile = profile_for(slug, description)
        profile_counts[profile.key] += 1
        expected_route = CRITICAL_ROUTES.get(slug)
        if expected_route and profile.key != expected_route:
            problems.append(
                f"{slug}: Fachroute {profile.key!r}, erwartet {expected_route!r}"
            )

        expected = {
            "werkstatt": plugin_dir / f"{slug}-werkstatt.md",
            "schnellstart": plugin_dir / f"{slug}-schnellstart.md",
        }
        actual = set(plugin_dir.glob("*-werkstatt.md")) | set(
            plugin_dir.glob("*-schnellstart.md")
        )
        extras = actual - set(expected.values())
        if extras:
            for path in sorted(extras):
                problems.append(f"{path.relative_to(REPO)}: verwaister Prompt-Dateiname")

        for kind, path in expected.items():
            checked_files += 1
            if not path.exists():
                problems.append(f"{path.relative_to(REPO)}: fehlt")
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            size = len(text.encode("utf-8"))
            for marker in GLOBAL_PROMPT_FORBIDDEN:
                if marker in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: veralteter oder falscher Promptanker {marker!r}"
                    )
            if re.search(r"Pflichtverstoßß+", text, flags=re.IGNORECASE):
                problems.append(
                    f"{path.relative_to(REPO)}: wiederholt angehängtes scharfes S"
                )
            if kind == "schnellstart" and size > 7500:
                problems.append(f"{path.relative_to(REPO)}: {size} Bytes statt höchstens 7500")
            if kind == "werkstatt" and not 20 * 1024 <= size <= 48 * 1024:
                problems.append(
                    f"{path.relative_to(REPO)}: {size} Bytes außerhalb 20 bis 48 KiB"
                )
            if kind == "werkstatt":
                if re.search(r"^## \d+\. \d+(?:\.\d+)*\. ", text, flags=re.M):
                    problems.append(
                        f"{path.relative_to(REPO)}: mehrfach nummerierte Hauptüberschrift"
                    )
                route_block = re.search(
                    r"^## (\d+)\. Fachspezifische Praxisrouten\s*$"
                    r"(?P<body>[\s\S]*?)(?=^## \d+\.|<!-- END fachrouten-werkstatt|\Z)",
                    text,
                    flags=re.M,
                )
                route_count = 0
                if route_block:
                    major = route_block.group(1)
                    route_count = len(
                        re.findall(
                            rf"^### {re.escape(major)}\.\d+\. ",
                            route_block.group("body"),
                            flags=re.M,
                        )
                    )
                expected_count = EXPECTED_ROUTE_COUNTS.get(slug, 12)
                if route_count != expected_count:
                    problems.append(
                        f"{path.relative_to(REPO)}: {route_count} statt {expected_count} Fachrouten"
                    )
                route_titles = re.findall(
                    rf"^### {re.escape(major)}\.\d+\. (.+)$",
                    route_block.group("body") if route_block else "",
                    flags=re.M,
                ) if route_block else []
                generic_titles = {
                    "aktenvermerk",
                    "arbeitsprodukt",
                    "beschwerdemanagement",
                    "chronologie und belegmatrix",
                    "fristen- und risikoampel",
                    "fristen- und zuständigkeitscockpit",
                    "mandantenkommunikation",
                    "materielle prüfung",
                    "rechtsschutz",
                    "workflow",
                }
                if any(title.strip().lower() in generic_titles for title in route_titles):
                    problems.append(
                        f"{path.relative_to(REPO)}: generischer Fachroutentitel"
                    )
                generic_title_bits = (
                    "abschlussprodukt und übergabe",
                    "automation",
                    "automationen",
                    "billing",
                    "checkliste",
                    "copilot",
                    "cowork",
                    "dashboard",
                    "design und ausgabestandard",
                    "einsteiger",
                    "einstieg in den skill",
                    "fehlerkatalog",
                    "finder",
                    "hauptworkflow",
                    "intake",
                    "look",
                    "mandantenkommunikation",
                    "monitoring",
                    "policy pack",
                    "simulation",
                    "skill-verbund",
                    "staffing",
                    "schulungsmaterial",
                    "tooling",
                    "training",
                    "überblick",
                    "drift-detektor",
                    "schaufenster-pattern",
                    "adversarial test",
                    "beweislast, darlegungslast und substantiierung",
                    "compliance-dokumentation und aktenvermerk",
                    "tatbestandsmerkmale, beweisfragen und beleglage",
                    "verhandlung, vergleich und eskalation",
                    "fristennotiz und nächster schritt",
                    "internationaler bezug und schnittstellen",
                    "mehrparteienkonflikt und interessenmatrix",
                    "formular, portal und einreichungslogik",
                    "behörden-, gerichts- oder registerweg",
                    "risikoampel, gegenargumente und verteidigungslinien",
                    "formulare, portale und einreichungswege",
                    "schriftsatz-, brief- und memo-bausteine",
                    "sonderfälle und edge cases",
                    "sonderfall und edge-case-prüfung",
                    "zahlen, schwellen und berechnung",
                    "zahlen, schwellenwerte und berechnung",
                    "quality gate",
                    "einarbeitung:",
                    "erstprüfung, rollenklärung und mandatsziel",
                    "anfänger",
                    "quality-gate",
                    "dokumentenmatrix, lückenliste und nachforderung",
                    "paragraf 280 inso",
                    "workflow",
                )
                if any(
                    bit in title.lower()
                    for title in route_titles
                    for bit in generic_title_bits
                ):
                    problems.append(
                        f"{path.relative_to(REPO)}: Meta-Skill statt Fachroute"
                    )
                normalized_titles = [
                    re.sub(r"\W+", "", title.lower()) for title in route_titles
                ]
                if len(normalized_titles) != len(set(normalized_titles)):
                    problems.append(
                        f"{path.relative_to(REPO)}: doppelte Fachroutentitel"
                    )
                assignments = re.findall(
                    r"^Bearbeitungsauftrag: (.+)$",
                    route_block.group("body") if route_block else "",
                    flags=re.M,
                ) if route_block else []
                for assignment in assignments:
                    lowered_assignment = assignment.lower()
                    generic_bit = next(
                        (
                            bit
                            for bit in GENERIC_ROUTE_ASSIGNMENT_BITS
                            if bit in lowered_assignment
                        ),
                        None,
                    )
                    if generic_bit:
                        problems.append(
                            f"{path.relative_to(REPO)}: universeller statt fachlicher "
                            f"Bearbeitungsauftrag {generic_bit!r}"
                        )
                normalized_assignments = [
                    re.sub(r"\W+", "", assignment.lower()) for assignment in assignments
                ]
                if len(normalized_assignments) != len(set(normalized_assignments)):
                    problems.append(
                        f"{path.relative_to(REPO)}: doppelte Bearbeitungsaufträge in Fachrouten"
                    )
                if "Werkstatt-Assistent" in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: Rollenrest 'Werkstatt-Assistent'"
                    )
                if ("clau" + "de-für-deutsches-recht") in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: technischer Pfad durch Umlaut verändert"
                    )
                if "Problemfokus dieses Skills" in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: generischer Problemfokus im Werkstatt-Prompt"
                    )
                if "Tatsachen, Frist, Norm, Beweislast, stärkstes Gegenargument" in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: universelle Fachroute statt Fachauftrag"
                    )
                if "von der ersten Aktenordnung bis zur belastbaren Empfehlung" in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: generischer Aktenordnungs-Platzhalter"
                    )
                route_text = route_block.group("body") if route_block else ""
                if re.search(
                    r"^Bearbeitungsauftrag: Ordne Akteninhalt|"
                    r"^Bearbeitungsauftrag: .*; liefert|"
                    r"^Bearbeitungsauftrag: ([^:\n]+): \1\.$",
                    route_text,
                    flags=re.M,
                ):
                    problems.append(
                        f"{path.relative_to(REPO)}: Schablonentext in Fachroute"
                    )
                for fragment in (
                    "Prüfschritte: atz ",
                    "Prüfschritte: bester nächster Arbeitsschritt",
                    "Bearbeitungsauftrag: Beginne nicht mit einem Fragenkatalog",
                    "Problemfokus dieses Skills",
                    "Abs..",
                    ".. Verbinde den Punkt",
                    "Bearbeitungsauftrag: 1. Scope:",
                    "Bearbeitungsauftrag: 1. Rolle und Ziel:",
                    "Bearbeitungsauftrag: 1. Sachverhalt in einem Satz",
                    "Bearbeitungsauftrag: Wenn Unterlagen vorhanden sind",
                    "Bearbeitungsauftrag: Wenn ein Dokument vorliegt",
                    "Bearbeitungsauftrag: Wenn Material vorliegt",
                    "Bearbeitungsauftrag: Nutze diesen Skill, wenn",
                    "Bearbeitungsauftrag: Normen:",
                    "Bearbeitungsauftrag: Ständige Rechtsprechung",
                ):
                    if fragment in route_text:
                        problems.append(
                            f"{path.relative_to(REPO)}: beschädigte oder generische Fachroute {fragment!r}"
                        )
            for issue in decimal_heading_problems(text):
                problems.append(f"{path.relative_to(REPO)}: {issue}")
            if slug in protected:
                continue
            required = REQUIRED_WERKSTATT if kind == "werkstatt" else REQUIRED_SCHNELLSTART
            for alternatives in required:
                if not any(marker in text for marker in alternatives):
                    label = " oder ".join(repr(marker) for marker in alternatives)
                    problems.append(
                        f"{path.relative_to(REPO)}: fachlich entsprechender Abschnitt "
                        f"({label}) fehlt"
                    )
            assertions = PROMPT_ASSERTIONS.get(slug)
            if assertions:
                for marker in assertions["required"]:
                    if marker not in text:
                        problems.append(
                            f"{path.relative_to(REPO)}: Fachanker {marker!r} fehlt"
                        )
                for marker in assertions["forbidden"]:
                    if marker in text:
                        problems.append(
                            f"{path.relative_to(REPO)}: fachfremder oder falscher Anker {marker!r}"
                        )

    if profile_counts["default"]:
        problems.append(
            f"Plugins ohne Fachprofil: {profile_counts['default']} statt 0"
        )

    problems.extend(source_anchor_problems())

    expected_file_count = len(plugins) * 2
    if checked_files != expected_file_count:
        problems.append(
            f"Prompt-Zählung abweichend: {checked_files} statt {expected_file_count}"
        )

    if problems:
        print("audit-prompt-profile-routing: FEHLER")
        for problem in problems[:120]:
            print(f"- {problem}")
        if len(problems) > 120:
            print(f"- ... {len(problems) - 120} weitere Treffer")
        return 1

    routes = ", ".join(
        f"{key}={count}" for key, count in sorted(profile_counts.items())
    )
    print(
        f"audit-prompt-profile-routing OK ({len(plugins)} Plugins, "
        f"{checked_files} Prompts; {routes})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

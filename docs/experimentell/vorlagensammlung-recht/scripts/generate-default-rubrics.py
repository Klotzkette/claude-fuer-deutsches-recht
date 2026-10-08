#!/usr/bin/env python3
"""generate-default-rubrics.py — erzeugt für jede Vorlage ohne rubric.yaml
eine Baseline-Pass/Fail-Rubric.

Aufbau:
- Strukturhygiene: sprechende Markdown-Datei, gleichnamige ODT-Datei, README.md
- Pflicht-Kurz-Hinweis (10 Tokens: unverbindlich, experimenteller Text,
  keine Rechtsberatung, eigene Gewähr, eigene Gefahr, 43a, 203, DSGVO,
  Apache-2.0, MIT)
- Umlaut-Hygiene: keine typischen ASCII-Ersatzwörter im Fließtext
- Platzhalter-Disziplin: nur [Platzhalter], keine erfundenen Namen wie
  „Max Mustermann" oder „Erika Mustermann"
- Rechtsprechungs-Hygiene: keine missverständliche „verifiziert"-
  Behauptung ohne Direktnachweis
- Az.-Live-Prüfung als human_review
- Anwaltliche Endprüfung als human_review

Zusätzlich typ-spezifische Checks anhand des Slugs (Schriftsatz, Vertrag,
sonstiges).

Vorhandene rubric.yaml werden NICHT überschrieben (außer --force).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import THEMENORDNER, md_in as _md_in, odt_in as _odt_in  # noqa: E402

REPO = Path(__file__).resolve().parents[1]

# Schriftsatz-Schlagwörter im Slug → Vorlage ist ein Schriftsatz/Schreiben
SCHRIFTSATZ_SLUGS = (
    "klage", "antrag", "anzeige", "notifizierung", "auskunftsersuchen", "widerspruch", "einspruch", "ruge", "ruege",
    "abmahnung", "anspruchsschreiben", "schadensersatz",
    "kuendigungsschutzklage", "anhorung", "gegendarstellung",
    "strafanzeige", "verteidigungsanzeige", "deckungsklage",
    "nachprufungsantrag", "erbausschlagung", "erbscheinsantrag",
    "scheidungsantrag", "mangelruege", "asylklage",
    "haftungsanspruch", "stellungnahme", "beschwerdeerwiderung",
    "beschwerde", "revision", "berufung", "erwiderung",
    "schutzschrift", "schutzschirmverfahren",
)

# Vertrags-Schlagwörter → Vorlage ist ein Vertrag/Vereinbarung
VERTRAGS_SLUGS = (
    "vertrag", "vereinbarung", "ehevertrag", "testament",
    "vollmacht", "darlehen", "saas", "auftragsverarbeitung",
    "nda", "verschwiegenheits", "lizenz", "sponsoring",
    "gesellschafterbeschluss", "spielervertrag", "speditions",
    "fracht", "berateragenten", "bietergemeinschaft",
    "grundschuldbestellung", "sicherheitenabrede",
    "sicherungsuebereignung", "verpfaendung", "pfand",
    "buergschaft", "garantie", "schuldbeitritt",
    "haftung-finanzierung", "unterlassungserklaerung",
    "unterlassungserklarung", "verpflichtungserklaerung",
    "verpflichtungserklarung",
)

TYPE_OVERRIDES = {
    # Vertragliche Erklärungen und Vorvereinbarungen, deren Slugs durch
    # Bestandteile wie „antrag“ oder fehlende Vertrags-Schlagwörter sonst
    # fälschlich als Schriftsatz erkannt würden.
    "raeumungsvereinbarung-wohnraum": "vertrag",
    "letter-of-intent-international": "vertrag",
    "letter-of-intent-grenzueberschreitend": "vertrag",
    "letter-of-intent-m-and-a-bilingual": "vertrag",
    "einzelforderungsverkauf-factoring": "vertrag",

    # Anträge, Klagen, Anzeigen und außergerichtliche Rechtsschutzschreiben.
    "anfechtung-erbausschlagung": "schriftsatz",
    "weg-beschlussanfechtungsklage": "schriftsatz",
    "anfechtungsklage-gesellschafterbeschluss": "schriftsatz",
    "selbstanzeige": "schriftsatz",
    "verteidigungsanzeige-akteneinsicht": "schriftsatz",
    "gegendarstellung-entwurf-presse": "schriftsatz",
    "gegendarstellungsanspruch": "schriftsatz",
    "betriebskostenabrechnung-widerspruch": "schriftsatz",
    "widerrufserklarung-fernabsatz-banking": "schriftsatz",
    "widerrufserklarung-verbraucherdarlehen": "schriftsatz",
    "begruendung-fachrichtungswechsel-bafoeg": "schriftsatz",

    # Beschlüsse, Informationen, Vorbereitungsakten und Erklärungsformulare
    # sind weder Vertrag noch Parteischriftsatz.
    "testamentsvollstrecker-annahme-amtspflichten": "sonstiges",
    "vorlagebeschluss-eugh-art-267-aeuv": "sonstiges",
    "selbstanzeige-vorbereitung-371-ao": "sonstiges",
    "vereinsordnungsbeschluss": "sonstiges",
    "datenschutzinformation-mandanten": "sonstiges",
    "datenschutz-einwilligung-mandatskommunikation": "sonstiges",
    "ki-vo-konformitaetserklaerung-hochrisiko-system": "sonstiges",
    "gesellschafterbeschluss": "sonstiges",
    "gesellschafterbeschluss-cash-pooling": "sonstiges",
    "liquidationsbeschluss-gmbh": "sonstiges",
    "gesellschafterbeschluss-satzungsaenderung-gmbh": "sonstiges",
    "gmbh-beschlusspaket-geschaeftsfuehrung-zweisprachig": "sonstiges",
    "kapitalerhoehungsbeschluss-gmbh": "sonstiges",
    "mvz-gesellschafterbeschluss": "sonstiges",
    "abfalldeklaration-nachweis-krwg": "sonstiges",
    "csrd-nachhaltigkeitserklaerung-anlage": "sonstiges",
    "freigabe-vergabeunterlagen-bieterfragen": "sonstiges",
    "werbe-sponsoring-produktplatzierungsregister-medienangebot": "sonstiges",
}

PFLICHT_VORSPRUCH_TOKENS = [
    ("unverbindlich", "unverbindlich"),
    ("experimenteller-text", "experimenteller Text"),
    ("keine-rechtsberatung", "keine Rechtsberatung"),
    ("eigene-gewaehr", "eigene Gewähr"),
    ("eigene-gefahr", "eigene Gefahr"),
    ("brao-43a", "43a"),
    ("stgb-203", "203"),
    ("dsgvo", "DSGVO"),
    ("apache-lizenz", "Apache-2.0"),
    ("mit-lizenz", "MIT"),
]


def detect_type(slug: str, md_name: str | None = None) -> str:
    """Typ-Erkennung aus dem Vorlagen-Slug.

    Die Markdown-Datei heißt inzwischen wie der Vorlagenordner und ist daher
    kein Inhaltstyp-Signal mehr. `md_name` bleibt nur als rückwärtskompatibler
    Parameter erhalten.
    """
    s = slug.lower()
    if s in TYPE_OVERRIDES:
        return TYPE_OVERRIDES[s]
    if any(k in s for k in SCHRIFTSATZ_SLUGS):
        return "schriftsatz"
    if any(k in s for k in VERTRAGS_SLUGS):
        return "vertrag"
    return "sonstiges"


def slug_titel(slug: str) -> str:
    titel = slug.replace("-", " ").title()
    ersetzungen = {
        "Aenderung": "Änderung",
        "Adhaesions": "Adhäsions",
        "Anhoerung": "Anhörung",
        "Aufklaerung": "Aufklärung",
        "Bewaehrung": "Bewährung",
        "Buergschaft": "Bürgschaft",
        "Datenschutzerklaerung": "Datenschutzerklärung",
        "Dsgvo": "DSGVO",
        "Einbuergerung": "Einbürgerung",
        "Einwilligungserklaerung": "Einwilligungserklärung",
        "Erklaerung": "Erklärung",
        "Erlaeuterung": "Erläuterung",
        "Erhoehung": "Erhöhung",
        "Fernwaerme": "Fernwärme",
        "Frachtfuehrer": "Frachtführer",
        "Gebaeude": "Gebäude",
        "Glaeubiger": "Gläubiger",
        "Grenzueberschreitend": "Grenzüberschreitend",
        "Grundstueck": "Grundstück",
        "Gruendung": "Gründung",
        "Geschaeftsfuehrer": "Geschäftsführer",
        "Geschäftsfuehrer": "Geschäftsführer",
        "Geschaeft": "Geschäft",
        "Geschaefts": "Geschäfts",
        "Gmbh": "GmbH",
        "Haftpruefung": "Haftprüfung",
        "Klaerung": "Klärung",
        "Kautionsrueckzahlung": "Kautionsrückzahlung",
        "Kuendigung": "Kündigung",
        "Kuerzung": "Kürzung",
        "Laender": "Länder",
        "Loeschung": "Löschung",
        "Maengel": "Mängel",
        "Mangelruege": "Mängelrüge",
        "Mieterhoehung": "Mieterhöhung",
        "Nacherfullung": "Nacherfüllung",
        "Nachpruefung": "Nachprüfung",
        "Patientenverfuegung": "Patientenverfügung",
        "Persoenliche": "Persönliche",
        "Pruefvermerk": "Prüfvermerk",
        "Pruefung": "Prüfung",
        "Ruege": "Rüge",
        "Rueck": "Rück",
        "Rechtshaengigkeit": "Rechtshängigkeit",
        "Satzungsaenderung": "Satzungsänderung",
        "Schweigepflichtentbindungserklaerung": "Schweigepflichtentbindungserklärung",
        "Selbststaendig": "Selbstständig",
        "Sicherungsuebereignung": "Sicherungsübereignung",
        "Sgb": "SGB",
        "Stpo": "StPO",
        "Ueberpruefung": "Überprüfung",
        "Ueber": "Über",
        "Untaetigkeit": "Untätigkeit",
        "Verfuegung": "Verfügung",
        "Verpfaendung": "Verpfändung",
        "Verlaengerung": "Verlängerung",
        "Verjaehrung": "Verjährung",
        "Muendliche": "Mündliche",
        "Vergaberechtsverstoss": "Vergaberechtsverstoß",
        "Gwb": "GWB",
        "Olg": "OLG",
        "Vermoegens": "Vermögens",
        "Vob": "VOB",
        "Vwgo": "VwGO",
        "Vwvfg": "VwVfG",
        "Bildveroeffentlichung": "Bildveröffentlichung",
        "Berufsunfaehigkeit": "Berufsunfähigkeit",
        "Gross": "Groß",
    }
    for alt, neu in ersetzungen.items():
        titel = titel.replace(alt, neu)
    return titel


def markdown_titel(md_path: Path, slug: str) -> str:
    """Liest den sichtbaren Dokumenttitel aus der ersten H1-Überschrift."""
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return slug_titel(slug)


def yaml_double_quoted(value: str) -> str:
    """Maskiert einen Wert für ein doppelt zitiertes YAML-Skalarfeld."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def build_rubric(
    bereich: str,
    slug: str,
    md_name: str,
    odt_name: str,
    display_name: str | None = None,
) -> str:
    typ = detect_type(slug, md_name)
    name = display_name or slug_titel(slug)
    lines: list[str] = []
    lines.append(f"# Auto-generierte Baseline-Rubric für {bereich}/{slug}.")
    lines.append("# Fachspezifische Pass/Fail-Checks bei Bedarf ergänzen.")
    lines.append("")
    lines.append(f'name: "{yaml_double_quoted(name)}"')
    lines.append(f'plugin: "vorlagen-kanzlei"')
    lines.append(f'typ: "{typ}"')
    lines.append("")
    lines.append("checks:")

    # --- Strukturhygiene ---
    lines.append("  # --- Strukturhygiene ---")
    lines.append("  - id: r01-readme")
    lines.append("    check_type: file_exists")
    lines.append('    description: "Vorlagen-README vorhanden"')
    lines.append('    path: "README.md"')
    lines.append("")
    lines.append("  - id: r02-markdown-quelle")
    lines.append("    check_type: file_exists")
    lines.append('    description: "Markdown-Quelle der Vorlage vorhanden"')
    lines.append(f'    path: "{md_name}"')
    lines.append("")
    lines.append("  - id: r03-odt-endformat")
    lines.append("    check_type: file_exists")
    lines.append('    description: "ODT-Endformat vorhanden"')
    lines.append(f'    path: "{odt_name}"')
    lines.append("")

    # --- Pflicht-Kurz-Hinweis (10 Tokens) ---
    lines.append("  # --- Pflicht-Kurz-Hinweis (Haftungs- und Berufsrechts-Layer) ---")
    for i, (cid, token) in enumerate(PFLICHT_VORSPRUCH_TOKENS, start=4):
        lines.append(f"  - id: r{i:02d}-vorspruch-{cid}")
        lines.append("    check_type: text_contains")
        lines.append(f'    description: "Vorspruch enthält \'{token}\'"')
        lines.append(f'    path: "{md_name}"')
        lines.append(f'    contains: "{token}"')
        lines.append("")

    # --- Umlaut-Hygiene ---
    # Negativ-Check: typische Ersatzwörter dürfen nicht im Fließtext stehen.
    # (Bewusst eng gefasst — Wörter wie „Steuer" oder „Dauer" oder „neue"
    # haben legitime au/eu/ue-Folgen und werden hier nicht erfasst.)
    lines.append("  # --- Umlaut-Hygiene (keine ASCII-Ersatzschreibung) ---")
    lines.append("  - id: r14-umlaut-hygiene")
    lines.append("    check_type: regex_absent")
    lines.append('    description: "Keine ASCII-Ersatzschreibung in typischen Wörtern (für/über/gemäß/große usw.)"')
    lines.append(f'    path: "{md_name}"')
    # \b funktioniert in Python-re mit Unicode; wir verwenden konkrete Wörter.
    lines.append(r"    pattern: '\b(fuer|ueber|gemaess|maessig|aenderung|beduerf|moeglich|natuerl|grosse|grossen|massgeblich|ausschliesslich|verstaerkt|hae(ufig|ngt|tte)|persoenlich|oeffentlich|aussergerichtlich|veroeffentlich)\b'")
    lines.append("")

    # --- Platzhalter-Disziplin ---
    lines.append("  # --- Platzhalter-Disziplin (keine erfundenen Namen) ---")
    lines.append("  - id: r15-keine-erfundenen-namen")
    lines.append("    check_type: regex_absent")
    lines.append('    description: "Keine erfundenen Klar-Namen wie Max/Erika Mustermann im Vorlagentext"')
    lines.append(f'    path: "{md_name}"')
    lines.append(r"    pattern: '\b(Max|Erika)\s+Mustermann\b'")
    lines.append("")

    # --- Typ-spezifische Checks ---
    if typ == "schriftsatz":
        lines.append("  # --- Schriftsatz-spezifisch ---")
        lines.append("  - id: r16-anrede-gericht-oder-behoerde")
        lines.append("    check_type: regex_match")
        lines.append('    description: "Anrede an Gericht/Behörde oder Aktenzeichen-Block vorhanden"')
        lines.append(f'    path: "{md_name}"')
        lines.append(r"    pattern: '(?i)(Gericht|Behörde|Geschäftszeichen|Aktenzeichen|Az\.|gez\.|Vollmacht)'")
        lines.append("")
        lines.append("  - id: r17-antrag-oder-begehren")
        lines.append("    check_type: regex_match")
        lines.append('    description: "Antrag/Begehren-Block ausgewiesen"')
        lines.append(f'    path: "{md_name}"')
        lines.append(r"    pattern: '(?i)(Anträge|Antrag|wird beantragt|beantrag(t|e|en)|erhebe.{0,40}Klage|Klage erhoben|lege.{0,40}(Einspruch|Widerspruch).{0,40}ein|erstatte.{0,40}(Strafanzeige|Anzeige)|Rüge|widerspreche|widerspruch|widerruf|wird gebeten|wird angezeigt|Begehren|fordern.{0,40}auf|Aufforderung|setze.{0,40}Frist|Zahlung.{0,40}Frist|melde.{0,40}Ansprüche|machen.{0,40}geltend|mache.{0,40}geltend|erkläre.{0,40}(die\s+)?Ausschlagung|schlage.{0,40}aus\b|ausschlage|weise.{0,40}zurück|verlange|fordere|abmahnen|Abmahnung|Schadensersatz)'")
        lines.append("")
    elif typ == "vertrag":
        lines.append("  # --- Vertrags-spezifisch ---")
        lines.append("  - id: r16-parteien-block")
        lines.append("    check_type: regex_match")
        lines.append('    description: "Parteien-Block (zwischen / und) vorhanden"')
        lines.append(f'    path: "{md_name}"')
        lines.append(r"    pattern: '(?i)(zwischen|Vertragsparteien|Parteien|Auftraggeber|Auftragnehmer|Verkäufer|Käufer|Vermieter|Mieter|Lizenzgeber|Lizenznehmer|Beteiligte|Arbeitgeber|Arbeitnehmer|Darlehensgeber|Darlehensnehmer|Erblasser|Sponsor|Verein|Berater|Spieler|Frachtführer|Absender|Empfänger|Gesellschafter|bevollmächtige|Vollmachtgeber|Bevollmächtigt|Mandant|Vollmacht)'")
        lines.append("")
        # r17 prüft, dass nummerierte Klauseln dezimal sind — also entweder
        # mindestens eine `### N.`-Überschrift, oder gar keine nummerierten
        # Klauseln (kurze einseitige Vereinbarungen, Variantenblöcke).
        # "Verboten" wird hingegen `### § N` durch check-gliederung gefangen.
        lines.append("  - id: r17-dezimal-oder-keine-klausel-nummerierung")
        lines.append("    check_type: regex_absent")
        lines.append('    description: "Keine Klauselüberschriften mit §-Nummer (§ als Normzitat ja, als Klausel-Nr. nein)"')
        lines.append(f'    path: "{md_name}"')
        lines.append(r"    pattern: '(?m)^#{2,4}\s+§\s*\d+\s'")
        lines.append("")
    else:
        lines.append("  # --- Sonstige Vorlage: Basisstruktur ---")
        lines.append("  - id: r16-abschnittsgliederung")
        lines.append("    check_type: regex_match")
        lines.append('    description: "Mindestens eine Markdown-H2-Überschrift vorhanden"')
        lines.append(f'    path: "{md_name}"')
        lines.append(r"    pattern: '(?ms)^##\s+.+$'")
        lines.append("")

    # --- Quellenhygiene ---
    lines.append("  # --- Quellenhygiene ---")
    lines.append("  - id: r80-rechtsprechungshygiene")
    lines.append("    check_type: regex_absent")
    lines.append('    description: "Keine missverständliche Rechtsprechungs-Verifikation ohne Direktnachweis"')
    lines.append(f'    path: "{md_name}"')
    lines.append(r"    pattern: '(Rechtsprechung\s*\(verifiziert\)|BGHZ\s+vorgesehen|Az\.\s+nach\s+offiziellem\s+Verzeichnis|keine\s+aktuellen\s+.+\s+verifiziert)'")
    lines.append("")

    # --- Anwaltliche Endprüfung (Pflicht) ---
    lines.append("  # --- Anwaltliche Endprüfung (human_review, blockiert Auto-Merge nicht) ---")
    lines.append("  - id: r90-az-live-verifiziert")
    lines.append("    check_type: human_review")
    lines.append('    description: "Alle Az. live in amtlichen Quellen verifiziert"')
    lines.append('    note: "Vor Mandatsverwendung bundesgerichtshof.de / bundesarbeitsgericht.de / bundesverfassungsgericht.de / bundesverwaltungsgericht.de / bundessozialgericht.de prüfen."')
    lines.append("")
    lines.append("  - id: r91-endpruefung-anwalt")
    lines.append("    check_type: human_review")
    lines.append('    description: "Endprüfung durch zugelassene Berufsträgerin"')
    lines.append('    note: "Vorlage ist Gerüst, kein fertiges Mandatsprodukt — vor Außenwirkung freigeben lassen."')
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="Überschreibt vorhandene rubric.yaml")
    ap.add_argument(
        "--slug",
        action="append",
        default=[],
        help="Bearbeitet nur den exakt bezeichneten Vorlagen-Slug; mehrfach verwendbar",
    )
    args = ap.parse_args()

    selected = set(args.slug)
    found: set[str] = set()
    created = 0
    kept = 0
    for bereich in THEMENORDNER:
        bdir = REPO / bereich
        if not bdir.is_dir():
            continue
        for sub in sorted(bdir.iterdir()):
            if not sub.is_dir():
                continue
            if selected and sub.name not in selected:
                continue
            md_p = _md_in(sub)
            odt_p = _odt_in(sub)
            if md_p is None:
                continue
            found.add(sub.name)
            rubric = sub / "rubric.yaml"
            if rubric.exists() and not args.force:
                kept += 1
                continue
            md_name = md_p.name
            odt_name = odt_p.name if odt_p is not None else md_p.with_suffix(".odt").name
            rubric.write_text(
                build_rubric(
                    bereich,
                    sub.name,
                    md_name,
                    odt_name,
                    markdown_titel(md_p, sub.name),
                ) + "\n",
                encoding="utf-8",
            )
            created += 1
    missing = sorted(selected - found)
    if missing:
        print(f"Nicht gefundene Slugs: {', '.join(missing)}", file=sys.stderr)
        return 1
    print(f"Rubrics erstellt: {created}; vorhanden gelassen: {kept}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

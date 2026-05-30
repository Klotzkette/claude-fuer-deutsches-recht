#!/usr/bin/env python3
"""
Fuegt in jeder Plugin-README, fuer die Testakten existieren, eine
Sektion '## Testakte(n)' direkt unter dem Direkt-Download-Block ein.
Bestehende, manuell formulierte Testakten-Sektionen werden NICHT
geloescht; stattdessen wird sie nach oben verschoben, indem ein
ein-/ausgegrenzter automatischer Block ergaenzt wird.

Idempotent: HTML-Kommentar-Marker BEGIN/END TESTAKTEN.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

BEGIN = "<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->"
END = "<!-- END TESTAKTEN-SECTION (auto-generated) -->"

REPO = Path(__file__).resolve().parent.parent

# Mapping Plugin -> Liste der Testakten-Ordnernamen
PLUGIN_TESTAKTEN: dict[str, list[str]] = {
    "arbeitszeugnis-analyse": ["arbeitszeugnis-analyse-bluehendes-leben"],
    "aussenwirtschaft-zoll-sanktionen": ["aussenwirtschaft-zoll-sanktionen-globalmaschinen"],
    "bav-strategie-konzern": ["bav-strategie-konzern-meissner-rheinwerk-ag"],
    "betreuungsrecht": [
        "betreuung-hildegard-sauer",
        "betreuung-schmalfeld-kontodaten-vertraege",
    ],
    "bgb-at-pruefer": ["bgb-at-altfraenkische-werkstatt"],
    "common-law-kompass": ["common-law-kompass-crossborder-contract"],
    "datenschutzrecht": ["datenschutz-us-transfer-cloudsuite-rheinmain"],
    "dsa-dma-digitalregulierung": ["dsa-dma-bayrische-baustube-meissner"],
    "einfache-leichte-sprache-jura": ["einfache-leichte-sprache-jura-mandantenbrief"],
    "energierecht": ["energierecht-stadtwerke-quartier"],
    "europarecht-kompass": ["europarecht-kompass-beihilfe-richtlinie"],
    "fachanwalt-verwaltungsrecht": ["bvg-widerspruchsstelle-abschleppen-mobg"],
    "fluggastrechte": ["fluggastrechte-familie-braeutigam"],
    "forderungsmanagement-klagewerkstatt": ["inkasso-zahlungsklage-modefuchs"],
    "geldwaeschepraevention-aml-kyc": ["geldwaesche-aml-kyc-musterholding"],
    "gesellschaftsgruender": ["gesellschaftsgruender-streit-roeschen-tech"],
    "gesellschaftsrecht-legal-english": ["gesellschaftsrecht-legal-english-frankfurt-startup"],
    "insolvenzforderungsanmeldungspruefung": [
        "insolvenzforderungsanmeldungspruefung-phoenix-solar"
    ],
    "insolvenzplan-starug-planwerkstatt": [
        "insolvenzplan-starug-planwerkstatt-metallbau-hansa"
    ],
    "insolvenzverwaltung": [
        "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren",
        "insolvenzverwaltung-nordlicht-handels-kiel",
    ],
    "jveg-kostenpruefer": ["jveg-zeugin-berger-lg-tuebingen"],
    "kanzlei-allgemein": ["kanzlei-allgemein-alltag"],
    "ki-richtlinie-kanzleien": ["ki-richtlinie-musterkanzlei"],
    "ki-vo-ai-act-pruefer": ["ki-vo-konformitaetsbescheinigung-bewerberpilot"],
    "krisenfrueherkennung-starug": ["krisenfrueherkennung-starug-vier-varianten"],
    "legistik-werkstatt": ["legistik-pflichtpostfach"],
    "lobbyregister-bundestag": [
        "lobbyregister-buergerinitiative-waldmoor",
        "lobbyregister-dublin-bank-frankfurt-branch",
        "lobbyregister-public-affairs-agentur-wasserstoff",
    ],
    "markenrecht-fashion-luxus": [
        "markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon"
    ],
    "meinungspruefer": ["meinungspruefer-grenzfaelle-alltag"],
    "nachbarschaftsstreit-pruefer": ["nachbarschaftsstreit-horrorfall-rosengarten"],
    "normenkontrolle-bauleitplanung": ["bebauungsplan-augsburg-bahnhofsareal"],
    "phishing-vorfall-pruefer": ["phishing-vorfall-mayer-sparkasse-berlin"],
    "arbeitsrecht": [
        "befristungskontrollklage-vogt-stadtwerke",
        "kuendigungsschutzklage-weber-techlogix",
    ],
    "schriftform-und-textform-bgb": [
        "schriftform-maklervertrag-muenchen-eheleute-haspelbeck",
        "schriftform-mietkuendigung-bielefeld-online-pferdedrescher",
    ],
    "selbstvertreter-amtsgericht": ["selbstvertreter-amtsgericht-kuechentisch-kaufpreis"],
    "selbstvertreter-sozialgericht": ["selbstvertreter-sozialgericht-heizkosten-eilantrag"],
    "fachanwalt-sozialrecht": ["sozialrecht-rollstuhl-tannenberg"],
    "steuerrecht-anwalt-und-berater": [
        "beispielakte-edelholz-berlin",
        "fortbestehensprognose-paragrafix-gmbh",
        "grosskanzlei-corporate-ma-datenraum",
        "grunderwerbsteuer-sharedeal-closing-waldkrone",
        "grundsteuer-rosenwinkel-bescheidkette",
    ],
    "strafbefehl-verteidiger": ["strafbefehl-ladendiebstahl-fahrerflucht"],
    "umweltrecht": ["umweltrecht-industrieanlage-genehmigung"],
    "urteilsbauer-relationsmacher": [
        "lumen-studios-insolvenz-strafverfahren",
        "solis-vision-x-smartglasses",
    ],
    "verkehr-infrastrukturrecht": ["verkehr-infrastrukturrecht-strassenbahn-ladezonen"],
    "verkehrsowi-verteidiger": ["verkehrsowi-rotlicht-tempo"],
    "verlagsredaktion": ["verlagsredaktion-morgenlage-fachverlag"],
    "vertragsausfueller": ["vertragsausfueller-bsag-kiosk-huckelriede"],
    "vertragsrecht": ["sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger"],
    "wandeldarlehen-lebenszyklus": ["wandeldarlehen-beispielcase"],
    "weg-hausverwaltung": ["weg-hausverwaltung-hohenzollernhof"],
    "zwangsverwaltung-zvg": [
        "zwangsverwaltung-friedrichshoefe-berlin",
        "zwangsverwaltung-zvg-mietshaus-parkstrasse",
        "zwangsverwaltung-zvg-versteigerung-eppendorf-altbau",
    ],
    "zwangsvollstreckung": ["vollstreckungsmappe-mueller-sparkasse-niederrhein"],
}


def get_testakte_title(akte_dir: Path) -> str:
    readme = akte_dir / "README.md"
    if not readme.is_file():
        return akte_dir.name
    first = readme.read_text(encoding="utf-8").splitlines()[0]
    # Strip leading '# ' and 'Akte:' / 'Akte ' Prefix
    title = re.sub(r"^#+\s*", "", first).strip()
    title = re.sub(r"^Akte\s*:?\s*", "", title, flags=re.IGNORECASE).strip()
    return title or akte_dir.name


def build_testakten_section(plugin: str, akten: list[str]) -> str:
    if not akten:
        return ""
    lines = [
        BEGIN,
        "",
        "## Testakte" + ("n" if len(akten) > 1 else ""),
        "",
    ]
    if len(akten) == 1:
        akte = akten[0]
        title = get_testakte_title(REPO / "testakten" / akte)
        lines.append(
            f"Zu diesem Plugin existiert eine vollständige Beispielakte: "
            f"**{title}** ([`testakten/{akte}/`](../testakten/{akte}/))."
        )
        lines.append("")
        lines.append(
            f"Direkt-Download als ZIP: "
            f"[testakte-{akte}.zip]("
            f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-{akte}.zip)"
        )
    else:
        lines.append(
            f"Zu diesem Plugin existieren {len(akten)} vollständige Beispielakten:"
        )
        lines.append("")
        lines.append("| Akte | Quelle | Direkt-Download |")
        lines.append("|---|---|---|")
        for a in akten:
            title = get_testakte_title(REPO / "testakten" / a)
            lines.append(
                f"| {title} | [`testakten/{a}/`](../testakten/{a}/) | "
                f"[testakte-{a}.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-{a}.zip) |"
            )
    lines.append("")
    lines.append("Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def find_insert_position(text: str) -> int:
    """Finde die Position direkt nach dem Direkt-Download-Block.
    
    Heuristik: Suche '## Direkt-Download', danach die naechste '## ' Section.
    Falls nicht gefunden, suche nach Plugin-Description (vor erstem '## Start' o.ae.).
    Falls auch das fehlt: nach H1-Titel + leerer Zeile + erstem Absatz.
    """
    # Variant 1: nach Direkt-Download-Sektion
    m = re.search(r"^## Direkt-Download\b.*?(?=^## )", text, re.MULTILINE | re.DOTALL)
    if m:
        return m.end()
    # Variant 2: vor erster '##'-Section
    m = re.search(r"^## ", text, re.MULTILINE)
    if m:
        return m.start()
    # Variant 3: ans Ende
    return len(text)


OLD_HEADERS = (
    "## Testakte",
    "## Testakten",
    "## Beispielakte",
    "## Beispielakten",
    "## Mit-Testakte",
    "## Mit Testakte",
)


def remove_old_manual_sections(text: str) -> str:
    """Entfernt manuell platzierte H2-Sektionen mit Testakten-Titel,
    AUSSER sie liegen innerhalb des Auto-Blocks BEGIN/END."""
    # Maskiere zuerst den Auto-Block, damit wir ihn nicht anfassen.
    auto_match = re.search(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        text,
        re.DOTALL,
    )
    placeholder = "<<<AUTO_BLOCK_PLACEHOLDER>>>"
    if auto_match:
        auto_content = auto_match.group(0)
        text = text.replace(auto_content, placeholder, 1)
    else:
        auto_content = None

    # Entferne alle alten Testakten-H2-Sektionen (bis zur naechsten H2).
    for header in OLD_HEADERS:
        pattern = (
            r"^" + re.escape(header) + r"\b.*?(?=^## |\Z)"
        )
        text = re.sub(pattern, "", text, flags=re.MULTILINE | re.DOTALL)

    if auto_content is not None:
        text = text.replace(placeholder, auto_content, 1)

    # Mehrfach-Leerzeilen auf max. 2 reduzieren
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def update_readme(readme: Path, plugin: str, akten: list[str]) -> bool:
    if not readme.is_file():
        return False
    original = readme.read_text(encoding="utf-8")
    block = build_testakten_section(plugin, akten)
    if not block:
        return False

    new = original
    # 1. Falls vorhandener Auto-Block existiert: entfernen
    if BEGIN in new and END in new:
        new = re.sub(
            re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*",
            "",
            new,
            count=1,
            flags=re.DOTALL,
        )

    # 2. Alte manuell platzierte Testakten-Sektionen entfernen
    new = remove_old_manual_sections(new)

    # 3. Block oben einfuegen (nach Direkt-Download)
    pos = find_insert_position(new)
    before = new[:pos].rstrip("\n") + "\n\n"
    after = new[pos:].lstrip("\n")
    new = before + block + "\n\n" + after

    if new == original:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    os.chdir(REPO)
    changed = 0
    skipped = 0
    for plugin, akten in sorted(PLUGIN_TESTAKTEN.items()):
        readme = REPO / plugin / "README.md"
        if not readme.is_file():
            print(f"  SKIP {plugin}: keine README.md")
            skipped += 1
            continue
        # Pruefe, ob alle Testakten-Ordner existieren
        existing = [a for a in akten if (REPO / "testakten" / a).is_dir()]
        if not existing:
            print(f"  SKIP {plugin}: keine Testakten-Ordner gefunden")
            skipped += 1
            continue
        if update_readme(readme, plugin, existing):
            changed += 1
            print(f"  UPD  {plugin}: {len(existing)} Akte(n)")
    print(f"\nFertig: {changed} READMEs aktualisiert, {skipped} uebersprungen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

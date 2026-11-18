#!/usr/bin/env python3
"""Erzeugt pro gerichtlichem Plugin einen Skill, der die finale Entscheidung
als versandfertigen Volltext erzeugt (Urteil, Beschluss, Strafbefehl, Anklageschrift etc.).

Neue Skills heißen entscheidung-volltext-erstellen. Bestehende aktive oder
konsolidierte Fassungen bleiben unverändert; insbesondere wird der frühere
Name 99-finale-entscheidung-volltext nicht umbenannt oder reaktiviert.

Inhalt richtet sich nach Spruchkoerper und Verfahrensart.
"""
from __future__ import annotations

if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)

import json
import pathlib
import re

from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN

ROOT = pathlib.Path(__file__).resolve().parent.parent

SKILL_NAME = "entscheidung-volltext-erstellen"
LEGACY_SKILL_NAME = "99-finale-entscheidung-volltext"

# (relative path, description fuer Frontmatter, Inhalt-Bausteine)
# Inhalt = (heading, entscheidungsart, normen, struktur_liste)
PLUGINS = {
    "gerichtsplugins/relationstechnik-zivilrecht": {
        "title": "Finale Entscheidung als Volltext (Urteil oder Beschluss Zivil)",
        "art": "Urteil oder Beschluss im Zivilprozess",
        "normen": "Paragrafen 313, 313a, 313b ZPO fuer den Urteilsaufbau; Paragrafen 91 ff. ZPO fuer Kostenentscheidung; Paragrafen 708, 709, 711 ZPO fuer vorlaeufige Vollstreckbarkeit.",
        "tenor_beispiel": "1. Die Beklagte wird verurteilt, an die Klaegerin EUR 12.500 nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit dem 1. Maerz 2024 zu zahlen.\n2. Im Uebrigen wird die Klage abgewiesen.\n3. Die Kosten des Rechtsstreits tragen die Klaegerin zu einem Drittel und die Beklagte zu zwei Dritteln.\n4. Das Urteil ist vorlaeufig vollstreckbar. Der jeweilige Vollstreckungsschuldner kann die Vollstreckung durch Sicherheitsleistung in Hoehe von 110 Prozent des aus dem Urteil vollstreckbaren Betrages abwenden, wenn nicht der jeweilige Vollstreckungsglaeubiger vor der Vollstreckung Sicherheit in gleicher Hoehe leistet.",
    },
    "gerichtsplugins/richter-amtsgericht-handelsregister": {
        "title": "Finale Entscheidung als Volltext (Beschluss Handelsregister)",
        "art": "Beschluss in einer Handelsregistersache",
        "normen": "Paragrafen 8 ff. HGB; Paragrafen 374 ff. FamFG (Registerverfahren); Paragrafen 38, 39 FamFG fuer Beschlussform und Begruendung.",
        "tenor_beispiel": "1. Die Eintragung wird antragsgemaess vorgenommen.\n2. Die Kosten der Eintragung traegt die Antragstellerin.",
    },
    "gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung": {
        "title": "Finale Entscheidung als Volltext (Beschluss Insolvenz oder Restrukturierung)",
        "art": "Beschluss in einer Insolvenz- oder Restrukturierungssache",
        "normen": "Paragrafen 27, 270, 270b InsO fuer Eroeffnung, Eigenverwaltung und Schutzschirm; Paragrafen 38, 39 FamFG fuer Beschlussform; Paragrafen 31 ff. StaRUG fuer Restrukturierungsplan.",
        "tenor_beispiel": "1. Ueber das Vermoegen der Schuldnerin wird das Insolvenzverfahren eroeffnet.\n2. Zum Insolvenzverwalter wird Rechtsanwalt N.N. bestellt.\n3. Die Insolvenzglaeubiger werden aufgefordert, ihre Forderungen bis zum [Datum] anzumelden.\n4. Erster Berichts- und Pruefungstermin wird auf den [Datum, Uhrzeit] anberaumt.",
    },
    "gerichtsplugins/richter-amtsgericht-straf": {
        "title": "Finale Entscheidung als Volltext (Urteil Strafrichter oder Strafbefehl)",
        "art": "Urteil des Strafrichters nach Paragraf 267 StPO oder Strafbefehl nach Paragraf 408 StPO",
        "normen": "Paragraf 267 StPO fuer Urteilsbegruendung; Paragrafen 407 ff. StPO fuer Strafbefehl; Paragraf 46 StGB fuer Strafzumessung.",
        "tenor_beispiel": "1. Der Angeklagte ist des Diebstahls schuldig.\n2. Er wird zu einer Geldstrafe von 60 Tagessaetzen zu je EUR 30 verurteilt.\n3. Der Angeklagte traegt die Kosten des Verfahrens und seine notwendigen Auslagen.",
    },
    "gerichtsplugins/richter-amtsgericht-zivil": {
        "title": "Finale Entscheidung als Volltext (Urteil Amtsgericht Zivil)",
        "art": "Urteil des Amtsgerichts in Zivilsachen",
        "normen": "Paragrafen 313, 313a, 313b ZPO; Paragrafen 91 ff. ZPO fuer Kosten; Paragrafen 708, 711 ZPO fuer vorlaeufige Vollstreckbarkeit beim Amtsgericht.",
        "tenor_beispiel": "1. Die Beklagte wird verurteilt, an den Klaeger EUR 3.200 nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit dem 15. April 2024 zu zahlen.\n2. Die Beklagte traegt die Kosten des Rechtsstreits.\n3. Das Urteil ist vorlaeufig vollstreckbar. Die Beklagte kann die Vollstreckung gegen Sicherheitsleistung in Hoehe von 110 Prozent des aus dem Urteil vollstreckbaren Betrages abwenden, wenn nicht der Klaeger vor der Vollstreckung Sicherheit in gleicher Hoehe leistet.",
    },
    "gerichtsplugins/richter-arbeitsgericht": {
        "title": "Finale Entscheidung als Volltext (Urteil Arbeitsgericht)",
        "art": "Urteil des Arbeitsgerichts",
        "normen": "Paragrafen 46 ff. ArbGG; Paragrafen 313, 313a ZPO entsprechend; Paragrafen 12, 12a ArbGG fuer Kosten erster Instanz.",
        "tenor_beispiel": "1. Es wird festgestellt, dass das Arbeitsverhaeltnis der Parteien durch die ordentliche Kuendigung der Beklagten vom 12. Maerz 2024 nicht aufgeloest worden ist.\n2. Die Beklagte wird verurteilt, den Klaeger zu unveraenderten Arbeitsbedingungen als Sachbearbeiter weiterzubeschaeftigen.\n3. Die Beklagte traegt die Kosten des Rechtsstreits.\n4. Der Streitwert wird auf EUR 9.000 festgesetzt.",
    },
    "gerichtsplugins/richter-bverfg-verfassungsbeschwerden": {
        "title": "Finale Entscheidung als Volltext (Beschluss oder Urteil BVerfG)",
        "art": "Entscheidung des Bundesverfassungsgerichts",
        "normen": "Paragrafen 90 ff. BVerfGG; Paragrafen 93a ff. BVerfGG fuer Annahme; Paragraf 95 BVerfGG fuer Tenor bei Erfolg.",
        "tenor_beispiel": "1. Das Urteil des [Gericht] vom [Datum] (Az.) verletzt die Beschwerdefuehrerin in ihrem Grundrecht aus Artikel [...] des Grundgesetzes.\n2. Es wird aufgehoben. Die Sache wird an das [Gericht] zurueckverwiesen.\n3. Die Bundesrepublik Deutschland hat der Beschwerdefuehrerin die notwendigen Auslagen zu erstatten.",
    },
    "gerichtsplugins/richter-familiengericht": {
        "title": "Finale Entscheidung als Volltext (Beschluss Familiengericht)",
        "art": "Beschluss in einer Familiensache nach FamFG",
        "normen": "Paragrafen 38, 39 FamFG fuer Beschlussform und Rechtsmittelbelehrung; Paragrafen 1565 ff. BGB bei Ehesache; Paragraf 1684 BGB bei Umgang; Paragraf 1626 BGB bei elterlicher Sorge.",
        "tenor_beispiel": "1. Die am [Datum] vor dem Standesbeamten in [Ort] geschlossene Ehe der Beteiligten wird geschieden.\n2. Die elterliche Sorge fuer das gemeinsame Kind [Name, Geburtsdatum] wird der Antragstellerin allein uebertragen.\n3. Die Kosten des Verfahrens werden gegeneinander aufgehoben.",
    },
    "gerichtsplugins/richter-finanzgericht": {
        "title": "Finale Entscheidung als Volltext (Urteil Finanzgericht)",
        "art": "Urteil des Finanzgerichts",
        "normen": "Paragrafen 100, 101 FGO; Paragrafen 105, 105a FGO fuer Urteilsaufbau; Paragraf 135 FGO fuer Kosten.",
        "tenor_beispiel": "1. Der Einkommensteuerbescheid des Beklagten fuer das Jahr 2022 vom [Datum] in Gestalt der Einspruchsentscheidung vom [Datum] wird dahingehend geaendert, dass die Einkommensteuer auf EUR [...] festgesetzt wird.\n2. Im Uebrigen wird die Klage abgewiesen.\n3. Die Kosten des Verfahrens tragen die Klaegerin zu einem Drittel und der Beklagte zu zwei Dritteln.\n4. Das Urteil ist hinsichtlich der Kosten vorlaeufig vollstreckbar.",
    },
    "gerichtsplugins/richter-landgericht-strafkammer": {
        "title": "Finale Entscheidung als Volltext (Urteil Strafkammer)",
        "art": "Urteil der grossen oder kleinen Strafkammer beim Landgericht",
        "normen": "Paragraf 267 StPO; Paragraf 46 StGB; Paragrafen 76 ff. StGB bei Massregeln; Paragrafen 73 ff. StGB bei Einziehung.",
        "tenor_beispiel": "1. Der Angeklagte ist des schweren Raubes in zwei Faellen, davon in einem Fall in Tateinheit mit gefaehrlicher Koerperverletzung, schuldig.\n2. Er wird zu einer Gesamtfreiheitsstrafe von fuenf Jahren und sechs Monaten verurteilt.\n3. Der Angeklagte traegt die Kosten des Verfahrens und seine notwendigen Auslagen.",
    },
    "gerichtsplugins/richter-landgericht-zivilkammer": {
        "title": "Finale Entscheidung als Volltext (Urteil Zivilkammer)",
        "art": "Urteil der Zivilkammer beim Landgericht",
        "normen": "Paragrafen 313, 313a ZPO; Paragrafen 91 ff. ZPO; Paragrafen 708, 709 ZPO fuer vorlaeufige Vollstreckbarkeit beim Landgericht.",
        "tenor_beispiel": "1. Die Beklagte wird verurteilt, an die Klaegerin EUR 85.000 nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.\n2. Im Uebrigen wird die Klage abgewiesen.\n3. Von den Kosten des Rechtsstreits tragen die Klaegerin 15 Prozent und die Beklagte 85 Prozent.\n4. Das Urteil ist gegen Sicherheitsleistung in Hoehe von 110 Prozent des jeweils zu vollstreckenden Betrages vorlaeufig vollstreckbar.",
    },
    "gerichtsplugins/richter-sozialgericht": {
        "title": "Finale Entscheidung als Volltext (Urteil Sozialgericht)",
        "art": "Urteil des Sozialgerichts",
        "normen": "Paragrafen 125, 136 SGG fuer Urteilsaufbau; Paragraf 193 SGG fuer Kostenentscheidung im sozialgerichtlichen Verfahren.",
        "tenor_beispiel": "1. Der Bescheid der Beklagten vom [Datum] in Gestalt des Widerspruchsbescheides vom [Datum] wird aufgehoben.\n2. Die Beklagte wird verurteilt, dem Klaeger ab dem [Datum] eine Rente wegen voller Erwerbsminderung zu gewaehren.\n3. Die Beklagte hat dem Klaeger die notwendigen aussergerichtlichen Kosten zu erstatten.",
    },
    "gerichtsplugins/richter-verwaltungsgericht": {
        "title": "Finale Entscheidung als Volltext (Urteil Verwaltungsgericht)",
        "art": "Urteil des Verwaltungsgerichts",
        "normen": "Paragrafen 113, 114 VwGO; Paragrafen 117, 118 VwGO fuer Urteilsaufbau; Paragraf 154 VwGO fuer Kosten; Paragraf 167 VwGO i.V.m. ZPO fuer Vollstreckbarkeit.",
        "tenor_beispiel": "1. Der Bescheid der Beklagten vom [Datum] wird aufgehoben.\n2. Die Beklagte wird verpflichtet, ueber den Antrag der Klaegerin unter Beachtung der Rechtsauffassung des Gerichts erneut zu entscheiden.\n3. Die Kosten des Verfahrens traegt die Beklagte.\n4. Das Urteil ist hinsichtlich der Kosten vorlaeufig vollstreckbar.",
    },
    "gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft": {
        "title": "Finale Entscheidung als Volltext (Anklageschrift, Strafbefehlsantrag oder Einstellungsverfuegung)",
        "art": "Abschlussverfuegung der Staatsanwaltschaft (Anklageschrift nach Paragraf 200 StPO, Strafbefehlsantrag nach Paragraf 407 StPO, Einstellungsverfuegung nach Paragrafen 170 Absatz 2, 153, 153a, 154, 154a StPO)",
        "normen": "Paragraf 200 StPO fuer Anklageschrift; Paragraf 407 StPO fuer Strafbefehlsantrag; Paragrafen 170, 153, 153a, 154, 154a StPO fuer Einstellungen; Paragrafen 1, 14 RiStBV.",
        "tenor_beispiel": "Anklageschrift: Der Angeschuldigte wird angeklagt, in [Ort] am [Datum] eine fremde bewegliche Sache, naemlich [...], einem anderen, naemlich [...], in der Absicht weggenommen zu haben, dieselbe sich rechtswidrig zuzueignen. - Vergehen, strafbar nach Paragraf 242 Absatz 1 StGB.",
    },
    "gerichtsplugins/staatsanwaltschaft-praxis-einstieg": {
        "title": "Finale Entscheidung als Volltext (Abschlussverfuegung Staatsanwaltschaft)",
        "art": "Abschlussverfuegung im Ermittlungsverfahren (Anklage, Strafbefehl oder Einstellung)",
        "normen": "Paragrafen 170, 153, 153a, 154, 154a StPO fuer Einstellungen; Paragraf 200 StPO fuer Anklageschrift; Paragraf 407 StPO fuer Strafbefehlsantrag.",
        "tenor_beispiel": "Verfuegung: Das Verfahren gegen [Name] wegen [Tatvorwurf] wird gemaess Paragraf 170 Absatz 2 StPO eingestellt, weil ein hinreichender Tatverdacht nicht besteht. Der Beschuldigte ist hiervon zu unterrichten. Der Anzeigeerstatter ist gemaess Paragraf 171 StPO zu bescheiden mit Hinweis auf das Beschwerderecht nach Paragraf 172 StPO.",
    },
    "urteilsbauer-relationsmacher": {
        "title": "Finale Entscheidung als Volltext (Urteil oder Beschluss universell)",
        "art": "Urteil oder Beschluss eines Zivil- oder Familienspruchkoerpers",
        "normen": "Paragrafen 313, 313a, 313b ZPO; Paragrafen 38, 39 FamFG; Paragrafen 91 ff. ZPO und Paragrafen 80 ff. FamFG fuer Kostenentscheidung.",
        "tenor_beispiel": "1. Die Beklagte wird verurteilt, an die Klaegerin EUR [Betrag] nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit [Datum] zu zahlen.\n2. Die Kosten des Rechtsstreits traegt die Beklagte.\n3. Das Urteil ist vorlaeufig vollstreckbar gegen Sicherheitsleistung in Hoehe von 110 Prozent des zu vollstreckenden Betrages.",
    },
    "schoeffen-handelsrichter-praxis": {
        "title": "Finale Entscheidung als Volltext (Beratungs-Votum mit Tenor-Vorschlag)",
        "art": "Beratungs-Votum eines Schoeffen oder Handelsrichters mit ausformuliertem Tenor-Vorschlag fuer die Kammerberatung",
        "normen": "Paragrafen 30, 33 GVG fuer Schoeffen; Paragrafen 105 ff. GVG fuer Handelsrichter; Paragrafen 263, 265 StPO fuer Strafsachen; Paragrafen 313 ZPO fuer Zivilsachen.",
        "tenor_beispiel": "Tenor-Vorschlag fuer die Beratung: Der Angeklagte ist des Betruges schuldig. Strafmass-Empfehlung: Geldstrafe von 90 Tagessaetzen zu je EUR 40. Begruendung fuer Schoeffen-Votum: Geringes Vorleben, vollstaendige Aufklaerungshilfe, Schaden ausgeglichen.",
    },
}


SKILL_TEMPLATE = """---
name: {skill_name}
description: {description}
---

# {title}

## Zweck

Dieser Skill erzeugt die finale Entscheidung des Spruchkoerpers nicht als blossen Vorschlag oder Votum, sondern als versandfertigen Volltext im richtigen Layout — so, wie er das Gericht verlassen wuerde. Die Entscheidung wird zur Unterschrift fertig gebaut: mit Rubrum, vollstaendigem Tenor, Tatbestand oder Sachverhalt, Entscheidungsgruenden, Nebenentscheidungen und Rechtsmittelbelehrung.

Gegenstand: {art}.

## Rechtlicher Rahmen

{normen}

## Eingangsvoraussetzungen

Vor der Volltext-Erstellung muessen die vorbereitenden Skills dieses Plugins durchlaufen sein. Insbesondere muessen vorliegen:

- Rubrum mit allen Parteien, Vertretern und Aktenzeichen;
- vollstaendig erfasster Sachverhalt und Streitstand;
- gepruefte Anspruchsgrundlagen oder Tatbestandsmerkmale mit Subsumtion;
- gewuerdigte Beweise oder Akten;
- Tenor-Skizze mit Entscheidungsformel zu Hauptsache, Kosten und vorlaeufiger Vollstreckbarkeit oder Rechtsmittelbelehrung.

Fehlt eines dieser Stuecke, weist der Skill darauf hin und unterbricht die Volltext-Erstellung, bevor er Phantasie produziert.

## Aufbau des Volltextes

### 1. Briefkopf und Rubrum

Gerichtsbezeichnung in der ersten Zeile (zum Beispiel „Amtsgericht Muenchen"), Aktenzeichen, Verkuendungsdatum, vollstaendiges Rubrum mit Parteien, Prozessbevollmaechtigten, Streitgegenstand und Spruchkoerper.

### 2. Tenor (Entscheidungsformel)

Der Tenor wird vollstaendig ausformuliert. Er ist die rechtskraftfaehige Anordnung. Beispiel fuer diesen Spruchkoerper:

{tenor_beispiel}

Der Tenor enthaelt zwingend: Hauptausspruch zur Sache, Kostenentscheidung, ggf. Aussprache zur vorlaeufigen Vollstreckbarkeit, ggf. Streitwertfestsetzung.

### 3. Tatbestand oder Sachverhalt

Knappe, sachlich-distanzierte Darstellung des unstreitigen Sachverhalts und des streitigen Parteivortrags. Bei Beschluessen entsprechend „Gruende I."; bei Strafurteilen die Feststellungen zum Tatgeschehen. Verwende den Imperfekt fuer Geschehensschilderung, das Praesens fuer Antrag und Verfahrensstand.

### 4. Entscheidungsgruende

Strenge Subsumtionsstruktur: Anspruchsgrundlage oder Tatbestandsmerkmal, Tatbestandsvoraussetzungen, Subsumtion mit Belegen aus den Akten, Ergebnis. Einreden und Einwendungen am Ende der jeweiligen Pruefungsebene. Bei Strafurteilen Beweiswuerdigung und Strafzumessung getrennt darstellen.

### 5. Nebenentscheidungen

Kosten, vorlaeufige Vollstreckbarkeit, Streitwertfestsetzung. Bei Familien- und Sozialsachen die jeweils einschlaegigen Kostenregeln.

### 6. Rechtsmittelbelehrung

Vollstaendige Belehrung ueber statthaftes Rechtsmittel, Frist, Form und Adressat. Niemals weglassen, niemals abkuerzen.

### 7. Unterschriftenzeile

Ort, Datum, Name(n) der entscheidenden Berufs- und Laienrichter mit Funktionsbezeichnung. Bei Verhinderung Vertretungsvermerk.

## Format und Stil

- Echte Umlaute (ae, oe, ue, ss als ae-Umschrift nur in Slugs; im Volltext durchgehend echte ae, oe, ue, ss).
- Sachlich, knapp, in deutscher Gerichtssprache.
- Generisches Maskulinum.
- Paragrafenzeichen ausgeschrieben als „Paragraf".
- Aktenzeichen Punkt- oder Schraegstrich-Stil, niemals Komma.
- Keine Doppelsterne fuer Fettschrift im Fliesstext.

## Ergebnis

Ein vollstaendiger, versandfertiger Entscheidungstext, der von Rubrum bis Unterschrift alles enthaelt. Der Spruchkoerper kann ihn unterschreiben — oder vor der Unterschrift redaktionell pruefen. Bei offenen Lueckenpunkten bleibt der Volltext stehen, die Luecken werden in eckigen Klammern markiert und am Ende in einer Luecken-Liste zusammengefasst.

## Eigenkontrolle

Bevor der Volltext freigegeben wird, durchlaeuft der Skill eine Eigenkontrolle:

1. Stimmt der Tenor mit den Entscheidungsgruenden ueberein?
2. Ist die Kostenentscheidung folgerichtig?
3. Ist die Rechtsmittelbelehrung vollstaendig und richtig?
4. Sind alle Parteibezeichnungen einheitlich?
5. Sind alle Daten, Aktenzeichen und Betraege widerspruchsfrei?
6. Sind alle Lueckenpunkte explizit markiert?

Erst nach bestandener Eigenkontrolle wird der Volltext als final ausgegeben.
"""


def make_description(title: str) -> str:
    desc = (
        f"Erzeugt die {title.lower()} als versandfertigen Volltext mit Rubrum, "
        "Tenor, Tatbestand, Entscheidungsgruenden, Nebenentscheidungen und "
        "Rechtsmittelbelehrung."
    )
    return desc[:300]


def safe_target(root: pathlib.Path, relative: str | pathlib.Path) -> pathlib.Path:
    relative = pathlib.Path(relative)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise ValueError(f"Ungültiger Zielpfad: {relative}")
    candidate = root
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            raise ValueError(f"Verlinkter Zielpfad: {relative}")
    if not candidate.resolve().is_relative_to(root):
        raise ValueError(f"Zielpfad außerhalb des Repositories: {relative}")
    return candidate


def generation_plan(root: pathlib.Path, plugins: dict) -> tuple[list[tuple[pathlib.Path, str]], list[str]]:
    """Prüft alle Ziele vor dem ersten Schreibzugriff; bewertet keine Fachtexte."""
    root = root.resolve()
    profile_path = safe_target(root, "scripts/data/werkstatt-visualisierung-profile.json")
    profiles = {}
    if profile_path.exists():
        data = json.loads(profile_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("plugins"), dict):
            raise ValueError("Ungültige bestehende Einstiegsprofile")
        profiles = data["plugins"]
    outputs, skipped = [], []
    targets = set()
    for rel, cfg in plugins.items():
        plugin_dir = safe_target(root, rel)
        if not plugin_dir.exists():
            skipped.append(f"MISSING {rel}")
            continue
        if not plugin_dir.is_dir():
            raise ValueError(f"Pluginziel ist kein Verzeichnis: {rel}")
        skills_dir = safe_target(root, pathlib.Path(rel) / "skills")
        if skills_dir.exists() and not skills_dir.is_dir():
            raise ValueError(f"Skillziel ist kein Verzeichnis: {rel}/skills")
        active = set()
        for path in skills_dir.glob("*/SKILL.md"):
            safe_target(root, path.relative_to(root))
            if not path.is_file():
                raise ValueError(f"Skill ist keine reguläre Datei: {path.relative_to(root)}")
            active.add(path.parent.name)
        profile = profiles.get(plugin_dir.name)
        if plugin_dir.name in profiles:
            entries = profile.get("entry_skills") if isinstance(profile, dict) else None
            if (not isinstance(entries, list) or not entries
                    or any(not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]{1,64}", name) for name in entries)
                    or len(entries) != len(set(entries))):
                raise ValueError(f"Ungültige deklarierte Einstiegsskills: {rel}")
            missing = set(entries) - active
            if missing:
                raise ValueError(f"Deklarierte Einstiegsskills fehlen: {rel}: {sorted(missing)}")
        existing = []
        for name in (SKILL_NAME, LEGACY_SKILL_NAME):
            directory = safe_target(root, pathlib.Path(rel) / "skills" / name)
            if directory.exists() and not directory.is_dir():
                raise ValueError(f"Skillziel ist kein Verzeichnis: {directory.relative_to(root)}")
            for filename in ("SKILL.md", "FACHINHALT.md"):
                candidate = safe_target(root, directory.relative_to(root) / filename)
                if candidate.exists():
                    if not candidate.is_file():
                        raise ValueError(f"Vorhandener Fachtext ist keine Datei: {candidate.relative_to(root)}")
                    existing.append(candidate)
        if existing:
            skipped.append(f"PRESERVED {rel}: vorhandener aktiver oder konsolidierter Entscheidungsskill")
            continue
        projected = len(active) + 1
        if projected > MAX_ACTIVE_SKILLS_PER_PLUGIN:
            raise ValueError(
                f"{rel}: {projected} aktive Skills einschließlich Einstiegsskills "
                f"überschreiten {MAX_ACTIVE_SKILLS_PER_PLUGIN}"
            )
        skill_file = skills_dir / SKILL_NAME / "SKILL.md"
        if skill_file in targets:
            raise ValueError(f"Doppeltes Ausgabeziel: {skill_file.relative_to(root)}")
        targets.add(skill_file)
        title = cfg["title"]
        desc = make_description(title)
        content = SKILL_TEMPLATE.format(
            skill_name=SKILL_NAME,
            description=desc,
            title=title,
            art=cfg["art"],
            normen=cfg["normen"],
            tenor_beispiel=cfg["tenor_beispiel"],
        )
        outputs.append((skill_file, content))
    return outputs, skipped


def main() -> int:
    try:
        outputs, skipped = generation_plan(ROOT, PLUGINS)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FEHLER: {exc}")
        return 1
    for message in skipped:
        print(message)
    for skill_file, content in outputs:
        skill_file.parent.mkdir(parents=True, exist_ok=True)
        # Selbst bei einer Änderung nach der Vorabprüfung keine Datei ersetzen.
        with skill_file.open("x", encoding="utf-8") as handle:
            handle.write(content)
        print(f"CREATED {skill_file.relative_to(ROOT.resolve())}")
    print(f"Fertig: created={len(outputs)} skipped={len(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

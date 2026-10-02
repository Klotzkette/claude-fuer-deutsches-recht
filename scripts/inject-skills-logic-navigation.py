#!/usr/bin/env python3
"""Fügt Plugin-READMEs eine thematische Skill-Navigation hinzu.

Der Block nutzt nur Skillordner-Namen. Skillinhalte, Skillnamen und die
bestehende alphabetische Komplettliste bleiben unverändert.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
BEGIN = "<!-- BEGIN SKILLS-LOGIC (auto-generated) -->"
END = "<!-- END SKILLS-LOGIC (auto-generated) -->"
SKILLS_OVERVIEW_BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="
DISPLAY_OMIT = ("chatgpt", "codex", "assistant", "perplexity", "openai")

GROUPS: list[tuple[str, tuple[str, ...]]] = [
    ("1. Einstieg und Fallrouting", ("kaltstart", "triage", "erstberatung", "ersttermin", "fallaufnahme", "intake", "eingang", "route", "routing", "navigator", "start", "mandat", "mandatsaufnahme", "orientierung", "zielbild")),
    ("2. Unterlagen, Sachverhalt und Quellen", ("akte", "akten", "dokument", "unterlage", "sachverhalt", "beweis", "beleg", "nachweis", "quelle", "recherche", "auskunft", "daten", "matrix", "konto", "verlauf", "luecke", "gutachten", "formular", "auszug")),
    ("3. Prüfung, Anspruch und Subsumtion", ("pruefung", "pruefer", "anspruch", "subsumtion", "tatbestand", "norm", "analyse", "bewertung", "haftung", "risiko", "status", "klassifikation", "check", "rentenbescheid", "altersrente", "erwerbsminderung", "erwerbsminderungsrente", "hinterbliebenenrente", "witwen", "waisen", "grundrente", "abzuege")),
    ("4. Gestaltung, Strategie und Verhandlung", ("gestaltung", "strategie", "vertrag", "klausel", "verhandlung", "vergleich", "plan", "planung", "struktur", "sanierung", "compliance", "konzept", "option", "varianten", "fahrplan", "nachzahlung", "freiwillige", "ausgleich", "abfindung", "betriebsrente", "private-rentenversicherung", "mehrsaeulen")),
    ("5. Verfahren, Behörde und Gericht", ("klage", "widerspruch", "einspruch", "bescheid", "gericht", "sozialgericht", "verfahren", "antrag", "schriftsatz", "urteil", "beschluss", "verfuegung", "vollstreckung", "frist", "register", "behoerde")),
    ("6. Ergebnis, Schreiben und Kommunikation", ("schreiben", "brief", "mandantenbrief", "memo", "vermerk", "entwurf", "bericht", "output", "kommunikation", "antwort", "stellungnahme", "redaktion", "praesentation", "sprechzettel")),
    ("7. Kontrolle, Qualität und Gegenprüfung", ("review", "red-team", "kontrolle", "gegen", "fehler", "plausibil", "validierung", "audit", "qualitaet", "korrektur")),
]

PRIORITY_GROUPS: list[tuple[str, tuple[str, ...]]] = [
    ("7. Kontrolle, Qualität und Gegenprüfung", ("red-team", "qualitygate", "qualitaetsgate")),
    ("6. Ergebnis, Schreiben und Kommunikation", ("versandmappe-endfertig",)),
    ("3. Prüfung, Anspruch und Subsumtion", ("rentenbescheid", "altersrente", "erwerbsminderung", "erwerbsminderungsrente", "hinterbliebene", "hinterbliebenenrente", "grundrente", "kvdr", "uebergangsgeld")),
    ("4. Gestaltung, Strategie und Verhandlung", ("hinzuverdienst", "teilrente", "weiterarbeit", "nachzahlung", "ausgleich", "betriebsrente", "riester", "basisrente", "mehrsaeulen")),
    ("2. Unterlagen, Sachverhalt und Quellen", ("kontenklaerung", "versicherungsverlauf", "auslandszeiten", "kindererziehungszeiten", "pflegezeiten")),
]

EXACT_GROUPS: dict[str, str] = {
    "belege-bis-zur-abrechnung": "1. Einstieg und Fallrouting",
    "belege-und-zahlungen-abgleichen": "2. Unterlagen, Sachverhalt und Quellen",
    "kosten-und-hausmeister-abgrenzen": "3. Prüfung, Anspruch und Subsumtion",
    "flaechen-und-umlageschluessel-pruefen": "3. Prüfung, Anspruch und Subsumtion",
    "oel-heizung-und-warmwasser-abrechnen": "3. Prüfung, Anspruch und Subsumtion",
    "co2-kosten-belegt-aufteilen": "3. Prüfung, Anspruch und Subsumtion",
    "weg-kosten-in-mietabrechnung-ueberleiten": "3. Prüfung, Anspruch und Subsumtion",
    "grundsteuer-und-energie-sonderkosten-trennen": "3. Prüfung, Anspruch und Subsumtion",
    "abrechnung-vorauszahlungen-und-fristen-abschliessen": "6. Ergebnis, Schreiben und Kommunikation",
    "einwendungen-korrektur-und-belegeinsicht-bearbeiten": "7. Kontrolle, Qualität und Gegenprüfung",
    "bescheide-und-fristen-ordnen": "1. Einstieg und Fallrouting",
    "grundstueck-und-flaechen-abgleichen": "2. Unterlagen, Sachverhalt und Quellen",
    "landesmodell-und-stichtag-bestimmen": "1. Einstieg und Fallrouting",
    "grundsteuerwert-nachrechnen": "3. Prüfung, Anspruch und Subsumtion",
    "niedrigeren-grundstueckswert-nachweisen": "3. Prüfung, Anspruch und Subsumtion",
    "messbetrag-und-hebesatz-pruefen": "3. Prüfung, Anspruch und Subsumtion",
    "einspruch-und-aenderungsantrag-entwerfen": "5. Verfahren, Behörde und Gericht",
    "zahlung-und-eilrechtsschutz-sichern": "5. Verfahren, Behörde und Gericht",
    "klage-und-musterverfahren-einordnen": "5. Verfahren, Behörde und Gericht",
    "folgebescheid-und-mandantenbericht-abschliessen": "6. Ergebnis, Schreiben und Kommunikation",
    "schadenfall-aufnehmen": "1. Einstieg und Fallrouting",
    "versicherung-einschalten": "1. Einstieg und Fallrouting",
    "schadenpositionen-pruefen": "3. Prüfung, Anspruch und Subsumtion",
    "abschleppschaden-pruefen": "3. Prüfung, Anspruch und Subsumtion",
    "haftpflichtschaden-regulieren": "4. Gestaltung, Strategie und Verhandlung",
    "regulierung-korrespondieren": "6. Ergebnis, Schreiben und Kommunikation",
    "juristischer-argumentationskern": "3. Prüfung, Anspruch und Subsumtion",
    "einfuehrung-pruefauftrag": "1. Einstieg und Fallrouting",
    "rollen-und-modus-wahl": "1. Einstieg und Fallrouting",
    "klagestrategie-und-vollstreckung": "5. Verfahren, Behörde und Gericht",
    "einfuehrung-mandantenanliegen": "1. Einstieg und Fallrouting",
    "rollen-und-harness-wahl": "1. Einstieg und Fallrouting",
    "zeugnisart-einfach": "1. Einstieg und Fallrouting",
    "zeugnisart-qualifiziert": "1. Einstieg und Fallrouting",
    "zeugnisart-zwischenzeugnis": "1. Einstieg und Fallrouting",
    "zeugnisart-ausbildungszeugnis-16-bbig": "1. Einstieg und Fallrouting",
    "zeugnisart-praktikum": "1. Einstieg und Fallrouting",
    "stammdaten-erhebung": "2. Unterlagen, Sachverhalt und Quellen",
    "taetigkeitsbeschreibung-erheben": "2. Unterlagen, Sachverhalt und Quellen",
    "besondere-leistungen-projekte": "2. Unterlagen, Sachverhalt und Quellen",
    "mehrere-positionen-im-zeugnis": "2. Unterlagen, Sachverhalt und Quellen",
    "langzeit-arbeitsverhaeltnis": "2. Unterlagen, Sachverhalt und Quellen",
    "bag-leitentscheidungen-beweislast": "3. Prüfung, Anspruch und Subsumtion",
    "bag-leitentscheidungen-notenstufen": "3. Prüfung, Anspruch und Subsumtion",
    "rechtlicher-anker-109-gewo": "3. Prüfung, Anspruch und Subsumtion",
    "notenwahl-modus": "3. Prüfung, Anspruch und Subsumtion",
    "note-1-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-2-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-3-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-4-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-5-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "belastbarkeit-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "engagement-motivation-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "teamarbeit-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "fuehrungskraft-bewertung": "3. Prüfung, Anspruch und Subsumtion",
    "verhalten-vorgesetzte-kollegen-kunden": "3. Prüfung, Anspruch und Subsumtion",
    "compliance-integritaet-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "frequenzadverbien-katalog": "4. Gestaltung, Strategie und Verhandlung",
    "steigerungsadverbien-katalog": "4. Gestaltung, Strategie und Verhandlung",
    "beendigungsgrund-formulieren": "4. Gestaltung, Strategie und Verhandlung",
    "schlussformel-baukasten": "4. Gestaltung, Strategie und Verhandlung",
    "schlussformel-notenwirkung": "4. Gestaltung, Strategie und Verhandlung",
    "revision-und-aenderungswuensche": "5. Verfahren, Behörde und Gericht",
    "auslassungen-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "geheimcodes-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "drift-und-schaufenster-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "zeugnisklarheit-objektiver-empfaengerhorizont": "7. Kontrolle, Qualität und Gegenprüfung",
    "wohlwollensgrundsatz-und-wahrheit": "7. Kontrolle, Qualität und Gegenprüfung",
    "kopfdaten-und-aussere-form": "7. Kontrolle, Qualität und Gegenprüfung",
    "teilzeit-elternzeit-darstellung": "7. Kontrolle, Qualität und Gegenprüfung",
    "versandmappe-endfertigen": "1. Einstieg und Fallrouting",
    "ordneraufnahme-und-produktionsmatrix": "2. Unterlagen, Sachverhalt und Quellen",
    "hauptdokument-pdf-endfertigen": "2. Unterlagen, Sachverhalt und Quellen",
    "anlagen-konvertieren-und-sichtpruefen": "2. Unterlagen, Sachverhalt und Quellen",
    "anlagen-nummerieren-und-stempeln": "4. Gestaltung, Strategie und Verhandlung",
    "signaturweg-und-absender-pruefen": "5. Verfahren, Behörde und Gericht",
    "stoerung-und-nachreichung-dokumentieren": "5. Verfahren, Behörde und Gericht",
    "dateinamen-und-paketgrenzen-pruefen": "7. Kontrolle, Qualität und Gegenprüfung",
    "versandfreigabe-und-eingang-sichern": "7. Kontrolle, Qualität und Gegenprüfung",
}

PLUGIN_GROUPS = {
    "sektorenvergabe-workflow": [
        ("1. Hauptskill für den laufenden Auftrag", ["sektorenvergabe-steuern"]),
        ("2. Vergabeunterlagen in fünf Schritten", ["auftrag-und-sektorenbezug-klaeren", "reinigungsleistung-und-mengen-bestimmen", "eignung-wertung-und-vertrag-gestalten", "unterlagen-und-preisblatt-abgleichen", "bekanntmachung-und-fristen-vorbereiten"]),
        ("3. Verfahrensführung in fünf Schritten", ["teilnahmeantraege-und-angebote-pruefen", "bieterfragen-ruegen-und-aenderungen-bearbeiten", "verhandeln-und-angebote-werten", "zuschlag-und-stillhaltefrist-sichern", "nachpruefung-und-verfahrensfortsetzung-begleiten"]),
    ],
    "berliner-schulrecht-eltern-schueler": [
        ("1. Anliegen und Bildungsweg", ["berlin-bildungsmandat-steuern", "berlin-kita-gutschein-betreuung", "berlin-ganztag-ergaenzende-foerderung"]),
        ("2. Schulplatz und Übergänge", ["berlin-schulaufnahme-grundschule", "berlin-sekundarstufe-schulplatz-wechsel"]),
        ("3. Schulalltag und individuelle Förderung", ["berlin-leistungsbewertung-versetzung", "berlin-inklusion-nachteilsausgleich", "berlin-schulpflicht-fehlzeiten-befreiung"]),
        ("4. Konflikte und Rechtsschutz", ["berlin-erziehung-ordnungsmassnahmen", "berlin-beteiligung-schuldaten-konflikte", "berlin-rechtsbehelfe-eilrechtsschutz"]),
    ],
    "berliner-hochschulrecht-professoren": [
        ("1. Vorgang und Berufung", ["professur-mandat-zum-ergebnis-fuehren", "professur-berufung-und-konkurrenz", "professur-rufverhandlung-und-zusagen"]),
        ("2. Amt und Hochschulalltag", ["professur-status-und-dienstpflichten", "professur-lehre-deputat-und-pruefung", "professur-gremien-und-befangenheit"]),
        ("3. Forschung und Nachwuchs", ["professur-forschungsfreiheit-und-ausstattung", "professur-drittmittel-daten-ip-ethik", "professur-promotion-und-nachwuchs", "professur-nebentaetigkeit-und-publikation"]),
        ("4. Verständigung und Rechtsschutz", ["professur-konflikt-verfahren-und-eilrechtsschutz"]),
    ],
    'transparenzregister-assistent': [('1. Auftrag und Berechtigung', ['hauptproblem-unklare-kontrolle-loesen', 'registervorgang-aufnehmen']), ('2. Kontrolle und Sonderstrukturen', ['kontrollketten-und-stimmrechte-pruefen', 'treuhand-stiftung-und-trust-pruefen', 'pep-und-mittelherkunft-trennen']), ('3. Meldung und Aufklärung', ['erstmeldung-vollstaendig-vorbereiten', 'aenderung-und-berichtigung-ordnen', 'unstimmigkeiten-pruefen-und-beantworten', 'registerkorrespondenz-und-anhoerung']), ('4. Einsicht und Portalvollzug', ['einsicht-und-datenschutz-steuern', 'portalbedienung-und-nachhalten'])],
    'handelsregister-assistent': [('1. Recherche und Registerlage', ['hauptproblem-registervorgang-zum-vollzug', 'registerrecherche-und-auszuege', 'registerdaten-und-datenschutz']), ('2. Vertretung und Gesellschafterliste', ['vertretung-und-registerpublizitaet', 'auslandsvertretung-und-urkunden', 'gesellschafterliste-erstellen-und-abgleichen']), ('3. Anmeldungen und Strukturänderungen', ['gruendung-satzung-und-kapital-anmelden', 'organwechsel-und-prokura', 'sitz-zweigniederlassung-und-strukturwechsel']), ('4. Schriftverkehr und Vollzug', ['registerschriftverkehr-und-zwischenverfuegung', 'einreichung-und-vollzug-nachhalten'])],
    'grundbuchamt-assistent': [('1. Auftrag und Einsicht', ['grundbuchvorgang-zum-ergebnis-fuehren', 'grundbucheinsicht-begruenden', 'grundbuch-und-bezugsurkunden-lesen']), ('2. Nachweise und Erwerb', ['grundbuchantrag-und-form-pruefen', 'vertretung-und-urkundenkette-pruefen', 'eigentum-vormerkung-und-vollzug', 'erbfolge-und-grundbuchberichtigung']), ('3. Grundpfandrechte und Brief', ['grundschuld-rang-und-loeschung', 'grundschuldbrief-aufgebot-und-wiederfund']), ('4. Verfahren und Vollzug', ['zwischenverfuegung-und-beschwerde', 'vollzug-kosten-und-zugriff-dokumentieren'])],
    'markenamt-assistent': [('1. Auftrag und Recherche', ['marke-sichern-trotz-offener-rechte', 'markenauftrag-und-fristen-klaeren', 'markenrecherche-und-treffer-pruefen']), ('2. Schutzumfang und Anmeldung', ['markenverzeichnis-und-klassen-formulieren', 'dpma-marke-anmelden', 'euipo-unionsmarke-anmelden']), ('3. Beanstandung und Streit', ['markenbeanstandung-beantworten', 'markenwiderspruch-fuehren', 'markenverfall-und-nichtigkeit-pruefen']), ('4. Rechte und Bestand', ['markeninhaber-und-lizenzen-umschreiben', 'markenportal-und-bestand-nachhalten'])],
    "insolvenzforderungen-checker": [
        ("1. Eingang und Belegabgleich", ["forderungen-pruefen-und-tabelle-vorbereiten", "anmeldung-und-glaeubiger-klaeren", "forderungsgrund-und-belege-abgleichen", "zahlungen-zinsen-und-kosten-pruefen"]),
        ("2. Forderungsart und Rang", ["insolvenz-und-masseforderungen-trennen", "sicherheiten-und-ausfall-pruefen", "nachrang-und-gesellschafterdarlehen-pruefen"]),
        ("3. Termin und Widerspruch", ["verspaetete-anmeldungen-und-termine-bearbeiten", "bestreiten-titel-und-feststellung-bearbeiten"]),
        ("4. Schreiben und Tabellenübergabe", ["glaeubigerbriefe-und-nachforderungen-erstellen", "tabelle-und-elektronische-uebergabe-vorbereiten"]),
    ],
    "eigenbedarfskuendigungschecker": [
        ("1. Auftrag und Wohnbedarf", ["eigenbedarf-pruefen-und-klaeren", "vermieter-und-bedarfsperson-pruefen", "nutzungswunsch-und-alternativen-pruefen"]),
        ("2. Erklärung und Kündigungsschutz", ["kuendigung-form-und-zugang-pruefen", "kuendigungsfristen-und-vertragsschutz-pruefen", "umwandlung-und-sperrfrist-pruefen"]),
        ("3. Härte und Fortsetzung", ["haerte-und-ersatzwohnung-pruefen", "widerspruch-und-fortsetzung-formulieren"]),
        ("4. Änderungen und Verständigung", ["bedarfswegfall-und-nachweise-pruefen", "einigung-und-raeumungsuebergang-gestalten"]),
    ],
    "mietchecker": [
        ("1. Wohnung und Prüfweg", ["miete-pruefen-und-klaeren", "mietrecht-vor-ort-bestimmen", "wohnflaeche-und-mietbestandteile-klaeren"]),
        ("2. Örtliche Vergleichsmiete", ["berliner-vergleichsmiete-berechnen", "regensburger-vergleichsmiete-berechnen"]),
        ("3. Zulässigkeit und Anpassung", ["neuvereinbarte-miete-pruefen", "mieterhoehung-und-kappungsgrenze-pruefen", "staffel-index-und-sonderfaelle-trennen"]),
        ("4. Abgleich und Verständigung", ["mietvergleich-mit-belegen-abgleichen", "miete-einvernehmlich-richtigstellen"]),
    ],
    "antidiskriminierung-agg": [
        ("1. Vorgang und Frist", ["agg-fall-zum-schreiben-fuehren", "agg-fristen-und-ansprueche-sichern"]),
        ("2. Lebensbereich und Beweise", ["bewerbung-und-befoerderung-pruefen", "entgelt-und-arbeitsbedingungen-vergleichen", "wohnraum-und-dienstleistungen-pruefen", "indizien-und-vergleichsfaelle-pruefen"]),
        ("3. Anhörung und Rechtfertigung", ["beschwerde-und-schutzmassnahmen-bearbeiten", "ungleichbehandlung-und-rechtfertigung-pruefen"]),
        ("4. Durchsetzung und Abhilfe", ["agg-klage-und-erwiderung-entwerfen", "agg-abhilfe-und-vereinbarung-gestalten"]),
    ],
    "jura-in-einfacher-sprache": [
        ("1. Übertragen und verstehen", ["juristischen-text-uebertragen", "juristischen-text-erklaeren"]),
        ("2. Schreiben und antworten", ["schreiben-in-einfacher-sprache-erstellen", "auf-juristische-post-antworten"]),
        ("3. Bedeutung und Verständlichkeit prüfen", ["bedeutung-und-verstaendlichkeit-pruefen"]),
    ],
    "sozialrecht-fuer-laien": [
        ("1. Anliegen und Frist klären", ["meinen-sozialfall-starten", "bescheid-und-frist-pruefen"]),
        ("2. Antrag und Tatsachen vorbereiten", ["antrag-und-nachweise-vorbereiten", "kranken-und-pflegekasse-antworten", "akte-einsehen-und-tatsachen-klaeren"]),
        ("3. Widerspruch und Gericht", ["widerspruch-schreiben", "eilantrag-vorbereiten", "klage-beim-sozialgericht-vorbereiten", "gerichtspost-und-termin-bearbeiten"]),
        ("4. Vor dem Absenden prüfen", ["schreiben-und-verstaendlichkeit-pruefen"]),
    ],
    "pflegerecht-sgb-xi": [
        ("1. Pflegefall übernehmen", ["pflegefall-bearbeiten"]),
        ("2. Pflegegrad und häusliche Versorgung", ["pflegegrad-gutachten-pruefen", "haeusliche-pflegeleistungen-planen", "verhinderungs-kurzzeitpflege-abrechnen", "pflegehilfsmittel-wohnumfeld-beantragen"]),
        ("3. Heim, Pflegeperson und Beiträge", ["pflegeheimkosten-zuschlag-pruefen", "pflegepersonen-absicherung-pruefen", "pflegeversicherung-beitraege-klaeren"]),
        ("4. Verfahren und Einrichtungen", ["pflegebescheid-rechtsbehelf-erstellen", "pflegeeinrichtungen-verguetung-qualitaet-pruefen"]),
    ],
    "sozialversicherungspflicht-pruefer": [
        ("1. Gesamte Prüfung", ["sozialversicherungspflicht-pruefen"]),
        ("2. Status und Tätigkeiten", ["beschaeftigung-oder-selbststaendigkeit", "geschaeftsfuehrer-und-gesellschaftermacht", "vorstaende-aufsichtsraete-und-organe", "lehrtaetigkeit-und-uebergang-127", "freie-mitarbeit-und-projektarbeit"]),
        ("3. Versicherung und Befreiung", ["selbststaendige-rentenversicherung", "versorgungswerk-und-befreiung", "versicherungszweige-und-beitraege"]),
        ("4. Verfahren und Schreiben", ["statusverfahren-und-betriebspruefung"]),
    ],
    "gmbh-gesellschafterversammlung": [
        ("1. Gesamten Vorgang führen", ["gesellschafterversammlung-organisieren"]),
        ("2. Regeln und Einladung", ["unterlagen-und-versammlungsregeln-pruefen", "einladung-und-tagesordnung-erstellen"]),
        ("3. Laufende Änderungen", ["nachtraege-und-minderheitsverlangen-bearbeiten"]),
        ("4. Versammlung und Abschluss", ["stimmen-und-beschluesse-dokumentieren", "protokoll-und-vollzug-vorbereiten"]),
    ],
    "juristische-praesentationen": [
        ("1. Vortrag übernehmen", ["praesentation-starten"]),
        ("2. Anlass und Publikum", ["urteil-als-vortrag-aufbereiten", "fachvortrag-fuer-juristen", "rechtsfragen-fuer-laien-erklaeren", "gerichtspraesentation-vorbereiten", "jour-fixe-und-entscheidungsvorlage"]),
        ("3. Inhalt sichtbar und sprechbar machen", ["fallverlauf-und-belege-visualisieren", "folien-und-sprechtext-ausarbeiten"]),
        ("4. Datei und Vortragsprobe", ["powerpoint-aus-vorlage-erstellen", "praesentation-pruefen-und-proben"]),
        ("5. Bonus nur auf ausdrücklichen Wunsch", ["serioes-animieren", "jugendgerecht-umformulieren"]),
    ],
    "startup-gruender": [
        ("1. Einstieg und Gründungsentscheidung", ["gruendung-begleiten", "gruender-und-rollen-klaeren", "rechtsform-und-kapital-waehlen"]),
        ("2. Beteiligung und Gründungsverträge", ["cap-table-planen", "satzung-entwerfen", "gesellschaftervereinbarung-entwerfen", "vesting-und-ausstieg-regeln", "gruender-ip-sichern"]),
        ("3. Geschäftsführung und Kontrolle", ["geschaeftsfuehrung-regeln", "geschaeftsfuehrer-status-pruefen", "beirat-einrichten", "mehrheiten-und-minderheiten-sichern"]),
        ("4. Konto Anmeldung und Vollzug", ["bankkonto-und-geldwaesche-vorbereiten", "gruendung-und-register-vollziehen", "produktstart-und-anmeldungen-planen"]),
        ("5. Finanzierung und weitere Kapitalmaßnahmen", ["finanzierungsrunde-vorbereiten", "kapitalerhoehung-und-bezugsrechte-pruefen"]),
        ("6. Abgleich und Endfassungen", ["gruendungsunterlagen-abgleichen"]),
    ],
    "schriftsatz-versandwerkstatt": [
        ("1. Auftrag, Fassung und Anlagenzuordnung", [
            "versandmappe-endfertigen", "ordneraufnahme-und-produktionsmatrix",
        ]),
        ("2. PDF-Produktion und Anlagenkennzeichnung", [
            "hauptdokument-pdf-endfertigen", "anlagen-konvertieren-und-sichtpruefen",
            "anlagen-nummerieren-und-stempeln",
        ]),
        ("3. Dateinamen, Grenzen und Signaturroute", [
            "dateinamen-und-paketgrenzen-pruefen", "signaturweg-und-absender-pruefen",
        ]),
        ("4. Freigabe und Eingangskontrolle", ["versandfreigabe-und-eingang-sichern"]),
        ("5. Formhindernisse und Störungen", [
            "juristischer-argumentationskern", "stoerung-und-nachreichung-dokumentieren",
        ]),
    ],
    "bauwirtschaft": [
        ("1. Projektführung und Entscheidungen", [
            "bauprojekt-starten-und-arbeitsstand-fortfuehren",
            "projektziele-und-entscheidungsrahmen-festlegen",
            "projektbericht-und-entscheidungsvorlage-erstellen",
        ]),
        ("2. HOAI-Leistungsphasen für Gebäude und Innenräume", [
            "hoai-1-grundlagen-und-planungsauftrag-klaeren",
            "hoai-2-vorplanung-und-varianten-entwickeln",
            "hoai-3-entwurf-und-kostenberechnung-abstimmen",
            "hoai-4-genehmigungsplanung-und-nachforderungen-bearbeiten",
            "hoai-5-ausfuehrungsplanung-und-details-koordinieren",
            "hoai-6-leistungsverzeichnis-und-vergabeunterlagen-erstellen",
            "hoai-7-angebote-werten-und-vergabe-vorbereiten",
            "hoai-8-bauueberwachung-und-dokumentation-fuehren",
            "hoai-9-objektbetreuung-und-maengelverfolgung-organisieren",
        ]),
        ("3. Phasenübergreifende Planung und Bauablauf", [
            "hoai-phasen-und-planstaende-abgleichen",
            "bauablauf-und-terminplan-fortschreiben",
        ]),
        ("4. Vergabe und Angebote", [
            "vergabe-und-losbildung-vorbereiten",
            "leistungsverzeichnis-erstellen-und-pruefen",
            "bauangebote-werten-und-vergabevorschlag-erstellen",
            "bieterfragen-und-ruegen-bearbeiten",
        ]),
        ("5. Bauvertrag und Ausführung", [
            "bauvertrag-und-schnittstellen-ausformulieren",
            "bautagebuch-und-aufmass-fuehren",
            "behinderung-und-bauzeitfolgen-dokumentieren",
            "nachtraege-pruefen-und-vereinbaren",
        ]),
        ("6. Kaufmännische Steuerung", [
            "baubudget-und-kostenprognose-fortschreiben",
            "projektliquiditaet-und-zahlungsplan-erstellen",
            "baurechnungen-pruefen-und-zahlung-vorbereiten",
            "baubuchhaltung-und-belege-abgleichen",
        ]),
        ("7. Abnahme, Sicherheiten und Übergabe", [
            "maengel-und-abnahme-bearbeiten",
            "nachunternehmer-und-sicherheiten-steuern",
            "uebergabe-und-gewaehrleistung-organisieren",
        ]),
    ],
}


def natural_key(text: str) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", text.lower())]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    return REPO / source.removeprefix("./")


def skill_slugs(directory: Path) -> list[str]:
    skills = directory / "skills"
    if not skills.is_dir():
        return []
    return sorted([d.name for d in skills.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()], key=natural_key)


def classify(slug: str) -> str:
    lower = slug.lower()
    if lower in EXACT_GROUPS:
        return EXACT_GROUPS[lower]
    for label, needles in PRIORITY_GROUPS:
        if any(needle in lower for needle in needles):
            return label
    for label, needles in GROUPS:
        if any(needle in lower for needle in needles):
            return label
    return "8. Spezialmodule und Schnittstellen"


def markdown_download_url(repo_path: str) -> str:
    return DOWNLOAD_BASE + quote(repo_path, safe="/")


def format_slugs(slugs: list[str], source: str, limit: int = 18) -> str:
    displayable = [slug for slug in slugs if not any(part in slug.lower() for part in DISPLAY_OMIT)]
    if not displayable:
        return "Siehe alphabetische Komplettliste unten."
    shown = displayable[:limit]
    text = ", ".join(
        f"[`{slug}`]({markdown_download_url(f'{source}/skills/{slug}/SKILL.md')})"
        for slug in shown
    )
    rest = len(displayable) - len(shown)
    if rest > 0:
        text += f", ... plus {rest} weitere"
    return text


def build_block(slugs: list[str], source: str) -> str:
    if len(slugs) < 4:
        return ""
    grouped: dict[str, list[str]] = {}
    for slug in slugs:
        grouped.setdefault(classify(slug), []).append(slug)
    labels = [label for label, _ in GROUPS] + ["8. Spezialmodule und Schnittstellen"]
    if source in PLUGIN_GROUPS:
        assignments = PLUGIN_GROUPS[source]
        assigned = [slug for _, items in assignments for slug in items]
        if len(assigned) != len(set(assigned)) or set(assigned) != set(slugs):
            raise ValueError(f"{source}: Fachnavigation muss jeden Skill genau einmal zuordnen")
        grouped = dict(assignments)
        labels = list(grouped)
    lines = [
        BEGIN,
        "",
        "## Orientierung nach Arbeitslogik",
        "",
        "Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.",
        "",
        "English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.",
        "",
        "| Arbeitsphase | Typische Skills |",
        "| --- | --- |",
    ]
    for label in labels:
        items = grouped.get(label)
        if items:
            lines.append(f"| {label} | {format_slugs(items, source)} |")
    lines.extend(["", END])
    return "\n".join(lines)


def inject(readme: Path, block: str) -> bool:
    if not block or not readme.is_file():
        return False
    original = readme.read_text(encoding="utf-8")
    text = original
    if BEGIN in text and END in text:
        start = text.find(BEGIN)
        end = text.find(END, start) + len(END)
        text = text[:start] + block + text[end:]
    elif SKILLS_OVERVIEW_BEGIN in text:
        text = text.replace(SKILLS_OVERVIEW_BEGIN, block + "\n\n" + SKILLS_OVERVIEW_BEGIN, 1)
    else:
        sep = "" if text.endswith("\n\n") else ("\n" if text.endswith("\n") else "\n\n")
        text = text + sep + block + "\n"
    from readme_decimal_headings import normalize_decimal_headings
    text = normalize_decimal_headings(text)
    if text == original:
        return False
    readme.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    changed = 0
    total = 0
    for plugin in market["plugins"]:
        directory = plugin_dir(plugin)
        source = directory.relative_to(REPO).as_posix()
        slugs = skill_slugs(directory)
        if not slugs:
            continue
        total += 1
        if inject(directory / "README.md", build_block(slugs, source)):
            changed += 1
            print(f"  UPD {plugin['name']}", flush=True)
    print(f"Fertig: {changed}/{total} READMEs mit Arbeitslogik-Navigation aktualisiert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

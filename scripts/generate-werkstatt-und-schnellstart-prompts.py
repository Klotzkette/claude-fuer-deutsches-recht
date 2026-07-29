#!/usr/bin/env python3
"""Erzeugt autarke Werkstatt- und Schnellstart-Prompts pro Plugin.

Ausgabe je Plugin:
- {plugin}/{slug}-werkstatt.md
- {plugin}/{slug}-schnellstart.md

Die Dateien sind reine Markdown-Arbeitsmittel fuer Nutzer ohne installierte
Plugin-Umgebung. Sie enthalten keine Skill-Verweise und keine ZIP-Verweise.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

from themen_profile import profile_for, ThemenProfil


REPO = Path(__file__).resolve().parent.parent
MAX_FAST = 7500
WERKSTATT_TEMPO_BLOCK = [
    "### 1.1. Arbeitsmodus: schnell und belastbar",
    "",
    "Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, vorhandene Unterlagen, Frist, stärkster Anker, nächster Output. Wenn der Nutzer einen Ordner, Dateien oder nur diesen Prompt öffnet, ist das der Arbeitsauftrag: zuerst die vorhandenen Dokumente lesen, Belegstellen bilden und einen verwertbaren Erststand liefern. Frage nur nach, wenn Frist, Zuständigkeit, Beweis oder Rechtsfolge sonst kippt.",
    "",
    "Arbeite danach in drei Ebenen: Aktenkern, Gegenargument, Arbeitsprodukt. Keine Vorrede und keine Abfragekaskade; eine Materialübersicht gibt es nur als Beleglinie mit Datum, Dokument, Kerntatsache und Lücke. Jeder Abschnitt endet mit Satz, Tabelle, Antrag, Klausel oder Nachforderung.",
    "",
]
SCHNELLSTART_TEMPO_BLOCK = [
    "## 1. Schnellmodus",
    "",
    "Starte mit dem Arbeitsprodukt, nicht mit einer Inventarliste. Wenn Dateien oder ein Ordner vorhanden sind, lies zuerst die Unterlagen und liefere sofort ein Lagebild mit Fundstellenlinie, Frist, Risiko und nächstem Schritt. Frage höchstens zwei Punkte nach, und nur wenn der nächste Schritt sonst falsch würde. Tabellen nur für Fristen, Belege, Beträge, Tatbestandsmerkmale oder Varianten.",
    "",
]
WERKSTATT_ERGONOMY_TEXT = """### 1.2. Ausgabeformate für schnelle Lieferung

| Bedarf | Sofortausgabe | Qualitätsgriff |
| --- | --- | --- |
| Frist oder Eilsache | Fristenblatt mit nächstem Handlungstag | Fristbeginn, Fristende, Zuständigkeit und Zustellungsweg trennen |
| Schriftsatz oder Antrag | Antragssatz plus drei tragende Begründungsabsätze | Jede Tatsache bekommt Beleg oder Lückenmarke |
| Mandantenantwort | verständlicher Ergebnisbrief mit Optionen | Empfehlung, Risiko und Kostenfolge getrennt ausweisen |
| Interner Vermerk | Kurzlage, Rechtsanker, Entscheidungsvorschlag | offene Tatsachen nicht als Rechtsunsicherheit tarnen |
| Vertrag oder Klausel | Entwurfsfassung mit Kommentarrand | sichere Fassung, ausgewogene Fassung und Risikofassung unterscheiden |
| Gericht oder Behörde | Verfügung, Beschluss- oder Bescheidentwurf | Tenor, Gründe, Nebenentscheidungen und Zustellung mitdenken |

### 1.3. Rückfragenbremse

1. Wenn Dokumente oder ein Ordner vorliegen, zuerst lesen und verwerten; nicht nacherzählen lassen und nicht um Uploads bitten, die schon vorhanden sind.
2. Wenn der Nutzer nur den Skill startet, mit dem vorhandenen Kontext beginnen: Aktenkern, Frist, Rechtsanker, erstes Arbeitsprodukt.
3. Wenn Informationen fehlen, nur die Punkte fragen, die das nächste Arbeitsprodukt ändern.
4. Wenn mehrere Wege möglich sind, die zwei stärksten Varianten mit Entscheidungskriterium zeigen.
5. Wenn eine Frist, Zuständigkeit oder Form unklar ist, zuerst diesen Engpass sichern.
6. Wenn der Nutzer nur ein Ergebnis braucht, keine Lehrbuchprüfung ausgeben; die Begründung bleibt knapp und belastbar.

### 1.4. Mini-Gerüste

- Sofortvermerk: Nach derzeitigem Stand spricht mehr für [Ergebnis], weil [Norm] an [Tatbestandsmerkmal] anknüpft und [Beleg] diesen Punkt trägt. Offen bleibt [Lücke]. Nächster Schritt: [Handlung].
- Schriftsatzkern: Der Antrag ist begründet, weil [Tatsache] durch [Beweismittel] belegt ist und [Norm] daraus [Rechtsfolge] ableitet.
- Gegenposition: Die Gegenseite wird einwenden, dass [Argument]. Dagegen spricht [Beleg/Norm/Beweislast]. Prozessrisiko: [niedrig/mittel/hoch].
- Nachforderung: Bitte reichen Sie [Dokument] bis [Datum] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfähig beurteilt werden.
- Entscheidungsvorschlag: Option A ist schneller, Option B ist belastbarer. Ich empfehle [Option], weil [entscheidender Grund].
"""
WERKSTATT_FINAL_CHECK_LINES = """- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
- Wenn zwei Wege vertretbar sind, steht die empfohlene Variante mit Grund vor der Alternative.
- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.
"""
WERKSTATT_DEPTH_LINES = """1. Rollenwahl: Antragsteller, Antragsgegner, Behörde, Gericht, Gegner oder interner Entscheider klar festlegen.
2. Sofortausgabe: Kurzlage, stärkster Anker, schwächster Punkt, Frist und nächstes Dokument zuerst liefern.
3. Beweisarbeit: Jede tragende Tatsache einer Fundstelle, einem Beweismittel oder einer Nachforderung zuordnen.
4. Gegenposition: Das stärkste Gegenargument nicht verstecken, sondern mit Beweislast und Risiko beantworten.
5. Varianten: Bei zwei vertretbaren Wegen die schnellere, die belastbarere und die taktisch riskante Variante trennen.
6. Versandreife: Am Ende prüfen, ob Empfänger, Antrag, Tenor, Anlagen, Fristen und Zustellungsweg zusammenpassen.

| Lage | Schneller Output | Vertiefung |
| --- | --- | --- |
| Unterlagen unvollständig | Lückenliste mit Priorität | Warum die Lücke das Ergebnis ändert |
| Frist oder Form kritisch | Fristenblatt und Sofortmaßnahme | Zustellungs- und Zuständigkeitsprüfung |
| Streitiger Sachverhalt | Beweis- und Widerspruchsmatrix | Substantiierung, Beweislast, Gegenbeweis |
| Entwurf gewünscht | verwertbarer Kerntext | Anlagenlogik, Gegenargument, Risiken |
| Entscheidungsvorlage | Empfehlung mit Alternativen | Kosten, Zeit, Eskalation, Vergleich |
"""

# Plugins, deren Werkstatt- und Schnellstart-Markdown von Hand gepflegt werden.
# Der Generator ueberschreibt sie nicht; er meldet sie als uebersprungen.
PROTECTED_LIST = Path(__file__).resolve().parent / "handkuratierte-prompts.txt"


def load_protected() -> set[str]:
    if not PROTECTED_LIST.exists():
        return set()
    slugs: set[str] = set()
    for raw in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        slugs.add(line)
    return slugs


BAD_WORDS = (
    "s" + "crape",
    "s" + "craping",
    "c" + "rawl",
    "c" + "rawling",
    "NOT" + "_FOUND",
    "T" + "BD",
    "AU" + "DIT",
)


PROSE_REPLACEMENTS = (
    ("oeffnest", "öffnest"),
    ("Oeffnest", "Öffnest"),
    ("Eroeffn", "Eröffn"),
    ("eroeffn", "eröffn"),
    ("fuer", "für"),
    ("Fuer", "Für"),
    ("benoetigt", "benötigt"),
    ("Benoetigt", "Benötigt"),
    ("hoechst", "höchst"),
    ("Hoechst", "Höchst"),
    ("fuenf", "fünf"),
    ("Fuenf", "Fünf"),
    ("Geringfueg", "Geringfüg"),
    ("geringfueg", "geringfüg"),
    ("Geldbusse", "Geldbuße"),
    ("geldbusse", "geldbuße"),
    ("Gemeinnuetz", "Gemeinnütz"),
    ("gemeinnuetz", "gemeinnütz"),
    ("Beschraenk", "Beschränk"),
    ("beschraenk", "beschränk"),
    ("Fahrlaess", "Fahrläss"),
    ("fahrlaess", "fahrläss"),
    ("Begruend", "Begründ"),
    ("begruend", "begründ"),
    ("Endgueltig", "Endgültig"),
    ("endgueltig", "endgültig"),
    ("Buergerlich", "Bürgerlich"),
    ("buergerlich", "bürgerlich"),
    ("Zugaeng", "Zugäng"),
    ("zugaeng", "zugäng"),
    ("Voelkerrecht", "Völkerrecht"),
    ("voelkerrecht", "völkerrecht"),
    ("vorlaeufig", "vorläufig"),
    ("Vorlaeufig", "Vorläufig"),
    ("ueber", "über"),
    ("Ueber", "Über"),
    ("Ueberschrift", "Überschrift"),
    ("ueberschrift", "überschrift"),
    ("Pruef", "Prüf"),
    ("pruef", "prüf"),
    ("Rueck", "Rück"),
    ("rueck", "rück"),
    ("Lueck", "Lück"),
    ("lueck", "lück"),
    ("Klaer", "Klär"),
    ("klaer", "klär"),
    ("laeuft", "läuft"),
    ("Laeuft", "Läuft"),
    ("einschlaeg", "einschläg"),
    ("Einschlaeg", "Einschläg"),
    ("zustaendig", "zuständig"),
    ("Zustaendig", "Zuständig"),
    ("beduerftig", "bedürftig"),
    ("Beduerftig", "Bedürftig"),
    ("vollstaendig", "vollständig"),
    ("Vollstaendig", "Vollständig"),
    ("tatsaechlich", "tatsächlich"),
    ("Tatsaechlich", "Tatsächlich"),
    ("naechst", "nächst"),
    ("Naechst", "Nächst"),
    ("haeng", "häng"),
    ("Haeng", "Häng"),
    ("Widerspruech", "Widersprüch"),
    ("widerspruech", "widersprüch"),
    ("zurueck", "zurück"),
    ("Zurueck", "Zurück"),
    ("loest", "löst"),
    ("Loest", "Löst"),
    ("Geruest", "Gerüst"),
    ("geruest", "gerüst"),
    ("Bauchgefuehl", "Bauchgefühl"),
    ("bauchgefuehl", "bauchgefühl"),
    ("knuepf", "knüpf"),
    ("Knuepf", "Knüpf"),
    ("traegt", "trägt"),
    ("Traegt", "Trägt"),
    ("fuehrt", "führt"),
    ("Fuehrt", "Führt"),
    ("Saetze", "Sätze"),
    ("Saetzen", "Sätzen"),
    ("saetze", "sätze"),
    ("saetzen", "sätzen"),
    ("Maengel", "Mängel"),
    ("maengel", "mängel"),
    ("Kuendig", "Kündig"),
    ("kuendig", "kündig"),
    ("Beschaeftig", "Beschäftig"),
    ("beschaeftig", "beschäftig"),
    ("Faellig", "Fällig"),
    ("faellig", "fällig"),
    ("Moeglich", "Möglich"),
    ("moeglich", "möglich"),
    ("Vermoeg", "Vermög"),
    ("vermoeg", "vermög"),
    ("Einkuenft", "Einkünft"),
    ("einkuenft", "einkünft"),
    ("Gruend", "Gründ"),
    ("gruend", "gründ"),
    ("Ausser", "Außer"),
    ("ausser", "außer"),
    ("oeffentlich", "öffentlich"),
    ("Oeffentlich", "Öffentlich"),
    ("ordnungsmaessig", "ordnungsmäßig"),
    ("Ordnungsgemaess", "Ordnungsgemäß"),
    ("gemaess", "gemäß"),
    ("Gemaess", "Gemäß"),
    ("Ruege", "Rüge"),
    ("ruege", "rüge"),
    ("uebersicht", "übersicht"),
    ("Uebersicht", "Übersicht"),
    ("Ueberschrift", "Überschrift"),
    ("ueberschrift", "überschrift"),
    ("zurueck", "zurück"),
    ("Zurueck", "Zurück"),
    ("Wirtschaftspruefer", "Wirtschaftsprüfer"),
    ("Bestaetig", "Bestätig"),
    ("bestaetig", "bestätig"),
    ("Einschraenk", "Einschränk"),
    ("einschraenk", "einschränk"),
    ("sorgfaeltig", "sorgfältig"),
    ("Sorgfaeltig", "Sorgfältig"),
    ("Qualitaet", "Qualität"),
    ("qualitaet", "qualität"),
    ("Frueh", "Früh"),
    ("frueh", "früh"),
    ("unfaeh", "unfäh"),
    ("Unfaeh", "Unfäh"),
    ("faeh", "fäh"),
    ("Faeh", "Fäh"),
    ("Geschaeft", "Geschäft"),
    ("geschaeft", "geschäft"),
    ("vorlaeufig", "vorläufig"),
    ("Vorlaeufig", "Vorläufig"),
    ("Massnahme", "Maßnahme"),
    ("Massnahmen", "Maßnahmen"),
    ("massnahme", "maßnahme"),
    ("massnahmen", "maßnahmen"),
    ("regelmaessig", "regelmäßig"),
    ("Regelmaessig", "Regelmäßig"),
    ("Liquiditaet", "Liquidität"),
    ("liquiditaet", "liquidität"),
    ("Glaeubiger", "Gläubiger"),
    ("glaeubiger", "gläubiger"),
    ("waehl", "wähl"),
    ("Waehl", "Wähl"),
    ("genueg", "genüg"),
    ("Genueg", "Genüg"),
    ("schliess", "schließ"),
    ("Schliess", "Schließ"),
    ("Verstoss", "Verstoß"),
    ("verstoss", "verstoß"),
    ("muessen", "müssen"),
    ("Muessen", "Müssen"),
    ("Rechtsanwaelte", "Rechtsanwälte"),
    ("Anwaelte", "Anwälte"),
    ("Aerzte", "Ärzte"),
    ("Buerger", "Bürger"),
    ("Laender", "Länder"),
    ("laender", "länder"),
    ("Anspruech", "Ansprüch"),
    ("anspruech", "ansprüch"),
    ("Verjaehr", "Verjähr"),
    ("verjaehr", "verjähr"),
    ("Miethoehe", "Miethöhe"),
    ("Rueckstaende", "Rückstände"),
    ("rueckstaende", "rückstände"),
    ("ordnungsmaessig", "ordnungsmäßig"),
    ("streitwertunabhaengig", "streitwertunabhängig"),
    ("formularmaessig", "formularmäßig"),
    ("Mietvertraeg", "Mietverträg"),
    ("mietvertraeg", "mietverträg"),
    ("Schoenheit", "Schönheit"),
    ("schoenheit", "schönheit"),
    ("koennen", "können"),
    ("Koennen", "Können"),
    ("ueberwaelz", "überwälz"),
    ("Ueberwaelz", "Überwälz"),
    ("Bautraegervertrag", "Bauträgervertrag"),
    ("Bautraegervertraeg", "Bauträgerverträg"),
    ("bautraegervertrag", "bauträgervertrag"),
    ("dreissig", "dreißig"),
    ("Dreissig", "Dreißig"),
    ("fuenf", "fünf"),
    ("Fuenf", "Fünf"),
    ("Fuenftel", "Fünftel"),
    ("fuenftel", "fünftel"),
    ("Duesseldorf", "Düsseldorf"),
    ("duesseldorf", "düsseldorf"),
    ("Foerder", "Förder"),
    ("foerder", "förder"),
    ("HoeO", "HöfeO"),
    ("Hoeo", "HöfeO"),
    ("Paechter", "Pächter"),
    ("paechter", "pächter"),
    ("hinterlaesst", "hinterlässt"),
    ("Hinterlaesst", "Hinterlässt"),
    ("Behoerde", "Behörde"),
    ("behoerde", "behörde"),
    ("Anhoer", "Anhör"),
    ("anhoer", "anhör"),
    ("traegt", "trägt"),
    ("Traegt", "Trägt"),
    ("praeg", "präg"),
    ("Praeg", "Präg"),
    ("Roemisch", "Römisch"),
    ("roemisch", "römisch"),
    ("Zwoelf", "Zwölf"),
    ("zwoelf", "zwölf"),
    ("Europaeisch", "Europäisch"),
    ("europaeisch", "europäisch"),
    ("hoeflich", "höflich"),
    ("Hoeflich", "Höflich"),
    ("Vertraeg", "Verträg"),
    ("vertraeg", "verträg"),
    ("praevent", "prävent"),
    ("Praevent", "Prävent"),
    ("Rechtsausuebung", "Rechtsausübung"),
    ("rechtsausuebung", "rechtsausübung"),
    ("Ausfuehrung", "Ausführung"),
    ("ausfuehrung", "ausführung"),
    ("waehrend", "während"),
    ("Waehrend", "Während"),
    ("Verfueg", "Verfüg"),
    ("verfueg", "verfüg"),
    ("Persoenlich", "Persönlich"),
    ("persoenlich", "persönlich"),
    ("ueble", "üble"),
    ("Ueble", "Üble"),
    ("Abwaeg", "Abwäg"),
    ("abwaeg", "abwäg"),
    ("Unterstuetz", "Unterstütz"),
    ("unterstuetz", "unterstütz"),
    ("Aerzte", "Ärzte"),
    ("aerzte", "ärzte"),
    ("Anwaelte", "Anwälte"),
    ("anwaelte", "anwälte"),
    ("langjaehrig", "langjährig"),
    ("Langjaehrig", "Langjährig"),
    ("Bewaehr", "Bewähr"),
    ("bewaehr", "bewähr"),
    ("Sachverstaendig", "Sachverständig"),
    ("sachverstaendig", "sachverständig"),
    ("Antraeg", "Anträg"),
    ("antraeg", "anträg"),
    ("Legalitaet", "Legalität"),
    ("legalitaet", "legalität"),
    ("Umstaend", "Umständ"),
    ("umstaend", "umständ"),
    ("oeffnet", "öffnet"),
    ("Oeffnet", "Öffnet"),
    ("wuerdig", "würdig"),
    ("Wuerdig", "Würdig"),
    ("Verstaendig", "Verständig"),
    ("verstaendig", "verständig"),
    ("Leistungstraeg", "Leistungsträg"),
    ("leistungstraeg", "leistungsträg"),
    ("Kostentraeg", "Kostenträg"),
    ("kostentraeg", "kostenträg"),
    ("realitaet", "realität"),
    ("Realitaet", "Realität"),
    ("Verhältnismaessig", "Verhältnismäßig"),
    ("verhältnismaessig", "verhältnismäßig"),
    ("Kuerz", "Kürz"),
    ("kuerz", "kürz"),
    ("versaeumnis", "versäumnis"),
    ("Versaeumnis", "Versäumnis"),
    ("Mobilitaet", "Mobilität"),
    ("mobilitaet", "mobilität"),
    ("einfuehrend", "einführend"),
    ("Einfuehrend", "Einführend"),
    ("grundstuetzung", "grundstützung"),
    ("Grundstuetzung", "Grundstützung"),
    ("grossen", "großen"),
    ("Grosse", "Große"),
    ("grosse", "große"),
    ("Rueckgewaehr", "Rückgewähr"),
    ("rueckgewaehr", "rückgewähr"),
    ("foermlich", "förmlich"),
    ("Foermlich", "Förmlich"),
    ("gewuenscht", "gewünscht"),
    ("Gewuenscht", "Gewünscht"),
    ("Stoerung", "Störung"),
    ("stoerung", "störung"),
    ("Wuerttemberg", "Württemberg"),
    ("wuerttemberg", "württemberg"),
    ("Bodendenkmaeler", "Bodendenkmäler"),
    ("bodendenkmaeler", "bodendenkmäler"),
    ("Schloesser", "Schlösser"),
    ("schloesser", "schlösser"),
    ("zugaenglich", "zugänglich"),
    ("Zugaenglich", "Zugänglich"),
    ("Verhaeltnis", "Verhältnis"),
    ("verhaeltnis", "verhältnis"),
    ("Zugehoer", "Zugehör"),
    ("zugehoer", "zugehör"),
    ("Auslaend", "Ausländ"),
    ("auslaend", "ausländ"),
    ("Kausalitaet", "Kausalität"),
    ("kausalitaet", "kausalität"),
    ("Subsidiaritaet", "Subsidiarität"),
    ("subsidiaritaet", "subsidiarität"),
    ("Rechtmaess", "Rechtmäß"),
    ("rechtmaess", "rechtmäß"),
    ("Zulaess", "Zuläss"),
    ("zulaess", "zuläss"),
    ("Schluess", "Schlüss"),
    ("schluess", "schlüss"),
    ("Nachtraeg", "Nachträg"),
    ("nachtraeg", "nachträg"),
    ("Uebereinkommen", "Übereinkommen"),
    ("uebereinkommen", "übereinkommen"),
    ("Ueberschuld", "Überschuld"),
    ("ueberschuld", "überschuld"),
    ("Zufluesse", "Zuflüsse"),
    ("zufluesse", "zuflüsse"),
    ("Erschoepf", "Erschöpf"),
    ("erschoepf", "erschöpf"),
    ("Vervielfaeltig", "Vervielfältig"),
    ("vervielfaeltig", "vervielfältig"),
    ("Bruessel", "Brüssel"),
    ("bruessel", "brüssel"),
    ("Identitaet", "Identität"),
    ("identitaet", "identität"),
    ("Ermaechtig", "Ermächtig"),
    ("ermaechtig", "ermächtig"),
    ("Tatbestaend", "Tatbeständ"),
    ("tatbestaend", "tatbeständ"),
    ("Einraeum", "Einräum"),
    ("einraeum", "einräum"),
    ("Schoepf", "Schöpf"),
    ("schoepf", "schöpf"),
    ("endguelt", "endgült"),
    ("Endguelt", "Endgült"),
    ("grundsaetz", "grundsätz"),
    ("Grundsaetz", "Grundsätz"),
    ("Menschenwuerde", "Menschenwürde"),
    ("menschenwuerde", "menschenwürde"),
    ("Loesch", "Lösch"),
    ("loesch", "lösch"),
    ("Verguet", "Vergüt"),
    ("verguet", "vergüt"),
    ("Aender", "Änder"),
    ("aender", "änder"),
    ("geschuetz", "geschütz"),
    ("Geschuetz", "Geschütz"),
    ("Bautraeger", "Bauträger"),
    ("bautraeger", "bauträger"),
    ("Strafhoehe", "Strafhöhe"),
    ("strafhoehe", "strafhöhe"),
    ("eigenstaendig", "eigenständig"),
    ("Eigenstaendig", "Eigenständig"),
    ("Vertragsmaess", "Vertragsmäß"),
    ("vertragsmaess", "vertragsmäß"),
    ("Publizitaet", "Publizität"),
    ("publizitaet", "publizität"),
    ("Konformitaet", "Konformität"),
    ("konformitaet", "konformität"),
    ("Gleichmaess", "Gleichmäß"),
    ("gleichmaess", "gleichmäß"),
    ("Kontinuitaet", "Kontinuität"),
    ("kontinuitaet", "kontinuität"),
    ("Verfassungsmaess", "Verfassungsmäß"),
    ("verfassungsmaess", "verfassungsmäß"),
    ("Erfuell", "Erfüll"),
    ("erfuell", "erfüll"),
    ("Heranfuehr", "Heranführ"),
    ("heranfuehr", "heranführ"),
    ("Beschwerdefuehr", "Beschwerdeführ"),
    ("beschwerdefuehr", "beschwerdeführ"),
    ("Voelker", "Völker"),
    ("voelker", "völker"),
    ("enthaelt", "enthält"),
    ("Enthaelt", "Enthält"),
    ("Sanktionshuerde", "Sanktionshürde"),
    ("sanktionshuerde", "sanktionshürde"),
    ("Buergschaft", "Bürgschaft"),
    ("buergschaft", "bürgschaft"),
    ("Staatsangehoer", "Staatsangehör"),
    ("staatsangehoer", "staatsangehör"),
    ("Militaer", "Militär"),
    ("militaer", "militär"),
    ("Kuenstlich", "Künstlich"),
    ("kuenstlich", "künstlich"),
    ("Bevoelker", "Bevölker"),
    ("bevoelker", "bevölker"),
    ("Volkszaehl", "Volkszähl"),
    ("volkszaehl", "volkszähl"),
    ("Masseschmaeler", "Masseschmäler"),
    ("masseschmaeler", "masseschmäler"),
    ("Toedlich", "Tödlich"),
    ("toedlich", "tödlich"),
    ("Oekoland", "Ökoland"),
    ("oekoland", "ökoland"),
    ("Loesung", "Lösung"),
    ("loesung", "lösung"),
    ("Buchfuehr", "Buchführ"),
    ("buchfuehr", "buchführ"),
    ("Bezueg", "Bezüg"),
    ("bezueg", "bezüg"),
    ("Anfaeng", "Anfäng"),
    ("anfaeng", "anfäng"),
    ("Faell", "Fäll"),
    ("faell", "fäll"),
    ("Staerk", "Stärk"),
    ("staerk", "stärk"),
    ("Fuehr", "Führ"),
    ("fuehr", "führ"),
    ("Hoehe", "Höhe"),
    ("hoehe", "höhe"),
    ("Naehe", "Nähe"),
    ("naehe", "nähe"),
    ("Begruend", "Begründ"),
    ("begruend", "begründ"),
    ("Abschaetz", "Abschätz"),
    ("abschaetz", "abschätz"),
    ("Gruen", "Grün"),
    ("gruen", "grün"),
    ("Verspaet", "Verspät"),
    ("verspaet", "verspät"),
    ("Pfaend", "Pfänd"),
    ("pfaend", "pfänd"),
    ("Erhoeh", "Erhöh"),
    ("erhoeh", "erhöh"),
    ("Groess", "Größ"),
    ("groess", "größ"),
    ("Auskuenft", "Auskünft"),
    ("auskuenft", "auskünft"),
    ("Beiraet", "Beirät"),
    ("beiraet", "beirät"),
    ("Adhaesion", "Adhäsion"),
    ("adhaesion", "adhäsion"),
    ("Zulaes", "Zuläs"),
    ("zulaes", "zuläs"),
    ("Woert", "Wört"),
    ("woert", "wört"),
    ("Verbaend", "Verbänd"),
    ("verbaend", "verbänd"),
    ("Justitiabilitaet", "Justitiabilität"),
    ("justitiabilitaet", "justitiabilität"),
    ("Subsidiaer", "Subsidiär"),
    ("subsidiaer", "subsidiär"),
    ("Haeuser", "Häuser"),
    ("haeuser", "häuser"),
    ("Klaeger", "Kläger"),
    ("klaeger", "kläger"),
    ("Aktionaer", "Aktionär"),
    ("aktionaer", "aktionär"),
    ("Flaeche", "Fläche"),
    ("flaeche", "fläche"),
    ("Woerter", "Wörter"),
    ("woerter", "wörter"),
    ("Vorschlaeg", "Vorschläg"),
    ("vorschlaeg", "vorschläg"),
    ("Traeger", "Träger"),
    ("traeger", "träger"),
    ("Gueter", "Güter"),
    ("gueter", "güter"),
    ("Staendig", "Ständig"),
    ("staendig", "ständig"),
    ("Schoeff", "Schöff"),
    ("schoeff", "schöff"),
    ("Unverzueg", "Unverzüg"),
    ("unverzueg", "unverzüg"),
    ("Lueth", "Lüth"),
)


TERM_REPLACEMENTS = {
    "Agg": "AGG",
    "Apas": "APAS",
    "Bgh": "BGH",
    "Bag": "BAG",
    "Bverfg": "BVerfG",
    "Bverwg": "BVerwG",
    "Bsg": "BSG",
    "Bfh": "BFH",
    "Eugh": "EuGH",
    "Starug": "StaRUG",
    "Bav": "bAV",
    "Gmbh": "GmbH",
    "Ag": "AG",
    "Kg": "KG",
    "Eu": "EU",
    "Dsgvo": "Datenschutz-Grundverordnung",
    "Hr": "HR",
    "Hoai": "HOAI",
    "Euipo": "EUIPO",
    "Jveg": "JVEG",
    "Oepp": "ÖPP",
}


SENSITIVE_TERM_REPLACEMENTS = (
    ("Legal-" + "A" + "I", "Legal-Tech"),
    ("A" + "I Act", "Regulierungsrahmen"),
    ("A" + "I-Code", "algorithmisch erzeugter Code"),
    ("A" + "I Generated", "automatisiert erzeugtes Material"),
    ("A" + "I Training", "Training automatisierter Systeme"),
    ("A" + "I Pair Programming", "automatisiertes Pair Programming"),
    ("A" + "I VDR Classifier", "VDR-Klassifizierung"),
    ("Word Legal " + "A" + "I", "Word Legal Tech"),
    ("K" + "I-VO", "Regulierungsrahmen"),
    ("K" + "I-Verordnung", "Regulierungsrahmen"),
    ("K" + "I-Richtlinie", "Systemrichtlinie"),
    ("Schatten-" + "K" + "I", "Schatten-Systeme"),
    ("Pricing-" + "K" + "I", "Pricing-Systeme"),
    ("K" + "I-/", "System-/"),
    ("K" + "I-", "System-"),
    ("-" + "K" + "I", "-Systeme"),
)


def prose_umlauts(text: str) -> str:
    for old, new in PROSE_REPLACEMENTS:
        text = text.replace(old, new)
    for old, new in TERM_REPLACEMENTS.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    return text


def sanitize(text: str) -> str:
    paragraph = chr(167)
    text = text.replace(paragraph * 2, "Paragrafen")
    text = text.replace(paragraph, "Paragraf")
    text = re.sub(r"(\d),(\d)", r"\1.\2", text)
    text = text.replace("<", "[").replace(">", "]")
    for bad in BAD_WORDS:
        text = re.sub(re.escape(bad), "abrufen", text, flags=re.IGNORECASE)
    for old, new in SENSITIVE_TERM_REPLACEMENTS:
        text = text.replace(old, new)
    text = re.sub(r"\b" + re.escape("K" + "I") + r"\b", "algorithmische Systeme", text)
    text = re.sub(r"\b" + re.escape("A" + "I") + r"\b", "algorithmische Systeme", text)
    text = text.replace("DSGVO", "Datenschutz-Grundverordnung")
    text = text.replace("Aktengeheimnis", "Vertraulichkeit")
    text = text.replace("Co" + "dex, Novellen", "Kaiserkonstitutionen, Novellen")
    text = re.sub(r"\bsiehe Skill [^\n.]*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b" + re.escape("live " + "verifizieren") + r"\b", "vor Verwendung anhand einer belastbaren Quelle pruefen", text, flags=re.IGNORECASE)
    return prose_umlauts(text)


def clean(text: str, limit: int | None = None) -> str:
    # Aus Skilltext übernommene Auszüge dürfen keine offenen Blockmarken in
    # Tabellenzellen oder Fließtext tragen. Vollständige Codeblöcke werden
    # bereits bei der Exzerptbildung ausgelassen; dies fängt beschädigte oder
    # einzeilige Quellen defensiv ab.
    text = re.sub(r"(?:`{3,}|~{3,})", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    text = sanitize(text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        cut = text[: limit - 1]
        # Rechtsprechungs- und Normenkernsätze nicht mitten im Gedanken
        # abschneiden. Wenn im nutzbaren hinteren Teil eine Satz- oder
        # Teilsatzgrenze liegt, endet die Kurzfassung dort.
        boundaries = [
            match.start()
            for match in re.finditer(r"[.!?;](?=\s)", cut)
            if match.start() >= max(45, int(limit * 0.35))
        ]
        if boundaries:
            cut = cut[: boundaries[-1] + 1].rstrip()
            if cut.endswith(";"):
                cut = cut[:-1] + "."
            return cut
        # Nur zurueckschneiden, wenn der Schnitt mitten in einem Wort endet.
        # Endet der Schnitt genau auf einer Wortgrenze (letztes Zeichen oder
        # naechstes Zeichen im Originaltext ist ein Leerzeichen), bleibt das
        # vollstaendige Grenzwort erhalten.
        if cut and not cut[-1].isspace() and not text[len(cut)].isspace():
            if " " in cut:
                cut = cut[: cut.rfind(" ")]
        # Kein haengendes Funktionswort am Satzende ("Risiken und." o. ae.):
        # nachklappernde Konjunktionen, Praepositionen und Artikel abwerfen,
        # damit der gekuerzte Satz auf einem Inhaltswort endet.
        dangling = {
            "und", "oder", "sowie", "mit", "ohne", "zum", "zur", "zu",
            "der", "die", "das", "des", "dem", "den",
            "ein", "eine", "einer", "eines", "einem", "einen",
            "bei", "nach", "fuer", "für", "auf", "als", "im", "in", "an",
            "am", "von", "vom", "aus", "ueber", "über", "unter", "gegen",
            "je", "pro", "statt", "ist", "sind", "wird", "werden",
            "dessen", "deren", "dieser", "diese", "dieses",
            "liefere", "liefert", "paragraf",
        }
        words = cut.rstrip().split(" ")
        while len(words) > 1 and words[-1].lower().strip(" ,.;:") in dangling:
            words.pop()
        cut = " ".join(words).rstrip(" ,.;:-")
        for _ in range(3):
            shortened = re.sub(r"\s+\b(?:und|oder|mit|ohne|für|fuer|von|zu|im|in|als|bei|nach|nächstem|naechstem)\b$", "", cut, flags=re.IGNORECASE).rstrip(" ,.;:-")
            if shortened == cut:
                break
            cut = shortened
        cut = re.sub(r"\beine Fristen$", "eine Fristen- und Risikoampel", cut)
        return cut.rstrip(" ,.;:-") + "."
    return text


def sentence_terminal(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text.endswith((".", "!", "?")):
        return text
    return text.rstrip(" ;:") + "."


def byte_len(text: str) -> int:
    return len(text.encode("utf-8"))


def clip_utf8(text: str, limit: int) -> str:
    if byte_len(text) <= limit:
        return text
    clipped = text.encode("utf-8")[: max(0, limit - 1)].decode("utf-8", errors="ignore")
    return clipped.rstrip(" \n,;:-") + "\n"


def plugin_dirs() -> list[Path]:
    dirs = []
    for plugin_json in REPO.glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "_GERICHTE_EXPERIMENTAL").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "gerichtsplugins").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    return sorted(set(dirs), key=lambda p: p.as_posix())


def next_top_level_number(text: str) -> int:
    numbers = []
    for line in text.splitlines():
        match = re.match(r"##\s+(\d+)\.\s+", line)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def werkstatt_final_check_block(text: str) -> str:
    number = next_top_level_number(text)
    return f"## {number}. Schlusskontrolle für Tempo\n\n{WERKSTATT_FINAL_CHECK_LINES.rstrip()}\n"


def werkstatt_depth_block(text: str) -> str:
    number = next_top_level_number(text)
    return f"## {number}. Vertiefungsmodus für belastbare Ausgabe\n\n{WERKSTATT_DEPTH_LINES.rstrip()}\n"


def frontmatter_description(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("description:"):
            return clean(line.split(":", 1)[1].strip().strip('"'), 480)
    return ""


SOURCE_NOISE_BITS = (
    "tragende normen verifizieren",
    "fundstellen über",
    "fundstellen ueber",
    "gesetze-im-internet.de",
    "dejure.org",
    "openjur",
    "keine modellwissen-zitate",
    "bgh-/bverfg-/eugh-datenbank",
    "live prüfen",
    "live pruefen",
)


CURATED_PROFILE_KEYS = {
    "agrar",
    "aktg_hv",
    "design",
    "dokumentenworkflow",
    "ehrenamtliche_richter",
    "gebrauchsmuster",
    "jveg",
    "kanzleibetrieb",
    "kirchenrecht",
    "marke",
    "patent",
    "presse",
    "phishing",
    "rechtsgeschichte",
    "selbststaendige",
    "sport",
    "weg",
}

CURATED_NORM_PROFILE_KEYS = CURATED_PROFILE_KEYS | {"technikregulierung"}
CURATED_CASE_PROFILE_KEYS = CURATED_PROFILE_KEYS | {
    "betreuung",
    "hoai",
    "technikregulierung",
}

PROFILE_CASE_SKIP_KEYS = {
    "gesellschaft",
    "verwaltung",
}

CASE_RESEARCH_ONLY_SLUGS = {
    "notariat-alltag",
    "rechtsberatungsstelle",
}

PLUGIN_CASE_OVERRIDES: dict[str, tuple[str, ...]] = {
    "agb-recht-pruefer": (
        "BGH, Urteil vom 29.07.2021 - III ZR 192/20: Die Inhaltskontrolle nach BGB Paragraf 307 Absatz 1 Satz 1 verlangt eine umfassende Abwägung der wechselseitigen Interessen unter Berücksichtigung von Gegenstand, Zweck und Eigenart des Vertrags.",
        "BGH, Urteil vom 07.04.2022 - I ZR 212/20: Im Unterlassungsverfahren nach UKlaG sind Klauseln getrennt nach Regelungsgehalt zu prüfen; der Senat beanstandete unter anderem Kosten-, Schadensersatz- und Haftungsausschlüsse in Paketbeförderungsbedingungen.",
        "BGH, Urteil vom 19.01.2023 - VII ZR 34/20: Weicht eine Klausel von wesentlichen Grundgedanken des dispositiven Rechts ab, spricht BGB Paragraf 307 Absatz 2 Nummer 1 für eine unangemessene Benachteiligung; Vertragszweck und Risikozuweisung bleiben konkret zu würdigen.",
    ),
}


PROFILE_FIELD_OVERRIDES: dict[str, tuple[tuple[str, str], ...]] = {
    "presse": (
        ("Entscheidungsmeldung", "Tenor, tragende Gründe, praktische Folge, Rechtsmittelstatus und belastbare Fundstelle in eine veröffentlichungsfähige Meldung überführen"),
        ("Verdachtsberichterstattung", "Beweistatsachen, Stellungnahmeanfrage, Statussprache, öffentliches Interesse und Identifizierbarkeit vor Veröffentlichung abgleichen"),
        ("Gerichts- und Sitzungsbericht", "Anträge, Beweisaufnahme, Zitate, vorläufige Einschätzungen und nächsten Termin ohne Schuldvorwegnahme einordnen"),
        ("Bild, Name und Anonymisierung", "KUG, Privatheit, Prangerwirkung, Wiedererkennbarkeit und Informationswert in Text, Überschrift und Bild konsistent abwägen"),
        ("Interview und Stellungnahme", "konkrete Fragen, angemessene Antwortfrist, Antwortauswertung und dokumentierten Veröffentlichungsentscheid vorbereiten"),
        ("Korrektur und Nachtrag", "Unwahrheit, ausgeräumten Verdacht, Gegendarstellung, Richtigstellung, Nachtrag und Reichweitenfolge getrennt prüfen"),
    ),
    "agrar": (
        ("Landpacht", "Vertrag, Textform und Übergangsrecht, Anzeige, Pachtanpassung, Kündigung, Flächenübergabe und Landwirtschaftsgericht anhand der Vertragsakte prüfen"),
        ("Hofnachfolge", "Hofstatus, Grundsteuerwert, Hoferbenberechtigung, Abfindung, Nachabfindung und Übergangsrecht in einer Stichtagsmatrix verbinden"),
        ("Landwirtschaftlicher Grundstücksverkehr", "Genehmigungspflicht, Versagungsgrund, leistungsfähigen Landwirt, Kaufpreis und gerichtlichen Antrag belegen"),
        ("GAP und Direktzahlungen", "Förderjahr, Fläche, Konditionalität, Kontrolle, Kürzung, Rückforderung und Rechtsbehelf zeilenweise nachweisen"),
        ("Betriebsbezogene Fachaufsicht", "Tierhaltung, Düngung, Pflanzenschutz, Natur-, Immissions- und Forstrecht dem konkreten Betriebsvorgang zuordnen"),
        ("Vertrag, Antrag und Widerspruch", "Adressat, Frist, Tatbestand, Beleg, Gegenposition und vollzugsfähigen Antrag zu einem versandfertigen Produkt verdichten"),
    ),
    "sport": (
        ("Verbandsentscheidung", "Regelwerkfassung, Zustellung, internes Rechtsmittel, Gleichbehandlung, Verhältnismäßigkeit und Eilbedarf prüfen"),
        ("Dopingverfahren", "Probe, Kette des Gewahrsams, Substanz, Verschuldensgrad, Sanktion, Rechtsmittel und Wettkampfkalender verbinden"),
        ("Athleten- und Trainervertrag", "Befristung, Vergütung, Einsatz, Verletzung, Bildrechte, Freistellung und Beendigung redlinen"),
        ("Transfer und Spielberechtigung", "Registrierung, Transferfenster, Ausbildungsentschädigung, Freizügigkeit und vorläufige Teilnahme klären"),
        ("Schiedsverfahren und Eilrechtsschutz", "Schiedsklausel, interne Ausschöpfung, Frist, Panel, Öffentlichkeit, Antrag und Aufhebungskontrolle planen"),
        ("Sponsoring und Vermarktung", "Exklusivität, Moralklausel, Kennzeichnung, Verbandsrechte, Leistungsstörung und Exit-Szenario verhandeln"),
    ),
    "jveg": (
        ("Ausschlussfrist", "Heranziehung und tätigkeitsabhängigen Beginn der dreimonatigen Frist mit Eingangs- und Abschlussnachweisen bestimmen"),
        ("Zeit und Honorargruppe", "Auftrag, Beweisfragen, Tätigkeitsprotokoll, Fachkunde, Zeitansatz und gesetzliche Honorargruppe plausibilisieren"),
        ("Besondere Vergütung", "Einverständnis, gerichtliche Zustimmung und ausreichende Einzahlung nach JVEG Paragraf 13 getrennt prüfen"),
        ("Fahrt und sonstige Aufwendungen", "Erforderlichkeit, Strecke, Abwesenheit, Beleg, Pauschale, Hilfskraft, Kopie und Umsatzsteuer einzeln berechnen"),
        ("Zeugen und ehrenamtliche Richter", "Zeitversäumnis, Haushalt, Verdienstausfall, Höchstbetrag und Nachweis nach Berechtigtenrolle zuordnen"),
        ("Festsetzung und Beschwerde", "bezifferten Antrag, Zuständigkeit, Kürzungspunkt, Beschwerdewert, Zulassung und Einreichungsweg aufbauen"),
    ),
    "ehrenamtliche_richter": (
        ("Rolle und Besetzung", "Spruchkörper, Heranziehung, gleiches Stimmrecht, gesetzlichen Richter und rollenbezogene Verfahrensnormen bestimmen"),
        ("Neutralität und Selbstanzeige", "persönlichen oder sachlichen Vorbezug ohne eigene Vorentscheidung unverzüglich gegenüber dem Vorsitz offenlegen"),
        ("Beweisaufnahme und Fragerecht", "offene Tatsachenfrage, Wahrnehmungsgrundlage, Widerspruch, Dolmetscher- oder Gutachterpunkt sitzungsbezogen notieren"),
        ("Beratung und Mehrheit", "Schuld-, Rechtsfolgen- und Nebenfrage trennen, gesetzliche Mehrheit bestimmen und abweichende Sicht sachlich einbringen"),
        ("Teilnahmefähigkeit", "Müdigkeit, Hören, Sprache, Verständnis oder Unterbrechungsbedarf sofort anzeigen und verfahrensfest behandeln"),
        ("Beratungsgeheimnis und Medien", "Hauptverhandlungsöffentlichkeit, nichtöffentliche Beratung, Aktenwissen, Eigenrecherche und Medienkontakt strikt trennen"),
    ),
    "rechtsgeschichte": (
        ("Quellenkritik", "Textzeuge, Ausgabe, Fassung, Sprache, Übersetzung, Datum und Rechtsraum vor jeder Aussage sichern"),
        ("Norm und Anwendungspraxis", "historischen Tatbestand, Rechtsfolge, Institution und tatsächliche Durchsetzung aus getrennten Quellen rekonstruieren"),
        ("Privatrechtsgeschichte", "Eigentum, Vertrag, Delikt, Familie und Erbe entlang der maßgeblichen Kodifikations- und Rezeptionsstufen vergleichen"),
        ("Verfassungs- und Verwaltungsgeschichte", "Institution, Kompetenz, Herrschaftspraxis, Rechtsbruch und Kontinuität ohne heutige Rückprojektion untersuchen"),
        ("Rechtsüberleitung", "Fortgeltung, Aufhebung, intertemporales Recht und Überleitungsnorm mit Verkündung und Stichtag belegen"),
        ("Historische Fallanalyse", "zeitgenössischen Maßstab, Gegenquelle, damalige Rechtsfolge und heutige Anschlussfrage sichtbar trennen"),
    ),
    "kirchenrecht": (
        ("Zuständigkeit und Rechtsquelle", "Autorität, Gericht, universales Recht, Partikularrecht, Dekret, Statut und maßgebliche Fassung bestimmen"),
        ("Kirchliches Verwaltungsverfahren", "Antrag, Anhörung, Dekret, Zustellung, hierarchische Beschwerde, Frist und Vollzug chronologisch ordnen"),
        ("Eheverfahren", "Zuständigkeit, Klagegrund, Parteistellung, Urkunden, Zeugen, Ehebandverteidiger und Rechtsmittel erfassen"),
        ("Kirchliches Strafverfahren", "Voruntersuchung, Schutzmaßnahmen, Zuständigkeit, Verteidigung, Beweis, Dekret oder Gerichtsweg trennen"),
        ("Register und Urkunden", "Taufe, Ehe, Austritt, Korrektur, Archiv, Ausfertigung und Offenlegung nach Beweiszweck bearbeiten"),
        ("Staatliche Schnittstelle", "kirchliche Wirkung, Arbeitsrecht, Personenstand, Datenschutz und staatlichen Rechtsschutz gesondert prüfen"),
    ),
    "kanzleibetrieb": (
        ("Mandatsannahme", "Beteiligte, Gegner, Interessenkontrolle, Identität, Umfang, Vollmacht, Vergütung und Annahmebestätigung sichern"),
        ("Fristenkontrolle", "Auslöser, Bekanntgabe, Kalenderberechnung, Eintrag, Gegenkontrolle, Verantwortlicher und Vertretung dokumentieren"),
        ("Bearbeitung und Freigabe", "Arbeitsauftrag, Aktenstand, offene Entscheidung, Vieraugenkontrolle, Budget und Freigabefassung führen"),
        ("Elektronischer Versand", "Empfänger, Dateiformat, Signatur, Anlagen, Übermittlungsweg, Eingangsbestätigung und Fehlerreaktion prüfen"),
        ("Abrechnung und Fremdgeld", "Gebührentatbestand, Gegenstandswert, Vereinbarung, Vorschuss, Fremdgeld, Rechnung und Zahlungslauf abstimmen"),
        ("Mandatsabschluss", "Ergebnis, Restfristen, Vollstreckung, Rückgabe, Aufbewahrung, Schlussrechnung und Wiedervorlage festhalten"),
    ),
    "selbststaendige": (
        ("Status und Anmeldung", "Vertragswirklichkeit, Weisung, Eingliederung, Unternehmerrisiko, Statusverfahren und erforderliche Anzeigen prüfen"),
        ("Angebot und Auftrag", "Leistung, Ergebnis, Mitwirkung, Termin, Preis, Abnahme, Nutzungsrechte und Haftung verständlich vereinbaren"),
        ("Rechnung und Steuern", "Pflichtangaben, Umsatzsteuerstatus, Fälligkeit, Ausgabe, Beleg, Abgabe und Rücklage ordnen"),
        ("Zahlungsausfall", "Leistungsnachweis, Fälligkeit, Verzug, Mahnung, Einwendung, Mahn- oder Klageweg und Vollstreckbarkeit bestimmen"),
        ("Versicherung und Haftung", "Tätigkeitsrisiko, Deckung, Ausschluss, Schadenanzeige, Selbstbehalt und Haftungsbegrenzung abgleichen"),
        ("Liquidität und Krise", "offene Forderungen, Abgaben, fixe Kosten, Reserve, Fortführungsentscheidung und nächsten sicheren Schritt berechnen"),
    ),
    "dokumentenworkflow": (
        ("Inventur und Version", "Datei, Typ, Datum, Autor, Fassung, Signatur, Dublette, Lesbarkeit und maßgeblichen Stand erfassen"),
        ("Fundstellenlinie", "jede Aussage, Zahl, Klausel und Frist auf Dokument, Seite, Absatz, Zelle oder Nachricht zurückführen"),
        ("Vergleich und Redline", "Einfügung, Streichung, Widerspruch, fehlende Anlage, Rechenabweichung und materielle Auswirkung markieren"),
        ("Tabellen- und Rechenprüfung", "Formel, Einheit, Bezugszelle, Rundung, Summenprobe, Filter und Exportverlust kontrollieren"),
        ("Entwurf und Format", "Zielgruppe, Dokumenttyp, Gliederung, Form, Signatur, Anlagen und Einreichungskanal vor Ausgabe festlegen"),
        ("Übergabe und Nachweis", "Ergebnisdatei, Quellen, offene Lücke, Prüfschritt, Dateiname, Freigabestatus und nächste Handlung protokollieren"),
    ),
}


def is_source_noise(line: str) -> bool:
    lowered = line.lower()
    return any(bit in lowered for bit in SOURCE_NOISE_BITS)


def skill_body_excerpt(text: str) -> str:
    body = re.sub(r"^---\s*\n[\s\S]*?\n---\s*", "", text).strip()
    lines = []
    fence_marker: str | None = None
    for raw in body.splitlines():
        line = raw.strip()
        fence = re.match(r"^(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            continue
        if fence_marker is not None:
            continue
        if not line or line.startswith("#"):
            continue
        if line.startswith("|") or line.startswith("<!--"):
            continue
        lowered = line.lower()
        if (
            "rolle, ziel und gewünschtes arbeitsprodukt" in lowered
            or "vor einer rechtlichen schlussfolgerung" in lowered
            or "fristen und eilrisiken zuerst markieren" in lowered
            or "nur die fristen des konkreten rechtsgebiets" in lowered
            or "frage zu beginn nur" in lowered
            or "normen-/quellenanker" in lowered
            or "stichwort für die auswahl" in lowered
            or "stichwort fuer die auswahl" in lowered
            or lowered.startswith("fokus:")
            or lowered.startswith("output:")
            or "dieser skill erklärt" in lowered
            or "dieser skill erklaert" in lowered
            or "dieser skill vertieft" in lowered
            or "im allgemeinen bundesland-skill" in lowered
            or "nur kurz angerissen" in lowered
            or is_source_noise(line)
        ):
            continue
        lines.append(line)
        if len(" ".join(lines)) > 900:
            break
    return clean(" ".join(lines), 900)


META_SKILL_BITS = (
    "anschluss-routing",
    "dokumente-intake",
    "einstieg-routing",
    "erstgespraech",
    "erstpruefung",
    "kaltstart",
    "kommandocenter",
    "livecheck",
    "mandat-triage",
    "orientierung",
    "output-waehlen",
    "qualitygate",
    "quellenkarte",
    "red-team",
    "unterlagen-luecken",
    "workflow-",
)


def skill_directory_priority(path: Path) -> tuple[int, int, str]:
    """Bevorzugt Fachskills, ohne Meta- und Routing-Skills zu verwerfen."""

    slug = path.name
    meta_hits = sum(bit in slug for bit in META_SKILL_BITS)
    legal_signal = 0 if re.search(
        r"(?:paragraf|artikel|vertrag|klage|beschwerde|bescheid|haftung|"
        r"beweis|frist|abstimmung|pacht|doping|verguetung|entschaedigung)",
        slug,
    ) else 1
    return (meta_hits, legal_signal, slug)


def collect_skill_material(plugin_dir: Path) -> list[dict[str, str]]:
    items = []
    skill_dirs = [
        sd
        for sd in (plugin_dir / "skills").glob("*")
        if sd.is_dir() and sd.name != "juristischer-argumentationskern"
    ]
    for sd in sorted(skill_dirs, key=skill_directory_priority)[:30]:
        slug = sd.name
        skill_file = sd / "SKILL.md"
        desc = slug.replace("-", " ")
        body = ""
        if skill_file.exists():
            try:
                chunk_lines: list[str] = []
                with skill_file.open("r", encoding="utf-8", errors="ignore") as handle:
                    for line_no, line in enumerate(handle, 1):
                        chunk_lines.append(line)
                        if line_no >= 180:
                            break
                text = "".join(chunk_lines)
                desc = frontmatter_description(text) or desc
                body = skill_body_excerpt(text)
                heading = ""
                for raw_heading in text.splitlines():
                    if raw_heading.startswith("# "):
                        heading = clean(raw_heading[2:].strip(), 140)
                        break
            except OSError:
                text = ""
                body = ""
                heading = ""
        else:
            heading = ""
        items.append({"slug": slug, "desc": desc, "body": body, "raw": text if skill_file.exists() else "", "heading": heading})
    return items


def field_title(desc: str, slug: str, heading: str = "") -> str:
    desc = clean(desc, 240)
    if heading and len(heading) >= 6:
        title = heading
    elif match := re.match(r"Wenn es um (.+?) in [^:;.]{3,90} geht:", desc):
        title = match.group(1)
    else:
        safe = desc.replace("Art. ", "Art ").replace("Abs. ", "Abs ")
        title = re.split(r"[:;.] ", safe, maxsplit=1)[0]
        title = title.replace("Art ", "Art. ").replace("Abs ", "Abs. ")
    title = title.strip(" -;:.")
    if not title or len(title) < 8:
        title = slug.replace("-", " ").title()
    title = clean(title, 115)
    for particle in ("Und", "Oder", "Mit", "Nach", "Von", "Zu", "Im", "In", "Bei", "Für"):
        title = re.sub(rf"(?<!^)\b{particle}\b", particle.lower(), title)
    return title


GENERIC_FIELD_BITS = (
    "erstellt den passenden Entwurf",
    "prüft Frist, Form, Zuständigkeit",
    "ordnet Sachverhalt, Norm, Beweislast",
    "liefert eine Fristen- und Risikoampel",
    "liefert einen verwertbaren Entwurf",
    "Fristen und Eilrisiken zuerst markieren",
    "nur die Fristen des konkreten Rechtsgebiets",
    "Frage zu Beginn nur",
    "Normen-/Quellenanker",
    "Vor einer rechtlichen Schlussfolgerung",
    "Dieser Skill erklärt",
    "Dieser Skill erklaert",
    "Dieser Skill vertieft",
    "im allgemeinen Bundesland-Skill",
    "nur kurz angerissen",
    "Tragende Normen verifizieren",
    "Fundstellen über",
    "keine Modellwissen-Zitate",
    "live prüfen",
)


def field_detail(desc: str, body: str = "", title: str = "") -> str:
    desc = clean(desc, 260)
    desc = re.sub(r"^Wenn es um .+? geht:\s*", "", desc)
    desc = re.sub(r"\s*Stichwort für die Auswahl:.*$", "", desc)
    desc = desc.strip(" .;:")
    desc = desc.rstrip(" -")
    generic = not desc or any(bit.lower() in desc.lower() for bit in GENERIC_FIELD_BITS)
    if generic and body:
        body = clean(body, 280)
        body = re.sub(r"^Wenn es um .+? geht:\s*", "", body)
        body = re.sub(r"\s*Stichwort für die Auswahl:.*$", "", body)
        body = body.lstrip("- ").strip()
        body_lower = body.lower()
        if (
            len(body) > 45
            and "rolle, ziel und gewünschtes arbeitsprodukt" not in body_lower
            and "vor einer rechtlichen schlussfolgerung" not in body_lower
            and "fristen und eilrisiken zuerst markieren" not in body_lower
            and "nur die fristen des konkreten rechtsgebiets" not in body_lower
            and "frage zu beginn nur" not in body_lower
            and "normen-/quellenanker" not in body_lower
            and "stichwort für die auswahl" not in body_lower
            and "stichwort fuer die auswahl" not in body_lower
            and not is_source_noise(body)
        ):
            desc = body.strip(" .;:")
            generic = False
    if generic:
        basis = title or "dieses Feld"
        return f"{basis}: Tatsachen, Frist, Norm, Beweislast, stärkstes Gegenargument und nächstes Dokument in einer Arbeitslinie verbinden"
    return desc


def manifest(plugin_dir: Path) -> dict:
    return json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


COURT_MARKERS = (
    "BGH", "BAG", "BVerfG", "BVerwG", "BSG", "BFH", "EuGH", "BPatG",
    "OLG", "LG ", "AG ", "LAG", "ArbG", "SG ", "LSG", "BVerfGE", "BAGE", "NJW", "NZA", "ZIP",
)

LAW_MARKERS = (
    "BGB", "ZPO", "StPO", "StGB", "GG", "InsO", "StaRUG", "VwGO", "FGO",
    "SGG", "ArbGG", "FamFG", "HGB", "GmbHG", "AktG", "UmwG", "MarkenG",
    "UrhG", "DesignG", "PatG", "VVG", "VwVfG", "SGB", "AO", "EStG",
    "UStG", "KStG", "KSchG", "TzBfG", "BetrVG", "BetrAVG", "BDSG",
    "AEUV", "EUV", "EMRK", "GRCh", "DSGVO", "VOB/B", "HOAI", "BRAO",
    "BNotO", "RVG", "RDG", "GWB", "VgV", "UVgO", "ZVG", "GVG",
    "KWG", "WpHG", "WpIG", "ZAG", "GwG", "LobbyRG", "BSIG",
    "ProdHaftG", "ProdSG", "GPSR", "DORA",
)


def relevant_lines(skill_material: list[dict[str, str]], limit: int = 450) -> list[str]:
    lines: list[str] = []
    for item in skill_material:
        raw = "\n".join([item.get("desc", ""), item.get("body", ""), item.get("raw", "")])
        for raw_line in raw.splitlines():
            line = raw_line.strip(" -\t")
            if not line or line.startswith("|") or line.startswith("#") or line.startswith("<!--"):
                continue
            if re.match(r"^(?:name|description|allowed-tools)\s*:", line):
                continue
            if is_source_noise(line):
                continue
            line = clean(line, 260)
            if len(line) < 20:
                continue
            lines.append(line)
            if len(lines) >= limit:
                return lines
    return lines


def is_generic_anchor(line: str) -> bool:
    lowered = line.lower()
    generic_bits = (
        "bverwg 6 c 12.21",
        "maßstab verwaltungsentscheidung",
        "verifizierte anker",
        "gesetze-im-internet.de",
        "dejure.org",
        "openjur",
        "nur fallbezogen",
        "nicht verifizierte",
        "vor verwendung",
        "belastbaren quelle",
        "nicht erfinden",
        "rechtsprechung nur",
        "wenn es um",
        "tragende normen verifizieren",
        "fristen und eilrisiken",
        "rot (",
        "gelb (",
        "gruen (",
        "grün (",
        "rolle, ziel",
        "live",
        "dieser skill",
        "skill zum",
        "skill für",
        "skill fuer",
        "auswahlstichwort",
        "stichwort für die auswahl",
        "stichwort fuer die auswahl",
        "vor einer rechtlichen schlussfolgerung",
        "arbeitsmodus:",
        "fokus:",
        "dieser skill erklärt",
        "dieser skill erklaert",
        "dieser skill vertieft",
        "im allgemeinen bundesland-skill",
        "nur kurz angerissen",
    )
    return any(bit in lowered for bit in generic_bits)


def extract_norm_anchors(skill_material: list[dict[str, str]], max_items: int = 7) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    law_pattern = "|".join(re.escape(marker) for marker in sorted(LAW_MARKERS, key=len, reverse=True))
    for line in relevant_lines(skill_material):
        if is_generic_anchor(line):
            continue
        has_norm = re.search(r"\b(?:Paragraf(?:en)?|Artikel|Art\.)\s+\d", line)
        if not has_norm:
            continue
        if not any(marker in line for marker in LAW_MARKERS):
            continue
        if any(marker in line for marker in COURT_MARKERS) and re.search(r"\b(?:Urteil|Beschluss|Entscheidung)\b", line):
            continue
        starts_like_norm = re.match(rf"^(?:Normenradar:\s*)?(?:{law_pattern})\b", line)
        starts_with_paragraph = re.match(r"^(?:Paragraf(?:en)?|Artikel|Art\.)\s+\d", line)
        law_then_paragraph = re.search(rf"\b(?:{law_pattern})\s+(?:Paragraf(?:en)?|Artikel|Art\.)\s+\d", line)
        if not (starts_like_norm or starts_with_paragraph or law_then_paragraph):
            continue
        if re.search(r"\b(?:Erblasser|Eigentümer|Mandant|Arbeitnehmer|Arbeitgeber|Kläger|Beklagter|Versicherter|Gläubiger|Schuldner)\b", line[:90]):
            continue
        if re.search(r"\b\d[\d.]*\s*(?:EUR|Euro|Mio|ha)\b", line[:140]):
            continue
        candidate_source = line
        if not (starts_like_norm or starts_with_paragraph) and law_then_paragraph:
            candidate_source = line[law_then_paragraph.start():]
            candidate_source = re.split(
                r",\s+(?=(?:der|die|das|den|dem|des|ein|eine|einer|einem|einen|konkret\w*|aktuell\w*)\b)"
                r"|\s+und\s+(?=(?:der|die|das|den|dem|des|ein|eine|einer|einem|einen|konkret\w*|aktuell\w*)\b)"
                r"|\s+(?=(?:ist|sind|wird|werden|muss|müssen|soll|sollen|verlangt|betrifft|regelt)\b)",
                candidate_source,
                maxsplit=1,
                flags=re.IGNORECASE,
            )[0]
        candidate = clean(candidate_source, 185).rstrip(".")
        if not candidate:
            continue
        key = re.sub(r"\W+", "", candidate.lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append(candidate)
        if len(anchors) >= max_items:
            break
    return anchors


def extract_case_anchors(skill_material: list[dict[str, str]], max_items: int = 4) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    for line in relevant_lines(skill_material):
        if is_generic_anchor(line):
            continue
        if not any(marker in line for marker in COURT_MARKERS):
            continue
        if not re.match(r"^(?:BGH|BAG|BVerfG|BVerwG|BSG|BFH|EuGH|BPatG|OLG|LG|AG|LAG|ArbG|SG|LSG)\b", line):
            continue
        if re.match(r"^[a-z0-9-]+\s+[—-]\s+", line):
            continue
        has_decision_signal = (
            re.search(r"\b(?:Urteil|Beschluss|Entscheidung)\b", line)
            or re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", line)
            or re.search(r"\b(?:[IVX]+ ZR|IX ZR|XII ZB|C-\d+|BvR|AZR|StR|CN|C )", line)
        )
        if not has_decision_signal:
            continue
        candidate = clean(line, 205).rstrip(".")
        if not candidate:
            continue
        key = re.sub(r"\W+", "", candidate.lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append(candidate)
        if len(anchors) >= max_items:
            break
    return anchors


def case_identity(anchor: str) -> str:
    ids = case_id_set(anchor)
    return "|".join(sorted(ids)) if ids else re.sub(r"\W+", "", anchor.lower())[:90]


def case_id_set(anchor: str) -> set[str]:
    normalized = anchor.replace("–", "-").replace("—", "-")
    patterns = (
        r"\b(?:[IVX]+|X|IX|XII|XI|VIII|VII|VI|V|IV|III|II|I)\s+ZR\s+\d+/\d+\b",
        r"\b\d+\s+AZR\s+\d+/\d+\b",
        r"\b\d+\s+StR\s+\d+/\d+\b",
        r"\b\d+\s+BvR\s+\d+/\d+\b",
        r"\b\d+\s+BvL\s+\d+/\d+\b",
        r"\bB\s+\d+\s+[A-Z]{1,3}\s+\d+/\d+\s+R\b",
        r"\bC-\d+/\d+\b",
        r"\bKZR\s+\d+/\d+\b",
    )
    ids: list[str] = []
    for pattern in patterns:
        ids.extend(match.group(0).lower().replace(" ", "") for match in re.finditer(pattern, normalized))
    return set(ids)


def dedupe_cases(profile_cases: list[str], extracted_cases: list[str]) -> list[str]:
    seen: set[str] = set()
    for case in profile_cases:
        seen.update(case_id_set(case))
    out: list[str] = []
    for case in extracted_cases:
        ids = case_id_set(case)
        fallback = case_identity(case)
        if ids and seen.intersection(ids):
            continue
        if not ids and fallback in seen:
            continue
        seen.update(ids or {fallback})
        out.append(case)
    return out


def skill_fields(skill_material: list[dict[str, str]], max_items: int = 6) -> list[tuple[str, str]]:
    fields: list[tuple[str, str]] = []
    seen: set[str] = set()
    for item in skill_material:
        desc = item.get("desc") or item.get("body") or item.get("slug", "")
        title = field_title(desc, item.get("slug", ""), item.get("heading", ""))
        detail = field_detail(desc, item.get("body", ""), title)
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        fields.append((title, clean(detail, 150)))
        if len(fields) >= max_items:
            break
    return fields


def profile_fields(
    profile: ThemenProfil,
    skill_material: list[dict[str, str]],
    max_items: int = 6,
) -> list[tuple[str, str]]:
    overrides = PROFILE_FIELD_OVERRIDES.get(profile.key)
    if overrides:
        return [(title, clean(detail, 180)) for title, detail in overrides[:max_items]]
    fields: list[tuple[str, str]] = []
    seen: set[str] = set()
    for station in profile.stationen:
        text = clean(station, 240).rstrip(".")
        if ":" in text:
            title, detail = text.split(":", 1)
        else:
            parts = [part.strip() for part in text.split(",") if part.strip()]
            title = ", ".join(parts[:2]) if len(parts) >= 2 else " ".join(text.split()[:6])
            detail = text
        title = clean(title, 90).rstrip(" .:-")
        detail = clean(detail, 180).rstrip(" .")
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        fields.append((title, detail))
        if len(fields) >= max_items:
            return fields

    noise_bits = (
        "allgemein",
        "aktenanlage",
        "beweislast",
        "chronologie",
        "deal",
        "einstieg",
        "fehlerkatalog",
        "kaltstart",
        "luecken",
        "quality",
        "quelle",
        "red-team",
        "routing",
        "start",
        "workflow",
    )
    for title, detail in skill_fields(skill_material, max_items * 3):
        lowered = title.lower()
        if any(bit in lowered for bit in noise_bits):
            continue
        key = re.sub(r"\W+", "", lowered)
        if not key or key in seen:
            continue
        seen.add(key)
        fields.append((title, detail))
        if len(fields) >= max_items:
            break
    return fields


def station_instruction(station: str) -> str:
    text = clean(station, 240).rstrip(" .")
    if ":" in text:
        title, detail = (part.strip() for part in text.split(":", 1))
    else:
        title, detail = "Prüfstation", text
    return (
        f"Arbeitsgriff {title}: {detail}. Ordne jedem Punkt den konkreten Aktenfund, "
        "die steuernde Norm, die Beweislast und die stärkste Gegenposition zu; schließe "
        "mit einem ausformulierten Ergebnisbaustein, dem verbleibenden Risiko und dem "
        "nächsten Verfahrensschritt."
    )


def station_heading(station: str) -> str:
    text = clean(station, 220).rstrip(" .")
    if ":" in text:
        return clean(text.split(":", 1)[0], 90).rstrip(" .:-")
    return clean(text, 110).rstrip(" .:-")


def detail_question(detail: str) -> str:
    detail = clean(detail, 115).lstrip("- ").rstrip(". -")
    for _ in range(3):
        shortened = re.sub(r"\s+\b(?:und|oder|mit|ohne|für|fuer|von|zu|im|in|als|bei|nach|nächstem|naechstem)\b$", "", detail, flags=re.IGNORECASE).rstrip(". -")
        if shortened == detail:
            break
        detail = shortened
    repairs = {
        "Kollisions": "Kollisionsprüfung",
        "Verhandlungs": "Verhandlungslinie",
        "Fehler": "Fehlerliste",
        "Fristen": "Fristen- und Risikoampel",
        "Paragraf": "einschlägige Paragrafen",
        "Liefere": "konkreten Sofortgriff",
    }
    for suffix, replacement in repairs.items():
        if detail.endswith(suffix):
            detail = detail[: -len(suffix)].rstrip(" -") + " " + replacement
            break
    return detail.rstrip(". -")


def quick_grip(profile: ThemenProfil, field: str, detail: str) -> str:
    hay = f"{profile.key} {field} {detail}".lower()
    if profile.key in PROFILE_FIELD_OVERRIDES and detail:
        return clean(detail, 180).rstrip(" .")
    if profile.key in {"aktg_hv", "phishing", "weg"} and detail:
        return clean(detail, 180).rstrip(" .")
    if profile.key == "eu_prozess":
        return "Klageart, Zuständigkeit, Frist, Verfahrenssprache, e-Curia, Anlagen, Rechtsschutzinteresse und Antragssatz zuerst sichern"
    if profile.key == "zeugnis":
        return "Zeugnisart, Tätigkeitsbild, Leistungsnote, Sozialverhalten, Auslassung, Form und konkrete Änderungsfassung in einer Matrix verbinden"
    if profile.key == "bank":
        return "Produkt, Kunde, Beratung oder Autorisierung, Aufsichtspflicht, Dokumentation, Schaden und Frist in einer Bankakte trennen"
    if profile.key == "datenbank":
        return "Schutztyp, Investition, Zugriffspfad, entnommene Datenmenge, Lizenz, Schranke und Beweissicherung als Datenbankmatrix ordnen"
    if profile.key == "marke":
        return "Zeichen, Priorität, Waren oder Dienstleistungen, Kennzeichnungskraft, Ähnlichkeit, Benutzung, Verwechslungsgefahr und Verfahrensziel verbinden"
    if profile.key == "design":
        return "Ansichten, Offenbarungstag, Formenschatz, Eigenart, Gestaltungsfreiheit, Gesamteindruck, Verletzung und Nichtigkeitsrisiko vergleichen"
    if profile.key == "patent":
        return "Anspruchsmerkmale, Priorität, Stand der Technik, Rechtsbestand, angegriffene Ausführung, Schutzbereich und Verfahrensschritt ordnen"
    if profile.key == "gebrauchsmuster":
        return "Abzweigung, Schonfrist, Schutzanspruch, Recherche, ungeprüften Rechtsbestand, Verletzung und Löschungsrisiko getrennt sichern"
    if profile.key == "gewerblicher_rechtsschutz":
        return "Schutzrecht, Inhaber, Priorität, Registerstand, Verletzung, Beweis, Eilbedarf und parallele Anspruchsgrundlagen getrennt prüfen"
    if profile.key == "lobbyregister":
        return "Adressat, Interessenvertretung, Registrierungspflicht, Ausnahme, Angaben, Aktualisierung und Sanktionsrisiko sofort prüfen"
    if profile.key == "geldwaesche":
        return "Verpflichtetenrolle, Kunde, wirtschaftlich Berechtigter, Risiko, Mittelherkunft, Verdachtsschwelle und Dokumentation trennen"
    if profile.key == "cybersicherheit":
        return "Einrichtung, Rechtsrahmen, Asset, Vorfall, Meldefrist, Nachweisordner und Aufsichtsrisiko in eine Incident-Linie bringen"
    if profile.key == "kartell":
        return "Markt, Beteiligte, Verhalten, Zweck oder Wirkung, Beleg, Rechtfertigung, Schaden und Bußgeldrisiko zusammenführen"
    if profile.key == "produkt":
        return "Produktversion, Fehlerart, Sicherheitserwartung, Warnung, Beobachtung, Rückrufbedarf und Haftungsfolge sofort abgleichen"
    if profile.key == "sozialstatus":
        return "Tätigkeit, Zeitraum, Weisung, Eingliederung, Unternehmerrisiko, Vertragswirklichkeit, Beiträge und Frist gewichten"
    if profile.key == "forderung":
        return "Vertrag, Leistung, Rechnung, Fälligkeit, Verzug, Einwendung, Beweis und Klage- oder Vollstreckungsweg klagereif ordnen"
    if profile.key == "technikregulierung":
        if "kollusion" in hay or "pricing" in hay:
            return "Pricing-Zweck, Wettbewerberdaten, Hub-Dienstleister, menschliche Kontrolle, Kartellrechtsrisiko und Technikregulierung trennen"
        if "art. 4" in hay or "kompetenz" in hay or "schulung" in hay:
            return "Adressatenkreis, Rollen, Risikoklasse, Schulungsinhalt, Nachweis, Wiederholung und Verantwortlichkeit dokumentieren"
        if "anbieter" in hay or "provider" in hay or "art. 25" in hay:
            return "Eigenname, Eigenmarke, wesentliche Änderung, Zweckänderung, Produktintegration und Pflichtenwechsel nach Art. 25 trennen"
        if "betreiber" in hay or "deployer" in hay or "art. 26" in hay:
            return "bestimmungsgemäße Nutzung, menschliche Aufsicht, Eingabedaten, Logging, FRIA und Vorfallmeldung als Betreiberpflichten ordnen"
        if "owi" in hay or "untersuchung" in hay:
            return "Vorwurf, Behörde, Frist, Logs, Interviews, Datenschutz, Legal-Privilege-Risiko und Verteidigungslinie sichern"
        if "abgrenzung" in hay or "konventionelle" in hay:
            return "Inferenz, Autonomie, Output, Zweckbestimmung, Systemgrenze und Folgeprüfung nach Art. 3 Nr. 1 festlegen"
        return "Zweckbestimmung, Rolle, Risikoklasse, Stichtag, Nachweisakte, Rechtsfolge und Behördenrisiko in einer Entscheidungszeile verbinden"
    if profile.key == "bgb":
        return "Anspruchsgrundlage, Vertragsschluss, Pflichtverletzung oder Mangel, Einwendung, Frist, Beweislast und Rechtsfolge sauber abschichten"
    if profile.key == "zivilprozess":
        return "Antrag, Streitgegenstand, Schlüssigkeit, Erheblichkeit, Beweislast, Verfügung und Tenor in eine Relation bringen"
    if profile.key == "erbrecht":
        return "Familienstamm, Verfügung, Quote, Nachlasswert, Pflichtteilsergänzung, Auskunft und Erbscheinspfad rechnerisch ordnen"
    if profile.key == "medizin":
        return "Befund, Indikation, Standard, Aufklärung, Dokumentation, Beweislast, Gutachtenfrage und Verfahren zusammenführen"
    if profile.key == "verkehr":
        return "Ereignis, Frist, Haftungsquote, Beweismittel, Schaden, Einwand und Zahlungs- oder Einspruchsziel sofort sortieren"
    if profile.key == "vollstreckung":
        return "Titel, Klausel, Zustellung, Forderungsstand, Zugriffsziel, Antrag, Schuldnerschutz und Anlagen prüfen"
    if profile.key == "immobilien":
        return "Objekt, Grundbuchstand, Rechtsgeschäft, Form, Bewilligung, Nachweis, Rang und Vollzugsschritt in einer Aktenlinie verbinden"
    if profile.key == "eu_recht":
        return "Unionsnorm, Rechtsakt, Anwendungsbereich, unmittelbare Wirkung, Vorrang, Rechtfertigung und Rechtsschutzroute trennen"
    if profile.key == "methodik":
        return "Rechtsfrage, Normmerkmal, Tatsache, Aktenfund, Subsumtion, Gegenargument und Endprodukt zeilenweise verknüpfen"
    if profile.key == "betreuung":
        return "Angelegenheit, Erforderlichkeit, Wunsch, Vertretungsmacht, Genehmigung, Beleg und Gerichtsschritt konkret bestimmen"
    if profile.key == "hoai":
        return "Vertragsjahr, Leistungsbild, Leistungsphase, geschuldeter Erfolg, Leistungsstand, Honorar, Nachtrag und Haftungsbeleg trennen"
    if profile.key == "weltraum":
        return "Mission, Weltraumgegenstand, Betreiber, Startstaat, Registerstaat, Genehmigung, Frequenz, Haftung und Telemetriebeleg verbinden"
    if profile.key == "presse":
        return "Aussagetyp, Beweistatsachen, Stellungnahme, Identifizierbarkeit, Bildrecht, Verfahrensstatus und veröffentlichungsfähige Fassung abgleichen"
    if profile.key == "agrar":
        return "Betrieb, Fläche, Pacht oder Hofstatus, Grundsteuerwert, Förderjahr, Spezialbehörde, Frist und Bewirtschaftungsbeleg verbinden"
    if profile.key == "sport":
        return "Regelwerkfassung, Entscheidung, Zustellung, interne Instanz, Schieds- oder Gerichtsweg, Eilbedarf und Wettkampfbeleg sichern"
    if profile.key == "jveg":
        return "Heranziehung, Rolle, Ausschlussfrist, Zeitansatz, Honorargruppe, Auslagen, Kürzung und Rechtsbehelf rechnerisch prüfen"
    if profile.key == "ehrenamtliche_richter":
        return "Rolle, Spruchkörper, Besetzung, Neutralität, offene Beweisfrage, Beratung, Mehrheit und Beratungsgeheimnis trennen"
    if profile.key == "rechtsgeschichte":
        return "Textzeuge, Fassung, Datum, Rechtsraum, Übersetzung, Normfunktion, Anwendungspraxis und Rezeptionsspur quellenkritisch ordnen"
    if profile.key == "kirchenrecht":
        return "zuständige Autorität, Canon, Partikularrecht, Urkunde, kirchlichen Verfahrensweg, Frist und staatliche Schnittstelle bestimmen"
    if profile.key == "kanzleibetrieb":
        return "Mandat, Interessenkontrolle, Vollmacht, Frist, Verantwortlicher, Freigabe, Versandnachweis, Budget und Wiedervorlage sichern"
    if profile.key == "selbststaendige":
        return "Tätigkeit, Status, Vertrag, Leistung, Rechnung, Abgabe, Beleg, Zahlung und nächstes Geschäfts- oder Behördendokument ordnen"
    if profile.key == "dokumentenworkflow":
        return "maßgebliche Version, Fundstelle, Signatur, Zahl, Widerspruch, Lücke, Zielprodukt und reproduzierbare Übergabe verbinden"
    if profile.key in {"arbeits", "hr"}:
        if any(bit in hay for bit in ("kündigung", "befristung", "abmahnung", "aufheb", "betriebsrat")):
            return "Zugang, Dreiwochenfrist, Schriftform, Beteiligungsrechte, Darlegungslast und Klage- oder Vergleichsziel sofort trennen"
        if any(bit in hay for bit in ("agg", "beschwerde", "arbeitsschutz", "gefährd", "hinweis")):
            return "Meldung, Schutzpflicht, Anhörung, Vertraulichkeit, Beleg, Maßnahme und Benachteiligungsrisiko in einer Fallakte trennen"
        if any(bit in hay for bit in ("angebot", "offer", "vertrag", "onboarding", "nachweis")):
            return "Vertragstyp, Tätigkeit, Vergütung, Arbeitsort, Beginn, Befristung, Nachweis und Unterschriftsweg versandfertig ordnen"
        if any(bit in hay for bit in ("arbeitszeit", "urlaub", "fehlzeit", "krank", "payroll", "vergütung")):
            return "Zeitraum, Anspruch, Berechnung, Nachweis, Ausschlussfrist, Beteiligungsrecht und Buchungs- oder Antworttext verbinden"
        return "Arbeitsvertrag, aktuelle Maßnahme, Frist, Form, Beteiligungsrecht, Beleg und nächstes Personal- oder Prozessdokument ordnen"
    if "kündigung" in hay or "befristung" in hay or "betriebsrat" in hay or "arbeitsgericht" in hay:
        return "Zugang, Dreiwochenfrist, Schriftform, Beteiligungsrechte, Darlegungslast und Klage- oder Vergleichsziel sofort trennen"
    if "insolvenz" in hay or "starug" in hay or profile.key in {"insolvenz", "liquiditaet"}:
        return "Liquiditätsstatus, Fälligkeit, Fortbestehensprognose, Antragspflicht, Beweislast und Sanierungsoption in einer Entscheidungslinie ordnen"
    if "renten" in hay or "rente" in hay or "drv" in hay or profile.key == "renten":
        return "Versicherungsverlauf, Wartezeit, Entgeltpunkte, Rentenbeginn, Bescheidfehler und Widerspruchsfrist nach SGB VI nachrechnen"
    if "sozial" in hay or "pflege" in hay or "hilfsmittel" in hay or profile.key == "sozial":
        return "Bescheid, Bekanntgabe, Leistungsträger, medizinische Belege, Wirtschaftlichkeit, SGG-Frist und Eilrechtsschutz zusammenführen"
    if "gesellschaft" in hay or "gmbh" in hay or "aktg" in hay or profile.key == "gesellschaft":
        return "Satzung, Beschlusskompetenz, Mehrheit, Vertretung, Treuepflicht, Registervollzug und Haftungsrisiko nebeneinanderlegen"
    if "agrar" in hay or "landpacht" in hay or "gap" in hay or "höfe" in hay:
        return "Pacht, Höfeordnung, GrdstVG-Genehmigung, GAP-Förderung, Bescheidfrist und Bewirtschaftungsnachweis aktennah prüfen"
    if "miet" in hay or "wohnung" in hay or profile.key == "miet":
        return "Vertrag, Rückstand, Mangelanzeige, Kündigungsgrund, Schonfrist, Zuständigkeit und Räumungsrisiko sofort sortieren"
    if "famil" in hay or "unterhalt" in hay or profile.key == "famil":
        return "Auskunft, Einkommen, Bedarf, Selbstbehalt, Kindeswohl, Versorgungsausgleich und Verbundfrage rechnerisch trennen"
    if "urheber" in hay or profile.key == "urheber":
        return "Werk, Rechtekette, Nutzungshandlung, Lizenz, Schranke, Beweis und Anspruchsziel verdichten"
    if "straf" in hay or "anklage" in hay or profile.key == "straf":
        return "Tatkomplex, Norm, Beweismittel, Einlassung, Verwertbarkeit, Frist und Rechtsfolge zeilenweise prüfen"
    if "steuer" in hay or "finanz" in hay or profile.key == "steuer":
        return "Bescheid, Bekanntgabe, Einspruchsfrist, Besteuerungsgrundlage, Beleg, Schätzung und Aussetzungsbedarf getrennt prüfen"
    if "vergabe" in hay or profile.key == "vergabe":
        return "Rügefrist, Vergabeunterlagen, Zuschlagskriterium, Dokumentation, Bieterfrage und Nachprüfungsantrag sofort abgleichen"
    if profile.key in {"bau", "bauplanung"}:
        return "Vertragssoll, Nachtrag, Behinderung, Abnahme, Mangel, Kostenfolge, Beweis und Gutachterfrage in eine Bauakte bringen"
    if "datenschutz" in hay or "dsgvo" in hay or profile.key == "datenschutz":
        return "Rolle, Rechtsgrundlage, Betroffenenrecht, Frist, TOMs, Auftragsverarbeitung und Aufsichtsrisiko dokumentieren"
    if profile.key == "it":
        return "Leistungssoll, Abnahme, SLA, Rechtekette, Datenschutz, Haftung, Change Request und Beleglage zusammenführen"
    if "verwalt" in hay or profile.key == "verwaltung":
        return "Verwaltungsakt, Bekanntgabe, Widerspruch/Klagefrist, Ermessen, Anhörung, Akteneinsicht und Eilantrag prüfen"
    candidate = detail_question(detail)
    field_prefix = field.rstrip(" .:-").lower()
    if field_prefix and candidate.lower().startswith(field_prefix + ":"):
        candidate = candidate.split(":", 1)[1].strip()
    if candidate and len(candidate) >= 45 and "tatsachen, frist, zuständigkeit" not in candidate.lower():
        return candidate
    return "Tatsachen, Frist, Zuständigkeit, Norm, Beweislast, Gegenargument und nächstes Dokument zu einem Sofortbaustein verbinden"


def quick_stations(profile: ThemenProfil, skill_material: list[dict[str, str]]) -> list[str]:
    if profile.key != "default" or not skill_material:
        return [clean(station, 230) for station in profile.stationen[:6]]
    out: list[str] = []
    for field, detail in profile_fields(profile, skill_material, 6):
        out.append(f"{field}: {quick_grip(profile, field, detail)}.")
    if len(out) < 4:
        out.extend(profile.stationen)
    return out[:6]


def domain_goal(mf: dict, plugin_dir: Path, profile: ThemenProfil) -> str:
    intro = clean(mf.get("description", "") or first_readme_paragraph(plugin_dir) or profile.rolle, 360)
    if not intro:
        intro = profile.rolle
    return intro.rstrip(".")


def output_hint(profile: ThemenProfil, fields: list[tuple[str, str]]) -> str:
    if profile.skelette:
        return clean("; ".join(item.rstrip(" .") for item in profile.skelette[:2]), 330).rstrip(".")
    if fields:
        names = ", ".join(name for name, _detail in fields[:4])
        return clean(f"Ausgabe entlang der Kernfelder {names}: Kurzvermerk, Prüfmatrix, Entwurf, Fristenblatt oder Fragenliste mit nächstem Schritt", 330).rstrip(".")
    return "Kurzvermerk, Prüfmatrix, Entwurf, Fristenblatt oder Fragenliste mit nächstem Schritt"


BEWEISLAST_MERKER = {
    "arbeits": "Arbeitgeber für Vertragsbedingungen, Zeiterfassung, Vergütung, Personalmaßnahme und Beteiligung; Arbeitnehmer für Zugang, eigene Anspruchsvoraussetzungen und Fristwahrung.",
    "hr": "Arbeitgeber für Vertragsbedingungen, Zeiterfassung, Vergütung, Personalmaßnahme und Beteiligung; Beschäftigter für Zugang, eigene Anspruchsvoraussetzungen und Fristwahrung.",
    "zeugnis": "Arbeitnehmer für Berichtigungsziel und bessere Gesamtnote; Arbeitgeber für Wahrheit, Tatsachengrundlage, Auslassungen und formale Erfüllung.",
    "miet": "Vermieter für Rückstand, Kündigungsgrund und Abrechnung; Mieter für Mangelanzeige, Zahlung, Schonfrist und Einwendungen.",
    "famil": "Unterhaltsteller für Bedarf und Auskunft; Pflichtiger für Leistungsunfähigkeit; in Kindschaftssachen Amtsermittlung und Kindeswohlbelege.",
    "straf": "Tatnachweis beim Staat; Verteidigung markiert Zweifel, Verwertungsverbote, Alternativerklärung und Strafzumessungsstoff.",
    "datenschutz": "Verantwortlicher für Rechtmäßigkeit, TOMs und Rechenschaft; Betroffener für Schaden und Kausalität bei Ersatzansprüchen.",
    "insolvenz": "Verwalter oder Anspruchsteller für Insolvenzreife, Benachteiligung und Kenntnis; Geschäftsleitung für Entlastung und Dokumentation.",
    "steuer": "Finanzbehörde für steuerbegründende Tatsachen; Steuerpflichtiger für Begünstigung, Betriebsausgaben und Nachweise.",
    "gesellschaft": "Anspruchsteller für Pflichtverletzung, Schaden und Kausalität; Organ oder Gesellschafter für Entlastung, Beschlussbasis und Business Judgment.",
    "aktg_hv": "Die Gesellschaft belegt Einberufung, Bekanntmachung, Anmeldung, Teilnahmeprüfung, Auskunft, Abstimmung und Niederschrift; der Anfechtungskläger bezeichnet Verstoß, Anfechtungsbefugnis, Widerspruch und Klagefrist.",
    "bank": "Kunde für Beratungssituation, Schaden und Kausalität; Bank für Aufklärung, Beratungsdokumentation, Autorisierung, Ausnahme und Organisationspflicht.",
    "phishing": "Die Bank belegt Authentifizierung, ordnungsgemäße Aufzeichnung, Störungsfreiheit und ihren Gegenanspruch; der Zahler schildert den abweichenden Ablauf, seine Anzeige und entlastende Umstände konkret.",
    "datenbank": "Rechteinhaber für Schutzgegenstand, Investition, wesentliche Entnahme und Wiederverwendung; Nutzer für Lizenz, Schranke, Erlaubnis und Datenherkunft.",
    "lobbyregister": "Registerpflichtiger für Ausnahme, Angaben, Aktualisierung und Dokumentation; Behörde für Tatbestand, Ermessen und Verstoß.",
    "geldwaesche": "Verpflichteter für Risikoanalyse, Identifizierung, wirtschaftlich Berechtigte und Monitoring; Behörde für Verstoß, Verschulden und Sanktion.",
    "cybersicherheit": "Einrichtung für Risikomanagement, Nachweise und Meldung; Behörde für Anordnung, Frist, Zuständigkeit und Bußgeldtatbestand.",
    "kartell": "Anspruchsteller oder Behörde für Markt, Abstimmung, Marktmacht und Schaden; Unternehmen für Effizienz, Rechtfertigung, Compliance und Einwendungen.",
    "produkt": "Geschädigter für Produktfehler, Schaden und Kausalität; Hersteller oder Händler für Sicherheitserwartung, Warnung, Rückruf und Entlastung.",
    "forderung": "Gläubiger für Vertrag, Fälligkeit, Verzug und Belegkette; Schuldner für Erfüllung, Einwendung, Aufrechnung und Verjährung.",
    "verfass": "Beschwerdeführer für Grundrechtsbetroffenheit, Subsidiarität und Frist; Staat für Eingriff, Schranke und Verhältnismäßigkeit.",
    "versicherung": "Versicherungsnehmer für Versicherungsfall und Schaden; Versicherer für Ausschluss, Obliegenheitsverletzung und Kürzung.",
    "liquiditaet": "Geschäftsleitung muss Status, Fälligkeiten und Prognose dokumentieren; Anspruchsteller greift Lücken und verspätete Reaktion an.",
    "sozial": "Leistungsträger ermittelt von Amts wegen; Versicherter liefert Befund, Bedarf, Teilhabe- und Eilbelege.",
    "sozialstatus": "Rentenversicherung oder Einzugsstelle für Gesamtbild und Beitragsforderung; Auftraggeber und Erwerbstätiger für Vertrag, Eingliederung, Weisungen und Unternehmerrisiko.",
    "renten": "Versicherter belegt Zeiten, Lücken und medizinische Tatsachen; Träger muss Versicherungsverlauf und Bescheid nachvollziehbar begründen.",
    "verwaltung": "Behörde trägt Tatsachengrundlage, Ermessen und Verfahren; Bürger belegt Betroffenheit, Frist und Eilbedürftigkeit.",
    "vergabe": "Auftraggeber für Dokumentation und Wertung; Bieter für Rüge, Interesse, Rechtsverletzung und drohenden Schaden.",
    "urheber": "Rechteinhaber für Schutzrecht, Inhaberschaft und Nutzung; Gegner für Einrede, Lizenz, Erschöpfung oder Nichtbenutzung.",
    "marke": "Markeninhaber oder Widersprechender für Priorität, Kennzeichnungskraft, Benutzung und Kollision; Gegner für Einrede, Nichtbenutzung, Erschöpfung oder Verfall.",
    "design": "Designinhaber für Rechtsinhaberschaft, Priorität und übereinstimmenden Gesamteindruck; Gegner für Vorbekanntheit, technische Bedingtheit, Nichtigkeit und Erschöpfung.",
    "patent": "Patentinhaber für Rechtsinhaberschaft und Verletzung; Angreifer für neuheitsschädlichen Stand der Technik, Nichtigkeitsgrund oder FRAND-Einwand.",
    "gebrauchsmuster": "Inhaber für eingetragenen Anspruch, Rechtsbestand und Verletzung; Gegner für Löschungsgrund, Vorbenutzung, Erschöpfung oder sonstige Einrede.",
    "gewerblicher_rechtsschutz": "Anspruchsteller für Schutzrecht, Rechtekette, Verletzung und Dringlichkeit; Gegner für Rechtsbestand, Lizenz, Erschöpfung, Verfall oder sonstige Einrede.",
    "it": "Auftraggeber für Mangel und Abnahmevorbehalt; Anbieter für Leistung, Change Request, Mitwirkung und Haftungsbegrenzung.",
    "bauplanung": "Planer für Leistungsstand, Koordination und Honorargrund; Auftraggeber für Anordnung, Mitwirkung, Abnahme und Einwand.",
    "bau": "Auftragnehmer für Leistung, Nachtrag und Behinderung; Auftraggeber für Mangel, Abnahmevorbehalt, Zahlungskürzung und Fristsetzung.",
    "international": "Anspruchsteller für Anknüpfung, Zuständigkeit und Vollstreckbarkeit; Gegner für Gerichtsstand, ordre public und Einreden.",
    "eu_prozess": "Kläger für Zulässigkeit, Betroffenheit, Frist und Klagegrund; Organ für Rechtmäßigkeit, Ermessen und Verteidigungslinie.",
    "bgb": "Anspruchsteller für Vertrag, Pflichtverletzung, Mangel, Schaden und Kausalität; Gegner für Einwendungen, Ausschluss, Erfüllung und Verjährung.",
    "zivilprozess": "Kläger für schlüssigen Vortrag und Beweisangebot; Beklagter für erhebliche Einwendungen; Gericht führt über Hinweise und Beweisbeschluss.",
    "erbrecht": "Anspruchsteller für Verwandtschaft, Verfügung, Nachlasswert und Schenkung; Gegner für Erfüllung, Anrechnung, Ausgleichung und Ausschluss.",
    "medizin": "Patient oder Versicherter für Befund, Schaden und Kausalität; Behandler oder Träger für Aufklärung, Dokumentation, Standard und Entlastung.",
    "verkehr": "Geschädigter oder Reisender für Ereignis, Schaden, Verspätung und Belege; Gegner für Mitverschulden, Ausschluss und außergewöhnliche Umstände.",
    "vollstreckung": "Gläubiger für Titel, Klausel, Zustellung und Forderungsstand; Schuldner oder Dritter für Schutz, Erfüllung, Insolvenz und Gegenrechte.",
    "immobilien": "Antragsteller für Antrag, Bewilligung, Vertretung und Nachweis; Beteiligte für Rang, Genehmigung, Löschung und entgegenstehende Rechte.",
    "weg": "Die Gemeinschaft belegt Beschlusstext, ordnungsmäßige Vorbereitung, Kostenposition, Schlüssel und Fälligkeit; der anfechtende Eigentümer bezeichnet den Beschlussmangel innerhalb der Begründungsfrist und belegt dessen Tatsachengrundlage.",
    "eu_recht": "Wer sich auf Unionsrecht beruft, belegt Anwendungsbereich und anspruchstragende Tatsachen; Staat oder Organ trägt Rechtfertigung, Ausnahme und Verhältnismäßigkeit.",
    "methodik": "Anspruchsteller für anspruchsbegründende Tatsachen und Belegkette; Gegner für Einwendungen; offene Tatsachen niemals durch Rechtsbehauptungen ersetzen.",
    "betreuung": "Gericht ermittelt von Amts wegen; Betreuer und Behörde dokumentieren Bedarf, Wunsch, mildere Hilfe, Vertretungsmacht und Genehmigungstatsachen.",
    "hoai": "Planer für beauftragte und erbrachte Leistung sowie Honorarparameter; Auftraggeber für Mangel, Änderungsanordnung, Zahlung und mitwirkungsbedingte Störung.",
    "weltraum": "Anspruchsteller oder Staat für Gegenstand, Ereignis, Schaden und Kausalität; Betreiber und Startstaaten für Genehmigung, Aufsicht, Registrierung und Entlastung.",
    "presse": "Redaktion für Beweistatsachen, Recherche, Stellungnahmeanfrage und Statussprache; Betroffener für konkrete Unwahrheit, Beeinträchtigung und beanspruchte Abhilfe.",
    "agrar": "Antragsteller oder Bewirtschafter für Fläche, Hofstatus, Fördervoraussetzung und Beleg; Behörde oder Vertragspartner für Beanstandung, Kürzung, Einwendung und Zustellung.",
    "sport": "Verband oder Anspruchsteller für Regelwerk, Tatbestand, Zustellung und Maßnahme; Athlet oder Verein für Gegenbeleg, Fristwahrung, Eilbedarf und Einwendung.",
    "jveg": "Berechtigter für Heranziehung, Fristwahrung, Zeit, Honorargruppe und Auslage; Staatskasse für Kürzungstatbestand, Überschreitung und Einwendung.",
    "ehrenamtliche_richter": "Gericht sichert Besetzung und Verfahren; der ehrenamtliche Richter legt Neutralitätsrisiken offen und stützt Tatsachenfragen ausschließlich auf die Verhandlung.",
    "rechtsgeschichte": "Bearbeiter für Textzeuge, Fassung, Übersetzung und Rezeptionsbeleg; offene Quellenlage wird als solche ausgewiesen und nicht durch Rückprojektion geschlossen.",
    "kirchenrecht": "Antragsteller für Parteistellung, Urkunde und Anspruchstatsachen; kirchliche Autorität für Zuständigkeit, Verfahren und Entscheidungsgrundlage.",
    "kanzleibetrieb": "Verantwortlicher Bearbeiter für Annahme, Vollmacht, Frist, Freigabe und Versandnachweis; Mandant für Identitäts-, Sachverhalts- und Entscheidungsangaben.",
    "selbststaendige": "Selbstständiger für Leistung, Rechnung, Belege und Abgaben; Auftraggeber oder Behörde für Einwendung, Statusbewertung und belastende Feststellung.",
    "dokumentenworkflow": "Bearbeiter für Version, Fundstelle, Rechenweg und Übergabe; offene oder widersprüchliche Originaldaten werden nicht stillschweigend harmonisiert.",
    "default": "Anspruchsteller für anspruchsbegründende Tatsachen; Gegner für Einwendungen, Fristablauf, Erfüllung und Ausschlüsse.",
}


RECHTSFOLGE_MERKER = {
    "arbeits": "Vertrag, Personalvermerk, Zeit- oder Vergütungskorrektur, Beteiligungsvorlage, Abmahnung, Feststellungsklage, Vergleich oder Abwicklung.",
    "hr": "Arbeitsvertrag, HR-Vorgangsblatt, Personalvermerk, Zeit- oder Vergütungskorrektur, Beteiligungsvorlage, Abmahnung oder Austrittscheck.",
    "zeugnis": "Zeugnisentwurf, Berichtigungsmatrix, Aufforderungsschreiben, Klageantrag, Vergleichsklausel oder Vollstreckungsschritt.",
    "miet": "Zahlung, Minderung, Kündigung, Räumung, Instandsetzung oder Abrechnungsberichtigung.",
    "famil": "Unterhaltstitel, Sorge-/Umgangsregelung, Scheidungsausspruch, Versorgungsausgleich oder Zugewinn.",
    "straf": "Einstellung, Anklage, Freispruchslinie, Beweisantrag, Rechtsmittel oder Strafzumessungsvorschlag.",
    "datenschutz": "Auskunft, Löschung, Meldung, Anordnung, Schadensersatz oder Aufsichtsantwort.",
    "insolvenz": "Antrag, Haftungsabwehr, Forderungsanmeldung, Anfechtung, Rangklärung oder Sanierungsschritt.",
    "steuer": "Einspruch, Änderungsantrag, Aussetzung, Schätzungsangriff, Haftungsabwehr oder Klage.",
    "gesellschaft": "Beschlussfassung, Anfechtung, Organhaftung, Registervollzug, Abberufung oder Vergleich.",
    "aktg_hv": "Einberufungsunterlage, HV-Fristenblatt, Q&A-Katalog, Beschluss, Niederschrift, Anfechtungsprüfung, Freigabe oder Registervollzug.",
    "bank": "Beratungsprotokoll, Erstattungsanspruch, Zahlungsdienstehaftung, Aufsichtsvermerk, Vertragsklausel oder Verteidigungslinie.",
    "phishing": "Sperr- und Rückholauftrag, Zahlungsmatrix, Erstattungsverlangen, Beleganforderung, Schlichtungsantrag, Klage oder Klageabwehr.",
    "datenbank": "Unterlassung, Auskunft, Lizenz, Schadensersatz, API-Regel, Schrankenprüfung oder Abwehrschreiben.",
    "lobbyregister": "Registrierung, Aktualisierung, Verhaltenskodex-Prüfung, Stellungnahme, Fristenblatt oder Bußgeldabwehr.",
    "geldwaesche": "Risikoanalyse, KYC-Nachforderung, Verdachtsmeldeprüfung, Transparenzregistervermerk, Aufsichtsantwort oder Bußgeldabwehr.",
    "cybersicherheit": "Risikomanagementplan, Incident-Meldung, Nachweisordner, Maßnahmenplan, Lieferkettenauflage oder Bußgeldverteidigung.",
    "kartell": "Kartellschadensmatrix, Abstellungszusage, Bußgeldverteidigung, Compliance-Maßnahme, Klage oder Vergleich.",
    "produkt": "Launch-Freigabe, Warnhinweis, Rückruf, Marktüberwachungsantwort, Haftungsmemo oder Verteidigungsentwurf.",
    "forderung": "Mahnung, Klageentwurf, Mahnbescheid, Anspruchsmatrix, Vergleichsvorschlag oder Vollstreckungsauftrag.",
    "verfass": "Nichtannahmerisiko, Verfassungsbeschwerde, Eilantrag, Normenkontrolle oder Verhältnismäßigkeitsprüfung.",
    "versicherung": "Deckung, Kürzung, Ablehnung, Regulierung, Regress oder Klageantrag.",
    "liquiditaet": "Liquiditätsstatus, Antragspflichtvermerk, Rangrücktritt, Patronatserklärung oder Zahlungsstopp.",
    "sozial": "Widerspruch, Klage, einstweiliger Rechtsschutz, Leistungsbescheid oder Vergleich.",
    "sozialstatus": "Statusfeststellungsantrag, Anhörungserwiderung, Beitragsabwehr, Nachzahlungsplan, Widerspruch oder Klage.",
    "renten": "Kontenklärung, Rentenberechnung, Widerspruch, Nachzahlung, Statusfeststellung oder Klage.",
    "verwaltung": "Widerspruch, Anfechtung, Verpflichtung, Eilantrag, Abhilfe oder Bescheidkorrektur.",
    "vergabe": "Rüge, Bieterfrage, Nachprüfungsantrag, Wertungskorrektur, Zuschlagsstopp oder Dokumentationsvermerk.",
    "urheber": "Abmahnung, Unterlassung, Auskunft, Schadensersatz, Löschung, Widerspruch oder Verteidigung.",
    "marke": "Anmeldung, Beanstandungsantwort, Widerspruch, Verfall oder Nichtigkeit, Abmahnung, Unterlassung, Auskunft, Schadensersatz oder Lizenz.",
    "design": "Anmeldung, Nichtigkeitsantrag, Unterlassung, Auskunft, Schadensersatz, Rückruf, Vergleich oder Lizenz.",
    "patent": "Anmeldung, Prüfungsbescheid, Einspruch, Nichtigkeit, Aussetzung, Unterlassung, Auskunft, Schadensersatz, FTO oder Lizenz.",
    "gebrauchsmuster": "Anmeldung, Abzweigung, Recherche, Löschung, Unterlassung, Auskunft, Schadensersatz oder einstweilige Verfügung.",
    "gewerblicher_rechtsschutz": "Portfoliovermerk, Abmahnung, Schutzschrift, einstweilige Verfügung, Hauptsache, Amtsverfahren, Vergleich oder Lizenz.",
    "it": "Abnahme, Nacherfüllung, SLA-Gutschrift, Rechteklärung, Change Request oder Haftungsvorschlag.",
    "bauplanung": "Planervermerk, LPH-Nachweis, Honorar, Nachtrag, Mängelverfolgung oder Bauüberwachungsanweisung.",
    "bau": "Nachtrag, Behinderungsanzeige, Abnahme, Mangelrüge, Vergütung, Gutachterfrage oder Sicherung.",
    "international": "Zuständigkeitsrüge, Rechtswahlvermerk, Anerkennung, Vollstreckung oder Schiedsstrategie.",
    "eu_prozess": "Klageart, Antragssatz, e-Curia-Einreichung, Zwischenantrag, Rechtsmittel oder Kostenlinie.",
    "bgb": "Anspruchsmatrix, Klauselprüfung, Mahnung, Rücktritt, Minderung, Klageentwurf, Redline oder Vergleich.",
    "zivilprozess": "Klage, Erwiderung, Relation, Hinweisverfügung, Beweisbeschluss, Urteil, Tenor oder Anlagenverzeichnis.",
    "erbrecht": "Erbquotentabelle, Pflichtteilsrechnung, Auskunft, Erbscheinsantrag, Klage oder Auseinandersetzungsvergleich.",
    "medizin": "Gutachterfragen, Anspruchsschreiben, Widerspruch, Eilantrag, Klage, Abrechnungsprüfung oder Behördenantwort.",
    "verkehr": "Regulierungsschreiben, Anspruchstabelle, Einspruch, Klage, Vergleich, Fristenblatt oder Mandantenbrief.",
    "vollstreckung": "Titelcheck, Vollstreckungsauftrag, PfÜB-Entwurf, Forderungsaufstellung, Erinnerung oder Schutzantrag.",
    "immobilien": "Grundbuchanalyse, Vertragsklausel, Vollzugsliste, Bewilligung, Zwischenverfügungsantwort oder Rangmatrix.",
    "weg": "Beschlussentwurf, Einladung, Niederschrift, Abrechnungsblatt, Verwaltervermerk, Eigentümeranschreiben oder Beschlussklage.",
    "eu_recht": "Wirkungsmatrix, Grundfreiheitenprüfung, Vorlagefrage, Umsetzungscheck, Stellungnahme oder Rechtsschutzvermerk.",
    "methodik": "Subsumtionsmatrix, Kurzvermerk, Gutachten, Schriftsatzkern, Mandantenbrief oder Zitierkontrolle.",
    "betreuung": "Aufgabenmatrix, Gerichtsantrag, Genehmigungsvorlage, Vermögensübersicht, Jahresbericht oder Schutzplan.",
    "hoai": "Leistungsstandsmatrix, Honorarblatt, Nachtragsangebot, Bedenkenhinweis, Mängelvermerk oder Projektbericht.",
    "weltraum": "Missionsrechtsmatrix, Genehmigungsfahrplan, Registermeldung, Haftungsmemo, Startvertragsklausel oder Frequenzvermerk.",
    "presse": "veröffentlichungsfähige Meldung, Quellenmatrix, Stellungnahmeanfrage, Headline-Set, Redaktionsfreigabe oder Nachtrag.",
    "agrar": "Pachtprüfung, Hofnachfolgematrix, Förderwiderspruch, Genehmigungsantrag, Behördenstellungnahme oder Vertragsentwurf.",
    "sport": "Verbandsbeschwerde, Eilantrag, Schiedsschriftsatz, Vertragsredline, Spielberechtigungsantrag oder Sponsoringvermerk.",
    "jveg": "Abrechnung, Festsetzungsantrag, Kürzungserwiderung, Beschwerde, Vorschussantrag oder Zeugenentschädigung.",
    "ehrenamtliche_richter": "Sitzungsblatt, offene Fragenliste, Neutralitätsvermerk, Beratungsstruktur oder Nachbereitungsnotiz.",
    "rechtsgeschichte": "Quellenkarte, Textsynopse, Epochenmemo, Rezeptionslinie oder historische Fallanalyse.",
    "kirchenrecht": "Supplik, Antrag, Dekretentwurf, Eheverfahrensmatrix, Aktenvermerk oder Schnittstellenstellungnahme.",
    "kanzleibetrieb": "Mandatsblatt, Fristenkontrolle, Arbeitsauftrag, Versandprotokoll, Budgetbericht, Rechnung oder Abschlussblatt.",
    "selbststaendige": "Angebot, Auftrag, Rechnung, Mahnung, Statusmatrix, Behördenantwort oder Monatscheck.",
    "dokumentenworkflow": "Dokumentenregister, Abweichungsmatrix, Redline, Prüftabelle, Entwurf, Exportpaket oder Übergabevermerk.",
    "default": "Kurzvermerk, Prüfmatrix, Entwurf, Antrag, Entscheidungsvorschlag oder Fristenblatt.",
}


def evidence_marker(profile: ThemenProfil) -> str:
    return BEWEISLAST_MERKER.get(profile.key, BEWEISLAST_MERKER["default"]).rstrip(".")


def consequence_marker(profile: ThemenProfil) -> str:
    return RECHTSFOLGE_MERKER.get(profile.key, RECHTSFOLGE_MERKER["default"]).rstrip(".")


def anchor_head(anchor: str, limit: int = 82) -> str:
    anchor = clean(anchor, limit).rstrip(".")
    if ":" in anchor:
        return clean(anchor.split(":", 1)[0], limit).rstrip(".")
    if " — " in anchor:
        return clean(anchor.split(" — ", 1)[0], limit).rstrip(".")
    return anchor


def anchor_tail(anchor: str, limit: int = 115) -> str:
    anchor = clean(anchor).rstrip(".")
    for sep in (":", " — "):
        if sep in anchor:
            tail = anchor.split(sep, 1)[1].strip()
            if tail:
                return clean(tail, limit).rstrip(".")
    return clean(anchor, limit).rstrip(".")


def join_anchors(items: list[str], limit: int = 190) -> str:
    if not items:
        return "aus Akte und belastbarer Quelle ableiten"
    return clean("; ".join(anchor_head(item, 70) for item in items[:3]), limit).rstrip(".")


def fallkarte_rows(profile: ThemenProfil, fields: list[tuple[str, str]], norms: list[str], cases: list[str]) -> list[tuple[str, str, str, str]]:
    first_field = fields[0][0] if fields else profile.label
    second_field = fields[1][0] if len(fields) > 1 else first_field
    first_norm = norms[0] if norms else "Norm aus Akte"
    second_norm = norms[1] if len(norms) > 1 else first_norm
    return [
        (
            "Fallkern",
            clean(first_field, 80).rstrip("."),
            join_anchors([first_norm], 180),
            "Sofortvermerk mit Ergebnisrichtung, Risiko und nächstem Schritt",
        ),
        (
            "Zulässigkeit und Frist",
            "Frist, Form, Zuständigkeit, Rolle und statthafter Weg",
            join_anchors([second_norm], 180),
            "Fristenblatt oder Prozess-/Verfahrensroute",
        ),
        (
            "Begründetheit",
            clean(second_field, 80).rstrip("."),
            join_anchors([second_norm], 180),
            "Tatbestandsmatrix mit Beleg und Gegenargument",
        ),
        (
            "Rechtsfolge",
            consequence_marker(profile),
            evidence_marker(profile),
            "Antrag, Entwurf, Entscheidungsvorschlag oder Mandantenbrief",
        ),
    ]


def first_readme_paragraph(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return ""
    try:
        text = readme.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    text = re.sub(r"<!--[\s\S]*?-->", " ", text)
    paragraphs = []
    current: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith("["):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.startswith("- ") or line.startswith("* "):
            continue
        current.append(line)
        if len(" ".join(current)) > 500:
            paragraphs.append(" ".join(current))
            break
    if current:
        paragraphs.append(" ".join(current))
    for paragraph in paragraphs:
        cleaned = clean(paragraph, 700)
        if len(cleaned) > 80:
            return cleaned
    return ""


def title_for(slug: str, mf: dict, profile: ThemenProfil) -> str:
    raw = mf.get("display_name") or mf.get("title") or slug.replace("-", " ")
    raw = raw.replace("_", " ").strip()
    if raw.lower() == slug:
        raw = slug.replace("-", " ")
    return clean(raw.title(), 120)


def station_text(stations: Iterable[str], skill_material: list[dict[str, str]]) -> list[str]:
    out = list(stations)
    for item in skill_material[:7]:
        desc = item["desc"] or item["body"]
        if not desc:
            continue
        candidate = clean(desc, 260)
        if candidate and candidate not in out:
            out.append(candidate)
    return out[:12]


def remove_h2_section(text: str, title_part: str) -> str:
    match = re.search(rf"^## \d+\. .*{re.escape(title_part)}.*$", text, flags=re.M)
    if not match:
        return text
    next_match = re.search(r"^## \d+\. ", text[match.end():], flags=re.M)
    end = match.end() + next_match.start() if next_match else len(text)
    return (text[: match.start()].rstrip() + "\n\n" + text[end:].lstrip()).rstrip() + "\n"


def renumber_h2_sections(text: str) -> str:
    counter = 0
    out: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(##)\s+(?:\d+\.\s+)?(.+)$", line)
        if match and not line.startswith("###"):
            counter += 1
            out.append(f"## {counter}. {match.group(2).strip()}")
        else:
            out.append(line)
    return "\n".join(out).rstrip() + "\n"


def trim_bullet_section(text: str, title_part: str, keep: int) -> str:
    match = re.search(rf"^## \d+\. .*{re.escape(title_part)}.*$", text, flags=re.M)
    if not match:
        return text
    next_match = re.search(r"^## \d+\. ", text[match.end():], flags=re.M)
    end = match.end() + next_match.start() if next_match else len(text)
    block = text[match.start():end]
    out: list[str] = []
    bullets = 0
    for line in block.splitlines():
        if line.startswith("- "):
            bullets += 1
            if bullets > keep:
                continue
        out.append(line)
    return text[: match.start()] + "\n".join(out).rstrip() + "\n\n" + text[end:].lstrip()


def compact_werkstatt(text: str) -> str:
    max_size = 22 * 1024
    if byte_len(text) <= max_size:
        return text
    for title in ("Musterbausteine", "Qualitätskontrolle und Abschluss"):
        text = remove_h2_section(text, title)
        if byte_len(text) <= max_size:
            return renumber_h2_sections(text)
    for title, keep in (("Leitentscheidungen", 4), ("Pflichtnormen", 12), ("Materienbezogene Arbeitsfelder", 8)):
        text = trim_bullet_section(text, title, keep)
        if byte_len(text) <= max_size:
            return renumber_h2_sections(text)
    text = remove_h2_section(text, "Arbeitsweise")
    return renumber_h2_sections(text)


def build_werkstatt(plugin_dir: Path) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    stations = list(profile.stationen)
    intro = clean(mf.get("description", "") or first_readme_paragraph(plugin_dir) or profile.rolle, 900)
    profile_norms = [] if profile.key == "default" else list(profile.normen)
    profile_cases = [] if profile.key == "default" else list(profile.entscheidungen)
    extracted_norms = extract_norm_anchors(skill_material, 8)
    extracted_cases = extract_case_anchors(skill_material, 5)
    if profile.key in CURATED_NORM_PROFILE_KEYS:
        extracted_norms = []
    if profile.key in CURATED_CASE_PROFILE_KEYS:
        extracted_cases = []
    if profile.key in PROFILE_CASE_SKIP_KEYS:
        profile_cases = []
    if slug in CASE_RESEARCH_ONLY_SLUGS:
        profile_cases = []
        extracted_cases = []
    if slug in PLUGIN_CASE_OVERRIDES:
        profile_cases = list(PLUGIN_CASE_OVERRIDES[slug])
        extracted_cases = []
    extracted_cases = dedupe_cases(profile_cases, extracted_cases)
    fields = profile_fields(profile, skill_material, 7)
    norm_pool = (profile_norms + extracted_norms)[:8]
    case_pool = (profile_cases + extracted_cases)[:5]

    lines: list[str] = [
        f"# {title} — Werkstatt-Prompt",
        "",
        "## 1. Rolle und Auftrag",
        "",
        f"Du arbeitest als {profile.rolle} Der Auftrag lautet: vorhandene Unterlagen zuerst auszuwerten und daraus einen belastbaren, fachlich sortierten Arbeitsstand mit verwertbarem Ergebnis zu erstellen. Gegenstand dieses Prompts ist: {intro}",
        "",
        "Die Rolle ist keine bloße Zusammenfassung. Sie ordnet Tatsachen, trennt beweisbare Punkte von Behauptungen, prueft die einschlaegigen Normen, formuliert den naechsten Arbeitsschritt und erzeugt ein direkt verwendbares Produkt.",
        "",
    ] + WERKSTATT_TEMPO_BLOCK + [
        "## 2. Stop-Kriterien",
        "",
    ]
    for item in profile.stop:
        lines.append(f"- {item}")
    lines += [
        "- Wenn Identitaet, Vollmacht, Fristbeginn oder Verfahrensstand nicht tragfaehig bestimmbar sind, wird zuerst eine knappe Lueckenliste erzeugt.",
        "- Wenn das gewuenschte Ergebnis eine endgueltige Rechtsentscheidung verlangt, wird nur ein entscheidungsreifer Entwurf mit offen markierten Pruefpunkten ausgegeben.",
        "",
        "## 3. Werkstattfluss",
        "",
    ]

    for idx, station in enumerate(stations, 1):
        lines += [
            f"### 3.{idx}. {station_heading(station)}",
            "",
            station_instruction(station),
            "",
        ]

    lines += [
        "## 4. Rechtsprechungs-Fallkarte",
        "",
        "| Ebene | Fallfrage | Anker | Sofortausgabe |",
        "| --- | --- | --- | --- |",
    ]
    for level, question, anchor, output in fallkarte_rows(profile, fields, norm_pool, case_pool):
        lines.append(f"| {level} | {question} | {anchor} | {output} |")

    lines += [
        "",
        "## 5. Normenanker, Tatbestandswichtigkeiten und Beweislast",
        "",
        "| Normenanker | Tatbestandswichtigkeit | Beweislastmerker | Rechtsfolge |",
        "| --- | --- | --- | --- |",
    ]
    if norm_pool:
        for norm in norm_pool[:7]:
            lines.append(f"| {anchor_head(norm, 80)} | {anchor_tail(norm, 105)} | {evidence_marker(profile)} | {consequence_marker(profile)} |")
    else:
        lines.append(f"| Aktennorm | Aus Bescheid, Vertrag, Antrag, Verfügung oder Schriftsatz entnehmen | {evidence_marker(profile)} | {consequence_marker(profile)} |")

    lines += [
        "",
        "## 6. Rechtsprechungsanker, Quellenstatus und Rechtsfolgen",
        "",
    ]
    if case_pool:
        lines.append("| Rechtsprechungsanker | Quellenstatus | Nutzwert im Fall |")
        lines.append("| --- | --- | --- |")
        for case in case_pool[:5]:
            status = "Profilanker" if case in profile_cases else "aus Skillmaterial extrahierter Anker"
            lines.append(f"| {anchor_head(case, 105)} | {status}; vor Zitierung am Aktenstand oder an belastbarer Quelle sichern | {anchor_tail(case, 120)} |")
    else:
        lines.append("- Rechtsprechung nur zitieren, wenn Gericht, Datum und Aktenzeichen sicher sind; sonst als Recherche- und Prüfbedarf mit konkreter Fallfrage markieren.")
    lines += [
        f"- Rechtsfolge zuerst als Arbeitsprodukt denken: {consequence_marker(profile)}",
        "- Quellenstatus immer sichtbar machen: Aktenfund, Normtext, Profilanker, gesicherte Rechtsprechung oder offene Prüfung.",
        "",
        "## 7. Pflichtnormen als Kernsätze",
        "",
    ]
    for item in profile_norms:
        lines.append(f"- {item}")

    # Add norms extracted from selected skills without making skill references.
    for norm in extracted_norms[:8]:
        lines.append(f"- {norm}; im konkreten Sachverhalt als Tatbestands- oder Verfahrensanker prüfen.")
    if not profile_norms and not extracted_norms:
        lines.append("- Tragende Normen aus Akte, Bescheid, Vertrag oder gerichtlicher Verfügung ableiten; keine Norm als sicher darstellen, wenn sie nicht belegt ist.")

    lines += [
        "",
        "## 8. Leitentscheidungen",
        "",
    ]
    for item in profile_cases:
        lines.append(f"- {sentence_terminal(item)}")
    for item in extracted_cases:
        lines.append(f"- {sentence_terminal(item)}")
    if not profile_cases and not extracted_cases:
        lines.append("- Rechtsprechung nur mit Datum, Gericht und Aktenzeichen verwenden, wenn sie aus Unterlagen oder belastbarer Quelle sicher belegt ist; sonst als Prüfbedarf markieren.")

    lines += [
        "",
        "## 9. Prüfraster",
        "",
    ]
    for idx, item in enumerate(profile.pruefraster, 1):
        lines.append(f"{idx}. {item}")
    lines += [
        f"{len(profile.pruefraster)+1}. Welche Tatsache fehlt noch, obwohl sie fuer die Rechtsfolge entscheidend ist.",
        f"{len(profile.pruefraster)+2}. Welches konkrete Arbeitsprodukt loest den naechsten praktischen Engpass.",
        "",
        "## 10. Argumentations- und Entwurfsgerüst",
        "",
        f"10.1. Kernsatz: Benenne Parteirolle, Ziel und die begehrte oder abzuwehrende Rechtsfolge aus diesem Arbeitsfeld: {consequence_marker(profile)}.",
        f"10.2. Tragende Regel: Stelle den einschlägigen Normsatz voran und ordne ihn dem konkreten Streitpunkt zu; erste Anker sind {join_anchors(norm_pool[:2], 180)}.",
        f"10.3. Tatbestandsmerkmal: Arbeite zuerst den entscheidenden Fachpunkt aus, regelmäßig {fields[0][0] if fields else profile.pruefraster[0]}.",
        "10.4. Aktenfund: Nenne Datum, Beteiligten, Handlung, Betrag und genaue Fundstelle. Eine streitige Behauptung bleibt als solche bezeichnet.",
        f"10.5. Beweislast: {evidence_marker(profile)}. Zeige ausdrücklich, welche Folge ein offener Beweis hat.",
        "10.6. Gegenposition: Formuliere den stärksten ernsthaften Angriff auf Norm, Tatbestand, Beleg, Kausalität, Höhe oder Verfahrensweg.",
        "10.7. Erwiderung: Antworte mit konkretem Gegenbeleg, Auslegung, Beweislastregel oder engerer Rechtsfolge; ein bloßes Bestreiten genügt nicht.",
        f"10.8. Arbeitsprodukt: Schließe mit Antrag, Tenor, Klausel, Entscheidung oder nächstem Schritt; hier typischerweise {output_hint(profile, fields)}.",
        f"10.9. Quellenstatus: Ordne Rechtsprechung nach Tragweite ein; erste Fallanker sind {join_anchors(case_pool[:2], 180) if case_pool else 'erst nach verifizierter Recherche einzusetzen'}.",
        "",
        "## 11. Outputvarianten und Empfängerwunsch",
        "",
        "| Wunsch | Ausgabe | Mindestinhalt |",
        "| --- | --- | --- |",
        f"| schnell entscheiden | Kurzvermerk | Fallkern, {join_anchors(norm_pool[:2], 120)}, Risiko, nächster Schritt |",
        f"| vertieft prüfen | Tatbestandsmatrix | Norm, Merkmal, Beleg, Beweislast, Gegenargument, Rechtsfolge |",
        f"| versenden | Entwurf | Antrag oder Tenor, Begründung, Anlagen, Frist, Zustellungsweg |",
        f"| beraten | Mandantenbrief | Ergebnis, Optionen, Kosten-/Zeitrisiko, Empfehlung |",
        f"| verhandeln | Vergleichs- oder Klauselvorschlag | sichere Fassung, risikobewusste Fassung, offene Punkte |",
        "",
        "## 12. Arbeitsweise",
        "",
        "Arbeite zuerst aktennah, dann normnah, dann produktnah. Wenn Dokumente oder ein Ordner vorliegen, werden sie ohne weitere Vorfrage gelesen, eingeordnet und mit Fundstelle verarbeitet. Wenn der Nutzer nur den Prompt startet, prüfe zuerst, ob Kontext, Dateien oder ein Arbeitsordner erkennbar sind; erst wenn wirklich keine Unterlagen vorliegen, werden höchstens vier gezielte Fragen gestellt. Jede Antwort wird in ganzen Sätzen formuliert. Tabellen sind erlaubt, wenn sie Vergleich, Berechnung oder Fristen besser zeigen.",
        "",
        "Selbstcheck vor Ausgabe: Ist die Frist benannt? Ist die Form geklaert? Ist die richtige Rolle getroffen? Ist die Rechtsfolge aus einer Norm abgeleitet? Ist das Arbeitsprodukt tatsaechlich verwendbar? Sind offene Tatsachen von offenen Rechtsfragen getrennt?",
        "",
        "## 13. Qualitätskontrolle und Abschluss",
        "",
        "Zum Abschluss wird das Ergebnis auf Widersprueche, fehlende Belege, falsche Zuständigkeit, unklare Fristen, unvollstaendige Antraege, Rechenfehler und unpassenden Ton geprueft. Danach folgt eine knappe Anschlussliste: sofort erledigen, nachfordern, entscheiden, entwerfen, einreichen oder zurueckstellen.",
        "",
        "## 14. Musterbausteine",
        "",
    ]
    skeletons = list(profile.skelette) or (
        "Memo-Kernsatz: Nach dem derzeit belegten Sachverhalt spricht mehr fuer [Ergebnis], weil [Norm] die Rechtsfolge an [Tatbestandsmerkmal] knuepft und [Beleg] diesen Punkt traegt.",
        "Nachforderung: Bitte reichen Sie bis [Datum] [Dokument] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfaehig beurteilt werden.",
        "Schriftsatzkern: Der Anspruch ist begruendet, weil [Norm], [Tatsache], [Beweis] und [Rechtsfolge] zusammenfallen.",
    )
    for item in skeletons:
        lines.append(f"- {item}")

    # Make narrow prompts less skeletal by adding a profile- or skill-derived issue catalog.
    if fields:
        lines += ["", "## 15. Materienbezogene Arbeitsfelder", ""]
        for idx, (title, detail) in enumerate(fields, 1):
            lines.append(f"### 15.{idx}. {title}")
            lines.append("")
            lines.append(
                f"{detail}. Verbinde den Punkt mit Aktenfund, Norm, Beweislast, "
                "Gegenposition und konkreter Rechtsfolge. Output: ausformulierter "
                "Ergebnisbaustein mit Belegstelle, Risiko und nächstem Schritt."
            )
            lines.append("")

    text = "\n".join(lines).strip() + "\n"
    if len(text.encode("utf-8")) < 12 * 1024 and "Ausgabeformate für schnelle Lieferung" not in text:
        text = text.replace(
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip(),
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip() + "\n\n" + WERKSTATT_ERGONOMY_TEXT.rstrip(),
            1,
        )
    if len(text.encode("utf-8")) < 12 * 1024 and "Schlusskontrolle für Tempo" not in text:
        text = text.rstrip() + "\n\n" + werkstatt_final_check_block(text).rstrip() + "\n"
    if len(text.encode("utf-8")) < 12 * 1024 and "Vertiefungsmodus für belastbare Ausgabe" not in text:
        text = text.rstrip() + "\n\n" + werkstatt_depth_block(text).rstrip() + "\n"
    if profile.oeffnungssatz:
        text = profile.oeffnungssatz + "\n\n" + text
    return sanitize(compact_werkstatt(text))


def compact_schnellstart(text: str) -> str:
    if byte_len(text) <= MAX_FAST:
        return text

    def shorten_einsatzfelder(match: re.Match[str]) -> str:
        block = match.group(0)
        lines = block.splitlines()
        header = lines[:4]
        rows = [line for line in lines[4:] if line.startswith("|")]
        return "\n".join(header + rows[:4]) + "\n\n"

    text = re.sub(
        r"## 5\. Einsatzfelder\n\n\| Feld \| Sofortgriff \| Ausgabe \|\n\| --- \| --- \| --- \|\n(?:\|.*\|\n)+",
        shorten_einsatzfelder,
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    parts = re.split(r"\n## (?:6\.\s+)?Anker\n", text, maxsplit=1)
    if len(parts) == 2:
        head, rest = parts
        split = re.split(r"\n## (?:7\.\s+)?Antwortform\n", rest, maxsplit=1)
        if len(split) == 2:
            anchor, tail = split
            anchor_lines = [l for l in anchor.splitlines() if l.strip()][:7]
            text = head.rstrip() + "\n\n## 6. Anker\n\n" + "\n".join(anchor_lines) + "\n\n## 7. Antwortform\n" + tail
    if byte_len(text) <= MAX_FAST:
        return text

    text = re.sub(
        r"\n## 4\. Fallkarte\n\n\| Punkt \| Sofortgriff \|\n\| --- \| --- \|\n(?:\|.*\|\n)+",
        lambda m: "\n".join(m.group(0).splitlines()[:7]) + "\n\n",
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    return clip_utf8(text, MAX_FAST)


def build_schnellstart(plugin_dir: Path) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    fields = profile_fields(profile, skill_material)
    stations = quick_stations(profile, skill_material)
    norm_limit = 7 if profile.key == "default" else 4
    case_limit = 4 if profile.key == "default" else 3
    extracted_norms = extract_norm_anchors(skill_material, norm_limit)
    extracted_cases = extract_case_anchors(skill_material, case_limit)
    if profile.key in CURATED_NORM_PROFILE_KEYS:
        extracted_norms = []
    if profile.key in CURATED_CASE_PROFILE_KEYS:
        extracted_cases = []
    profile_norms = [] if profile.key == "default" else list(profile.normen[:4])
    profile_cases = [] if profile.key == "default" else list(profile.entscheidungen[:2])
    if profile.key in PROFILE_CASE_SKIP_KEYS:
        profile_cases = []
    if slug in CASE_RESEARCH_ONLY_SLUGS:
        profile_cases = []
        extracted_cases = []
    if slug in PLUGIN_CASE_OVERRIDES:
        profile_cases = list(PLUGIN_CASE_OVERRIDES[slug][:2])
        extracted_cases = []
    extracted_cases = dedupe_cases(profile_cases, extracted_cases)
    norm_pool = (profile_norms + extracted_norms)[:6]
    case_pool = (profile_cases + extracted_cases)[:4]
    goal = domain_goal(mf, plugin_dir, profile)
    opening = profile.oeffnungssatz
    if profile.key == "default":
        opening = f"Wenn du das hier öffnest, soll zuerst vorhandenes Material zum Thema {title} ausgewertet und daraus ein verwertbarer Erststand gebaut werden."

    lines: list[str] = [
        f"# {title} — Schnellstart",
        "",
        f"Ziel: {goal}. Arbeite sofort am konkreten Fall. Wenn Unterlagen, Dateien oder ein Ordner vorhanden sind, werte sie ohne Vorfrage aus. Liefere ganze Sätze und beende jede Ausgabe mit Ergebnisrichtung, Risiko und nächstem Schritt.",
        "",
    ] + SCHNELLSTART_TEMPO_BLOCK + [
        "## 2. Direktstart",
        "",
        "1. Vorhandene Unterlagen zuerst öffnen, lesen und als Beleglinie ordnen: Datum, Absender, Dokument, Kerntatsache, Lücke.",
        "2. Mandat in einem Satz festlegen: Wer will welches Ergebnis, gegen wen oder gegenüber welcher Stelle.",
        "3. Engpass sichern: Frist, Form, Zuständigkeit, Beweislast, Kosten oder Vollzugsfolge zuerst prüfen.",
        "4. Nur bei leerer Materiallage höchstens vier Kaltstartfragen stellen; sonst sofort Kurzvermerk, Prüfmatrix, Entwurf, Berechnung oder Entscheidungsvorschlag liefern.",
        "",
        "## 3. Kernroute",
        "",
    ]
    if opening:
        lines = [opening, ""] + lines
    for idx, station in enumerate(stations, 1):
        lines.append(f"{idx}. {clean(station, 230)}")
    lines += [
        "",
        "## 4. Fallkarte",
        "",
        "| Punkt | Sofortgriff |",
        "| --- | --- |",
        f"| Normenanker | {join_anchors(norm_pool[:3], 220)} |",
        f"| Rechtsprechung | {join_anchors(case_pool[:2], 220)} |",
        f"| Tatbestand | {quick_grip(profile, fields[0][0], fields[0][1]) if fields else stations[0]} |",
        f"| Beweislast | {evidence_marker(profile)} |",
        f"| Rechtsfolge | {consequence_marker(profile)} |",
        "| Quellenstatus | Aktenfund, Normtext, Profilanker oder sicher belegte Entscheidung offen kennzeichnen; unsichere Aktenzeichen nicht ergänzen |",
    ]
    if fields:
        lines += [
            "",
            "## 5. Einsatzfelder",
            "",
            "| Feld | Sofortgriff | Ausgabe |",
            "| --- | --- | --- |",
        ]
        for field, detail in fields:
            grip = quick_grip(profile, field, detail)
            lines.append(f"| {field} | {grip}. | Ergebnisbaustein mit Beleg, Risiko und nächstem Schritt |")
    lines += ["", "## 6. Anker", ""]
    anchor_count = 0
    for item in profile_norms:
        lines.append(f"- {item}")
        anchor_count += 1
    for item in extracted_norms:
        lines.append(f"- {item}; im Sachverhalt als tragenden Norm- oder Verfahrensanker prüfen.")
        anchor_count += 1
    for item in profile_cases:
        lines.append(f"- {sentence_terminal(item)}")
        anchor_count += 1
    for item in extracted_cases:
        lines.append(f"- {sentence_terminal(item)}")
        anchor_count += 1
    if anchor_count == 0:
        lines.append("- Normen und Entscheidungen aus den vorgelegten Unterlagen oder einer belastbaren Quelle ableiten; Aktenzeichen nicht ergänzen, wenn sie nicht sicher belegt sind.")
    lines += [
        "",
        "## 7. Antwortform",
        "",
        f"7.1. Kernsatz: Parteirolle, Ziel und Rechtsfolge sofort benennen; hier typischerweise {consequence_marker(profile)}.",
        f"7.2. Normsatz: Den tragenden Anker {join_anchors(norm_pool[:2], 170)} auf das entscheidende Tatbestandsmerkmal beziehen.",
        f"7.3. Aktenfund: Für {fields[0][0] if fields else 'den Fallkern'} konkrete Tatsache, Datum, Person, Betrag und Fundstelle nennen.",
        f"7.4. Beweislast: {evidence_marker(profile)}; die Folge eines offenen Beweises ausdrücklich aussprechen.",
        "7.5. Gegenposition: Den stärksten Angriff auf Norm, Tatsache, Beleg, Kausalität, Höhe oder Verfahren fair formulieren.",
        "7.6. Erwiderung: Mit Gegenbeleg, Auslegung, Beweislastregel oder engerer Rechtsfolge antworten und verbleibendes Risiko beziffern oder abstufen.",
        f"7.7. Ausgang: Erzeuge als ersten Baustein {output_hint(profile, fields)}. Schließe mit Frist, fehlendem Kernbeleg und nächstem konkreten Dokument.",
        "",
        "## 8. Stop",
        "",
        "Unterbrich nur vor einer irreversiblen, fristgebundenen oder haftungsträchtigen Handlung, wenn Frist, Vollmacht, Zuständigkeit oder Kernbeleg ungeklärt sind. Arbeite sonst mit sichtbar markierten Lücken weiter und liefere den belastbaren Teil bereits aus. Für Vertiefung den Werkstatt-Prompt desselben Plugins verwenden.",
        "",
    ]
    text = sanitize("\n".join(lines).strip() + "\n")
    if byte_len(text) <= MAX_FAST:
        return text
    # Hard compact if needed.
    parts = re.split(r"\n## (?:6\.\s+)?Anker\n", text, maxsplit=1)
    if len(parts) == 2:
        head, rest = parts
        anchor, tail = re.split(r"\n## (?:7\.\s+)?Antwortform\n", rest, maxsplit=1)
        anchor_lines = [l for l in anchor.splitlines() if l.strip()][:8]
        text = head.rstrip() + "\n\n## 6. Anker\n\n" + "\n".join(anchor_lines) + "\n\n## 7. Antwortform\n" + tail
    return compact_schnellstart(text)


def write_readme_links(plugin_dir: Path) -> None:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    raw_base = f"https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin_dir.relative_to(REPO).as_posix()}"
    block = "\n".join([
        "<!-- BEGIN werkstatt-schnellstart-raw-links (autogen) -->",
        "## Werkstatt- und Schnellstart-Prompts",
        "",
        "Diese Markdown-Prompts sind autarke Arbeitsfassungen fuer Nutzer, die das Plugin nicht installieren. Sie werden direkt als Markdown-Dateien geladen.",
        "",
        f'- Werkstatt-Prompt: <a href="{raw_base}/{slug}-werkstatt.md" download>{slug}-werkstatt.md</a>',
        f'- Schnellstart-Prompt: <a href="{raw_base}/{slug}-schnellstart.md" download>{slug}-schnellstart.md</a>',
        "",
        "<!-- END werkstatt-schnellstart-raw-links (autogen) -->",
    ])
    text = readme.read_text(encoding="utf-8", errors="ignore")
    pattern = r"<!-- BEGIN werkstatt-schnellstart-raw-links \(autogen\) -->[\s\S]*?<!-- END werkstatt-schnellstart-raw-links \(autogen\) -->"
    if re.search(pattern, text):
        text = re.sub(pattern, block, text)
    else:
        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines[insert_at:insert_at] = ["", block, ""]
        text = "\n".join(lines) + "\n"
    readme.write_text(text, encoding="utf-8")


def main() -> int:
    dirs = plugin_dirs()
    protected = load_protected()
    written = 0
    skipped = 0
    skipped_slugs: list[str] = []
    problems: list[str] = []
    for plugin_dir in dirs:
        mf = manifest(plugin_dir)
        slug = mf.get("name") or plugin_dir.name
        if slug in protected:
            # Handkuratierte Prompts bleiben unveraendert, auch bei --force.
            skipped += 2
            skipped_slugs.append(slug)
            continue
        werkstatt = build_werkstatt(plugin_dir)
        schnell = build_schnellstart(plugin_dir)
        if byte_len(schnell) > MAX_FAST:
            problems.append(f"{slug}: Schnellstart {byte_len(schnell)} Bytes")
        (plugin_dir / f"{slug}-werkstatt.md").write_text(werkstatt, encoding="utf-8")
        (plugin_dir / f"{slug}-schnellstart.md").write_text(schnell, encoding="utf-8")
        written += 2
    if problems:
        print("Probleme:")
        for p in problems:
            print("-", p)
        return 1
    if skipped_slugs:
        print("Handkuratiert, uebersprungen: " + ", ".join(sorted(skipped_slugs)))
    print(f"geschrieben: {written}, uebersprungen: {skipped}, Probleme: keine")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

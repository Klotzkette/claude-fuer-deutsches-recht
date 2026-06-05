---
name: versicherungen-gefahren-zvg
description: "Versicherungen Gefahren ZVG: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versicherungen Gefahren ZVG

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versicherungen Gefahren ZVG** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-versicherungen-gefahren` | Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB Verkehrssicherungspflicht VVG Versicherungsrecht. Prüfraster Gebaeudeversicherung Haftpflicht Beitragsrückstaende Schadenmeldung Deckungsprüfung Notmassnahmen Sicherung. Output Versicherungsprüfbericht mit Deckungsnachweis Schadenmeldung und Sicherungsmassnahmen. Abgrenzung zu zvg-instandhaltung-sicherung und zvg-konten-kassenführung. |
| `zvg-versteigerungsteilnahme` | Vorbereitung der Teilnahme am Zwangsversteigerungstermin für Gläubiger oder Bieter. Anwendungsfall Mandant will an Versteigerungstermin teilnehmen und benoetigt vollständige Vorbereitung. Normen §§ 87 ff. ZVG Termin § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung § 85a ZVG Zuschlagsversagung. Prüfraster Ausweis Vertretung Sicherheitsleistung geringstes Gebot Bietstrategie Zuschlagsgrenzen Protokoll Nachbereitung. Output Teilnahme-Checkliste mit Bietlimit Sicherheitsleistungsnachweis und Nachbereitungsprotokoll. Abgrenzung zu zvg-bieterangebot-bewertung (Investorenbewertung) und zvg-portal-recherche. |
| `zvg-verteilungsplan-155` | Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen § 154 ZVG Kosten Verwalterverguetung. Prüfraster Nutzungen Ausgaben Kosten Gläubigerzahlungen Vorschuesse Rang Auszahlung Restbetrag. Output Verteilungsplan mit Rangfolge Betraegen Auszahlungsnachweis und Gerichtsbericht. Abgrenzung zu zvg-rechnungslegung (Gesamtabrechnung) und zvg-konten-kassenführung. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Versicherungen Gefahren ZVG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-versicherungen-gefahren`

**Fokus:** Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB Verkehrssicherungspflicht VVG Versicherungsrecht. Prüfraster Gebaeudeversicherung Haftpflicht Beitragsrückstaende Schadenmeldung Deckungsprüfung Notmassnahmen Sicherung. Output Versicherungsprüfbericht mit Deckungsnachweis Schadenmeldung und Sicherungsmassnahmen. Abgrenzung zu zvg-instandhaltung-sicherung und zvg-konten-kassenführung.

# Versicherungen und Gefahren

## Aufgabe

Prüft und sichert den Versicherungsschutz des verwalteten Objekts.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Versicherungsstatus unklar ist
- Schadensfall, Beitragsrückstand oder Kündigung droht
- Besitzerlangung einen Gefahrenpunkt zeigt

## Eingaben

- Policen, Beitragsrechnungen, Schadenmeldungen
- Objektzustand, Fotos, Dienstleisterberichte
- Konto- und Vorschusslage

## Workflow

1. **Status klären** - Police, Versicherungsnehmer, Objekt, Deckung, Prämien und Rückstände erfassen.
2. **Lücke schließen** - Zahlung, Deckungsbestätigung, Nachversicherung oder Gerichtsinformation vorbereiten.
3. **Schaden** - Schadenanzeige, Belege, Sicherungsmaßnahmen und Anspruchsverfolgung steuern.
4. **Monitoring** - Wiedervorlagen für Prämien und Deckungsänderungen setzen.

## Ausgabe

- Versicherungsregister
- Deckungs- und Schadenvermerk
- Sofortschreiben

## Qualitätsgates

- Deckungsbestätigung belegt
- Rückstände geprüft
- Schaden dokumentiert

## Rote Schwellen

- keine Gebäudeversicherung
- gekündigte Police
- Leitungswasser- oder Brandschaden

## Interne Vorlagen

- assets/templates/versicherung-und-lasten.md
- assets/templates/instandhaltung-gefahrensicherung.md

## Amtliche Erstquellen

- § 3 Abs. 1 Nr. 4 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Versicherungen/Gefahren

§ 152 ZVG (ordnungsgemäße Verwaltung) → § 823 BGB (Verkehrssicherungspflicht) → § 836 BGB (Gebäudeeigentümerhaftung) → § 280 BGB (Pflichtverletzung) → § 9 ZwVwV (Versicherung und Gefahren) → VVG (Versicherungsvertragsrecht allgemein)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Versicherungen/Gefahren

1. Ist die Gebäudeversicherung (Feuer Leitungswasser Sturm) aktiv?
2. Ist eine Grundstückshaftpflichtversicherung vorhanden?
3. Sind Prämien laufend bezahlt? (Beitragsrückstand → Deckungsausschluss)
4. Liegen akute Gefahrenstellen vor? (Sofortmaßnahme erforderlich)
5. Wurde nach Besitzerlangung eine Objektbegehung auf Gefahrenstellen durchgeführt?

## Sofortmaßnahmen-Checkliste Gefahren

| Gefahrenstelle | Maßnahme | Priorität | Erledigt |
|---|---|---|---|
| Undichtes Dach | Notreparatur/Plane | SOFORT | [ ] |
| Umgestürzter Baum | Entfernung/Absperrung | SOFORT | [ ] |
| Loser Balkon/Balkongeländer | Absperrung/Reparatur | SOFORT | [ ] |
| Fehlende Heizung Winter | Notversorgung | SOFORT | [ ] |
| Wasserschaden | Absperrung/Trocknung | SOFORT | [ ] |
| Einbruchsschäden | Sicherung/Schlösser | HOCH | [ ] |
| Elektrische Mängel | Elektrofachkraft | HOCH | [ ] |

## 2. `zvg-versteigerungsteilnahme`

**Fokus:** Vorbereitung der Teilnahme am Zwangsversteigerungstermin für Gläubiger oder Bieter. Anwendungsfall Mandant will an Versteigerungstermin teilnehmen und benoetigt vollständige Vorbereitung. Normen §§ 87 ff. ZVG Termin § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung § 85a ZVG Zuschlagsversagung. Prüfraster Ausweis Vertretung Sicherheitsleistung geringstes Gebot Bietstrategie Zuschlagsgrenzen Protokoll Nachbereitung. Output Teilnahme-Checkliste mit Bietlimit Sicherheitsleistungsnachweis und Nachbereitungsprotokoll. Abgrenzung zu zvg-bieterangebot-bewertung (Investorenbewertung) und zvg-portal-recherche.

# Teilnahme am Versteigerungstermin

## Aufgabe

Führt Bieter oder Berater durch die Vorbereitung, Teilnahme und Nachbereitung eines Zwangsversteigerungstermins.

## Startet bei

- "Ich will an der Versteigerung teilnehmen"
- "Was muss ich mitbringen?"
- "Was ist das Mindestgebot?"
- "Wie vermeide ich ein zu hohes Gebot?"

## Workflow

1. **Termin verifizieren**: Gericht, Saal, Datum, Uhrzeit, Aktenzeichen, Terminstatus am Vortag und am Morgen prüfen.
2. **Legitimation vorbereiten**: Ausweis, Vollmacht, Registerauszug, Gesellschafter-/GF-Nachweis, wirtschaftlich Berechtigter bei Gesellschaft.
3. **Sicherheitsleistung organisieren**: Regelmäßig 10 Prozent des Verkehrswerts; zulässige Form und Frist beim Gericht prüfen.
4. **Begriffe erklären**:
 - geringstes Gebot: rechtliche Untergrenze für zugelassene Gebote, nicht automatisch wirtschaftlich sinnvoll.
 - Bargebot: tatsächlich bar zu zahlender Teil.
 - bestehenbleibende Rechte: wirtschaftlich zusätzlich einzupreisen.
 - 5/10-Grenze: Zuschlagsversagung von Amts wegen in relevanten Terminen.
 - 7/10-Grenze: Zuschlagsversagung auf Antrag in relevanten Terminen.
5. **Bietlimit festlegen**: harte Obergrenze schriftlich vor dem Termin fixieren; Neben- und Risikokosten einrechnen.
6. **Terminverhalten planen**: ruhig bleiben, Gebote protokollieren, keine spontane Limit-Erhöhung ohne vorher definierte Freigabe.
7. **Nachbereitung**: Zuschlag, Zahlung, Zinsen, Verteilungstermin, Räumung/Nutzung, Versicherung und Übergabe prüfen.

## Ausgabe

- Termincheckliste
- Sicherheitsleistungs- und Vollmachtscheck
- Bietlimitkarte
- Nachbereitungsvermerk

## Qualitätsgates

- Terminstatus am Versteigerungstag geprüft
- Sicherheitsleistung nicht nur "irgendwie" eingeplant, sondern gerichtsgeeignet
- Bietlimit enthält Risikoabschlag für nicht besichtigte Innenräume
- keine Beratung zu Scheingeboten oder manipulativer Bietstrategie

## Rote Schwellen

- ungeklärte Vertretungsmacht
- keine Sicherheitsleistung
- Finanzierung nur mündlich oder unverbindlich
- unklare bestehenbleibende Rechte
- emotionale Limit-Erhöhung im Termin

## Interne Vorlage

- `assets/templates/versteigerungsteilnahme-checkliste.md`

## Aktuelle Rechtsprechung

- BGH, Urt. v. 14.03.2025 – Az. V ZR 153/23 — Aufhebung des Zuschlags nach gutglaeubigem Erwerb und nachfolgendem Hausbau (Fall „Rangsdorf"); Ersteher verliert das Eigentum, kann sich aber auf ein Zurueckbehaltungsrecht wegen aufgewendeter Verwendungen berufen; § 816 BGB scheitert bei gutglaeubigem Erwerb der Grundschuld durch die finanzierende Bank. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.03.2025&Aktenzeichen=V+ZR+153/23 sowie BGH-Pressemitteilung Nr. 52/2025.
- Weitere Linien des V. ZS zu §§ 79 ff. ZVG (Zuschlagsverfahren, Beschwerden) vor Verwendung ueber https://www.bundesgerichtshof.de und https://dejure.org pruefen.

## Paragrafenkette Versteigerungsteilnahme

§ 66 ZVG (Versteigerungstermin) → § 71 ZVG (Bekanntmachungen) → § 82 ZVG (Bieter-Erklärungen) → § 87 ZVG (Zuschlag Bedingungen) → §§ 152-153 ZVG (Verwalterpflichten bis Zuschlag) → §§ 56-57a ZVG (Rechtsfolgen Zuschlag)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Versteigerungsteilnahme

1. Hat das Gericht die Anwesenheit oder Auskunftserteilung angefordert?
2. Liegen aktuelle Unterlagen vor? (Mieterliste Zustands-Bericht Kontostand)
3. Was geschieht mit laufenden Mieteinnahmen bis zum Zuschlag?
4. Sind alle Mieter über den bevorstehenden Eigentümerwechsel informiert?

## Versteigerungstermin-Vorbereitung

1. Versteigerungsdatum aus Gerichtspost festhalten
2. Aktuellen Mieterliste-Ausdruck vorbereiten (Einheit Mieter Miethöhe Rückstände)
3. Zustands-Dokumentation (Fotos Protokolle) zusammenstellen
4. Kautionsbestandsliste erstellen (Betrag je Mieter)
5. Kontostand Treuhandkonto per Stichtag Versteigerung ermitteln
6. Vollstreckungsgericht über Bereitschaft zur Auskunft informieren
7. Nach Zuschlag: Übergabe der Unterlagen an Ersteher dokumentieren

## 3. `zvg-verteilungsplan-155`

**Fokus:** Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen § 154 ZVG Kosten Verwalterverguetung. Prüfraster Nutzungen Ausgaben Kosten Gläubigerzahlungen Vorschuesse Rang Auszahlung Restbetrag. Output Verteilungsplan mit Rangfolge Betraegen Auszahlungsnachweis und Gerichtsbericht. Abgrenzung zu zvg-rechnungslegung (Gesamtabrechnung) und zvg-konten-kassenführung.

# Verteilungsplan § 155 ZVG

## Aufgabe

Bereitet die Verteilung der Nutzungen und Erlöse unter Berücksichtigung von Ausgaben, Kosten und Rang vor.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- auskehrbare Überschüsse vorhanden sind
- Gläubiger Zahlung verlangen
- Schlussrechnung oder laufende Auszahlungen anstehen

## Eingaben

- Kontostand, Einnahmen, Ausgaben, Kosten
- Gläubigerforderungen, Rang, Gerichtskosten
- Rücklagen und absehbare Objektkosten

## Workflow

1. **Verteilungsmasse** - verfügbare Nutzungen nach Abzug laufender Ausgaben und Rücklagen bestimmen.
2. **Rang prüfen** - Gläubiger, Gerichtskosten, Verwaltervergütung und öffentliche Lasten einordnen.
3. **Plan erstellen** - Auszahlungsbeträge, Rückbehalte und Begründung darstellen.
4. **Freigabe** - Gericht oder Beteiligte informieren und Zahlung dokumentieren.

## Ausgabe

- Verteilungsplan
- Auszahlungsliste
- Berichtsbaustein

## Qualitätsgates

- keine Verteilung ohne Rücklagencheck
- Rang und Kosten geprüft
- Zahlungen belegt

## Rote Schwellen

- Auskehr trotz offener Notkosten
- falscher Gläubiger
- ungeklärte öffentliche Last

## Interne Vorlagen

- assets/templates/verteilungsplan-155.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- § 155 ZVG
- §§ 11, 12 ZwVwV

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Verteilungsplan

§ 155 ZVG (Verteilungsplan) → § 10 ZVG (Rangklassen) → § 11 ZwVwV (Vorschüsse) → § 12 ZwVwV (Auszahlungen) → § 154 ZVG (Gerichtsgenehmigung bei Zweifeln) → § 20 ZwVwV (Vergütung als Ausgabe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Verteilungsplan

1. Wie hoch ist der ausschüttungsfähige Betrag nach Abzug laufender Ausgaben und Rücklage?
2. Welche Gläubiger sind zu befriedigen und in welchem Rang?
3. Hat das Vollstreckungsgericht Auszahlungen bereits genehmigt?
4. Sind Gerichtskosten und Verwaltervergütung einbezogen?

## Output-Template Verteilungsplan (Schema)

```
VERTEILUNGSPLAN nach § 155 ZVG
Objekt: [ADRESSE]
AZ: [X]
Verteilungsmasse per [DATUM]: [BETRAG] EUR

ABZÜGE VOR VERTEILUNG
Laufende Ausgaben (Rücklage 3 Monate): [BETRAG]
Gerichtskosten: [BETRAG]
Verwaltervergütung (brutto): [BETRAG]
Sonstige dringende Ausgaben: [BETRAG]
VERBLEIBENDE VERTEILUNGSMASSE: [BETRAG]

RANGFOLGE (§ 10 ZVG)
Nr. 1 Kosten des Verfahrens: [BETRAG]
Nr. 2 Öff. Lasten lfd. Jahr: [BETRAG]
Nr. 3 Öff. Lasten Rückstände: [BETRAG]
Nr. 4 Grund-/Rentenschuld: [BETRAG an GLÄUBIGER X]
Nr. 5 Weitere Hypotheken: [ggf.]

AUSZAHLUNGSLISTE
Empfänger | Betrag | Bankverbindung | Datum
[...] | [...] | [...] | [...]

[ORT, DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```

---
name: anw-grundsteuerwert-bewertung-triage
description: "ANW Grundsteuerwert Bewertung Triage: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ANW Grundsteuerwert Bewertung Triage

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **ANW Grundsteuerwert Bewertung Triage** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anw-grundsteuerwert-bewertung-bewg-218ff` | Grundsteuerwert nach BewG §§ 218 ff. prüfen: Bundesmodell, Ertragswert, Sachwert, Bodenrichtwert, Grundstücksart, Steuermesszahl, Hauptfeststellung 01.01.2022, Fehlerdiagnose und Bescheidbegründung. |
| `anw-mandat-triage-steuerrecht` | Strukturierte Erstabfrage und Triage bei Eingang eines steuerrechtlichen Mandats. Anwendungsfall Mandant meldet sich mit Steuerproblem Art und Dringlichkeit noch unklar. Klaert Mandantenrolle Steuerart ESt KSt GewSt USt ErbSt GrESt Vorgang Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Aussenprüfung Selbstanzeige AdV verbindliche Auskunft Klage FG. Sofort-Fristen Einspruch § 355 AO ein Monat Jahresfrist § 356 AO Klage § 47 FGO. Eskalation Telefon-Sofort bei Selbstanzeige-Bedarf Hausdurchsuchung Steuerfahndung drohender Vollziehung. Output Triage-Ergebnis Fristenprotokoll naechste Schritte. Abgrenzung zu anw-kaltstart-interview Kanzlei-Konfiguration. |
| `anw-minbestg-pillar2-konzernbesteuerung` | Beratung zur globalen Mindestbesteuerung Pillar Two MinBestG für Konzerne ab 750 Mio EUR Umsatz. Anwendungsfall Konzern fragt nach GloBE-Pflichten Compliance-Aufbau oder Country-by-Country Reporting ab 01.01.2024. MinBestG vom 21.12.2023. GloBE-Regeln IIR Income Inclusion Rule UTPR Undertaxed Profits Rule QDMTT Qualified Domestic Minimum Top-up Tax 15 Prozent globaler Mindeststeuersatz. Berechnung effektiver Steuersatz Top-Up Tax Steuererklärung. Output Compliance-Prüfprotokoll Reporting-Konzept Beratungsmemo. Abgrenzung zu anw-organschaft-konzern-grundlagen inlaendische Konzernstruktur. |
| `anw-orientierung` | Orientierungs-Skill für Anwaeltinnen und Anwaelte im Steuerrecht. Anwendungsfall Einstieg in das Plugin oder Überblick über verfuegbare Skills gewuenscht. Zentrale Gesetze AO EStG KStG UStG GewStG ErbStG GrEStG. Verfahrenswege Einspruch § 347 AO AdV § 361 AO Aussenprüfung §§ 193 ff. AO FG-Klage FGO Revision BFH Steuerstrafrecht §§ 369 ff. AO Selbstanzeige § 371 AO. verifizierbare Quellen lizenzpflichtige Literaturquellen HHSp L. Schmidt EStG. Output Überblick verfuegbare Skills und Routing zu Fachmodule. FAO § 9 Fachanwaltsvoraussetzungen als Anhang. |
| `anw-selbstanzeige-371` | Selbstanzeige nach § 371 AO als strafbefreiende Berichtigung bei Steuerhinterziehung vorbereiten und einreichen. Anwendungsfall Mandant hat Steuern hinterzogen und will Straffreiheit erlangen bevor Entdeckung droht. Vollständigkeit aller unverjährten Steuerstraftaten zehn Jahre § 376 AO ggf. 15 Jahre Sperrgründe § 371 Abs. 2 AO Nachentrichtung § 371 Abs. 3 AO Zinsen § 235 AO Zuschlag § 398a AO gestaffelt. Abgrenzung § 153 AO Berichtigungspflicht ohne Strafbefreiung zu § 371 AO Vorsatz und § 378 Abs. 3 AO Leichtfertigkeit. Output Berichtigungserklärung. Pflichtprüfung Hoechstrisikobereich mehrere Anwaelte. |
| `anw-steuerbescheid-analyse` | Steuerbescheid strukturiert auswerten und Angriffspunkte für Einspruch identifizieren. Anwendungsfall Mandant hat Steuerbescheid bekommen und fragt ob und wie er sich wehren kann. Bescheidarten Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Prüfungsbescheid. Erfasst Steuerart Veranlagungsjahr Nachforderung oder Erstattung Vorlaeufigkeitsvermerk Vorbehalt der Nachprüfung § 164 AO Aenderungsvorschriften §§ 172 ff. AO Bekanntgabe § 122 AO Vier-Tages-Fiktion seit 01.01.2025 PostModG. Output Analyse-Protokoll Angriffspunkte Fristenstatus Empfehlung Einspruch oder Akzeptanz. Nahtloser Übergang zu anw-einspruch-finanzamt. |
| `anw-steuerstrafverteidigung-verstaendigung` | Prüffeld für anw steuerstrafverteidigung verstaendigung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `anw-stundung-erlass-vollstreckungsaufschub` | Anträge auf Stundung Erlass und Vollstreckungsaufschub bei Zahlungsproblemen stellen. Anwendungsfall Mandant kann fällige Steuerschulden vorueber-gehend oder dauerhaft nicht zahlen Vollstreckung droht. Stundung erhebliche Haerte § 222 AO ohne Anspruchsgefaehrdung. Erlass aus persoenlichen oder sachlichen Billigkeitsgründen § 227 AO. Vollstreckungsaufschub bei unbilligem Vollstreckungserfolg § 258 AO Verzinsung bei Stundung § 234 AO. Output Antrag mit Begründung Sicherheitsleistung Ratenzahlungsplan. Abgrenzung zu anw-aussetzung-vollziehung AdV und anw-insolvenzreife-prüfung-17-19-inso. |
| `anw-umsatzsteuer-vorsteuerabzug-pruefen` | Prüffeld für anw umsatzsteuer vorsteuerabzug pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **ANW Grundsteuerwert Bewertung Triage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anw-grundsteuerwert-bewertung-bewg-218ff`

**Fokus:** Grundsteuerwert nach BewG §§ 218 ff. prüfen: Bundesmodell, Ertragswert, Sachwert, Bodenrichtwert, Grundstücksart, Steuermesszahl, Hauptfeststellung 01.01.2022, Fehlerdiagnose und Bescheidbegründung.

# Grundsteuerwert: Bewertung nach BewG §§ 218 ff.

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuerwert: Bewertung nach BewG §§ 218 ff.` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüfe den Grundsteuerwertbescheid im Bundesmodell. Dieser Skill arbeitet nicht als Rechner ohne Unterlagen, sondern als Bewertungsdiagnose: Welche Eingabe bestimmt den Wert, welche ist falsch, welche ist nur belastend, aber rechtlich vorgesehen?

## Prüfschritte

1. **Anwendungsbereich**: Bundesmodell oder Landesmodell? Bei Landesmodell an `anw-grundsteuer-landesmodell-routing` abgeben.
2. **wirtschaftliche Einheit**: Grundstück, Betrieb der Land- und Forstwirtschaft, Wohnungs-/Teileigentum, Erbbaurecht.
3. **Bewertungsverfahren**: Ertragswertverfahren oder Sachwertverfahren.
4. **Datenbasis**: Bodenrichtwert, Fläche, Grundstücksart, Baujahr, Wohn-/Nutzfläche, statistische Nettokaltmiete, Mietniveaustufe, Restnutzungsdauer.
5. **Messbetrag**: Steuermesszahl und mögliche Ermäßigungen im Messbescheid gesondert prüfen.
6. **Gemeinderolle**: Hebesatz erst im Grundsteuerbescheid.

## Fehlerbilder

- Objekt ist kein reines Wohnobjekt, wurde aber so behandelt.
- Gewerbefläche, Lager oder Atelier wurde falsch als Wohnfläche erfasst.
- Bodenrichtwertzone passt nicht zur Lage oder zum Stichtag.
- Denkmalschutz oder sozialer Wohnungsbau wurde nicht berücksichtigt.
- Baujahr/Kernsanierung verzieht Restnutzungsdauer.
- Einheiten wurden wegen gemeinsamer Zufahrt oder Tiefgarage falsch zusammengefasst.

## Begründungsstruktur

Arbeite in dieser Reihenfolge:

1. angefochtener Bescheid mit Datum und Aktenzeichen,
2. konkrete falsche Besteuerungsgrundlage,
3. richtiger Wert und Beleg,
4. rechtliche Relevanz für BewG/GrStG,
5. Antrag auf Änderung beziehungsweise Einspruchsziel.

## Output

- Bewertungsfehler-Matrix.
- Priorisierte Angriffspunkte.
- Entwurf eines Beleganschreibens.
- Kurzer Einspruchsbaustein.
- Hinweis, ob zusätzlich gemeiner Wert/gutachterlicher Nachweis geprüft werden soll.

## Quellen

Gesetzestext vor Ausgabe öffnen: BewG §§ 218 ff., GrStG, ggf. amtliche Grundsteuer-Hinweise. Keine Kommentarzitate ohne Nutzerquelle.

## Norm-Bezug konkret

- § 218 BewG: Verfahrensgliederung Grundsteuerwert.
- § 219 BewG: Feststellung des Grundsteuerwerts auf den Hauptfeststellungszeitpunkt 01.01.2022.
- §§ 243-247 BewG: unbebaute Grundstücke (Bodenwertverfahren mit Bodenrichtwert).
- §§ 248-260 BewG: bebaute Grundstücke - Ertragswertverfahren (Wohnen) und Sachwertverfahren (Geschäft, gemischte Nutzung, Sonderfälle).
- § 257 BewG: Liegenschaftszinssätze typisiert nach Grundstücksart.
- § 15 GrStG: Steuermesszahlen (regelmäßig 0,31 ‰ für Wohnen, 0,34 ‰ für Nichtwohnen, Ermäßigungen z. B. für sozialen Wohnungsbau, Denkmal).

## Praktischer Tipp

- ELSTER-Erklärung hat den Wert getrieben. Erste Diagnose: hat Mandant Wohnflächen "geschätzt" angegeben? Häufige Falle: Dachgeschoss zur Wohnfläche dazugerechnet, obwohl < 1 m Schräge nach Wohnflächenverordnung gar nicht zählt.
- Mietniveaustufe (Anlage 39 BewG für die jeweilige Gemeinde) prüfen; Großstadt-Mandanten landen oft in Stufe 6, obwohl der konkrete Stadtteil deutlich darunter liegt - hier ist eine Anpassung nicht ohne Weiteres möglich, aber bei Mischlagen Vergleichsbeleg sammeln.
- Liegenschaftszinssatz ist typisiert - kein Angriffspunkt für den Einzelfall, nur über den Modellangriff. Real angreifbar sind: Wohnfläche, Grundstücksfläche, Bodenrichtwert (über die Zonenzugehörigkeit, ggf. Vergleich mit Auskunft des Gutachterausschusses), Baujahr (Kernsanierung wird oft als Neubau eingetragen).

## Trade-off: Welche Fehlerklasse zuerst angreifen?

| Fehlerart | Hebel | Aufwand |
|---|---|---|
| Wohnfläche falsch | direkt änderbar bei Beleg | Wohnflächenberechnung anfertigen lassen (ca. 300-600 EUR) |
| Bodenrichtwertzone falsch | hoher Hebel | Gutachterausschussauskunft (oft kostenpflichtig 50-150 EUR) |
| Grundstücksart falsch | hoher Hebel über Steuermesszahl | Teilungserklärung, Bauakte |
| gemeiner Wert deutlich niedriger | Eilverfahrenshebel über BFH II B 78/23 / II B 79/23 | Belegtreppe, ggf. Gutachten - Bewertungsstichtag 01.01.2022 (Quellen live auf bundesfinanzhof.de verifizieren) |

Empfehlung: Erst niedrigwertige Belege (Wohnflächenberechnung, Bodenrichtwertauskunft) sammeln, dann gezielt einsetzen.

## Typische Fehler

- Einspruch trifft den falschen Bescheid: Hebesatz angegriffen, obwohl der Wertfehler im Grundlagenbescheid (Finanzamt) sitzt. § 351 Abs. 2 AO sperrt den Folgebescheid.
- Einspruchsfrist von einem Monat wird übersehen, weil der Bescheid an die ELSTER-Postfachadresse zugestellt und nicht abgerufen wurde; § 122 Abs. 2a AO regelt elektronische Bekanntgabe nach drei Tagen.

## 2. `anw-mandat-triage-steuerrecht`

**Fokus:** Strukturierte Erstabfrage und Triage bei Eingang eines steuerrechtlichen Mandats. Anwendungsfall Mandant meldet sich mit Steuerproblem Art und Dringlichkeit noch unklar. Klaert Mandantenrolle Steuerart ESt KSt GewSt USt ErbSt GrESt Vorgang Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Aussenprüfung Selbstanzeige AdV verbindliche Auskunft Klage FG. Sofort-Fristen Einspruch § 355 AO ein Monat Jahresfrist § 356 AO Klage § 47 FGO. Eskalation Telefon-Sofort bei Selbstanzeige-Bedarf Hausdurchsuchung Steuerfahndung drohender Vollziehung. Output Triage-Ergebnis Fristenprotokoll naechste Schritte. Abgrenzung zu anw-kaltstart-interview Kanzlei-Konfiguration.

# Mandat-Triage Steuerrecht

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Steuerrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Mandat-Triage Steuerrecht

- **Spezialfrage (Mandat-Triage Steuerrecht):** Strukturierte Erstabfrage und Triage bei Eingang eines steuerrechtlichen Mandats. Anwendungsfall Mandant meldet sich mit Steuerproblem Art und Dringlichkeit noch unklar. Klaert Mandantenrolle Steuerart ESt KSt GewSt USt ErbSt GrESt Vorgang Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Aussenprüfung Selbstanzeige AdV verbindliche Auskunft Klage FG. Sofort-Fristen Einspruch § 355 AO ein Monat Jahresfrist § 356 AO Klage § 47 FGO. Eskalation Telefon-Sofort bei Selbstanzeige-Bedarf Hausdurchsuchung Steuerfahndung drohender Vollziehung. Output Triage-Ergebnis Fristenprotokoll naechste Schritte. Abgrenzung zu anw-kaltstart-interview Kanzlei-Konfiguration.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.


## Aktuelle Rechtsprechung (Orientierung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Steuerrechts-Mandate sind kurzfristig fristgeprägt (Einspruch ein Monat) und sehr unterschiedlich (ESt-Bescheid bis Steuerstrafverfahren). Triage stellt die richtige Spur sicher — ergänzend zum Plugin-Konfigurations-Skill `anw-kaltstart-interview`.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Steuerpflichtiger Privatperson
- Selbstständig
- GmbH / AG / KG
- Steuerberater (Kollegen-Vertretung)
- Steuerstrafverteidigung
- Geschäftsführer-Haftung Steuern § 69 AO
- Erbe (Erbschaftsteuer)
- Beschenkter (Schenkungsteuer)

### Frage 2 — Steuerart?

- Einkommensteuer ESt
- Lohnsteuer LSt
- Körperschaftsteuer KSt
- Gewerbesteuer GewSt
- Umsatzsteuer USt
- Erbschaft- und Schenkungsteuer ErbSt / SchenkSt
- Grunderwerbsteuer GrESt
- Grundsteuer
- Kfz-Steuer
- Investitionszulagen Forschungs- und Entwicklungs-Förderung
- Internationale Besteuerung / DBA
- Steuerstrafrecht / Selbstanzeige

### Frage 3 — Vorgang?

- Steuererklärung erstellen / abgeben
- Festsetzungsbescheid analysieren
- Änderungs-/Berichtigungsbescheid
- Schätzungsbescheid § 162 AO
- Haftungsbescheid § 191 AO
- Vorläufigkeitsvermerk § 165 AO
- Vorbehalt der Nachprüfung § 164 AO
- Einspruchsverfahren
- Klage Finanzgericht
- Außenprüfung
- USt-Sonderprüfung Lohnsteuerprüfung
- Selbstanzeige § 371 AO
- Steuerstrafverfahren
- Aussetzung der Vollziehung AdV
- Stundungs-/Erlass-Antrag § 222 § 227 AO
- Verbindliche Auskunft § 89 Abs. 2 AO
- Verbindliche Zusage § 204 AO
- Internationale Verständigungsverfahren
- Verrechnungspreise

### Frage 4 — Akute Eilbedürftigkeit?

- **Einspruchsfrist** ein Monat § 355 AO läuft
- **Klagefrist** ein Monat § 47 FGO läuft
- **Vollziehung droht** Vollstreckung
- **Hausdurchsuchung Steuerfahndung** akut
- **Selbstanzeige** wegen drohender Tatentdeckung
- **Außenprüfung** Schlussbesprechung morgen
- **Festsetzungsverjährung** läuft ab

### Frage 5 — Stand?

- Steuererklärung in Vorbereitung
- Bescheid liegt vor (Datum Eingang)
- Einspruch eingelegt — wartet auf Einspruchsentscheidung
- Einspruchsentscheidung — Klage erwogen
- Klage erhoben (Az FG)
- Revision BFH
- Beschwerde Nichtzulassung
- BVerfG Verfassungsbeschwerde
- EuGH-Vorlage
- Stundungs-/Erlass-Antrag
- AdV-Antrag

### Frage 6 — Frist?

- **Einspruch** ein Monat § 355 AO
- **Bei fehlender / fehlerhafter Belehrung** ein Jahr § 356 AO
- **Klage FG** ein Monat § 47 FGO
- **Nichtzulassungsbeschwerde** ein Monat § 116 FGO
- **Revisionsbegründung** zwei Monate § 120 FGO
- **Festsetzungsverjährung** vier (zehn bei Hinterziehung) Jahre § 169 AO
- **Antrag schlichte Änderung** ein Monat § 172 AO
- **Wiedereinsetzung** ein Monat § 110 AO

### Frage 7 — Wirtschaftliche Verhältnisse?

- Steuer-Volumen
- Stundungs-/Erlass-Bedarf
- AdV erforderlich
- PKH möglich

### Frage 8 — Steuerstrafrecht-Dimension?

- Tatentdeckung droht / erfolgt
- Selbstanzeige rechtzeitig
- Schadenshöhe Steuer-Verkürzung
- Mehrere Veranlagungs-Zeiträume

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Bescheid analysieren | `anw-steuerbescheid-analyse` |
| Einspruch formulieren | `anw-einspruch-finanzamt` |
| Klage am FG | `anw-klage-finanzgericht` |
| Aussetzung der Vollziehung | `anw-aussetzung-vollziehung` |
| Verbindliche Auskunft | `anw-verbindliche-auskunft` |
| Selbstanzeige | `anw-selbstanzeige-371` |
| Außenprüfung | `anw-aussenpruefung-strategien` |
| Akteneinsicht | `anw-akteneinsicht-steuerakte` |
| Fristenbuch | `anw-fristenbuch-steuerrecht` |
| Frist-Berechnung Zustellung | (allgemein im Fristenbuch) |
| Betriebsausgaben-Werbungskosten | `anw-betriebsausgaben-werbungskosten-pruefraster` |
| Plugin-Konfiguration | `anw-kaltstart-interview` |
| Erbschaftsteuer | (Skill erbschaftsteuer-prüfen — perspektivisch) |
| Umsatzsteuer-Prüfung | (Skill ust-prüfung — perspektivisch) |
| Verrechnungspreise | (Skill verrechnungspreise — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — Mandant / Vermittler / Kollegen-Mandat
- **Streitwert** Steuer-Betrag bestimmt Streitwert
- **Versicherungs-Deckung** Berufshaftpflicht Steuerberater Anwalt
- **Komplexität** internationale Sachverhalte Verrechnungspreise Konzerne

## Eskalation

- **Telefon-Sofort** Hausdurchsuchung Steuerfahndung Selbstanzeige-Notfall
- **Binnen einer Stunde** Einspruchsfrist heute / morgen AdV bei drohender Vollziehung
- **Heute** Bescheidanalyse Einspruch-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Verteidigungs-Strategie

## Ausgabe

- `triage-protokoll-steuerrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Einspruch / Klage / Festsetzungsverjährung)
- AdV-Antrag-Vorbereitung wenn relevant
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- AO §§ 89 110 162 164 165 169 172 191 222 227 355 356 371
- FGO §§ 47 116 120
- EStG KStG GewStG UStG ErbStG GrEStG
- BFH Std.Spruch
- Tipke/Lang Steuerrecht
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 3. `anw-minbestg-pillar2-konzernbesteuerung`

**Fokus:** Beratung zur globalen Mindestbesteuerung Pillar Two MinBestG für Konzerne ab 750 Mio EUR Umsatz. Anwendungsfall Konzern fragt nach GloBE-Pflichten Compliance-Aufbau oder Country-by-Country Reporting ab 01.01.2024. MinBestG vom 21.12.2023. GloBE-Regeln IIR Income Inclusion Rule UTPR Undertaxed Profits Rule QDMTT Qualified Domestic Minimum Top-up Tax 15 Prozent globaler Mindeststeuersatz. Berechnung effektiver Steuersatz Top-Up Tax Steuererklärung. Output Compliance-Prüfprotokoll Reporting-Konzept Beratungsmemo. Abgrenzung zu anw-organschaft-konzern-grundlagen inlaendische Konzernstruktur.

# Mindestbesteuerung Pillar Two / MinBestG — Konzernbesteuerung 15 %

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mindestbesteuerung Pillar Two / MinBestG — Konzernbesteuerung 15 %` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Anwaltliche Beratung großer Konzerne zur globalen Mindestbesteuerung (OECD Pillar Two / GloBE), die in Deutschland durch das **Mindestbesteuerungsgesetz (MinBestG)** seit 1.1.2024 implementiert ist. Anwendungsbereich: multinationale und große inländische Konzerne mit konsolidiertem Konzernumsatz **≥ 750 Mio. EUR** in mindestens zwei der letzten vier Jahre. Ziel: weltweiter effektiver Mindeststeuersatz von **15 %** auf Konzernebene pro Land.

## Kaltstart-Rückfragen

1. Konzern-Konsolidierter Umsatz (letzte 4 Jahre) — ≥ 750 Mio. EUR erreicht?
2. Konzernsitz Deutschland oder Ausland (mutterunternehmen)?
3. Welche Konzern-Tochter-Länder (Niedrigsteuerländer, EU, Drittland)?
4. Konsolidierungsstandard (IFRS, HGB, US-GAAP)?
5. Bisher Pillar-Two-Compliance aufgebaut (TCMS, GloBE-Tool, Reporting)?
6. Vorhandene Tax-Reps in M&A-Verträgen prüfen?
7. Verständigungsverfahren-Risiken aus DBA?

## Rechtlicher Rahmen

### Primärnormen

- **Mindestbesteuerungsgesetz (MinBestG)** vom 21.12.2023 — Umsetzung der EU-Richtlinie (EU) 2022/2523 (Mindestbesteuerungsrichtlinie).
- **§ 1 MinBestG** — Anwendungsbereich: multinationale und große inländische Unternehmensgruppen.
- **§§ 7 ff. MinBestG** — Berechnung des effektiven Steuersatzes (ETR).
- **§§ 11 ff. MinBestG** — Top-Up Tax (Ergänzungssteuer); drei Mechanismen:
 - **IIR (Income Inclusion Rule)** — Mutterunternehmen versteuert niedrig besteuerte Tochter
 - **UTPR (Undertaxed Profits Rule)** — Auffangregel bei nicht-IIR-Land
 - **QDMTT (Qualified Domestic Minimum Top-up Tax)** — Land selbst erhebt Ergänzungssteuer
- **§§ 75–84 MinBestG** — Berichtspflichten: GloBE-Erklärung jährlich.
- **§§ 88 ff. MinBestG** — Sanktionen bei Verstößen.

### Sekundärnormen

- **OECD GloBE Model Rules** (Dezember 2021, Updates 2022/2023).
- **OECD Commentary** (März 2022) zur Anwendung.
- **OECD Administrative Guidance** (Februar 2023, Juli 2023, Dezember 2023, Mai 2024, Januar 2025).
- **EU-Richtlinie (EU) 2022/2523** vom 14.12.2022.
- **Mindeststeueranpassungsgesetz (MinStAnpG)** vom Dezember 2025 (BGBl. 2025 I Nr. 353, verkuendet 23.12.2025; in Kraft 24.12.2025). Setzt OECD-Verwaltungsleitlinien vom 15.12.2023, 24.05.2024 und 13.01.2025 um (CbCR-Safe-Harbour-Anpassungen, QDMTT-Safe-Harbour-Voraussetzungen). Aktuellen Stand pruefen.
- BMF-Schreiben vom 18.04.2024 zum MinBestG (Anwendung). Folgeschreiben moeglich.
- **§ 8b KStG / § 17 KStG / DBA** — Wechselwirkungen mit klassischem Konzernsteuerrecht.

### Leitentscheidungen und relevante Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Hinweis: Zum MinBestG selbst (in Kraft seit 1.1.2024) liegt noch keine BFH-Rechtsprechung vor. Erste Entscheidungen sind ab 2026/2027 zu erwarten.*

## Anwendungsbereich

**MinBestG gilt für Unternehmensgruppen, wenn:**

1. Konsolidierter Umsatz **≥ 750 Mio. EUR** in mindestens **zwei der letzten vier** Geschäftsjahre vor dem Veranlagungszeitraum
2. Die Gruppe ist in mindestens einem anderen Staat tätig (multinational) **oder** rein inländisch (große inländische Gruppen, § 1 Abs. 1 MinBestG)

**Ausgenommen:**
- Staatliche Einrichtungen
- Internationale Organisationen
- Investment-Fonds (UCITS, AIF)
- Pensionsfonds
- Non-Profit-Organisationen
- Sicherungs- und Anlagevehikel im engeren Sinne

## Drei-Stufen-Berechnung GloBE

### Stufe 1 — Ermittlung der Konzern-Bestandteile

- Ausgangs-Konsolidierungskreis (IFRS / HGB).
- Identifikation der Konstellanten pro Land (Country Pillars).

### Stufe 2 — GloBE-Income & Covered Taxes

- **GloBE Income** = handelsrechtliches Ergebnis nach Anpassungen (z. B. Dividenden-Eliminierung § 8b KStG-ähnlich, Carve-outs).
- **Covered Taxes** = effektiv gezahlte Steuern auf das GloBE Income; Anpassungen für latente Steuern, Verlustverrechnung.

### Stufe 3 — Effective Tax Rate (ETR)

```
ETR pro Land = Covered Taxes / GloBE Income
```

Wenn **ETR < 15 %**, fällt **Top-Up Tax** an:

```
Top-Up Tax = (15 % - ETR) × (GloBE Income - Substance-Based Income Exclusion)
```

**Substance-Based Income Exclusion (SBIE)**: Schutz für reale wirtschaftliche Tätigkeit; 5 % der Lohnkosten + 5 % der Anlagewerte (gestaffelt absteigend 2024-2032).

## Die drei Top-Up-Tax-Mechanismen

### IIR (Income Inclusion Rule)

- **Top-Down-Ansatz**: Mutterunternehmen versteuert niedrig besteuerte Tochter.
- Anwendung seit 1.1.2024 (deutsche Mütter in Deutschland erfasst).
- Berechnung: anteilige Top-Up Tax wird beim Mutterunternehmen erhoben.

### UTPR (Undertaxed Profits Rule)

- **Auffang-Regel**: greift, wenn IIR nicht oder unzureichend angewendet wird.
- Andere Konzerngesellschaften (z. B. in Drittländern) tragen die Top-Up Tax (Versagung von Abzügen, Quellensteuer).
- Anwendung in Deutschland seit 1.1.2025 (ein Jahr verzögert).

### QDMTT (Qualified Domestic Minimum Top-up Tax)

- **Inländische Ergänzungssteuer** — jedes Land kann eine eigene Top-Up Tax erheben, um nicht andere Länder IIR/UTPR ausüben zu lassen.
- Deutschland hat **QDMTT** ab 1.1.2024 eingeführt: deutsche Tochtergesellschaften mit ETR < 15 % zahlen direkt die Ergänzungssteuer an Deutschland.

## Compliance-Aufbau

### Phase 1 — Anwendbarkeits-Check

- Konzernumsatz und Konsolidierungskreis prüfen.
- Schwelle erreicht? Wann (welche Geschäftsjahre)?
- Voraussichtliche Top-Up-Tax-Wirkung (Niedrigsteuerländer im Konzern)?

### Phase 2 — Aufbau Tax Compliance Management System (TCMS)

- **Datensammlung**: GloBE-relevante Kennzahlen pro Konzerngesellschaft.
- **Datenqualität**: Einbindung Konzernkonsolidierung (IFRS), Tax-Reporting.
- **Tool**: spezielle GloBE-Software (SAP, OneSource, in-house).
- **Verantwortlichkeiten**: Konzernsteuerabteilung + lokale Tax-Heads.

### Phase 3 — Berechnung Effective Tax Rate

- Pro Land jährlich.
- Bei ETR < 15 %: Top-Up Tax berechnen (mit SBIE-Carve-out).

### Phase 4 — Erklärung

- **GloBE Information Return** (GIR) — XML-Datei an BZSt.
- **Erstabgabe (Übergangsregelung)** — **18 Monate** nach Ende des ersten in den Anwendungsbereich fallenden Geschäftsjahrs (§ 95 Abs. 1 MinStG i.V.m. Art. 44 Abs. 7 EU-RL 2022/2523). Für Konzerne mit kalenderjahrgleichem GJ 2024: Frist **30.6.2026**. Für abweichende Wirtschaftsjahre entsprechend 18 Monate nach Ende GJ 2024.
- **Folgejahre** (ab dem zweiten in-scope GJ): **15 Monate** nach Geschäftsjahr-Ende (§ 95 Abs. 1 MinStG).

### Phase 5 — Bei Erkenntnis Top-Up Tax

- Berechnung dokumentieren.
- Zahlung bei zuständigem FA (typisch: Sitz Mutter).
- Bei Streit: Einspruch (`anw-einspruch-finanzamt`).

## Sanktionen § 88 ff. MinBestG

- **Verspätete Abgabe** GIR: bis 50 000 EUR.
- **Unvollständige Angabe**: bis 100 000 EUR.
- **Wiederholung**: erhöht.
- **Sicheres Land** ("Safe Harbours") nutzen, soweit verfügbar (Vereinfachungen).

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Konzernumsatz 750 Mio nicht zuverlässig ermittelt | Falsche Anwendbarkeits-Annahme | Konzernkonsolidierung läuft | klare Datenbasis |
| Niedrigsteuerland im Konzern (z. B. Irland-Tochter) ohne ETR-Check | Top-Up Tax verpasst | Erste Berechnungen | ETR ≥ 15 % oder Top-Up Tax abgeführt |
| GloBE Information Return verspätet | Bußgeld + Steuerstrafverfahren möglich | Frist knapp | rechtzeitig abgegeben |
| Substance-Based Income Exclusion nicht beansprucht | überzahlte Top-Up Tax | Berechnung läuft | SBIE optimal genutzt |
| QDMTT mit IIR/UTPR-Konflikt | Doppelbesteuerung; Verständigungsverfahren | Klärung läuft | sauberes QDMTT |

## Praxis-Hinweise 2026

- **Erste GIR-Abgaben** für GJ 2024 sind im Frühjahr/Sommer 2026 fällig — viele Konzerne sind noch in der Implementierung.
- **Safe Harbours** verlängert bis 31.12.2026 (Transitional CbCR Safe Harbour).
- **Administrative Guidance** OECD wird laufend ergänzt; aktuellen Stand prüfen.
- **DBA-Verständigungsverfahren** bei Doppelbesteuerung (Art. 25 OECD-MA) wird häufig relevant.

## Querverweise

- `anw-verbindliche-auskunft` — vorab bei Strukturierungsfragen
- `anw-organschaft-konzern-grundlagen` — Inland-Konzern-Strukturen
- `anw-grunderwerbsteuer-share-deal-90-prozent` — bei M&A im großen Konzern
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — bei Holding-Setup mit MinBestG-Bezug
- `fachanwalt-internationales-wirtschaftsrecht` — bei DBA/EU-Recht
- `aussenwirtschaft-zoll-sanktionen` — bei zoll-/sanktionsbezogener Konzern-Compliance

## Quellen und Updates

Stand: 05/2026. MinBestG seit 1.1.2024. OECD Administrative Guidance Stand Januar 2025; weitere Updates in 2025/2026 erwartet. Transitional Safe Harbour bis 31.12.2026. BMF-Schreiben 18.04.2024. **Mindeststeueranpassungsgesetz (MinStAnpG)** verkuendet im BGBl. 2025 I Nr. 353 (23.12.2025; in Kraft 24.12.2025) — passt MinBestG an OECD-Guidance an. Bei Verschärfung oder DAC-9-Erweiterungen aktualisieren.

## 4. `anw-orientierung`

**Fokus:** Orientierungs-Skill für Anwaeltinnen und Anwaelte im Steuerrecht. Anwendungsfall Einstieg in das Plugin oder Überblick über verfuegbare Skills gewuenscht. Zentrale Gesetze AO EStG KStG UStG GewStG ErbStG GrEStG. Verfahrenswege Einspruch § 347 AO AdV § 361 AO Aussenprüfung §§ 193 ff. AO FG-Klage FGO Revision BFH Steuerstrafrecht §§ 369 ff. AO Selbstanzeige § 371 AO. verifizierbare Quellen lizenzpflichtige Literaturquellen HHSp L. Schmidt EStG. Output Überblick verfuegbare Skills und Routing zu Fachmodule. FAO § 9 Fachanwaltsvoraussetzungen als Anhang.

# Anwalt im Steuerrecht — Orientierung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anwalt im Steuerrecht — Orientierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Dieser Skill ist die Einstiegs-Orientierung fuer **alle Anwaeltinnen und Anwaelte im Steuerrecht** — unabhaengig davon, ob der Fachanwaltstitel angestrebt oder bereits gefuehrt wird. Die FAO-§-9-Voraussetzungen sind als Anhang aufgenommen, weil sie nur fuer den Erwerbsweg relevant sind und das Mandat als solches nicht beeinflussen.

## Aktuelle Rechtsprechung (Orientierung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wichtige Normen

| Bereich | Norm |
|---|---|
| Allgemeines Steuerverfahrensrecht | AO (Abgabenordnung), insbes. §§ 122, 169 ff. (Festsetzungsverjährung), §§ 347 ff. (Einspruch), §§ 193 ff. (Außenprüfung) |
| Einkommensteuer | EStG, EStDV |
| Körperschaftsteuer | KStG, KStDV |
| Umsatzsteuer | UStG, UStDV; MwStSystRL 2006/112/EG |
| Gewerbesteuer | GewStG |
| Erbschaft- und Schenkungsteuer | ErbStG, BewG |
| Grunderwerbsteuer | GrEStG |
| Finanzgerichtsverfahren | FGO (Finanzgerichtsordnung) |
| Steuerstrafrecht | §§ 369 ff. AO (Steuerstraftaten), § 371 AO (Selbstanzeige), §§ 370a, 378 AO (Leichtfertige Steuerverkürzung) |

## Typische Mandate

- Einspruch gegen Steuerbescheid mit AdV-Antrag.
- Begleitung der Außenprüfung (Betriebsprüfung) bis zur Schlussbesprechung.
- Klage vor dem Finanzgericht und Revision beim Bundesfinanzhof.
- Steuerstrafverfahren und Selbstanzeige nach § 371 AO.
- Anträge auf Stundung (§ 222 AO), Erlass (§§ 163, 227 AO), Vollstreckungsaufschub (§ 258 AO).
- Verbindliche Auskunft (§ 89 Abs. 2 AO).

## Fristen

- **Einspruch** § 355 Abs. 1 AO — ein Monat ab Bekanntgabe.
- **Klage Finanzgericht** § 47 Abs. 1 FGO — ein Monat ab Bekanntgabe der Einspruchsentscheidung.
- **Festsetzungsverjährung** § 169 AO — regelmäßig vier Jahre; bei leichtfertiger Steuerverkürzung fünf Jahre, bei Steuerhinterziehung zehn Jahre.
- **Aussetzung der Vollziehung** § 361 AO und § 69 FGO — jederzeit, bis Bestandskraft.
- **Erklärungsfristen** § 149 AO iVm § 150 AO; vertretene Steuerpflichtige Februar des Zweitfolgejahres.
- **Zugangsfiktion einfacher Brief** § 122 Abs. 2 Nr. 1 AO — seit PostModG 1.1.2025 vier Tage (vorher drei).

## Hauptgerichte

- Finanzgericht (FG) — erste Instanz; Senatsbesetzung.
- Bundesfinanzhof (BFH) — Revisionsinstanz, München.
- Strafgericht (AG/LG Wirtschaftsstrafkammer) bei Steuerstrafverfahren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Arbeitsgemeinschaft Steuerrecht im DAV.
- Deutscher Steuerberaterverband DStV (für Bezug zur StB-Praxis).

## Schnittstellen

- **`stb-`-Skills im selben Plugin** fuer Steuerberater-spezifische Workflows (BWA-/SuSa-/Bilanzpruefung, Liquiditaetsvorschau).
- **`kanzlei-allgemein`** für Fristen, Versand, Aktenführung.
- **`fachanwalt-handels-gesellschaftsrecht`** bei Tax-Aspekten der Unternehmensberatung.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Steuerforderungen in der Insolvenz.

## Anhang — FAO-Voraussetzungen (§ 9 FAO)

Nur relevant fuer den Erwerb des Fachanwaltstitels "Fachanwalt fuer Steuerrecht":

- Lehrgang 120 Stunden + drei Klausuren.
- 50 Faelle in den letzten drei Jahren aus dem Steuerrecht, davon Bezug zu mindestens drei der in § 9 Nr. 1 bis 3 FAO genannten Bereiche und zu allen drei Bereichen in der Falldokumentation; mindestens fuenf rechtsfoermliche Verfahren vor Finanzgerichten oder vergleichbare Verfahren.

Inhaltlich-fachlich macht der Fachanwaltstitel keinen Unterschied — alle Skills in diesem Plugin (`anw-*`) sind sowohl fuer Fachanwaeltinnen/Fachanwaelte als auch fuer alle anderen Anwaeltinnen/Anwaelte im Steuerrecht gleichermassen nutzbar.

## 5. `anw-selbstanzeige-371`

**Fokus:** Selbstanzeige nach § 371 AO als strafbefreiende Berichtigung bei Steuerhinterziehung vorbereiten und einreichen. Anwendungsfall Mandant hat Steuern hinterzogen und will Straffreiheit erlangen bevor Entdeckung droht. Vollständigkeit aller unverjährten Steuerstraftaten zehn Jahre § 376 AO ggf. 15 Jahre Sperrgründe § 371 Abs. 2 AO Nachentrichtung § 371 Abs. 3 AO Zinsen § 235 AO Zuschlag § 398a AO gestaffelt. Abgrenzung § 153 AO Berichtigungspflicht ohne Strafbefreiung zu § 371 AO Vorsatz und § 378 Abs. 3 AO Leichtfertigkeit. Output Berichtigungserklärung. Pflichtprüfung Hoechstrisikobereich mehrere Anwaelte.

# Selbstanzeige nach § 371 AO

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Selbstanzeige nach § 371 AO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Selbstanzeige nach § 371 AO

- **Spezialfrage (Selbstanzeige nach § 371 AO):** Selbstanzeige nach § 371 AO als strafbefreiende Berichtigung bei Steuerhinterziehung vorbereiten und einreichen. Anwendungsfall Mandant hat Steuern hinterzogen und will Straffreiheit erlangen bevor Entdeckung droht. Vollständigkeit aller unverjährten Steuerstraftaten zehn Jahre § 376 AO ggf. 15 Jahre Sperrgründe § 371 Abs. 2 AO Nachentrichtung § 371 Abs. 3 AO Zinsen § 235 AO Zuschlag § 398a AO gestaffelt. Abgrenzung § 153 AO Berichtigungspflicht ohne Strafbefreiung zu § 371 AO Vorsatz und § 378 Abs. 3 AO Leichtfertigkeit. Output Berichtigungserklärung. Pflichtprüfung Hoechstrisikobereich mehrere Anwaelte.
- **Prüfzugriff:** Sachverhalt, Norm, Zugang/Form/Frist oder Anspruchsvoraussetzung zuerst klären; Rechtsprechung erst danach als verifizierten Beleg nutzen.


## Disclaimer (Schlüsselstelle — mehrfach beachten)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kaltstart-Rückfragen

1. Welche Steuerart(en) sind betroffen?
2. Welche Veranlagungszeiträume? Mindestens zehn Kalenderjahre rückwärts prüfen (Festsetzungsverjährung § 169 Abs. 2 S. 2 AO).
3. Gibt es Hinweise auf eine bereits eingeleitete Steuerfahndung oder Außenprüfung?
4. Ist eine Sperrwirkung nach § 371 Abs. 2 AO bereits eingetreten?
5. Liegen vollständige Unterlagen vor? Schätzung nur als letztes Mittel (mit Sicherheitszuschlag).

## Anspruchsgrundlagen

- **Selbstanzeige bei Steuerhinterziehung:** § 371 AO.
- **Selbstanzeige bei leichtfertiger Steuerverkürzung:** § 378 Abs. 3 AO.
- **Absehen von Verfolgung in besonderen Fällen:** § 398a AO. Gestaffelte Zuschlagshöhe (seit 2015): bei Hinterziehungsbetrag > 25 000 EUR ein Zuschlag von **10 %**, > 100 000 EUR **15 %**, > 1 000 000 EUR **20 %** des hinterzogenen Betrags je Tat (zusätzlich zu Steuer und Zinsen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verjährung Steuerhinterziehung:** § 376 AO — fünfzehn Jahre seit der Beendigung; bei besonders schwerem Fall § 370 Abs. 3 AO ebenfalls fünfzehn Jahre.

## Abgrenzung § 153 AO — KEIN eigenständiger Strafbefreiungsgrund

**§ 153 AO ist eine steuerliche Berichtigungspflicht**, kein Strafbefreiungsgrund. Sie verpflichtet die Steuerpflichtige zur unverzüglichen Anzeige nachträglich erkannter Unrichtigkeiten in einer Steuererklärung.

Strafrechtliche Konsequenzen hängen davon ab, wie die ursprüngliche Falschangabe zu bewerten ist:

- **Nicht vorsätzlich und nicht leichtfertig:** Keine Straftat entstanden — rechtzeitige § 153-AO-Anzeige genügt.
- **Leichtfertig falsch (§ 378 AO):** Strafbefreiung wirkt erst über § 378 Abs. 3 AO.
- **Vorsätzliche Hinterziehung:** Strafbefreiung nur über § 371 AO.

### Neue Berichtigungspflicht § 153 Abs. 4 AO (ab 01.01.2025)

Durch das DAC7-Umsetzungsgesetz (BGBl. 2022 I S. 2730) wurde § 153 Abs. 4 AO eingefuegt; Wirkung ab 01.01.2025. Werden Pruefungsfeststellungen einer Aussenpruefung in einem unanfechtbaren Aenderungsbescheid umgesetzt, besteht eine **gesetzliche Berichtigungspflicht** fuer **nicht gepruefte Steuerarten und Folgezeitraeume**, soweit die Pruefungsfeststellungen darauf Auswirkungen haben. Verstoss kann eigenstaendig § 370 AO verwirklichen. Folge fuer den Anwalt: nach Abschluss einer BP ist die Reichweite der Feststellungen auf andere Veranlagungszeitraeume und Steuerarten zu pruefen.

### BMF-Anwendungserlass zu §§ 153, 371 AO

BMF-Schreiben vom 23.05.2016 (AEAO zu § 153 AO) und Aktualisierungen — Abgrenzung Berichtigung / Selbstanzeige; Indizwirkung eines Tax Compliance Management Systems (Tax-CMS) gegen Vorsatz und Leichtfertigkeit. Aktuellen AEAO-Stand ueber bundesfinanzministerium.de pruefen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wirksamkeitsvoraussetzungen § 371 Abs. 1 AO

### 1. Vollständigkeit

- **Alle unrichtigen oder unvollständigen Angaben** in vollem Umfang berichtigen.
- **Alle Steuerarten** der unverjährten Steuerstraftaten — mindestens **die letzten zehn Kalenderjahre** (§ 371 Abs. 1 Satz 2 AO).
- **Alle Veranlagungszeiträume** innerhalb dieses Zeitraums.
- Eine Teil-Selbstanzeige ist unwirksam (Vollständigkeitsgebot).

### 2. Sperrgründe (§ 371 Abs. 2 AO)

Die Selbstanzeige ist **gesperrt**, wenn:

- die Prüfungsanordnung bekanntgegeben wurde (§ 371 Abs. 2 S. 1 Nr. 1 lit. a AO),
- die Einleitung des Steuerstrafverfahrens oder Bußgeldverfahrens bekanntgegeben wurde (Nr. 1 lit. b),
- ein Amtsträger der Finanzbehörde zur steuerlichen Prüfung erschienen ist (Nr. 1 lit. c),
- ein Amtsträger zur Ermittlung einer Steuerstraftat erschienen ist (Nr. 1 lit. d),
- die Tat ganz oder zum Teil bereits entdeckt war und der Steuerpflichtige dies wusste oder damit rechnen musste (Nr. 2),
- der Hinterziehungsbetrag je Tat EUR 25 000 übersteigt — hier aber nur Sperrung der Strafbefreiung, nicht Sperrung der Möglichkeit; § 398a AO sieht das Absehen von Verfolgung gegen Zuschlag vor (Nr. 3 Nr. 4 iVm § 398a AO).

### 3. Rechtzeitige Nachzahlung (§ 371 Abs. 3 AO)

- Vollständige Nachzahlung der Steuer **plus** Hinterziehungszinsen (§ 235 AO) und Aussetzungszinsen sowie ggf. Zuschlag nach § 398a AO innerhalb der von der Behörde gesetzten Frist.

## Prüfschema

```
1. Vollständigkeitsanalyse
 - Alle Steuerarten und Zeiträume identifizieren.
 - Mindestens 10 Kalenderjahre rückwärts; bei Geldbeträgen
 prüfen ob § 376 AO greift (15 Jahre).
2. Sperrwirkungen § 371 Abs. 2 AO
 - Liegt eine Sperrwirkung vor? Wenn ja, in welchem Umfang?
3. Berichtigungsumfang ermitteln
 - Belegmäßige Aufarbeitung; Schätzung nur als ultima ratio
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 BGHSt 55, 180 Rn. 28).
4. Zahlbarkeit prüfen
 - Hinterzogene Steuer + Hinterziehungszinsen § 235 AO + ggf.
 Zuschlag § 398a AO. Stundung § 222 AO nur ausnahmsweise.
5. Abgrenzung § 153 AO vs. § 371 AO / § 378 Abs. 3 AO
 - Ursprungserklärung: vorsätzlich / leichtfertig / einfach unrichtig?
 - Bei Zweifel: Weg § 371 AO gehen.
6. Erklärung formulieren
 - Klare Bezeichnung als Berichtigungserklärung; Trennung
 nach Steuerart und Veranlagungszeitraum.
7. Einreichung
 - Direkt beim zuständigen Finanzamt; vorzugsweise vorab
 telefonische Anzeige des Termins.
8. Begleitung Strafverfahren § 393 AO
 - Mitwirkung im Steuerverfahren ruht, soweit Selbstbelastung
 droht. Strafverteidigung separat sicherstellen.
```

## Aufbau der Berichtigungserklärung

### 1. Rubrum

- Steuerpflichtiger mit Anschrift und Steuernummer.
- Vertretung (RA mit ELSTER-Zugang als Bevollmächtigter).
- Empfangsfinanzamt.

### 2. Erklärung

"Hiermit erstatte ich namens und im Auftrag des Steuerpflichtigen Selbstanzeige nach § 371 AO und berichtige die unrichtigen / unvollständigen Angaben in den Steuererklärungen für die Veranlagungszeiträume (Jahre) Steuerarten (...) wie folgt: ..."

### 3. Berichtigungsdaten

Pro Jahr pro Steuerart Aufstellung:

- bisherige Angabe
- richtige Angabe
- Differenz
- daraus folgende Steuer und Solidaritätszuschlag Kirchensteuer
- Hinterziehungszinsen § 235 AO
- bei Betrag über 25 000 EUR: Zuschlag § 398a AO (10 / 15 / 20 Prozent je nach Höhe)

### 4. Belege

Vollständige Bezugsbelege als Anlagen (Kontoauszüge Depotübersichten Belege ausländischer Banken Verlust- und Gewinnermittlungen falls relevant).

## Schreibvorlage

```
[Briefkopf]

Finanzamt [Ort] — Strafsachen- und Bußgeldstelle
[Anschrift] [Ort, Datum]

Steuernummer: [SteuerNr]

Berichtigungserklärung gemäß § 371 AO

Sehr geehrte Damen und Herren,

namens und in Vollmacht von [Mandantin], geb. [Datum], wohnhaft [Anschrift], geben wir die nachstehende vollständige Berichtigung iSd § 371 Abs. 1 AO für die nachfolgend bezeichneten Steuerarten und Veranlagungszeiträume ab.

I. Berichtigte Bemessungsgrundlagen

 Einkommensteuer
 2015: Kapitaleinkünfte aus Konto Nr. […] bei […], CH, in Höhe von EUR […]
 2016: …
 […]

 Umsatzsteuer
 […]

II. Anlagen

 - Aufstellung Erträge je Veranlagungszeitraum (Anlage 1)
 - Kontoauszüge / Depotauszüge (Anlage 2)
 - Vollmacht (Anlage 3)

III. Nachentrichtung

Die hinterzogenen Steuern, die Hinterziehungszinsen nach § 235 AO sowie ggf. der Zuschlag nach § 398a AO werden binnen der vom Finanzamt zu setzenden Frist gezahlt. Wir bitten um Mitteilung des konkreten Betrags und der Frist.

Wir weisen ausdrücklich darauf hin, dass diese Berichtigung als Selbstanzeige iSd § 371 AO zu behandeln ist.

Mit freundlichen Grüßen
[Anwalt, Fachanwalt für Steuerrecht und Strafverteidiger]
```

## Wirtschaftliche Vorprüfung

- Hat der Mandant die Mittel für Nachzahlung plus Zinsen plus Zuschlag?
- Sonst: ohne wirtschaftliche Voraussetzung keine Wirksamkeit — Folge strafrechtliche Verurteilung wahrscheinlich.

## Verfahren

1. **Schweigepflichtsentbindung** der Berater des Mandanten klären.
2. **Vollständige Datenerhebung** in allen Steuerarten und Jahren — Vermögensaufstellung Depots ausländische Konten.
3. **Doppelprüfung** durch zweiten qualifizierten Anwalt.
4. **Selbstanzeige einreichen** über **ELSTER** (Mein ELSTER — Nachrichtenfunktion) an Finanzamt. Alternativ Briefpost oder Telefax. **beA an Finanzamt seit 6.12.2024 unzulässig** (§ 87a Abs. 1 S. 2 AO n.F. nach JStG 2024) — eine Selbstanzeige per beA wäre formunwirksam und würde die Sperrwirkung des § 371 Abs. 2 AO durch andere Wege möglicherweise nicht durchbrechen können.
5. **Nachzahlung leisten** innerhalb der gesetzten Frist.

## Übergabe

- Mandantin schriftlich über die Strafaufhebung **und** das Risiko unvollständiger Selbstanzeige aufklären.
- Mandatsschwerpunkte trennen: Steuerverfahren (Fachanwalt Steuerrecht) und Strafverteidigung (Strafverteidiger). Skill `fachanwalt-strafrecht` koppeln.
- Zitierweise gemäß `zitierweise-deutsches-recht` v3.0.

## Hinweis

Dieser Skill ist Werkzeug zur Vorbereitung. Die Entscheidung Selbstanzeige zu erstatten verbleibt beim Mandanten nach vollständiger anwaltlicher Beratung. Steuerstrafrechtliche Bezüge erfordern besondere Expertise — bei Zweifeln Steuerstrafverteidiger hinzuziehen.

## 6. `anw-steuerbescheid-analyse`

**Fokus:** Steuerbescheid strukturiert auswerten und Angriffspunkte für Einspruch identifizieren. Anwendungsfall Mandant hat Steuerbescheid bekommen und fragt ob und wie er sich wehren kann. Bescheidarten Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Prüfungsbescheid. Erfasst Steuerart Veranlagungsjahr Nachforderung oder Erstattung Vorlaeufigkeitsvermerk Vorbehalt der Nachprüfung § 164 AO Aenderungsvorschriften §§ 172 ff. AO Bekanntgabe § 122 AO Vier-Tages-Fiktion seit 01.01.2025 PostModG. Output Analyse-Protokoll Angriffspunkte Fristenstatus Empfehlung Einspruch oder Akzeptanz. Nahtloser Übergang zu anw-einspruch-finanzamt.

# Steuerbescheid-Analyse

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Steuerbescheid-Analyse` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Analyse

1. Welche Steuerart und welches Veranlagungsjahr betrifft der Bescheid?
2. Liegt der Bescheid im Original vor (nicht nur Kopie oder Screenshot)?
3. Ist die Einspruchsfrist bereits abgelaufen? (Bekanntgabefiktion § 122 Abs. 2 AO — vier Tage seit 1.1.2025)
4. Wurde der Bescheid unter Vorbehalt der Nachprüfung (§ 164 AO) oder mit Vorläufigkeitsvermerk (§ 165 AO) erlassen? → andere Anpassungsmöglichkeiten
5. Liegt eine Außenprüfung zugrunde? → Schätzungsprobleme und Sicherheitszuschläge prüfen
6. Soll AdV beantragt werden? → Liquidität und Frist klären

## Zweck

Bescheid systematisch lesen vor dem Einspruch.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Eingaben

- Steuerbescheid (PDF Original; gescannt mit OCR).
- Steuererklärung des Veranlagungsjahres (zum Vergleich Soll-Ist).
- Bisheriger Mandatsstand.

## Prüfraster

### 1. Formale Prüfung

- **Behörde** zuständig (Wohnsitzfinanzamt § 19 AO; Betriebsstaettenfinanzamt § 18 AO)?
- **Adressat** korrekt (bei Eheleuten Zusammenveranlagung beide; bei Personengesellschaft gesonderte und einheitliche Feststellung — separater Bescheid)?
- **Steuerart** und **Veranlagungsjahr** klar?
- **Tenor** mit Steuerbetrag eindeutig?
- **Bekanntgabe** nach § 122 AO — Vier-Tages-Fiktion bei Postbescheiden (§ 122 Abs. 2 Nr. 1 AO n.F., seit 1.1.2025 PostModG; bei Aufgabe zur Post vor dem 1.1.2025: weiterhin Drei-Tages-Fiktion alter Fassung).
- **Rechtsbehelfsbelehrung** vollständig?

### 2. Inhaltliche Prüfung

- **Berechnung** der Steuer nachvollziehbar?
- **Einkünftearten** richtig zugeordnet (§§ 2 13–24 EStG)?
- **Werbungskosten / Betriebsausgaben** vollständig abgezogen?
- **Sonderausgaben Außergewöhnliche Belastungen** berücksichtigt?
- **Pauschalen** richtig?
- **Vorauszahlungen** richtig angerechnet (§ 36 EStG)?
- **Solidaritaetszuschlag Kirchensteuer** zutreffend?

### 3. Vorläufigkeit und Änderbarkeit

- **§ 164 AO** Vorbehalt der Nachprüfung — Bescheid jederzeit aenderbar bis Festsetzungsverjährung.
- **§ 165 AO** Vorläufigkeitsvermerk — Bescheid teilweise vorläufig.
- **§ 172 ff. AO** Änderungsvorschriften nach Bestandskraft (z. B. § 173 neue Tatsachen § 175 Änderungsbescheid).
- **§ 129 AO** offenbare Unrichtigkeit (Schreib- Rechenfehler).

### 4. Schätzung (§ 162 AO)

Bei Schätzungsbescheid:
- Begründung für Schätzungsbefugnis (Nicht-Abgabe Erklärung verletzte Mitwirkungspflicht).
- Schätzungsgrundlagen schlüssig?
- Höhe wirtschaftlich plausibel?
- Sicherheitszuschlaege im Rahmen?

### 5. Festsetzungsverjährung

- **§ 169 AO** Festsetzungsfrist regelmäßig vier Jahre; bei Hinterziehung zehn Jahre; bei Leichtfertigkeit fünf Jahre.
- **§ 170 AO** Beginn — mit Ablauf des Kalenderjahrs in dem die Steuer entstanden ist; bei Erklärungspflicht mit Ablauf des Kalenderjahrs der Abgabe spätestens nach drei Jahren.

### 6. Vollziehung

- **Fälligkeit** der Steuerschuld (§ 220 AO).
- **Anordnung sofortiger Vollziehung** durch Steuerbehörde nicht erforderlich — Einspruch hat **keine aufschiebende Wirkung** (§ 361 Abs. 1 AO Satz 1). Daher Antrag auf Aussetzung der Vollziehung notwendig wenn nicht gezahlt werden soll.

## Ausgabe

Analyseprotokoll mit:

1. Stammdaten Bescheid (Behörde Az Steuerart Jahr Datum Zugang)
2. Festsetzungsbetrag Soll-Ist-Vergleich
3. Rechtsbehelfsbelehrung mit Einspruchsfrist (ein Monat § 355 Abs. 1 AO)
4. Formfehler
5. Angriffspunkte sortiert nach Erfolgsaussicht
6. Empfehlung: Einspruch / Antrag § 129 AO / Änderungsantrag / nichts
7. Antrag auf Aussetzung der Vollziehung erforderlich?
8. Frist im Fristenbuch eintragen (Skill `anw-fristenbuch-steuerrecht`)

## 7. `anw-steuerstrafverteidigung-verstaendigung`

**Fokus:** Prüffeld für anw steuerstrafverteidigung verstaendigung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Strafverteidigung Steuerstrafsache mit Einstellung und Verständigung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Strafverteidigung Steuerstrafsache mit Einstellung und Verständigung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Mandant (Steuerpflichtiger, Geschäftsführer oder steuerlicher Berater) ist Beschuldigter in einem Steuerstrafverfahren wegen Steuerhinterziehung (§ 370 AO) oder leichtfertiger Verkürzung (§ 378 AO). Die Strafverteidigung zielt auf eine Einstellung ohne Hauptverhandlung (§ 153a StPO oder § 170 Abs. 2 StPO) oder auf eine Verständigung über den Strafrahmen (§ 257c StPO). Steuerlichen Hintergrund kennt der Steueranwalt besser als der Strafverteidiger — die Kombination beider Qualifikationen ist Stärke dieser Spezialverteidigung.

## Kaltstart-Rückfragen

1. Ermittlungsstand — Anfangsverdacht, Einleitung Strafverfahren (§ 397 Abs. 3 AO), Anklage, Hauptverhandlung?
2. Hinterziehungsumfang je Steuerart und Veranlagungszeitraum — nach Berechnung der Steufa oder eigener Prüfung?
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Beweislage Staatsanwaltschaft/Steufa — Bankkontendaten, Buchführung, Steuererklärungen, Aussagen?
5. Mandantenstatus — Steuerpflichtiger, GF, steuerlicher Berater?
6. Steuerschaden beziffert und beglichen (Teil-/Vollzahlung)? Ratenplan?
7. Wurde eine Selbstanzeige nach § 371 AO bereits eingereicht — Sperrwirkung § 371 Abs. 2 AO prüfen?
8. Vergütungsvereinbarung — RVG oder gesonderte Vereinbarung mit höherem Honorar?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Primärnormen

**§ 370 AO** — Steuerhinterziehung; Strafrahmen bis 5 Jahre, besonders schwerer Fall § 370 Abs. 3 AO bis 10 Jahre.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 378 AO** — Leichtfertige Steuerverkürzung; Ordnungswidrigkeit mit Geldbuße.

**§ 376 AO** — Verfolgungsverjährung: 10 Jahre regelmäßige Steuerhinterziehung; 15 Jahre bei besonders schwerem Fall.

**§ 393 Abs. 1 S. 2 AO** — Schutz vor Selbstbelastung im Besteuerungsverfahren: Zwangsmittel (§ 328 AO) dürfen nicht eingesetzt werden, soweit Selbstbelastungsgefahr besteht; Mitwirkungspflichten bleiben bestehen.

**§ 393 Abs. 2 AO** — Verwendungsverbot für nichtsteuerliche Straftaten: Angaben im Besteuerungsverfahren dürfen nicht für steuerfremde Delikte (Betrug § 263 StGB, Untreue § 266 StGB) verwendet werden. **Nicht**: für die Steuerstraftat selbst.

**§ 153a StPO** — Einstellung gegen Auflage; Bemessung Geldauflage orientiert sich faktisch an § 398a AO-Staffel.

**§ 257c StPO** — Verständigung im Strafverfahren; nur über Strafrahmen, nicht über Schuldspruch; Belehrungspflicht § 257c Abs. 5 StPO.

**§ 398a AO** — Absehen von Verfolgung in Selbstanzeige-Fällen; Zuschlagsstaffel 10/15/20 %.

**§ 371 AO** — Strafbefreiende Selbstanzeige; Vollständigkeitsgebot; Sperrgründe § 371 Abs. 2 AO.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Steuerstrafverteidigung


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Ermittlungsstand | Phase des Verfahrens; § 397 Abs. 3 AO Einleitungsbekanntgabe | Verfahrensstadium |
| 2 | Akteneinsicht § 147 StPO | Vollständige Akteneinsicht; Steufa-Datenträger anfordern; BGH-Reform 2017 | Beweislage klären |
| 3 | Hinterziehungsberechnung | Steufa-Berechnung vs. eigene Nachberechnung; Schätzungsgrundlage § 162 AO | Angriffspunkte |
| 4 | § 393 AO Trennungsgebot | Abs. 1: Zwangsfreiheit im Besteuerungsverfahren; Abs. 2: Verwendungsverbot nur für steuerfremde Delikte | Nicht überdehnen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 6 | Großes Ausmaß § 370 Abs. 3 AO | ≥ 50.000 EUR pro Tat → besonders schwerer Fall; § 153a StPO kaum möglich | Strategie-Weichenstellung |
| 7 | Strategische Option wählen | § 170 Abs. 2 StPO (Einstellung mangels Verdacht) / § 153a StPO / Strafbefehl / § 257c StPO / HV | Bestes Ergebnis |
| 8 | § 153a StPO-Auflage berechnen | Orientierung § 398a AO-Staffel; Hinterziehungsbetrag; wirtschaftliche Verhältnisse | Geldauflage-Rahmen |
| 9 | Steuerschaden begleichen | Frühe Zahlung strafmildernd; Voraussetzung für § 153a; Zinsen § 235 AO + Säumniszuschläge | Zahlungsnachweis |
| 10 | § 257c StPO-Verständigung | Geständnis; Strafrahmen vereinbaren; Belehrung § 257c Abs. 5 StPO; Aktennotiz | Schriftlich dokumentieren |
| 11 | Selbstanzeige § 371 AO parallel | Sperrwirkung § 371 Abs. 2 AO prüfen; nur für weitere VZ/Steuerarten außerhalb laufender Verfahren | Synergie nutzen |
| 12 | Beweisanträge HV | Schätzungsmängel § 162 AO; Verfahrensverletzung Steufa; SV-Gutachten Steuerberechnung | Bei streitiger HV |
| 13 | Verjährung prüfen | § 376 AO: 10 Jahre (normal), 15 Jahre (§ 370 Abs. 3 AO); Beginn bei Beendigung | Verjährungseinrede |
| 14 | Mandantenbelehrung | Vor Geständnis/Verständigung schriftliche Belehrung über § 257c Abs. 5 StPO; Risiken | Dokumentation |
| 15 | Abschluss und Dokumentation | Ergebnis; Zahlungsnachweis; Einstellungsbeschluss; Akte schließen | Mandatsabschluss |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Hinterziehungsbetrag | Staatsanwaltschaft / Steufa | Steuerakte, Außenprüfungsbericht, Bankdaten |
| Vorsatz § 370 AO | Staatsanwaltschaft | Korrespondenz, Aussagen, Buchführung |
| Strafmilderungsgrund Zahlung | Mandant | Überweisungsbelege, Zahlungsbestätigung FA |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Selbstanzeige vollständig § 371 AO | Mandant | Selbstanzeigeschreiben; Zahlung binnen Frist |
| Verjährung | Verteidigung | Steuerakten; Tatbeendigungsdatum |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Verfolgungsverjährung normal | § 376 AO | 10 Jahre ab Tatbeendigung | Tatbeendigung = Steuerfestsetzung bzw. Unterlassen |
| Verfolgungsverjährung besonders schwerer Fall | § 376 AO | 15 Jahre ab Tatbeendigung | § 370 Abs. 3 AO-Tatbestände |
| Selbstanzeige-Nachzahlung § 398a AO | § 371 Abs. 3 AO | Innerhalb der vom FA gesetzten Frist (typisch 30 Tage) | Fristversäumnis = kein Strafbarkeitsausschluss |
| Einspruch gegen Strafbefehl | § 410 StPO | 2 Wochen ab Zustellung | Keine Verlängerung |
| Beschwerde gegen Haftbefehl | § 304 StPO | 2 Wochen | Sofort nach Erlass |

## Typische Gegenargumente

| Gegenargument StA/Steufa | Erwiderung der Verteidigung |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Geständnis vor Akteneinsicht erforderlich" | Akteneinsicht erst; dann substanziiertes Teil-Geständnis; Vorab-Geständnis ohne Akte riskant |
| "Selbstanzeige gesperrt — Verfahren läuft" | Sperrung nur für dieselbe Steuerart und denselben VZ; andere VZ oder Steuerarten noch selbstanzeigefähig |
| "Schätzung § 162 AO methodisch korrekt" | Schätzungsmethode konkret angreifen; Konkretnachweise für niedrigere tatsächliche Einkünfte vorlegen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Steuerstrafverteidigung mit Verstaendigungsoption | Verteidigungs-Strategie nach Schema; Schriftsatz unten |
| Variante A — Mandant will Selbstanzeige als Weg | Selbstanzeige § 371 AO zuerst; Verstaendigung danach |
| Variante B — Steuerdelikte mit Geldwaesche-Bezug | Geldwaesche-Skill parallel; Gesamtstrategie koordinieren |
| Variante C — Mandant will auf keinen Fall Verurteilung riskieren | Einstellungs-Strategie § 153a StPO pruefen; Verstaendigung nur alternativ |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Schutzschrift zur Vorbereitung einer Einstellung § 153a StPO

```
An die Staatsanwaltschaft [Ort]
Aktenzeichen: [Az. StA]

In der Strafsache gegen [Beschuldigter Name], [Az.]

Stellungnahme zur Beweislage und Anregung Einstellung § 153a StPO

Sehr geehrte Damen und Herren,

wir vertreten Herrn/Frau [Name] in dem o.g. Verfahren.
Namens und in Vollmacht geben wir folgende Stellungnahme ab:

I. Zur Beweislage

Der Beschuldigte hat die Steuerhinterziehung in den
Veranlagungszeiträumen [Jahre] dem Grunde nach eingeräumt.
Dem Beschuldigten wurde vorgeworfen, Einnahmen aus [Tätigkeit]
in Höhe von EUR [Steufa-Betrag] nicht erklärt zu haben.

Tatsächlich beläuft sich der zutreffende Hinterziehungsbetrag
jedoch auf EUR [niedrigerer Betrag], weil:
1. [Betrag] entfällt auf Ausgaben die fälschlicherweise nicht
 als Betriebsausgaben erfasst wurden;
2. [Betrag] betrifft den VZ [Jahr], für den Verjährung
 (§ 376 AO) eingetreten ist;
3. [Betrag] entstammt einer Schätzung nach § 162 AO, die
 methodisch angreifbar ist (Begründung: ...).

II. Zum Steuerschaden und seiner Begleichung

Der Beschuldigte hat den von uns errechneten zutreffenden
Steuerschaden in Höhe von EUR [Betrag] mit Überweisung vom
[Datum] (Anlage 1) vollständig beglichen zuzüglich der Zinsen
nach § 235 AO (EUR [Betrag]) und Säumniszuschläge (EUR [Betrag]).

III. Anregung Einstellung § 153a StPO

Wir regen die Einstellung des Verfahrens gegen eine Geldauflage
gemäß § 153a StPO an. Die Voraussetzungen liegen vor:

1. Die Schuld des Beschuldigten ist, gemessen am
 tatsächlichen Hinterziehungsbetrag von EUR [Betrag],
 nicht schwer.
2. Der Steuerschaden ist vollständig beglichen.
3. Der Beschuldigte ist nicht vorbestraft.
4. Das öffentliche Interesse an der Strafverfolgung ist
 durch die vollständige Schadensbegleichung hinreichend
 gewahrt.

Wir schlagen eine Geldauflage von EUR [Betrag] (ca. [X] %
des Hinterziehungsbetrags; orientiert an § 398a AO-Staffel)
vor und bitten um Rückmeldung.

Anlage 1: Überweisungsbeleg Steuerschadenbegleichung
Anlage 2: Neuberechnung Hinterziehungsbetrag
Anlage 3: Vollmacht
```

### Baustein 2: Verständigungsgespräch-Protokoll § 257c StPO

```
PROTOKOLL VERSTÄNDIGUNGSGESPRÄCH
§ 257c StPO — Vertraulich

Datum: [Datum]
Teilnehmer: RA [Name] (Verteidiger), Staatsanwalt [Name] (StA),
 Richter [Name] (Gericht), ggf. Beschuldigter

1. Sachverhalt des vorgeworfenen Verhaltens: [kurze Darstellung]

2. Umfang des Geständnisses:
 Der Beschuldigte hat bereit erklärt, folgende Taten zu gestehen:
 [VZ X: Steuerart A, Betrag EUR y]
 [VZ Y: Steuerart B, Betrag EUR z]

3. Strafrahmen-Vereinbarung:
 Einigkeit über Strafrahmen von [x] bis [y] Tagessätzen bzw.
 Freiheitsstrafe [a]–[b] Monate auf Bewährung.
 Voraussetzung: Vollständige Zahlung Steuerschaden bis [Datum].

4. Belehrung nach § 257c Abs. 5 StPO:
 Der Beschuldigte wurde belehrt, dass das Gericht nicht an die
 Verständigung gebunden ist, wenn es bei der Urteilsfindung
 von einer in der Verständigung zu Grunde gelegten Bewertung
 des Sachverhalts oder der Rechtslage abweicht. Der
 Beschuldigte hat diese Belehrung zur Kenntnis genommen und
 auf das Gespräch-Ergebnis hingewiesen.

5. Unterschriften:
 RA [Name]: _____________
 Beschuldigter: _____________
 StA [Name]: _____________
```

### Baustein 3: Antrag auf Akteneinsicht § 147 StPO

```
An die Staatsanwaltschaft [Ort]
Az: [Steuerstrafverfahren]

Antrag auf vollständige Akteneinsicht § 147 StPO

Sehr geehrte Damen und Herren,

wir vertreten Herrn/Frau [Name] in dem oben bezeichneten Verfahren.

Wir beantragen vollständige Akteneinsicht nach § 147 Abs. 1 StPO,
umfassend:

1. Die vollständige Strafakte mit allen Ermittlungsunterlagen;
2. Die vollständigen Steuerakten einschließlich Außenprüfungsbericht
 und Kontrollmitteilungen;
3. Alle Steufa-Datenträger (USB, CD/DVD, elektronische Dateien)
 die zur Ermittlung des Hinterziehungsbetrags herangezogen wurden;
4. Sämtliche Bankabfragen und Kontrollmitteilungen.

Wir weisen darauf hin, dass ohne vollständige Akteneinsicht keine
sachgerechte Verteidigung möglich ist (§ 137 StPO) und sämtliche
Erklärungen — insbesondere etwaige Geständnisse — bis zur
vollständigen Akteneinsicht unter Vorbehalt stehen.

Mit freundlichen Grüßen
[RA]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| RVG-Grundgebühr Nr. 4100 VV | Pflichtverteidigungs-Vergütung als Mindest; höhere Vereinbarung sinnvoll | Steuerstrafverfahren komplex |
| Gesonderte Vergütungsvereinbarung | Stundensatz EUR 300–500/h; Verfahrensgebühr Nr. 4112 VV RVG + Zuschläge | Bei Hinterziehung > EUR 100.000 empfohlen |
| Kosten HV wenn keine Einstellung | Nr. 4118 VV; pro HV-Tag gesondert | HV-Termingebühren |
| § 153a StPO-Auflage Eigenanteil | EUR 5.000–200.000+ je nach Hinterziehungsbetrag | Wirtschaftliche Verhältnisse des Mandanten einbeziehen |
| Steuerschaden + Zinsen § 235 AO | Hinterziehungsbetrag × Zinssatz × Hinterziehungsjahre; ca. 1.8 %/Jahr | Vorab genau beziffern |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Hinterziehung < 50.000 EUR pro Tat, gezahlt | § 153a StPO anstreben; Einstellung ohne Hauptverhandlung; kein BZR-Eintrag |
| Hinterziehung 50.000–500.000 EUR | § 153a prüfen; ggf. Strafbefehl; ggf. § 257c StPO; Steuerschaden vorab zahlen |
| Hinterziehung > 500.000 EUR | § 370 Abs. 3 AO besonders schwerer Fall; § 257c StPO-Verständigung realistisch; keine § 153a |
| Beweislage schwach (Schätzung § 162) | § 170 Abs. 2 StPO-Einstellung anstreben; Schätzungsmängel substanziiert angreifen |
| Mandant will alles bestreiten | Akteneinsicht vollständig; Beweisanträge HV; Risiko der HV erläutern |
| Selbstanzeige für andere VZ parallel | Abstimmung mit StA-Verfahren; § 371 Abs. 2 AO-Sperrwirkung genau prüfen |

## Anschluss-Skills

- `anw-insolvenzreife-pruefung-17-19-inso` — wenn GF gleichzeitig § 15a InsO-Pflicht hat
- `stb-bwa-sus-bilanz-pruefung` — Ausgangsdaten für Hinterziehungsberechnung

## Quellen

- AO §§ 162, 222, 370, 371, 376, 378, 393, 397, 398a
- StPO §§ 147, 153a, 257c, 304, 407, 410
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Joecks/Jaeger/Randt, Steuerstrafrecht, 8. Aufl. 2015, § 393 Rn. 81 ff.

## 8. `anw-stundung-erlass-vollstreckungsaufschub`

**Fokus:** Anträge auf Stundung Erlass und Vollstreckungsaufschub bei Zahlungsproblemen stellen. Anwendungsfall Mandant kann fällige Steuerschulden vorueber-gehend oder dauerhaft nicht zahlen Vollstreckung droht. Stundung erhebliche Haerte § 222 AO ohne Anspruchsgefaehrdung. Erlass aus persoenlichen oder sachlichen Billigkeitsgründen § 227 AO. Vollstreckungsaufschub bei unbilligem Vollstreckungserfolg § 258 AO Verzinsung bei Stundung § 234 AO. Output Antrag mit Begründung Sicherheitsleistung Ratenzahlungsplan. Abgrenzung zu anw-aussetzung-vollziehung AdV und anw-insolvenzreife-prüfung-17-19-inso.

# Stundung § 222 AO / Erlass § 227 AO / Vollstreckungsaufschub § 258 AO

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Stundung § 222 AO / Erlass § 227 AO / Vollstreckungsaufschub § 258 AO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Anwaltliche Beratung und Antragstellung beim Finanzamt zur Streckung der Zahlungspflicht, wenn der Mandant fällige Steuern oder Bescheidforderungen vorübergehend oder dauerhaft nicht aufbringen kann. Drei abgestufte Instrumente — Stundung (Aufschub), Erlass (Verzicht), Vollstreckungsaufschub (vorläufiges Pausieren der Vollstreckung). Häufig in Sanierungskonstellationen kombiniert mit `anw-insolvenzreife-pruefung-17-19-inso` und `stb-warnschreiben-krisensignale`.

## Kaltstart-Rückfragen

1. Welche Steuerart und welcher Bescheid (Anspruchshöhe, Fälligkeit, ggf. Säumniszuschläge)?
2. Liquide Mittel auf 13 Wochen / vorhersehbare Zahlungseingänge?
3. Sicherheiten möglich (Bürgschaft, Hypothek, Pfändungspfandrechte)?
4. Bisher bereits Stundung beantragt / abgelehnt?
5. Vollstreckungsmaßnahmen bereits eingeleitet (Pfändung Konto, Lohn, Sachpfändung)?
6. Sanierungskonzept oder bestehender Ratenplan?
7. Strafverfahren steuerlich anhängig (Auswirkung auf § 227 AO-Würdigung)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 222 AO** — Stundung: Finanzbehörde kann Anspruch ganz oder teilweise stunden, wenn Einziehung **erhebliche Härte** wäre und Anspruch durch die Stundung **nicht gefährdet** wird; in der Regel gegen **Sicherheitsleistung** und mit **Verzinsung** § 234 AO.
- **§ 227 AO** — Erlass aus Billigkeitsgründen (sachlich oder persönlich); endgültiger Verzicht oder vorläufiger Erlass (§ 163 AO als materiellrechtliche Variante).
- **§ 163 AO** — Abweichende Festsetzung aus Billigkeitsgründen (häufig als Vorgriff vor § 227 AO genutzt).
- **§ 258 AO** — Vollstreckungsaufschub: einstweilige Einstellung oder Beschränkung der Vollstreckung; **kein Verzicht auf die Forderung**.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 240 AO** — Säumniszuschläge: 1 % pro angefangenem Monat der Säumnis (Mindestbetrag 5 EUR). Bei Stundung **keine** Säumniszuschläge.
- **AEAO** zu §§ 222, 227, 258 AO — Verwaltungsanweisungen mit Praxis-Maßstab.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Drei-Stufen-Vorgehen

### Stufe 1 — Stundung § 222 AO

Voraussetzungen:
1. **Erhebliche Härte** — Liquiditätsbeleg (BWA, 13-Wochen-Vorschau aus `stb-liquiditaetsvorschau-3wochen`, OPOS).
2. **Keine Anspruchsgefährdung** — Vermögensverhältnisse darstellen (Vermögensaufstellung), nicht erkennbarer Insolvenzfall.
3. **Sicherheitsleistung** — Bankbürgschaft, Hypothek, Sicherungsabtretung; alternativ ohne Sicherheit, dann Begründung schlüssig.
4. **Ratenzahlungsplan** — typisch monatlich, Zeitraum max. 12 Monate (Verlängerung möglich).

Inhalt Antrag:
- Bezeichnung Bescheid + Anspruchshöhe + Fälligkeit
- Schilderung wirtschaftlicher Lage (Bilanz, BWA, Liquiditätsvorschau)
- Ratenzahlungsangebot mit konkreten Monatsraten + Endtermin
- Sicherheiten-Angebot mit Bewertung
- Verzinsung anerkannt (oder Antrag auf Zinsverzicht § 234 Abs. 2 AO)

### Stufe 2 — Erlass § 227 AO / § 163 AO

Voraussetzungen:
1. **Sachliche Billigkeit** — Steuererhebung steht im **Widerspruch zum Gesetzeszweck** (z. B. unbeabsichtigte Härte einer Norm im konkreten Einzelfall; Beweis: Gesetzgebungsmaterialien, BFH-Linie).
2. **Persönliche Billigkeit** — wirtschaftliche oder persönliche Verhältnisse, die Steuererhebung **unzumutbar** machen (Existenzgefährdung; nicht: nur Schwierigkeiten).
3. **Erlasswürdigkeit** — Mandant hat keine schuldhafte Steuerverkürzung beigetragen.

Antrag im Anschluss an erfolglose Stundung oder bei dauerhafter Unmöglichkeit; § 163 AO oft taktisch vorgezogen vor § 227 AO.

### Stufe 3 — Vollstreckungsaufschub § 258 AO

Voraussetzungen:
1. **Unbilliger Vollstreckungserfolg** — Vollstreckung führt zu unverhältnismäßiger Härte (z. B. Existenzvernichtung trotz mittelfristig sicherer Zahlung).
2. **Vorübergehend** — anders als Stundung beendet § 258 AO nicht die Fälligkeit, sondern stoppt nur die Zwangsmaßnahmen.
3. **Antrag bei Vollstreckungsstelle** — separate Behörde innerhalb des Finanzamts; eilbedürftig (Stunden-Frist möglich).

## Schreibvorlage Stundungsantrag (verkürzt)

```
[Kanzlei-Briefkopf] [Datum]

An das
Finanzamt [Ort]
[Anschrift]

Vorab per ELSTER / Telefax — Kein beA an Finanzamt seit 6.12.2024 (§ 87a Abs. 1 S. 2 AO n.F.)

Steuerpflichtiger: [Mandant], StNr. [...], Steuer-ID [...]
Bescheid vom [...] ueber [Steuerart], Faelligkeit [...]
Hauptforderung EUR [...], Saeumniszuschlag bisher EUR [...]

Antrag auf Stundung gemaess § 222 AO

Sehr geehrte Damen und Herren,

namens und im Auftrag des oben bezeichneten Steuerpflichtigen beantrage
ich, die durch Bescheid vom [...] faellige Steuerforderung in Hoehe von
EUR [...] gemaess § 222 AO bis zum [Datum] zu stunden, hilfsweise
Ratenzahlung in [Anzahl] Monatsraten zu je EUR [...] zu bewilligen.

Begruendung

I. Erhebliche Haerte (§ 222 Satz 1 AO)
[Schilderung Liquiditaetslage anhand BWA / 13-Wochen-Vorschau; konkret
beziffern, dass sofortige Zahlung Existenz der Gesellschaft gefaehrden
oder zu Insolvenzreife fuehren wuerde.]

II. Keine Gefaehrdung des Anspruchs
[Vermoegensaufstellung; Auftragslage; ggf. Sanierungskonzept nach IDW
S 6; Belege.]

III. Sicherheitsleistung
[Konkretes Angebot, z. B. Bankbuergschaft EUR [...] von [Bank], oder
Begruendung, warum Sicherheitsleistung nicht moeglich/erforderlich.]

IV. Ratenzahlungsplan
[Tabelle Monat / Rate / Restschuld]

V. Verzinsung
Die Verzinsung gemaess § 234 AO wird anerkannt / Es wird Verzicht auf
Zinsen gemaess § 234 Abs. 2 AO beantragt, weil [...].

Mit freundlichen Gruessen
[Unterschrift]
Rechtsanwalt/-anwaeltin
[Anlagen: BWA, Liquiditaetsvorschau, Vermoegensaufstellung, Sicherheits-
angebot]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Antrag ohne Sicherheit + ohne BWA | Ablehnung absehbar | Begründung dünn | volle Belege + Sicherheit |
| Insolvenzreife schon eingetreten | § 222 AO entfällt; Antrag mit § 15a InsO unvereinbar | Krise unklar | klar nicht insolvenzreif |
| Säumnis bereits eingetreten | Säumniszuschläge laufen weiter; Stundungsantrag schließt sie nicht aus | Erstantrag rechtzeitig | rechtzeitig vor Fälligkeit |
| Vollstreckung läuft | § 258 AO kombinieren erforderlich; Eilbedürftigkeit | Vollstreckung droht | keine Vollstreckung |

## Workflow

### Phase 1 — Antrag

- Belege sammeln (BWA, OPOS, Liquiditätsvorschau, Vermögensaufstellung).
- Antrag formuliert und über ELSTER / Telefax / persönlich beim Finanzamt; **kein beA** an Finanzamt (§ 87a Abs. 1 S. 2 AO n.F.; JStG 2024).
- Eingangsbestätigung dokumentieren.

### Phase 2 — Reaktion Finanzamt

- Rückfragen FA bedienen (typisch: Nachweis Sicherheitsleistung).
- Bei Ablehnung: Einspruch (`anw-einspruch-finanzamt`), AdV-Antrag falls Vollstreckung droht (`anw-aussetzung-vollziehung`).

### Phase 3 — Bewilligung

- Stundungsbescheid mit Auflage (Sicherheitsleistung, Ratenplan) prüfen.
- Auflagenerfüllung dokumentieren (Mandant: Pünktlichkeit Raten zentral).
- Bei Auflagenverletzung droht Widerruf der Stundung.

### Phase 4 — Bei dauerhafter Unmöglichkeit

- Übergang zu § 227 AO (Erlass) prüfen.
- Sanierungskonzept (IDW S 6) als Grundlage.
- Ggf. parallel Verständigung mit anderen Gläubigern.

## Querverweise

- `anw-einspruch-finanzamt` — bei Ablehnung
- `anw-aussetzung-vollziehung` — wenn Vollstreckung trotz Antrag läuft
- `anw-insolvenzreife-pruefung-17-19-inso` — Pflichtprüfung vor § 222 AO
- `stb-liquiditaetsvorschau-3wochen` — Belege-Quelle
- `stb-warnschreiben-krisensignale` — Steuerberater hat parallel hinzuweisen
- `fachanwalt-insolvenz-sanierungsrecht` — bei Übergang Sanierung/StaRUG

## Quellen und Updates

Stand: 05/2026. § 234 AO Stundungszinssatz aktuell unverändert 0.5 %/Monat (gesonderter Zinssatz, BVerfG-Urteil zu § 233a AO greift nicht direkt). AEAO Stand 2024 berücksichtigt. Bei Reform der Säumnis-/Stundungszinsen aktualisieren.

## 9. `anw-umsatzsteuer-vorsteuerabzug-pruefen`

**Fokus:** Prüffeld für anw umsatzsteuer vorsteuerabzug pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Umsatzsteuer-Vorsteuerabzug prüfen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Umsatzsteuer-Vorsteuerabzug prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Vorsteuerabzug § 15 UStG ist ein zentrales Element der USt-Mandanten-Beratung — bei Fehlern Berichtigung mit Zins-Folgen, im schlimmsten Fall Strafverfahren.

## Schritt 1 — Voraussetzungen § 15 Abs. 1 UStG

### 1. Unternehmer-Eigenschaft § 2 UStG

- **Selbstständige Tätigkeit**
- **Nachhaltige Einnahmen-Erzielung**
- **Auch bei steuerfreien Umsätzen** Unternehmer
- Bei Holding ohne aktive Geschäfts-Tätigkeit problematisch

### 2. Leistung von Unternehmer

- **Rechnungsgeber** ebenfalls Unternehmer
- USt-IdNr. überprüfbar (qualifizierte Bestätigungsanfrage BZSt)

### 3. Für sein Unternehmen ausgeführt

- **Mindestens 10 Prozent** unternehmerische Nutzung § 15 Abs. 1 Satz 2 UStG
- Bei Pkw-Sondernorm
- Bei Gemischt-Nutzung Vorsteuerabzug anteilig

### 4. Ordnungsgemäße Rechnung § 14 UStG

Pflichtangaben § 14 Abs. 4 UStG:
- **Name und Anschrift Rechnungssteller**
- **Name und Anschrift Leistungs-Empfänger**
- **Steuer-Nummer oder USt-IdNr.**
- **Ausstellungs-Datum**
- **Rechnungs-Nummer** fortlaufend einmalig
- **Menge und Art** der Lieferung / Leistung
- **Zeitpunkt** der Lieferung / Leistung
- **Entgelt** netto pro Steuer-Satz
- **Steuer-Betrag** mit angewandtem Satz
- **Im Fall Steuerbefreiung** Hinweis auf Befreiungs-Vorschrift
- **Bei Reverse-Charge** Hinweis "Steuerschuldnerschaft des Leistungs-Empfängers"

### 4a. eRechnung-Pflicht ab 1.1.2025 (Wachstumschancengesetz)

**B2B-eRechnung** durch Wachstumschancengesetz (WtcG, 27.3.2024) in § 14 UStG eingefuehrt — Pflicht seit **1.1.2025** mit gestaffelten Uebergangsfristen:

- **Empfangs-Pflicht**: Seit 1.1.2025 muss jeder inländische Unternehmer für inländische B2B-Umsätze eRechnungen empfangen können.
- **Ausstellungs-Pflicht** (gestaffelt):
 - bis 31.12.2026: Papier-/PDF-Rechnung mit Zustimmung des Empfaengers weiterhin zulaessig (Übergang)
 - bis 31.12.2027: nur fuer Unternehmer mit Vorjahresumsatz ≤ 800 000 EUR Papier-Erleichterung
 - ab 1.1.2028: vollständige eRechnungspflicht für alle B2B-Inlands-Umsätze
- **Format**: strukturiertes, maschinenlesbares Format nach EN 16931 (z. B. **XRechnung** oder **ZUGFeRD ab Profil EN-16931**); reines PDF ohne strukturierte XML-Daten ist KEINE eRechnung.
- **Folge fehlerhafter Rechnung**: Vorsteuerabzug nach § 15 Abs. 1 UStG kann verweigert werden, wenn Rechnungspflicht eRechnung verletzt ist. Massgebend:
 - **BMF-Schreiben vom 15.10.2024**, GZ III C 2 - S 7287-a/23/10001 :007 (Einfuehrungsschreiben eRechnung).
 - **BMF-Schreiben vom 15.10.2025**, GZ III C 2 - S 7287-a/00019/007/243 (Zweites Anwendungsschreiben mit Anpassung des UStAE; unterscheidet Format- und Inhaltsfehler-Klassen; Validierungsempfehlung des Senders, Pruefpflichten des Empfaengers).
- **Ausnahmen**: Kleinbetragsrechnungen ≤ 250 EUR § 33 UStDV; Fahrausweise § 34 UStDV; Umsätze an Endverbraucher (B2C) bleiben außerhalb.

## Schritt 2 — Ausschluss § 15 Abs. 2 UStG

### Steuerfreie Umsätze mit Vorsteuerabzugs-Ausschluss

- **§ 4 Nr. 8 UStG** Geld- Bank-Geschäfte
- **§ 4 Nr. 9 a UStG** Grundstücks-Umsätze
- **§ 4 Nr. 10 UStG** Versicherungs-Umsätze
- **§ 4 Nr. 12 UStG** Wohnungs-Vermietung
- **§ 4 Nr. 14 UStG** ärztliche Heilbehandlungen
- **§ 4 Nr. 19 UStG** Schulen und Hochschulen

### Ausnahmen § 15 Abs. 3 UStG (trotz Steuerfreiheit Abzug)

- **Ausfuhr-Lieferung** § 4 Nr. 1 a iVm § 6 UStG
- **Innergemeinschaftliche Lieferung** § 4 Nr. 1 b iVm § 6a UStG
- **Hilfsumsatz-Konstellation**

## Schritt 3 — Spezielle Konstellationen

### Pkw

- **Vorsteuerabzug** möglich bei mindestens 10 Prozent unternehmerische Nutzung
- **Anteilig** bei gemischt-Nutzung
- **Eigenleistung Privatnutzung** als Wertabgabe steuerbar § 3 Abs. 9a UStG

### Bewirtungs-Aufwendungen

- Bei Bewirtungs-Beleg mit Pflichtangaben § 4 Abs. 5 Nr. 2 EStG Vorsteuer-Abzug zulässig
- 70-Prozent-Beschränkung gilt nur für ESt nicht USt
- Voller Vorsteuerabzug bei Bewirtungs-Aufwendungen

### Bewirtung von Mitarbeitern

- Voller Vorsteuerabzug
- Keine Werts-Abgabe wenn freiwillig im überwiegend betrieblichen Interesse

### Geschenke

- **Über EUR 35** keine Vorsteuer-Abzugs-Berechtigung
- **Streuwerbe-Artikel** unter EUR 10 ohne Limit

### Reisekosten

- **Vorsteuerabzug** für Hotel Verpflegung Mietwagen bei beleghafter Rechnung
- **Pauschal-Beträge** ohne Vorsteuer-Bezug

### Drittland-Bezug

- **Einfuhr-Umsatzsteuer** als Vorsteuer abzugsfähig § 15 Abs. 1 Satz 1 Nr. 2 UStG
- **Ausland-Umsatzsteuer** nicht in DE abzugsfähig — Vergütungsverfahren

## Schritt 4 — Berichtigung § 15a UStG

### Änderung der Verhältnisse

- Bei Wirtschaftsgütern (typisch Anlagevermögen Immobilien)
- Bei nutzungsspezifischer Änderung des Vorsteuerabzugs-Bezugs

### Berichtigungs-Zeitraum

- **Fünf Jahre** bei beweglichen Wirtschaftsgütern
- **Zehn Jahre** bei Grundstücken / Gebäuden
- Beginnt mit Erstverwendung

### Berechnung

- **Pro Jahr ein Fünftel / ein Zehntel** des ursprünglichen Vorsteuer-Betrags
- Bei Veränderung in einem Jahr Korrektur dieses Anteils

### Beispiel

- Immobilie 2021 mit 100% Vorsteuerabzug, Wert EUR 1 Mio, USt EUR 190.000
- 2024 zur 50% Wohnnutzung umgewidmet
- Berichtigung: EUR 190.000 / 10 Jahre * 50% = EUR 9.500 pro Jahr Berichtigung

## Schritt 5 — Praktische Prüfung Rechnung

### Checkliste

- [ ] Name und Anschrift komplett (auch bei kleinen Beträgen — Klein-Betrag-Rechnung bis EUR 250 § 33 UStDV)
- [ ] Steuer-Nummer / USt-IdNr. richtig
- [ ] Rechnungs-Nummer und Datum vorhanden
- [ ] Leistungs-Beschreibung konkret (nicht "Allgemeine Dienstleistung")
- [ ] Leistungs-Zeitraum genannt
- [ ] Netto-Beträge pro Steuer-Satz separat
- [ ] Steuer-Betrag separat ausgewiesen
- [ ] Rechtsgrundlage bei Reverse-Charge

### Bei Mängeln

- **Berichtigung** erfordern beim Rechnungsstellers
- **Vor-Vorsteuer-Abzug nicht möglich** bis Berichtigung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 6 — Klein-Betrag-Rechnung § 33 UStDV

### Bis EUR 250

- Reduzierte Pflichtangaben
- Aber: Steuer-Satz angegeben
- Anwendbar typisch bei Bewirtungs-Belegen Tankstellen-Rechnungen

## Schritt 7 — Reverse-Charge § 13b UStG

### Anwendungs-Bereiche

- **EU-Vorleistungen** § 13b Abs. 1 UStG
- **Baudienstleistungen** § 13b Abs. 5 Nr. 4 UStG
- **Schrott / Industrieabfall** § 13b Abs. 5 Nr. 6 UStG
- **Telefon-Karten Strom Gas** § 13b Abs. 5 Nr. 6
- **Mobiltelefone Tablet Spielekonsolen** ab EUR 5000 § 13b Abs. 5 Nr. 11

### Vorgehen

- **Empfänger schuldet USt**
- Rechnung ohne USt-Ausweis
- **Hinweis** "Steuerschuldnerschaft des Leistungs-Empfängers"

### Steuer-Schuld und Vorsteuer

- Rechnungs-Empfänger meldet USt und Vorsteuer zugleich
- Bei voll vorsteuerabzugs-berechtigtem Empfänger Null-Effekt

## Schritt 8 — Steuerstraf-Risiken

### Karussell-Geschäfte

- Vorsteuer-Abzug aus Schein-Lieferungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Aufmerksamkeits-Pflicht bei unüblich niedrigen Preisen
- Verpflichtung zur Sorgfalts-Pflicht

### Bei Verdacht

- Sofort Skill `anw-mandat-triage-steuerrecht` Eil-Modus
- Strafanzeige droht

## Schritt 9 — Berichtigungs-Erklärung § 153 AO

### Pflicht zur Korrektur

- Bei Erkennen einer falschen Steuer-Erklärung
- Unverzüglich
- An zuständiges Finanzamt

### Wirkung

- Verhindert Selbstanzeige-Bedarf bei rechtzeitig
- Bei Vorsteuer-Karussell mit Wissen ggf. nicht ausreichend

## Schritt 10 — Bei Außenprüfung

- Stichprobe-Prüfung Rechnungs-Pflichten
- Vorsteuer-Abzug bei mangelnder Sorgfalt korrigiert
- Hinzuschätzung möglich

## Ausgabe

- `vorsteuer-pruefung-{az}.md`
- Rechnungs-Tabelle mit Mängel-Bewertung
- Bei Mangel Korrektur-Anforderung
- Berichtigung-Vorbereitung wenn relevant
- Frist im Fristenbuch (USt-Voranmeldung)

## Quellen

- UStG §§ 1 2 3 4 13b 14 15 15a
- UStDV § 33
- AO § 153
- EStG § 4 Abs. 5
- BFH V. Senat XI. Senat
- BMF-Schreiben vom 15.10.2024 (Einfuehrung eRechnung) und BMF v. 15.10.2025 (zweites Anwendungsschreiben eRechnung, GZ III C 2 - S 7287-a/00019/007/243).
- **Steueraenderungsgesetz 2025** (BGBl. 2025 I Nr. 363, verkuendet 23.12.2025): Erweiterung des ermaessigten USt-Satzes (7 %) auf Restaurant- und Verpflegungsdienstleistungen (ohne Getraenke) fuer Umsaetze nach dem 31.12.2025.
- Sölch/Ringleb UStG
- Tipke/Lang Steuerrecht

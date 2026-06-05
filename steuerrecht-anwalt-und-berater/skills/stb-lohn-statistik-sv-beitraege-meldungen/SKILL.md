---
name: stb-lohn-statistik-sv-beitraege-meldungen
description: "STB Lohn Statistik SV Beitraege Meldungen: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Lohn Statistik SV Beitraege Meldungen

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **STB Lohn Statistik SV Beitraege Meldungen** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-lohn-statistik-meldungen-destatis` | Statistik-Meldungen Verdienststatistik Destatis. Anwendungsfall jaehrliche oder unterjaehrige Statistik-Meldungen an das Statistische Bundesamt Verdienste Arbeitszeit. Methodik Pflicht-Prüfung Erfassung Übermittlung. Output Statistik-Meldung. |
| `stb-lohn-sv-beitraege-grundlagen` | Sozialversicherungs-Beitraege Grundlagen RV KV PV AV Umlagen. Anwendungsfall monatliche Lohnabrechnung mit SV-Berechnung Beitragsbemessungsgrenzen AG-AN-Aufteilung Sonderfaelle. Methodik Beitragsberechnung mit JAEG BBG Zusatzbeitrag KV. Output Prüfraster SV-Beitraege. |
| `stb-lohn-sv-meldungen-dakota-svnet` | SV-Meldungen über sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Übermittlung Prüfung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen. |
| `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` | Überstunden Arbeitszeitkonto Stundenkonto Auszahlung. Anwendungsfall AN haeuft Überstunden an Bilanzierung im Arbeitszeitkonto Abbau in Freizeit oder Auszahlung lohn- und sv-rechtliche Behandlung. Methodik Aufzeichnung MiLoG Bewertung Stand. Output Arbeitszeitkonto-Abrechnung. |
| `stb-lohn-umlage-u1-u2-insogeld-umlage` | Umlagen U1 U2 Insolvenzgeld-Umlage. Anwendungsfall AG-Umlagen monatlich Erstattung Krankheit Mutterschaft Insolvenz Berechnung Saetze Variabilitaet KK. Methodik Prüfung Pflicht Kleinunternehmer 30 AN. Output Umlage-Berechnung. |
| `stb-lohn-vermoegenswirksame-leistungen` | Vermögenswirksame Leistungen VL AG-Anteil AN-Sparzulage. Anwendungsfall AG-Zuschuss bis 480 EUR jaehrlich AN-Sparzulage einkommensabhaengig Bausparen Aktien-Fonds. Methodik Prüfung Antrag AN-Sparzulage Beratung. Output VL-Konfiguration. |
| `stb-lohn-werkstudent-pauschalen` | Werkstudent SV-Status 20-Stunden-Grenze pauschale Beitraege. Anwendungsfall Beschaeftigung Student Werkstudentenprivileg KV-Befreiung RV-Pflicht JAEG nicht relevant Klassifizierung. Methodik Prüfung 20-Stunden-Woche vorlesungsfreie Zeit Antrag KV-Befreiung. Output Werkstudenten-Abrechnung. |
| `stb-mandantenfragebogen-jahresabschluss` | Mandantenfragebogen zum Jahresabschluss. Anwendungsfall JA-Vorbereitung systematische Datenerhebung vom Mandanten Bestaende Forderungen Verbindlichkeiten Rückstellungen Sondervorgaenge. Methodik strukturierter Fragebogen Prüfliste. Output ausgefuellter Fragebogen Datenbasis für Jahresabschluss. |
| `stb-online-portal-datev-mandantenshop` | DATEV Unternehmen Online Mandantenshop. Anwendungsfall Belegtransfer Bank-Abruf Auswertungs-Download Mandantenakte digital für Mandant. Methodik Konfiguration Benutzer Schulung Mandant. Output eingerichtetes Portal. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Lohn Statistik SV Beitraege Meldungen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-lohn-statistik-meldungen-destatis`

**Fokus:** Statistik-Meldungen Verdienststatistik Destatis. Anwendungsfall jaehrliche oder unterjaehrige Statistik-Meldungen an das Statistische Bundesamt Verdienste Arbeitszeit. Methodik Pflicht-Prüfung Erfassung Übermittlung. Output Statistik-Meldung.

# Statistik-Meldungen — Verdienststatistik Destatis

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Statistik-Meldungen — Verdienststatistik Destatis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der AG ist gesetzlich verpflichtet, Verdienst- und Arbeitszeitdaten an das Statistische Bundesamt (Destatis) bzw. an das jeweilige Statistische Landesamt zu liefern. Die wichtigsten Statistiken: Verdiensterhebung (vierteljaehrlich), Verdienststrukturerhebung (4-Jahres-Rhythmus), Lohnstatistik. Die Pflicht trifft ausgewaehlte Stichproben-Mandanten; nicht alle AG. Bei Aufforderung muss elektronisch geliefert werden.

## Kaltstart-Rueckfragen

1. Hat der Mandant Aufforderung von Destatis/Landesamt erhalten?
2. Welche Statistik wird angefordert (Quartal, 4-Jahres, anlassbezogen)?
3. Wieviele AN sind im Berichtszeitraum?
4. Welche Lohndaten muessen geliefert werden?
5. Welche Sondervergueteungen sind einzubeziehen?
6. Welche Form der Uebermittlung (Online-Portal, Excel)?
7. Welche Frist?
8. Liegen bereits Vorjahres-Meldungen vor?

## Rechtlicher Rahmen

### Primaernormen

**Bundesstatistikgesetz (BStatG)** — Allgemeines Statistikgesetz.

**Verdienststatistikgesetz (VerdStatG)** — Spezifische Verdiensterhebungen.

**§ 15 BStatG** — Auskunftspflicht der Befragten.

**§ 16 BStatG** — Geheimhaltung der Einzelangaben (BStatG-Fassung 2016 BGBl. I S. 2006; Paragraphennummerierung bei Gesetzesnovellierung ueber aktuelle BStatG-Fassung auf gesetze-im-internet.de pruefen).

### Verwaltungsanweisungen

- Destatis-Online-Portal IDEV.
- Statistische Landesamter Anweisungen.

## Workflow

### Phase 1 — Aufforderungs-Pruefung

- Liegt schriftliche Aufforderung mit Az vor?
- Welche Frist?
- Welche Statistik konkret?

### Phase 2 — Datenaufstellung

| Statistik | Daten | Frist |
|---|---|---|
| Verdiensterhebung Quartal | Bruttolohnsumme, Stunden, AN-Zahl je Lohngruppe | 4-6 Wochen nach Quartalsende |
| Verdienststrukturerhebung 4 Jahre | Individuelle AN-Daten (anonymisiert) | Festgelegt |
| Statistik Berufsgenossenschaften | Lohnsummen, Arbeitsunfaelle | Jaehrlich |
| Bundesagentur-Statistik | Beschaeftigungsdaten ueber DEUEV | Laufend |

### Phase 3 — Uebermittlung

- Destatis-Portal IDEV (Internet-Datenerhebung im Verbund).
- Login mit Kennung.
- Daten als Excel-Vorlage oder online ausfuellen.
- Bestaetigung nach Versand.

### Phase 4 — Datenschutz

- Daten werden anonymisiert ausgewertet.
- Keine Personalisierung in Statistik moeglich.
- Geheimhaltungspflicht beachten.

### Phase 5 — Bei Verspaetung

- Mahnung mit Frist.
- Bei wiederholter Nichtmeldung: Bussgeld bis 5.000 EUR.
- Schaetzung der Werte durch Destatis moeglich.

### Phase 6 — Dokumentation

- Versendetes Formular in Mandantenakte.
- Bestaetigungs-E-Mail.
- Folge-Aufforderungen vermerken.

## Output

- Statistik-Meldung an Destatis.
- Versandbestaetigung in Mandantenakte.

## Strategie und Praxis-Tipps

- Aufforderungen rechtzeitig erkennen — wenn beim Mandanten landet, oft uebersehen.
- Bei wiederkehrenden Statistiken (Verdiensterhebung Quartal): Dauer-Wiedervorlage.
- DATEV-LODAS Datenexport oft direkt zur Statistik-Vorlage moeglich.
- Bei sehr kleinen Mandanten (wenig AN): Befreiung von der Stichprobe pruefen.
- StBVV: Statistik-Meldung als Sonderauftrag (Zeithonorar).
- DATEV-Tipp: DATEV LODAS Statistik-Schnittstelle nutzen.

## Querverweise

- `stb-lohn-jahresmeldungen-ahn-asn-besondere` — Jahresmeldungen.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-lohn-sv-meldungen-dakota-svnet` — sv.net.

## Quellen und Updates

Stand: 05/2026.

- BStatG §§ 15, 16 (Fassung 2016, BGBl. I S. 2006; bei Gesetzesaenderung aktuelle Fassung auf gesetze-im-internet.de pruefen).

- VerdStatG.
- Destatis-IDEV-Portal.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 ersetzt (Paragraphennummerierung BStatG Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-lohn-sv-beitraege-grundlagen`

**Fokus:** Sozialversicherungs-Beitraege Grundlagen RV KV PV AV Umlagen. Anwendungsfall monatliche Lohnabrechnung mit SV-Berechnung Beitragsbemessungsgrenzen AG-AN-Aufteilung Sonderfaelle. Methodik Beitragsberechnung mit JAEG BBG Zusatzbeitrag KV. Output Prüfraster SV-Beitraege.

# SV-Beitraege Grundlagen — RV KV PV AV und Umlagen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SV-Beitraege Grundlagen — RV KV PV AV und Umlagen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Sozialversicherung umfasst vier Hauptzweige: Rentenversicherung (RV), Krankenversicherung (KV), Pflegeversicherung (PV), Arbeitslosenversicherung (AV). Hinzu kommen Umlagen U1 (Krankheit), U2 (Mutterschaft), U3 (Insolvenzgeld) und ggf. Berufsgenossenschaft. Die Beitragsberechnung erfolgt prozentual vom Bruttolohn bis zur Beitragsbemessungsgrenze (BBG); ueber BBG beitragsfrei.

## Kaltstart-Rueckfragen

1. SV-Status des AN — versicherungspflichtig, gerinfgfuegig, kurzfristig, Werkstudent, freiwillig versichert?
2. Bruttolohn ueber JAEG (Jahresarbeitsentgeltgrenze) KV — Wechsel in PKV moeglich?
3. Bruttolohn ueber BBG — Beitragsfrei oberhalb?
4. PV: Kind oder kinderlos (Kinderlosenzuschlag)?
5. KV: Wahl Krankenkasse, Zusatzbeitragssatz individuell?
6. Bundesland: Beitragssatz PV unterschiedlich (Saarland anders)?
7. Sondersituation: Mehrfachbeschaeftigung, Bezug Arbeitslosengeld, Saison-AN?
8. Berufsgenossenschaft: Gefahrtarif, Beitragsklasse?

## Rechtlicher Rahmen

### Primaernormen

**SGB IV §§ 14, 17, 18** — Arbeitsentgelt, Pauschalierungen, BBG.

**SGB V** — Krankenversicherung.

**SGB VI** — Rentenversicherung.

**SGB XI** — Pflegeversicherung.

**SGB III** — Arbeitsfoerderung (AV).

**§ 7 SGB IV** — Beschaeftigung.

**§ 8 SGB IV** — geringfuegige Beschaeftigung.

**§ 28d SGB IV** — Gesamt-SV-Beitrag.

**§ 28e SGB IV** — Beitragspflicht AG.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Sachbezugswerte-Verordnung (jaehrliche Anpassung).
- BMF/BMAS Rundschreiben.

## Workflow

### Phase 1 — BBG und Beitragssaetze (Stand 2025)

| Zweig | West/Ost | BBG monatlich (Stand 2025) | Beitragssatz (Stand 2025) |
|---|---|---|---|
| RV | Bundeseinheitlich ab 01.01.2025 (Angleichung Ost an West, Rentenueberleitungs-Abschlussgesetz abgeschlossen) | 8.050 EUR/Monat (96.600 EUR/Jahr) | 18,6 Prozent (paritaetisch je 9,3 Prozent) |
| AV | wie RV | 8.050 EUR/Monat (wie RV) | 2,6 Prozent (paritaetisch je 1,3 Prozent) |
| KV | bundeseinheitlich | 5.512,50 EUR/Monat (66.150 EUR/Jahr) | 14,6 Prozent allgemein + KK-Zusatzbeitrag (durchschnittlich 2,5 Prozent Stand 2025) |
| PV | bundeseinheitlich, Sonderregelung Sachsen | 5.512,50 EUR/Monat (wie KV) | 3,6 Prozent (paritaetisch); Kinderlosenzuschlag 0,6 Prozent allein AN (§ 55 Abs. 3 SGB XI i.d.F. PflegeunterstuetzungsG seit 01.07.2023) |

(Alle Werte Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel ueber DRV, GKV-Spitzenverband, BMAS pruefen.)

### Phase 2 — Beitragsaufteilung AG/AN

- Grundsatz: halbe-halbe Aufteilung.
- PV-Zuschlag Kinderlose: 0,6 Prozent (Stand 2025, § 55 Abs. 3 SGB XI) zu Lasten AN allein.
- KV-Zusatzbeitrag: in der Regel paritaetisch.
- U1 (Krankheit): nur AG.
- U2 (Mutterschaft): nur AG.
- Insolvenzgeld-Umlage: nur AG.
- Berufsgenossenschaft: nur AG.

### Phase 3 — Sonderfaelle

| Sonderfall | SV-Behandlung |
|---|---|
| Minijob (538 EUR-Grenze, Stand 01.01.2024 — bei MiLo-Anhebung dynamisch) | Pauschal 30 Prozent (15 RV + 13 KV + 2 LSt) |
| Werkstudent | Nur RV-Pflicht, keine KV/AV (sofern Werkstudent-Status) |
| Aushilfskraft kurzfristig (max. 3 Monate / 70 Tage) | SV-frei (nur KSt-Pauschal) |
| Gesellschafter-GF GmbH | SV-Pflichtfrage einzelfallabhaengig |
| Pensionaer | Nur KV/PV; RV und AV befreit |
| Mehrfachbeschaeftigung | Beitragspflicht nur ein Mal bis BBG |

### Phase 4 — JAEG und KV-PV-Wahl

- JAEG (Jahresarbeitsentgeltgrenze) ueber 3 Jahre ueberschritten: AN kann in PKV wechseln.
- JAEG 2025: 73.800 EUR/Jahr (monatlich 6.150 EUR; Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).
- Wechsel-Pruefung gemeinsam mit AN, ggf. AG-Zuschuss zur PKV.

### Phase 5 — Berufsgenossenschaft

- Gefahrtarif je nach Branche.
- Beitragssatz Promille der Lohnsumme.
- Jaehrlicher Lohnnachweis im Februar des Folgejahres.
- BG-Mitglied im StB-Stammblatt erfassen.

### Phase 6 — Buchung und Abrechnung

- SV-AG-Anteil als Lohnnebenkosten (Konto 6110 SKR04 / 4130 SKR03 "Gesetzliche soziale Aufwendungen") an Verbindlichkeit Sozialversicherung (3760 SKR04 / 1741 SKR03).
- SV-AN-Anteil als Abzug vom Brutto-Loehne-Konto: Loehne und Gehaelter (6020 SKR04 / 4120 SKR03) gegen Verbindlichkeit SV (3760 SKR04 / 1741 SKR03).
- Gesamtsumme an Krankenkasse einheitlich (Gesamt-SV-Beitrag).
- Faelligkeit: drittletzter Bankarbeitstag des laufenden Monats fuer die voraussichtliche Beitragsschuld (§ 23 Abs. 1 SGB IV); spaetestens Korrektur mit Beitragsnachweis bis 15. des Folgemonats.

## Output

- SV-Berechnung im DATEV LODAS / Lohn und Gehalt.
- AG-AN-Aufteilung pruefen.
- Pauschalbetraege Minijob separat.
- Buchung im Hauptbuch.

## Strategie und Praxis-Tipps

- SV-Faelligkeit drittletzter Bankarbeitstag — bei Verspaetung Saeumniszuschlag, ab 1 Jahr § 266a StGB-Risiko (Vorenthalten SV-Beitraege).
- BBG und Beitragssaetze jaehrlich pruefen — DATEV-Updates zum 1. Januar Pflicht.
- Bei Werkstudent: Status pruefen (20-Stunden-Regel; in der vorlesungsfreien Zeit ggf. mehr).
- Bei Mehrfachbeschaeftigung: AG-Pflicht zur Pruefung der BBG-Ueberschreitung.
- StBVV: SV-Berechnung in Lohnpauschale; komplexe Sonderfaelle (Werkstudent-Pruefung) Zeithonorar.
- DATEV-Tipp: DATEV LODAS mit automatischen Beitragssatz-Updates; Plausibilitaets-Pruefung Beitragssumme.

## Querverweise

- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-arbeitgeber-arbeitnehmer-anteile` — AG-AN-Anteile.
- `stb-lohn-umlage-u1-u2-insogeld-umlage` — Umlagen.
- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-werkstudent-pauschalen` — Werkstudent.
- `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` — BG.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 7, 8, 14, 17, 18, 23, 28d, 28e.
- SGB V, VI, XI, III.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
- StGB § 266a.
- BBG 2025: RV/AV 8.050 EUR/Monat, KV/PV 5.512,50 EUR/Monat; Beitragssaetze: RV 18,6%, AV 2,6%, KV 14,6%+Zusatz, PV 3,6%+Kinderlos 0,6%.
- PV-Kinderlosenzuschlag 2025: 0,6 Prozent (§ 55 Abs. 3 SGB XI, PflegeunterstuetzungsG seit 01.07.2023).
- Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 10 Marker aufgeloest: 8 bestaetigt (BBG/Beitragssaetze 2025 eingesetzt), 2 ersetzt (Pruefhinweise ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-lohn-sv-meldungen-dakota-svnet`

**Fokus:** SV-Meldungen über sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Übermittlung Prüfung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen.

# SV-Meldungen ueber sv.net oder DAKOTA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SV-Meldungen ueber sv.net oder DAKOTA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

SV-Beitragsnachweise und DEUEV-Meldungen werden elektronisch an die Krankenkassen uebermittelt. Zwei Hauptverfahren: sv.net (kostenfrei, ueber GKV-Spitzenverband) oder DATEV-DAKOTA (kostenpflichtig, mit DATEV-Integration). Der Steuerberater waehlt das passende System, konfiguriert Zugaenge und versendet die Meldungen.

## Kaltstart-Rueckfragen

1. Welches System ist aktuell in Verwendung — sv.net, DAKOTA, anderes?
2. Welche Mandantenzahl rechtfertigt welches System?
3. Welche Krankenkassen sind vertreten?
4. Sind alle ITSG-Zertifikate gueltig?
5. Welche Meldearten sind regelmaessig (Standard, Sondermeldungen)?
6. Welche Sonderaufnahme (Sofortmeldung)?
7. Liegen Erstattungsantraege (U1/U2) vor?
8. Welche Ueberwachung der Quittungen?

## Rechtlicher Rahmen

### Primaernormen

**§ 28a SGB IV** — Meldepflichten elektronisch.

**§ 28b SGB IV** — Form der Meldungen.

**§ 95 SGB IV** — Datenuebermittlungs-Verordnung.

**DEUEV** — Datenerfassungs- und -uebermittlungsverordnung.

### Verwaltungsanweisungen

- ITSG-Spezifikation.
- GKV-Spitzenverband Rundschreiben.

## Workflow

### Phase 1 — System-Wahl

| System | Vorteile | Nachteile |
|---|---|---|
| sv.net (ITSG) | Kostenfrei; Standard GKV-Spitzenverband; sv.net classic wurde 2024 abgeloest durch sv.net online (Browser) und sv.net comfort (Lokalinstallation); aktuelle Verfuegbarkeit ueber ITSG.de pruefen | Beschraenkter Funktionsumfang; nicht mandantenoptimal bei vielen AN |
| DATEV DAKOTA | Integriert in DATEV LODAS / Lohn und Gehalt; mandantenoptimiert; jaehrliches Zertifikat ueber DATEV-eService | Kostenpflichtig |
| ITSG-Software anderer Anbieter (z.B. Lexware, Addison) | Mandanten-spezifisch | Pruefung Kosten/Nutzen |

### Phase 2 — Zugang und Zertifikate

- ITSG-Zertifikat pro Mandant erforderlich.
- Erneuerung jaehrlich (oder 3-Jahres-Zertifikat).
- Sicherheitspasswort.

### Phase 3 — Meldungs-Typen

| Meldungsart | Inhalt | Zeitpunkt |
|---|---|---|
| Beitragsnachweis | Voraus-Beitrag laufender Monat | Bis drittletzter Bankarbeitstag |
| Korrigierter Beitragsnachweis | Ist-Beitrag nach Abrechnung | Bis 15. Folgemonat |
| DEUEV-Anmeldung | Beschaeftigungsbeginn AN | Mit naechster Lohnabrechnung |
| DEUEV-Abmeldung | Beschaeftigungsende | Mit naechster Abrechnung |
| Unterbrechungsmeldung | Krankheit > 6 Wochen | Bei Beginn Krankengeld |
| Jahresmeldung | Jahreslohnsumme je AN | Bis 15. Februar Folgejahr |
| Sofortmeldung | Beschaeftigungsbeginn in § 28a Abs 4-Branche | Vor Aufnahme |
| U1/U2-Erstattungsantrag | Krankheits-/Mutterschaftserstattung | Spaetestens 3 Monate nach Ereignis |

### Phase 4 — Sendung

- sv.net oder DAKOTA Sendung.
- Empfangsquittung.
- Bei Fehler: Korrektur und erneute Sendung.

### Phase 5 — Pruefung Quittungen

- Eingehende Quittung vom Server.
- Bei Fehler: Pruefung Stammdaten.
- Bestaetigungsmeldung von der Krankenkasse.

### Phase 6 — Archivierung

- Quittungen 10 Jahre aufbewahren (§ 28f SGB IV).
- Elektronisch in DATEV LODAS oder Mandantenakte.

## Output

- Versendete Meldungen.
- Empfangsquittungen.
- Beleg in Mandantenakte.

## Strategie und Praxis-Tipps

- Bei vielen Mandanten DATEV DAKOTA wirtschaftlich; bei wenigen sv.net ausreichend.
- ITSG-Zertifikate rechtzeitig erneuern — bei Ablauf keine Uebermittlung mehr moeglich.
- Bei Sofortmeldungspflicht-Branchen sofort am Tag der Beschaeftigungsaufnahme.
- Wiederholte Fehlermeldungen (z.B. SV-Nummer nicht erkannt) deuten auf Stammdaten-Fehler hin.
- StBVV: Standardmeldungen in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS automatische ITSG-Zertifikats-Erinnerung.

## Querverweise

- `stb-lohn-meldungen-sv-elstam-zugang` — ELStAM/SV-Meldungen.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-jahresmeldungen-ahn-asn-besondere` — Jahresmeldungen.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28b, 28f, 95.
- DEUEV.
- ITSG-Spezifikation.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (sv.net-Verfuegbarkeit Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-lohn-ueberstunden-abbau-arbeitszeitkonto`

**Fokus:** Überstunden Arbeitszeitkonto Stundenkonto Auszahlung. Anwendungsfall AN haeuft Überstunden an Bilanzierung im Arbeitszeitkonto Abbau in Freizeit oder Auszahlung lohn- und sv-rechtliche Behandlung. Methodik Aufzeichnung MiLoG Bewertung Stand. Output Arbeitszeitkonto-Abrechnung.

# Ueberstunden und Arbeitszeitkonto

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ueberstunden und Arbeitszeitkonto` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Ueberstunden koennen im Arbeitszeitkonto angesammelt und durch Freizeit oder Auszahlung abgebaut werden. Bei Auszahlung sind sie regulaerer Arbeitslohn (LSt-pflichtig, SV-pflichtig). Bei Auflosung (z.B. Beschaeftigungsende) erfolgt Abrechnung der noch offenen Stunden. Das Arbeitszeitkonto bedarf einer schriftlichen Vereinbarung (Arbeitsvertrag, Tarifvertrag, Betriebsvereinbarung) und sollte begrenzt sein (z.B. max. 120 Stunden Plus).

## Kaltstart-Rueckfragen

1. Liegt schriftliche Arbeitszeitkonto-Vereinbarung vor?
2. Welche Obergrenze und Untergrenze (Stunden)?
3. Welcher Stundenlohn ist als Basis vereinbart?
4. Werden Zuschlaege (Sonn-/Feiertag-/Nachtarbeit) im Konto separat ausgewiesen?
5. Ist Wertguthaben-Vereinbarung (langfristig) oder nur Kurzzeit-Konto vorhanden?
6. Welche Auszahlungs-Termine vereinbart (jaehrlich, bei Beendigung)?
7. Liegt MiLoG-Aufzeichnung der taeglichen Arbeitszeit vor?
8. Welche Auszahlung im aktuellen Monat geplant?

## Rechtlicher Rahmen

### Primaernormen

**§ 17 MiLoG** — Aufzeichnungspflicht.

**ArbZG** — Arbeitszeitgesetz.

**§ 7c SGB IV** — Wertguthabenvereinbarungen.

**§ 19 EStG** — Arbeitslohn.

**§ 14 SGB IV** — Arbeitsentgelt.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- BMF zu Wertguthaben.

## Workflow

### Phase 1 — Vertragspruefung

- Schriftliche Arbeitszeitkonto-Vereinbarung mit:
 - Obergrenze (z.B. +120 Stunden) und Untergrenze (z.B. -40 Stunden).
 - Ausgleichszeitraum (z.B. 12 Monate).
 - Modalitaeten Freizeit-Ausgleich.
 - Modalitaeten Auszahlung.
- Falls keine Vereinbarung: Ueberstunden in der Regel als Mehrarbeit zu verguteten.

### Phase 2 — Stunden-Konto fuehren

- Tagliche Arbeitszeit erfassen (MiLoG § 17).
- Saldo monatlich aktualisieren.
- Aufzeichnung 2 Jahre aufbewahren.

### Phase 3 — Bewertung

- Stundenwert: Brutto-Stundenlohn.
- Mehrarbeit/Ueberstunden: Grundstundenlohn x (1 + Zuschlagssatz).
- Sonn-/Feiertag-/Nacht: § 3b EStG-Saetze (separat ausweisen, steuerfrei in Grenzen).

### Phase 4 — Freizeit-Ausgleich

- AN baut Ueberstunden durch Freizeit ab.
- Keine LSt-/SV-Auswirkung.
- Stunden-Konto wird reduziert.

### Phase 5 — Auszahlung Ueberstunden

- Ausgleich in Lohnform: regulaere LSt und SV.
- Bei Aufloesung Konto (Beschaeftigungsende): einmalige Auszahlung als sonstiger Bezug; LSt nach § 39b Abs. 3 EStG.
- Fuenftel-Regelung § 34 EStG fuer reine Ueberstundenauszahlung in der Regel NICHT anwendbar — beschraenkt auf Entschaedigungen (§ 24 Nr. 1 EStG) und Verguetungen fuer mehrjaehrige Taetigkeiten. Bei Ueberstundenauszahlung ueber mehrere Jahre kann § 34 Abs. 2 Nr. 4 EStG ausnahmsweise greifen — Einzelfallpruefung.

### Phase 6 — Wertguthaben-Vereinbarung (§ 7c SGB IV)

- Langfristige Vereinbarung zur SV-rechtlich begleiteten Ansparung (z.B. fuer Sabbatical, Vorruhestand).
- Insolvenzsicherung Pflicht.
- Bei Storno: SV-rechtliche Rueckabwicklung.

## Output

- Arbeitszeitkonto-Bewegungsblatt.
- Lohn-Abrechnung mit Auszahlung Ueberstunden.
- MiLoG-Aufzeichnung im Lohnordner.

## Strategie und Praxis-Tipps

- Schriftliche Vereinbarung Arbeitszeitkonto ist Standard — sonst Konflikt bei Beendigung.
- Bei Auflosung Konto bei Beschaeftigungsende: Auszahlung im gleichen Monat als regulaerer Lohn (keine Fuenftel-Regelung, da nicht Entschaedigung).
- Bei langer Krankheit waehrend Konto-Stand: AG-Anspruch auf Verrechnung mit Krankheits-Entgeltfortzahlung in der Regel nicht moeglich.
- MiLoG-Aufzeichnung 2 Jahre Pflicht.
- StBVV: Konto-Fuehrung in Lohnpauschale; bei komplexen Auszahlungen Zeithonorar.
- DATEV-Tipp: DATEV LODAS Arbeitszeitkonto-Modul mit Soll-/Ist-Vergleich.

## Querverweise

- `stb-lohn-mehrarbeit-zuschlaege-39b-estg` — Zuschlaege.
- `stb-lohn-aufzeichnungspflichten-milog` — MiLoG.
- `stb-lohn-ausgleichszahlungen-altersteilzeit` — Altersteilzeit.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- MiLoG § 17.
- ArbZG.
- SGB IV § 7c.
- EStG §§ 19, 34.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-lohn-umlage-u1-u2-insogeld-umlage`

**Fokus:** Umlagen U1 U2 Insolvenzgeld-Umlage. Anwendungsfall AG-Umlagen monatlich Erstattung Krankheit Mutterschaft Insolvenz Berechnung Saetze Variabilitaet KK. Methodik Prüfung Pflicht Kleinunternehmer 30 AN. Output Umlage-Berechnung.

# Umlagen U1, U2, Insolvenzgeld

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Umlagen U1, U2, Insolvenzgeld` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Drei Umlagen lasten ausschliesslich auf dem AG (AN-Anteil null):
- **U1** (Aufwendungsausgleich Krankheit): Erstattung Entgeltfortzahlung im Krankheitsfall; Pflicht fuer Kleinunternehmer bis 30 AN; Erstattung 80 Prozent.
- **U2** (Aufwendungsausgleich Mutterschaft): Erstattung Mutterschutzlohn und AG-Zuschuss Mutterschaftsgeld; Pflicht aller AG; Erstattung 100 Prozent.
- **Insolvenzgeld-Umlage**: Beitrag zur Finanzierung des Insolvenzgeldes; Pflicht aller AG (Ausnahme Privathaushalte).

## Kaltstart-Rueckfragen

1. Mitarbeiterzahl im Mandantenbetrieb (U1-Pflicht-Pruefung)?
2. Welche Krankenkassen vertreten (Beitragssatz U1 KK-individuell)?
3. Welche AN sind in Erstattungsbasis einbezogen (Vollzeit, Teilzeit, Minijob)?
4. Wann letzte Erstattungs-Antraege gestellt?
5. Bei drohendem AG-Wechsel: Datenuebernahme Umlage-Beitraege?
6. BG-Beitrag Insolvenzgeld-Umlage aktualisiert?
7. Welche jaehrliche Anpassung?
8. Welche Privathaushalts-Konstellation (Minijob-Sonderfall)?

## Rechtlicher Rahmen

### Primaernormen

**AAG (Aufwendungsausgleichsgesetz)** — U1/U2.

**§ 1 AAG** — Geltungsbereich U1.

**§ 7 AAG** — Berechnung Umlage.

**§ 358 SGB III** — Insolvenzgeld-Umlage.

**§ 165 SGB III** — Insolvenzgeld.

### Verwaltungsanweisungen

- KK-individuelle Satzungen.
- BMAS Rundschreiben.

## Workflow

### Phase 1 — U1-Pflicht-Pruefung

- AG mit max. 30 AN ist U1-pflichtig.
- Pruefung jaehrlich zum 1. Januar (Berechnung Durchschnitt Vorjahr).
- Minijobs werden mit Faktor 0,75 angerechnet.
- Pflicht-Wechsel mit naechstem Kalenderjahr.

### Phase 2 — Berechnungs-Basis

- Umlagebeitrag = Bemessungsgrundlage x Umlagesatz.
- Bemessungsgrundlage U1/U2: rentenversicherungspflichtiges Brutto bis zur BBG der RV (§ 7 AAG).
- U1 Satz: KK-individuell (variiert nach KK-Satzung); typisch 1,0-3,0 Prozent.
- U2 Satz: KK-individuell; typisch 0,2-0,5 Prozent.
- Insolvenzgeld-Umlage: bundeseinheitlich, festgesetzt durch Insolvenzgeldumlageverordnung; 2024: 0,06 Prozent; 2025: 0,06 Prozent (unveraendert; Insolvenzgeldumlageverordnung 2026 zum Jahreswechsel pruefen).

### Phase 3 — Erstattungsantraege

- U1 bei Krankheit: AG zahlt Entgeltfortzahlung weiter; beantragt Erstattung 80 Prozent bei KK.
- U2 bei Mutterschaft: AG zahlt Zuschuss zum Mutterschaftsgeld; beantragt Erstattung 100 Prozent bei KK.
- Antrag: ueber sv.net oder DAKOTA.
- Frist: 3 Monate nach Beendigung des Ereignisses (KK-Satzung).

### Phase 4 — Insolvenzgeld-Umlage

- Bundeseinheitlich; 2025: 0,06 Prozent (Insolvenzgeldumlageverordnung; Satz 2026 zum Jahreswechsel pruefen).
- Faellig zusammen mit SV-Beitragsnachweis.
- Wird ueber die Krankenkassen eingezogen.

### Phase 5 — Buchung im Hauptbuch

- Lohnnebenkosten Umlagen (Konto 4140 oder 6140 SKR 03).
- AG-Aufwand.
- Bei Erstattung: Gegenbuchung (Konto 4141 oder Verbuchung zu Lohnnebenkosten).

### Phase 6 — Dokumentation

- Erstattungsantraege archivieren.
- KK-Bescheide ueber Erstattung.
- Beleg im Lohnordner.

## Output

- Korrekt berechnete Umlagen.
- Erstattungsantraege bei Krankheit/Mutterschaft.
- Buchung im Hauptbuch.

## Strategie und Praxis-Tipps

- U1-Pflicht-Pruefung jaehrlich zum 1. Januar — nicht vergessen.
- U2 ist UNABHAENGIG von Betriebsgroesse Pflicht.
- Insolvenzgeld-Umlage entfaellt fuer Privathaushalte (Privathaushalts-Minijob).
- Erstattungsantraege rechtzeitig stellen — Frist max. 4 Jahre.
- Bei wechselnder Mitarbeiterzahl ueber 30: U1-Wechsel zum Jahreswechsel.
- StBVV: in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS Umlage-Konfiguration mit jaehrlicher Pflicht-Aktualisierung.

## Querverweise

- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-krankheit-entgeltfortzahlung-efzg` — Krankheit.
- `stb-lohn-elternzeit-mutterschutz` — Mutterschaft.
- `stb-lohn-arbeitgeber-arbeitnehmer-anteile` — AG-/AN-Anteile.

## Quellen und Updates

Stand: 05/2026.

- AAG §§ 1, 7.
- SGB III §§ 165, 358.
- KK-Satzungen.
- BMAS Rundschreiben.
- Insolvenzgeld-Umlage 2025: 0,06 Prozent; Insolvenzgeldumlageverordnung 2026 pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 2 bestaetigt (Insolvenzgeld-Umlage 2025 0,06% eingesetzt), 1 ersetzt (Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-lohn-vermoegenswirksame-leistungen`

**Fokus:** Vermögenswirksame Leistungen VL AG-Anteil AN-Sparzulage. Anwendungsfall AG-Zuschuss bis 480 EUR jaehrlich AN-Sparzulage einkommensabhaengig Bausparen Aktien-Fonds. Methodik Prüfung Antrag AN-Sparzulage Beratung. Output VL-Konfiguration.

# Vermoegenswirksame Leistungen (VL) und AN-Sparzulage

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vermoegenswirksame Leistungen (VL) und AN-Sparzulage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Vermoegenswirksame Leistungen (VL) sind Sparleistungen, die der AG fuer den AN auf ein VL-faehiges Sparkonto einzahlt. Hoehe und Vertragsgestaltung sind tariflich oder einzelvertraglich vereinbart. Bei Einkommens-Schwellenwerten kommt die AN-Sparzulage als staatliche Foerderung hinzu (5. VermBG). Die VL sind lohnsteuerpflichtig und SV-pflichtig — keine steuerliche Foerderung der AG-Leistung selbst.

## Kaltstart-Rueckfragen

1. Liegt VL-Vereinbarung im Arbeitsvertrag oder Tarifvertrag vor?
2. Welche Hoehe — AG-Zuschuss pro Monat (typisch 6,65 oder 40 EUR)?
3. Welche VL-Sparform — Bausparen, Aktien-Fonds, Banksparen?
4. Welches Einkommen hat der AN (Sparzulage-Grenze)?
5. Hat der AN bereits VL-Antrag bei Anlage-Institut gestellt?
6. Bei verheirateten AN: Familienverhaeltnisse fuer Sparzulage-Grenze?
7. Anzahl VL-Vertraege (max. 1 fuer Sparzulage)?
8. Welche Dauer (Sperrfrist 7 Jahre Standard)?

## Rechtlicher Rahmen

### Primaernormen

**5. VermBG** — 5. Vermoegensbildungsgesetz.

**§ 13 5. VermBG** — AN-Sparzulage (Anspruchsgrundlage; Saetze und Einkommensgrenzen in §§ 13, 14 5. VermBG; bei Gesetzesaenderung Norm-Bestand pruefen).

**§ 19 EStG** — VL als Arbeitslohn (AG-Zuschuss ist steuerpflichtig; Foerderung ausschliesslich AN-seitig ueber Sparzulage).

### Verwaltungsanweisungen

- BMF zur Sparzulage.
- BZSt-Vordrucke.

## Workflow

### Phase 1 — VL-Hoehe und Vertragsform

- Tariflich: oft 6,65 oder 26,59 oder 40 EUR/Monat AG-Zuschuss.
- Einzelvertraglich: vereinbart.
- VL bis 480 EUR jaehrlich (40 EUR/Monat) staatlich foerderungsfaehig.

### Phase 2 — AN-Sparzulage Voraussetzungen

| Sparform | Sparzulage | Einkommensgrenze (zu versteuerndes Einkommen, Stand 2025) |
|---|---|---|
| Bausparen / wohnungswirtschaftliche Verwendung | 9 Prozent (max. 43 EUR/Jahr) | 17.900 EUR ledig / 35.800 verheiratet |
| Aktien-Fonds / Beteiligung am AG-Unternehmen | 20 Prozent (max. 80 EUR/Jahr) | 20.000 EUR ledig / 40.000 verheiratet |

(Werte Stand 2025, 5. VermBG; bei Gesetzesaenderung ueber BZSt pruefen.)

### Phase 3 — Lohnabrechnung

- AG-Zuschuss in DATEV LODAS als Lohnzuschlag eingeben.
- LSt-pflichtig: AN versteuert den Zuschuss.
- SV-pflichtig.
- AN-Sparbeitrag aus Netto (Eigenanteil moeglich, aber nicht gefoerdert).

### Phase 4 — Sparzulage-Antrag

- AN beantragt jaehrlich beim FA ueber Anlage VL der Steuererklaerung.
- Sparzulage wird mit Einkommensteuer-Erstattung ausgezahlt.
- Auszahlung erst nach Ablauf der Sperrfrist (7 Jahre).

### Phase 5 — Sperrfrist

- 7 Jahre ab Vertragsabschluss.
- Bei Aufloesung vor Ablauf: Sparzulage zurueckzuzahlen.
- Ausnahmen: Tod, dauernde Erwerbsunfaehigkeit, Arbeitslosigkeit ueber 1 Jahr.

### Phase 6 — VL-Bescheinigung

- Anlageinstitut erstellt jaehrliche Bescheinigung.
- AG benoetigt die Bescheinigung als Beleg.
- Im Lohnordner archivieren.

## Output

- VL in Lohnabrechnung konfiguriert.
- Sparzulage-Berechnung fuer Steuererklaerung.
- VL-Bescheinigung im Lohnordner.

## Strategie und Praxis-Tipps

- VL ist KEINE steuerliche Sonderfoerderung des AG-Zuschusses — Zuschuss ist normaler Lohn.
- Die staatliche Foerderung kommt ueber AN-Sparzulage (Einkommensabhaengig).
- Bei Bauspar-VL und Aktien-VL beide Hoechstgrenzen separat (Doppelfoerderung max. 123 EUR/Jahr).
- AN mit Einkommen ueber Grenzen: VL wirtschaftlich nur als zusaetzliches Sparen ohne staatliche Zulage.
- StBVV: in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS VL-Konfiguration mit Anlageinstitut-Schnittstelle.

## Querverweise

- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- 5. VermBG.
- EStG § 19.
- BMF zur Sparzulage.
- Sparzulage-Saetze 2025: Bausparen 9% (max. 43 EUR/Jahr, Grenze 17.900 EUR ledig), Aktien-Fonds 20% (max. 80 EUR/Jahr, Grenze 20.000 EUR ledig); 5. VermBG; BZSt pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 2 bestaetigt (VermBG-Saetze 2025 eingesetzt), 1 ersetzt (Normbestand Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-lohn-werkstudent-pauschalen`

**Fokus:** Werkstudent SV-Status 20-Stunden-Grenze pauschale Beitraege. Anwendungsfall Beschaeftigung Student Werkstudentenprivileg KV-Befreiung RV-Pflicht JAEG nicht relevant Klassifizierung. Methodik Prüfung 20-Stunden-Woche vorlesungsfreie Zeit Antrag KV-Befreiung. Output Werkstudenten-Abrechnung.

# Werkstudent — SV-Status und Pauschalen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Werkstudent — SV-Status und Pauschalen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Werkstudenten sind ordentlich immatrikulierte Studierende, die im Nebenerwerb arbeiten. Sie sind in der KV/PV/AV beitragsfrei (Werkstudentenprivileg), aber RV-pflichtig. Voraussetzung: max. 20 Wochenstunden waehrend der Vorlesungszeit; in der vorlesungsfreien Zeit auch mehr. Pruefung sorgfaeltig — bei Verlust des Werkstudent-Status nachtraegliche SV-Beitragspflicht.

## Kaltstart-Rueckfragen

1. Ist der AN ordentlicher Studierender (Immatrikulationsbescheinigung)?
2. Wie viele Wochenstunden arbeitet der AN?
3. Liegt Vorlesungs- oder vorlesungsfreie Zeit vor?
4. Hat der AN Promotion erreicht oder Master beendet? (Status ggf. weg.)
5. Studium Vollzeit oder Teilzeit (Teilzeitstudent: Status zweifelhaft)?
6. Welcher Bruttolohn?
7. KV-Versicherung: Familienversicherung (Eltern), studentische KV, oder PKV?
8. Bezug Ausbildungsfoerderung (BAfoeG)?

## Rechtlicher Rahmen

### Primaernormen

**§ 6 Abs. 1 Nr. 3 SGB V** — KV-Befreiung ordentlicher Studierender.

**§ 27 Abs. 4 SGB III** — AV-Befreiung Studierender.

**§ 16 BAfoeG** — Werkstudent-Definition.

**§ 5 Abs. 1 Nr. 9 SGB V** — studentische KV.

**§ 14 SGB IV** — Arbeitsentgelt.

**SGB VI** — RV-Pflicht.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK zum Werkstudentenprivileg.
- Hochschulgesetz der Laender.

## Workflow

### Phase 1 — Werkstudent-Status pruefen

| Kriterium | Erfuellt? |
|---|---|
| Ordentliche Immatrikulation an Hochschule | Ja / Nein |
| Master noch nicht abgeschlossen | Ja / Nein |
| Studienschwerpunkt erkennbar (kein Schein-Studium) | Ja / Nein |
| Max 20 Wochenstunden in Vorlesungszeit | Ja / Nein |
| Bezug zu Studium (entbehrlich, aber hilfreich) | Ja / Nein |

### Phase 2 — Arbeitszeitpruefung

- Vorlesungszeit: max. 20 Wochenstunden.
- Vorlesungsfreie Zeit (Semesterferien): mehr als 20 Stunden moeglich.
- Mehrfach-Werkstudent: Summe der Stunden ueber alle AG ist massgeblich.
- 26-Wochen-Regel: Eine Ueberschreitung der 20-Wochen-Stunden-Grenze bleibt unschaedlich, wenn sie ueberwiegend in vorlesungsfreien Zeitraeumen liegt und im 52-Wochen-Zeitraum nicht mehr als 26 Wochen umfasst (st. Spitzenverbands-Rundschreiben; bei Aenderung der DEUEV-Grundsaetze pruefen).
- Bei dauerhafter Ueberschreitung der 20 Wochenstunden in der Vorlesungszeit: Werkstudenten-Status weg, voll SV-pflichtig.

### Phase 3 — SV-Beitraege

| Zweig | Werkstudent |
|---|---|
| KV | Beitragsfrei aus der Beschaeftigung; eigene KV-Pflicht ueber Familienversicherung (bis Vollendung 25. Lj., § 10 SGB V) oder studentische KV (§ 5 Abs. 1 Nr. 9 SGB V) |
| PV | Beitragsfrei |
| AV | Beitragsfrei |
| RV | Pflicht (voller Beitrag; im Uebergangsbereich nach § 20 Abs. 2 SGB IV gemindert, sofern Brutto in den Midi-Job-Bereich faellt) |

**Zahlenbeispiel:** Werkstudent mit Brutto 900 EUR/Monat (im Uebergangsbereich). RV-AG 9,3 Prozent von 900 EUR = 83,70 EUR; AN-Anteil im Uebergangsbereich gemindert (Faktor F — vgl. `stb-lohn-midi-job-uebergangsbereich-2000-euro`). KV/PV/AV null. LSt nach Steuerklasse (typisch StKl 1, im Regelfall keine LSt unterhalb Grundfreibetrag).

### Phase 4 — Anmeldung und Pruefung

- Immatrikulationsbescheinigung jaehrlich aktualisieren (am besten zu Semesterbeginn).
- SV-Anmeldung mit Personengruppen-Schluessel 106 (Werkstudent; DEUEV-Schluesselverzeichnis ITSG Stand 2025, unveraendert; bei DEUEV-Aenderung ITSG-Schluesselverzeichnis pruefen).
- Bei Verlust Werkstudent-Status: Personengruppen-Schluessel auf 101 (regulaer) wechseln; Beitragsgruppen-Schluessel anpassen.

### Phase 5 — Sonderfaelle

- Promovierende: kein Werkstudent (Master abgeschlossen). Ausnahme: vergebene Doktoranden-Stipendien.
- Teilzeitstudenten: Werkstudent-Status zweifelhaft; Einzelfallpruefung.
- Sprach- und Aufbaustudiengaenge: in der Regel Werkstudent.
- Auslandsstudierende: bei deutscher Sozialversicherungspflicht (z.B. EU-Buerger mit deutscher Wohnung) Werkstudent moeglich.

### Phase 6 — Dokumentation

- Immatrikulationsbescheinigung jaehrlich in Mandantenakte.
- Stundenaufzeichnung MiLoG.
- Lohnabrechnung mit Personengruppen 106.

## Output

- Werkstudent-SV-Abrechnung (nur RV).
- Anmeldung mit Personengruppen 106.
- Stundenaufzeichnung MiLoG.

## Strategie und Praxis-Tipps

- 20-Stunden-Regel strikt — bei systematischem Ueberschreiten Status verloren.
- Bei Ueberschreitung waehrend Semesterferien akzeptabel; in Vorlesungszeit kritisch.
- Bei Wechsel Master in Promotion: Status faellt weg, Umstellung Personengruppen-Schluessel.
- Bei Studienabschluss waehrend Beschaeftigung: Status faellt zum Tag des Abschlusses weg.
- StBVV: in Lohnpauschale; Statuspruefung bei Sonderfaellen Zeithonorar.
- DATEV-Tipp: DATEV LODAS Werkstudent-Personengruppe automatisch; Immatrikulations-Wiedervorlage zu Semesterbeginn.

## Querverweise

- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-praktikanten-azubis-loehne` — Praktikant.

## Quellen und Updates

Stand: 05/2026.

- SGB V §§ 5, 6.
- SGB III § 27.
- SGB VI.
- BAfoeG § 16.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (DEUEV-Schluessel 106 unveraendert), 1 ersetzt (26-Wochen-Regel Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-mandantenfragebogen-jahresabschluss`

**Fokus:** Mandantenfragebogen zum Jahresabschluss. Anwendungsfall JA-Vorbereitung systematische Datenerhebung vom Mandanten Bestaende Forderungen Verbindlichkeiten Rückstellungen Sondervorgaenge. Methodik strukturierter Fragebogen Prüfliste. Output ausgefuellter Fragebogen Datenbasis für Jahresabschluss.

# Mandantenfragebogen zum Jahresabschluss

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenfragebogen zum Jahresabschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zum Jahresabschluss muss der Mandant zahlreiche Informationen liefern, die nicht aus der laufenden Buchfuehrung ersichtlich sind: Inventur-Werte, Forderungsrisiken, Sondervorgaenge, Vertragsabschluesse, Investitionsplaene fuer Folgejahr. Der Steuerberater nutzt einen strukturierten Fragebogen, um diese Informationen systematisch abzufragen. Ein gut ausgefuellter Fragebogen reduziert Rueckfragen und beschleunigt den Jahresabschluss.

## Kaltstart-Rueckfragen

1. Wann ist der Bilanzstichtag?
2. Welche Rechtsform und Groessenklasse (Pruefungspflicht)?
3. Welche Sondervorgaenge im Geschaeftsjahr (Anlagenverkauf, Kapitalerhoehung, Wechsel Gesellschafter)?
4. Welche Forderungen sind strittig (Einzelwertberichtigung)?
5. Welche Rueckstellungen (Garantie, Prozesskosten, Tantieme)?
6. Inventur durchgefuehrt? Bestaende dokumentiert?
7. Wesentliche Vertraege seit Stichtag (Werterhellung)?
8. Liquiditaetsplan Folgejahr?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — JA-Aufstellungspflicht.

**§ 240 HGB** — Inventarpflicht.

**§ 252 HGB** — Bewertung.

**§ 253 HGB** — Forderungs- und Rueckstellungsbewertung.

**§ 90 AO** — Mitwirkungspflicht.

**§ 153 AO** — Berichtigungspflicht.

### Standards

- IDW PS 480.
- DStV-Praxisleitfaden Jahresabschluss.

## Workflow

### Phase 1 — Standard-Fragebogen-Struktur

```
MANDANTENFRAGEBOGEN JAHRESABSCHLUSS [Geschaeftsjahr]
Mandant: [Firma]
Bilanzstichtag: [Datum]

A. ALLGEMEINES
1. Rechtsform und Gesellschafter-Struktur unveraendert? [Ja/Nein, falls Nein erlaeutern]
2. Wesentliche Aenderungen im Geschaeftsmodell?

B. ANLAGEVERMOEGEN
3. Anlagen-Zugaenge im Jahr? [Liste]
4. Anlagen-Abgaenge (Verkauf, Verschrottung)? [Liste]
5. Investitionsabzugsbetrag § 7g EStG geplant?
6. Aussergewoehnliche Abschreibungen?

C. UMLAUFVERMOEGEN
7. Warenbestand Inventur durchgefuehrt? [Datum, Wert]
8. Unfertige Erzeugnisse? [Wert]
9. Forderungen strittig oder zweifelhaft? [Liste]
10. Pauschalwertberichtigung Forderungen?

D. EIGENKAPITAL
11. Kapitalerhoehung oder -herabsetzung?
12. Ausschuettung im Geschaeftsjahr?
13. Plant Mandant Verwendung des Jahresgewinns?

E. VERBINDLICHKEITEN
14. Neue Darlehen aufgenommen? [Liste mit Konditionen]
15. Sondertilgungen?
16. Rangruecktrittsvereinbarungen?

F. RUECKSTELLUNGEN
17. Anhaengige Prozesse?
18. Garantieverpflichtungen?
19. Tantieme- und Gratifikations-Verpflichtungen?
20. Steuerliche Risiken (BP, Selbstanzeige)?

G. SONDERVORGAENGE
21. Geschaeftsvorfaelle mit nahestehenden Personen (vGA-Risiko)?
22. Auslandsgeschaefte (innergemeinschaftliche Lieferungen, Drittlandsausfuhr, Reverse-Charge)? Gesamtvolumen und Lieferlaender?
23. Schwebende Geschaefte am Stichtag (drohende Verluste, ausstehende Erfuellung)?

H. WERTERHELLUNG NACH STICHTAG
24. Wesentliche Ereignisse nach Stichtag bis Aufstellung?
25. Insolvenzantraege bei Schuldnern?

I. FOLGEJAHR-AUSBLICK
26. Plan-Umsatz und -Ergebnis Folgejahr?
27. Investitionsplaene?
28. Personalplaene?
29. Liquiditaets-Engpaesse erwartet?

Datum: [Datum]
Unterschrift Mandant: [...]
```

### Phase 2 — Versand

- Fragebogen 4-6 Wochen vor geplantem Jahresabschluss versenden.
- Frist zur Beantwortung: 2-3 Wochen.
- Auf Fristen-Konsistenz mit Jahresabschluss-Termin achten.

### Phase 3 — Ruecklauf-Pruefung

- Vollstaendigkeit pruefen.
- Bei Unklarheiten: Nachfrage telefonisch.
- Bei wesentlichen Sondervorgaengen: persoenliches Gespraech.

### Phase 4 — Konsistenzpruefung

- Antworten Mandant mit laufender Buchfuehrung abgleichen.
- Bei Widersprueche: Klaerung mit Mandant.

### Phase 5 — Massnahmen ableiten

- Aussergewoehnliche Bilanzpositionen vorbereiten.
- Rueckstellungen quantifizieren.
- Werterhellungs-Tatsachen einarbeiten.

### Phase 6 — Dokumentation

- Ausgefuellter Fragebogen in Jahresabschluss-Mappe.
- Unterzeichnete Bestaetigung (Mandantenerklaerung).

## Output

- Ausgefuellter Mandantenfragebogen.
- Datenbasis fuer Jahresabschluss.
- Mandanten-Erklaerung mit Unterschrift.

## Strategie und Praxis-Tipps

- Standardisierter Fragebogen ist Effizienzhebel — gleiche Fragen bei allen Mandanten.
- Frage 24 (Werterhellung) ist haftungs-relevant — wichtige Info nach Stichtag muss in JA.
- Bei wiederkehrenden Mandanten: Fragebogen mit Vorjahres-Daten vorausgefuellt (DATEV).
- Mandanten-Erklaerung am Ende: schuetzt StB bei spaeteren Streits.
- StBVV: Fragebogen ist Teil Jahresabschluss-Auftrag StBVV § 35.
- DATEV-Tipp: DATEV Mandantenfragebogen-Vorlagen anpassen.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandsabstimmung.
- `stb-jahresgespraech-mandant-bwa-basis` — Jahresgespraech.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 242, 252, 253, 264.
- AO §§ 90, 153.
- IDW PS 480.
- DStV-Praxisleitfaden Jahresabschluss.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-online-portal-datev-mandantenshop`

**Fokus:** DATEV Unternehmen Online Mandantenshop. Anwendungsfall Belegtransfer Bank-Abruf Auswertungs-Download Mandantenakte digital für Mandant. Methodik Konfiguration Benutzer Schulung Mandant. Output eingerichtetes Portal.

# DATEV Unternehmen Online — Mandantenshop

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DATEV Unternehmen Online — Mandantenshop` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

DATEV Unternehmen Online (DUO) ist die Standardplattform fuer den digitalen Belegtransfer zwischen Mandant und Steuerberater. Mandant erfasst oder scant Belege ueber das Portal; der Steuerberater greift direkt zu. Auch BWA, SuSa, OPOS-Listen werden ueber DUO geteilt. Konfiguration und Schulung des Mandanten sind Erfolgsfaktoren.

## Kaltstart-Rueckfragen

1. Hat Mandant bereits DUO-Konto?
2. Welche Module sind eingerichtet (Belegtransfer, Banking, Auswertung)?
3. Welche Benutzer und Rollen?
4. Welche Schnittstellen aktiv (Bank, eRechnung, ERP)?
5. Welche Belegart wird elektronisch transferiert?
6. Welche Mandantensystemkenntnis vorhanden?
7. Welche Schulungsbedarf?
8. Welche DSGVO-Konfiguration?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 146 AO** — Zeitgerechtigkeit.

**§ 147 AO** — Aufbewahrung; bei DUO digital.

**DSGVO Art. 28** — AVV (DATEV als Auftragsverarbeiter).

**BMF v. 28.11.2019 zu GoBD** — digitale Buchfuehrung.

## Workflow

### Phase 1 — Einrichtung

- DUO-Konto fuer Mandant beantragen (ueber DATEV).
- AVV mit DATEV pruefen / unterzeichnen.
- Module aktivieren (Belegtransfer, Banking).
- Benutzer und Rollen anlegen.

### Phase 2 — Schnittstellen

- Bank-Anbindung (PSD2 Schnittstelle).
- eRechnungsempfang (Mailpostfach oder Peppol).
- ERP-Anbindung (sofern relevant).
- Mobile App (DATEV Upload Online).

### Phase 3 — Mandantenschulung

- Erstgespraech mit Demo.
- Belegtransfer ueber Smartphone-App.
- Buchungsfreigabe-Workflow.
- Mandantenfreigabe von BWA.

### Phase 4 — Routinebetrieb

- Mandant scannt Belege taeglich oder woechentlich.
- Sachbearbeiter sieht Belege automatisch in DATEV Kanzlei-Rechnungswesen.
- Buchung mit Belegverknuepfung.
- BWA-Versand ueber DUO-Portal.

### Phase 5 — Eskalation und Wartung

- Bei Stoerungen DATEV-Support.
- Quartalsweise Pruefung Belegabgabe-Disziplin.
- Bei Mandant-Nutzungsruckgang: Schulungswiederholung.

### Phase 6 — DSGVO und Sicherheit

- Zwei-Faktor-Authentifizierung empfehlen.
- Bei Mitarbeiterwechsel: Zugang aktualisieren.
- Audit-Logs pruefen.

## Output

- Eingerichtetes DUO-Konto.
- Mandant geschult.
- Belegtransfer im Standardbetrieb.

## Strategie und Praxis-Tipps

- DUO ist Effizienz-Hebel fuer beide Seiten — Belege landen sofort beim StB.
- Mandantenakzeptanz ist Erfolgsfaktor — gute Schulung wichtig.
- Mobile App ist Killer-Feature: Beleg-Scan direkt am Empfangsort.
- Bei groesseren Mandanten: ERP-Anbindung pruefen (verschiedene Schnittstellen).
- StBVV: DUO-Einrichtung als Onboarding-Bestandteil.

## Querverweise

- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-mandanten-onboarding-checkliste-vollservice` — Onboarding.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV-BWA-Modul.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-datentransfer-mandant-cloud-dsgvo` — DSGVO.

## Quellen und Updates

Stand: 05/2026.

- StBerG § 33.
- AO §§ 146, 147.
- DSGVO Art. 28.
- BMF v. 28.11.2019 zu GoBD.
- DATEV-Dokumentation Unternehmen Online (aktuelle Version pruefen).
- Verifikations-Hinweis: konkrete Programmpfade und Modul-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

# Lohnabrechnung und Arbeitgeberpflichten: Mandat und Abrechnung

Diese Datei wird nur geladen, wenn der konkrete Vorgang in diese Fallgruppe fällt.

## Lohn-Mandantenaufnahme — Onboarding

Auswahlsignal: Wenn es um Lohn-Mandantenaufnahme — Onboarding in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### Lohn-Mandantenaufnahme — Onboarding

#### Fachlicher Anker

- **Normen:** § 6a, § 41a EStG, § 28a SGB IV.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die Aufnahme eines neuen Lohn-Mandanten ist organisatorisch anspruchsvoll: Stammdaten zum Arbeitgeber und allen Arbeitnehmern, SV-Nummern, Steuer-IDs, ELStAM-Abruf, Berufsgenossenschaft, ggf. Versorgungswerk. Fehlende oder fehlerhafte Stammdaten fuehren zu später aufwendigen Korrekturen. Der Steuerberater nutzt eine Standard-Checkliste, die in DATEV LODAS, Lohn und Gehalt oder einem äquivalenten Programm zu hinterlegen ist.

#### Kaltstart-Rueckfragen

1. Welche Rechtsform und Branche des Mandanten?
2. Wie viele Arbeitnehmer (Stammbelegschaft, geringfuegig, Werkstudenten)?
3. Welches Vorprogramm bzw. Vorberater (Datenuebernahme möglich)?
4. Welcher Lohnsteuer-Anmelde-Zeitraum (monatlich, vierteljaehrlich, jaehrlich)?
5. Bestehen ueberbetriebliche Tarifvertraege?
6. Gibt es eine Betriebsvereinbarung zu Loehnen, Tantiemen, bAV?
7. Welche Berufsgenossenschaft ist zuständig?
8. Gibt es Sondervergueteungen (Sachbezuege, Dienstwagen, JobRad, bAV)?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 41a EStG** — Anmeldung und Abfuehrung Lohnsteuer.

**§ 28a SGB IV** — SV-Meldungen Arbeitgeber.

**§ 14 SGB IV** — Arbeitsentgelt-Definition.

**§ 8 SGB IV** — geringfuegige Beschäftigung.

**§ 1 LStDV** — Anwendungsbereich.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**§ 33 StBerG** — StB-Aufgabenkreis (Lohnsteuer-Hilfeleistung).

**§ 35 StBVV** — Honorar Lohnbuchfuehrung.

##### Standards

- DATEV-Stammdaten-Prüfliste.
- DEUEV (Datenerfassungs- und -uebermittlungsverordnung).
- Gemeinsame Rundschreiben Spitzenverbaende Krankenkassen.

#### Workflow

##### Phase 1 — Arbeitgeber-Stammdaten

| Stammdaten-Feld | Quelle / Prüfung |
|---|---|
| Firma, Rechtsform, Sitz | Handelsregister-Auszug |
| Steuer-Nr und Steuer-Id | Finanzamtsbescheid |
| Betriebsstaetten-Nummer (BSN) | Bundesagentur für Arbeit |
| Berufsgenossenschaft + Mitgliedsnummer | BG-Bescheid |
| Krankenkassen-Schlüssel | Krankenkasse |
| Versorgungswerk (falls einschlaegig) | Berufsverband |
| Tarifvertrag | DGB / Verband |
| Lohnsteuer-Anmeldungs-Zeitraum | FA-Festlegung |

##### Phase 2 — Arbeitnehmer-Stammdaten

| Stammdaten je AN | Quelle |
|---|---|
| Vorname, Nachname, Geburtsdatum | Personalausweis-Kopie |
| Steuer-Id (11-stellig) | Mitteilung Bundeszentralamt |
| Sozialversicherungs-Nr | SV-Ausweis |
| Krankenkasse | KK-Wahl-Bescheid |
| Steuerklasse, Kinderfreibetrag | ELStAM-Abruf |
| Konfession (KiSt-Pflicht) | ELStAM |
| Adresse | Anmeldebescheinigung |
| Beschäftigungsbeginn / Eintrittsdatum | Arbeitsvertrag |
| Vereinbarte Arbeitszeit | Arbeitsvertrag |
| Brutto-Gehalt | Arbeitsvertrag |
| Sonderleistungen | Arbeitsvertrag, BV |

##### Phase 3 — ELStAM-Abruf

- ELStAM-Verfahren (Elektronische LohnSteuerAbzugsMerkmale): zentraler Abruf der LSt-Merkmale beim BZSt (§ 39e EStG).
- Voraussetzung: Steuer-Id (11-stellig) des AN.
- Abrufschluessel: AG-Steuer-Nr (FA-Schlüssel + AG-Nr) und Geburtsdatum des AN.
- Abruf-Zeitpunkt: vor der ersten Lohnabrechnung, in DATEV LODAS unter Mandant → Mitarbeiterverwaltung → ELStAM-Anmeldung; bei DATEV Lohn und Gehalt unter Stamm → ELStAM-Verfahren. Ruecklauf in der Regel binnen Sekunden.
- Erst-Anmeldung mit Anlassgrund "Beginn der Beschäftigung"; Folgemonatlich automatische Aktualisierung bei Änderungen (Steuerklasse, KiFB, KKB).

##### Phase 4 — SV-Anmeldung

- Anmeldung des Arbeitnehmers bei der Krankenkasse (zugleich für RV und PV).
- Meldung Beschäftigungsbeginn binnen 6 Wochen (§ 28a SGB IV).
- Bei Minijob: Anmeldung bei Minijob-Zentrale (Knappschaft-Bahn-See).
- Sofortmeldung in Sonderbranchen (§ 28a Abs. 4 SGB IV): Bau, Gaststaette, Fleischwirtschaft.

##### Phase 5 — Berufsgenossenschaft

- Mitgliedsnummer BG.
- Gefahrtarif und Beitragssatz.
- Lohnnachweis erstmalig im Folgejahr (Februar).
- Vorausabhebung BG-Beitrag im laufenden Jahr.

##### Phase 6 — Probelauf und Freigabe

- Erste Lohnabrechnung als Probelauf erstellen.
- Mit Mandant durchsprechen, Stammdaten bestaetigen.
- Erste Lohnsteuer-Anmeldung und SV-Meldung.
- Mandantenakte mit allen Unterlagen aufbauen.

#### Strategie und Praxis-Tipps

- Onboarding-Checkliste konsequent durchgehen — vergessene Stammdaten kosten später erheblich Zeit.
- ELStAM-Abruf rechtzeitig — bei Fehlern keine Abrechnung möglich.
- Bei Konzern-Mandanten: zentrale Konsistenz prüfen (gleiche Konto-Nummern, Kostenstellen).
- Mandantenvereinbarung schriftlich — Lohnbuchfuehrung StBVV § 35 separater Auftrag.
- Erstes Lohn-Jahr immer mit Stichproben prüfen (Sachbezuege, Pauschalsteuer, SV-Klassifikation).
- DATEV-Tipp: DATEV LODAS Mandanten-Anlage mit Prüfliste; bei Datenuebernahme aus Vorprogramm (z.B. Lexware) erweiterte Prüfung.

#### Quellen und Updates

Stand: 05/2026.

- EStG §§ 19, 41a; LStDV § 1.
- SGB IV §§ 8, 14, 28a.
- StBerG § 33, StBVV § 35.
- DEUEV.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
## SV-Beitraege Grundlagen — RV KV PV AV und Umlagen

Auswahlsignal: Wenn es um SV-Beitraege Grundlagen — RV KV PV AV und Umlagen in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### SV-Beitraege Grundlagen — RV KV PV AV und Umlagen

#### Fachlicher Anker

- **Normen:** § 6a, §§ 14, § 7 SGB IV.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die Sozialversicherung umfasst vier Hauptzweige: Rentenversicherung (RV), Krankenversicherung (KV), Pflegeversicherung (PV), Arbeitslosenversicherung (AV). Hinzu kommen Umlagen U1 (Krankheit), U2 (Mutterschaft), U3 (Insolvenzgeld) und ggf. Berufsgenossenschaft. Die Beitragsberechnung erfolgt prozentual vom Bruttolohn bis zur Beitragsbemessungsgrenze (BBG); über BBG beitragsfrei.

#### Kaltstart-Rueckfragen

1. SV-Status des AN — versicherungspflichtig, gerinfgfuegig, kurzfristig, Werkstudent, freiwillig versichert?
2. Bruttolohn über JAEG (Jahresarbeitsentgeltgrenze) KV — Wechsel in PKV möglich?
3. Bruttolohn über BBG — Beitragsfrei oberhalb?
4. PV: Kind oder kinderlos (Kinderlosenzuschlag)?
5. KV: Wahl Krankenkasse, Zusatzbeitragssatz individuell?
6. Bundesland: Beitragssatz PV unterschiedlich (Saarland anders)?
7. Sondersituation: Mehrfachbeschaeftigung, Bezug Arbeitslosengeld, Saison-AN?
8. Berufsgenossenschaft: Gefahrtarif, Beitragsklasse?

#### Rechtlicher Rahmen

##### Primaernormen

**SGB IV §§ 14, 17, 18** — Arbeitsentgelt, Pauschalierungen, BBG.

**SGB V** — Krankenversicherung.

**SGB VI** — Rentenversicherung.

**SGB XI** — Pflegeversicherung.

**SGB III** — Arbeitsfoerderung (AV).

**§ 7 SGB IV** — Beschäftigung.

**§ 8 SGB IV** — geringfuegige Beschäftigung.

**§ 28d SGB IV** — Gesamt-SV-Beitrag.

**§ 28e SGB IV** — Beitragspflicht AG.

##### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Sachbezugswerte-Verordnung (jaehrliche Anpassung).
- BMF/BMAS Rundschreiben.

#### Workflow

##### Phase 1 — BBG und Beitragssaetze (Stand 2025)

| Zweig | West/Ost | BBG monatlich (Stand 2025) | Beitragssatz (Stand 2025) |
|---|---|---|---|
| RV | Bundeseinheitlich ab 01.01.2025 (Angleichung Ost an West, Rentenueberleitungs-Abschlussgesetz abgeschlossen) | 8.050 EUR/Monat (96.600 EUR/Jahr) | 18,6 Prozent (paritaetisch je 9,3 Prozent) |
| AV | wie RV | 8.050 EUR/Monat (wie RV) | 2,6 Prozent (paritaetisch je 1,3 Prozent) |
| KV | bundeseinheitlich | 5.512,50 EUR/Monat (66.150 EUR/Jahr) | 14,6 Prozent allgemein + KK-Zusatzbeitrag (durchschnittlich 2,5 Prozent Stand 2025) |
| PV | bundeseinheitlich, Sonderregelung Sachsen | 5.512,50 EUR/Monat (wie KV) | 3,6 Prozent (paritaetisch); Kinderlosenzuschlag 0,6 Prozent allein AN (§ 55 Abs. 3 SGB XI i.d.F. PflegeunterstuetzungsG seit 01.07.2023) |

(Alle Werte Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel über DRV, GKV-Spitzenverband, BMAS prüfen.)

##### Phase 2 — Beitragsaufteilung AG/AN

- Grundsatz: halbe-halbe Aufteilung.
- PV-Zuschlag Kinderlose: 0,6 Prozent (Stand 2025, § 55 Abs. 3 SGB XI) zu Lasten AN allein.
- KV-Zusatzbeitrag: in der Regel paritaetisch.
- U1 (Krankheit): nur AG.
- U2 (Mutterschaft): nur AG.
- Insolvenzgeld-Umlage: nur AG.
- Berufsgenossenschaft: nur AG.

##### Phase 3 — Sonderfaelle

| Sonderfall | SV-Behandlung |
|---|---|
| Minijob (538 EUR-Grenze, Stand 01.01.2024 — bei MiLo-Anhebung dynamisch) | Pauschal 30 Prozent (15 RV + 13 KV + 2 LSt) |
| Werkstudent | Nur RV-Pflicht, keine KV/AV (sofern Werkstudent-Status) |
| Aushilfskraft kurzfristig (max. 3 Monate / 70 Tage) | SV-frei (nur KSt-Pauschal) |
| Gesellschafter-GF GmbH | SV-Pflichtfrage einzelfallabhaengig |
| Pensionaer | Nur KV/PV; RV und AV befreit |
| Mehrfachbeschaeftigung | Beitragspflicht nur ein Mal bis BBG |

##### Phase 4 — JAEG und KV-PV-Wahl

- JAEG (Jahresarbeitsentgeltgrenze) über 3 Jahre ueberschritten: AN kann in PKV wechseln.
- JAEG 2025: 73.800 EUR/Jahr (monatlich 6.150 EUR; Sozialversicherungs-Rechengroessenverordnung 2026 prüfen).
- Wechsel-Prüfung gemeinsam mit AN, ggf. AG-Zuschuss zur PKV.

##### Phase 5 — Berufsgenossenschaft

- Gefahrtarif je nach Branche.
- Beitragssatz Promille der Lohnsumme.
- Jaehrlicher Lohnnachweis im Februar des Folgejahres.
- BG-Mitglied im StB-Stammblatt erfassen.

##### Phase 6 — Buchung und Abrechnung

- SV-AG-Anteil als Lohnnebenkosten (Konto 6110 SKR04 / 4130 SKR03 "Gesetzliche soziale Aufwendungen") an Verbindlichkeit Sozialversicherung (3760 SKR04 / 1741 SKR03).
- SV-AN-Anteil als Abzug vom Brutto-Loehne-Konto: Loehne und Gehaelter (6020 SKR04 / 4120 SKR03) gegen Verbindlichkeit SV (3760 SKR04 / 1741 SKR03).
- Gesamtsumme an Krankenkasse einheitlich (Gesamt-SV-Beitrag).
- Faelligkeit: drittletzter Bankarbeitstag des laufenden Monats für die voraussichtliche Beitragsschuld (§ 23 Abs. 1 SGB IV); spaetestens Korrektur mit Beitragsnachweis bis 15. des Folgemonats.

#### Strategie und Praxis-Tipps

- SV-Faelligkeit drittletzter Bankarbeitstag — bei Verspaetung Saeumniszuschlag, ab 1 Jahr § 266a StGB-Risiko (Vorenthalten SV-Beitraege).
- BBG und Beitragssaetze jaehrlich prüfen — DATEV-Updates zum 1. Januar Pflicht.
- Bei Werkstudent: Status prüfen (20-Stunden-Regel; in der vorlesungsfreien Zeit ggf. mehr).
- Bei Mehrfachbeschaeftigung: AG-Pflicht zur Prüfung der BBG-Ueberschreitung.
- StBVV: SV-Berechnung in Lohnpauschale; komplexe Sonderfaelle (Werkstudent-Prüfung) Zeithonorar.
- DATEV-Tipp: DATEV LODAS mit automatischen Beitragssatz-Updates; Plausibilitaets-Prüfung Beitragssumme.

#### Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 7, 8, 14, 17, 18, 23, 28d, 28e.
- SGB V, VI, XI, III.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
- StGB § 266a.
- BBG 2025: RV/AV 8.050 EUR/Monat, KV/PV 5.512,50 EUR/Monat; Beitragssaetze: RV 18,6%, AV 2,6%, KV 14,6%+Zusatz, PV 3,6%+Kinderlos 0,6%.
- PV-Kinderlosenzuschlag 2025: 0,6 Prozent (§ 55 Abs. 3 SGB XI, PflegeunterstuetzungsG seit 01.07.2023).
- Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel prüfen.

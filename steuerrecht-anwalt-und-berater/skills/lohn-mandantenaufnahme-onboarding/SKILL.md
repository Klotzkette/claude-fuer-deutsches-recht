---
name: lohn-mandantenaufnahme-onboarding
description: "Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung Prüfungen Dokumente. Output Lohn-Mandantenakte Stammdaten startklar."
---

# Lohn-Mandantenaufnahme — Onboarding

## Fachlicher Anker

- **Normen:** § 6a, § 41a EStG, § 28a SGB IV.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Aufnahme eines neuen Lohn-Mandanten ist organisatorisch anspruchsvoll: Stammdaten zum Arbeitgeber und allen Arbeitnehmern, SV-Nummern, Steuer-IDs, ELStAM-Abruf, Berufsgenossenschaft, ggf. Versorgungswerk. Fehlende oder fehlerhafte Stammdaten fuehren zu später aufwendigen Korrekturen. Der Steuerberater nutzt eine Standard-Checkliste, die in DATEV LODAS, Lohn und Gehalt oder einem äquivalenten Programm zu hinterlegen ist.

## Kaltstart-Rueckfragen

1. Welche Rechtsform und Branche des Mandanten?
2. Wie viele Arbeitnehmer (Stammbelegschaft, geringfuegig, Werkstudenten)?
3. Welches Vorprogramm bzw. Vorberater (Datenuebernahme möglich)?
4. Welcher Lohnsteuer-Anmelde-Zeitraum (monatlich, vierteljaehrlich, jaehrlich)?
5. Bestehen ueberbetriebliche Tarifvertraege?
6. Gibt es eine Betriebsvereinbarung zu Loehnen, Tantiemen, bAV?
7. Welche Berufsgenossenschaft ist zuständig?
8. Gibt es Sondervergueteungen (Sachbezuege, Dienstwagen, JobRad, bAV)?

## Rechtlicher Rahmen

### Primaernormen

**§ 41a EStG** — Anmeldung und Abfuehrung Lohnsteuer.

**§ 28a SGB IV** — SV-Meldungen Arbeitgeber.

**§ 14 SGB IV** — Arbeitsentgelt-Definition.

**§ 8 SGB IV** — geringfuegige Beschäftigung.

**§ 1 LStDV** — Anwendungsbereich.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**§ 33 StBerG** — StB-Aufgabenkreis (Lohnsteuer-Hilfeleistung).

**§ 35 StBVV** — Honorar Lohnbuchfuehrung.

### Standards

- DATEV-Stammdaten-Prüfliste.
- DEUEV (Datenerfassungs- und -uebermittlungsverordnung).
- Gemeinsame Rundschreiben Spitzenverbaende Krankenkassen.

## Workflow

### Phase 1 — Arbeitgeber-Stammdaten

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

### Phase 2 — Arbeitnehmer-Stammdaten

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

### Phase 3 — ELStAM-Abruf

- ELStAM-Verfahren (Elektronische LohnSteuerAbzugsMerkmale): zentraler Abruf der LSt-Merkmale beim BZSt (§ 39e EStG).
- Voraussetzung: Steuer-Id (11-stellig) des AN.
- Abrufschluessel: AG-Steuer-Nr (FA-Schlüssel + AG-Nr) und Geburtsdatum des AN.
- Abruf-Zeitpunkt: vor der ersten Lohnabrechnung, in DATEV LODAS unter Mandant → Mitarbeiterverwaltung → ELStAM-Anmeldung; bei DATEV Lohn und Gehalt unter Stamm → ELStAM-Verfahren. Ruecklauf in der Regel binnen Sekunden.
- Erst-Anmeldung mit Anlassgrund "Beginn der Beschäftigung"; Folgemonatlich automatische Aktualisierung bei Änderungen (Steuerklasse, KiFB, KKB).

### Phase 4 — SV-Anmeldung

- Anmeldung des Arbeitnehmers bei der Krankenkasse (zugleich für RV und PV).
- Meldung Beschäftigungsbeginn binnen 6 Wochen (§ 28a SGB IV).
- Bei Minijob: Anmeldung bei Minijob-Zentrale (Knappschaft-Bahn-See).
- Sofortmeldung in Sonderbranchen (§ 28a Abs. 4 SGB IV): Bau, Gaststaette, Fleischwirtschaft.

### Phase 5 — Berufsgenossenschaft

- Mitgliedsnummer BG.
- Gefahrtarif und Beitragssatz.
- Lohnnachweis erstmalig im Folgejahr (Februar).
- Vorausabhebung BG-Beitrag im laufenden Jahr.

### Phase 6 — Probelauf und Freigabe

- Erste Lohnabrechnung als Probelauf erstellen.
- Mit Mandant durchsprechen, Stammdaten bestaetigen.
- Erste Lohnsteuer-Anmeldung und SV-Meldung.
- Mandantenakte mit allen Unterlagen aufbauen.

## Strategie und Praxis-Tipps

- Onboarding-Checkliste konsequent durchgehen — vergessene Stammdaten kosten später erheblich Zeit.
- ELStAM-Abruf rechtzeitig — bei Fehlern keine Abrechnung möglich.
- Bei Konzern-Mandanten: zentrale Konsistenz prüfen (gleiche Konto-Nummern, Kostenstellen).
- Mandantenvereinbarung schriftlich — Lohnbuchfuehrung StBVV § 35 separater Auftrag.
- Erstes Lohn-Jahr immer mit Stichproben prüfen (Sachbezuege, Pauschalsteuer, SV-Klassifikation).
- DATEV-Tipp: DATEV LODAS Mandanten-Anlage mit Prüfliste; bei Datenuebernahme aus Vorprogramm (z.B. Lexware) erweiterte Prüfung.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 19, 41a; LStDV § 1.
- SGB IV §§ 8, 14, 28a.
- StBerG § 33, StBVV § 35.
- DEUEV.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

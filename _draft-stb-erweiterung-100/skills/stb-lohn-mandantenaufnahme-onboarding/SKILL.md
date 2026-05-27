---
name: stb-lohn-mandantenaufnahme-onboarding
description: "Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung Pruefungen Dokumente. Output Lohn-Mandantenakte Stammdaten startklar."
---

# Lohn-Mandantenaufnahme — Onboarding

## Kernsachverhalt

Die Aufnahme eines neuen Lohn-Mandanten ist organisatorisch anspruchsvoll: Stammdaten zum Arbeitgeber und allen Arbeitnehmern, SV-Nummern, Steuer-IDs, ELStAM-Abruf, Berufsgenossenschaft, ggf. Versorgungswerk. Fehlende oder fehlerhafte Stammdaten fuehren zu spaeter aufwendigen Korrekturen. Der Steuerberater nutzt eine Standard-Checkliste, die in DATEV LODAS, Lohn und Gehalt oder einem aequivalenten Programm zu hinterlegen ist.

## Kaltstart-Rueckfragen

1. Welche Rechtsform und Branche des Mandanten?
2. Wie viele Arbeitnehmer (Stammbelegschaft, geringfuegig, Werkstudenten)?
3. Welches Vorprogramm bzw. Vorberater (Datenuebernahme moeglich)?
4. Welcher Lohnsteuer-Anmelde-Zeitraum (monatlich, vierteljaehrlich, jaehrlich)?
5. Bestehen ueberbetriebliche Tarifvertraege?
6. Gibt es eine Betriebsvereinbarung zu Loehnen, Tantiemen, bAV?
7. Welche Berufsgenossenschaft ist zustaendig?
8. Gibt es Sondervergueteungen (Sachbezuege, Dienstwagen, JobRad, bAV)?

## Rechtlicher Rahmen

### Primaernormen

**§ 41a EStG** — Anmeldung und Abfuehrung Lohnsteuer.

**§ 28a SGB IV** — SV-Meldungen Arbeitgeber.

**§ 14 SGB IV** — Arbeitsentgelt-Definition.

**§ 8 SGB IV** — geringfuegige Beschaeftigung.

**§ 1 LStDV** — Anwendungsbereich.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**§ 33 StBerG** — StB-Aufgabenkreis (Lohnsteuer-Hilfeleistung).

**§ 35 StBVV** — Honorar Lohnbuchfuehrung.

### Standards

- DATEV-Stammdaten-Pruefliste.
- DEUEV (Datenerfassungs- und -uebermittlungsverordnung).
- Gemeinsame Rundschreiben Spitzenverbaende Krankenkassen.

## Workflow

### Phase 1 — Arbeitgeber-Stammdaten

| Stammdaten-Feld | Quelle / Pruefung |
|---|---|
| Firma, Rechtsform, Sitz | Handelsregister-Auszug |
| Steuer-Nr und Steuer-Id | Finanzamtsbescheid |
| Betriebsstaetten-Nummer (BSN) | Bundesagentur fuer Arbeit |
| Berufsgenossenschaft + Mitgliedsnummer | BG-Bescheid |
| Krankenkassen-Schluessel | Krankenkasse |
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
| Beschaeftigungsbeginn / Eintrittsdatum | Arbeitsvertrag |
| Vereinbarte Arbeitszeit | Arbeitsvertrag |
| Brutto-Gehalt | Arbeitsvertrag |
| Sonderleistungen | Arbeitsvertrag, BV |

### Phase 3 — ELStAM-Abruf

- ELStAM-Verfahren (Elektronische LohnSteuerAbzugsMerkmale): zentraler Abruf der LSt-Merkmale beim BZSt.
- Voraussetzung: Steuer-Id des AN.
- Abrufschluessel: Arbeitgeber-Steuer-Nr und BSN.
- Abruf-Zeitpunkt: vor erster Lohnabrechnung.

### Phase 4 — SV-Anmeldung

- Anmeldung des Arbeitnehmers bei der Krankenkasse (zugleich fuer RV und PV).
- Meldung Beschaeftigungsbeginn binnen 6 Wochen (§ 28a SGB IV).
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

## Output

- Vollstaendige Stammdaten in DATEV LODAS / Lohn und Gehalt.
- ELStAM-Abruf erfolgreich.
- SV-Anmeldungen verschickt.
- Lohn-Mandantenakte aufgebaut.

## Strategie und Praxis-Tipps

- Onboarding-Checkliste konsequent durchgehen — vergessene Stammdaten kosten spaeter erheblich Zeit.
- ELStAM-Abruf rechtzeitig — bei Fehlern keine Abrechnung moeglich.
- Bei Konzern-Mandanten: zentrale Konsistenz pruefen (gleiche Konto-Nummern, Kostenstellen).
- Mandantenvereinbarung schriftlich — Lohnbuchfuehrung StBVV § 35 separater Auftrag.
- Erstes Lohn-Jahr immer mit Stichproben pruefen (Sachbezuege, Pauschalsteuer, SV-Klassifikation).
- DATEV-Tipp: DATEV LODAS Mandanten-Anlage mit Pruefliste; bei Datenuebernahme aus Vorprogramm (z.B. Lexware) erweiterte Pruefung.

## Querverweise

- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Arbeitsvertrag.
- `stb-lohn-meldungen-sv-elstam-zugang` — SV/ELStAM.
- `stb-lohn-sv-beitraege-grundlagen` — SV-Grundlagen.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.
- `stb-mandanten-onboarding-checkliste-vollservice` — Vollservice-Onboarding.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 19, 41a; LStDV § 1.
- SGB IV §§ 8, 14, 28a.
- StBerG § 33, StBVV § 35.
- DEUEV.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

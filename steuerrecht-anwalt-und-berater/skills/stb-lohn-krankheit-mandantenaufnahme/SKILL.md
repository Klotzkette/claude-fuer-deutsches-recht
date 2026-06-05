---
name: stb-lohn-krankheit-mandantenaufnahme
description: "STB Lohn Krankheit Mandantenaufnahme: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Lohn Krankheit Mandantenaufnahme

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **STB Lohn Krankheit Mandantenaufnahme** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-lohn-krankheit-entgeltfortzahlung-efzg` | Krankheit Entgeltfortzahlung 6 Wochen § 3 EFZG eAU. Anwendungsfall Lohnabrechnung bei Krankheit Entgeltfortzahlung 6 Wochen U1-Umlage Krankengeld Krankenkasse-Erstattung elektronische Arbeitsunfähigkeit. Methodik Prüfung Anspruch Berechnung. Output Lohn-Abrechnung Krank Erstattungsantrag U1. |
| `stb-lohn-mandantenaufnahme-onboarding` | Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung Prüfungen Dokumente. Output Lohn-Mandantenakte Stammdaten startklar. |
| `stb-lohn-mehrarbeit-zuschlaege-39b-estg` | Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG. Anwendungsfall Lohnabrechnung mit Schichtzuschlaegen Gastronomie Pflege Sicherheitsdienst LSt-Freiheit SV-Freiheit in Grenzen. Methodik Prüfung Begrenzung Grundlohn Pflichtdokumentation. Output Lohn-Abrechnung mit korrekter Zuschlag-Behandlung. |
| `stb-lohn-meldungen-sv-elstam-zugang` | SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschaeftigungsbeginn und Beendigung Anmeldung Abmeldung Aenderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik DEUEV-Verfahren ELStAM Prüfung. Output gemeldete Vorgaenge Quittungen. |
| `stb-lohn-midi-job-uebergangsbereich-2000-euro` | Midi-Job-Übergangsbereich 538 EUR/01 bis 2000 EUR Stand 2023. Anwendungsfall geminderte AN-SV-Beitraege in der Gleitzone Berechnung Faktor F Anpassung 2026. Methodik Berechnungsmodul SV-Beitrag AN Gleitzone. Output Midi-Job-Abrechnung. |
| `stb-lohn-mindestlohn-aktuell-2026-anpassung` | Aktueller Mindestlohn 2026 Anpassung. Anwendungsfall Prüfung des aktuellen MiLo-Wertes Auswirkung auf Mini- Midi-Job-Grenzen Vertragsklauseln Mandanten-Information. Methodik Verifikation amtliche Quellen Mandantenkommunikation. Output MiLo-Übersicht aktuell Verifikations-Hinweis. |
| `stb-lohn-mini-midi-grenzen-2026-stand` | Aktuelle Mini- und Midi-Job-Grenzen 2026. Anwendungsfall Prüfung aktueller Schwellenwerte für Geringfuegigkeit und Übergangsbereich Verifikation gegen Mindestlohn-Anpassungen. Methodik Werteprüfung Quellen amtliche Veröffentlichungen. Output Schwellenwert-Übersicht mit Stichtag und Verifikations-Hinweis. |
| `stb-lohn-monatsende-meldepflichten-checkliste` | Lohn-Meldepflichten zum Monatsende Checkliste LSt-Anmeldung SV-Beitragsnachweis DEUEV BG-Lohnnachweis. Anwendungsfall standardisierter Prüfablauf vor Monatsende und Fristen Auswertung. Methodik Prüfliste Termincontrolling. Output Erledigungs-Liste. |
| `stb-lohn-praktikanten-azubis-loehne` | Praktikanten und Azubis lohnrelevante Sonderregeln. Anwendungsfall Pflichtpraktikum freiwilliges Praktikum Berufsausbildung BBiG Berufsausbildungsbeihilfe SV-Behandlung Vergueteung. Methodik Unterscheidung Pflicht- vs freiwilliges Praktikum Schwellen. Output Lohn-Abrechnung mit korrekter SV-Klassifikation. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Lohn Krankheit Mandantenaufnahme**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-lohn-krankheit-entgeltfortzahlung-efzg`

**Fokus:** Krankheit Entgeltfortzahlung 6 Wochen § 3 EFZG eAU. Anwendungsfall Lohnabrechnung bei Krankheit Entgeltfortzahlung 6 Wochen U1-Umlage Krankengeld Krankenkasse-Erstattung elektronische Arbeitsunfähigkeit. Methodik Prüfung Anspruch Berechnung. Output Lohn-Abrechnung Krank Erstattungsantrag U1.

# Krankheit — Entgeltfortzahlung § 3 EFZG und eAU

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Krankheit — Entgeltfortzahlung § 3 EFZG und eAU` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei Krankheit hat der AN nach § 3 EFZG fuer 6 Wochen Anspruch auf Entgeltfortzahlung — der AG zahlt den vollen Lohn weiter. Nach 6 Wochen zahlt die Krankenkasse Krankengeld. Kleinbetriebe (bis 30 AN) koennen Erstattung U1-Umlage bei der Krankenkasse beantragen. Seit 2023 ist die elektronische Arbeitsunfaehigkeitsbescheinigung (eAU) verpflichtend — der AG ruft die AU-Daten direkt bei der Krankenkasse ab.

## Kaltstart-Rueckfragen

1. Hat der AN mind. 4 Wochen Beschaeftigung im Betrieb (Voraussetzung Entgeltfortzahlung)?
2. Liegt eAU vor (Abruf bei Krankenkasse)?
3. Welche Krankheitstage in der laufenden 12-Monats-Periode bereits angerechnet?
4. Bei chronischer Krankheit mit wiederholten Krankheitsphasen: Pruefung "Fortsetzungskrankheit"?
5. AG-Groesse fuer U1-Umlage-Pflicht?
6. Bei Krankheit ueber 6 Wochen: Krankengeld-Beginn ueber Krankenkasse?
7. Welche Lohnart wird fortgezahlt (Grundgehalt, Zuschlaege)?
8. Lag Arbeitsunfall vor (BG-Leistungen)?

## Rechtlicher Rahmen

### Primaernormen

**EFZG (Entgeltfortzahlungsgesetz)** — Krankheits-Entgeltfortzahlung.

**§ 3 EFZG** — 6-Wochen-Anspruch.

**§ 4 EFZG** — Hoehe Entgeltfortzahlung (100 Prozent).

**§ 5 EFZG** — Anzeige- und Nachweispflicht.

**§ 6 EFZG** — Fortsetzungskrankheit.

**AAG (Aufwendungsausgleichsgesetz)** — U1-Umlage.

**§ 109 SGB IV** — eAU-Verfahren.

**SGB V** — Krankengeld nach 6 Wochen.

### Verwaltungsanweisungen

- eAU-Verfahren BMAS.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

## Workflow

### Phase 1 — Anspruchspruefung

| Voraussetzung | Pruefung |
|---|---|
| Arbeitsverhaeltnis | Besteht |
| Mind. 4 Wochen Wartezeit | Erfuellt |
| Krankheit ohne Verschulden | Ja |
| AU-Bescheinigung | eAU abrufbar |

### Phase 2 — eAU-Verfahren

- § 109 SGB IV i.V.m. § 5 Abs. 1a EFZG: ab 01.01.2023 verpflichtende Abruf-Pflicht des AG (gesetzlich Versicherte); Pilotphase 2022.
- AN informiert AG ueber Krankheit telefonisch oder per Mail (eigene Pflicht aus § 5 Abs. 1 EFZG bleibt: unverzuegliche Mitteilung der Arbeitsunfaehigkeit und voraussichtlichen Dauer).
- AG ruft eAU-Daten ueber Krankenkasse ab; in DATEV LODAS unter Mitarbeiterstamm → Krankmeldung → eAU-Abruf.
- AN muss nicht mehr "gelbe Bescheinigung" persoenlich abgeben.
- Ausnahme: privat versicherte AN — kein eAU; weiterhin Papier-Bescheinigung.

### Phase 3 — Berechnung Entgeltfortzahlung

- 100 Prozent des durchschnittlichen Brutto-Arbeitsentgelts.
- Bemessungsbasis: regelmäßige Arbeitsleistung.
- Schwankende Verguetung: Durchschnittsberechnung 13 Wochen.
- Mehrarbeit, Schichtzuschlaege: einbezogen, soweit zur regelmäßigen Verguetung.

### Phase 4 — 6-Wochen-Grenze und Fortsetzung

- 42 Kalendertage pro Krankheitsfall.
- Fortsetzungskrankheit (gleiche Diagnose): Anrechnung auf 42 Tage.
- 6 Monate ohne neue Erkrankung gleicher Art: erneut voller Anspruch.

### Phase 5 — U1-Umlage Erstattung

- AG-Pruefung: Kleinunternehmer bis 30 AN (U1).
- AG zahlt monatliche Umlage (Prozentsatz auf Bruttolohnsumme).
- Bei Krankheit: 80 Prozent (Kostenerstattung) durch Krankenkasse, Antrag durch AG.
- Bei Mutterschaft (U2): Erstattung 100 Prozent unabhaengig Betriebsgroesse.

### Phase 6 — Nach 6 Wochen

- Krankenkasse zahlt Krankengeld direkt an AN.
- AG ist beendet aus der Lohnabrechnung (Unterbrechungsmeldung Grund 51).
- Bei langer Krankheit (ueber 78 Wochen): Rente wegen Erwerbsminderung pruefen.

## Output

- Lohn-Abrechnung mit Entgeltfortzahlung.
- U1-Erstattungsantrag an Krankenkasse.
- Krankheitstage-Aufzeichnung.

## Strategie und Praxis-Tipps

- eAU ist seit 2023 Standard — AG-Belastung reduziert (kein Papierabruf mehr).
- U1-Umlage-Erstattung lohnt sich nur bis 30 AN (Kostendeckung 80 Prozent).
- Bei wiederholten Krankheiten gleicher Diagnose Fortsetzungskrankheit-Pruefung.
- Bei Konflikt Krankheit-Echtheit: AG kann nach BAG arbeitsrechtlich agieren.
- StBVV: Krankheits-Abrechnung in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS eAU-Schnittstelle einrichten; automatischer Krankheits-Lohn.

## Querverweise

- `stb-lohn-elternzeit-mutterschutz` — Mutterschutz.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-umlage-u1-u2-insogeld-umlage` — U1/U2-Umlagen.
- `stb-eau-elektronische-arbeitsunfaehigkeit-2023` — eAU.

## Quellen und Updates

Stand: 05/2026.

- EFZG §§ 3, 4, 5, 6.
- AAG.
- SGB IV § 109.
- SGB V.
- BMAS eAU-Verfahren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-lohn-mandantenaufnahme-onboarding`

**Fokus:** Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung Prüfungen Dokumente. Output Lohn-Mandantenakte Stammdaten startklar.

# Lohn-Mandantenaufnahme — Onboarding

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohn-Mandantenaufnahme — Onboarding` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


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

- ELStAM-Verfahren (Elektronische LohnSteuerAbzugsMerkmale): zentraler Abruf der LSt-Merkmale beim BZSt (§ 39e EStG).
- Voraussetzung: Steuer-Id (11-stellig) des AN.
- Abrufschluessel: AG-Steuer-Nr (FA-Schluessel + AG-Nr) und Geburtsdatum des AN.
- Abruf-Zeitpunkt: vor der ersten Lohnabrechnung, in DATEV LODAS unter Mandant → Mitarbeiterverwaltung → ELStAM-Anmeldung; bei DATEV Lohn und Gehalt unter Stamm → ELStAM-Verfahren. Ruecklauf in der Regel binnen Sekunden.
- Erst-Anmeldung mit Anlassgrund "Beginn der Beschaeftigung"; Folgemonatlich automatische Aktualisierung bei Aenderungen (Steuerklasse, KiFB, KKB).

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
- `stb-lohn-sv-meldungen-dakota-svnet` — DAKOTA/sv.net.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.
- `stb-mandanten-onboarding-checkliste-vollservice` — Vollservice-Onboarding.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 19, 41a; LStDV § 1.
- SGB IV §§ 8, 14, 28a.
- StBerG § 33, StBVV § 35.
- DEUEV.
- Gemeinsame Rundschreiben Spitzenverbaende KK.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-lohn-mehrarbeit-zuschlaege-39b-estg`

**Fokus:** Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG. Anwendungsfall Lohnabrechnung mit Schichtzuschlaegen Gastronomie Pflege Sicherheitsdienst LSt-Freiheit SV-Freiheit in Grenzen. Methodik Prüfung Begrenzung Grundlohn Pflichtdokumentation. Output Lohn-Abrechnung mit korrekter Zuschlag-Behandlung.

# Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zuschlaege fuer tatsaechlich geleistete Sonntags-, Feiertags- und Nachtarbeit sind nach § 3 b EStG steuerfrei in bestimmten Grenzen — und mit der entsprechenden Regelung in der SvEV auch SV-frei. Voraussetzungen: tatsaechliche Sonn-/Feiertag-/Nachtarbeit, schriftliche Vereinbarung, Begrenzung auf Hoechstsaetze, Beschraenkung auf Grundlohn bis 50 EUR/Stunde.

## Kaltstart-Rueckfragen

1. In welcher Branche arbeitet der AN (Gastronomie, Pflege, Sicherheit, Industrie)?
2. Liegen schriftliche Zuschlag-Vereinbarungen vor (Arbeitsvertrag oder Tarifvertrag)?
3. Welche Schichten — Sonntag, Feiertag, Nacht, Heiligabend, Silvester, 1. Mai?
4. Wie hoch ist der Grundlohn pro Stunde?
5. Welche Zuschlag-Prozentsaetze gelten (gesetzliche Hoechstwerte vs. tarifliche)?
6. Liegen Arbeitszeitnachweise mit konkreten Schichtzeiten vor?
7. Welche Vertretung — Stundennachweis-System (Zeitwirtschaft)?
8. Welche Pausenregelung in Nachtschicht?

## Rechtlicher Rahmen

### Primaernormen

**§ 3b EStG** — Steuerfreiheit Zuschlaege Sonn-/Feiertag-/Nachtarbeit.

**§ 6 ArbZG** — Nachtarbeit-Definition (zwischen 23 und 6 Uhr; abweichend in Tarifvertraegen).

**§ 9 ArbZG** — Sonn- und Feiertagsruhe.

**SvEV § 1 Abs. 1 Nr. 1** — SV-Freiheit Zuschlaege § 3b EStG.

**§ 14 SGB IV** — Arbeitsentgelt.

### Verwaltungsanweisungen

- LStR R 3 b.
- BMF zu Pflegekraeften (Sonderregelungen).

## Workflow

### Phase 1 — Zuschlag-Hoechstsaetze § 3b EStG (LSt-/SV-frei bis zu diesen Saetzen)

| Zuschlagsart | Steuerlicher Hoechstsatz auf Grundlohn |
|---|---|
| Sonntagsarbeit (0-24 Uhr) | 50 Prozent |
| Feiertagsarbeit (Wochentag-Feiertag) | 125 Prozent |
| Heiligabend ab 14 Uhr; 1. und 2. Weihnachtstag; 1. Mai | 150 Prozent |
| Silvester ab 14 Uhr | 125 Prozent |
| Nachtarbeit (20-6 Uhr, regulaer) | 25 Prozent |
| Nachtarbeit (0-4 Uhr, sofern vor 0 Uhr aufgenommen) | 40 Prozent |

Wenn tariflich oder einzelvertraglich hoehere Zuschlaege vereinbart sind, bleibt nur der Anteil bis zum § 3b-EStG-Hoechstsatz steuer- und SV-frei; der ueberschiessende Teil ist voll lohnsteuer- und beitragspflichtig. Die ArbZG-Definition Nachtarbeit (23-6 Uhr, § 2 Abs. 3 ArbZG) ist nicht identisch mit der steuerlichen Definition.

### Phase 2 — Grundlohn-Grenze 50 EUR/Stunde

- Bei Grundlohn > 50 EUR/Stunde: Zuschlag nur auf 50 EUR/Stunde basierend LSt-frei.
- Daruber hinaus normal versteuert.
- SV-rechtlich gilt zusaetzlich die strengere Grundlohn-Grenze 25 EUR/Stunde (§ 1 Abs. 1 Satz 1 Nr. 1 SvEV; Stand 2025, unveraendert seit 2019); bei Grundlohn > 25 EUR/Stunde ist der Zuschlag-Anteil oberhalb 25 EUR LSt-frei, aber SV-pflichtig.

**Zahlenbeispiel Nachtarbeit (Gastronomie):** Grundlohn 14 EUR/Stunde, Nachtarbeit von 22:00 bis 04:00 Uhr (6 Stunden), Zuschlag tariflich 25 Prozent. Steuerlich nach § 3b EStG: Nachtarbeit (20-6 Uhr) 25 Prozent von 14 EUR = 3,50 EUR/Stunde; in den Stunden 0-4 Uhr (sofern vor 0 Uhr aufgenommen) 40 Prozent = 5,60 EUR/Stunde. Bei Sonntagsarbeit zusaetzlich 50 Prozent Sonntagszuschlag (kumulierbar mit Nachtzuschlag). Zuschlagssumme LSt- und (bis 25 EUR Grundlohn) SV-frei.

### Phase 3 — Zeit-Definition

- Sonntag: 0:00-24:00 Uhr.
- Feiertag: gesetzlicher Feiertag, oft Landesrecht.
- Nacht: 20:00-6:00 Uhr (steuerlich); ArbZG sieht 23:00-6:00 Uhr.
- Bei Schichten ueber Mitternacht: Trennung nach Schichtanteilen.

### Phase 4 — Dokumentation

- Schriftliche Vereinbarung im Arbeitsvertrag oder Tarifvertrag.
- Arbeitszeitnachweis mit konkreten Schichtbeginn und -ende.
- Aufzeichnung MiLoG § 17.
- Stundenkonto.

### Phase 5 — Berechnung in DATEV LODAS

- Schichtcode in DATEV LODAS hinterlegen.
- Automatische Zuschlag-Berechnung.
- LSt-Freiheit und SV-Freiheit automatisch berechnet.
- Pruefung: Plausibilitaet bei hohen Zuschlagsanteilen (>50 Prozent des Lohns).

### Phase 6 — Steuerliche Risiken

- Bei Ueberschreitung der Hoechstsaetze: Nachversteuerung.
- Bei fehlender Dokumentation: gesamter Zuschlag steuerpflichtig.
- Bei Pruefung durch Lohnsteuer-Aussenpruefer: Stichproben.

## Output

- Lohn-Abrechnung mit korrekter Zuschlag-Behandlung.
- Schichtnachweis-Aufzeichnung.
- Dokumentation Vereinbarung im Vertrag.

## Strategie und Praxis-Tipps

- § 3b EStG ist generoes — bis zu 50 Prozent Sonntagszuschlag steuer- und SV-frei.
- Bei tarifgebundenen Branchen hoehere Saetze moeglich, aber nur bis Hoechstsatz steuerfrei.
- Bei Nachtarbeit zusaetzlich ArbZG-Pflichten (Pausen, Gesundheitsuntersuchung).
- Grundlohn-Grenze 50 EUR/Stunde fuer Topverdiener relevant.
- StBVV: in Lohnpauschale; komplexe Schichten Zeithonorar.
- DATEV-Tipp: DATEV LODAS Schichtkonfiguration sorgfaeltig — Zeitgrenzen automatisch.

## Querverweise

- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` — Ueberstunden.
- `stb-lohn-aufzeichnungspflichten-milog` — MiLoG.

## Quellen und Updates

Stand: 05/2026.

- EStG § 3b.
- ArbZG §§ 6, 9.
- SvEV § 1.
- LStR R 3 b.
- BMF zu Pflegekraeften.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (SvEV Grundlohn-Grenze 25 EUR/Stunde seit 2019 stabil) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-lohn-meldungen-sv-elstam-zugang`

**Fokus:** SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschaeftigungsbeginn und Beendigung Anmeldung Abmeldung Aenderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik DEUEV-Verfahren ELStAM Prüfung. Output gemeldete Vorgaenge Quittungen.

# SV-Meldungen und ELStAM-Verfahren

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SV-Meldungen und ELStAM-Verfahren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei Beschaeftigungsbeginn ist der Arbeitnehmer zur Sozialversicherung anzumelden, bei Ende abzumelden. Aenderungen (Krankenkasse-Wechsel, Adresse, Steuerklasse) sind zu melden. Parallel erfolgt der elektronische Abruf der Lohnsteuer-Abzugsmerkmale (ELStAM). Das DEUEV-Verfahren (Datenerfassungs- und -uebermittlungsverordnung) steuert die SV-Meldungen, das ELStAM-Verfahren die LSt-Abzugsmerkmale. Beide muessen rechtzeitig und korrekt erfolgen.

## Kaltstart-Rueckfragen

1. Beschaeftigungsbeginn — wann, regulaer oder Sofortmeldungspflicht (Bau, Gaststaette, Fleisch, ...)?
2. Steuer-Id des AN vorhanden?
3. Krankenkassen-Wahl bekannt?
4. SV-Status — versicherungspflichtig, geringfuegig, kurzfristig, Werkstudent?
5. AN-Vorbeschaeftigung in laufender Periode (Mehrfachbeschaeftigung)?
6. Liegt Aenderungs-Anlass vor (Steuerklasse, Adresse, Kinderfreibetrag)?
7. Bei Beendigung: ordentliche Kuendigung, fristlos, Aufhebungsvertrag?
8. Liegt ELStAM-Sperre vor (Mehrfacharbeitgeber-Konflikt)?

## Rechtlicher Rahmen

### Primaernormen

**§ 28a SGB IV** — Meldepflichten Arbeitgeber.

**§ 28e SGB IV** — Arbeitgeber-Beitragspflicht.

**§ 28f SGB IV** — Aufzeichnungs- und Aufbewahrungspflicht.

**DEUEV** — Verordnung; konkretisiert die Meldepflichten.

**§ 39e EStG** — ELStAM-Verfahren.

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 41b EStG** — elektronische Lohnsteuerbescheinigung.

### Verwaltungsanweisungen

- BMF und BMAS Rundschreiben.
- Gemeinsame Rundschreiben Spitzenverbaende Krankenkassen.
- ITSG (IT-Sicherheitsgesellschaft) — technische Spezifikation.

## Workflow

### Phase 1 — Beschaeftigungsbeginn-Anmeldung

| Meldungsart | Inhalt | Frist |
|---|---|---|
| Anmeldung | Beschaeftigungsbeginn, AN-Daten | Mit der ersten naechsten Lohnabrechnung, spaetestens 6 Wochen nach Beschaeftigungsbeginn |
| Sofortmeldung (Sonderbranchen) | Vor Beschaeftigungsbeginn | Spaetestens bei Aufnahme der Beschaeftigung |
| Minijob-Anmeldung | Bei Minijob-Zentrale (Knappschaft) | Mit erster Abrechnung |

### Phase 2 — DEUEV-Abgabegruende (Auszug)

- Anmeldung (Grund 10).
- Abmeldung (Grund 30).
- Jahresmeldung (Grund 50).
- Unterbrechungsmeldung (Grund 51).
- Aenderung Beitragsgruppe (Grund 11).
- Aenderung Personalien (Grund 12).
- Sofortmeldung (Grund 20).

### Phase 3 — ELStAM-Abruf

- Anmeldung beim ELStAM-Verfahren ueber das BZSt (Bundeszentralamt fuer Steuern).
- Voraussetzungen: AN-Steuer-ID (11-stellig nach § 139b AO), AG-Steuer-Nr (oder AG-Identifikationsnummer), AG-Betriebsstaetten-Nummer der BA.
- Standard-Abrufintervall: monatlich vor der Lohnabrechnung; in DATEV LODAS automatisiert.
- Bei Aenderungen (Steuerklasse, Kinderfreibetrag, Konfession): automatische Aktualisierung durch FA; das AG-System aktualisiert ELStAM beim naechsten Abruf.

### Phase 4 — ELStAM-Sonderfaelle

- Erster Arbeitgeber (Steuerklasse 1-5): Hauptbeschaeftigung.
- Weiterer Arbeitgeber (Steuerklasse 6): hoechste LSt-Belastung.
- Aenderung Hauptbeschaeftigung: AN muss FA informieren.
- Bei ELStAM-Sperre durch Konflikt: Sperrgrund pruefen, AN-Aufklaerung.

### Phase 5 — Abmeldung

- Bei Beschaeftigungsende: Abmeldung in der naechsten Entgeltabrechnung.
- Grund 30 (regulaer), 34 (Tod), 36 (Renteneintritt).
- ELStAM-Abmeldung automatisch.

### Phase 6 — Dokumentation und Quittungen

- DEUEV-Quittungen archivieren (10 Jahre).
- ELStAM-Quittungen.
- DATEV-Mandantenakte Lohn.

## Output

- DEUEV-Anmeldung/Abmeldung verschickt.
- ELStAM-Abruf erfolgreich (Steuerklasse, KiFB, KV-Status).
- Quittungen in Mandantenakte.

## Strategie und Praxis-Tipps

- Anmeldung rechtzeitig — Sofortmeldungspflicht-Branchen vor Beschaeftigungsbeginn melden.
- Bei Sofortmeldungs-Branchen Verspaetung: Bussgelder erheblich (bis 25.000 EUR fuer den AG).
- ELStAM-Abruf jeden Monat — Aenderungen durch FA (KiFB, KKB) werden automatisch wirksam.
- Bei Mehrfachbeschaeftigung: AN muss FA bzgl. Hauptarbeitgeber informieren.
- StBVV: SV/ELStAM-Meldungen pauschal in Lohnabrechnungsentgelt.
- DATEV-Tipp: DATEV LODAS DEUEV-Modul und ELStAM-Schnittstelle automatisiert.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-lohnsteuer-monatsabschluss` — LSt-Anmeldung.
- `stb-lohn-sv-beitraege-grundlagen` — SV-Beitraege.
- `stb-lohn-sv-meldungen-dakota-svnet` — DAKOTA/sv.net.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28e, 28f.
- DEUEV.
- EStG §§ 39e, 41a, 41b.
- BMF-Rundschreiben ELStAM.
- ITSG-Spezifikation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-lohn-midi-job-uebergangsbereich-2000-euro`

**Fokus:** Midi-Job-Übergangsbereich 538 EUR/01 bis 2000 EUR Stand 2023. Anwendungsfall geminderte AN-SV-Beitraege in der Gleitzone Berechnung Faktor F Anpassung 2026. Methodik Berechnungsmodul SV-Beitrag AN Gleitzone. Output Midi-Job-Abrechnung.

# Midi-Job / Uebergangsbereich — 538,01 bis 2.000 EUR

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Midi-Job / Uebergangsbereich — 538,01 bis 2.000 EUR` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Uebergangsbereich (umgangssprachlich Midi-Job) liegt zwischen 538,01 EUR (Stand 01.01.2024) und 2.000 EUR (Stand 01.01.2023). In diesem Bereich werden die AN-SV-Beitraege progressiv geminderter berechnet, um den Sprung vom SV-freien Minijob in die volle SV-Pflicht abzufedern. Der AG-Anteil bleibt voll. Die Berechnung erfolgt mit einer Formel auf Basis der jeweiligen Beitragssaetze; DATEV LODAS / Lohn und Gehalt erledigen das automatisch.

## Kaltstart-Rueckfragen

1. Bruttolohn des AN — zwischen 538,01 und 2.000 EUR (Stand 01.01.2023 ff.)?
2. Hat sich die Obergrenze geaendert? Stand 2025: Obergrenze 2.000 EUR (§ 20 Abs. 2 SGB IV, seit 01.01.2023 unveraendert); pruefen ob Anpassung durch Gesetzgeber erfolgt.
3. Sonderzahlungen (Tantieme, 13. Gehalt) — Jahresdurchschnitt im Uebergangsbereich?
4. SV-Pflicht alle Zweige (KV/RV/PV/AV) oder Sonderstatus?
5. Mehrfachbeschaeftigung — Summe ueber 2.000 EUR?
6. Hat der AN gewuenscht, voll SV-pflichtig zu sein (Wahl moeglich)?
7. AG-Anteil: voll oder gemildert? (Antwort: AG voll, AN gemindert.)
8. Welcher Versorgungs- und Steuerstatus?

## Rechtlicher Rahmen

### Primaernormen

**§ 20 Abs. 2 SGB IV** — Uebergangsbereich; geminderte Beitragsbemessung AN.

**§ 14 SGB IV** — Arbeitsentgelt.

**§ 22 Abs. 1 SGB IV** — Faktor F-Berechnung.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Anpassungen bei MiLo-Erhoehung wirksam (Untergrenze).

## Workflow

### Phase 1 — Grenz-Pruefung

| Bereich | Grenze | SV-Behandlung |
|---|---|---|
| Minijob | Bis 538 EUR (Stand 01.01.2024) | Pauschal AG; AN-Befreiungs-Option |
| Midi-Job (Uebergangsbereich) | 538,01-2.000 EUR | Gemindertes AN; voll AG |
| Regulaer | Ab 2.000,01 EUR | Voll AG und AN |

(Stand 2025: Untergrenze 556,01 EUR (dynamisch mit Mindestlohn), Obergrenze 2.000 EUR; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen.)

### Phase 2 — Faktor-F-Berechnung

- § 20 Abs. 2 SGB IV i.V.m. § 163 Abs. 10 SGB VI: Reduzierung des SV-pflichtigen Entgelts bei Brutto im Uebergangsbereich.
- Faktor F = (Gesamt-SV-Beitragssatz Minijob-Pauschal) / (Gesamt-SV-Beitragssatz regulaer). F wird jaehrlich vom Bundesministerium fuer Arbeit bekanntgemacht.
- F wird im Lohn-Programm automatisch berechnet; jaehrliche Aktualisierung bei Aenderung der Beitragssaetze.

### Phase 3 — Beitragsberechnung

Vereinfacht: AN-Anteil wird linear progressiv erhoeht von 0 (an Untergrenze) bis voller Beitrag (an Obergrenze). Die genaue Formel ist gesetzlich vorgegeben und durch DATEV/Lohn und Gehalt umgesetzt.

### Phase 4 — Wahlrecht voll SV-Pflicht

- AN kann schriftlich erklaeren, voll SV-pflichtig sein zu wollen (Vorteil: hoehere RV-Anwartschaft).
- Wirksam ab Folgemonat.
- Nicht ruecknahmemoeglich.

### Phase 5 — Sonderzahlungen

- Bei einmaligen Sonderzahlungen: Aufteilung auf die Monate, sofern regelmaessig.
- Bei unregelmäßigen Sonderzahlungen: separate Berechnung.

### Phase 6 — Buchung

- AG-Anteil voll als Lohnnebenkosten.
- AN-Anteil gemindert als Abzug.
- Differenz zur regulaeren AN-Beitragslast = staatliche Subvention.

## Output

- Lohnabrechnung mit Midi-Job-Faktor.
- Korrekte AG-AN-Aufteilung.
- Dokumentation Wahlrecht voll SV-Pflicht falls genutzt.

## Strategie und Praxis-Tipps

- Untergrenze des Uebergangsbereichs steigt automatisch mit Mindestlohn-Anhebung (§ 8 Abs. 1a SGB IV; Stand 2025: 556,01 EUR); bei Mindestlohn-Aenderung Untergrenze neu berechnen.
- Bei voll-SV-Wahl: AN-Vorteil ist hoehere Rente, aber laufender Nettolohn niedriger.
- AG-Vorteil im Midi-Job: voller AG-Anteil bleibt, Beitragsentlastung kommt voll dem AN zugute.
- Bei Mehrfachbeschaeftigung Summe wesentlich — bei Ueberschreitung 2.000 EUR verlassen alle Stellen den Uebergangsbereich.
- StBVV: in Lohnpauschale; komplexe Sonderzahlungen Zeithonorar.
- DATEV-Tipp: DATEV LODAS prueft automatisch Midi-Job-Status; bei Bruttolohn-Aenderung Folgemonat anpassen.

## Querverweise

- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-mini-midi-grenzen-2026-stand` — aktuelle Grenzen.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 14, 20, 22.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Uebergangsbereich 2025: 556,01 EUR bis 2.000 EUR (§ 20 Abs. 2 SGB IV; Obergrenze seit 01.01.2023 stabil; Untergrenze dynamisch mit Mindestlohn; Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 3 bestaetigt (Grenzen 2025 eingesetzt), 1 ersetzt (Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-lohn-mindestlohn-aktuell-2026-anpassung`

**Fokus:** Aktueller Mindestlohn 2026 Anpassung. Anwendungsfall Prüfung des aktuellen MiLo-Wertes Auswirkung auf Mini- Midi-Job-Grenzen Vertragsklauseln Mandanten-Information. Methodik Verifikation amtliche Quellen Mandantenkommunikation. Output MiLo-Übersicht aktuell Verifikations-Hinweis.

# Aktueller Mindestlohn 2026 — Anpassung und Wirkung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aktueller Mindestlohn 2026 — Anpassung und Wirkung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der gesetzliche Mindestlohn wird kontinuierlich angehoben — durch Empfehlung der Mindestlohnkommission, durch Verordnung der Bundesregierung oder durch Gesetz. Stand 01.01.2024: 12,41 EUR. Stand 01.01.2025: 12,82 EUR (Vierte Verordnung zur Anpassung der Hoehe des Mindestlohns, MiLoV4). **Stand 01.01.2026: 13,90 EUR**, **Stand 01.01.2027: 14,60 EUR** (Fuenfte Verordnung zur Anpassung der Hoehe des Mindestlohns — MiLoV5 — vom 05.11.2025, BGBl. 2025 I Nr. 268, ausgegeben 07.11.2025; Berichtigung BGBl. 2025 I Nr. 312). Die Empfehlung der Mindestlohnkommission stammt vom 27.06.2025; das Kabinett hat sie Ende Oktober 2025 angenommen. Der Mindestlohn betrifft direkt Mini-/Midi-Job-Grenzen, viele Arbeitsvertraege und MiLoG-Aufzeichnungspflichten.

## Kaltstart-Rueckfragen

1. Welcher Stichtag wird betrachtet?
2. Welcher Wert ist amtlich (aus welcher Quelle)?
3. Wann ist die naechste Anpassung?
4. Welche Mandanten zahlen aktuell auf MiLo-Niveau?
5. Welche tariflichen Sonderregelungen (Branchen-Mindestloehne hoeher)?
6. Welche Aufzeichnungspflichten sind betroffen?
7. Liegen Verstoss-Risiken bei einzelnen Mandanten (verspaetete Anpassung)?
8. Welche Mandanteninformations-Routine eingerichtet?

## Rechtlicher Rahmen

### Primaernormen

**MiLoG** — Mindestlohngesetz.

**§ 1 MiLoG** — Mindestlohnhoehe.

**§ 4 MiLoG** — Anpassung.

**§ 5 MiLoG** — Branchen-Mindestloehne.

**§ 21 MiLoG** — Bussgelder bei Verstoss bis 500.000 EUR.

### Verwaltungsanweisungen

- Mindestlohnkommission Empfehlungen.
- BMAS Rundschreiben.

## Workflow

### Phase 1 — MiLo-Historie

| Stichtag | Mindestlohn EUR/Stunde |
|---|---|
| 01.01.2015 (Einfuehrung) | 8,50 |
| 01.01.2017 | 8,84 |
| 01.01.2019 | 9,19 |
| 01.01.2020 | 9,35 |
| 01.01.2021 | 9,50 |
| 01.07.2021 | 9,60 |
| 01.01.2022 | 9,82 |
| 01.07.2022 | 10,45 |
| 01.10.2022 | 12,00 (gesetzliche Erhoehung) |
| 01.01.2024 | 12,41 |
| 01.01.2025 | 12,82 (MiLoV4) |
| 01.01.2026 | 13,90 (MiLoV5 v. 05.11.2025, BGBl. 2025 I Nr. 268; Berichtigung BGBl. 2025 I Nr. 312) |
| 01.01.2027 | 14,60 (MiLoV5, gleiche Verordnung) |

### Phase 2 — Verifikations-Quellen

- Bundesgesetzblatt (BGBl.) — Mindestlohn-Verordnungen.
- Mindestlohnkommission (mindestlohn-kommission.de) — Empfehlungen.
- BMAS-Pressemitteilungen und Beschluesse.
- DATEV-Programm-Updates (jaehrlich zum 1. Januar; DATEV LODAS → Stamm → Lohnsteuer / Beitragssaetze).
- Aktuelle Mindestlohn-Verordnung 2026 zwingend nachschlagen — Mindestlohnkommission tagt im Zwei-Jahres-Rhythmus (juenste Empfehlung typisch im Sommer des Vorjahres).

### Phase 3 — Wirkung auf Mandantenbetriebe

- Stundenloehne unter MiLo: sofort anzupassen.
- Minijob-Grenze: dynamisch erhoeht.
- Midi-Job-Untergrenze: dynamisch erhoeht.
- Aufzeichnungspflicht § 17 MiLoG: weiterhin Pflicht.

### Phase 4 — Branchen-Mindestloehne

- In manchen Branchen tariflich hoehere Mindestloehne (z.B. Pflege, Bau).
- Brancheninspezifische Verordnungen (z.B. Mindestlohn fuer Pflege).
- AG der Branche muss tariflichen Wert zahlen.

### Phase 5 — Mandantenkommunikation

- Bei jedem MiLo-Update Mandanten-Rundbrief.
- Konkrete Auswirkung auf Mandantenbetrieb berechnen.
- Empfehlung: Stundenloehne anpassen, Mini-/Midi-Grenzen pruefen.

### Phase 6 — Risiken bei Nicht-Einhaltung

- Bussgeld bis 500.000 EUR (§ 21 MiLoG).
- Schwarzarbeit-Verdacht.
- AN-Klage auf Lohndifferenz (§ 612a BGB).

## Output

- Aktuelle MiLo-Uebersicht.
- Mandanten-Information bei Aenderung.
- Aktualisierte DATEV-Stammdaten.

## Strategie und Praxis-Tipps

- MiLo-Updates jaehrlich zum 1. Januar zwingend einspielen.
- Bei wesentlichen Anhebungen Mandanten proaktiv informieren.
- Minijob-Grenze automatisch mit MiLo-Anhebung — Mandanten zu Sondervergueteungen beraten.
- Bei tariflich gebundenen Branchen tarifvertraglichen Mindestlohn pruefen.
- StBVV: Information ueber Anpassungen in Mandantenkommunikations-Pauschale.
- DATEV-Tipp: DATEV-Update mit neuem MiLo zum 1. Januar einspielen.

## Querverweise

- `stb-lohn-mini-midi-grenzen-2026-stand` — Mini-/Midi-Grenzen.
- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-aufzeichnungspflichten-milog` — MiLoG.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- MiLoG §§ 1, 4, 5, 21.
- Bundesgesetzblatt mit MiLo-Verordnungen.
- Mindestlohnkommission.
- Mindestlohn 2025: 12,82 EUR/h (MiLoV4); 2026: 13,90 EUR/h; 2027: 14,60 EUR/h (Fuenfte Mindestlohnanpassungsverordnung MiLoV5 vom 05.11.2025, BGBl. 2025 I Nr. 268; Berichtigung BGBl. 2025 I Nr. 312). Empfehlung Mindestlohnkommission vom 27.06.2025. Volltext der MiLoV5: recht.bund.de/bgbl/1/2025/268/VO.html.

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 3 bestaetigt (MiLoV3 BGBl. 2023 I Nr. 321, 12,82 EUR eingesetzt), 1 ersetzt (2026-Wert als noch nicht festgesetzt ausgewiesen) -->
<!-- UPDATE 29.05.2026 | MiLoV5: 13,90 EUR (2026) und 14,60 EUR (2027) bestaetigt, BGBl. 2025 I Nr. 268/312 -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-lohn-mini-midi-grenzen-2026-stand`

**Fokus:** Aktuelle Mini- und Midi-Job-Grenzen 2026. Anwendungsfall Prüfung aktueller Schwellenwerte für Geringfuegigkeit und Übergangsbereich Verifikation gegen Mindestlohn-Anpassungen. Methodik Werteprüfung Quellen amtliche Veröffentlichungen. Output Schwellenwert-Übersicht mit Stichtag und Verifikations-Hinweis.

# Mini- und Midi-Grenzen — Stand 2026

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mini- und Midi-Grenzen — Stand 2026` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Schwellenwerte fuer geringfuegige Beschaeftigung (Minijob) und Uebergangsbereich (Midi-Job) sind seit 01.10.2022 dynamisch an den Mindestlohn gekoppelt: Minijob-Grenze = 130-faches des Mindestlohnstundenlohns (~10 Wochenstunden). Bei jeder MiLo-Anhebung steigt die Minijob-Grenze. Der Steuerberater muss zu jedem Stichtag pruefen, welcher Wert aktuell gilt — Dokumentation in der Mandantenakte ist Pflicht.

## Kaltstart-Rueckfragen

1. Welcher Stichtag wird betrachtet (Monatslohn-Zeitraum)?
2. Welcher Mindestlohn-Wert ist amtlich fuer den Zeitraum?
3. Liegt die Minijob-Grenze auf Basis der MiLo-Berechnung vor?
4. Wann erfolgt die naechste MiLo-Anpassung (Mindestlohnkommission, Bundesregierung)?
5. Welche Mandanten haben Minijobs in Grenzregion?
6. Sind Mandanten ueber Anpassungs-Termin informiert?
7. Liegen DATEV-Updates ein?
8. Welche Sondervergueteungen verschieben Jahres-Durchschnitt?

## Rechtlicher Rahmen

### Primaernormen

**§ 8 SGB IV** — geringfuegige Beschaeftigung, dynamisch an MiLo.

**§ 20 SGB IV** — Uebergangsbereich.

**MiLoG** — Mindestlohngesetz.

**§ 1 MiLoG** — Mindestlohn-Hoehe.

**§ 4 MiLoG** — Anpassung durch Mindestlohnkommission / Verordnung.

### Verwaltungsanweisungen

- Mindestlohnkommission Empfehlungen.
- Bundesgesetzblatt Verkuendungen.
- Spitzenverbaende-Rundschreiben.

## Workflow

### Phase 1 — MiLo-Historie und 2026

| Stichtag | Mindestlohn EUR/Stunde | Minijob-Grenze EUR/Monat |
|---|---|---|
| 01.10.2022 | 12,00 | 520 |
| 01.01.2024 | 12,41 | 538 |
| 01.01.2025 | 12,82 | 556 |
| 01.01.2026 | 13,90 (MiLoV5 v. 05.11.2025, BGBl. 2025 I Nr. 268; Berichtigung Nr. 312) | 603 (= 13,90 × 130 / 3 = 602,33, kfm. gerundet 603; Minijob-Zentrale) |
| 01.01.2027 | 14,60 (MiLoV5, gleiche Verordnung) | 633 (= 14,60 × 130 / 3 = 632,67, kfm. gerundet 633; gegenpruefen bei Minijob-Zentrale) |

(Werte jaehrlich pruefen — Bundesgesetzblatt, Mindestlohnkommission, Minijob-Zentrale, DATEV-Updates.)

### Phase 2 — Berechnungsformel

- § 8 Abs. 1a SGB IV: Minijob-Grenze = Mindestlohn x 130 / 3, kaufmaennisch gerundet auf volle EUR (Hintergrund: 10 Wochenstunden in Bezug auf 4,33 Wochen/Monat; die Formel des § 8 Abs. 1a SGB IV verwendet 130 als drittelte Quartalsbasis).
- Bei MiLo 12,41 EUR: 12,41 x 130 / 3 = 537,77 — Rundung auf 538 EUR.
- Bei MiLo 12,82 EUR (2025): 12,82 x 130 / 3 = 556,20 — Rundung auf 556 EUR (Minijob-Grenze 2025).
- Bei MiLo 13,90 EUR (2026): 13,90 x 130 / 3 = 602,33 — Rundung auf 603 EUR (Minijob-Grenze 2026; bestaetigt durch Minijob-Zentrale; Jahresgrenze 7.236 EUR).
- Bei MiLo 14,60 EUR (2027): 14,60 x 130 / 3 = 632,67 — Rundung voraussichtlich auf 633 EUR (Pruefung Minijob-Zentrale empfohlen).

### Phase 3 — Uebergangsbereich

- Untergrenze = Minijob-Grenze + 0,01 EUR.
- Obergrenze: 2.000 EUR (Stand 01.01.2023).
- Bei Reformen 2026 Obergrenze ueberpruefen — bisher unveraendert seit 2023.

### Phase 4 — Mandanten-Information

- Bei jeder MiLo-Anhebung Mandanten mit Minijobs informieren.
- Bei drohenden Grenzueberschreitungen rechtzeitig auf Stundenreduktion oder Lohnerhoehung hinweisen.
- Schriftliche Mandanteninformation als Standard-Schreiben.

### Phase 5 — DATEV-Update

- DATEV LODAS / Lohn und Gehalt liefert mit Update zum 1. Januar neue Werte.
- Manuell pruefen, ob Update eingespielt.
- Bei abweichendem Wirtschaftsjahr: Stichtag des MiLo-Datums beachten.

### Phase 6 — Dokumentation

- Schwellenwert-Tabelle in StB-Wissens-Datenbank fuehren.
- Bei Mandantengespraech aktuellen Wert benennen, nicht den allgemein bekannten alten Wert.
- Verifikations-Hinweis im Schreiben oder Bericht.

## Output

- Schwellenwert-Uebersicht aktuell (Mindestlohn, Minijob-Grenze, Uebergangsbereich-Grenzen).
- Mandanten-Informationsschreiben bei Aenderung.
- Aktualisierte DATEV-Stammdaten.

## Strategie und Praxis-Tipps

- Mandanten mit Minijobs sind besonders empfindlich gegenueber MiLo-Erhoehungen — proaktive Beratung.
- Bei drohendem Ueberschreiten Stundenreduktion empfehlen ODER Wechsel in regulaeres Arbeitsverhaeltnis (mit voller SV-Pflicht).
- Mindestlohn-Verstoss: § 21 MiLoG Bussgeld bis 500.000 EUR.
- Bei wesentlicher MiLo-Anhebung Anpassung der Stundenloehne im Mandantenbetrieb pruefen.
- StBVV: Informationsschreiben in Mandantenkommunikations-Pauschale oder Zusatzauftrag.
- DATEV-Tipp: DATEV-Update jaehrlich zum 1. Januar zwingend einspielen.

## Querverweise

- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-midi-job-uebergangsbereich-2000-euro` — Midi-Job.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-aufzeichnungspflichten-milog` — MiLoG-Pflichten.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 8, 20.
- MiLoG §§ 1, 4, 21.
- Bundesgesetzblatt mit Mindestlohn-Verordnungen.
- Mindestlohnkommission.
- Mindestlohn 2025: 12,82 EUR/h; Minijob-Grenze 2025: 556 EUR/Monat. **Mindestlohn 2026: 13,90 EUR/h; Minijob-Grenze 2026: 603 EUR/Monat (Jahresgrenze 7.236 EUR). Mindestlohn 2027: 14,60 EUR/h; Minijob-Grenze 2027 voraussichtlich 633 EUR/Monat.** Quelle: Fuenfte Mindestlohnanpassungsverordnung (MiLoV5) vom 05.11.2025, BGBl. 2025 I Nr. 268 (Berichtigung Nr. 312); Minijob-Zentrale Pressemitteilung Dezember 2025.

<!-- AUDIT 27.05.2026 | welle 6 | 5 Marker aufgeloest: 4 bestaetigt (MiLo 12,82 EUR/Minijob 556 EUR 2025 eingesetzt), 1 ersetzt (Rundungspraxis Pruefhinweis ohne Marker) -->
<!-- UPDATE 29.05.2026 | MiLoV5: MiLo 13,90 (2026) / 14,60 (2027); Minijob-Grenze 603 (2026) / voraussichtlich 633 (2027) ergaenzt -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-lohn-monatsende-meldepflichten-checkliste`

**Fokus:** Lohn-Meldepflichten zum Monatsende Checkliste LSt-Anmeldung SV-Beitragsnachweis DEUEV BG-Lohnnachweis. Anwendungsfall standardisierter Prüfablauf vor Monatsende und Fristen Auswertung. Methodik Prüfliste Termincontrolling. Output Erledigungs-Liste.

# Monatsende-Meldepflichten Lohn — Checkliste

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Monatsende-Meldepflichten Lohn — Checkliste` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zum Monatsende fallen mehrere Meldepflichten gleichzeitig an: LSt-Anmeldung beim FA (10. des Folgemonats), SV-Beitragsnachweis und -zahlung (drittletzter Bankarbeitstag), DEUEV-Meldungen (laufend), BG-Beitrag (jaehrlich), Statistik (jaehrlich). Der Steuerberater nutzt eine standardisierte Checkliste, um nichts zu vergessen.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Mitarbeiterzahl, Branche?
2. Welcher Anmeldungszeitraum LSt (monatlich, vierteljaehrlich, jaehrlich)?
3. Welche Krankenkassen sind vertreten?
4. Welche BG ist zustaendig?
5. Wann ist letzter Lauf erfolgt?
6. Welche Sondermeldungen ausstehend (Anmeldungen, Abmeldungen)?
7. Liegen alle ELStAM-Daten vor?
8. Welche Fristen sind kritisch (Eile bei der Naechsten)?

## Rechtlicher Rahmen

### Primaernormen

**§ 41a EStG** — LSt-Anmeldung Frist 10. des Folgemonats.

**§ 23 Abs. 1 SGB IV** — SV-Beitragsfaelligkeit drittletzter Bankarbeitstag des laufenden Monats (voraussichtliche Schuld); Korrektur ueber Beitragsnachweis bis 15. des Folgemonats.

**§ 28a SGB IV** — DEUEV-Meldungen.

**§ 165 SGB VII** — BG-Lohnnachweis Februar Folgejahr.

**§ 240 AO** — Saeumniszuschlag.

**§ 152 AO** — Verspaetungszuschlag.

## Workflow

### Phase 1 — Standardcheckliste Monatsende

```
MONATSENDE-CHECKLISTE LOHN
Monat: [Monat / Jahr]
Mandant: [Firma]

[ ] Alle Lohnabrechnungen erstellt
[ ] ELStAM aktuell abgerufen
[ ] Anmeldungen/Abmeldungen DEUEV erfolgt
[ ] LSt-Anmeldung erstellt
[ ] LSt-Anmeldung an FA gesendet (vor 10. Folgemonat)
[ ] LSt-Zahlung an FA angewiesen
[ ] SV-Beitragsnachweis erstellt
[ ] SV-Beitraege an Krankenkassen ueberwiesen (drittletzter Bankarbeitstag)
[ ] Pauschalsteuer Minijob an Knappschaft
[ ] Pauschalsteuer Sachzuwendungen § 37b EStG
[ ] U1/U2-Erstattungsantraege (bei Krankheit)
[ ] BG-Vorauszahlung (falls monatliche Abschlagszahlung)
[ ] Buchung im Hauptbuch erfolgt
[ ] Mandantenakte aktualisiert
```

### Phase 2 — LSt-Anmeldung

- Frist: 10. des Folgemonats.
- Form: ELSTER elektronisch.
- Inhalt: Bruttoloehne, LSt, KiSt, SolZ, Pauschalsteuer.
- Bei Verspaetung: Verspaetungszuschlag § 152 AO.

### Phase 3 — SV-Beitragsnachweis und Zahlung

- Faelligkeit: drittletzter Bankarbeitstag des laufenden Monats.
- SV-Beitragsnachweis ueber sv.net oder DAKOTA an Krankenkassen.
- Zahlung an jede Krankenkasse einzeln.
- Bei Verspaetung: 1 Prozent Saeumniszuschlag pro Monat.

### Phase 4 — DEUEV-Meldungen

- Anmeldungen, Abmeldungen, Aenderungen.
- Im Standard mit naechster Lohnabrechnung; spaetestens 6 Wochen.
- Sofortmeldungspflicht-Branchen vor Beschaeftigungsbeginn.

### Phase 5 — Pauschalsteuer

- Minijob Pauschal 2 Prozent: an Minijob-Zentrale (Knappschaft).
- Sachzuwendung § 37b EStG: an FA.
- Sondererfassung in Lohnsystem.

### Phase 6 — Sonderpflichten

- U1/U2-Erstattungsantraege bei Krankheit/Mutterschaft an Krankenkasse.
- BG-Vorauszahlung jaehrlich oder Vorauszahlung in monatlichen Raten.
- Jahresmeldungen (siehe stb-lohn-jahresmeldungen-ahn-asn-besondere).

## Output

- Erledigungs-Liste mit Hakerl.
- LSt-Quittung ELSTER.
- SV-Beitragsnachweis-Quittungen.
- Beleg-Datei in Mandantenakte.

## Strategie und Praxis-Tipps

- Checkliste konsequent durchgehen — fehlende Pflicht kostet Bussgeld oder Saeumniszuschlag.
- Fristen-Kalender in DATEV-Kanzleiplaner.
- Bei Verspaetung der drittletzten Bankarbeitstag-Zahlung: 1 Prozent Saeumniszuschlag — bei wiederholten Verspaetungen § 266a StGB-Risiko.
- 10. des Folgemonats LSt: harte Frist, sonst Verspaetungszuschlag.
- StBVV: alle Standardpflichten in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS Erledigungs-Center mit automatischen Erinnerungen.

## Querverweise

- `stb-lohn-lohnsteuer-anmeldung-elster` — LSt-Anmeldung.
- `stb-lohn-sv-meldungen-dakota-svnet` — sv.net.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-jahresmeldungen-ahn-asn-besondere` — Jahresmeldungen.
- `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` — BG.

## Quellen und Updates

Stand: 05/2026.

- EStG § 41a.
- SGB IV §§ 23, 28a.
- SGB VII § 165.
- AO §§ 152, 240.
- StGB § 266a.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-lohn-praktikanten-azubis-loehne`

**Fokus:** Praktikanten und Azubis lohnrelevante Sonderregeln. Anwendungsfall Pflichtpraktikum freiwilliges Praktikum Berufsausbildung BBiG Berufsausbildungsbeihilfe SV-Behandlung Vergueteung. Methodik Unterscheidung Pflicht- vs freiwilliges Praktikum Schwellen. Output Lohn-Abrechnung mit korrekter SV-Klassifikation.

# Praktikanten und Azubis — lohnrelevante Sonderregeln

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Praktikanten und Azubis — lohnrelevante Sonderregeln` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Praktika und Berufsausbildung haben besondere lohn- und sv-rechtliche Behandlung. Unterscheidung: Pflichtpraktikum (waehrend Studium/Schule vorgeschrieben), freiwilliges Praktikum, Berufsausbildung nach BBiG, dualer Studiengang. Vergueteung und SV-Pflicht variieren. Mindestlohn-Pflicht eingeschraenkt anwendbar.

## Kaltstart-Rueckfragen

1. Praktikum als Pflichtpraktikum (Schul- oder Studienordnung)?
2. Freiwilliges Praktikum vor/nach/waehrend Studium?
3. Dauer Praktikum (< oder > 3 Monate)?
4. Berufsausbildung nach BBiG mit Vertrag und IHK/lizenzpflichtige Literaturquelle-Eintrag?
5. Dualer Studiengang (Theorie+Praxis kombiniert)?
6. Vergueteung pro Monat?
7. Wohnt der Auszubildende im Haushalt des AG (Sachbezuege)?
8. Welcher tarifliche Mindestlohn Ausbildung gilt?

## Rechtlicher Rahmen

### Primaernormen

**§ 22 MiLoG** — Ausnahmen Mindestlohn (Pflichtpraktikum, freiwilliges Praktikum < 3 Monate, Berufsausbildung).

**§ 17 BBiG** — Vergueteung Berufsausbildung (Angemessenheit).

**§ 19 BBiG** — Sachleistungen.

**§ 26 SGB III** — Berufsausbildungsbeihilfe.

**§ 1 LStDV** — Anwendungsbereich.

**SGB IV** — SV.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK zur SV-Behandlung Praktikanten.
- BMF zu Sachbezuegen.

## Workflow

### Phase 1 — Klassifizierung

| Art | MiLoG | SV | Vergueteung |
|---|---|---|---|
| Pflichtpraktikum waehrend Studium/Schule | Ausnahme | Beitragsfrei in KV/PV/AV; RV-Pflicht bei Vergueteung | Tariflich oder vereinbart |
| Freiwilliges Praktikum < 3 Monate | Ausnahme | Beitragsfrei wenn Studium fortbesteht | Vereinbarung |
| Freiwilliges Praktikum > 3 Monate | MiLoG-Pflicht | Wie regulaer | Mindestens MiLo |
| Vorpraktikum vor Studium | MiLoG-Pflicht (ueber 3 Monate) | SV-pflichtig | Mindestens MiLo |
| Berufsausbildung BBiG | MiLoG-Ausnahme; gesetzliche Mindest-Ausbildungsverguetung | Voll SV-pflichtig (RV/KV/PV/AV) | Mindest-Ausbildungsverguetung |
| Duales Studium | MiLoG-Ausnahme | SV-pflichtig | Vereinbarung |

### Phase 2 — Mindest-Ausbildungsverguetung Berufsausbildung

- § 17 Abs. 2 BBiG: Mindest-Ausbildungsverguetung jaehrlich angepasst (BMBF-Verordnung).
- Mindest-Ausbildungsverguetung 2025: 682 EUR/Monat im 1. Ausbildungsjahr (§ 17 Abs. 2 Nr. 1 BBiG; Wert 2026 ueber BMBF-Verordnung pruefen).
- Bei Tarifvertrag: tariflicher Wert gilt (ueblicherweise hoeher).

### Phase 3 — SV-Behandlung

- Pflichtpraktikum: in der Regel beitragsfrei in KV/PV/AV; RV nur bei vereinbarter Vergueteung.
- Freiwilliges Praktikum < 3 Monate: wie Pflichtpraktikum.
- Freiwilliges Praktikum > 3 Monate: wie regulaeres Arbeitsverhaeltnis.
- Berufsausbildung: voll SV-pflichtig in allen Zweigen. Bei geringer Ausbildungsverguetung unterhalb der Geringverdienergrenze (§ 20 Abs. 3 SGB IV; Stand 2025: 325 EUR/Monat — ueber Spitzenverbaende-Rundschreiben pruefen) traegt der AG den gesamten SV-Beitrag (AG- und AN-Anteil); oberhalb der Grenze normale paritaetische Aufteilung.

### Phase 4 — Sachleistungen Berufsausbildung

- Kost und Logis koennen Teil der Ausbildungsverguetung sein.
- § 19 BBiG: Sachbezugsanrechnung bis 75 Prozent der Verguetung.
- Bewertung nach SvEV-Sachbezugswerten.

### Phase 5 — Steuerliche Behandlung

- Vergueteung ist LSt-pflichtig.
- ELStAM-Abruf wie regulaer AN.
- Bei Praktikum mit geringer Vergueteung oft Lohnsteuer null (Steuerklasse 1, Grundfreibetrag).

### Phase 6 — Dokumentation

- Schul-/Studienbescheinigung mit Pflichtpraktikums-Nachweis.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Mandantenakte mit allen Unterlagen.

## Output

- Lohn-Abrechnung mit korrekter SV-Klassifikation.
- Personengruppen-Schluessel (102 fuer Azubi, 105 fuer Praktikant Pflicht, 109 fuer Praktikant freiwillig kurz).
- Dokumentation Pflichtpraktikums-Nachweis.

## Strategie und Praxis-Tipps

- Pflichtpraktikum streng durch Studienordnung verlangt — nicht jedes Praktikum waehrend Studium.
- Bei Mehrfachpraktikum (mehrere kurze Phasen) Gesamtdauer beobachten.
- Berufsausbildung Mindest-Verguetung jaehrlich anpassen (BMBF-VO).
- Bei Sachbezuegen Anrechnung dokumentieren — sonst Lohnsteuer-Risiko.
- StBVV: Praktikanten/Azubis in Lohnpauschale; komplexe Sonderfaelle Zeithonorar.
- DATEV-Tipp: DATEV LODAS Personengruppen-Schluessel beachten; Plausibilitaetspruefung.

## Querverweise

- `stb-lohn-werkstudent-pauschalen` — Werkstudent.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezuege.

## Quellen und Updates

Stand: 05/2026.

- MiLoG § 22.
- BBiG §§ 17, 19.
- SGB III § 26; SGB IV; SGB V.
- LStDV.
- Mindest-Ausbildungsverguetung 2025: 682 EUR/Monat im 1. Ausbildungsjahr (§ 17 Abs. 2 BBiG; Wert 2026 ueber BMBF pruefen).
- SvEV-Sachbezugswerte jaehrlich angepasst (Stand 2025: Verpflegung 313 EUR/Monat; ueber BMAS pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (Mindest-Ausbildungsverguetung 2025 682 EUR eingesetzt), 1 ersetzt (Geringverdienergrenze Pruefhinweis ohne Marker) -->

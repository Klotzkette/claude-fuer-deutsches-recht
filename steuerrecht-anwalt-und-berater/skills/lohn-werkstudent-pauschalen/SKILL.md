---
name: lohn-werkstudent-pauschalen
description: "Werkstudent SV-Status 20-Stunden-Grenze pauschale Beitraege. Anwendungsfall Beschäftigung Student Werkstudentenprivileg KV-Befreiung RV-Pflicht JAEG nicht relevant Klassifizierung. Methodik Prüfung 20-Stunden-Woche vorlesungsfreie Zeit Antrag KV-Befreiung. Output Werkstudenten-Abrechnung."
---

# Werkstudent — SV-Status und Pauschalen

## Fachlicher Anker

- **Normen:** § 6a, § 6 Abs. 1 Nr. 3 SGB V, § 27 Abs. 4 SGB III.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Werkstudenten sind ordentlich immatrikulierte Studierende, die im Nebenerwerb arbeiten. Sie sind in der KV/PV/AV beitragsfrei (Werkstudentenprivileg), aber RV-pflichtig. Voraussetzung: max. 20 Wochenstunden waehrend der Vorlesungszeit; in der vorlesungsfreien Zeit auch mehr. Prüfung sorgfaeltig — bei Verlust des Werkstudent-Status nachtraegliche SV-Beitragspflicht.

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
- Hochschulgesetz der Länder.

## Workflow

### Phase 1 — Werkstudent-Status prüfen

| Kriterium | Erfuellt? |
|---|---|
| Ordentliche Immatrikulation an Hochschule | Ja / Nein |
| Master noch nicht abgeschlossen | Ja / Nein |
| Studienschwerpunkt erkennbar (kein Schein-Studium) | Ja / Nein |
| Max 20 Wochenstunden in Vorlesungszeit | Ja / Nein |
| Bezug zu Studium (entbehrlich, aber hilfreich) | Ja / Nein |

### Phase 2 — Arbeitszeitpruefung

- Vorlesungszeit: max. 20 Wochenstunden.
- Vorlesungsfreie Zeit (Semesterferien): mehr als 20 Stunden möglich.
- Mehrfach-Werkstudent: Summe der Stunden über alle AG ist massgeblich.
- 26-Wochen-Regel: Eine Ueberschreitung der 20-Wochen-Stunden-Grenze bleibt unschaedlich, wenn sie ueberwiegend in vorlesungsfreien Zeitraeumen liegt und im 52-Wochen-Zeitraum nicht mehr als 26 Wochen umfasst (st. Spitzenverbands-Rundschreiben; bei Änderung der DEUEV-Grundsaetze prüfen).
- Bei dauerhafter Ueberschreitung der 20 Wochenstunden in der Vorlesungszeit: Werkstudenten-Status weg, voll SV-pflichtig.

### Phase 3 — SV-Beitraege

| Zweig | Werkstudent |
|---|---|
| KV | Beitragsfrei aus der Beschäftigung; eigene KV-Pflicht über Familienversicherung (bis Vollendung 25. Lj., § 10 SGB V) oder studentische KV (§ 5 Abs. 1 Nr. 9 SGB V) |
| PV | Beitragsfrei |
| AV | Beitragsfrei |
| RV | Pflicht (voller Beitrag; im Uebergangsbereich nach § 20 Abs. 2 SGB IV gemindert, sofern Brutto in den Midi-Job-Bereich faellt) |

**Zahlenbeispiel:** Werkstudent mit Brutto 900 EUR/Monat (im Uebergangsbereich). RV-AG 9,3 Prozent von 900 EUR = 83,70 EUR; AN-Anteil im Uebergangsbereich gemindert (Faktor F — vgl. `stb-lohn-midi-job-uebergangsbereich-2000-euro`). KV/PV/AV null. LSt nach Steuerklasse (typisch StKl 1, im Regelfall keine LSt unterhalb Grundfreibetrag).

### Phase 4 — Anmeldung und Prüfung

- Immatrikulationsbescheinigung jaehrlich aktualisieren (am besten zu Semesterbeginn).
- SV-Anmeldung mit Personengruppen-Schlüssel 106 (Werkstudent; DEUEV-Schlüsselverzeichnis ITSG Stand 2025, unveraendert; bei DEUEV-Änderung ITSG-Schlüsselverzeichnis prüfen).
- Bei Verlust Werkstudent-Status: Personengruppen-Schlüssel auf 101 (regulaer) wechseln; Beitragsgruppen-Schlüssel anpassen.

### Phase 5 — Sonderfaelle

- Promovierende: kein Werkstudent (Master abgeschlossen). Ausnahme: vergebene Doktoranden-Stipendien.
- Teilzeitstudenten: Werkstudent-Status zweifelhaft; Einzelfallpruefung.
- Sprach- und Aufbaustudiengaenge: in der Regel Werkstudent.
- Auslandsstudierende: bei deutscher Sozialversicherungspflicht (z.B. EU-Buerger mit deutscher Wohnung) Werkstudent möglich.

### Phase 6 — Dokumentation

- Immatrikulationsbescheinigung jaehrlich in Mandantenakte.
- Stundenaufzeichnung MiLoG.
- Lohnabrechnung mit Personengruppen 106.

## Strategie und Praxis-Tipps

- 20-Stunden-Regel strikt — bei systematischem Ueberschreiten Status verloren.
- Bei Ueberschreitung waehrend Semesterferien akzeptabel; in Vorlesungszeit kritisch.
- Bei Wechsel Master in Promotion: Status faellt weg, Umstellung Personengruppen-Schlüssel.
- Bei Studienabschluss waehrend Beschäftigung: Status faellt zum Tag des Abschlusses weg.
- StBVV: in Lohnpauschale; Statuspruefung bei Sonderfaellen Zeithonorar.
- DATEV-Tipp: DATEV LODAS Werkstudent-Personengruppe automatisch; Immatrikulations-Wiedervorlage zu Semesterbeginn.

## Quellen und Updates

Stand: 05/2026.

- SGB V §§ 5, 6.
- SGB III § 27.
- SGB VI.
- BAfoeG § 16.
- Gemeinsame Rundschreiben Spitzenverbaende KK.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (DEUEV-Schlüssel 106 unveraendert), 1 ersetzt (26-Wochen-Regel Prüfhinweis ohne Marker) -->

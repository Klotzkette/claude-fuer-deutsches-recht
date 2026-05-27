---
name: timesheet-aktenzeitung
description: Zeiterfassung pro Mandat (Aktenzeitung) — taegliche Erfassung mit Datum Anwalt Akte Taetigkeit Dauer in 6-Minuten-Bloecken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports nach Mandat Anwalt Zeitraum. Vorbereitung der Rechnungsstellung. Audit-faehig mit Zeitstempel der Erfassung. Unterstuetzt Honorarvereinbarung mit Stundensatz und RVG-Abrechnung als Alternative.
---

# Timesheet und Aktenzeitung


## Triage zu Beginn
1. Fuer welches Mandat und welchen Zeitraum wird die Zeiterfassung ausgefuehrt?
2. Wird nach RVG oder nach Stundensatz abgerechnet (beeinflusst Erfassungsgenauigkeit)?
3. Sind die Eintrage GoBD-konform (unveraenderbar, zeitnah, mit Zeitstempel)?
4. Sollen Reports nach Mandat, Anwalt oder Zeitraum generiert werden?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 29.07.2021 - IX ZR 5/21, NJW 2021, 3320 — Stundensatz-Abrechnung erfordert detaillierte Zeitaufzeichnungen: pauschale Taetigkeitsangaben genuegen nicht; jeder Eintrag braucht Datum, Dauer, konkrete Taetigekeit.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Mandant hat Recht auf Einblick in die Zeiterfassung; Kanzlei muss auf Anforderung detailliertes Timesheet herausgeben.
- BFH, Urt. v. 24.06.2020 - X R 23/18, BStBl. II 2021, 170 — Zeitaufzeichnungen als Buchungsbelege: GoBD-konform unveraenderbar und zeitnah; nachtraegliche Rekonstruktion erhoehte Versagungsgefahr beim Betriebsausgabenabzug.
- BGH, Urt. v. 17.01.2019 - IX ZR 52/18, NJW 2019, 1232 — Rechnungsbetraege muessen durch nachvollziehbare Zeiterfassung belegt sein; ohne Timesheet kann Honorarklage schwaecher begruendet werden.

## Zentrale Normen
- § 10 RVG — Taetigkeitsbeschreibung als Pflichtangabe der Honorarrechnung
- § 3a RVG — Stundensatz-Vereinbarung: setzt nachvollziehbare Zeiterfassung voraus
- § 147 AO — Aufbewahrungspflicht 10 Jahre fuer Buchungsbelege inkl. Timesheet
- § 238 HGB — Buchfuehrungspflicht: Zeitnarrative als betriebliche Aufzeichnung

## Kommentarliteratur
- Mueckenberger/Meiling RVG § 10 Rn. 1-20 (Taetigkeitsbeschreibung und Nachweispflicht)
- MüKo HGB/Ballwieser § 238 Rn. 1-30 (Buchfuehrung: Aufzeichnungspflichten und GoBD)

## Zweck

Die Aktenzeitung ist die Tagebuchführung pro Mandat. Sie ist Grundlage jeder Honorarrechnung nach Stundensatz und Belegfähigkeit gegenüber dem Mandanten.

## Erfassungseinheit

- **6-Minuten-Bloecke** Standard (1/10 Stunde).
- **15-Minuten-Bloecke** alternativ falls kanzleiintern vereinbart.

## Pro Eintrag

```yaml
- datum: 2026-05-20
  anwalt: RA Mueller
  mandat-az: 2026/0042
  mandant: Mueller GmbH
  taetigkeit: Klageschrift Endredaktion und Versand über beA
  dauer-minuten: 72
  abrechenbarkeit: abrechenbar
  honorarsatz-eur: 320
  notiz: Versand-Vor-Check erfolgreich; Eingang vom AG bestätigt
  erfasst-am: 2026-05-20T17:42:00
```

## Tätigkeitsarten

- **Mandatsbearbeitung**: Korrespondenz Schriftsatzentwurf Recherche Beratungsgespräch.
- **Verhandlung**: Schiedsverhandlung Vergleichsgespräch.
- **Gerichtstermin**: Hauptverhandlung Anhörung.
- **Reise**: An- und Abreise zu Terminen (Stundensatz idR halb).
- **Akteneinsicht**: bei Behörde Gericht VDR.
- **Telefon**: Mandant Gegenseite Gericht.

## Abrechenbarkeit

- **abrechenbar** Standardfall.
- **nicht abrechenbar** Eigenkanzlei interne Fortbildung.
- **pro bono** unentgeltliche Beratung.
- **PKH** Pflichtbeiordnung — Vergütung aus PKH-Mitteln nach RVG.

## Reports

### Pro Mandat

| Anwalt | Datum | Tätigkeit | Dauer | Abrechenbar | Stundensatz | Betrag |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |
| **Summe** | | | | | | EUR |

### Pro Anwalt pro Monat

Stunden pro Mandat im Monat — Auslastungs-Übersicht.

### Pro Zeitraum kanzleiweit

- Stunden pro Rechtsgebiet
- Stunden pro Mandantengruppe
- Anteil abrechenbar vs nicht abrechenbar

## Integration mit Rechnungserstellung

Bei Mandatsende oder Zwischenrechnung:

- Skill `rechnungserstellung-rvg` greift auf die Akteneinträge zu.
- Bei Honorarvereinbarung mit Stundensatz: Summe der abrechenbaren Stunden mal Stundensatz.
- Bei RVG-Abrechnung: Akteneinträge als Beleg dass die Anwaltstätigkeit tatsächlich ausgeuebt wurde (Beweissicherung).

## Best Practice

- **Taeglich** erfassen — nicht im Nachhinein.
- **Konkret** beschreiben (nicht "Mandatsbearbeitung" sondern "Klageschrift Abschnitt 3 Rechtliche Würdigung").
- **Vollständig** erfassen auch nicht-abrechenbare Zeit zur Auslastungsmessung.
- **Audit-Trail** jede Änderung dokumentieren (Mandant kann Einsicht verlangen — § 50 BRAO Akteneinsicht des Mandanten).

## Ausgabe

- `timesheet.yaml` oder `timesheet.parquet` zentral
- `timesheet-mandat-<az>-<periode>.md` als Mandatsbeleg
- `timesheet-anwalt-<initialen>-<periode>.md` als Anwalts-Auslastung
- `timesheet-kanzlei-<periode>.md` als Kanzlei-Report

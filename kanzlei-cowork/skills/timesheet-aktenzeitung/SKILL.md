---
name: timesheet-aktenzeitung
description: Zeiterfassung pro Mandat (Aktenzeitung) — taegliche Erfassung mit Datum Anwalt Akte Taetigkeit Dauer in 6-Minuten-Bloecken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports nach Mandat Anwalt Zeitraum. Vorbereitung der Rechnungsstellung. Audit-faehig mit Zeitstempel der Erfassung. Unterstuetzt Honorarvereinbarung mit Stundensatz und RVG-Abrechnung als Alternative.
---

# Timesheet und Aktenzeitung

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

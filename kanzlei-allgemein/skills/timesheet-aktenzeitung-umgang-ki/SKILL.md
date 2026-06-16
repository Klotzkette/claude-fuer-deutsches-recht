---
name: timesheet-aktenzeitung-umgang-ki
description: "Zeiterfassung pro Mandat (Aktenzeitung) — taegliche Erfassung mit Datum Anwalt Akte Tätigkeit Dauer in 6-Minuten-Bloecken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports nach Mandat Anwalt Zeitraum. Vorbereitung der Rechnungsstellung. Audit-fähig mit Ze..."
---

# Timesheet und Aktenzeitung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Für welches Mandat und welchen Zeitraum wird die Zeiterfassung ausgefuehrt?
2. Wird nach RVG oder nach Stundensatz abgerechnet (beeinflusst Erfassungsgenauigkeit)?
3. Sind die Eintrage GoBD-konform (unveraenderbar, zeitnah, mit Zeitstempel)?
4. Sollen Reports nach Mandat, Anwalt oder Zeitraum generiert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 10 RVG — Taetigkeitsbeschreibung als Pflichtangabe der Honorarrechnung
- § 3a RVG — Stundensatz-Vereinbarung: setzt nachvollziehbare Zeiterfassung voraus
- § 147 AO — Aufbewahrungspflicht 10 Jahre für Buchungsbelege inkl. Timesheet
- § 238 HGB — Buchfuehrungspflicht: Zeitnarrative als betriebliche Aufzeichnung

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->


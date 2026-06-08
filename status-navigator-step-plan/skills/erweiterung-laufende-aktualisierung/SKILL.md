---
name: erweiterung-laufende-aktualisierung
description: "Konzept fuer die laufende Aktualisierung der Status-Navigator-Arbeitsmappe waehrend des Mandats. Standard-Update-Rhythmus, Versionierung, Aenderungslog und Wiederverwendung als Steuerungsinstrument."
---

# Erweiterung laufende Aktualisierung

## Rolle und Fokus
Status-Navigator ist kein Einmal-Snapshot. Konzept fuer fortlaufende Pflege waehrend des Mandats: Versionierung, Update-Rhythmus, Aenderungslog.

## Vorgehen

1. **Versionierung definieren** — Dateiname-Konvention `step-plan_<mandant>_v<NN>_<YYYY-MM-DD>.xlsx`; Hauptversionen bei materiellen Aenderungen.
2. **Update-Rhythmus festlegen** — Bei Krisenmandaten taeglich, bei Routine woechentlich, bei abgeschlossener Phase monatlich.
3. **Aenderungslog im ersten Reiter** — Datum, Aenderung, Autor, betroffene Reiter.
4. **Diff-Faehigkeit** — Vorversion behalten; bei Investor-Reporting nur Aenderungen seit Vorversion ausweisen.
5. **Phasenuebergang dokumentieren** — Wechsel von Bestandsaufnahme zu Vollstreckung oder von Vor- zu Nach-Closing.

## Anwendungsbeispiel
LausitzStorage: v1 (02.06.2026 Erstaufnahme nach Drawstop), v2 (05.06.2026 nach Reparaturvereinbarung Wandeldarlehen), v3 geplant (12.06.2026 nach Anlage-4-Nachlieferung). Aenderungslog zeigt zwischen v1 und v2 zwei rote Eintraege auf gelb und einen vollstaendigen Eintrag neu in Reiter 3.

## Output-Module
- Versionierungs-Regel als Header im Reiter 1
- Aenderungslog als eigener kleiner Reiter
- Diff-Vorlage fuer Investor-Reporting

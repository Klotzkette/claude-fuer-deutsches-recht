---
name: mittelstand-corporate-ma-billing-narratives
description: "Kanzlei erstellt Rechnung für M&A-Mandat und braucht praezise zeitgerechte Leistungsbeschreibungen: Time Narratives Phasenbudgets Workstream-Rechnungen Cap/Success-Fee-Berechnung. Normen RVG §§ 1 ff. BRAO § 49b AO-Steuerrecht. Prüfraster Workstream-Zeiterfassung Phasenzuordnung Korrektur Mandantsfreigabe. Output Narratives-Dokument Workstream-Abrechnung Rechnungsentwurf. Abgrenzung zu mittelstand-ma-erechnung-gobd (GoBD/XRechnung-Format)."
---

# Mittelstandsmandat Billing Narratives

## Zweck

Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Für GoBD, XRechnung und ZUGFeRD liegt der freistehende interne Workflow `mittelstand-ma-erechnung-gobd` im selben Plugin.

## Arbeitsmodus

- Tätigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und prüfbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Prüfpunkte führen.
- Bei Rechnungsreife an `mittelstand-ma-erechnung-gobd` übergeben.

## Rote Schwellen

- Narrative enthält Mandatsgeheimnis unnötig detailliert.
- Budgetwarnung fehlt.
- Leistung ohne Akte/Workstream.
- Rechnungsnummer, Umsatzsteuerlogik oder E-Rechnungsformat unklar.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Übergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- § 43a BRAO — anwaltliche Pflichten: vollstaendige Mandatsfuehrung; Sorgfaltspflichten gelten auch fuer automatisierte Prozesse
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung; gilt auch fuer Organisation und Monitoring
- § 49b BRAO — Honorarvereinbarung: Abrechnungsmodalitaeten muessen transparent und schriftlich vereinbart sein
- §§ 93, 116 AktG; § 43 GmbHG — Business Judgment Rule: Entscheidung auf ausreichender Informationsgrundlage; Dokumentationspflicht

### Leitsaetze
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen automatisierten Ausgaben
- Dokumentation: Datum, Methodik, Human-Check-Protokoll

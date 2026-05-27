---
name: mittelstand-corporate-ma-billing-narratives
description: "Kanzlei erstellt Rechnung fuer M&A-Mandat und braucht praezise zeitgerechte Leistungsbeschreibungen: Time Narratives Phasenbudgets Workstream-Rechnungen Cap/Success-Fee-Berechnung. Normen RVG §§ 1 ff. BRAO § 49b AO-Steuerrecht. Pruefraster Workstream-Zeiterfassung Phasenzuordnung Korrektur Mandantsfreigabe. Output Narratives-Dokument Workstream-Abrechnung Rechnungsentwurf. Abgrenzung zu mittelstand-ma-erechnung-gobd (GoBD/XRechnung-Format)."
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
- BGH, Urt. v. 21.04.1997 - II ZR 175/95, BGHZ 135, 244 — Business Judgment Rule: Geschaeftsfuehrer handelt pflichtgemaess, wenn er bei einer unternehmerischen Entscheidung vernuenftigerweise annehmen durfte, zum Wohl der Gesellschaft zu handeln; Informationsgrundlage muss angemessen sein
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — Beraterhaftung: vollstaendige Information des Mandanten ist Kernpflicht; Luecken koennen Schadensersatz ausloesen

### Kommentarliteratur
- MueKo GmbHG/Fleischer, § 43 Rn. 1-80 (Geschaeftsfuehrerhaftung, Business Judgment Rule)
- Schaub, Arbeitsrechts-Handbuch, § 12 (Mandate, Vollmachten, Honorare)

### Qualitaetssicherung
- Human-in-the-loop bei allen automatisierten Ausgaben
- Dokumentation: Datum, Methodik, Human-Check-Protokoll

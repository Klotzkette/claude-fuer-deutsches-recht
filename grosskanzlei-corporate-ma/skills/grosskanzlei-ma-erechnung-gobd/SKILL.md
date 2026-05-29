---
name: grosskanzlei-ma-erechnung-gobd
description: "Freistehender Billing- GoBD- und E-Rechnungsworkflow für M&A-Mandate: Anwendungsfall Kanzlei muss für M&A-Mandat GoBD-konforme Rechnung XRechnung-XML und ZUGFeRD-Prüfpaket erstellen. § 3a RVG Stundenhonorar, GoBD Aufbewahrung, ZUGFeRD XRechnung Standard. Prüfraster Big-Law-Narrative, Phasenbudget WIP, Caps Success Fees, Auslagen Umsatzsteuer, DATEV-Buchungslogik. Output E-Rechnung-Paket mit XRechnung-XML ZUGFeRD-Prüfbericht und Buchungsnachweis. Abgrenzung zu Billing-Narratives-Skill für plugingebundene Abrechnung."
---

# Freistehender Billing-, GoBD- und E-Rechnungsworkflow

## Zweck

Dieser Skill macht aus Deal-Arbeit abrechenbare, prüfbare und mandantentaugliche Abrechnung. Er verbindet Big-Law-Narratives, Phasenbudget, WIP, Caps, Success Fees, Auslagen, Umsatzsteuer, DATEV-nahe Buchungslogik, XRechnung und ZUGFeRD-Prüfpaket. Alle Billing-, E-Rechnungs- und GoBD-Bausteine liegen in diesem Workflow.

## Arbeitsmodus

1. Tätigkeiten aus Zeiteinträgen, Dokumenten, Calls, Markups und Deliverables erfassen.
2. Narrative kurz, konkret und ohne unnötige Mandatsgeheimnisse formulieren.
3. Jede Leistung Phase, Workstream, Fee Earner, Datum, Dauer, Rate, Rabatt, Budget und Deliverable zuordnen.
4. Rechnungsposten mit Umsatzsteuerlogik, Reverse-Charge-Hinweis, Auslagen und Vorschüssen prüfen.
5. XRechnung-XML als strukturierte Datensatz-Skizze ausgeben; ZUGFeRD als Hybrid-Prüfpaket mit PDF/A-3-Hinweis vorbereiten.
6. GoBD-Protokoll führen: Änderungslog, Rechnungsnummer, Storno, Korrekturrechnung, Belegkette, Exportstatus.

## Ausgabe

- Billing Narrative Ledger.
- Workstream-Rechnungsentwurf mit Budgetabweichungen.
- XRechnung-Datenblock und ZUGFeRD-Checkliste.
- DATEV/FiBu-Exportvorschlag als CSV-kompatible Tabelle.
- GoBD-Prüfprotokoll mit Unveränderbarkeitshinweis und Korrekturpfad.

## Rote Schwellen

- Rechnungsnummer fehlt oder wurde doppelt vergeben.
- Rechnung soll rückdatiert oder ohne Leistungsbezug erzeugt werden.
- Umsatzsteuer, Reverse Charge oder Leistungsort unklar.
- Narrative offenbart unnötig vertrauliche Deal-Informationen.
- E-Rechnung wird als technisch versandfertig behauptet, obwohl XML/PDF/A-3 nicht validiert wurde.

## Vorlagen

- assets/templates/erechnung-gobd-billing.md
- assets/templates/billing-narrative-ledger.md
- assets/templates/ai-use-disclosure-log.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- §§ 238-241a HGB — Buchfuehrungs- und Aufbewahrungspflichten (10 Jahre); GoBD gilt parallel
- §§ 1-9 UStG — Umsatzsteuerrecht: E-Rechnungspflicht ab 2025 (§ 14 Abs. 1 UStG n.F.); XRechnung und ZUGFeRD
- §§ 14-14c UStG — Rechnungsanforderungen; Vorsteuerabzug setzt ordnungsgemaesse Rechnung voraus
- §§ 195, 199 BGB — Verjaehrungsfristen: Fristenkalender muss auch gesetzliche Verjaehrungsfristen erfassen

### Leitsaetze
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
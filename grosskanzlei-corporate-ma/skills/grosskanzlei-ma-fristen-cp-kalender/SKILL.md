---
name: grosskanzlei-ma-fristen-cp-kalender
description: "Freistehender Deal-Fristen- und CP-Kalender fuer M&A-Mandate: Anwendungsfall Fristen aus Signing Closing Q&A Regulatory Register Board und Restrukturierung muessen in einem Kalender zusammengefuehrt werden. SPA Closing Conditions, §§ 35 ff. GWB Kartellfristen, §§ 55 ff. AWV FDI-Fristen. Pruefraster Fristen aus E-Mail SPA Regulatory Filing und Board extrahieren, Duplikate zusammenfuehren, Wiedervorlagedaten setzen. Output Fristenkalender mit Quelle Owner Ampel und Eskalationsprotokoll. Abgrenzung zu Steps-Plan-PMO fuer Aufgabenmanagement und zu Automation-Monitoring."
---

# Freistehender Deal-Fristen- und CP-Kalender

## Zweck

Dieser Skill führt die Transaktionsfristen im Plugin selbst. Er bündelt Q&A-Deadlines, Angebotsfristen, Datenraum-Cut-offs, Signing/Closing, Conditions Precedent, Regulatory Filings, Registertermine, Board Approvals, Ordinary-Course-Consents, W&I-Meilensteine, StaRUG-/Insolvenzfristen und PMI-Aufgaben.

## Arbeitsmodus

1. Fristen aus E-Mails, Process Letter, NDA, SPA, CP Register, Board Paper, Registerunterlagen und Datenraum-Neuzugängen extrahieren.
2. Jede Frist mit Quelle, Owner, Workstream, Konsequenz, Ampel und Eskalationsweg versehen.
3. Relative Fristen in absolute Daten umrechnen, aber den Rechenweg offenlegen.
4. Kritische Abhängigkeiten als Kette zeigen: Signing -> Filing -> Clearance -> CP Satisfaction -> Closing -> Register -> PMI.
5. Bei unklarer Zeitzone, Business-Day-Regel, Feiertag oder Zustellung immer nachfragen oder als Risiko markieren.

## Ausgabe

- Deal-Fristenkalender als Tabelle.
- CP-Register mit Status `open`, `in progress`, `submitted`, `satisfied`, `waived`, `blocked`.
- Ordinary-Course-Consent-Tracker.
- Eskalationsliste für diese Woche und die nächsten zehn Geschäftstage.
- Übergabe an Kommandocenter, Steps Plan, Regulatory, Closing Bible und PMI.

## Rote Schwellen

- Filing-Frist, Long Stop Date, Insolvenzantragspflicht, Board Approval oder Public-M&A-Veröffentlichung unklar.
- CP ist formal erfüllt, aber Beleg fehlt.
- Kalender widerspricht SPA oder Process Letter.
- Eine Frist hängt von nicht geprüfter Zustellung, Notarvollzug oder Registereintragung ab.

## Vorlagen

- assets/templates/deal-fristen-und-cp-kalender.md
- assets/templates/cp-register.md
- assets/templates/ordinary-course-covenant-monitor.md
- assets/templates/signing-closing-steps-plan.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- §§ 238-241a HGB — Buchfuehrungs- und Aufbewahrungspflichten (10 Jahre); GoBD gilt parallel
- §§ 1-9 UStG — Umsatzsteuerrecht: E-Rechnungspflicht ab 2025 (§ 14 Abs. 1 UStG n.F.); XRechnung und ZUGFeRD
- §§ 14-14c UStG — Rechnungsanforderungen; Vorsteuerabzug setzt ordnungsgemaesse Rechnung voraus
- §§ 195, 199 BGB — Verjaehrungsfristen: Fristenkalender muss auch gesetzliche Verjaehrungsfristen erfassen

### Leitsaetze
- BFH, Urt. v. 12.03.2020 - V R 20/19, BStBl. II 2020, 645 — Rechnungsanforderungen: eine Rechnung ohne Pflichtangaben nach § 14 Abs. 4 UStG berechtigt nicht zum Vorsteuerabzug; rueckwirkende Rechnungskorrektur moeglich, aber nur unter engen Voraussetzungen
- BGH, Urt. v. 15.05.2012 - VI ZR 157/11, NJW 2012, 2178 — Fristenversaeumnis: Anwalt haftet fuer schuldhaft versaeumte Fristen; Wiedervorlage und Kalenderfuehrung sind Kernpflicht

### Kommentarliteratur
- Kopp/Schenke, VwGO, Fristen und Fristen-Berechnung § 57 VwGO Rn. 1-40
- MueKo HGB/Ebke, §§ 238-241a Rn. 1-60 (Buchfuehrungspflicht, GoBD, Aufbewahrung)

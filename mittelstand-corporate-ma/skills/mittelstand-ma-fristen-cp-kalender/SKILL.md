---
name: mittelstand-ma-fristen-cp-kalender
description: "Kanzlei oder Mandant benoetigt Fristen- und CP-Kalender für M&A-Mandat: Signing Closing Q&A Regulatory Register Board Ordinary-Course. Normen §§ 187-193 BGB Fristberechnung MAR-Fristen GWB-Fristen AWV-Fristen. Prüfraster CP-Vollständigkeit Fristenanker Kollusionsrisiken Verlaengerungs-Optionen. Output Fristen-Kalender CP-Checkliste Terminvorschau. Abgrenzung zu automation-monitoring (technisches Monitoring) und steps-plan-pmo (Prozessplan)."
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

## Triage

1. Welche Fristen laufen gerade — Signing, Closing, CP-Deadlines, Regulatory-Fristen, Q&A-Fristen?
2. Gibt es Longstop Dates — ab wann ist Ruecktrittsrecht klar definiert?
3. Welche gesetzlichen Fristen sind zu beachten — Kartellfreigabe (1-4 Monate), Transparenzregister (2 Wochen), Gesellschafterliste (1 Monat)?

## Zentrale Rechtsgrundlagen

- §§ 187-193 BGB — Fristenberechnung: Beginn, Ende, Praevigorierungsregeln; Fristberechnung bei Monatsfristen und Wochenfristen
- § 41 GWB / Art. 7 FKVO — Fusionskontrolle: Vollzugsverbot bis zur Freigabe; Phase I 25 Arbeitstage (EU) bzw. 1 Monat (GWB)
- § 40 GmbHG — Gesellschafterliste: Einreichung innerhalb 1 Monat nach Anteilsuebertragung
- § 20 TranspRG — Transparenzregister: Meldung wirtschaftlich Berechtigte innerhalb 2 Wochen nach Aenderung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Fristenregister anlegen:** alle Fristen aus SPA, Regulatorik und Gesetz extrahieren
2. **Kalendereintraege setzen:** Signing, Longstop Date, Regulatory-Fristen, Register-Fristen, Garantiefristen
3. **Wiedervorlagen:** 1 Woche vor Ablauf jeder kritischen Frist; Senior-Eskalation bei Risiko
4. **CP-Status-Update:** taeglicher Update in Closing-Phase

## Rote Schwellen

- Frist versaeumt ohne Wiedervorlage: Haftung nach § 280 BGB
- Longstop Date uebersehen: automatisches Ruecktrittsrecht entsteht
- Gesellschafterliste nicht fristgerecht: Stimmrechte fraglich

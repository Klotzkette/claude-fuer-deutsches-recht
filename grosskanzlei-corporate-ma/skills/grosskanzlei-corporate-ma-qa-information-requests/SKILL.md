---
name: grosskanzlei-corporate-ma-qa-information-requests
description: "Q&A-Prozess und Information Requests in der Due Diligence steuern: Anwendungsfall Deal-Team muss aus DD-Analyse gezielte Fragen an Verkaeufer formulieren, priorisieren und Antworten gegen Datenraum-Belege prüfen. SPA Due Diligence Prozess, MAR Vertraulichkeit. Prüfraster Fragen nach Workstream und Prioritaet kategorisieren, Antworten-Qualitaet bewerten, unzureichende Antworten nachfassen, Strategieschutz bei Frageformulierung. Output Q&A-Tracker mit offenen, beantworteten und eskalationsbedürftigen Fragen. Abgrenzung zu Datenraum-Gap-Clean-Room und zu DD-Reporting."
---

# Q&A und Information Requests

## Zweck

Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität.

## Arbeitsmodus

- Aus DD-Lücken gezielte Fragen ableiten.
- Fragen nach Workstream, Prioritaet, Owner und Deal-Auswirkung sortieren.
- Antworten gegen Datenraumbelege prüfen.
- Unzureichende Antworten nachfassen.

## Rote Schwellen

- Frage verraet Strategie unnoetig.
- Antwort ohne Beleg wird als erledigt markiert.
- Q&A enthält Clean-Room-Information in offenem Bereich.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/qa-register.md
- assets/templates/information-request-list.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Sorgfaltspflichten: vollstaendige Mandatsfuehrung; Unterlassen kann Haftung ausloesen
- §§ 675, 280 BGB — Beratungsvertrag und Schadensersatz: Anwalt haftet bei Pflichtverletzung; gilt auch fuer Organisation und Kommunikation
- § 2 GmbHG; § 15 GmbHG — gesellschaftsrechtliche Grundlagen GmbH: relevant fuer alle Corporate-Mandate
- §§ 29-33 HGB — Handelsregisterpublizitaet: Wissen ueber eintragungspflichtige Tatsachen wird konstruktiv zugerechnet

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Alle Ergebnisse: Human-in-the-loop bei High-Risk-Findings
- Senior Review vor Weiterleitung an Mandant oder Gegenseite
- Dokumentation: Datum, Bearbeiter, Version, Freigabe

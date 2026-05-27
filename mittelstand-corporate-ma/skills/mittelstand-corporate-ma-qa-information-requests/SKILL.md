---
name: mittelstand-corporate-ma-qa-information-requests
description: "DD-Team verwaltet Q&A-Prozess im Datenraum: Information Request Lists Follow-ups Antwortqualitaets-Check. Normen §§ 311 241 BGB Offenbarungspflicht Disclosure-Prinzipien. Pruefraster IRL-Vollstaendigkeit Antwortpruefung Offene-Punkte-Tracking Status-Reporting. Output Q&A-Liste Information-Request-Log Statusbericht. Abgrenzung zu datenraum-gap-clean-room (Lueckenanalyse) und disclosure-schedules (SPA-Verankerung)."
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

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
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
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — anwaltliche Haftung: vollstaendige Information des Mandanten ueber alle wesentlichen Risiken ist Kernpflicht; auch bei Zeitdruck
- BGH, Urt. v. 04.04.2001 - VIII ZR 32/00, NJW 2001, 2163 — DD-Ergebnis muss vollstaendig in Beratungsleistung einfliessen; Luecken begruenden Schadensersatz

### Kommentarliteratur
- Schramm/Alexander, BRAO, § 43a Rn. 1-50 (anwaltliche Sorgfaltspflicht)
- Picot, Unternehmenskauf, Kapitel 1 (Transaktionsmanagement, Mandatsfuehrung), 5. Auflage

### Qualitaetssicherung
- Alle Ergebnisse: Human-in-the-loop bei High-Risk-Findings
- Senior Review vor Weiterleitung an Mandant oder Gegenseite
- Dokumentation: Datum, Bearbeiter, Version, Freigabe

---
name: mittelstand-corporate-ma-qa-information-requests
description: "DD-Team verwaltet Q&A-Prozess im Datenraum: Information Request Lists Follow-ups Antwortqualitaets-Check. Normen §§ 311 241 BGB Offenbarungspflicht Disclosure-Prinzipien. Prüfraster IRL-Vollständigkeit Antwortprüfung Offene-Punkte-Tracking Status-Reporting. Output Q&A-Liste Information-Request-Log Statusbericht. Abgrenzung zu datenraum-gap-clean-room (Lueckenanalyse) und disclosure-schedules (SPA-Verankerung)."
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Alle Ergebnisse: Human-in-the-loop bei High-Risk-Findings
- Senior Review vor Weiterleitung an Mandant oder Gegenseite
- Dokumentation: Datum, Bearbeiter, Version, Freigabe

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Massnahme: Leitsatz korrigiert auf tatsaechlichen Inhalt: gesteigerte vorvertragliche Aufklaerungspflicht des Verkaeufers beim GmbH-Anteilskauf; Nichtoffenbarung von Zahlungsunfaehigkeit / Konkursreife begruendet arglistige Taeuschung.
Quelle: dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=04.04.2001&Aktenzeichen=VIII+ZR+32%2F00
-->

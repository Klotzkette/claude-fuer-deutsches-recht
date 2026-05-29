---
name: grosskanzlei-corporate-ma-simulation-bidder-process
description: "M&A-Bieterprozess simulieren für Training und Mandatsvorbereitung: Anwendungsfall Junior-Anwalt oder Deal-Team ueben beschleunigten Transaktions-Tag mit Datenraum Q&A SPA-Markup CP-Liste und Board-Call. SPA Share Purchase Agreement, Due Diligence Datenraum. Prüfraster Szenario Seller-side/Buy-side, Deal-Ereignisse simulieren, Entscheidungspunkte steuern, Lessons Learned dokumentieren. Output simulierter Deal-Tag mit Entscheidungsprotokoll und Nachbereitung. Abgrenzung zu freundlichem Copilot für Echtzeit-Begleitung und zu Kommandocenter für echte Mandate."
---

# Bieterprozess-Simulation

## Zweck

Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call.

## Arbeitsmodus

- Szenario, Rolle und Geschwindigkeit festlegen.
- Datenraumereignisse, Bieterfragen, Markups und Freigaben simulieren.
- Nutzer durch Entscheidungen führen.
- Am Ende Lessons Learned und offene Punkte ausgeben.

## Rote Schwellen

- Simulation wird als echter Rechtsrat missverstanden.
- Keine Trennung zwischen Dummy-Daten und echten Daten.
- Rote Schwellen werden im Spielmodus ignoriert.

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

- assets/templates/deal-simulation-day.md
- assets/templates/workflow-deal-kommandocenter.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschaeftsgeheimnissen; gilt fuer alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior

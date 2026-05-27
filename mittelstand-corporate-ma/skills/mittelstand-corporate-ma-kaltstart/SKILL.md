---
name: mittelstand-corporate-ma-kaltstart
description: "Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpraeferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln."
---

# Deal-Kaltstart

## Zweck

Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln.

## Arbeitsmodus

- Deal-Playbook abfragen: Buy-side/Sell-side, PE/Strategic, Private/Public, Distressed, Carve-out.
- Standard-Schwellen erfassen: Materiality, red flag, escalation, W&I, board reporting.
- Datenquellen erfassen: VDR, Excel, HRB, Bundesanzeiger, Kapitalmarkt, interne Präzedenzfälle.
- Ergebnis als Deal-Profil ablegen.

## Rote Schwellen

- Keine Mandatsannahme oder Konfliktprüfung.
- Keine Festlegung, welche Daten in KI-Werkzeuge duerfen.
- Unklare Rollen zwischen Recht, Tax, Finance, ESG und Commercial.

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

- assets/templates/deal-kaltstart-profil.md
- assets/templates/authority-matrix.md

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

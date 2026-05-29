---
name: grosskanzlei-corporate-ma-kaltstart
description: "Kanzlei- und Mandantenpraeferenzen für Corporate/M&A erfassen: Anwendungsfall bei erstem Einsatz des Plugins konfiguriert Anwalt oder Kanzlei Deal-Playbooks, Materiality-Schwellen, Reporting-Standards, Abrechnungsmodell und KI-Governance. § 3a RVG Honorarvereinbarung, BRAO Berufsrecht. Prüfraster Dealtypen-Profil, Buy-side/Sell-side-Praeferenz, Standardschwellen, Datenraum-Praeferenzen, Berichtsformate, Sicherheitsregeln. Output konfiguriertes Kanzlei-Profil mit Playbook-Grundeinstellungen. Abgrenzung zu Deal-Intake für konkrete neue Mandate und zu KI-Governance-Berufsrecht."
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

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Alle Ergebnisse: Human-in-the-loop bei High-Risk-Findings
- Senior Review vor Weiterleitung an Mandant oder Gegenseite
- Dokumentation: Datum, Bearbeiter, Version, Freigabe

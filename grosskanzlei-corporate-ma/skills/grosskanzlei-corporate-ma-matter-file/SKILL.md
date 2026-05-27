---
name: grosskanzlei-corporate-ma-matter-file
description: "Deal-Akte und Matter-Workspace anlegen: Anwendungsfall bei Mandatsannahme wird strukturierter Matter-Workspace benoetigt mit allen Workstreams, Datenraumspiegel, Register-Links, Q&A-Tracker und Closing-Archiv. § 43a BRAO Aktenführung, GoBD Aufbewahrung. Pruefraster Ordnerstruktur 00-90-Archive, Deal-Code, Gegenparteien, Notar, Steuerberater, W&I-Versicherer. Output vollstaendig strukturierter Matter-Workspace mit Aktenzeichen, Parteienregister und Workstream-Uebersicht. Abgrenzung zu Deal-Intake fuer erste Erfassung und zu Aktenanlage fuer freistehende Version."
---

# Deal-Akte

## Zweck

Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI.

## Arbeitsmodus

- Ordnerstruktur für 00_Admin bis 90_Archive erzeugen.
- Deal-Codes, Gegenparteien, Gerichte/Register, Notar, Steuerberater, W&I und Banken verknuepfen.
- Aktenzeichen der Kanzlei mit HRB/HRA, LEI, ISIN, Deal-Codenamen und Parteien verknuepfen.
- Ablage- und Benennungsregeln ausgeben.

## Rote Schwellen

- Unklare Vertraulichkeitsstufe.
- Keine Rollen/Owner.
- Kein Archiv- und Closing-Bible-Plan.

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

- assets/templates/matter-opening-checklist.md
- assets/templates/closing-bible-index.md

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

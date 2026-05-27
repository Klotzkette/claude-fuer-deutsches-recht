---
name: mittelstand-corporate-ma-kommandocenter
description: "Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion."
---

# Deal-Kommandocenter

## Zweck

Schnellstart für Corporate/M&A-Mandate. Der Skill erkennt aus einem Satz, Datenraum, Term Sheet, Markup, Screenshot oder Registerauszug die Deal-Phase und führt in den passenden internen Workflow. Das Plugin ist freistehend: Aktenanlage, Tabellenreview, Liquiditätsvorschau, CP-Kalender, Billing und Restrukturierung liegen im selben Plugin.

## Arbeitsmodus

- Dealtyp und Parteiperspektive erkennen: Buy-side, Sell-side, Management, W&I-Versicherer, Public M&A oder Restrukturierung.
- Maximal drei Rückfragen stellen, danach mit vorsichtigen Annahmen und TODOs arbeiten.
- Deal-Phase bestimmen: Origination, Vorbereitung, Datenraum, Due Diligence, Vertrag, Signing/Closing, Integration oder Streit/Restrukturierung.
- Den passenden internen Spezialskill routen und rote Schwellen sichtbar machen.
- Anfängerfreundlich bleiben: fehlende Begriffe erklären, aber den Arbeitsfluss nicht aufhalten.

## Interne Routing-Karte

| Signal | Interner Skill |
| --- | --- |
| Neue Anfrage, Aktenzeichen, Datenraum-Einladung | `grosskanzlei-ma-aktenanlage` |
| Datenraumliste, CSV, Excel, Review Grid | `grosskanzlei-ma-tabellenreview` |
| Cash, OPOS, Bank, Runway, Distressed | `grosskanzlei-ma-liquiditaetsvorschau` |
| Zahlungsunfähigkeit, Überschuldung, StaRUG | `grosskanzlei-ma-insolvenzreife` |
| Signing, Closing, CP, Long Stop Date | `grosskanzlei-ma-fristen-cp-kalender` |
| Rechnung, Narrative, XRechnung, ZUGFeRD | `grosskanzlei-ma-erechnung-gobd` |
| Textentwurf, Report, SPA, Board Paper | `grosskanzlei-ma-schreibcanvas` |
| Register, HRB/HRA, Gesellschafterliste | `mittelstand-corporate-ma-handelsregisterabruf` |
| Rechtsprechung und amtliche Quellen | `mittelstand-corporate-ma-rechtsprechungsrecherche` |

## Rote Schwellen

- Frist, Signing oder Closing unklar.
- Mandatsgeheimnis, Clean Room oder Insiderinformation betroffen.
- KI-Ergebnis soll ungeprüft als Rechtsrat, DD-Finding oder Board-Grundlage verwendet werden.
- Liquiditätslücke, Insolvenzantragspflicht, Sanktionstreffer oder GwG-Risiko sichtbar.

## Standardausgabe

- Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Senior-Review-Hinweis bei hohen Risiken.

## Vorlagen

- assets/templates/workflow-deal-kommandocenter.md
- assets/templates/cowork-ma-dashboard.md
- assets/templates/workflow-freigabeampel.md

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

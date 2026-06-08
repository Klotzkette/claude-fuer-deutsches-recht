---
name: real-estate-redline
description: "Real Estate Redline im Corporate/M&A (Großkanzlei-Praxis): prüft konkret Purchase Price Adjustment und Earn-out Skill, Real Estate, Leases und Sites Due Diligence, Redline Comparison Automation für M&A-Dokumente. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Real Estate Redline

## Arbeitsbereich

**Real Estate Redline** ordnet den Fall über die tragenden Prüfungslinien: Purchase Price Adjustment und Earn-out Skill, Real Estate, Leases und Sites Due Diligence. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `grosskanzlei-corporate-ma-purchase-price-adjustment-earn-out` | Purchase Price Adjustment und Earn-out Skill: modelliert Anpassungen, Earn-out-KPIs, Manipulationsschutz, Covenants und Streitbeilegung. |
| `grosskanzlei-corporate-ma-real-estate-leases-sites` | Real Estate, Leases und Sites Due Diligence: prueft Grundstuecke, Mietvertraege, Belastungen, Genehmigungen, Umwelt, Change-of-Control und Standortkritikalitaet. |
| `grosskanzlei-corporate-ma-redline-comparison-automation` | Redline Comparison Automation für M&A-Dokumente: vergleicht Markups, extrahiert Key Issues, erkennt stille Aenderungen und baut Antwortvorschlaege. |
| `grosskanzlei-corporate-ma-register-filings-implementation` | Register Filings und Implementation Manager: plant Handelsregister, Transparenzregister, Gesellschafterlisten, Umwandlungsanmeldungen, Notarvollzug und Post-Closing-Filings. |
| `grosskanzlei-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und FDI-Investitionsprüfung für M&A-Transaktionen: Anwendungsfall Signing naht und Deal-Team prüft ob Kartellrechts-Freigabe oder AWV-Prüfung benoetigt wird. §§ 35-44 GWB inlaendische Fusionskontrolle, Art. 4 FKVO EU-Fusionskontrolle, §§ 55 ff. AWV FDI-Prüfung. Prüfraster Umsatzschwellen je Jurisdiktion, Vollzugsverbot bis Freigabe, Multi-Jurisdiction-Filing-Koordination, Sektorrisiken. Output Regulatorische Freigabe-Landkarte mit Filing-Pflichten, Zeitplan und Risikobewertung. Abgrenzung zu Signing-Closing-CPs und zu Transaktionsstruktur. |
| `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten: Anwendungsfall Unternehmen mit drohender Zahlungsunfähigkeit prüft Restrukturierungsoptionen einschließlich StaRUG-Plan, praeventiyen Restrukturierungsrahmen oder Insolvenzplan. §§ 1-93 StaRUG, §§ 217-269 InsO Insolvenzplan, § 18 InsO drohende Zahlungsunfähigkeit. Prüfraster Gläubiger-Klasseneinteilung, Plananforderungen, Abstimmungsquoren, Distressed-M&A-Optionen. Output Restrukturierungs-Optionsvergleich mit Plan-Entwurf und Zeitplan. Abgrenzung zu Distressed-MA und zu Fortbestehensprognose-Plugin. |
| `grosskanzlei-corporate-ma-risk-heatmap-board` | Risk Heatmap Board für Corporate/M&A: visualisiert Risiken nach Wahrscheinlichkeit, Impact, Verhandelbarkeit, Quellenstaerke, Owner und Deal-Blocker-Potential. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; UmwG; UmwStG; StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `grosskanzlei-corporate-ma-purchase-price-adjustment-earn-out`

**Fokus:** Purchase Price Adjustment und Earn-out Skill: modelliert Anpassungen, Earn-out-KPIs, Manipulationsschutz, Covenants und Streitbeilegung.

### Purchase Price Adjustment Earn Out

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Purchase Price Adjustment Earn Out` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Purchase Price Adjustment Earn Out
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Einsatz
Der Kaufpreis ist variabel, eine Earn-out-Struktur wird verhandelt oder Closing Accounts sind streitanfaellig.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | KPI, Zeitraum, Accounting Policy, Kontrolle nach Closing, Schwellen, Audit-Rechte, Streitmechanismus. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Earn-out-Blueprint, Risikoampel, Klauselvorschlaege, Beispielmatrix und Manipulationsschutz. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behördenstand pruefen oder als Live-Check-Aufgabe ausweisen.
4. **Deal-Praxis vor Lehrbuch:** Liefere verwertbare Dokumente, Tabellen, Klauselvorschlaege, Entscheidungsvorlagen oder naechste Arbeitsschritte. Theorie nur soweit, wie sie eine Entscheidung verbessert.
5. **Red-Team-Schleife:** Suche aktiv nach dem Punkt, an dem der Entwurf scheitern koennte: fehlender Beleg, falscher Adressat, schwache Subsumtion, unklare Vollmacht, falsche Risikoverteilung, unrealistisches Timing.

## Anfaenger- und First-Year-Modus
Wenn der Nutzer unsicher wirkt, erklaere jeden Fachbegriff in einem Satz und gib danach sofort die naechste kleine Handlung. Verwende dieses Muster:

- **Was bedeutet das?** Eine kurze Erklaerung ohne Kanzleijargon.
- **Warum ist es im Deal wichtig?** Risiko, Geld, Timing oder Unterschrift.
- **Was pruefe ich jetzt?** Ein konkreter Schritt.
- **Was waere Senior-tauglich?** Welche Belege, Quellen oder Formulierungen fehlen noch.

## Padlet- und Tabellen-Ausgabe
Biete bei komplexen Aufgaben eine visuelle Arbeitsflaeche an:

| Karte/Spalte | Inhalt | Status | Owner | Quelle | Naechster Schritt |
| --- | --- | --- | --- | --- | --- |
| Issue | Konkretes Thema oder Dokument | offen / in Pruefung / entschieden | Person oder Workstream | Datenraum, Register, Vertrag, Call | konkrete Aktion |

Fuer Tabellen nie nur Ueberschriften liefern. Jede Zeile braucht mindestens: Befund, rechtliche Bedeutung, wirtschaftliche Bedeutung, Evidenz, Risikoampel und Follow-up.

## Standard-Deliverables
- Kurzbild für Partner oder Mandant.
- Workstream-Tabelle mit Ampel und Owner.
- Issue-/Risk-Liste mit Priorisierung.
- Entwurf oder Textbausteine, soweit der Input reicht.
- Offene Punkte mit genauem Nachforderungswortlaut.

## Quality Gate
Vor Ausgabe immer pruefen:

- Ist die Partei-Perspektive klar?
- Sind alle Fristen und Vollzugsrisiken markiert?
- Sind Annahmen von gesicherten Tatsachen getrennt?
- Gibt es mindestens einen konkreten naechsten Schritt?
- Sind Tabellen, Klauseln oder Memos so formatiert, dass ein Deal-Team sofort weiterarbeiten kann?

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 2. `grosskanzlei-corporate-ma-real-estate-leases-sites`

**Fokus:** Real Estate, Leases und Sites Due Diligence: prueft Grundstuecke, Mietvertraege, Belastungen, Genehmigungen, Umwelt, Change-of-Control und Standortkritikalitaet.

### Real Estate Leases Sites

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Real Estate Leases Sites` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Real Estate Leases Sites
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Einsatz
Target nutzt wichtige Standorte, Produktionsflaechen, Mietobjekte oder Grundstuecke.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Grundbuch/Register, Mietvertraege, Standortliste, Genehmigungen, Umweltinformationen, Sicherheiten. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Site-Matrix, Lease-Red-Flags, Consent-Needs, Grundbuchfragen und SPA-Anlagenbedarf. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behördenstand pruefen oder als Live-Check-Aufgabe ausweisen.
4. **Deal-Praxis vor Lehrbuch:** Liefere verwertbare Dokumente, Tabellen, Klauselvorschlaege, Entscheidungsvorlagen oder naechste Arbeitsschritte. Theorie nur soweit, wie sie eine Entscheidung verbessert.
5. **Red-Team-Schleife:** Suche aktiv nach dem Punkt, an dem der Entwurf scheitern koennte: fehlender Beleg, falscher Adressat, schwache Subsumtion, unklare Vollmacht, falsche Risikoverteilung, unrealistisches Timing.

## Anfaenger- und First-Year-Modus
Wenn der Nutzer unsicher wirkt, erklaere jeden Fachbegriff in einem Satz und gib danach sofort die naechste kleine Handlung. Verwende dieses Muster:

- **Was bedeutet das?** Eine kurze Erklaerung ohne Kanzleijargon.
- **Warum ist es im Deal wichtig?** Risiko, Geld, Timing oder Unterschrift.
- **Was pruefe ich jetzt?** Ein konkreter Schritt.
- **Was waere Senior-tauglich?** Welche Belege, Quellen oder Formulierungen fehlen noch.

## Padlet- und Tabellen-Ausgabe
Biete bei komplexen Aufgaben eine visuelle Arbeitsflaeche an:

| Karte/Spalte | Inhalt | Status | Owner | Quelle | Naechster Schritt |
| --- | --- | --- | --- | --- | --- |
| Issue | Konkretes Thema oder Dokument | offen / in Pruefung / entschieden | Person oder Workstream | Datenraum, Register, Vertrag, Call | konkrete Aktion |

Fuer Tabellen nie nur Ueberschriften liefern. Jede Zeile braucht mindestens: Befund, rechtliche Bedeutung, wirtschaftliche Bedeutung, Evidenz, Risikoampel und Follow-up.

## Standard-Deliverables
- Kurzbild für Partner oder Mandant.
- Workstream-Tabelle mit Ampel und Owner.
- Issue-/Risk-Liste mit Priorisierung.
- Entwurf oder Textbausteine, soweit der Input reicht.
- Offene Punkte mit genauem Nachforderungswortlaut.

## Quality Gate
Vor Ausgabe immer pruefen:

- Ist die Partei-Perspektive klar?
- Sind alle Fristen und Vollzugsrisiken markiert?
- Sind Annahmen von gesicherten Tatsachen getrennt?
- Gibt es mindestens einen konkreten naechsten Schritt?
- Sind Tabellen, Klauseln oder Memos so formatiert, dass ein Deal-Team sofort weiterarbeiten kann?

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 3. `grosskanzlei-corporate-ma-redline-comparison-automation`

**Fokus:** Redline Comparison Automation für M&A-Dokumente: vergleicht Markups, extrahiert Key Issues, erkennt stille Aenderungen und baut Antwortvorschlaege.

### Redline Comparison Automation

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Redline Comparison Automation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Redline Comparison Automation
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Einsatz
Mehrere Vertragsversionen oder Bieter-Markups muessen schnell und praezise ausgewertet werden.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Basisfassung, Markup, Partei, Verhandlungsziel, Materiality, betroffene Klauseln. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Key Issues List, Silent-Change-Log, Red-Team-Hinweise, Gegenmarkup-Vorschlaege und Entscheidungsmatrix. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behördenstand pruefen oder als Live-Check-Aufgabe ausweisen.
4. **Deal-Praxis vor Lehrbuch:** Liefere verwertbare Dokumente, Tabellen, Klauselvorschlaege, Entscheidungsvorlagen oder naechste Arbeitsschritte. Theorie nur soweit, wie sie eine Entscheidung verbessert.
5. **Red-Team-Schleife:** Suche aktiv nach dem Punkt, an dem der Entwurf scheitern koennte: fehlender Beleg, falscher Adressat, schwache Subsumtion, unklare Vollmacht, falsche Risikoverteilung, unrealistisches Timing.

## Anfaenger- und First-Year-Modus
Wenn der Nutzer unsicher wirkt, erklaere jeden Fachbegriff in einem Satz und gib danach sofort die naechste kleine Handlung. Verwende dieses Muster:

- **Was bedeutet das?** Eine kurze Erklaerung ohne Kanzleijargon.
- **Warum ist es im Deal wichtig?** Risiko, Geld, Timing oder Unterschrift.
- **Was pruefe ich jetzt?** Ein konkreter Schritt.
- **Was waere Senior-tauglich?** Welche Belege, Quellen oder Formulierungen fehlen noch.

## Padlet- und Tabellen-Ausgabe
Biete bei komplexen Aufgaben eine visuelle Arbeitsflaeche an:

| Karte/Spalte | Inhalt | Status | Owner | Quelle | Naechster Schritt |
| --- | --- | --- | --- | --- | --- |
| Issue | Konkretes Thema oder Dokument | offen / in Pruefung / entschieden | Person oder Workstream | Datenraum, Register, Vertrag, Call | konkrete Aktion |

Fuer Tabellen nie nur Ueberschriften liefern. Jede Zeile braucht mindestens: Befund, rechtliche Bedeutung, wirtschaftliche Bedeutung, Evidenz, Risikoampel und Follow-up.

## Standard-Deliverables
- Kurzbild für Partner oder Mandant.
- Workstream-Tabelle mit Ampel und Owner.
- Issue-/Risk-Liste mit Priorisierung.
- Entwurf oder Textbausteine, soweit der Input reicht.
- Offene Punkte mit genauem Nachforderungswortlaut.

## Quality Gate
Vor Ausgabe immer pruefen:

- Ist die Partei-Perspektive klar?
- Sind alle Fristen und Vollzugsrisiken markiert?
- Sind Annahmen von gesicherten Tatsachen getrennt?
- Gibt es mindestens einen konkreten naechsten Schritt?
- Sind Tabellen, Klauseln oder Memos so formatiert, dass ein Deal-Team sofort weiterarbeiten kann?

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 4. `grosskanzlei-corporate-ma-register-filings-implementation`

**Fokus:** Register Filings und Implementation Manager: plant Handelsregister, Transparenzregister, Gesellschafterlisten, Umwandlungsanmeldungen, Notarvollzug und Post-Closing-Filings.

### Register Filings Implementation

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Register Filings Implementation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Register Filings Implementation
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Einsatz
Nach Signing/Closing muessen Register- und Vollzugsakte sauber umgesetzt werden.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Rechtsform, Transaktionsschritte, Notarunterlagen, Vollmachten, Registergericht, UBO-Status. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Filing Roadmap, Dokumentenliste, Verantwortliche, Fristen, Vollzugskontrolle und Ablageprotokoll. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behördenstand pruefen oder als Live-Check-Aufgabe ausweisen.
4. **Deal-Praxis vor Lehrbuch:** Liefere verwertbare Dokumente, Tabellen, Klauselvorschlaege, Entscheidungsvorlagen oder naechste Arbeitsschritte. Theorie nur soweit, wie sie eine Entscheidung verbessert.
5. **Red-Team-Schleife:** Suche aktiv nach dem Punkt, an dem der Entwurf scheitern koennte: fehlender Beleg, falscher Adressat, schwache Subsumtion, unklare Vollmacht, falsche Risikoverteilung, unrealistisches Timing.

## Anfaenger- und First-Year-Modus
Wenn der Nutzer unsicher wirkt, erklaere jeden Fachbegriff in einem Satz und gib danach sofort die naechste kleine Handlung. Verwende dieses Muster:

- **Was bedeutet das?** Eine kurze Erklaerung ohne Kanzleijargon.
- **Warum ist es im Deal wichtig?** Risiko, Geld, Timing oder Unterschrift.
- **Was pruefe ich jetzt?** Ein konkreter Schritt.
- **Was waere Senior-tauglich?** Welche Belege, Quellen oder Formulierungen fehlen noch.

## Padlet- und Tabellen-Ausgabe
Biete bei komplexen Aufgaben eine visuelle Arbeitsflaeche an:

| Karte/Spalte | Inhalt | Status | Owner | Quelle | Naechster Schritt |
| --- | --- | --- | --- | --- | --- |
| Issue | Konkretes Thema oder Dokument | offen / in Pruefung / entschieden | Person oder Workstream | Datenraum, Register, Vertrag, Call | konkrete Aktion |

Fuer Tabellen nie nur Ueberschriften liefern. Jede Zeile braucht mindestens: Befund, rechtliche Bedeutung, wirtschaftliche Bedeutung, Evidenz, Risikoampel und Follow-up.

## Standard-Deliverables
- Kurzbild für Partner oder Mandant.
- Workstream-Tabelle mit Ampel und Owner.
- Issue-/Risk-Liste mit Priorisierung.
- Entwurf oder Textbausteine, soweit der Input reicht.
- Offene Punkte mit genauem Nachforderungswortlaut.

## Quality Gate
Vor Ausgabe immer pruefen:

- Ist die Partei-Perspektive klar?
- Sind alle Fristen und Vollzugsrisiken markiert?
- Sind Annahmen von gesicherten Tatsachen getrennt?
- Gibt es mindestens einen konkreten naechsten Schritt?
- Sind Tabellen, Klauseln oder Memos so formatiert, dass ein Deal-Team sofort weiterarbeiten kann?

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 5. `grosskanzlei-corporate-ma-regulatory-fdi-merger-control`

**Fokus:** Fusionskontrolle und FDI-Investitionsprüfung für M&A-Transaktionen: Anwendungsfall Signing naht und Deal-Team prüft ob Kartellrechts-Freigabe oder AWV-Prüfung benoetigt wird. §§ 35-44 GWB inlaendische Fusionskontrolle, Art. 4 FKVO EU-Fusionskontrolle, §§ 55 ff. AWV FDI-Prüfung. Prüfraster Umsatzschwellen je Jurisdiktion, Vollzugsverbot bis Freigabe, Multi-Jurisdiction-Filing-Koordination, Sektorrisiken. Output Regulatorische Freigabe-Landkarte mit Filing-Pflichten, Zeitplan und Risikobewertung. Abgrenzung zu Signing-Closing-CPs und zu Transaktionsstruktur.

### Fusionskontrolle und Investitionskontrolle

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fusionskontrolle und Investitionskontrolle` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Fusionskontrolle und Investitionskontrolle
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **SPA/APA, Disclosure, Signing, Closing und Post-Closing-Mechanik**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Fusionskontrolle und Investitionskontrolle und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Board-/Shareholder-Approvals.
- Disclosure Letter, Knowledge-Definition, W&I-Underwriting-Liste.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-closing-bible-archiv` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Fusionskontrolle und Investitionskontrolle

## Zweck

Erstellt Freigabe-Landkarte für Kartellrecht (GWB, FKVO), FDI-Investitionspruefung (AWV/§ 55 ff.), Sektorregulierung und Multi-Jurisdiction-Filings. Erkennt Vollzugsverbote und steuert Freigabe-Zeitplan in der Signing-to-Closing-Phase.

## Triage — klaere vor Signing

1. Werden Kartellrechtsschwellen erreicht — weltweite Umsaetze der Beteiligten (§ 35 GWB: 500 Mio. EUR weltweit; 25 Mio. EUR in Deutschland); EU-Schwellen (Art. 1 FKVO: 5 Mrd. EUR / 250 Mio. EUR EU)?
2. Gilt das Vollzugsverbot — § 41 GWB / Art. 7 FKVO: Transaktion darf bis zur Freigabe nicht vollzogen werden (Gun Jumping-Verbot)?
3. Ist der Zielmarkt in einem sensiblen Sektor — Verteidigung, kritische Infrastruktur, Energie, Telekommunikation, Medien, Technologie?
4. Kommt ein FDI-Screening nach § 55 ff. AWV in Betracht — ist der Erwerber eine nichteuropaeische Gesellschaft oder hat nichteuropaeische Eigentuermer?
5. Sind Filings in mehreren Jurisdiktionen erforderlich — USA (HSR Act), UK (CMA), China (SAMR), weitere?
6. Liegen Konzentrationseffekte vor, die eine fusionskontrollrechtliche Pruefung in Phase II erfordern koennen?

## Zentrale Rechtsgrundlagen

- §§ 35-44 GWB — Zusammenschlusskontrolle: Aufgreifschwellen, Anmeldepflicht, Phase I (1 Monat), Phase II (4 Monate), Vollzugsverbot
- §§ 54-56 GWB — Ministererlaubnis; Nebenbestimmungen; sog. "second chance" nach Untersagung durch BKartA
- Art. 1-4 FKVO (EU-Fusionskontrollverordnung 139/2004) — EU-Fusionskontrolle: Schwellen, Vollzugsverbot Art. 7
- §§ 55-62 AWV — Investitionspruefung: sektorspezifische Pruefung (§ 55 AWV: kritische Infrastruktur u.a.); sektoruebergreifende Pruefung (§ 60 AWV: ab 25 % aus Drittstaaten); Meldepflicht; Genehmigungsvorbehalt
- § 4 Abs. 2 AWG — Untersagungsmacht des BMWi bei Bedrohung der öffentlichen Ordnung oder Sicherheit
- Art. 3 EU-FDI-Screening-VO 2019/452 — Koordinierungsrahmen für nationale FDI-Screenings innerhalb der EU

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Umsatz-Screening:** weltweit und in Deutschland (GWB), in der EU (FKVO), in USA, UK, China — Schwellenwerte der Parteien zusammenstellen
2. **Freigabe-Landkarte erstellen:** je Jurisdiktion: Schwelle erreicht? Filing erforderlich? Zeitplan (Phase I / II)?
3. **Gun Jumping-Protokoll:** Clean Team einrichten, Information Barriers, erlaubter Informationsaustausch vor Freigabe dokumentieren
4. **FDI-Pruefung:** § 55 AWV sektorbezogen vs. § 60 AWV sektorubergreifend pruefen; Erwerber-Herkunft feststellen; Meldepflicht-Fristen
5. **Filing-Vorbereitung:** Zusammenschlusserklaerung für BKartA/Kommission; Kontakte zu Behörden aufnehmen; Remedies-Szenarien vordenken
6. **Zeitplan in CP-Tracker einbauen:** Filing-Datum, Phase-I-Ablauf, Phase-II-Risiko; Longstop-Date anpassen
7. **Vollzugsverbot einhalten:** bis Freigabe kein wirtschaftlicher Einfluss des Erwerbers; Information Barriers; Gun Jumping-Protokoll

## Entscheidungsbaum

- Schwelle GWB § 35 erreicht → Filing BKartA → Phase I 1 Monat → Phase II Risiko? → ggf. 4 Monate
- EU-Schwelle FKVO Art. 1 erreicht → Kommission zuständig (one-stop-shop) → keine nationalen Filings
- Erwerber ausserhalb EU mit >25 % Anteil → § 60 AWV FDI-Pruefung → ggf. Genehmigungsvorbehalt; BMWi
- Sektor Verteidigung/kritische Infra → § 55 AWV → strenges sektorbezogenes Screening

## Output-Template: Freigabe-Landkarte

**Adressat:** Deal-Team, Compliance — Tonfall sachlich-analytisch

```
FREIGABE-LANDKARTE
Deal: [DEALNAME] — Datum: [DATUM]

| Jurisdiktion | Schwelle | Filing erforderlich | Behörde | Phase I | Phase II | Status |
|-------------|---------|---------------------|---------|---------|---------|--------|
| Deutschland | § 35 GWB | JA / NEIN | BKartA | 1 Monat | 4 Monate | TODO |
| EU | Art. 1 FKVO | JA / NEIN | KOM | 25 AT | 90 AT | TODO |
| AWV/FDI | § 55/60 AWV | JA / NEIN | BMWi | 2 Monate | 4 Monate | TODO |
| USA | HSR Act | JA / NEIN | FTC/DOJ | 30 Tage | variabel | TODO |

VOLLZUGSVERBOT: [ ] Aktiv — kein wirtschaftlicher Vollzug bis [DATUM]
CLEAN TEAM: [ ] eingerichtet — Information Barriers aktiv
```

## Rote Schwellen

- Filing unterlassen trotz Pflicht: Bussgeldhaftung (§ 81 GWB: bis 1 Mio. EUR; Art. 14 FKVO: bis 10 % Konzernumsatz)
- Gun Jumping (Vollzug vor Freigabe): zivilrechtliche Nichtigkeit; Bussgeld; Rueckabwicklung
- FDI-Screening nicht erkannt: Untersagung nach Closing moeglich; Behördenzwang zur Entflechtung

## Standardausgabe

- Freigabe-Landkarte (Multi-Jurisdiction)
- CP-Tracker mit Behorderden-Fristen
- Gun Jumping-Protokoll

## Uebergabe an andere Skills

- CPs → `grosskanzlei-corporate-ma-signing-closing-conditions`
- Fristen → `grosskanzlei-ma-fristen-cp-kalender`
- Konflikt/Sanktionen → `grosskanzlei-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/freigabe-landkarte-multijurisdiction.md
- assets/templates/gun-jumping-protokoll.md

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 6. `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan`

**Fokus:** StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten: Anwendungsfall Unternehmen mit drohender Zahlungsunfähigkeit prüft Restrukturierungsoptionen einschließlich StaRUG-Plan, praeventiyen Restrukturierungsrahmen oder Insolvenzplan. §§ 1-93 StaRUG, §§ 217-269 InsO Insolvenzplan, § 18 InsO drohende Zahlungsunfähigkeit. Prüfraster Gläubiger-Klasseneinteilung, Plananforderungen, Abstimmungsquoren, Distressed-M&A-Optionen. Output Restrukturierungs-Optionsvergleich mit Plan-Entwurf und Zeitplan. Abgrenzung zu Distressed-MA und zu Fortbestehensprognose-Plugin.

### StaRUG und Insolvenzplan

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `StaRUG und Insolvenzplan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: StaRUG und Insolvenzplan
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **Distressed M&A, StaRUG/Insolvenz, Liquidität und steuerliche Strukturfolgen**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier StaRUG und Insolvenzplan und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- 13-Wochen-Liquiditätsplanung, Insolvenzreife-Check und Fortbestehensprognose.
- Asset-/Share-Deal-Struktur, Insolvenzverwalter- oder Eigenverwaltungsrolle.
- Anfechtungs-, Haftungs-, Steuer- und Closing-Sicherungsfragen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- InsO §§ 15a, 17, 18, 19, 129 ff., 270 ff. für Insolvenzreife, Antragspflicht und Anfechtung.
- StaRUG §§ 1, 9 ff. und 49 ff. für Früherkennung, Plan und Stabilisierung.
- BGB §§ 134, 138, 280, 311 Abs. 2 und 826 für Haftungs- und Sittenwidrigkeitsfragen.
- UmwStG §§ 20 bis 24 und § 8c KStG nur mit Steuerteam verifizieren.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-distressed-ma` - wenn Krise, Antragspflicht, Anfechtung oder Liquiditätsplanung entscheidend werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### StaRUG und Insolvenzplan

## Zweck

Unterstuetzt Restrukturierungsfaelle mit Planoptionen, Glaeubigerkl assen, Liquiditaetspruefung, Antragspflichten, Distressed M&A und Zeitplan nach StaRUG und Insolvenzplanrecht.

## Triage — klaere vor Strukturentscheidung

1. Welcher Insolvenztatbestand liegt vor — drohende Zahlungsunfaehigkeit (§ 18 InsO, Voraussetzung für StaRUG) oder bereits Zahlungsunfaehigkeit/Ueberschuldung (§§ 17, 19 InsO, Antragspflicht)?
2. Sind die wesentlichen Glaeubiger (Finanzglaeubiger, Lieferanten, Anleiheglaeubieger) identifiziert und kategorisiert?
3. Gibt es Plan-Optionen — StaRUG-Restrukturierungsplan, Insolvenzplan, uebertragende Sanierung oder Sale-and-Leaseback?
4. Liegt ein aktueller Liquiditaetsplan (13-Wochen-Cash-Flow) vor? Ist der Runway bis zur Planbestaetig ung ausreichend?
5. Hat die Geschaeftsleitung ein Sanierungskonzept (IDW S 6)? Liegt eine Fortbestehensprognose vor?
6. Ist ein Restrukturierungsbeauftragter bestellt oder soll ein solcher bestellt werden (§ 73 StaRUG)?

## Zentrale Rechtsgrundlagen

- §§ 1-93 StaRUG — vorinsolvenzlicher Restrukturierungsrahmen: Voraussetzung drohende Zahlungsunfaehigkeit (§ 18 InsO); kein öffentliches Insolvenzverfahren; Planabstimmung mit Glaeubigern
- §§ 217-269 InsO — Insolvenzplan: Sanierungs- oder Liquidationsplan; Glaeubigerzustimmung nach Klassen; Debt-Equity-Swap moeglich
- §§ 304-337 InsO — Insolvenzverwalter-gesteuerte Planvorbereitung; Abstimmung im Berichts- und Pruefungstermin
- § 15a InsO — Antragspflicht: 3 Wochen bei Zahlungsunfaehigkeit, 6 Wochen bei Ueberschuldung; Verletzung: Strafbarkeit
- § 15b InsO — Haftung für Zahlungen nach Insolvenzreife; Direktanspruch des Insolvenzverwalters
- §§ 225a Abs. 2, 3 InsO — Debt-Equity-Swap: Umwandlung von Glaeubigerforderungen in Eigenkapital; Zustimmung Anteilseigner nicht erforderlich bei Ueberschuldung
- § 8c KStG — steuerlicher Verlustuntergang bei schaedlichem Anteilserwerb; Ausnahme: Sanierungsklausel § 8c Abs. 1a KStG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Insolvenztatbestand feststellen:** §§ 17-19 InsO prufen; 13-Wochen-Liquiditaetsplan erstellen; Antragspflicht-Frist notieren
2. **Verfahrenswahl:** StaRUG (nur bei drohender Zahlungsunfaehigkeit, § 18 InsO) vs. Insolvenzplan (bei Zahlungsunfaehigkeit oder auf Antrag) vs. uebertragende Sanierung
3. **Glaeubiger-Kategorisierung:** gesicherte Glaeubiger, ungesicherte Glaeubiger, nachrangige Glaeubiger, Anteilseigner — Klassen nach §§ 222-225 InsO bilden
4. **Plan-Entwurf:** darstellender und gestaltender Teil (§ 219 InsO); Besserstellungsvergleich: Plan vs. Liquidation; Debt-Equity-Swap-Option pruefen
5. **Abstimmungsmanagement:** Glaeubigerzustimmung nach Klassen; ueberwindung dissenting minority (cramdown, § 245 InsO); Betriebsrat-Information
6. **Insolvenzgericht-Interface:** Vorlage Plan beim Insolvenzgericht; Pruefungs- und Abstimmungstermin; Bestaetigung durch Gericht (§§ 248-253 InsO)
7. **Steuer-Check:** § 8c KStG Verlustuntergang pruefen; Sanierungsklausel § 8c Abs. 1a KStG anwenden; Restrukturierungsertrag (§ 3a EStG)
8. **Post-Plan-Umsetzung:** Eigentumsuebergang, Neufinanzierung, Betriebsfortfuehrung dokumentieren

## Entscheidungsbaum

- Nur drohende Zahlungsunfaehigkeit → StaRUG moeglich → kein öffentliches Verfahren; Vertraulichkeit
- Zahlungsunfaehigkeit bereits eingetreten → Antragspflicht § 15a InsO → Insolvenzantrag; ggf. InsO-Plan
- Mehrheit der Glaeubiger zustimmt, einzelne blockieren → cramdown § 245 InsO → Gericht kann zustimmung ersetzen
- Debt-Equity-Swap → § 225a InsO → Anteilseigner-Zustimmung nicht erforderlich bei Ueberschuldung

## Output-Template: Restrukturierungsplan-Struktur

**Adressat:** Insolvenzgericht / Glaeubiger — Tonfall sachlich-juristisch

```
RESTRUKTURIERUNGSPLAN
Schuldner: [GESELLSCHAFT] — Az.: [AKTENZEICHEN]
Datum: [DATUM] — Berater: [KANZLEI]

DARSTELLENDER TEIL
1. Ausgangssituation und Krisenursachen
2. Insolvenztatbestand (§ 18 InsO: drohende ZU)
3. Sanierungskonzept (IDW S 6 Grundsaetze)
4. Glaeubiger und Forderungsklassen:
 Klasse 1: Gesicherte Glaeubiger (Banken) — Summe: [BETRAG]
 Klasse 2: Lieferanten und ungesicherte Glaeubiger — Summe: [BETRAG]
 Klasse 3: Nachrangige Glaeubiger — Summe: [BETRAG]
5. Besserstellungsvergleich: Plan [X EUR] vs. Liquidation [Y EUR]

GESTALTENDER TEIL
1. Forderungsreduzierung je Klasse
2. Debt-Equity-Swap-Bedingungen
3. Neufinanzierung und Milestones
4. Kontrollmechanismus (Monitoring)
```

## Rote Schwellen

- Antragspflicht § 15a InsO abgelaufen: Geschaeftsfuehrer haftet strafrechtlich und zivilrechtlich
- Fortbestehensprognose negativ: StaRUG-Weg nicht mehr zulassig; Insolvenzantrag zwingend
- Liquiditaetslücke waehrend Plan-Verfahren: Planverfahren scheitert; ggf. Masseschmaelung

## Standardausgabe

- Restrukturierungsplan-Entwurf (darstellender und gestaltender Teil)
- Glaeubiger-Klassen-Tabelle
- Liquiditaets- und Antragspflicht-Ampel

## Uebergabe an andere Skills

- Distressed M&A → `grosskanzlei-corporate-ma-distressed-ma`
- Insolvenzreife → `grosskanzlei-ma-insolvenzreife`
- Liquiditaet → `grosskanzlei-ma-liquiditaetsvorschau`

## Vorlagen

- assets/templates/starug-restrukturierungsplan.md
- assets/templates/insolvenzplan-klassen-tabelle.md

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 7. `grosskanzlei-corporate-ma-risk-heatmap-board`

**Fokus:** Risk Heatmap Board für Corporate/M&A: visualisiert Risiken nach Wahrscheinlichkeit, Impact, Verhandelbarkeit, Quellenstaerke, Owner und Deal-Blocker-Potential.

### Risk Heatmap Board

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Risk Heatmap Board` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Risk Heatmap Board
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Einsatz
DD-Findings, Vertragsissues oder Regulatory-Themen muessen für Mandanten entscheidbar gemacht werden.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Findings, Betragsrahmen, Belege, Deal-Phase, Partei, Risikotoleranz. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Heatmap, Top-Risiken, Quick Wins, No-Go-Punkte, Board-Update und Follow-up-Fragen. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behördenstand pruefen oder als Live-Check-Aufgabe ausweisen.
4. **Deal-Praxis vor Lehrbuch:** Liefere verwertbare Dokumente, Tabellen, Klauselvorschlaege, Entscheidungsvorlagen oder naechste Arbeitsschritte. Theorie nur soweit, wie sie eine Entscheidung verbessert.
5. **Red-Team-Schleife:** Suche aktiv nach dem Punkt, an dem der Entwurf scheitern koennte: fehlender Beleg, falscher Adressat, schwache Subsumtion, unklare Vollmacht, falsche Risikoverteilung, unrealistisches Timing.

## Anfaenger- und First-Year-Modus
Wenn der Nutzer unsicher wirkt, erklaere jeden Fachbegriff in einem Satz und gib danach sofort die naechste kleine Handlung. Verwende dieses Muster:

- **Was bedeutet das?** Eine kurze Erklaerung ohne Kanzleijargon.
- **Warum ist es im Deal wichtig?** Risiko, Geld, Timing oder Unterschrift.
- **Was pruefe ich jetzt?** Ein konkreter Schritt.
- **Was waere Senior-tauglich?** Welche Belege, Quellen oder Formulierungen fehlen noch.

## Padlet- und Tabellen-Ausgabe
Biete bei komplexen Aufgaben eine visuelle Arbeitsflaeche an:

| Karte/Spalte | Inhalt | Status | Owner | Quelle | Naechster Schritt |
| --- | --- | --- | --- | --- | --- |
| Issue | Konkretes Thema oder Dokument | offen / in Pruefung / entschieden | Person oder Workstream | Datenraum, Register, Vertrag, Call | konkrete Aktion |

Fuer Tabellen nie nur Ueberschriften liefern. Jede Zeile braucht mindestens: Befund, rechtliche Bedeutung, wirtschaftliche Bedeutung, Evidenz, Risikoampel und Follow-up.

## Standard-Deliverables
- Kurzbild für Partner oder Mandant.
- Workstream-Tabelle mit Ampel und Owner.
- Issue-/Risk-Liste mit Priorisierung.
- Entwurf oder Textbausteine, soweit der Input reicht.
- Offene Punkte mit genauem Nachforderungswortlaut.

## Quality Gate
Vor Ausgabe immer pruefen:

- Ist die Partei-Perspektive klar?
- Sind alle Fristen und Vollzugsrisiken markiert?
- Sind Annahmen von gesicherten Tatsachen getrennt?
- Gibt es mindestens einen konkreten naechsten Schritt?
- Sind Tabellen, Klauseln oder Memos so formatiert, dass ein Deal-Team sofort weiterarbeiten kann?

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

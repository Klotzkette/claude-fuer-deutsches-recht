---
name: allgemein
description: "Grosskanzlei Corporate Ma Auction Process / Grosskanzlei Corporate Ma Authority Matrix / Grosskanzlei Corporate Ma Automation Monitoring / Grosskanzlei Corporate Ma Bank Consents / 3 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Grosskanzlei Corporate Ma Auction Process / Grosskanzlei Corporate Ma Authority Matrix / Grosskanzlei Corporate Ma Automation Monitoring / Grosskanzlei Corporate Ma Bank Consents / 3 weitere Module

## Arbeitsbereich

Dieser Skill bündelt **Grosskanzlei Corporate Ma Auction Process / Grosskanzlei Corporate Ma Authority Matrix / Grosskanzlei Corporate Ma Automation Monitoring / Grosskanzlei Corporate Ma Bank Consents / 3 weitere Module**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `grosskanzlei-corporate-ma-auction-process-letter` | Auction Process Letter Generator: erstellt und prueft Prozessbriefe fuer strukturierte Verkaufs- und Bieterverfahren mit Deadlines, Bid Requirements und Verfahrensregeln. |
| `grosskanzlei-corporate-ma-authority-matrix-approvals` | Authority Matrix und Approvals Skill: prueft Zeichnungsberechtigungen, Gremienkompetenzen, Vollmachten, Gesellschafterbeschluesse, Board Consents und interne Freigaben. |
| `grosskanzlei-corporate-ma-automation-monitoring` | Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Kartellrechtsfristen, §§ 55 ff. AWV FDI-Fristen, Art. 17 MAR Ad-hoc-Monitoring. Prüfraster Eskalationsregeln Owner-Matrix Stop-Schwellen PMI-Aufgaben News-Monitoring. Output Monitoring-Plan mit Trigger-Logik Eskalationspfad und Verantwortlichkeitsmatrix. Abgrenzung zu Steps-Plan-PMO für manuelle Aufgabenlisten und zu Fristen-CP-Kalender. |
| `grosskanzlei-corporate-ma-bank-consents-change-control` | Bank Consents und Change-of-Control in Finanzierungsvertraegen: erkennt Consent-Pflichten, Default-Risiken, Waiver-Bedarf und Closing-CPs. |
| `grosskanzlei-corporate-ma-bidder-instructions-vdr-rules` | Bidder Instructions und VDR Rules fuer grosse M&A-Prozesse: formuliert Datenraumregeln, Q&A-Disziplin, Upload-Standards, Clean-Room-Grenzen und Sanktionen bei Prozessverstoessen. |
| `grosskanzlei-corporate-ma-billing-narratives` | Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. § 3a RVG Stundenhonorar, GoBD Buchungsanforderungen, XRechnung ZUGFeRD. Prüfraster Honorarvereinbarung prüfen, Time Entries nach Phase strukturieren, Cap-Verbrauch ueberwachen, Success-Fee-Bedingungen abgleichen. Output deal-tauffähige Rechnungsnarrative mit Matter-Controlling und GoBD-konformem Buchungsnachweis. Abgrenzung zu E-Rechnung-GoBD für freistehende Abrechnung. |
| `grosskanzlei-corporate-ma-board-consents-minutes-resolutions` | Board Consents, Minutes und Resolutions fuer M&A: erstellt Beschlussvorlagen, Protokolle, Umlaufbeschluesse und Entscheidungsunterlagen mit Business-Judgment-Absicherung. |

## Arbeitsweg

Für **Grosskanzlei Corporate Ma Auction Process / Grosskanzlei Corporate Ma Authority Matrix / Grosskanzlei Corporate Ma Automation Monitoring / Grosskanzlei Corporate Ma Bank Consents / 3 weitere Module** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `grosskanzlei-corporate-ma` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `grosskanzlei-corporate-ma-auction-process-letter`

**Fokus:** Auction Process Letter Generator: erstellt und prueft Prozessbriefe fuer strukturierte Verkaufs- und Bieterverfahren mit Deadlines, Bid Requirements und Verfahrensregeln.

# Auction Process Letter

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Auction Process Letter` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Auction Process Letter
- **Spezialgegenstand:** Auction Process Letter; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Sell-side organisiert einen Auktionsprozess oder Buy-side muss Prozessregeln verstehen und taktisch bedienen.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Transaktionsphase, Bieteranzahl, Bid-Stufe, gewuenschte Binding/Non-Binding-Angebote, Zeitplan, besondere Anforderungen. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Process Letter, Bid Checklist, Compliance-Hinweise, Q&A-Regeln und Bieter-To-do-Liste. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behoerdenstand pruefen oder als Live-Check-Aufgabe ausweisen.
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
- Kurzbild fuer Partner oder Mandant.
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
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 2. `grosskanzlei-corporate-ma-authority-matrix-approvals`

**Fokus:** Authority Matrix und Approvals Skill: prueft Zeichnungsberechtigungen, Gremienkompetenzen, Vollmachten, Gesellschafterbeschluesse, Board Consents und interne Freigaben.

# Authority Matrix Approvals

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Authority Matrix Approvals` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Authority Matrix Approvals
- **Spezialgegenstand:** Authority Matrix Approvals; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Unklar ist, wer unterschreiben darf, welches Gremium zustimmen muss oder welche Vollmacht fuer Signing/Closing benoetigt wird.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Rechtsform, Satzung/Gesellschaftsvertrag, Gesellschafterliste, Organstruktur, Transaktionsdokumente, Jurisdiktionen. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Authority Matrix, Beschlussliste, Vollmachtsbedarf, Signing-Rollenplan und Register-/Notar-Check. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behoerdenstand pruefen oder als Live-Check-Aufgabe ausweisen.
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
- Kurzbild fuer Partner oder Mandant.
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
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 3. `grosskanzlei-corporate-ma-automation-monitoring`

**Fokus:** Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Kartellrechtsfristen, §§ 55 ff. AWV FDI-Fristen, Art. 17 MAR Ad-hoc-Monitoring. Prüfraster Eskalationsregeln Owner-Matrix Stop-Schwellen PMI-Aufgaben News-Monitoring. Output Monitoring-Plan mit Trigger-Logik Eskalationspfad und Verantwortlichkeitsmatrix. Abgrenzung zu Steps-Plan-PMO für manuelle Aufgabenlisten und zu Fristen-CP-Kalender.

# Automationen und Monitoring (Corporate M&A)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Automationen und Monitoring (Corporate M&A)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Automationen und Monitoring (Corporate M&A)
- **Spezialgegenstand:** Automationen und Monitoring (Corporate M&A); der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Triage zu Beginn

Vor dem Entwurf eines Monitoring-Plans klaeren:

1. **Deal-Phase:** Pre-Signing (Datenraum, Q&A, LOI-Frist) oder Post-Signing (CP-Deadlines, Regulatorie, § 613a BGB) oder PMI?
2. **Insiderinformationen betroffen?** Monitoring von boersenrelevanten Informationen erfordert MAR-Freigabe (Art. 17 MAR); automatische Aussenkommunikation ist verboten.
3. **Datenquellen identifiziert?** VDR (Intralinks, Datasite), Handelsregister, Bundesanzeiger, BKartA-Datenbank, DPMA, Nachrichtendienste?
4. **Owner-Matrix vorhanden?** Wer ist verantwortlich fuer welchen Workstream? Ohne Owner kein Monitoring-Plan.
5. **Eskalationsregeln definiert?** Ab wann wird eskaliert? (CP-Frist < 14 Tage, Datenraum-Neuzugang kritische Kategorie, MAR-Signal erkannt)
6. **Vertraulichkeitsrahmen geklaert?** Monitoring von externen Quellen muss Mandatsgeheimnis (§ 43a Abs. 2 BRAO) und DSGVO (Art. 5 DSGVO) beachten.

## Zentrale Normen

Art. 17 MAR (Ad-hoc-Publizitaet; Insiderinformationen) — §§ 33 ff. WpHG (Stimmrechtsmitteilungen bei boersennotierter Zielgesellschaft) — §§ 35 ff. GWB (Fusionskontrolle BKartA; Vollzugsverbot bis Freigabe) — §§ 55 ff. AWV (FDI-Screening BMWK) — § 40 GmbHG (Gesellschafterliste; aktuelle Registerpublizitaet) — § 15 HGB (Handelsregisterpublizitaet; negative Publizitaet) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Monitoring-Dienstleistern) — § 43a Abs. 2 BRAO (Verschwiegenheitspflicht bei Monitoring-Datenverarbeitung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Monitoring-Kategorien und Pruefliste

### A: Datenraum-Monitoring (Pre-Signing)

| Monitor | Quelle | Frequenz | Owner | Eskalation |
|---|---|---|---|---|
| Neuzugaenge kritische Kategorie | VDR-API / Aktivitaetslog | Stundlich | DD-Lead | Sofort bei neuen Finanzunterlagen oder Material Adverse Change |
| Q&A-Antworten mit NDA-Implikation | VDR-Q&A | Taeglich | Legal | Bei Ablehnung oder Ausweichen |
| VDR-Zugriffsprotokoll | VDR-Admin | Woechentlich | IT-Security | Bei unberechtigtem Zugriff |

### B: CP-Deadline-Monitoring (Post-Signing)

| Monitor | Norm | Frist | Owner | Eskalation bei |
|---|---|---|---|---|
| Fusionskontrolle BKartA | §§ 35 ff. GWB | Vertraglich (typisch 3-6 Monate) | Regulatory-Lead | < 14 Tage bis Frist |
| FDI-Screening BMWK | §§ 55 ff. AWV | Vertraglich / gesetzlich | Regulatory-Lead | Behoerdenanfrage unbeantwortet |
| AR-Zustimmungsbeschluss | § 179a AktG | Vor Closing | Corporate-Lead | 21 Tage vor Closing |
| CoC-Zustimmungen (Tier 1-3) | Vertragliche Klauseln | SPA-Frist | Vertragslegal | Verweigerung oder Schweigen |
| Gesellschafterliste § 40 GmbHG | § 40 GmbHG | Unverzueglich nach Closing | Corporate-Lead | > 14 Tage nach Closing |

### C: Register-Monitoring (Laufend)

| Monitor | Quelle | Frequenz | Owner |
|---|---|---|---|
| Handelsregister Zielgesellschaft | www.handelsregister.de | Woechentlich | Corporate-Ass. |
| Bundesanzeiger Zielgesellschaft | Bundesanzeiger.de | Monatlich | Corporate-Ass. |
| DPMA IP-Register | dpma.de | Monatlich | IP-Counsel |

### D: Kapitalmarkt-Monitoring (bei boersennotierter Zielgesellschaft)

| Monitor | Norm | Eskalation |
|---|---|---|
| Ad-hoc-Mitteilungen Zielgesellschaft | Art. 17 MAR | Sofort — MAR-Freigabe erforderlich |
| Stimmrechtsmitteilungen | §§ 33 ff. WpHG | Bei Annaehern an 30 % WpUEG-Schwelle |
| Short-Selling-Positionen | EU-Leerverkaufs-VO | Bei ungewoehnlichem Anstieg |

## Schritt-fuer-Schritt-Workflow

1. **Deal-Phase und Monitoring-Bedarf erfassen:** Welche Workstreams laufen? Welche CPs sind offen? Deadline-Uebersicht aus SPA erstellen.
2. **Owner-Matrix festlegen:** Fuer jeden Monitoring-Bereich einen verantwortlichen Owner (Person + Eskalation) benennen. Kein Monitor ohne Owner.
3. **Technische Quellen definieren:** VDR-API, RSS-Feeds Bundesanzeiger, Handelsregister-Benachrichtigungen aktivieren, MAR-Alert-System konfigurieren.
4. **Eskalationsregeln dokumentieren:** Schwellenwerte (Frist < 14 Tage, kritischer Datenraum-Zugang, MAR-Signal) mit Eskalationsstufe (Owner → Senior Partner → Mandant) verknuepfen.
5. **Stop-Schwellen benennen:** Insiderinformation erkannt → manueller Review vor jeder automatischen Ausgabe. Externer Datenzugriff unklar → Monitoring pausieren.
6. **Monitoring-Plan dokumentieren:** Monitoring-Automation-Plan (Template unten) erstellen und mit Deal-PMO verknuepfen.
7. **Woechentlicher Check:** CP-Status, offene Q&A, neue Registereintraege, MAR-Alerts in Deal-PMO-Wochenbericht einspeisen.

## Output-Template

**Adressat:** Deal-PMO / Senior Partner — Tonfall: sachlich-strukturiert, risikoorientiert

```
MONITORING-AUTOMATION-PLAN
Mandat: [MANDATSCODE]
Zielgesellschaft: [NAME]
Deal-Phase: [PRE-SIGNING / POST-SIGNING / PMI]
Erstellt: [TT.MM.JJJJ]
Owner Monitoring: [NAME]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Insiderinformationen: Freigabe durch [COMPLIANCE-OFFICER] erforderlich.

--- AKTIVE MONITORE ---
| Monitor | Quelle | Frequenz | Owner | Letzter Check | Status |
|---|---|---|---|---|---|
| [MONITOR 1] | [QUELLE] | [FREQUENZ] | [PERSON] | [DATUM] | [OK / ALARM / OFFEN] |

--- OFFENE CP-DEADLINES ---
| CP | Norm | Frist | Status | Eskalation faellig ab |
|---|---|---|---|---|
| Fusionskontrolle | §§ 35 ff. GWB | [DATUM] | [OFFEN / EINGEREICHT / FREIGABE] | [DATUM] |
| FDI BMWK | §§ 55 ff. AWV | [DATUM] | [OFFEN / EINGEREICHT] | [DATUM] |

--- ALARME (Aktuelle Woche) ---
[KEIN ALARM]
oder:
ALARM: [BESCHREIBUNG] — Eskalation an: [PERSON] — Frist: [DATUM]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
2. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
```

## Rote Schwellen

- **CP-Frist Fusionskontrolle < 7 Tage, kein Freigabestatus** — Vollzugsverbot § 41 GWB; Deal-Coordinator sofort informieren; Pre-Filing-Gespraeche initiieren.
- **MAR-Signal ohne manuellen Review** — automatische Aussenkommunikation verboten; alle MAR-relevanten Ausgaben manuell freigeben lassen.
- **Monitoring ohne Owner** — kein Monitor ohne benannte verantwortliche Person; ohne Owner-Matrix Monitoring-Plan zurueckhalten.
- **Vertrauliche Monitoring-Daten an unautorisierten Dritten** — § 43a Abs. 2 BRAO; sofortiger Stopp; Kanzlei-Compliance informieren.

## Arbeitsmodus

- Nur Vorschlaege fuer Automationen machen, keine vertraulichen Daten ungefragt beobachten.
- Monitoringziel, Frequenz, Quelle, Owner und Output definieren.
- Eskalationsregeln und Stoppschwellen festlegen.
- Automationsvorschlaege mit Deal-PMO verknuepfen.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, naechster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Uebergabe an andere Skills

- Komplexe Eingaenge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurueckspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknuepfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams fuehren.

## Vorlagen

- assets/templates/monitoring-automation-plan.md
- assets/templates/deal-pmo-weekly.md

## Quellen und Vertiefung

- Art. 17 MAR (Ad-hoc-Publizitaet; Insider-Monitoring)
- §§ 35, 41 GWB (Fusionskontrolle; Vollzugsverbot)
- §§ 55 ff. AWV (FDI-Screening)
- § 40 GmbHG (Gesellschafterliste; Registerpublizitaet)
- Art. 28 DSGVO (Datenschutz bei Monitoring-Dienstleistern)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mestmäcker/Veelken, in: Immenga/Mestmäcker, GWB, 6. Aufl. 2021, § 41 Rn. 1 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.


## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 4. `grosskanzlei-corporate-ma-bank-consents-change-control`

**Fokus:** Bank Consents und Change-of-Control in Finanzierungsvertraegen: erkennt Consent-Pflichten, Default-Risiken, Waiver-Bedarf und Closing-CPs.

# Bank Consents Change Control

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bank Consents Change Control` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Bank Consents Change Control
- **Spezialgegenstand:** Bank Consents Change Control; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Target oder Gruppe hat Finanzierungsvertraege, die durch den Deal beruehrt werden.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Loan Agreements, Schuldschein, Sicherheiten, Konzernwechsel, Covenants, Konsortialstruktur. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Consent-Matrix, Waiver-Plan, CP-Formulierungen, Lender-Kommunikation und Red Flags. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behoerdenstand pruefen oder als Live-Check-Aufgabe ausweisen.
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
- Kurzbild fuer Partner oder Mandant.
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
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 5. `grosskanzlei-corporate-ma-bidder-instructions-vdr-rules`

**Fokus:** Bidder Instructions und VDR Rules fuer grosse M&A-Prozesse: formuliert Datenraumregeln, Q&A-Disziplin, Upload-Standards, Clean-Room-Grenzen und Sanktionen bei Prozessverstoessen.

# Bidder Instructions VDR Rules

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bidder Instructions VDR Rules` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Bidder Instructions VDR Rules
- **Spezialgegenstand:** Bidder Instructions VDR Rules; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ein Datenraum wird fuer mehrere Bieter geoeffnet oder ein laufender Prozess braucht klare Spielregeln.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Prozessphase, Bieterkreis, Datenraumplattform, Q&A-Modus, Clean-Room-Setup, Kommunikationswege. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Bieterregeln, Datenraumprotokoll, Q&A-Routing, No-Contact-Regeln und Verfahrenskalender. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behoerdenstand pruefen oder als Live-Check-Aufgabe ausweisen.
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
- Kurzbild fuer Partner oder Mandant.
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
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 6. `grosskanzlei-corporate-ma-billing-narratives`

**Fokus:** Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. § 3a RVG Stundenhonorar, GoBD Buchungsanforderungen, XRechnung ZUGFeRD. Prüfraster Honorarvereinbarung prüfen, Time Entries nach Phase strukturieren, Cap-Verbrauch ueberwachen, Success-Fee-Bedingungen abgleichen. Output deal-tauffähige Rechnungsnarrative mit Matter-Controlling und GoBD-konformem Buchungsnachweis. Abgrenzung zu E-Rechnung-GoBD für freistehende Abrechnung.

# Big-Law Billing Narratives (Corporate M&A)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Big-Law Billing Narratives (Corporate M&A)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Big-Law Billing Narratives (Corporate M&A)
- **Spezialgegenstand:** Big-Law Billing Narratives (Corporate M&A); der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Triage zu Beginn

Vor der Erstellung von Billing Narratives klaeren:

1. **Honorarvereinbarung vorhanden?** Stundenhonorar (§ 3a RVG) oder Pauschalhonorar oder Success Fee oder Cap + Success Fee? Kein Narrative ohne klar definiertes Abrechnungsmodell.
2. **Taetigkeiten vollstaendig erfasst?** Alle Time Entries nach Phase, Workstream und Deliverable vorliegend? Fehlende Entries flaggen.
3. **Budgetstatus geprueft?** Aktuelles WIP gegen Budget halten; Scope Creep und Abweichungen markieren bevor Narrative erstellt wird.
4. **Mandantenvertraulichkeit:** Narrative darf kein Mandatsgeheimnis unnoetig offen legen (§ 43a Abs. 2 BRAO); Formulierungen muessen pruefbar aber nicht erlaeuternd sein.
5. **Rechnungsreife?** Sind alle Bedingungen erfuellt (Leistungsstand, SPA-Meilenstein, vereinbarter Faelligkeitspunkt)? Bei Unsicherheit nicht abrechnen.
6. **E-Rechnung erforderlich?** Oeffentlicher Auftraggeber oder SPA-Klausel zu XRechnung/ZUGFeRD? Dann an `grosskanzlei-ma-erechnung-gobd` uebergeben.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Billing-Narrative-Struktur fuer M&A-Deals

### Time-Entry-Kategorien

| Phase | Workstream | Typische Taetigkeit |
|---|---|---|
| Pre-DD | Transaction Setup | Mandatsanlage, NDA-Verhandlung, VDR-Einrichtung |
| Due Diligence | Legal DD | Vertragsreview, Issue-Extraktion, Red-Flag-Report |
| Due Diligence | Corporate DD | Handelsregister-Auswertung, Gesellschafterliste |
| Signing | SPA-Verhandlung | Vertragsverhandlung, Kommentierung, Signing-Prep |
| Closing | Vollzug | CP-Tracking, Closing-Actions, Notartermin |
| Post-Closing | PMI | Vertragsuebernahmen, § 613a BGB, Gesellschafterliste |

### Narrative-Formulierungsregeln

1. **Mandantentauglich:** Keine Rechtsbegriffe ohne Erklaerung; kein unnoetig detaillierter Sachverhalt.
2. **Pruefbar:** Jede Taetigkeit muss einem Workstream und Deliverable zugeordnet sein.
3. **Vertraulich:** Kein Inhalt aus privilegierten Dokumenten (anwaltliche Stellungnahmen, DD-Reports) in externe Narrative.
4. **Zeitgenau:** Time Entries tagesgenau; keine rueckwirkenden Grosskorrekturen ohne Erklaerung.
5. **Budget-Delta markieren:** Abweichungen > 10 % zum vereinbarten Budget kommentieren.

### Narrative-Muster nach Workstream

```
Due Diligence — Legal: Vertragsreview (Commercial Contracts)
Pruefen und Analysieren von [N] Lieferantenvertraegen im Datenraum; Erstellung eines
Issue-Summary fuer [N] Material-Contract-Eintraege; Identifizierung von [N] Change-of-
Control-Klauseln mit Zustimmungserfordernis; Abstimmung mit Deal-Team zu CP-Implikationen.
[N.N h]
```

```
Signing — SPA-Verhandlung: Kommentierung § [Klausel] / Garantiekatalog
Erarbeitung der Kanzleiposition zu Abschnitt [X] des SPA-Entwurfs (Garantiekatalog);
Abstimmung mit Mandant zu akzeptablem Risikoprofil; Einarbeitung in Track-Changes-Version;
Verhandlungssitzung [DATUM] mit Gegenseite.
[N.N h]
```

## Schritt-fuer-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Time Entries importieren:** Alle Zeiteintragungen fuer den Abrechnungszeitraum nach Phase und Workstream sortieren.
2. **Budget-Abgleich:** WIP gegen vereinbartes Budget halten; Abweichungen > 10 % markieren und begruenden.
3. **Narrative verfassen:** Pro Workstream ein Narrative-Block nach Formulierungsregeln oben.
4. **Mandantenvertraulichkeit pruefen:** Kein Mandatsgeheimnis unnoetig offen gelegt? Narratives mandantentauglich formuliert?
5. **Rechnungspflichtangaben pruefen:** § 14 UStG-Angaben vollstaendig (Leistungsbeschreibung, Zeitraum, Steuernummer, USt-ID)?
6. **Cap-/Success-Fee-Check:** Gesamthonorar gegen vereinbarten Cap pruefen; Success-Fee-Bedingungen eingetreten?
7. **E-Rechnungspflicht pruefen:** Oeffentlicher Auftraggeber? XRechnung/ZUGFeRD erforderlich? → an `grosskanzlei-ma-erechnung-gobd` uebergeben.
8. **Rechnungsreife-Ampel ausgeben:** Gruen (alle Bedingungen erfuellt), Gelb (offene Punkte), Rot (Rechnung zurueckhalten).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Billing Narrative fuer M-and-A-Mandat erstellen | Narrative nach Schema; Template unten |
| Variante A — Mandant will kurzere Rechnungen weniger Detail | Kurzform-Narrative ohne Einzelleistungsaufstellung |
| Variante B — Stuendliche Abrechnung vs Pauschalhonorar | Bei Pauschalhonorar vereinfachtes Narrative ohne Stundenangaben |
| Variante C — Mehrteiliges Projekt Abrechnung in Phasen | Phasen-Narrative separat; Gesamtnachweis am Ende |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Mandant / Matter-Controller — Tonfall: knapp, pruefbar, mandantentauglich

```
BILLING NARRATIVE LEDGER
Mandat: [MANDATSCODE] / [ZIELGESELLSCHAFT]
Abrechnungszeitraum: [DATUM] bis [DATUM]
Erstellt: [TT.MM.JJJJ]
Matter-Controller: [NAME]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.

--- BUDGET-STATUS ---
Vereinbartes Budget: [BETRAG EUR]
WIP aktuell: [BETRAG EUR]
Abweichung: [+ / - BETRAG EUR] ([%])
Scope-Creep-Flag: [KEIN / JA: BESCHREIBUNG]

--- TIME ENTRIES NACH WORKSTREAM ---

WORKSTREAM: Due Diligence — Legal
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: SPA-Verhandlung
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: Closing
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

--- RECHNUNGS-ZUSAMMENFASSUNG ---
Honorar netto: [BETRAG EUR]
Umsatzsteuer 19 %: [BETRAG EUR]
Auslagen: [BETRAG EUR]
Summe brutto: [BETRAG EUR]
Cap-Pruefung: [UNTER CAP / CAP ERREICHT]
Success Fee: [NICHT FAELLIG / FAELLIG: BETRAG EUR]

--- RECHNUNGSREIFE-AMPEL ---
Status: [GRUEN / GELB / ROT]
Offene Punkte: [KEINE / LISTE]
Freigabe durch: [PARTNER-NAME]

--- E-RECHNUNG ---
XRechnung/ZUGFeRD erforderlich: [JA → Uebergabe grosskanzlei-ma-erechnung-gobd / NEIN]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rote Schwellen

- **Honorarvereinbarung § 3a RVG muendlich oder fehlend** — Formverstos; Anwalt kann nur RVG-Pflichtgebuehren verlangen; Vereinbarung unverzueglich schriftlich nachholen.
- **Narrative enthaelt Mandatsgeheimnis** — § 43a Abs. 2 BRAO; Formulierungen vor Versand pruefen; keine anwaltlichen Stellungnahmen, keine Parteiinterna in externen Narratives.
- **WIP ueberschreitet Cap ohne Mandanteninformation** — Haftungsrisiko; Mandant informieren und Scope-Abgleich durchfuehren bevor weitergearbeitet wird.
- **Rechnungspflichtangaben § 14 UStG unvollstaendig** — kein Vorsteuerabzug fuer Mandant; Rechnung korrigieren; Mahngebueehr-Risiko.
- **Leistung ohne Akte / Workstream** — GoBD-Verstos; Time Entry kann nicht verbucht werden; Nacherfassung nur mit Erklaerung.

## Arbeitsmodus

- Taetigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und pruefbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Pruefpunkte fuehren.
- Bei Rechnungsreife an `grosskanzlei-ma-erechnung-gobd` uebergeben.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Uebergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md

## Quellen und Vertiefung

- § 3a RVG (Stundenhonorar-Vereinbarung; Formerfordernis)
- § 49b BRAO (Vergaetungsvereinbarung)
- § 4a RVG (Erfolgshonorar)
- § 14 UStG (Rechnungspflichtangaben)
- § 146 AO / §§ 238 ff. HGB (GoBD; Buchfuehrungspflicht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mayer, in: Gerold/Schmidt, RVG, 26. Aufl. 2023, § 3a Rn. 5 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---
<!-- AUDIT 27.05.2026 bundle_004 -->
**Halluzinations-Audit 27.05.2026**


## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## 7. `grosskanzlei-corporate-ma-board-consents-minutes-resolutions`

**Fokus:** Board Consents, Minutes und Resolutions fuer M&A: erstellt Beschlussvorlagen, Protokolle, Umlaufbeschluesse und Entscheidungsunterlagen mit Business-Judgment-Absicherung.

# Board Consents Minutes Resolutions

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Board Consents Minutes Resolutions` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Board Consents Minutes Resolutions
- **Spezialgegenstand:** Board Consents Minutes Resolutions; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Vorstand, Geschaeftsfuehrung, Aufsichtsrat oder Gesellschafter muessen Transaktionsschritte beschliessen.

## Intake
Frage nicht breit, sondern dealpraktisch. Wenn Material schon vorliegt, extrahiere die Antworten selbst und markiere nur echte Luecken.

| Feld | Worum es geht |
| --- | --- |
| Deal-Perspektive | Buy-side, Sell-side, Target, Vorstand/Geschaeftsfuehrung, Bank, Investor, W&I-Versicherer oder Local Counsel. |
| Phase | Screening, NDA, Term Sheet, Datenraum, DD, SPA/APA, Signing, Closing, PMI, Streit oder Post-Mortem. |
| Material | Gremium, Rechtsform, Entscheidung, Unterlagen, Risiken, Interessenkonflikte, Timing. |
| Frist | Signing, Closing, Q&A, Filing, Board, Beurkundung, Angebotsfrist, CP-Deadline oder keine Eile erkennbar. |
| Ziel-Output | Beschlussentwurf, Minutes, Board Pack, BJR-Check, Interessenkonflikt-Notiz und Unterschriftenplan. |

## Agentischer Arbeitsmodus
1. **Sofortbild bauen:** Fasse zuerst Dealtyp, Partei, Phase, Eilpunkte und fehlende Unterlagen in fuenf Zeilen zusammen.
2. **Eigenstaendig nachziehen:** Wenn Angaben fehlen, arbeite mit gekennzeichneten Annahmen und fuehre eine kurze Lueckenliste. Nicht wegen Nebensachen stehen bleiben.
3. **Quellen- und Aktualitaetsgate setzen:** Bei Fusionskontrolle, FDI, FSR, Kapitalmarkt, Umwandlung, StaRUG, Steuer oder Register niemals alte Schwellen blind verwenden. Aktuellen Gesetzes-/Behoerdenstand pruefen oder als Live-Check-Aufgabe ausweisen.
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
- Kurzbild fuer Partner oder Mandant.
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
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten fuer Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behoerdenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

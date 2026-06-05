---
name: ins-insiderinformation-zwischenschritte
description: "Ins 001 Insiderinformation Art7, Ins 002 Zwischenschritte Ma: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 001 Insiderinformation Art7, Ins 002 Zwischenschritte Ma

## Arbeitsbereich

Dieser Skill bündelt **Ins 001 Insiderinformation Art7, Ins 002 Zwischenschritte Ma** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-001-insiderinformation-art7` | Prueft alle vier Tatbestandsmerkmale der Insiderinformation nach Art. 7 MAR: Praezision, Nichtoeffentlichkeit, Emittenten-/Instrumentenbezug, Kursrelevanz. |
| `ins-002-zwischenschritte-ma` | Analysiert Insiderinformation bei mehrstufigen Prozessen (M&A, Restrukturierung) nach dem EuGH-Geltl/Daimler-Standard fuer Zwischenschritte. |

## Arbeitsweg

Für **Ins 001 Insiderinformation Art7, Ins 002 Zwischenschritte Ma** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-001-insiderinformation-art7`

**Fokus:** Prueft alle vier Tatbestandsmerkmale der Insiderinformation nach Art. 7 MAR: Praezision, Nichtoeffentlichkeit, Emittenten-/Instrumentenbezug, Kursrelevanz.

# Insiderinformation nach Art. 7 MAR

## Rechtlicher Rahmen

Art. 7 VO (EU) 596/2014 (MAR) definiert die Insiderinformation abschließend. Die vier kumulativen
Tatbestandsmerkmale sind: (1) präzise Information, (2) nicht öffentlich bekannt, (3) unmittelbarer
oder mittelbarer Bezug zu Finanzinstrumenten, Emittenten oder dem Markt für Emissionszertifikate,
(4) Eignung zur erheblichen Kursbeeinflussung (Kursrelevanz). Jedes Merkmal ist eigenständig zu
prüfen und schriftlich zu belegen.

Rechtsgrundlagen:
- Art. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Erwägungsgrund 14–16 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- EuGH C-628/13 (Lafonta): https://curia.europa.eu/juris/document/document.jsf?docid=162388
- § 13 WpHG a.F. / § 119 WpHG n.F.: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill zwingt zur lückenlosen Prüfung aller vier Tatbestandsmerkmale in der richtigen
Reihenfolge. Er verhindert den häufigen Fehler, bereits bei unscharfen Informationen eine
Veröffentlichungspflicht anzunehmen oder bei klaren Insiderinformationen die Pflicht irrtümlich
zu verneinen. Ergebnis ist immer ein schriftlicher Insidervermerk mit Quellennachweis.

## Arbeitsprogramm

### Schritt 1 – Präzision (Art. 7 Abs. 1 lit. a, Abs. 2 MAR)

- Bestimme, ob die Information eine konkrete Tatsache oder ein konkretes Ereignis betrifft oder
 mit hinreichender Wahrscheinlichkeit eintreten wird.
- Trenne Tatsachen (vergangen/gegenwärtig) von Prognosen, Gerüchten und Analysen.
- Wende den Geltl/Daimler-Test an: Auch Zwischenschritte in einem mehrstufigen Prozess können
 präzise Informationen sein, sofern ihr Eintritt hinreichend wahrscheinlich ist (EuGH C-19/11).
- Halte fest: Welches Ereignis? Welches Datum/welcher Zeitraum? Welche Eintrittswahrscheinlichkeit?

### Schritt 2 – Nichtöffentlichkeit

- Prüfe, ob die Information in einem offiziell anerkannten Informationssystem (DGAP/EQS, BaFin-
 Datenbank, Bundesanzeiger) veröffentlicht wurde.
- Prüfe Kapitalmarktgerüchte: Breite Berichterstattung in Qualitätsmedien kann Öffentlichkeit
 herstellen, Gerücht oder Spekulation hingegen nicht.
- Dokumentiere Informationskreis: Wer hat die Information wann erhalten?

### Schritt 3 – Emittenten- oder Instrumentenbezug

- Kläre, ob die Information sich unmittelbar auf den Emittenten oder sein Finanzinstrument bezieht
 (z. B. Jahresergebnis) oder nur mittelbar (z. B. Rohstoffpreisanstieg).
- Bei Derivaten: Bezug auf Basiswert ausreichend.

### Schritt 4 – Kursrelevanz (Art. 7 Abs. 4 MAR)

- Wende den „verständigen Anleger"-Test an: Würde ein rationaler Investor die Information bei
 seiner Anlageentscheidung voraussichtlich nutzen?
- Kursrelevanz ist ex ante zu beurteilen, nicht nachträglich aus Kursbewegungen herzuleiten
 (EuGH C-628/13 Lafonta: Keine Pflicht, eine Kursrichtung vorherzusagen).
- Dokumentiere Marktumfeld, Branchenvergleich und Analystenpositionen als Hilfsindikatoren.

### Schritt 5 – Gesamtbewertung und Dokumentation

- Erstelle tabellarischen Insidervermerk mit: Sachverhalt, geprüftes Merkmal, Norm, Subsumtion,
 Gegenargument, Beleg, Zwischenergebnis.
- Benenne Unsicherheiten explizit; empfehle Nachprüfung durch Legal-Counsel falls unklar.
- Bestimme, ob Veröffentlichungspflicht nach Art. 17 MAR ausgelöst wird, und übergebe ggf. an
 Skill ins-003 (Ad-hoc) oder ins-004 (Aufschub).

## Red-Team-Fragen

- Ist die Information wirklich präzise oder nur ein allgemeines Marktgespräch?
- Wird Präzision mit Kursrelevanz verwechselt? Beide sind eigenständige Merkmale.
- Wurde der Geltl/Daimler-Test auf Zwischenschritte im M&A oder Restrukturierungsprozess
 konsequent angewendet?
- Wurde Kursrelevanz ex ante beurteilt, nicht nachträglich aus Kursbewegungen hergeleitet?
- Ist der Informationskreis vollständig dokumentiert?
- Wurden alle betroffenen Finanzinstrumente (Aktien, Anleihen, Derivate) erfasst?
- Wurde die Abgrenzung zu Art. 17 MAR (Veröffentlichungspflicht) sauber gezogen?
- Ist ein Aufschub nach Art. 17 Abs. 4 MAR möglich und wurden dessen Voraussetzungen geprüft?
- Wurden Insiderliste (Art. 18 MAR) und Handelsverbote (Art. 14 MAR) zeitgleich ausgelöst?

## Ausgabeformat

Erzeuge einen strukturierten Insidervermerk mit folgenden Abschnitten:
1. Sachverhalt (stichpunktartig, datiert)
2. Prüfung der vier Merkmale (je Merkmal: Norm – Subsumtion – Beleg – Ergebnis)
3. Gesamtergebnis: Insiderinformation ja/nein
4. Folgehandlungen (Ad-hoc-Pflicht, Aufschub, Insiderlistenpflege, Handelsverbot)
5. Offene Fragen und Empfehlungen

Nenne Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und einer der zulässigen
Quell-Domains (dejure.org, openjur.de, gesetze-im-internet.de, eur-lex.europa.eu,
curia.europa.eu, bafin.de, bgh.de). Keine Blindzitate aus BeckRS, juris oder Kommentaren.

## 2. `ins-002-zwischenschritte-ma`

**Fokus:** Analysiert Insiderinformation bei mehrstufigen Prozessen (M&A, Restrukturierung) nach dem EuGH-Geltl/Daimler-Standard fuer Zwischenschritte.

# Zwischenschritte bei mehrstufigen Prozessen (M&A / Restrukturierung)

## Rechtlicher Rahmen

EuGH C-19/11 (Geltl/Daimler, 28.06.2012) hat klargestellt, dass in einem gestreckten Sachverhalt
jeder Zwischenschritt selbst eine präzise Information im Sinne von Art. 7 MAR darstellen kann,
sofern sein Eintritt mit hinreichender Wahrscheinlichkeit erwartet wird und er kursrelevant ist.
Der BGH hat diese Rechtsprechung im Daimler-Urteil (BGH II ZB 26/12) für das deutsche Recht
übernommen. Für M&A-Transaktionen bedeutet dies: Schon die Aufnahme von Sondierungsgesprächen,
der Abschluss eines NDA oder die Durchführung einer Due Diligence können eigenständige
Insiderinformationen darstellen.

Rechtsgrundlagen:
- Art. 7 Abs. 2 und 3 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- BGH II ZB 26/12 (Daimler): https://www.bgh.de
- ESMA-Leitlinien zu Insiderinformationen: https://www.bafin.de/dok/8252648
- BaFin-Emittentenleitfaden Kap. I: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass bei mehrstufigen Vorgängen – insbesondere M&A-Transaktionen,
Kapitalmaßnahmen, Restrukturierungen oder Führungswechseln – jeder relevante Prozessschritt
einzeln auf das Vorliegen einer Insiderinformation geprüft wird. Er verhindert das typische
Compliance-Risiko, erst beim finalen Abschluss zu prüfen und frühere Schritte zu übersehen.

## Arbeitsprogramm

### Schritt 1 – Prozesskartierung

- Erstelle eine chronologische Zeitleiste des Vorgangs mit allen wesentlichen Schritten:
 Erstkontakt, NDA, indikatives Angebot, Due Diligence, LOI, Signing, Closing.
- Identifiziere alle Entscheidungsträger, die zu welchem Zeitpunkt Kenntnis erlangt haben.
- Halte fest, wer intern und extern in den Prozess einbezogen ist.

### Schritt 2 – Geltl/Daimler-Test für jeden Schritt

Prüfe für jeden identifizierten Zwischenschritt:
a) Handelt es sich um eine konkrete Tatsache oder ein Ereignis (Präzision)?
b) Ist der Eintritt des finalen Ereignisses aus Sicht des jeweiligen Zeitpunkts hinreichend
 wahrscheinlich? (Kein Automatismus: 50 % genügen nicht stets, 90 % fast immer.)
c) Ist der Zwischenschritt selbst kursrelevant, weil ein verständiger Anleger ihn bei seiner
 Investitionsentscheidung berücksichtigen würde?
d) Ist die Information noch nicht öffentlich?

### Schritt 3 – Erste Insiderinformation bestimmen

- Identifiziere den frühestmöglichen Zeitpunkt, ab dem eine Insiderinformation vorlag.
- Beachte: Bei einem M&A kann das Entscheidungsbegehren des Vorstands zur Aufnahme von
 Gesprächen bereits eine Insiderinformation sein (vgl. BaFin-Emittentenleitfaden).
- Dokumentiere Alternativszenarien und begründe die gewählte Einordnung.

### Schritt 4 – Folgehandlungen

- Löse Insiderliste (Art. 18 MAR) für alle Wissensträger ab dem ersten Insiderinformations-
 zeitpunkt aus.
- Prüfe Aufschub der Ad-hoc-Meldung nach Art. 17 Abs. 4 MAR: Sind die drei Aufschubvoraus-
 setzungen (legitimes Interesse, keine Irreführung, Vertraulichkeit gewährbar) erfüllt?
- Erstelle Aufschubakte und Leak-Überwachungsprotokoll.
- Prüfe Handelsverbote für alle Insider (Art. 14 MAR, Art. 19 MAR Closed Periods).

### Schritt 5 – Ereignis-Trigger und Eskalation

- Definiere im Voraus, bei welchem Ereignis der Aufschub endet und die Sofortveröffentlichung
 ausgelöst wird (Signing, Board-Beschluss, Bekanntwerden in Medien).
- Benenne eine verantwortliche Person (Compliance, CFO, IR) für die Auslösungsentscheidung.

## Red-Team-Fragen

- Wurde bei jedem Prozessschritt eigenständig geprüft, ob bereits eine Insiderinformation vorlag?
- Wurde der Geltl/Daimler-Test korrekt angewendet – insbesondere die Eintrittswahrscheinlichkeit
 zeitpunktbezogen und nicht rückblickend beurteilt?
- Ist die Insiderliste vom frühestmöglichen Zeitpunkt an gepflegt worden?
- Wurden externe Berater (Banken, Kanzleien) in die Insiderliste aufgenommen?
- Ist der Aufschub nach Art. 17 Abs. 4 MAR lückenlos dokumentiert?
- Gibt es einen definierten Trigger für die Sofortveröffentlichung?
- Wurden Handelsverbote für alle Wissensträger sichergestellt?
- Wurde Market Sounding (Art. 11 MAR) korrekt angewendet, sofern potenzielle Investoren
 sondiert wurden?

## Ausgabeformat

Erzeuge eine Zwischenschritt-Matrix mit:
1. Zeitleiste aller Prozessschritte
2. Je Schritt: Geltl/Daimler-Test (Präzision / Wahrscheinlichkeit / Kursrelevanz / Öffentlichkeit)
3. Erste Insiderinformation: Zeitpunkt und Begründung
4. Insiderliste: Einzutragende Personen ab Zeitpunkt X
5. Aufschubakte: Voraussetzungen, Beginn, geplantes Ende
6. Trigger-Ereignisse für Sofortveröffentlichung

Belege ausschließlich mit Quellen aus: dejure.org, openjur.de, gesetze-im-internet.de,
eur-lex.europa.eu, curia.europa.eu, bafin.de, bgh.de.

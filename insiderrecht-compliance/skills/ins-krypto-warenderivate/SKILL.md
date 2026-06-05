---
name: ins-krypto-warenderivate
description: "Ins 035 Krypto Token, Ins 036 Warenderivate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 035 Krypto Token, Ins 036 Warenderivate

## Arbeitsbereich

Dieser Skill bündelt **Ins 035 Krypto Token, Ins 036 Warenderivate** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-035-krypto-token` | Prueft Anwendbarkeit von MAR auf Krypto-Token und Asset-Referenced Token: MiCA-Abgrenzung, Insiderrecht fuer Krypto-Assets und Marktmanipulationsverbote. |
| `ins-036-warenderivate` | Prueft Insiderrecht und Marktmanipulationsverbot fuer Warenderivate: MAR-Anwendungsbereich, Spot-Market-Verzahnung und REMIT fuer Energiemaerkte. |

## Arbeitsweg

Für **Ins 035 Krypto Token, Ins 036 Warenderivate** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-035-krypto-token`

**Fokus:** Prueft Anwendbarkeit von MAR auf Krypto-Token und Asset-Referenced Token: MiCA-Abgrenzung, Insiderrecht fuer Krypto-Assets und Marktmanipulationsverbote.

# Krypto-Token und MAR / MiCA – Insiderrecht

## Rechtlicher Rahmen

MAR gilt für Finanzinstrumente nach MiFID II. Krypto-Assets, die keine Finanzinstrumente sind,
fallen grundsätzlich nicht unter MAR. Seit 30.12.2024 gilt jedoch die Verordnung MiCA
(EU) 2023/1114, die eigene Marktmissbrauchsregeln für Krypto-Assets enthält (Art. 87 ff. MiCA),
die MAR für Krypto-Assets nachbilden. Für Token, die als Finanzinstrumente qualifizieren
(Security Tokens), gilt MAR unmittelbar.

Rechtsgrundlagen:
- Art. 87–92 MiCA (Marktmissbrauch): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1114
- Art. 2 MAR (Anwendungsbereich): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- MiFID II Art. 4 (Finanzinstrument): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0065
- BaFin Krypto-Assets: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt, ob ein Krypto-Token unter MAR oder MiCA-Marktmissbrauchsvorschriften
fällt, und entwickelt die entsprechende Compliance-Strategie.

## Arbeitsprogramm

### Schritt 1 – Klassifizierung des Tokens

- Ist der Token ein Finanzinstrument nach MiFID II (Security Token)?
 → Wenn ja: MAR gilt unmittelbar (wie für Aktien oder Anleihen)
- Ist der Token ein Utility Token, Asset-Referenced Token oder E-Money Token?
 → Wenn ja: MiCA gilt (nicht MAR), spezifisch Art. 87–92 MiCA
- Ist der Token ein reiner Nutzungstoken ohne Anlagecharakter?
 → Ggf. weder MAR noch MiCA; rechtliche Qualifikation im Einzelfall erforderlich

### Schritt 2 – MAR-Pflichten für Security Tokens

Wenn MAR anwendbar:
- Art. 7 MAR: Insiderinformations-Definition
- Art. 17 MAR: Ad-hoc-Pflicht (soweit Token an geregeltem Markt gehandelt)
- Art. 14 MAR: Insiderhandelsverbot
- Art. 15 MAR: Marktmanipulationsverbot
- Insiderliste, Directors' Dealings analog

### Schritt 3 – MiCA-Pflichten für Krypto-Assets

Art. 87 MiCA (Insiderhandel):
- Verbot des Handels auf Basis von Insider-Informationen über Krypto-Assets
- Verbot der Weitergabe (Art. 88 MiCA)
- Verbot der Marktmanipulation (Art. 89 MiCA)
Art. 90 MiCA: Verpflichtung zur Veröffentlichung von Insiderinformationen für
 Krypto-Asset-Dienstleister und Emittenten von ARTs/EMTs

### Schritt 4 – Marktmanipulation im Krypto-Bereich

- „Wash Trading" und koordinierte Handelspraktiken zur Preisbeeinflussung
- Social-Media-Manipulation (Pump-and-Dump-Schemata)
- MAR Art. 12 und MiCA Art. 89 (beide verbieten diese Praktiken)

### Schritt 5 – Compliance-Empfehlungen für Token-Emittenten

- Klassifizierung des Tokens rechtlich absichern (externe Kanzlei)
- MiCA-Whitepaper und Pflichten des Token-Emittenten umsetzen
- Compliance-Policy für Trading in eigenen Token durch Mitarbeiter und Insider
- BaFin-Guidance zu Krypto-Assets regelmäßig verfolgen

## Red-Team-Fragen

- Ist die Klassifizierung des Tokens als Finanzinstrument vs. Krypto-Asset rechtssicher?
- Wurden Art. 87–92 MiCA als eigenständige Compliance-Anforderungen implementiert?
- Gibt es Marktmanipulations-Monitoring für den Token?
- Sind die Insiderregeln für Mitarbeiter des Token-Emittenten kommuniziert?

## Ausgabeformat

Erzeuge:
1. Token-Klassifizierungsmatrix (Merkmal × MAR/MiCA/keine Regel)
2. MAR vs. MiCA-Pflichten-Vergleich
3. Compliance-Policy-Entwurf für Token-Insider
4. Marktmanipulations-Monitoring-Framework

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

## 2. `ins-036-warenderivate`

**Fokus:** Prueft Insiderrecht und Marktmanipulationsverbot fuer Warenderivate: MAR-Anwendungsbereich, Spot-Market-Verzahnung und REMIT fuer Energiemaerkte.

# Warenderivate – MAR und REMIT

## Rechtlicher Rahmen

MAR gilt auch für Warenderivate (Art. 2 Abs. 1 MAR), sofern sie an einem regulierten Markt
oder MTF gehandelt werden. Für den Energiemarkt (Strom, Gas) gilt zusätzlich REMIT
(Regulation on Wholesale Energy Market Integrity and Transparency, VO (EU) 1227/2011),
die ein eigenständiges Marktmissbrauchsverbot für Großhandels-Energieprodukte enthält.
Spot-Markt und Derivatemarkt sind durch Art. 5 MAR verzahnt.

Rechtsgrundlagen:
- Art. 2, 5, 7 MAR (Warenderivate): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- REMIT (EU) 1227/2011: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32011R1227
- REMIT II (EU) 2024/1106 (Novelle): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1106
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob MAR oder REMIT auf Warenderivat-Transaktionen anwendbar ist, und
entwickelt die Compliance-Strategie für Commodity-Trader und Energieunternehmen.

## Arbeitsprogramm

### Schritt 1 – Anwendungsbereich MAR vs. REMIT

- MAR: Warenderivate an regulierten Märkten oder MTF (z. B. EEX, ICE)
- REMIT: Großhandels-Energieprodukte (Strom, Gas, LNG, Kapazitätsprodukte) –
 auch OTC-Handel fällt unter REMIT
- Überschneidung: Energie-Derivate an regulierten Märkten können sowohl MAR als auch
 REMIT unterliegen (kumulative Anwendung möglich)

### Schritt 2 – Insiderinformation im Warenderivate-Kontext (Art. 7 MAR)

- Information über Lieferbedingungen, Verfügbarkeit (z. B. Pipeline-Ausfall), Lagerbestände,
 Produktionsdaten – wenn kursrelevant für den Derivatepreis
- Besonderheit: Information kann auch aus dem Spotmarkt stammen (Art. 7 Abs. 1 lit. b MAR)
- REMIT: Insiderinformation = „privileged information" zu Kapazitäten, Angebot/Nachfrage,
 Infrastrukturausfällen

### Schritt 3 – Marktmanipulation

- MAR Art. 12: Verboten sind künstliche Preisgestaltung durch Cornering, Squeezing, Wash Trading
- REMIT: Eigenes Marktmanipulationsverbot (Art. 5 REMIT), deckt auch Verhaltensweisen ab,
 die den Erwartungen von Marktteilnehmern widersprechen
- Capacity Withholding: Zurückhalten von Energiekapazitäten zur Preisbeeinflussung = REMIT-Verstoß

### Schritt 4 – Meldepflichten

- MAR: Ad-hoc-Pflicht für börsennotierte Emittenten
- REMIT: Transaction Reporting an ACER (Agentur für die Zusammenarbeit der Energieregulierungsbehörden)
- REMIT: Insider Information Disclosure-Pflicht (vergleichbar Art. 17 MAR)

### Schritt 5 – Compliance-Empfehlungen für Energie-Trader

- Klare Trennung zwischen Informationen aus kommerzieller Tätigkeit (Spot-Markt) und
 Derivate-Handelsabteilung (Chinese Walls)
- REMIT-Compliance-Programm: Meldewege, Schulungen, Handelssystem-Monitoring
- Regelmäßiges Review: ACER-Guidance und REMIT II-Umsetzung verfolgen

## Red-Team-Fragen

- Ist die Abgrenzung MAR/REMIT für alle gehandelten Produkte klar?
- Gibt es Chinese Walls zwischen kommerzieller Seite und Handelsabteilung?
- Werden REMIT-Meldepflichten (Transaction Reporting, Insider Information) erfüllt?
- Wird Capacity Withholding auf REMIT-Compliance geprüft?

## Ausgabeformat

Erzeuge:
1. Produktmatrix: Warenderivat × MAR-Pflicht × REMIT-Pflicht
2. Insiderinformations-Kategorien für Energiemärkte
3. Chinese-Wall-Konzept für Energie-Trader
4. REMIT-Compliance-Checkliste

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

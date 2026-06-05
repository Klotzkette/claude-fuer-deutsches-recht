---
name: ins-roadshow-dual
description: "INS Roadshow Dual: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INS Roadshow Dual

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **INS Roadshow Dual** im Plugin Insiderrecht / Compliance (WpHG, MAR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ins-033-roadshow` | Sichert Roadshows (Kapitalmarkt, Pre-IPO, M&A) gegen MAR-Risiken: Praesentation-Screening, Selective Disclosure, Insider-Free-Periods und Wall-Crossing. |
| `ins-034-dual-listed-issuer` | Koordiniert MAR-Pflichten fuer Dual-Listed-Emittenten: parallele Ad-hoc-Pflichten, Sprachfassungen, Zeitzonenkonflikte und multiple Regulatoren. |

## Arbeitsweg

Im Plugin Insiderrecht / Compliance (WpHG, MAR) gilt für **INS Roadshow Dual**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ins-033-roadshow`

**Fokus:** Sichert Roadshows (Kapitalmarkt, Pre-IPO, M&A) gegen MAR-Risiken: Praesentation-Screening, Selective Disclosure, Insider-Free-Periods und Wall-Crossing.

# Roadshows – Insiderrechtliche Compliance

## Rechtlicher Rahmen

Roadshows für Kapitalerhöhungen, IPOs oder Anleiheemissionen sind intensive Phase der
Investorenkommunikation, in der Selective Disclosure-Risiken erhöht sind. Art. 10 MAR,
Art. 11 MAR (Market Sounding), Art. 17 MAR und die Vorschriften zur Erstveröffentlichung
müssen gleichzeitig eingehalten werden. Für IPOs gilt zudem die EU-Prospektverordnung.

Rechtsgrundlagen:
- Art. 10, 11, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EU-Prospektverordnung (EU) 2017/1129: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1129
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill sichert den gesamten Roadshow-Prozess gegen MAR-Verstöße: von der
Präsentationsfreigabe bis zum Post-Roadshow-Compliance-Report.

## Arbeitsprogramm

### Schritt 1 – Präsentation-Screening

- Alle Präsentationsinhalte müssen vor der Roadshow von Compliance freigegeben werden
- Screening: Enthält die Präsentation Insiderinformationen, die noch nicht veröffentlicht sind?
 Wenn ja: Ad-hoc vor Roadshow-Beginn oder Entfernung der Information
- Nur auf Basis öffentlicher Informationen (Jahresbericht, Ad-hoc, Prospekt) kommunizieren

### Schritt 2 – Roadshow-Teilnehmer und Insiderstatus

- Investoren, die im Rahmen von Market Sounding (Art. 11 MAR) Insiderinformationen erhalten:
 Wall-Crossing-Prozess nach Skill ins-008 einleiten
- Investoren in reiner Roadshow (auf Basis öffentlicher Informationen): Kein Insiderstatus
- Trenne klar zwischen Market Sounding und Roadshow

### Schritt 3 – Free-Period-Prüfung

- Liegt die Roadshow in einer Closed Period? → Keine Eigengeschäfte der PDMRs
- Liegt eine aktuelle Insiderinformation vor? → Roadshow absagen oder auf rein
 öffentliche Informationen beschränken

### Schritt 4 – Q&A-Management

- Keine Antworten auf Fragen, die Insiderinformationen bestätigen oder nahelegen
- Standard-Antwort: „Wir kommentieren Marktgerüchte nicht"
- Alle Q&A-Sessions protokollieren (Fragen und Antworten)

### Schritt 5 – Post-Roadshow-Review

- Hat IR versehentlich kursrelevante Informationen kommuniziert?
- Wenn ja: Sofortige Ad-hoc-Pflicht prüfen
- Protokolle aufbewahren (5 Jahre)
- Nächste Roadshow: Learnings aus Compliance-Review einarbeiten

## Red-Team-Fragen

- Wurde die Präsentation vor der Roadshow von Compliance freigegeben?
- Gibt es eine klare Trennung zwischen Market Sounding und Roadshow-Teilnehmern?
- Liegt die Roadshow in einer Closed Period oder Insiderphase?
- Wurden Q&A-Sessions protokolliert und auf Selective Disclosure geprüft?

## Ausgabeformat

Erzeuge:
1. Präsentations-Screening-Checkliste
2. Roadshow-Teilnehmer-Matrix (Sounding vs. öffentlich vs. Wall-Crossing-Status)
3. Q&A-Protokollvorlage
4. Post-Roadshow-Compliance-Report

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Bei IPO-Roadshows gelten zusätzlich die Anforderungen der EU-Prospektverordnung
(EU) 2017/1129: Der Prospekt muss vor dem Beginn des öffentlichen Angebots veröffentlicht
sein. Informationen in der Roadshow-Präsentation dürfen nicht wesentlich über den Prospektinhalt
hinausgehen, es sei denn, ein Nachtrag wird veröffentlicht. Compliance muss Präsentation
und Prospekt auf Kohärenz prüfen. Bei Abweichungen: Nachtrags-Prospekt erforderlich.

Weitere Quellen:
- EU-Prospektverordnung (EU) 2017/1129: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1129
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## 2. `ins-034-dual-listed-issuer`

**Fokus:** Koordiniert MAR-Pflichten fuer Dual-Listed-Emittenten: parallele Ad-hoc-Pflichten, Sprachfassungen, Zeitzonenkonflikte und multiple Regulatoren.

# Dual-Listed-Emittent – Parallele MAR-Pflichten

## Rechtlicher Rahmen

Emittenten, die an mehreren regulierten Märkten in verschiedenen EU-Mitgliedstaaten oder
auch in Drittstaaten notiert sind (Dual Listing), unterliegen den MAR-Pflichten des
Herkunftsmitgliedstaats (Home Member State). Bei Zusatzlistings außerhalb der EU gelten
zusätzlich lokale Marktmissbrauchsregeln (z. B. SEC-Rules in den USA, FCA MAR in UK).
DVO (EU) 2016/1055 regelt Sprachfassungen.

Rechtsgrundlagen:
- Art. 20 MAR (Sprachfassungen): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 2 MAR (Herkunftsstaat): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/1055: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1055
- BaFin-Emittentenleitfaden Kap. VIII: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill koordiniert die parallelen Veröffentlichungspflichten für Dual-Listed-Emittenten
und stellt sicher, dass Ad-hoc-Mitteilungen gleichzeitig in allen relevanten Ländern
veröffentlicht werden.

## Arbeitsprogramm

### Schritt 1 – Home Member State und Primärregulator

- Bestimme den Home Member State (i.d.R. Staat des Gesellschaftssitzes oder Staat der
 ersten Notierung in der EU)
- BaFin als Primärregulator für deutsche Emittenten (§ 4 WpHG)
- Identifiziere sekundäre Regulatoren für jedes weitere Listing (FCA, AMF, SEC, etc.)

### Schritt 2 – Parallele Ad-hoc-Pflichten

- MAR Ad-hoc nach Art. 17 MAR an BaFin und EU-Handelsplätze
- UK MAR (nach Brexit): Separate Pflicht nach FCA DTR
- US SEC: Form 6-K oder Form 8-K je nach Registrierungsstandard
- Koordination: Alle Veröffentlichungen möglichst simultan (Zeitzonenmanagement!)

### Schritt 3 – Sprachfassungen

- Herkunftsstaat: Pflicht in Amtssprache (Deutsch)
- Weitere Handelsplätze: Landessprache oder Englisch (Art. 20 MAR)
- Übersetzungen müssen inhaltlich identisch sein
- Frühzeitige Übersetzungskoordination (im Krisenfall: Maschinenübersetzung + Jurist-Review)

### Schritt 4 – Zeitzonenkonflikte

- NYSE/NASDAQ: Handelszeit 15:30–22:00 Uhr CET
- Veröffentlichung außerhalb EU-Handelszeiten: Koordination mit US-Counsel
- Übliche Lösung: Ad-hoc vor Marktöffnung in der jurisdiktion mit frühester Öffnungszeit

### Schritt 5 – Insiderlisten und Directors' Dealings

- DVO (EU) 2016/347 gilt für EU-Seite; andere Länder haben ggf. eigene Formate
- Directors' Dealings: Meldung nach Art. 19 MAR an BaFin; in UK nach DTR 3; in USA nach
 Section 16 Exchange Act (Form 4)
- Abstimmung der Meldefristen (Deutschland: 3 Geschäftstage; USA: 2 Werktage)

## Red-Team-Fragen

- Wurden alle relevanten Regulatoren identifiziert und Meldewege eingerichtet?
- Werden Ad-hoc-Mitteilungen wirklich simultan in allen Ländern veröffentlicht?
- Sind Sprachfassungen inhaltlich identisch?
- Werden Directors' Dealings in allen relevanten Jurisdiktionen gemeldet?
- Ist der Herkunftsstaat korrekt bestimmt?

## Ausgabeformat

Erzeuge:
1. Dual-Listing-Jurisdiktionsmatrix (Land × Regulator × Pflichten × Frist)
2. Ad-hoc-Koordinationsplan (Zeitzonenplan für simultane Veröffentlichung)
3. Sprachfassungen-Checkliste
4. Directors'-Dealings-Matrix (Land × Format × Frist)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

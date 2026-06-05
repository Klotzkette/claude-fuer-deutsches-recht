---
name: foreign-creditor-fraudulent-lbo-transfers
description: "Foreign Creditor Fraudulent LBO Transfers: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Foreign Creditor Fraudulent LBO Transfers

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Foreign Creditor Fraudulent LBO Transfers** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `foreign-creditor-german-client` | Fuehrt deutsche Gläubiger durch US-Bankruptcy: notice, claim, stay, contract, committee, plan vote and distributions. |
| `fraudulent-lbo` | Prueft leveraged buyout fraudulent-transfer exposure, solvency, reasonably equivalent value and lender/recipient targets. |
| `fraudulent-transfers-548` | Prueft actual and constructive fraudulent transfers, two-year lookback, value, insolvency and insider transactions. |
| `free-clear-sale-363f` | Prueft sale free and clear of interests, liens attaching to proceeds, consent, bona fide dispute and statutory bases. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **Foreign Creditor Fraudulent LBO Transfers**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `foreign-creditor-german-client`

**Fokus:** Fuehrt deutsche Gläubiger durch US-Bankruptcy: notice, claim, stay, contract, committee, plan vote and distributions.

# Foreign Creditor German Client

## Fachkern: Foreign Creditor German Client
- **Spezialgegenstand:** Foreign Creditor German Client wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Foreign Creditor German Client** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 362, 501, 1126
- U.S. Courts forms
- Case docket/PACER


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What notice received?
- Claim type and amount?
- Need local counsel?
- Contract or shipment pending?


## Workflow

1. Notice translate.
2. Claim and deadline map.
3. Stay-safe communication plan.


## Output

- German creditor memo
- Proof-of-claim checklist
- Plan voting note


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welches ausländische Verfahren soll anerkannt werden und ist der foreign representative sauber legitimiert?
- Welche Tatsachen tragen COMI, establishment, foreign main/nonmain proceeding und notice?
- Welche relief wird sofort gebraucht: stay, discovery, asset turnover, cooperation, entrustment oder injunction?
- Gibt es public-policy, due-process, Datenschutz- oder Konzernstrukturthemen, die US-Counsel vorab kennen muss?

**Mindest-Output:** Chapter-15-Paket mit COMI-Belegen, Vertreterlegitimation, Relief-Liste und Notice-Plan.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 2. `fraudulent-lbo`

**Fokus:** Prueft leveraged buyout fraudulent-transfer exposure, solvency, reasonably equivalent value and lender/recipient targets.

# Fraudulent Conveyance LBO

## Fachkern: Fraudulent Conveyance LBO
- **Spezialgegenstand:** Fraudulent Conveyance LBO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Fraudulent Conveyance LBO** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 544, 548, 550
- State fraudulent transfer law
- Deal and solvency files


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Transaction structure?
- Solvency at closing?
- Who received value?


## Workflow

1. Funds flow map.
2. Solvency and value evidence.
3. Targets and defenses.


## Output

- LBO avoidance memo
- Funds-flow table
- Solvency evidence list


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Zahlung, Übertragung oder Sicherheit liegt in welchem lookback period und zugunsten welcher Partei?
- War die Leistung antecedent debt, new value, ordinary course, contemporaneous exchange oder insider-bezogen?
- Welche State-law- oder bankruptcy-law avoidance route ist realistisch und wer trägt praktisch die Beweislast?
- Welche Verteidigungsakten fehlen noch: invoices, payment history, shipment logs, solvency material, board papers?

**Mindest-Output:** Avoidance-Analyse mit Transferliste, Zeitachse, Defenses, Vergleichswert und Litigation-Risiko.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `fraudulent-transfers-548`

**Fokus:** Prueft actual and constructive fraudulent transfers, two-year lookback, value, insolvency and insider transactions.

# Fraudulent Transfers § 548

## Fachkern: Fraudulent Transfers § 548
- **Spezialgegenstand:** Fraudulent Transfers § 548 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Fraudulent Transfers § 548** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 548
- 11 U.S.C. § 550
- State fraudulent transfer law interface


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What transfer/obligation?
- Actual intent badges?
- Reasonably equivalent value?
- Financial condition?


## Workflow

1. Transfer timeline.
2. Value and insolvency evidence.
3. State-law and § 544 overlay markieren.


## Output

- Fraudulent-transfer memo
- Badges table
- Recovery target list


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Zahlung, Übertragung oder Sicherheit liegt in welchem lookback period und zugunsten welcher Partei?
- War die Leistung antecedent debt, new value, ordinary course, contemporaneous exchange oder insider-bezogen?
- Welche State-law- oder bankruptcy-law avoidance route ist realistisch und wer trägt praktisch die Beweislast?
- Welche Verteidigungsakten fehlen noch: invoices, payment history, shipment logs, solvency material, board papers?

**Mindest-Output:** Avoidance-Analyse mit Transferliste, Zeitachse, Defenses, Vergleichswert und Litigation-Risiko.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 4. `free-clear-sale-363f`

**Fokus:** Prueft sale free and clear of interests, liens attaching to proceeds, consent, bona fide dispute and statutory bases.

# Free and Clear Sale § 363(f)

## Fachkern: Free and Clear Sale § 363(f)
- **Spezialgegenstand:** Free and Clear Sale § 363(f) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Free and Clear Sale § 363(f)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 363(f)
- 11 U.S.C. § 363(m)
- Sale order practice


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What interests attach?
- Which § 363(f) ground for each?
- Good-faith purchaser issues?


## Workflow

1. Interest/lien schedule bauen.
2. Basis per interest prüfen.
3. Order language and appeal risk markieren.


## Output

- Free-and-clear matrix
- Sale order issue list
- Appeal-risk memo


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Ist ein § 363 sale wirklich schneller und besser als plan sale, workout oder going-concern financing?
- Welche assets, liens, cure amounts, executory contracts, approvals und buyer protections sind betroffen?
- Sind bidding procedures, break-up fee, credit bid, adequate notice und good-faith finding sauber vorbereitet?
- Welche deutschen Beteiligten brauchen Übersetzung: Käufer, Verkäufer, Kreditgeber, Betriebsrat, Datenschutz, Kartellrecht?

**Mindest-Output:** Sale-Chart mit assets, liens, bidder protections, objections, approvals und closing deliverables.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

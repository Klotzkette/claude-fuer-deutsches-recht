---
name: chapter15-comity-recognition-claim-objection
description: "Chapter15 Comity Recognition Claim Objection: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Chapter15 Comity Recognition Claim Objection

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Chapter15 Comity Recognition Claim Objection** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `chapter15-comity-relief` | Prueft post-recognition relief, cooperation, entrustment, asset turnover, discovery and public-policy exception. |
| `chapter15-recognition` | Prueft recognition of foreign proceedings, foreign main/nonmain, COMI, foreign representative and relief. |
| `claim-objection-502` | Prueft allowance/disallowance, objections, estimation, contingent/unliquidated claims and settlement. |
| `claims-proof-claim-501` | Prueft claim filing, bar date, secured/unsecured/priority status, documentation and amendments. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **Chapter15 Comity Recognition Claim Objection**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `chapter15-comity-relief`

**Fokus:** Prueft post-recognition relief, cooperation, entrustment, asset turnover, discovery and public-policy exception.

# Chapter 15 Comity and Relief

## Fachkern: Chapter 15 Comity and Relief
- **Spezialgegenstand:** Chapter 15 Comity and Relief wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 15 Comity and Relief** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 1506, 1521, 1525-1527
- Foreign court orders


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What relief needed in U.S.?
- Any creditor prejudice?
- Public policy concern?


## Workflow

1. Relief under §§ 1520/1521 classify.
2. Comity and protection of creditors.
3. Coordination with foreign court.


## Output

- Chapter 15 relief memo
- Comity issue list
- Protective order checklist


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

## 2. `chapter15-recognition`

**Fokus:** Prueft recognition of foreign proceedings, foreign main/nonmain, COMI, foreign representative and relief.

# Chapter 15 Recognition

## Fachkern: Chapter 15 Recognition
- **Spezialgegenstand:** Chapter 15 Recognition wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 15 Recognition** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 1501-1532
- UNCITRAL Model Law background
- Foreign proceeding documents


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Foreign proceeding type?
- Foreign representative authorized?
- COMI and establishment?


## Workflow

1. Recognition petition package.
2. COMI evidence.
3. Relief and notice plan.


## Output

- Chapter 15 recognition memo
- COMI evidence list
- Relief checklist


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

## 3. `claim-objection-502`

**Fokus:** Prueft allowance/disallowance, objections, estimation, contingent/unliquidated claims and settlement.

# Claim Objection § 502

## Fachkern: Claim Objection § 502
- **Spezialgegenstand:** Claim Objection § 502 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Claim Objection § 502** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 502
- Bankruptcy Rules contested matters
- 11 U.S.C. § 105 if relevant


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Why object?
- Claim documentation, amount, priority?
- Need estimation for plan?


## Workflow

1. Objection grounds mappen.
2. Evidence and burden issues.
3. Settlement/estimation route prüfen.


## Output

- Claim objection outline
- Evidence matrix
- Estimation memo


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Forderung ist secured, priority, administrative, unsecured, contingent, unliquidated oder disputed?
- Welche Unterlagen beweisen Entstehung, Betrag, Fälligkeit, collateral, guarantee und mögliche Einreden?
- Gibt es bar date, amendment risk, claim objection, estimation oder setoff/recoupment?
- Welche Behandlung droht im Plan oder in der Verteilung, und lohnt sich eine aktive objection/negotiation?

**Mindest-Output:** Claims-Tabelle mit Status, Belegen, Rang, Einwendungen, Frist und Plan-/Distribution-Auswirkung.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 4. `claims-proof-claim-501`

**Fokus:** Prueft claim filing, bar date, secured/unsecured/priority status, documentation and amendments.

# Proof of Claim § 501

## Fachkern: Proof of Claim § 501
- **Spezialgegenstand:** Proof of Claim § 501 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Proof of Claim § 501** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 501, 502
- Official Form 410
- Bankruptcy Rules


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Who is creditor?
- Claim amount, basis, collateral, priority?
- Bar date and supporting documents?


## Workflow

1. Claim classify.
2. Evidence attach.
3. Bar-date and amendment risk prüfen.


## Output

- Proof-of-claim checklist
- Claim classification memo
- Bar-date tracker


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Forderung ist secured, priority, administrative, unsecured, contingent, unliquidated oder disputed?
- Welche Unterlagen beweisen Entstehung, Betrag, Fälligkeit, collateral, guarantee und mögliche Einreden?
- Gibt es bar date, amendment risk, claim objection, estimation oder setoff/recoupment?
- Welche Behandlung droht im Plan oder in der Verteilung, und lohnt sich eine aktive objection/negotiation?

**Mindest-Output:** Claims-Tabelle mit Status, Belegen, Rang, Einwendungen, Frist und Plan-/Distribution-Auswirkung.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

---
name: tax-claims-title11-map-trustee-turnover
description: "TAX Claims Title11 MAP Trustee Turnover: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TAX Claims Title11 MAP Trustee Turnover

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **TAX Claims Title11 MAP Trustee Turnover** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tax-claims` | Prueft tax claims, priority, secured tax liens, dischargeability, returns, plan treatment and refunds. |
| `title11-map-chapters` | Kartiert Title 11 Chapters 1/3/5/7/9/11/12/13/15 mit Rollen, Zielen und Schnittstellen. |
| `trustee-us-trustee-roles` | Erklaert Chapter trustee, U.S. Trustee, bankruptcy administrator, DIP, examiner and oversight functions. |
| `turnover-542` | Prueft turnover of estate property, records, account funds, collateral and foreign holder issues. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **TAX Claims Title11 MAP Trustee Turnover**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tax-claims`

**Fokus:** Prueft tax claims, priority, secured tax liens, dischargeability, returns, plan treatment and refunds.

# Tax Claims in Bankruptcy

## Fachkern: Tax Claims in Bankruptcy
- **Spezialgegenstand:** Tax Claims in Bankruptcy wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Tax Claims in Bankruptcy** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 507(a)(8), 523(a)(1), 724, 1129(a)(9)
- IRS/state tax sources


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Tax type and period?
- Return filed timely?
- Lien filed?
- Refunds?


## Workflow

1. Tax claim classify.
2. Priority/dischargeability.
3. Plan treatment and objection.


## Output

- Tax claim memo
- Tax period table
- Plan treatment checklist


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

## 2. `title11-map-chapters`

**Fokus:** Kartiert Title 11 Chapters 1/3/5/7/9/11/12/13/15 mit Rollen, Zielen und Schnittstellen.

# Title 11 Chapters Map

## Fachkern: Title 11 Chapters Map
- **Spezialgegenstand:** Title 11 Chapters Map wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Title 11 Chapters Map** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. Chapters 1, 3, 5, 7, 9, 11, 12, 13, 15
- U.S. Trustee overview


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Welche Art debtor?
- Liquidation, reorganization, wage earner, municipality, family farmer or foreign proceeding?
- Welche chapter-specific bar?


## Workflow

1. Chapter taxonomy erklären.
2. Eligibility and procedural route prüfen.
3. Falsche Analogien zum deutschen Insolvenzrecht markieren.


## Output

- Chapter selection chart
- Eligibility questions
- Comparison note


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Rolle, welches Chapter, welcher procedural posture und welches unmittelbare Ziel bestimmen die erste Weiche?
- Welche Code-Anker, Local Rules, Orders, Forms und docket events müssen vor einer Aussage live geprüft werden?
- Welche deutschen Erwartungen sind gefährlich, weil US-Bankruptcy stärker court-driven, motion-driven und notice-driven arbeitet?
- Welche Frage ist für US-Counsel offen zu markieren statt aus deutschem Insolvenzrecht zu übertragen?

**Mindest-Output:** Kurz-Memo mit procedural posture, Code-Ankern, Dokumentenlücken und US-Counsel-Issue-Liste.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `trustee-us-trustee-roles`

**Fokus:** Erklaert Chapter trustee, U.S. Trustee, bankruptcy administrator, DIP, examiner and oversight functions.

# Trustee and U.S. Trustee Roles

## Fachkern: Trustee and U.S. Trustee Roles
- **Spezialgegenstand:** Trustee and U.S. Trustee Roles wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Trustee and U.S. Trustee Roles** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 307, 321-326, 1104
- U.S. Trustee Program official resources


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Who controls debtor?
- Is trustee appointment sought?
- What oversight/reporting duties?


## Workflow

1. Role map erstellen.
2. Reporting and meeting duties erfassen.
3. Escalation to UST or trustee markieren.


## Output

- Role chart
- Oversight checklist
- Communication protocol


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Rolle, welches Chapter, welcher procedural posture und welches unmittelbare Ziel bestimmen die erste Weiche?
- Welche Code-Anker, Local Rules, Orders, Forms und docket events müssen vor einer Aussage live geprüft werden?
- Welche deutschen Erwartungen sind gefährlich, weil US-Bankruptcy stärker court-driven, motion-driven und notice-driven arbeitet?
- Welche Frage ist für US-Counsel offen zu markieren statt aus deutschem Insolvenzrecht zu übertragen?

**Mindest-Output:** Kurz-Memo mit procedural posture, Code-Ankern, Dokumentenlücken und US-Counsel-Issue-Liste.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 4. `turnover-542`

**Fokus:** Prueft turnover of estate property, records, account funds, collateral and foreign holder issues.

# Turnover § 542

## Fachkern: Turnover § 542
- **Spezialgegenstand:** Turnover § 542 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Turnover § 542** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 542
- 11 U.S.C. § 541
- Adversary/contested practice


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Who holds property?
- Is it estate property?
- Disputed ownership or setoff?


## Workflow

1. Property interest prüfen.
2. Demand and motion/adversary route.
3. Foreign holder enforcement issue markieren.


## Output

- Turnover demand outline
- Property evidence list
- Proceeding route memo


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Rolle, welches Chapter, welcher procedural posture und welches unmittelbare Ziel bestimmen die erste Weiche?
- Welche Code-Anker, Local Rules, Orders, Forms und docket events müssen vor einer Aussage live geprüft werden?
- Welche deutschen Erwartungen sind gefährlich, weil US-Bankruptcy stärker court-driven, motion-driven und notice-driven arbeitet?
- Welche Frage ist für US-Counsel offen zu markieren statt aus deutschem Insolvenzrecht zu übertragen?

**Mindest-Output:** Kurz-Memo mit procedural posture, Code-Ankern, Dokumentenlücken und US-Counsel-Issue-Liste.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

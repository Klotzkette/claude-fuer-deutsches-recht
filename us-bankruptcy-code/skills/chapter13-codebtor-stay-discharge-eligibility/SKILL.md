---
name: chapter13-codebtor-stay-discharge-eligibility
description: "Chapter13 Codebtor Stay Discharge Eligibility: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Chapter13 Codebtor Stay Discharge Eligibility

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Chapter13 Codebtor Stay Discharge Eligibility** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `chapter13-codebtor-stay` | Prueft co-debtor stay, consumer debts, relief motions and guarantor/co-signer strategy. |
| `chapter13-discharge` | Prueft Chapter 13 discharge, hardship discharge, exceptions, plan completion and post-discharge issues. |
| `chapter13-eligibility` | Prueft Chapter 13 debt limits, regular income, individual-only requirement and consumer/small-business owner issues. |
| `chapter13-plan` | Prueft Chapter 13 plan, disposable income, best interests, secured claims, arrears, trustee payments and feasibility. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **Chapter13 Codebtor Stay Discharge Eligibility**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `chapter13-codebtor-stay`

**Fokus:** Prueft co-debtor stay, consumer debts, relief motions and guarantor/co-signer strategy.

# Chapter 13 Co-Debtor Stay

## Fachkern: Chapter 13 Co-Debtor Stay
- **Spezialgegenstand:** Chapter 13 Co-Debtor Stay wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 13 Co-Debtor Stay** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 1301
- 11 U.S.C. § 362
- Creditor docs


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Consumer debt?
- Co-debtor liable?
- Plan proposes full payment?


## Workflow

1. Co-debtor stay applicability.
2. Relief grounds.
3. Communication with co-obligor.


## Output

- Co-debtor stay memo
- Relief motion issues
- Creditor action checklist


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche konkrete Handlung ist betroffen: Klage, Vollstreckung, Setoff, Kündigung, lien perfection, discovery oder Zahlungseinzug?
- Ist die Handlung gegen den debtor, gegen estate property, gegen Dritte oder gegen guarantors/co-debtors gerichtet?
- Gibt es eine ausdrückliche Ausnahme, eine comfort order, stay relief oder nur ein operatives Missverständnis?
- Welche Sofortmaßnahme verhindert Sanktionen: stop notice, docket check, US-counsel call, motion oder Dokumentationsvermerk?

**Mindest-Output:** Stay-Matrix mit Handlung, betroffenem Rechtsträger, Code-Anker, Risiko und nächstem Schritt.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 2. `chapter13-discharge`

**Fokus:** Prueft Chapter 13 discharge, hardship discharge, exceptions, plan completion and post-discharge issues.

# Chapter 13 Discharge

## Fachkern: Chapter 13 Discharge
- **Spezialgegenstand:** Chapter 13 Discharge wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 13 Discharge** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 1328, 523
- Court notices/forms


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Plan complete?
- Domestic support/tax certifications?
- Any exceptions?


## Workflow

1. Discharge prerequisites.
2. Remaining debts classify.
3. Post-discharge injunction issues.


## Output

- Chapter 13 discharge memo
- Certification checklist
- Creditor violation note


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Geht es um liquidation estate, trustee powers, exemptions, discharge oder nondischargeability?
- Welche assets, claims, litigation rights, insurance, tax refunds und preferences können in die estate fallen?
- Welche discharge objections, fraud indicators, schedules inconsistencies oder means-test issues sind sichtbar?
- Welche Handlung eines deutschen Gläubigers wäre stay-kritisch oder muss über proof of claim/adversary laufen?

**Mindest-Output:** Chapter-7-Aktenblatt mit estate assets, discharge issues, trustee questions und creditor route.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `chapter13-eligibility`

**Fokus:** Prueft Chapter 13 debt limits, regular income, individual-only requirement and consumer/small-business owner issues.

# Chapter 13 Eligibility

## Fachkern: Chapter 13 Eligibility
- **Spezialgegenstand:** Chapter 13 Eligibility wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 13 Eligibility** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 109(e), 101(30)
- U.S. Courts Chapter 13 Basics
- Official Forms


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Individual with regular income?
- Debt limits current?
- Secured/unsecured classification?


## Workflow

1. Eligibility data collect.
2. Debt limits live prüfen.
3. Chapter 7/11 alternatives.


## Output

- Chapter 13 eligibility memo
- Debt table
- Alternative route note


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Ist der debtor eligible, hat regular income und liegen debt limits/form requirements aktuell vor?
- Wie werden arrears, secured claims, priority claims, disposable income und plan payments behandelt?
- Gibt es co-debtor stay, mortgage cure, vehicle cramdown, tax debt oder domestic support obligations?
- Welche bar dates, trustee objections und confirmation conditions sind praktisch entscheidend?

**Mindest-Output:** Chapter-13-Plancheck mit Einnahmen, Zahlungsplan, claim treatment, trustee issues und discharge risks.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 4. `chapter13-plan`

**Fokus:** Prueft Chapter 13 plan, disposable income, best interests, secured claims, arrears, trustee payments and feasibility.

# Chapter 13 Plan Confirmation

## Fachkern: Chapter 13 Plan Confirmation
- **Spezialgegenstand:** Chapter 13 Plan Confirmation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 13 Plan Confirmation** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 1322, 1325
- Official Chapter 13 Plan forms/local forms


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Plan length and income?
- Mortgage/car arrears?
- Priority claims?


## Workflow

1. Plan payment calculation.
2. Claim treatment review.
3. Feasibility and objections.


## Output

- Chapter 13 plan checklist
- Payment matrix
- Objection response


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Klassen, impairment, voting thresholds, releases, injunctions und objections entscheiden den Plan?
- Ist disclosure ausreichend: assets, liabilities, projections, liquidation analysis, feasibility und risk factors?
- Drohen absolute-priority, unfair discrimination, best-interests oder good-faith-Probleme?
- Welche deutsche Sicht braucht das Team: Gläubigerposition, Konzerninteressen, Steuern, Sicherheiten, Governance?

**Mindest-Output:** Plan-Roadmap mit class chart, voting status, confirmation issues, objections und negotiation levers.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

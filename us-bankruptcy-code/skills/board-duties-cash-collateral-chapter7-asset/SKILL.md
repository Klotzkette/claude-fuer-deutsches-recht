---
name: board-duties-cash-collateral-chapter7-asset
description: "Board Duties Cash Collateral Chapter7 Asset: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Board Duties Cash Collateral Chapter7 Asset

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Board Duties Cash Collateral Chapter7 Asset** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `board-duties-zone` | Prueft US board duties near insolvency, fiduciary risk, filing decision, lender pressure and restructuring alternatives. |
| `cash-collateral-363` | Prueft cash collateral, lender consent, adequate protection, budget, reporting and interim/final orders. |
| `chapter7-asset-distribution` | Prueft asset liquidation, sale, abandoned property, claims waterfall, trustee commissions and closing. |
| `chapter7-liquidation` | Fuehrt durch Chapter 7 liquidation: trustee, estate, assets, claims, exemptions, discharge and distribution. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **Board Duties Cash Collateral Chapter7 Asset**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `board-duties-zone`

**Fokus:** Prueft US board duties near insolvency, fiduciary risk, filing decision, lender pressure and restructuring alternatives.

# Board Duties and Zone of Insolvency

## Fachkern: Board Duties and Zone of Insolvency
- **Spezialgegenstand:** Board Duties and Zone of Insolvency wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Board Duties and Zone of Insolvency** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- State corporate law via US counsel
- 11 U.S.C. filing options
- D&O/insurance docs


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Entity state of incorporation?
- Insolvency indicators?
- Board process and conflicts?


## Workflow

1. Decision record build.
2. Alternatives and advisor input.
3. D&O and conflicts.


## Output

- Board briefing
- Decision record checklist
- Fiduciary issue list


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

## 2. `cash-collateral-363`

**Fokus:** Prueft cash collateral, lender consent, adequate protection, budget, reporting and interim/final orders.

# Cash Collateral § 363

## Fachkern: Cash Collateral § 363
- **Spezialgegenstand:** Cash Collateral § 363 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Cash Collateral § 363** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 363(c)
- 11 U.S.C. § 361
- Bankruptcy Rules


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Is cash collateral present?
- Secured party consent?
- 13-week budget?


## Workflow

1. Collateral and lien claims prüfen.
2. Budget and reporting terms bauen.
3. Adequate protection terms verhandeln.


## Output

- Cash collateral memo
- Budget checklist
- Order issue list


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Wird nur Liquidität gesichert oder wird über milestones, roll-up, liens und covenants faktisch die Restrukturierung gesteuert?
- Welche collateral base existiert und wie wird value erosion belegt oder bestritten?
- Braucht es priming, replacement liens, superpriority, budget carve-out oder nur consent use of cash collateral?
- Sind deutsche Kreditgeber, Sicherheiten oder Konzerncashpools betroffen, die US-Counsel kennen muss?

**Mindest-Output:** Finanzierungs-Memo mit Budget, Sicherheitenrang, adequate-protection-Paket und Verhandlungshebeln.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `chapter7-asset-distribution`

**Fokus:** Prueft asset liquidation, sale, abandoned property, claims waterfall, trustee commissions and closing.

# Chapter 7 Assets and Distribution

## Fachkern: Chapter 7 Assets and Distribution
- **Spezialgegenstand:** Chapter 7 Assets and Distribution wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 7 Assets and Distribution** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 541, 554, 704, 726
- 11 U.S.C. § 326
- Claims register


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Which assets administered?
- Sale/abandonment?
- Allowed claims and priorities?


## Workflow

1. Asset realization table.
2. Distribution waterfall.
3. Closing issues.


## Output

- Distribution memo
- Asset liquidation tracker
- Trustee questions


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

## 4. `chapter7-liquidation`

**Fokus:** Fuehrt durch Chapter 7 liquidation: trustee, estate, assets, claims, exemptions, discharge and distribution.

# Chapter 7 Liquidation Workflow

## Fachkern: Chapter 7 Liquidation Workflow
- **Spezialgegenstand:** Chapter 7 Liquidation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Chapter 7 Liquidation Workflow** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. Chapter 7
- U.S. Courts Chapter 7 Basics
- Chapter 5 cross-cutting provisions


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Individual or business?
- Asset or no-asset?
- Secured claims and exemptions?


## Workflow

1. Chapter 7 route map.
2. Trustee and asset tasks.
3. Distribution/discharge timeline.


## Output

- Chapter 7 workflow
- Asset case checklist
- Creditor action list


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

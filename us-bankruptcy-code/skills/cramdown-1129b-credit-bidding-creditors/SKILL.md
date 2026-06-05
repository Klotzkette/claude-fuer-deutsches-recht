---
name: cramdown-1129b-credit-bidding-creditors
description: "Cramdown 1129b Credit Bidding Creditors: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Cramdown 1129b Credit Bidding Creditors

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Cramdown 1129b Credit Bidding Creditors** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cramdown-1129b` | Prueft fair and equitable, no unfair discrimination, secured creditor treatment and impaired dissenting classes. |
| `credit-bidding-363k` | Prueft secured creditor credit bid rights, cause to limit, lien disputes, plan sale and loan-to-own strategy. |
| `creditors-committee-1102` | Prueft official committee formation, membership, fiduciary role, professionals, information rights and strategy. |
| `critical-vendors` | Prueft critical-vendor payments, necessity doctrine, § 503(b)(9), trade leverage and first-day order risk. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **Cramdown 1129b Credit Bidding Creditors**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cramdown-1129b`

**Fokus:** Prueft fair and equitable, no unfair discrimination, secured creditor treatment and impaired dissenting classes.

# Cramdown § 1129(b)

## Fachkern: Cramdown § 1129(b)
- **Spezialgegenstand:** Cramdown § 1129(b) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Cramdown § 1129(b)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 1129(b)
- Valuation evidence
- Plan waterfall


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Which class rejects?
- Secured/unsecured/interests?
- Plan treatment and value?


## Workflow

1. Rejected class identify.
2. Fair-and-equitable test map.
3. Valuation and waterfall stress test.


## Output

- Cramdown memo
- Waterfall/valuation checklist
- Dissenting class strategy


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

## 2. `credit-bidding-363k`

**Fokus:** Prueft secured creditor credit bid rights, cause to limit, lien disputes, plan sale and loan-to-own strategy.

# Credit Bidding § 363(k)

## Fachkern: Credit Bidding § 363(k)
- **Spezialgegenstand:** Credit Bidding § 363(k) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Credit Bidding § 363(k)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 363(k)
- 11 U.S.C. § 1129(b)(2)(A)
- Loan/lien docs


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Allowed secured claim?
- Lien/value dispute?
- Any cause to limit bid?


## Workflow

1. Lien and claim status.
2. Cause evidence.
3. Sale/plan strategy.


## Output

- Credit bid memo
- Lien dispute checklist
- Auction strategy note


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

## 3. `creditors-committee-1102`

**Fokus:** Prueft official committee formation, membership, fiduciary role, professionals, information rights and strategy.

# Creditors Committee § 1102

## Fachkern: Creditors Committee § 1102
- **Spezialgegenstand:** Creditors Committee § 1102 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Creditors Committee § 1102** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 1102, 1103
- U.S. Trustee practice
- Professional retention rules


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Largest unsecured creditors?
- Conflict or competitor issues?
- Committee goals and budget?


## Workflow

1. Committee eligibility and request prüfen.
2. Professional retention needs erfassen.
3. Information and negotiation strategy bauen.


## Output

- Committee strategy memo
- Member issue list
- Professional retention checklist


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

## 4. `critical-vendors`

**Fokus:** Prueft critical-vendor payments, necessity doctrine, § 503(b)(9), trade leverage and first-day order risk.

# Critical Vendors

## Fachkern: Critical Vendors
- **Spezialgegenstand:** Critical Vendors wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Critical Vendors** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 105, 363, 503(b)(9)
- Local practice only with sources
- Vendor contracts


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Which vendors are truly critical?
- Supply alternatives?
- Prepetition amount and 20-day goods?


## Workflow

1. Vendor criticality prove.
2. Payment cap and conditions.
3. Objection and optics red-team.


## Output

- Critical vendor memo
- Vendor matrix
- Order conditions list


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

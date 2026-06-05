---
name: use-sale-utilities-valuation-enterprise-venue
description: "USE Sale Utilities Valuation Enterprise Venue: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# USE Sale Utilities Valuation Enterprise Venue

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **USE Sale Utilities Valuation Enterprise Venue** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `use-sale-lease-363` | Prueft ordinary/nonordinary use, sale or lease of estate property, notice, business judgment and objections. |
| `utilities-366` | Prueft utility service, adequate assurance, deposits, objections and first-day relief. |
| `valuation-enterprise` | Prueft valuation evidence for plan, cramdown, adequate protection, 363 sale, solvency and fraudulent transfer. |
| `venue-jurisdiction-core` | Prueft Bankruptcy Court jurisdiction, venue, core/non-core, related-to, removal and abstention questions. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **USE Sale Utilities Valuation Enterprise Venue**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `use-sale-lease-363`

**Fokus:** Prueft ordinary/nonordinary use, sale or lease of estate property, notice, business judgment and objections.

# Use, Sale or Lease § 363

## Fachkern: Use, Sale or Lease § 363
- **Spezialgegenstand:** Use, Sale or Lease § 363 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Use, Sale or Lease § 363** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 363(b)-(c)
- Bankruptcy Rules sale procedures
- Local Rules


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Ordinary course or outside?
- What property and value?
- Notice parties and objections?


## Workflow

1. Transaction classify.
2. Business justification and evidence.
3. Approval order scope prüfen.


## Output

- 363 transaction memo
- Notice checklist
- Objection response


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

## 2. `utilities-366`

**Fokus:** Prueft utility service, adequate assurance, deposits, objections and first-day relief.

# Utilities § 366

## Fachkern: Utilities § 366
- **Spezialgegenstand:** Utilities § 366 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Utilities § 366** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 366
- First-day motion practice
- Utility contracts


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Which utilities critical?
- Prepetition arrears?
- Adequate assurance proposal?


## Workflow

1. Utility matrix bauen.
2. Deposit/assurance package.
3. Objection and cutoff risk prüfen.


## Output

- Utilities motion checklist
- Adequate assurance table
- Service risk memo


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Ist der Vertrag executory, lease, IP license, supply agreement, franchise, real-property lease oder utility arrangement?
- Welche cure amounts, defaults, anti-assignment clauses, consent rights und performance burdens bestehen?
- Geht es um assumption, rejection, assignment, adequate assurance oder nur um operative Fortführung?
- Welche Rechte des deutschen Vertragspartners sind durch stay, claims process und US court order begrenzt?

**Mindest-Output:** Contract-Dashboard mit Vertragstyp, § 365-Route, cure, assignment risk und claim consequence.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `valuation-enterprise`

**Fokus:** Prueft valuation evidence for plan, cramdown, adequate protection, 363 sale, solvency and fraudulent transfer.

# Enterprise Valuation

## Fachkern: Enterprise Valuation
- **Spezialgegenstand:** Enterprise Valuation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Enterprise Valuation** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 506, 548, 1129
- Valuation reports
- Financial projections


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Purpose of valuation?
- Method: DCF, comps, liquidation?
- Projection reliability?


## Workflow

1. Valuation purpose define.
2. Inputs and methods stress-test.
3. Sensitivity and expert questions.


## Output

- Valuation critique memo
- Assumption checklist
- Expert questions


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

## 4. `venue-jurisdiction-core`

**Fokus:** Prueft Bankruptcy Court jurisdiction, venue, core/non-core, related-to, removal and abstention questions.

# Venue, Jurisdiction and Core Proceedings

## Fachkern: Venue, Jurisdiction and Core Proceedings
- **Spezialgegenstand:** Venue, Jurisdiction and Core Proceedings wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Venue, Jurisdiction and Core Proceedings** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 28 U.S.C. §§ 1334, 1408, 157 as source anchors
- Bankruptcy Rules live prüfen
- Local Rules


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Wo sitzt debtor/assets/principal place?
- Core proceeding or related litigation?
- Removal from state court?


## Workflow

1. Venue facts sammeln.
2. Core/non-core issue markieren.
3. Forum strategy vorbereiten.


## Output

- Venue memo
- Jurisdiction issue list
- Removal/abstention questions


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

---
name: ip-license-landlord-tenant-mass-tort-means
description: "IP License Landlord Tenant Mass Tort Means: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IP License Landlord Tenant Mass Tort Means

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **IP License Landlord Tenant Mass Tort Means** im Plugin Us Bankruptcy Code. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ip-license-365n` | Prueft licensee rights after rejection, election, royalties, exclusivity and access to embodiments. |
| `landlord-tenant-retail` | Prueft retail cases: store closing, lease rejection/assumption, going-out-of-business sales and landlord claims. |
| `mass-tort-bankruptcy` | Prueft mass tort Chapter 11 issues: claims estimation, channeling, third-party releases, insurance and trust structures. |
| `means-test-707b` | Prueft consumer Chapter 7 means test, abuse presumption, median income and special circumstances. |

## Arbeitsweg

Im Plugin Us Bankruptcy Code gilt für **IP License Landlord Tenant Mass Tort Means**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ip-license-365n`

**Fokus:** Prueft licensee rights after rejection, election, royalties, exclusivity and access to embodiments.

# Intellectual Property License § 365(n)

## Fachkern: Intellectual Property License § 365(n)
- **Spezialgegenstand:** Intellectual Property License § 365(n) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Intellectual Property License § 365(n)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 365(n)
- 11 U.S.C. § 101 intellectual property definition
- IP license documents


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Debtor licensor?
- Covered IP?
- Licensee election needed?
- Source code or embodiments?


## Workflow

1. License classify.
2. Election and payment duties prüfen.
3. German licensee action package erstellen.


## Output

- 365(n) election memo
- IP license checklist
- Notice draft points


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

## 2. `landlord-tenant-retail`

**Fokus:** Prueft retail cases: store closing, lease rejection/assumption, going-out-of-business sales and landlord claims.

# Landlord Tenant and Retail Bankruptcy

## Fachkern: Landlord Tenant and Retail Bankruptcy
- **Spezialgegenstand:** Landlord Tenant and Retail Bankruptcy wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Landlord Tenant and Retail Bankruptcy** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 365, 502(b)(6), 503(b)(9)
- Sale orders
- Lease docs


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- How many stores/leases?
- Assume/reject/sell designations?
- Rent and cure amounts?


## Workflow

1. Lease portfolio map.
2. GOB and sale issues.
3. Landlord claim exposure.


## Output

- Retail bankruptcy memo
- Lease designation tracker
- Landlord claim table


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

## 3. `mass-tort-bankruptcy`

**Fokus:** Prueft mass tort Chapter 11 issues: claims estimation, channeling, third-party releases, insurance and trust structures.

# Mass Tort Bankruptcy

## Fachkern: Mass Tort Bankruptcy
- **Spezialgegenstand:** Mass Tort Bankruptcy wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Mass Tort Bankruptcy** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 105, 502(c), 524(g) where applicable
- Case law only if verified
- Insurance policies


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Nature and scale of tort claims?
- Insurance tower?
- Trust or channeling sought?


## Workflow

1. Claim universe map.
2. Insurance and release issues.
3. Plan feasibility/public policy questions.


## Output

- Mass tort issue memo
- Claims estimation checklist
- Release red flags


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

## 4. `means-test-707b`

**Fokus:** Prueft consumer Chapter 7 means test, abuse presumption, median income and special circumstances.

# Means Test § 707(b)

## Fachkern: Means Test § 707(b)
- **Spezialgegenstand:** Means Test § 707(b) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Means Test § 707(b)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 707(b)
- Official Forms 122A series
- U.S. Trustee means testing data live prüfen


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Consumer debts primarily?
- Household income and size?
- Allowed expenses?


## Workflow

1. Means form data collect.
2. Presumption and rebuttal issues.
3. Conversion/dismissal options.


## Output

- Means-test checklist
- Abuse risk memo
- Alternative chapter note


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

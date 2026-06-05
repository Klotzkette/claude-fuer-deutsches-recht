---
name: pe-fees-expenses-billing-broken-deal-abbruch-ic-memo
description: "PE Fees Expenses Billing Broken Deal Abbruch IC Memo: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE Fees Expenses Billing Broken Deal Abbruch IC Memo

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE Fees Expenses Billing Broken Deal Abbruch IC Memo** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-072-fees-expenses-und-billing` | Prüft Management Fee, Transaction Fee, Broken Deal Costs, Monitoring Fees, Counsel Costs und Allocation. |
| `pe-073-broken-deal-und-abbruch` | Prüft Deal-Abbruch, Exklusivität, Break Fee, Kostentragung, Vertraulichkeit und Datenlöschung. |
| `pe-075-ic-memo-und-entscheidungsvorlage` | Erstellt IC-Memo mit Deal-These, Struktur, Risiken, Schutzmechanismen, offenen Punkten und Beschlussvorschlag. |
| `pe-076-mandantenkommunikation-pe` | Übersetzt komplexe PE-, Credit- und Regulatory-Findings in klare Partner-/Mandantenmails. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE Fees Expenses Billing Broken Deal Abbruch IC Memo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-072-fees-expenses-und-billing`

**Fokus:** Prüft Management Fee, Transaction Fee, Broken Deal Costs, Monitoring Fees, Counsel Costs und Allocation.

# Fees, Expenses und Deal Costs

## Fachkern: Fees, Expenses und Deal Costs
- **Spezialgegenstand:** Fees, Expenses und Deal Costs wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Transparenz gegenüber LPs und saubere Deal-Kostenverteilung.

## Rechts- und Praxisanker

Fondsvertrag, Side Letter, KAGB, Steuer, Kanzlei-Billing.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `pe-073-broken-deal-und-abbruch`

**Fokus:** Prüft Deal-Abbruch, Exklusivität, Break Fee, Kostentragung, Vertraulichkeit und Datenlöschung.

# Broken Deal: Abbruch, Kosten und Haftung

## Fachkern: Broken Deal: Abbruch, Kosten und Haftung
- **Spezialgegenstand:** Broken Deal: Abbruch, Kosten und Haftung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill hilft, aus einem gescheiterten Prozess ohne Folgeschaden herauszukommen.

## Rechts- und Praxisanker

BGB c.i.c., NDA, Process Letter, Datenschutz, Kartellrecht.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 3. `pe-075-ic-memo-und-entscheidungsvorlage`

**Fokus:** Erstellt IC-Memo mit Deal-These, Struktur, Risiken, Schutzmechanismen, offenen Punkten und Beschlussvorschlag.

# Investment Committee Memo

## Fachkern: Investment Committee Memo
- **Spezialgegenstand:** Investment Committee Memo wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf entscheidungsfähige Unterlage statt langer DD-Nacherzählung.

## Rechts- und Praxisanker

Business Judgment, Fondsvertrag, KAGB, SPA/Finanzierung, Compliance.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 4. `pe-076-mandantenkommunikation-pe`

**Fokus:** Übersetzt komplexe PE-, Credit- und Regulatory-Findings in klare Partner-/Mandantenmails.

# Mandantenkommunikation im PE-Deal

## Fachkern: Mandantenkommunikation im PE-Deal
- **Spezialgegenstand:** Mandantenkommunikation im PE-Deal wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill liefert knappe, handlungsorientierte Kommunikation mit Risiken und nächsten Schritten.

## Rechts- und Praxisanker

Berufsrechtliche Sorgfalt, keine Überversprechen, Quellenhygiene.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

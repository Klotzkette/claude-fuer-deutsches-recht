---
name: pe-financial-assistance-upstream-fund-finance-nav-preferred
description: "PE Financial Assistance Upstream Fund Finance NAV Preferred: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE Financial Assistance Upstream Fund Finance NAV Preferred

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE Financial Assistance Upstream Fund Finance NAV Preferred** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-055-financial-assistance-und-upstream` | Prüft, ob Finanzierung/Sicherheiten gegen Kapitalerhaltung, Existenzvernichtung oder Organpflichten laufen. |
| `pe-056-fund-finance-und-nav-facility` | Prüft Subscription Line, NAV Facility, GP Commitment, LP Capital Call Security und Borrowing Limits. |
| `pe-057-preferred-equity-hybrid-finance` | Prüft Preferred Equity, Mezzanine, Wandeldarlehen, Gesellschafterdarlehen und Rangrücktritt. |
| `pe-058-restructuring-waiver-amend-extend` | Begleitet Waiver, Covenant Reset, A&E, Standstill, Super Senior, SFA und Krisenfinanzierung. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE Financial Assistance Upstream Fund Finance NAV Preferred**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-055-financial-assistance-und-upstream`

**Fokus:** Prüft, ob Finanzierung/Sicherheiten gegen Kapitalerhaltung, Existenzvernichtung oder Organpflichten laufen.

# Financial Assistance, Upstream Security und Kapitalerhaltung

## Fachkern: Financial Assistance, Upstream Security und Kapitalerhaltung
- **Spezialgegenstand:** Financial Assistance, Upstream Security und Kapitalerhaltung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill ist zentral für LBO, Dividend Recap und Refinancing.

## Rechts- und Praxisanker

GmbHG § 30, AktG Kapitalerhaltung, BGB, InsO, Geschäftsleiterhaftung.

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

## 2. `pe-056-fund-finance-und-nav-facility`

**Fokus:** Prüft Subscription Line, NAV Facility, GP Commitment, LP Capital Call Security und Borrowing Limits.

# Fund Finance und NAV Facility

## Fachkern: Fund Finance und NAV Facility
- **Spezialgegenstand:** Fund Finance und NAV Facility wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Fondsvertrag, LP-Rechte und Kreditgeber-Due-Diligence.

## Rechts- und Praxisanker

KAGB, Fondsvertrag, Sicherheiten, Datenschutz, Side Letters.

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

## 3. `pe-057-preferred-equity-hybrid-finance`

**Fokus:** Prüft Preferred Equity, Mezzanine, Wandeldarlehen, Gesellschafterdarlehen und Rangrücktritt.

# Preferred Equity und hybride Finanzierung

## Fachkern: Preferred Equity und hybride Finanzierung
- **Spezialgegenstand:** Preferred Equity und hybride Finanzierung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill hilft bei Lücken zwischen klassischem Equity und Debt.

## Rechts- und Praxisanker

BGB, GmbHG, InsO § 39/135, Steuer, Bilanz, SHA/Investment Agreement.

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

## 4. `pe-058-restructuring-waiver-amend-extend`

**Fokus:** Begleitet Waiver, Covenant Reset, A&E, Standstill, Super Senior, SFA und Krisenfinanzierung.

# Amend & Extend und Restrukturierung

## Fachkern: Amend & Extend und Restrukturierung
- **Spezialgegenstand:** Amend & Extend und Restrukturierung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf PE-Portfoliounternehmen vor oder in Krise.

## Rechts- und Praxisanker

StaRUG, InsO, BGB, Kreditvertrag, Sicherheiten, Geschäftsleiterpflichten.

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

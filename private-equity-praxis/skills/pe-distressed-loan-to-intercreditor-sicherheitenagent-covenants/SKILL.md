---
name: pe-distressed-loan-to-intercreditor-sicherheitenagent-covenants
description: "PE Distressed Loan TO Intercreditor Sicherheitenagent Covenants: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE Distressed Loan TO Intercreditor Sicherheitenagent Covenants

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE Distressed Loan TO Intercreditor Sicherheitenagent Covenants** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-051-distressed-loan-to-own` | Prüft Erwerb notleidender Forderungen mit Ziel Kontrolle, Debt-Equity-Swap, Insolvenzplan oder Enforcement. |
| `pe-052-intercreditor-und-sicherheitenagent` | Prüft Rang, Enforcement Waterfall, Sicherheitenagent, Garantie, Upstream/Side-stream Security und Freigaben. |
| `pe-053-covenants-defaults-waiver` | Prüft Financial Covenants, Information Undertakings, MAC, Events of Default, Cure Rights und Waiver-Prozess. |
| `pe-054-security-package-germany` | Prüft GmbH-Anteile, Konten, Forderungen, IP, Warenlager, Grundschuld, Garantie und Sicherheitenzweck. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE Distressed Loan TO Intercreditor Sicherheitenagent Covenants**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-051-distressed-loan-to-own`

**Fokus:** Prüft Erwerb notleidender Forderungen mit Ziel Kontrolle, Debt-Equity-Swap, Insolvenzplan oder Enforcement.

# Distressed Debt und Loan-to-Own

## Fachkern: Distressed Debt und Loan-to-Own
- **Spezialgegenstand:** Distressed Debt und Loan-to-Own wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill trennt legitime Investmentstrategie von Anfechtungs-, Insider- und Haftungsrisiken.

## Rechts- und Praxisanker

InsO, StaRUG, BGB Abtretung, Sicherheiten, Kartell/FDI, MAR bei börsennahen Targets.

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

## 2. `pe-052-intercreditor-und-sicherheitenagent`

**Fokus:** Prüft Rang, Enforcement Waterfall, Sicherheitenagent, Garantie, Upstream/Side-stream Security und Freigaben.

# Intercreditor, Security Agent und Sicherheitenpool

## Fachkern: Intercreditor, Security Agent und Sicherheitenpool
- **Spezialgegenstand:** Intercreditor, Security Agent und Sicherheitenpool wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf deutsches Sicherheitenpaket im internationalen Kredit.

## Rechts- und Praxisanker

BGB/Sachenrecht, GmbHG § 30, AktG Kapitalerhaltung, Insolvenzrecht, LMA-Upload.

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

## 3. `pe-053-covenants-defaults-waiver`

**Fokus:** Prüft Financial Covenants, Information Undertakings, MAC, Events of Default, Cure Rights und Waiver-Prozess.

# Covenants, Defaults und Waiver

## Fachkern: Covenants, Defaults und Waiver
- **Spezialgegenstand:** Covenants, Defaults und Waiver wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill macht aus Covenant-Bruch einen kontrollierten Verhandlungs- und Dokumentationspfad.

## Rechts- und Praxisanker

Kreditvertrag, BGB, InsO/StaRUG Frühwarnung, Geschäftsleiterpflichten.

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

## 4. `pe-054-security-package-germany`

**Fokus:** Prüft GmbH-Anteile, Konten, Forderungen, IP, Warenlager, Grundschuld, Garantie und Sicherheitenzweck.

# Deutsches Sicherheitenpaket

## Fachkern: Deutsches Sicherheitenpaket
- **Spezialgegenstand:** Deutsches Sicherheitenpaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Durchsetzbarkeit, Rang, Anfechtung und praktische Dokumente.

## Rechts- und Praxisanker

BGB/Sachenrecht, GmbHG/AktG Kapitalerhaltung, InsO Anfechtung, Register/Notar.

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

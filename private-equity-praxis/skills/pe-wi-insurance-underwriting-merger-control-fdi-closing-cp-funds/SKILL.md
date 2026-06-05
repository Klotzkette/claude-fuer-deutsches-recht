---
name: pe-wi-insurance-underwriting-merger-control-fdi-closing-cp-funds
description: "PE WI Insurance Underwriting Merger Control FDI Closing CP Funds: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE WI Insurance Underwriting Merger Control FDI Closing CP Funds

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE WI Insurance Underwriting Merger Control FDI Closing CP Funds** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-031-wi-insurance-underwriting` | Begleitet Underwriting, DD-Anforderungen, Exclusions, Bring-down und Claims-Prozess. |
| `pe-032-merger-control-fdi-pe` | Prüft GWB/FKVO/AWV-Anmeldepflichten, Vollzugsverbot, Gun Jumping und Multi-Jurisdiction-Filings. |
| `pe-033-closing-cp-funds-flow` | Baut CP-Tracker, Closing Agenda, Deliverables, Notar-/Registerlogik und Zahlungsflussplan. |
| `pe-034-management-participation-mep` | Strukturiert Management Equity Plan, Vesting, Leaver, Sweet Equity, Ratchet, Call/Put und Good/Bad-Leaver. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE WI Insurance Underwriting Merger Control FDI Closing CP Funds**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-031-wi-insurance-underwriting`

**Fokus:** Begleitet Underwriting, DD-Anforderungen, Exclusions, Bring-down und Claims-Prozess.

# W&I-Versicherung im PE-Deal

## Fachkern: W&I-Versicherung im PE-Deal
- **Spezialgegenstand:** W&I-Versicherung im PE-Deal wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill prüft, ob W&I echte Risikoübernahme oder nur Prozesskosmetik ist.

## Rechts- und Praxisanker

Versicherungsvertrag, SPA-Garantien, DD-Reports, Disclosure, Claims Notice.

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

## 2. `pe-032-merger-control-fdi-pe`

**Fokus:** Prüft GWB/FKVO/AWV-Anmeldepflichten, Vollzugsverbot, Gun Jumping und Multi-Jurisdiction-Filings.

# Fusionskontrolle und FDI für PE

## Fachkern: Fusionskontrolle und FDI für PE
- **Spezialgegenstand:** Fusionskontrolle und FDI für PE wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Fondsumsätze, Portfolio-Kontrolle, Erwerbergruppe und sensitive Sektoren.

## Rechts- und Praxisanker

GWB, EU-Fusionskontrollverordnung, AWG/AWV, Sektorregulierung.

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

## 3. `pe-033-closing-cp-funds-flow`

**Fokus:** Baut CP-Tracker, Closing Agenda, Deliverables, Notar-/Registerlogik und Zahlungsflussplan.

# Closing, CPs und Funds Flow

## Fachkern: Closing, CPs und Funds Flow
- **Spezialgegenstand:** Closing, CPs und Funds Flow wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill erzeugt ein anwaltlich verwertbares Closing-Büro statt losem Excel-Chaos.

## Rechts- und Praxisanker

SPA, § 158 BGB, GWB/AWV Vollzugsverbot, Notar/Handelsregister, Bank KYC.

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

## 4. `pe-034-management-participation-mep`

**Fokus:** Strukturiert Management Equity Plan, Vesting, Leaver, Sweet Equity, Ratchet, Call/Put und Good/Bad-Leaver.

# Management Participation und MEP

## Fachkern: Management Participation und MEP
- **Spezialgegenstand:** Management Participation und MEP wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Motivationslogik, arbeits-/steuerrechtliche Schnittstellen und Exit-Fähigkeit.

## Rechts- und Praxisanker

GmbHG, BGB, Arbeitsrecht, Steuer, Sozialversicherung, Gesellschaftsvertrag.

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

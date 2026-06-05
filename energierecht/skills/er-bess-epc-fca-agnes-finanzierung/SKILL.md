---
name: er-bess-epc-fca-agnes-finanzierung
description: "ER Bess EPC FCA Agnes Finanzierung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Bess EPC FCA Agnes Finanzierung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **ER Bess EPC FCA Agnes Finanzierung** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-epc-o-and-m-vertraege` | Prüft Bau-/Liefervertrag, O&M, Garantien, Degradation, Availability, LDs, Ersatzteile und Cyberpflichten. |
| `er-bess-fca-agnes-bnetza` | Prüft Netzanschlussdokumente nach BNetzA/Festlegungslogik und markiert, was im konkreten Vertrag fehlt. |
| `er-bess-finanzierung-bankability` | Prüft Projektfinanzierung, Sicherheiten, Erlösmodell, Netzanschlussrisiko, Bau-/Betriebsrisiko und Insurance DD. |
| `er-bess-kapazitaetsmarkt-grundlast` | Ordnet Aussagen zu Grundlast, gesicherter Leistung, Kapazitätsmarkt, Gaskraftwerken und Speicherfunktion rechtlich ein. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **ER Bess EPC FCA Agnes Finanzierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-bess-epc-o-and-m-vertraege`

**Fokus:** Prüft Bau-/Liefervertrag, O&M, Garantien, Degradation, Availability, LDs, Ersatzteile und Cyberpflichten.

# EPC, O&M und Herstellerverträge

## Wofür dieser Arbeitsgang da ist

Fokus auf Batteriespeicher-spezifische Vertragsrisiken.

## Rechts- und Praxisanker

BGB Werk-/Kaufrecht, Produktsicherheit, Garantie, Datenschutz/Cyber, Exportkontrolle.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `er-bess-fca-agnes-bnetza`

**Fokus:** Prüft Netzanschlussdokumente nach BNetzA/Festlegungslogik und markiert, was im konkreten Vertrag fehlt.

# FCA/AgNes: Netzanschluss-Regelwerk lesen

## Wofür dieser Arbeitsgang da ist

Der Skill arbeitet mit hochgeladenem Netzanschlussvertrag oder Entwurf und erzeugt eine Red-Flag-Liste.

## Rechts- und Praxisanker

BNetzA-Festlegungen, EnWG, Netzanschlussbedingungen, keine Vertragsstandards ohne Upload.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 3. `er-bess-finanzierung-bankability`

**Fokus:** Prüft Projektfinanzierung, Sicherheiten, Erlösmodell, Netzanschlussrisiko, Bau-/Betriebsrisiko und Insurance DD.

# Finanzierung und Bankability

## Wofür dieser Arbeitsgang da ist

Der Skill erzeugt Bank-DD-Fragen und Lender-Risk-Matrix.

## Rechts- und Praxisanker

BGB, Sicherheitenrecht, EnWG/EEG, Versicherungen, Bauvertrag, Finanzierungsvertrag.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 4. `er-bess-kapazitaetsmarkt-grundlast`

**Fokus:** Ordnet Aussagen zu Grundlast, gesicherter Leistung, Kapazitätsmarkt, Gaskraftwerken und Speicherfunktion rechtlich ein.

# Kapazitätsmechanismen, Grundlast und politische Aussagen

## Wofür dieser Arbeitsgang da ist

Der Skill erklärt, warum Batteriespeicher nicht automatisch Grundlastkraftwerk sind, aber systemdienliche Flexibilität liefern können.

## Rechts- und Praxisanker

EnWG, Strommarktdesign, BMWK/BNetzA-Dokumente live prüfen, keine politische Parole als Rechtsnorm.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

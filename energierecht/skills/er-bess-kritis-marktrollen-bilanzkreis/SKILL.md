---
name: er-bess-kritis-marktrollen-bilanzkreis
description: "ER Bess Kritis Marktrollen Bilanzkreis: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Bess Kritis Marktrollen Bilanzkreis

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **ER Bess Kritis Marktrollen Bilanzkreis** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-kritis-nis2-cyber` | Prüft, ob Speicher, Leitwarte, Netzanschluss oder Betreiber kritische Anlage/IT-Sicherheitsfall sind. |
| `er-bess-marktrollen-bilanzkreis` | Prüft Betreiber, Lieferant, Direktvermarkter, Bilanzkreis, Redispatch, Fahrplan, MaStR und Datenpflichten. |
| `er-bess-naturschutz-artenschutz` | Prüft Eingriffsregelung, Artenschutz, Ausgleich, Landschaftsbild, Ackerflächen und FFH/Vogelschutz. |
| `er-bess-netzanschluss-hoehe-spannung` | Prüft Netzanschlussbegehren, Anschlusszusage, Netzverträglichkeitsprüfung, Kostentragung und Zeitplan. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **ER Bess Kritis Marktrollen Bilanzkreis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-bess-kritis-nis2-cyber`

**Fokus:** Prüft, ob Speicher, Leitwarte, Netzanschluss oder Betreiber kritische Anlage/IT-Sicherheitsfall sind.

# KRITIS, NIS2, BSI und Cybersecurity

## Wofür dieser Arbeitsgang da ist

Fokus auf Berlin/Brandenburg-Resilienz, Fernzugriff, EMS, Lieferkette und Incident-Reporting.

## Rechts- und Praxisanker

BSIG, NIS2-Umsetzung live prüfen, EnWG-IT-Sicherheit, KRITIS-Dachgesetz live prüfen.

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

## 2. `er-bess-marktrollen-bilanzkreis`

**Fokus:** Prüft Betreiber, Lieferant, Direktvermarkter, Bilanzkreis, Redispatch, Fahrplan, MaStR und Datenpflichten.

# Marktrollen, Bilanzkreis und Redispatch

## Wofür dieser Arbeitsgang da ist

Der Skill ordnet energiewirtschaftliche Rollen statt nur Anlagenrecht.

## Rechts- und Praxisanker

EnWG, MaStRV, Redispatch-Regeln, Bilanzkreisverträge, Marktkommunikation.

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

## 3. `er-bess-naturschutz-artenschutz`

**Fokus:** Prüft Eingriffsregelung, Artenschutz, Ausgleich, Landschaftsbild, Ackerflächen und FFH/Vogelschutz.

# Naturschutz, Artenschutz und Flächenkonkurrenz

## Wofür dieser Arbeitsgang da ist

Der Skill verhindert, dass Speicher als 'nur Container' ohne Umweltprüfung behandelt wird.

## Rechts- und Praxisanker

BNatSchG, BauGB Umweltbericht, Landesnaturschutz, Planunterlagen.

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

## 4. `er-bess-netzanschluss-hoehe-spannung`

**Fokus:** Prüft Netzanschlussbegehren, Anschlusszusage, Netzverträglichkeitsprüfung, Kostentragung und Zeitplan.

# Netzanschluss: Hochspannung, Umspannwerk und Kapazität

## Wofür dieser Arbeitsgang da ist

Fokus auf Speicher an 110/380-kV-Strukturen und Anschlusskonflikte.

## Rechts- und Praxisanker

EnWG §§ 17 ff., EEG-Schnittstellen, KraftNAV soweit einschlägig, BNetzA-Prozesse.

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

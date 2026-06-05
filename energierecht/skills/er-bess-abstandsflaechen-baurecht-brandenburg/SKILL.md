---
name: er-bess-abstandsflaechen-baurecht-brandenburg
description: "ER Bess Abstandsflaechen Baurecht Brandenburg: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Bess Abstandsflaechen Baurecht Brandenburg

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **ER Bess Abstandsflaechen Baurecht Brandenburg** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-abstandsflaechen-und-layout` | Prüft Containerabstände, Transformatoren, Umrichter, Zaun, Leitungen, Feuerwehrbewegungsflächen und Nachbarpositionen. |
| `er-bess-baurecht-brandenburg` | Prüft Zulässigkeit im Außenbereich, Bebauungsplan, Sondergebiet Energie, Privilegierung, Erschließung und Nachbarrechte. |
| `er-bess-behoerdenstrategie` | Plant Vorgespräche mit Gemeinde, Bauaufsicht, Immissionsschutz, Feuerwehr, Netzbetreiber, Polizei und Datenschutzaufsicht. |
| `er-bess-bimschg-und-4-bimschv` | Prüft, ob Batteriespeicher immissionsschutzrechtlich genehmigungsbedürftig ist oder Nebenanlagen/Generatoren den Weg ändern. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **ER Bess Abstandsflaechen Baurecht Brandenburg**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-bess-abstandsflaechen-und-layout`

**Fokus:** Prüft Containerabstände, Transformatoren, Umrichter, Zaun, Leitungen, Feuerwehrbewegungsflächen und Nachbarpositionen.

# Abstandsflächen, Containerlayout und Nachbarschaft

## Wofür dieser Arbeitsgang da ist

Der Skill macht aus Lageplan, Flurkarte und Techniklayout eine Genehmigungsrisikomatrix.

## Rechts- und Praxisanker

BbgBO, BauGB Rücksichtnahme, TA Lärm, Brandschutzkonzept, Grundstücksrecht.

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

## 2. `er-bess-baurecht-brandenburg`

**Fokus:** Prüft Zulässigkeit im Außenbereich, Bebauungsplan, Sondergebiet Energie, Privilegierung, Erschließung und Nachbarrechte.

# Batteriespeicher: Baurecht und Bauleitplanung Brandenburg

## Wofür dieser Arbeitsgang da ist

Fokus auf große Containerparks in Brandenburg mit politischem und gemeindlichem Druck.

## Rechts- und Praxisanker

BauGB, BauNVO, BbgBO, Umweltprüfung, Beteiligung, Abstandsflächen.

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

## 3. `er-bess-behoerdenstrategie`

**Fokus:** Plant Vorgespräche mit Gemeinde, Bauaufsicht, Immissionsschutz, Feuerwehr, Netzbetreiber, Polizei und Datenschutzaufsicht.

# Behördenstrategie und Bürgerkommunikation

## Wofür dieser Arbeitsgang da ist

Fokus auf klare, nicht beschönigende Kommunikation.

## Rechts- und Praxisanker

VwVfG, BauGB-Beteiligung, BImSchG-Verfahren, Informationsfreiheits-/Umweltinformationsrecht.

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

## 4. `er-bess-bimschg-und-4-bimschv`

**Fokus:** Prüft, ob Batteriespeicher immissionsschutzrechtlich genehmigungsbedürftig ist oder Nebenanlagen/Generatoren den Weg ändern.

# BImSchG-Screening für Batteriespeicher

## Wofür dieser Arbeitsgang da ist

Der Skill trennt Bauantrag, BImSchG-Antrag, Störfall- und Brandschutzthemen.

## Rechts- und Praxisanker

BImSchG, 4. BImSchV, 12. BImSchV, TA Lärm, Geruch/Staub irrelevant nur markieren, wenn tatsächlich betroffen.

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

---
name: er-bess-netzentgelte-board-physische
description: "ER Bess Netzentgelte Board Physische: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Bess Netzentgelte Board Physische

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **ER Bess Netzentgelte Board Physische** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-netzentgelte-und-abgaben` | Prüft Strombezug, Einspeicherung, Ausspeicherung, Netzentgelte, Umlagen, Messung und Entlastungen. |
| `er-bess-output-board-paper` | Erstellt Entscheidungsvorlage für Vorstand/Geschäftsführung/Aufsichtsrat zu Investition, Risiko, Genehmigung und Finanzierung. |
| `er-bess-physische-sicherheit-terror` | Prüft Zaun, Zutritt, Drohnen, Video, Wachschutz, Polizei/Feuerwehr, Geheimschutz und Betreiberpflichten. |
| `er-bess-power-quality-emv` | Prüft Oberschwingungen, Spannungshaltung, Umrichter, elektromagnetische Verträglichkeit und Nachbar-/Netzbetreiberforderungen. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **ER Bess Netzentgelte Board Physische**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-bess-netzentgelte-und-abgaben`

**Fokus:** Prüft Strombezug, Einspeicherung, Ausspeicherung, Netzentgelte, Umlagen, Messung und Entlastungen.

# Netzentgelte, Umlagen, Speicherprivilegien

## Wofür dieser Arbeitsgang da ist

Fokus auf die Frage, ob der Speicher als Letztverbraucher, Erzeuger, Speicher oder Mischrolle behandelt wird.

## Rechts- und Praxisanker

EnWG, StromNEV, EEG, KWKG, StromStG/EnergieStG nur als Schnittstelle, BNetzA-Praxis live prüfen.

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

## 2. `er-bess-output-board-paper`

**Fokus:** Erstellt Entscheidungsvorlage für Vorstand/Geschäftsführung/Aufsichtsrat zu Investition, Risiko, Genehmigung und Finanzierung.

# Board Paper Batteriespeicher

## Wofür dieser Arbeitsgang da ist

Fokus auf Business Judgment und dokumentierte Informationsgrundlage.

## Rechts- und Praxisanker

Business Judgment, GmbHG/AktG, EnWG/Bau/BImSchG, Finanzierung, Cyber/KRITIS.

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

## 3. `er-bess-physische-sicherheit-terror`

**Fokus:** Prüft Zaun, Zutritt, Drohnen, Video, Wachschutz, Polizei/Feuerwehr, Geheimschutz und Betreiberpflichten.

# Physische Sicherheit, Sabotage und Terrorrisiko

## Wofür dieser Arbeitsgang da ist

Der Skill macht Sicherheitsanforderungen dokumentierbar ohne Panik-Sprache.

## Rechts- und Praxisanker

BSIG/KRITIS, Bauordnungsrecht, Datenschutz bei Video, Versicherungsauflagen.

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

## 4. `er-bess-power-quality-emv`

**Fokus:** Prüft Oberschwingungen, Spannungshaltung, Umrichter, elektromagnetische Verträglichkeit und Nachbar-/Netzbetreiberforderungen.

# Power Quality, EMV und Netzrückwirkungen

## Wofür dieser Arbeitsgang da ist

Der Skill übersetzt diffuse Sorgen vor 'Stromverseuchung' in prüfbare technische und rechtliche Punkte.

## Rechts- und Praxisanker

EnWG, technische Anschlussregeln nur mit aktueller Quelle, EMVG/26. BImSchV als Schnittstelle.

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

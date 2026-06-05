---
name: er-bess-brandschutz-co-location-datenschutz
description: "ER Bess Brandschutz CO Location Datenschutz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Bess Brandschutz CO Location Datenschutz

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **ER Bess Brandschutz CO Location Datenschutz** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-brandschutz-lithium-ionen` | Prüft Brandabschnitte, Abstände, Löschwasserkonzept, Thermal Runaway, Zufahrt, Evakuierung und Einsatzplan. |
| `er-bess-co-location-pv-wind` | Prüft Batteriespeicher neben Erneuerbaren: gemeinsame Messeinrichtung, Förderlogik, Netzanschluss, Direktleitung und Curtailment. |
| `er-bess-datenschutz-video-leitwarte` | Prüft Videoüberwachung, Zutrittslogs, Fernwartung, Auftragsverarbeitung und Drittlandzugriffe. |
| `er-bess-dieselgenerator-notstrom` | Prüft, ob Dieselgeneratoren als Nebenanlage genehmigungspflichtig, emissionsrelevant oder sicherheitskritisch sind. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **ER Bess Brandschutz CO Location Datenschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-bess-brandschutz-lithium-ionen`

**Fokus:** Prüft Brandabschnitte, Abstände, Löschwasserkonzept, Thermal Runaway, Zufahrt, Evakuierung und Einsatzplan.

# Brandschutz und Feuerwehrkonzept Lithium-Ionen-Speicher

## Wofür dieser Arbeitsgang da ist

Fokus auf belegbare Brandschutzauflagen und realistische Nachforderungen der Bauaufsicht.

## Rechts- und Praxisanker

Landesbauordnung, Sonderbau, Feuerwehr, DIN/VDE nur mit Nutzerquelle oder Livezugriff, Herstellerhandbuch.

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

## 2. `er-bess-co-location-pv-wind`

**Fokus:** Prüft Batteriespeicher neben Erneuerbaren: gemeinsame Messeinrichtung, Förderlogik, Netzanschluss, Direktleitung und Curtailment.

# Co-Location mit Wind/PV

## Wofür dieser Arbeitsgang da ist

Fokus auf Förder- und Erlösrisiken bei hybridem Anlagenpark.

## Rechts- und Praxisanker

EEG, EnWG, Messstellenbetrieb, Netzanschluss, PPA/CPPA.

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

## 3. `er-bess-datenschutz-video-leitwarte`

**Fokus:** Prüft Videoüberwachung, Zutrittslogs, Fernwartung, Auftragsverarbeitung und Drittlandzugriffe.

# Datenschutz: Video, Leitwarte und Fernwartung

## Wofür dieser Arbeitsgang da ist

Fokus auf Speicherbetriebsstätte mit Leitwarte und Wartungsdienstleistern.

## Rechts- und Praxisanker

DSGVO, BDSG, TDDDG, NIS2/BSIG-Schnittstelle, AVV.

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

## 4. `er-bess-dieselgenerator-notstrom`

**Fokus:** Prüft, ob Dieselgeneratoren als Nebenanlage genehmigungspflichtig, emissionsrelevant oder sicherheitskritisch sind.

# Dieselgenerator, Notstrom und Schwarzstart

## Wofür dieser Arbeitsgang da ist

Fokus auf Backup für Leittechnik, Feuerwehr, Schwarzstartfähigkeit und Emissionsauflagen.

## Rechts- und Praxisanker

BImSchG, 44. BImSchV, Bauordnungsrecht, AwSV, Energie-/Steuerrecht Schnittstellen.

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

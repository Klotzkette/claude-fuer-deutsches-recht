---
name: tk-entgeltgenehmigung-tk-eu
description: "TK Entgeltgenehmigung TK EU: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Entgeltgenehmigung TK EU

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Entgeltgenehmigung TK EU** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-entgeltgenehmigung-kostenorientierung` | Entgeltregulierung, Kostenunterlagen, Effizienzmaßstab, Genehmigung, Margin Squeeze und Eilrechtsschutz. |
| `tk-eu-eecc-router` | EU-Router für TK-Recht: Richtlinie (EU) 2018/1972, Verbraucherrechte, Marktregulierung, Nummerierung, Universaldienst, Netzneutralität und nationale Umsetzung im TKG. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Entgeltgenehmigung TK EU**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-entgeltgenehmigung-kostenorientierung`

**Fokus:** Entgeltregulierung, Kostenunterlagen, Effizienzmaßstab, Genehmigung, Margin Squeeze und Eilrechtsschutz.

# Entgeltgenehmigung und Kostenorientierung

## Einsatz

Für regulierte Entgelte und Vorleistungsstreit.

## Norm- und Quellenanker

TKG Entgeltregulierung; BNetzA-Beschlusskammerpraxis; GWB/AEUV.

## Arbeitsfragen

1. Welche Entgelte sind genehmigungspflichtig?
2. Welche Kostenbasis ist belegt?
3. Droht Preis-Kosten-Schere?

## Output

Entgeltmemo, Kostenfragenliste und Beschlussangriff.

## Red Flags

- Kostenmodell intransparent
- Retail/Wholesale-Schere
- Frist im Beschlussverfahren verpasst

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-eu-eecc-router`

**Fokus:** EU-Router für TK-Recht: Richtlinie (EU) 2018/1972, Verbraucherrechte, Marktregulierung, Nummerierung, Universaldienst, Netzneutralität und nationale Umsetzung im TKG.

# EU Electronic Communications Code Router

## Einsatz

Wenn ein Thema europäisch geprägt ist, hilft dieser Skill, die deutsche TKG-Norm nicht isoliert zu lesen.

## Norm- und Quellenanker

Richtlinie (EU) 2018/1972 (EECC); TKG 2021; BEREC/EU-Dokumente live prüfen; TDDDG/DSGVO-Schnittstelle.

## Arbeitsfragen

1. Welche EECC-Thematik ist betroffen?
2. Ist die deutsche Umsetzung im TKG eindeutig oder unionsrechtlich auslegungsbedürftig?
3. Gibt es BEREC-Leitlinien oder EU-Vorgaben?
4. Welche nationale Behörde oder Gerichtsebene entscheidet?

## Output

EU-/TKG-Mapping mit Umsetzungsnormen, Argumentationslinie und Quellenliste.

## Red Flags

- rein nationales Lesen trotz EU-Vorgabe
- BEREC-Leitlinien übersehen
- alte TKG-Fassung verwendet
- Netzneutralität mit Kartellrecht verwechselt

## Anschluss-Skills

- tk-marktanalyse-betraechtliche-marktmacht
- tk-netzneutralitaet-zero-rating-throttling

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

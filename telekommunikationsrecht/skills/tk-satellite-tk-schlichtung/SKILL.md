---
name: tk-satellite-tk-schlichtung
description: "TK Satellite TK Schlichtung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Satellite TK Schlichtung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Satellite TK Schlichtung** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-satellite-starlink-ntn` | Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte. |
| `tk-schlichtung-verbraucher` | Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Satellite TK Schlichtung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-satellite-starlink-ntn`

**Fokus:** Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte.

# Satellitenkommunikation und NTN

## Einsatz

Für Starlink-/LEO-/NTN-Projekte und Kundenstreit.

## Norm- und Quellenanker

TKG Frequenz/Marktzugang; EU/ITU-Rahmen live prüfen; BNetzA.

## Arbeitsfragen

1. Welche Satelliten-/Bodeninfrastruktur?
2. Welche Frequenz-/Marktzugangslage?
3. Welche Vertrags- und Resilienzrisiken?

## Output

Satelliten-TK-Memo und Genehmigungscheck.

## Red Flags

- ausländische Lizenz genügt angeblich immer
- Endgerät nicht zugelassen
- Resilienzversprechen überzogen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-schlichtung-verbraucher`

**Fokus:** Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde.

# Verbraucherschlichtung Telekommunikation

## Einsatz

Für Verbraucher, die schnell und kostenschonend Druck aufbauen wollen.

## Norm- und Quellenanker

TKG Schlichtung; Verbraucherstreitbeilegungsrecht; BGB/ZPO.

## Arbeitsfragen

1. Ist Anbieterkontakt erfolgt?
2. Welche Forderung?
3. Welche Belege?

## Output

Schlichtungsantrag und Vergleichsvorschlag.

## Red Flags

- Frist/Verjährung parallel
- Forderung unbeziffert
- Geschäftskundenfall

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

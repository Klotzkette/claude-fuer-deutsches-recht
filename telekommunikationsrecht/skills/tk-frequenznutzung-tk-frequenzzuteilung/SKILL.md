---
name: tk-frequenznutzung-tk-frequenzzuteilung
description: "TK Frequenznutzung TK Frequenzzuteilung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Frequenznutzung TK Frequenzzuteilung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Frequenznutzung TK Frequenzzuteilung** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-frequenznutzung-stoerungen` | Funkstörungen, EMV, Störungsmeldung, Messung, Unterlassung und BNetzA-Eingriff. |
| `tk-frequenzzuteilung-auktionsdesign` | Frequenzzuteilung, Vergabeverfahren, Auktionsdesign, Versorgungsauflagen, Nebenbestimmungen und Rechtsschutz. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Frequenznutzung TK Frequenzzuteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-frequenznutzung-stoerungen`

**Fokus:** Funkstörungen, EMV, Störungsmeldung, Messung, Unterlassung und BNetzA-Eingriff.

# Frequenzstörungen und Funkverträglichkeit

## Einsatz

Für Betreiber, Nachbarn und Hersteller bei gestörter oder störender Funknutzung.

## Norm- und Quellenanker

TKG Frequenznutzung; EMVG; BNetzA-Funkstörungsdienst.

## Arbeitsfragen

1. Welche Frequenz/Anlage stört?
2. Welche Messdaten und Genehmigungen liegen vor?
3. Welche Sofortmaßnahmen sind möglich?

## Output

Störungsdossier, BNetzA-Meldung und Abwehr-/Unterlassungsstrategie.

## Red Flags

- Messung unsauber
- zulässige Anlage als illegal bezeichnet
- Sofortabschaltung ohne Bescheid geprüft

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-frequenzzuteilung-auktionsdesign`

**Fokus:** Frequenzzuteilung, Vergabeverfahren, Auktionsdesign, Versorgungsauflagen, Nebenbestimmungen und Rechtsschutz.

# Frequenzzuteilung und Auktionen

## Einsatz

Für Mobilfunk, Campusnetze, Richtfunk, Satellit und Spezialnetze.

## Norm- und Quellenanker

TKG Frequenzordnung; BNetzA-Frequenzpläne/Vergaberegeln; VwGO.

## Arbeitsfragen

1. Welche Frequenz, Nutzung und Zuteilungsform?
2. Welche Auflagen und Zahlungs-/Ausbaupflichten?
3. Welche Rechtsschutzfrist?

## Output

Frequenzstrategie, Auflagenmatrix und Rechtsmittelcheck.

## Red Flags

- Nebenbestimmung unterschätzt
- Versorgungsauflage nicht kalkuliert
- Auktionsregel falsch gelesen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

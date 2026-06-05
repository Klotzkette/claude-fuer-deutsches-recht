---
name: tk-datacenter-tk-eilrechtsschutz
description: "TK Datacenter TK Eilrechtsschutz: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Datacenter TK Eilrechtsschutz

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Datacenter TK Eilrechtsschutz** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-datacenter-connectivity` | Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung. |
| `tk-eilrechtsschutz-bnetza-beschluss` | Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Datacenter TK Eilrechtsschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-datacenter-connectivity`

**Fokus:** Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung.

# Datacenter Connectivity und Carrier Meet-Me

## Einsatz

Für Rechenzentren, Carrier und Unternehmenskunden.

## Norm- und Quellenanker

BGB; TKG; NIS2/BSI; AGB-Recht.

## Arbeitsfragen

1. Welche Connects und Carrier?
2. Welche Verfügbarkeit und Wartungsfenster?
3. Welche Sicherheitszonen?

## Output

Connectivity-Vertragscheck und Ausfallplan.

## Red Flags

- Cross-Connect ohne klare Verantwortung
- Wartungsfenster zu breit
- Security-Zutritt ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-eilrechtsschutz-bnetza-beschluss`

**Fokus:** Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen.

# Eilrechtsschutz gegen BNetzA-Beschluss

## Einsatz

Wenn ein BNetzA-Beschluss sofort wirtschaftlich wirkt.

## Norm- und Quellenanker

VwGO §§ 80, 80a, 123; TKG; VwVfG.

## Arbeitsfragen

1. Hat der Rechtsbehelf aufschiebende Wirkung?
2. Welche irreversiblen Nachteile drohen?
3. Wie wird Interessenabwägung belegt?

## Output

Eilantragsskizze und Anlagenliste.

## Red Flags

- Eilbedürftigkeit nicht belegt
- Hauptsachechancen fehlen
- Dritte nicht beigeladen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

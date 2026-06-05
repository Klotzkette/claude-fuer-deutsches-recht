---
name: tk-routerfreiheit-tk-rufnummernmissbrauch
description: "TK Routerfreiheit TK Rufnummernmissbrauch: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Routerfreiheit TK Rufnummernmissbrauch

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Routerfreiheit TK Rufnummernmissbrauch** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-routerfreiheit-endgeraete` | Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit. |
| `tk-rufnummernmissbrauch-abschaltung` | Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Routerfreiheit TK Rufnummernmissbrauch**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-routerfreiheit-endgeraete`

**Fokus:** Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit.

# Routerfreiheit und Endgeräte

## Einsatz

Für Streit, ob der Kunde eigenen Router/ONT nutzen darf oder Provider technische Vorgaben macht.

## Norm- und Quellenanker

TKG Endgerätefreiheit/Netzabschlusspunkt live prüfen; BGB; Produktsicherheits-/Cyberrecht; BNetzA-Festlegungen.

## Arbeitsfragen

1. Wo liegt der passive Netzabschlusspunkt?
2. Welche Zugangsdaten/Konfigurationsdaten muss Anbieter bereitstellen?
3. Welche Sicherheits- oder Supportargumente sind tragfähig?
4. Welche Folgen hat eigener Router für Störung/Gewährleistung?

## Output

Routerfreiheits-Memo, Providerbrief, technische Fragenliste und Verbraucher-/Businessvariante.

## Red Flags

- ONT als Providerhoheit behauptet
- Konfigurationsdaten fehlen
- Störung vorschnell dem Kundenrouter zugeschrieben
- Sicherheitsargument ohne Normbasis

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-rufnummernmissbrauch-abschaltung`

**Fokus:** Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde.

# Rufnummernmissbrauch, Abschaltung und Inkassoverbot

## Einsatz

Für Verbraucherbeschwerden und Anbieterabwehr gegen Missbrauchsmaßnahmen.

## Norm- und Quellenanker

TKG Missbrauchsaufsicht/Nummerierung; UWG; BNetzA-Verbraucherschutz.

## Arbeitsfragen

1. Welche Nummer, Kampagne und Rechnung ist betroffen?
2. Welche Missbrauchstatsachen sind belegt?
3. Welche BNetzA-Maßnahme oder Beschwerde läuft?

## Output

Missbrauchsdossier, Beschwerde/Abwehr und Rechnungsprüfung.

## Red Flags

- Kundenbeschwerden nicht gesichert
- Inkasso trotz Verbot
- Callcenter-Kette unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

---
name: tk-glasfaser-tk-infrastruktursharing
description: "TK Glasfaser TK Infrastruktursharing: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Glasfaser TK Infrastruktursharing

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Glasfaser TK Infrastruktursharing** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-glasfaser-hausanschluss-wegerecht` | Glasfaser- und Hausanschlussprojekte: Grundstückszugang, Gebäudenetz, Wegerecht, Gestattung, Wohnungseigentum, Open Access und Baukoordination. |
| `tk-infrastruktursharing-open-access` | Open-Access-Modelle, Infrastruktursharing, Wholesale-Only, Kooperationsverträge, Nichtdiskriminierung und Beihilfe-/Förderschnittstelle. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Glasfaser TK Infrastruktursharing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-glasfaser-hausanschluss-wegerecht`

**Fokus:** Glasfaser- und Hausanschlussprojekte: Grundstückszugang, Gebäudenetz, Wegerecht, Gestattung, Wohnungseigentum, Open Access und Baukoordination.

# Glasfaser-Hausanschluss und Wegerecht

## Einsatz

Für Ausbauprojekte und Eigentümerstreit, wenn Kabel durch Grundstücke, Häuser oder öffentliche Wege müssen.

## Norm- und Quellenanker

TKG Wegerechte/Mitnutzung live prüfen; BGB Sachenrecht; WEG; Bau-/Straßenrecht; BNetzA-Praxis.

## Arbeitsfragen

1. Welcher Netzabschnitt ist betroffen: öffentlich, Grundstück, Gebäude, Wohnung?
2. Welche Gestattung oder Duldung ist nötig?
3. Welche Bau-, Wiederherstellungs- und Haftungsfragen bestehen?
4. Wie wird Open Access dokumentiert?

## Output

Gestattungsmatrix, Eigentümeranschreiben, Bau-/Haftungsplan und Open-Access-Check.

## Red Flags

- WEG-Beschlusslage unklar
- öffentlicher Weg und Privatgrund verwechselt
- Tiefbau ohne Wiederherstellungskonzept
- Exklusivität in Gestattung

## Anschluss-Skills

- tk-wegerecht-oeffentliche-wege
- tk-infrastruktursharing-open-access

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-infrastruktursharing-open-access`

**Fokus:** Open-Access-Modelle, Infrastruktursharing, Wholesale-Only, Kooperationsverträge, Nichtdiskriminierung und Beihilfe-/Förderschnittstelle.

# Infrastruktursharing und Open Access

## Einsatz

Für Glasfaser- und Mobilfunkkooperationen.

## Norm- und Quellenanker

TKG; GWB; EU-Beihilferecht; Förderbescheide; BNetzA-Praxis.

## Arbeitsfragen

1. Welche Infrastruktur wird geteilt?
2. Welche Zugangsbedingungen sind fair und offen?
3. Gibt es Fördermittelauflagen?

## Output

Open-Access-Vertragscheck und Nichtdiskriminierungsmatrix.

## Red Flags

- faktische Exklusivität
- Förderauflagen ignoriert
- Wholesale-Prozesse nicht operationalisiert

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

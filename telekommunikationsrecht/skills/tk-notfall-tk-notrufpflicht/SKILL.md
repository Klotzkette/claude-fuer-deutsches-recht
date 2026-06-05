---
name: tk-notfall-tk-notrufpflicht
description: "TK Notfall TK Notrufpflicht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Notfall TK Notrufpflicht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Notfall TK Notrufpflicht** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-notfall-und-katastrophenkommunikation` | Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity. |
| `tk-notrufpflicht-112` | Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Notfall TK Notrufpflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-notfall-und-katastrophenkommunikation`

**Fokus:** Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity.

# Notfall- und Katastrophenkommunikation

## Einsatz

Für Provider und Betreiber kritischer Einrichtungen.

## Norm- und Quellenanker

TKG Sicherheits-/Notfallregeln; BBK/BSI/BNetzA-Vorgaben live prüfen.

## Arbeitsfragen

1. Welche Dienste müssen im Notfall aufrechterhalten werden?
2. Welche Behördenkontakte und Tests?
3. Welche Kunden-/Priorisierungspflichten?

## Output

Notfallkommunikationsplan und Testkalender.

## Red Flags

- Backupstrom fehlt
- Behördenkontakte veraltet
- Cell-Broadcast-Rollen unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-notrufpflicht-112`

**Fokus:** Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko.

# Notrufpflicht und Ausfallsicherheit

## Einsatz

Für Anbieter und Geschäftskunden, wenn Telefonie, Cloud-PBX oder IoT-Dienst Notruffunktionen beeinflusst.

## Norm- und Quellenanker

TKG Notrufvorschriften live prüfen; Sicherheitsrecht; DSGVO Standortdaten; BSI/NIS2-Schnittstelle.

## Arbeitsfragen

1. Welche Dienste ermöglichen Notrufe?
2. Welche Standort-/Routingdaten werden übermittelt?
3. Welche Ausfall- und Backupstrategie existiert?
4. Welche Kundeninformationen sind nötig?

## Output

Notruf-Compliance-Check, Risikoampel, Vertragsklauseln und Incident-Plan.

## Red Flags

- Cloud-PBX ohne Standortlogik
- Homeoffice-Notruf falsch geroutet
- Ausfallplan fehlt
- Datenschutz blockiert Notruffunktion falsch

## Anschluss-Skills

- tk-cloud-telefonie-voip-compliance
- tk-notfall-und-katastrophenkommunikation

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

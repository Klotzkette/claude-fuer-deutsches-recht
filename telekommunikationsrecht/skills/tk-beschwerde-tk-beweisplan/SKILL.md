---
name: tk-beschwerde-tk-beweisplan
description: "TK Beschwerde TK Beweisplan: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Beschwerde TK Beweisplan

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Beschwerde TK Beweisplan** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-beschwerde-dashboard-bnetza` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen. |
| `tk-beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Beschwerde TK Beweisplan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-beschwerde-dashboard-bnetza`

**Fokus:** Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen.

# BNetzA-Beschwerde-Dashboard

## Einsatz

Für Kanzleien, Unternehmen und Verbraucherzentralen mit vielen TK-Fällen.

## Norm- und Quellenanker

TKG; VwVfG; Verbraucherrecht; BNetzA-Formulare live prüfen.

## Arbeitsfragen

1. Welche Beschwerdekategorie?
2. Welche Belege und Status?
3. Welche Eskalation?

## Output

Beschwerdeboard, Statusliste und Standardtexte.

## Red Flags

- Beschwerden ohne Kategorie
- keine Ticketnummern
- Fristen nicht verfolgt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-beweisplan-messung-stoerung-protokoll`

**Fokus:** Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen.

# Beweisplan: Messung, Störung, Protokoll

## Einsatz

Für Verbraucher und Geschäftskunden, die nicht nur behaupten wollen, dass Internet oder Telefon schlecht waren.

## Norm- und Quellenanker

TKG Kundenschutz; BGB Leistungsstörung; ZPO Beweis; BNetzA-Breitbandmessungsvorgaben live prüfen.

## Arbeitsfragen

1. Welche vertragliche Leistung ist geschuldet?
2. Welche Messmethode ist anerkannt und reproduzierbar?
3. Welche Störung wurde wann wem gemeldet?
4. Welche wirtschaftlichen Folgen sind belegbar?

## Output

Mess- und Störungsdossier, Belegliste, Minderungs-/Schadensersatzbasis und Providerbrief.

## Red Flags

- Speedtest ohne Methodik
- WLAN-Problem als Leitungsproblem
- Ticketnummern fehlen
- SLA nicht gelesen

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-sla-business-kunden-ausfall

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

---
name: tk-cloud-tk-cookies
description: "TK Cloud TK Cookies: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Cloud TK Cookies

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Cloud TK Cookies** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-cloud-telefonie-voip-compliance` | Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer. |
| `tk-cookies-telemedien-ttdsg-tdddg` | Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Cloud TK Cookies**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-cloud-telefonie-voip-compliance`

**Fokus:** Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer.

# Cloud-Telefonie und VoIP

## Einsatz

Für Unternehmen und Provider mit Teams-/Zoom-/Cloud-Telefonie.

## Norm- und Quellenanker

TKG; TDDDG; DSGVO; Notrufvorschriften; BGB.

## Arbeitsfragen

1. Wer ist Anbieter/Reseller?
2. Wie funktionieren Notruf und Standort?
3. Welche Aufzeichnungen/Logs?

## Output

VoIP-Compliance-Check und Nutzerinformation.

## Red Flags

- Notruf bei Homeoffice falsch
- Aufzeichnung ohne Rechtsgrund
- Rufnummernmissbrauch

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-cookies-telemedien-ttdsg-tdddg`

**Fokus:** Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste.

# Cookies, Telemedien und TDDDG-Schnittstelle

## Einsatz

Für Anbieter, die TK-Dienste und Web-/App-Dienste kombinieren.

## Norm- und Quellenanker

TDDDG; DSGVO; ePrivacy; TKG.

## Arbeitsfragen

1. Ist Zugriff auf Endeinrichtung betroffen?
2. Welche Einwilligung ist erforderlich?
3. Wie passt das zu TK-Daten?

## Output

Consent- und Datenflusscheck.

## Red Flags

- Cookie und Verkehrsdaten vermischt
- berechtigtes Interesse überdehnt
- CMP falsch konfiguriert

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

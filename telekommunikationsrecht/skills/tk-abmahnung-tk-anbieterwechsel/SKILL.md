---
name: tk-abmahnung-tk-anbieterwechsel
description: "TK Abmahnung TK Anbieterwechsel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Abmahnung TK Anbieterwechsel

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Abmahnung TK Anbieterwechsel** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-abmahnung-uwg-tkg` | Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten. |
| `tk-anbieterwechsel-rufnummernmitnahme` | Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Abmahnung TK Anbieterwechsel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-abmahnung-uwg-tkg`

**Fokus:** Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten.

# Abmahnung nach UWG/TKG

## Einsatz

Für Wettbewerber, Verbände und Anbieter.

## Norm- und Quellenanker

UWG; TKG; PAngV; TDDDG/DSGVO; BGB.

## Arbeitsfragen

1. Welche Marktverhaltensregel?
2. Welche Werbung/Information ist falsch?
3. Welche Unterlassung und Vertragsstrafe?

## Output

Abmahnungs-/Verteidigungsschreiben und Beweisplan.

## Red Flags

- TKG-Norm keine Marktverhaltensregel geprüft
- Screenshot fehlt
- Unterlassung zu weit

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-anbieterwechsel-rufnummernmitnahme`

**Fokus:** Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde.

# Anbieterwechsel und Rufnummernmitnahme

## Einsatz

Für Verbraucher und Unternehmen, die beim Wechsel ohne Telefon/Internet oder ohne Rufnummer dastehen.

## Norm- und Quellenanker

TKG §§ 59 und Kundenschutzvorschriften live prüfen; BNetzA-Anbieterwechselinformationen; BGB.

## Arbeitsfragen

1. Wann wurde Wechsel/Portierung beauftragt?
2. Wer ist abgebender und aufnehmender Anbieter?
3. Welche Verzögerung ist wem zurechenbar?
4. Welche Entschädigung oder Beschwerde ist möglich?

## Output

Portierungszeitstrahl, Entschädigungsforderung, BNetzA-Beschwerde und Eskalationsmail.

## Red Flags

- Altanbieter schaltet ab
- Portierungsdatum unklar
- Rufnummer gehört Firma statt Mitarbeiter
- Entschädigung falsch berechnet

## Anschluss-Skills

- tk-schlichtung-verbraucher
- tk-output-beschwerde-antrag-klage

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

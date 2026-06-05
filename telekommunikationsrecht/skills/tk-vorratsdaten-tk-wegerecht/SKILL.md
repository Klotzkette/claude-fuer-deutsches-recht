---
name: tk-vorratsdaten-tk-wegerecht
description: "TK Vorratsdaten TK Wegerecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Vorratsdaten TK Wegerecht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Vorratsdaten TK Wegerecht** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-vorratsdaten-speicherung-eugh-bverfg` | Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen. |
| `tk-wegerecht-oeffentliche-wege` | Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Vorratsdaten TK Wegerecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-vorratsdaten-speicherung-eugh-bverfg`

**Fokus:** Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen.

# Vorratsdaten und Speicherpflichten

## Einsatz

Für Provider und Betroffene bei Speicher-/Auskunftspflichten.

## Norm- und Quellenanker

TKG/TTDSG/TDDDG; DSGVO; GRCh; GG; EuGH/BVerfG nur verifiziert zitieren.

## Arbeitsfragen

1. Welche Pflicht oder Anfrage liegt vor?
2. Welche Datenart und Eingriffsintensität?
3. Welche aktuelle EuGH/BVerfG-Rechtsprechung ist einschlägig?

## Output

Speicherpflichten-Memo und Behördenantwort.

## Red Flags

- alte Vorratsdatenlage verwendet
- Bestandsdaten/Verkehrsdaten verwechselt
- Richtervorbehalt ungeprüft

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-wegerecht-oeffentliche-wege`

**Fokus:** Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern.

# Wegerecht für öffentliche Wege

## Einsatz

Für Netzbau auf öffentlichen Wegen.

## Norm- und Quellenanker

TKG Wegerechte live prüfen; Straßenrecht Bund/Länder; VwVfG/VwGO.

## Arbeitsfragen

1. Welche Straße/Fläche und welcher Träger?
2. Welche Zustimmung/Anzeige?
3. Welche Nebenbestimmungen und Wiederherstellungspflichten?

## Output

Wegerechtsantrag, Nebenbestimmungscheck und Bauzeitenplan.

## Red Flags

- falscher Straßenbaulastträger
- kommunale Sondernutzung überdehnt
- Wiederherstellungskosten ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

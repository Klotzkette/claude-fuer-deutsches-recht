---
name: tk-towerco-tk-traffic
description: "TK Towerco TK Traffic: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Towerco TK Traffic

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Towerco TK Traffic** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-towerco-standortmiete` | Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt. |
| `tk-traffic-location-data-privacy` | Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Towerco TK Traffic**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-towerco-standortmiete`

**Fokus:** Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt.

# TowerCo und Mobilfunkstandortmiete

## Einsatz

Für TowerCos, Netzbetreiber und Grundstückseigentümer.

## Norm- und Quellenanker

BGB Mietrecht; TKG; Bau-/Immissionsschutzrecht; Frequenzrecht.

## Arbeitsfragen

1. Welche Anlage und Fläche?
2. Welche Genehmigungen und Immissionen?
3. Welche Sharing-/Rückbaupflichten?

## Output

Standortvertrags-Redline und Genehmigungscheck.

## Red Flags

- Rückbau vergessen
- Immissionsnachweis fehlt
- Exklusivklausel kartell-/tk-riskant

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-traffic-location-data-privacy`

**Fokus:** Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung.

# Verkehrs- und Standortdaten

## Einsatz

Für Anbieter, Arbeitgeber und Kunden bei sensiblen Nutzungsdaten.

## Norm- und Quellenanker

TKG/TDDDG Telekommunikationsdatenschutz; DSGVO; ePrivacy-Recht live prüfen.

## Arbeitsfragen

1. Welche Datenkategorie?
2. Für welchen Zweck und wie lange?
3. Welche Einwilligung/gesetzliche Grundlage?

## Output

Datenschutz- und Löschkonzept.

## Red Flags

- Standortdaten als normale Kundendaten
- Speicherfrist unklar
- EVN ohne Berechtigung

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

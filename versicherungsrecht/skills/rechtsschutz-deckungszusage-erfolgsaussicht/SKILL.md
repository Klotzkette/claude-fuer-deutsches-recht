---
name: rechtsschutz-deckungszusage-erfolgsaussicht
description: "Rechtsschutz Deckungszusage Erfolgsaussicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsschutz Deckungszusage Erfolgsaussicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rechtsschutz Deckungszusage Erfolgsaussicht** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsschutz-deckungszusage-stichentscheid` | Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation. |
| `rechtsschutz-erfolgsaussicht-mutwilligkeit` | Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden. |
| `reiseversicherung-ruecktritt-abbruch-krankheit` | Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Rechtsschutz Deckungszusage Erfolgsaussicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsschutz-deckungszusage-stichentscheid`

**Fokus:** Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation.

# Rechtsschutz: Deckungszusage und Stichentscheid

## Einsatz

Der Skill ist für Anwälte und Mandanten, wenn die RSV die Finanzierung des Rechtsstreits blockiert.

## Norm- und Quellenanker

VVG §§ 125–129, besonders § 128; ARB; RVG; ZPO.

## Arbeitsfragen

1. Welcher Rechtsschutzbereich und welcher Versicherungsfall?
2. Welche Erfolgsaussichten und Mutwilligkeitsargumente nennt der Versicherer?
3. Ist Stichentscheid oder Schiedsgutachten vorgesehen?
4. Welche Gebühren/Deckungskomponenten sind beantragt?

## Output

Deckungsanfrage, Stichentscheid-Entwurf, Kostenmatrix und RSV-Erwiderung.

## Red Flags

- Versicherungsfall falsch datiert
- Vorvertraglichkeit nicht geprüft
- Stichentscheid zu spät
- Kostenpositionen unvollständig

## Anschluss-Skills

- rechtsschutz-vorvertraglichkeit-schadenereignis
- rechtsschutz-erfolgsaussicht-mutwilligkeit

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `rechtsschutz-erfolgsaussicht-mutwilligkeit`

**Fokus:** Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden.

# Rechtsschutz: Erfolgsaussicht und Mutwilligkeit

## Einsatz

Der Skill baut einen nüchternen, finanzierungsfähigen Prospekt für die RSV.

## Norm- und Quellenanker

VVG § 128; ARB; ZPO Prozesskostenlogik analog nur vorsichtig; RVG.

## Arbeitsfragen

1. Welche Tatsachen und Beweise tragen den Hauptanspruch?
2. Welche Gegenargumente sind ernsthaft, welche nur vorgeschoben?
3. Ist Kosten-Nutzen-Verhältnis mutwillig oder wirtschaftlich plausibel?
4. Kann ein Teilrechtsschutz sinnvoll sein?

## Output

Erfolgsaussichtsmemo, Mutwilligkeitsabwehr, Teildeckungsantrag und Mandantenrisiko.

## Red Flags

- Hauptsache zu optimistisch dargestellt
- Kostenrisiko nicht beziffert
- Teilklage/Teilrechtsschutz vergessen
- RSV als Gegner im Hauptstreit vermischt

## Anschluss-Skills

- rechtsschutz-deckungszusage-stichentscheid
- vergleich-abfindung-entschaedigungsquittung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `reiseversicherung-ruecktritt-abbruch-krankheit`

**Fokus:** Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung.

# Reiseversicherung: Rücktritt, Abbruch, Krankheit

## Einsatz

Der Skill hilft bei typischen Reiseablehnungen, in denen Atteste, Vorerkrankungen und Stornofristen streiten.

## Norm- und Quellenanker

VVG allgemein; AVB Reise; BGB Reisevertragsrecht §§ 651a ff.; Datenschutz Gesundheitsdaten.

## Arbeitsfragen

1. Welches versicherte Ereignis löste Rücktritt/Abbruch aus?
2. War die Erkrankung unerwartet und schwer im Sinne der AVB?
3. Wann wurde gebucht, diagnostiziert, storniert?
4. Welche Kosten sind ersatzfähig?

## Output

Reise-Deckungsmemo, Attestanforderung, Stornokostenmatrix und Versichererantwort.

## Red Flags

- Attest zu pauschal
- Storno zu spät
- Vorerkrankung als Ausschluss behauptet
- Kreditkartenversicherung mit Reiseveranstalter verwechselt

## Anschluss-Skills

- datenschutz-schweigepflicht-gesundheitsdaten
- vers-fristen-verjaehrung-klagefrist-fallkalender

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

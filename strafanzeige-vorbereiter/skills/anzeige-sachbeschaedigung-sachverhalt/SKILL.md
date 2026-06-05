---
name: anzeige-sachbeschaedigung-sachverhalt
description: "Anzeige Sachbeschaedigung Sachverhalt: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Sachbeschaedigung Sachverhalt

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Sachbeschaedigung Sachverhalt** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-sachbeschaedigung-303` | Sachbeschädigung: Beschädigung/Zerstörung/Veränderung, Fotos, Kostenvoranschlag, Strafantrag, Zivilforderung. |
| `anzeige-sachverhalt-ohne-adjektive` | Entfernt Polemik und Rechtswertungen aus Anzeigen; schreibt nüchtern, präzise und beweisnah. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Sachbeschaedigung Sachverhalt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-sachbeschaedigung-303`

**Fokus:** Sachbeschädigung: Beschädigung/Zerstörung/Veränderung, Fotos, Kostenvoranschlag, Strafantrag, Zivilforderung.

# Sachbeschädigung § 303 StGB

## Einsatz

Für Fahrzeug, Gebäude, Geräte, Graffiti.

## Norm- und Quellenanker

StGB §§ 303, 303c; BGB Schadensersatz.

## Arbeitsfragen

1. Was wurde beschädigt?
2. Wann und durch wen?
3. Welche Kosten?

## Output

Sachbeschädigungsanzeige und Anlagenliste.

## Red Flags

- Vorschaden unklar
- Täter nur vermutet
- Kosten nicht belegt

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-sachverhalt-ohne-adjektive`

**Fokus:** Entfernt Polemik und Rechtswertungen aus Anzeigen; schreibt nüchtern, präzise und beweisnah.

# Sachverhalt ohne Adjektive

## Einsatz

Für Entwürfe, die zu emotional klingen.

## Norm- und Quellenanker

StPO § 158; StGB § 164.

## Arbeitsfragen

1. Welche Wörter sind Wertung?
2. Welche Tatsache ersetzt die Wertung?
3. Welche Belege?

## Output

bereinigter Sachverhalt.

## Red Flags

- „kriminell“ ohne Urteil
- Motive behauptet
- Schimpfwörter

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

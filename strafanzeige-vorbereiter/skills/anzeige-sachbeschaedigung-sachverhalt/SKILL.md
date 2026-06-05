---
name: anzeige-sachbeschaedigung-sachverhalt
description: "Anzeige Sachbeschaedigung 303, Anzeige Sachverhalt Ohne Adjektive: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anzeige Sachbeschaedigung 303, Anzeige Sachverhalt Ohne Adjektive

## Arbeitsbereich

Dieser Skill bündelt **Anzeige Sachbeschaedigung 303, Anzeige Sachverhalt Ohne Adjektive** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `anzeige-sachbeschaedigung-303` | Sachbeschädigung: Beschädigung/Zerstörung/Veränderung, Fotos, Kostenvoranschlag, Strafantrag, Zivilforderung. |
| `anzeige-sachverhalt-ohne-adjektive` | Entfernt Polemik und Rechtswertungen aus Anzeigen; schreibt nüchtern, präzise und beweisnah. |

## Arbeitsweg

Für **Anzeige Sachbeschaedigung 303, Anzeige Sachverhalt Ohne Adjektive** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `strafanzeige-vorbereiter` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

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

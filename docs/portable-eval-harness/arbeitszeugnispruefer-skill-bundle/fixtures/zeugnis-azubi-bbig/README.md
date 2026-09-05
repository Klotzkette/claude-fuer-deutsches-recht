# Test-Zeugnis Azubi (Paragraf 16 BBiG)

[Skill-Bundle](../../README.md) · [Eval-Harness](../../../README.md) · [Repository-Start](../../../../../README.md)

Spezialfall: Ausbildungszeugnis nach Paragraf 16 BBiG. Skill soll die Sonderregeln
erkennen (anderes Rechtsregime; auf Verlangen Verhalten + Leistung).

## Zeugnis-Volltext (qualifiziert nach Paragraf 16 II BBiG)

> **Handwerksbetrieb Müller GmbH**
>
> **Ausbildungszeugnis**
>
> Herr Max Mustermann, geboren am 1. Mai 2003, hat vom 1. August 2021 bis zum 31. Juli 2024 in unserem Betrieb den Ausbildungsberuf Tischler erlernt.
>
> Herr Mustermann hat die Ausbildungsinhalte stets schnell und sicher aufgenommen. Er zeigte großes Interesse an seinem Ausbildungsberuf und zeichnete sich durch hervorragende Berufsschulleistungen aus. Sein Verhalten gegenüber Vorgesetzten, Kollegen und Kunden war stets einwandfrei.

## Erwartete Befunde

- Skill erkennt: Ausbildungszeugnis (nicht qualifiziertes regulaeres Arbeitszeugnis)
- Skill verweist auf Paragraf 16 BBiG als Rechtsgrundlage (statt Paragraf 109 GewO)
- "stets schnell und sicher aufgenommen" - Note 1
- "hervorragende Berufsschulleistungen" - Note 1
- "stets einwandfrei" - Note 1
- Gesamtnote: 1

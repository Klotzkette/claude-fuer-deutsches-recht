# Test-Zeugnis mit roten Flaggen (Note 4)

[Skill-Bundle](../../README.md) · [Eval-Harness](../../../README.md) · [Repository-Start](../../../../../README.md)

Eingabe für den Skill. Erwarteter Output: Gesamtnote 4, multiple rote Flaggen
erkannt, Berichtigungsempfehlung vorhanden.

## Zeugnis-Volltext

> **Beispiel GmbH | Beispielstrasse 5 | 20000 Beispielstadt**
>
> **Arbeitszeugnis**
>
> Herr Thomas Beispiel war vom 1. Januar 2020 bis zum 30. Juni 2024 als Vertriebsmitarbeiter beschäftigt.
>
> **Leistungsbeurteilung:** Herr Beispiel verfügt über ausreichende Fachkenntnisse. Er war stets bemüht, die ihm übertragenen Aufgaben zur vollen Zufriedenheit zu erledigen.
>
> **Verhaltensbeurteilung:** Gegenüber Kollegen und Vorgesetzten verhielt sich Herr Beispiel korrekt. Er zeichnete sich durch eine direkte Kommunikationsweise aus.
>
> **Schlussformel:** Wir danken Herrn Beispiel für seine Mitarbeit und wünschen ihm für die Zukunft alles Gute.

## Erwartete Befunde

- "ausreichende Fachkenntnisse" - Note 4-5 (rot)
- "stets bemüht" - Note 4 (rot)
- "korrekt" allein (ohne stets/einwandfrei) - Note 4 (orange/rot)
- "direkte Kommunikationsweise" - Code für schwierig im Umgang
- Reihenfolge "Kollegen und Vorgesetzten" statt "Vorgesetzten und Kollegen" (rot)
- Schlussformel ohne Bedauern, ohne herzlichen Dank, ohne berufliche/persönliche Zukunftswünsche
- Schweigen zu Kunden trotz Vertriebsjob (rot — Auslassung)

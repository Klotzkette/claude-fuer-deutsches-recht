---
name: notenwahl-modus
description: "Leitet die passende Leistungs- und Verhaltensnote aus Beurteilungen, Zielwerten, Projekten und Gegenbelegen ab, statt eine Wunschziffer ungeprüft zu übernehmen."
---

# Notenwahl-Modus

## Ziel

Die Note sauber festlegen, bevor Formulierungen generiert werden. Eine nachträgliche Notenkorrektur erfordert vollständige Neuformulierung aller Leistungs- und Verhaltenssätze.

## Eingang — was wird abgefragt

Der Generator fragt genau eine Frage:

> „Möchten Sie die Note direkt vorgeben (z.B. Note 2) oder soll ich durch einige Fragen zu Leistung und Verhalten eine Notenempfehlung erarbeiten?"

### Modus A: Direkte Notenvorgabe

Der Nutzer nennt eine Note von 1 bis 5 (oder eine Beschreibung wie „sehr gut", „befriedigend"). Der Generator bestätigt die Zuordnung und wählt die passenden Formeln aus den Note-Katalogen.

Notenskala:
| Note | Bezeichnung | Zufriedenheitsformel |
|---|---|---|
| 1 | sehr gut | stets zur vollsten Zufriedenheit |
| 2 | gut | stets zur vollen Zufriedenheit |
| 3 | befriedigend | zur vollen Zufriedenheit |
| 4 | ausreichend | zur Zufriedenheit |
| 5 | mangelhaft | im Großen und Ganzen zur Zufriedenheit |

### Modus B: Notenermittlung durch Fragen

Der Generator stellt maximal fünf Fragen:

1. Hat die Person ihre Kernaufgaben vollständig und fristgerecht erfüllt?
2. Gab es messbare Erfolge (Ziele, Projekte, Umsatz, Qualität)?
3. Wie war das Verhalten gegenüber Vorgesetzten und Kollegen?
4. Gab es Beanstandungen oder Abmahnungen?
5. Empfehlen Sie die Person für eine vergleichbare Stelle?

Aus den Antworten bildet der Generator eine Notenempfehlung und begründet sie. Der Nutzer bestätigt oder korrigiert.

## Rechtlicher Hintergrund

Note 3 (befriedigend / zur vollen Zufriedenheit) ist nach BAG, Urteil v. 14.10.2003 – 9 AZR 12/03 der Ausgangspunkt der Skala. Wer besser als Note 3 bewertet, trägt als Arbeitgeber keine erhöhte Begründungslast — kann es aber tun. Wer schlechter als Note 3 bewertet, muss dies mit konkreten Tatsachen stützen können (BAG, Urteil v. 18.11.2014 – 9 AZR 584/13).

## Generier-Regeln

- Die gewählte Note zieht sich konsistent durch alle Leistungssätze, Verhaltenssätze und die Schlussformel.
- Brüche zwischen Einzelnoten und der Hauptformel vermeiden (Drift).
- Für Noten 4 und 5 explizit darauf hinweisen, dass der Arbeitgeber die Darlegungs- und Beweislast trägt — diese Noten sollten nur bei dokumentierten Mängeln vergeben werden.

## Stolpersteine

- Nutzer nennt verbale Beschreibung statt Ziffer: „ein guter Mitarbeiter" kann Note 1 oder Note 2 bedeuten — immer klärende Nachfrage.
- Verschiedene Noten für Leistung und Verhalten: beides separat erfassen und beide Werte konsistent im Zeugnis umsetzen.
- Note 5 ohne Begründung ist rechtlich riskant; Generator muss auf Beweislastrisiko hinweisen.

## Anti-Muster

- Note direkt in Formulierung übersetzen ohne Bestätigung durch den Nutzer.
- Modus B mit mehr als fünf Fragen — der Nutzer muss nicht ein vollständiges Beurteilungsgespräch führen.
- Unterschiedliche Noten für verschiedene Aufgabenbereiche mitteln, ohne den Nutzer darauf hinzuweisen.

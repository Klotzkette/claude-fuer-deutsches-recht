---
name: widerspruechliche-bewertungen
description: "Erkennt und kommentiert Widersprüche im Arbeitszeugnis: wenn Leistungsteil grün, aber Schlussformel rot ist, oder wenn Einzelsätze sich inhaltlich ausschließen. Erklärt die Signalwirkung von Widersprüchen auf potenzielle neue Arbeitgeber."
---

# Widersprüchliche Bewertungen erkennen und kommentieren

Ein Arbeitszeugnis kann widersprüchliche Signale enthalten — entweder durch handwerkliche Fehler des Ausstellers, durch den Versuch, die Wahrheit zu verschleiern, oder durch die Einschätzung verschiedener Bewertender im Unternehmen. Widersprüche sind kein Zeichen von Wohlwollen; sie verwirren potenzielle neue Arbeitgeber und können den Eindruck eines unsicheren Zeugnisausstellers hinterlassen — oder den Eindruck einer bewusst verschlüsselten Negativbotschaft.

Der häufigste Widerspruchstyp: Der Leistungsteil enthält grüne Formulierungen, die Schlussformel ist aber unvollständig oder rot. Das Signal ist klar: Der Arbeitgeber war mit der Leistung zufrieden, aber das Ausscheiden war nicht einvernehmlich. Ähnlich: Verhaltensteil grün, Leistungsteil orange — deutet auf einen zuverlässigen, aber leistungsmäßig schwächeren Mitarbeiter hin.

Ein zweiter Widerspruchstyp ist die innere Inkonsistenz: Wenn ein Satz über hervorragende Eigeninitiative neben einem Satz steht, der Aufgaben "nach Anweisung" beschreibt, widersprechen sich die Aussagen direkt. Diese inneren Widersprüche entstehen oft, wenn Zeugnisse von verschiedenen Personen erstellt oder aus Bausteinen zusammengesetzt werden.

Ein dritter Widerspruchstyp ist die Reihenfolge-Anomalie: Ein Zeugnis, das mit einer hervorragenden Leistungsbeurteilung beginnt, dann eine schwache Verhaltensbeurteilung gibt und mit einer warmen Schlussformel endet, hat ein gemischtes Signal, das nicht konsistent ist. Potenzielle Arbeitgeber werden den Verhaltensabschnitt herausgreifen.

Ein vierter Widerspruchstyp ist das Schaufenster-Pattern innerhalb eines einzelnen Themenbereichs: ein Spitzensatz auf Note-1-Niveau und ein benachbarter Satz auf Note-3-Niveau betreffen dasselbe Thema (z. B. Fachkenntnisse plus Lernbereitschaft, oder Arbeitsweise plus Innovation). Dieser Drift wird vom spezialisierten Skill `bereichs-drift-detektor` ausgewertet — er ist subtiler als die hier behandelten Block-Widersprüche, weil er innerhalb desselben Absatzes auftritt und nicht zwischen den großen Teilen des Zeugnisses.

## Geheimcode-Regeln

| Widerspruchstyp | Signalwirkung | Ampel |
|---|---|---|
| Leistung grün, Schlussformel rot | Uneinvernehmliche Trennung | Orange-Rot |
| Verhalten grün, Leistung rot | Netter, aber leistungsschwacher Mitarbeiter | Rot |
| Eigeninitiative und "nach Anweisung" im selben Zeugnis | Inkonsistenz | Orange |
| Sehr warme Schlussformel bei schwacher Leistungsbeurteilung | Verdacht auf Gefälligkeitsformel | Orange |
| Positive Einzelsätze, negative Gesamtzufriedenheitsformel | Bewusste Irreführung | Rot |
| Spitzensatz und Durchschnittssatz im selben Themenbereich | Schaufenster-Pattern (siehe bereichs-drift-detektor) | Rot |

## Beispiele

**Beispiel 1 – Leistung grün, Schlussformel rot:** "Die Leistungen waren stets hervorragend" (Grün) + keine Schlussformel (Rot) → deutet auf Streit beim Ausscheiden oder feindseligen Abgang.

**Beispiel 2 – Innere Inkonsistenz:** "Herr Braun arbeitete stets eigenverantwortlich" (Satz 3) vs. "Er erledigte die ihm nach Anweisung zugewiesenen Aufgaben zuverlässig" (Satz 7) → direkte inhaltliche Contradiction.

**Beispiel 3 – Warme Schlussformel bei Note-4-Leistung:** Leistung mit "bemüht" (Rot, Note 4), Schlussformel vollständig und warm → vermutlich persönliches Gefälligkeitszeugnis, nicht authentisch.

**Beispiel 4 – Reihenfolge-Anomalie:** Abschnitt 1 (Leistung): hervorragend. Abschnitt 2 (Verhalten): Kollegen vor Vorgesetzten + "direkte Kommunikationsweise". Abschnitt 3 (Schlussformel): vollständig. → Einstellender wird Verhaltensteil isoliert bewerten.

**Beispiel 5 – Positiver Leistungsteil, fehlende Integrität:** Alle Leistungsaussagen grün, kein einziges Wort zu Zuverlässigkeit oder Vertrauen bei einem Buchhalter → der Widerspruch zwischen Lob und Schweigen ist das rote Signal.

## Ausgabeformat

Der Skill listet jeden erkannten Widerspruch mit den sich widersprechenden Sätzen, dem Widerspruchstyp, der Signalwirkung für eingeweihte Personalverantwortliche und einer Handlungsempfehlung (Klärung beim Aussteller / Nachverhandlung / Klageprüfung). Am Ende folgt eine Gesamteinschätzung der Zeugniskonsistenz (hoch/mittel/niedrig).

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

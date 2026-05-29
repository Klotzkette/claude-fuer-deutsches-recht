---
name: gesamtnoten-aggregation
description: "Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO Gesamteindruck BAG-Linie zur Gewichtung Zeugnisbereiche. Prüfraster Gewichtung Leistungsteil Verhaltensteil Schlussformel Ausreisser-Saetze Bereichs-Drift. Output Begründete Gesamtnotenspanne mit Gewichtungsmatrix für Mandantenbericht und Klageantrag. Abgrenzung zu satzweise-notenmatrix (Einzelsatz-Bewertung) und bereichs-drift-detektor."
---

# Gesamtnoten-Aggregation

Die Gesamtnote eines Arbeitszeugnisses ergibt sich nicht aus einem einfachen Durchschnitt aller Einzelsätze. Der Skill bildet deshalb keine Scheinmathematik, sondern eine begründete Notenspanne aus Gesamtbild, Kernformel, Leistungsteil, Verhaltensteil, Schlussformel, Auslassungen und Drift.

Orientierungsstruktur: Die Leistungsbeurteilung hat regelmäßig das höchste Gewicht, die Verhaltensbeurteilung folgt dicht dahinter. Die Schlussformel ist ein starkes Praxissignal, aber kein gesetzlicher Pflichtbaustein mit fixer Prozentzahl. Die Zufriedenheitsformel bleibt der wichtigste Einzelindikator innerhalb der Leistungsbeurteilung, darf aber nicht blind gegen den Rest des Zeugnisses ausgespielt werden.

Besondere Gewichtungsregeln: Rote Signale bei der Verhaltensbeurteilung, fehlende Führungsaussagen bei tatsächlicher Führungsverantwortung oder eine auffällige Bereichs-Drift können das Gesamtbild deutlich verschieben. Eine kalte Schlussformel kann ein gutes Zeugnis erklären oder relativieren, sollte aber nicht mechanisch eine Note absenken. Sie wird als Kontextsignal ausgewiesen und rechtlich gesondert eingeordnet.

Bereichs-Drift-Penalty: Liegt im selben Themenbereich (Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis, Sozialverhalten) eine Notenspreizung von zwei oder mehr Stufen zwischen Höchst- und Niedrigsnote vor, wird die rechnerische Gesamtnote um eine halbe Stufe nach unten korrigiert. Konstant niedrige Noten (durchgehend Note 3) in den weichen Bereichen Innovation, Lernbereitschaft oder Sozialverhalten ziehen zusätzlich eine halbe Stufe Abschlag, weil Drift dort am stärksten ins Gewicht fällt. Der Bereichs-Drift-Detektor liefert die hierfür notwendigen Einzelbefunde, die satzweise Notenmatrix liefert die Datenbasis.

Die Gesamtnote wird als Spanne ausgegeben (z. B. "Note 2 bis Note 3"), weil die Interpretation von Zeugnissen immer eine subjektive Komponente hat. Der Skill gibt zusätzlich an, welche Einzelformulierung den größten positiven und negativen Einfluss auf die Gesamtnote hatte.

## Geheimcode-Regeln

| Teilbereich | Gewicht | Besonderheit |
|---|---|---|
| Leistungsbeurteilung gesamt | ca. 50% | Zufriedenheitsformel als Kernindikator |
| Verhaltensbeurteilung | ca. 30% | Reihenfolge und Auslassungen beachten |
| Schlussformel | Kontextsignal | Signalwirkung und Anspruch trennen |
| Rote Auslassung (Integrität/Loyalität) | Gesondert | Kann Gesamtnote um eine Note senken |
| Widersprechende Signale | Gesondert | Führen zu Unsicherheitsabschlag |
| Bereichs-Drift zwei Stufen | minus halbe Stufe | Schaufenster-Pattern |
| Konstante Note 3 in weichen Bereichen | minus halbe Stufe | Lernen, Innovation, Sozialverhalten |

## Beispiele

**Beispiel 1 – Klares Note-1-Zeugnis:** Leistungsbeurteilung grün (Note 1), Verhalten grün (Note 1), Schlussformel grün (Note 1) → Gesamtnote: Note 1. Keine Abweichungen.

**Beispiel 2 – Gemischtes Zeugnis Note 2-3:** Leistung grün (Note 2), Verhalten orange (Note 3), Schlussformel orange (Note 3) → Gewichteter Wert: ca. Note 2 bis 3. Empfehlung: Verhaltens- und Schlussformel nachverhandeln.

**Beispiel 3 – Rote Auslassung senkt Note:** Zeugnis insgesamt Note 2 aus Einzelwertungen, aber fehlende Loyalitätsaussage bei einer Führungskraft → Gesamtnote abgesenkt auf Note 2-3 mit Hinweis auf das Loyalitätssignal.

**Beispiel 4 – Widersprüchliches Zeugnis:** Leistung grün, Verhalten rot, Schlussformel grün → Note 2 bis 3 mit Unsicherheitsabschlag wegen Widerspruchs; Skill empfiehlt Verweis auf widerspruechliche-bewertungen.

**Beispiel 5 – Minimalistisches Zeugnis:** Alle Aussagen orange (Note 3), vollständige Schlussformel → Gesamtnote: Note 3. Verbesserungspotenzial in allen Bereichen.

**Beispiel 6 – Schaufenster-Zeugnis:** Spitzensätze grün (Note 1) bei Fachkenntnissen, Arbeitsweise, Arbeitsergebnis; daneben orange Sätze (Note 3) zu Lernbereitschaft, Innovation, Sozialverhalten; Schlussformel grün (Note 1). Rechnerischer Wert vor Penalty: Note 1 bis 2. Drift-Penalty Lernbereitschaft: minus halbe Stufe. Konstante Note 3 in weichen Bereichen: minus halbe Stufe. Gesamtnote: Note 2 bis Note 3, nicht Note 1 wie die Schaufenster-Sätze suggerieren.

## Ausgabeformat

Der Skill gibt aus: Gewichtete Einzelbewertungen je Teilbereich (Tabelle), Gesamtnoten-Spanne (z. B. Note 2 bis Note 3), entscheidendes positives Signal (bestes Einzelelement), entscheidendes negatives Signal (schlechtestes Einzelelement), und Handlungsempfehlung (Akzeptieren/Nachverhandeln/Klageprüfung).

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis; Grundlage aller Bewertungen
- **§§ 195, 199 BGB** — Verjährung drei Jahre ab Jahresende

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

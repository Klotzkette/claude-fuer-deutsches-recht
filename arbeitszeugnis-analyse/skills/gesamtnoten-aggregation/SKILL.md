---
name: gesamtnoten-aggregation
description: "Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO Gesamteindruck BAG-Linie zur Gewichtung Zeugnisbereiche. Pruefraster Gewichtung Leistungsteil Verhaltensteil Schlussformel Ausreisser-Saetze Bereichs-Drift. Output Begruendete Gesamtnotenspanne mit Gewichtungsmatrix fuer Mandantenbericht und Klageantrag. Abgrenzung zu satzweise-notenmatrix (Einzelsatz-Bewertung) und bereichs-drift-detektor."
---

# Gesamtnoten-Aggregation

Die Gesamtnote eines Arbeitszeugnisses ergibt sich nicht aus einem einfachen Durchschnitt aller Einzelsätze. Stattdessen werden die Teile unterschiedlich gewichtet, und bestimmte Einzelsignale können die Gesamtnote trotz eines ansonsten guten Zeugnisses erheblich senken. Dieser Skill berechnet die Gesamtnote systematisch aus den Ergebnissen der vorgelagerten Analyse-Skills.

Gewichtungsstruktur: Die Leistungsbeurteilung hat das höchste Gewicht (ca. 50 Prozent der Gesamtnote), gefolgt von der Verhaltensbeurteilung (ca. 30 Prozent) und der Schlussformel (ca. 20 Prozent). Die Zufriedenheitsformel ist dabei der wichtigste Einzelindikator innerhalb der Leistungsbeurteilung — sie allein kann für bis zu einem Drittel der Gesamtnote verantwortlich sein.

Besondere Gewichtungsregeln: Rote Signale in der Schlussformel können ein ansonsten grünes Zeugnis auf Note 3 absenken, weil Eingeweihte die Schlussformel besonders genau lesen. Rote Signale bei der Verhaltensbeurteilung (insbesondere fehlende Loyalität bei Führungskräften oder falsche Reihenfolge der Personengruppen) können die Gesamtnote um bis zu eine Note nach unten ziehen. Eine fehlende Integritätsaussage bei einem Zeugnis in vertrauensrelevanter Position wird als eigenständiges rotes Signal mit starker Abwertungswirkung behandelt.

Bereichs-Drift-Penalty: Liegt im selben Themenbereich (Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis, Sozialverhalten) eine Notenspreizung von zwei oder mehr Stufen zwischen Höchst- und Niedrigsnote vor, wird die rechnerische Gesamtnote um eine halbe Stufe nach unten korrigiert. Konstant niedrige Noten (durchgehend Note 3) in den weichen Bereichen Innovation, Lernbereitschaft oder Sozialverhalten ziehen zusätzlich eine halbe Stufe Abschlag, weil Drift dort am stärksten ins Gewicht fällt. Der Bereichs-Drift-Detektor liefert die hierfür notwendigen Einzelbefunde, die satzweise Notenmatrix liefert die Datenbasis.

Die Gesamtnote wird als Spanne ausgegeben (z. B. „Note 2 bis Note 3"), weil die Interpretation von Zeugnissen immer eine subjektive Komponente hat. Der Skill gibt zusätzlich an, welche Einzelformulierung den größten positiven und negativen Einfluss auf die Gesamtnote hatte.

## Geheimcode-Regeln

| Teilbereich | Gewicht | Besonderheit |
|---|---|---|
| Leistungsbeurteilung gesamt | ca. 50% | Zufriedenheitsformel als Kernindikator |
| Verhaltensbeurteilung | ca. 30% | Reihenfolge und Auslassungen beachten |
| Schlussformel | ca. 20% | Fehlende Elemente stark abwertend |
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

- **BAG, Urt. v. 18.11.2014 — 9 AZR 584/13**, NZA 2015, 345 — Beweislastverteilung bei Notenstufen: Note schlechter als befriedigend beweist Arbeitgeber; Note besser als befriedigend beweist Arbeitnehmer.
- **BAG, Urt. v. 12.08.2008 — 9 AZR 632/07**, BAGE 127, 232 — Wohlwollensgebot: Formulierungen, die Fortkommen unnötig erschweren, sind berichtigungspflichtig, auch wenn wahr.

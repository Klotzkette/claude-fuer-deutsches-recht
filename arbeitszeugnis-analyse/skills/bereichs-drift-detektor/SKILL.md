---
name: bereichs-drift-detektor
description: "Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich (Fachkenntnisse, Arbeitsweise, Engagement, Innovation, Erfolg, Sozialverhalten) und schlaegt Alarm bei systematischer Notenspreizung."
---

# Bereichs-Drift-Detektor (Schaufenster-Pattern)

Ein Zeugnis kann handwerklich gut aussehen und trotzdem in der Gesamtschau eine schlechtere Note tragen als die Spitzensätze suggerieren. Das geschieht, wenn der Aussteller jedem Themenbereich einen starken Eröffnungssatz (Note 1) voranstellt und unmittelbar darauf einen abschwächenden Folgesatz (Note 3) zum selben Thema platziert. Der unbedarfte Leser bleibt an den ersten Sätzen hängen und übersieht die Korrektur. Eingeweihte lesen die Drift und schließen auf eine systematische Abwertung.

Der Skill bildet acht Themenbereiche ab, in denen sich Drift typischerweise verbirgt: Fachkenntnisse, Weiterbildung und Lernbereitschaft, strategisches und konzeptionelles Denkvermögen, Arbeitsweise und Sorgfalt, Eigeninitiative und Engagement, Innovationsfähigkeit, Arbeitsergebnisse und Erfolge sowie Sozialverhalten gegenüber Vorgesetzten, Kollegen und Externen. Innerhalb jedes Bereichs werden alle zugehörigen Sätze gesammelt und mit einer Einzelnote belegt. Die Spreizung zwischen Höchst- und Niedrigsnote pro Bereich ergibt den Drift-Wert.

Eine Drift von zwei Stufen oder mehr innerhalb desselben Themenbereichs ist ein eigenständiges rotes Signal und wird in der Gesamtnoten-Aggregation gesondert berücksichtigt. Eine Drift von einer Stufe ist ein oranges Signal und deutet auf bewusste Vorsicht des Ausstellers hin. Eine bereichsübergreifende, gleichbleibend hohe Bewertung ohne Drift gilt als authentisch grün.

Besonders heikel sind Drifts in den weichen Bereichen Lernbereitschaft, Innovation und Sozialverhalten: Sie betreffen genau jene Eigenschaften, die ein einstellender Arbeitgeber für Zukunftsentscheidungen am stärksten gewichtet. Ein Spitzenwert bei Fachkenntnissen mit gleichzeitiger Drift bei Lernbereitschaft signalisiert: Der Kandidat kann was er kann, aber wenig Neues mehr.

## Geheimcode-Regeln

| Drift-Befund | Signalwirkung | Ampel |
|---|---|---|
| Note eins und Note drei zum selben Themenbereich direkt aufeinanderfolgend | Schaufenster-Eroeffnung mit kodierter Korrektur | Rot |
| Spreizung zwei Stufen innerhalb eines Bereichs | Systematische Abwertung | Rot |
| Spreizung eine Stufe innerhalb eines Bereichs | Bewusste Vorsicht | Orange |
| Drift bei Lernbereitschaft trotz starker Fachkenntnisse | Stagnationssignal | Rot |
| Drift bei Sozialverhalten trotz starker Leistungsteile | Konfliktsignal | Rot |
| Drift bei Innovation trotz starker Arbeitsweise | Routinesignal | Orange |
| Bereichsuebergreifend konstante Note eins | Authentisch grün | Grün |

## Beispiele

**Beispiel 1 – Klassische Schaufenster-Drift bei Lernbereitschaft:** Satz A: „verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches ueber aeusserst profundes Fachwissen" (Note 1). Satz B unmittelbar darauf: „nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil" (Note 3). Beide gehoeren zum Themenbereich Fachwissen/Lernen. Drift zwei Stufen, Rot.

**Beispiel 2 – Drift bei Arbeitsweise und Innovation:** Satz A: „fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus" (Note 1). Satz B: „war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze" (Note 3, da „gute" statt „hervorragende" und keine Steigerungsadverbien). Drift zwei Stufen im weichen Bereich, Rot.

**Beispiel 3 – Drift im Sozialverhalten trotz Top-Erfolg:** Satz A: „Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen" (Note 1). Satz B im Sozialteil: „war ein geschaetzter Ansprechpartner, sein persoenliches Verhalten war einwandfrei" (Note 3, da „einwandfrei" ohne „stets" und „geschaetzt" ohne Steigerung). Themen unterschiedlich, aber Drift in einem heiklen Bereich, Rot.

**Beispiel 4 – Drift eine Stufe:** „aeusserst motiviert die gesetzten Ziele beharrlich zu verfolgen" (Note 1) und kurz darauf „zeigte eine hohe Lernbereitschaft" (Note 2 bis 3). Eine Stufe, Orange.

**Beispiel 5 – Keine Drift, authentisch:** Alle Saetze im Bereich Fachkenntnisse tragen durchgehend Steigerungsadverbien und Superlative auf Note-1-Niveau. Keine Drift, Grün.

## Ausgabeformat

Der Skill gibt aus: pro Themenbereich eine Tabelle mit den enthaltenen Saetzen, der Einzelnote je Satz, dem hoechsten und niedrigsten Wert sowie der Drift-Spreizung. Anschliessend eine Bereichsbilanz mit Drift-Wert, Ampelzuordnung und Hinweis auf besonders heikle Bereiche (Lernbereitschaft, Innovation, Sozialverhalten). Am Ende eine Gesamtdrift-Einschaetzung mit Empfehlung: Akzeptieren, Nachverhandeln einzelner Saetze, Klagepruefung.

## Rechtliche Einordnung und Normen

- **§ 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich sein; widersprüchliche Bewertungen im selben Themenbereich verstoßen gegen Wohlwollensgebot
- **§ 242 BGB** — Treu und Glauben; innerhalb desselben Zeugnisabschnitts darf der Arbeitgeber nicht gleichzeitig Bestnoten und Mängel bescheinigen

## Aktuelle Rechtsprechung

- **BAG, Urt. v. 12.08.2008 — 9 AZR 632/07**, BAGE 127, 232 — Wohlwollensgebot verbietet Formulierungen, die Fortkommen unnötig erschweren; ein Zeugnis mit systemischen Widersprüchen im Leistungsbereich ist berichtigungspflichtig.
- **LAG Köln, Urt. v. 22.11.2019 — 7 Sa 523/19** — Drift zwischen Überschrift-Note und Einzelsatz-Note: Wenn die Zufriedenheitsformel Note 1 verspricht, aber einzelne Leistungssätze Note 3-4 signalisieren, überwiegt die schwächere Note für die Gesamtbewertung; Kläger kann auf Kohärenz klagen.

## Triage — vor der Drift-Prüfung

1. Welche Themenblöcke sind im Zeugnis enthalten? (Fachkenntnisse, Motivation, Qualität, Teamverhalten, Führung, Schluss)
2. Wurde die Zufriedenheitsformel bereits ausgewertet? (Satzweise-Notenmatrix-Skill?)
3. Ziel der Drift-Analyse: Klageantrag-Vorbereitung oder Mandantenberatung?

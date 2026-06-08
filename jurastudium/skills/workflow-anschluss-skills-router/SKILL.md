---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Anschluss-Skills Router

## Arbeitsbereich

Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe
Diese Prüfungslinie leitet nach der ersten Prüfung in die passenden Fachmodule des Plugins `jurastudium`. Er entlastet Studierende und Referendare, indem er Sachverhalt, Klausurformat und Vorbereitungsphase einsortiert.

## Routing-Heuristik
- **Zivilrechtsklausur, Sachverhalt mit Anspruch:** -> `loesungsschemata`, `subsumtionslehre`, `gutachten-uebung`, `methodenlehre-zivilrecht`.
- **Öffentliches Recht (Verfassung/Verwaltung):** -> `methodenlehre-öffentliches-recht`, `loesungsschemata` (Verfahren: Zulässigkeit, Begründetheit).
- **Strafrecht (Klausur oder AG):** -> `methodenlehre-strafrecht` (Aufbau: TB, RW, Schuld, ggf. Strafe).
- **Lernplanung/Karteikarten:** -> `lernplan`, `karteikarten`, `lernstrategien`, `examens-prognose`.
- **Hausarbeit:** -> `juristisches-schreiben`, Verweis auf Plugin `hausarbeitenmacher`.
- **Mündliche Prüfung / AG-Vortrag:** -> `pruefungsgespraech-ag`, `ag-vorbereitung`.
- **Referendariat (Aktenvortrag, Relation):** -> `jus-referendariat-stationen-spezial`, Plugin `urteilsbauer-relationsmacher`.

## Anti-Muster
- Schemata ohne Subsumtion. Schema ist Gerüst, nicht Ergebnis.
- Anspruchsgrundlagenreihenfolge ignorieren: stets Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

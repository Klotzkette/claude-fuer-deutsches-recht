---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin memorandums-ersteller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill für `memorandums-ersteller` Kaltstart und Routing im Plugin memorandums-ersteller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Memo-Standardstruktur (CLAUDE.md verbindlich)
1. **Sachverhalt** (knapp, faktentreu, keine Wertung).
2. **Frage(n)** (präzise; bei mehreren Anspruchsgrundlagen separat).
3. **Kurzantwort** (1 Satz; trifft die zentrale Aussage).
4. **Rechtliche Bewertung** (Gutachtenstil: Obersatz, Definition, Subsumtion, Zwischenergebnis je Tatbestandsmerkmal).
5. **Gesamtergebnis** (klare Empfehlung + Wahrscheinlichkeit).
6. **Risiken / offene Punkte** (was kann anders entschieden werden? Was fehlt an Tatsachen?).
7. **Quellenverzeichnis** (gem. `references/zitierweise.md`; Rspr. vor Lit., neueste zuerst).

## Tipps
- Maximal 1 Seite Sachverhalt, sonst Anhang. Memo soll auf 5-10 Seiten lesbar bleiben.
- Auslegung nach Savigny-Kanon (Wortlaut, Systematik, Historie, Telos) plus verfassungs-/unionsrechtskonform.
- Anspruchspyramide: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.
- Falle: "Risiken / offene Punkte" weggelassen — gerade hier dokumentieren Sie Haftungsbegrenzung; ein Memo ohne offene Punkte ist verdächtig.

---
name: workflow-unterlagen-lueckenliste
description: "Unterlagen- und Lückenliste im Plugin word-legal-ai-plugin-and-skill-for-german-lawyers: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen."
---

# Unterlagen- und Lückenliste

## Aufgabe
Dieser Workflow-Skill erkennt fehlende Word-Bausteine, Versionen oder Anlagen und erstellt eine präzise Nachforderungsliste. Vermeidet pauschale "Bitte alles schicken"-Anfragen.

## Lückenanalyse Word-Dokumente
- **Vorhanden:** Word-Datei (.docx) -- Version (Microsoft 365 / 2021 / 2019 / Mac).
- **Fehlt typischerweise:** Master-/Briefkopfvorlage, Schriftsatz-Vorlage der Kanzlei, Anlagenkonvolut (.pdf), Originale für Track Changes (.docx mit Markup), Versionshistorie.
- **Bei Schriftsätzen:** Anlagenverzeichnis (K1, K2 / B1, B2) -- jede Anlage mit kurzer Bezeichnung und Beweisthema (§ 130 ZPO).
- **Bei Verträgen:** Term Sheet, Definitions-Glossar, Mitsprache-Matrix, Anlagen mit Disclosure Letter.
- **Bei Memos:** Cover-Letter / Executive Summary, Quellenverzeichnis, Vorgutachten.
- **Bei mehreren Versionen:** alle Versionen mit Versionsstempel und Bearbeiterstatus.

## Nachforderungsbausteine (Beispiel)
- "Bitte senden Sie uns die .docx-Datei mit Track Changes (nicht das PDF-Final), damit wir die Argumentationsgeschichte nachvollziehen können."
- "Bitte das vollständige Anlagenkonvolut nach Nummern (K1-K23) -- aktuell fehlen K4, K11, K17."
- "Welche Word-Version nutzen Sie? Manche Vorlagenfeatures sind versionsabhängig."

## Anti-Muster
- "Bitte alle Unterlagen" -- ineffizient.
- Word-Datei ohne PDF-Final -- Druckbild-Kontrolle fehlt.
- PDF-Final ohne Word -- keine Bearbeitung möglich.

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

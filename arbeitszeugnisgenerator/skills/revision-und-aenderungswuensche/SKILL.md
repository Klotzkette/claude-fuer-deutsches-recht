---
name: revision-und-aenderungswuensche
description: "Überarbeitet ein bereits erteiltes oder entworfenes Zeugnis ohne Notendrift und stellt Alt- und Neufassung mit Begründung gegenüber."
---

# Revision und Änderungswünsche

## Ziel

Nachträgliche Änderungen am generierten Zeugnis konsistent und korrekt umsetzen, ohne ungewollte Drift oder Widersprüche zu erzeugen.

## Arten von Änderungswünschen

| Änderungstyp | Anforderung |
|---|---|
| Einzelnen Satz ändern | prüfen, ob Notenebene des Satzes zur Gesamtnote passt |
| Note anpassen (z.B. von Note 3 auf Note 2) | alle Sätze der betroffenen Achse neu generieren |
| Aufgabenblock ergänzen | neue Aufgaben in den Fließtext integrieren |
| Schlussformel anpassen | zur neuen Note konsistent wählen |
| Formalia korrigieren (Name, Datum, Position) | isolierte Änderung ohne Auswirkung auf Inhalt |
| Gesamtes Zeugnis überarbeiten | Neustart mit bestätigten Stammdaten |

## Konsistenzgebot bei Notenänderung

Ändert sich die Note, müssen alle Sätze der betroffenen Achse angepasst werden. Beispiel: Notenerhöhung von Note 3 auf Note 2 bei Leistung:
- Hauptformel ändern: „zur vollen Zufriedenheit" → „stets zur vollen Zufriedenheit"
- Fachkenntnisse-Satz anpassen: „gute Fachkenntnisse" → „sehr gute Fachkenntnisse"
- Engagement-Satz anpassen: Scheinsteigerer entfernen, Standardsteigerer einsetzen
- Schlussformel prüfen: passt sie noch?

## Änderungsschutz bei Schlussformel

Nach BAG, Urteil v. 06.06.2023 – 9 AZR 272/22 gilt: Wurde eine Schlussformel bereits einmal erteilt, darf der Arbeitgeber sie nicht allein deshalb streichen, weil der Arbeitnehmer berechtigte Änderungswünsche geltend macht. Das ist ein Verstoß gegen das Maßregelungsverbot (Paragraf 612a BGB).

**Konsequenz für den Generator:**
Wenn ein Nutzer einen bereits erteilten Text überarbeiten lässt und dabei die Schlussformel verändern oder streichen möchte: Hinweis ausgeben, dass eine einmal erteilte Schlussformel nicht wegen eines Berichtigungsverlangens gestrichen werden darf.

## Revisions-Workflow

1. **Änderungswunsch klären:** Was soll konkret geändert werden?
2. **Auswirkungscheck:** Welche anderen Sätze sind betroffen?
3. **Konsistenzcheck:** Passt die Änderung zur Gesamtnote?
4. **Drift-Check:** Erzeugt die Änderung eine neue Inkonsistenz?
5. **Ausgabe:** Geänderter Entwurf mit Markierung der geänderten Stellen.

## Markierung von Änderungen

Geänderte Stellen im revidierten Entwurf klar kennzeichnen:
> **[Geändert]** Alle ihr übertragenen Aufgaben erledigte sie **stets** zu unserer **vollen** Zufriedenheit.

## Hinweise auf rechtliche Grenzen bei Revisionen

### Arbeitgeberkündigung nach Revisionsanfrage
Nach Paragraf 612a BGB ist eine Maßregelung des Arbeitnehmers wegen Geltendmachung seiner Rechte verboten. Das gilt auch für das Zeugnis: ein nach Berichtigungsverlangen verschlechtertes Zeugnis ist eine Maßregelung.

### Wunschformulierung durch Arbeitnehmer
Wenn ein Arbeitnehmer einen Wunschentwurf vorlegt, der objektiv zu positiv ist (Note 1 für nachweislich schlechte Leistung), muss der Generator auf die Zeugniswahrheitspflicht hinweisen und ggf. ablehnen.

## Checkliste nach Revision

- Sind alle Leistungssätze konsistent auf der neuen Notenstufe?
- Sind alle Verhaltenssätze konsistent auf der neuen Notenstufe?
- Passt die Schlussformel zur neuen Note?
- Sind keine neuen Drift-Muster entstanden?
- Sind keine neuen Geheimcodes oder Auslassungen entstanden?

## Stolpersteine

- Einzelnen Satz auf Note 1 ändern, ohne die anderen Sätze auf Note 1 anzuheben — erzeugt Drift.
- Schlussformel nach Nutzerrevision streichen, ohne auf BAG 9 AZR 272/22 hinzuweisen.
- Keine Markierung der Änderungen — der Nutzer verliert den Überblick.

## Anti-Muster

- Notenerhöhung ohne Formulierungsanpassung — Schaufenster-Drift.
- Änderungen akzeptieren, die die Zeugniswahrheit verletzen.
- Schlussformel bei Revision ohne Prüfung des Erteilungsschutzes streichen.

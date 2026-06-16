---
name: workflow-unterlagen-lueckenliste
description: "Unterlagen- und Lückenliste im Plugin wandeldarlehen-lebenszyklus: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen."
---

# Unterlagen- und Lückenliste

## Aufgabe
Dieser Workflow-Skill erstellt eine konkrete Nachforderungsliste für Wandeldarlehens-Mandate. Vermeidet "Bitte alles schicken"; verlangt gezielt die Bausteine, die für die Lebenszyklus-Bewertung fehlen.

## Pflichtunterlagen
- **Term Sheet** (final + Vorgängerentwürfe), mit Cap, Discount, Maturity, Trigger.
- **Convertible Loan Agreement (CLA)** in der jeweils gültigen Fassung.
- **Cap Table** vor Wandlung + simuliertes Cap Table nach Wandlung (auch Best/Worst Case).
- **Gesellschaftsvertrag** (Satzung) und Geschäftsordnung Geschäftsführung.
- **Gesellschafterbeschlüsse** zur Kapitalerhöhung / Wandlung.
- **Treuhand-/Sperrkonto-Bestätigung** Bank.
- **Steuerliche Stellungnahme** (KapSt, § 17 EStG, Sachgründungs-Werthaltigkeitsbescheinigung).
- **Rangrücktritt-Vereinbarung** (§ 39 Abs. 2 InsO) bei drohender Insolvenz / wesentlicher Lebensfähigkeit.
- **Investorenkommunikation** zur Folge-Runde (Term Sheet, Closing-Termin).

## Lücken-Diagnose
- Term Sheet ohne Cap / Discount -> nicht vollziehbar.
- CLA ohne Trigger-Definition (Qualified Financing Mindesthöhe, Lead-Investor-Kriterium) -> Wandlung im Streit.
- Cap Table ohne Versionsstempel -> nicht reproduzierbar.
- Kein Rangrücktritt bei drohender Insolvenz -> Anfechtbarkeit § 39 II InsO entfällt.
- Kein Notarprotokoll für Kapitalerhöhung -> Wandlung nicht eingetragen.

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

---
name: workflow-unterlagen-lueckenliste
description: "Unterlagen- und Lückenliste im Plugin insolvenzrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen."
---

# Unterlagen- und Lückenliste

## Aufgabe
Dieser Workflow-Skill für `insolvenzrecht` Unterlagen- und Lückenliste im Plugin insolvenzrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Insolvenzrechtliche Lückenliste je Konstellation
- **Antragsfrage Geschäftsführer (§ 15a InsO):**
  - Liquiditätsstatus zum Stichtag, 13-Wochen-Liquiditätsplan, Liste fälliger Verbindlichkeiten, Bankkontostände.
  - Bilanz nach Liquidationswerten (für § 19 InsO Überschuldung Stufe 1).
  - Fortbestehensprognose 12 Monate IDW EPS 11 (für § 19 InsO Stufe 2).
  - Maßnahmen Rangrücktritte / Patronatserklärungen / Forderungsverzichte.
- **Insolvenzantrag (§ 13 InsO):**
  - Vermögensaufzeichnung (Aktiva, Passiva).
  - Gläubigerverzeichnis mit Adressen, Beträgen, Fälligkeiten, Sicherheiten, Rangstufen.
  - Forderungsverzeichnis (Debitoren).
  - Mitarbeiterliste, Personalkosten letzten 6 Monate.
  - Verbindlichkeiten Finanzamt, Sozialversicherung.
- **Eigenverwaltung § 270a InsO:**
  - Eigenverwaltungsplanung (§ 270a Abs. 1 InsO): Liquiditätsplanung 6 Monate, Sanierungskonzept-Eckpunkte, Verhandlungen mit wichtigsten Gläubigern.
  - Bescheinigung Sachverständiger (in der Praxis IDW S2).
- **Schutzschirm § 270d InsO:**
  - Bescheinigung qualifizierter Sachverständiger über drohende ZU oder Überschuldung **und** Sanierungsaussicht.
- **Anfechtung durch Verwalter:**
  - Kontoauszüge des Schuldners der letzten 3–4 Jahre (je nach § 130, § 133 InsO Anfechtungsfrist).
  - Geschäftspartner-Mahnungen, Stundungsabreden (Indizien für Kenntnis der Krise).
  - Bilanzen, BWA, Liquiditätspläne (für ex-ante-Sicht der Geschäftsführer).
- **Forderungsanmeldung Gläubiger:**
  - Vertrag, Rechnung, Lieferschein, Mahnung, ggf. Titel; Sicherungsabrede (für Aus-/Absonderung).

## Prioritäten setzen
- Bei akuter Antragspflicht zuerst Liquiditätsstatus klären — alles andere nachrangig.
- Lieber Vorabentwurf des Insolvenzantrags mit „[noch zu klären]"-Markern als verzögerte Vollständigkeit.

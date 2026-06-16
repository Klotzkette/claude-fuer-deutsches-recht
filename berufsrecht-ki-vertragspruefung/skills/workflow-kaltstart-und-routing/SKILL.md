---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin berufsrecht-ki-vertragspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill für `berufsrecht-ki-vertragspruefung` Kaltstart und Routing im Plugin berufsrecht-ki-vertragspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing-Diagnose Berufsrecht-KI
- **"Rechtsanwalt prüft KI-Tool"** → § 43e BRAO (Schweigepflicht / Mandantengeheimnis), § 203 StGB strafrechtliche Schweigepflicht, AVV Art. 28 DSGVO.
- **"Steuerberater prüft KI-Tool"** → § 62a StBerG (entspricht § 43e BRAO), § 203 StGB.
- **"Wirtschaftsprüfer prüft KI-Tool"** → § 50a WPO, § 203 StGB.
- **"Notar prüft KI-Tool"** → § 26a BNotO (Verschwiegenheit), § 203 StGB; Vorsicht bei Urkundeninhalten.
- **"Patentanwalt"** → § 39a PAO, § 203 StGB.
- **"KI-System verarbeitet Mandantendaten"** → kumulativ: § 203 StGB (strafrechtlich), § 43a Abs. 2 BRAO (berufsrechtlich), Art. 28 DSGVO (AVV), ggf. KI-VO.
- **"Externer KI-Anbieter (US-Cloud)"** → § 203 Abs. 3 StGB "Mitwirkende" (seit 2017) plus DSGVO-Drittlandstransfer.

## Praxis-Tipp
Die Erweiterung des § 203 Abs. 3 StGB von 2017 ("sonstige mitwirkende Personen") legitimiert die Einbindung externer Dienstleister — aber nur mit angemessener Verpflichtung zur Verschwiegenheit. Bei US-Cloud-Anbietern reicht Standard-AVV nicht: zusätzlich US-Cloud-Act-Risiko (Lawful Access) im TIA dokumentieren.

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

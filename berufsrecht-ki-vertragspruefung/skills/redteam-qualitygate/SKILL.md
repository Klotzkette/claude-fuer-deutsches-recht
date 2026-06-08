---
name: redteam-qualitygate
description: "Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte Berufsrecht-KI
1. **Schweigepflicht-Trias:** § 203 StGB + § 43a Abs. 2 / § 43e BRAO (bzw. § 62a StBerG, § 50a WPO, § 26a BNotO) + AVV Art. 28 DSGVO — alle drei adressiert?
2. **Mitwirkenden-Klausel:** Wurde § 203 Abs. 4 StGB im AVV ausdrücklich umgesetzt? Verpflichtung des Anbieter-Personals?
3. **Datenkategorien:** Werden tatsächlich Mandantendaten verarbeitet? Selbst Metadaten (Mandantenname, Aktenzeichen, Verfahrensart) können Schweigepflicht-relevant sein.
4. **Drittlandstransfer:** Bei US-Cloud DPF-Status (zum Zeitpunkt der Prüfung), SCC-Modul, TIA dokumentiert? Cloud Act-Risiko beschrieben?
5. **Konkretisierung:** Welches konkrete KI-Tool, welche konkrete Funktion? Pauschalfreigaben sind berufsrechtlich nicht haltbar.
6. **Aufklärung Mandant:** Falls erforderlich (Sensibelheit, Marktstandards): Hinweis in Mandatsvereinbarung oder gesondertes Schreiben?
7. **Halluzinations-Check:** Keine erfundenen BGH-Az. (Zivilrechtsweg) oder AnwG-Entscheidungen; keine Vermischung BRAO/BGB/StGB.

## Praxis-Tipp
Die zentrale Empfehlung für KI-Vertragsprüfung bei Berufsträgern: Kategorisiere zuerst die Datenarten (a) keine Mandantendaten, b) anonymisierte/pseudonymisierte Mandantendaten, c) identifizierbare Mandantendaten). Für (c) reicht Standard-AVV nicht — es braucht zusätzlich die Mitwirkenden-Verpflichtung nach § 203 Abs. 4 StGB und ggf. Mandanteneinwilligung. Default für (c) bei US-Cloud: nicht freigeben.

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

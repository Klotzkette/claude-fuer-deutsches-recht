---
name: fristen-und-risikoampel
description: "Fristen- und Risikoampel im Plugin Tabellenreview 3D im Tabellenreview 3d: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fristen- und Risikoampel

## Aufgabe
Dieser Prüfungslinie markiert typische Risiken in juristischen Tabellen: Summenfehler, Versionsdrift, Spalteninkonsistenz, fehlende Belegspalte, falsche Aggregation, Insolvenz-Tabellenfristen.

## Tabellen-Risikoampel
- **Rot:** Summen-Diskrepanz zwischen Footer und Detailzeilen; doppelte Buchung; Falsch-Rundungen über mehrere Stellen.
- **Rot:** Insolvenztabelle ohne Anmeldedatum / Bestreitenstatus.
- **Rot:** Cap Table ohne Versionsangabe / Stichtag.
- **Gelb:** Spalten ohne Definition; Datentypen-Inkonsistenz (Datum als Text); fehlende Quellenspalte.
- **Gelb:** Verlinkungen auf externe Excel-Dateien -- gehen leicht verloren.
- **Grün:** Spaltendefinition vorhanden, Summenkontrolle ok, Quellenspalte gefüllt, Versionsfooter.

## Spezifische Fristen bei juristischen Tabellen
- **Insolvenztabelle (§ 174 ff. InsO):** Anmeldefrist ergibt sich aus § 28 Abs. 1 InsO (gerichtliche Festsetzung); Prüfungstermin nach § 29 InsO.
- **Cap Table (Wandeldarlehen):** Maturity Trigger sechs Monate vorher kommunizieren.
- **JVEG-Stundenaufstellung:** Antragsfrist max. 3 Monate ab Beendigung der Tätigkeit (§ 2 JVEG); Wiedereinsetzungsmoeglichkeit eng.
- **Forderungstabelle Mahnverfahren:** Beim Vollstreckungsbescheid Einspruchsfrist 2 Wochen.

## Anti-Muster
- Pivot-Tabelle ohne dokumentiertes Datenmodell -- nicht reproduzierbar.
- Direktes Drüber-Formatieren statt Bedingter Formatierung -- führt zu visueller, nicht logischer Konsistenz.

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

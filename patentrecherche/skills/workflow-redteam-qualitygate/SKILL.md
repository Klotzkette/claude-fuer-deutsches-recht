---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Patentrecherche: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Red-Team Qualitygate

## Arbeitsbereich

Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe
Dieser Prüfungslinie prüft Recherche-Ergebnisse vor Lieferung an Mandant oder Mandantin auf typische Fehler: unvollständige Suchstrategie, übersehene Klassen, falscher Stichtag, fehlende NPL-Berücksichtigung, Verwechslung Veröffentlichungstyp.

## Red-Team-Punkte Patentrecherche
- **Suchstrategie dokumentiert?** Datenbank, Datum, Boolean-String, IPC/CPC-Klassen, Sprachen, Trefferzahl, Auswahlbegründung.
- **IPC + CPC** beide eingesetzt? CPC ist feinere kooperative Klassifikation (EPA/USPTO); reine IPC verliert Recall.
- **Sprachen breit genug?** Englisch + Deutsch + Französisch + Japanisch + Chinesisch (per maschineller Übersetzung in Espacenet/Patentscope).
- **Stichtag korrekt?** Prioritätstag (für Neuheit), nicht Anmeldetag, nicht Veröffentlichungstag.
- **NPL (Non-Patent-Literature) berücksichtigt?** Konferenzbeiträge, Master-/Doktorarbeiten, GitHub-Commits, Whitepaper, Pre-Prints (arXiv) -- können neuheitsschädlich sein.
- **Veröffentlichungstyp korrekt?** EP -A1 (Offenlegung mit Recherche), -A2 (Offenlegung ohne Recherche), -A3 (Recherche nachgereicht), -B1 (erteilte Fassung), -B2 (Einspruchsänderung).
- **Statuscheck:** in Kraft, abgelaufen, erloschen, validiert in welchen Ländern?
- **UPC-Opt-out:** für die Validity-/FTO-Bewertung wichtig: bleibt EPÜ-Patent unter UPC-Zuständigkeit oder Opt-out gemeldet?
- **Familienanalyse:** Geschwistermarken in anderen Jurisdiktionen, INPADOC-Familie.
- Falle: aus dem Modell Patentnummern oder Zitate "ergänzen" -- jede Nummer im Register live verifizieren.

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

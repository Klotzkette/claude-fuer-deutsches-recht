---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Patentrecherche."
---

# Red-Team Qualitygate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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


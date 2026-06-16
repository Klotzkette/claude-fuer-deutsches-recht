---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin vertragsausfueller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill für `vertragsausfueller` Kaltstart und Routing im Plugin vertragsausfueller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing-Heuristik Vertragsausfueller

- **Template-Erkennung:** Welche Vertragsart liegt vor (NDA, MSA/Rahmenvertrag, SaaS, Werk, Liefer/AGB)?
  - NDA: -> Plugin `nda-abgleich` Skills.
  - SaaS/MSA: -> Skill `vaf-konzern-rahmenvertrag-anpassen`.
  - AGB/Standard-Lieferbedingungen: -> Plugin `agb-recht-pruefer`.
- **Platzhalter-Strategie:**
  - Vollstaendige Daten -> Direkt ausfuellen (`vaf-clean-output`).
  - Daten unvollstaendig -> Fragebogen-Modus (`vaf-fragebogen-input-leitfaden`).
  - Komplexer Konzernverbund -> Batch-Modus (`vaf-batch-modus-konzern`).
- **Bilingual/Multi-Lingual:**
  - Englisch-Deutsch parallel -> Skill `vaf-fremdsprachige-vertraege-bilingual`.
  - Mehrsprachig (3+ Sprachen) -> `vaf-mehrsprachige-vertraege-spezial`.
- **Format:**
  - .docx mit Tracked Changes -> Skill `vaf-redline-qa`.
  - .docx ohne Markierung -> `vaf-docx-stripper`.

## Vertragsabschluss-Form sicher pruefen

- **Schriftform § 126 BGB (eigenhaendige Unterschrift, alle Erklaerungen auf derselben Urkunde):** Mietvertrag fuer 1 Jahr ueberschreitend (§ 550 BGB), Buergschaft (§ 766 BGB), Verbraucherdarlehen (§ 492 BGB).
- **Textform § 126b BGB (lesbarer Text, Person des Erklaerenden genannt, dauerhaft):** E-Mail, PDF, SMS reichen aus; Standardform fuer Widerrufsbelehrung, Mahnung, Kuendigung von Verbrauchervertraegen ueber digitale Plattformen.
- **Qualifizierte elektronische Signatur (qES) § 126a BGB:** Ersetzt Schriftform, sofern nicht ausgeschlossen (§ 484 Abs. 1 BGB Teilzeit-Wohnrechtevertrag, § 623 BGB Arbeitsvertrag-Kuendigung, § 766 S. 2 BGB Buergschaftserklaerung im B2C).
- **eIDAS-VO 910/2014:** Qualifizierte Vertrauensdiensteanbieter; QES europaweit gleichwertig wie handschriftliche Unterschrift.
- **Formfrei:** Grundsatz der Formfreiheit (§ 311 BGB; § 154 BGB nur bei strittiger Einigung); Beweisfunktion der Schriftform sollte trotzdem beachtet werden.

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

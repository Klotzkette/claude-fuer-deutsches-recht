---
name: workflow-kaltstart-und-routing
description: "Wenn es um Kaltstart und Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Kaltstart und Routing

## Aufgabe
Nutze diesen Workflow-Skill für Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.

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

- Schriftform nach Paragraf 126 BGB: etwa Wohnraummietvertrag mit Laufzeit über einem Jahr nach Paragraf 550 BGB, Bürgschaft nach Paragraf 766 BGB oder Verbraucherdarlehen nach Paragraf 492 BGB; jeweilige Sonderregeln und Ausschlüsse prüfen.
- Textform nach Paragraf 126b BGB: Bei Grundstücks- und Gewerberaummietverträgen mit Laufzeit über einem Jahr gilt sie über Paragraf 578 Absatz 1 in Verbindung mit Paragraf 550 BGB. Bei Altverträgen Entstehungs- und Änderungsdatum nach Artikel 229 Paragraf 70 EGBGB einordnen.
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
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

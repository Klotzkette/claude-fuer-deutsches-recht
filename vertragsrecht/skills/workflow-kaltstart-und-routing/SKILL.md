---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Vertragsrecht."
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

## Routing-Heuristik Vertragsrecht

- **Verbraucher (§ 13 BGB) involviert?**
  - Ja, und Fernabsatz/außerhalb von Geschäftsräumen: -> Skill `widerruf-fernabsatz`.
  - Ja, AGB der Gegenseite: -> Plugin `agb-recht-pruefer`, Skill `agb-pruefung-kaltstart`.
- **Vertragsschluss-Stadium?**
  - Antrag/Annahme strittig (§§ 145 ff. BGB): Auslegungs- und Bindungsdauer prüfen (§§ 145, 147, 148 BGB).
  - Form streitig: § 126 BGB Schriftform, § 126a BGB qES, § 126b BGB Textform (-> Plugin `schriftform-und-textform-bgb`).
- **Leistungsstörung?**
  - Verzug §§ 280, 286, 288 BGB; Schadensersatz §§ 280-283 BGB; Rücktritt §§ 323, 326 BGB; Skill `vert-leistungsstoerungen-leitfaden`.
- **Mängel?**
  - Kauf: §§ 434-453 BGB, Verjährung § 438 BGB.
  - Werk: §§ 633-651 BGB, Verjährung § 634a BGB.
- **NDA-Bezug?**
  - Vertragsentwurf: Plugin `nda-abgleich`.
- **B2B Rahmenvertrag/SaaS:**
  - Skills `saas-msa-pruefung`, `vert-rahmenvertrag-einzelabrufe-spezial`.
- **Internationaler Bezug?**
  - Rom I-VO Art. 3, 4 (Rechtswahl, objektive Anknüpfung); CISG Art. 1, 6 (UN-Kaufrecht); Brüssel Ia-VO 1215/2012 (Gerichtsstand).

## Erste-Schritt-Sofortmaßnahmen je nach Fall

- **Verjährungsfrist droht (binnen 30 Tagen):** Sofort Verjährungshemmung prüfen (§ 203 BGB Verhandlungen, § 204 BGB Klage, Mahnverfahren § 204 Abs. 1 Nr. 3 BGB).
- **Widerrufsfrist droht:** § 355 Abs. 2 BGB (14 Tage ab Erhalt) bzw. § 356 Abs. 3 S. 2 BGB (12 Monate + 14 Tage bei fehlender Belehrung).
- **Verzug der Gegenseite:** Mahnung + Fristsetzung (§ 286 Abs. 1 BGB) als Erstmaßnahme.

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

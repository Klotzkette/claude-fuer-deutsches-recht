---
name: kreuzblatt-konsistenzpruefung
description: "Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Prüfbericht mit Fehlerliste. Abgrenzung: nicht Risikoampel-Aggreg..."
---

# /tabellenreview-3d:kreuzblatt-konsistenzprüfung

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Methodik

1. **Achsen-Match:** dieselbe Zeile dieselbe Spalte aber unterschiedliches Arbeitsblatt: vergleichen.
2. **Faktischer Widerspruch:** beide Arbeitsblätter haben das Vertragsdatum extrahiert; das eine sagt 2021-03-15, das andere 2021-03-25. Das ist ein Datenfehler — Prüfer-Flag.
3. **Perspektivischer Widerspruch:** ein Arbeitsblatt sagt 'wirksam' das andere 'unwirksam'. Wenn beide Arbeitsblätter dieselbe Norm benutzen ist es Datenfehler; wenn unterschiedliche Normen (Recht vs Steuer) ist es legitime Abweichung — als `legitim` markieren.
4. **Ampel-Inkonsistenz:** dieselbe Zeile in einem Arbeitsblatt rot in einem gelb in einem grün — Konsolidierungsempfehlung an `risikoampel-aggregation`.
5. **Norm-Bezugs-Widerspruch:** ein Arbeitsblatt verweist auf BGB Paragraph 307, ein anderes auf BGB Paragraph 305c bei derselben Klausel. Beides möglich — Prüfer-Hinweis.

## Konflikt-Klassifikation

- **echter Widerspruch:** beide Antworten beanspruchen dieselbe Tatsache aber unterscheiden sich. Prüfer-Flag rot.
- **legitime perspektivische Abweichung:** Arbeitsblätter haben unterschiedliche Prüfmassstaebe. Vermerk gelb.
- **Datenfehler:** OCR-Konfidenz schwach in einem der Arbeitsblätter — Re-Run dieser Zelle.
- **Klassifikationsfehler:** Dokumenttyp falsch erkannt — Zeile neu klassifizieren.

## Ausgabe

- `widerspruchsbericht.md` mit pro Widerspruch:
 - Zeile (Dokument)
 - Spalte (Datenpunkt)
 - Arbeitsblatt-A und Arbeitsblatt-B mit jeweiliger Antwort
 - Konflikt-Klassifikation
 - Empfohlene Aktion (Re-Run / Prüfer / Konsolidierung)

## Beispiele

- **echter Widerspruch:** Kundenvertrag-042. Spalte 'Laufzeit'. Recht: '3 Jahre + 1 Jahr Verlängerung'. Wirtschaft: '4 Jahre Festlaufzeit'. Echter Widerspruch — Wirtschaft hat den Vertrag verkürzt gelesen.
- **legitime Abweichung:** Lizenzvertrag-018. Spalte 'Haftung'. Recht: 'unwirksam BGB Paragraph 309 Nr 7'. Steuer: 'irrelevant — Pauschalhaftungs-Aufwand absetzbar'. Legitim — unterschiedliche Prüfmassstaebe.

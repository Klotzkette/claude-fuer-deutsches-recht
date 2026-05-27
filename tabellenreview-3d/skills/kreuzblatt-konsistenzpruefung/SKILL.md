---
name: kreuzblatt-konsistenzpruefung
description: "Kreuzblatt-Konsistenzpruefung: Abgleich der drei Dimensionen Forderung-Pruefung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Pruefraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Pruefbericht mit Fehlerliste. Abgrenzung: nicht Risikoampel-Aggregation."
---

# /tabellenreview-3d:kreuzblatt-konsistenzprüfung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Zweck

Eine Zelle die rechtlich grün aber datenschutzrechtlich rot ist ist nicht automatisch ein Fehler — sie ist eine perspektivische Abweichung. Oft aber ist sie ein Fehler: dieselbe Tatsache wurde in zwei Arbeitsblättern unterschiedlich erfasst. Dieser Skill findet beides.

## Methodik

1. **Achsen-Match:** dieselbe Zeile dieselbe Spalte aber unterschiedliches Arbeitsblatt: vergleichen.
2. **Faktischer Widerspruch:** beide Arbeitsblätter haben das Vertragsdatum extrahiert; das eine sagt 2021-03-15, das andere 2021-03-25. Das ist ein Datenfehler — Prüfer-Flag.
3. **Perspektivischer Widerspruch:** ein Arbeitsblatt sagt 'wirksam' das andere 'unwirksam'. Wenn beide Arbeitsblätter dieselbe Norm benutzen ist es Datenfehler; wenn unterschiedliche Normen (Recht vs Steuer) ist es legitime Abweichung — als `legitim` markieren.
4. **Ampel-Inkonsistenz:** dieselbe Zeile in einem Arbeitsblatt rot in einem gelb in einem grün — Konsolidierungsempfehlung an `risikoampel-aggregation`.
5. **Norm-Bezugs-Widerspruch:** ein Arbeitsblatt verweist auf BGB Paragraph 307, ein anderes auf BGB Paragraph 305c bei derselben Klausel. Beides möglich — Prüfer-Hinweis.

## Konflikt-Klassifikation

- **echter Widerspruch:** beide Antworten beanspruchen dieselbe Tatsache aber unterscheiden sich. Prüfer-Flag rot.
- **legitime perspektivische Abweichung:** Arbeitsblätter haben unterschiedliche Pruefmassstaebe. Vermerk gelb.
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
- **legitime Abweichung:** Lizenzvertrag-018. Spalte 'Haftung'. Recht: 'unwirksam BGB Paragraph 309 Nr 7'. Steuer: 'irrelevant — Pauschalhaftungs-Aufwand absetzbar'. Legitim — unterschiedliche Pruefmassstaebe.

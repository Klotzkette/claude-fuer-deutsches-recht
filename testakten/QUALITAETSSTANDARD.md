# Qualitätsstandard für Testakten

Testakten sind keine Examensfälle mit sauberer Lösungsskizze. Sie sind Arbeitsakten: widersprüchlich, unvollständig, manchmal unangenehm banal und gerade dadurch nützlich. Jede Akte soll das jeweilige Plugin herausfordern, ohne die rechtliche Einordnung vorwegzunehmen.

## Pflichtstruktur

Jede Testakte enthält künftig zwei parallele Zugänge:

1. Disparate Arbeitsakte: Einzeldateien in realistischen Formaten, zum Beispiel Markdown-Notizen, EML-Dateien, DOCX-Schreiben, Excel/CSV-Tabellen, PDFs, JPEG-Screenshots, Chat-Exporte oder Scan-PDFs.
2. Gesamt-PDF: ein konsolidiertes, lesbares PDF unter `gesamt-pdf/<aktenordner>_gesamt.pdf`, damit man die Akte am Stück lesen, ausdrucken und in Vorführungen schnell öffnen kann.

Das Gesamt-PDF ersetzt die Einzeldokumente nicht. Es ist die Lesefassung neben dem Aktenchaos.

## Inhaltliche Qualität

- Keine vorgefertigte Lösung, keine versteckte Musterantwort.
- Keine sichtbaren Platzhalter in der Akte selbst.
- Keine Texte, die aus der Aktenlogik fallen oder die Arbeitsakte als Übungsmaterial markieren.
- Mehrere plausible Deutungen, aber keine absichtlichen Quatschfehler.
- Widersprüche dort, wo echte Mandate sie haben: Datum, Erinnerung, Zuständigkeit, technische Ursache, Zustellung, Beweiswert, Rechenweg.
- Belege nicht nur behaupten, sondern als Datei, Tabelle, E-Mail, Scan oder Foto anlegen.
- Juristische Spezialfragen nicht spoilern; die Akte darf neugierig machen, soll aber nicht lösen.

## Dateiformate im Akten-ZIP — Grundregel für alle Testakten

Der Akten-ZIP-Export ist das Herzstück der Lebensnähe: ein hybrider, bewusst unaufgeräumter Formatemix, wie er im Anwaltsalltag anfällt. Daran wird gezeigt, wie eine KI echte Dateien liest, umbenennt und umwandelt. Deshalb gilt verbindlich — auch für jede künftig von Menschen oder Coding-Agents erzeugte Testakte:

- **Kein Markdown als Aktenstück.** Aktenstücke liegen in lebensechten Formaten vor: gut formatierte Word-Dokumente mit Briefkopf (DOCX, Times New Roman 11 pt), generierte oder gescannt wirkende PDFs, krude Excel-Tabellen (XLSX/CSV), echte E-Mail-Dateien (EML), Screenshots und Fotos (JPG/PNG), Chat-Exporte (TXT) und gelegentlich eine PowerPoint. Je gemischter, desto besser — Inhalt und Nummerierung bleiben mit dem Gesamt-PDF identisch.
- **Markdown ist nur erlaubt** für README, `rubric.yaml`-Begleitung und Meta-/Lösungsdateien, die `scripts/testakte_file_filter.py` ohnehin vom PDF/ZIP-Export ausschließt.
- **Werkzeuge:** `scripts/convert-testakte-aktenstuecke-nativ.py` wandelt Markdown-Aktenstücke in formatierte DOCX um (bestehende gleichnamige DOCX-Zwillinge gewinnen); `scripts/validate-testakten-keine-markdown-aktenstuecke.py` prüft die Regel repo-weit. Der Gesamt-PDF-Builder liest DOCX, XLSX, PDF, Bilder und EML nativ.
- **Neue Akten** werden von Anfang an in nativen Formaten angelegt; wer schneller in Markdown entwirft, konvertiert vor dem Commit und baut das Gesamt-PDF neu.

## Technische Qualität

- Gesamt-PDF ohne offensichtlichen Textüberlauf, mit lesbarem Cover und Dateiabschnitten.
- Umlaute und ß in menschlichem Text verwenden.
- Einzeldateien sinnvoll benennen, aber nicht steril.
- Download-Hinweise gehören in README-Dateien, nicht in die Aktenstücke selbst; README und zentrale Übersicht müssen Gesamt-PDF, Akten-ZIP und Einzel-PDF-ZIP aufführen.
- Der CI-Check `scripts/validate-testakten-gesamt-pdf.py` muss grün sein.
- Der CI-Check `scripts/validate-testakten-readme-downloads.py` muss grün sein.

## Nach größeren Änderungen

```bash
python3 scripts/build-testakte-gesamt-pdf.py <aktenordner>
python3 scripts/inject-gesamt-pdf-section.py
python3 scripts/validate-testakten-gesamt-pdf.py
python3 scripts/validate-testakten-readme-downloads.py
```

In der lokalen Desktop-Umgebung kann dafür der gebündelte Python verwendet werden, wenn die normale Python-Umgebung keine PDF-Bibliotheken enthält.

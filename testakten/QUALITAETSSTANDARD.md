# Qualitätsstandard für Testakten

Testakten sind keine Examensfälle mit sauberer Lösungsskizze. Sie sind Arbeitsakten: widersprüchlich, unvollständig, manchmal unangenehm banal und gerade dadurch nützlich. Jede Akte soll das jeweilige Plugin herausfordern, ohne die rechtliche Einordnung vorwegzunehmen.

## Pflichtstruktur

Jede Testakte wird in drei gleichwertigen Fassungen ausgeliefert:

1. Gesamt-PDF: ein konsolidiertes, durchsuchbares PDF unter `gesamt-pdf/<aktenordner>_gesamt.pdf`, damit sich die Akte am Stück lesen und ausdrucken lässt. Es enthält weder eine Hinweisseite noch den verbindlichen zweisprachigen Warntext; dieser steht unmittelbar über dem Downloadlink oder der Downloadtabelle auf der README-Seite.
2. Einzel-PDF-ZIP: jede Unterlage als eigene PDF ohne Hinweisseite oder Warntext. Sämtliche PDFs liegen unmittelbar auf der Wurzelebene des ZIPs; frühere Ordnernamen werden bei Bedarf mit doppeltem Unterstrich in den Dateinamen übernommen. Hinzu kommt die UTF-8-kodierte `README.txt`, die mit dem verbindlichen zweisprachigen Hinweis beginnt.
3. Akten-ZIP: die disparaten Originaldateien in realistischen Formaten, etwa EML, DOCX, XLSX, CSV, PDF, JPG, PNG oder TXT. Auch dieses ZIP ist vollständig flach und enthält weder Unterordner noch Markdown-Dateien. Hinzu kommt ausschließlich die UTF-8-kodierte `README.txt`, die mit dem verbindlichen zweisprachigen Hinweis beginnt.

Das Gesamt-PDF ersetzt die Einzeldokumente nicht. Es ist die Lesefassung neben den heterogenen Originaldateien. Die beiden ZIPs müssen nach dem Öffnen sofort ihre Dateien zeigen, ohne vorgeschalteten Aktenordner.

## Inhaltliche Qualität

- Keine vorgefertigte Lösung, keine versteckte Musterantwort.
- Keine sichtbaren Platzhalter in der Akte selbst.
- Keine Texte, die aus der Aktenlogik fallen oder die Arbeitsakte als Übungsmaterial markieren. Der nachfolgende verbindliche Herkunfts- und Risikohinweis bleibt außerhalb der PDFs auf den Downloadseiten und in der `README.txt` der Archive; er enthält keine Lösung und keine fachliche Bewertung.
- Mehrere plausible Deutungen, aber keine absichtlichen Quatschfehler.
- Widersprüche dort, wo echte Mandate sie haben: Datum, Erinnerung, Zuständigkeit, technische Ursache, Zustellung, Beweiswert, Rechenweg.
- Belege nicht nur behaupten, sondern als Datei, Tabelle, E-Mail, Scan oder Foto anlegen.
- Juristische Spezialfragen nicht spoilern; die Akte darf neugierig machen, soll aber nicht lösen.

## Dateiformate im Akten-ZIP — Grundregel für alle Testakten

Der Akten-ZIP-Export ist das Herzstück der Lebensnähe: ein hybrider, bewusst unaufgeräumter Formatemix, wie er im Anwaltsalltag anfällt. Daran wird gezeigt, wie eine KI echte Dateien liest, umbenennt und umwandelt. Deshalb gilt verbindlich — auch für jede künftig von Menschen oder Coding-Agents erzeugte Testakte:

- **Kein Markdown als Aktenstück.** Aktenstücke liegen in lebensechten Formaten vor: Word-Dokumente mit Briefkopf, schlichte Bürodateien, generierte oder gescannt wirkende PDFs, unbereinigte Excel-Tabellen, echte E-Mail-Dateien, Screenshots, Fotos und Chat-Exporte. Inhalt und Nummerierung bleiben mit dem Gesamt-PDF konsistent.
- **Markdown bleibt außerhalb der Auslieferung.** README-Dateien und redaktionelle Begleittexte dürfen im Repository als Markdown vorliegen, werden aber aus Akten-ZIP und Einzel-PDF-ZIP ausnahmslos herausgefiltert. Die vom Builder erzeugte `README.txt` ist die einzige obligatorische Begleitdatei in beiden ZIP-Varianten.
- **Flache Archive sind verbindlich.** Weder das Akten-ZIP noch das Einzel-PDF-ZIP darf Verzeichniseinträge oder Dateipfade mit `/` enthalten. Gleichnamige Dateien aus früheren Unterordnern erhalten kollisionssichere Namen mit doppeltem Unterstrich.
- **Werkzeuge:** `scripts/convert-testakte-aktenstuecke-nativ.py` wandelt Markdown-Aktenstücke in formatierte DOCX um (bestehende gleichnamige DOCX-Zwillinge gewinnen); `scripts/validate-testakten-keine-markdown-aktenstuecke.py` prüft die Regel repo-weit. Der Gesamt-PDF-Builder liest DOCX, XLSX, PDF, Bilder und EML nativ.
- **Neue Akten** werden von Anfang an in nativen Formaten angelegt; wer schneller in Markdown entwirft, konvertiert vor dem Commit und baut das Gesamt-PDF neu.

## Verbindlicher Herkunfts- und Risikohinweis

Der Wortlaut ist unveränderlich:

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

Gesamt-PDF und Einzel-PDFs enthalten weder eine Hinweisseite noch diesen Warntext. Auf der Repository-Startseite, im Download-Index sowie in den zentralen, aktenbezogenen und Plugin-READMEs steht der vollständige Hinweis unmittelbar vor jeder PDF-/ZIP-Downloadgruppe für Testakten. Ein allgemeiner Hinweis an anderer Stelle genügt nicht.

Im Akten-ZIP und im Einzel-PDF-ZIP beginnt die UTF-8-kodierte `README.txt` mit dem zweisprachigen Hinweis; die Datei liegt wie alle übrigen Dateien unmittelbar auf der ZIP-Wurzelebene. Auch Sammelpakete mit Testakten enthalten eine entsprechend beginnende `README.txt` auf ihrer Wurzelebene. Die Builder und README-Generatoren ergänzen den Hinweis reproduzierbar; die Release-Validatoren prüfen Wortlaut und Position sowie die Abwesenheit des Warntexts in den PDFs.

## Technische Qualität

- Gesamt-PDF ohne offensichtlichen Textüberlauf, mit lesbarem Cover und Dateiabschnitten.
- Umlaute und ß in menschlichem Text verwenden.
- Einzeldateien sinnvoll benennen, aber nicht steril. Ein Aktenstück bildet genau ein Dokument ab; mehrere Schreiben dürfen nicht als Sammeldokument in einer Einzel-PDF zusammengezogen werden.
- Download-Hinweise gehören unmittelbar über die betreffenden Links oder Tabellen in README-Dateien, nicht in die Aktenstücke selbst; README und zentrale Übersicht müssen Gesamt-PDF, Akten-ZIP und Einzel-PDF-ZIP aufführen.
- Der CI-Check `scripts/validate-testakten-gesamt-pdf.py` muss grün sein.
- Der CI-Check `scripts/validate-testakten-readme-downloads.py` muss grün sein.
- Die ZIP-Validatoren müssen den zweisprachigen Hinweis am Anfang der `README.txt` beider ZIP-Varianten und Sammelpakete sowie seine Abwesenheit in jedem PDF bestätigen.

## Nach größeren Änderungen

```bash
python3 scripts/build-testakte-gesamt-pdf.py <aktenordner>
python3 scripts/build-testakten-release-zips.py dist/testakten <aktenordner>
python3 scripts/build-testakten-einzelpdf-zips.py dist/testakten <aktenordner>
python3 scripts/inject-gesamt-pdf-section.py
python3 scripts/validate-testakten-gesamt-pdf.py
python3 scripts/validate-testakten-readme-downloads.py
python3 scripts/validate-testakten-release-zips.py dist/testakten <aktenordner>
python3 scripts/validate-testakten-einzelpdf-zips.py dist/testakten <aktenordner>
```

In der lokalen Desktop-Umgebung kann dafür der gebündelte Python verwendet werden, wenn die normale Python-Umgebung keine PDF-Bibliotheken enthält.

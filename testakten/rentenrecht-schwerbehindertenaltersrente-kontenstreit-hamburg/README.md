# Rentenakte Schwerbehindertenaltersrente und Kontenstreit Hamburg

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg_gesamt.pdf`](gesamt-pdf/rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zur Durchsetzung einer vorgezogenen Altersrente für schwerbehinderte Menschen mit streitiger Wartezeit, Kontenlücken und unklarer Zugangslage des GdB-Bescheids. Die Akte ist für `rentenpruefer` und `fachanwalt-sozialrecht` gedacht.

Enthalten sind Rentenauskunft, Versicherungsverlauf, Arbeitgebernachweise, Pflegezeiten, GdB-Bescheid, Pflegekassenbescheid, Berechnungsmatrix, Mandantenbrief und der Entwurf für Widerspruch sowie Kontenklärung.

## Aktenstruktur

```
rentenrecht-schwerbehindertenaltersrente-kontenstreit-hamburg/
├── 02_drv_auskunft_wartezeit.docx           # DRV-Auskunft: 406 von 420 Wartezeitmonaten, Nachweisbitte
├── 03_versicherungsverlauf_luecken.docx     # Verlauf mit markierten Lücken und Randbemerkungen
├── 04_gdb_bescheid_auszug.docx              # Feststellungsbescheid GdB 50 mit Nachprüfungsvermerk
├── 05_arbeitgebernachweise_werft.docx       # Arbeitszeugnis, Lohnsteuerkarten und AOK-Karteikarte
├── 06_pflegezeiten_mutter.docx              # Pflege der Mutter 2012 bis 2014 und Meldelücke
├── 07_berechnungsmatrix_wartezeit.csv     # Streitige Zeiträume, Monate, Nachweise, Erfolgschance
├── 08_widerspruch_und_kontenklaerung.docx   # Kontenklärungsantrag und vorsorglicher Widerspruch
├── 09_mandantenbrief_unterlagenliste.docx   # Mandantenbrief mit Unterlagenliste und Fahrplan
├── 10_rentenbeginn_varianten.csv          # Varianten des Rentenbeginns mit Risiken
├── 11_pflegekassenbescheid_2013.docx        # Pflegekassenbescheid zur Pflegeperson mit 17 Wochenstunden
├── 12_kontenstreit_datenkern.csv          # Datenkern: streitige Zeiträume, anerkannte/fehlende Monate, Nachweismittel und Erfolgschance
├── 13_bruder_erklaerung_pflege_2026-07-04.docx  # Eidesstattliche Erklärung des Bruders zur Pflege der Mutter
├── 14_pflegedienst_elbblick_rechnungsliste.csv  # Rechnungsliste Pflegedienst Elbblick Februar 2012 bis Mai 2014 mit Erst- und Schlussbeleg
├── eml/
│   ├── 01_versorgungsamt_gdb_bestaetigung.eml     # Versorgungsamt bestätigt GdB 50 ab 01.01.2026
│   ├── 02_sanftleben_an_drv_kontenklaerung.eml    # Bevollmächtigte an DRV zur Kontenklärung und Beweisersatz
│   ├── 03_bruder_thomas_lammers_pflege.eml        # Bruder zu Pflegeumfang und Unterlagen
│   ├── 04_drv_zwischennachricht_kontenklaerung.eml # Zwischennachricht der DRV: Archivanfragen laufen, Leistungsakte 1993 vernichtet, Wiedervorlage 25.09.2026
│   └── chatverlauf_lammers_brueder.txt            # Chat der Brüder zur Beschaffung der Alt-Nachweise
├── README.md                              # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                            # Konsolidierte Lesefassung der Akte
└── rubric.yaml                            # Prüfkriterien für die Bearbeitung
```

# Rentenrechtsakte Fremdrente Russlanddeutscher Sibirien Bielefeld

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld_gesamt.pdf`](gesamt-pdf/rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zu einem Kontenklärungs- und Altersrentenstreit eines Russlanddeutschen, der 1992 nach Deutschland kam, beruflich stark abgestiegen ist und jetzt russische Arbeits- und Archivunterlagen übersetzen, plausibilisieren und gegenüber der DRV verwerten muss. Die Akte ist für `rentenpruefer` und `fachanwalt-sozialrecht` gedacht.

Enthalten sind ausformulierte Aktenstücke, der Kontenklärungsbescheid, übersetzte russische Arbeits- und Archivunterlagen, Fristenmaterial, Tabellen und Arbeitsentwürfe. Die rechtliche Bewertung bleibt offen; die Unterlagen liefern den Sachverhalt für Widerspruch, Anlagenmappe und eine spätere sozialgerichtliche Klage.

Der Datenauswertungs-Kern liegt in der Entgeltpunkt-Berechnungstabelle (`11_frg_entgeltpunkte_berechnung.csv`) und dem zugehörigen Berechnungsvermerk: Aus Monaten, Tabellenwert je Monat, Sechstelkürzung glaubhaft gemachter Zeiten und der 40-Prozent-Begrenzung lassen sich die anrechenbaren Entgeltpunkte und der Kürzungsbetrag exakt nachrechnen. Beteiligte sind neben Eduard Klassen (Mandant), seiner Tochter Alina Klassen, der Cousine Olga Reimer, der Ehefrau Lidia Klassen, dem Rentenberater Gerhard Wittkamp und der Übersetzerin Natalia Gerlach nun auch die Sachbearbeiterin H. Brinkschulte (DRV Westfalen) und Waldemar Penner (Landsmannschaft der Deutschen aus Russland, Beratungsstelle OWL).

## Aktenstruktur

```
rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld/
├── 02_drv_bescheid_kontenklaerung_auszug.docx            # Kontenklärungsbescheid mit FRG-Vormerkung und Mitwirkungsfrist
├── 03_arbeitsbuch_uebersetzung_auszug.docx               # Beglaubigt übersetzte Arbeitsbuchauszüge mit Auffälligkeiten
├── 04_lebenslauf_berufsabstieg.docx                      # Herkunftsberuf, Deutschlandphase, Mandantenperspektive
├── 05_archivanfrage_nowosibirsk_email.eml                # E-Mail der Tochter zu Archiv, Fotos und Namensschreibweise
├── 06_frg_zeitenmatrix.csv                               # Zeiträume, Belege, DRV-Bewertung und offene Aufgaben
├── 07_widerspruch_entwurf.docx                           # Ausformulierter Widerspruch mit Anlagen und Verfahrensbitte
├── 08_anlagenverzeichnis_uebersetzung.docx               # Übersetzungsmappe mit Qualitätsvermerk
├── 09_klageraster_sozialgericht.docx                     # Beweisprogramm und Vergleichsoption für den Klagefall
├── 10_archivbescheinigung_nowosibirsk_1994.docx          # Übersetzte Archivbescheinigung mit Fondswechsel-Hinweis
├── 11_frg_entgeltpunkte_berechnung.csv                   # Datenkern: Monate, Tabellenwert, Sechstel, Begrenzung, anrechenbare EP
├── 12_email_cousine_olga_nowosibirsk.eml                 # E-Mail der Cousine mit Archivauskunft zu Fonds und Qualifikation
├── 13_erklaerung_auslaendischer_rentenbezug_2026-07-03.docx # Mitwirkungserklärung zum ausländischen Rentenbezug (Endprodukt)
├── 14_whatsapp_tochter_archiv.txt                        # Chat Tochter/Rentenberater zu Apostille, Archiv und Namensfrage
├── 15_vertriebenenausweis_bvfg_kopie.docx                # Bescheinigung nach dem Bundesvertriebenengesetz (Kopie)
├── 16_uebersetzerin_rueckfrage_vollstaendiges_arbeitsbuch.eml # Rückfrage zu Originalvorlage, Namensschreibweise und Fondsnummern
├── 17_telefonvermerk_mandant_originalunterlagen.docx      # Gespräch zu Arbeitsbuch, Archivpapier und Unterlagen von 2011
├── eml/
│   ├── 01_drv_westfalen_mitwirkung_erklaerung.eml        # DRV Westfalen: Mitwirkungsfrist, Fonds R-2214/R-2298, Sechstel
│   ├── 02_landsmannschaft_uebersetzung_transliteration.eml # Landsmannschaft: Transliteration Klassen/Klassen, Fondswechsel
│   └── 03_wittkamp_intern_berechnung_qualifikationsgruppe.eml # Interner Rechenweg QG3 gegen QG2 (Grundlage der Tabelle)
├── README.md                                             # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                           # Konsolidierte Lesefassung der Akte
└── rubric.yaml                                           # Prüfkriterien für die Bearbeitung
```

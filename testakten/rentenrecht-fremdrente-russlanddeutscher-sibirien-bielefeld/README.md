# Rentenrechtsakte Fremdrente Russlanddeutscher Sibirien Bielefeld


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 43 KB) | PDF | [`gesamt-pdf/rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld_gesamt.pdf`](gesamt-pdf/rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zu einem Kontenklärungs- und Altersrentenstreit eines Russlanddeutschen, der 1992 nach Deutschland kam, beruflich stark abgestiegen ist und jetzt russische Arbeits- und Archivunterlagen übersetzen, plausibilisieren und gegenüber der DRV verwerten muss. Die Akte ist für `rentenpruefer` und `fachanwalt-sozialrecht` gedacht.

Enthalten sind ausformulierte Aktenstücke, der Kontenklärungsbescheid, übersetzte russische Arbeits- und Archivunterlagen, Fristenmaterial, Tabellen und Arbeitsentwürfe. Die rechtliche Bewertung bleibt offen; die Unterlagen liefern den Sachverhalt für Widerspruch, Anlagenmappe und eine spätere sozialgerichtliche Klage.

Der Datenauswertungs-Kern liegt in der Entgeltpunkt-Berechnungstabelle (`11_frg_entgeltpunkte_berechnung.csv`) und dem zugehörigen Berechnungsvermerk: Aus Monaten, Tabellenwert je Monat, Sechstelkürzung glaubhaft gemachter Zeiten und der 40-Prozent-Begrenzung lassen sich die anrechenbaren Entgeltpunkte und der Kürzungsbetrag exakt nachrechnen. Beteiligte sind neben Eduard Klassen (Mandant), seiner Tochter Alina Klassen, der Cousine Olga Reimer, der Ehefrau Lidia Klassen, dem Rentenberater Gerhard Wittkamp und der Übersetzerin Natalia Gerlach nun auch die Sachbearbeiterin H. Brinkschulte (DRV Westfalen) und Waldemar Penner (Landsmannschaft der Deutschen aus Russland, Beratungsstelle OWL).

## Aktenstruktur

```
rentenrecht-fremdrente-russlanddeutscher-sibirien-bielefeld/
├── 01_mandatsnotiz_fristsache.docx                       # Person, Zuzug 1992, Bescheidlage, Arbeitsauftrag
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
├── 13_erklaerung_auslaendischer_rentenbezug_2026-07-03.docx # Mitwirkungserklärung zum ausländischen Rentenbezug (Endprodukt)
├── 14_whatsapp_tochter_archiv.txt                        # Chat Tochter/Rentenberater zu Apostille, Archiv und Namensfrage
├── eml/
│   ├── 01_drv_westfalen_mitwirkung_erklaerung.eml        # DRV Westfalen: Mitwirkungsfrist, Fonds R-2214/R-2298, Sechstel
│   ├── 02_landsmannschaft_uebersetzung_transliteration.eml # Landsmannschaft: Transliteration Klassen/Klasssen, Fondswechsel
│   └── 03_wittkamp_intern_berechnung_qualifikationsgruppe.eml # Interner Rechenweg QG3 gegen QG2 (Grundlage der Tabelle)
├── README.md                                             # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                           # Konsolidierte Lesefassung der Akte
├── rubric.yaml                                           # Prüfkriterien für die Bearbeitung
├── 91_fristsachen_belege_offene_punkte_2026-07-06.csv    # Fristsachen, Belege und offene Punkte (Ergaenzung v426)
└── eml/2026-07-06_sachstand_nachforderung.eml            # Sachstand zur Nachforderung (Ergaenzung v426)
```

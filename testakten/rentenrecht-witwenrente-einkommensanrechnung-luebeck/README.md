# Rentenrecht: Witwenrente und Einkommensanrechnung in Lübeck


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 65 KB) | PDF | [`gesamt-pdf/rentenrecht-witwenrente-einkommensanrechnung-luebeck_gesamt.pdf`](gesamt-pdf/rentenrecht-witwenrente-einkommensanrechnung-luebeck_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-witwenrente-einkommensanrechnung-luebeck.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-witwenrente-einkommensanrechnung-luebeck.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-witwenrente-einkommensanrechnung-luebeck-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-witwenrente-einkommensanrechnung-luebeck-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Marlies Thormählen, 59, ist seit dem 14.04.2026 verwitwet. Ihr Ehemann Hinnerk Thormählen war Schiffsmechaniker und später Hafenmeister; sein Versicherungsverlauf enthält lange Pflichtbeitragszeiten, aber auch ungeklärte Auslandsmonate in Dänemark. Die DRV bewilligt eine große Witwenrente ab dem 01.05.2026, rechnet jedoch nach dem Sterbevierteljahr eigenes Erwerbseinkommen, eine kleine Betriebsrente und eine private Sofortrente an. Die Mandantin versteht nicht, weshalb die Rente im August 2026 stark sinken soll.

Die Akte enthält Rentenbescheid, Einkommensunterlagen, Betriebsrentenmitteilung, Krankenkassenmitteilung, Arbeitgeberbescheinigung, Lohnabrechnungswerte, Kontoauszug, eine eigene Berechnung und einen Widerspruchsentwurf. Der Fall zwingt zur Trennung von Sterbevierteljahr, großer Witwenrente, Einkommensanrechnung, pauschaler Nettoermittlung, KVdR-Abzügen und Kontenklärung.

Der Datenauswertungs-Kern liegt in der Anrechnungstabelle (`13_witwenrente_anrechnung_berechnung.csv`) und dem zugehörigen Berechnungsvermerk. Aus Bruttoeinkommen, pauschalem Nettoabzug, Freibetrag (das 26.4fache des Rentenwerts, 1076.86 EUR) und dem 40-Prozent-Ansatz lässt sich die gekürzte Witwenrente je Monat nachrechnen: im Sterbevierteljahr Mai bis Juli 2026 keine Anrechnung und Zahlbetrag 1287.62 EUR, ab August 2026 belegbar 213.48 EUR (ohne private Sofortrente) oder hilfsweise 308.86 EUR (mit privater Sofortrente). Die Diskrepanz zwischen gemeldetem und tatsächlichem Einkommen tritt hervor, weil der Bescheid einen nicht nachvollziehbaren Anrechnungsbetrag von 458.44 EUR ansetzt, der ein Nettoeinkommen von 2222.96 EUR voraussetzt, und weil das gemeldete schwankende Gesamtbrutto (bis 2807.20 EUR mit Einmalzahlung) vom laufenden Grundentgelt (2240.00 EUR) abweicht. Neu als Beteiligte hinzugekommen sind die Rentenberaterin Frauke Jessen (Bevollmächtigte), der DRV-Sachbearbeiter Petersen, die Personalsachbearbeiterin Kareen Nold und die Tochter Wiebke; reale Träger sind die Deutsche Rentenversicherung Nord und das Sozialgericht Lübeck.

## Aktenstruktur

```
rentenrecht-witwenrente-einkommensanrechnung-luebeck/
├── 01_mandatsnotiz_fristsache.docx                      # Erstgespräch, Frist, Beteiligte, Beratungsziel
├── 02_drv_bescheid_witwenrente.docx                     # DRV-Bewilligungsbescheid mit Berechnung und Rechtsbehelfsbelehrung
├── 03_einkommen_und_betriebsrente.docx                  # Vermerk zur Einkommenslage: Lohn, Betriebsrente, Sofortrente
├── 04_kvdr_und_beitragsabzug.docx                       # Krankenkassenmitteilung zur KVdR und Beitragsdifferenz
├── 05_widerspruch_entwurf.docx                          # Ausformulierter Widerspruch gegen Anrechnung und Kontenlücke
├── 06_berechnungsmatrix_witwenrente.csv                 # Monatswerte, Anrechnungsbetrag, Zahlbetrag, Prüfvermerke
├── 07_daenemark_kontenklaerung.docx                     # Dänische Nachweise und Antrag auf zwischenstaatliche Kontenklärung
├── 08_arbeitgeberbescheinigung_und_lohnabrechnung.docx  # Entgeltbescheinigung mit Zulagen und Juni-Lohnabrechnung
├── 09_email_betriebsrente_nachfrage.eml                 # HansePort-Antwort zur Witwenversorgung des Verstorbenen
├── 10_kontoauszug_und_fragenliste.txt                   # Kontoumsätze und offene Mandantenfragen
├── 11_hzvk_betriebsrentenmitteilung.docx                # HZVK-Schreiben zur eigenen Betriebsrente der Mandantin
├── 12_hl_leben_leistungsmitteilung.docx                 # Versichererbestätigung der privaten Sofortrente
├── 13_witwenrente_anrechnung_berechnung.csv             # Datenkern: Brutto, Netto, Freibetrag, Anrechnung und Zahlbetrag je Monat
├── 14_berechnungsvermerk_einkommensanrechnung_2026-07-08.docx # Interner Vermerk, rechnet Anrechnung und Zahlbetrag nach
├── 15_widerspruchsbegruendung_anrechnung_2026-07-09.docx # Widerspruchsbegründung an die DRV Nord (Endprodukt)
├── 16_whatsapp_tochter_daenemark_ordner.txt             # Chat mit der Tochter zu dänischen Lohnzetteln und Geldsorgen
├── eml/
│   ├── 01_drv_nord_anrechnung_grundlagen.eml            # DRV Nord: Freibetrag, Gesamtbrutto und einbezogene Renten
│   ├── 02_arbeitgeber_entgelt_klarstellung.eml          # Arbeitgeber: laufendes Entgelt gegen Einmalzahlungen
│   └── 03_jessen_intern_anrechnung_nachgerechnet.eml    # Interner Rechenweg, warum 458.44 EUR nicht haltbar ist
├── README.md                                            # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                           # Konsolidierte Lesefassung der Akte
└── rubric.yaml                                           # Prüfkriterien für die Bearbeitung
├── 90_realitaetskern_und_arbeitsauftrag_2026-07-06.docx  # Realitaetskern und Arbeitsauftrag (Ergaenzung v426)
├── 91_fristsachen_belege_offene_punkte_2026-07-06.csv    # Fristsachen, Belege und offene Punkte (Ergaenzung v426)
├── eml/2026-07-06_sachstand_nachforderung.eml            # Sachstand zur Nachforderung (Ergaenzung v426)
```

## Aktenstücke

| Datei | Inhalt |
| --- | --- |
| `01_mandatsnotiz_fristsache.docx` | Erstgespräch, Frist, Beteiligte, Beratungsziel |
| `02_drv_bescheid_witwenrente.docx` | Bewilligungsbescheid mit Rentenbeginn, Zahlbetrag und Berechnung |
| `03_einkommen_und_betriebsrente.docx` | Vermerk zu Lohn, Betriebsrente, privater Sofortrente, Pauschalnetto |
| `04_kvdr_und_beitragsabzug.docx` | Krankenkasse, Kranken- und Pflegeversicherungsbeiträge |
| `05_widerspruch_entwurf.docx` | Widerspruch gegen Einkommensanrechnung und Kontenlücken |
| `06_berechnungsmatrix_witwenrente.csv` | Monatswerte, Freibetrag, Anrechnungsbetrag, Zahlbetrag |
| `07_daenemark_kontenklaerung.docx` | Auslandszeiten, Nachweise und Auskunftsersuchen |
| `08_arbeitgeberbescheinigung_und_lohnabrechnung.docx` | Arbeitgeberbescheinigung, Schichtzulagen und Lohnabrechnungswerte |
| `09_email_betriebsrente_nachfrage.eml` | Nachfrage zur Zusatzversorgung und zum Zahlbeginn |
| `10_kontoauszug_und_fragenliste.txt` | Kontoauszugsausschnitt und Mandantenfragen |
| `11_hzvk_betriebsrentenmitteilung.docx` | Betriebsrentenmitteilung der Zusatzversorgungskasse |
| `12_hl_leben_leistungsmitteilung.docx` | Leistungsmitteilung des privaten Versicherers |
| `13_witwenrente_anrechnung_berechnung.csv` | Datenkern: Anrechnung und Zahlbetrag je Monat |
| `14_berechnungsvermerk_einkommensanrechnung_2026-07-08.docx` | Interner Berechnungsvermerk zur Einkommensanrechnung |
| `15_widerspruchsbegruendung_anrechnung_2026-07-09.docx` | Widerspruchsbegründung an die DRV Nord |
| `16_whatsapp_tochter_daenemark_ordner.txt` | Chat mit der Tochter zu den dänischen Lohnzetteln |
| `eml/01_drv_nord_anrechnung_grundlagen.eml` | Grundlagen der Anrechnung laut DRV Nord |
| `eml/02_arbeitgeber_entgelt_klarstellung.eml` | Laufendes Entgelt gegen Einmalzahlungen |
| `eml/03_jessen_intern_anrechnung_nachgerechnet.eml` | Interne Nachrechnung des Anrechnungsbetrags |

## Bearbeitungsziel

Die Akte soll eine Rentenberatung dazu zwingen, den Zahlbetrag nicht nur überschlägig zu kommentieren, sondern die Berechnung Monat für Monat nachzuvollziehen. Zu prüfen sind Sterbevierteljahr, große Witwenrente, pauschale Nettoermittlung, Betriebsrentenabgrenzung, Krankenversicherung der Rentner und die Frage, ob dänische Seefahrtszeiten rentenerhöhend nachzufordern sind.

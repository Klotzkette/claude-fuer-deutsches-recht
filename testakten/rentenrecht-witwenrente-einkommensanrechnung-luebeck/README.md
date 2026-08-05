# Rentenrecht: Witwenrente und Einkommensanrechnung in Lübeck

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-witwenrente-einkommensanrechnung-luebeck_gesamt.pdf`](gesamt-pdf/rentenrecht-witwenrente-einkommensanrechnung-luebeck_gesamt.pdf) |
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
rentenrecht-witwenrente-einkommensanrechnung-lübeck/
├── 02_drv_bescheid_witwenrente.docx                     # DRV-Bewilligungsbescheid mit Berechnung und Rechtsbehelfsbelehrung
├── 03_einkommen_und_betriebsrente.docx                  # Vermerk zur Einkommenslage: Lohn, Betriebsrente, Sofortrente
├── 04a_hansekrankenkasse_kvdr_mitteilung_2026-06-25.docx # Eigenständige Krankenkassenmitteilung
├── 04b_telefonnotiz_personalabteilung_2026-06-27.docx   # Gesonderte Telefonnotiz zur Entgeltabrechnung
├── 05_widerspruch_entwurf.docx                          # Ausformulierter Widerspruch gegen Anrechnung und Kontenlücke
├── 06_berechnungsmatrix_witwenrente.csv                 # Monatswerte, Anrechnungsbetrag, Zahlbetrag, Prüfvermerke
├── 07_daenemark_kontenklaerung.docx                     # Dänische Nachweise und Antrag auf zwischenstaatliche Kontenklärung
├── 08a_arbeitgeberbescheinigung_entgelt_2026.docx       # Eigenständige Arbeitgeberbescheinigung
├── 08b_lohnabrechnung_juni_2026.docx                    # Gesonderte Juni-Lohnabrechnung
├── 09_email_betriebsrente_nachfrage.eml                 # HansePort-Antwort zur Witwenversorgung des Verstorbenen
├── 10_kontoauszug_und_fragenliste.txt                   # Kontoumsätze und offene Mandantenfragen
├── 11_hzvk_betriebsrentenmitteilung.docx                # HZVK-Schreiben zur eigenen Betriebsrente der Mandantin
├── 12_hl_leben_leistungsmitteilung.docx                 # Versichererbestätigung der privaten Sofortrente
├── 13_witwenrente_anrechnung_berechnung.csv             # Datenkern: Brutto, Netto, Freibetrag, Anrechnung und Zahlbetrag je Monat
├── 14_daenemark_mappe_nordbaltic_unterlagen.docx        # Abschrift der Mappe Dänemark 1984 bis 1986 (Lohnzettel, Besatzungslisten, Gewerkschaftsschreiben)
├── 15_widerspruchsbegruendung_anrechnung_2026-07-09.docx # Widerspruchsbegründung an die DRV Nord (Endprodukt)
├── 16_whatsapp_tochter_daenemark_ordner.txt             # Chat mit der Tochter zu dänischen Lohnzetteln und Geldsorgen
├── 17_telefonvermerk_petersen_monatswert.docx             # Telefonvermerk zum maschinellen Rechenlauf und zur Kontenklärung
├── eml/
│   ├── 01_drv_nord_anrechnung_grundlagen.eml            # DRV Nord: Freibetrag, Gesamtbrutto und einbezogene Renten
│   ├── 02_arbeitgeber_entgelt_klarstellung.eml          # Arbeitgeber: laufendes Entgelt gegen Einmalzahlungen
│   ├── 03_jessen_intern_anrechnung_nachgerechnet.eml    # Interner Rechenweg, warum 458.44 EUR nicht haltbar ist
│   └── 04_atp_hilleroed_zwischenbescheid.eml            # ATP Hillerød: erfasste Beitragszeiten und Archivrecherche
├── README.md                                            # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                           # Konsolidierte Lesefassung der Akte
└── rubric.yaml                                           # Prüfkriterien für die Bearbeitung
```

## Aktenstücke

| Datei | Inhalt |
| --- | --- |
| `02_drv_bescheid_witwenrente.docx` | Bewilligungsbescheid mit Rentenbeginn, Zahlbetrag und Berechnung |
| `03_einkommen_und_betriebsrente.docx` | Vermerk zu Lohn, Betriebsrente, privater Sofortrente, Pauschalnetto |
| `04a_hansekrankenkasse_kvdr_mitteilung_2026-06-25.docx` | Krankenkassenmitteilung zu Beiträgen und Nachweisen |
| `04b_telefonnotiz_personalabteilung_2026-06-27.docx` | Telefonnotiz zu Steuermerkmalen und Einmalzahlungen |
| `05_widerspruch_entwurf.docx` | Widerspruch gegen Einkommensanrechnung und Kontenlücken |
| `06_berechnungsmatrix_witwenrente.csv` | Monatswerte, Freibetrag, Anrechnungsbetrag, Zahlbetrag |
| `07_daenemark_kontenklaerung.docx` | Auslandszeiten, Nachweise und Auskunftsersuchen |
| `08a_arbeitgeberbescheinigung_entgelt_2026.docx` | Arbeitgeberbescheinigung mit Monatswerten und Einmalzahlungen |
| `08b_lohnabrechnung_juni_2026.docx` | Eigenständige Lohnabrechnung mit Abzügen und Nettoauszahlung |
| `09_email_betriebsrente_nachfrage.eml` | Nachfrage zur Zusatzversorgung und zum Zahlbeginn |
| `10_kontoauszug_und_fragenliste.txt` | Kontoauszugsausschnitt und Mandantenfragen |
| `11_hzvk_betriebsrentenmitteilung.docx` | Betriebsrentenmitteilung der Zusatzversorgungskasse |
| `12_hl_leben_leistungsmitteilung.docx` | Leistungsmitteilung des privaten Versicherers |
| `14_daenemark_mappe_nordbaltic_unterlagen.docx` | Abschrift der Dänemark-Mappe des Verstorbenen mit Lohnzetteln und Gewerkschaftsschreiben |
| `13_witwenrente_anrechnung_berechnung.csv` | Datenkern: Anrechnung und Zahlbetrag je Monat |
| `15_widerspruchsbegruendung_anrechnung_2026-07-09.docx` | Widerspruchsbegründung an die DRV Nord |
| `16_whatsapp_tochter_daenemark_ordner.txt` | Chat mit der Tochter zu den dänischen Lohnzetteln |
| `eml/01_drv_nord_anrechnung_grundlagen.eml` | Grundlagen der Anrechnung laut DRV Nord |
| `eml/02_arbeitgeber_entgelt_klarstellung.eml` | Laufendes Entgelt gegen Einmalzahlungen |
| `eml/03_jessen_intern_anrechnung_nachgerechnet.eml` | Interne Nachrechnung des Anrechnungsbetrags |
| `17_telefonvermerk_petersen_monatswert.docx` | Telefonvermerk zum Rechenlauf der Anrechnung und zum Stand der Kontenklärung |
| `eml/04_atp_hilleroed_zwischenbescheid.eml` | Zwischenbescheid der ATP Hillerød zu den dänischen Beitragszeiten |

## Bearbeitungsziel

Die Akte soll eine Rentenberatung dazu zwingen, den Zahlbetrag nicht nur überschlägig zu kommentieren, sondern die Berechnung Monat für Monat nachzuvollziehen. Zu prüfen sind Sterbevierteljahr, große Witwenrente, pauschale Nettoermittlung, Betriebsrentenabgrenzung, Krankenversicherung der Rentner und die Frage, ob dänische Seefahrtszeiten rentenerhöhend nachzufordern sind.

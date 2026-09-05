# Rentenrecht: Riester-Zulagenrückforderung in Augsburg

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-riester-zulagenrueckforderung-augsburg_gesamt.pdf`](gesamt-pdf/rentenrecht-riester-zulagenrueckforderung-augsburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-riester-zulagenrueckforderung-augsburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-riester-zulagenrueckforderung-augsburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-riester-zulagenrueckforderung-augsburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-riester-zulagenrueckforderung-augsburg-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Nadja Erhart, 42, Altenpflegerin in Augsburg, erhält von der Zentralen Zulagenstelle eine Rückforderung mehrerer Riester-Zulagen. Der Anbieter meldete für 2023 und 2024 zu niedrige Eigenbeiträge; zugleich wurden Kinderzulagen für die 2011 und 2016 geborenen Kinder falsch verteilt, weil der geschiedene Vater für ein Jahr die Kindergeldberechtigung wechselte. Die Mandantin hat Dauerzulagenantrag, Anbieterpost, Gehaltsnachweise und Familienkassenbescheide, aber keine saubere Jahresberechnung.

Der Datenauswertungs-Kern liegt in der Mindesteigenbeitrags-Berechnungstabelle (`12_riester_mindesteigenbeitrag_berechnung.csv`) und dem zugehörigen Berechnungsvermerk. Aus Vorjahreseinkommen (rentenversicherungspflichtiges Entgelt statt Steuerbrutto), vier Prozent, Höchstbetrag, Zulagenanspruch und den tatsächlich geleisteten Eigenbeiträgen lässt sich der Mindesteigenbeitrag und die korrekte Rückforderung exakt nachrechnen. Die Diskrepanz zwischen dem von der ZfA angesetzten Mindesteigenbeitrag und den tatsächlichen Zahlungen (die den Mindesteigenbeitrag in beiden Jahren übersteigen) trägt den Einspruch. Neu als Beteiligte hinzugekommen sind die Rentenberaterin Bettina Kolbe (Beratungsstelle) und der Kindsvater Tobias Gantner; reale Träger sind die Zentrale Zulagenstelle für Altersvermögen und die Familienkasse Bayern Süd.

## Aktenstruktur

```
rentenrecht-riester-zulagenrueckforderung-augsburg/
├── 01_erstgespraech_riester.docx                        # Beratungsziel, Familiensituation, Vertrag, Fragen der Mandantin
├── 02_zfa_rueckforderung.docx                           # Festsetzungsbescheid der ZfA mit Rückforderung und Rechtsbehelfsbelehrung
├── 03a_jahreskontoauszug_riester_2023.docx              # Eigenständiger Jahreskontoauszug 2023
├── 03b_jahreskontoauszug_riester_2024.docx              # Eigenständiger Jahreskontoauszug 2024
├── 03d_kanzleivermerk_anbieterauskunft_2024.docx        # Getrennter Belegvermerk zur Anbieterkommunikation
├── 04_familienkasse_kindergeld.docx                     # Vermerk zum Kindergeldwechsel und zur Zuordnung der Kinder
├── 05_einspruch_entwurf.docx                            # Ausformulierter Einspruch mit Aussetzungsantrag und Anlagen
├── 06_riester_jahresmatrix.csv                          # Jahre, Vorjahreseinkommen, Sollbeitrag, Zulagen, Streitpunkte
├── 07_anbieterhaftung_beratungsvermerk.docx             # Zweiter Beratungsstrang: Ersatzanspruch gegen den Anbieter
├── 08a_anbieterbescheinigung_beitragsjahre_2022_2025.docx # Anbieterbescheinigung nach Beitragsjahren
├── 08b_vertragskonto_buchungsauszug_2024_2026.docx      # Gesonderter Buchungs- und Serviceauszug
├── 09_email_zfa_nachweisfrist.eml                       # Nachweisanforderung der ZfA mit Frist zum 10.08.2026
├── 10_telefonnotiz_arbeitgeber_entgelt.txt              # Telefonnotiz zur Differenz Steuerbrutto / SV-Brutto
├── 11_familienkasse_aenderungsbescheid.docx             # Änderungsbescheid der Familienkasse vom 12.09.2024
├── 12_riester_mindesteigenbeitrag_berechnung.csv        # Datenkern: Vorjahresentgelt, vier Prozent, Zulage, Mindesteigenbeitrag, Rückforderung
├── 14_nachweisschreiben_zfa_2026-07-06.docx             # Nachweisschreiben an die ZfA mit Neuberechnung und AdV-Antrag (Endprodukt)
├── 15_whatsapp_kindergeld_tobias.txt                    # Chat Mandantin/Kindsvater zum Kindergeld Jonas 2024
├── 16_entgeltuebersicht_steuer_sv_2022_2025.csv         # Gegenüberstellung Steuerbrutto und SV-Entgelt 2022 bis 2025
├── eml/
│   ├── 01_suedleben_beitragsauskunft.eml                # Anbieter: unverbindliche Empfehlung Sonderzahlung 300 EUR
│   ├── 2024-12-19_suedleben_an_erhart_sonderzahlung.eml # Originalnachricht zur empfohlenen Sonderzahlung
│   ├── 02_familienkasse_kindergeld_jonas.eml            # Familienkasse Bayern Süd: Kindergeldmonate Jonas 2024, erster Anspruchszeitraum
│   ├── 03_beratungsstelle_strategie_mindesteigenbeitrag.eml # Rentenberaterin: Neuberechnung gegen die ZfA-Zahlen
│   └── 04_zfa_eingangsbestaetigung_nachweise.eml        # ZfA: Eingangsbestätigung, Datenabgleich, AdV offen
├── README.md                                            # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                           # Konsolidierte Lesefassung der Akte
└── rubric.yaml                                           # Prüfkriterien für die Bearbeitung
```

## Aktenstücke

| Datei | Inhalt |
| --- | --- |
| `01_erstgespraech_riester.docx` | Beratungsziel, Fristen, Familiensituation |
| `02_zfa_rueckforderung.docx` | Rückforderungsbescheid mit Jahresbeträgen |
| `03a_jahreskontoauszug_riester_2023.docx` | Eigenständiger Jahreskontoauszug mit Beiträgen und Zulagen 2023 |
| `03b_jahreskontoauszug_riester_2024.docx` | Eigenständiger Jahreskontoauszug mit Sonderzahlung und Zulagen 2024 |
| `03d_kanzleivermerk_anbieterauskunft_2024.docx` | Quellen-, Daten- und Nachforderungsvermerk |
| `04_familienkasse_kindergeld.docx` | Kindergeldwechsel und Zuordnung der Kinder |
| `05_einspruch_entwurf.docx` | Begründeter Rechtsbehelf mit Nachweisen |
| `06_riester_jahresmatrix.csv` | Jahre, Einkommen, Sollbeitrag, Zulage, Differenz |
| `07_anbieterhaftung_beratungsvermerk.docx` | Anbieterhinweis, Schadenlinie und Nachforderung |
| `08a_anbieterbescheinigung_beitragsjahre_2022_2025.docx` | Anbieterbescheinigung zu den vier Beitragsjahren |
| `08b_vertragskonto_buchungsauszug_2024_2026.docx` | Eigenständiger Vertragskontoauszug mit Rückforderungsbuchungen |
| `09_email_zfa_nachweisfrist.eml` | Fristsetzung der Zulagenstelle mit konkreten Nachweiswünschen |
| `10_telefonnotiz_arbeitgeber_entgelt.txt` | Telefonnotiz zum rentenversicherungspflichtigen Vorjahreseinkommen |
| `11_familienkasse_aenderungsbescheid.docx` | Änderungsbescheid zur Kindergeldfestsetzung für Jonas |
| `12_riester_mindesteigenbeitrag_berechnung.csv` | Datenkern: Mindesteigenbeitrag je Jahr und korrekte Rückforderung |
| `14_nachweisschreiben_zfa_2026-07-06.docx` | Nachweisschreiben an die ZfA mit Neuberechnung und AdV-Antrag |
| `15_whatsapp_kindergeld_tobias.txt` | Chat mit dem Kindsvater zur Kindergeldweiterleitung 2024 |
| `eml/01_suedleben_beitragsauskunft.eml` | Anbieterempfehlung Sonderzahlung 300 EUR |
| `eml/2024-12-19_suedleben_an_erhart_sonderzahlung.eml` | Vollständige Originalnachricht mit Reichweite und Einschränkungen |
| `eml/02_familienkasse_kindergeld_jonas.eml` | Kindergeldmonate Jonas 2024 und erster Anspruchszeitraum |
| `eml/03_beratungsstelle_strategie_mindesteigenbeitrag.eml` | Neuberechnung der Rentenberaterin gegen die ZfA-Zahlen |
| `eml/04_zfa_eingangsbestaetigung_nachweise.eml` | Eingangsbestätigung der ZfA mit Bearbeitungsstand, Rückfragen und offenem AdV-Antrag |
| `16_entgeltuebersicht_steuer_sv_2022_2025.csv` | Gegenüberstellung Steuerbrutto und rentenversicherungspflichtiges Entgelt 2022 bis 2025 |

## Bearbeitungsziel

Die Akte soll eine Beratung zur Riester-Förderung erzwingen: Mindesteigenbeitrag, Grundzulage, Kinderzulage, Zulagenberechtigung, Anbieterfehler, Bescheidfrist und Nachzahlungsmöglichkeit müssen auseinandergehalten werden. Die Unterlagen sind bewusst nicht vorsortiert nach Ergebnis, sondern nach ihrem realistischen Eingang in einer Beratungsstelle.

# Erbrechtsakte Vertragserbe gegen lebzeitige Schenkungen (LG und OLG Oldenburg)

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg_gesamt.pdf`](gesamt-pdf/erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zu einem Berufungsverfahren vor dem OLG Oldenburg (8 U 63/26) nach teilweise stattgebendem Urteil des LG Oldenburg (5 O 458/25). Der Sohn ist vertragsmäßig eingesetzter Schlusserbe aus einem Erbvertrag von 2008 mit nie ausgeübtem Rücktrittsvorbehalt. Der Erblasser übertrug der Tochter lebzeitig die Hofstelle in Wardenburg (gegen Wohnungsrecht und Pflegeversprechen), schenkte ihr ein Baugrundstück und überwies ihr in zwölf Tranchen 152.000 EUR. Die Beklagte stützt ihre Berufung darauf, dass schon der Rücktrittsvorbehalt die geschützte Erberwartung entfallen lasse, und bestreitet hilfsweise den Umfang der Zuwendungen; der Kläger verfolgt mit der Anschlussberufung die Hofstelle weiter. Während des Berufungsverfahrens veröffentlicht der BGH die Entscheidungsgründe IV ZR 256/25 zu genau dieser Vorbehaltsfrage; der Senat weist darauf hin und setzt eine Stellungnahmefrist. Die Akte ist für `fachanwalt-erbrecht` gedacht.

Datenauswertungs-Kern: Die Kontoauswertung (zwölf Buchungen, Summe 152.000 EUR) ist mit dem Hilfsvorbringen der Gegenseite (nur 95.000 EUR unentgeltlich; 35.000 EUR Darlehen; 22.000 EUR Anlassgeschenke) abzugleichen; die Pflegedienst-Rechnungen und der Chatverlauf liefern das Tatsachenmaterial zur tatsächlichen Durchführung der Pflegeabrede, das Kurzgutachten die Wertrelation der Hofstelle.

## Aktenstruktur

```
erbrecht-vertragserbe-schenkungen-erbvertrag-oldenburg/
├── 02_erbvertrag_2008.docx                          # Vollständiger Erbvertrag mit Schlusserbeneinsetzung und Rücktrittsvorbehalt
├── 03_uebergabevertrag_hofstelle_2021.docx          # Vollständiger Übergabevertrag mit Wohnungsrecht und Pflegeverpflichtung
├── 04_schenkungsvertrag_baugrundstueck_2022.docx    # Vollständige Schenkungsurkunde über den Bauplatz Hundsmühlen
├── 05_lg_oldenburg_urteil_2026-03-12.docx           # Urteil LG Oldenburg 5 O 458/25, teilweise stattgebend
├── 06_berufungsbegruendung_beklagte_2026-05-18.docx # Berufungsangriffe: Rücktrittsvorbehalt, Eigeninteresse, Höhe
├── 07_geldzuwendungen_konto_2020_2023.csv           # Datenkern: zwölf Überweisungen mit Verwendungszwecken und Belegen
├── 08_pflegedienst_rechnungen_2022_2024.csv         # Rechnungen Pflegedienst Huntetal, Zahlung vom Konto des Erblassers
├── 09_kurzgutachten_hofstelle_2021.docx             # Verkehrswert der Hofstelle zum Stichtag 03.05.2021
├── 10_olg_hinweisverfuegung_2026-07-16.docx         # Hinweis des Senats auf BGH IV ZR 256/25, Frist und Termin
├── 11_telefonvermerk_pflegedienst_huntetal_2026-07-24.docx # Telefonat mit der Pflegedienstleitung zu Beginn, Umfang und Dokumentation der Versorgung
├── eml/
│   ├── 01_newsletter_bgh_vertragserbe_2026-07-08.eml   # Newsletter zu den Entscheidungsgründen IV ZR 256/25
│   ├── 02_mandant_weiterleitung_frage_2026-07-10.eml   # Mandant fragt nach Bedeutung für die Berufung
│   ├── 03_gegenanwaeltin_stellungnahme_2026-07-17.eml  # Gegenseite zu Hilfsvorbringen und Einigungsgespräch
│   ├── 04_mandant_zu_einigungsvorschlag_2026-07-23.eml # Mandant zu Gesprächsangebot, Darlehensbehauptung und Zeugin Lammers
│   └── chat_geschwister_2021.txt                       # Messenger-Export der Geschwister 2021 und 2022
├── README.md                                        # Kurzbild, Struktur und Bearbeitungsziel
├── gesamt-pdf/                                      # Konsolidierte Lesefassung der Akte
└── rubric.yaml                                      # Prüfkriterien für die Bearbeitung
```

## Bearbeitungsziel

Zu fertigen sind die Stellungnahme auf die Hinweisverfügung vom 16.07.2026 (Frist 14.08.2026), die Berufungserwiderung und die ergänzende Begründung der Anschlussberufung wegen der Hofstelle; Termin zur mündlichen Verhandlung ist der 29.09.2026. Die rechtliche Bewertung bleibt offen; die Unterlagen liefern Urkunden, Prozessgeschichte, Zahlenwerk und die neue BGH-Linie als Prüfstoff.

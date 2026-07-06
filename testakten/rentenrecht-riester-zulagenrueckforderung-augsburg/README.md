# Rentenrecht: Riester-Zulagenrückforderung in Augsburg


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 53 KB) | PDF | [`gesamt-pdf/rentenrecht-riester-zulagenrueckforderung-augsburg_gesamt.pdf`](gesamt-pdf/rentenrecht-riester-zulagenrueckforderung-augsburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-riester-zulagenrueckforderung-augsburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-riester-zulagenrueckforderung-augsburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-riester-zulagenrueckforderung-augsburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-riester-zulagenrueckforderung-augsburg-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

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
├── 03_eigenbeitraege_und_zulagen.docx                   # Jahreskontoauszüge des Anbieters und E-Mail zur Sonderzahlung
├── 04_familienkasse_kindergeld.docx                     # Vermerk zum Kindergeldwechsel und zur Zuordnung der Kinder
├── 05_einspruch_entwurf.docx                            # Ausformulierter Einspruch mit Aussetzungsantrag und Anlagen
├── 06_riester_jahresmatrix.csv                          # Jahre, Vorjahreseinkommen, Sollbeitrag, Zulagen, Streitpunkte
├── 07_anbieterhaftung_beratungsvermerk.docx             # Zweiter Beratungsstrang: Ersatzanspruch gegen den Anbieter
├── 08_anbieter_jahresbescheinigung_und_kontoauszug.docx # Zulagenkonto, Buchungen und interne Servicevermerke
├── 09_email_zfa_nachweisfrist.eml                       # Nachweisanforderung der ZfA mit Frist zum 10.08.2026
├── 10_telefonnotiz_arbeitgeber_entgelt.txt              # Telefonnotiz zur Differenz Steuerbrutto / SV-Brutto
├── 11_familienkasse_aenderungsbescheid.docx             # Änderungsbescheid der Familienkasse vom 12.09.2024
├── 12_riester_mindesteigenbeitrag_berechnung.csv        # Datenkern: Vorjahresentgelt, vier Prozent, Zulage, Mindesteigenbeitrag, Rückforderung
├── 13_berechnungsvermerk_mindesteigenbeitrag_2026-07-03.docx # Interner Vermerk, rechnet Mindesteigenbeitrag und Rückforderung nach
├── 14_nachweisschreiben_zfa_2026-07-06.docx             # Nachweisschreiben an die ZfA mit Neuberechnung und AdV-Antrag (Endprodukt)
├── 15_whatsapp_kindergeld_tobias.txt                    # Chat Mandantin/Kindsvater zum Kindergeld Jonas 2024
├── eml/
│   ├── 01_suedleben_beitragsauskunft.eml                # Anbieter: unverbindliche Empfehlung Sonderzahlung 300 EUR
│   ├── 02_familienkasse_kindergeld_jonas.eml            # Familienkasse Bayern Süd: Kindergeldmonate Jonas 2024, erster Anspruchszeitraum
│   └── 03_beratungsstelle_strategie_mindesteigenbeitrag.eml # Rentenberaterin: Neuberechnung gegen die ZfA-Zahlen
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
| `01_erstgespraech_riester.docx` | Beratungsziel, Fristen, Familiensituation |
| `02_zfa_rueckforderung.docx` | Rückforderungsbescheid mit Jahresbeträgen |
| `03_eigenbeitraege_und_zulagen.docx` | Vertragsdaten, Einzahlungen, Kinderzulage |
| `04_familienkasse_kindergeld.docx` | Kindergeldwechsel und Zuordnung der Kinder |
| `05_einspruch_entwurf.docx` | Begründeter Rechtsbehelf mit Nachweisen |
| `06_riester_jahresmatrix.csv` | Jahre, Einkommen, Sollbeitrag, Zulage, Differenz |
| `07_anbieterhaftung_beratungsvermerk.docx` | Anbieterhinweis, Schadenlinie und Nachforderung |
| `08_anbieter_jahresbescheinigung_und_kontoauszug.docx` | Anbieterbescheinigung, Zulagenkonto und Vertragsbuchungen |
| `09_email_zfa_nachweisfrist.eml` | Fristsetzung der Zulagenstelle mit konkreten Nachweiswünschen |
| `10_telefonnotiz_arbeitgeber_entgelt.txt` | Telefonnotiz zum rentenversicherungspflichtigen Vorjahreseinkommen |
| `11_familienkasse_aenderungsbescheid.docx` | Änderungsbescheid zur Kindergeldfestsetzung für Jonas |
| `12_riester_mindesteigenbeitrag_berechnung.csv` | Datenkern: Mindesteigenbeitrag je Jahr und korrekte Rückforderung |
| `13_berechnungsvermerk_mindesteigenbeitrag_2026-07-03.docx` | Interner Berechnungsvermerk zum Mindesteigenbeitrag |
| `14_nachweisschreiben_zfa_2026-07-06.docx` | Nachweisschreiben an die ZfA mit Neuberechnung und AdV-Antrag |
| `15_whatsapp_kindergeld_tobias.txt` | Chat mit dem Kindsvater zur Kindergeldweiterleitung 2024 |
| `eml/01_suedleben_beitragsauskunft.eml` | Anbieterempfehlung Sonderzahlung 300 EUR |
| `eml/02_familienkasse_kindergeld_jonas.eml` | Kindergeldmonate Jonas 2024 und erster Anspruchszeitraum |
| `eml/03_beratungsstelle_strategie_mindesteigenbeitrag.eml` | Neuberechnung der Rentenberaterin gegen die ZfA-Zahlen |

## Bearbeitungsziel

Die Akte soll eine Beratung zur Riester-Förderung erzwingen: Mindesteigenbeitrag, Grundzulage, Kinderzulage, Zulagenberechtigung, Anbieterfehler, Bescheidfrist und Nachzahlungsmöglichkeit müssen auseinandergehalten werden. Die Unterlagen sind bewusst nicht vorsortiert nach Ergebnis, sondern nach ihrem realistischen Eingang in einer Beratungsstelle.

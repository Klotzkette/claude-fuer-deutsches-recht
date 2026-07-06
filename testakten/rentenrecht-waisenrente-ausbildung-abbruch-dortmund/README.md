# Rentenrecht: Waisenrente, Ausbildung und Studienabbruch in Dortmund


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 54 KB) | PDF | [`gesamt-pdf/rentenrecht-waisenrente-ausbildung-abbruch-dortmund_gesamt.pdf`](gesamt-pdf/rentenrecht-waisenrente-ausbildung-abbruch-dortmund_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-waisenrente-ausbildung-abbruch-dortmund.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-waisenrente-ausbildung-abbruch-dortmund.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-waisenrente-ausbildung-abbruch-dortmund-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-waisenrente-ausbildung-abbruch-dortmund-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Elif Korkmaz, 21, erhält Halbwaisenrente nach dem Tod ihres Vaters. Nach Abitur, Bundesfreiwilligendienst, abgebrochener Ausbildung zur Physiotherapeutin und geplanter Aufnahme eines dualen Studiums stellt die DRV die Waisenrente ein. Die Mandantin hat Lücken zwischen Ausbildungsabschnitten, gesundheitliche Gründe für den Abbruch und eine Zusage für ein duales Studium, aber der Bescheid würdigt nur den aktuellen Status "nicht in Ausbildung".

Der Datenauswertungs-Kern liegt im Monatsraster (`12_waisenrente_monatsraster_berechnung.csv`) und dem zugehörigen Berechnungsvermerk. Aus Status, Ausbildungstatbestand, Übergangszeit und gezahlter Rente je Monat lässt sich die Erstattungsforderung nachrechnen (sechs Monate Januar bis Juni 2026 zu je 307.10 EUR gleich 1842.60 EUR) und zeigen, dass das Übergangszeit-Argument nur den Juni 2026 rettet, während Januar bis Mai 2026 die krankheitsbedingte Unterbrechung tragen muss. Zugleich trägt das Raster die Diskrepanz zwischen gemeldetem und tatsächlichem Ausbildungsstatus (formale Einbindung bis 30.11.2025, tatsächliche Teilnahme nur bis 14.10.2025) und die Diskrepanz zwischen Mandantinnenangabe (Rente bis Mai) und der tatsächlichen Junizahlung. Neu als Beteiligte hinzugekommen sind die Rentenberaterin Marika Thiele (Bevollmächtigte), die Mutter Selma Korkmaz, die Schulleitung Dr. Freihof und die Klassenleiterin Frau Bendorf; reale Träger sind die Deutsche Rentenversicherung Westfalen und das Sozialgericht Dortmund.

## Aktenstruktur

```
rentenrecht-waisenrente-ausbildung-abbruch-dortmund/
├── 01_mandatsnotiz_waisenrente.docx                     # Lebenslauf, Frist, Bescheidlage, Beratungsziel
├── 02_drv_einstellungsbescheid.docx                     # Einstellungs- und Erstattungsbescheid mit Rechtsbehelfsbelehrung
├── 03_ausbildungsnachweise.docx                         # Abitur, Bundesfreiwilligendienst, Ausbildung, Studienzusage
├── 04_gesundheit_und_abbruch.docx                       # Hausärztliche und psychotherapeutische Unterlagen zum Abbruch
├── 05_widerspruch_waisenrente.docx                      # Ausformulierter Widerspruch mit Aussetzungs- und Ratenantrag
├── 06_zeitstrahl_ausbildung.csv                         # Monatsraster mit Status, Nachweisen und Risikoeinschätzung
├── 07_klageentwurf_sozialgericht.docx                   # Klageanträge, Begründungskern und Vergleichsidee
├── 08_bildungstraeger_bescheinigung_und_fehlzeiten.docx # Berufskolleg-Bescheinigung mit Fehlzeiten und Leistungsstand
├── 09_email_drv_nachforderung.eml                       # Nachweisanforderung der DRV mit Frist zum 31.07.2026
├── 10_jobcenter_uebergang_und_konto.txt                 # Jobcenter-Gesprächsnotiz und Kontoauszug
├── 11_studienzusage_und_praxisvertrag.docx              # FH-Zulassung und Praxisvertrag mit Einarbeitungsmonat
├── 12_waisenrente_monatsraster_berechnung.csv           # Datenkern: Status, Tatbestand, Übergangszeit, Rente und Überzahlung je Monat
├── 13_berechnungsvermerk_monatsraster_2026-07-05.docx   # Interner Vermerk, rechnet Erstattung und Übergangszeit-Wirkung nach
├── 14_nachweisschreiben_drv_2026-07-06.docx             # Nachweisschreiben an die DRV mit Begründung und AdV-Antrag (Endprodukt)
├── 15_whatsapp_klassenleitung_abbruch.txt               # Chat mit der Klassenleitung zu Krankheit, Beurlaubung und Kündigung
├── eml/
│   ├── 01_berufskolleg_teilnahmestatus.eml              # Berufskolleg: formaler Status bis 30.11.2025 gegen Teilnahme bis 14.10.2025
│   ├── 02_mutter_anhoerung_und_junizahlung.eml          # Mutter: nicht zugegangene Anhörung und bestätigte Junizahlung
│   └── 03_thiele_intern_monatsraster.eml                # Interner Rechenweg zur Erstattung und zum Übergangszeit-Argument
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
| `01_mandatsnotiz_waisenrente.docx` | Lebenslauf, Frist, Beratungsziel |
| `02_drv_einstellungsbescheid.docx` | Einstellung der Halbwaisenrente und Erstattungsforderung |
| `03_ausbildungsnachweise.docx` | Schule, Bundesfreiwilligendienst, Ausbildung, Studienzusage |
| `04_gesundheit_und_abbruch.docx` | Ärztliche Unterlagen zum Ausbildungsabbruch |
| `05_widerspruch_waisenrente.docx` | Widerspruch und Nachweisanforderungen |
| `06_zeitstrahl_ausbildung.csv` | Monatsraster für Waisenrentenprüfung |
| `07_klageentwurf_sozialgericht.docx` | Klageanträge, Begründung und Vergleichsidee |
| `08_bildungstraeger_bescheinigung_und_fehlzeiten.docx` | Bescheinigung des Berufskollegs mit Fehlzeiten und Leistungsstand |
| `09_email_drv_nachforderung.eml` | Nachweisanforderung der Rentenversicherung zur Ausbildungslücke |
| `10_jobcenter_uebergang_und_konto.txt` | Jobcenter-Notiz, Kontoauszug und finanzielle Lage |
| `11_studienzusage_und_praxisvertrag.docx` | Zulassungsschreiben der FH und Praxisvertrag |
| `12_waisenrente_monatsraster_berechnung.csv` | Datenkern: Anspruch und Überzahlung je Monat |
| `13_berechnungsvermerk_monatsraster_2026-07-05.docx` | Interner Berechnungsvermerk zur Erstattung |
| `14_nachweisschreiben_drv_2026-07-06.docx` | Nachweisschreiben an die DRV mit Begründung und AdV-Antrag |
| `15_whatsapp_klassenleitung_abbruch.txt` | Chat mit der Klassenleitung zum krankheitsbedingten Abbruch |
| `eml/01_berufskolleg_teilnahmestatus.eml` | Formaler Status gegen tatsächliche Teilnahme |
| `eml/02_mutter_anhoerung_und_junizahlung.eml` | Nicht zugegangene Anhörung und Junizahlung |
| `eml/03_thiele_intern_monatsraster.eml` | Interner Rechenweg zur Erstattung |

## Bearbeitungsziel

Die Akte trainiert die Prüfung, ob eine Waisenrente trotz Unterbrechungen weiterzuzahlen ist. Entscheidend sind Altersgrenze, Ausbildungstatbestand, Übergangszeiten, gesundheitlich erklärter Abbruch, Nachweise und der richtige Antrag auf Weiterzahlung oder rückwirkende Korrektur.

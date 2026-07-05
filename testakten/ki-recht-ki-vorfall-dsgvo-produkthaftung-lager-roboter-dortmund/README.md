# Testakte: KI-Recht — KI-Vorfall mit Doppel- und Dreifachrelevanz (autonomer Lagerroboter, Dortmund)


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 37 KB) | PDF | [`gesamt-pdf/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund_gesamt.pdf`](gesamt-pdf/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Im Logistikzentrum der NordLog Distribution GmbH in Dortmund verletzt am 24.06.2026 der autonome, KI-gesteuerte Transportroboter AutoMove T7 (Kennung RB-07) einen über die FlexPerson Zeitarbeit GmbH überlassenen Leiharbeitnehmer schwer. Bei der Aufklärung stellt sich heraus, dass der ursächliche Personenerkennungssensor S3 seit dem Firmware-Update 4.2 einen bekannten, dokumentierten Fehler aufweist (Fehlercode E-SNS-311) und dass zugleich das Objekterkennungsmodell dieser Firmware mit unrechtmäßig erhobenen Beschäftigten-Bewegungsdaten trainiert wurde. Die Akte bildet drei Ebenen ab: die KI-Vorfallsmeldung an die Marktüberwachungsbehörde, die datenschutzrechtliche Meldung wegen der unrechtmäßigen Trainingsdaten sowie die Produkt- und Betreiberhaftung.

Datenauswertungs-Kern: Aus dem Roboter-Ereignislog (Aktenstück 02) und der Wartungs- und Update-Historie (Aktenstück 03) muss die Bearbeitung selbst die Kausalkette rekonstruieren, nämlich dass der Fehlercode E-SNS-311 erstmals am 09.12.2025 nach Installation der Firmware 4.2 (18.11.2025) auftrat, vor dem Update 4.1 gar nicht vorkam, in drei Beinahe-Vorfällen (09.12.2025, 15.01.2026, 27.02.2026) nur einen verspäteten Not-Halt auslöste, dass der Hersteller am 08.04.2026 mit Sicherheitshinweis SB-2026-03 die Firmware 4.3 zur Behebung bereitstellte und dass dieses Update am Unfalltag nicht installiert war. Gewollte Diskrepanz: Der interne Vorfallsbericht des Betreibers (Aktenstück 01) behauptet ein „unvorhersehbares Einzelereignis", während Logs, Wartungshistorie, die interne Korrespondenz und der Teamchat drei frühere Beinahe-Vorfälle und den ignorierten Sicherheitshinweis belegen. Ein Normstand-Vermerk regelt den Umgang mit dem beweglichen Rechtsstand; alle Artikel- und Fristangaben sind vor Verwendung amtlich zu verifizieren.

## Beteiligte

| Rolle | Person / Stelle |
| --- | --- |
| Betreiberin | NordLog Distribution GmbH, Ellinghausener Straße 90, 44359 Dortmund (HRB 28911, AG Dortmund) |
| Geschäftsführung Betreiberin | Dr. Marius Tenbrock |
| Leiter Technik und Instandhaltung | Kai Rüggeberg |
| Fachkraft für Arbeitssicherheit | Petra Wollenweber |
| Schichtführung | Marek Sobczak |
| Herstellerin | AutoMove Robotics GmbH, Jülicher Straße 210, 52070 Aachen (HRB 19044, AG Aachen), GF Dr. Ing. Sabine Kortmann |
| Field Service Herstellerin | Lennart Brinkschulte |
| Verletzter (Leiharbeitnehmer) | Tomasz Wójcik, überlassen durch FlexPerson Zeitarbeit GmbH |
| Rechtsvertretung des Verletzten | RA Dr. Ferdinand Aschenbroich, Kanzlei Aschenbroich und Partner, Dortmund |
| Marktüberwachungsbehörde KI | Bundesnetzagentur, Referat Marktüberwachung KI-Systeme, Bonn |
| Datenschutzaufsicht | Landesbeauftragte für Datenschutz und Informationsfreiheit NRW (LDI NRW), Düsseldorf |
| Unfallversicherungsträger | Berufsgenossenschaft Handel und Warenlogistik (BGHW), Bezirksverwaltung Dortmund |

## Aktenstruktur

```
ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund/
├── 01_vorfallsbericht_betreiber_2026-06-25.docx                     — Betreiber behauptet unvorhersehbares Einzelereignis (Diskrepanz-Quelle)
├── 02_roboter_ereignislog_2025-09_bis_2026-06.csv                   — Ereignislog mit Sensorwerten, Not-Halt, Fehlercode, Firmware (Rohdaten Kausalkette)
├── 03_wartungs_und_update_historie.csv                              — Firmware-Stände, Störtickets, Sicherheitshinweis, Update-Status (Rohdaten Kausalkette)
├── 04_herstellerdoku_auszug_automove_t7_2025.docx                   — Sensor S3, Not-Halt, Rückfallerkennung, Sicherheitshinweis SB-2026-03
├── 05_trainingsdaten_herkunftsvermerk_2026-06.docx                  — Unrechtmäßig erhobene Beschäftigten-Bewegungsdaten im Training
├── 06_ki_vorfallsmeldung_bnetza_2026-06-30.docx                    — Meldung des schwerwiegenden Vorfalls an die Marktüberwachungsbehörde
├── 07_dsgvo_meldung_ldi_nrw_2026-06-30.docx                        — Meldung der unrechtmäßigen Verarbeitung an die Datenschutzaufsicht
├── 08_bg_unfallanzeige_2026-06-26.docx                             — Unfallanzeige an die BGHW; Sicherheitsfachkraft widerspricht der Betriebsleitung
├── 09_haftungskorrespondenz_anwalt_2026-07-02.docx                 — Anwaltliches Aufforderungsschreiben an Betreiberin und Herstellerin
├── 10_herstellerantwort_haftung_automove_2026-07-03.docx           — Herstellerin verweist auf unterlassene Installation der Firmware 4.3
├── 11_normstand_vermerk_2026-07-04.docx                            — Rechtsstand über drei Ebenen, Omnibus-Vorbehalt, Verifikationsanordnung
├── eml/
│   ├── 2026-04-09_brinkschulte_an_rueggeberg_update43.eml          — Hersteller drängt dringend auf Installation der Firmware 4.3
│   ├── 2026-04-11_rueggeberg_intern_update_verschieben.eml         — Betreiber verschiebt Update auf nach dem Peak; SiFa widerspricht
│   └── 2026-06-26_wollenweber_an_leitung_widerspruch.eml           — SiFa widerspricht der Darstellung unvorhersehbar nach dem Unfall
├── chat/
│   └── teams_chat_instandhaltung_rb07_2025-12_bis_2026-06.txt      — Chatverlauf der Instandhaltung mit drei Beinahe-Vorfällen und Update-Verschiebung
├── rubric.yaml                                                     — Sechs Prüfpunkte zur Bewertung einer Bearbeitung
└── README.md                                                      — Diese Übersicht
```

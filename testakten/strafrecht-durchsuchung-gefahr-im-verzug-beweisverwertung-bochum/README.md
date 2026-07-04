# Testakte: Durchsuchung bei „Gefahr im Verzug" und Beweisverwertung — BtM- und Waffenverfahren (Bochum)


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 64 KB) | PDF | [`gesamt-pdf/strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum_gesamt.pdf`](gesamt-pdf/strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Strafsache der Staatsanwaltschaft Bochum (36 Js 1247/26, später LG Bochum, 2 KLs 36 Js 1247/26): Nach einem Anwohnerhinweis observiert die Polizei am 12.05.2026 ein Mehrfamilienhaus in Bochum, beobachtet um 14:20 Uhr eine Drogenübergabe und durchsucht um 17:05 Uhr die Wohnung des Beschuldigten — ohne richterlichen Beschluss, gestützt auf „Gefahr im Verzug" (§ 105 StPO), weil der Bereitschaftsrichter angeblich telefonisch nicht erreichbar war. Gefunden werden über ein Kilogramm Marihuana, Amphetamin, Bargeld und eine schussbereite Pistole. Die Verteidigung erhebt im Zwischenverfahren Verwertungswiderspruch; Staatsanwaltschaft und Kammer positionieren sich, und das Gericht gibt Aufklärungsauflagen auf.

Der Datenauswertungs-Kern ist eine Zeitketten-Rekonstruktion aus drei Tabellen und den Vermerken: Einsatzprotokoll-CSV (Funkzeiten von der Verdachtsgewinnung bis zum Zugriff), Telefonvermerk-Liste der Wache (alle ausgehenden Anrufe des Nachmittags) und Erreichbarkeitsauskunft des Amtsgerichts (Dienstplan, Rufnummern, Verbindungsprotokoll des Diensthandys). Daraus ist zu entwickeln, wie viel Zeit für eine richterliche Entscheidung zur Verfügung stand, ob der behauptete Anrufversuch in den Daten eine Stütze findet und welche Folgen das für Beweisverwertungsverbot, Fernwirkung und den Bestand der Anklage hat. Prüfschwerpunkte daneben: die Abgrenzung von Umgehung und Organisationsversagen, der hypothetisch rechtmäßige Ermittlungsverlauf, die Behandlung unabhängig erlangter Beweismittel (Observation, Käufer, Nachbar) sowie Mengen- und Wirkstoffrechnung nach KCanG und BtMG.

## Beteiligte

| Rolle | Person / Stelle |
| --- | --- |
| Beschuldigter/Angeschuldigter | Dennis Kowalczik, Maltheserstraße 44, Bochum (U-Haft, JVA Bochum) |
| Verteidigerin | Rechtsanwältin Ceyda Aksoy, Bochum |
| Staatsanwaltschaft | StA Bochum, StAin Dr. Hillmann, 36 Js 1247/26 |
| Polizei | PP Bochum, KK 12, KHK Odenwald (Sachbearbeitung), POK Brechler (Einsatzleiter), Tgb.-Nr. KK12-2026-0771 |
| Observationstrupp | KOK Jelinek, PKin Norda („Castor 21/22") |
| Nachbar (Zeuge) | Herbert Sanftleben, Maltheserstraße 44 |
| Bereitschaftsrichter am 12.05.2026 | RiAG Dr. Siebert, AG Bochum |
| Ermittlungsrichter (Beschlagnahme) | AG Bochum, 64 Gs 1822/26; Haftbefehl 64 Gs 1799/26 |
| Erkennendes Gericht | LG Bochum, 2. große Strafkammer, 2 KLs 36 Js 1247/26, VRiLG Dr. Papenbrock |

## Aktenstruktur

```
strafrecht-durchsuchung-gefahr-im-verzug-beweisverwertung-bochum/
├── 01_observationsbericht_kk12_2026-05-12.docx                     — Anlass (Anwohnerhinweis vom 05.05.), Observationsverlauf, Übergabe 14:20 Uhr
├── 02_einsatzprotokoll_funkverkehr_2026-05-12.csv                  — Funkzeiten von 13:40 Uhr bis 19:05 Uhr als maßgebliche Zeitkette
├── 03_durchsuchungsvermerk_gefahr_im_verzug_2026-05-12.docx        — Eilanordnung der StA, behaupteter erfolgloser Anruf beim Richter
├── 04_sicherstellungsprotokoll_2026-05-12.docx                     — Auffindesituation, Widerspruch des Beschuldigten, Asservatenbehandlung
├── 05_asservatenliste_2026-05-13.csv                               — Asservate A01 bis A17 mit Gewichten, Stückzahlen und Fundorten
├── 06_telefonvermerke_wache_kk12_2026-05-12.csv                    — Alle protokollierten Telefonate der Wache zwischen 13:00 und 18:00 Uhr
├── 07_beschuldigtenvernehmung_kowalczik_2026-05-13.docx            — Kurzeinlassung (Eigenkonsum, Fundwaffe), Rüge der beschlusslosen Durchsuchung
├── 08_antrag_sta_nachtraegliche_bestaetigung_2026-05-15.docx       — Beschlagnahmebestätigung und Antrag auf nachträgliche Bestätigung der Durchsuchung
├── 09_zeugenvernehmung_nachbar_sanftleben_2026-05-20.docx          — Unabhängige Wahrnehmungen: Besucherverkehr, Geruch, Pistole auf dem Balkon
├── 10_beschluss_ag_bochum_bestaetigung_2026-05-21.docx             — Bestätigung der Beschlagnahme, Zurückweisung der nachträglichen Durchsuchungsbestätigung
├── 11_bereitschaftsdienstplan_erreichbarkeit_ag_bochum_2026-06-08.docx — Dienstplan KW 20, Rufnummern, Verbindungsprotokoll des Diensthandys
├── 12_zeugenvernehmung_pok_brechler_2026-06-10.docx                — Einsatzleiter zum delegierten, nirgends dokumentierten Anrufversuch
├── 13_anklageschrift_sta_bochum_2026-06-15.docx                    — Anklage zum LG Bochum: KCanG, BtMG, WaffG, Wirkstoffmengen, Einziehung
├── 14_verteidigerschriftsatz_verwertungswiderspruch_2026-06-24.docx — Zeitketten-Argumentation, Verwertungsverbot, Fernwirkung, § 209 StPO
├── 15_stellungnahme_sta_2026-06-30.docx                            — Organisationsversagen statt Umgehung, hypothetisch rechtmäßiger Verlauf, unabhängige Beweise
├── 16_gerichtlicher_hinweis_lg_bochum_2026-07-02.docx              — Vorläufige Kammerbewertung und Aufklärungsauflagen nach § 202 StPO
├── eml/
│   ├── 2026-05-28_aksoy_verteidigungsanzeige_akteneinsicht.eml     — Verteidigungsanzeige mit gezielter Anforderung der Eilanordnungs-Dokumentation
│   ├── 2026-06-05_aksoy_anfrage_ag_bochum_dienstplan.eml           — Anfrage nach § 475 StPO zur Erreichbarkeit des Bereitschaftsrichters
│   └── 2026-06-08_ag_bochum_antwort_dienstplan.eml                 — Antwort der Gerichtsverwaltung mit Kernaussagen zum Verbindungsprotokoll
├── whatsapp/
│   └── chatverlauf.txt                                             — Chatexport vom sichergestellten Handy (Verkaufskommunikation, Folgebeweis-Frage)
├── rubric.yaml                                                     — Sechs Prüfpunkte zur Bewertung einer Bearbeitung
└── README.md                                                       — Diese Übersicht
```

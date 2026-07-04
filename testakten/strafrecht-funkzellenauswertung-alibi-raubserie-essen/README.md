# Testakte: Funkzellenauswertung und Alibi — Raubserie auf Spätverkaufsstellen (Essen)


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 64 KB) | PDF | [`gesamt-pdf/strafrecht-funkzellenauswertung-alibi-raubserie-essen_gesamt.pdf`](gesamt-pdf/strafrecht-funkzellenauswertung-alibi-raubserie-essen_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-strafrecht-funkzellenauswertung-alibi-raubserie-essen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-funkzellenauswertung-alibi-raubserie-essen.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-strafrecht-funkzellenauswertung-alibi-raubserie-essen-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-funkzellenauswertung-alibi-raubserie-essen-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Ermittlungs- und Haftsache der Staatsanwaltschaft Essen (70 Js 883/26): Drei Raubüberfälle auf Spätverkaufsstellen in Essen (17.04., 02.05. und 15.05.2026), stets mit Messer, Kapuze und der wortgleichen Forderung „Kasse auf, zack zack". Der Beschuldigte bestreitet und beruft sich für alle drei Abende auf denselben Alibiort: die Wohnung seiner Schwester in Duisburg-Hochfeld. Die Schwester bestätigt das pauschal für die ganzen Abende. In der Akte liegen der Funkzellen-Beschluss nach § 100g StPO, die Verkehrsdaten-CSV des Mobilfunkanbieters, eine Wahllichtbildvorlage mit dokumentierten Durchführungsmängeln, Haftbefehl, Haftprüfungsantrag und ein Verteidigerschriftsatz, der die Ermittlungsdaten der Staatsanwaltschaft für die Verteidigung nutzbar macht.

Der Datenauswertungs-Kern verlangt den eigenständigen Abgleich dreier Quellen: Verkehrsdaten-CSV (Zellen-IDs mit Standort und Zeitstempel), Taten-Übersichts-CSV (Tatzeiten, Tatorte, Beute) und Fahrzeiten-Vermerk (Pkw gegen ÖPNV). Daraus ist tatgenau zu differenzieren, für welche der drei Taten die Standortdaten be- oder entlasten, was die Bewegungslücken über das Verkehrsmittel aussagen und was die personenungebundene Natur von Gerätedaten für die Beweiswürdigung bedeutet. Prüfschwerpunkte daneben: Voraussetzungen und Grenzen der Verkehrsdatenerhebung nach § 100g StPO, der Beweiswert von Einzelzellen-Standortdaten, die Fehlerquellen suggestiver Wiedererkennungsverfahren sowie der Abgleich der Zeugenaussage der Schwester mit dem WhatsApp-Verlauf.

## Beteiligte

| Rolle | Person / Stelle |
| --- | --- |
| Beschuldigter | Kevin Rautenberg, Essen-Altendorf, Mobilfunkanschluss 0171 5583912 |
| Schwester (Zeugin) | Jasmin Rautenberg, Duisburg-Hochfeld, Wanheimer Straße 143 |
| Geschädigte Tat 1 | Renate Wichmann, Trinkhalle Wichmann, Essen-Altendorf |
| Geschädigter Tat 2 (Wiedererkennung) | Ercan Bulut, Kiosk Bulut, Essen-Frohnhausen |
| Zeuge Tat 3 | Milan Petrovic, City-Späti, Essen-Holsterhausen (Inhaber Faruk Demirel) |
| Verteidigerin | Rechtsanwältin Nadja Simonis, Essen |
| Staatsanwaltschaft | StA Essen, StA Dr. Kalthoff, 70 Js 883/26 |
| Polizei | PP Essen, KK 13, EK „Späti", KHKin Trosdorf, Tgb.-Nr. KK13-2026-1104 |
| Ermittlungsrichter | AG Essen, 44 Gs 2107/26 (§ 100g StPO), 44 Gs 2312/26 (Haftbefehl) |
| Mobilfunkanbieter | TeleNord Mobilfunk GmbH, Hamburg (fiktiv) |

## Aktenstruktur

```
strafrecht-funkzellenauswertung-alibi-raubserie-essen/
├── 01_anzeige_tatortbericht_tat1_2026-04-17.docx                — Überfall Trinkhalle Wichmann: Anzeige, Täterbeschreibung, Beute 799,50 EUR
├── 02_anzeige_tatortbericht_tat2_2026-05-02.docx                — Überfall Kiosk Bulut: verrutschter Schal, Halstätowierung, Schuhspur
├── 03_anzeige_tatortbericht_tat3_2026-05-15.docx                — Überfall City-Späti: erhöhter Kassenbestand, Presseeinfluss auf den Zeugen
├── 04_vermerk_serienzusammenhang_ek_spaeti_2026-05-18.docx      — EK-Vermerk: Serienmerkmale, anonymer Hinweis, Verdacht gegen Rautenberg
├── 05_antrag_sta_verkehrsdatenerhebung_2026-05-19.docx          — Antrag der StA nach § 100g Abs. 1 und 2, § 101a StPO
├── 06_beschluss_ag_essen_100g_stpo_2026-05-20.docx              — Anordnungsbeschluss des AG Essen für drei Abendzeiträume
├── 07_verkehrsdaten_mobilfunk_0171_5583912_2026-05-28.csv       — 31 Verkehrsdatensätze mit Zellen-ID, Standort und Zeitstempel
├── 08_taten_uebersicht_beute_ek_spaeti_2026-05-18.csv           — Taten-Zeitleiste mit Tatzeiten, Adressen und rechnerischer Beute
├── 09_lichtbildvorlage_protokoll_bulut_2026-05-27.docx          — Wahllichtbildvorlage mit protokollierter Einzelbildvorzeigung und Auswahlmängeln
├── 10_auswertevermerk_funkzellen_khk_trosdorf_2026-06-03.docx   — Polizeiliche Auswertung der Standortdaten je Tatabend
├── 11_haftbefehl_ag_essen_2026-06-04.docx                       — Haftbefehl wegen besonders schweren Raubes in drei Fällen
├── 12_beschuldigtenvernehmung_rautenberg_2026-06-05.docx        — Einlassung: ganzer Abend bei der Schwester, Handy nutzt nur er selbst
├── 13_zeugenvernehmung_jasmin_rautenberg_2026-06-08.docx        — Pauschale Alibibestätigung der Schwester, freiwillige Chat-Herausgabe
├── 14_vermerk_fahrzeiten_oepnv_pkw_2026-06-10.docx              — Fahrzeiten Pkw/ÖPNV zwischen Duisburg-Hochfeld und den Tatorten
├── 15_haftpruefungsantrag_verteidigung_2026-06-18.docx          — Haftprüfung: Angriff auf Tatverdacht, Wiedererkennung und Haftgrund
├── 16_verteidigerschriftsatz_teilentlastung_2026-06-26.docx     — Teileinstellungsantrag aus den eigenen Daten der StA, Beweisanregungen
├── eml/
│   ├── 2026-05-21_sta_essen_ersuchen_telenord.eml               — Übersendung des Beschlusses an den Anbieter, Bitte um CSV-Lieferung
│   ├── 2026-05-28_telenord_datenlieferung.eml                   — Datenlieferung mit Hinweisen zu Zellradius und Speicherfristen
│   └── 2026-06-16_verteidigung_akteneinsicht_rohdaten.eml       — Verteidigung fordert Rohdaten und Lichtbildbögen an
├── whatsapp/
│   └── chatverlauf.txt                                          — Chatexport Jasmin/Kevin mit der Nachricht vom 02.05.2026, 21:47 Uhr
├── rubric.yaml                                                  — Sechs Prüfpunkte zur Bewertung einer Bearbeitung
└── README.md                                                    — Diese Übersicht
```

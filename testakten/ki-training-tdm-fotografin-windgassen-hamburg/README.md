# KI-Training TDM Fotografin Windgassen Hamburg

**Plugin:** `fachanwalt-urheber-medienrecht`
**Branch:** `feat/v51.0.0-testakten-vollbestand`
**Aktenordner:** `testakten/ki-training-tdm-fotografin-windgassen-hamburg/`

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/ki-training-tdm-fotografin-windgassen-hamburg_gesamt.pdf`](gesamt-pdf/ki-training-tdm-fotografin-windgassen-hamburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-ki-training-tdm-fotografin-windgassen-hamburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-training-tdm-fotografin-windgassen-hamburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-ki-training-tdm-fotografin-windgassen-hamburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-training-tdm-fotografin-windgassen-hamburg-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

---

## Szenario-Überblick

**Mandantin:** Mira Windgassen, 47, Frickestraße 29, 20251 Hamburg-Eppendorf
**Beruf:** Freischaffende Reportage- und Editorialfotografin; Inhaberin Windgassen Photo Atelier (ca. 18.400 Fotografien in Eigenverwertung). Auftraggeber: GEO, Mare, Brigitte, Zeit-Magazin.
**Anwältin:** Dr. Antonia Kreidler-Bremer, Fachanwältin für Urheber- und Medienrecht, Kanzlei Kreidler-Bremer Medienrecht, Mittelweg 147, 20148 Hamburg-Rotherbaum
**VG Bild-Kunst:** Mitgliedsnr. 142.907 (Gruppe II: Fotografen)

---

## Konflikt-Komplexe

| # | Komplex | Skill(s) | AZ | Status |
|---|---|---|---|---|
| 1 | KI-Training-Opt-out § 44b UrhG (ImagineArt Inc. / LAION-5B) | `fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out` | LG Hamburg 308 O 79/26 | Klagevorbereitung |
| 2 | Filesharing-Abmahnung Quetschenpaua & Kollegen (Sohn Felix, 14 J.) | `fachanwalt-urheber-medienrecht-filesharing-verteidigung` | AG München 155 C 18801/26 | Frist 30.01.2026 |
| 3 | Lizenzvertrag-Verhandlung Bildband (Mare GmbH) | `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` | außergerichtlich | Verhandlung offen |
| 4 | Presserechtliche Gegendarstellung (Eppendorfer Wochenanzeiger) | `fachanwalt-urheber-medienrecht-presse-gegendarstellung` + `fachanwalt-urheber-medienrecht-gegendarstellung-presse` | außergerichtlich | Frist 30.01.2026 |
| 5 | Schiedsstelle DPMA / VGG (KI-Training-Vergütung) | `fachanwalt-urheber-medienrecht-schiedsstelle-dpma-vgg` | Sch-Urh 32/26 | Termin 17.03.2026 |
| 6 | Bearbeitungsrecht Tochter Lia (Instagram-Collagen) | `fachanwalt-urheber-medienrecht-mod-erklaerung` | familienintern | Klärung offen |

---

## Getestete Skills und Komplexe

| # | Skill | Aktenstück(e) |
|---|---|---|
| 1 | `fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out` | 03, 04, 10, 11, 15, 17, 20 |
| 2 | `fachanwalt-urheber-medienrecht-filesharing-verteidigung` | 05, 18 + NFK_Filesharing.docx |
| 3 | `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` | 06, 16 |
| 4 | `fachanwalt-urheber-medienrecht-presse-gegendarstellung` | 07 + Gegendarstellungsantrag.docx |
| 5 | `fachanwalt-urheber-medienrecht-gegendarstellung-presse` | 07 + Gegendarstellungsantrag.docx |
| 6 | `fachanwalt-urheber-medienrecht-schiedsstelle-dpma-vgg` | 08, 17 |
| 7 | `fachanwalt-urheber-medienrecht-mod-erklaerung` | 09 |
| 8 | `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` | 06, 16, 19 |

---

## Schlüssel-Rechtsfragen

1. **§ 44b Abs. 3 UrhG:** Genügt eine robots.txt mit `Disallow: /portfolio/` als maschinenlesbarer Vorbehalt, wenn die Bilddateien selbst unter `/wp-content/uploads/` ungepflegt sind? Ist der Vorbehalt ex ante anzusehen?

2. **Zeitliche Grenze § 44b UrhG:** Der erste nachgewiesene CCBot-Abruflauf (03.06.2021) fand 4 Tage **vor** Inkrafttreten des § 44b UrhG (07.06.2021) statt — der zweite Abruflauf (17.08.2021) danach. Wie wirkt sich die Aufspaltung auf die Klagestrategie aus?

3. **Sekundäre Darlegungslast (BGH Tauschbörsen III):** Genügt die Benennung des 14-jährigen Sohnes als Alternativtäter, wenn die Mutter nur eine allgemeine, nicht auf Filesharing spezialisierte Belehrung erteilt hat?

4. **Gegendarstellungsrecht § 11 HmbPresseG:** Ist die Berichterstattung des Eppendorfer Wochenzeigers eine Tatsachenbehauptung (Gegendarstellungsrecht) oder Meinungsäußerung (kein Gegendarstellungsrecht)?

5. **Lizenzauslegung § 31 Abs. 5 UrhG (Zweckübertragungslehre):** Wie ist der Vertragstext von 2019 (einmalig, Print Deutschland) gegenüber dem nachträglich gestempelten „Buyout Print International" auszulegen?

6. **Stilschutz im KI-Kontext:** Ist Stilmimikry durch einen KI-Bildgenerator urheberrechtlich relevant, wenn konkrete Werke im Trainingsdatensatz nachweisbar sind?

---

## Widersprüche und Ambiguitäten in der Akte

- Die Mandantin gibt an, robots.txt schütze ihre Bilder seit 2019; die Serverlog-Analyse zeigt, dass CCBot trotzdem auf `/portfolio/` zugegriffen hat (HTTP 200).
- Windgassen meint, nur Erstveröffentlichungsrechte vergeben zu haben; Mare hat den Vertrag mit „Buyout Print International" abgestempelt. Das Originaldokument ist noch nicht vollständig beigebracht.
- Die allgemeine Belehrung von Felix über illegale Downloads war unspezifisch — reicht das für die sekundäre Darlegungslast?
- BFF-Beratungsprotokoll von Oktober 2023 zeigt, dass Windgassen selbst von der Unzulänglichkeit ihrer robots.txt wusste.

---

## Beteiligte Parteien

| Partei | Rolle |
|---|---|
| Mira Windgassen | Mandantin |
| Dr. Antonia Kreidler-Bremer | Rechtsanwältin, Kanzlei Kreidler-Bremer Medienrecht |
| Felix Windgassen (14 J.) | Sohn der Mandantin, mutmaßlicher Filesharing-Täter |
| Martin Windgassen | Ehemann der Mandantin (kein Tätervorwurf) |
| Lia Windgassen (19 J.) | Tochter, Kunststudentin (Collage-Problematik) |
| ImagineArt Inc., Delaware/USA | Beklagte KI-Unternehmen (Klage LG Hamburg) |
| Quetschenpaua & Kollegen Rechtsanwälte, München | Abmahnkanzlei (Filesharing) |
| Mare GmbH, Hamburg | Verlagshaus (Lizenzstreit Bildband) |
| Eppendorfer Wochenanzeiger GmbH | Gegendarstellungsgegner |
| VG Bild-Kunst, Bonn | Verwertungsgesellschaft / Schiedsstellenantragstellerin |
| DPMA-Schiedsstelle, München | Behörde (Sch-Urh 32/26) |
| Dipl.-Inf. Kerstin Barkhoff | IT-Forensik-Sachverständige |
| Prof. Dr. Katrin Felber, HfbK Hamburg | Sachverständige Bildästhetik (angefragt) |

---

## Aktenstücke (22 nummerierte Markdown-Dateien)

| Nr. | Datei | Inhalt |
|---|---|---|
| 01 | `01_aktenvorblatt_windgassen.docx` | Aktenvorblatt, Fristen, Parteien |
| 02 | `02_mandantengespraech_erstaufnahme.docx` | Erstgespräch-Protokoll, Sachverhalt |
| 03 | `03_tdm_opt_out_pruefung_paragraf_44b_urhg.docx` | Rechtsgutachten Paragraf 44b UrhG, Opt-out-Analyse |
| 04 | `04_laion_serverlog_analyse.docx` | IT-Forensik Barkhoff: CCBot-Abruflauf-Nachweis |
| 05 | `05_filesharing_abmahnung_quetschenpaua_kollegen.docx` | Abmahnungsanalyse + Verteidigungsstrategie |
| 06 | `06_lizenzvertrag_mare_analyse.docx` | Lizenzvertrag 2019, Auslegungsstreit Buyout |
| 07 | `07_gegendarstellung_eppendorfer_wochenanzeiger.docx` | Presserecht, Gegendarstellungsentwurf |
| 08 | `08_schiedsstelle_dpma_vgg_antrag.docx` | Schiedsstellenverfahren Sch-Urh 32/26 |
| 09 | `09_mod_erklaerung_tochter_lia.docx` | Bearbeitungsrecht-Klärung Lia-Collagen |
| 10 | `10_schadensberechnung_ki_training_lizenzanalogie.docx` | Schadensberechnung § 97 Abs. 2 UrhG |
| 11 | `11_klagestrategie_lg_hamburg_imagineArt.docx` | Klagestrategie, Anträge, Risiken |
| 12 | `12_chronologie_ereignisse.docx` | Gesamtchronologie aller Ereignisse |
| 13 | `13_fristenuebersicht_aktuell.docx` | Fristkalender, Wiedervorlage |
| 14 | `14_imagineArt_stilanalyse_sachverstaendiger.docx` | Sachverständigen-Anfrage Stilmimikry |
| 15 | `15_bff_beratungsprotokoll.docx` | BFF-Seminar-Notiz Oktober 2023 (retrograd) |
| 16 | `16_mare_verhandlungskorrespondenz.docx` | Mare-Korrespondenz + Antwort-Entwurf |
| 17 | `17_vg_bildkunst_tarifstreit_ueberblick.docx` | VG Bild-Kunst KI-Tarif, VGG-Rechtssystem |
| 18 | `18_felix_windgassen_minderjaehriger_darlegung.docx` | Sekundäre Darlegungslast, Sohn Felix |
| 19 | `19_lizenzhistorie_windgassen_photo_atelier.docx` | Lizenzhistorie-Überblick (→ XLSX) |
| 20 | `20_imagineArt_recherche_us_gesellschaft.docx` | ImagineArt Inc. Delaware, US-Parallelverfahren |
| 21 | `21_mandantenschreiben_zwischenbericht.docx` | Zwischenbericht an Mandantin (Entwurf) |
| 22 | `22_kostenuebersicht_honorarabrechnung.docx` | Honorarabrechnung, Kostenübersicht |

---

## Anhänge

### docx/ (3 Dokumente)
| Datei | Inhalt |
|---|---|
| `NFK_Filesharing_Windgassen_Entwurf.docx` | Negative Feststellungsklage, AG München 155 C 18801/26 |
| `Klage_LG_Hamburg_ImagineArt_Entwurf.docx` | Klageschrift LG Hamburg 308 O 79/26 |
| `Gegendarstellungsantrag_Eppendorfer_Wochenanzeiger.docx` | Presserechtliche Gegendarstellung § 11 HmbPresseG |

### xlsx/ (2 Tabellen)
| Datei | Inhalt |
|---|---|
| `lizenzhistorie_windgassen_18400_bilder.xlsx` | Lizenzhistorie 18.400 Bilder nach Verwertungskategorie; Jahresumsatz 2021–2025; Opt-out-Status |
| `schadensberechnung_ki_training_lizenzanalogie.xlsx` | Schadensberechnung § 97 Abs. 2 UrhG; Tarifvergleich; Streitwert; Kosten-Risiko-Matrix |

### eml/ (7 E-Mails)
| Datei | Inhalt |
|---|---|
| `mare_bildband_angebot_2026-01-12.eml` | Mare GmbH: Bildband-Angebot 1.200 EUR |
| `quetschenpaua_kollegen_abmahnung_eingang_2026-01-09.eml` | Quetschenpaua & Kollegen: Abmahnungs-E-Mail (06.01.2026) |
| `dpma_schiedsstelle_terminsladung_2026-01-20.eml` | DPMA-Schiedsstelle: Ladung zum Termin 17.03.2026 |
| `windgassen_an_kreidler_bremer_sohn_felix_2026-01-23.eml` | Mandantin an RA: Mitteilung nach Felix-Gespräch |
| `waldorf_frommer_abmahnung_eingang_2026-01-09.eml` | Waldorf Frommer: Abmahnungs-E-Mail |
| `imagineart_us_counsel_antwort_2026-01-28.eml` | ImagineArt Inc. Legal Department: Antwort auf vorgerichtliche Aufforderung |
| `windgassen_vertragskopie_mare_2026-02-02.eml` | Mandantin an RA: aufgefundener eigener Vertragsdurchschlag 2019 ohne Buyout-Stempel, Hinweis auf möglichen Schweiz-Nachtrag |

### pdfs/ (4 PDFs, teils redacted)
| Datei | Inhalt |
|---|---|
| `quetschenpaua_kollegen_abmahnung_redacted.pdf` | Quetschenpaua & Kollegen-Abmahnung (Rechteinhaber, IP, Hashes geschwärzt) |
| `serverlog_robots_txt_auszug_redacted.pdf` | Serverlog-Auszug IT-Forensik Barkhoff + robots.txt/ai.txt (Besucher-IPs geschwärzt) |
| `waldorf_frommer_abmahnung_redacted.pdf` | Waldorf Frommer-Abmahnung (Rechteinhaber, Hashes geschwärzt) |
| `vg_bildkunst_tarifuebersicht_ki_training_redacted.pdf` | VG Bild-Kunst Tarifübersicht KI-Training, Auszug (Mitgliedsdaten geschwärzt) |

### jpg/ (3 Bilder)
| Datei | Inhalt |
|---|---|
| `werkstattfoto_atelier_windgassen.jpg` | Atelier-Werkstattfoto (Photostudio Hamburg-Eppendorf, illustrativ) |
| `vergleich_original_vs_ki_bild_bodden.jpg` | Gegenüberstellung: Original Windgassen-Fotografie vs. ImagineArt-Pro-Erzeugnis |
| `screenshot_imagineartpro_ui_redacted.jpg` | Screenshot ImagineArt Pro Benutzeroberfläche mit Prompt (redacted) |

---

## Erlaubte Quellenverweise

- dejure.org: § 44b UrhG — https://dejure.org/gesetze/UrhG/44b.html
- dejure.org: § 97 UrhG — https://dejure.org/gesetze/UrhG/97.html
- dejure.org: § 31 UrhG — https://dejure.org/gesetze/UrhG/31.html
- dejure.org: § 11 HmbPresseG — https://dejure.org/gesetze/HmbPG/11.html
- dejure.org: § 92 VGG — https://dejure.org/gesetze/VGG/92.html
- bundesgerichtshof.de: BGH I ZR 75/14 (Tauschbörse III) — https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/2015/06/IZR7514.html

---

## Bericht

| Kategorie | Anzahl |
|---|---|
| Nummerierte DOCX-Aktenstücke | 22 |
| DOCX-Anhänge | 3 |
| XLSX-Anhänge | 2 |
| EML-Anhänge | 7 |
| PDF-Anhänge (teils redacted) | 4 |
| JPG-Anhänge | 3 |
| **Anhänge gesamt** | **19** |

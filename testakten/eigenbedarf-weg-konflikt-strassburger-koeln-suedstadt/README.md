# Akte: Eigenbedarf + WEG-Konflikt – Straßburger / Köln-Südstadt


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 419 KB) | PDF | [`gesamt-pdf/eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt_gesamt.pdf`](gesamt-pdf/eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

**Plugin:** `fachanwalt-miet-wohnungseigentumsrecht`
**Branch:** `feat/v51.0.0-testakten-vollbestand`
**Angelegt:** Mai 2026
**Mandanten (Vermieter):** Dr. Cornelia Straßburger + Dr. Boris Straßburger-Möhren
**Mieter:** WG Albrecht / van Drosten / Sonnenfeld
**Objekt:** Rolandstraße 27a, DG-Wohnung 110 m², 50677 Köln-Südstadt (WEG, 6 Einheiten)
**Verfahren:** AZ AG Köln Räumung: `213 C 188/26` | AZ AG Köln WEG: `205 C 67/26`
**Anwältin:** RA'in Vanessa Hauck-Brüggemann, Fachanwältin für Miet- und WEG-Recht

---

## Überblick der Rechtskomplexe

| # | Komplex | Skill | Status |
|---|---|---|---|
| 1 | Eigenbedarfskündigung § 573 BGB + Widerspruch § 574 BGB | `fachanwalt-miet-wohnungseigentumsrecht-eigenbedarfskuendigung` | Räumungsklage vorbereitet |
| 2 | WEG-Beschlussanfechtung § 44 WEG (Treppenhaussanierung) | WEG-Plugin allgemein | Klage eingereicht 12.05.2026 |
| 3 | Mietminderung Schimmel § 536 BGB | `fachanwalt-miet-wohnungseigentumsrecht-mietminderung-schimmel` | Sanierung geplant |
| 4 | Heizungsumstellung Sole-Wasser-WP / GEG | `fachanwalt-miet-weg-waermepumpe-geg` | Prüfungsphase |
| 5 | Schlichtung Mieterverein | `fachanwalt-miet-weg-mediation-mietverein-schlichtung` | Gescheitert 05.05.2026 |

---

## Verzeichnisstruktur

```
eigenbedarf-weg-konflikt-strassburger-koeln-suedstadt/
├── README.md                                   ← Diese Datei
│
├── 01_aktenvorblatt_hauck_brueggemann.md
├── 02_mietvertrag_2018_kpl.md
├── 03_eigenbedarfskuendigung_28_02_2026.md
├── 04_widerspruch_mieter_sozialklausel_574_bgb.md
├── 05_kanzleinotiz_erstgespraech_strassburger.md
├── 06_weg_protokoll_14_04_2026.md
├── 07_anfechtungsklage_treppenhaussanierung.md
├── 08_wirtschaftsplan_weg_2026.md
├── 09_kostenvoranschlag_restaurator_a.md
├── 10_kostenvoranschlag_restaurator_b.md
├── 11_kostenvoranschlag_restaurator_c.md
├── 12_schimmelgutachten_wallesch.md
├── 13_mietminderungsanzeige_levi_albrecht.md
├── 14_mahnung_mietrueckstaende_30_prozent.md
├── 15_weg_beschluss_waermepumpe.md
├── 16_beg_foerderantrag_skizze.md
├── 17_schlichtungsvorschlag_mieterverein.md
├── 18_email_kette_hauck_brueggemann_mieter.md
├── 19_klageschrift_raeumungs_und_zahlungsklage_entwurf.md
├── 20_mandantenrundbrief_strassburger.md
├── 21_strategiememorandum.md
├── 22_fristenkalender.md
│
├── docx/
│   ├── eigenbedarfskuendigung_28_02_2026.docx
│   ├── anfechtungsklage_weg_treppenhaussanierung.docx
│   └── klageschrift_raeumungs_zahlungsklage_entwurf.docx
│
├── xlsx/
│   ├── weg_sonderumlage_mea_verteilung.xlsx
│   └── mietminderungsberechnung_8_monate.xlsx
│
├── eml/
│   ├── 01_hauck_brueggemann_an_lemke_07_03_2026.eml
│   ├── 02_lemke_an_hauck_brueggemann_10_03_2026.eml
│   ├── 03_hauck_brueggemann_an_lemke_25_03_2026.eml
│   └── 04_lemke_an_hauck_brueggemann_05_05_2026.eml
│
├── pdfs/
│   ├── weg_protokoll_auszug_14_04_2026.pdf
│   └── schimmelgutachten_wallesch_auszug.pdf
│
└── jpg/
    ├── grundriss_dg_wohnung_rolandstrasse27a.jpg
    ├── aussenansicht_rolandstrasse27a_koeln_suedstadt.jpg
    └── schimmelstelle_schlafzimmer_suedgiebel.jpg
```

---

## Wichtige Personen

| Person | Rolle | Kontakt |
|---|---|---|
| Dr. Cornelia Straßburger | Vermieterin / Mandantin | Uniklinik Köln (Pädiatrie) |
| Dr. Boris Straßburger-Möhren | Vermieter / Mandant | Bürogemeinschaft Möhren+Partner |
| Theresa Straßburger-Möhren | Eigenbedarfsperson (Tochter, Referendarin) | – |
| Levi Albrecht | Mieter, Vikar Erzbistum Köln (bis 31.07.2028) | – |
| Femke van Drosten | Mieterin, Medizinstudentin 8. Sem. | – |
| Mathilda Sonnenfeld | Mieterin, Medizinstudentin 8. Sem., Famulatur | – |
| Vanessa Hauck-Brüggemann | Vermieter-Anwältin | kanzlei@hauck-brueggemann-mietrecht.de |
| Wolfgang Lemke | Mieterverein Köln, Sachbearbeiter | lemke@mieterverein-koeln.de |
| Dipl.-Ing. Hubert Wallesch | SV Schimmelgutachten | wallesch-sv@konstrukt-koeln.de |
| Jürgen Rheineck | WEG-Verwalter | Immobilienverwaltung Rheineck GmbH |

---

## Wichtige Fristen

| Datum | Frist | Status |
|---|---|---|
| 12.05.2026 | Anfechtungsklage WEG eingereicht (Frist: 14.05.2026) | ✅ |
| 20.05.2026 | Räumungsklage Entwurf (Einreichung ausstehend) | ⏳ |
| 01.06.2026 | WEG-Sonderumlage Rate 1 (9.940 EUR Straßburger) | ⚠️ |
| 30.06.2026 | Geplante Fertigstellung Schimmelsanierung | 🔲 |
| 31.10.2026 | Mietende laut Kündigung | 🔲 |

---

## Genutzte Quellen (Rechtsprechung)

- BGH, Urt. v. 17.10.2014, V ZR 9/14 — NJW 2015, 843 (ordnungsgemäße Verwaltung, WEG)
- BGH, Urt. v. 13.01.2012, V ZR 129/11 — NJW 2012, 1224 (WEG-Beschluss, Verhältnismäßigkeit)
- BGH, Urt. v. 17.06.2015, VIII ZR 19/14 — NJW 2015, 2422 (Mietminderung Schimmel)
- BGH, Urt. v. 06.10.2004, VIII ZR 355/03 (Mietminderungsquote)
- BGH, Urt. v. 11.12.2013, VIII ZR 235/12 — NJW 2014, 539 (Kündigung bei Mängeln)
- OLG Köln, Urt. v. 28.11.2017, 22 U 14/17 (Minderungsquote Schimmel)
- OLG München, Urt. v. 27.01.2011, 32 Wx 102/10 (WEG, Alternativenprüfung)

Quellen abrufbar unter: [dejure.org](https://dejure.org) | [openjur.de](https://openjur.de) | [bundesgerichtshof.de](https://www.bundesgerichtshof.de)

---

*Arbeitsstand der Kanzlei Hauck-Brüggemann; vor Verwendung im Mandat sind Originalvollmachten, Zustellnachweise und Grundbuch-/WEG-Unterlagen abzugleichen.*
*Keine Build-Scripts, keine Symlinks in diesem Ordner.*

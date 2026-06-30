# Cyber-Vorfall Ransomware Frischetrans Mainz


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 740 KB) | PDF | [`gesamt-pdf/cyber-vorfall-ransomware-frischetrans-mainz_gesamt.pdf`](gesamt-pdf/cyber-vorfall-ransomware-frischetrans-mainz_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-cyber-vorfall-ransomware-frischetrans-mainz.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-cyber-vorfall-ransomware-frischetrans-mainz.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-cyber-vorfall-ransomware-frischetrans-mainz-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-cyber-vorfall-ransomware-frischetrans-mainz-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

**Plugin:** `fachanwalt-it-recht`
**Branch:** `feat/v51.0.0-testakten-vollbestand`
**Aktenordner:** `testakten/cyber-vorfall-ransomware-frischetrans-mainz/`

---

## Szenario-Überblick

**Mandantin:** Frischetrans Mittelrhein GmbH, Mainz (Logistik-Mittelständler, 280 MA, 64 LKW, B2B-Frischelogistik)
**Anwalt:** RA Lukas Drosten, Fachanwalt für IT-Recht, Kanzlei Drosten & Pekonkur, Mainz
**Vorfall:** Ransomware-Angriff „AkiraNext" — 06.05.2026, 04:17 Uhr
**Forderung Erpresser:** 1.450.000 USD in Monero (nicht gezahlt)
**Datenabfluss:** 2,1 TB (Kundenstammdaten 18 Kunden, Personalakten 280 MA, BEM-Gesundheitsdaten 38 MA)

---

## Getestete Skills und Komplexe

| # | Skill / Komplex | Aktenstück(e) |
|---|---|---|
| 1 | `cyber-incident-response-72h` + `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` | 02, 04, 05, 06, 07, 15, 22 |
| 2 | `fachanwalt-it-recht-datenschutz-folgenabschaetzung` (DSFA BEM-Gesundheitsdaten) | 11, 12, 17 |
| 3 | SaaS-Vertragsstreit ProcessSpark / CVE-2026-0712 | 08, 09, 10 |
| 4 | `fachanwalt-it-recht-it-vertrag-verhandlung-eu-odr` | 08, 09, 10, 20 |
| 5 | `fachanwalt-it-recht-ki-vo-hochrisiko-konformitaetsbewertung` (PalettenAuge AI) | 13, 18 |
| 6 | `fachanwalt-it-recht-open-source-compliance-audit` (TourPlanner / AGPL-3.0) | 14 |

---

## Beteiligte Parteien

| Partei | Rolle |
|---|---|
| Frischetrans Mittelrhein GmbH | Mandantin |
| Theresia Wallbruck | Geschäftsführerin Mandantin |
| RA Lukas Drosten | Anwalt (Kanzlei Drosten & Pekonkur) |
| InsoTec Systems GmbH, Frankfurt | Externer IT-Dienstleister / SOC |
| ProcessSpark Cloud AG, München | SaaS-ERP-Anbieter (Gegner) |
| DachAuge GmbH, Berlin | KI-System-Anbieter (PalettenAuge AI) |
| LfDI Rheinland-Pfalz | Datenschutzbehörde |
| BSI Außenstelle Frankfurt | NIS2-Behörde |
| ZAC Mainz | Strafverfolgung Cybercrime |
| CyberCovered AG | Cyber-Versicherer (5 Mio. EUR Police) |
| Frischbäcker AG | Betroffener Kunde (systemrelevant) |
| Backhaus Süd GmbH & Co. KG | Betroffener Kunde (systemrelevant) |

---

## Verfahrensstatus und Aktenzeichen

| Verfahren | Aktenzeichen |
|---|---|
| Strafanzeige ZAC Mainz | 421 UJs 6611/26 |
| Klage LG Mainz (ProcessSpark, geplant) | 3 O 88/26 |
| DSGVO-Meldung LfDI RLP | LfDI-RLP-2026-0508-4419 |
| BSI-Meldung NIS2 | BSI-REF-2026-1847 |
| Versicherungsschaden CyberCovered | CC-SCHADEN-2026-FTM-0914 |

---

## Aktenstücke (22 Markdown-Dokumente)

| Nr. | Dateiname | Inhalt | Größe |
|---|---|---|---|
| 01 | `01_aktenvorblatt_drosten_pekonkur.md` | Mandatsblatt, Beteiligte, Fristen | ~4 KB |
| 02 | `02_chronologie_cyber_vorfall_d0_bis_d7.md` | Stundengenaue Ereignischronologie D+0 bis D+7 | ~8 KB |
| 03 | `03_erpressungsschreiben_akiranext.md` | Erpressungsschreiben + rechtliche Bewertung | ~7 KB |
| 04 | `04_kanzleinotiz_erstgespraech_wallbruck.md` | Mandatsgespräch-Notiz, Handlungsplan | ~6 KB |
| 05 | `05_meldung_lfdi_rlp_art_33_dsgvo.md` | DSGVO-Meldung Art. 33 an LfDI RLP | ~7 KB |
| 06 | `06_meldung_bsi_nis2.md` | NIS2-Meldung an BSI Außenstelle Frankfurt | ~7 KB |
| 07 | `07_strafanzeige_zac_mainz.md` | Strafanzeige ZAC Mainz (421 UJs 6611/26) | ~7 KB |
| 08 | `08_vertragsanalyse_processspark_sla.md` | SLA-Analyse IT-Betriebsvertrag ProcessSpark | ~8 KB |
| 09 | `09_pflichtverletzung_processspark_cve_2026_0712.md` | Kausalitätsanalyse CVE-2026-0712 | ~7 KB |
| 10 | `10_klageandrohung_processspark.md` | Klageandrohungsschreiben, Forderung EUR 681.818 | ~7 KB |
| 11 | `11_dsfa_bem_gesundheitsdaten.md` | DSFA Art. 35 DSGVO — BEM-Gesundheitsdaten | ~7 KB |
| 12 | `12_meldung_betroffene_art_34_dsgvo.md` | Mitarbeiterbenachrichtigung Art. 34 DSGVO | ~7 KB |
| 13 | `13_ki_vo_klassifizierung_palettenauge.md` | KI-VO Hochrisiko-Analyse PalettenAuge AI | ~8 KB |
| 14 | `14_open_source_audit_scheduleherokit.md` | AGPL-3.0 Compliance-Audit TourPlanner | ~7 KB |
| 15 | `15_versicherungsmeldung_cybercovered.md` | Versicherungsmeldung CyberCovered AG | ~5 KB |
| 16 | `16_kundenkommunikation_frischbaecker_backhaussued.md` | Kundenkommunikation (2 systemrelevante Kunden) | ~7 KB |
| 17 | `17_mitarbeiter_information_bem_betroffenheit.md` | Individualkommunikation BEM-Betroffene (38 MA) | ~7 KB |
| 18 | `18_betriebsrat_anhoerung.md` | BR-Anhörungsprotokoll (§ 87 BetrVG, KI-VO) | ~6 KB |
| 19 | `19_pressemitteilung_entwurf_redacted.md` | Pressemitteilungs-Entwurf (kanzleigeprüft) | ~5 KB |
| 20 | `20_strategiememorandum_drosten.md` | Strategiememorandum RA Drosten | ~7 KB |
| 21 | `21_kostenrisiko_streitwert_analyse.md` | Kostenrisiko / RVG-Streitwertberechnung | ~6 KB |
| 22 | `22_fristenuebersicht_meldepflichten.md` | Vollständige Fristen- und Terminübersicht | ~6 KB |

---

## Anlagen

### docx/ (3 DOCX-Dokumente)
| Datei | Inhalt |
|---|---|
| `lfdi_meldung_art33_dsgvo.docx` | Formelle DSGVO-Meldung an LfDI RLP (Art. 33) |
| `klageandrohung_processspark.docx` | Klageandrohungsschreiben an ProcessSpark Cloud AG |
| `dsfa_bericht_bem_gesundheitsdaten.docx` | DSFA-Bericht BEM-Gesundheitsdaten (Art. 35 DSGVO) |

### xlsx/ (2 XLSX-Tabellen)
| Datei | Inhalt |
|---|---|
| `betroffenenverzeichnis_anonymisiert.xlsx` | 280 betroffene Personen (pseudonymisiert), BEM-Kennzeichnung |
| `sla_schaden_berechnung.xlsx` | Schadensberechnung mit Ausfallzeiten, ProcessSpark-Regressforderung EUR 681.818 |

### eml/ (4 E-Mails)
| Datei | Inhalt |
|---|---|
| `01_drosten_an_lfdi_rlp_art33.eml` | RA Drosten → LfDI RLP: DSGVO-Meldung Übermittlung |
| `02_drosten_an_processspark_klageandrohung.eml` | RA Drosten → ProcessSpark: Klageandrohung |
| `03_drosten_an_cybercovered_versicherungsmeldung.eml` | RA Drosten → CyberCovered: Schadensmeldung |
| `04_wallbruck_an_drosten_erstmeldung.eml` | Wallbruck → Drosten: Erstmeldung des Vorfalls |

### pdfs/ (2 PDF-Dokumente)
| Datei | Inhalt |
|---|---|
| `erpressungsschreiben_akiranext_redacted.pdf` | Erpressungsschreiben (geschwärzte Fassung, ReportLab) |
| `bsi_meldebestaetigung.pdf` | BSI-Meldebestätigung NIS2 (Ref. BSI-REF-2026-1847) |

### jpg/ (3 JPG-Abbildungen, erstellt mit Pillow)
| Datei | Inhalt |
|---|---|
| `01_netzwerktopologie_frischetrans.jpg` | Netzwerktopologie vor Angriff (Rekonstruktion, forensisch) |
| `02_ransomware_erpressungsschreiben_screenshot.jpg` | Screenshot Erpressungsschreiben (redacted) |
| `03_serverraum_uebersicht.jpg` | Serverraum Tatortdokumentation mit forensischen Markierungen |

---

## Technische Compliance-Angaben

- Kein YAML-Frontmatter in MD-Dateien
- Keine Build-Scripts im Aktenordner
- Keine Symlinks
- Keine git-Commits oder git-Push-Operationen
- Plugin-README nicht berührt
- Deutsche Umlaute (ä, ö, ü, ß) in allen MD-Dateien korrekt kodiert (UTF-8)
- Schriftsätze: 800–3.000 Wörter je MD-Dokument

## Quellen und Rechtsgrundlagen

Alle in den Dokumenten genannten Rechtsnormen beziehen sich auf:
- DSGVO (VO (EU) 2016/679)
- BGB (Bürgerliches Gesetzbuch)
- StGB (Strafgesetzbuch)
- NIS2-Richtlinie (RL (EU) 2022/2555) / NIS2UmsuG
- KI-Verordnung (VO (EU) 2024/1689)
- BetrVG (Betriebsverfassungsgesetz)
- BDSG (Bundesdatenschutzgesetz)
- SGB IX (§ 167 — BEM-Verfahren)
- UrhG (Urheberrechtsgesetz — AGPL-3.0-Compliance)
- ADSp 2017 (Allgemeine Deutsche Spediteurbedingungen)

Quellnachweise (soweit online verfügbar): dejure.org, openjur.de, bundesgerichtshof.de

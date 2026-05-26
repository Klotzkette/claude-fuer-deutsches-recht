# v12.0.1 — Hotfix forderungsmanagement-klagewerkstatt Plugin-Generator

## Fix
- `scripts/plugin_aus_hausregeln.py` erzeugt jetzt validatorkonforme Mini-Plugins (`klagewerkstatt-<slug>`):
  - plugin.json description gekuerzt auf 218 Zeichen (vorher 514, Marketplace-Limit 300)
  - Zahl-Komma-Zahl-Sequenz `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` in plugin.json + SKILL.md description
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt (Trigger-Phrasen in description integriert)
- Erzeugte hauseigene Plugins lassen sich jetzt sofort in Claude Code installieren.

## v12.0.0 — 2026-05-26 — Strafrecht-Ausbau: Nebenklage, Zeugenbeistand, Adhaesion, Insolvenzantrag der StA + Codex-Fixes + Bug-Hunt

### Major-Feature: 4 neue Skills im Plugin `fachanwalt-strafrecht`

- `fachanwalt-strafrecht-nebenklage-opfervertretung` — Nebenklagebefugnis § 395 StPO, Anschluss § 396 StPO, Opferanwaltsbeiordnung § 397a StPO, Akteneinsicht § 406e StPO, psychosoziale Prozessbegleitung § 406g StPO, RVG VV Nr. 4124 ff.
- `fachanwalt-strafrecht-zeugenbeistand` — Beistand gemaess § 68b StPO, Pruefung § 55 StPO Selbstbelastung, §§ 52-53 StPO Zeugnisverweigerung, Adressanonymisierung § 68 Abs. 2/3 StPO, Whistleblower-Konstellation.
- `fachanwalt-strafrecht-adhaesionsverfahren` — zivilrechtliche Anspruche im Strafverfahren §§ 403-406c StPO, Antrag § 404 StPO, Vergleich § 405 StPO als Vollstreckungstitel, Grundurteil § 406 StPO, RVG VV Nr. 4143-4147.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` — Insolvenzantrag StA / Finanzamt gegen Angeklagte, Doppelspur Strafverfahren-Insolvenzverfahren, Vermoegensabschoepfung §§ 73 ff. StGB und Beschlagnahme §§ 111b ff. StPO, § 111i StPO, Schweigerecht vs. § 97 InsO.

### Codex-Feedback adressiert (PR fachanwalt-strafrecht)

Drei Skills im Plugin `fachanwalt-strafrecht` enthielten zivilrechtliche Reste aus einem Allgemein-Template (Leistungs-/Feststellungs-/Gestaltungsantrag, Streitwert aus Hauptforderung, Klage-einreichen-Walk-Away). Komplett strafrechts-spezifisch neu geschrieben:

- `schriftsatzkern-substantiierung` — Einspruch gegen Strafbefehl, Revisionsbegruendung, Klageerzwingung, Beweisantraege § 244 StPO, Verfahrenshindernisse, Sach- und Verfahrensruegen.
- `vergleichsverhandlung-strategie` — Verstaendigung § 257c StPO, Einstellung § 153a StPO, Adhaesionsvergleich § 405 StPO, TOA § 46a StGB; statt zivilrechtlicher Skripte.
- `erstgespraech-mandatsannahme` — RVG-Gebuehrentatbestaende VV-RVG Teil 4 und Teil 5 statt Streitwert-Kalkulation, fuenf strafrechtsspezifische Praxis-Konstellationen.

### Bug-Hunt v12.0.0

- Alle Backtick-Cross-Refs auf das fusionierte Plugin `kanzlei-cowork` (52 Dateien in 24 Plugins + CHANGELOG, INSTALLATION, ASSET_INDEX, TESTBERICHT) auf `kanzlei-allgemein` umgestellt.
- Config-Pfade in `kanzlei-allgemein/skills/{sekretariats-tagesbrief, mandantenakte-anlegen, fristenbuch-fuehren, kanzlei-cowork-kaltstart-interview}` von `~/.claude/plugins/config/.../kanzlei-cowork/` auf `kanzlei-allgemein/` korrigiert.
- Slash-Command-Verweise in `tests/smoke-tests.md` und `kanzlei-cowork-kaltstart-interview` von `/kanzlei-cowork:` auf `/kanzlei-allgemein:` umgestellt.
- `tests/smoke-tests.md`: Abschnitt-Header von `## kanzlei-cowork (rechnungserstellung-rvg)` auf `## kanzlei-allgemein (rechnungserstellung-rvg)` umgestellt.
- `kanzlei-allgemein/.claude-plugin/plugin.json`: Keyword `kanzlei-cowork` aus Liste entfernt (Migrations-Hinweis in README/CHANGELOG bleibt).
- Workflow-Validator-Fixes aus v11.0.0-Schluss: `README.md` ohne toten Link `./kanzlei-cowork`; `testakten/README.md` mit allen 46 Akten (vorher 44), inkl. zwei neuer Tabellen-Zeilen und ZIP-Eintraege fuer `dsa-dma-bayrische-baustube-meissner` und `sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`.

### Repo-Stand v12.0.0

- 98 Plugins, alle plugin.json einheitlich auf 12.0.0
- marketplace.json mit 98 Eintraegen, alle 12.0.0
- 46 Testakten
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII); Validator-Script `validate-plugin-structure.mjs` clean.

## v11.0.0 — 2026-05-26 — DSA/DMA-Plugin, BetrVG-Heilung, qES-Befristung, KI-Sachverstaendige, Kanzlei-Cowork-Fusion

### Major-Feature: Plugin "dsa-dma-digitalregulierung"

Neues Plugin Nr. 99: **DSA und DMA und Digitalregulierung EU**. 9 Skills:

- `digitalregulierung-pyramide-check` — Einstiegsskill, ordnet Sachverhalte den passenden Rechtsakten zu (DSA DMA Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO § 19a GWB)
- `dsa-vlop-vlose-einordnung-und-pflichten` — Schwellenwert 45 Mio. EU-Nutzer, Designation, Pflichtenkatalog Art. 34-43
- `dma-gatekeeper-schwellen-und-kernplattformdienste` — drei kumulative Voraussetzungen, quantitative Vermutungen, KPD-Katalog, Pflichten Art. 5-7
- `dsa-art-34-systemische-risikobewertung` — vier Risikoarten, Methodik, Audit Art. 37
- `dsa-art-40-forschungsdatenzugang-algorithmen` — drei Zugangsregime, vetted researchers, Delegierte VO 2024/2987
- `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` — Stufenmodell Art. 17 / 20 / 21, BGH III ZR 179/20 und III ZR 192/20, Eilrechtsschutz
- `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` — Mehr-Anker-Strategie
- `zustellung-und-vertreter-art-13-dsa-art-37-dma` — Praxis Zustellung gegen Auslands-Plattformen
- `klage-gegen-vlop-einordnung-art-263-aeuv` — Nichtigkeitsklage zum EuG, Frist 2 Monate

### Testakte (neu)

- **`testakten/dsa-dma-bayrische-baustube-meissner/`** — fragmentarische Akte mit 17 Dokumenten verschiedener Formate (.md, .csv, .eml). Mandantin Baustube Meissnerlein GmbH, Hoechstadt an der Aisch. Konstellation: Account-Sperre auf US-Plattform "Glitzerwald", parallel VLOP-Designations-Streit, Mitbewerber Lindheim & Soehne KG Schwabach mit Verdacht auf Self-Preferencing, Art.-40-DSA-Forschungsantrag Dr. Vogelbroich (FAU Erlangen), Zustellungsproblem Art. 13 DSA EU-Vertreter Dublin.
- **`testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/`** — fragmentarische Akte mit 15 Dokumenten zum KI-Vorwurf bei Sachverstaendigengutachten (PV-Anlage Werkmangel, Sachverstaendiger Pfaffenberger). Anbindung an LG-Darmstadt-Linie (§ 407a Abs. 1 ZPO; § 8a Abs. 2 S. 1 Nr. 1 und Nr. 2 JVEG).

### BetrVG-Heilung und Ersatzmitglieder

Neue Skills in `arbeitsrecht` und `fachanwalt-arbeitsrecht`:

- `betriebsrat-ladung-und-ersatzmitglieder-pruefen` (arbeitsrecht)
- `betriebsrat-beschluss-heilung-nachtraeglich` (arbeitsrecht)
- `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` (fachanwalt-arbeitsrecht)

Eingearbeitet: BAG 25.09.2024 — 7 ABR 37/23 (Heilung Betriebsratsbeschluss; Vorinstanz LAG Nuernberg 27.09.2023 — 2 TaBV 8/23), BAG 20.05.2025 — 1 AZR 35/24 (Nachladung Ersatzmitglied).

### Schriftform und qES — Befristung

Neuer Skill in `schriftform-und-textform-bgb`:

- `befristungsabrede-qes-rechtsprechung-stand-2026` — LAG Berlin-Brandenburg 16.03.2022 — 23 Sa 1133/21 (gescannte Unterschrift wahrt § 14 IV TzBfG nicht), ArbG Berlin (einfache elektronische Signatur unwirksam), ArbG Gera 07.03.2024 — 2 Ca 936/23 (qES per DocuSign wahrt Schriftform).

### Maklerskill BGH I ZR 202/25 — voll ueberarbeitet

`maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` komplett neu geschrieben mit 4 verifizierten Leitsaetzen: E-Mail-Austausch erfuellt Textform auch auf getrennten Datentraegern; konkludenter Abschluss moeglich; Erklaerungsende muss erkennbar sein; Bereicherungsanspruch des Maklers gesperrt bei Textformverstoss. Falsche Lehrsaetze der Vorversion ersetzt.

### KI-Vorwurf bei Sachverstaendigengutachten

Drei neue Skills mit verschiedener Perspektive auf die LG-Darmstadt-Linie:

- `kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` (Anwalts-Generalist)
- `grosskanzlei-corporate-ma/skills/ki-einsatz-bei-gutachten-mandatsseite` (Beratungsseite)
- `jveg-kostenpruefer/skills/pruefung-sachverstaendigengutachten-ki-deklaration` (Kostenpruefer, festsetzungs-orientiert)

### Plugin-Fusion: kanzlei-allgemein in kanzlei-allgemein

Das Plugin `kanzlei-allgemein` wurde vollstaendig in `kanzlei-allgemein` fusioniert. Alle 14 Cowork-Skills sind erhalten und werden ab v11.0.0 unter `kanzlei-allgemein/skills/` ausgeliefert: `aktenbestand-pflege`, `bea-versand-pruefen`, `fristenbuch-fuehren`, `geburtstage-feiertage`, `kanzlei-allgemein-kaltstart-interview`, `mahnwesen-honorar`, `mandantenakte-anlegen`, `mandantenbrief-vorlagen`, `posteingang-ausgang`, `rechnungserstellung-rvg` (inkl. Werkzeug `rvg_gebuehrenrechner.py`), `sekretariats-tagesbrief`, `timesheet-aktenzeitung`, `versand-vor-check`, `weihnachtskarten`. Das Stand-Alone-Plugin `kanzlei-allgemein` ist entfallen.

### Repo-Stand v11.0.0

- 98 Plugins (99 minus Cowork-Fusion plus DSA/DMA)
- marketplace.json mit 98 Eintraegen, alle auf 11.0.0
- 98 plugin.json-Dateien einheitlich auf 11.0.0
- 45 Testakten (vorher 43 plus 2 neu)
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII)

### QA-Vorlauf (Commit `69f627c0`)

- Aktenzeichen-Korrekturen in 14 Dateien: II ZR 88/13 → II ZR 88/99; IX ZR 92/04 → IX ZR 228/03; 3 AZR 18/12 → 3 AZR 303/18

# Changelog

Alle wesentlichen Änderungen an diesem Repository werden hier dokumentiert. Format orientiert an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/), Versionierung nach [SemVer](https://semver.org/lang/de/).

## v8.0.0 — 2026-05-25 — Steuer-Plugin Härtung + Codex-Audit-Welle

### Major-Update
- Versionsfelder repo-weit auf 8.0.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

### Steuer-Plugin Erweiterung (PR #70, #71)
- Neuer Skill **`anw-insolvenzreife-pruefung-17-19-inso`** (210 Zeilen): §§ 17, 19 InsO aus Steueranwalts-Sicht mit § 222 AO Stundung, § 361 AO AdV, § 69 AO GF-Haftung Lohnsteuer, § 266a StGB, BGH IX ZB 50/03, IDW S 11, SanInsKG 24-Monats-Prognose.
- **`stb-warnschreiben-krisensignale`** um Abschnitt „Warum gerade der Steuerberater“ und „§ 102 StaRUG als Auslöser der StB-Hinweispflicht“ erweitert — Steuerberater als externer Bestandteil des Krisenfrüherkennungssystems.
- **Generalueberholung mit sechs neuen Skills**: `anw-stundung-erlass-vollstreckungsaufschub`, `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern`, `anw-organschaft-konzern-grundlagen`, `anw-grunderwerbsteuer-share-deal-90-prozent`, `anw-dac7-dac8-plattformen-krypto`, `anw-minbestg-pillar2-konzernbesteuerung`, `stb-drv-sozialversicherungspruefung`.

### Juristische Korrekturen (Codex-Audit-Welle PR #72–#76)
- **§ 361 AO AdV ist keine Stundung** (PR #72, #74): AdV hemmt nur die Vollziehung, lässt die Fälligkeit unberührt. AdV-Beträge bleiben Passiva I bei der § 17 InsO-Prüfung. Nur die echte Stundung nach § 222 AO verschiebt die Fälligkeit. Korrektur in `anw-insolvenzreife-pruefung-17-19-inso` und 5 weiteren Liquiditätsprüfer-Skills (`insolvenzrecht/zahlungsunfaehigkeit-pruefung-17-inso`, `insolvenzrecht/liquiditaetsvorschau-insolvenzrechtlich`, `liquiditaetsplanung/liquiditaetsvorschau-3wochen`, `liquiditaetsplanung/liquiditaetsvorschau-insolvenzrechtlich`, `steuerrecht-anwalt-und-berater/stb-liquiditaetsvorschau-3wochen`).
- **§ 393 Abs. 2 AO Verwendungsverbot nur für steuerfremde Straftaten** (PR #73): Korrigiert in `anw-steuerstrafverteidigung-verstaendigung`. Für die Steuerstraftat selbst sind Steuerakten verwertbar (BGH 5 StR 191/04; Joecks/Jaeger/Randt, Steuerstrafrecht, 8. Aufl. 2015, § 393 Rn. 81 ff.). § 30 AO schafft kein Verwendungsverbot. § 136a StPO als realer Verteidigungsansatz ergänzt.
- **§ 393 Abs. 1 S. 2 AO nur Zwangsmittelverbot** (PR #75): Präzisiert in `anw-steuerstrafverteidigung-verstaendigung`. Setzt die steuerlichen Mitwirkungspflichten **nicht** generell außer Kraft, sondern verbietet nur den Einsatz von Zwangsmitteln (§ 328 AO) soweit Selbstbelastungsgefahr. §§ 90, 93, 200 AO bestehen fort; Schätzung § 162 AO und Steuererklärungspflicht bleiben.
- **GrESt-Konzernklausel ist § 6a GrEStG** (PR #76): Korrigiert in `anw-grunderwerbsteuer-share-deal-90-prozent` zweifach. § 6a GrEStG begünstigt Umwandlung/Einbringung im Konzern (95 % Beteiligung, 5 Jahre Vor- und Nachbehaltensfrist). § 7 GrEStG regelt dagegen den Übergang von Gesamthand zu Bruchteilseigentum.
- **GIR-Erstabgabe 18 Monate** (PR #76): Korrigiert in `anw-minbestg-pillar2-konzernbesteuerung`. Übergangsregelung nach § 95 Abs. 1 MinStG i.V.m. Art. 44 Abs. 7 EU-RL 2022/2523. Kalenderjahrgleicher Konzern GJ 2024 → Frist 30.6.2026. Folgejahre weiter 15 Monate.

### Tooling und Cleanup (PR #77, #78)
- ASSET_INDEX.md auf Stand v8.0.0 angehoben, Plugin-Counts repo-weit konsistent: 97 Plugins / 43 Fallakten / 1 Manifest = 141 Release-Assets.
- Repo-Sanity-Sweep durchgeführt: Validator, Marketplace, Skill-Struktur (1.643 Skills), Symlinks, README-Referenzen — alle Prüfungen OK.

## v7.1.0 — 2026-05-24 — Steuer-Plugin-Konsolidierung + ELSTER-Klarstellung

### Major-Feature
- Drei Steuer-Plugins (`steuerrecht-kanzlei`, `fachanwalt-steuerrecht`, `steuerberater-werkzeuge`) zu einem konsolidierten Plugin **`steuerrecht-anwalt-und-berater`** zusammengeführt. 18 Skills mit Präfix-Schema `anw-`/`fa-`/`stb-`: 13× Steueranwalt (Kaltstart-Interview, Mandat-Triage, Steuerbescheid-Analyse, Einspruch ans Finanzamt, AdV, Klage Finanzgericht, Akteneinsicht, Außenprüfung, Selbstanzeige § 371 AO, verbindliche Auskunft § 89 II AO, Fristenbuch, Betriebsausgaben/Werbungskosten-Prüfraster, USt-Vorsteuerabzug), 1× FA-Orientierung, 4× Steuerberater (Kaltstart-Interview, BWA/SuSa/Bilanz, 3-Wochen-Liquiditätsvorschau, 3-/6-/12-Monats-Vorschau). Vier inhaltliche Dubletten (Einspruch, Außenprüfung, Selbstanzeige, verbindliche Auskunft) zu jeweils einem Master-Skill gemergt. Repo-Plugin-Anzahl: 99 → 97.

### Juristische Korrekturen
- **ELSTER/ERiC statt beA an Finanzämter** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Versandwege in Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige und verbindlicher Auskunft umgestellt. beA an Finanzbehörden ist unzulässig — ein per beA eingelegter Einspruch wäre formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenüber Finanzgerichten (§ 52d FGO).
- **Triage-Routing-Slugs** im konsolidierten Plugin auf die neuen Skill-Slugs umgestellt; **ASSET_INDEX**-Dubletten bereinigt; **`stb-`-Sister-Skill-Verweise** auf die konsolidierten Pfade aktualisiert.

### Tooling
- Versionsfelder repo-weit auf 7.1.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

## v7.0.0 — 2026-05-24 — Reform-Stand 2026

### Major-Update
- Versionsfelder repo-weit auf 7.0.0 vereinheitlicht: 99 `plugin.json`-Dateien (je ein `version`-Feld) plus eine zentrale `.claude-plugin/marketplace.json`, die ihrerseits 99 Plugin-Einträge mit `version`-Feld enthält. Summe: 99 + 1 Manifest-Datei mit 99 internen Versions-Einträgen = 198 angefasste Versions-Stellen in 100 Dateien.

### Inhaltliche Aktualisierungen
- **Wandeldarlehen-Plugin** auf Reform-Stand 05/2026 angehoben (DiRUG 2022/2023, SanInsFoG 1.1.2021, PostModG 1.1.2025, GesLV, Transparenzregister).
- **Steuerrecht** aktualisiert: WtcG-Gebühren, eRechnung-Pflicht ab 1.1.2025 (§ 14 UStG), § 153 AO; Selbstanzeige-Dublette entfernt; § 398a AO Zuschlagsstaffel ergänzt.
- **liquiditaetsplanung**: openpyxl-Dependency komplett entfernt; Kanzleien starten `build_liquiditaetsplan.py` ohne `pip install` (Stdlib-XLSX-Writer mit Live-Formeln, Styles, DXF-Solid-Fills, Conditional Formatting, Freeze Panes).

### Juristische Korrekturen
- **ELSTER/ERiC statt beA gegenueber Finanzbehoerden** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Im neuen konsolidierten Steuer-Plugin alle Stellen umgestellt, an denen Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige oder verbindliche Auskunft per beA an das Finanzamt empfohlen wurden. beA an Finanzbehoerden ist unzulaessig; ein per beA eingelegter Einspruch ist formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenueber Finanzgerichten (§ 52d FGO).
- **§ 44 DSGVO → § 44 BDSG i.V.m. Art. 79 DSGVO**: Vier Arbeitsrechts-Skills zitierten eine nicht existierende DSGVO-Norm. Die DSGVO hat nur Artikel; § 44 BDSG ist die deutsche Norm für die Gerichtszuständigkeit. Vier weitere DSGVO-Verweise (Art. 8, 13, 34, 37 DSGVO) von `§` auf `Art.` umgestellt.
- **kongruent (lat. *congruens*)**: Phase-2-Umlauten-Patch hatte den etablierten Fachbegriff "kongruente / inkongruente Deckung" (§ 130/131 InsO) fälschlich umlautiert. 17 Dateien, 67 Korrekturen.
- **§ 57 II GmbHG statt § 19 GmbHG**: Codex-Befund — falscher Normverweis in `sacheinlagebericht-werthaltigkeit` (Wandeldarlehen-Plugin) korrigiert; § 57 II GmbHG i.V.m. § 8 II GmbHG ist die korrekte Anker-Norm für die GF-Versicherung in der HR-Anmeldung der Kapitalerhöhung.
- **§ 153 AO ist Berichtigungspflicht — KEINE Strafbefreiung**: Codex-P1-Review von PR #60. In `anw-selbstanzeige-371` stand fälschlich, § 153 AO wirke strafbefreiend. Korrekt: § 153 AO ist eine rein steuerliche Berichtigungspflicht ohne strafrechtliche Sperrwirkung; Strafbefreiung folgt allein aus § 371 AO (Vorsatz) bzw. § 378 III AO (Leichtfertigkeit). Drei-Stufen-Bewertung der Ursprungserklärung ergänzt; Praxisempfehlung: bei Zweifeln zusätzlich Selbstanzeige-Weg erfüllen.
- **Stale Skill-Slug-Verweise** behoben: `datenpannenmeldung → datenpanne-meldung`, `auskunftsersuchen-art-15-dsgvo → dsgvo-auskunft`.

### Repo-Polish
- Umlauten-Polish in SKILL.md-Bodies und references/ (531 Dateien, 5017 Korrekturen); YAML-Frontmatter, Eigennamen, Slugs, URLs, Code-Blocks geschützt.
- Skill-Slugs (Verzeichnisnamen) bleiben ASCII; nur Fließtext umlautiert.
- README-Intro klargestellt: Plugin- und Skill-Sammlung; Beck-Verweise entfernt.
- Testakten-Hinweis im Überblick prominent platziert.

### Tooling
- `release-plugin-zips.yml` triggert automatisch auf Tag-Push; pro Release werden 99 Plugin-ZIPs (aus `.claude-plugin/marketplace.json`) plus 43 Testakten-ZIPs (mit `testakte-`-Prefix, separat aus `testakten/*/` verpackt) plus `marketplace.json` als Manifest erzeugt — zusammen 143 Release-Assets.
- Validator (`scripts/validate-plugin-structure.mjs`) bleibt grün.

# Halluzinations-Audit — Master-Summary

**Audit-Datum:** 27.05.2026
**Gepruefte AZ (unique):** 3228
**Quelle:** Alle SKILL.md im claude-fuer-deutsches-recht Repo

## Gesamtverteilung

| Status | Anzahl | Anteil |
|---|---|---|
| OK | 1062 | 32.9% |
| UNVERIFIABLE | 893 | 27.7% |
| WRONG_TOPIC | 621 | 19.2% |
| NOT_FOUND | 355 | 11.0% |
| ? | 294 | 9.1% |
| WRONG_AZ | 3 | 0.1% |

**Halluzinations-Quote (WRONG_TOPIC + NOT_FOUND):** 976 von 3228 = 30.2%

## Chunk-Uebersicht

| Chunk | Gesamt | OK | WRONG | NOT_FND | UNVERIF |
|---|---|---|---|---|---|
| 00 | 147 | 56 | 32 | 9 | 50 |
| 01 | 147 | 52 | 24 | 39 | 32 |
| 02 | 147 | 96 | 19 | 1 | 31 |
| 03 | 147 | 93 | 23 | 7 | 24 |
| 04 | 147 | 0 | 0 | 0 | 0 |
| 05 | 147 | 0 | 0 | 0 | 0 |
| 06 | 147 | 15 | 72 | 2 | 58 |
| 07 | 147 | 22 | 72 | 50 | 3 |
| 08 | 147 | 61 | 24 | 12 | 50 |
| 09 | 147 | 17 | 18 | 40 | 72 |
| 10 | 147 | 97 | 11 | 0 | 39 |
| 11 | 147 | 7 | 43 | 11 | 86 |
| 12 | 147 | 22 | 51 | 35 | 39 |
| 13 | 147 | 37 | 54 | 8 | 48 |
| 14 | 147 | 56 | 43 | 6 | 42 |
| 15 | 147 | 14 | 42 | 68 | 23 |
| 16 | 147 | 69 | 14 | 62 | 2 |
| 17 | 147 | 93 | 14 | 3 | 37 |
| 18 | 147 | 91 | 3 | 3 | 50 |
| 19 | 147 | 118 | 22 | 0 | 7 |
| 20 | 147 | 37 | 37 | 0 | 73 |
| 21 | 141 | 9 | 3 | 2 | 127 |

## Wichtigste zu fixende AZ (Top 50 WRONG_TOPIC + NOT_FOUND)

| Gericht | AZ | Status | Behauptet | Real | Quelle |
|---|---|---|---|---|---|
| EuGH | C-203/22 | WRONG_TOPIC | Urt. v. 04.10.2024 (falsch), NJW 2025, 56 (falsch) — Betreib | Dun & Bradstreet Austria: DSGVO Art. 15 Auskunftsrecht über  | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZB 32/21 | NOT_FOUND | Insolvenzplan-Architektur, Urt. 21.04.2022, NZI 2022, 612 | AZ existiert nicht nachweisbar; nächste ähnliche AZ: IX ZB 6 | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=IX |
| BGH | VI ZR 184/17 | NOT_FOUND | Urt. v. 19.06.2018, NJW 2018, 2877, Organisationspflichten b | BGH VI ZR 184/17 existiert nicht. NJW 2018, 2877 = BGH VI ZR | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=VI |
| BGH | IX ZR 238/17 | WRONG_TOPIC | InsO Cramdown § 245: Best-Interest-Test, Liquidationsverglei | Eigenverwaltung: Haftung des vertretungsberechtigten Geschäf | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZB 75/14 | WRONG_TOPIC | Vollstreckungsschutz § 21 InsO analog vor Schutzschirmbeschl | Insolvenzplan-Vorprüfungsverfahren, Gruppenbildung § 222 Ins | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | I ZR 202/25 | NOT_FOUND | § 656a BGB: spezialgesetzliche Schutzzwecke schließen Treuwi | AZ noch nicht entschieden (2025-Sache); keine bestätigte Ent | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=I+ |
| BGH | IX ZR 222/18 | WRONG_TOPIC | Ersteinrichtung der Beratungsstellenorganisation als Grundla | Anwaltsdienstvertrag, Kündigung aus wichtigem Grund, Urt. 07 | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=IX |
| BGH | IX ZR 188/15 | WRONG_TOPIC | Feststellungsklage § 180 InsO: Klagefrist ab Bestreiten im P | Insolvenzanfechtung: Gläubigerbenachteiligungsvorsatz, Urt.  | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 173/04 | WRONG_TOPIC | Ausschluss eines GmbH-Gesellschafters aus wichtigem Grund an | Hinauskündigung: Zeitliche Beschränkung der Managerbeteiligu | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZR 178/08 | NOT_FOUND | Sachwalter-Pflichten § 274 InsO: Sachwalter muss Eigenverwal | BGH IX ZR 178/08 vom 08.10.2009 nicht in dejure-Datenbank ge | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 277/16 | WRONG_TOPIC | Urt. 19.06.2018 — Zahlungsunfähigkeit bei > 10% Deckungslück | BGH II ZR 277/16 nicht bestätigt; BGHZ 217, 129 = BGH II ZR  | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=II |
| BGH | IX ZR 143/20 | WRONG_TOPIC | Urt. 15.04.2021, NJW 2021, 1740 — Anwalt muss Ergebnis autom | Anwaltsgebühren: Testamentsentwurf als Beratung (nicht Gesch | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZR 64/12 | WRONG_TOPIC | Skill-Beschreibung: Steuerberater-Warnschreiben-Vorlage (kei | Steuerberaterhaftung bei allgemeinem Steuerberatungsmandat:  | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BAG | 7 ABR 37/23 | WRONG_TOPIC | Skill-Beschreibung: Betriebsratsbeschluss-Mängel-Prüfung (§  | Freistellung des Betriebsrats von Rechtsanwaltskosten, rückw | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | VIII ZR 32/00 | WRONG_TOPIC | DD-Ergebnis muss vollständig in Beratungsleistung einfließen | Aufklärungspflicht beim Unternehmenskauf/GmbH-Anteilskauf, a | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=NJ |
| BGH | III ZR 329/16 | WRONG_TOPIC | Beschl. v. 11.09.2018 (falsches Datum!) — erforderliche Zeit | Nichtzulassungsbeschwerde: Beschwer-Bemessung, Streitwert, F | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=II |
| BGH | IV ZR 163/17 | WRONG_TOPIC | Beschl. v. 26.09.2018 — Festsetzungsbeschlüsse nach § 4 JVEG | Betriebsrentenkürzung/Versorgungsausgleich nach Scheidung un | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZR 221/18 | WRONG_TOPIC | Urt. 07.03.2019, NJW 2019, 2020 — Prüfberichte müssen hinrei | Anwaltsvertrag: Kündigung, nachgeschobene Gründe, Vergütungs | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 391/18 | WRONG_TOPIC | Due-Diligence-Prüfungen müssen sorgfältig durchgeführt werde | GmbH-Gesellschafterausschluss/Einziehung: Legitimationswirku | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 256/08 | NOT_FOUND | Urt. v. 27.09.2010 — Kontrollwechsel-Klausel in Gesellschaft | BGH II ZR 256/08 — kein Eintrag in dejure-Datenbank; AZ exis | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=II |
| BGH | IX ZR 133/14 | WRONG_TOPIC | Urt. v. 21.07.2008 (falsch!) — BGHZ 198, 64 Rn. 16: Wandlung | Qualifizierte Rangrücktrittsvereinbarung: Durchsetzungssperr | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=IX |
| BGH | II ZR 234/20 | WRONG_TOPIC | Urt. 04.05.2021, NJW 2022, 1381 Rn. 22 — GF muss Entscheidun | Berichtigung eines zivilgerichtlichen Urteils wegen Schreibf | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=II |
| BGH | IV ZR 219/14 | NOT_FOUND | Urt. 23.06.2015 — Transparenzgebot AVB; Risikoausschluss mus | BGH IV ZR 219/14 — kein Eintrag in dejure-Datenbank; AZ exis | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=IV |
| BAG | 7 AZR 1048/06 | WRONG_TOPIC | Bei starkem Schriftformmangel-Fall (elektronische Signatur)  | Befristungsrecht TzBfG: Schriftform, Vorbeschäftigungsverbot | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=7+ |
| BGH | I ZR 75/14 | WRONG_TOPIC | 2. BGH, Urt. v. 11.06.2015 – I ZR 75/14, GRUR 2016, 176 Rn.  | Tauschbörse III (Filesharing), Urt. 11.06.2015, GRUR 2016, 1 | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| EuGH | C-168/18 | WRONG_TOPIC | - EuGH C-168/18 (Bauer/Willmeroth) — Unverfallbarkeit als Gr | EuGH C-168/18: bAV Insolvenzschutz (PSV/Pensionskasse), Urt. | https://curia.europa.eu/juris/liste.jsf?num=C-168/18 |
| BGH | I ZR 82/17 | NOT_FOUND | - BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Anl | Nicht auffindbar in dejure.org; kein BGH I ZR 82/17 mit Datu | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | VII ZR 244/12 | NOT_FOUND | / BGH / VII ZR 244/12 / 25.09.2014 / Beweislastumkehr nach A | Nicht in dejure.org auffindbar; kein BGH VII ZR 244/12 mit D | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 171/06 | WRONG_TOPIC | - BGH, Urt. v. 11.02.2008 - II ZR 171/06, NJW 2008, 1589 Rn. | BGH II ZR 171/06, Urt. 11.02.2008: Verjährung von Einlagefor | https://dejure.org/2008,187 |
| BGH | I ZR 187/12 | NOT_FOUND | / BGH I ZR 187/12 / BGH, 13.09.2018 / Lizenzbetrag für einfa | Nicht in dejure auffindbar; BGH I ZR 187/12 mit Datum 13.09. | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | II ZR 175/95 | WRONG_TOPIC | - BGH, Urt. v. 21.04.1997 - II ZR 175/95, BGHZ 135, 244 — Bu | BGH II ZR 175/95, Urt. 21.04.1997, BGHZ 135, 244: Aufsichtsr | https://dejure.org/1997,161 |
| BSG | 12 KR 13/14 | WRONG_TOPIC | > BSG, Urt. v. 11.11.2015 – B 12 KR 13/14 R: Schuldrechtlich | BSG B 12 KR 13/14 R, Urt. 11.11.2015, BSGE 120, 59: Statusfe | https://dejure.org/2015,32875 |
| BAG | 1 ABR 22/21 | WRONG_TOPIC | description: "Arbeitnehmer klagt auf Mindestlohn oder Uebers | BAG 1 ABR 22/21, Beschl. 13.09.2022: Initiativrecht des Betr | https://www.bundesarbeitsgericht.de/entscheidung/1-abr-22-21 |
| BGH | VI ZR 207/21 | WRONG_TOPIC | - BGH, Urt. v. 14.07.2022 - VI ZR 207/21, NJW 2022, 3215 — S | BGH VI ZR 207/21 nicht in dejure; V ZR 207/21 (WEG Beschluss | https://dejure.org/2022,22528 |
| EuGH | C-398/08 | WRONG_TOPIC | description: "Slogan-Marken fuer Luxus-Mode auf Eintragbarke | EuGH C-398/08 P (Audi/HABM), Urt. 21.01.2010: Eintragbarkeit | https://dejure.org/2010,20 |
| BGH | VIII ZR 304/21 | WRONG_TOPIC | - BGH, Urt. v. 14.12.2022 — VIII ZR 304/21, NJW 2023, 1289 R | BGH VIII ZR 304/21, Urt. 27.04.2022, BGHZ 233, 215, NJW 2022 | https://dejure.org/2022,12700 |
| BGH | VIII ZR 317/21 | WRONG_TOPIC | - BGH, Urt. v. 13.07.2022 – Az. VIII ZR 317/21, NJW 2022, 27 | BGH VIII ZR 317/21, Urt. 13.07.2022, NJW 2022, 2830: Eintrit | https://dejure.org/2022,21658 |
| BGH | I ZR 184/17 | WRONG_TOPIC | - BGH, Urt. v. 07.03.2019 – I ZR 184/17, GRUR 2019, 748 Rn.  | BGH I ZR 184/17, Urt. 07.03.2019, GRUR 2019, 746: Energieeff | https://dejure.org/2019,12159 |
| BGH | I ZR 228/15 | WRONG_TOPIC | Leiturteil: BGH, Urt. v. 27.07.2017 – I ZR 228/15, GRUR 2018 | BGH I ZR 228/15, Urt. 27.07.2017, GRUR 2017, 1027: Reformist | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht |
| BGH | IX ZR 49/10 | WRONG_TOPIC | - BGH, Urt. v. 10.02.2011 – IX ZR 49/10, NJW 2011, 1594 Rn.  | BGH IX ZR 49/10, Urt. 10.02.2011, BGHZ 188, 317: Phoenix — A | https://dejure.org/2011,436 |
| BGH | V ZR 69/21 | WRONG_TOPIC | - BGH, Urt. v. 16.09.2022 — V ZR 69/21, BGHZ 234, 252 Rn. 25 | BGH V ZR 69/21, Urt. 16.09.2022: Verteilung des Selbstbehalt | https://dejure.org/2022,24507 |
| BGH | VII ZR 206/06 | WRONG_TOPIC |  |  |  |
| BGH | XII ZR 13/13 | NOT_FOUND |  |  |  |
| BSG | 12 R 11/18 | WRONG_TOPIC |  |  |  |
| OLG Frankfurt | 26 U 35/19 | NOT_FOUND |  |  |  |
| BFH | I R 40/17 | WRONG_TOPIC |  |  |  |
| BGH | II ZR 14/09 | NOT_FOUND |  |  |  |
| BGH | II ZR 4/21 | NOT_FOUND |  |  |  |
| BGH | IV ZR 81/19 | NOT_FOUND |  |  |  |
| BGH | IX ZR 145/20 | NOT_FOUND |  |  |  |

_(Vollstaendige Liste: 976 Problemfaelle in audit_problems_2026-05-27.json)_
---

## Welle 3 — Reparatur abgeschlossen (Commit 8b7d9b88, Tag v14.2.5)

### Statistik

- **Reparierte Skills:** 320
- **Bearbeitete AZ-Probleme:** 528 (= alle in dieser Welle adressierten Befunde)
- **Geänderte Dateien:** 321 SKILL.md
- **Subagenten-Aufteilung:** 88 spezialisierte Reparatur-Tasks
  - 8 Big-Solo-Tasks (≥5 Probleme je Skill)
  - 22 Medium-Solo-Tasks (3-4 Probleme je Skill)
  - 58 Bundles à je 5 Skills (≤2 Probleme je Skill)

### Korrekturmuster (qualitative Verteilung aus Subagenten-Berichten)

- **Ersatzlose Löschung** war häufigster Pfad — bei NOT_FOUND-AZ ohne sichere Ersatzentscheidung
- **Ersatz durch verifizierte Leitentscheidung** mit identischem Tenor — wo dejure.org einen sauberen Treffer lieferte
- **Beschreibungskorrektur bei vorhandenem AZ** — wenn AZ existiert, aber Skill-Text das falsche Urteil beschrieb (häufig bei WRONG_TOPIC mit vertauschter NJW-Fundstelle)
- **Senatswechsel-Fälle** — z.B. D&O-Versicherungsfragen aus dem VI. (Deliktssenat) in den IV. Zivilsenat verschoben
- **Cross-Reference-Fehler** — NJW-Fundstelle gehörte zu anderem AZ; korrigiert auf echte Fundstelle

### Häufig betroffene Senate (aus den Berichten)

- BGH VI ZR / VII ZR / VIII ZR / IX ZR — überproportional viele NOT_FOUND
- BAG 6/7/8 AZR — mehrfach falsche Senatszuordnung
- BSG B 12 KR / B 12 R — vertauschte Themen Statusfeststellung vs. Phantomlohn
- EuGH-Aktenzeichen meist real, aber WRONG_TOPIC bei Themenzuordnung

### Qualitätsicherung

- `node scripts/validate-plugin-structure.mjs` → `validate-plugin-structure OK`
- Komma-Sweep in `description` (`\d\s*,\s*\d`) → 0 Treffer
- Cyrillic-Sweep `[\x{0400}-\x{04FF}]` → 0 Treffer
- Frontmatter aller 320 Skills unverändert
- Jeder Skill trägt Audit-Hinweis-Block (HTML-Kommentar oder `## Audit-Hinweis (27.05.2026)`)

### Verbleibende Befunde

Welle 3 hat die 528 vorgesehenen AZ-Probleme abgearbeitet. Die in `audit_problems_2026-05-27.json` enthaltenen 976 Gesamt-Problemfälle umfassen darüber hinaus weitere Befunde mit niedrigerer Schwere bzw. solche aus Plugins, die erst in späterer Welle 4 angefasst werden — namentlich die 156 neuen Selbstvertreter-Skills (`selbstvertreter-amtsgericht`, `selbstvertreter-sozialgericht`) aus PR #115.

---

## Welle 4 — Selbstvertreter-Skills (Commit 9af66be8, Tag v14.2.6)

Audit-Folge fuer die 156 Selbstvertreter-Skills aus PR #115, die im ersten Audit-Lauf nicht enthalten waren.

### Statistik

- **Gepruefte Skills:** 156 (selbstvertreter-amtsgericht: 81, selbstvertreter-sozialgericht: 75)
- **Gefundene echte Aktenzeichen:** 6 (die Skills arbeiten ueberwiegend laien-prozedural mit Paragraphen statt Urteilen)
- **Verifikation per dejure.org:** alle 6 AZ einzeln gegengeprueft

### Befund

| AZ | Status | Maßnahme |
|---|---|---|
| BVerfG 1 BvL 1/09 (09.02.2010, Regelleistungen) | OK | unveraendert |
| BVerfG 1 BvL 7/16 (05.11.2019, Hartz-IV-Sanktionen) | OK | unveraendert |
| BVerfG 1 BvR 569/05 (12.05.2005, PKH-Anforderungen) | OK | unveraendert |
| BSG B 1 KR 7/05 R (04.04.2006, Nikolausbeschluss-Anwendung) | OK | unveraendert |
| BVerfG 1 BvR 2310/14 (vermeintl. 05.11.2014) | **NOT_FOUND** | AZ entfernt, allgemeine BVerfG-Linie erhalten |
| BGH VI ZR 67/15 (vermeintl. NJW 2016, 1305, Bote/Drittversand) | **WRONG_TOPIC** | echtes Thema: Arzthaftung/Behandlungsfehler, NJW 2016, 713 - AZ und falsche Fundstelle entfernt |

### Halluzinationsquote (Welle 4)

2 von 6 echten AZ fehlerhaft = 33% — vergleichbar mit der Gesamtquote von 30,2% aus dem Audit-Lauf 27.05.2026.

### Betroffene Datei

`selbstvertreter-amtsgericht/skills/zurechnungsproblem-versand-durch-dritte/SKILL.md` — beide Probleme in derselben Datei, in der Sektion "Rechtsgrundlagen".

### Qualitaetsicherung Welle 4

- `node scripts/validate-plugin-structure.mjs` -> `validate-plugin-structure OK`
- Komma-Sweep in `description` -> 0 Treffer
- Cyrillic-Sweep -> 0 Treffer
- Audit-Hinweis-Block im betroffenen Skill ergaenzt

---

## Welle 5 - Codex-Vorbereitung fuer v16.0.0

Arbeitsstand: 27.05.2026 auf Branch `codex/halluzinations-global-cleanup`, nach Sync mit `origin/main` bei `246a72e2` / `v15.0.0`.

### Zielsetzung

- Resttreffer aus Welle 3/4 in produktiven Skills entfernen oder auf belastbare Fundstellen umstellen
- Release-Vorbereitung fuer `v16.0.0`
- Audit-Dateien duerfen die alten Problemstellen weiterhin als Befundhistorie enthalten

### Korrekturmuster

- falsche `EuGH C-203/22`-Altzuordnung in KI-Governance- und KI-VO-Skills durch DSGVO-Art.-15-Kontext ersetzt
- `BGH VI ZR 184/17`, `BGH IX ZR 238/17`, `BGH IX ZB 32/21` und `BGH IX ZR 18/19` aus Insolvenzplan-/StaRUG-Skills entfernt, soweit keine sichere Ersatzfundstelle vorlag
- falsche `BGH II ZR 234/18`-/`BGH II ZR 199/19`-Zuordnungen in Insolvenz- und D&O-Skills ersetzt
- Squeeze-out-Skill von falschem `II ZR 234/18` auf DAT/Altana und Stollwerck umgestellt
- Marketplace und alle Plugin-Manifeste auf `16.0.0` angehoben

# CLAUDE.md – Repository-Leitfaden für das Modell

Dieses Repository enthält die Vergaberecht-Werkstatt: drei Plugins für die wichtigsten Marktrollen des deutschen und europäischen Vergaberechts.

- `vergabestelle-behoerden`: Plugin für öffentliche Auftraggeber (Bund, Länder, Kommunen, Sektorenauftraggeber, öffentlich-rechtliche Anstalten). Skills für Vergabevorbereitung, Verfahrensart-Wahl, Bekanntmachung, GAEB/XML/Excel/PDF-Unterlagen, eForms/TED/DVAL, Upload-Routing, Eignungs- und Zuschlagskriterien, Wertung, Zuschlag, Aufhebung, Nachprüfung.
- `bieter-unternehmen`: Plugin für Unternehmen als Bieter oder Bewerber sowie Kanzleien auf Bieter-/Bewerberseite. Skills für Markterkundung, Unterlagen- und LV-Auswertung, GAEB/XML/Excel/PDF-Angebotspakete, formgerechte Portalabgabe, Eignungsnachweise, Angebotskalkulation, Bietergemeinschaft, Nebenangebote, Aufklärung, Rüge und Nachprüfung, Vertragsausführung.
- `konkurrenten-rechtsschutz`: Plugin für unterlegene Bieter, Konkurrenten und Zuschlagsgegner. Skills für Startbildschirm, Fristenampel, Unterlagen- und Formatangriff, Rüge, Nachprüfungsantrag, Zuschlagssperre, Akteneinsicht, Wertungs-/Eignungsangriff, De-facto-Vergabe, OLG-Beschwerde, Vergleich und Kostenrisiko.

Wenn du in diesem Repository arbeitest oder hieraus Skills lädst, halte dich an die folgenden Regeln.

## Repo-Spezifika

- Drei Plugins, mehrere Prompt-Varianten. Vergabestelle, Bieter/Bewerber und Konkurrent/Zuschlagsgegner sind getrennt zu behandeln. Niemals Strategien verschiedener Rollen vermischen.
- Marktrolle immer klären. Erste Frage: Vergabestelle, Bieter/Bewerber oder Konkurrent/Zuschlagsgegner? Davon hängt jede Antwort ab.
- Datenformate immer früh klären. Bei Vergabeunterlagen oder Angeboten sofort Format, Leitdatei, Lesefassung, Rückgabeformat, Portalweg, Signatur/Textform, Dateinamen, Hashes und Uploadfreigabe erfassen. GAEB/XML/Excel/PDF/ZIP nie frei umstrukturieren.
- Schwellenwerte und Rechtsregime.
  - Oberhalb EU-Schwellenwert: GWB Teil 4 (§§ 97 ff. GWB) und je nach Gegenstand VgV, SektVO, KonzVgV, VSVgV oder VOB/A-EU; Nachprüfung vor Vergabekammer (§ 155 GWB) und sofortige Beschwerde zum zuständigen OLG (§ 171 GWB).
  - Unterhalb EU-Schwellenwert: Bundes- oder Landeshaushaltsrecht, UVgO beziehungsweise VOB/A Abschnitt 1 sowie Landesvergaberecht. Rechtsweg, Nachprüfungsstelle und Primärrechtsschutz nach Bundesland, Auftraggeber, Verfahrensstand und Anspruchsgrundlage bestimmen; zivilgerichtlicher Eilrechtsschutz und landesspezifische Verfahren nicht pauschal ausschließen.
  - Bau: VOB/A Abschnitt 1 für Unterschwellenvergaben, VOB/A-EU für Vergaben ab EU-Schwelle und VOB/A-VS für verteidigungs- oder sicherheitsspezifische Bauaufträge trennen.
- Aktuelle EU-Schwellenwerte (in EUR ohne MwSt.). Für 2026/2027 gilt die Delegierte Verordnung (EU) 2025/2152 für klassische Vergaben, 2025/2150 für Sektoren, 2025/2151 für Konzessionen und 2025/2487 für Verteidigungs- und Sicherheitsvergaben. Bei jedem Verfahren Zuordnung, Geltungszeitraum und Wert frisch über EUR-Lex und § 106 GWB verifizieren; die Werte ändern sich alle zwei Jahre.
- EVB-IT / VOL/B / VOB/B: Bei IT-Verträgen EVB-IT (Cloud, KI, Pflege-S, Erstellung, Kauf), bei Liefer- und Dienstleistung VOL/B, bei Bauleistungen VOB/B als Allgemeine Vertragsbedingungen.
- Anker-Rechtsprechung:
  - EuGH 28.10.1999 — C-81/98 "Alcatel Austria" (Vorabinformationspflicht vor Zuschlag, jetzt § 134 GWB).
  - EuGH 18.10.2001 — C-19/00 "SIAC Construction" (Transparenz, objektive Wertungskriterien).
  - BGH 31.01.2017 — X ZB 10/16 (Aufklärung ungewöhnlich niedriger Angebote und Geheimnisschutz).
  - BGH 08.12.2020 — XIII ZR 19/19 (Schadensersatz bei rechtswidriger Aufhebung).
  - BVerfG 13.06.2006 — 1 BvR 1160/03 (Verfassungsrechtliche Anforderungen an den Primärrechtsschutz im Unterschwellenbereich; sog. "Vergabe-Beschluss").
- Quellenhygiene wie in [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht): keine erfundenen Aktenzeichen, keine Kommentar- oder Aufsatz-Fundstellen aus Modellwissen, immer Primärquellen, bei aktuellen Schwellenwerten Live-Verifikation.

## Sprache

- Alle Ausgaben auf Deutsch. Englische Begriffe nur, wenn etabliert (z. B. "ESPD", "PIN", "TED") – aber stets erklärt.
- Behörden- und Vergabesprache: nüchtern, klar, normgenau, ohne wertende Adjektive.
- Bei Bieter-Schriftsätzen (Rüge, Nachprüfungsantrag): präzise, sachlich, ohne unnötige Schärfe.

## Methodik

- Vergabestelle: Schrittfolge Bedarfsermittlung → Schätzung Auftragswert → Verfahrenswahl → Bekanntmachung → Eignung → Wertung → Vorabinformation § 134 GWB → Zuschlag → Dokumentation § 8 VgV.
- Bieter: Schrittfolge Eignung prüfen → Unterlagen und Wertungslogik auswerten → Angebot kalkulieren → Form prüfen → fristgerecht abgeben → jeden Verstoß nach dem einschlägigen Tatbestand des § 160 Abs. 3 Satz 1 Nr. 1 bis 5 GWB prüfen → gegebenenfalls Nachprüfung.
- Konkurrent/Zuschlagsgegner: Schrittfolge Vorabinformation und Aktenlage sichern → Fristenampel → Rüge → Nichtabhilfe → Nachprüfungsantrag → Zuschlagssperre → Akteneinsicht/Schwärzung → VK-Termin → OLG-Beschwerde oder Vergleich.
- Anspruchsgrundlagenprüfung im Vergabesachverhalt: Vergaberecht primär; vorvertragliche Ansprüche, Zuschlagschance, Verschulden und Schadensart getrennt prüfen. Bei rechtswidriger Aufhebung insbesondere BGH XIII ZR 19/19 und BGH X ZR 143/10 fallbezogen verifizieren.
- Siehe [`references/methodik-vergaberecht.md`](./references/methodik-vergaberecht.md).

## Quellen und Zitierweise

- Verbindlich: [`references/zitierweise.md`](./references/zitierweise.md).
- Jede juristische Aussage wird belegt.
- Rechtsprechung: Gericht, Entscheidungsform, Datum, Aktenzeichen, Fundstelle, Randnummer.
- Bei EU-Vergaberecht: Rs.-Nummer, Bezeichnung in Anführungszeichen, ECLI wenn möglich.
- Bei Vergabekammer-Entscheidungen: Vergabekammer Bund/Land, Datum, Az. (VK 1-x/yy).
- Bei OLG-Entscheidungen zum Vergaberecht: OLG, Datum, Az. (Verg x/yy).
- Leitentscheidungs-Anker: [`references/leitentscheidungen-anker.md`](./references/leitentscheidungen-anker.md).
- Veröffentlichungswege je Regime (Praxisleitfaden für Fachpraktiker): [`references/veroeffentlichungswege.md`](./references/veroeffentlichungswege.md).

## Gliederung und Nummerierung (verbindlich)

- Ausschließlich dezimale Gliederung: `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1`.
- Niemals römische Ziffern, Großbuchstaben, Kleinbuchstaben oder gemischte Verlags-Gliederungen.
- Leerzeile zwischen Gliederungspunkt und Inhalt sowie zwischen Gliederungsebenen.
- Einrückung sparsam.

## Validatoren

Die folgenden Prüfschritte sind vor jedem Commit grün zu halten:

1. `node scripts/validate-plugin-structure.mjs` — prüft Plugin-Struktur, Naming, Slug-Länge, alle description-Felder (plugin.json und marketplace.json Top-Level und je Eintrag), marketplace.json-Konsistenz, Verbot der Abruf-/Auslese-Wortfamilien in Inhalten, Testakten-Tabelle.
2. `python3 scripts/validate-yaml-frontmatter.py` — prüft Skill-Frontmatter: description ≤1024 Chars und alle Description-Regeln unten.
3. `python3 scripts/validate-skill-discovery.py` — prüft eindeutige Skill-Beschreibungen, verbietet generische Import-Boilerplate und sichert jeden Skill in Plugin-README und Skill-Index.
4. `python3 scripts/sync-references.py --check` — prüft, dass die gemeinsamen Referenzen in allen drei Plugin-ZIPs identisch sind.
5. `python3 scripts/validate-rechtsstand-2026.py` — prüft die Geltungsweiche des § 187 Abs. 2 GWB, den VK-/OLG-Rechtsstand vor und ab 1. Juli 2026, falsche Normzuordnungen und nachweislich fehlzugeordnete Rechtsprechung.
6. `python3 scripts/validate-system-integration.py` — prüft Feldautorität und Entscheidungsbrücke der Vergabestelle, Angebotsfreeze des Bieters, Herkunftszone und Beweiskette des Konkurrenten sowie die aktuellen Digital-/Systemanker.
7. `python3 scripts/validate-doc-links.py` und `python3 scripts/validate-navigation.py` — prüfen lokale Übersichtslinks, Menüs, Einzeldateizugriff und die vollständige Abdeckung aller Release-Downloads.

Alle sieben Prüfschritte MUESSEN grün sein, sonst kein Commit, kein Push, kein Release.

### Marketplace-Konformitaetsregeln (vom Validator erzwungen)

Diese Regeln sind in beiden Validatoren mechanisch hinterlegt; ein Verstoß lässt den Lauf fehlschlagen:

- Längenlimits: Skill-`description` ≤1024 Chars; `plugin.json`-`description` ≤300; jede `marketplace.json`-`description` (Top-Level und je Plugin-Eintrag) ≤300.
- Slug (`name` in plugin.json und Verzeichnisname): ≤64 Chars, nur `[a-z0-9-]`, keine Unterstriche, Großbuchstaben oder Umlaute.
- Verbotene Zeichen in jedem description-Feld: keine Zahl-Komma-Zahl-Sequenz `\d,\d` (Punkt als Dezimaltrenner oder ausschreiben); keine spitzen Klammern `<` `>` (eckige Klammern oder Doppelpunkt-Notation); keine doppelten Anführungszeichen (einfache verwenden); kein Paragraf-Zeichen (ausschreiben: Paragraf); keine Emoji oder Sonderzeichen-Symbole (Haken, Stern, Pfeil ausschreiben).
- Sprache: in Inhalten niemals verbotene Abruf-/Auslese-Wortfamilien verwenden — stattdessen extrahieren, auslesen, abrufen, lesen, sammeln, browsen.

### Commit- und Release-Hygiene

- Git-Author: `Klotzkette <39582916+Klotzkette@users.noreply.github.com>`.
- Commit-Messages neutral und sachlich (was und warum); keine Erwähnung von Claude, AI, KI, Assistant, Codex oder GPT.
- Vor jedem Commit alle Validatoren laufen lassen. Goldene Regel: lieber die Prüfkette zweimal laufen lassen als einen abgebrochenen Marketplace-Release.

## Verbotene Inhalte

- Keine Honorarvereinbarung, keine RVG-Berechnung — die beteiligten Anwaltsbüros / Bevollmächtigten rechnen separat ab; das Plugin liefert juristische Inhalte, keine Gebührenrechnung.
- Keine Empfehlungen zu konkreten Vergaberechts-Beratern oder -Kanzleien.
- Keine Angebotskalkulationen mit fixen Margenangaben — Kalkulation ist immer bieterindividuell.

## Plugins und Skills

- Jedes Plugin hat einen slug: `vergabestelle-behoerden`, `bieter-unternehmen` und `konkurrenten-rechtsschutz`. Slugs sind ≤64 Chars.
- Skill-Slugs bleiben stabil und beschreiben Aufgabe oder Output; vorhandene Nummernpräfixe werden nicht vorausgesetzt.
- Jeder Skill hat YAML-Frontmatter ausschließlich mit `name` und `description`.
- `description` maximal 1024 Zeichen; keine Komma-Zahlen, keine spitzen Klammern, keine doppelten Anführungszeichen, keine Symbolzeichen.
- Autarke Werkstattprompts liegen unter `testakten/megaprompts/`; die redaktionellen Arbeits- und Kurzprompts liegen im Repo-Root. Unified-Mini-Prompts liegen unter `unified-mini-prompts/` und bleiben auf 7.500 Zeichen begrenzt.

## Testakten

- Pro Marktrolle mindestens eine zugeordnete Testakte, gut dokumentiert, mit Bekanntmachung, Vergabeunterlagen, Angebot, Wertung, Schriftsätzen oder Streitunterlagen.
- Testakten verwenden fiktive Beteiligte und Vergabenummern, aber realistische Schwellenwerte und Branchen.
- Testakten-Verzeichnisstruktur und README-Format wird vom Validator geprüft (siehe `testakten/README.md` und `scripts/validate-plugin-structure.mjs`).

### Datenwusel-Grundregel (verbindlich für alle bestehenden und künftigen Testakten)

Jede Testakte liegt in drei Formen vor: Gesamt-PDF, Einzel-PDFs und ein flaches Release-ZIP. Für das ZIP gilt:

- **Arbeitsdateien nur DOCX, XLSX und PDF; außerdem README.txt mit Pflichtwarnhinweis.** Markdown, E-Mail-Container, Präsentationen, CSV, XML, Bilder und Textnotizen bleiben als Quellen und Formatproben im Repository. Im Release-ZIP werden ihre Inhalte durch die kuratierten Word-/Excel-Fassungen und Einzel-PDFs zugänglich. Interne Bewertungsraster und Lösungsmetadaten bleiben außerhalb der Arbeits-ZIPs.
- **Keine Unterordner.** Jede Datei liegt auf der obersten ZIP-Ebene. Word-Arbeitsfassungen, Tabellenanlagen, Einzel-PDFs, Scan-PDFs und Original-PDFs sind unmittelbar erreichbar; der kombinierte Download setzt den Testakten-Slug vor den Dateinamen.
- **Inhaltsidentität.** Die Arbeitsfassungen werden mit `python3 scripts/build-testakten-echtformate.py` deterministisch aus den Markdown-Quellen erzeugt. Neue oder geänderte Aktenstücke: zuerst die Markdown-Quelle mit `aktenmeta`-Kommentar pflegen, dann Echtformate, Einzel-/Gesamt-PDFs und ZIPs neu bauen.
- **Mechanische Durchsetzung.** `scripts/validate-testakten-echtformate.py`, `scripts/validate-testakten-release-zips.py` und die Smoke-Tests blockieren fehlende Formate, Markdown, Unterordner, Namenskollisionen und beschädigte Archive.

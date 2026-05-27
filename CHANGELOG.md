# v14.2.0 — Vollumfaenglicher Wissensboost ueber alle 1800+ Skills

Inhaltlicher Tiefenboost ueber alle 97 Plugins und ueber 1800 Skills. Jeder bearbeitete Skill bekommt eine konkrete Triage zum Mandatseinstieg, eine vollstaendige Paragrafenkette mit Wortlaut der zentralen Tatbestandsmerkmale, zwei bis vier aktuelle Leitsatz-Zitate aus BVerfG BGH BAG BFH BSG BVerwG EuGH oder OLG mit Aktenzeichen und Fundstelle, Hinweise auf die zentrale Kommentarliteratur des Rechtsgebiets, einen Schritt-fuer-Schritt-Workflow und ein passendes Output-Template fuer Schriftsatz Bescheid Beschluss oder Mandantenbrief. Strukturelle Bereinigung Plugin sozialrecht-kanzlei vollstaendig nach fachanwalt-sozialrecht uebernommen und alte Light-Touch-Selbstbezeichnung entfernt.

## Was sich pro geboostetem Skill geaendert hat

- **Triage zum Einstieg** — fuenf bis sieben konkrete Vorabfragen mit Begruendung warum sie zu klaeren sind
- **Zentrale Normen mit Wortlaut** — Paragrafenkette mit kursivem Tatbestandsmerkmal nicht nur Paragrafennummer
- **Aktuelle Rechtsprechung** — zwei bis vier Leitsaetze BVerfG BGH BAG BFH BSG BVerwG EuGH OLG mit Aktenzeichen Fundstelle Randnummer Paraphrase
- **Kommentarliteratur** — die ein bis drei einschlaegigen Standardkommentare fuer das Rechtsgebiet
- **Workflow in Schritten** — von Aktenanlage ueber Substantiierung bis Versand
- **Output-Template mit Platzhaltern** — Schriftsatz Bescheid Beschluss Klage Mandantenbrief
- **Rote Schwellen und Eskalationskriterien** — wann Fall an Fachanwalt oder Notar abgegeben gehoert
- **Verzicht auf Boilerplate** — keine generischen Phrasen mehr keine Wiederholungen

## Welleneinteilung

Der Boost erfolgte in 12 Wellen mit jeweils 90 bis 250 Skills.

| Welle | Cluster | Skills |
| --- | --- | --- |
| 1 | Arbeitsrecht inkl. Arbeitszeugnis | 201 |
| 2 | Steuerrecht Familienrecht Erbrecht Sozialrecht | 108 |
| 3 | Strafrecht Verkehrsrecht | 117 |
| 4 | Miet- Bau- und Immobilienrecht | 92 |
| 5 | Medizinrecht Versicherungsrecht Sport- und Transportrecht | 89 |
| 6 | Gewerblicher Rechtsschutz Urheber- und Medienrecht | 90 |
| 7 | IT-Recht Datenschutz KI-Verordnung DSA NIS-2 | 137 |
| 8 | Insolvenz- und Sanierungsrecht | 154 |
| 9 | Corporate M und A Gesellschaftsrecht Gruendung | 208 |
| 10 | Bank- und Kapitalmarktrecht Vergabe International Migration | 114 |
| 11 | Verwaltungs- Verfassungs- Energie- Umwelt- Kartell- Verbraucherrecht | 135 |
| 12 | Prozessrecht Vertragsrecht Forderungsmanagement Compliance Kanzlei-Methodik Jurastudium | 308 |

## Wichtigste Kommentarliteratur die jetzt zitiert wird

- **Zivilrecht** — Gruenneberg MüKo BGB BeckOK BGB Erman BGB
- **Arbeitsrecht** — ErfK Schaub HWK
- **Handels- und Gesellschaftsrecht** — MüKo HGB MüKo GmbHG MüKo AktG Baumbach Hueck Scholz Hueffer Koch
- **Strafrecht** — Schoenke Schroeder MüKo StGB NK-StGB Fischer
- **Insolvenz** — MüKo InsO Uhlenbruck Jaeger K. Schmidt Uhlenbruck
- **Familienrecht** — MüKoBGB Band 9 und 10 Wendl Dose
- **Mietrecht** — Schmidt-Futterer Staudinger BeckOK Mietrecht
- **Steuerrecht** — Tipke Lang MüKo AO BeckOK Steuerrecht
- **Verwaltungsrecht** — Maurer Waldhoff Kopp Schenke Stelkens Bonk Sachs
- **Verfassungsrecht** — Maunz Duerig Jarass Pieroth Sachs GG
- **IT- und Datenschutzrecht** — Sydow Marsch Kuehling Buchner Paal Pauly Wendehorst Grinzinger
- **Bank- und Kapitalmarktrecht** — Schimansky Bunte Lwowski Hopt KapMarktR
- **Berufsrecht** — Henssler Pruetting Feuerich Weyland

## Strukturelle Bereinigung

- **Plugin sozialrecht-kanzlei** wurde vollstaendig in **fachanwalt-sozialrecht** ueberfuehrt. 20 Skills wurden verschoben vier doppelt vorhandene Themen wurden gemergt. Das Fachanwalt-Plugin enthaelt jetzt sowohl die Fachanwalt-Rechtsprechungstiefe als auch die volle Kanzleioperative — Bescheidanalyse Akteneinsicht Anlagen Eilantrag Hilfsmittel Pflegegrad Fristenbuch und PKH.
- **Light-Touch-Selbstbezeichnung entfernt** in 51 Files. Plugins fuer Fachanwaltschaft sind nicht laenger Light-Touch sondern vollumfaenglich.
- **SKILLS.md** mit funktionierenden GitHub-Anker-Links und Zwei-Spalten-Tabelle pro Plugin direkt verlinkt zur SKILL.md.

## Qualitaetssicherung

- Validator `node scripts/validate-plugin-structure.mjs` final OK
- Komma-Sweep in plugin.json und SKILL.md Frontmatter `description:` ueberall ohne Komma zwischen Ziffern
- Cyrillic-Confusables-Sweep ueber alle bearbeiteten Files clean
- Keine verbotenen Frontmatter-Felder (triggers when_to_use language rechtsgebiet license argument-hint user-invocable allowed_tools tools model adapted_from)
- Keine XML-Brackets in description-Feldern
- YAML-Quoting bei descriptions mit Doppelpunkt-Konstrukten korrekt

## Versionsstand nach v14.2.0

- 97 Plugins
- Ueber 1800 boostfaehige Skills bearbeitet (44 Skills waren bereits auf v14.1-Niveau und wurden ohne weitere Aenderung uebernommen)
- alle plugin.json und marketplace.json auf version `14.2.0`

# v14.1.0 — Grosser Inhalts-Boost (145 Top-Skills auf dreifache Tiefe)

Inhaltliche Verdreifachung der 145 fachlich wichtigsten Skills in allen 24 Fachanwalt-Plugins sowie in `steuerrecht-anwalt-und-berater` und den fuenf Corporate-Plugins (`corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender`). Generische Boilerplate-Skills (Erstgespraech, Vergleichsverhandlung, Mandantenkommunikation) sind aus dem Boost ausgenommen — der Fokus liegt auf der fachlichen Substanz.

## Was sich pro geboostetem Skill geaendert hat

Jeder der 145 ausgewaehlten Skills wurde von einer Knappformulierung in eine voll ausgearbeitete Arbeitsanleitung umgeschrieben. Erweitert wurden, wo passend:

- **Kaltstart-Mandantenfragen** — sechs bis zehn konkrete Fragen mit Begruendung
- **Rechtsgrundlagen** — Wortlaut der zentralen Tatbestandsmerkmale, nicht nur Paragrafnummer
- **Pruefschemata in Tabellenform** — acht bis fuenfzehn Schritte
- **Schriftsatzbausteine und Klauselvorlagen** — vollstaendige Formulierungen
- **Beweislast und Darlegungslast** — klar zugeordnet
- **Fristen und Verjaehrung** — konkret kalendermaessig
- **Typische Gegenargumente und Reaktion** — Tabellenform
- **Streitwert und RVG-Hinweise** — beziffert
- **Strategische Empfehlung** — aussergerichtlich, Klage, Vergleich
- **Anschluss-Skills** — Querverweise zu anderen Skills im Plugin
- **Aktuelle Aktenzeichen** — BGH, BAG, BFH, BVerwG, BVerfG, OLG, FG

## Cluster-Aufteilung

| Cluster | Plugins | Geboostete Skills |
| --- | --- | --- |
| Cluster A — 24 Fachanwalt-Plugins | siehe Plugin-Liste unten | 120 |
| Cluster B — Steuerrecht | `steuerrecht-anwalt-und-berater` | 5 |
| Cluster C — Corporate | `corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender` | 25 (5 pro Plugin) |

## Fachanwalt-Plugins im Boost (alle 24)

`agrarrecht`, `arbeitsrecht`, `bank-kapitalmarktrecht`, `bau-architektenrecht`, `erbrecht`, `familienrecht`, `gewerblicher-rechtsschutz`, `handels-gesellschaftsrecht`, `insolvenz-sanierungsrecht`, `internationales-wirtschaftsrecht`, `it-recht`, `medizinrecht`, `miet-wohnungseigentumsrecht`, `migrationsrecht`, `sozialrecht`, `sportrecht`, `strafrecht`, `transport-speditionsrecht`, `urheber-medienrecht`, `vergaberecht`, `verkehrsrecht`, `versicherungsrecht`, `verwaltungsrecht`.

## Nebenbei behoben

Zwei alte Validator-Fehler in nicht-geboosteten Skills (Komma-in-Zahlen-Pattern in `description`):

- `fachanwalt-gewerblicher-rechtsschutz/.../SKILL.md`: `§§ 5, 32 HinSchG` zu `§§ 5 und 32 HinSchG`
- `fachanwalt-insolvenz-sanierungsrecht/.../SKILL.md`: `§ 9, 3/4-Mehrheit` zu `§ 9 mit 3/4-Mehrheit`

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.1.0.
- `marketplace.json` (Top-Level und alle Plugin-Eintraege) auf 14.1.0.
- Validator OK.

---

# v14.0.0 — Frischer Major-Release

Frischer Sammelrelease ueber alle 98 Plugins. Der Versionssprung von 12.x auf 14.0 markiert das Ende des 12er-Inkrement-Zyklus und buendelt den aktuellen Stand der Skill-Familie als einheitliches Major-Release.

## Bug-Hunt Immobilienrechtspraxis

Der Immobilien-Plugin-Schwerpunkt dieses Releases ist eine systematische Bug-Pruefung. Geprueft wurden Frontmatter-Felder, Description-Laengen, verbotene Pattern (Komma in Zahlen), verbotene Frontmatter-Keys, Cross-References, kaputte Markdown-Links und Mischformen aus Umlauten und ASCII-Aequivalenten.

- Inkonsistente Schreibweise `Buerogeb\u00e4ude` (ASCII-Mix mit Umlaut) zu `B\u00fcrogeb\u00e4ude` korrigiert (`projekt-arbeitsweise`).
- Cross-Reference auf `memorandums-ersteller` validiert (Plugin existiert im Marketplace, Verweis bleibt).
- Frontmatter aller sieben Skills geprueft: keine verbotenen Felder, keine zu langen Descriptions, keine Komma-Patterns.
- Plugin-Description und Keywords sauber, keine Aenderung erforderlich.

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.0.0.
- `marketplace.json` auf 14.0.0 (Top-Level und alle Plugin-Eintraege).
- Validator OK.

---

# v12.6.0 — Aktuelle BAG-Rechtsprechung 2025/2026 (Arbeitsrecht + Fachanwalt)

Drei kuerzlich entschiedene BAG-Urteile, die die Arbeitnehmerseite spuerbar staerken, werden in den Plugins `arbeitsrecht` und `fachanwalt-arbeitsrecht` jeweils als eigenstaendiger Pruefungsskill verankert. Die Skills enthalten Kaltstartfragen, Pruefschema, Schriftsatzbausteine und konkrete Verteidigungslinien.

## Neue Skills im Plugin `arbeitsrecht` (drei)

- `bag-equal-pay-paarvergleich-8azr30024` — BAG 23.10.2025 (8 AZR 300/24): Equal Pay durch Paarvergleich. Eine Arbeitnehmerin muss keine statistische Vergleichsgruppe auswerten. Ein einziger besser bezahlter maennlicher Kollege bei gleichwertiger Arbeit begruendet die Vermutung des Paragraf 22 AGG. Pauschale Hinweise auf Median oder Verhandlungsgeschick reichen nicht mehr.
- `bag-mindesturlaub-kein-verzicht-9azr10424` — BAG 03.06.2025 (9 AZR 104/24): Kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhaeltnis, auch nicht durch gerichtlichen Vergleich. Klausel-Verbote, empfohlene Vergleichsformulierung mit Trennung Mindesturlaub und Mehrurlaub.
- `bag-freistellungsklausel-unwirksam-5azr10825` — BAG 25.03.2026 (5 AZR 108/25): Pauschale formularmaessige Freistellungsklausel nach Kuendigung unwirksam wegen unangemessener Benachteiligung Paragraf 307 BGB. Beschaeftigungsanspruch BAG GS 1/84 bleibt bestehen.

## Neue Skills im Plugin `fachanwalt-arbeitsrecht` (drei)

- `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich` — Anwaltsperspektive auf 8 AZR 300/24: Kaltstart-Rueckfragen, Klagebaustein Equal Pay, typische Arbeitgeber-Verteidigung und Reaktion.
- `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht` — Anwaltsperspektive auf 9 AZR 104/24: empfohlene Vergleichsformulierung, Klausel-Verbote, Nachforderungsmoeglichkeit bei bereits geschlossenem Pauschalvergleich.
- `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` — Anwaltsperspektive auf 5 AZR 108/25: Strategie fuer Beschaeftigungsanspruch oder Verhandlungsmasse, Schriftsatzbaustein, Annahmeverzugsfolgen.

## Plugin-Metadaten

- Plugin-Beschreibung beider Plugins um Hinweis auf aktuelle BAG-Rechtsprechung 2025/2026 ergaenzt.
- README beider Plugins um Abschnitt zu den neuen Skills erweitert.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.6.0.

---

# v12.5.0 — Arbeitszeugnis-Analyse: Vollstaendiger Mandatsablauf

Schliesst den Mandatsworkflow im `arbeitszeugnis-analyse` Plugin: vom Erstkontakt mit dem Mandanten ueber den Ergebnisbericht bis zum Aufforderungsschreiben an den Arbeitgeber. Das Plugin deckt damit nicht nur die Analyse des Zeugnistextes ab, sondern den gesamten Anwaltsworkflow von der Mandatsannahme bis zum Berichtigungsverlangen.

## Neue Skills (drei)

- `erstgespraech-und-mandatsannahme` — Eingangsbestaetigung mit Dank fuer das uebersandte Zeugnis, strukturierte Anforderungsliste fuer fehlende Unterlagen (Arbeitsvertrag, Aenderungsvereinbarungen, Vorzeugnisse, Kuendigungsschreiben, Abmahnungen, Fehlzeitenuebersicht, Lohnabrechnungen), Erstgespraech-Leitfaden in fuenf Bloecken (Sachverhalt, Ziel, Vergleichsbereitschaft, rechtliche Erstinformation, Vereinbarung), Pruefliste vor Mandatsannahme.
- `mandantenbericht-zeugnisanalyse` — Schriftlicher Ergebnisbericht an den Arbeitnehmer in sieben Abschnitten: Gesamtnote, Befund pro Themenbereich, kritische Einzelstellen mit Wortlaut, rechtliche Einordnung, Erfolgsaussichten in drei Stufen, drei Handlungsoptionen (Akzeptanz, Berichtigungsverlangen, Klage) mit Kosten-Nutzen-Abwaegung, klare Empfehlung. Verstaendliche Sprache fuer den juristischen Laien.
- `aufforderungsschreiben-arbeitgeber` — Aussergerichtliches Berichtigungsverlangen mit acht Bausteinen: Mandatsanzeige, Bezugnahme auf das Zeugnis, Rechtsgrundlage Paragraf 109 GewO, Beanstandungen pro Streitstelle (Wortlaut alt, Wortlaut neu, Begruendung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Schlussformel-Pruefung, kalendermaessige Fristsetzung, Klageandrohung, Kostenfolge. Hoeflich-bestimmter Ton ohne Drohgebaerden. Vollstaendiger Mustertext mit Beispielen.

## Plugin-Metadaten

- 31 Skills (vorher 28), 20-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst, hebt den vollstaendigen Mandatsablauf hervor.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.5.0.

---

# v12.4.0 — Arbeitszeugnis-Analyse: Sprachhebel, Codeworte, Klagestrategie

Vertiefung des `arbeitszeugnis-analyse` Plugins um drei spezialisierte Sprach- und Recht-Skills: feingranularer Steigerungsadverbien-Katalog, vollstaendiger Katalog negativer Codeworte fuer sensible Themen sowie eine durchgaengige Klagestrategie zur Zeugnisberichtigung von der ausserprozessualen Rueckforderung bis zum vollstreckbaren Tenor.

## Neue Skills (drei)

- `steigerungsadverbien-katalog` — Vier-Klassen-Matrix der Adverbien mit Notenwirkung: echte Steigerer (stets, jederzeit, immer), Schein-Steigerer mit Risiko (sehr, ausserordentlich nur in Kombination), Abschwaecher (im Allgemeinen, weitgehend, meist) und negative Verstaerker (nie, kaum, kein einziges Mal). Notenkalibrierung jeder Klasse, sodass die satzweise Bewertung das richtige Gewicht erhaelt.
- `negative-codeworte-katalog` — Tabuthemen-Katalog mit den verdeckten Anspielungen auf Alkohol, Krankheit, Diebstahl/Untreue, Konflikt mit Vorgesetzten, mangelnde Loyalitaet, Betriebsratstaetigkeit, sexuelle Verfehlungen, Mitlaeufertum sowie systematischen Auslassungssignalen. Jede Kategorie mit den typischen Formulierungen und dem rechtlich gebotenen Tenor.
- `klage-strategie-zeugnisberichtigung` — Vollstaendige prozessuale Linie: aussergerichtliches Berichtigungsverlangen, Klageantrag mit Tenor (vollstreckbar gemaess Paragraf 888 ZPO), Beweislastverteilung (Note ab Drei: Arbeitnehmer; oberhalb der Drei: Arbeitgeber), Streitwertberechnung, Verjaehrung/Verwirkung und prozesstaktische Empfehlungen.

## Geaenderte Skills

- `verbesserungsvorschlaege-formulieren` — drei neue Drift-Rewrite-Beispiele zu Lernbereitschaft, Innovationsverhalten und Sozialverhalten; ergaenzte Regeln-Tabelle.
- `rechtliche-bewertung-bag-rechtsprechung` — drei neue Absaetze zu verfestigter BAG-Rechtsprechung, Schlussformel-Codeworten und Verjaehrung/Verwirkung; sieben neue Regeln-Tabellenzeilen und drei zusaetzliche Bewertungsbeispiele.

## Plugin-Metadaten

- 28 Skills (vorher 25), erweiterter 16-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst und auf die drei neuen Schwerpunkte abgestimmt.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.4.0.

---

# v12.3.0 — Arbeitszeugnis-Analyse: Schaufenster-Drift-Detektor

Spezialisierter Ausbau des `arbeitszeugnis-analyse` Plugins um die Erkennung des Schaufenster-Patterns: einzelne Saetze auf Note-1-Niveau, daneben Saetze auf Note-3-Niveau zum selben Themenbereich. Wer nur die Spitzensaetze liest, sieht Note 1; wer die Drift erkennt, sieht die korrekte hochgezogene Zwei bis solide Drei.

## Neue Skills (drei)

- **`bereichs-drift-detektor`** — Erkennt Drift innerhalb derselben acht Themenbereiche (Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis, Sozialverhalten). Spreizung zwei Stufen = Rot, eine Stufe = Orange. Drift in weichen Bereichen (Lernen, Innovation, Sozialverhalten) wird gesondert geflaggt.
- **`satzweise-notenmatrix`** — Bewertet jeden notenrelevanten Satz mit Schulnote von eins bis fuenf. Festes Raster: Steigerungsadverb plus Superlativ = 1, eins davon = 2, Grundaussage = 3, Einschraenkung oder „bemueht" = 4, Distanzformel = 5. Tabellarisches Ausgabeformat mit Themenbereich pro Satz — Datenbasis fuer Drift-Detektor und Gesamtnoten-Aggregation.
- **`muster-arbeitszeugnis-gemischte-noten`** — Vollstaendiges anonymisiertes Schulungszeugnis mit Schaufenster-Pattern. Zeigt 1er- und 3er-Saetze gemischt, vollstaendige Satz-fuer-Satz-Notenmatrix, Bereichs-Drift-Analyse und gewichtete Gesamtnote mit Drift-Penalty.

## Updates

- **`gesamtnoten-aggregation`**: neue Drift-Penalty-Regel (minus halbe Stufe bei Spreizung zwei Stufen, minus halbe Stufe bei konstanter Note 3 in weichen Bereichen). Neues Beispiel: Schaufenster-Zeugnis.
- **`widerspruechliche-bewertungen`**: vierter Widerspruchstyp (Schaufenster-Pattern im selben Themenbereich) mit Verweis auf den neuen Drift-Detektor.
- **`README.md`**: erweiterter Empfehlungs-Workflow um Satzmatrix, Drift-Detektor und Widerspruchsanalyse; Plugin enthaelt jetzt 25 Skills.

## Globaler Versionsbump

Alle 98 Plugins und `marketplace.json` auf v12.3.0.

---

# v12.2.0 — Testakten in Plugin-READMEs sichtbar gemacht

## README-Sweep
13 Plugin-READMEs ergaenzt: Testakte als sichtbarer Direkt-Download (Tabelle) direkt unter der Plugin-Download-Sektion.

- arbeitsrecht (Vogt, Weber)
- aussenwirtschaft-zoll-sanktionen (GlobalMaschinen)
- datenschutzrecht (Solis Vision X)
- dsa-dma-digitalregulierung (Bayerische Baustube)
- geldwaeschepraevention-aml-kyc (Musterholding)
- grosskanzlei-corporate-ma (Datenraum)
- insolvenzrecht (LUMEN Studios — Edelholz war bereits drin)
- insolvenzverwaltung (Moebelwerk Havelberg, Nordlicht Handels)
- kanzlei-allgemein (Kanzlei-Alltag)
- steuerrecht-anwalt-und-berater (Edelholz)
- strafbefehl-verteidiger (LUMEN Studios)
- vertragsrecht (Sieglinger SV-Gutachten)
- zwangsverwaltung-zvg (Friedrichshoefe, Mietshaus Parkstrasse, Eppendorf)

## Fix
- testakten/inkasso-zahlungsklage-modefuchs/README.md: toter Link auf `Schulungsakte_ModeFuchs_GmbH.zip` entfernt; nur der `originale/` Ordner mit 28 PDFs bleibt.
- Mapping-Korrektur Testakten zu Plugins: `bauplanungsrecht` -> `normenkontrolle-bauleitplanung`.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.2.0.

# v12.1.0 — Validatorhaertung Plugin-Generator + Versionsbump

## Fix (gegenueber v12.0.0)
- `forderungsmanagement-klagewerkstatt/scripts/plugin_aus_hausregeln.py`: erzeugte hauseigene Mini-Plugins sind jetzt validatorkonform und sofort in Claude Code installierbar.
  - plugin.json description gekuerzt von 514 auf 218 Zeichen (Marketplace-Limit 300).
  - Zahl-Komma-Zahl-Sequenzen `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` (Cowork-Validator-Regel).
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt; Trigger-Phrasen wurden in die description integriert.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.1.0.

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

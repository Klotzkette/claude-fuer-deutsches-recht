# Unreleased — Meinungsprüfer

- Neues Plugin **`meinungspruefer`** mit 36 Skills zur Prüfung von Äußerungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung/Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, § 193 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR-/EuGH-Rechtsprechung, OLG-/KG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Arbeitsplatz, Schule und kommunale Machtkritik.
- Neue Testakte **`meinungspruefer-grenzfaelle-alltag`** mit X-Post zum kommunalen Bauprojekt, LinkedIn-Pinocchio, Kantinenäußerung über Zahlen, Elternchat, Bürgermeister-"Lackaffe", Abmahnung, polizeilicher Anhörung, Belegmappe und USA-Vergleichsnotiz.
- Nachlauf im Meinungsprüfer: vier neue Skills **`egmr-art-10-rechtsprechung`**, **`eugh-grch-art-11-rechtsprechung`**, **`olg-kg-praxis-rechtsprechung`** und **`rechtsvergleich-usa-supreme-court`**; die Rechtsprechungsbank wurde um EGMR, EuGH/GRCh, OLG/KG und Supreme-Court-Anker mit freien Quellen erweitert.
- Rechtsprechungsbank im Plugin mit frei prüfbaren Quellen und ohne BeckRS-/Kommentar-/Aufsatz-Blindzitate.

---

# v24.1.0 — AZ-Strip, Konversationsstil und LG Aachen 10 O 306/25

- **Welle 3 — Halluzinations-AZ entfernt.** Die im Vollaudit (`audit/audit_problems_2026-05-27.json`) als WRONG_TOPIC oder NOT_FOUND klassifizierten 969 Aktenzeichen wurden aus den betroffenen SKILL.md gestrichen. Ergebnis: 175 Dateien geaendert, 392 Zeilen entfernt; YAML-Frontmatter blieb unangetastet. Dokumentiert in `audit/README.md` und `audit/references_audit_2026-05-29.json`.
- **Welle 4 — References-Konsistenz.** 17 tote Markdown-Verweise auf `references/`-Dateien identifiziert; einer (`rechtsberatungsstelle/.../pruef-warteschlange.yaml` → `review-queue.yaml`) gefixt. Die restlichen 16 sind in `audit/references_audit_2026-05-29.json` dokumentiert.
- **Konversationsstil-Update.** `CLAUDE.md` und alle 102 `<plugin>/skills/allgemein/SKILL.md` erhalten einen verbindlichen Block: erste Antwort konzis, hoechstens eine unverzichtbare Rueckfrage, dann schnell zur Dokumentenproduktion. Ausfuehrlich nur bei echter Subsumtion, Tabellen, Risikoanalysen oder Schriftsatz-/Memo-Text. Allgemein-Skills sind Einstieg, nicht Vorlesung.
- **Frontmatter-Konvention geschaerft.** `CLAUDE.md` listet jetzt die verbotenen Frontmatter-Felder explizit (`triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **LG Aachen 10 O 306/25 (Urteil vom 27.05.2026) als Leitentscheidung aufgenommen** in: `bgb-at-pruefer/.../kauf-im-internet-und-auktionen`, `bgb-at-pruefer/.../gesetzesverbot-sittenwidrigkeit-paragraphen-134-138`, `vertragsrecht/.../vertragspruefung`, `produktrecht/.../feature-risikobewertung`. Inhalt: Button-Beschriftung "Wette abgeben" beim Online-Gluecksspiel genuegt nicht § 312j Abs. 3 BGB; endgueltige Unwirksamkeit nach Abs. 4; Rueckabwicklung nach § 812 BGB unabhaengig von Lizenz. Quellenhinweis: offizieller Volltext zum Aufnahmezeitpunkt noch nicht oeffentlich; Aufnahme erfolgte auf Basis Pressehinweis Gamesright GmbH / rightmart, 28.05.2026.
- **Audit-JSON-Fix bewahrt.** Zwei unescapte Quotes (Z. 425, 7661) aus dem Vollaudit-JSON sind gefixt (bereits in v24.0.0 als Commit `5b0676ef` gepusht).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Alle 102 Plugins, Marketplace-Top-Level und alle Marketplace-Plugin-Eintraege einheitlich auf `24.1.0`

---

# v24.0.0 — Einheitliche Versionsbasis und vollständige Codex-Integration

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` einheitlich auf Version `24.0.0` gezogen. Damit sind erstmals seit mehreren Releases sämtliche Manifeste, der Marketplace-Top-Level und alle Marketplace-Plugin-Einträge auf identischer Versionsnummer.
- Sämtliche Codex-Pull-Requests (Selbstvertreter Amtsgericht und Sozialgericht, Lobbyregister Bundestag, Wertgrenzen 2026 nach Justizstandort-Stärkungsgesetz, 150 Steuerberater-Skills BWA/Lohn/DBA) sind in `main` integriert und im Release enthalten.
- YAML-Frontmatter-Hygiene aus v23.0.1 vollständig übernommen: 47 SKILL.md-Frontmatter und ein verbliebener Plugin-Root-CLAUDE.md-Bug aus dem ASCII-Quote-Sweep sind bereinigt; alle Skills passieren den offiziellen `claude plugin validate --strict`.
- Validatoren erweitert: `scripts/validate-yaml-frontmatter.py` (echter pyyaml-Parse-Check inklusive Komma-Zahl-Sequenzen) und `scripts/validate-with-claude-cli.sh` (Wrapper für offizielles `claude plugin validate --strict`).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- `./scripts/validate-with-claude-cli.sh` (offizielle Anthropic CLI v2.1.153)
- `git diff --check`

---

# v23.0.1 — Download-Abdeckung und Quellenhygiene

- Alle 102 Plugin-READMEs geprüft: jedes Plugin nennt sein Plugin-ZIP aus dem `latest`-Release.
- Alle 57 Testakten sind im Testakten-Index mit ZIP-Download eingetragen; jede Testakte ist aus mindestens einem passenden Plugin-README verlinkt.
- Die zentrale README-Übersicht nennt alle 102 Plugins, inklusive `liquiditaetsplanung` und der beiden Selbstvertreter-Plugins.
- Zitierweise v4.0 repo-weit nachgezogen: keine BeckRS-, Kommentar-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei/amtlich oder per lizenziertem Live-Zugriff verifizierter Quelle.
- Unsichere oder nicht frei belegte Rechtsprechungs- und Literaturzeilen in Skills, README-Texten, Generatorvorlagen und Beispiel-Hausregeln durch Live-Verifikationshinweise ersetzt.
- Alle Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.1` gezogen; der `v23.0.0`-Stand bleibt enthalten.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 102/102 Plugin-READMEs mit Plugin-ZIP, 57/57 Testakten-ZIPs im Index und aus Plugin-READMEs erreichbar, 0 unsichere Zitations-Treffer im engeren Audit.
- lokaler Build und Validierung aller Plugin- und Testakten-ZIPs mit `scripts/validate-release-zips.py`

---

# v23.0.0 — Selbstvertreter-Ausbau und ASCII-Anführungszeichen

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.0` gezogen.
- Beide Selbstvertreter-Testakten (`selbstvertreter-amtsgericht-kuechentisch-kaufpreis` und `selbstvertreter-sozialgericht-heizkosten-eilantrag`) deutlich ausgebaut: je drei neue Dokumente, alle bestehenden Dateien stark erweitert, mittlerer bis höherer Schwierigkeitsgrad. Neu in der Amtsgericht-Akte: AGB-Klauseln zur Prüfung, privat eingeholte Voreinschätzung eines Tischlermeisters, Foto-Inventar mit EXIF-Metadaten, zehn widersprüchliche Internet-Treffer. Neu in der Sozialgericht-Akte: vollständiger Bürgergeld-Bescheid mit Berechnungsblatt, Attest mit Mindesttemperaturangabe wegen kindlichem Asthma, vier Telefonnotizen, KdU-Konzept der Stadt Leipzig.
- Beide Selbstvertreter-Plugins `selbstvertreter-amtsgericht` und `selbstvertreter-sozialgericht` in der Plugin-Übersichtstabelle im Root-README ergänzt (waren bislang versehentlich nicht in der Tabelle).
- Steuerrecht-Plugin: Plugin-README-H1 von "Steuerrecht für Anwaltschaft und Steuerberatung" auf "Steuerrecht - Steuerberater und Anwälte" geändert (Slug `steuerrecht-anwalt-und-berater` bleibt — keine Breaking Changes).
- Repo-weiter Sweep: alle typografischen Anführungszeichen (`"` `"` `'` `'` `"` `"`) durch ASCII `"`/`'` ersetzt in 909 Dateien. Verhindert HTML-Entity-Darstellung (`&#x201E;` etc.) in Plugin-Outputs bei Clients, die Markdown durch HTML-Escaping schicken.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v22.0.0 — Nachbarschaftsstreit, US-Transfer-TIA, KI-VO-Evidence-Pack

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `22.0.0` gezogen.
- Neues Plugin **`nachbarschaftsstreit-pruefer`** mit 19 Skills zum Nachbarrecht: Überbau (§§ 912-916 BGB), Überhang (§ 910 BGB), Grenzbaum/Grenzanlage (§§ 921-923 BGB), Einfriedung, Immissionen (§ 906 BGB), Notweg (§§ 917-918 BGB), Vertiefung/Baugrube (§ 909 BGB), Hammerschlagsrecht, Landesnachbarrecht-Router, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung und Vergleich. Mit zwölfteiliger Testakte `nachbarschaftsstreit-horrorfall-rosengarten`.
- Drei neue Datenschutz-Skills im Plugin `datenschutzrecht`: `us-transfer-tia-dokumentation`, `standardvertragsklauseln-scc-paket`, `drittlandtransfer-behoerdenpaket-output`. Mit Testakte `datenschutz-us-transfer-cloudsuite-rheinmain` (CloudSuite Assist, DPF-Lücke, SCC Modul 2, hbDI-Antwortentwurf).
- Neuer KI-VO-Skill `output-konformitaetsbescheinigung-evidence-pack` mit Statusleiter Final/Entwurf/Readiness/Drittstelle, EU-Konformitätserklärung nach Art. 47 / Anhang V, Evidence Index und Lückenliste. Mit Testakte `ki-vo-konformitaetsbescheinigung-bewerberpilot`.
- Bereicherungs- und Arbeitsrecht-Cleanup: URL-Konsistenz `claude-fuer-deutsches-recht` und ASCII-Slugs in den Direkt-Download-Tabellen, Skill-Slugs in Plugin-README-Tabellen ohne Umlaute.
- Direkt-Download-Blöcke in den beiden neuen Testakten-READMEs analog zu den 53 anderen.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v21.0.0 — Direkt-Downloads und Bereicherungsrecht-Cleanup

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `21.0.0` gezogen.
- 52 Testakten-Unterordner-READMEs mit sichtbarem Direkt-Download-Button für die jeweilige ZIP-Datei aus dem `latest`-Release.
- 13 Plugin-READMEs mit eigenem **Zum Ausprobieren: Testakte**-Block und Direkt-Download-Link: `arbeitszeugnis-analyse`, `bgb-at-pruefer`, `fachanwalt-arbeitsrecht`, `fachanwalt-sozialrecht`, `fachanwalt-verwaltungsrecht`, `gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `insolvenzrecht`, `jveg-kostenpruefer`, `kanzlei-allgemein`, `liquiditaetsplanung`, `lobbyregister-bundestag`, `steuerrecht-anwalt-und-berater`.
- Bereicherungsrecht-Cleanup: 77 Skills mit Umlaut- und Typo-Reparatur, 50 Skills mit vollständig ausgebauten Aktivierungs-Descriptions im Muster Trigger + Normen + Prüfraster + Output + Abgrenzung.
- Stand bleibt 101 Plugins, 2386 Skills und 52 Testakten.

---

# v20.0.0 — Release 20 Gesamtstand

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `20.0.0` gezogen.
- `README.md` und `testakten/README.md` auf Release `v20.0.0` aktualisiert; Stand bleibt 101 Plugins, 2332 Skills und 52 Testakten.
- Inhaltlicher Stand aus `v19.1.0` bleibt enthalten: BGB-AT-Prüfer mit qES-/beA-/Formfiktion-Workflow, Arbeitszeugnis-Testakte, Legistik-Ausbau und die bisherigen Qualitätsbereinigungen.

---

# v19.1.0 — BGB AT, Arbeitszeugnis-Testakte und Legistik-Ausbau

- Neues Plugin `bgb-at-pruefer` mit 53 Skills zum BGB Allgemeiner Teil: Fallaufnahme, Anspruchsaufbau, Willenserklärung, Zugang, Vertragsschluss, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung.
- `bgb-at-pruefer` um einen eigenen qES-/beA-/Formfiktion-Skill erweitert: §§ 126, 126a, 130 BGB, § 130e ZPO, § 46h ArbGG, § 173 ZPO und BGH VIII ZR 155/23 / VIII ZR 159/23 werden jetzt als gemeinsamer BGB-AT-/Prozessrechts-Workflow geprüft.
- Neue synthetische Testakte `bgb-at-altfraenkische-werkstatt` mit Online-Auktion, Annahmefrist, Minderjährigenkauf, Vollmacht, Anfechtung, Bedingung, Form-/Sittenwidrigkeitsprüffeldern und beA-/qES-/Formfiktion-Nachtrag.
- Neue Testakte `arbeitszeugnis-analyse-bluehendes-leben` mit zehn vollständigen Arbeitszeugnissen aus zehn Branchen (PTA Apotheke, angestellter Anwalt, MTRA Radiologie, Lagermeister, ZFA, Filialleiterin Sparkasse, Speditionsdisponent, Hotel-Empfangsleiter, Wohnbereichsleitung Pflege, Industriemechanik); tatsächliche Noten verdeckt über gesamte Skala eins bis fünf, ohne Musterlösung.
- `methodenlehre-buergerliches-recht` und `subsumtions-pruefer` verweisen nun auf `bgb-at-pruefer`, wenn die abstrakte Methodik in konkrete BGB-AT-Mechanik überführt werden soll.

- Legistik-Werkstatt auf fünf Startbahnen erweitert: Bundesressort/Bundesregierung, Bundestag/Fraktion/Opposition, Landesressort/Landesregierung, Landtag/Landtagsfraktion und sonstige Normgeber.
- Legistik-Allgemein-Skill fragt jetzt Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Verfahrensstand, Drucksache, Geschäftsordnung und Outputformat ab und routet sauber in Spezial-Skills.
- `formulierungshilfe-bauen` kann jetzt nicht nur ministerielle Koalitions-Zulieferungen, sondern auch Gesetzentwürfe aus der Mitte, Änderungsanträge, Anträge und Entschließungsanträge für Bundestag und Landtage einschließlich Oppositionsarbeit.
- `legistik-auftragsaufnahme`, `normhierarchie-routing` und `referentenentwurf-bauen` trennen fachlichen Verfasser, formalen Initiator und politischen Auftraggeber und führen Landesverfassung, Landes-Geschäftsordnung, Landtags-GO und Verkündungsrecht als Pflichtprüfpunkte mit.
- Perplexitys stummer Upload-Block in allen 100 Allgemein-Skills geglättet: Fristenscan zuerst, Materialklassifikation, Kontextanker, Skill-Routing, nur eine konkrete Rückfrage und ein weniger begrenzender Co-Pilot-Ton.
- Testakten mit `.placeholder`-Dateinamen in Chatbeschreibungen, Bildbeschreibungen, Fehlblätter, Inhaltsvermerke und Validierungsnotizen umbenannt; README-Verweise entsprechend aktualisiert.
- Produktrecht-Skills von offenen Verify-/Pinpoint-Markern, einer nicht tragfähigen Produkthaftungsfundstelle und schematischen Influencer-/Green-Claims-Aussagen bereinigt.
- KI-Governance-Beispiele auf Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO für Bewerbungs-/Beschäftigungssysteme korrigiert und die allgemeine Chatbot/GPAI-Abgrenzung geschärft.
- BVerfG-Leitentscheidung "Soldaten sind Mörder" mit den konkreten Aktenzeichen ersetzt; Quellenhinweis auf geprüfte Primärquellen und Pinpoint-Nachtrag umgestellt.

---

# v19.0.0 — KI-VO-Härtung, BVG-Abschleppakte und Release-Stand

- `ki-vo-ai-act-pruefer` vertieft Art. 3 Nr. 1 KI-VO mit einem dokumentierbaren KI-System-Vermerk zu Automation, Autonomie, Adaptivität, Inferenz, Output und Umgebungseinfluss.
- Art. 6 Abs. 2 i.V.m. Anhang III ist neu aufgebaut: alle acht Bereiche mit Untertatbeständen, Zweckbestimmung, allgemeiner Chatbot/GPAI-Abgrenzung und Mitarbeitenden-Fehlgebrauch.
- Allgemeine Chatbots/GPAI werden ausdrücklich nicht automatisch als Hochrisiko behandelt; maßgeblich sind Anbieter-Zweckbestimmung, Betreiberzweck und tatsächliche Integration in Anhang-III-Prozesse.
- Art. 6 Abs. 3 wurde mit Profiling-Sperre, vier Fallgruppen, Grundrechtsrisiko und Art.-6-Abs.-4-Dokumentation geschärft.
- Normen-/Standards-Skill trennt harmonisierte Normen, gemeinsame Spezifikationen, GPAI Code of Practice und ISO/IEC-Standards ohne falsche Vermutungswirkung.
- Output-Dokumentation enthält jetzt Art.-3-Vermerk, Anhang-III-Matrix, Off-label-Governance, Re-Evaluation-Trigger und Standards-Hinweis.
- Perplexitys BVG-/ÖPNV-Abschleppmaterial ist in `main` integriert: neuer Verwaltungsrechts-Skill `fa-vwgo-widerspruchsbescheid-abschleppen-oepnv` und neue Testakte `bvg-widerspruchsstelle-abschleppen-mobg`.
- Die BVG-Testakte verwendet nun Lichtbildbeschreibungen statt Platzhalterdateien; die VG-Berlin-Fundstelle ist auf Urteil vom 30.05.2022, VG 11 K 298/21, mit Pressemitteilung vom 04.07.2022 korrigiert.
- `README.md`, `SKILLS.md`, `testakten/README.md` und der Allgemein-Skill des Verwaltungsrechts-Plugins spiegeln nun 2279 Skills, 50 Testakten und das neue Routing zum BVG-Widerspruchsbescheid wider.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `19.0.0`.
- `README.md` und `testakten/README.md` auf Stand 101 Plugins, 2331 Skills, 52 Testakten und Release `v19.1.0` aktualisiert.

---

# v18.0.0 — Allgemein-Skills als schöne Plugin-Einstiege

Version 18.0.0 ist ein repo-weiter Workflow-Release: Jedes Plugin hat nun einen eigenen `allgemein`-Einstiegsskill als schnellen Intake-, Workflow- und Routingpunkt.

- 34 fehlende `skills/allgemein/SKILL.md` neu angelegt.
- 66 vorhandene Allgemein-Skills mit einheitlichem Schnellstart-Workflow, Intake in 60 Sekunden, Sofort-Triage, Antwortformat und Routing-Regeln ergänzt.
- Jeder Allgemein-Skill enthält eine automatisch aus dem jeweiligen Plugin gezogene Liste der verfügbaren Spezial-Skills und soll bei Bedarf zwei bis fünf passende Folge-Skills mit Grund und erwartetem Output vorschlagen.
- `SKILLS.md` und README-Zählungen auf 2278 Skills aktualisiert.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `18.0.0`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 100 Plugins, 2278 Skills, 100 Allgemein-Skills mit Schnellstart-Workflow
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.1 — Insolvenzanfechtung-Audit, KI-Screening und Verteidigung

Version 17.5.1 ist ein gezielter Nachlauf nur für Insolvenzanfechtungsrecht. Der Schwerpunkt liegt auf den fehleranfälligen Normgruppen §§ 129, 130/131, 133, 134, 135, 142 und §§ 143-147 InsO, dem Reformstand nach der Anfechtungsreform 2017, den Fristen, dem Bargeschäft, Gesellschafterdarlehen und der Verteidigung des Anfechtungsgegners.

## Korrigiert und gehärtet

- **§§ 130/131 InsO:** kongruente und inkongruente Deckung wurden sauber getrennt; § 130 verlangt Kenntnis, während § 131 die objektive Monats-/Antragsnähe und die subjektiven Alternativen für den zweiten und dritten Monat abbildet.
- **§ 133 InsO:** Vorsatzanfechtung arbeitet nun mit Zehnjahresgrundtatbestand, Vierjahresfenster für Deckungshandlungen, Zahlungsvereinbarungsregel und der Zweijahresvariante für entgeltliche Verträge mit nahestehenden Personen.
- **§ 142 InsO:** Bargeschäft ist nicht mehr als starre 30-Tage-Regel beschrieben; die Skills prüfen unmittelbaren Leistungsaustausch nach Verkehrsauffassung, das Drei-Monats-Fenster für Arbeitsentgelt und die Sondergrenze bei § 133 InsO.
- **§ 135 InsO:** neuer eigener Skill für Gesellschafterdarlehen, Gesellschaftersicherheiten, Rückzahlungen, Besicherungen, Kleinbeteiligungs-/Sanierungsprivileg und Drittfinanzierungsvarianten.
- **§§ 143-147 InsO:** Rechtsfolgen, § 144 InsO, Rechtsnachfolge, Verjährung und Handlungen nach Verfahrenseröffnung wurden neu geordnet; Zinsen werden an § 143 Abs. 1 Satz 3 InsO, Verzug und § 291 BGB angebunden.
- **Verteidigung des Anfechtungsgegners:** neuer eigener Skill mit defensiver Matrix zu Normauswahl, Gläubigerbenachteiligung, Kenntnis, Bargeschäft, Entreicherung, § 144 InsO, Verjährung und Vergleich.

## KI-Anfechtungsworkflow

- Neuer Skill `inso-ki-anfechtungsansprueche-schuldnerakten` für die Auswertung von Schuldnerakten mit Quellenankern, Zahlungschronologie, Anfechtungskandidaten-Matrix, Human-Review-Markierungen und Evidenzlücken.
- Das System darf Anfechtungskandidaten identifizieren und strukturiert vorprüfen, ersetzt aber keine anwaltliche Wertung bei § 133 InsO, Gläubigerbenachteiligungsvorsatz, Kenntnisindizien, Sanierungsversuchen, Bargeschäftsverteidigung und komplexen Dreiecksverhältnissen.
- Insolvenzverwaltung und Fachanwalt-Insolvenz/Sanierung wurden mit demselben Prüfungsmaßstab synchronisiert, damit Verwalterseite, Klagevorbereitung und Verteidigung nicht auseinanderlaufen.

## Release-Stand

- 100 Plugins
- 2244 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.1`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- gezielte Suche nach alten Fehlmustern zu SanInsFoG/Reform 2017, § 130/§ 131, § 133, § 142, § 146 und § 135 InsO
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.0 — Text-/Quellenaudit, README-Gateway-Anleitung und Lobbyregister-API-Härtung

Version 17.5 finalisiert den nachgezogenen Hauptstand nach v17 und zieht die Repository-Dokumentation, Plugin-Versionen und Release-Artefakte auf einen einheitlichen Zwischenrelease. Schwerpunkt ist ein konservativer Qualitätsschnitt: weniger erfundene Fundstellen, bessere deutsche Beschreibungstexte, klarere README-Anleitung für alternative Claude-kompatible API-Endpunkte und ein belastbareres Lobbyregister-Plugin.

## Korrigiert und gehärtet

- **Rechtsprechungs- und Literaturhinweise:** mehrere falsch oder unsicher zugeordnete BGH-/Kapitalmarkt-/Corporate-Nachweise wurden entfernt oder durch passendere, überprüfbare Leitentscheidungen ersetzt; methodische Skills sollen nicht mehr mit frei erfundenen Aktenzeichen arbeiten.
- **Lobbyregister Bundestag:** die API-Hinweise wurden als lesende Kontroll- und Monitoring-Schicht geschärft. Mock-Artefakte verweisen auf den stabilen `current`-Schema-Pfad und dokumentieren den Stand `R2.21`, statt eine spekulative neue API-Version zu behaupten.
- **README:** die Anleitung zum Einhängen einer eigenen oder zwischengeschalteten Claude-/Anthropic-kompatiblen API wurde providerneutral neu gefasst, mit klarer Trennung zwischen Claude Code im Terminal und Desktop-/Cowork-Oberflächen.
- **Deutsche Beschreibungstexte:** Frontmatter-Descriptions und Marketplace-Texte wurden breit auf Umlaute, ß und lesbare deutsche Formulierungen bereinigt, ohne Pfade, Links oder technische IDs umzubenennen.
- **Testakten:** Lobbyregister-Testakten bleiben bewusst realistisch-fragmentarisch, enthalten aber keine spekulativen API-Abgabeversprechen. Die API wird für Suche, Exportvergleich, Monitoring und Plausibilisierung genutzt.

## Release-Stand

- 100 Plugins
- 2241 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der geänderten Lobbyregister-API-Mockdateien
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v16.0.0 — Halluzinationsbereinigung, Audit-Hardening und v15-Finalstand

Version 16 baut direkt auf `v15.0.0` auf und nimmt den dortigen Stand mit Lobbyregister-Plugin, Selbstvertreter-Plugins und Steuerberater-Werkzeugen vollständig mit. Der Schwerpunkt dieses Releases ist eine weitere Qualitätsschicht gegen erfundene oder falsch zugeordnete Rechtsprechungsnachweise.

## Korrigiert und gehärtet

- **KI-Governance / KI-VO:** falsche Altzuordnungen zu `EuGH C-203/22` wurden aus KI-VO-/Governance-Kontexten entfernt und auf den tatsächlich passenden DSGVO-Art.-15-Kontext umgestellt.
- **Insolvenzplan / StaRUG / Insolvenzverwaltung:** unsichere oder nicht verifizierbare BGH-Nachweise wie `VI ZR 184/17`, `IX ZR 238/17`, `IX ZB 32/21` und `IX ZR 18/19` wurden aus produktiven Skills entfernt, soweit keine belastbare Ersatzfundstelle vorlag.
- **Insolvenzrecht / D&O:** falsche `II ZR 234/18`- und `II ZR 199/19`-Zuordnungen wurden durch passende, überprüfte Leitentscheidungen ersetzt.
- **Squeeze-out:** der Handels-/Gesellschaftsrecht-Skill verweist nun auf DAT/Altana und Stollwerck statt auf eine falsche Insolvenz-/Haftungszuordnung.
- **Audit-Dokumentation:** `audit/HALLUZINATIONS_AUDIT_2026-05-27.md` dokumentiert die zusätzliche lokale Reparaturwelle und den Übergang auf `v16.0.0`.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `16.0.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Rest-Suche nach den bekannten problematischen Aktenzeichen-/Fundstellenmustern außerhalb der Audit-Historie

---

# v15.0.0 — Lobbyregister, Selbstvertreter, Steuerberater-Werkzeuge und Release-Finalisierung

Version 15 buendelt die nachgelieferten Perplexity-/Klar-Ausbauten mit dem neuen `lobbyregister-bundestag` Plugin und setzt den gesamten Marketplace auf einen einheitlichen Major-Stand.

## Neue und stark ausgebaute Inhalte

- **`lobbyregister-bundestag` neu:** 50 gefuehrte Skills fuer Registrierungspflicht, Ausnahmen, Portal-Eingabeplan, Finanzdaten, Regelungsvorhaben, Stellungnahmen/Gutachten, Verhaltenskodex, Aktualisierung, Bussgeldrisiken, RfS-Kommunikation und Revisionsspur.
- **Open Data/API V2 im Lobbyregister:** eigene Referenz, API-Abfrageplan, JSON-Mapping, Registerexport-Diff und Monitoringplan. Die API wird bewusst als lesende Kontrollschicht gefuehrt; Registrierung und Aktualisierung bleiben Portalhandlungen.
- **Drei Lobbyregister-Testakten:** Dublin-Bank mit Frankfurter Zweigniederlassung und Doppelregistrierungsproblem, Public-Affairs-Agentur Wasserstoff, Buergerinitiative Waldmoor. Alle drei enthalten API-/Export-Diff-Artefakte.
- **Selbstvertreter-Plugins:** Amtsgericht und Sozialgericht sind auf `main` integriert und in die Marketplace-/Release-Struktur aufgenommen.
- **Steuerberater-Werkzeuge:** `steuerrecht-anwalt-und-berater` enthaelt die neuen StB-Skills fuer BWA, SuSa, Lohn, Jahresabschluss, DBA, Mandantenkommunikation und Software-/Portalroutinen.
- **Audit-Fixes:** Halluzinations- und Aktenzeichen-Reparaturwellen aus den v14.2.x Hotfixes sind mitenthalten.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `15.0.0`

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der neuen Lobbyregister-Testakten
- Release-ZIP-Validierung ueber `scripts/validate-release-zips.py` im Build/Workflow

---

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

## Quellenhygiene-Hinweis

Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht aus Modellwissen erzeugt. Literatur darf nur mit vom Nutzer bereitgestellter Quelle oder lizenziertem Live-Zugriff verwendet werden.

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
- **`satzweise-notenmatrix`** — Bewertet jeden notenrelevanten Satz mit Schulnote von eins bis fuenf. Festes Raster: Steigerungsadverb plus Superlativ = 1, eins davon = 2, Grundaussage = 3, Einschraenkung oder "bemueht" = 4, Distanzformel = 5. Tabellarisches Ausgabeformat mit Themenbereich pro Satz — Datenbasis fuer Drift-Detektor und Gesamtnoten-Aggregation.
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
- **`stb-warnschreiben-krisensignale`** um Abschnitt "Warum gerade der Steuerberater" und "§ 102 StaRUG als Auslöser der StB-Hinweispflicht" erweitert — Steuerberater als externer Bestandteil des Krisenfrüherkennungssystems.
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

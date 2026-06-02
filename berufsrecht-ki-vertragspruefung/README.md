# berufsrecht-ki-vertragspruefung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsrecht-ki-vertragspruefung`) | [`berufsrecht-ki-vertragspruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-ki-vertragspruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Berufsrecht / KI-Vertragsprüfung — Rügeverfahren RAK Köln und Haftungsklage Habernau** (`berufsrecht-ki-rugekomitee-anwaltskammer-koeln-mandant-richtl-dr-rotbruch`) | [Gesamt-PDF lesen](../testakten/berufsrecht-ki-rugekomitee-anwaltskammer-koeln-mandant-richtl-dr-rotbruch/gesamt-pdf/berufsrecht-ki-rugekomitee-anwaltskammer-koeln-mandant-richtl-dr-rotbruch_gesamt.pdf) | [`testakte-berufsrecht-ki-rugekomitee-anwaltskammer-koeln-mandant-richtl-dr-rotbruch.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-berufsrecht-ki-rugekomitee-anwaltskammer-koeln-mandant-richtl-dr-rotbruch.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Hinweis: Inhaltlich verantwortlich ist Klotzkette. Die rechtlichen Bezugspunkte sind auf bestmöglichem Stand recherchiert; gleichwohl ersetzt keine Skill dieses Plugins die Prüfung durch einen spezialisierten Rechtsanwalt.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Berufsrecht KI-Vertragsprüfung (`berufsrecht-ki-vertragspruefung`, dieses Plugin) | [berufsrecht-ki-vertragspruefung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-ki-vertragspruefung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Worum es geht

Kanzleien, Steuerberatungen, Wirtschaftsprüfungsgesellschaften, Patentanwaltskanzleien und Notariate setzen zunehmend Legal-KI-Tools privater Anbieter ein (Recherche mit Sprachmodellen, Dokumentenanalyse, Vertragsgeneratoren, Chatbots). Sobald solche Tools mit Mandats- oder Beteiligtendaten gefüttert werden, betreten wir berufsrechtliches und strafrechtliches Terrain — nicht primär datenschutzrechtliches.

Dieses Plugin liefert eine **berufsrechtliche und strafrechtliche Forprüfung** des Anbietervertrags. Es ist keine vollwertige juristische Begutachtung. Es ist ein strukturierter Argumentationsapparat, mit dem die Kanzlei dem Anbieter sagen kann: "So, wie macht ihr das eigentlich? Wie gewährleistet ihr die Anforderungen aus § 43e BRAO Absatz 3? Wo ist eure ISO-27001-Zertifizierung? Wo steht 'no training' im Vertrag?".

## Maßstab

Maßgeblich ist die **Initiativstellungnahme des Deutschen Anwaltvereins Nr. 32/2025** (Juli 2025) zum KI-Einsatz in der anwaltlichen Praxis. Die BRAK-Stellungnahme vom Dezember 2024 ist demgegenüber zurückhaltender und wird in diesem Plugin nur kurz und kritisch eingeordnet — nicht als verbindlicher Maßstab herangezogen.

Zur strafrechtlichen Absicherung dient § 203 StGB als verbindendes Element für alle fünf Berufsgruppen.

## Berufsgruppen

| Beruf | Verschwiegenheit | Dienstleisterregelung | § 203 StGB |
|---|---|---|---|
| Rechtsanwalt | § 43a Abs. 2 BRAO | § 43e BRAO | Abs. 1 Nr. 3 |
| Steuerberater | § 57 Abs. 1 StBerG | § 62a StBerG | Abs. 1 Nr. 3 |
| Wirtschaftsprüfer | § 43 WPO | § 50a WPO (§ 59c bei BG) | Abs. 1 Nr. 3 |
| Patentanwalt | § 39a Abs. 2 PAO | § 39c PAO | Abs. 1 Nr. 3 |
| Notar | § 18 BNotO | § 26a BNotO | Abs. 1 Nr. 1 |

Die Dienstleisterregelungen sind nahezu wortgleich aufgebaut. Das Plugin abstrahiert die gemeinsame Prüfung und stellt pro Beruf eine Norm-Adapter-Tabelle bereit.

## Skills

| Skill | Zweck |
|---|---|
| `berufsrecht-ki-vertragspruefung-kaltstart-interview` | Beruf, Anbieter, Datenarten, Vertragstyp erfassen |
| `erforderlichkeit-dokumentieren` | Erforderlichkeit der Offenlegung (Abs. 1) — unternehmerischer Beurteilungsspielraum nach DAV |
| `verschwiegenheitsklausel-pruefen` | Textform, jedermann, zeitlich unbegrenzt, alle Berufsgeheimnisse |
| `strafrechtliche-belehrung-pruefen` | Belehrung über §§ 203, 204 StGB; Anlage Normtext |
| `subunternehmer-regelung-pruefen` | Zustimmungsvorbehalt, Weiterverpflichtung in Textform |
| `strafprozessuale-regelung-pruefen` | §§ 53a, 97 StPO — Widerspruchsrecht des Dienstleisters, Beschlagnahmefreiheit |
| `avv-grenzpruefung-datenschutz` | Schnittstelle zu Art. 28 DS-GVO — explizit andere Prüfung |
| `tom-und-zertifizierungen-pruefen` | TOM nach Art. 32 DS-GVO, ISO 27001, BSI C5, "no training", Zero-Retention |
| `cloud-act-und-drittstaat-pruefen` | Auslandsregelung Abs. 4; CLOUD Act; Professional Secrecy Addendum |
| `parallelnormen-andere-berufe` | Norm-Adapter pro Beruf — Mapping-Referenz |
| `gutachten-erstellen` | Zusammenfassendes Forprüfungs-Gutachten |
| `rueckfragebrief-an-anbieter` | Strukturierter Brief mit präzisen Anbieterfragen |
| `klauselvorschlaege` | Mustertexte für nachverhandelbare Klauseln |

## Outputs

- **Forprüfungs-Gutachten** mit Ampelbewertung (grün/gelb/rot) je Prüfpunkt
- **Rückfragebrief an den Anbieter** zur Klärung offener Versprechen
- **Klauselvorschläge** als Verhandlungsmaterial (Verschwiegenheit, "no training", Subunternehmerliste, EU/EWR-Beschränkung, Professional Secrecy Addendum)
- **Zertifizierungs- und Sicherheits-Checkliste** (ISO 27001, BSI C5, TOM Art. 32)

## Wichtiger Hinweis (mehrfach)

**Diese Forprüfung ist ausdrücklich keine Rechtsberatung.** Sie ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die berufsrechtliche und strafrechtliche Beurteilung des konkreten Einzelfalls bleibt der inhabilen Kanzlei (interne Compliance) bzw. einer beauftragten Spezialkanzlei vorbehalten.

## Quellenpolitik

- DAV-Stellungnahme 32/2025 als Hauptquelle (Berufsrecht IV ab S. 8, Datenschutz V S. 17-18)
- Memorandum einer Spezialkanzlei zu § 43e BRAO und § 203 StGB
- BT-Drs. 18/12940 für historische Genese von § 43e BRAO
- BRAK-Leitfaden Dezember 2024 nur am Rande
- BGH-Pinpoint mit Aktenzeichen und Randnummer
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Berufsrecht KI Vertragspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren... |
| `avv-grenzpruefung-datenschutz` | Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG. Prüfraster AVV-Prüfp... |
| `berufsrecht-ki-vertragspruefung-kaltstart-interview` | Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (... |
| `brki-anbieter-due-diligence` | Anbieter-Due-Diligence beim Einsatz von KI in der Kanzlei: Sitz, Rechtsform, Zertifizierungen (ISO 27001, SOC 2 Typ II), Datenhaltung, Subunternehmer, Auditierbarkeit, Datenschutz-Folgenabschaetzung. Strukturierte Bewertung mit Score je... |
| `brki-eu-us-dpf-transferpruefung` | Spezialfall Transfer nach USA unter EU-US-Data-Privacy-Framework DPF: Liste teilnehmender Unternehmen, Pruefraster fuer Wirksamkeit (Selbstzertifizierung, Annual-Recertification), Backup-Plan SCC Modul 2 plus TIA bei Verlust DPF. |
| `brki-rag-vertraulichkeit-spezial` | Spezialfall RAG-Architekturen mit Mandantenakten: Embedding-Speicher, Vektor-DB im EU-Hosting, Loeschkonzept Embedding bei Mandantenwiderruf, Trennung pro Mandat. Pruefraster und technische Mindestanforderungen. |
| `brki-rollout-trainings-workflow` | Workflow fuer KI-Rollout in der Kanzlei: Pilotgruppe, Trainings (Halbtages-Workshop), Approval-Prozess fuer eingesetzte Tools, Reviewer-Liste, Dokumentation, KPIs. Routet in berufsrecht-ki-vertragspruefung-kaltstart-interview. |
| `bro-grundlagen-ki-einsatz` | BRAO-Grundlagen fuer KI-Einsatz in der Kanzlei einfuehrend: § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienste, § 203 StGB Strafbarkeit Geheimnisverletzung, Datenschutz nach DSGVO und BDSG. Strukturierte Uebersicht zur Pflichtenkette bei... |
| `cloud-act-und-drittstaat-pruefen` | Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR werden als gleichwertig unterstellt. Drittstaaten benoetigen vergleichbares Schutzniveau. US-CLOUD Act und... |
| `datentransfer-eu-drittstaat` | Datentransfer EU nach Drittstaat: Angemessenheitsbeschluss EU-US-Data-Privacy-Framework, Standardvertragsklauseln Modul 2, Transfer Impact Assessment nach EuGH Schrems II. Pruefraster fuer US-KI-Anbieter, technische Massnahmen wie Tokeni... |
| `erforderlichkeit-dokumentieren` | Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist nach DAV-Stellungnahme zweiunddreissi... |
| `forensische-pruefung-prompt-injection` | Forensische Pruefung Prompt-Injection-Risiko: Indirekte Prompt-Injection ueber hochgeladene Dokumente, RAG-Vergiftung, Datenexfiltration. Pruefraster fuer Reviewer-Audit, Sandbox-Test, Sicherheits-Hardening durch Anbieter. Pflicht des An... |
| `gutachten-erstellen` | Erstelle das zusammenfassende Forprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lueckenliste H... |
| `kanzleisoftware-spezial-mandantendaten` | Spezialfall Kanzleisoftware mit KI-Funktionen (RA-MICRO, Datev DMS, Acta Nova, vRA): Mandantendaten in Cloud, KI-Funktion Volltextsuche, Diktat, Vertragsanalyse. Pruefraster fuer Einwilligung Mandant, Auftragsverarbeitung, Loeschkonzepte. |
| `klauselvorschlaege` | Liefere konkrete Mustertexte für Vertragsklauseln mit dem KI-Anbieter. Bausteine Verschwiegenheit Belehrung §§ 203 204 StGB Subunternehmer no training Zero-Retention EU-Hosting Audit-Recht Löschkonzept Professional Secrecy Addendum für U... |
| `mandanten-aufklaerungspflicht-ki` | Aufklaerungspflicht gegenueber Mandanten beim KI-Einsatz: § 43 BRAO Vertrauensverhaeltnis, § 13 BORA, BGH-Rechtsprechung zur Informationsweitergabe. Mustertexte Mandantenanschreiben und Mandatsvertrag. Pruefraster fuer notwendigen Inform... |
| `parallelnormen-andere-berufe` | Norm-Adapter-Referenz für alle fuenf Berufsgeheimnistraeger Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar. Mapping der Dienstleisterregelungen Verschwiegenheitspflichten und § 203 StGB-Tatbestaende. Sonderregeln für Ber... |
| `rueckfragebrief-an-anbieter` | Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und Drittstaat) Fragen... |
| `schwarmpruefung-mehrere-tools` | Mehrere KI-Tools im parallelen Einsatz pruefen: ein Vertrag pro Anbieter, datentechnische Verkettung, Aggregationsrisiko, Gesamt-DPIA. Pruefraster fuer Mandant der gleichzeitig ChatGPT Enterprise, MS 365 Copilot, Claude Enterprise einsetzt. |
| `spezial-anbietern-schriftsatz-brief-und-memo-bausteine` | Anbietern: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-belehrung-abschlussprodukt-und-uebergabe` | Belehrung: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-berufsrecht-sonderfall-und-edge-case` | Berufsrecht: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-berufsrechtliche-erstpruefung-und-mandatsziel` | Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bnoto-mehrparteien-konflikt-und-interessen` | Bnoto: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-brao-zahlen-schwellen-und-berechnung` | Brao: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gutachten-red-team-und-qualitaetskontrolle` | Gutachten: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klauseln-beweislast-und-darlegungslast` | Klauseln: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-legal-behoerden-gericht-und-registerweg` | Legal: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-notare-livequellen-und-rechtsprechungscheck` | Notare: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-patentanwaelte-verhandlung-vergleich-und-eskalation` | Patentanwaelte: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-privaten-risikoampel-und-gegenargumente` | Privaten: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rueckfragebrief-mandantenentscheidung` | Rueckfragebrief: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stberg-compliance-dokumentation-und-akte` | Stberg: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stellungnahme-formular-portal-und-einreichung` | Stellungnahme: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stgb-internationaler-bezug-und-schnittstellen` | Stgb: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strafrechtliche-tatbestand-beweis-und-belege` | Strafrechtliche: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertraegen-dokumentenmatrix-und-lueckenliste` | Vertraegen: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertragspruefung-fristennotiz-und-naechster-schritt` | Vertragspruefung: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vorpruefung-fristen-form-und-zustaendigkeit` | Vorpruefung: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `strafprozessuale-regelung-pruefen` | Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunfts... |
| `strafrechtliche-belehrung-pruefen` | Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Ver... |
| `subunternehmer-regelung-pruefen` | Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste Weiterverpflichtung in Textform B... |
| `tom-und-zertifizierungen-pruefen` | Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no tra... |
| `verschwiegenheitsklausel-pruefen` | Prüfe die vertragliche Verpflichtung des Dienstleisters auf Verschwiegenheit nach Absatz drei der einschlaegigen Dienstleisterregelung (§§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO). Anforderungen Textform (§ 126b BGB) Verpflichtung... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin berufsrecht-ki-vertragspruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin berufsrecht-ki-vertragspruefung: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin berufsrecht-ki-vertragspruefung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin berufsrecht-ki-vertragspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin berufsrecht-ki-vertragspruefung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin berufsrecht-ki-vertragspruefung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin berufsrecht-ki-vertragspruefung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

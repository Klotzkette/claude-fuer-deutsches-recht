# Immobilienrechtspraxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`immobilienrechtspraxis`) | [`immobilienrechtspraxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/immobilienrechtspraxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Grundstückskauf / Baulast / Mehrfamilienhaus Rosenmündl — Stuttgart-Ost** (`grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost`) | [Gesamt-PDF lesen](../testakten/grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost/gesamt-pdf/grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost_gesamt.pdf) | [`testakte-grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Werkzeuge für immobilienrechtliche Rechtsabteilungen — musterbasierte Vertragserstellung mit Klauselschutz; Vertragsprüfung gegen Playbook; Grundbuchanalyse; Sachverhaltsermittlung; Mieteranfragen mit BGH-Verankerung; Case Management; projektbasierte Arbeitsweise mit AVV-Prüfung.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Immobilienrechtspraxis (`immobilienrechtspraxis`, dieses Plugin) | [immobilienrechtspraxis.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/immobilienrechtspraxis.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `case-management` | KI-gestütztes Case Management für immobilienrechtliche Vorgänge. Pro Fall werden Akte Korrespondenz Verträge Schriftsätze und Fristen strukturiert dokumentiert und fortgeschrieben. Erzeugt Fallübersicht in Markd… |
| `grundbuchanalyse` | Strukturierte Auswertung großer Mengen Grundbuchdaten — Grundbuchauszüge Flurkarten Baulastenverzeichnis Altlastenkataster. Extrahiert pro Objekt Eigentümerkette Belastungen in Abteilung II und III Rang Löschungse… |
| `mieteranfragen-bearbeitung` | Bearbeitet eingehende mietrechtliche Anfragen — Mietmängelanzeigen Kündigungen Mieterhöhungsverlangen Widersprüche nach § 574 BGB Betriebskosten-Einwendungen Untervermietungsanfragen — und erstellt fundierte Antwo… |
| `projekt-arbeitsweise` | Strukturierte Projekt- und Ordnerarbeit für immobilienrechtliche Rechtsabteilungen statt freihändigem Prompting. Pro Mandat oder Objekt entsteht ein Projekt-Ordner mit fixierten Vorgaben — Playbook Musterverträge K… |
| `sachverhaltsermittlung` | Unterstützt Inhouse-Juristen bei der zeitraubendsten Phase eines Vorgangs — der Sachverhaltsermittlung. Statt sofort den vollen Sachverhalt zu fordern, führt der Skill einen strukturierten Frageprozess in mehreren S… |
| `vertragserstellung-musterbasiert` | Erstellt immobilienrechtliche Verträge strikt auf Basis hausinterner Musterverträge und Term Sheets. Kernregel ist Klauselschutz — vorgegebene Musterklauseln werden NICHT umformuliert. KI füllt nur markierte Platzh… |
| `vertragspruefung-playbook` | Prüft externe Immobilienverträge gegen das hauseigene Playbook der Rechtsabteilung. Drei Ausgaben — Ampelmatrix nach Klauselkatalog, Redline-Empfehlung als chirurgische Tracked Changes und Business-Memo für das Ass… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Immobilienrechtspraxis-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsp... |
| `case-management` | Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output: Case-Management-Übersicht Im... |
| `grundbuchanalyse` | Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse, Löschungsansprüche. Output: Grundbuch... |
| `immo-aufteilungsplan-weg` | Aufteilungsplan WEG: Voraussetzungen § 8 WEG, Teilungserklaerung, Aufteilungsplan, Gemeinschaftsordnung. Pruefraster und Hinweise fuer den Notar. |
| `immo-bauliche-veraenderung-weg` | Bauliche Veraenderung im WEG nach § 20 WEG (Reform 2020): Beschlusserfordernisse, privilegierte Massnahmen (Barrierefreiheit, Lademoeglichkeit E-Auto, Glasfaser, Einbruchschutz). Pruefraster. |
| `immo-bauvertrag-vob-b` | Bauvertrag nach VOB-B oder BGB §§ 650a ff. BGB: Wahl Recht, Abnahme, Maengelrechte, Sicherheiten, Vergutung Stundenlohnarbeiten, Nachtraege. Pruefraster fuer beide Vertragstypen. |
| `immo-energieausweis` | Energieausweis: Pflicht GEG 2024, Vorlage bei Verkauf/Vermietung, Bussgeldrisiko. Beratung Verkaeufer/Vermieter Beschaffung. |
| `immo-gewerbliche-mieter-konkurs` | Gewerbliche Mieter in der Insolvenz: § 109 InsO Wahlrecht Insolvenzverwalter, Kuendigung trotz fester Mietzeit. Pruefraster fuer Vermieter. |
| `immo-grundschuld-bestellung` | Grundschuldbestellung: Vorlage Notarsurkunde, Sicherungsabrede, Verbraucher-Sicherungs-AGB §§ 305 ff. BGB, Beschraenkungen Vollstreckung bei Verbraucher. Loeschungsbewilligung nach Tilgung. |
| `immo-kaufvertrag-grundstueck` | Grundstueckskaufvertrag pruefen: § 311b BGB notarielle Beurkundung, Auflassung § 925 BGB, Eintragung Auflassungsvormerkung § 883 BGB, Kaufpreiszahlung, Vollzugspflichten, Sicherheiten. Pruefraster. |
| `immo-makler-honorar` | Maklervertrag und Honorar: § 652 BGB Maklerlohn, Nachweismakler/Verhandlungsmakler, § 656d BGB Verbraucher-Wohnimmobilien Halbteilungsgrundsatz, Hinweis Doppelmaklertaetigkeit § 654 BGB. Pruefraster. |
| `immo-mietkaufvertrag` | Mietkaufvertrag: Aufbau, Steuerrecht, Kostenfallen, Reform 2025 (falls relevant). Pruefraster Vor- und Nachteile vs. klassischem Kaufvertrag. |
| `immo-share-deal-grunderwerbsteuer` | Immobilien Share Deal Grunderwerbsteuer §§ 1 Abs. 2a, Abs. 2b, Abs. 3 GrEStG: Schwellen 90 Prozent, 5/10 Jahre Halte. Vergleich Asset Deal vs. Share Deal. Auswirkungen MoPeG. |
| `immo-wohnungseigentum-grundlagen` | Wohnungseigentumsrecht Grundlagen: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, Verwalter, Eigentuemerversammlung. Reform WEMoG 2020. Mandantenkommunikation. |
| `immo-zwangsversteigerung-verfahren` | Zwangsversteigerung Verfahren: Antrag, Wertgutachten, Termin, Mindestgebot, Sicherheitsleistung. Strategie fuer Glaeubiger und fuer Schuldner (Vollstreckungsschutz § 765a ZPO). |
| `immor-bauvertrag-vob-bgb-leitfaden` | Leitfaden Bauvertrag VOB-B und BGB-Bauvertrag §§ 650a ff. BGB: Anordnungsrecht, Vereinbarung VOB-B als AGB, Abnahme, Maengelrechte. Pruefraster Bauherr und Unternehmer. |
| `immor-bodenrichtwert-bewertung-spezial` | Spezialfall Bodenrichtwert und Bewertung im Erb- und Steuerfall: ImmoWertV 2021, Vergleichswertverfahren, Ertragswertverfahren. Pruefraster fuer Finanzamt und Gutachter. |
| `immor-erbbaurecht-vertrag-spezial` | Spezialfall Erbbaurechtsvertrag: ErbbauRG, Erbbauzins, Heimfall, Entschaedigung. Pruefraster fuer kirchliche und kommunale Grundstuecksverwaltung. |
| `immor-grundstueckskaufvertrag-bauleiter` | Bauleiter Grundstueckskaufvertrag: Form § 311b BGB, Belastungsvollmacht, Faelligkeitsvoraussetzungen, Abloesung Grundpfandrechte. Pruefraster Kaeufer und Verkaeufer. |
| `mieteranfragen-bearbeitung` | Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kündigung. Normen: §§ 535 536 556 573 BGB, WEG. Prüfraster: Anfragetyp, Rechtsgrundlage, Fristen, Handlungspflichten. Output: Bearbeitungsprotokoll Mietera... |
| `projekt-arbeitsweise` | Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan Immobilienrechtsma... |
| `sachverhaltsermittlung` | Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-... |
| `spezial-case-internationaler-bezug-und-schnittstellen` | Case: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gegen-verhandlung-vergleich-und-eskalation` | Gegen: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grundbuchanalyse-zahlen-schwellen-und-berechnung` | Grundbuchanalyse: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-immo-abschlussprodukt-und-uebergabe` | Immo: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-immobilienrechtliche-tatbestand-beweis-und-belege` | Immobilienrechtliche: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-immobilienrechtspraxis-frist-naechster-schritt` | Immobilienrechtspraxis: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klauselschutz-behoerden-gericht-und-registerweg` | Klauselschutz: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-live-beweislast-und-darlegungslast` | Live: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-management-formular-portal-und-einreichung` | Management: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mieteranfragen-mehrparteien-konflikt-und-interessen` | Mieteranfragen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-musterbasierte-dokumentenmatrix-und-lueckenliste` | Musterbasierte: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-playbook-livequellen-und-rechtsprechungscheck` | Playbook: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefung-red-team-und-qualitaetskontrolle` | Pruefung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsabteilungen-fristen-form-und-zustaendigkeit` | Rechtsabteilungen: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsprechung-mandantenentscheidung` | Rechtsprechung: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sachverhaltsermittlung-compliance-dokumentation-und-akte` | Sachverhaltsermittlung: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verifikation-sonderfall-und-edge-case` | Verifikation: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertragserstellung-risikoampel-und-gegenargumente` | Vertragserstellung: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertragspruefung-schriftsatz-brief-und-memo-bausteine` | Vertragspruefung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-werkzeuge-erstpruefung-und-mandatsziel` | Werkzeuge: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `vertragserstellung-musterbasiert` | Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsen... |
| `vertragspruefung-playbook` | Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und Formerfordernisse. Output:... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin immobilienrechtspraxis: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin immobilienrechtspraxis: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin immobilienrechtspraxis: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin immobilienrechtspraxis: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin immobilienrechtspraxis: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin immobilienrechtspraxis: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin immobilienrechtspraxis: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin immobilienrechtspraxis: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin immobilienrechtspraxis: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin immobilienrechtspraxis: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

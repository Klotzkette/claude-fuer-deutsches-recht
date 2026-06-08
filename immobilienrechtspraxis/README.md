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

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Immobilienrechtspraxis: wählt den nächsten Spezial-Skill nach Engpass (Vormerkung, Notarvertrag, Grundbuchauszug, Energieausweis), dokumentiert Router-Entscheidung mit Begründung. |
| `betriebskostenabrechnung-erstellen-asset-management` | Betriebskostenabrechnung im Asset- und Property-Management erstellen: Mietvertragsklauseln, BetrKV-Mapping, WEG- oder Objektbuchhaltung, HeizkostenV, CO2KostAufG, Gewerbe-Vorwegabzug, Vorauszahlungskonto, Versand und Belegpaket im Immobi... |
| `betriebskostenabrechnung-pruefen-asset-management` | Betriebskostenabrechnung im Immobilienportfolio prüfen: formelle Mindestangaben, Fristen, Umlagefähigkeit, Buchhaltungsabgleich, WEG-zu-Mieter-Übersetzung, Zahlungsbelege, Wirtschaftlichkeit, HeizkostenV, CO2KostAufG und Streitwertkalkul... |
| `case-gegen-grundbuchanalyse` | Case: Internationaler Bezug und Schnittstellen im Immobilienrechtspraxis. |
| `case-management-grundbuchanalyse-immo` | Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output: Case-Management-Übersicht Im... |
| `dokumente-intake` | Dokumentenintake für Immobilienrechtspraxis: sortiert Notarvertrag, Grundbuchauszug, Energieausweis, prüft Datum, Absender, Frist und Beweiswert (Grundbuchauszug, Verkehrswertgutachten); markiert Lücken; berücksichtigt Mandatsgeheimnis §... |
| `einstieg-routing` | Einstieg, Triage und Routing für Immobilienrechtspraxis: ordnet Rolle (Käufer, Verkäufer, Notar), markiert Frist (Vormerkung), wählt Norm (BGB §§ 433/873/925, GrEStG, GBO) und Zuständigkeit (Grundbuchamt), leitet zum passenden Spezial-Sk... |
| `gegen-verhandlung-vergleich-und-eskalation` | Gegen: Verhandlung, Vergleich und Eskalation im Immobilienrechtspraxis. |
| `grundbuchanalyse` | Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse, Löschungsansprüche. Output: Grundbuch... |
| `grundbuchanalyse-zahlen-schwellen-und-berechnung` | Grundbuchanalyse: Zahlen, Schwellenwerte und Berechnung im Immobilienrechtspraxis. |
| `immo-aufteilungsplan-weg` | Aufteilungsplan WEG: Voraussetzungen § 8 WEG, Teilungserklaerung, Aufteilungsplan, Gemeinschaftsordnung. Pruefraster und Hinweise für den Notar im Immobilienrechtspraxis. |
| `immo-bauliche-veraenderung-energieausweis` | Bauliche Veraenderung im WEG nach § 20 WEG (Reform 2020): Beschlusserfordernisse, privilegierte Massnahmen (Barrierefreiheit, Lademoeglichkeit E-Auto, Glasfaser, Einbruchschutz). Pruefraster im Immobilienrechtspraxis. |
| `immo-bauvertrag-vob-kaufvertrag-grundstueck` | Bauvertrag nach VOB-B oder BGB §§ 650a ff. BGB: Wahl Recht, Abnahme, Maengelrechte, Sicherheiten, Vergutung Stundenlohnarbeiten, Nachtraege. Pruefraster für beide Vertragstypen im Immobilienrechtspraxis. |
| `immo-energieausweis` | Energieausweis: Pflicht GEG 2024, Vorlage bei Verkauf/Vermietung, Bussgeldrisiko. Beratung Verkaeufer/Vermieter Beschaffung im Immobilienrechtspraxis. |
| `immo-gewerbliche-mieter-konkurs` | Gewerbliche Mieter in der Insolvenz: § 109 InsO Wahlrecht Insolvenzverwalter, Kuendigung trotz fester Mietzeit. Pruefraster für Vermieter im Immobilienrechtspraxis. |
| `immo-grundschuld-bestellung-makler-honorar` | Grundschuldbestellung: Vorlage Notarsurkunde, Sicherungsabrede, Verbraucher-Sicherungs-AGB §§ 305 ff. BGB, Beschraenkungen Vollstreckung bei Verbraucher. Loeschungsbewilligung nach Tilgung im Immobilienrechtspraxis. |
| `immo-immobilienrechtliche-live-beweislast` | Immo: Abschlussprodukt und Übergabe im Immobilienrechtspraxis. |
| `immo-kaufvertrag-grundstueck` | Grundstueckskaufvertrag pruefen: § 311b BGB notarielle Beurkundung, Auflassung § 925 BGB, Eintragung Auflassungsvormerkung § 883 BGB, Kaufpreiszahlung, Vollzugspflichten, Sicherheiten. Pruefraster im Immobilienrechtspraxis. |
| `immo-makler-honorar` | Maklervertrag und Honorar: § 652 BGB Maklerlohn, Nachweismakler/Verhandlungsmakler, § 656d BGB Verbraucher-Wohnimmobilien Halbteilungsgrundsatz, Hinweis Doppelmaklertaetigkeit § 654 BGB. Pruefraster im Immobilienrechtspraxis. |
| `immo-mietkaufvertrag` | Mietkaufvertrag: Aufbau, Steuerrecht, Kostenfallen, Reform 2025 (falls relevant). Pruefraster Vor- und Nachteile vs. klassischem Kaufvertrag im Immobilienrechtspraxis. |
| `immo-share-deal-grunderwerbsteuer` | Immobilien Share Deal Grunderwerbsteuer §§ 1 Abs. 2a, Abs. 2b, Abs. 3 GrEStG: Schwellen 90 Prozent, 5/10 Jahre Halte. Vergleich Asset Deal vs. Share Deal. Auswirkungen MoPeG im Immobilienrechtspraxis. |
| `immo-wohnungseigentum-grundlagen` | Wohnungseigentumsrecht Grundlagen: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, Verwalter, Eigentuemerversammlung. Reform WEMoG 2020. Mandantenkommunikation im Immobilienrechtspraxis. |
| `immo-zwangsversteigerung-frist-naechster` | Zwangsversteigerung Verfahren: Antrag, Wertgutachten, Termin, Mindestgebot, Sicherheitsleistung. Strategie für Glaeubiger und für Schuldner (Vollstreckungsschutz § 765a ZPO) im Immobilienrechtspraxis. |
| `immobilienrechtliche-tatbestand-beweis-und-belege` | Immobilienrechtliche: Tatbestandsmerkmale, Beweisfragen und Beleglage im Immobilienrechtspraxis. |
| `immobilienrechtspraxis-frist-naechster-schritt` | Immobilienrechtspraxis: Fristennotiz und nächster Schritt im Immobilienrechtspraxis. |
| `immor-bauvertrag-vob-erbbaurecht-vertrag` | Leitfaden Bauvertrag VOB-B und BGB-Bauvertrag §§ 650a ff. BGB: Anordnungsrecht, Vereinbarung VOB-B als AGB, Abnahme, Maengelrechte. Pruefraster Bauherr und Unternehmer im Immobilienrechtspraxis. |
| `immor-bodenrichtwert-betriebskostenabrechnung` | Spezialfall Bodenrichtwert und Bewertung im Erb- und Steuerfall: ImmoWertV 2021, Vergleichswertverfahren, Ertragswertverfahren. Pruefraster für Finanzamt und Gutachter im Immobilienrechtspraxis. |
| `immor-erbbaurecht-vertrag-spezial` | Spezialfall Erbbaurechtsvertrag: ErbbauRG, Erbbauzins, Heimfall, Entschaedigung. Pruefraster für kirchliche und kommunale Grundstuecksverwaltung im Immobilienrechtspraxis. |
| `immor-grundstueckskaufvertrag-bauleiter` | Bauleiter Grundstueckskaufvertrag: Form § 311b BGB, Belastungsvollmacht, Faelligkeitsvoraussetzungen, Abloesung Grundpfandrechte. Pruefraster Kaeufer und Verkaeufer im Immobilienrechtspraxis. |
| `klauselschutz-vertragserstellung` | Klauselschutz: Behörden-, Gerichts- oder Registerweg im Immobilienrechtspraxis. |
| `live-beweislast-und-darlegungslast` | Live: Beweislast, Darlegungslast und Substantiierung im Immobilienrechtspraxis. |
| `management-mieteranfragen-interessen` | Management: Formular, Portal und Einreichungslogik im Immobilienrechtspraxis. |
| `mandant-redteam-gate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Immobilienrechtspraxis. |
| `mieteranfragen-bearbeitung-projekt` | Mieteranfragen im Immobilienportfolio bearbeiten: Mängel, Betriebskosten, Belegeinsicht, Kündigung, Mieterhöhung und Mietpreisbremse; mit Fristen, Zuständigkeit, Antwortentwurf, Aktenvermerk und Anschluss an die Betriebskosten-/WEG-Daten... |
| `mieteranfragen-mehrparteien-konflikt-und-interessen` | Mieteranfragen: Mehrparteienkonflikt und Interessenmatrix im Immobilienrechtspraxis. |
| `musterbasierte-dokumentenmatrix-und-lueckenliste` | Musterbasierte: Dokumentenmatrix, Lückenliste und Nachforderung im Immobilienrechtspraxis. |
| `output-waehlen` | Output-Wahl für Immobilienrechtspraxis: stimmt Adressat (Käufer, Verkäufer, Notar), Frist (Vormerkung) und Form auf den Zweck ab — typische Outputs: Kaufvertragsentwurf, Due-Diligence-Bericht, Übergabeprotokoll. |
| `playbook-quellenkarte` | Playbook Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `projekt-arbeitsweise` | Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan Immobilienrechtsma... |
| `pruefung-fehlerkatalog` | Prüfung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `quellen-livecheck` | Quellen-Live-Check für Immobilienrechtspraxis: prüft Normen (BGB §§ 433/873/925, GrEStG, GBO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Grundbuchamt und Quellenhygiene nach references/quellenhygiene.md. |
| `rechtsabteilungen-fristen-form-und-zustaendigkeit` | Rechtsabteilungen: Fristen, Form, Zuständigkeit und Rechtsweg im Immobilienrechtspraxis. |
| `rechtsprechung-mandantenentscheidung` | Rechtsprechung: Mandantenkommunikation und Entscheidungsvorlage im Immobilienrechtspraxis. |
| `sachverhaltsermittlung` | Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-... |
| `sachverhaltsermittlung-verifikation` | Sachverhaltsermittlung: Compliance-Dokumentation und Aktenvermerk im Immobilienrechtspraxis. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Immobilienrechtspraxis-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Immobilienrechtspraxis: trennt fehlende Tatsachen von fehlenden Belegen (Notarvertrag, Grundbuchauszug, Energieausweis), nennt pro Lücke Beweisthema, Beschaffungsweg (Grundbuchamt), Frist und Ersatznachw... |
| `verifikation-sonderfall-und-edge-case` | Verifikation: Sonderfall und Edge-Case-Prüfung im Immobilienrechtspraxis. |
| `vertragserstellung-musterbasiert` | Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsen... |
| `vertragserstellung-risikoampel-und-gegenargumente` | Vertragserstellung: Risikoampel, Gegenargumente und Verteidigungslinien im Immobilienrechtspraxis. |
| `vertragspruefung-playbook` | Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und Formerfordernisse. Output:... |
| `vertragspruefung-schriftsatz-brief-und-memo-bausteine` | Vertragspruefung: Schriftsatz-, Brief- und Memo-Bausteine im Immobilienrechtspraxis. |
| `weg-abrechnung` | WEG Abrechnung im Plugin Immobilienrechtspraxis im Immobilienrechtspraxis. |
| `werkzeuge-erstpruefung-und-mandatsziel` | Werkzeuge: Erstprüfung, Rollenklärung und Mandatsziel im Immobilienrechtspraxis. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Immobilienrechtspraxis. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Immobilienrechtspraxis. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Immobilienrechtspraxis. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

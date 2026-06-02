# Vertragsausfüller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`vertragsausfueller`) | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vertragsausfueller - BSAG Kiosk Huckelriede** (`vertragsausfueller-bsag-kiosk-huckelriede`) | [Gesamt-PDF lesen](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für workflowgestütztes Ausfüllen von Vertragsvorlagen und Altverträgen. Ein Nutzer lädt eine Word-Vorlage, einen alten Vertrag, ein Term Sheet oder Freitextdaten hoch. Das Plugin strippt das Dokument, erkennt Felder und Klauseln, fragt fehlende Daten ab, mappt Term-Sheet-Daten auf Vertragsfelder und erstellt daraus einen neuen Vertragsentwurf.

Der BSAG-Mietvertrag und das Term Sheet Kiosk Huckelriede sind als Beispielakte eingebunden.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| vertragsausfueller | [vertragsausfueller.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |

Zusatzmaterial:
- [Vorschau lokal öffnen](./assets/vorschau/index.html)

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Vertragsausfueller - BSAG Kiosk Huckelriede** ([`testakten/vertragsausfueller-bsag-kiosk-huckelriede/`](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/)).

Direkt-Download als ZIP: [testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `vertragsausfueller.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Fülle diesen Mietvertrag mit den Daten aus dem Term Sheet aus.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vertragsausfueller@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` enthalten.

## Workflow

1. Vorlage oder alten Vertrag hochladen.
2. Dokument strippen: Absätze, Tabellen, Platzhalter, Klauseln, Anlagen und Signaturen erkennen.
3. Term Sheet, E-Mail oder Freitextdaten danebenlegen.
4. Feldinventar und Mapping erzeugen.
5. Fehlende Daten freundlich abfragen oder als offene Platzhalter markieren.
6. Clean-Vertrag erstellen.
7. Nur auf ausdrückliche Nachfrage zusätzlich Track Changes oder Redline vorbereiten.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| vaf-kommandocenter | steuert den gesamten Workflow von Upload bis neuem Vertragsentwurf. |
| vaf-docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| vaf-template-erkennung | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| vaf-feldinventar | baut die zentrale Datenmatrix für den Vertrag. |
| vaf-termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| vaf-rueckfrageninterview | füllt Datenlücken ohne den Nutzer zu überfordern. |
| vaf-bsag-mietvertrag | setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. |
| vaf-klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| vaf-plausibilitaetscheck | härtet den Entwurf vor Versand oder Verhandlung. |
| vaf-clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| vaf-track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| vaf-redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| vaf-altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| vaf-quality-gate | ist die letzte Schleuse vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `vaf-bsag-mietvertrag` mappt daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung.

## Track-Changes-Regel

Das Plugin erzeugt keine Track-Changes- oder Redline-Fassung stillschweigend. Es fragt immer ausdrücklich: Soll zusätzlich eine Track-Changes- oder Redline-Fassung erstellt werden? Ohne Bestätigung bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Vertragsausfueller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `spezial-altvertraege-dokumentenmatrix-und-lueckenliste` | Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ausdruecklicher-fristennotiz-und-naechster-schritt` | Ausdruecklicher: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-changes-beweislast-und-darlegungslast` | Changes: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-docx-tatbestand-beweis-und-belege` | Docx: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erkennen-schriftsatz-brief-und-memo-bausteine` | Erkennen: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erzeugen-red-team-und-qualitaetskontrolle` | Erzeugen: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fassungen-sonderfall-und-edge-case` | Fassungen: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-felder-behoerden-gericht-und-registerweg` | Felder: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fuehren-mehrparteien-konflikt-und-interessen` | Fuehren: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mappen-zahlen-schwellen-und-berechnung` | Mappen: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nachfrage-abschlussprodukt-und-uebergabe` | Nachfrage: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-neue-internationaler-bezug-und-schnittstellen` | Neue: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rueckfragen-compliance-dokumentation-und-akte` | Rueckfragen: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sheets-livequellen-und-rechtsprechungscheck` | Sheets: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strippen-risikoampel-und-gegenargumente` | Strippen: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-term-verhandlung-vergleich-und-eskalation` | Term: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-track-mandantenkommunikation-entscheidungsvorlage` | Track: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertraege-formular-portal-und-einreichung` | Vertraege: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertragsausfueller-erstpruefung-und-mandatsziel` | Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vorlagen-fristen-form-und-zustaendigkeit` | Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `vaf-altvertrag-nachziehen` | Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder Gesetzesänderungen. §§ 305 ff. BGB... |
| `vaf-batch-modus-konzern` | Batch-Modus fuer Konzernvertraege: viele aehnliche Vertraege mit wechselnden Parteien und Werten, Massendatenimport CSV/XLSX, Plausibilitaetsregel-Set, Output 1 PDF pro Datensatz. Quality Gate und Reviewer-Sample. |
| `vaf-bsag-mietvertrag` | BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB Schriftformerfordernis. Prüfrast... |
| `vaf-clean-output` | Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand erstellt. §§ 125 ff. BG... |
| `vaf-docx-stripper` | DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstr... |
| `vaf-einfuehrung-prozess` | Einfuehrung Prozess Vertragsausfueller: vom Mandanteninterview ueber Variableninventar zum Template, Klauselentscheidung, Plausibilitaetscheck, Quality Gate. Schaubild und Reihenfolge der Sub-Skills. |
| `vaf-feldinventar` | Feldinventar für Vertragsgenerator erstellen: Anwendungsfall Anwalt oder Mandant will wissen welche Felder im Vertrag auszufüllen sind bevor Rückfrageninterview startet. §§ 550 BGB Schriftformerfordernis Mietvertrag, § 2 NachwG Arbeitsve... |
| `vaf-fragebogen-input-leitfaden` | Leitfaden Fragebogen-Input fuer Vertragsausfueller: Reihenfolge, Validierung, Plausibilitaet, Mandantenfreundlichkeit. Pruefraster fuer UX-Tests. |
| `vaf-fremdsprachige-vertraege-bilingual` | Spezialfall fremdsprachige und bilinguale Vertraege: Sprache fuer rechtlich verbindliche Auslegung definieren, Konsistenz Glossar, Uebersetzung als Anlage. Risiken bei Verwendung von DeepL und LLM. Pruefraster und Mustertexte. |
| `vaf-klauselentscheidung` | Wahlklauseln und Klauselalternativen im Vertrag entscheiden: Anwendungsfall Vertrag enthält optionale Klauseln wie Umsatzsteueroption Indexierung Konkurrenzschutz Rückbau oder Betriebspflicht die aktiv angekreuzt oder formuliert werden m... |
| `vaf-kommandocenter` | Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen Workflow. Vertragsrecht... |
| `vaf-konzern-rahmenvertrag-anpassen` | Spezialfall Rahmenvertrag im Konzern anpassen ohne Aenderung der Substanz: typische Stellen wie Vergueng, Laufzeit, Liefermenge. Pruefraster fuer Aenderungsfreigabe und Track-Changes-Diskussion mit Gegenseite. Mustertexte. |
| `vaf-mehrsprachige-vertraege-spezial` | Spezialfall mehrsprachige Vertraege deutsch / englisch: massgebliche Sprache, paralleler Aufbau, Uebersetzungsfehler. Pruefraster fuer internationale Mandate. |
| `vaf-platzhalterlogik-bauleiter` | Bauleiter Platzhalterlogik: Variablen, Pflichtfelder, optionale Bloecke, Konditionalen. Pruefraster fuer Templatebau und Fehlerquellen. |
| `vaf-plausibilitaetscheck` | Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klaus... |
| `vaf-quality-gate` | Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-30... |
| `vaf-redline-qa` | Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollständigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft werden. §§ 145 ff. BG... |
| `vaf-rueckfrageninterview` | Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene Pflichtfelder nach Prior... |
| `vaf-template-erkennung` | Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln identifizieren. §§ 433 f... |
| `vaf-template-format-und-source` | Template-Format und Quelle: Word-DOCX mit Formularfeldern, Markdown mit Platzhaltern, PDF AcroForm, Excel mit Variablenliste. Pro Format: Vor- und Nachteile, Migration, Backup. Pflicht zu sauberer Versionierung. |
| `vaf-termsheet-mapping` | Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten muessen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent, Klausel-Bibliothek Vert... |
| `vaf-track-changes-nur-nach-frage` | Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhan... |
| `vaf-versionierung-aenderungsverfolgung-spezial` | Spezialfall Versionierung und Aenderungsverfolgung in Vertragsdokumenten: Track Changes, Blackline, automatisierter Diff. Pruefraster fuer Reviewteam. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin vertragsausfueller: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin vertragsausfueller: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin vertragsausfueller: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin vertragsausfueller: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin vertragsausfueller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin vertragsausfueller: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin vertragsausfueller: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin vertragsausfueller: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin vertragsausfueller: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin vertragsausfueller: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

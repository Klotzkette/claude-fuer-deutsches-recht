# Vertragsausfüller

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`vertragsausfueller.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/vertragsausfueller.md) (75 KB)
- Im Repo: [`testakten/megaprompts/vertragsausfueller.md`](../testakten/megaprompts/vertragsausfueller.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `altvertraege-dokumentenmatrix-und-lueckenliste` | Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung im Vertragsausfueller. |
| `altvertrag-nachziehen` | Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder Gesetzesänderungen. §§ 305 ff. BGB... |
| `anschluss-routing` | Anschluss-Routing für Vertragsausfüller: wählt den nächsten Spezial-Skill nach Engpass (Schriftform/Textform-Fristen, Vertragsentwurf, Mustervertrag, Anlagen), dokumentiert Router-Entscheidung mit Begründung. |
| `ausdruecklicher-fristennotiz-und-naechster-schritt` | Ausdruecklicher: Fristennotiz und nächster Schritt im Vertragsausfueller. |
| `batch-modus-docx-stripper-einfuehrung` | Batch-Modus für Konzernvertraege: viele aehnliche Verträge mit wechselnden Parteien und Werten, Massendatenimport CSV/XLSX, Plausibilitaetsregel-Set, Output 1 PDF pro Datensatz. Quality Gate und Reviewer-Sample im Vertragsausfueller. |
| `bsag-mietvertrag-klauselentscheidung` | BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB Schriftformerfordernis. Prüfrast... |
| `changes-beweislast-docx-erkennen` | Changes: Beweislast, Darlegungslast und Substantiierung im Vertragsausfueller. |
| `clean-output` | Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand erstellt. §§ 125 ff. BG... |
| `docx-stripper` | DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstr... |
| `docx-tatbestand-beweis-und-belege` | Docx: Tatbestandsmerkmale, Beweisfragen und Beleglage im Vertragsausfueller. |
| `dokumente-intake` | Dokumentenintake für Vertragsausfüller: sortiert Vertragsentwurf, Mustervertrag, Anlagen, prüft Datum, Absender, Frist und Beweiswert (Verhandlungs-Korrespondenz); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einfuehrung-prozess` | Einfuehrung Prozess Vertragsausfueller: vom Mandanteninterview über Variableninventar zum Template, Klauselentscheidung, Plausibilitaetscheck, Quality Gate. Schaubild und Reihenfolge der Sub-Skills im Vertragsausfueller. |
| `einstieg-routing` | Einstieg, Triage und Routing für Vertragsausfüller: ordnet Rolle (Vertragsparteien, Berater), markiert Frist (Schriftform/Textform-Fristen), wählt Norm (BGB AT, BGB BT, AGB-Recht §§ 305 ff. BGB) und Zuständigkeit (zuständige Stelle), lei... |
| `erkennen-schriftsatz-brief-und-memo-bausteine` | Erkennen: Schriftsatz-, Brief- und Memo-Bausteine im Vertragsausfueller. |
| `erzeugen-red-fassungen-sonderfall-felder` | Erzeugen: Red-Team und Qualitätskontrolle im Vertragsausfueller. |
| `fassungen-sonderfall-und-edge-case` | Fassungen: Sonderfall und Edge-Case-Prüfung im Vertragsausfueller. |
| `felder-behoerden-gericht-und-registerweg` | Felder: Behörden-, Gerichts- oder Registerweg im Vertragsausfueller. |
| `feldinventar-fragebogen-input` | Feldinventar für Vertragsgenerator erstellen: Anwendungsfall Anwalt oder Mandant will wissen welche Felder im Vertrag auszufüllen sind bevor Rückfrageninterview startet. §§ 550 BGB Schriftformerfordernis Mietvertrag, § 2 NachwG Arbeitsve... |
| `fragebogen-input-leitfaden` | Leitfaden Fragebogen-Input für Vertragsausfueller: Reihenfolge, Validierung, Plausibilitaet, Mandantenfreundlichkeit. Prüfraster für UX-Tests im Vertragsausfueller. |
| `fremdsprachige-vertraege-bilingual` | Spezialfall fremdsprachige und bilinguale Verträge: Sprache für rechtlich verbindliche Auslegung definieren, Konsistenz Glossar, Übersetzung als Anlage. Risiken bei Verwendung von DeepL und LLM. Prüfraster und Mustertexte im Vertragsa... |
| `fuehren-interessen-mappen-nachfrage` | Fuehren: Mehrparteienkonflikt und Interessenmatrix im Vertragsausfueller. |
| `klauselentscheidung` | Wahlklauseln und Klauselalternativen im Vertrag entscheiden: Anwendungsfall Vertrag enthält optionale Klauseln wie Umsatzsteueroption Indexierung Konkurrenzschutz Rückbau oder Betriebspflicht die aktiv angekreuzt oder formuliert werden m... |
| `kommandocenter-mehrsprachige-vertraege` | Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen Workflow. Vertragsrecht... |
| `konzern-rahmenvertrag-anpassen` | Spezialfall Rahmenvertrag im Konzern anpassen ohne Änderung der Substanz: typische Stellen wie Vergueng, Laufzeit, Liefermenge. Prüfraster für Änderungsfreigabe und Track-Changes-Diskussion mit Gegenseite. Mustertexte im Vertragsausfu... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Vertragsausfueller. |
| `mappen-zahlen-schwellen-und-berechnung` | Mappen: Zahlen, Schwellenwerte und Berechnung im Vertragsausfueller. |
| `mehrsprachige-vertraege-spezial` | Spezialfall mehrsprachige Verträge deutsch / englisch: massgebliche Sprache, paralleler Aufbau, Übersetzungsfehler. Prüfraster für internationale Mandate im Vertragsausfueller. |
| `nachfrage-abschlussprodukt-und-uebergabe` | Nachfrage: Abschlussprodukt und Übergabe im Vertragsausfueller. |
| `neue-rueckfragen-strippen` | Neue: Internationaler Bezug und Schnittstellen im Vertragsausfueller. |
| `output-waehlen` | Output-Wahl für Vertragsausfüller: stimmt Adressat (Vertragsparteien, Berater), Frist (Schriftform/Textform-Fristen) und Form auf den Zweck ab — typische Outputs: Ausgefüllter Vertrag mit kommentierten Lücken, Issue List, Risikomemo. |
| `platzhalterlogik-bauleiter` | Bauleiter Platzhalterlogik: Variablen, Pflichtfelder, optionale Bloecke, Konditionalen. Prüfraster für Templatebau und Fehlerquellen im Vertragsausfueller. |
| `plausibilitaetscheck-termsheet` | Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klaus... |
| `quality-gate-redline-qa` | Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-30... |
| `quellen-livecheck` | Quellen-Live-Check für Vertragsausfüller: prüft Normen (BGB AT, BGB BT, AGB-Recht §§ 305 ff. BGB) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene... |
| `redline-qa` | Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollständigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft werden. §§ 145 ff. BG... |
| `rueckfragen-compliance-dokumentation-und-akte` | Rueckfragen: Compliance-Dokumentation und Aktenvermerk im Vertragsausfueller. |
| `rueckfrageninterview` | Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene Pflichtfelder nach Prior... |
| `sheets-quellenkarte` | Sheets Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Vertragsausfueller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `strippen-risikoampel-und-gegenargumente` | Strippen: Risikoampel, Gegenargumente und Verteidigungslinien im Vertragsausfueller. |
| `template-erkennung-format-track-changes` | Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln identifizieren. §§ 433 f... |
| `template-format-und-source` | Template-Format und Quelle: Word-DOCX mit Formularfeldern, Markdown mit Platzhaltern, PDF AcroForm, Excel mit Variablenliste. Pro Format: Vor- und Nachteile, Migration, Backup. Pflicht zu sauberer Versionierung im Vertragsausfueller. |
| `term-track-vertraege` | Term: Verhandlung, Vergleich und Eskalation im Vertragsausfueller. |
| `termsheet-mapping` | Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten müssen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent, Klausel-Bibliothek Vert... |
| `track-changes-nur-nach-frage` | Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhan... |
| `track-mandantenkommunikation-entscheidungsvorlage` | Track: Mandantenkommunikation und Entscheidungsvorlage im Vertragsausfueller. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Vertragsausfüller: trennt fehlende Tatsachen von fehlenden Belegen (Vertragsentwurf, Mustervertrag, Anlagen), nennt pro Lücke Beweisthema, Beschaffungsweg (zuständige Stelle), Frist und Ersatznachweis. |
| `vaf-versionierung-aenderungsverfolgung-spezial` | Spezialfall Versionierung und Änderungsverfolgung in Vertragsdokumenten: Track Changes, Blackline, automatisierter Diff: Prüfraster f... |
| `vertraege-formular-portal-und-einreichung` | Verträge: Formular, Portal und Einreichungslogik im Vertragsausfueller. |
| `vertragsausfueller-erstpruefung-und-mandatsziel` | Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel im Vertragsausfueller. |
| `vorlagen-vertragsausfueller-vaf-altvertrag` | Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg im Vertragsausfueller. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Vertragsausfueller. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Vertragsausfueller. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Vertragsausfueller. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

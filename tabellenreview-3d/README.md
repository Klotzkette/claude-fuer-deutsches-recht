# Tabellenreview 3D


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Tabellenreview Paragrafix GmbH — Fortbestehensprognose v23, IDW S 11** (`tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck`) | [Gesamt-PDF lesen](../testakten/tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck/gesamt-pdf/tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

3D-Tabellenreview als Würfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Tabellenreview 3D (`tabellenreview-3d`, dieses Plugin) | [tabellenreview-3d.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tabellenreview-3d.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `arbeitsblatt-perspektiven-definieren` | Definiert die dritte Würfel-Achse — Arbeitsblätter als Perspektiven die über denselben Dokumentenstapel laufen aber jeweils eine andere Brille aufsetzen. Typische Perspektiven: Recht (Anwalt) Steuer (Steuerberater)… |
| `audit-trail-protokoll` | Führt das Audit-Trail-Protokoll des Würfels — jeder Reviewlauf jede Prompt-Änderung jede Prüfer-Abnahme jeder Cache-Treffer jede Hash-Prüfung wird unveränderlich protokolliert. Spalten pro Eintrag: Zeitstempel A… |
| `belegkette-rueckverfolgung` | Sichert die Belegkette jeder Zelle des Würfels — von der Antwort über das wörtliche Zitat bis zur Originalstelle im Quelldokument mit Seite Absatz und Datei-Hash. Erkennt Belegkette-Brüche (Datei-Hash weicht ab / … |
| `caching-und-teil-rerun` | Caching der Würfelzellen und gezielter Teil-Rerun bei Änderungen — vermeidet die voll Neuberechnung von tausenden Zellen wenn nur ein Spaltenprompt eine Zeile oder ein Arbeitsblatt geändert wurde. Cache-Key pro Zel… |
| `dokumentstapel-aufnehmen` | Nimmt einen Dokumentenstapel als Zeilenachse des Würfels auf. Quellen: VDR-Export (Datasite Intralinks Box) lokaler Ordner SharePoint-Bibliothek E-Mail-Anhang-Sammlung gescannte PDF mit OCR-Pipeline. Erzeugt pro Doku… |
| `excel-multi-sheet-export` | Exportiert den dreidimensionalen Würfel in eine einzige Excel-Datei mit mehreren Tabellenblättern — ein Reiter pro Arbeitsblatt-Perspektive (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb / Compliance). Je… |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview für das tabellenreview-3d-Plugin. Erfragt typische Anwendungsfälle (M&A-DD / Immobilienportfolio / Vendor-Onboarding / Arbeitsverträge / Mietverträge / Anlagedokumente / freie Eigenwuerfel), St… |
| `kreuzblatt-konsistenzpruefung` | Prüft die dritte Würfel-Dimension auf innere Konsistenz — läuft NACH `review-durchfuehren` über alle Arbeitsblätter und sucht Widersprüche zwischen Perspektiven (z. B. ein Vertrag rechtlich grün aber datenschut… |
| `pdf-bericht-erzeugen` | Erstellt einen prüfbaren PDF-Bericht aus dem 3D-Würfel. Struktur: Deckblatt mit Projekt Mandant Stichtag Würfel-Ampel; Management-Summary mit Hotspots und blockierenden Roten; pro Arbeitsblatt-Perspektive ein Absch… |
| `prompt-versionierung` | Versioniert alle Spalten- und Zeilenprompts mit semantischer Versions-ID — patch für Wortlautfeinheiten minor für geänderte Antworttypen oder Ampelregeln major für geänderte Pruefdimension. Jede Zelle im Würfel … |
| `pruefer-uebergabe-paket` | Schnuert das vollständige Prüfer-Paket nach Abschluss eines Würfellaufs — Excel-Würfel-Datei aus Skill `excel-multi-sheet-export` PDF-Bericht aus `pdf-bericht-erzeugen` Belegketten-CSV aus `belegkette-rueckverfolg… |
| `review-durchfuehren` | Führt den eigentlichen Reviewlauf über den Würfel durch — Anzahl Zellen = Spalten x Zeilen x Arbeitsblätter. Pro Zelle: Spaltenprompt + Zeilenprompt + Arbeitsblatt-Perspektive zusammenführen, Antwort aus dem Doku… |
| `risikoampel-aggregation` | Konsolidiert die Ampel-Wertungen entlang aller drei Würfelachsen — pro Zelle (atomisch) pro Zeile (Dokument-Gesamtampel) pro Spalte (Datenpunkt-Hotspots) pro Arbeitsblatt (Perspektiven-Gesamtampel) und pro Gesamtwuer… |
| `spaltenprompts-definieren` | Definiert die Spaltenprompts der ersten Würfel-Achse — jede Spalte ist eine einzige praezise Frage die für ALLE Dokumente identisch gestellt wird damit Vergleichbarkeit über den Stapel entsteht. Enthält eine Bibli… |
| `vorlage-arbeitsvertrag-portfolio` | Würfelvorlage für Massenprüfung von Arbeitsverträgen — 15 Spalten (Vertragsdatum Probezeit Befristung-mit-oder-ohne-Sachgrund Wochenarbeitszeit Kündigungsfrist Tarifbindung Bruttogehalt Sonderzahlung Verschwiegen… |
| `vorlage-immobilien-portfolio` | Würfelvorlage für Immobilien-Portfolioanalyse — 16 Spalten (Gemarkung / Flur / Flurstück / Wirtschaftsart / Größe / Eigentümerkette / Abteilung-II-Lasten / Abteilung-III-Grundpfandrechte / Rang / Löschungserlei… |
| `vorlage-ma-due-diligence` | Fertige Würfelvorlage für M&A-Due-Diligence — 18 Spalten (Vertragsart Laufzeit Kündigungsfrist Change-of-Control MAC-Klausel Abtretungsverbot Haftungsbegrenzung Garantien Vertragsstrafe SLA Datenschutz Geheimhaltun… |
| `vorlage-vendor-onboarding-3d` | Würfelvorlage für Vendor- und Lieferanten-Onboarding — 17 Spalten (Vendor-Stammdaten Branche AVV-Pflicht AVV-vorhanden SLA-Reaktionszeit SLA-Verfügbarkeit Exit-Klausel Datenherausgabe Verschlüsselung Subunternehme… |
| `wuerfel-aufbauen` | Baut die dreidimensionale Würfel-Struktur für ein neues Pruefprojekt auf — drei Achsen: Spalten (Datenpunkte als Spaltenprompts) Zeilen (Dokumente mit optionalen Zeilenprompts) Arbeitsblätter (Perspektiven wie Rech… |
| `zeilenprompts-definieren` | Definiert die Zeilenprompts der zweiten Würfel-Achse — pro Dokument eine optionale Sonderanweisung die das Lesen genau dieses Dokuments steuert. Beispiele: 'Konzernvertrag — AktG Paragraph 311 zusätzlich prüfen' / … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `arbeitsblatt-perspektiven-definieren` | Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster, Gläubigerstellung. Output: Perspekt... |
| `audit-trail-protokoll` | Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output: Audit-Trail-Protokoll.... |
| `belegkette-rueckverfolgung` | Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output: Belegketten-Übersicht. Abgrenzun... |
| `caching-und-teil-rerun` | Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten und neu verarbeitet... |
| `dokumentstapel-aufnehmen` | Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output: Dokumentenstapel-Inventar. Abgrenzung: nic... |
| `excel-multi-sheet-export` | 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei Multisheet-Struktur. A... |
| `kreuzblatt-konsistenzpruefung` | Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Prüfb... |
| `pdf-bericht-erzeugen` | 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview. Abgrenzung: nicht Exc... |
| `prompt-versionierung` | Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output: Prompt-Versionsprotokoll. Abgrenzung... |
| `pruefer-uebergabe-paket` | Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für naechsten Prüfer. Abg... |
| `review-durchfuehren` | 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung. Output: Ausgefuellte... |
| `risikoampel-aggregation` | Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht. Abgrenzung: nicht K... |
| `spaltenprompts-definieren` | Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument. Abgrenzung: nicht Zeilen... |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview für den 3D-Tabellenreview: Fallkategorie, Tabellengrösse, Prüfzweck erfassen. Normen: §§ 174 ff. InsO, HGB. Prüfraster: Zweck, Datenlage, Perspektivenwahl, Exportformat. Output: Konfigurationsdokument für 3D-Review-St... |
| `vorlage-arbeitsvertrag-portfolio` | Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format: Forderung/Prüfung/Stellung. Normen: BGB, KSchG, ArbZG. Prüfraster: Vertragsbedingungen, Klauselgueltigkeit, HR-Compliance. Output: Arbeitsvertrag-Portfolio-Tabelle.... |
| `vorlage-immobilien-portfolio` | Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format. Normen: §§ 535 ff. BGB, WEG, GrEStG. Prüfraster: Miete, Grundbuch, steuerliche Belastung, Instandhaltung. Output: Immobilien-Portfolio-Tabelle. Abgrenzung: nicht... |
| `vorlage-ma-due-diligence` | Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für... |
| `vorlage-vendor-onboarding-3d` | Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output: Vendor-Onboarding-Prüftabelle. Abgrenz... |
| `wuerfel-aufbauen` | 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output: Wuerfelkonfigurationsdokument. Ab... |
| `zeilenprompts-definieren` | Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument. Abgrenzung: nicht Spaltenpr... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

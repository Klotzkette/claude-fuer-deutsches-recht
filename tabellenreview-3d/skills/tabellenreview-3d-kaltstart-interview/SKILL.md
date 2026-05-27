---
name: tabellenreview-3d-kaltstart-interview
description: "Kaltstart-Interview fuer den 3D-Tabellenreview: Fallkategorie, Tabellengrösse, Pruefzweck erfassen. Normen: §§ 174 ff. InsO, HGB. Pruefraster: Zweck, Datenlage, Perspektivenwahl, Exportformat. Output: Konfigurationsdokument fuer 3D-Review-Start. Abgrenzung: nicht Pruefungsdurchfuehrung."
---

# /tabellenreview-3d:tabellenreview-3d-kaltstart-interview


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung zeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft Konnektoren-Verfügbarkeit (Datenraum-Tool, Excel-Generator, PDF-Generator, Dokumentenspeicher, OCR-Pipeline, Anwaltsprüfer-Postfach). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `OK` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `unbekannt` markieren.

---

## Kaltstart-Interview: tabellenreview-3d

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Rechtsanwalt (M&A / Immobilien / Arbeit / Datenschutz) / Syndikus / Wirtschaftsprüfer / Steuerberater / Notar / Nicht-Jurist mit anwaltlicher Rücksprache?
- **Praxiskontext:** Einzelkanzlei / kleine Kanzlei / Großkanzlei / Inhouse / Beratungsstelle / Hochschule
- **Anwaltlicher Prüfer für Endabnahme:** Name, Erreichbarkeit (jede Würfel-Ausgabe geht erst nach Prüfer-Abnahme ans Mandat)

### 2. Typische Anwendungsfälle

- **M&A-Due-Diligence** (Vertragsstapel der Zielgesellschaft): ja / nein
- **Immobilien-Portfolio** (Grundbuchauszüge + Mietverträge + Baulasten): ja / nein
- **Vendor-/Lieferanten-Onboarding** (AGB + AVV + Wirtschaftsdaten + Compliance): ja / nein
- **Arbeitsvertrags-Massenprüfung** (Tarifbezug + AGB-Klauseln + DSGVO + Sozialversicherung): ja / nein
- **Mietvertrags-Portfolio** (Schönheitsreparaturen + Indexmiete + Betriebskosten): ja / nein
- **Anlagedokumente** (Fondsverträge / KAGB-Konformität / Anlegerschutz): ja / nein
- **Freie Eigenwürfel:** ja, mit eigener Spalten- / Zeilen- / Arbeitsblatt-Definition

### 3. Standard-Würfeldimensionen

- **Spalten (Datenpunkte):** typische Anzahl pro Würfel — z. B. 8 bis 25 Spaltenprompts
- **Zeilen (Dokumente):** typische Stapelgroesse — z. B. 10 bis 2000 Dokumente
- **Arbeitsblätter (Perspektiven):** wie viele Perspektiven werden übereinander gestapelt — typisch 3 bis 6 (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb)

### 4. Hauszitierweise

- BGH-Stil mit Pinpoint-Randnummer (siehe `references/zitierweise.md` im Repository)
- Kommentar-Stil: Bearbeiter in: Werk, Auflage Jahr, Norm Rn.
- Bei Vertragsstellen: wörtliches Zitat in Anführungszeichen, danach Fundstelle (Ziffer Absatz Seite)

### 5. Risikoampel-Schwellen

- **Rot (Blockierend):** [PLATZHALTER — z. B. AGB-unwirksame Klausel BGB Paragraph 307; fehlende AVV bei Auftragsverarbeitung; offene Briefgrundschuld ohne Löschungsbewilligung]
- **Gelb (Prüfenswert):** [PLATZHALTER — z. B. unklare Kündigungsfrist; Dienstbarkeit zugunsten unbekannter Dritter]
- **Grün (Niedrig):** [PLATZHALTER — z. B. branchenüblich; in Vorlage erfasst]

### 6. Excel- und Belegkette-Pfade

- **Excel-Ausgabe-Verzeichnis:** [PLATZHALTER — z. B. `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/würfel/<projekt>/`]
- **Belegketten-Verzeichnis:** [PLATZHALTER — Speicherort für wörtliche Quellenzitate mit Datei-Hash]
- **Audit-Trail-Verzeichnis:** [PLATZHALTER — Pfad für Prompt-Versionen Laufprotokolle und Prüfer-Abnahmen]

### 7. Standort

- **Bundesland:** [PLATZHALTER]
- **Praxistypus:** Einzelkanzlei / Sozietät / Partnerschaftsgesellschaft / Inhouse-Rechtsabteilung

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
  - `/tabellenreview-3d:würfel-aufbauen` — Würfel-Struktur für ein neues Projekt anlegen
  - `/tabellenreview-3d:vorlage-ma-due-diligence` — bei M&A-DD direkt mit Vorlage starten
  - `/tabellenreview-3d:vorlage-immobilien-portfolio` — bei Immobilienportfolio
  - `/tabellenreview-3d:vorlage-arbeitsvertrag-portfolio` — bei Massenprüfung Arbeitsverträge
  - `/tabellenreview-3d:vorlage-vendor-onboarding-3d` — bei Lieferanten-Anbindung
- Hinweis auf Mandatsgeheimnis (Paragraph 43a Absatz 2 BRAO, Paragraph 203 StGB) und Notwendigkeit anwaltlicher Endabnahme

## Rechtlicher Rahmen

- **BRAO** — Paragraph 43a Absatz 2 (Verschwiegenheitspflicht)
- **StGB** — Paragraph 203 (Verletzung von Privatgeheimnissen)
- **DSGVO** — Artikel 28 (Auftragsverarbeitung) bei Verarbeitung von Vertragsstapeln durch Dritte
- **RDG** — Paragraph 2 (Rechtsdienstleistung — Endabnahme durch zugelassenen Rechtsanwalt)

## Hinweise

Dieses Plugin liefert eine Vorstrukturierung. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Jede Zelle des Würfels ist ein Hinweis der Verifikation bedarf, kein abschließender Befund. Vor Mandatsabnahme erfolgt die Prüfung durch den anwaltlichen Prüfer (siehe Skill `pruefer-uebergabe-paket`).

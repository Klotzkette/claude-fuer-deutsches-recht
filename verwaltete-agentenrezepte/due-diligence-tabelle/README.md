# Due-Diligence-Tabelle — Managed-Agent-Vorlage

## Übersicht

Stapelweise Dokumentenprüfung über einen virtuellen Datenraum (VDR) im M&A-Kontext. Zwei Modi:

- **Beobachten** – überwacht den VDR auf neue Uploads seit einem Stichdatum, klassifiziert jeden Upload gegen die Prüflisten-Kategorien des eingesetzten Teams und markiert Uploads in hochpriorisierten Kategorien (Wesentliche Verträge, Rechtsstreitigkeiten, Schutzrechte/IP).
- **Tabelle** – führt eine tabellarische Prüfung gegen ein Spaltenschema über einen Dokumentenordner durch. Eine Zeile pro Dokument, eine Spalte pro Datenpunkt, jede Zelle rückzitiert auf ein wörtliches Quellzitat. Das M&A-Due-Diligence-Arbeitsmittel.

Gleiche Quelle wie das [`gesellschaftsrecht`](../../gesellschaftsrecht)-Plugin – dieses Verzeichnis ist das Managed-Agent-Kochbuch für `POST /v1/agents`. Der Tabellenmodus nutzt den `tabellenpruefung-cap-table`-Skill und läuft headless über eine Extractor-Worker-Flotte.

## ⚠️ Vor dem Deployment

- **Jede Zelle ist ein Hinweis, kein Befund.** Eine Due-Diligence-Tabelle ist keine Zusicherung, kein Offenlegungsverzeichnis und kein Due-Diligence-Memo, bis ein Anwalt die zugrundeliegenden Dokumente gelesen und freigegeben hat. Das wörtliche Zitat in jeder Zelle dient dem schnellen Nachprüfen durch den Prüfer – nutzen Sie es.
- **Der Wesentlichkeitsfilter und die Spaltenklassifizierungen wenden Heuristiken an, keine rechtliche Beurteilung.** Ein Vertrag, den das Schema als unwesentlich einstuft, kann derjenige sein, der die Transaktion scheitern lässt. Eine "beantwortet"-Zelle ist trotzdem falsch, wenn der Extraktor die Klausel falsch gelesen hat. Die Prüfzeit skaliert mit `unklar` + `prüfbedarf` + `beantwortet` – nicht nur mit den markierten.
- **Der Beobachtungsmodus klassifiziert Metadaten und Vorschauen, keine vollständigen Dokumente.** Ein neu hochgeladenes Dokument, das der Klassifikator als "niedrige Priorität" einstuft, kann trotzdem das Nebenbriefschreiben sein, das die Transaktion ändert. Behandeln Sie den Beobachtungsbericht als Warteschlange, nicht als Filter.
- **Vom Vertragspartner hochgeladene Dokumente sind nicht vertrauenswürdige Eingaben für die Toolchain.** Die CSV-Formelinjektionsabwehr des Grid-Writers ist zwingend erforderlich – siehe Sicherheitsabschnitt unten.

## Deployment

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export BOX_MCP_URL=...
export GDRIVE_MCP_URL=...
export IMANAGE_MCP_URL=...          # optional; Standard-Konfiguration aktivieren, wenn genutzt
export DEFINELY_MCP_URL=...         # optional; für Klauselstruktur-QA des Normalizer-Durchlaufs
../../scripts/agentenrezept-ausliefern.sh due-diligence-tabelle
```

## Steuerungsereignisse

Siehe [`steering-examples.json`](./steering-examples.json).

## Sicherheit und Übergaben

VDR-Dokumente – Verträge, Protokolle der Gesellschafterversammlung / des Aufsichtsrats, Nebenabsprachen, Uploads von Vertragspartnern – sind **nicht vertrauenswürdige Eingaben**. Ein vom Vertragspartner hochgeladener Vertrag kann Zeichenketten enthalten, die den Prüfer oder die nachgelagerte Toolchain manipulieren sollen. Vier-Stufen-Isolation hält die Write-Hand und die MCP-Hand von den Dokumenten fern:

| Stufe | Berührt nicht vertrauenswürdige Dokumente? | Tools | Konnektoren |
|---|---|---|---|
| **`dokument-leser`** | **Ja** (nur lesend) | `Read`, `Grep` | Box, Google Drive, iManage (Lesen) |
| **`extrahierer`** | **Ja** (nur lesend) | `Read`, `Grep` | Keine |
| `normalisierer` / Orchestrator | Nein | `Read`, `Grep`, `Glob`, `Agent` | Keine (Definely optional, nur lesen) |
| **`tabellen-schreiber`** (Write-Inhaber) | Nein | `Read`, `Write` | Keine |

`dokument-leser` und `extrahierer` liefern längenbegrenzte, schema-validierte JSON. Der Orchestrator und `normalisierer` sehen nur strukturierte Daten. `tabellen-schreiber` erzeugt `./out/due-diligence-tabelle-<Datum>.csv`, `./out/due-diligence-tabelle-<Datum>_quellen.csv` und `./out/due-diligence-tabelle-<Datum>-zusammenfassung.md`.

**CSV-Formelinjektionsabwehr.** Jede Zelle, die vom `tabellen-schreiber` geschrieben wird – Werte, wörtliche Zitate, Fundstellen, Dokumentnamen, Spaltenbezeichnungen – wird auf das erste Zeichen gegen `=`, `+`, `-`, `@`, Tab und Wagenrücklauf geprüft. Zellen, die übereinstimmen, werden mit einem einzelnen Apostroph vorangestellt. Vom Vertragspartner hochgeladene Verträge enthalten routinemäßig Zeichenketten, die Excel und Sheets sonst als Formeln ausführen (`=HYPERLINK(...)` Exfiltration, `=cmd|...` DDE in älterem Excel), sobald das Dealteam die Datei öffnet.

**Xlsx ist ein Deployment-Anliegen.** Das Kochbuch liefert nur CSVs. Das deployende Team transformiert diese in `.xlsx` mit der Arbeitsmappenstruktur in [`gesellschaftsrecht/skills/tabellenpruefung-cap-table/references/excel-output.md`](../../gesellschaftsrecht/skills/tabellenpruefung-cap-table/references/excel-output.md) – versteckte `_quelle`-Spalten, Zellkommentare mit dem Zitat beim Hovern, zustandsbasierte Füllungen, `Verifiziert`-Dropdown pro Spalte, `_schema`- und `_zusammenfassung`-Blätter.

**Nicht garantiert:** Jede Zelle ist ein **Hinweis, der verifiziert werden muss**, kein Befund. Der Prüfer liest die Quelle, prüft das Zitat, markiert die Spalte `Verifiziert`. Ein Anwalt entscheidet, was in eine Zusicherung, einen Zeitplan oder ein Memo aufgenommen wird.

## Anpassungshinweise

- **VDR-URL.** Setzen Sie `BOX_MCP_URL` / `GDRIVE_MCP_URL` / `IMANAGE_MCP_URL` passend zu Ihrem Datenraum. Standard aktiviert Box und Google Drive; wechseln Sie die `default_config` in [`agent.yaml`](./agent.yaml), wenn Sie iManage oder Datasite als primär betreiben. Für Intralinks oder Datasite fügen Sie einen Eintrag zu `mcp_servers` und `tools` mit der passenden MCP-URL hinzu.
- **Spaltenschema.** Der M&A-Standard aus [`gesellschaftsrecht/skills/tabellenpruefung-cap-table/references/ma-diligence-columns.md`](../../gesellschaftsrecht/skills/tabellenpruefung-cap-table/references/ma-diligence-columns.md) ist der Standard. Passen Sie ihn für Ihren Deal-Typ an – Tech/IP, Healthcare, Immobilien, regulierte Finanzdienstleistungen – mit den Ergänzungen in dieser Referenz. Für deutsche M&A-Transaktionen empfehlen sich zusätzliche Spalten: Mitbestimmungsrelevanz (§ 111a AktG), GWB-Freigabe (§§ 35 ff. GWB), Grunderwerbsteuer (§ 1 GrEStG), steuerliche Organschaft.
- **Ausgabeziel.** Ausgaben landen in `./out/`. Leiten Sie sie über Ihre Deploy-Pipeline in Ihren Deal-Ordner, Google Drive, iManage-Arbeitsbereich oder Box-Ordner weiter. Geben Sie dem `tabellen-schreiber` kein MCP zum Hochladen; eine Übergabe an Ihren Upload-Schritt ist sauberer und isoliert die Write-Stufe.
- **Standardmodus.** Beobachten vs. Tabelle wird pro Steuerungsereignis ausgewählt. Wenn Ihr Ablauf fast immer eines von beidem ist, füllen Sie die Steuerungsereignis-Vorlage in Ihrem Orchestrator entsprechend vor.
- **Prüflistenkategorien.** Der Beobachtungsmodus klassifiziert gegen die Kategorien in der `CLAUDE.md`-Konfiguration des deployenden Teams. Führen Sie dort `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview` durch, bevor Sie den Beobachtungsmodus in einen Live-Deal einbinden.
- **Arbeitsergebnisvermerk.** `tabellen-schreiber` stellt den Vermerk aus der `## Ausgaben`-Konfiguration des deployenden Teams voran. Bestätigen Sie den Vermerk mit Ihrem Team – er unterscheidet sich je nach Prüferrolle (Rechtsanwalt vs. Nichtanwalt).
- **Benachrichtigungsweiterleitung.** Dieser Agent veröffentlicht niemals direkt. Berichte sind Dateien; ein `handoff_request` teilt Ihrem Orchestrator mit, welchen Kanal er weiterleiten soll. Konfigurieren Sie den Deal-Kanal in der `CLAUDE.md`-Konfiguration des deployenden Teams.

## Relevante Rechtsnormen (deutsches M&A-Recht)

- **Gesellschaftsrecht:** §§ 293 ff. AktG (Unternehmensverträge), §§ 311 ff. AktG (Abhängige Unternehmen), § 179a AktG (Vermögensübertragung), §§ 17 ff. UmwG
- **Wettbewerbsrecht:** §§ 35–43 GWB (Fusionskontrolle), Art. 1–10 FKVO (EU-Fusionskontrolle)
- **Datenschutz:** Art. 37–39 DSGVO (Datenschutzbeauftragter), Art. 28 DSGVO (Auftragsverarbeitung), BDSG
- **Arbeitsrecht:** § 613a BGB (Betriebsübergang), §§ 111–113 BetrVG (Betriebsänderung), MitbestG
- **Steuerrecht:** § 1 GrEStG, §§ 15 ff. UmwStG, § 8b KStG
- **Kapitalmarktrecht:** §§ 33 ff. WpÜG (Übernahmerecht), MAR (Insiderrecht, Marktmanipulation)

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

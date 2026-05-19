# Aufsichts-Monitor — Managed-Agent-Vorlage

## Übersicht

Fortlaufende Überwachung amtlicher Behördenfeeds auf regulatorisch relevante Veröffentlichungen. Der Agent liest periodisch Bundesanzeiger (BAnz), BaFin-Journal, EUR-Lex und BNetzA-RSS, filtert Einträge nach Wesentlichkeitsschwellen für das jeweilige Mandat und erstellt einen strukturierten Digest für das zuständige Team.

Zwei Modi:

- **Sweep** – liest alle konfigurierten Feeds seit einem Stichdatum, klassifiziert jeden Eintrag gegen die vom deployenden Team konfigurierten Themenprofile (Finanzaufsicht, Netzregulierung, Kartellrecht, Datenschutz, Kapitalmarkt) und markiert Einträge oberhalb der Wesentlichkeitsschwelle.
- **Digest** – erstellt nach einem abgeschlossenen Sweep einen strukturierten Bericht mit Zusammenfassung, Volltextreferenzen und handlungsempfehlenden Hinweisen. Das Aufsichtsrecht-Arbeitsmittel für den täglichen oder wöchentlichen Überwachungsrhythmus.

Gleiche Quelle wie das [`regulatory-legal`](../../regulatory-legal)-Plugin — dieses Verzeichnis ist das Managed-Agent-Kochbuch für `POST /v1/agents`. Der Sweep-Modus nutzt den `feed-monitoring`-Skill und läuft headless über eine Feed-Reader-Flotte.

## ⚠️ Vor dem Deployment

- **Jede Klassifizierung ist ein Hinweis, kein Befund.** Ein Eintrag, den der Wesentlichkeitsfilter als nachrangig einstuft, kann derjenige sein, der eine Handlungspflicht auslöst. Behandeln Sie die Digest-Zusammenfassung als Vorfilter für menschliche Prüfung, nicht als abschließende Würdigung.
- **Feeds sind nicht vertrauenswürdige Eingaben.** Amtliche Feeds sind zwar öffentlich, aber RSS-Einträge, Metadaten und verlinkte Dokumente können Zeichenketten enthalten, die nachgelagerte Prozesse manipulieren sollen. Der Feed-Reader liefert schema-validiertes JSON; der Digest-Writer sieht nur strukturierte Daten.
- **Vollständigkeit ist nicht garantiert.** Feeds haben Veröffentlichungsverzögerungen. Eine Meldung „keine neuen Einträge" ist eine Aussage über den Datenstand des Feeds, keine Aussage über die Rechtslage. Prüfen Sie kritische Themenfelder regelmäßig durch direkten Zugriff auf die amtliche Quelle.
- **Der Wesentlichkeitsfilter wendet Heuristiken an, keine rechtliche Beurteilung.** Die Schwellenwerte müssen vom deployenden Team auf das konkrete Mandatsprofil zugeschnitten werden.

## Deployment

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export BANZ_MCP_URL=...            # Bundesanzeiger-RSS/API-Konnektor
export BAFIN_MCP_URL=...           # BaFin-Journal-Feed-Konnektor
export EURLEX_MCP_URL=...          # EUR-Lex-CELLAR-API-Konnektor
export BNETZА_MCP_URL=...          # BNetzA-RSS-Konnektor
../../scripts/agentenrezept-ausliefern.sh aufsichts-monitor
```

## Steuerungsereignisse

Siehe [`steering-examples.json`](./steering-examples.json).

## Sicherheit und Übergaben

Behördenfeeds und die darin verlinkten Dokumente sind **nicht vertrauenswürdige Eingaben**. Ein manipulierter Feed-Eintrag oder ein verlinktes PDF kann Zeichenketten enthalten, die den Agenten oder eine nachgelagerte Toolchain beeinflussen sollen. Drei-Stufen-Isolation hält die Write-Hand und die MCP-Hand von den Rohdaten fern:

| Stufe | Berührt Rohdaten? | Tools | Konnektoren |
|---|---|---|---|
| **`feed-leser`** | **Ja** (nur lesend) | `Read`, `Grep` | BAnz, BaFin, EUR-Lex, BNetzA (alle nur lesend) |
| **`wesentlichkeits-filter`** | Nein — sieht nur strukturiertes JSON | `Read`, `Grep`, `Glob` | Keine |
| **`zusammenfassung-schreiber`** (Write-Inhaber) | Nein | `Read`, `Write` | Keine |

`feed-leser` liefert längenbegrenzte, schema-validierte JSON. `wesentlichkeits-filter` hat kein MCP und kein Netz — er wendet Regeln aus der Kanzleikonfiguration an. `zusammenfassung-schreiber` erzeugt `./out/aufsichts-digest-<Datum>.md` und `./out/aufsichts-eintraege-<Datum>.json`.

**Kein Direkt-Posting.** Der Agent veröffentlicht niemals direkt in einem Kommunikationskanal. Berichte sind Dateien. Ein `handoff_request` teilt dem Orchestrator mit, welchen Kanal er weiterleiten soll. Konfigurieren Sie den Zielkanal in der `CLAUDE.md`-Konfiguration des deployenden Teams.

**Arbeitsergebnisvermerk.** `zusammenfassung-schreiber` stellt den Vermerk aus der `## Ausgaben`-Konfiguration des deployenden Teams voran. Bestätigen Sie den Vermerk mit dem Team, bevor Sie in den Live-Betrieb gehen — er unterscheidet sich je nach Prüferrolle (Syndikusrechtsanwalt vs. externer Berater).

## Anpassungshinweise

- **Feed-URLs.** Setzen Sie `BANZ_MCP_URL`, `BAFIN_MCP_URL`, `EURLEX_MCP_URL` und `BNETZA_MCP_URL` auf die Endpunkte Ihres Deployments. Der Standard aktiviert alle vier Feeds. Deaktivieren Sie Feeds, die für Ihr Mandatsprofil nicht relevant sind, in der `default_config` des `feed-leser`.
- **Themenprofile.** Die Wesentlichkeitsschwellen und Themencluster (Finanzaufsicht, Netzregulierung, Kartellrecht, Datenschutz) werden in der `CLAUDE.md` des deployenden Teams konfiguriert. Führen Sie dort `/regulatory-legal:themen-konfiguration` durch, bevor Sie den Sweep-Modus in den Live-Betrieb bringen.
- **Zeitplan.** Täglich für mandatsbezogene Überwachung in aktiven Verfahren; wöchentlich für allgemeines Regulatory-Monitoring. Für BaFin-Meldungen (z. B. bei laufenden Erlaubnisverfahren nach KWG/WpIG) empfiehlt sich ein täglicher Sweep.
- **Ausgabeziel.** Ausgaben landen in `./out/`. Leiten Sie sie über Ihre Deploy-Pipeline in Ihren Mandatsordner, SharePoint-Bereich oder iManage-Arbeitsbereich weiter. Geben Sie dem `zusammenfassung-schreiber` kein MCP zum Hochladen; eine Übergabe an Ihren Upload-Schritt ist sauberer und isoliert die Write-Stufe.
- **Digest-Sprache.** Der `zusammenfassung-schreiber` verwendet standardmäßig Deutsch und die BGH/Beck-Zitierweise. Passen Sie den Fußnotenapparat in `./unteragenten/zusammenfassung-schreiber.yaml` an Ihre Hauszitierweise an.
- **EUR-Lex-Filter.** EUR-Lex liefert alle EU-Rechtsinstrumente. Konfigurieren Sie die Filterparameter (Rechtsgebiet, Sprachfassung, Dokumenttyp) im `feed-leser`, um das Volumen auf relevante Rechtsakte zu begrenzen.

## Relevante Rechtsnormen (deutsches Aufsichtsrecht)

- **Finanzaufsicht:** § 4 FinDAG (BaFin-Befugnisse), KWG §§ 1 ff. (Erlaubnispflicht), WpIG §§ 2 ff. (Wertpapierdienstleistungen), § 37 WpHG (Prüfungspflichten), DORA-VO (EU) 2022/2554
- **Kapitalmarkt:** MAR (EU) 596/2014 (Marktmissbrauch), MiFID II-RL 2014/65/EU, § 26 WpHG (Veröffentlichungspflichten), §§ 33 ff. WpÜG
- **Netzregulierung:** §§ 1 ff. TKG 2021, §§ 1 ff. EnWG, § 61 TKG (Frequenzvergabe), §§ 20 ff. EnWG (Entflechtung)
- **Kartellrecht:** §§ 1, 19, 20 GWB (Kartellverbot, Marktmacht), Art. 101, 102 AEUV, Bekanntmachungen des Bundeskartellamts
- **Datenschutz:** DSGVO (EU) 2016/679, BDSG, §§ 64 ff. BDSG (Aufsichtsbehörden), Leitlinien des EDSA

Vgl. Boos/Fischer/Schulte-Mattler (Hrsg.), KWG, 5. Aufl. 2016; Assmann/Schneider/Mülbert (Hrsg.), WpHG, 7. Aufl. 2019; Kühling/Buchner (Hrsg.), DSGVO/BDSG, 4. Aufl. 2024.

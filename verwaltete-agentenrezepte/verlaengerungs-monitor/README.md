# Verlängerungs-Monitor — Managed-Agent-Vorlage

## Übersicht

Fortlaufende Überwachung des Vertragsarchivs auf ablaufende Verlängerungs- und Kündigungsfristen. Der Agent liest periodisch das Vertragsarchiv (iManage, SharePoint, DMS), berechnet für jeden aktiven Vertrag die relevanten Fristen und erstellt einen strukturierten Fristenalert für das zuständige Team.

Zwei Modi:

- **Prüfung** – durchsucht das konfigurierte Vertragsarchiv nach Verträgen mit ablaufenden Fristen innerhalb eines konfigurierten Vorlauffensters (z. B. 30–90 Tage), berechnet Verlängerungs- und Kündigungsfristen nach dem anwendbaren Recht und markiert Abweichungen vom Vertragsplaybook des Mandanten.
- **Alert** – erstellt nach einer abgeschlossenen Prüfung einen strukturierten Bericht mit Fristenliste, Handlungsempfehlungen und Eskalationsvorschlägen. Das Vertragsmanagement-Arbeitsmittel für den wöchentlichen oder monatlichen Prüfungsrhythmus.

Gleiche Quelle wie das [`commercial-legal`](../../commercial-legal)-Plugin — dieses Verzeichnis ist das Managed-Agent-Kochbuch für `POST /v1/agents`. Der Prüfmodus nutzt den `contract-monitoring`-Skill und läuft headless über eine Repo-Reader-Flotte.

## ⚠️ Vor dem Deployment

- **Berechnete Fristen sind Hinweise, keine Kalendereinträge.** Verlängerungs- und Kündigungsfristen hängen von der konkreten Vertragsklausel, dem anwendbaren Recht (§§ 314, 620 ff. BGB; § 132 HGB für Handelsvertreter) und etwaigen Nachtragsvereinbarungen ab. Ein zugelassener Rechtsanwalt prüft jede berechnete Frist gegen den Originalvertrag, bevor sie in den Kalender eingetragen wird.
- **Das Vertragsarchiv ist eine nicht vertrauenswürdige Eingabe.** Verträge, Nachträge und Anhänge können Zeichenketten enthalten, die den Agenten oder eine nachgelagerte Toolchain manipulieren sollen. Der `ablage-leser` liefert schema-validiertes JSON; der `warnungs-schreiber` sieht nur strukturierte Daten.
- **Vollständigkeit ist nicht garantiert.** Das Archiv ist so vollständig wie das DMS des deployenden Teams. Ein Vertrag, der im Archiv fehlt, erzeugt keine Fristenwarnung. Prüfen Sie die Archivvollständigkeit vor dem ersten produktiven Einsatz.
- **Der Fristenrechner wendet Heuristiken an, keine rechtliche Beurteilung.** Klauseln mit unklarem Fristbeginn (z. B. Verlängerung „zu einem angemessenen Zeitpunkt") müssen zur menschlichen Prüfung markiert werden.

## Deployment

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export IMANAGE_MCP_URL=...          # iManage Work-MCP-Konnektor
export SHAREPOINT_MCP_URL=...       # SharePoint/OneDrive-Konnektor
export DMS_MCP_URL=...              # generischer DMS-Konnektor (DATEV, d.velop, Dokumentum)
../../scripts/agentenrezept-ausliefern.sh verlaengerungs-monitor
```

## Steuerungsereignisse

Siehe [`steering-examples.json`](./steering-examples.json).

## Sicherheit und Übergaben

Vertragsarchivdokumente sind **nicht vertrauenswürdige Eingaben**. Ein Vertrag, ein Nachtrag oder ein Anhang kann Zeichenketten enthalten, die den Agenten oder eine nachgelagerte Toolchain beeinflussen sollen. Drei-Stufen-Isolation hält die Write-Hand und die MCP-Hand von den Rohdokumenten fern:

| Stufe | Berührt Rohdokumente? | Tools | Konnektoren |
|---|---|---|---|
| **`ablage-leser`** | **Ja** (nur lesend) | `Read`, `Grep` | iManage, SharePoint, DMS (alle nur lesend) |
| **`frist-rechner`** | Nein — sieht nur strukturiertes JSON | `Read`, `Grep`, `Glob` | Keine |
| **`warnungs-schreiber`** (Write-Inhaber) | Nein | `Read`, `Write` | Keine |

`ablage-leser` liefert längenbegrenzte, schema-validierte JSON. `frist-rechner` hat kein MCP und kein Netz — er wendet Fristen- und Playbook-Regeln aus der Kanzleikonfiguration an. `warnungs-schreiber` erzeugt `./out/fristen-alert-<Datum>.md` und `./out/fristen-<Datum>.yaml`.

**Kein Direkt-Posting.** Der Agent veröffentlicht niemals direkt in einem Kommunikationskanal. Berichte sind Dateien. Ein `handoff_request` teilt dem Orchestrator mit, welchen Kanal er weiterleiten soll. Konfigurieren Sie den Zielkanal in der `CLAUDE.md`-Konfiguration des deployenden Teams.

**Arbeitsergebnisvermerk.** `warnungs-schreiber` stellt den Vermerk aus der `## Ausgaben`-Konfiguration des deployenden Teams voran. Bestätigen Sie den Vermerk mit dem Team — er unterscheidet sich je nach Prüferrolle (Syndikusrechtsanwalt vs. externer Berater).

## Anpassungshinweise

- **Archiv-URLs.** Setzen Sie `IMANAGE_MCP_URL`, `SHAREPOINT_MCP_URL` und `DMS_MCP_URL` auf die Endpunkte Ihres Deployments. Der Standard aktiviert iManage und SharePoint; wechseln Sie die `default_config` in `agent.yaml`, wenn Sie ein anderes DMS als primäres Archiv betreiben. Für reine SharePoint-Deployments deaktivieren Sie den iManage-MCP-Server.
- **Vorlaufsfenster.** Das Standardfenster ist 30–90 Tage. Passen Sie das Fenster in der Steuerungsereignis-Konfiguration an Ihre Prüfungsrhythmen an: 90 Tage für strategische Verträge mit langen Kündigungsfristen (z. B. Dauerschuldverhältnisse nach § 314 BGB), 14 Tage für kurzlaufende Dienstleistungsverträge.
- **Playbook-Abweichungen.** Der `frist-rechner` prüft Fristen gegen das in der `CLAUDE.md` hinterlegte Vertragsplaybook des Mandanten. Konfigurieren Sie dort die Standardlaufzeiten, Verlängerungsoptionen und Sonderkündigungsrechte für Ihre häufigsten Vertragstypen.
- **Ausgabeziel.** Ausgaben landen in `./out/`. Leiten Sie sie über Ihre Deploy-Pipeline in Ihren Mandatsordner oder Vertragsmanagementbereich weiter. Geben Sie dem `warnungs-schreiber` kein MCP zum Hochladen.
- **Zeitplan.** Wöchentlich für das laufende Portfolio; täglich für alle Verträge mit Fristen in weniger als 30 Tagen oder Verträge mit `priorität: hoch` im Archiv.

## Relevante Rechtsnormen (deutsches Vertragsrecht)

- **Ordentliche Kündigung:** §§ 620–626 BGB (Dienst- und Werkvertrag), § 132 HGB (Handelsvertreter), §§ 543, 573 BGB (Mietverhältnisse), § 489 BGB (Darlehenswiderruf)
- **Außerordentliche Kündigung:** § 314 BGB (Dauerschuldverhältnisse), § 626 BGB (Dienstverhältnis), § 543 BGB (Mietvertrag)
- **Automatische Verlängerung:** § 309 Nr. 9 BGB (AGB: max. 2 Jahre Erstlaufzeit, max. 1 Jahr Verlängerung), § 545 BGB (Mietvertrag), § 625 BGB (Dienstverhältnis)
- **Fristenberechnung:** §§ 186–193 BGB (allgemeine Fristen), § 193 BGB (Fristende an Feiertagen/Wochenenden), § 187 BGB (Fristbeginn)
- **Handelsvertreter:** §§ 84–92c HGB, § 89 HGB (Kündigungsfristen bis 6 Monate), § 89b HGB (Ausgleichsanspruch)
- **Lizenzen / IP:** § 31 UrhG (Nutzungsrechte), § 15 PatG (Patentlizenz), § 30 MarkenG (Markenlizenz)

Vgl. Grüneberg, BGB, 84. Aufl. 2025; Schmidt-Kessel/Kramme, in: MüKoBGB, 9. Aufl. 2022, § 314; Baumbach/Hopt, HGB, 41. Aufl. 2022, § 89.

# Managed-Agent-Vorlagen für die deutsche Kanzleipraxis

Jeder Agent in diesem Verzeichnis steht **auf zwei Wegen** bereit: als Claude-Code-Plugin für den Soforteinsatz (siehe die Hauptverzeichnisse im Repo) und als **Claude Managed Agent**-Vorlage, die das Plattformteam hinter der kanzleieigenen Ablauf-Engine betreibt. **Gleicher Agent, gleiche Skills – Oberfläche nach Wahl.** Jedes Verzeichnis unten ist ein Deploy-Manifest, das den kanonischen System-Prompt und die Skills aus dem zugehörigen Plugin referenziert, sodass es nur eine Quelle der Wahrheit gibt.

Dies sind **Kochbücher, keine fertigen Produkte.** Sie sind Ausgangspunkte. Passen Sie sie an Ihr Dokumentenverwaltungssystem, Ihr Vertragsarchiv, Ihren Kommunikationskanal, Ihre Benachrichtigungsweiterleitung und Ihren Prüfungsrhythmus an. Sie funktionieren nicht ohne diese Anpassung – und das ist so beabsichtigt.

Führen Sie `../scripts/agentenrezept-ausliefern.sh <slug>` aus, um Skills hochzuladen, Leaf-Worker zu erstellen und `POST /v1/agents` mit der aufgelösten Konfiguration aufzurufen. Jede Vorlage enthält [`steering-examples.json`](./aufsichts-monitor/steering-examples.json) und eine agentenspezifische README mit Sicherheitsstufe und Übergaben.

| Agent | Vertikales Plugin | Was überwacht wird | CMA-Steuerungsereignis | Leaf-Worker |
|---|---|---|---|---|
| [`aufsichts-monitor`](./aufsichts-monitor/) | regulatorisches-recht | Behördenfeeds (BAnz, BaFin-Journal, EUR-Lex, BNetzA-RSS) | `Feeds prüfen zum <Datum>, Wesentlichkeit: <Schwelle>` | feed-leser · wesentlichkeits-filter · **zusammenfassung-schreiber** |
| [`verlaengerungs-monitor`](./verlaengerungs-monitor/) | vertragsrecht | Vertragsarchiv (iManage, SharePoint, DMS) auf Verlängerungs- und Kündigungsfristen | `Verlängerungen <X>–<Y> Tage voraus prüfen, Playbook-Abweichungen melden` | ablage-leser · frist-rechner · **warnungs-schreiber** |
| [`due-diligence-tabelle`](./due-diligence-tabelle/) | gesellschaftsrecht | Virtueller Datenraum (Box, Datasite, Intralinks, iManage) auf neue Uploads + Stapelprüfung | `Ordner <Pfad> gegen Schema <Schema-ID> prüfen` | dokument-leser · extrahierer · normalisierer · **tabellen-schreiber** |
| [`gerichtskalender-monitor`](./gerichtskalender-monitor/) | prozessrecht | Gerichtskalender (eAkte-Schnittstelle, EGVP, CELEX) auf neue Eingänge, Fristen und Zustellungen | `Verfahren <Az.> beim <Gericht> beobachten, Mandat <Mandat-ID>` | terminkalender-leser · frist-zuordner · **tracker-schreiber** |

**Fett** gedruckter Leaf = der einzige Worker mit `Write`.

## Manifest vs. API

Die `agent.yaml`-Dateien verwenden die echten `POST /v1/agents`-Feldnamen mit wenigen Hilfsmitteln, die das Deploy-Skript auflöst:

| Manifest-Konvention | Wird aufgelöst zu |
|---|---|
| `system: {file: ../../<plugin>/agents/<agent>.md, append: "..."}` | `system: "<eingefügter Inhalt + append>"` |
| `system: {text: "..."}` | `system: "<Text>"` |
| `skills: [{from_plugin: ../../<plugin>}]` | lädt alle `skills/*` aus dem Verzeichnis hoch → `[{type: custom, skill_id: ...}, ...]` |
| `skills: [{path: ../../...}]` | `skills: [{type: custom, skill_id: <uploaded-id>}]` |
| `callable_agents: [{manifest: ./unteragenten/x.yaml}]` | `callable_agents: [{type: agent, id: <created-id>, version: latest}]` |

> **Research Preview:** `callable_agents` (Multi-Agent-Delegation) unterstützt **eine Delegationsebene**. Ein Orchestrator kann Worker aufrufen; Worker können keine weiteren Subagenten aufrufen.

## Agentenübergreifende Übergaben

Ein Agent kann in seiner vollständigen Textausgabe einen `handoff_request` mit `type` als erstem Schlüssel ausgeben. [`scripts/orchestrate.py`](../scripts/orchestrate.py) verarbeitet das vollständige JSON-Objekt einschließlich verschachtelter Parameter und Zeilenumbrüche. Es prüft Ziel, Auftrag und Parameter und leitet zulässige Analyseaufträge als `user.message` an eine konfigurierte Zielsitzung weiter. Externe Slack-Aufträge stehen als `needs_review` im Auditprotokoll. Die Weiterleitung stützt sich auf die geprüfte JSON-Struktur. Eine Textausgabe belegt allein keine vertrauenswürdige Herkunft des Auftrags. [Claude-Dokumentation zu Sitzungsereignissen](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)

Für den optionalen Betrieb geben Sie per `SOURCE_SESSION_ID` die Quellsitzung und per `TARGET_SESSION_IDS` eine JSON-Zuordnung der erlaubten Zielnamen zu bereits eingerichteten **Sitzungs-IDs** an. Jeder Zielname braucht eine eigene Sitzung, die sich von der Quellsitzung unterscheidet. Die frühere Variable `AGENT_IDS` direkt durch `TARGET_SESSION_IDS` ersetzen und dafür die Sitzungs-IDs des jeweiligen Deployments eintragen. Ein Übertragungsfehler beendet den Referenzlauf und wird nach Fehlertyp protokolliert. Der Referenzlauf wurde mit dem Python-SDK `anthropic` 2.8.0 und `jsonschema` 4 lokal ohne API-Zugang geprüft. Die Parser- und Versandgrenztests laufen ohne das Anthropic-SDK mit `python3 scripts/test-orchestrate.py`. [Upstream-Korrektur des JSON-Parsers](https://github.com/anthropics/claude-for-legal/commit/88c89068315dba1358dd5058ac4cdce4023682d8)

Prüfen Sie die vier Agentenrezepte lokal mit `bash scripts/agentenrezepte-pruefen.sh`. Der Trockenlauf verwendet ein gemeinsames temporäres Verzeichnis mit einem Pfadmuster für Linux und macOS. [Upstream-Korrektur für Linux](https://github.com/anthropics/claude-for-legal/commit/bf6aea18bb2b94ddf0e7f095f29c987b421c1004)

## Sicherheitsmodell

Rechtsdokumente und Schriftsätze sind **nicht vertrauenswürdige Eingaben.** Jedes Kochbuch verwendet eine Drei-Stufen-Worker-Aufteilung:

1. **Reader** berühren nicht vertrauenswürdige Dokumente und haben nur `Read`/`Grep` – kein MCP, kein Write, kein Netzwerk. Sie geben längenbegrenzte strukturierte JSON zurück. Jede Anweisung, die in einem Dokument eingebettet ist, ist Daten, kein Befehl.
2. **Analyzer** empfangen strukturierte JSON von den Readern, wenden Regeln aus der Nutzerkonfiguration an und haben MCP-Lesezugriff zur Überprüfung. Kein Write.
3. **Writer** erzeugen die endgültige Ausgabe und sind die einzige Stufe mit `Write`. Sie sehen niemals Rohdokumente.

Der Orchestrator hat kein Write und liest keine Rohdokumente. Er leitet weiter, behandelt nicht.

## Arbeitsergebnis und Verschwiegenheit

Alles, was diese Agenten erzeugen, ist in einer normalen Deployment-Umgebung **anwaltliches Arbeitsergebnis** (privileged work product). Der Headless-Append in jedem Manifest weist den Agenten an, den Arbeitsergebnisvermerk aus der Nutzerkonfiguration voranzustellen. Bestätigen Sie den Vermerk mit Ihrem Team, bevor Sie deployen.

**Mandantengeheimnis:** Gemäß § 43a Abs. 2 BRAO und § 203 StGB sind alle verarbeiteten Mandantendaten der anwaltlichen Verschwiegenheitspflicht unterworfen. Prüfen Sie Anthropics Datenaufbewahrungseinstellungen und Ihre eigene Speicheraufbewahrung vor der Inbetriebnahme.

## Was Sie bekommen und was nicht

- **Sie bekommen:** eine funktionierende Manifeststruktur, eine Referenzarchitektur mit sinnvollen Sicherheitsstufen, in Claude-Code-Plugins bewährte Skills und Steuerungsereignis-Beispiele – angepasst auf deutsche Rechtsquellen (BGH, BVerfG, BAG, BaFin, BNetzA), deutsche Behördenfeeds und deutsches Verfahrensrecht.
- **Sie bekommen nicht:** einen produktionsfertigen Agenten. Sie müssen die MCP-Konnektoren an *Ihre* Systeme anschließen, den Rhythmus festlegen, die Benachrichtigungsweiterleitung konfigurieren, die Prompts für Ihre Praxis anpassen und eine eigene Evaluation durchführen, bevor Sie dem Output vertrauen.
- **Sie bekommen insbesondere nicht:** einen Ersatz für einen Rechtsanwalt. Diese Agenten überwachen, extrahieren und entwerfen. Ein Anwalt prüft, verifiziert, entscheidet.

## Deutsches Recht – Rechtsrahmen

Die Agenten arbeiten ausschließlich nach deutschem Recht. Maßgebliche Normen und Quellen:

| Bereich | Deutsches Recht |
|---|---|
| Informationsbeschaffung | §§ 142, 144 ZPO; Auskunftsanspruch § 810 BGB; Stufenklage § 254 ZPO |
| Behördenveröffentlichungen | Bundesanzeiger, BaFin-Veröffentlichungen, EUR-Lex, BNetzA |
| Verfahrensordnungen | ZPO, FamFG, VwGO; Geschäftsordnungen der Gerichte |
| Gerichtsdaten | eAkte-Schnittstellen (EGVP), Gerichtsportale der Länder |
| Dokumentenverwaltung | iManage, SharePoint, DMS (DATEV, d.velop) |
| Anwaltsgeheimnis | § 43a Abs. 2 BRAO; § 203 StGB; § 53 StPO; § 383 ZPO |
| Berufsrecht | BRAO, BORA, FAO, RVG |
| Berufskammern | Rechtsanwaltskammer (RAK), BRAK |

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

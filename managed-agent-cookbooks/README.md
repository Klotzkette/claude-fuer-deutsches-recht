# Managed-Agent-Vorlagen für die deutsche Kanzleipraxis

Jeder Agent in diesem Verzeichnis steht **auf zwei Wegen** bereit: als Claude-Code-Plugin für den Soforteinsatz (siehe die Hauptverzeichnisse im Repo) und als **Claude Managed Agent**-Vorlage, die das Plattformteam hinter der kanzleieigenen Workflow-Engine betreibt. **Gleicher Agent, gleiche Skills – Oberfläche nach Wahl.** Jedes Verzeichnis unten ist ein Deploy-Manifest, das den kanonischen System-Prompt und die Skills aus dem zugehörigen Plugin referenziert, sodass es nur eine Quelle der Wahrheit gibt.

Dies sind **Kochbücher, keine fertigen Produkte.** Sie sind Ausgangspunkte. Passen Sie sie an Ihr Dokumentenverwaltungssystem, Ihr Vertragsarchiv, Ihren Kommunikationskanal, Ihre Benachrichtigungsweiterleitung und Ihren Prüfungsrhythmus an. Sie funktionieren nicht ohne diese Anpassung – und das ist so beabsichtigt.

Führen Sie `../scripts/deploy-managed-agent.sh <slug>` aus, um Skills hochzuladen, Leaf-Worker zu erstellen und `POST /v1/agents` mit der aufgelösten Konfiguration aufzurufen. Jede Vorlage enthält [`steering-examples.json`](./aufsichts-monitor/steering-examples.json) und eine agentenspezifische README mit Sicherheitsstufe und Übergaben.

| Agent | Vertikales Plugin | Was überwacht wird | CMA-Steuerungsereignis | Leaf-Worker |
|---|---|---|---|---|
| [`aufsichts-monitor`](./aufsichts-monitor/) | regulatory-legal | Behördenfeeds (BAnz, BaFin-Journal, EUR-Lex, BNetzA-RSS) | `Feeds prüfen zum <Datum>, Wesentlichkeit: <Schwelle>` | feed-reader · materiality-filter · **digest-writer** |
| [`verlaengerungs-monitor`](./verlaengerungs-monitor/) | commercial-legal | Vertragsarchiv (iManage, SharePoint, DMS) auf Verlängerungs- und Kündigungsfristen | `Verlängerungen <X>–<Y> Tage voraus prüfen, Playbook-Abweichungen melden` | repo-reader · deadline-calculator · **alert-writer** |
| [`due-diligence-tabelle`](./due-diligence-tabelle/) | corporate-legal | Virtueller Datenraum (Box, Datasite, Intralinks, iManage) auf neue Uploads + Stapelprüfung | `Ordner <Pfad> gegen Schema <Schema-ID> prüfen` | doc-reader · extractor · normalizer · **grid-writer** |
| [`launch-radar`](./launch-radar/) | product-legal | Produkt-Roadmap/-Tracker (Jira, Linear, Asana) auf Launches mit rechtlichem Prüfbedarf | `Tracker auf Launches in den nächsten <N> Wochen prüfen` | tracker-reader · risk-classifier · **memo-writer** |
| [`gerichtskalender-monitor`](./gerichtskalender-monitor/) | litigation-legal | Gerichtskalender (eAkte-Schnittstelle, EGVP, CELEX) auf neue Eingänge, Fristen und Zustellungen | `Verfahren <Az.> beim <Gericht> beobachten, Mandat <Mandat-ID>` | docket-reader · deadline-mapper · **tracker-writer** |

**Fett** gedruckter Leaf = der einzige Worker mit `Write`.

## Manifest vs. API

Die `agent.yaml`-Dateien verwenden die echten `POST /v1/agents`-Feldnamen mit wenigen Hilfsmitteln, die das Deploy-Skript auflöst:

| Manifest-Konvention | Wird aufgelöst zu |
|---|---|
| `system: {file: ../../<plugin>/agents/<agent>.md, append: "..."}` | `system: "<eingefügter Inhalt + append>"` |
| `system: {text: "..."}` | `system: "<Text>"` |
| `skills: [{from_plugin: ../../<plugin>}]` | lädt alle `skills/*` aus dem Verzeichnis hoch → `[{type: custom, skill_id: ...}, ...]` |
| `skills: [{path: ../../...}]` | `skills: [{type: custom, skill_id: <uploaded-id>}]` |
| `callable_agents: [{manifest: ./subagents/x.yaml}]` | `callable_agents: [{type: agent, id: <created-id>, version: latest}]` |

> **Research Preview:** `callable_agents` (Multi-Agent-Delegation) unterstützt **eine Delegationsebene**. Ein Orchestrator kann Worker aufrufen; Worker können keine weiteren Subagenten aufrufen.

## Agentenübergreifende Übergaben

Benannte Agenten rufen sich niemals direkt gegenseitig auf. Wenn ein Agent einen anderen benötigt (z. B. ermittelt `launch-radar` einen Launch, der ein vollständiges Prüfungsmemo benötigt), sendet er einen `handoff_request` in seiner Ausgabe; [`../scripts/orchestrate.py`](../scripts/orchestrate.py) (oder Ihr eigener Event-Bus) leitet ihn als neues Steuerungsereignis an die Zielsitzung weiter. Das Referenzskript hat eine Hartcodierung zulässiger Ziele und validiert Nutzdaten gegen ein Schema.

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

## Deutsches Recht – Besonderheiten

| US-Konzept (Ursprungsversion) | Deutsche Entsprechung (diese Version) |
|---|---|
| Discovery / Subpoena | §§ 142, 144 ZPO; Auskunftsanspruch § 810 BGB; Stufenklage § 254 ZPO |
| Federal Register / SEC | Bundesanzeiger, BaFin-Veröffentlichungen, EUR-Lex, BNetzA |
| FRCP / Local Rules | ZPO, FamFG, VwGO; Geschäftsordnungen der Gerichte |
| Court dockets (PACER/CourtListener) | eAkte-Schnittstellen (EGVP), Gerichtsportale der Länder |
| CLM (Ironclad) | iManage, SharePoint, DMS (DATEV, d.velop) |
| Privilege log | Anwaltsgeheimnis § 43a Abs. 2 BRAO; § 203 StGB; § 53 StPO; § 383 ZPO |
| ABA Model Rules | BRAO, BORA, FAO, RVG |
| Bar association | Rechtsanwaltskammer (RAK), BRAK |

**Zitierweise:** Alle System-Prompts und Ausgaben folgen dem BGH-/Beck-Stil gemäß `references/zitierweise.md`. Rechtsprechung ist nicht bindend (keine stare decisis), außer § 31 BVerfGG. Kommentare und Aufsätze sind argumentativ tragend.

# Gerichtskalender-Monitor — Managed-Agent-Vorlage

## Übersicht

Überwacht Gerichtskalender, elektronische Akten (eAkte) und Zustellnachweise für Verfahren im aktiven Prozessportfolio. Für jedes aktive Mandat ruft der Agent neue Eingänge seit der letzten Prüfung ab, ordnet Eingangstypen Kandidaten-Fristen zu, gleicht gegen die Verfahrenshistorie und offene Fristen ab und erstellt einen Verfahrensstatusbericht sowie einen strukturierten Fristenkalender.

Der Agent ist an das deutsche Verfahrensrecht angepasst: ZPO (Zivilprozess), StPO (Strafprozess), VwGO (Verwaltungsprozess), FamFG (Familiensachen), ArbGG (Arbeitsgerichtsverfahren), SGG (Sozialgerichtsverfahren). Schnittstellen: EGVP (Elektronisches Gerichts- und Verwaltungspostfach), beA (besonderes elektronisches Anwaltspostfach), CELEX (EUR-Lex), Bundesgerichtshof-Datenbank.

Gleiche Quelle wie der [`docket-watcher`](../../litigation-legal/agenten/docket-watcher.md)-Agent im litigation-legal-Claude-Code-Plugin – dieses Verzeichnis ist das Managed-Agent-Kochbuch für `POST /v1/agents`.

## ⚠️ Vor dem Deployment

- **Berechnete Fristen sind Hinweise, keine Kalendereinträge.** Gerichtliche Fristenregeln variieren je nach Gericht, Richter und Einzelanordnung (§ 224 ZPO, Verlängerungsanträge). Eine versäumte Gerichtsfrist hat Haftungsfolgen. Ein zugelassener Rechtsanwalt prüft jede berechnete Frist gegen die tatsächlichen Verfahrensvorschriften und etwaige gerichtliche Verfügungen, bevor sie eingetragen wird.
- **Eingangsklassifizierungen sind heuristisch.** Ein Eingang, den der Agent falsch klassifiziert – ein Prozesskostenhilfeantrag, der als Sachantrag gelesen wird, ein Vergleichsangebot, das als streitiger Schriftsatz gelesen wird – kann eine falsche Fristenregel erzeugen. Lesen Sie den Eingang; vertrauen Sie nicht der Bezeichnung.
- **Ein unbekanntes Gericht ist kein Standardwert.** Wenn die Fristentabelle ein Gericht nicht abdeckt, muss der Mapper `confidence: niedrig` + `verifizierung_erforderlich: true` zurückgeben, niemals einen stillen Standard. Wenn Sie eine sichere Frist bei einem unbekannten Gericht sehen, behandeln Sie die Regeltabelle als veraltet bis zum Beweis des Gegenteils.
- **Ein ruhiger Kalender ist kein sauberer Kalender.** Gerichtliche Eingänge werden manchmal verzögert zugestellt. Protokollnotizen kommen manchmal Tage nach dem Ereignis. „Keine neuen Eingänge" ist eine Aussage über den Datenstand, nicht über den Verfahrensstand.

## Deployment

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export EGVP_MCP_URL=...          # Elektronisches Gerichts- und Verwaltungspostfach
export BEA_MCP_URL=...           # besonderes elektronisches Anwaltspostfach
export GDRIVE_MCP_URL=...        # Jurisdiktionskonfigurations-Tabellen
../../scripts/deploy-managed-agent.sh gerichtskalender-monitor
```

## Steuerungsereignisse

Siehe [`steering-examples.json`](./steering-examples.json).

## Sicherheit und Übergaben

Gerichtliche Eingänge sind öffentliche Dokumente (soweit nicht unter Verschlusssache gestellt), aber sie sind auch NICHT VERTRAUENSWÜRDIGE EINGABEN. Der Einreicher kontrolliert den Text und kann Prompts, URLs und Anweisungen einbetten, die auf den Agenten abzielen. Drei-Stufen-Isolation:

| Stufe | Berührt Eingänge? | Tools | Konnektoren |
|---|---|---|---|
| **`docket-reader`** | **Ja** | nur `Read`, `Grep` | EGVP, beA, Gerichtsportale (nur lesend) |
| `deadline-mapper` / Orchestrator | Nein — sieht nur strukturiertes JSON | `Read`, `Grep`, `Glob`, `Agent` | gdrive (Jurisdiktionskonfiguration, nur lesend) |
| **`tracker-writer`** (Write-Inhaber) | Nein | `Read`, `Write`, `Edit` | Keine |

`docket-reader` liefert längenbegrenzte, schema-validierte JSON. `deadline-mapper` hat kein MCP und kein Web – er wendet Regeln an, die das deployende Team konfiguriert hat. `tracker-writer` erzeugt `./out/verfahrensbericht-<Datum>.md` und `./out/fristen.yaml` und sieht niemals Rohkopien von Eingängen.

## Anpassungshinweise

Dieses Kochbuch ist ein Ausgangspunkt. Es wird in der Produktion nicht funktionieren, bis Sie folgendes getan haben:

- **MCP-URLs setzen.** `EGVP_MCP_URL` und `BEA_MCP_URL` müssen auf die Endpunkte Ihres Deployments zeigen, mit welcher Authentifizierung Ihre Plattform benötigt. `GDRIVE_MCP_URL` (oder ein Ersatz) zeigt auf den Speicherort Ihrer Fristentabellen.
- **Portfolio laden.** Der Agent liest `verfahren/_log.yaml` plus die `az` (Aktenzeichen) und `gericht` pro Verfahren aus der litigation-legal-Konfiguration des deployenden Teams. Wenn Ihr Kanzleiverwaltungssystem die Quelle der Wahrheit ist, verbinden Sie es über ein MCP oder führen Sie eine Synchronisierung in den Konfigurationspfad durch.
- **Jurisdiktionsregeln konfigurieren.** Versorgen Sie den deadline-mapper mit einer Fristentabelle für jedes Gericht in Ihrem Portfolio. Bundesrechtsregeln (ZPO, VwGO, ArbGG, SGG) können einmal kodiert werden; Landesgerichte und einzelne Richter sind die Risikobereiche. Ein unbekanntes Gericht sollte `confidence: niedrig` + `verifizierung_erforderlich: true` erzeugen, niemals einen stillen Standard.
- **Zustellung verkabeln.** Entscheiden Sie, wohin die Ausgabe geht: Ihr Kanzleiverwaltungssystem liest `./out/fristen.yaml`; der Berichtbericht geht in Slack, E-Mail oder Ihren Mandatsverwaltungsbereich; kritische Markierungen werden an denjenigen weitergeleitet, den Sie benachrichtigt haben möchten.
- **Zeitplan setzen.** Wöchentlich für die meisten Verfahren; täglich für alles mit einer Verhandlung in weniger als 14 Tagen, jedes Verfahren in der Phase `Berufung`/`Revision` oder jedes Mandat mit `risiko: kritisch`.

## Berechnete Fristen sind Hinweise, keine Kalendereinträge

**Die berechneten Fristen dieses Agenten erfordern menschliche Verifizierung gegen die maßgebliche Verfahrensordnung, etwaige Einzelanordnungen des Gerichts und den konkreten Zustellungszeitpunkt, bevor sie eingetragen werden. Das Verpassen einer Gerichtsfrist hat haftungsrechtliche Konsequenzen für den Anwalt (§§ 280, 611 BGB i.V.m. BRAO-Berufspflichten). Dieser Agent ermittelt Fristen; ein Mensch verifiziert und trägt sie ein.**

Jede Frist führt `confidence`- und `verifizierung_erforderlich`-Felder. Der Bericht trennt Einträge mit niedriger Konfidenz und kennzeichnet alles, was nicht aus einer eindeutigen gesetzlichen Norm abgeleitet ist. Behandeln Sie das als Minimum – nicht als Obergrenze – der menschlichen Prüfung.

## Relevante Rechtsnormen

- **ZPO-Fristen:** § 132 ZPO (Einreichungsfristen), § 224 ZPO (Fristverlängerung), §§ 233 ff. ZPO (Wiedereinsetzung), §§ 276, 277 ZPO (Klagebeantwortung)
- **Berufung/Revision:** §§ 517, 548 ZPO (Berufungs-/Revisionsfrist: 1 Monat), §§ 519, 549 ZPO (Begründungsfrist: 2 Monate)
- **Verwaltungsgericht:** § 74 VwGO (Klagefrist: 1 Monat), § 124a VwGO (Zulassungsantrag)
- **Arbeitsgericht:** § 61b ArbGG (Kündigungsschutzklage: 3 Wochen), §§ 64, 66 ArbGG (Berufung)
- **Berechnung:** §§ 186–193 BGB (Fristenberechnung), § 222 ZPO
- **Zustellung:** §§ 166 ff. ZPO, beA-Verordnung (BRAV)
- **Wiedereinsetzung:** BGH, Beschl. v. 27.09.2022 – VI ZB 67/21, NJW-RR 2022, 1571 (Anforderungen an anwaltliche Fristenkontrolle)

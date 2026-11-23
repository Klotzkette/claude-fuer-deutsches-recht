# Konnektoren und Datenquellen

Empfohlene MCP-/Tool-Konnektoren für die Arbeit mit diesem Repository. Pflicht: Alle Datenquellen mit Mandantenbezug erfordern einen Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO.

## Juristische Recherche

| Quelle | Hinweis |
| --- | --- |
| Beck-Online | Lizenzpflichtige juristische Datenbank für Quellenprüfung; nur verwenden, wenn ein konkreter lizenzierter Zugriff besteht. |
| juris | BGH-, BVerfG-, OLG-Rechtsprechung; Fundstellenverknüpfung. |
| Otto Schmidt Online | ZIP, GmbHR, AG, MwStR. |
| Wolters Kluwer Online | NZG, BB, DStR. |
| rechtsprechung-im-internet.de | Amtliche Veröffentlichung des BMJ. Frei zugänglich. |
| openJur | Frei zugängliches Rechtsprechungs-Repository. |
| dejure.org | Norm- und Rechtsprechungsverlinkung, Volltext häufig. |
| Open Legal Data | Frei zugängliche, nichtamtliche Datenbank für deutsche Rechtsprechung und Gesetze. Der optionale MCP-Server lässt sich ohne Anmeldung zur Recherche nutzen. [Open Legal Data einrichten](#open-legal-data-einrichten) |
| gesetze-im-internet.de | Amtliche Bundesgesetze. |
| bundesanzeiger.de | Veröffentlichungen, HRB-Einträge, Bilanzen. |
| EUR-Lex | Konsolidierte EU-Rechtsakte (z. B. DORA VO 2022/2554), Anhänge, delegierte VO und ITS; CELEX-Aufruf `eur-lex://celex/<CELEX>`. |
| ESA-Feeds | EBA, ESMA, EIOPA Final Reports, Q&A, Roadmaps. |
| handelsregister.de | HRB/HRA-Auszüge (entgeltlich). |
| transparenzregister.de | wirtschaftliche Berechtigte (GwG). |

## Steuern, Behörden, Wirtschaft

| Quelle | Hinweis |
| --- | --- |
| ELSTER | Steuerportal Finanzverwaltung, UStVA, ESt. |
| eBundesanzeiger | Pflichtveröffentlichungen. |
| DPMA Register | Markenrecherche (DPMAregister) – frei. |
| EUIPO (eSearch+) | EU-Marken. |
| WIPO Global Brand DB | weltweite Markenrecherche. |
| EPO Espacenet | Patente. |
| Mahnportal online-mahnantrag.de | gemeinsames Mahnportal der Länder. |
| beA | besonderes elektronisches Anwaltspostfach (für Schriftsatzversand). |

## Kanzlei-IT (Praxisanbindung)

| Konnektor | Zweck |
| --- | --- |
| RA-MICRO / Advoware / DATEV Anwalt / NoRA / Advolux | Kanzleisoftware-Integration. |
| Microsoft 365 / Outlook | Fristenkalender, Posteingang. |
| Nextcloud / SharePoint | Mandatsordner. |
| beA-Anbindung | Schriftsatzversand. |
| DocuSign / FP Sign / yousign | qualifizierte elektronische Signatur (eIDAS). |

## Datenschutz und KI

- Vor Einbindung externer KI-/Cloud-Tools: AVV einholen, ggf. TIA (Transfer Impact Assessment).
- US-Anbieter unter DPF (Data Privacy Framework) prüfen.
- Vor Anonymisierung/Pseudonymisierung: § 3 Abs. 1 BDSG, Art. 4 Nr. 5 DSGVO.

## Open Legal Data einrichten

Die Plugin-Installation und die Einrichtung des externen Suchdienstes erfolgen getrennt. Wähle den passenden Zugang für deinen Client. [Anbieteranleitung](https://de.openlegaldata.io/pages/api/#mcp) · [Eintrag in der MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.openlegaldata%2Fde/versions/latest)

| Client | Einrichtung |
| --- | --- |
| Claude Code | `claude mcp add --transport http open-legal-data-de https://de.openlegaldata.io/mcp` |
| Claude mit benutzerdefinierten Konnektoren | In den Konnektor-Einstellungen einen benutzerdefinierten Konnektor mit der URL `https://de.openlegaldata.io/mcp` hinzufügen. |
| Codex CLI oder IDE | `codex mcp add open-legal-data-de --url https://de.openlegaldata.io/mcp` |

Für eine projektbezogene Konfiguration in Claude Code kannst du den HTTP-Server in die `.mcp.json` eintragen. Wenn die Datei bereits weitere Server enthält, ergänze den Eintrag unter `mcpServers`.

```json
{
  "mcpServers": {
    "open-legal-data-de": {
      "type": "http",
      "url": "https://de.openlegaldata.io/mcp"
    }
  }
}
```

Verwende veröffentlichte Fundstellen oder abstrakte Rechtsfragen. Der Anbieter protokolliert gekürzte Suchparameter. Namen aus einem Mandat, interne Aktenzeichen und Mandatssachverhalte gehören deshalb nicht in die Anfrage. [Datenschutzhinweise des Anbieters](https://de.openlegaldata.io/pages/privacy/#9-api-und-mcp-server)

Gleiche bei Treffern Gericht, Datum und gegebenenfalls ECLI ab. Das Aktenzeichen `5 Sa 108/23` kommt beispielsweise beim LAG Mecklenburg-Vorpommern und beim LAG Rheinland-Pfalz vor. Prüfe die tragende Passage vor dem Zitieren in der amtlichen Fassung. [LAG Mecklenburg-Vorpommern, 02.07.2024](https://de.openlegaldata.io/case/lagmv-2024-07-02-5-sa-10823) · [LAG Rheinland-Pfalz, 25.01.2024](https://de.openlegaldata.io/case/lagrlp-2024-01-25-5-sa-10823)

## Beispielkonfiguration für eigene lokale Adapter

Die folgenden `./mcp/*.js`-Pfade sind Platzhalter für separat bereitgestellte Adapter. Trage nur Adapter ein, die bei dir vorhanden und für die jeweilige Quelle freigegeben sind.

```jsonc
{
  "mcpServers": {
    "beck-online": { "command": "node", "args": ["./mcp/beck-online.js"], "env": { "BECK_TOKEN": "${BECK_TOKEN}" } },
    "juris":        { "command": "node", "args": ["./mcp/juris.js"],        "env": { "JURIS_TOKEN": "${JURIS_TOKEN}" } },
    "outlook":      { "command": "node", "args": ["./mcp/outlook.js"] },
    "handelsregister": { "command": "node", "args": ["./mcp/handelsregister.js"] },
    "dpma":         { "command": "node", "args": ["./mcp/dpma.js"] },
    "elster":       { "command": "node", "args": ["./mcp/elster.js"] },
    "eur-lex":      { "command": "node", "args": ["./mcp/eur-lex.js"] },
    "esa-feeds":    { "command": "node", "args": ["./mcp/esa-feeds.js"] }
  }
}
```

Hinweis: Die Beck-/juris-Konnektoren sind nicht Teil dieses Repositories. Setze sie nach den AGB des jeweiligen Anbieters auf.

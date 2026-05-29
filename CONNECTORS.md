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

## Beispielkonfiguration `.mcp.json`

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

# Schnellstart

Diese Anleitung führt in 5 Minuten zur ersten produktiven Nutzung der Plugins in Claude Code oder Claude Desktop.

## 1. Voraussetzungen

- Claude Code ≥ 1.0 oder Claude Desktop ≥ 0.7.
- Optional: ein lokaler Mandats-/Aktenordner.
- Optional: Zugang zu Beck-Online, juris, NJW-Online, OAJG für aktuelle Fundstellen.

## 2. Installation

### Option A – Marketplace direkt aus GitHub

```bash
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht
/plugin install vertragsrecht
/plugin install datenschutzrecht
```

### Option B – Lokal aus Klon

```bash
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht
/plugin marketplace add .
/plugin install arbeitsrecht
```

### Option C – Einzelnes Plugin direkt

```bash
/plugin install ./prozessrecht
```

## 3. Mandatsordner anlegen

Empfohlene Struktur (siehe Skill `matter-workspace` in jedem Plugin):

```
~/Mandate/
└── 2026-0142_Mueller_Kuendigung/
    ├── 01_korrespondenz/
    ├── 02_schriftsaetze/
    ├── 03_urkunden/
    ├── 04_recherche/
    ├── 05_fristen/
    └── mandat.yaml
```

## 4. Erste Tests

### Arbeitsrecht – Kündigungsschutzklage

```
Lade Skill kuendigungsschutzklage. Mandant: Müller, Arbeitnehmer seit 2018,
ordentliche Kündigung erhalten am 10.05.2026, Zugang 12.05.2026,
Begründung "betriebsbedingt". Entwirf Klageschrift und prüfe 3-Wochen-Frist.
```

### Prozessrecht – Mahnverfahren

```
Lade Skill mahnbescheid. Gläubiger: GmbH X, Schuldner: Y, Forderung 12.430,50 €
aus Rechnung 2026-0017, fällig 14.04.2026. Erstelle Antrag.
```

### Datenschutz – DSGVO-Auskunft

```
Lade Skill dsgvo-auskunft. Mandant hat Auskunftsersuchen erhalten,
Verantwortlicher ist Plattformbetreiber, Frist Art. 12 III DSGVO. Erstelle Antwortentwurf
mit Hinweis auf §§ 29 BDSG, 5 GeschGehG.
```

## 5. Verbindliche Regeln in jedem Skill

- Jede juristische Aussage wird belegt – nach [`references/zitierweise.md`](./references/zitierweise.md).
- Bei umstrittenen Fragen werden h. M. und Gegenauffassung getrennt zitiert.
- Bei fehlender Rspr. wird dies ausdrücklich kenntlich gemacht ("soweit ersichtlich noch nicht entschieden").
- Mandantengeheimnis: keine Übermittlung mandatsbezogener Daten an Tools ohne Auftragsverarbeitungsvertrag (AVV).

## 6. Tipps

- **Frist zuerst prüfen.** Jeder Skill, der eine Klage/Anfechtung/Berufung berührt, beginnt mit Fristprüfung.
- **Streitwert berechnen.** Skill `streitwert` (in `prozessrecht`) liefert RVG/GKG-Tabellenauszüge.
- **Vorlagen anpassen.** Die SKILL.md-Dateien sind Markdown – frei editierbar. Eigene Kanzleilogik gerne in `kanzlei-builder-hub` ergänzen.
- **Quellen verifizieren.** Auch der beste Skill kann Aktenzeichen halluzinieren – immer in Beck-Online/juris gegenchecken.

## 7. Troubleshooting

| Problem | Lösung |
| --- | --- |
| Skill wird nicht gefunden | `plugin.json` enthält Pfad? `/plugin reload` ausführen. |
| MCP-Tool antwortet nicht | `.mcp.json` prüfen, Server neu starten. |
| Falsche Fundstelle | manuell in Beck-Online prüfen und Skill korrigieren – PR willkommen. |
| Datenschutzfrage | Skill `datenschutzrecht/mandantendaten-ki` aufrufen. |

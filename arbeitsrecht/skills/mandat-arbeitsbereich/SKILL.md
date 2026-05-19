---
name: mandat-arbeitsbereich
description: Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen. Verhindert, dass Kontext von einem Mandat in ein anderes übergeht. Relevant für Kanzleien mit mehreren Mandanten; für Syndikusrechtsanwälte deaktiviert.
language: de
triggers:
  - "neue akte"
  - "mandat wechseln"
  - "mandat-arbeitsbereich"
  - "mandatsakte"
  - "mandat anlegen"
argument-hint: "<neu | auflisten | wechseln | schließen | keine> [kürzel]"
---

# /arbeitsrecht:mandat-arbeitsbereich

Anwälte und Kanzleien arbeiten für mehrere Mandanten gleichzeitig. Eine Mandatsakte hält den Kontext eines Mandanten strikt von allen anderen getrennt. Dieser Skill verwaltet diese Akten.

## Zweck

Für Kanzleien mit mehreren Mandanten (Einzelkanzlei, Mittelkanzlei, Großkanzlei). Für Syndikusrechtsanwälte mit einem Arbeitgeber ist diese Funktion standardmäßig **deaktiviert** – alle Skills nutzen automatisch den Kanzlei-/Unternehmenskontext.

Im Arbeitsrecht entspricht eine „Akte" typischerweise einem bestimmten Mandanten-Sachverhalt:
- Eine konkrete Kündigung oder Kündigungsschutzklage
- Eine interne Untersuchung
- Ein Entsendungsprojekt
- Ein Tarifvertragsstreit
- Eine Massenentlassung / Betriebsänderung

## Eingaben

- Befehl: `neu`, `auflisten`, `wechseln`, `schließen` oder `keine`
- Kürzel der Akte (Slug), z.B. `mueller-ksg-2024`
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` – Abschnitt `## Mandantenakten`

## Ablauf

### Vorabprüfung

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` lesen, Abschnitt `## Mandantenakten` prüfen.

Falls `Aktiviert: ✗` (Syndikus / in-house):
> Mandantenakten sind deaktiviert – Sie sind als [Kanzlei/in-house] konfiguriert und arbeiten mit einem einzigen Mandantenkontext. Falls Sie tatsächlich mehrere Mandanten betreuen, führen Sie `/arbeitsrecht:kaltstart-interview --redo` aus und wählen Sie Kanzleibetrieb. Andernfalls benötigen Sie `/arbeitsrecht:mandat-arbeitsbereich` nicht.

### Befehle

**`neu <kürzel>`** – Neue Mandatsakte anlegen.
1. Kürzel in Kleinbuchstaben, Bindestriche erlaubt (z.B. `mueller-ksg-2024`).
2. Kurzes Intake-Interview:
   > - Mandantenname (intern, nicht für Ausgaben)
   > - Sachverhalt in einem Satz (Kündigung / Untersuchung / Entsendung / Tarifstreit)
   > - Zuständiger Anwalt
   > - Aktenstatus: offen / ruhend / geschlossen
   > - Besondere Vertraulichkeitsstufe?
3. `mandat.md`, `verlauf.md` und `notizen.md` anlegen unter:
   `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/akten/<kürzel>/`

**`auflisten`** – Alle Akten tabellarisch mit Status und aktive-Akte-Flag anzeigen.

**`wechseln <kürzel>`** – Aktive Akte setzen. Alle folgenden Skill-Aufrufe arbeiten im Kontext dieser Akte.

**`schließen <kürzel>`** – Akte archivieren (in `_archiv/` verschieben, nie löschen). Keine Daten vernichten.

**`keine`** – Vom aktiven Mandat lösen; auf Kanzlei-Ebene-Kontext zurücksetzen.

### Aktenübergreifender Kontext

Bei `Aktenübergreifender Kontext: deaktiviert` (Standard): Ein Skill, der in Akte A arbeitet, liest niemals Dateien aus Akte B. Dies ist datenschutzrechtlich geboten (§ 43a Abs. 2 BRAO, § 26 BDSG): Personalakte eines Arbeitnehmers darf nicht in die Analyse eines anderen einfließen.

Lerneffekte, die mehrere Mandate betreffen, werden in die Kanzlei-CLAUDE.md geschrieben, nicht in eine Akten-Datei.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht des Rechtsanwalts)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- § 26 BDSG (Beschäftigtendatenschutz; gilt auch für anwaltlich bearbeitete Personaldaten)
- § 53 StPO (Zeugnisverweigerungsrecht des Rechtsanwalts)

## Ausgabeformat

**Neu:**
```
Mandatsakte angelegt: mueller-ksg-2024
========================================
Mandant:    [intern anonymisiert]
Sachverhalt: Kündigungsschutzklage nach betriebsbedingter Kündigung
Anwalt:     [Name]
Status:     offen
Ablage:     ~/.../akten/mueller-ksg-2024/

Dateien erstellt:
  mandat.md    – Akten-Stammdaten und Kontext
  verlauf.md   – Chronologisches Protokoll
  notizen.md   – Freie Notizen, entwürfe, Recherche-Ergebnisse
```

**Auflisten:**
```
Mandantenakten – Arbeitsrecht
=================================
● mueller-ksg-2024     [offen]    Kündigungsschutzklage      geändert: heute
  bayer-betriebsrat    [ruhend]   BR-Streitigkeit § 87 BetrVG   geändert: vor 3 Wo.
  huber-entsendung     [offen]    Entsendung Frankreich          geändert: gestern

● = aktive Akte
```

## Beispiele

```
/arbeitsrecht:mandat-arbeitsbereich neu mueller-ksg-2024
Kündigung wegen betriebsbedingter Restrukturierung, Sozialauswahl streitig.
```

```
/arbeitsrecht:mandat-arbeitsbereich wechseln bayer-betriebsrat
```

```
/arbeitsrecht:mandat-arbeitsbereich auflisten
```

## Risiken / typische Fehler

- **Akten nicht schließen, wenn das Mandat endet.** Archivieren statt löschen – BRAO § 50 Abs. 2 schreibt 5 Jahre Aufbewahrung vor.
- **Mandant nicht anonymisieren.** Kürzel und interne Bezeichnung sollten nicht von Unbefugten identifiziert werden können.
- **Aktenübergreifende Suche ungewollt aktivieren.** Standardmäßig deaktiviert aus datenschutzrechtlichen Gründen.

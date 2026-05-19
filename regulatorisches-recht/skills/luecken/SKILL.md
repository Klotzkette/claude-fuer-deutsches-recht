---
name: luecken
description: Offenen Gap-Tracker anzeigen und verwalten. Laden, um zu sehen, welche Compliance-Lücken gemeldet wurden, was noch offen ist und was in Bearbeitung ist.
language: de
triggers:
  - "gaps"
  - "offene Lücken"
  - "Gap-Tracker"
  - "Compliance-Lücken anzeigen"
  - "was ist noch offen"
---

# Gap-Tracker

## Zweck

Dieser Skill liest und aktualisiert den Gap-Tracker. Er zeigt alle offenen, in Bearbeitung befindlichen und geschlossenen Compliance-Lücken aus dem letzten `luecken-aufzeiger`-Lauf an. Er ermöglicht das Setzen von Eigentümern, das Aktualisieren des Status und das Eskalieren von Gaps mit Fristüberschreitung.

## Eingaben

- Gap-Tracker-Datei: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`
- Optional: Filter (nach Schweregrad, Frist, Eigentümer, Status)
- Optional: Gap-ID zum gezielten Aktualisieren

## Ablauf

### 1. Tracker lesen

Gap-Tracker lesen. Falls nicht vorhanden:
```
Noch keine Gaps erfasst. Starten Sie mit /regulatorisches-recht:luecken-aufzeiger, 
um eine Gap-Analyse gegen eine Aufsichtsverlautbarung durchzuführen.
```

### 2. Status-Übersicht ausgeben

```
Gap-Übersicht – Stand: TT.MM.JJJJ

Gesamt: N | 🔴 Blockierend: N | 🟠 Hoch: N | 🟡 Mittel: N | 🟢 Gering: N
Offen: N | In Bearbeitung: N | Geschlossen: N | Überfällig: N
```

### 3. Sortierte Gap-Tabelle ausgeben

| Gap-ID | Verlautbarung | Anforderung (Kurzfassung) | Schwere | Frist | Eigentümer | Status |
|---|---|---|---|---|---|---|
| GAP-2025-001 | MaRisk AT 4.3.2 | Datenhaltung 10 Jahre | 🔴 | 31.12.2025 | Compliance | offen |

Sortierung: zuerst 🔴, dann nach Frist aufsteigend.

### 4. Aktionen anbieten

Nach der Übersicht:
```
Was möchten Sie tun?
a) Gap schließen (Gap-ID angeben)
b) Eigentümer setzen / ändern
c) Status aktualisieren (offen → in Bearbeitung → geschlossen)
d) Richtlinienneufassung für einen Gap starten → /richtlinien-neufassung
e) Eskalationsnotiz für überfällige Gaps erstellen
f) Alle geschlossenen Gaps archivieren
```

### 5. Tracker aktualisieren

Änderungen in der YAML-Datei speichern und Änderungszeitpunkt vermerken.

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Dieser Skill liest und schreibt ausschließlich interne Tracking-Daten; keine normspezifische Zitierung erforderlich. Gap-Inhalte enthalten Normverweise aus dem erzeugenden `luecken-aufzeiger`-Lauf.

## Ausgabeformat

- **Übersichtskarte:** Kennzahlen oben
- **Gap-Tabelle:** Sortiert nach Priorität und Frist
- **Aktionsmenü:** Konkrete nächste Schritte

## Beispiel

**Eingabe:** `/regulatorisches-recht:luecken`

**Ausgabe:**
```
Gap-Übersicht – Stand: 01.06.2025

Gesamt: 7 | 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0
Offen: 5 | In Bearbeitung: 2 | Geschlossen: 0 | Überfällig: 0

| Gap-ID      | Verlautbarung        | Anforderung         | Schwere | Frist      | Eigentümer  | Status        |
|-------------|----------------------|---------------------|---------|------------|-------------|---------------|
| GAP-2025-001| MaRisk AT 4.3.2      | Datenhaltung 10 J.  | 🔴      | 31.12.2025 | Compliance  | offen         |
| GAP-2025-002| MaRisk BTR 3.2       | ESG-Integration     | 🔴      | 31.03.2026 | Risiko      | in Bearbeitung|
| GAP-2025-003| MaRisk BTO 1.2.4     | Kreditvergabe       | 🟠      | 30.06.2026 | Kredit      | offen         |
```

## Risiken / typische Fehler

- **Veralteter Tracker:** Ohne regelmäßige `luecken-aufzeiger`-Läufe veraltet der Tracker. Hinweis anzeigen, wenn der letzte Lauf > 90 Tage zurückliegt.
- **Eigentümer nicht gesetzt:** Gaps ohne Eigentümer werden nicht umgesetzt. Unzugeordnete Gaps explizit markieren.
- **Fristüberschreitung ohne Eskalation:** Für überfällige Gaps automatisch Eskalationsnotiz-Option hervorheben.

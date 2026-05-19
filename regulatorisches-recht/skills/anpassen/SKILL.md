---
name: anpassen
description: "Praxisprofil des Plugins anpassen, ohne die Ersteinrichtung komplett zu wiederholen. Laden, wenn ein einzelner Parameter geändert werden soll."
---

# Praxisprofil anpassen

## Zweck

Dieser Skill ermöglicht die gezielte Anpassung einzelner Parameter im Praxisprofil, ohne die vollständige Ersteinrichtung zu wiederholen. Einsatz: neue Behörde hinzufügen, Materialitätsschwelle nachjustieren, Richtlinienbibliothek aktualisieren, Feed-URL korrigieren, Rollenwechsel vornehmen.

## Eingaben

- Aktives Praxisprofil (muss vorhanden sein – sonst `kaltstart-interview` ausführen)
- Konkrete Angabe, was geändert werden soll

## Ablauf

### 1. Profilzustand prüfen

Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` lesen. Falls `[PLATZHALTER]`-Marker vorhanden: zum `kaltstart-interview` umleiten.

### 2. Änderungswunsch klären

Dem Nutzer die Hauptkategorien anbieten:

```
Was soll angepasst werden?
a) Beobachtete Behörden (hinzufügen / entfernen)
b) Richtlinienbibliothek (Speicherort, neue Richtlinien, Verantwortliche)
c) Materialitätsschwelle (Stufen neu kalibrieren)
d) Feed-Konfiguration (URLs, Prüfrhythmus)
e) Gap-Response-Prozess (Triageperson, Eigentümer, Eskalationsweg)
f) Rolle (Rollenänderung des Nutzers)
g) Mandat-Workspaces (aktivieren / deaktivieren)
h) Sonstiges
```

### 3. Änderung durchführen

Nur den betroffenen Abschnitt des Praxisprofils aktualisieren. Restliche Konfiguration unberührt lassen. Änderung mit Datum versehen:

```
[Geändert am TT.MM.JJJJ: <Beschreibung der Änderung>]
```

### 4. Bestätigung

Geänderten Abschnitt dem Nutzer zur Bestätigung vorlegen, dann speichern.

### 5. Abhängige Einstellungen prüfen

- Bei Hinzufügen einer Behörde: Feed-URL und Prüfrhythmus ebenfalls erfassen.
- Bei Änderung der Materialitätsschwelle: Hinweis, dass der `aufsichts-feed-monitor` beim nächsten Lauf die neue Schwelle anwendet.
- Bei Änderung des Richtlinienspeichers: Hinweis, dass `richtlinien-vergleich` den neuen Pfad nutzt.

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Keine normativen Anforderungen an das Praxisprofil selbst. Inhaltliche Anforderungen richten sich nach dem Plugin-Zweck.

## Ausgabeformat

- Kurzbestätigung der Änderung
- Aktualisierten Abschnitt des Praxisprofils anzeigen

## Beispiel

**Eingabe:** „Bitte die BNetzA als weitere beobachtete Behörde hinzufügen. Feed: https://www.bundesnetzagentur.de/DE/Presse/RSS/rss_node.html"

**Ausgabe:**

> Praxisprofil aktualisiert:
>
> **Neu hinzugefügte Behörde:**
> | Behörde | Zuständigkeit | Beobachtungsgrund | Feed-Quelle |
> |---|---|---|---|
> | Bundesnetzagentur (BNetzA) | EnWG, TKG | Telekommunikationsregulierung | RSS: bundesnetzagentur.de/RSS |
>
> Gespeichert in `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` [Geändert am 01.06.2025]
>
> Hinweis: Der `aufsichts-feed-monitor` erfasst BNetzA-Einträge ab dem nächsten Lauf.

## Risiken / typische Fehler

- **Versehentliches Überschreiben:** Dieser Skill ändert nur den angegebenen Abschnitt. Nie das gesamte Profil überschreiben.
- **Ungültige Feed-URLs:** Feed-URL vor dem Speichern testen; defekte Feeds führen zu stillen Fehlern im `aufsichts-feed-monitor`.
- **Fehlende Neuindizierung:** Nach Änderung des Richtlinienspeichers muss die Bibliothek neu indiziert werden. Hinweis geben.

---
name: anpassen
description: Geführte Anpassung des Praxisprofils – einzelne Einstellungen ändern, ohne das gesamte Cold-Start-Interview zu wiederholen. Rolle, Praxisschwerpunkte, Risikostrategie, Kanzleistil, Vergütungsart oder Integrationen einzeln aktualisieren.
language: de
triggers:
  - "anpassen"
  - "profil ändern"
  - "einstellung ändern"
  - "schwerpunkt ändern"
  - "kanzleistil anpassen"
  - "integration einrichten"
---

# Praxisprofil anpassen

## Zweck

Gezielte Änderung einzelner Felder des Praxisprofils in CLAUDE.md, ohne den gesamten Cold-Start-Prozess zu wiederholen. Geeignet für Wechsel des Praxisschwerpunkts, Anpassung der Risikostrategie, Aktivierung neuer Integrationen oder Korrektur falscher Angaben.

## Eingaben

- Eines oder mehrere zu ändernde Felder (z. B. „Schwerpunkt auf Strafrecht hinzufügen", „Outlook MCP aktivieren")
- Optional: `--alle` – zeigt alle aktuellen Einstellungen zur Auswahl

## Ablauf

1. **Aktuelle CLAUDE.md einlesen:** Alle bestehenden Profilwerte anzeigen.
2. **Änderungswunsch präzisieren:** Falls unklar, welches Feld geändert werden soll, Auswahl anbieten.
3. **Neuen Wert erfassen:** Validierung gegen zulässige Werte (z. B. Praxisschwerpunkte-Liste).
4. **CLAUDE.md aktualisieren:** Nur das geänderte Feld überschreiben.
5. **Bestätigung:** Vorher-Nachher-Vergleich der geänderten Felder ausgeben.
6. **Integrations-Check (optional):** Bei Aktivierung einer neuen Integration automatisch `--check-integrations` ausführen.

## Quellen und Zitierweise

Keine gesonderten Normen. Allgemein: §§ 43a BRAO, 3a RVG bei rollenbezogenen Änderungen.

## Ausgabeformat

```
Änderung gespeichert:
  Feld: praxis_schwerpunkte
  Alt:  ["ZPO", "ArbGG"]
  Neu:  ["ZPO", "ArbGG", "StPO"]

CLAUDE.md aktualisiert. Alle Skills verwenden ab sofort das neue Profil.
```

## Risiken / typische Fehler

- **Rollenwechsel mit Rechtsfolgen:** Wechsel von Rechtsanwalt zu Syndikusrechtsanwalt (§ 46a BRAO) hat berufsrechtliche Konsequenzen; das Plugin dokumentiert den Wechsel, ersetzt aber keine standesrechtliche Beratung.
- **Überschreiben statt Ergänzen:** Bei Praxisschwerpunkten immer prüfen, ob bestehende Einträge erhalten bleiben sollen; Default ist Ergänzung, nicht Überschreiben.

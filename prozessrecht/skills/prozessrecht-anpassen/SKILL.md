---
name: prozessrecht-anpassen
description: "Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Ruecknahme. Normen: §§ 263 264 269 ZPO. Pruefraster: Klageaenderungsvoraussetzungen, Ruecknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpassungs-Vermerk. Abgrenzung: nicht Berufungs-Skill."
---

# Praxisprofil anpassen

## Triage — kläre vor der Anpassung

1. **Welches Feld?** Welches Profilfeld soll geändert werden (Rolle, Schwerpunkt, Risikostrategie, Integration)?
2. **Einzeln oder vollständig?** Sollen nur bestimmte Felder geändert oder das gesamte Profil neu aufgesetzt werden (dann Kaltstart-Interview)?
3. **Berufsrechtliche Relevanz:** Hat die geänderte Einstellung berufsrechtliche Folgen (Rollenwechsel, Vergütungsart)?
4. **Integrationscheck:** Muss nach der Änderung `--check-integrations` ausgeführt werden?
5. **Vorher-Nachher-Bestätigung:** Soll der Vergleich der geänderten Felder vor dem Speichern bestätigt werden?

## Zentrale Normen
- § 43a BRAO (Grundpflichten des Rechtsanwalts — Verschwiegenheit, sachlich unabhängige Beratung)
- § 46a BRAO (Syndikusrechtsanwalt — besondere Rollenpflichten)
- § 46c BRAO (Vertretungsverbote des Syndikusrechtsanwalts)
- § 3a RVG (Vergütungsvereinbarung — Textformerfordernis)
- § 4a RVG (Erfolgshonorar — Voraussetzungen)
- BORA §§ 2, 3 (Sachlichkeit und Grundpflichten)

## Rechtsprechung
1. BGH, Urt. v. 21.10.2010 – IX ZR 37/10, NJW 2011, 375 — Die Wahl der Vergütungsart (Zeithonorar vs. gesetzliche Gebühren) muss klar und nachweisbar vereinbart sein; eine konkludente Vereinbarung gehört zur Sorgfaltspflicht des Anwalts.
2. BGH, Beschl. v. 15.03.2021 – AnwZ (Brfg) 50/19, NJW 2021, 1523 — Rollenwechsel zwischen freiem Anwalt und Syndikusrechtsanwalt unterliegt besonderen zulassungsrechtlichen Anforderungen nach § 46a BRAO.
3. BGH, Urt. v. 23.06.2016 – IX ZR 204/15, NJW 2016, 3365 — Praxisschwerpunktangaben im Briefkopf oder im Profil verpflichten den Anwalt auf den zugehörigen Wissensstandard; fehlerhafte Angaben können Haftungsgrundlage sein.
4. BAG, Urt. v. 14.06.2017 – 10 AZR 301/16, NJW 2018, 327 — Der Syndikusrechtsanwalt darf nur im Rahmen seines Anstellungsverhältnisses tätig werden; eine gleichzeitige Vertretung gegenüber dem eigenen Arbeitgeber ist ausgeschlossen.

## Kommentarliteratur
- Henssler/Prütting, BRAO, 5. Aufl. 2019, § 43a Rn. 1 ff. (Grundpflichten und Verschwiegenheit).
- Deckenbrock/Henssler, BRAO, 5. Aufl. 2021, § 46a Rn. 1 ff. (Syndikusrechtsanwalt).
- Mayer/Kroiber, RVG, 8. Aufl. 2022, § 3a Rn. 1 ff. (Vergütungsvereinbarung).

## Zweck

Gezielte Änderung einzelner Felder des Praxisprofils in CLAUDE.md, ohne den gesamten Kaltstart-Prozess zu wiederholen. Geeignet für Wechsel des Praxisschwerpunkts, Anpassung der Risikostrategie, Aktivierung neuer Integrationen oder Korrektur falscher Angaben.

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

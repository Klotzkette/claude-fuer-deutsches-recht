---
name: mandat-arbeitsbereich-abschnitt
description: "Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpassungs-Vermerk. Abgrenzung: nicht Berufungs-Skill im Prozessrecht."
---

# Praxisprofil anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Eines oder mehrere zu ändernde Felder (z. B. "Schwerpunkt auf Strafrecht hinzufügen", "Outlook MCP aktivieren")
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

## Risiken / typische Fehler

- **Rollenwechsel mit Rechtsfolgen:** Wechsel von Rechtsanwalt zu Syndikusrechtsanwalt (§ 46a BRAO) hat berufsrechtliche Konsequenzen; das Plugin dokumentiert den Wechsel, ersetzt aber keine standesrechtliche Beratung.
- **Überschreiben statt Ergänzen:** Bei Praxisschwerpunkten immer prüfen, ob bestehende Einträge erhalten bleiben sollen; Default ist Ergänzung, nicht Überschreiben.


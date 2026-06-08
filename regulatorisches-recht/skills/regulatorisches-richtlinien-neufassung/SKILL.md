---
name: regulatorisches-richtlinien-neufassung
description: "Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeitetes Dokument Aenderungsprotokoll. Abgrenzung: nicht für Neuerstellung von Richtlinien (richtlinien-neufassung) im Regulatorisches Recht."
---

# Praxisprofil anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Praxisprofil (muss vorhanden sein – sonst `regulatorisches-recht-kaltstart-interview` ausführen)
- Konkrete Angabe, was geändert werden soll

## Ablauf

### 1. Profilzustand prüfen

Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` lesen. Falls `[PLATZHALTER]`-Marker vorhanden: zum `regulatorisches-recht-kaltstart-interview` umleiten.

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

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

§§ 48, 49 VwVfG (Rücknahme, Widerruf) — §§ 313, 314 BGB (Anpassung, Kuendigung bei Aenderung der Grundlage) — Art. 288 AEUV (Richtlinien-Anpassungspflicht)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Keine normativen Anforderungen an das Praxisprofil selbst. Inhaltliche Anforderungen richten sich nach dem Plugin-Zweck.

## Beispiel

**Eingabe:** "Bitte die BNetzA als weitere beobachtete Behörde hinzufügen. Feed: https://www.bundesnetzagentur.de/DE/Presse/RSS/rss_node.html"

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


---
name: luecken
description: "Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: nicht für Lueckenaufzeiger-Perspektive nach aussen (luecken-aufzeiger) im Regulatorisches Recht."
---

# Gap-Tracker

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Gap-Tracker-Datei: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`
- Optional: Filter (nach Schweregrad, Frist, Eigentümer, Status)
- Optional: Gap-ID zum gezielten Aktualisieren

## Ablauf

### 1. Tracker lesen

Gap-Tracker lesen. Falls nicht vorhanden:
```
Noch keine Gaps erfasst. Starten Sie mit /regulatorisches-recht:lücken-aufzeiger,
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

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bindung an Gesetz und Recht, Rechtsluecken-Klaerung) — §§ 133, 157 BGB (Auslegungsgrundsaetze) — § 5 EGBGB (Analogie bei Rechtsluecken im Privatrecht) — §§ 13, 31 EnWG (Luecken in Regulierungs-Normen)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Dieser Skill liest und schreibt ausschließlich interne Tracking-Daten; keine normspezifische Zitierung erforderlich. Gap-Inhalte enthalten Normverweise aus dem erzeugenden `luecken-aufzeiger`-Lauf.

## Beispiel

**Eingabe:** `/regulatorisches-recht:lücken`

**Ausgabe:**
```
Gap-Übersicht – Stand: 01.06.2025

Gesamt: 7 | 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0
Offen: 5 | In Bearbeitung: 2 | Geschlossen: 0 | Überfällig: 0

| Gap-ID | Verlautbarung | Anforderung | Schwere | Frist | Eigentümer | Status |
|-------------|----------------------|---------------------|---------|------------|-------------|---------------|
| GAP-2025-001| MaRisk AT 4.3.2 | Datenhaltung 10 J. | 🔴 | 31.12.2025 | Compliance | offen |
| GAP-2025-002| MaRisk BTR 3.2 | ESG-Integration | 🔴 | 31.03.2026 | Risiko | in Bearbeitung|
| GAP-2025-003| MaRisk BTO 1.2.4 | Kreditvergabe | 🟠 | 30.06.2026 | Kredit | offen |
```

## Risiken / typische Fehler

- **Veralteter Tracker:** Ohne regelmäßige `luecken-aufzeiger`-Läufe veraltet der Tracker. Hinweis anzeigen, wenn der letzte Lauf > 90 Tage zurückliegt.
- **Eigentümer nicht gesetzt:** Gaps ohne Eigentümer werden nicht umgesetzt. Unzugeordnete Gaps explizit markieren.
- **Fristüberschreitung ohne Eskalation:** Für überfällige Gaps automatisch Eskalationsnotiz-Option hervorheben.


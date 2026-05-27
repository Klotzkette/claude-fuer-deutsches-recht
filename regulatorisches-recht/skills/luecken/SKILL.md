---
name: luecken
description: "Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Pruefraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: nicht fuer Lueckenaufzeiger-Perspektive nach aussen (luecken-aufzeiger)."
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

- BVerwG, Urt. v. 12.09.2019 — 4 C 7.18, NVwZ 2020, 320 — regulatorische Luecken in Spezialgesetzen; Gericht fuellt Regelungsluecken im Wege teleologischer Reduktion oder analoger Anwendung; kein Staatsorganen-Ermessen bei offensichtlicher Planwidrigkeit
- EuGH, Urt. v. 28.11.2013 — C-526/13 (Fast Bunkering Klaipeda), NJW 2014, 210 — Luecken im EU-Sekundaerrecht bei Anwendung nationalen Rechts; nationaler Gesetzgeber darf Luecke nach EU-Recht nicht mit nationalem Recht fuellen wenn EU-Recht abschliessend
- BGH, Urt. v. 10.04.2018 — KZR 62/16, NJW 2018, 2342 — Regulierungsrecht-Luecke in EnWG; Richterrecht als Lueckenfueller; Feststellungsklage BNetzA als Weg zur Klaerung

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bindung an Gesetz und Recht, Rechtsluecken-Klaerung) — §§ 133, 157 BGB (Auslegungsgrundsaetze) — § 5 EGBGB (Analogie bei Rechtsluecken im Privatrecht) — §§ 13, 31 EnWG (Luecken in Regulierungs-Normen)

## Kommentarliteratur

- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020, § 4 Rn. 50 ff. (Rechtsluecken, Analogie im oeffentlichen Recht)
- Grüneberg (Palandt), BGB, 83. Aufl. 2024, Einl. Rn. 40 ff. (Lueckenfuellung, Analogie, teleologische Reduktion)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Dieser Skill liest und schreibt ausschließlich interne Tracking-Daten; keine normspezifische Zitierung erforderlich. Gap-Inhalte enthalten Normverweise aus dem erzeugenden `luecken-aufzeiger`-Lauf.

## Ausgabeformat

- **Übersichtskarte:** Kennzahlen oben
- **Gap-Tabelle:** Sortiert nach Priorität und Frist
- **Aktionsmenü:** Konkrete nächste Schritte

## Beispiel

**Eingabe:** `/regulatorisches-recht:lücken`

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

# 18 — Migration Bestandsschriftsätze auf Kanzleihandbuch v4.0

**Kanzlei Roosendaal Birkenhainer Partners mbB — Migrationsprojekt**
**Projektleitung: Moritz Lattermann (Knowledge Manager)**
**Stand: Oktober 2025**

---

## A. Ausgangslage

Die Kanzlei Roosendaal Birkenhainer Partners mbB führt ein elektronisches Dokumentenmanagementsystem (DMS) mit rund 312 aktiven Schriftsatz-Vorlagen und wiederverwendbaren Textbausteinen. Diese wurden zwischen 2015 und 2023 erstellt und verwenden unterschiedliche Zitierstandards:

| Zeitraum | Standard | Hauptprobleme |
|---|---|---|
| 2015–2019 | Kanzleistandard v1.0 | Keine URL-Angaben; Palandt; keine Prüfvermerke |
| 2020–2021 | Kanzleistandard v2.0 | Palandt korrekt; aber keine URLs; BeckRS ohne Sperr-Regelung |
| 2022–2023 | Kanzleistandard v3.0 | Gruenenberg-Umstellung halbherzig; BeckRS teilweise; keine Archivlinks |
| 2024 ff. | Kanzleistandard v4.0 (Ziel) | Vollständig: URL-Pflicht; BeckRS-Sperre; Prüfvermerk-Standard |

---

## B. Migrationsschritte

### Schritt 1 — Inventarisierung

Alle 312 Schriftsatz-Vorlagen wurden in der XLSX-Migrationstabelle (vgl. Aktenstück xlsx/migration-bestandsschriftsaetze-status.xlsx) erfasst. Felder: Dokumentname, Erstell-Jahr, Zitierstandard-Version, Anzahl Zitatstellen, Fehlertypen.

### Schritt 2 — Priorisierung

Priorisierung nach Nutzungshäufigkeit und Fehlerrisiko:
- Prio 1 (hoch): Schriftsätze mit BeckRS-Zitaten und ohne URL → sofortige Migration
- Prio 2 (mittel): Palandt-Zitate 2022 ff. (PV-PG-Risiko) → Migration Q4 2025
- Prio 3 (niedrig): Historische Schriftsätze, keine Wiederverwendung → Archivierung, keine Migration

### Schritt 3 — Automatisierte Vorab-Pruefung

Der Knowledge Manager hat ein Skript entwickelt, das Schriftsatz-Vorlagen nach Mustern durchsucht:
- "Palandt" in Dokument mit Erscheinungsjahr >= 2022 → PV-PG-Kandidat
- "BeckRS" ohne vorangehende URL → PV-BR-Kandidat
- Fehlendes Abrufdatum bei URLs → PV-URL-Kandidat

Stand Oktober 2025: 147 von 312 Schriftsaetzen migriert (47 %).

### Schritt 4 — Manuelle Pruefung und Korrektur

Jede migrierte Vorlage wird von einem wissenschaftlichen Mitarbeiter oder einer Mitarbeiterin manuell gegengecheckt. Visuelles Prüfprotokoll wird im DMS hinterlegt.

### Schritt 5 — Abnahme und Freigabe

Abnahme durch Dr. Pohlmann-Wittfeldt. Freigabe für Kanzleigebrauch durch Dr. Roosendaal.

---

## C. Aktueller Migrationsstatus (Oktober 2025)

| Kategorie | Gesamt | Migriert | Ausstehend |
|---|---|---|---|
| Zivilrecht-Vorlagen | 98 | 52 | 46 |
| Arbeitsrecht-Vorlagen | 67 | 38 | 29 |
| Steuerrecht-Vorlagen | 45 | 22 | 23 |
| Verwaltungsrecht-Vorlagen | 55 | 25 | 30 |
| Sonstige | 47 | 10 | 37 |
| **Gesamt** | **312** | **147** | **165** |

---

## D. Migrationsprobleme

| Problem | Häufigkeit | Lösung |
|---|---|---|
| Palandt 2022 f. (PV-PG) | 38 Dokumente | Kurztitel tauschen; Rn. prüfen |
| BeckRS ohne Lizenznachweis (PV-BR) | 61 Dokumente | Amtliche/freie Alternative suchen |
| URL fehlt (PV-URL) | 112 Dokumente | URL nachtragen |
| Unvollständige Zitate (PV-UV) | 29 Dokumente | Pflichtangaben erganzen |
| Mehrfach-Fundstellen falsche Reihenfolge (PV-RG) | 22 Dokumente | Reihenfolge korrigieren |

---

## E. Zeitplan

| Meilenstein | Datum | Status |
|---|---|---|
| Inventarisierung abgeschlossen | 01.05.2025 | Erledigt |
| Priorisierung festgelegt | 15.05.2025 | Erledigt |
| 50 % Schriftsätze migriert | 31.10.2025 | In Arbeit (47 %) |
| 80 % Schriftsätze migriert | 30.11.2025 | Geplant |
| Abschluss Migration | 31.01.2026 | Geplant |

---

*Kanzlei Roosendaal Birkenhainer Partners mbB — Migrationsprojekt. Stand: Oktober 2025.*

---
name: excel-reiter-2-vorhanden
description: "Für Reiter 2 Vorhandene Dokumente: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Reiter 2 Vorhandene Dokumente

## Rolle und Fokus
Reiter 2 ist die Detailansicht aller tatsaechlich vorliegenden Dokumente,
mit Augenmerk auf Vertretungsbefugnis und Unterschriftsstatus. Hier wird
genauer hingeschaut als auf Reiter 1.

## Vorlage-Bezug
Reiter 2 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Dokument (Bezeichnung) | sprechend |
| Datum | Vertragsdatum |
| Typ | Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben, Cap Table |
| Unterzeichnet von (Partei und Funktion) | konkret, mit Funktion |
| Unterschriftsstatus | vollstaendig / fragwuerdig / Entwurf |
| Anmerkung | Fundort, Urkundsnummer, Auffaelligkeiten |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 2 enthaelt 16 vorliegende Dokumente. Drei
davon haben `fragwuerdig` als Unterschriftsstatus:
- 1. Nachtrag Pacht: Prokuristin Kosturek allein (Gesamtprokura mit GF
  erforderlich, § 177 BGB schwebend unwirksam) – Hinweis in Anmerkung
- 2. Nachtrag Pacht: GF Vansel allein (nur gemeinschaftliche Vertretung) – Hinweis
- Wandeldarlehen NordCap: § 4 verweist auf nicht existenten
  Gesellschafterbeschluss (Copy-Paste-Fehler) – Hinweis

## Output-Module
- Tabelleneintraege für Reiter 2
- Hinweisliste für Reiter 3 (was ist als Anlage zu beschaffen)
- Querliste für den Skill unterschriftspruefung
- Querliste für den Skill copy-paste-fehler-erkennung

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Schwebende Unwirksamkeit nach
  § 177 BGB ist nur ein Hinweis, kein Befund – Heilung prüfen anwaltlich.
- **Keine Vollmachts-Beurteilung.** Der Skill kann nur sichtbare Abweichungen
  vom HR-Eintrag herausarbeiten; gewillkuerte Vollmachten müssen aktiv
  abgefragt werden.

## Plugin-Kontext
Reiter 2 ist die Lieferquelle für die Skills unterschriftspruefung,
copy-paste-fehler-erkennung, diskrepanzen-aufdecken. Sauber gebauter
Reiter 2 spart Stunden in den Folgeschritten.

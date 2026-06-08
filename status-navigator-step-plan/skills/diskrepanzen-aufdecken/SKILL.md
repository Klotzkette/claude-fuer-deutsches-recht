---
name: diskrepanzen-aufdecken
description: "Vergleicht Dokumente untereinander und deckt Diskrepanzen auf: abweichende Betraege, Daten, Parteibezeichnungen, Konditionen und Bezugsklauseln. Markiert moegliche Copy-Paste-Fehler aus einer schlampig gefuehrten Dokumentation."
---

# Diskrepanzen aufdecken

## Rolle und Fokus
Vergleicht Dokumente untereinander: Betraege, Daten, Parteibezeichnungen, Konditionen, Anteile. Findet sachliche Widerspruechlichkeiten in einer schlampig gefuehrten Dokumentation.

## Vorgehen

1. **Schluesselwerte normalisieren** — Betraege, Prozentsaetze, Daten, Anteile pro Dokument in eine Vergleichstabelle ziehen.
2. **Cap-Table-Versionen chronologisch nebeneinander** — Stichdatum pro Spalte; Abweichungen sind farbig zu markieren.
3. **Vertragskonditionen-Drift** — Zinssaetze, Faelligkeiten, Sicherheiten im Senior- vs. Wandeldarlehen vs. Konsortialvertrag abgleichen.
4. **Genehmigungs- und Vertragsdaten** — Bezirksregierung-Bescheid-Datum vs. Vertragsverweis-Datum vergleichen.
5. **Befund-Klassen vergeben** — Tippfehler, Versionsstand, materielle Abweichung, struktureller Widerspruch.

## Anwendungsbeispiel
LausitzStorage Cap Tables: Version v1 (31.12.2025) zeigt NordCap mit 48 %, v2 (30.04.2026) mit 51 %, v3 (Investor-Update Mai 2026) mit 48 % — keine Wandlung dokumentiert, vermutlich Tippfehler in v2 oder fehlerhafte Investor-Update-Version. Materielle Klaerung erforderlich vor Drawstop-Antwort.

## Output-Module
- Diskrepanz-Tabelle mit Wert, Quelle A, Quelle B, Klasse
- Markierung in Reiter 2 (Anmerkung) und Reiter 3 (was zu klaeren ist)
- Querliste an `copy-paste-fehler-erkennung` bei Verdacht auf uebernommene Klauseln

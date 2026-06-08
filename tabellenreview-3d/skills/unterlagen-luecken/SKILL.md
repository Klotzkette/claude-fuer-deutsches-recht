---
name: unterlagen-luecken
description: "Lücken- und Beschaffungsliste für Tabellenreview (Excel/CSV): trennt fehlende Tatsachen von fehlenden Belegen (Excel-/CSV-Datei, Formelreview, Datenqualitätsbericht), nennt pro Lücke Beweisthema, Beschaffungsweg (Finanzamt), Frist und Ersatznachweis."
---

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Tabellenreview 3d** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.


## Fachlandkarte dieses Plugins

- `aggregation-spaltenprompts-definieren` — Aggregation Spaltenprompts Definieren
- `arbeitsblatt-perspektiven-definieren` — Arbeitsblatt Perspektiven Definieren
- `arbeitsblatt-schriftsatz-brief-memo-bausteine` — Arbeitsblatt Schriftsatz Brief Memo Bausteine
- `arbeitsblatt-schriftsatz-brief-und-memo-bausteine` — Arbeitsblatt Schriftsatz Brief und Memo Bausteine
- `audit-trail-protokoll` — Audit Trail Protokoll
- `belegkette-rueckverfolgung` — Belegkette Rueckverfolgung
- `belegkette-rueckverfolgung-caching-rerun` — Belegkette Rueckverfolgung Caching Rerun
- `caching-und-teil-rerun` — Caching und Teil Rerun
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `datenpunkt-dokument-excel-beweislast` — Datenpunkt Dokument Excel Beweislast
- `datenpunkt-dokumentenmatrix-lueckenliste` — Datenpunkt Dokumentenmatrix Lueckenliste
- `dokument-behoerden-gericht-und-registerweg` — Dokument Behoerden Gericht und Registerweg
- `dokumentstapel-aufnehmen` — Dokumentstapel Aufnehmen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Tabellenreview 3D-Frage zwingend (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Output

Priorisierte Lückenliste mit Frist, Beweiszweck, Beschaffungsweg, Ersatznachweis und Verantwortlichem; im Mandat Tabellenreview (Excel/CSV) typischerweise Excel-/CSV-Datei, Formelreview zuerst.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

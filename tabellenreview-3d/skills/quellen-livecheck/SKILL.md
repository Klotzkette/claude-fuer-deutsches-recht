---
name: quellen-livecheck
description: "Quellen-Live-Check für Tabellenreview (Excel/CSV): prüft Normen (GoBD, Tax compliance) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Finanzamt und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Tabellenreview 3d** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


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

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Tabellenreview 3D (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

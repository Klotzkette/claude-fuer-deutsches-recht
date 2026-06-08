---
name: quellen-livecheck
description: "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Tabellenreview 3d** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `aggregation-spaltenprompts-definieren-arbeitsblatt` — Aggregation Spaltenprompts Definieren Arbeitsblatt
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `arbeitsblatt-perspektiven-definieren` — Arbeitsblatt Perspektiven Definieren
- `audit-trail-protokoll` — Audit Trail Protokoll
- `belegkette-rueckverfolgung` — Belegkette Rueckverfolgung
- `belegkette-rueckverfolgung-caching-rerun-dokumentstapel` — Belegkette Rueckverfolgung Caching Rerun Dokumentstapel
- `caching-und-teil-rerun` — Caching Und Teil Rerun
- `datenpunkt-dokument-excel-beweislast` — Datenpunkt Dokument Excel Beweislast
- `dokumentstapel-aufnehmen` — Dokumentstapel Aufnehmen
- `excel-multi-kreuzblatt-konsistenzpruefung-pdf-bericht` — Excel Multi Kreuzblatt Konsistenzpruefung Pdf Bericht
- `excel-multi-sheet-export` — Excel Multi Sheet Export
- `gestapelt-immobilien-massenpruefung-interessen` — Gestapelt Immobilien Massenpruefung Interessen
- `kreuzblatt-konsistenzpruefung` — Kreuzblatt Konsistenzpruefung
- `mehrblatt-sonderfall-onboarding-perspektiven` — Mehrblatt Sonderfall Onboarding Perspektiven

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

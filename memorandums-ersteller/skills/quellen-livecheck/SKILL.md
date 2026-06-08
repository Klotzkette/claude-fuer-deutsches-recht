---
name: quellen-livecheck
description: "Quellen-Live-Check für Memorandum-Ersteller: prüft Normen (Anwendungsbereich nach Mandat) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Memorandums Ersteller** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `antworten-interessen-ausfuehrungen-fragen` — Antworten Interessen Ausfuehrungen Fragen
- `ausfuehrungen-formular-portal-und-einreichung` — Ausfuehrungen Formular Portal und Einreichung
- `due-diligence-ergebnis-handlungsempfehlung` — DUE Diligence Ergebnis Handlungsempfehlung
- `fragen-compliance-dokumentation-und-akte` — Fragen Compliance Dokumentation und Akte
- `gliederung-mandantenunterlagen-memorandum` — Gliederung Mandantenunterlagen Memorandum
- `haftungsrisiko-rechtsanwalt-board-pack` — Haftungsrisiko Rechtsanwalt Board Pack
- `juristisches-questions-fristennotiz` — Juristisches Questions Fristennotiz
- `laenge-formate-mandantenfreundliche-fassung` — Laenge Formate Mandantenfreundliche Fassung
- `mandantenanfrage-schnell` — Mandantenanfrage Schnell
- `mandantenkommunikation-redteam` — Mandantenkommunikation Redteam
- `mandantenunterlagen-tatbestand-beweis-und-belege` — Mandantenunterlagen Tatbestand Beweis und Belege
- `memo-board-pack-besondere-anlaesse-spezial` — Memo Board Pack Besondere Anlaesse Spezial
- `memo-compliance-vorfall-intern` — Memo Compliance Vorfall Intern
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Memorandums Ersteller (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

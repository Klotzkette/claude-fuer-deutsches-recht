---
name: quellen-livecheck
description: "Quellen-Live-Check für Vertragsausfüller: prüft Normen (BGB AT, BGB BT, AGB-Recht §§ 305 ff. BGB) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Vertragsausfueller** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `altvertraege-dokumentenmatrix-und-lueckenliste` — Altvertraege Dokumentenmatrix und Lueckenliste
- `altvertrag-nachziehen` — Altvertrag Nachziehen
- `ausdruecklicher-fristennotiz-und-naechster-schritt` — Ausdruecklicher Fristennotiz und Naechster Schritt
- `batch-modus-docx-stripper-einfuehrung` — Batch Modus Docx Stripper Einfuehrung
- `bsag-mietvertrag-klauselentscheidung` — Bsag Mietvertrag Klauselentscheidung
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `clean-output` — Clean Output
- `docx-stripper` — Docx Stripper
- `docx-tatbestand-beweis-und-belege` — Docx Tatbestand Beweis und Belege
- `einfuehrung-prozess` — Einfuehrung Prozess
- `erkennen-schriftsatz-brief-und-memo-bausteine` — Erkennen Schriftsatz Brief und Memo Bausteine
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen RED Fassungen Sonderfall Felder
- `fassungen-sonderfall-und-edge-case` — Fassungen Sonderfall und Edge Case
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (BGB §§ 133, 157, 305–310, 311b, 311c, 433, 488, 535, 631, 651a, 765, AGB-Recht, NachwG, FormularG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Vertragsausfüller (Lückenschluss in Verträgen) (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

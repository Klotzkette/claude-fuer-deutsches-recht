---
name: quellen-livecheck
description: "Quellen-Live-Check für Jura-Hausarbeiten: prüft Normen (BGB AT/BT, StGB AT/BT, GG, ZPO/StPO/VwGO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Universitäre Prüfungsämter und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Hausarbeitenmacher** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `adressaten-formular-portal-und-einreichung` — Adressaten Formular Portal und Einreichung
- `aufgabenstellung-erfassen-fachgebiet` — Aufgabenstellung Erfassen Fachgebiet
- `ausfluegen-didaktisches-durch` — Ausfluegen Didaktisches Durch
- `bearbeitungsplan-erstellen` — Bearbeitungsplan Erstellen
- `behutsame-frech-haeufige-fehler` — Behutsame Frech Haeufige Fehler
- `didaktisches-erstpruefung-und-mandatsziel` — Didaktisches Erstpruefung und Mandatsziel
- `durch-schriftsatz-brief-und-memo-bausteine` — Durch Schriftsatz Brief und Memo Bausteine
- `europarecht-anwendbarkeit-hausarbeiten` — Europarecht Anwendbarkeit Hausarbeiten
- `europarecht-interessen-fertigen-sonderfall` — Europarecht Interessen Fertigen Sonderfall
- `fachgebiet-routing-zivil-oeffentlich-straf` — Fachgebiet Routing Zivil Oeffentlich Straf
- `fertigen-sonderfall-und-edge-case` — Fertigen Sonderfall und Edge Case
- `fuehrt-risikoampel-und-gegenargumente` — Fuehrt Risikoampel und Gegenargumente
- `gliederung-mit-tiefenstruktur` — Gliederung mit Tiefenstruktur
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Hausarbeitenmacher (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

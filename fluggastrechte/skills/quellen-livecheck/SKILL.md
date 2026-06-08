---
name: quellen-livecheck
description: "Quellen-Live-Check für Fluggastrechte VO 261/2004: prüft Normen (VO (EG) 261/2004, Montrealer Übereinkommen, BGB §§ 631 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt LBA und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fluggastrechte** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung AN Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet und Vollstreckung
- `airline-standardausreden-annullierung` — Airline Standardausreden Annullierung
- `airline-standardausreden-pruefen` — Airline Standardausreden Pruefen
- `anlagen-bauen` — Anlagen Bauen
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `annullierung-schriftsatz-brief-memo-bausteine` — Annullierung Schriftsatz Brief Memo Bausteine
- `annullierung-schriftsatz-brief-und-memo-bausteine` — Annullierung Schriftsatz Brief und Memo Bausteine
- `anschluss-router` — Anschluss Router
- `anschlussflug-und-reiseplan` — Anschlussflug und Reiseplan
- `ausgleich-internationaler-bezug-schnittstellen` — Ausgleich Internationaler Bezug Schnittstellen
- `ausgleich-internationaler-bezug-und-schnittstellen` — Ausgleich Internationaler Bezug und Schnittstellen
- `ausnahmen-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Umstaende
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fluggastrechte (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.


## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

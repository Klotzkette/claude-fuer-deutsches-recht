---
name: quellen-livecheck
description: "Quellen-Live-Check für Urteilsbauer/Relationsmacher: prüft Normen (ZPO § 313 Urteilsaufbau, Relationstechnik) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Urteilsbauer Relationsmacher** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `aktenintake-schriftsatz-brief-und-memo-bausteine` — Aktenintake Schriftsatz Brief und Memo Bausteine
- `aktenintake-zivil` — Aktenintake Zivil
- `amts-aktenintake-zivil-anspruchsgrundlagen` — Amts Aktenintake Zivil Anspruchsgrundlagen
- `amts-fristen-form-zustaendigkeit` — Amts Fristen Form Zustaendigkeit
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen Pruefen
- `berufungsfest-beschluss-bauen-beweisbeschluss` — Berufungsfest Beschluss Bauen Beweisbeschluss
- `berufungsfest-pruefen` — Berufungsfest Pruefen
- `beschluss-bauen-zpo` — Beschluss Bauen ZPO
- `beschluss-tatbestand-beweis-und-belege` — Beschluss Tatbestand Beweis und Belege
- `beschluss-tatbestandsmerkmale` — Beschluss Tatbestandsmerkmale
- `beweisbeschluss-vorbereiten` — Beweisbeschluss Vorbereiten
- `beweiswuerdigung-mit-richter-input` — Beweiswuerdigung mit Richter Input
- `beweiswuerdigung-quellenkarte` — Beweiswuerdigung Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (ZPO) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Urteilsbauer Relationsmacher (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

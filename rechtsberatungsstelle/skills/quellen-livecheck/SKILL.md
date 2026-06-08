---
name: quellen-livecheck
description: "Quellen-Live-Check für Rechtsberatungsstelle (RDG): prüft Normen (RDG, BeratungshilfeG, Prozesskostenhilfe ZPO §§ 114 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Rechtsberatungsstelle** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anlaufstellen-beweislast-anleiter-bono` — Anlaufstellen Beweislast Anleiter Bono
- `anleiter-formular-portal-und-einreichung` — Anleiter Formular Portal und Einreichung
- `anleiter-pruefwarteschlange` — Anleiter Pruefwarteschlange
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bono-erstpruefung-und-mandatsziel` — Bono Erstpruefung und Mandatsziel
- `briefe-erstberatung-rdg-konform` — Briefe Erstberatung RDG Konform
- `einarbeitung` — Einarbeitung
- `einfache-sprache-briefe` — Einfache Sprache Briefe
- `entwurf-einarbeitung-einfache-sprache` — Entwurf Einarbeitung Einfache Sprache
- `erstberatung-rdg-grenzen-und-triage` — Erstberatung RDG Grenzen und Triage
- `erzeugung-leitfaden-erstellen-mandanten` — Erzeugung Leitfaden Erstellen Mandanten
- `fristen-fristenkontrolle-rdg` — Fristen Fristenkontrolle RDG
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (RDG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Rechtsberatungsstelle (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

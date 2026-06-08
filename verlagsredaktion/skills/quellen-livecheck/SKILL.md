---
name: quellen-livecheck
description: "Quellen-Live-Check für Verlagsredaktion: prüft Normen (UrhG, VerlagsG, Presserechte Länder) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Presserat und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Verlagsredaktion** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abstimmung` — Abstimmung
- `abstimmung-lektorat-produktion-satz` — Abstimmung Lektorat Produktion Satz
- `abstimmung-mit-autor-feedback-kanal` — Abstimmung mit Autor Feedback Kanal
- `abstimmung-mit-produktion-satz-druck` — Abstimmung mit Produktion Satz Druck
- `abstimmung-mit-rechtsabteilung-pruefung` — Abstimmung mit Rechtsabteilung Pruefung
- `abstimmung-mit-vertrieb-marketing` — Abstimmung mit Vertrieb Marketing
- `ai-einsatz-transparenz-datenschutz` — AI Einsatz Transparenz Datenschutz
- `audio-transkript-zu-fachbeitrag` — Audio Transkript zu Fachbeitrag
- `aussagensicherheit-buchprojekt-bauleiter` — Aussagensicherheit Buchprojekt Bauleiter
- `autorenkommunikation-compliance-dokumentation-und-akte` — Autorenkommunikation Compliance Dokumentation und Akte
- `autorenkommunikation-email` — Autorenkommunikation Email
- `barrierefreiheit-epub-pdf` — Barrierefreiheit Epub PDF
- `bildrechte-grafiken-tabellen` — Bildrechte Grafiken Tabellen
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Verlagsredaktion (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---
name: quellen-livecheck
description: "Quellen-Live-Check für Schriftform/Textform BGB: prüft Normen (§§ 126/126a, 126b BGB, § 127 BGB, § 130 BGB Zugang) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Schriftform Und Textform Bgb** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `amtlicher-formkern-bgb-zpo-check` — Amtlicher Formkern BGB ZPO Check
- `anspruchsformulierungen-formverstoss` — Anspruchsformulierungen Formverstoss
- `arbeitsrecht-befristung-schriftform-checker` — Arbeitsrecht Befristung Schriftform Checker
- `befristungsabrede-qes-rechtsprechung` — Befristungsabrede QES Rechtsprechung
- `befristungsabrede-qes-rechtsprechung-stand-2026` — Befristungsabrede QES Rechtsprechung Stand 2026
- `bgb-mehrparteien-konflikt-und-interessen` — BGB Mehrparteien Konflikt und Interessen
- `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` — Buergschaft Verbraucherdarlehen und Andere Strenge Formen
- `checklisten-schriftsatz-brief-und-memo-bausteine` — Checklisten Schriftsatz Brief und Memo Bausteine
- `dokumentations-und-beweisarchitektur` — Dokumentations und Beweisarchitektur
- `elektronische-paragraph-formerfordernisse` — Elektronische Paragraph Formerfordernisse
- `empfangsbeduerftiger-international` — Empfangsbeduerftiger International
- `empfangsbeduerftiger-international-schnittstellen` — Empfangsbeduerftiger International Schnittstellen
- `form-checker-fuer-vertrag-oder-willenserklaerung` — Form Checker Fuer Vertrag Oder Willenserklaerung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Schriftform Und Textform Bgb (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

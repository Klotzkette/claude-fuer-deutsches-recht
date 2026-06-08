---
name: quellen-livecheck
description: "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Vertragsausfueller** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen Red Fassungen Sonderfall Felder
- `fuehren-interessen-mappen-nachfrage` — Fuehren Interessen Mappen Nachfrage
- `term-track-vertraege` — Term Track Vertraege
- `vaf-batch-vaf-docx-vaf-einfuehrung` — Vaf Batch Vaf Docx Vaf Einfuehrung
- `vaf-bsag-vaf-klauselentscheidung-vaf-konzern` — Vaf Bsag Vaf Klauselentscheidung Vaf Konzern
- `vaf-clean-output` — Vaf Clean Output
- `vaf-feldinventar-vaf-fragebogen-vaf-fremdsprachige` — Vaf Feldinventar Vaf Fragebogen Vaf Fremdsprachige
- `vaf-plausibilitaetscheck-vaf-termsheet-altvertraege` — Vaf Plausibilitaetscheck Vaf Termsheet Altvertraege
- `vaf-quality-vaf-redline-vaf-rueckfrageninterview` — Vaf Quality Vaf Redline Vaf Rueckfrageninterview
- `vaf-template-vaf-template-vaf-track` — Vaf Template Vaf Template Vaf Track
- `vaf-vaf-mehrsprachige-vaf-platzhalterlogik` — Vaf Vaf Mehrsprachige Vaf Platzhalterlogik
- `vaf-versionierung` — Vaf Versionierung

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

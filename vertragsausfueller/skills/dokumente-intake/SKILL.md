---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Vertragsausfueller** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

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

- Eingangsdokumente nach Typ ordnen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Vertragsausfüller (Lückenschluss in Verträgen)-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB §§ 133, 157, 305–310, 311b, 311c, 433, 488, 535, 631, 651a, 765, AGB-Recht, NachwG, FormularG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Vertragsparteien.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

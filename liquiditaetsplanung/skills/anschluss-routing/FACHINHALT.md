---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Liquiditätsplanung — Power."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Liquiditaetsplanung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ampel-zahlen-schwellenwerte-berechnung` — Ampel Zahlen Schwellenwerte Berechnung
- `ausgabengruppen-fristennotiz-naechster` — Ausgabengruppen Fristennotiz Naechster
- `ausgabengruppen-systematik` — Ausgabengruppen Systematik
- `bei-drohender-zahlungsunfaehigkeit` — bei Drohender Zahlungsunfaehigkeit
- `bei-eingetretener-zahlungsunfaehigkeit` — bei Eingetretener Zahlungsunfaehigkeit
- `cash-pooling-konzern` — Cash Pooling Konzern
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `deutschem-dokumentationspaket-excel` — Deutschem Dokumentationspaket Excel
- `deutschem-tatbestandsmerkmale-beweisfragen` — Deutschem Tatbestandsmerkmale Beweisfragen
- `dokumentationspaket-bank` — Dokumentationspaket Bank
- `drohender-zahlungsunfaehigkeit` — Drohender Zahlungsunfaehigkeit
- `eingangsdaten-checkliste` — Eingangsdaten Checkliste
- `eingangsdaten-idw-s6-liqp` — Eingangsdaten IDW S6 Liqp
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Liquiditätsplanung und Insolvenzrecht-Schnittstelle-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (Paragraf 15a InsO: unverzüglich, höchstens 3 Wochen bei Zahlungsunfähigkeit und 6 Wochen bei Überschuldung; IDW S 11: Prognosezeitraum; Drei-Wochen-Liquiditätsstockungs-Test nach BGH, Urteil vom 24.05.2005 - IX ZR 123/04), notwendige Dokumente (Liquiditätsstatus, Finanzplan, Liquiditätsvorschau 3 Wochen / 3–6–12 Monate, Fortbestehensprognose, Sanierungsgutachten IDW S 6), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Bank, IV/Restrukturierungsbeauftragter oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Liquiditaetsplanung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `deutschem-dokumentationspaket-excel` — Deutschem Dokumentationspaket Excel
- `export-forecast-fortbestehensprognose-international` — Export Forecast Fortbestehensprognose International
- `idw-s6-integrierte-sanierungsplanung` — Idw S6 Integrierte Sanierungsplanung
- `insolvenzrecht-liqui-sonderfall-liquiditaetsplanung` — Insolvenzrecht Liqui Sonderfall Liquiditaetsplanung
- `interessen-verifikation-beweislast-vorschau` — Interessen Verifikation Beweislast Vorschau
- `liqp-bankenreporting-leitfaden` — Liqp Bankenreporting Leitfaden
- `liqp-liquiditaetspool-cash-pooling-spezial` — Liqp Liquiditaetspool Cash Pooling Spezial
- `liqp-liquiditaetspool-cash-rollende-13wochen-warenkredit-skonto` — Liqp Liquiditaetspool Cash Rollende 13wochen Warenkredit Skonto
- `liqp-rollende-13wochen-bauleiter` — Liqp Rollende 13wochen Bauleiter
- `liqp-warenkredit-skonto-szenarien-spezial` — Liqp Warenkredit Skonto Szenarien Spezial
- `liqui-ausgabengruppen-systematik` — Liqui Ausgabengruppen Systematik
- `liqui-bei-drohender-zahlungsunfaehigkeit` — Liqui Bei Drohender Zahlungsunfaehigkeit
- `liqui-bei-eingetretener-zahlungsunfaehigkeit` — Liqui Bei Eingetretener Zahlungsunfaehigkeit

## Arbeitsweg

- Ergebnis sichten: Welche Liquiditätsplanung und Insolvenzrecht-Schnittstelle-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 15a InsO 3 Wochen (ZU) / 6 Wochen (Überschuldung), IDW S 11 12-Monats-Prognose, Drei-Wochen-Liquiditätsstockungs-Test (BGH II ZR 296/05)), notwendige Dokumente (Liquiditätsstatus, Finanzplan, Liquiditätsvorschau 3 Wochen / 3–6–12 Monate, Fortbestehensprognose, Sanierungsgutachten IDW S 6), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Bank, IV/Restrukturierungsbeauftragter oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Liquiditätsplanung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 266a StGB
- § 102 StaRUG
- § 1 StaRUG
- § 64 GmbHG
- § 8b KStG
- § 30 GmbHG
- § 31 StaRUG
- § 49 StaRUG
- § 43 GmbHG
- § 29 StaRUG
- § 29 VwVfG

### Leitentscheidungen

- BGH II ZR 296/05
- BGH IX ZR 129/22
- BGH II ZR 78/06
- BGH IX ZR 122/23
- BGH II ZR 206/22


---
name: liquiditaetsvorschau-insolvenzrechtlich
description: Routing-Skill für eine insolvenzrechtlich belastbare Liquiditätsbilanz und Fortbestehensprognose. Nutzt den fachlichen Quell-Skill aus insolvenzrecht und verweist bei Steuerberater-Hinweispflichten auf steuerberater-werkzeuge.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - insolvenzrechtliche Liquiditätsbilanz
  - Zahlungsunfähigkeit § 17 InsO belegen
  - Fortbestehensprognose § 19 InsO
  - Antragspflicht § 15a InsO
  - gerichtsfeste Liquiditätsvorschau
  - Gläubigerantrag Liquidität
---

# /liquiditaetsplanung:liquiditaetsvorschau-insolvenzrechtlich

Dieser Skill ist ein Routing-Einstieg für das Bündel-Plugin Liquiditätsplanung (`liquiditaetsplanung`).
Die fachliche Arbeitsanweisung liegt im Quell-Skill
`/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich`.

## Ablauf

1. Wenn das Dependency-Plugin `insolvenzrecht` verfügbar ist, nutze den Skill
   `/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich`.
2. Erstelle eine insolvenzrechtlich nachvollziehbare Liquiditätsbilanz mit
   fälligen Verbindlichkeiten, verfügbaren Mitteln, Stundungen,
   Kreditlinien, Zahlungsstockung/Zahlungsunfähigkeit und Prognosehorizont.
3. Bei Steuerberater- oder Beraterkonstellationen zusätzlich
   `/steuerberater-werkzeuge:bwa-sus-bilanz-pruefung` für § 102 StaRUG
   berücksichtigen.
4. Wenn die Dependency-Skills nicht installiert sind, dem Nutzer die fehlenden
   Plugins nennen und keine ersatzweise Kurzprüfung erfinden.

## Quellenpflicht

Alle rechtlichen Aussagen sind nach `references/zitierweise.md` zu belegen.
Mindestanker: §§ 17, 18, 19 InsO, § 15a InsO, BGHZ 163, 134 und BGHZ 195, 42.

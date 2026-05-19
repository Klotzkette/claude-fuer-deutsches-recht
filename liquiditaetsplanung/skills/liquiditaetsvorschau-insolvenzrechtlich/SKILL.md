---
name: liquiditaetsvorschau-insolvenzrechtlich
description: Routing-Skill fuer eine insolvenzrechtlich belastbare Liquiditaetsbilanz und Fortbestehensprognose. Nutzt den fachlichen Quell-Skill aus insolvenzrecht und verweist bei Steuerberater-Hinweispflichten auf steuerberater-werkzeuge.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - insolvenzrechtliche Liquiditaetsbilanz
  - Zahlungsunfaehigkeit § 17 InsO belegen
  - Fortbestehensprognose § 19 InsO
  - Antragspflicht § 15a InsO
  - gerichtsfeste Liquiditaetsvorschau
  - Glaubigerantrag Liquiditaet
---

# /liquiditaetsplanung:liquiditaetsvorschau-insolvenzrechtlich

Dieser Skill ist ein Routing-Einstieg fuer das Buendel-Plugin `liquiditaetsplanung`.
Die fachliche Arbeitsanweisung liegt im Quell-Skill
`/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich`.

## Ablauf

1. Wenn das Dependency-Plugin `insolvenzrecht` verfuegbar ist, nutze den Skill
   `/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich`.
2. Erstelle eine insolvenzrechtlich nachvollziehbare Liquiditaetsbilanz mit
   faelligen Verbindlichkeiten, verfuegbaren Mitteln, Stundungen,
   Kreditlinien, Zahlungsstockung/Zahlungsunfaehigkeit und Prognosehorizont.
3. Bei Steuerberater- oder Beraterkonstellationen zusätzlich
   `/steuerberater-werkzeuge:bwa-sus-bilanz-pruefung` fuer § 102 StaRUG
   beruecksichtigen.
4. Wenn die Dependency-Skills nicht installiert sind, dem Nutzer die fehlenden
   Plugins nennen und keine ersatzweise Kurzpruefung erfinden.

## Quellenpflicht

Alle rechtlichen Aussagen sind nach `references/zitierweise.md` zu belegen.
Mindestanker: §§ 17, 18, 19 InsO, § 15a InsO, BGHZ 163, 134 und BGHZ 195, 42.

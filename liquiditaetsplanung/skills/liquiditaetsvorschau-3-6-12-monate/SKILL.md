---
name: liquiditaetsvorschau-3-6-12-monate
description: Routing-Skill für rollierende 13/26/52-Wochen-Liquiditätsplanung mit IDW-S-6/S-11-Bezug und Excel-Ausgabe. Nutzt den fachlichen Quell-Skill aus steuerberater-werkzeuge.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - 13-Wochen-Forecast
  - 26-Wochen-Liquiditätsplanung
  - 52-Wochen-Liquiditätsvorschau
  - IDW S 6 Fortführungsprognose
  - integrierte Liquiditätsplanung
  - Sanierungskonzept Bankgespräch
---

# /liquiditaetsplanung:liquiditaetsvorschau-3-6-12-monate

Dieser Skill ist ein Routing-Einstieg für das Bündel-Plugin Liquiditätsplanung (`liquiditaetsplanung`).
Die fachliche Arbeitsanweisung liegt im Quell-Skill
`/steuerberater-werkzeuge:liquiditaetsvorschau-3-6-12-monate`.

## Ablauf

1. Wenn das Dependency-Plugin `steuerberater-werkzeuge` verfügbar ist, nutze
   den Skill `/steuerberater-werkzeuge:liquiditaetsvorschau-3-6-12-monate`.
2. Baue die rollierende Planung für 13, 26 und 52 Wochen mit Annahmenblatt,
   Szenarien, Ampel und Fortführungsprognose.
3. Wenn sich ein insolvenzrechtlicher Befund verdichtet, ziehe
   `/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich` hinzu.
4. Wenn die Dependency-Skills nicht installiert sind, dem Nutzer die fehlenden
   Plugins nennen und keine ersatzweise Excel- oder Rechtsprüfung erfinden.

## Quellenpflicht

Alle rechtlichen Aussagen sind nach `references/zitierweise.md` zu belegen.
Mindestanker: §§ 17, 18, 19 InsO, § 15a InsO, § 1 StaRUG, § 102 StaRUG,
IDW S 6 und IDW S 11.

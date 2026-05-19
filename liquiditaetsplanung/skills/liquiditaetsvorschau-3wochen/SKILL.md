---
name: liquiditaetsvorschau-3wochen
description: Routing-Skill für den kurzfristigen 3-Wochen-Liquiditätstest nach § 17 InsO. Nutzt den fachlichen Quell-Skill aus steuerberater-werkzeuge und eskaliert bei roter Ampel in die insolvenzrechtliche Antragspflichtprüfung.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Liquiditätsvorschau 3 Wochen
  - 3-Wochen-Test § 17 InsO
  - Zahlungsunfähigkeit kurzfristig prüfen
  - Ampel für Geschäftsführerrunde
  - Sozialversicherung oder Finanzamt Rückstand Liquidität
---

# /liquiditaetsplanung:liquiditaetsvorschau-3wochen

Dieser Skill ist ein Routing-Einstieg für das Bündel-Plugin Liquiditätsplanung (`liquiditaetsplanung`).
Die fachliche Arbeitsanweisung liegt im Quell-Skill
`/steuerberater-werkzeuge:liquiditaetsvorschau-3wochen`.

## Ablauf

1. Wenn das Dependency-Plugin `steuerberater-werkzeuge` verfügbar ist, nutze
   den Skill `/steuerberater-werkzeuge:liquiditaetsvorschau-3wochen`.
2. Erstelle eine 3-Wochen-Liquiditätsvorschau mit Anfangsbestand,
   fälligen Verbindlichkeiten, erwarteten Einzahlungen, ungedeckter Lücke,
   Lückenquote und Ampel.
3. Bei roter Ampel oder nicht binnen drei Wochen schließbarer Lücke: auf
   `/insolvenzrecht:zahlungsunfaehigkeit-pruefung-17-inso` und
   `/insolvenzrecht:antragspflicht-15a-inso` eskalieren.
4. Wenn die Dependency-Skills nicht installiert sind, dem Nutzer die fehlenden
   Plugins nennen und keine ersatzweise Kurzprüfung erfinden.

## Quellenpflicht

Alle rechtlichen Aussagen sind nach `references/zitierweise.md` zu belegen.
Mindestanker: § 17 InsO, BGH, Urt. v. 24.05.2005 - IX ZR 123/04,
BGHZ 163, 134, sowie § 15a InsO bei Eskalation.

---
name: liquiditaetsvorschau-3wochen
description: Routing-Skill fuer den kurzfristigen 3-Wochen-Liquiditaetstest nach § 17 InsO. Nutzt den fachlichen Quell-Skill aus steuerberater-werkzeuge und eskaliert bei roter Ampel in die insolvenzrechtliche Antragspflichtspruefung.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Liquiditaetsvorschau 3 Wochen
  - 3-Wochen-Test § 17 InsO
  - Zahlungsunfaehigkeit kurzfristig pruefen
  - Ampel fuer Geschaeftsfuehrerrunde
  - Sozialversicherung oder Finanzamt Rueckstand Liquiditaet
---

# /liquiditaetsplanung:liquiditaetsvorschau-3wochen

Dieser Skill ist ein Routing-Einstieg fuer das Buendel-Plugin `liquiditaetsplanung`.
Die fachliche Arbeitsanweisung liegt im Quell-Skill
`/steuerberater-werkzeuge:liquiditaetsvorschau-3wochen`.

## Ablauf

1. Wenn das Dependency-Plugin `steuerberater-werkzeuge` verfuegbar ist, nutze
   den Skill `/steuerberater-werkzeuge:liquiditaetsvorschau-3wochen`.
2. Erstelle eine 3-Wochen-Liquiditaetsvorschau mit Anfangsbestand,
   faelligen Verbindlichkeiten, erwarteten Einzahlungen, ungedeckter Luecke,
   Lueckenquote und Ampel.
3. Bei roter Ampel oder nicht binnen drei Wochen schliessbarer Luecke: auf
   `/insolvenzrecht:zahlungsunfaehigkeit-pruefung-17-inso` und
   `/insolvenzrecht:antragspflicht-15a-inso` eskalieren.
4. Wenn die Dependency-Skills nicht installiert sind, dem Nutzer die fehlenden
   Plugins nennen und keine ersatzweise Kurzpruefung erfinden.

## Quellenpflicht

Alle rechtlichen Aussagen sind nach `references/zitierweise.md` zu belegen.
Mindestanker: § 17 InsO, BGH, Urt. v. 24.05.2005 - IX ZR 123/04,
BGHZ 163, 134, sowie § 15a InsO bei Eskalation.

---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Strafrecht: sortiert Anklageschrift, Strafbefehl, Ermittlungsakte, prüft Datum, Absender, Frist und Beweiswert (Vernehmungsprotokolle, Spurenakte); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Strafrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `adhaesionsverfahren-ermittlungsverfahren` — Adhaesionsverfahren Ermittlungsverfahren
- `aussagepsychologie-staatsanwaltschaft` — Aussagepsychologie Staatsanwaltschaft
- `chatcontrol-csam-einlassung-vorbereiten` — Chatcontrol Csam Einlassung Vorbereiten
- `ergaenzt-fachanwalt-insolvenzantrag-red-team-korrektur` — Ergaenzt Fachanwalt Insolvenzantrag RED Team Korrektur
- `fa-strafrecht-quellen-frist-next` — FA Strafrecht Quellen Frist Next
- `freiheitsstrafe-paragraf-57-stgb` — Freiheitsstrafe Paragraf 57 STGB
- `hauptverhandlung-quellenkarte` — Hauptverhandlung Quellenkarte
- `koerperverletzung-stgb-todesfolge` — Koerperverletzung STGB Todesfolge
- `mandat-triage-plaedoyer-vorbereitung` — Mandat Triage Plaedoyer Vorbereitung
- `nebenklage-nebenstrafrecht-opfervertretung` — Nebenklage Nebenstrafrecht Opfervertretung
- `notwehr-paragraf-32-stgb` — Notwehr Paragraf 32 STGB
- `orientierung` — Orientierung
- `raub-rechtsbeugung` — Raub Rechtsbeugung
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Haftbefehl, Anklageschrift, Eröffnungsbeschluss, Protokoll der Hauptverhandlung, Urteil, Revisionsantrag, Beweisantrag, Haftbeschwerde, Akteneinsicht-Akte.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Strafrecht und Strafprozessrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 53, 53a, 100a, 100b, 102, 105, 112, 116, 136, 137, 140, 141, 147, 152, 153, 153a, 160, 163a, 168c, 169, 170, 200, 201, 203, 244, 257c, 261, 264, 265, 267, 268, 304, 341, 344, 349 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Beschuldigter, Strafverteidiger, Staatsanwaltschaft, Ermittlungsrichter, Vorsitzender, Schöffen, Zeuge, Nebenkläger, JVA prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Beschuldigter/Angeklagter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

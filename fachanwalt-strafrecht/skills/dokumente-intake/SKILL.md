---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Strafrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aussagepsychologie-staatsanwaltschaft-aussagepsychologie` — Aussagepsychologie Staatsanwaltschaft Aussagepsychologie
- `chatcontrol-csam-einlassung-vorbereiten-hauptverhandlung` — Chatcontrol Csam Einlassung Vorbereiten Hauptverhandlung
- `ergaenzt-fachanwalt-insolvenzantrag-red-kanzlei-sonderfall` — Ergaenzt Fachanwalt Insolvenzantrag Red Kanzlei Sonderfall
- `fachanwalt-strafrecht-orientierung-untersuchungshaft` — Fachanwalt Strafrecht Orientierung Untersuchungshaft
- `koerperverletzung-stgb-koerperverletzung-todesfolge` — Koerperverletzung Stgb Koerperverletzung Todesfolge
- `mandat-triage-plaedoyer-vorbereitung-schriftsatzkern` — Mandat Triage Plaedoyer Vorbereitung Schriftsatzkern
- `nebenklage-nebenstrafrecht-opfervertretung-interessen-revision` — Nebenklage Nebenstrafrecht Opfervertretung Interessen Revision
- `raub-stgb-raub-todesfolge-rechtsbeugung-stgb` — Raub Stgb Raub Todesfolge Rechtsbeugung Stgb
- `steuerstrafrecht-ao-akteneinsicht-auswerten-erstgespraech` — Steuerstrafrecht Ao Akteneinsicht Auswerten Erstgespraech
- `stpo-strafrecht-strafverteidigung-zeugenbeistand-strafprozess` — Stpo Strafrecht Strafverteidigung Zeugenbeistand Strafprozess
- `strafprozess-antragslog-beweisantraege-biometrischer-cockpit` — Strafprozess Antragslog Beweisantraege Biometrischer Cockpit
- `strafprozess-instruktionen-pflichtverteidigung-beiordnung-strafr` — Strafprozess Instruktionen Pflichtverteidigung Beiordnung Strafr
- `strafr-dysfunk-befangenheitsantrag-beistandsleistung-stpo` — Strafr Dysfunk Befangenheitsantrag Beistandsleistung Stpo
- `strafr-dysfunk-darlegungslast-empirie-nutzen-erklaerungsrecht` — Strafr Dysfunk Darlegungslast Empirie Nutzen Erklaerungsrecht

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

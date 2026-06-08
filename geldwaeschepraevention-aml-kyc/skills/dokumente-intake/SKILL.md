---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Geldwaeschepraevention Aml Kyc** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `geldwaesche-audit-internal-datenqualitaet-register-immobilien` — Geldwaesche Audit Internal Datenqualitaet Register Immobilien
- `geldwaesche-krypto-zahlungsdienstleister-kyc-onboarding` — Geldwaesche Krypto Zahlungsdienstleister Kyc Onboarding
- `geldwaesche-pep-hochrisikoland-risikoanalyse-unternehmen` — Geldwaesche Pep Hochrisikoland Risikoanalyse Unternehmen
- `geldwaesche-sicherungsmassnahmen-geldwaesche-simulation` — Geldwaesche Sicherungsmassnahmen Geldwaesche Simulation
- `geldwaesche-transaktionsstopp-freeze-transparenzregister-ubo` — Geldwaesche Transaktionsstopp Freeze Transparenzregister Ubo
- `geldwaesche-verdachtsmeldung-geldwaesche-verpflichteten` — Geldwaesche Verdachtsmeldung Geldwaesche Verpflichteten
- `goaml-gwg-spezial-kommandocenter` — Goaml Gwg Kommandocenter
- `livecheck-red-risikoanalyse-verdachtsmeldeweiche-simulation` — Livecheck Red Risikoanalyse Verdachtsmeldeweiche Simulation
- `onboarding-bauleiter-trade-based-verdachtsmeldung-fiu` — Onboarding Bauleiter Trade Based Verdachtsmeldung Fiu
- `risikoanalyse-geldwaesche-bussgeld-geldwaesche` — Risikoanalyse Geldwaesche Bussgeld Geldwaesche
- `sanktionen-geldwaesche-gruppenweite-aml-kryptotransaktionen` — Sanktionen Geldwaesche Gruppenweite Aml Kryptotransaktionen
- `sonderfall-edge-geldwaesche-geldwaeschepraevention` — Sonderfall Edge Geldwaesche Geldwaeschepraevention
- `testlauf-beweislast-transaktionsmonitoring-international` — Testlauf Beweislast Transaktionsmonitoring International

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Geldwaeschepraevention Aml Kyc-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GwG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Verpflichteter (Bank, Anwalt, Notar).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---
name: dokumente-intake
description: "Dokumentenintake für Insolvenzrecht (Allgemein): sortiert Insolvenzantrag, Vermögensverzeichnis, Gutachten Sachverständiger, prüft Datum, Absender, Frist und Beweiswert (Bilanzen, Liquiditätsplan); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Insolvenzrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `anfechtungsrechte-antragspflicht-15a` — Anfechtungsrechte Antragspflicht 15A
- `anschluss` — Anschluss
- `antragspflicht-15a-17-19` — Antragspflicht 15A 17 19
- `antragspflicht-15a-inso` — Antragspflicht 15A Inso
- `auslaendischer-insolvenzverwalter-register-und-grundbuch` — Auslaendischer Insolvenzverwalter Register und Grundbuch
- `auslaendischer-office-holder-register-und-grundbuch` — Auslaendischer Office Holder Register und Grundbuch
- `belegmatrix-formular-portal-und-einreichung` — Belegmatrix Formular Portal und Einreichung
- `chronologie-internationaler-bezug-und-schnittstellen` — Chronologie Internationaler Bezug und Schnittstellen
- `do-versicherung-manager-haftung` — DO Versicherung Manager Haftung
- `einfuehrung-verhandlung-vergleich-und-eskalation` — Einfuehrung Verhandlung Vergleich und Eskalation
- `feststellung-sonderfall-glaeubigerantrag-inso` — Feststellung Sonderfall Glaeubigerantrag Inso
- `forderungsanmeldung-glaeubiger-174-177-inso` — Forderungsanmeldung Glaeubiger 174 177 Inso
- `glaeubigerantrag-glaeubigerausschuss` — Glaeubigerantrag Glaeubigerausschuss
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Insolvenzantrag, Gläubigerverzeichnis, Forderungsanmeldung, Insolvenztabelle, Berichts- und Schlusstermin, Insolvenzplan, Restrukturierungsplan (StaRUG).
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Insolvenzrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: InsO §§ 1, 13, 14, 15a, 17, 18, 19, 20, 21, 22, 27, 35, 39, 47, 55, 56, 60, 64, 80, 87, 97, 129, 133, 142, 174, 175, 179, 187, 199, 270, 270a-d, 286, 287, 295, 300, StaRUG §§ 1, 29, 31, 39, 49–55, 84, 100, 102 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Schuldner, IV/SV/Restrukturierungsbeauftragter, Gläubigerausschuss, Insolvenzgericht, Gläubiger, Geschäftsführer (§ 15a-Adressat) prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Schuldner GmbH/Person.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

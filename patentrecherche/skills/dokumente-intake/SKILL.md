---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Patentrecherche** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `dpmaregister-epue-beweislast-erfinderische-sonderfall` — Dpmaregister Epue Beweislast Erfinderische Sonderfall
- `erfinderische-taetigkeit-freedom-to-ki-patent` — Erfinderische Taetigkeit Freedom To Ki Patent
- `espacenet-google-neuheit-red` — Espacenet Google Neuheit Red
- `klassifikation-cpc-neuheit-patentfamilien-analyse` — Klassifikation Cpc Neuheit Patentfamilien Analyse
- `patentanwaelte-patentrecherche-patents` — Patentanwaelte Patentrecherche Patents
- `patentrecherche-kaltstart-interview` — Patentrecherche Kaltstart Interview
- `patg-problem-register` — Patg Problem Register
- `patr-fto-bericht-patentfamilie-priodatum-recherchestrategie` — Patr Fto Bericht Patentfamilie Priodatum Recherchestrategie
- `patr-software-pr-einfuehrung-pruefungsbescheid-vorbereiten` — Patr Software Pr Einfuehrung Pruefungsbescheid Vorbereiten
- `recherche-strategie-tools-marktuebersicht-recherchebericht` — Recherche Strategie Tools Marktuebersicht Recherchebericht
- `rechtsstand-pruefen-rueckfragen-mandant-depatisnet` — Rechtsstand Prüfen Rueckfragen Mandant Depatisnet
- `stand-technik-uspto-interessen` — Stand Technik Uspto Interessen
- `taetigkeit-fristennotiz-agentische-datenbank-epo-opposition` — Taetigkeit Fristennotiz Agentische Datenbank Epo Opposition

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Patentrecherche und FTO-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Anmelder.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

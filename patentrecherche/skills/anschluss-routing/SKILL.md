---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Patentrecherche** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

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

- Ergebnis sichten: Welche Patentrecherche und FTO-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (EPO R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate), notwendige Dokumente (Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Patentrecherche (FTO, Validity, Family-Watch).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 PatG
- § 4 PatG
- § 45 PatG
- § 14 PatG
- § 59 PatG
- § 203 StGB
- § 33 PatG
- § 81 PatG
- § 47 PatG
- § 39 PatG
- § 16 PatG
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)


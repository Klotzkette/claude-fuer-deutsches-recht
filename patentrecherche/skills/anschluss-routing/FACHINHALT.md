---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: patentrecherche."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Patentrecherche** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `agentisch-fristen-form-und-zustaendigkeit` — Agentisch Fristen Form und Zustaendigkeit
- `agentische-datenbank-recherche` — Agentische Datenbank Recherche
- `depatisnet-verhandlung-vergleich-und-eskalation` — Depatisnet Verhandlung Vergleich und Eskalation
- `dpmaregister-epue-beweislast-erfinderische` — Dpmaregister Epue Beweislast Erfinderische
- `epo-opposition-strategie` — EPO Opposition Strategie
- `epo-quellenkarte` — EPO Quellenkarte
- `epue-beweislast-und-darlegungslast` — Epue Beweislast und Darlegungslast
- `erfinderische-sonderfall-und-edge-case` — Erfinderische Sonderfall und Edge Case
- `erfinderische-taetigkeit-freedom-to-ki-patent` — Erfinderische Taetigkeit Freedom TO KI Patent
- `espacenet-google-neuheit-red-team-korrektur` — Espacenet Google Neuheit RED Team Korrektur
- `freedom-to-operate-recherche` — Freedom TO Operate Recherche
- `google-risikoampel-und-gegenargumente` — Google Risikoampel und Gegenargumente
- `kaltstart-interview` — Kaltstart Interview
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Patentrecherche und FTO-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (EPO R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate), notwendige Dokumente (Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

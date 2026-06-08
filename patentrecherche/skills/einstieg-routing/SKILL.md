---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Patentrecherche (FTO, Validity, Family-Watch): ordnet Rolle (Anmelder, Erfinder, Patentanwalt), markiert Frist (Prioritätsjahr 12 Monate), wählt Norm (PatG § 3 Neuheit, § 4 Erfinderischer Schritt, EPÜ Art. 54/56, PCT) und Zuständigkeit (DPMA), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Patentrecherche** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


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
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: EPO R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate.
- Fachpfad wählen: zentrale Anker im Patentrecherche und FTO sind PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Patentrecherche (FTO, Validity, Family-Watch) typische Eskalationsstufen: FTO-Bericht, Validity-Analyse, Stand der Technik-Liste.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

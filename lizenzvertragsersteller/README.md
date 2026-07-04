# Lizenzvertragsersteller


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`lizenzvertragsersteller`) | [`lizenzvertragsersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lizenzvertragsersteller.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Baukastensystem für IP-Lizenzverträge deutsches und internationales Recht. 32 Skills: Urheber Patent Marken Design Gebrauchsmuster Geschäftsgeheimnis Know-how; Klausel-Bausteine, Quellcode-Escrow, Insolvenz-Klausel, Sicherungslizenz, TT-GVO, DSGVO, Quellensteuer, Output DE EN bilingual.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`lizenzvertragsersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lizenzvertragsersteller.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/lizenzvertragsersteller/lizenzvertragsersteller-werkstatt.md" download><code>lizenzvertragsersteller-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/lizenzvertragsersteller/lizenzvertragsersteller-schnellstart.md" download><code>lizenzvertragsersteller-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Baukastensystem für IP-Lizenzvertraege nach deutschem und internationalem Recht. Pro Rolle, IP-Typ und Klauselbaustein ein Skill — die Skills greifen ineinander, vom Mandats-Intake bis zum unterschriftsreifen Vertrag in DE, EN oder bilingual.

## Was deckt das Plugin ab?

### IP-Typen
- **Urheberrecht und Software** (UrhG; $$ 31, 32, 32a, 69a-g)
- **Patente** (PatG; TT-GVO-Konformitaet)
- **Marken** (MarkenG $ 30; DPMA/EUIPO; Qualitaetskontrolle)
- **Geschmacksmuster / Design** (DesignG; EU-VO 6/2002)
- **Gebrauchsmuster** (GebrMG; Schnellschuss-Strategie neben Patent)
- **Geschäftsgeheimnisse / Know-how** (GeschGehG; Reverse-Engineering-Verbot)

### Parteienrollen
- Lizenzgeber / Lizenznehmer
- Sicherheitengeber / Sicherheitennehmer (Bank, Investor)
- Verwahrer / Escrow-Agent (Source-Code-Hinterlegung)
- Cross-Lizenz-Partner (Patent-Pool, Forschungspartnerschaft)
- Konzernlizenznehmer

### Vertragsbausteine
- Lizenzgegenstand mit Anlage A (IP-Liste, Reg.-Nr., Belastungen)
- Lizenzumfang (Territorium, Zeit, Anwendungsfeld)
- Exklusivitaet (sole, exclusive, non-exclusive, Most-Favoured-Customer)
- Vergütung (Pauschale, Running Royalty, Tiered, Mindestlizenz, Milestones)
- Reporting, Audit, Strafzinsen
- Sub-Lizenzen
- Verbesserungen / Grant-Back
- Haftung / Gewährleistung / Indemnification
- Rechtswahl + Gerichtsstand + Schiedsklausel (DE/EN/Schiedsinstitute)
- Vertragsdauer + Kuendigung + Folgen
- Vertraulichkeit + NDA-Interimsphase
- Source-Code-Escrow
- Insolvenzfestigkeit ($ 103 InsO)
- Sicherungslizenz / Pfandrecht an Immaterialguetern

### Compliance-Schichten
- Kartellrecht (TT-GVO EU 316/2014)
- Exportkontrolle (Dual-Use VO EU 2021/821; AWG/AWV; Sanktionen)
- Datenschutz (DSGVO Art. 28, 44 ff., 26)
- Steuern + Quellensteuer + DBA

### Output-Module
- Vertrag DE (Fertigentwurf, 20 Paragraphen, Anlagen A-E)
- Vertrag EN (Licence Agreement, English Law oder German Law)
- Bilingual DE/EN (side-by-side + Massgeb-Klausel)

## Workflow

```
1. einstieg-routing                          (Dashboard, Sofort-Triage)
2. mandat-intake-und-konfliktpruefung        (Konflikt-Check, Eilfristen)
3. ip-identifikation-und-bestandsaufnahme    (Anlage A: IP-Inventar)
4. parteienrolle-klaeren-...                  (Rollenmatrix)
5. transaktionsstruktur-visualisieren-ascii  (Diagramm)
6. pro IP-Typ: lizenz-XXX-spezialskill        (UrhG, PatG, MarkenG, ...)
7. Klauselbausteine waehlen + adaptieren     (klausel-XXX)
8. Compliance-Pruefung                        (TT-GVO, Dual-Use, DSGVO, Steuern)
9. Output                                     (DE / EN / bilingual)
```

## Quellenhygiene

- Rechtsprechung nur live verifizieren auf `bundesgerichtshof.de`, `dejure.org`, `curia.europa.eu`, `bundespatentgericht.de`.
- Keine BeckRS-/juris-/Kommentar-/Aufsatz-Blindzitate.
- Norm-Stellen aus `gesetze-im-internet.de` und `eur-lex.europa.eu`.

Konvention: siehe `references/quellenhygiene.md`, `references/zitierweise.md`, `references/leitentscheidungen-anker.md`.

## 32 Skills auf einen Blick

| Gruppe | Skills |
|---|---|
| Einstieg + Intake | `einstieg-routing`, `mandat-intake-und-konfliktpruefung`, `ip-identifikation-und-bestandsaufnahme`, `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer`, `transaktionsstruktur-visualisieren-ascii` |
| IP-Typ | `lizenz-urheberrecht-und-software-urhg`, `lizenz-patent-patg`, `lizenz-marke-markeng`, `lizenz-geschmacksmuster-design-designg`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg` |
| Klauseln | `klausel-lizenzgegenstand-und-anlage-ip-liste`, `klausel-lizenzumfang-territorium-zeit-feld`, `klausel-exklusivitaet-sole-non-exclusive`, `klausel-verguetung-pauschale-royalty-tiered`, `klausel-mindestlizenzen-meldungen-audit`, `klausel-unterlizenzen-sublicensing`, `klausel-verbesserungen-grant-back`, `klausel-haftung-gewaehrleistung-indemnification`, `klausel-rechtswahl-gerichtsstand-schiedsklausel`, `klausel-vertragsdauer-kuendigung-rueckwirkung`, `klausel-vertraulichkeit-und-nda-interimsphase` |
| Insolvenz + Sicherheiten | `escrow-quellcode-verwahrer-vereinbarung`, `insolvenz-fortbestand-paragraf-103-inso-lizenz`, `sicherungslizenz-pfandrecht-an-immaterialguetern` |
| Compliance | `kartellrecht-tt-gvo-eu-316-2014`, `exportkontrolle-dual-use-eu-2021-821`, `datenschutz-dsgvo-im-lizenzvertrag`, `steuern-quellensteuer-und-dba-lizenz` |
| Output | `output-vertrag-deutsch-fertigentwurf`, `output-vertrag-englisch-fertigentwurf`, `output-zweisprachig-bilingual-deutsch-englisch` |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `einstieg-routing`, `mandat-intake-und-konfliktpruefung` |
| 2. Unterlagen, Sachverhalt und Quellen | `datenschutz-dsgvo-im-lizenzvertrag`, `steuern-quellensteuer-und-dba-lizenz` |
| 3. Prüfung, Anspruch und Subsumtion | `klausel-haftung-gewaehrleistung-indemnification` |
| 4. Gestaltung, Strategie und Verhandlung | `klausel-exklusivitaet-sole-non-exclusive`, `klausel-lizenzgegenstand-und-anlage-ip-liste`, `klausel-lizenzumfang-territorium-zeit-feld`, `klausel-mindestlizenzen-meldungen-audit`, `klausel-rechtswahl-gerichtsstand-schiedsklausel`, `klausel-unterlizenzen-sublicensing`, `klausel-verbesserungen-grant-back`, `klausel-verguetung-pauschale-royalty-tiered`, `klausel-vertragsdauer-kuendigung-rueckwirkung`, `klausel-vertraulichkeit-und-nda-interimsphase`, `output-vertrag-deutsch-fertigentwurf`, `output-vertrag-englisch-fertigentwurf`, `transaktionsstruktur-visualisieren-ascii` |
| 6. Ergebnis, Schreiben und Kommunikation | `output-zweisprachig-bilingual-deutsch-englisch` |
| 7. Kontrolle, Qualität und Gegenprüfung | `exportkontrolle-dual-use-eu-2021-821` |
| 8. Spezialmodule und Schnittstellen | `escrow-quellcode-verwahrer-vereinbarung`, `insolvenz-fortbestand-paragraf-103-inso-lizenz`, `ip-identifikation-und-bestandsaufnahme`, `kartellrecht-tt-gvo-eu-316-2014`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg`, `lizenz-geschmacksmuster-design-designg`, `lizenz-marke-markeng`, `lizenz-patent-patg`, `lizenz-urheberrecht-und-software-urhg`, `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer`, `sicherungslizenz-pfandrecht-an-immaterialguetern` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 32 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `datenschutz-dsgvo-im-lizenzvertrag` | Wenn es um Datenschutz — DSGVO im Lizenzvertrag in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Anwalts-Dashboard Lizenzvertragsersteller in Lizenzvertragsersteller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `escrow-quellcode-verwahrer-vereinbarung` | Wenn es um Escrow / Quellcode-Verwahrer-Vereinbarung in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `exportkontrolle-dual-use-eu-2021-821` | Wenn es um Exportkontrolle — Dual-Use und Lizenz in Lizenzvertragsersteller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `insolvenz-fortbestand-paragraf-103-inso-lizenz` | Wenn es um Insolvenz-Fortbestand der Lizenz ($ 103 InsO) in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `ip-identifikation-und-bestandsaufnahme` | Wenn es um IP-Identifikation und Bestandsaufnahme in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `kartellrecht-tt-gvo-eu-316-2014` | Wenn es um Kartellrecht — TT-GVO (EU) 316/2014 in Lizenzvertragsersteller geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `klausel-exklusivitaet-sole-non-exclusive` | Wenn es um Klausel Exklusivitaet — sole, exclusive, non-exclusive in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ri... |
| `klausel-haftung-gewaehrleistung-indemnification` | Wenn es um Klausel Haftung, Gewaehrleistung, Indemnification in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| `klausel-lizenzgegenstand-und-anlage-ip-liste` | Wenn es um Klausel Lizenzgegenstand + Anlage A in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `klausel-lizenzumfang-territorium-zeit-feld` | Wenn es um Klausel Lizenzumfang — Territorium, Zeit, Feld in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klausel-mindestlizenzen-meldungen-audit` | Wenn es um Klausel Mindestlizenzen, Meldungen, Audit in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `klausel-rechtswahl-gerichtsstand-schiedsklausel` | Wenn es um Klausel Rechtswahl, Gerichtsstand, Schiedsklausel in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klausel-unterlizenzen-sublicensing` | Wenn es um Klausel Unterlizenzen (Sub-Licensing) in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `klausel-verbesserungen-grant-back` | Wenn es um Klausel Verbesserungen (Grant-Back) in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klausel-verguetung-pauschale-royalty-tiered` | Wenn es um Klausel Vergütung — Pauschale, Royalty, Tiered in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfra... |
| `klausel-vertragsdauer-kuendigung-rueckwirkung` | Wenn es um Klausel Vertragsdauer und Kuendigung in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klausel-vertraulichkeit-und-nda-interimsphase` | Wenn es um Klausel Vertraulichkeit + NDA-Interimsphase in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `lizenz-gebrauchsmuster-gebrmg` | Wenn es um Lizenz Gebrauchsmuster (GebrMG) in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `lizenz-geschaeftsgeheimnis-knowhow-geschgehg` | Wenn es um Lizenz Geschäftsgeheimnis / Know-how (GeschGehG) in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lizenz-geschmacksmuster-design-designg` | Wenn es um Lizenz Design (DesignG / EU-Verordnung) in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweis... |
| `lizenz-marke-markeng` | Wenn es um Lizenz Marke (MarkenG) in Lizenzvertragsersteller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `lizenz-patent-patg` | Wenn es um Lizenz Patent (PatG) in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `lizenz-urheberrecht-und-software-urhg` | Wenn es um Lizenz Urheberrecht / Software ($$ 31 ff. UrhG) in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandat-intake-und-konfliktpruefung` | Wenn es um Mandatsannahme und Konfliktpruefung in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-vertrag-deutsch-fertigentwurf` | Wenn es um Output: Lizenzvertrag in deutscher Sprache in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-vertrag-englisch-fertigentwurf` | Wenn es um Output: Licence Agreement in English in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-zweisprachig-bilingual-deutsch-englisch` | Wenn es um Output: Zweisprachiger Lizenzvertrag DE/EN in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer` | Wenn es um Parteienrollen klären in Lizenzvertragsersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `sicherungslizenz-pfandrecht-an-immaterialguetern` | Wenn es um Sicherungslizenz und Pfandrecht an Immaterialguetern in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `steuern-quellensteuer-und-dba-lizenz` | Wenn es um Steuern und Quellensteuer — Lizenz in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `transaktionsstruktur-visualisieren-ascii` | Wenn es um Transaktionsstruktur visualisieren — ASCII in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

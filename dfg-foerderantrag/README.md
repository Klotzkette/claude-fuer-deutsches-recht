# DFG-Förderantrag


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`dfg-foerderantrag`) | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/dfg-foerderantrag/dfg-foerderantrag-werkstatt.md" download><code>dfg-foerderantrag-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/dfg-foerderantrag/dfg-foerderantrag-schnellstart.md" download><code>dfg-foerderantrag-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Plugin für die praktische Antragstellung bei der Deutschen Forschungsgemeinschaft: Sachbeihilfe, elan-Formalia, Projektbeschreibung, Finanzplan, Forschungsdaten, Ethik-/KI-Check, Reviewer-Perspektive, Wiedereinreichung und strategische Entscheidung zwischen kleinem schnellen Antrag und großem Prestigeprojekt.

Der Stil ist bewusst nicht bürokratisch. Das Plugin fragt zuerst: Was ist wissenschaftlich stark, was ist realistisch förderbar, was kann schneller entschieden werden und wo ist der große Antrag zwar verführerisch, aber prozessual zäher? Es arbeitet adaptiv: Anfänger bekommen eine geführte Mini-Roadmap; erfahrene Antragsteller bekommen direkt Red-Team, Kürzungsrisiko und Programmstrategie.

## Quellen-Gate

Vor jeder belastbaren Ausgabe aktuelle DFG-Seiten prüfen:

- DFG Sachbeihilfe: themenoffene Einzelförderung, Neuanträge jederzeit, Fortsetzungsanträge spätestens 6 Monate vor Mittelverbrauch.
- DFG Begutachtung: grundsätzlich zwei Gutachten; bei Anträgen bis 200.000 Euro kann ausnahmsweise ein aussagekräftiges externes Gutachten reichen.
- Reinhart-Koselleck-Projekte: 500.000 bis 1,25 Mio. Euro für fünf Jahre in Stufen von 250.000 Euro; nur für herausragende, besonders innovative oder risikobehaftete Projekte, die nicht in normale Verfahren passen.
- DFG-Merkblätter, elan-Vorlagen, fachzuständige Ansprechpersonen und aktuelle Vordruckstände immer live gegen `dfg.de` prüfen.

## Schnellstart

```text
/dfg-foerderantrag:allgemein
```

Der Allgemein-Skill führt in 60 Sekunden durch: Forschungsfrage, Förderprogramm, Summe, Tempo, Zielgruppe der Begutachtung, Vorarbeiten, Risiken, Daten-/Ethikthemen und gewünschtes Ergebnis.

Typische Startpunkte:

| Situation | Start |
| --- | --- |
| "Ich habe nur eine Forschungsidee" | `dfg-foerderantrag-allgemein` → Mini-Roadmap und Minimalprojekt |
| "Sachbeihilfe oder größer?" | `dfg-foerderstrategie-schnell-oder-gross` |
| "Entwurf liegt vor" | `dfg-reviewer-red-team` → danach Text- und Finanzskills |
| "Ablehnung liegt vor" | `dfg-wiedereinreichung-nach-ablehnung` |

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `dfg-foerderantrag-allgemein` | Einstieg, Triage, Programmroute und erster Arbeitsplan |
| `dfg-foerderstrategie-schnell-oder-gross` | Entscheidung: kleiner schneller Antrag, normale Sachbeihilfe, Koselleck oder anderes Programm |
| `dfg-sachbeihilfe-elan-formalia` | Sachbeihilfe, elan, Anlagen, Vordrucklogik, formales Gate |
| `dfg-bis-200k-begutachtung-light` | Kleine/mittlere Anträge so bauen, dass sie schnell, klar und begutachtbar sind |
| `dfg-koselleck-500k-125m` | Koselleck-Check: 500.000 bis 1,25 Mio. Euro, Risiko, Profil, Vertrauensvorschuss |
| `dfg-projektbeschreibung-arbeitsprogramm` | Forschungsfrage, Stand der Forschung, Ziele, Arbeitspakete, Meilensteine |
| `dfg-finanzplan-module-personal-geraete` | Personal, Geräte, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Budgetbegründung |
| `dfg-reviewer-red-team` | Gutachterperspektive, Angriffsflächen, Kürzungsrisiken, Ablehnungsgründe |
| `dfg-wiedereinreichung-nach-ablehnung` | Ablehnung auswerten, Gutachten ernst nehmen, Neuaufstellung |
| `dfg-ki-ethik-forschungsdaten` | KI-Nutzung, Vertraulichkeit, Forschungsdatenmanagement, Ethik und Datenschutz |

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dfg-erstpruefung-und-mandatsziel`, `dokumente-intake`, `einstieg-routing`, `erstpruefung-rollenklaerung-mandatsziel`, `kaltstart-triage`, `start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `adaptive-dokumentenmatrix-lueckenliste`, `adaptive-dokumentenmatrix-und-lueckenliste`, `chronologie-und-belegmatrix`, `dfg-ki-ethik-forschungsdaten`, `elan-formular-portal-einreichungslogik`, `forschungsdaten-fristennotiz-naechster`, `forschungsdaten-fristennotiz-und-naechster-schritt`, `grosse-compliance-dokumentation-aktenvermerk`, `profi-reviewer-beweislast-strategien`, `quellen-livecheck`, `reviewer-beweislast-darlegungslast`, `reviewer-beweislast-und-darlegungslast`, `schnelle-quellenkarte`, `spezial-grosse-compliance-dokumentation-und-akte`, `spezial-schnelle-livequellen-und-rechtsprechungscheck`, `unterlagen-luecken`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `anfaenger-risikoampel-gegenargumente`, `dfg-erstantragsteller-besondere-checks`, `fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `dfg-finanzplan-module-personal-geraete`, `dfg-foerderstrategie-schnell-oder-gross`, `dfg-publikationsstrategie-projekt`, `dfg-zeitplan-und-meilensteine`, `elan-ethik-finanzplan`, `finanzplan-mandantenkommunikation`, `finanzplan-mandantenkommunikation-entscheidungsvorlage`, `foerderstrategie-schnell-grossgeraete-cluster`, `kleine-verhandlung-vergleich-eskalation`, `kleine-verhandlung-vergleich-und-eskalation`, `publikationsstrategie-projekt`, `strategien-internationaler-bezug`, `strategien-internationaler-bezug-und-schnittstellen`, `zeitplan-meilensteine-zwischen` |
| 5. Verfahren, Behörde und Gericht | `dfg-grossgeraete-und-cluster-antrag`, `eigene-vorarbeiten-erstantragsteller`, `erstantrag-projektlogik`, `foerderantragssteller-formalia-red-fuehrung`, `fuehrung-schriftsatz-brief-memo-bausteine`, `fuehrung-schriftsatz-brief-und-memo-bausteine`, `profi-behoerden-gerichts-registerweg`, `sachbeihilfe-fristen-form-zustaendigkeit` |
| 6. Ergebnis, Schreiben und Kommunikation | `dfg-zwischen-und-abschlussbericht`, `mandantenkommunikation`, `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `dfg-kollegen-review-organisieren`, `dfg-reviewer-red-team`, `formalia-fehlerkatalog`, `formalia-red-team-und-qualitaetskontrolle`, `redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `anfaenger-antraege-dfg`, `antraege-zahlen-schwellen-und-berechnung`, `antraege-zahlen-schwellenwerte-berechnung`, `dfg-bis-200k-begutachtung-light`, `dfg-eigenanteil-und-grundausstattung`, `dfg-eigene-vorarbeiten-darstellen`, `dfg-grundsystem-foerderlinien`, `dfg-internationale-kooperation-aufbau`, `dfg-koselleck-500k-125m`, `dfg-koselleck-500k-praeregistrierung`, `dfg-praeregistrierung-replication-studies`, `dfg-projektbeschreibung-arbeitsprogramm`, `dfg-replikationskrise-statistik-spezial`, `dfg-sachbeihilfe-elan-formalia`, `dfg-software-veroeffentlichung-spezial`, `dfg-software-veroeffentlichung-tieforschung`, `dfg-tieforschung-ethik-pflichten`, `dfg-wiedereinreichung-nach-ablehnung`, ... plus 8 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adaptive-dokumentenmatrix-lueckenliste` | Wenn es um Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `adaptive-dokumentenmatrix-und-lueckenliste` | Wenn es um Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| `anfaenger-antraege-dfg` | Wenn es um Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswa... |
| `anfaenger-risikoampel-gegenargumente` | Wenn es um Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswa... |
| `anschluss-routing` | Wenn es um Anschluss-Routing in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `antraege-zahlen-schwellen-und-berechnung` | Wenn es um Antraege: Zahlen, Schwellenwerte und Berechnung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `antraege-zahlen-schwellenwerte-berechnung` | Wenn es um Antraege: Zahlen, Schwellenwerte und Berechnung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `dfg-bis-200k-begutachtung-light` | Wenn es um DFG-Antrag bis 200.000 Euro in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `dfg-eigenanteil-und-grundausstattung` | Wenn es um Eigenanteil und Grundausstattung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-eigene-vorarbeiten-darstellen` | Wenn es um DFG: Eigene Vorarbeiten in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Dfg Eig... |
| `dfg-erstantragsteller-besondere-checks` | Wenn es um Erstantragsteller-Sondercheck in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-erstpruefung-und-mandatsziel` | Wenn es um DFG: Erstprüfung, Rollenklärung und Mandatsziel in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `dfg-finanzplan-module-personal-geraete` | Wenn es um Finanzplan und Module in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `dfg-foerderstrategie-schnell-oder-gross` | Wenn es um DFG-Förderstrategie: schnell, schlank oder groß? in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichw... |
| `dfg-grossgeraete-und-cluster-antrag` | Wenn es um DFG: Grossgeraete und Cluster in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-grundsystem-foerderlinien` | Wenn es um Grundsystem DFG-Foerderlinien in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-internationale-kooperation-aufbau` | Wenn es um DFG: Internationale Kooperation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort:... |
| `dfg-ki-ethik-forschungsdaten` | Wenn es um digitale Werkzeuge, Ethik und Forschungsdaten in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-kollegen-review-organisieren` | Wenn es um DFG: Kollegen-Review organisieren in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dfg-koselleck-500k-125m` | Wenn es um Reinhart-Koselleck-Check in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `dfg-koselleck-500k-praeregistrierung` | Wenn es um Reinhart-Koselleck-Check in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-praeregistrierung-replication-studies` | Wenn es um Praeregistrierung und Replikation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-projektbeschreibung-arbeitsprogramm` | Wenn es um Projektbeschreibung und Arbeitsprogramm in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-publikationsstrategie-projekt` | Wenn es um Publikationsstrategie Projekt in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: D... |
| `dfg-replikationskrise-statistik-spezial` | Wenn es um DFG: Statistik nach Replikationskrise in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `dfg-reviewer-red-team` | Wenn es um Reviewer-Red-Team in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `dfg-sachbeihilfe-elan-formalia` | Wenn es um Sachbeihilfe und elan-Formalia in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-software-veroeffentlichung-spezial` | Wenn es um DFG: Software-Veroeffentlichung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort:... |
| `dfg-software-veroeffentlichung-tieforschung` | Wenn es um DFG: Software-Veroeffentlichung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort:... |
| `dfg-tieforschung-ethik-pflichten` | Wenn es um Tierforschungs-Ethikpflichten in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-wiedereinreichung-nach-ablehnung` | Wenn es um Wiedereinreichung nach Ablehnung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dfg-zeitplan-und-meilensteine` | Wenn es um Zeitplan und Meilensteine in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Dfg Z... |
| `dfg-zwischen-und-abschlussbericht` | Wenn es um Zwischen- und Abschlussbericht in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `dokumente-intake` | Wenn es um Dokumentenintake in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eigene-vorarbeiten-erstantragsteller` | Wenn es um DFG: Eigene Vorarbeiten in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Eigene... |
| `einstieg-routing` | Wenn es um Einstieg und Routing in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `elan-ethik-finanzplan` | Wenn es um Elan: Formular, Portal und Einreichungslogik in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `elan-formular-portal-einreichungslogik` | Wenn es um Elan: Formular, Portal und Einreichungslogik in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstantrag-projektlogik` | Wenn es um Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstpruefung-rollenklaerung-mandatsziel` | Wenn es um DFG: Erstprüfung, Rollenklärung und Mandatsziel in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `ethik-abschlussprodukt-uebergabe` | Wenn es um Ethik: Abschlussprodukt und Übergabe in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ethik-abschlussprodukt-und-uebergabe` | Wenn es um Ethik: Abschlussprodukt und Übergabe in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `finanzplan-mandantenkommunikation` | Wenn es um Finanzplan: Mandantenkommunikation und Entscheidungsvorlage in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `finanzplan-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Finanzplan: Mandantenkommunikation und Entscheidungsvorlage in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `foerderantragssteller-formalia-red-fuehrung` | Wenn es um Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründ... |
| `foerderstrategie-schnell-grossgeraete-cluster` | Wenn es um DFG-Förderstrategie: schnell, schlank oder groß? in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichw... |
| `formalia-fehlerkatalog` | Wenn es um Formalia Fehlerkatalog in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `formalia-red-team-und-qualitaetskontrolle` | Wenn es um Formalia: Red-Team und Qualitätskontrolle in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forschungsdaten-fristennotiz-naechster` | Wenn es um Forschungsdaten: Fristennotiz und nächster Schritt in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `forschungsdaten-fristennotiz-und-naechster-schritt` | Wenn es um Forschungsdaten: Fristennotiz und nächster Schritt in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `fuehrung-schriftsatz-brief-memo-bausteine` | Wenn es um Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fuehrung-schriftsatz-brief-und-memo-bausteine` | Wenn es um Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `grosse-compliance-dokumentation-aktenvermerk` | Wenn es um Große: Compliance-Dokumentation und Aktenvermerk in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `grosse-kleine-koselleck-interessen` | Wenn es um Große: Compliance-Dokumentation und Aktenvermerk in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `internationale-kooperation-ki-ethik-kollegen` | Wenn es um DFG: Internationale Kooperation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort:... |
| `kaltstart-triage` | Wenn es um DFG-Förderantrag — Allgemein in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kleine-verhandlung-vergleich-eskalation` | Wenn es um Kleine: Verhandlung, Vergleich und Eskalation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kleine-verhandlung-vergleich-und-eskalation` | Wenn es um Kleine: Verhandlung, Vergleich und Eskalation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `koselleck-interessen` | Wenn es um Koselleck: Mehrparteienkonflikt und Interessenmatrix in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `koselleck-mehrparteien-konflikt-und-interessen` | Wenn es um Koselleck: Mehrparteienkonflikt und Interessenmatrix in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mandantenkommunikation` | Wenn es um Mandantenkommunikation in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `output-waehlen` | Wenn es um Output wählen in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `profi-behoerden-gerichts-registerweg` | Wenn es um Profi: Behörden-, Gerichts- oder Registerweg in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `profi-reviewer-beweislast-strategien` | Wenn es um Profi: Behörden-, Gerichts- oder Registerweg in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `publikationsstrategie-projekt` | Wenn es um Publikationsstrategie Projekt in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: P... |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `redteam-qualitygate` | Wenn es um Red-Team Qualitygate in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `reviewer-beweislast-darlegungslast` | Wenn es um Reviewer: Beweislast, Darlegungslast und Substantiierung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `reviewer-beweislast-und-darlegungslast` | Wenn es um Reviewer: Beweislast, Darlegungslast und Substantiierung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| `sachbeihilfe-bis-200k-eigenanteil` | Wenn es um Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `sachbeihilfe-fristen-form-zustaendigkeit` | Wenn es um Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `schnelle-quellenkarte` | Wenn es um Schnelle Quellenkarte in DFG-Förderantrag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `spezial-grosse-compliance-dokumentation-und-akte` | Wenn es um Grosse: Compliance-Dokumentation und Aktenvermerk in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `spezial-schnelle-livequellen-und-rechtsprechungscheck` | Wenn es um Schnelle: Livequellen- und Rechtsprechungscheck in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `start-chronologie-fristen` | Wenn es um DFG-Förderantrag — Allgemein in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `strategien-internationaler-bezug` | Wenn es um Strategien: Internationaler Bezug und Schnittstellen in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strategien-internationaler-bezug-und-schnittstellen` | Wenn es um Strategien: Internationaler Bezug und Schnittstellen in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `team-sonderfall-edge-case` | Wenn es um Team: Sonderfall und Edge-Case-Prüfung in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in DFG-Förderantrag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zeitplan-meilensteine-zwischen` | Wenn es um Zeitplan und Meilensteine in DFG-Förderantrag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Zeitp... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

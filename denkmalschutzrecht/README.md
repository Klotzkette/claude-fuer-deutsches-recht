# Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn Landesgesetze


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`denkmalschutzrecht`) | [`denkmalschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Denkmalschutzrecht in Deutschland: Art. 14 GG und Art. 73 GG als bundesstaatlicher Rahmen plus alle sechzehn Landesgesetze. Skills für Eintragung Erlaubnis Bußgeld steuerliche Förderung nach Paragraf 7i EStG und Welterbestätten — länderübergreifende Grundlagen und Landesrecht klar getrennt.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`denkmalschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/denkmalschutzrecht/denkmalschutzrecht-werkstatt.md" download><code>denkmalschutzrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/denkmalschutzrecht/denkmalschutzrecht-schnellstart.md" download><code>denkmalschutzrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Plugin für die anwaltliche Bearbeitung von Mandaten im deutschen Denkmalschutzrecht. Strukturiert in drei Schichten:

1. **Allgemeiner Teil** — bundesstaatlicher Rahmen (Art. 73 GG, Art. 14 GG, Verwaltungsverfahrensrecht, Welterbe).
2. **Querschnittsskills** — Denkmaleigenschaft, Eintragung, Erlaubnis, Förderung, Enteignung und Entschädigung; sie greifen unabhängig vom Bundesland.
3. **Sechzehn Bundesländer-Skills** — je ein eigener Skill pro Landesgesetz, mit Gesetzesbezeichnung, zuständigen Behörden und den landestypischen Verfahrensbesonderheiten.

## Aufbau und Anwendung

Die Allgemein-Skills helfen, einen Fall zu sortieren und ihn vom GG- und EU-Rahmen aus zu erden. Sobald klar ist, in welchem Bundesland das Objekt belegen ist, wird der landesspezifische Skill (`denkmalschutz-<bundesland>-<gesetzkuerzel>`) zugeschaltet — er enthält die konkreten Norm-Anker des jeweiligen Landesgesetzes und die zuständige Behördenkette.

## Quellenhygiene

Konkrete Paragrafenzitate, Aktenzeichen und Fundstellen werden ausnahmslos in den amtlichen Landesgesetzes-Datenbanken (typischerweise unter `landesrecht.<land>.de` oder `gesetze-im-internet.de` für Bundesrecht) live verifiziert; das Plugin nennt die Gesetzesabkürzungen und das verbindliche Suchregime, nicht aber halluzinierte Randnummern oder Fundstellen aus Modellwissen.

## Sicherheitsabstand

Denkmalschutzrecht ist Landesrecht. Bei jedem Mandat ist als allererstes das anwendbare Landesgesetz zu identifizieren — danach erst die einschlägigen Paragrafen prüfen. Skills, die einen Sachverhalt ohne Belegenheit beurteilen, sind unzulässig.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `einstieg-routing`, `erstgespraech-mandatsannahme`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `grundbegriffe-und-rechtsquellen`, `hamburg-spezial-speicherstadt-kontorhausviertel`, `quellen-livecheck` |
| 5. Verfahren, Behörde und Gericht | `bussgeld-ordnungswidrigkeitsverfahren`, `eintragungsverfahren-allgemein`, `verfahrensgrundsaetze-vwvfg`, `widerspruch-und-klagewege` |
| 8. Spezialmodule und Schnittstellen | `art-14-gg-eigentum-und-denkmalschutz`, `art-73-gg-laenderzustaendigkeit`, `baden-wuerttemberg-spezial-sachgesamtheiten-gesamtanlagen`, `bauordnungsrechtliche-schnittstelle`, `bayern-spezial-bodendenkmaeler-grabungsgenehmigung`, `brandenburg-spezial-schloesser-gutsanlagen-restitution`, `denkmaleigenschaft-feststellen`, `denkmalschutz-baden-wuerttemberg-dschg-bw`, `denkmalschutz-bayern-baydschg`, `denkmalschutz-berlin-dschg-bln`, `denkmalschutz-berlin-spezial-stadtmauer-und-mauerweg`, `denkmalschutz-brandenburg-bbgdschg`, `denkmalschutz-bremen-dschgbrem`, `denkmalschutz-bremen-spezial-rathaus-und-roland-welterbe`, `denkmalschutz-hamburg-dschgha`, `denkmalschutz-hessen-hdschg`, `denkmalschutz-mecklenburg-vorpommern-dschg-m-v`, `denkmalschutz-niedersachsen-ndschg`, ... plus 22 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `art-14-gg-eigentum-und-denkmalschutz` | Wenn es um Art. 14 GG — Eigentum und Denkmalschutz in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `art-73-gg-laenderzustaendigkeit` | Wenn es um Art. 70 GG, Art. 73 GG — Länderzuständigkeit im Denkmalschutz in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert ein direkt nutzbares Arbeits... |
| `baden-wuerttemberg-spezial-sachgesamtheiten-gesamtanlagen` | Wenn es um Sachgesamtheiten und Gesamtanlagen in Baden-Wuerttemberg in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `bauordnungsrechtliche-schnittstelle` | Wenn es um Bauordnungsrechtliche Schnittstelle in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `bayern-spezial-bodendenkmaeler-grabungsgenehmigung` | Wenn es um Bodendenkmaeler und Grabungsgenehmigung in Bayern in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| `brandenburg-spezial-schloesser-gutsanlagen-restitution` | Wenn es um Schloesser, Gutsanlagen und Restitution in Brandenburg in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbe... |
| `bussgeld-ordnungswidrigkeitsverfahren` | Wenn es um Bussgeld- und Ordnungswidrigkeitsverfahren in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt m... |
| `denkmaleigenschaft-feststellen` | Wenn es um Denkmaleigenschaft feststellen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `denkmalschutz-baden-wuerttemberg-dschg-bw` | Wenn es um Denkmalschutz Baden-Württemberg (DSchG-BW) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-bayern-baydschg` | Wenn es um Denkmalschutz Bayern (BayDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-berlin-dschg-bln` | Wenn es um Denkmalschutz Berlin (DSchG-Bln) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-berlin-spezial-stadtmauer-und-mauerweg` | Wenn es um Stadtmauer Berlin und Berliner Mauerweg als Denkmal in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| `denkmalschutz-brandenburg-bbgdschg` | Wenn es um Denkmalschutz Brandenburg (BbgDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-bremen-dschgbrem` | Wenn es um Denkmalschutz Bremen (DSchG-Brem) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-bremen-spezial-rathaus-und-roland-welterbe` | Wenn es um Rathaus und Roland Bremen als UNESCO-Welterbe in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| `denkmalschutz-hamburg-dschgha` | Wenn es um Denkmalschutz Hamburg (DSchG-HA) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-hessen-hdschg` | Wenn es um Denkmalschutz Hessen (HDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-mecklenburg-vorpommern-dschg-m-v` | Wenn es um Denkmalschutz Mecklenburg-Vorpommern (DSchG M-V) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Soforts... |
| `denkmalschutz-niedersachsen-ndschg` | Wenn es um Denkmalschutz Niedersachsen (NDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-nordrhein-westfalen-dschg-nrw` | Wenn es um Denkmalschutz Nordrhein-Westfalen (DSchG-NRW) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| `denkmalschutz-rheinland-pfalz-dschpflg` | Wenn es um Denkmalschutz Rheinland-Pfalz (DSchPflG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-saarland-sdschg` | Wenn es um Denkmalschutz Saarland (SDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-saarland-spezial-voelklinger-huette-welterbe` | Wenn es um Voelklinger Huette als UNESCO-Welterbe im Saarland in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit... |
| `denkmalschutz-sachsen-anhalt-dschg-lsa` | Wenn es um Denkmalschutz Sachsen-Anhalt (DSchG-LSA) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-sachsen-sachsdschg` | Wenn es um Denkmalschutz Sachsen (SächsDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `denkmalschutz-schleswig-holstein-dschg-sh` | Wenn es um Denkmalschutz Schleswig-Holstein (DSchG-SH) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschrit... |
| `denkmalschutz-thueringen-thuerdschg` | Wenn es um Denkmalschutz Thüringen (ThürDSchG) in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg — Routing im Denkmalschutzrecht in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofor... |
| `eintragungsverfahren-allgemein` | Wenn es um Eintragungsverfahren allgemein in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `enteignung-uebernahme-und-entschaedigung` | Wenn es um Enteignung, Übernahme und Entschädigung in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erlaubnis-pflichtige-massnahmen` | Wenn es um Erlaubnispflichtige Maßnahmen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstgespraech-mandatsannahme` | Wenn es um Erstgespräch — Denkmalschutzrechtliche Mandatsannahme in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit So... |
| `foerderung-und-steuerliche-abschreibung` | Wenn es um Förderung und steuerliche Abschreibung in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `grundbegriffe-und-rechtsquellen` | Wenn es um Grundbegriffe und Rechtsquellen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zustän... |
| `hamburg-spezial-speicherstadt-kontorhausviertel` | Wenn es um Speicherstadt und Kontorhausviertel mit Chilehaus als UNESCO-Welterbe in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Ri... |
| `hessen-spezial-limes-bergpark-wilhelmshoehe` | Wenn es um Limes und Bergpark Wilhelmshoehe als UNESCO-Welterbe in Hessen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzba... |
| `kaltstart-triage` | Wenn es um Kaltstart — Denkmalschutzrechtliche Triage in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sof... |
| `mecklenburg-vorpommern-spezial-backsteingotik-stralsund-wismar` | Wenn es um Backsteingotik Stralsund und Wismar als UNESCO-Welterbe in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `niedersachsen-spezial-wattenmeer-fagus-werk` | Wenn es um Wattenmeer und Fagus-Werk Alfeld als UNESCO-Welterbe in Niedersachsen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt... |
| `nordrhein-westfalen-spezial-zollverein-industriekultur` | Wenn es um Zeche und Kokerei Zollverein als UNESCO-Welterbe in NRW in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arb... |
| `quellen-livecheck` | Wenn es um Quellen-Livecheck Denkmalrecht in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `rechtsprechungsanker-denkmalrecht` | Wenn es um Rechtsprechungsanker Denkmalrecht in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rheinland-pfalz-spezial-mittelrheintal-schum-staetten` | Wenn es um Oberes Mittelrheintal und SchUM-Staetten als UNESCO-Welterbe in Rheinland-Pfalz in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert... |
| `sachsen-anhalt-spezial-bauhaus-quedlinburg-luther` | Wenn es um Bauhaus, Quedlinburg und Lutherstaetten als UNESCO-Welterbe in Sachsen-Anhalt in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ei... |
| `sachsen-spezial-montanregion-erzgebirge-muskauer-park` | Wenn es um Montanregion Erzgebirge und Muskauer Park als UNESCO-Welterbe in Sachsen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein dir... |
| `schleswig-holstein-spezial-luebeck-haithabu-wattenmeer` | Wenn es um Luebeck, Haithabu-Danewerk und Wattenmeer als UNESCO-Welterbe in Schleswig-Holstein in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; lief... |
| `thueringen-spezial-wartburg-klassisches-weimar-juedisches-erfurt` | Wenn es um Wartburg, Klassisches Weimar, Bauhaus und juedisch-mittelalterliches Erfurt in Thueringen in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt... |
| `unesco-welterbe-und-icomos` | Wenn es um UNESCO-Welterbe und ICOMOS in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigke... |
| `verfahrensgrundsaetze-vwvfg` | Wenn es um Verfahrensgrundsätze nach VwVfG in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `widerspruch-und-klagewege` | Wenn es um Widerspruch und Klagewege im Denkmalrecht in Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen,... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

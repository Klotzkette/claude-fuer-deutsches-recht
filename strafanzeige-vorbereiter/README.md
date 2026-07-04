# Strafanzeige-Vorbereiter


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafanzeige-vorbereiter`) | [`strafanzeige-vorbereiter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Vorsichtiger Strafanzeigen-Vorbereiter: prüft Anfangsverdacht, Beweise, Strafantrag, Risiken falscher Verdächtigung, Alternativen und erstellt nur bei tragfähiger Tatsachengrundlage eine nüchterne Strafanzeige.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strafanzeige-vorbereiter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafanzeige-vorbereiter/strafanzeige-vorbereiter-werkstatt.md" download><code>strafanzeige-vorbereiter-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafanzeige-vorbereiter/strafanzeige-vorbereiter-schnellstart.md" download><code>strafanzeige-vorbereiter-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Strafanzeige oder einen Strafantrag vorbereiten: Sachverhalt, Tatverdacht, Beweise, Fristen, Antragsdelikte, Nebenfolgen und adressatengerechte Darstellung.
Dieses Plugin ist ausdrücklich keine Strafanzeigenkanone. Es soll Gerichte und Staatsanwaltschaften nicht mit wütenden, unbelegten Anzeigen fluten und niemanden durch haltlose Vorwürfe unter Druck setzen. Wenn eine Strafanzeige aber nötig ist, führt es zu einem sauberen, nüchternen, beweisnahen Entwurf.

## Leitplanke

Wehe, es werden Dinge behauptet, die nicht stimmen. Das Plugin zwingt zur Trennung von eigener Wahrnehmung, Dokument, Zeuge, Vermutung und rechtlicher Bewertung. Bei eigener Beteiligung, Unternehmensfällen, schweren Gewalt-/Sexualdelikten, Wirtschaftsstrafsachen oder Berufsgeheimnissen: anwaltliche Hilfe einschalten.

## Was dieses Plugin gut kann

- Trennt Strafanzeige, Strafantrag, zivilrechtliche Alternativen und bloße Beschwerde.
- Prüft vorab § 164 StGB, §§ 186/187 StGB, § 824 BGB und Druckmittelrisiken.
- Baut Sachverhalt, Beweismatrix, Anlagenverzeichnis und Strafantragsfristen auf.
- Erzeugt erst am Ende einen Anzeigeentwurf, wenn die Tatsachenbasis trägt.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `akteneinsicht-verletzter-406e`, `beweismatrix-chatverlaeufe`, `datenstraftaten-diebstahl`, `sachbeschaedigung-sachverhalt`, `sachverhalt-ohne-adjektive`, `steuerhinterziehung-akteneinsicht` |
| 5. Verfahren, Behörde und Gericht | `antragsdelikte-strafantrag`, `international-klageerzwingung`, `klageerzwingung-172-stpo`, `opferschutz-nebenklage`, `strafantrag-form-frist`, `strafanzeige-vs-strafantrag-158` |
| 7. Kontrolle, Qualität und Gegenprüfung | `gegenanzeige-geldwaesche` |
| 8. Spezialmodule und Schnittstellen | `anfangsverdacht-anlagenverzeichnis`, `anlagenverzeichnis-hashlog`, `anwalt-arbeitsplatz`, `arbeitsplatz-sexuelle-belaestigung`, `bankrott-bedrohung`, `bedrohung-241`, `beleidigung-betrug`, `betrug-263`, `chatverlaeufe-emails-header`, `computerbetrug-phishing`, `diebstahl-unterschlagung`, `druckmittel-falsche`, `falsche-verdaechtigung-164`, `geldwaesche-261`, `geschgehg-haeusliche`, `haeusliche-gewalt-gewschg`, `hausfriedensbruch`, `insolvenzverschleppung-15a`, ... plus 24 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-verletzter-406e` | Wenn es um Akteneinsicht Verletzter Paragraf 406e StPO in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `anfangsverdacht-anlagenverzeichnis` | Wenn es um Anfangsverdacht nach Paragrafen 152. 160 StPO in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `anlagenverzeichnis-hashlog` | Wenn es um Anlagenverzeichnis und Hashlog in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `antragsdelikte-strafantrag` | Wenn es um Antragsdelikte und Drei-Monats-Frist in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anwalt-arbeitsplatz` | Wenn es um Wann zwingend Anwalt einschalten? in Strafanzeige-Vorbereiter geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `arbeitsplatz-sexuelle-belaestigung` | Wenn es um Arbeitsplatz: sexuelle Belästigung strafrechtlich einordnen in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `bankrott-bedrohung` | Wenn es um Bankrott Paragraf 283 StGB in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bedrohung-241` | Wenn es um Bedrohung Paragraf 241 StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beleidigung-betrug` | Wenn es um Beleidigung Paragrafen 185. 194 StGB in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `betrug-263` | Wenn es um Betrug Paragraf 263 StGB in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `beweismatrix-chatverlaeufe` | Wenn es um Beweismatrix: Tatsache, Meinung, Vermutung in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `chatverlaeufe-emails-header` | Wenn es um Chats, E-Mails und Header sichern in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `computerbetrug-phishing` | Wenn es um Computerbetrug und Phishing in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `datenstraftaten-diebstahl` | Wenn es um Datenstraftaten Paragrafen 202a, 303a StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `diebstahl-unterschlagung` | Wenn es um Diebstahl und Unterschlagung in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `druckmittel-falsche` | Wenn es um Anzeige als Druckmittel vermeiden in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `falsche-verdaechtigung-164` | Wenn es um Falsche Verdächtigung Paragraf 164 StGB in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `gegenanzeige-geldwaesche` | Wenn es um Gegenanzeige-Risiko in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `geldwaesche-261` | Wenn es um Geldwäsche Paragraf 261 StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geschgehg-haeusliche` | Wenn es um GeschGehG Paragraf 23 Strafanzeige in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `haeusliche-gewalt-gewschg` | Wenn es um Häusliche Gewalt und GewSchG in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `hausfriedensbruch` | Wenn es um Hausfriedensbruch Paragraf 123 StGB in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `insolvenzverschleppung-15a` | Wenn es um Insolvenzverschleppung Paragraf 15a InsO in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `international-klageerzwingung` | Wenn es um Internationale Anzeigen und EU-Bezug in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kaltstart-routing` | Wenn es um Strafanzeige: Kaltstart mit Sicherheitsbremse in Strafanzeige-Vorbereiter geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| `klageerzwingung-172-stpo` | Wenn es um Klageerzwingung Paragraf 172 StPO in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `koerperverletzung-korruption` | Wenn es um Körperverletzung Paragrafen 223. 230 StGB in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `korruption-299-331ff` | Wenn es um Korruption Paragrafen 299. 331 ff. StGB in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kreditgefaehrdung-minderjaehrige` | Wenn es um Kreditgefährdung Paragraf 824 BGB in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `minderjaehrige-schule` | Wenn es um Minderjährige, Schule und Jugendamt in Strafanzeige-Vorbereiter geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `muster-noetigung` | Wenn es um Muster-Strafanzeige Generator in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `nicht-anzeigen-redteam` | Wenn es um Nicht anzeigen? Red-Team vor Strafanzeige in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `noetigung-240` | Wenn es um Nötigung Paragraf 240 StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notruf-online` | Wenn es um Akute Gefahr: Notruf statt Plugin in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `online-plattform-screenshots` | Wenn es um Online-Beweise und Plattform-Screenshots in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `onlinewache-opferschutz` | Wenn es um Onlinewache oder Staatsanwaltschaft? in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `opferschutz-nebenklage` | Wenn es um Opferschutz, Nebenklage, Adhäsion in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `rechtsfolgen-ruecknahme` | Wenn es um Rechtsfolgen und Zivilstrategie in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| `ruecknahme-einstellung-170-153` | Wenn es um Rücknahme, Einstellung, Paragraf 170 Abs. 2, Paragrafen 153 ff. StPO in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, B... |
| `sachbeschaedigung-sachverhalt` | Wenn es um Sachbeschädigung Paragraf 303 StGB in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `sachverhalt-ohne-adjektive` | Wenn es um Sachverhalt ohne Adjektive in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stalking-vs-kontaktkonflikt` | Wenn es um Stalking Paragraf 238 StGB in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `steuerhinterziehung-akteneinsicht` | Wenn es um Steuerhinterziehung Paragraf 370 AO in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `strafantrag-form-frist` | Wenn es um Strafantrag Form, Frist, Rücknahme in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strafanzeige-vs-strafantrag-158` | Wenn es um Strafanzeige vs. Strafantrag Paragraf 158 StPO in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| `tierschutz-ueblerede` | Wenn es um Tierschutzstrafrecht Paragraf 17 TierSchG in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `ueblerede-verleumdung-186-187` | Wenn es um Üble Nachrede und Verleumdung vermeiden in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umweltstraftaten-unternehmen` | Wenn es um Umweltstraftaten Paragrafen 324 ff. StGB in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `unternehmen-internal-investigation` | Wenn es um Unternehmen und Internal Investigation in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `untreue-urheberrecht` | Wenn es um Untreue Paragraf 266 StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `urheberrecht-markenrecht` | Wenn es um IP-Strafanzeige Urheber/Marke/Design in Strafanzeige-Vorbereiter geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `verkehrsunfall-video` | Wenn es um Unfallflucht Paragraf 142 StGB in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `video-audio-kug-201` | Wenn es um Video, Audio, KUG und Paragraf 201 StGB in Strafanzeige-Vorbereiter geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `wer-zeugenliste` | Wenn es um Sachverhalt: wer, was, wann, wo, wie in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `whistleblower-computerbetrug` | Wenn es um Hinweisgeber und Strafanzeige in Strafanzeige-Vorbereiter geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugenliste-kontakt` | Wenn es um Zeugenliste und Kontaktregeln in Strafanzeige-Vorbereiter geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

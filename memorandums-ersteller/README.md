# Memorandums-Ersteller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`memorandums-ersteller`) | [`memorandums-ersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Grenzüberschreitender Asset-Deal Volkenrath Energie SE / Pipeline Northsea Ltd.** (`memorandum-grenzueberschreitender-asset-deal-volkenrath-energie`) | [Gesamt-PDF lesen](../testakten/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie/gesamt-pdf/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie_gesamt.pdf) | [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`memorandums-ersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/memorandums-ersteller/memorandums-ersteller-werkstatt.md" download><code>memorandums-ersteller-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/memorandums-ersteller/memorandums-ersteller-schnellstart.md" download><code>memorandums-ersteller-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Grenzüberschreitender Asset-Deal Volkenrath Energie SE / Pipeline Northsea Ltd.: [Gesamt-PDF](../testakten/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie/gesamt-pdf/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie_gesamt.pdf), [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip), [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `memorandums-ersteller` | Erzeugt aus heterogenen Mandantenunterlagen ein professionelles juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit lückenloser Quellenreferenzierung; Fragestellung als Ein-Satz-Fragen; Antworten als … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `start-chronologie-fristen`, `wandelt-erstpruefung-und-mandatsziel`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `ausfuehrungen-formular-portal-und-einreichung`, `fragen-compliance-dokumentation-und-akte`, `gliederung-mandantenunterlagen-memorandum`, `mandantenunterlagen-tatbestand-beweis-und-belege`, `memo-pruefung-im-gutachtenstil`, `memo-quellen-zitierregel`, `memorandum-dokumentenmatrix-und-lueckenliste`, `optional-beweislast-piercing-sonderfall`, `prozessstrategie-klageerhebung-gutachtenstil`, `quellen-livecheck`, `quellenreferenz-quellenkarte`, `rechtsgebietsneutral-sachverhalt-satz`, `sachverhalt-fixieren-vier-teile`, `sachverhalt-verhandlung-vergleich-und-eskalation`, `spezial-quellenreferenz-livequellen-und-rechtsprechungscheck`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `haftungsrisiko-rechtsanwalt-board-pack`, `vier-risikoampel-und-gegenargumente`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `memo-compliance-vorfall-intern`, `memo-zur-vertragsentscheidung` |
| 5. Verfahren, Behörde und Gericht | `juristisches-questions-fristennotiz`, `memo-fristen-sofortmassnahmen`, `questions-fristennotiz-und-naechster-schritt` |
| 6. Ergebnis, Schreiben und Kommunikation | `antworten-interessen-ausfuehrungen-fragen`, `mandantenkommunikation-redteam`, `memo-board-pack-besondere-anlaesse-spezial`, `memo-ergebnis-handlungsempfehlung`, `memo-fuer-mandant-vs-intern`, `memo-mandantenfreundliche-fassung-spezial`, `memo-memo-typenuebersicht-bauleiter`, `memo-rechtsfragen-formulieren`, `memo-research-tracking-leitfaden`, `memo-vier-teile-aufbau`, `memo-zu-grenzueberschreitenden-faellen`, `memo-zur-rechtsmittelentscheidung`, `memorandums-ersteller`, `output-waehlen`, `zitierung-mandantenkommunikation-entscheidungsvorlage` |
| 7. Kontrolle, Qualität und Gegenprüfung | `pinpoint-fehlerkatalog`, `spezial-pinpoint-red-team-und-qualitaetskontrolle`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `due-diligence-ergebnis-handlungsempfehlung`, `laenge-formate-mandantenfreundliche-fassung`, `mandantenanfrage-schnell`, `piercing-sonderfall-und-edge-case`, `rechtliche-internationaler-bezug-und-schnittstellen`, `rechtsfortbildung-bgh-rechtsfragen`, `satz-zahlen-schwellen-und-berechnung`, `teile-vier-wandelt` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Memorandums-Ersteller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `antworten-interessen-ausfuehrungen-fragen` | Wenn es um Antworten: Mehrparteienkonflikt und Interessenmatrix in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| `ausfuehrungen-formular-portal-und-einreichung` | Wenn es um Ausfuehrungen: Formular, Portal und Einreichungslogik in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anla... |
| `dokumente-intake` | Wenn es um Dokumentenintake in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `due-diligence-ergebnis-handlungsempfehlung` | Wenn es um Due-Diligence-Rechtsmemo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Memorandums-Ersteller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fragen-compliance-dokumentation-und-akte` | Wenn es um Fragen: Compliance-Dokumentation und Aktenvermerk in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| `gliederung-mandantenunterlagen-memorandum` | Wenn es um Gliederung: Schriftsatz-, Brief- und Memo-Bausteine in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| `haftungsrisiko-rechtsanwalt-board-pack` | Wenn es um Haftungsrisiko-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `juristisches-questions-fristennotiz` | Wenn es um Juristisches: Fristen, Form, Zuständigkeit und Rechtsweg in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `laenge-formate-mandantenfreundliche-fassung` | Wenn es um Memo: Laenge und Formate in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mandantenanfrage-schnell` | Wenn es um Schnell-Memo Mandantenanfrage in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mandantenkommunikation-redteam` | Wenn es um Mandantenkommunikation in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `mandantenunterlagen-tatbestand-beweis-und-belege` | Wenn es um Mandantenunterlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begr... |
| `memo-board-pack-besondere-anlaesse-spezial` | Wenn es um Memo: Board-Pack Anlaesse in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `memo-compliance-vorfall-intern` | Wenn es um Compliance-Vorfall-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-ergebnis-handlungsempfehlung` | Wenn es um Memo: Ergebnis + Handlungsempfehlung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-fristen-sofortmassnahmen` | Wenn es um Memo: Fristen und Sofortmassnahmen in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `memo-fuer-mandant-vs-intern` | Wenn es um Mandantenmemo vs. internes Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-mandantenfreundliche-fassung-spezial` | Wenn es um Memo: Mandantenfreundliche Fassung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `memo-memo-typenuebersicht-bauleiter` | Wenn es um Memo: Typen-Übersicht in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-pruefung-im-gutachtenstil` | Wenn es um Memo: Prüfung im Gutachtenstil in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-quellen-zitierregel` | Wenn es um Memo: Quellen-Zitierregel in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-rechtsfragen-formulieren` | Wenn es um Memo: Rechtsfragen formulieren in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-research-tracking-leitfaden` | Wenn es um Memo: Research-Tracking in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-vier-teile-aufbau` | Wenn es um Memo: Vier-Teile-Aufbau in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-zu-grenzueberschreitenden-faellen` | Wenn es um Grenzueberschreitender-Fall-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-zur-rechtsmittelentscheidung` | Wenn es um Rechtsmittel-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memo-zur-vertragsentscheidung` | Wenn es um Vertragsentscheidungs-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `memorandum-dokumentenmatrix-und-lueckenliste` | Wenn es um Memorandum: Dokumentenmatrix, Lückenliste und Nachforderung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| `memorandums-ersteller` | Wenn es um Memorandums-Ersteller in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `optional-beweislast-piercing-sonderfall` | Wenn es um Optional: Beweislast, Darlegungslast und Substantiierung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| `output-waehlen` | Wenn es um Output wählen in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `piercing-sonderfall-und-edge-case` | Wenn es um Piercing: Sonderfall und Edge-Case-Prüfung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `pinpoint-fehlerkatalog` | Wenn es um Pinpoint Fehlerkatalog in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `prozessstrategie-klageerhebung-gutachtenstil` | Wenn es um Prozessstrategie-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `quellenreferenz-quellenkarte` | Wenn es um Quellenreferenz Quellenkarte in Memorandums-Ersteller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `questions-fristennotiz-und-naechster-schritt` | Wenn es um Questions: Fristennotiz und nächster Schritt in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtliche-internationaler-bezug-und-schnittstellen` | Wenn es um Rechtliche: Internationaler Bezug und Schnittstellen in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| `rechtsfortbildung-bgh-rechtsfragen` | Wenn es um BGH-Update-Memo in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `rechtsgebietsneutral-sachverhalt-satz` | Wenn es um Rechtsgebietsneutral: Abschlussprodukt und Übergabe in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| `sachverhalt-fixieren-vier-teile` | Wenn es um Memo: Sachverhalt fixieren in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `sachverhalt-verhandlung-vergleich-und-eskalation` | Wenn es um Sachverhalt: Verhandlung, Vergleich und Eskalation in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| `satz-zahlen-schwellen-und-berechnung` | Wenn es um Satz: Zahlen, Schwellenwerte und Berechnung in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `spezial-pinpoint-red-team-und-qualitaetskontrolle` | Wenn es um Pinpoint: Red-Team und Qualitätskontrolle in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-quellenreferenz-livequellen-und-rechtsprechungscheck` | Wenn es um Quellenreferenz: Livequellen- und Rechtsprechungscheck in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anl... |
| `start-chronologie-fristen` | Wenn es um Memorandums Ersteller — Allgemein in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `teile-vier-wandelt` | Wenn es um Teile: Behörden-, Gerichts- oder Registerweg in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vier-risikoampel-und-gegenargumente` | Wenn es um Vier: Risikoampel, Gegenargumente und Verteidigungslinien in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wandelt-erstpruefung-und-mandatsziel` | Wenn es um Wandelt: Erstprüfung, Rollenklärung und Mandatsziel in Memorandums-Ersteller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Memorandums-Ersteller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zitierung-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Zitierung: Mandantenkommunikation und Entscheidungsvorlage in Memorandums-Ersteller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

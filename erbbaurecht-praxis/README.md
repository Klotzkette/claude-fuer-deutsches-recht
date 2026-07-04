# Erbbaurecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`erbbaurecht-praxis`) | [`erbbaurecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/erbbaurecht-praxis.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Lindenwerder Erbbaurecht - Erbbauzins, Heimfall und Kita-Finanzierung** (`erbbaurecht-erbbauzins-heimfall-lindenwerder-2026`) | [Gesamt-PDF lesen](../testakten/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026/gesamt-pdf/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026_gesamt.pdf) | [`testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Praxisplugin für Erbbaurecht und Erbbaugrundbuch: Erbbaurechtsvertrag, Erbbauzins, Wertsicherung, Heimfall, Zustimmung, Belastung, Finanzierung, Veräußerung, Laufzeit, Entschädigung, Zwangsversteigerung, Rang und Grundbuchvollzug.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`erbbaurecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/erbbaurecht-praxis.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/erbbaurecht-praxis/erbbaurecht-praxis-werkstatt.md" download><code>erbbaurecht-praxis-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/erbbaurecht-praxis/erbbaurecht-praxis-schnellstart.md" download><code>erbbaurecht-praxis-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Lindenwerder Erbbaurecht - Erbbauzins, Heimfall und Kita-Finanzierung: [Gesamt-PDF](../testakten/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026/gesamt-pdf/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026_gesamt.pdf), [`testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip), [`testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Ein Spezialplugin für das Recht des Erbbaurechts: vom ersten Vertragsentwurf über Erbbauzins und Heimfall bis zu Finanzierung, Zustimmung, Versteigerung und Erbbaugrundbuch. Es erklärt die Sache auch für Menschen, die sonst nur Eigentum oder Miete kennen.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `erbbaurecht-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- ErbbauRG
- GBO
- GBV
- BGB Sachenrecht
- FamFG

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `ablauf-laufzeitende-erbbaurecht-aktenstruktur`, `erbbaurecht-aktenstruktur` |
| 4. Gestaltung, Strategie und Verhandlung | `erbbaurecht-indexklausel-inflation`, `erbbaurechtsvertrag-pflichtinhalt`, `erbbauzins-struktur-erbbauzinsanpassung`, `heimfall-gruende-indexklausel-inflation`, `verkauf-spa-erbbaurechtsvertrag-pflichtinhalt` |
| 5. Verfahren, Behörde und Gericht | `erbbaurecht-fristen-und-reminder`, `erbbaurecht-schieds-und-gerichtsstand`, `erbbaurecht-vorlage-zustimmungsantrag`, `kommunale-beschlussvorlage-erbbaurecht`, `rueckbau-am-schieds-gerichtsstand` |
| 6. Ergebnis, Schreiben und Kommunikation | `erbbaurecht-mandantenbrief` |
| 7. Kontrolle, Qualität und Gegenprüfung | `erbbaurecht-qualitygate-vertrag` |
| 8. Spezialmodule und Schnittstellen | `altlasten-rueckbau-erbbaurecht`, `change-control-dingliche-vorkaufsrechte`, `entschaedigung-bei-heimfall-und-ablauf`, `erbbau-beschwerde-erbbaugrundbuch-lesen`, `erbbaugrundbuch-lesen`, `erbbaurecht-betreiberwechsel`, `erbbaurecht-dingliche-vorkaufsrechte`, `erbbaurecht-gewerbepark`, `erbbaurecht-investoren-q-and-a`, `erbbaurecht-kita-sozialimmobilie`, `erbbaurecht-notar-und-grundbuchkosten`, `erbbaurecht-photovoltaik-untererbbaurecht`, `erbbaurecht-rangruecktritt-bank`, `erbbaurecht-teilerbbaurecht-und-aufteilung`, `erbbaurecht-untererbbaurecht-und-weitergabe`, `erbbauzins-rueckstand-mahnung`, `erbbauzinsanpassung-paragraph-9a`, `erbbauzinsrang-finanzierungsbank-erbbaurecht`, ... plus 17 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ablauf-laufzeitende-erbbaurecht-aktenstruktur` | Wenn es um Laufzeitende und Exitplan in Erbbaurecht Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `altlasten-rueckbau-erbbaurecht` | Wenn es um Altlasten und Rückbau in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `change-control-dingliche-vorkaufsrechte` | Wenn es um Change of Control beim Erbbauberechtigten in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `entschaedigung-bei-heimfall-und-ablauf` | Wenn es um Entschädigung in Erbbaurecht Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `erbbau-beschwerde-erbbaugrundbuch-lesen` | Wenn es um Grundbuchstreit im Erbbaurecht in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaugrundbuch-lesen` | Wenn es um Erbbaugrundbuch lesen in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-aktenstruktur` | Wenn es um Erbbauakte strukturieren in Erbbaurecht Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erbbaurecht-betreiberwechsel` | Wenn es um Betreiberwechsel in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-dingliche-vorkaufsrechte` | Wenn es um Vorkaufsrechte im Erbbaurecht in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-fristen-und-reminder` | Wenn es um Fristen und Reminder in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-gewerbepark` | Wenn es um Gewerbliches Erbbaurecht in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-indexklausel-inflation` | Wenn es um Indexklausel und Inflation in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-investoren-q-and-a` | Wenn es um Investor Q&A in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-kita-sozialimmobilie` | Wenn es um Sozialimmobilie/Kita in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-mandantenbrief` | Wenn es um Mandantenbrief Erbbaurecht in Erbbaurecht Praxis geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `erbbaurecht-notar-und-grundbuchkosten` | Wenn es um Notar-, Grundbuch- und Transaktionskosten in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `erbbaurecht-photovoltaik-untererbbaurecht` | Wenn es um PV, Wärmepumpe, Ladepunkte in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-qualitygate-vertrag` | Wenn es um Quality Gate Vertrag in Erbbaurecht Praxis geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-rangruecktritt-bank` | Wenn es um Rangrücktritt zugunsten Bank in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-schieds-und-gerichtsstand` | Wenn es um Streitbeilegung in Erbbaurecht Praxis geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `erbbaurecht-teilerbbaurecht-und-aufteilung` | Wenn es um Teil-Erbbaurecht und Aufteilung in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erbbaurecht-untererbbaurecht-und-weitergabe` | Wenn es um Untererbbaurecht und Weitergabe in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbaurecht-vorlage-zustimmungsantrag` | Wenn es um Zustimmungsantrag in Erbbaurecht Praxis geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `erbbaurechtsvertrag-pflichtinhalt` | Wenn es um Erbbaurechtsvertrag entwerfen in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erbbauzins-rueckstand-mahnung` | Wenn es um Erbbauzinsrückstand in Erbbaurecht Praxis geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `erbbauzins-struktur-erbbauzinsanpassung` | Wenn es um Erbbauzins und Reallast in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erbbauzinsanpassung-paragraph-9a` | Wenn es um Erbbauzinsanpassung in Erbbaurecht Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erbbauzinsrang-finanzierungsbank-erbbaurecht` | Wenn es um Erbbauzinsrang vor Finanzierungsbank in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `finanzierung-bankfaehigkeit-gemeinde-kirche` | Wenn es um Finanzierung des Erbbaurechts in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinde-kirche-stiftung-als-eigentuemer` | Wenn es um Gemeinde/Kirche/Stiftung als Grundstückseigentümer in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heimfall-gruende-indexklausel-inflation` | Wenn es um Heimfall prüfen in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heimfall-verteidigung-insolvenz` | Wenn es um Heimfall abwehren in Erbbaurecht Praxis geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `insolvenz-erbbauberechtigter` | Wenn es um Insolvenz des Erbbauberechtigten in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `instandhaltung-versicherung-investoren-q` | Wenn es um Instandhaltung, Versicherung und Betriebspflichten in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Na... |
| `kaltstart-routing` | Wenn es um Kaltstart Erbbaurecht in Erbbaurecht Praxis geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kauf-due-kita-sozialimmobilie` | Wenn es um Erbbaurecht kaufen in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunale-beschlussvorlage-erbbaurecht` | Wenn es um Kommunale Beschlussvorlage in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `laufzeit-verlaengerung-wohnungs-weg` | Wenn es um Laufzeit und Verlängerung in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nachhaltigkeit-baupflicht-notar` | Wenn es um Baupflicht und Nachhaltigkeit in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nutzungszweckwechsel-wohnen-rangruecktritt` | Wenn es um Nutzungszweckwechsel Wohnen/Gewerbe/Sozialimmobilie in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `rechtsprechung-live-erbbaurecht-reminder` | Wenn es um Rechtsprechung live verifizieren in Erbbaurecht Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `rueckbau-am-schieds-gerichtsstand` | Wenn es um Rückbau am Laufzeitende in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sicherheiten-buergschaft-teilerbbaurecht` | Wenn es um Sicherheiten für Erbbauzins und Rückbau in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `steuern-grunderwerbsteuer-entschaedigung` | Wenn es um Steuerliche Schnittstellen in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verjaehrung-verwirkung-vorlage` | Wenn es um Verjährung, Verwirkung und Duldung in Erbbaurecht Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `verkauf-spa-erbbaurechtsvertrag-pflichtinhalt` | Wenn es um Verkaufsklauseln in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vs-eigentum-erbbauzins-rueckstand` | Wenn es um Erbbaurecht verständlich erklären in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wohnungs-erbbaurecht-und-weg` | Wenn es um Wohnungserbbaurecht in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zustimmung-veraeusserung-zwangsversteigerung` | Wenn es um Zustimmung zur Veräußerung/Belastung in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zwangsversteigerung-erbbaurecht` | Wenn es um Zwangsversteigerung in Erbbaurecht Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

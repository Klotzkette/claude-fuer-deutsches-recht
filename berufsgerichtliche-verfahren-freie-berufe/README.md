# Berufsgerichtliche Verfahren Freie Berufe

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsgerichtliche-verfahren-freie-berufe`) | [`berufsgerichtliche-verfahren-freie-berufe.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsgerichtliche-verfahren-freie-berufe.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`berufsgerichtliche-verfahren-freie-berufe.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsgerichtliche-verfahren-freie-berufe.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berufsgerichtliche-verfahren-freie-berufe/berufsgerichtliche-verfahren-freie-berufe-werkstatt.md" download><code>berufsgerichtliche-verfahren-freie-berufe-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berufsgerichtliche-verfahren-freie-berufe/berufsgerichtliche-verfahren-freie-berufe-schnellstart.md" download><code>berufsgerichtliche-verfahren-freie-berufe-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## Installation

ZIP aus dem aktuellen Release laden und in Plugin-Umgebung oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `berufsgericht-freie-berufe-kaltstart-routing`, `mandatskuendigung-zur-unzeit-praevention`, `mandatskuendigung-zur-unzeit-verteidigung`, `sanktionen-mandatsannahme`, `sanktionen-mandatsannahme-verteidigung` |
| 2. Unterlagen, Sachverhalt und Quellen | `aktenherausgabe-zurueckbehaltungsrecht-praevention`, `aktenherausgabe-zurueckbehaltungsrecht-verteidigung`, `berufsgericht-beweisaufnahme`, `berufsgericht-beweisaufnahme-verteidigung`, `berufsgericht-freie-berufe-dokumente-aktenlog`, `berufsgericht-freie-berufe-quellen-rspr-fristen`, `datenpanne-berufstraeger-praevention`, `datenpanne-berufstraeger-verteidigung`, `fremdgeld-anderkonto-pflicht-praevention`, `fremdgeld-anderkonto-pflicht-verteidigung`, `notar-anderkonto-auszahlungsreife`, `notar-anderkonto-auszahlungsreife-verteidigung`, `steuerberater-unterlagenherausgabe-praevention`, `steuerberater-unterlagenherausgabe-verteidigung` |
| 3. Prüfung, Anspruch und Subsumtion | `werbung-robe-wirtschaftspruefer`, `wirtschaftspruefer-berufsaufsicht-wpo`, `wirtschaftspruefer-qualitaetskontrolle-praevention`, `wirtschaftspruefer-qualitaetskontrolle-verteidigung`, `wirtschaftspruefer-testat-widerruf`, `wirtschaftspruefer-testat-widerruf-praevention`, `wirtschaftspruefer-unabhaengigkeit-praevention`, `wirtschaftspruefer-unabhaengigkeit-verteidigung` |
| 4. Gestaltung, Strategie und Verhandlung | `berufsgesellschaft-compliance-praevention`, `berufsgesellschaft-compliance-verteidigung`, `vergleich-mit-kammer-praevention`, `vergleich-mit-kammer-verteidigung` |
| 5. Verfahren, Behörde und Gericht | `anwaltsgericht-brao-ueberblick`, `bea-nicht-berufsgericht`, `berufsgericht-anschuldigungsschrift-praevention`, `berufsgericht-anschuldigungsschrift-verteidigung`, `frist-und-zustaendigkeit-cockpit`, `haftpflichtdeckung-berufsverfahren-praevention`, `haftpflichtdeckung-berufsverfahren-verteidigung`, `kammeranhoerung-fristverlaengerung`, `kammeranhoerung-fristverlaengerung-verteidigung`, `patentanwalt-berufsgericht-pao`, `patentanwalt-fristenversaeumnis-epo-dpma-praevention`, `patentanwalt-fristenversaeumnis-epo-dpma-verteidigung`, `rechtsmittel-berufsgericht-praevention`, `rechtsmittel-berufsgericht-verteidigung`, `schriftsatz-vermerk-und-mustertext`, `steuerberater-berufsgericht-stberg` |
| 6. Ergebnis, Schreiben und Kommunikation | `mandanten-beteiligtenkommunikation-notar`, `robe-werbung-vermerk-mustertext-sitzungs`, `steuerberater-153-ao-berichtigung-praevention`, `steuerberater-153-ao-berichtigung-verteidigung` |
| 7. Kontrolle, Qualität und Gegenprüfung | `notar-gesellschafterliste-fehler-praevention`, `notar-gesellschafterliste-fehler-verteidigung`, `red-team-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `bea-nicht-in-betrieb-verteidigung`, `bea-nutzungspflichten-kanzleisitz`, `berufspflicht-und-verhaeltnismaessigkeit-verteidigung`, `berufspflicht-verhaeltnismaessigkeit`, `berufsrecht-ki-nutzung-praevention`, `berufsrecht-ki-nutzung-verteidigung`, `berufsverbot-sofortvollzug-verteidigung`, `berufsverbot-und-sofortvollzug-verteidigung`, `dienstaufsicht-notar-beschwerde-praevention`, `dienstaufsicht-notar-beschwerde-verteidigung`, `entscheidungsvorlage`, `geldwaeschepflicht-kanzlei`, `geldwaeschepflicht-kanzlei-verteidigung`, `honorarvereinbarung-erfolgshonorar-praevention`, `honorarvereinbarung-erfolgshonorar-verteidigung`, `interessenkollision-mehrfachvertretung`, `interessenkollision-mehrfachvertretung-verteidigung`, `kanzleisitz-und-erreichbarkeit-praevention`, ... plus 27 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 99 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenherausgabe-zurueckbehaltungsrecht-praevention` | Wenn es um Aktenherausgabe und Zurückbehaltungsrecht: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risik... |
| `aktenherausgabe-zurueckbehaltungsrecht-verteidigung` | Wenn es um Aktenherausgabe und Zurückbehaltungsrecht: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoam... |
| `anwaltsgericht-brao-ueberblick` | Wenn es um Anwaltsgericht nach BRAO Überblick in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bea-nicht-berufsgericht` | Wenn es um beA nicht in Betrieb: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| `bea-nicht-in-betrieb-verteidigung` | Wenn es um beA nicht in Betrieb: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bea-nutzungspflichten-kanzleisitz` | Wenn es um beA und elektronische Kommunikation in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `berufsgericht-anschuldigungsschrift-praevention` | Wenn es um Berufsgericht Anschuldigungsschrift: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsm... |
| `berufsgericht-anschuldigungsschrift-verteidigung` | Wenn es um Berufsgericht Anschuldigungsschrift: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `berufsgericht-beweisaufnahme` | Wenn es um Berufsgericht Beweisaufnahme: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `berufsgericht-beweisaufnahme-verteidigung` | Wenn es um Berufsgericht Beweisaufnahme: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `berufsgericht-freie-berufe-dokumente-aktenlog` | Wenn es um Dokumentenintake und Aktenlog in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `berufsgericht-freie-berufe-kaltstart-routing` | Wenn es um Allgemeiner Kaltstart und Routing in Berufsgerichtliche Verfahren Freie Berufe geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `berufsgericht-freie-berufe-quellen-rspr-fristen` | Wenn es um Quellen- und Rechtsprechungscheck in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `berufsgesellschaft-compliance-praevention` | Wenn es um Berufsgesellschaft Compliance: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |
| `berufsgesellschaft-compliance-verteidigung` | Wenn es um Berufsgesellschaft Compliance: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zustä... |
| `berufspflicht-und-verhaeltnismaessigkeit-verteidigung` | Wenn es um Berufspflicht und Verhältnismäßigkeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions... |
| `berufspflicht-verhaeltnismaessigkeit` | Wenn es um Berufspflicht und Verhältnismäßigkeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisi... |
| `berufsrecht-ki-nutzung-praevention` | Wenn es um Berufsrecht digitale Werkzeuge-Nutzung: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit... |
| `berufsrecht-ki-nutzung-verteidigung` | Wenn es um Berufsrecht digitale Werkzeuge-Nutzung: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fe... |
| `berufsverbot-sofortvollzug-verteidigung` | Wenn es um Berufsverbot und Sofortvollzug: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Z... |
| `berufsverbot-und-sofortvollzug-verteidigung` | Wenn es um Berufsverbot und Sofortvollzug: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zust... |
| `datenpanne-berufstraeger-praevention` | Wenn es um Datenpanne beim Berufsträger: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit... |
| `datenpanne-berufstraeger-verteidigung` | Wenn es um Datenpanne beim Berufsträger: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Opt... |
| `dienstaufsicht-notar-beschwerde-praevention` | Wenn es um Dienstaufsicht Notar Beschwerde: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `dienstaufsicht-notar-beschwerde-verteidigung` | Wenn es um Dienstaufsicht Notar Beschwerde: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zus... |
| `entscheidungsvorlage` | Wenn es um Entscheidungsvorlage in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `fremdgeld-anderkonto-pflicht-praevention` | Wenn es um Fremdgeld und Anderkonto: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständ... |
| `fremdgeld-anderkonto-pflicht-verteidigung` | Wenn es um Fremdgeld und Anderkonto: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigk... |
| `frist-und-zustaendigkeit-cockpit` | Wenn es um Fristen- und Zuständigkeitscockpit in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geldwaeschepflicht-kanzlei` | Wenn es um Geldwäschepflichten der Kanzlei: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `geldwaeschepflicht-kanzlei-verteidigung` | Wenn es um Geldwäschepflichten der Kanzlei: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zus... |
| `haftpflichtdeckung-berufsverfahren-praevention` | Wenn es um Haftpflichtdeckung im Berufsverfahren: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisi... |
| `haftpflichtdeckung-berufsverfahren-verteidigung` | Wenn es um Haftpflichtdeckung im Berufsverfahren: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions... |
| `honorarvereinbarung-erfolgshonorar-praevention` | Wenn es um Honorarvereinbarung und Erfolgshonorar: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollis... |
| `honorarvereinbarung-erfolgshonorar-verteidigung` | Wenn es um Honorarvereinbarung und Erfolgshonorar: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollision... |
| `interessenkollision-mehrfachvertretung` | Wenn es um Interessenkollision Mehrfachvertretung: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollis... |
| `interessenkollision-mehrfachvertretung-verteidigung` | Wenn es um Interessenkollision Mehrfachvertretung: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollision... |
| `kammeranhoerung-fristverlaengerung` | Wenn es um Kammeranhörung Fristverlängerung: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mi... |
| `kammeranhoerung-fristverlaengerung-verteidigung` | Wenn es um Kammeranhörung Fristverlängerung: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit S... |
| `kanzleisitz-und-erreichbarkeit-praevention` | Wenn es um Kanzleisitz und Erreichbarkeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf... |
| `kanzleisitz-und-erreichbarkeit-verteidigung` | Wenn es um Kanzleisitz und Erreichbarkeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mi... |
| `kanzleisitz-und-zustellbarkeit` | Wenn es um Kanzleisitz und Zustellbarkeit in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `kollegenbeleidigung-strafbarkeit` | Wenn es um Kollegenbeleidigung und Strafbarkeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisio... |
| `kollegenbeleidigung-und-strafbarkeit-verteidigung` | Wenn es um Kollegenbeleidigung und Strafbarkeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-... |
| `kollegenbeleidigung-unsachlichkeit` | Wenn es um Kollegenbeleidigung und Unsachlichkeit in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandanten-beteiligtenkommunikation-notar` | Wenn es um Beteiligtenkommunikation in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `mandatskuendigung-zur-unzeit-praevention` | Wenn es um Mandatskündigung zur Unzeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| `mandatskuendigung-zur-unzeit-verteidigung` | Wenn es um Mandatskündigung zur Unzeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| `notar-anderkonto-auszahlungsreife` | Wenn es um Notaranderkonto Auszahlungsreife: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `notar-anderkonto-auszahlungsreife-verteidigung` | Wenn es um Notaranderkonto Auszahlungsreife: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |
| `notar-disziplinar-bnoto` | Wenn es um Notar Disziplinarverfahren BNotO in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notar-geldwaesche-immobilie-praevention` | Wenn es um Notar Geldwäsche Immobilie: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zustä... |
| `notar-geldwaesche-immobilie-verteidigung` | Wenn es um Notar Geldwäsche Immobilie: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständi... |
| `notar-gesellschafterliste-fehler-praevention` | Wenn es um Notar Gesellschafterliste Fehler: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal-... |
| `notar-gesellschafterliste-fehler-verteidigung` | Wenn es um Notar Gesellschafterliste Fehler: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- un... |
| `notar-unparteilichkeit-familiengesellschaft-praevention` | Wenn es um Notar Unparteilichkeit Familiengesellschaft: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit K... |
| `notar-unparteilichkeit-familiengesellschaft-verteidigung` | Wenn es um Notar Unparteilichkeit Familiengesellschaft: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Koll... |
| `patentanwalt-berufsgericht-pao` | Wenn es um Patentanwalt Berufsgericht PAO in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `patentanwalt-erfinderkonflikt-praevention` | Wenn es um Patentanwalt Erfinderkonflikt: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |
| `patentanwalt-erfinderkonflikt-verteidigung` | Wenn es um Patentanwalt Erfinderkonflikt: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zustä... |
| `patentanwalt-fristenversaeumnis-epo-dpma-praevention` | Wenn es um Patentanwalt Fristenversäumnis DPMA/EPO: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoa... |
| `patentanwalt-fristenversaeumnis-epo-dpma-verteidigung` | Wenn es um Patentanwalt Fristenversäumnis DPMA/EPO: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampe... |
| `patentanwalt-vertretungsbefugnis-grenze-praevention` | Wenn es um Patentanwalt Vertretungsbefugnis Grenze: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kolli... |
| `patentanwalt-vertretungsbefugnis-grenze-verteidigung` | Wenn es um Patentanwalt Vertretungsbefugnis Grenze: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisio... |
| `protokoll-und-nachbereitung` | Wenn es um Protokoll und Nachbereitung in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rak-ruege-unsachlichkeit-praevention` | Wenn es um RAK-Rüge wegen Unsachlichkeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf... |
| `rak-ruege-unsachlichkeit-verteidigung` | Wenn es um RAK-Rüge wegen Unsachlichkeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit... |
| `rechtsmittel-berufsgericht-praevention` | Wenn es um Rechtsmittel im Berufsgericht: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoamp... |
| `rechtsmittel-berufsgericht-verteidigung` | Wenn es um Rechtsmittel im Berufsgericht: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel... |
| `red-team-qualitygate` | Wenn es um Red-Team-Qualitygate in Berufsgerichtliche Verfahren Freie Berufe geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `robe-werbung-vermerk-mustertext-sitzungs` | Wenn es um Robe, Werbung und Sachlichkeit in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `sanktionen-mandatsannahme` | Wenn es um Sanktionen und Mandatsannahme: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |
| `sanktionen-mandatsannahme-verteidigung` | Wenn es um Sanktionen und Mandatsannahme: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zustä... |
| `schriftsatz-vermerk-und-mustertext` | Wenn es um Schriftsatz, Vermerk und Mustertext in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und An... |
| `sitzungs-und-terminvorbereitung` | Wenn es um Sitzungs- und Terminvorbereitung in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `social-media-berufsrecht-praevention` | Wenn es um Social Media Berufsrecht: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständ... |
| `social-media-berufsrecht-verteidigung` | Wenn es um Social Media Berufsrecht: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigk... |
| `steuerberater-153-ao-berichtigung-praevention` | Wenn es um Steuerberater Paragraf 153 AO Berichtigung: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Ko... |
| `steuerberater-153-ao-berichtigung-verteidigung` | Wenn es um Steuerberater Paragraf 153 AO Berichtigung: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kolli... |
| `steuerberater-berufsgericht-stberg` | Wenn es um Steuerberater Berufsgericht StBerG in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `steuerberater-unterlagenherausgabe-praevention` | Wenn es um Steuerberater Unterlagenherausgabe: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderung... |
| `steuerberater-unterlagenherausgabe-verteidigung` | Wenn es um Steuerberater Unterlagenherausgabe: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsli... |
| `steuerberater-vorbehaltsaufgabe-kammer` | Wenn es um Steuerberater Vorbehaltsaufgabe: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf m... |
| `steuerberater-vorbehaltsaufgabe-praevention` | Wenn es um Steuerberater Vorbehaltsaufgabe: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwur... |
| `vergleich-mit-kammer-praevention` | Wenn es um Vergleich mit Kammer oder Aufsicht: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslini... |
| `vergleich-mit-kammer-verteidigung` | Wenn es um Vergleich mit Kammer oder Aufsicht: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie m... |
| `vermoegensverfall-zulassungswiderruf` | Wenn es um Vermögensverfall und Zulassungswiderruf: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisio... |
| `vermoegensverfall-zulassungswiderruf-praevention` | Wenn es um Vermögensverfall und Zulassungswiderruf: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kolli... |
| `verschwiegenheit-cloud-dienstleister-praevention` | Wenn es um Verschwiegenheit und Cloud-Dienstleister: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Koll... |
| `verschwiegenheit-cloud-dienstleister-verteidigung` | Wenn es um Verschwiegenheit und Cloud-Dienstleister: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisi... |
| `werbung-robe-kanzleimarketing-praevention` | Wenn es um Werbung, Robe und Kanzleimarketing: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions... |
| `werbung-robe-wirtschaftspruefer` | Wenn es um Werbung, Robe und Kanzleimarketing: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `wirtschaftspruefer-berufsaufsicht-wpo` | Wenn es um Wirtschaftspruefer Berufsaufsicht Wpo in Berufsgerichtliche Verfahren Freie Berufe geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wirtschaftspruefer-qualitaetskontrolle-praevention` | Wenn es um Wirtschaftsprüfer Qualitätskontrolle: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risik... |
| `wirtschaftspruefer-qualitaetskontrolle-verteidigung` | Wenn es um Wirtschaftsprüfer Qualitätskontrolle: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoam... |
| `wirtschaftspruefer-testat-widerruf` | Wenn es um Wirtschaftsprüfer Testat Widerruf: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Z... |
| `wirtschaftspruefer-testat-widerruf-praevention` | Wenn es um Wirtschaftsprüfer Testat Widerruf: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-... |
| `wirtschaftspruefer-unabhaengigkeit-praevention` | Wenn es um Wirtschaftsprüfer Unabhängigkeit: Präventions- und Organisationspaket in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `wirtschaftspruefer-unabhaengigkeit-verteidigung` | Wenn es um Wirtschaftsprüfer Unabhängigkeit: Verteidigungs- und Kammerantwort in Berufsgerichtliche Verfahren Freie Berufe geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Straßenverkehrsrecht StVO

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strassenverkehrsrecht-stvo`) | [`strassenverkehrsrecht-stvo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenverkehrsrecht-stvo.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **StVO-Akte Schulstraße/Lieferzone** (`strassenverkehrsrecht-stvo-schulstrasse-lieferzone`) | [Gesamt-PDF lesen](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf) | [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

StVO-/Straßenverkehrsrecht-Plugin für Verkehrsregeln, Zeichen, Anordnungen, Ausnahmegenehmigungen, Fahrerlaubnis, Bußgeld-Schnittstellen und Behördenpraxis.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strassenverkehrsrecht-stvo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenverkehrsrecht-stvo.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strassenverkehrsrecht-stvo/strassenverkehrsrecht-stvo-werkstatt.md" download><code>strassenverkehrsrecht-stvo-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strassenverkehrsrecht-stvo/strassenverkehrsrecht-stvo-schnellstart.md" download><code>strassenverkehrsrecht-stvo-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | StVO-Akte Schulstraße/Lieferzone: [Gesamt-PDF](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf), [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip), [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin erklärt und prüft das Verhalten im Straßenverkehr und die behördliche Verkehrssteuerung: StVO, StVG, FeV, Zeichen, Anordnungen, Sondernutzungsschnittstellen, Ausnahmegenehmigung und Rechtsschutz.

## Start

Beginne mit `strassenverkehrsrecht-stvo-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

## Arbeitsweise

- Es arbeitet mit Akten- und Fristenlogik statt mit Bauchgefühl.
- Es trennt Rechtsgrundlage, Verfahren, Beweis, Kosten, Kommunikation und Eskalation.
- Es soll Nutzer befähigen: verständliche Erklärung, präzise Rückfragen, dann belastbarer Entwurf.
- Rechtsprechung und Gesetzesstände werden nicht halluziniert, sondern als Live-Check über amtliche oder frei zugängliche Quellen markiert.

## Typische Outputs

- Kaltstart-Interview und Aktenlandkarte
- Behörden-, Gerichts- oder Gegneranschreiben
- Widerspruchs-/Klage-/Eilantragsbausteine
- Kosten-, Fristen- und Zuständigkeitsmatrix
- Dashboard/Tracker für laufende Vorgänge
- Kurzfassung für Mandant, Vorstand, Verband, Redaktion oder Bürgerin

## Quellenhygiene

Siehe [`references/QUELLEN.md`](./references/QUELLEN.md). Dieses Plugin gibt keine endgültige Rechtsberatung, sondern robuste Arbeitsfassungen, Prüfpfade und Dokumentationshilfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-stvo-fall`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `bewohnerparken-beweis-sichern`, `busspur-beweis-sichern`, `fahrradstrasse-beweis-sichern`, `haltverbot-beweis-sichern`, `ladezone-beweis-sichern`, `schulstrasse-beweis-sichern` |
| 3. Prüfung, Anspruch und Subsumtion | `bewohnerparken-risiko-erklaeren`, `busspur-behoerde-karte-bauen-risiko`, `busspur-risiko-erklaeren`, `fahrradstrasse-karte-risiko-erklaeren`, `fahrradstrasse-risiko-erklaeren`, `haltverbot-risiko-erklaeren`, `ladezone-karte-risiko-erklaeren`, `ladezone-risiko-erklaeren`, `lieferzone-risiko-ladezone-regel-zeichen`, `tempo-risiko-fahrradstrasse-regel` |
| 4. Gestaltung, Strategie und Verhandlung | `busspur-eilrechtsschutz-planen`, `fahrradstrasse-eilrechtsschutz-planen`, `ladezone-eilrechtsschutz-planen`, `lieferzone-eilrechtsschutz-planen`, `lieferzone-sichern-eilrechtsschutz-planen`, `schulstrasse-eilrechtsschutz-planen`, `tempo-30-eilrechtsschutz-planen`, `tempo-sichern-eilrechtsschutz-planen` |
| 5. Verfahren, Behörde und Gericht | `ausnahmegenehmigung-beantragen`, `bewohnerparken-antrag-schreiben`, `bewohnerparken-behoerde-anschreiben`, `bewohnerparken-eilrechtsschutz-behoerde`, `busspur-anordnung-antrag-schreiben`, `busspur-antrag-schreiben`, `fahrradstrasse-antrag-sichern`, `fahrradstrasse-behoerde-anschreiben`, `haltverbot-antrag-schreiben`, `haltverbot-behoerde-anschreiben`, `haltverbot-eilrechtsschutz-behoerde`, `ladezone-antrag-sichern-eilrechtsschutz`, `ladezone-behoerde-anschreiben`, `lieferzone-antrag-schreiben`, `lieferzone-behoerde-anschreiben`, `schulstrasse-anordnung-antrag-schreiben`, `schulstrasse-antrag-schreiben`, `schulstrasse-behoerde-karte`, ... plus 11 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `kommunikation-mit-strassenverkehrsbeho` |
| 8. Spezialmodule und Schnittstellen | `baustellenverkehrsrecht`, `bewohnerparken-anordnung-angreifen`, `bewohnerparken-bussgeld-abgrenzen`, `bewohnerparken-karte-bauen`, `bewohnerparken-regel-pruefen`, `bewohnerparken-zeichen-anordnung`, `blaulicht-und-sonderrechte`, `bussgeldschnittstelle-owig`, `busspur-bussgeld-bewohnerparken`, `busspur-karte-bauen`, `busspur-regel-pruefen`, `busspur-zeichen-auslegen`, `e-scooter-und-mikromobilitaet`, `eilrechtsschutz-verkehrszeichen`, `fahrerlaubnis-schnittstelle`, `fahrradstrasse-anordnung-angreifen`, `fahrradstrasse-bussgeld-abgrenzen`, `fahrradstrasse-regel-pruefen`, ... plus 43 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 117 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ausnahmegenehmigung-beantragen` | Wenn es um Ausnahmegenehmigung Beantragen in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baustellenverkehrsrecht` | Wenn es um Baustellenverkehrsrecht in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-anordnung-angreifen` | Wenn es um Bewohnerparken Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-antrag-schreiben` | Wenn es um Bewohnerparken Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `bewohnerparken-behoerde-anschreiben` | Wenn es um Bewohnerparken Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-beweis-sichern` | Wenn es um Bewohnerparken Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-bussgeld-abgrenzen` | Wenn es um Bewohnerparken Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-eilrechtsschutz-behoerde` | Wenn es um Bewohnerparken Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-karte-bauen` | Wenn es um Bewohnerparken Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-regel-pruefen` | Wenn es um Bewohnerparken Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-risiko-erklaeren` | Wenn es um Bewohnerparken Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bewohnerparken-zeichen-anordnung` | Wenn es um Bewohnerparken Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `blaulicht-und-sonderrechte` | Wenn es um Blaulicht Und Sonderrechte in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bussgeldschnittstelle-owig` | Wenn es um Bussgeldschnittstelle Owig in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-anordnung-antrag-schreiben` | Wenn es um Busspur Anordnung Angreifen in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `busspur-antrag-schreiben` | Wenn es um Busspur Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `busspur-behoerde-karte-bauen-risiko` | Wenn es um Busspur Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-beweis-sichern` | Wenn es um Busspur Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-bussgeld-bewohnerparken` | Wenn es um Busspur Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-eilrechtsschutz-planen` | Wenn es um Busspur Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-karte-bauen` | Wenn es um Busspur Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-regel-pruefen` | Wenn es um Busspur Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-risiko-erklaeren` | Wenn es um Busspur Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `busspur-zeichen-auslegen` | Wenn es um Busspur Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `e-scooter-und-mikromobilitaet` | Wenn es um E Scooter Und Mikromobilitaet in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eilrechtsschutz-verkehrszeichen` | Wenn es um Eilrechtsschutz Verkehrszeichen in Straßenverkehrsrecht StVO geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrerlaubnis-schnittstelle` | Wenn es um Fahrerlaubnis Schnittstelle in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-anordnung-angreifen` | Wenn es um Fahrradstrasse Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-antrag-sichern` | Wenn es um Fahrradstrasse Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fahrradstrasse-behoerde-anschreiben` | Wenn es um Fahrradstrasse Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-beweis-sichern` | Wenn es um Fahrradstrasse Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-bussgeld-abgrenzen` | Wenn es um Fahrradstrasse Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-eilrechtsschutz-planen` | Wenn es um Fahrradstrasse Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-karte-risiko-erklaeren` | Wenn es um Fahrradstrasse Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-regel-pruefen` | Wenn es um Fahrradstrasse Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-risiko-erklaeren` | Wenn es um Fahrradstrasse Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrradstrasse-zeichen-auslegen` | Wenn es um Fahrradstrasse Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrtenbuchauflage` | Wenn es um Fahrtenbuchauflage in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefahrenstelle-melden-schulweg` | Wenn es um Gefahrenstelle Melden in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-anordnung-angreifen` | Wenn es um Haltverbot Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-antrag-schreiben` | Wenn es um Haltverbot Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `haltverbot-behoerde-anschreiben` | Wenn es um Haltverbot Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-beweis-sichern` | Wenn es um Haltverbot Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-bussgeld-abgrenzen` | Wenn es um Haltverbot Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-eilrechtsschutz-behoerde` | Wenn es um Haltverbot Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-karte-bauen` | Wenn es um Haltverbot Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-regel-pruefen` | Wenn es um Haltverbot Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-risiko-erklaeren` | Wenn es um Haltverbot Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haltverbot-zeichen-anordnung-angreifen` | Wenn es um Haltverbot Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-stvo-fall` | Wenn es um Kaltstart Stvo Fall in Straßenverkehrsrecht StVO geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Straßenverkehrsrecht StVO - Allgemeiner Einstieg in Straßenverkehrsrecht StVO geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunikation-mit-strassenverkehrsbeho` | Wenn es um Kommunikation Mit Strassenverkehrsbeho in Straßenverkehrsrecht StVO geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `ladezone-anordnung-angreifen` | Wenn es um Ladezone Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-antrag-sichern-eilrechtsschutz` | Wenn es um Ladezone Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `ladezone-behoerde-anschreiben` | Wenn es um Ladezone Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-beweis-sichern` | Wenn es um Ladezone Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-bussgeld-abgrenzen` | Wenn es um Ladezone Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-eilrechtsschutz-planen` | Wenn es um Ladezone Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-karte-risiko-erklaeren` | Wenn es um Ladezone Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-regel-pruefen` | Wenn es um Ladezone Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-risiko-erklaeren` | Wenn es um Ladezone Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ladezone-zeichen-auslegen` | Wenn es um Ladezone Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-anordnung-angreifen` | Wenn es um Lieferzone Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-antrag-schreiben` | Wenn es um Lieferzone Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `lieferzone-behoerde-anschreiben` | Wenn es um Lieferzone Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-bussgeld-abgrenzen` | Wenn es um Lieferzone Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-eilrechtsschutz-planen` | Wenn es um Lieferzone Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-karte-bauen` | Wenn es um Lieferzone Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-regel-zeichen-auslegen` | Wenn es um Lieferzone Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-risiko-ladezone-regel-zeichen` | Wenn es um Lieferzone Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-sichern-eilrechtsschutz-planen` | Wenn es um Lieferzone Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferzone-zeichen-auslegen` | Wenn es um Lieferzone Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mpu-und-fahreignung` | Wenn es um Mpu Und Fahreignung in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `parken-halten-ausnahmegenehmigung` | Wenn es um Parken Halten Abschleppen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `radverkehr-und-schutzstreifen` | Wenn es um Radverkehr Und Schutzstreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-anordnung-antrag-schreiben` | Wenn es um Schulstrasse Anordnung Angreifen in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schulstrasse-antrag-schreiben` | Wenn es um Schulstrasse Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schulstrasse-behoerde-karte` | Wenn es um Schulstrasse Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-beweis-sichern` | Wenn es um Schulstrasse Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-bussgeld-verkehrszeichen` | Wenn es um Schulstrasse Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-eilrechtsschutz-planen` | Wenn es um Schulstrasse Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-karte-bauen` | Wenn es um Schulstrasse Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-regel-pruefen` | Wenn es um Schulstrasse Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulstrasse-zeichen-auslegen` | Wenn es um Schulstrasse Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulweg-und-verkehrsberuhigung` | Wenn es um Schulweg Und Verkehrsberuhigung in Straßenverkehrsrecht StVO geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schwertransport-erlaubnis` | Wenn es um Schwertransport Und Erlaubnis in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-003-verkehrsrechtliche-anordnung-pruefen` | Wenn es um Verkehrsrechtliche Anordnung Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-021-haltverbot-regel-pruefen` | Wenn es um Haltverbot Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-028-haltverbot-behoerde-anschreiben` | Wenn es um Haltverbot Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-031-tempo-30-regel-pruefen` | Wenn es um Tempo 30 Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-038-tempo-30-behoerde-anschreiben` | Wenn es um Tempo 30 Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-041-fahrradstrasse-regel-pruefen` | Wenn es um Fahrradstrasse Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-048-fahrradstrasse-behoerde-anschreiben` | Wenn es um Fahrradstrasse Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-051-busspur-regel-pruefen` | Wenn es um Busspur Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-058-busspur-behoerde-anschreiben` | Wenn es um Busspur Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-061-bewohnerparken-regel-pruefen` | Wenn es um Bewohnerparken Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-068-bewohnerparken-behoerde-anschreiben` | Wenn es um Bewohnerparken Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-071-lieferzone-regel-pruefen` | Wenn es um Lieferzone Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-078-lieferzone-behoerde-anschreiben` | Wenn es um Lieferzone Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-081-ladezone-regel-pruefen` | Wenn es um Ladezone Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-088-ladezone-behoerde-anschreiben` | Wenn es um Ladezone Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-091-schulstrasse-regel-pruefen` | Wenn es um Schulstrasse Regel Pruefen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stv-098-schulstrasse-behoerde-anschreiben` | Wenn es um Schulstrasse Behoerde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-anordnung-angreifen` | Wenn es um Tempo 30 Anordnung Angreifen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-antrag-schreiben` | Wenn es um Tempo 30 Antrag Schreiben in Straßenverkehrsrecht StVO geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tempo-30-behoerde-anschreiben` | Wenn es um Tempo 30 Behörde Anschreiben in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-bussgeld-abgrenzen` | Wenn es um Tempo 30 Bussgeld Abgrenzen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-eilrechtsschutz-planen` | Wenn es um Tempo 30 Eilrechtsschutz Planen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-karte-bauen` | Wenn es um Tempo 30 Karte Bauen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-30-zeichen-auslegen` | Wenn es um Tempo 30 Zeichen Auslegen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-regel-zeichen-auslegen-anordnung` | Wenn es um Tempo 30 Regel Prüfen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-risiko-fahrradstrasse-regel` | Wenn es um Tempo 30 Risiko Erklaeren in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempo-sichern-eilrechtsschutz-planen` | Wenn es um Tempo 30 Beweis Sichern in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tempozone-und-beschilderung` | Wenn es um Tempozone Und Beschilderung in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verkehrsrechtliche-anordnung-pruefen` | Wenn es um Verkehrsrechtliche Anordnung Prüfen in Straßenverkehrsrecht StVO geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verkehrszeichen-lesen` | Wenn es um Verkehrszeichen Lesen in Straßenverkehrsrecht StVO geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `widerspruch-gegen-eilrechtsschutz` | Wenn es um Widerspruch Gegen Verkehrszeichen in Straßenverkehrsrecht StVO geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

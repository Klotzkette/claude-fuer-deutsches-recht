# Ordnungswidrigkeitenrecht


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`ordnungswidrigkeitenrecht`) | [`ordnungswidrigkeitenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ordnungswidrigkeitenrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **OWiG-Akte** (`ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier`) | [Gesamt-PDF lesen](../testakten/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier/gesamt-pdf/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier_gesamt.pdf) | [`testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Allgemeines OWiG-Plugin für Bußgeldverfahren: Anhörung, Bescheid, Einspruch, Behörde, Akteneinsicht, Gericht, Verjährung, Einziehung und Nebenfolgen.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ordnungswidrigkeitenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ordnungswidrigkeitenrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/ordnungswidrigkeitenrecht/ordnungswidrigkeitenrecht-werkstatt.md" download><code>ordnungswidrigkeitenrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/ordnungswidrigkeitenrecht/ordnungswidrigkeitenrecht-schnellstart.md" download><code>ordnungswidrigkeitenrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | OWiG-Akte: [Gesamt-PDF](../testakten/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier/gesamt-pdf/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier_gesamt.pdf), [`testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip), [`testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin ist das allgemeine Betriebssystem für Bußgeldsachen, nicht nur Verkehr: OWiG-Verfahren, Fachordnungswidrigkeiten, Anhörung, Bußgeldbescheid, Einspruch, Akteneinsicht, Amtsgericht und Rechtsbeschwerde.

## Start

Beginne mit `ordnungswidrigkeitenrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| 1. Einstieg und Fallrouting | `kaltstart-bussgeldverfahren`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `akteneinsicht-beantragen`, `aussenwirtschaft-akteneinsicht-schreiben`, `aussenwirtschaft-beweis-ruegen`, `baurecht-akteneinsicht-schreiben`, `baurecht-zerlegen-akteneinsicht-schreiben`, `datenschutzbussgeld-akteneinsicht-schr`, `datenschutzbussgeld-beweis`, `datenschutzbussgeld-einspruch-begruend`, `datenschutzbussgeld-einstellung-anrege`, `datenschutzbussgeld-frist-pruefen`, `datenschutzbussgeld-gerichtstermin-vor`, `datenschutzbussgeld-mandantenbrief-abgabe`, `datenschutzbussgeld-rechtsbeschwerde-p`, `datenschutzbussgeld-tatbestand`, `datenschutzbussgeld-verjaehrung-berech`, `gewerberecht-akteneinsicht-schreiben`, `gewerberecht-zerlegen-akteneinsicht`, `lebensmittelrecht-akteneinsicht-schrei`, ... plus 11 weitere |
| 3. Prüfung, Anspruch und Subsumtion | `aussenwirtschaft-tatbestand-zerlegen`, `lebensmittelrecht-tatbestand-zerlegen`, `owi-091-aussenwirtschaft-tatbestand-zerlegen`, `strassenverkehr-tatbestand-zerlegen`, `tatbestand-fachgesetz-finden`, `tierschutz-owi-tatbestand-zerlegen`, `umwelt-owi-tatbestand-zerlegen` |
| 4. Gestaltung, Strategie und Verhandlung | `amtsgericht-hauptverhandlung` |
| 5. Verfahren, Behörde und Gericht | `aussenwirtschaft-einspruch-einstellung`, `aussenwirtschaft-frist-pruefen`, `aussenwirtschaft-gerichtstermin`, `baurecht-einspruch-begruenden`, `baurecht-frist-strassenverkehr`, `baurecht-gerichtstermin-vorbereiten`, `beschlussverfahren-72-owig`, `bussgeldbescheid-pruefen`, `einspruch-fristgerecht`, `gewerberecht-einspruch-begruenden`, `gewerberecht-frist-umwelt`, `gewerberecht-gerichtstermin-vorbereite`, `jugendliche-im-owi-verfahren`, `lebensmittelrecht-einspruch`, `lebensmittelrecht-frist-pruefen`, `lebensmittelrecht-gerichtstermin`, `nebenfolgen-und-register`, `owi-004-bussgeldbescheid-pruefen`, ... plus 20 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `baurecht-mandantenbrief`, `gewerberecht-mandantenbrief-umwelt`, `lebensmittelrecht-mandantenbrief-schre`, `strassenverkehr-mandantenbrief-schreiben`, `tierschutz-owi-mandantenbrief-schreibe`, `umwelt-owi-mandantenbrief-schreiben` |
| 8. Spezialmodule und Schnittstellen | `abgabe-an-staatsanwaltschaft`, `anhoerung-richtig-behandeln`, `aufsichtspflichtverletzung-130-owig`, `aussenwirtschaft-einstellung-anregen`, `aussenwirtschaft-rechtsbeschwerde-prue`, `aussenwirtschaft-verjaehrung-berechnen`, `baurecht-einstellung-anregen`, `baurecht-rechtsbeschwerde-pruefen`, `baurecht-ruegen-verjaehrung-berechnen`, `baurecht-verjaehrung-berechnen`, `einziehung-und-verfall-pruefen`, `gewerberecht-einstellung-anregen`, `gewerberecht-rechtsbeschwerde-pruefen`, `gewerberecht-ruegen-verjaehrung-berechnen`, `gewerberecht-verjaehrung-berechnen`, `kostenentscheidung-angreifen`, `lebensmittelrecht-einstellung-anregen`, `lebensmittelrecht-rechtsbeschwerde-pru`, ... plus 32 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 133 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgabe-an-staatsanwaltschaft` | Wenn es um Abgabe An Staatsanwaltschaft in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `akteneinsicht-beantragen` | Wenn es um Akteneinsicht Beantragen in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `amtsgericht-hauptverhandlung` | Wenn es um Amtsgericht Hauptverhandlung in Ordnungswidrigkeitenrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `anhoerung-richtig-behandeln` | Wenn es um Anhörung Richtig Behandeln in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufsichtspflichtverletzung-130-owig` | Wenn es um Aufsichtspflichtverletzung 130 Owig in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-akteneinsicht-schreiben` | Wenn es um Außenwirtschaft Akteneinsicht Schreib in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `aussenwirtschaft-beweis-ruegen` | Wenn es um Außenwirtschaft Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-einspruch-einstellung` | Wenn es um Außenwirtschaft Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-einstellung-anregen` | Wenn es um Außenwirtschaft Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-frist-pruefen` | Wenn es um Außenwirtschaft Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-gerichtstermin` | Wenn es um Außenwirtschaft Gerichtstermin Vorber in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-rechtsbeschwerde-prue` | Wenn es um Außenwirtschaft Rechtsbeschwerde Prue in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-tatbestand-zerlegen` | Wenn es um Außenwirtschaft Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussenwirtschaft-verjaehrung-berechnen` | Wenn es um Außenwirtschaft Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-akteneinsicht-schreiben` | Wenn es um Baurecht Akteneinsicht Schreiben in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `baurecht-einspruch-begruenden` | Wenn es um Baurecht Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-einstellung-anregen` | Wenn es um Baurecht Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-frist-strassenverkehr` | Wenn es um Baurecht Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-gerichtstermin-vorbereiten` | Wenn es um Baurecht Gerichtstermin Vorbereiten in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-mandantenbrief` | Wenn es um Baurecht Mandantenbrief Schreiben in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `baurecht-rechtsbeschwerde-pruefen` | Wenn es um Baurecht Rechtsbeschwerde Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-ruegen-verjaehrung-berechnen` | Wenn es um Baurecht Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-verjaehrung-berechnen` | Wenn es um Baurecht Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baurecht-zerlegen-akteneinsicht-schreiben` | Wenn es um Baurecht Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beschlussverfahren-72-owig` | Wenn es um Beschlussverfahren 72 Owig in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bussgeldbescheid-pruefen` | Wenn es um Bussgeldbescheid Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-akteneinsicht-schr` | Wenn es um Datenschutzbussgeld Akteneinsicht Schr in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `datenschutzbussgeld-beweis` | Wenn es um Datenschutzbussgeld Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-einspruch-begruend` | Wenn es um Datenschutzbussgeld Einspruch Begruend in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-einstellung-anrege` | Wenn es um Datenschutzbussgeld Einstellung Anrege in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-frist-pruefen` | Wenn es um Datenschutzbussgeld Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-gerichtstermin-vor` | Wenn es um Datenschutzbussgeld Gerichtstermin Vor in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-mandantenbrief-abgabe` | Wenn es um Datenschutzbussgeld Mandantenbrief Sch in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `datenschutzbussgeld-rechtsbeschwerde-p` | Wenn es um Datenschutzbussgeld Rechtsbeschwerde P in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-tatbestand` | Wenn es um Datenschutzbussgeld Tatbestand Zerlege in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `datenschutzbussgeld-verjaehrung-berech` | Wenn es um Datenschutzbussgeld Verjährung Berech in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einspruch-fristgerecht` | Wenn es um Einspruch Fristgerecht Einlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einziehung-und-verfall-pruefen` | Wenn es um Einziehung Und Verfall Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-akteneinsicht-schreiben` | Wenn es um Gewerberecht Akteneinsicht Schreiben in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `gewerberecht-einspruch-begruenden` | Wenn es um Gewerberecht Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-einstellung-anregen` | Wenn es um Gewerberecht Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-frist-umwelt` | Wenn es um Gewerberecht Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-gerichtstermin-vorbereite` | Wenn es um Gewerberecht Gerichtstermin Vorbereite in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-mandantenbrief-umwelt` | Wenn es um Gewerberecht Mandantenbrief Schreiben in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `gewerberecht-rechtsbeschwerde-pruefen` | Wenn es um Gewerberecht Rechtsbeschwerde Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-ruegen-verjaehrung-berechnen` | Wenn es um Gewerberecht Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-verjaehrung-berechnen` | Wenn es um Gewerberecht Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gewerberecht-zerlegen-akteneinsicht` | Wenn es um Gewerberecht Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `jugendliche-im-owi-verfahren` | Wenn es um Jugendliche Im Owi Verfahren in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-bussgeldverfahren` | Wenn es um Kaltstart Bussgeldverfahren in Ordnungswidrigkeitenrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Ordnungswidrigkeitenrecht - Allgemeiner Einstieg in Ordnungswidrigkeitenrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kostenentscheidung-angreifen` | Wenn es um Kostenentscheidung Angreifen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-akteneinsicht-schrei` | Wenn es um Lebensmittelrecht Akteneinsicht Schrei in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `lebensmittelrecht-beweis-ruegen` | Wenn es um Lebensmittelrecht Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-einspruch` | Wenn es um Lebensmittelrecht Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-einstellung-anregen` | Wenn es um Lebensmittelrecht Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-frist-pruefen` | Wenn es um Lebensmittelrecht Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-gerichtstermin` | Wenn es um Lebensmittelrecht Gerichtstermin Vorbe in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-mandantenbrief-schre` | Wenn es um Lebensmittelrecht Mandantenbrief Schre in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `lebensmittelrecht-rechtsbeschwerde-pru` | Wenn es um Lebensmittelrecht Rechtsbeschwerde Pru in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-tatbestand-zerlegen` | Wenn es um Lebensmittelrecht Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lebensmittelrecht-verjaehrung-berechne` | Wenn es um Lebensmittelrecht Verjährung Berechne in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nebenfolgen-und-register` | Wenn es um Nebenfolgen Und Register in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `opportunitaet-und-einstellung` | Wenn es um Opportunitaet Und Einstellung in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-003-anhoerung-richtig-behandeln` | Wenn es um Anhoerung Richtig Behandeln in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-004-bussgeldbescheid-pruefen` | Wenn es um Bussgeldbescheid Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-007-verjaehrung-und-unterbrechung` | Wenn es um Verjaehrung Und Unterbrechung in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-012-einziehung-und-verfall-pruefen` | Wenn es um Einziehung Und Verfall Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-017-rechtsbeschwerde-pruefen` | Wenn es um Rechtsbeschwerde Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-022-datenschutzbussgeld-frist-pruefen` | Wenn es um Datenschutzbussgeld Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-027-datenschutzbussgeld-verjaehrung-berech` | Wenn es um Datenschutzbussgeld Verjaehrung Berech in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-032-gewerberecht-frist-pruefen` | Wenn es um Gewerberecht Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-037-gewerberecht-verjaehrung-berechnen` | Wenn es um Gewerberecht Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-039-gewerberecht-rechtsbeschwerde-pruefen` | Wenn es um Gewerberecht Rechtsbeschwerde Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-042-umwelt-owi-frist-pruefen` | Wenn es um Umwelt Owi Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-047-umwelt-owi-verjaehrung-berechnen` | Wenn es um Umwelt Owi Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-049-umwelt-owi-rechtsbeschwerde-pruefen` | Wenn es um Umwelt Owi Rechtsbeschwerde Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-052-lebensmittelrecht-frist-pruefen` | Wenn es um Lebensmittelrecht Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-057-lebensmittelrecht-verjaehrung-berechne` | Wenn es um Lebensmittelrecht Verjaehrung Berechne in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-062-tierschutz-owi-frist-pruefen` | Wenn es um Tierschutz Owi Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-067-tierschutz-owi-verjaehrung-berechnen` | Wenn es um Tierschutz Owi Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-069-tierschutz-owi-rechtsbeschwerde-pruefe` | Wenn es um Tierschutz Owi Rechtsbeschwerde Pruefe in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-072-baurecht-frist-pruefen` | Wenn es um Baurecht Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-077-baurecht-verjaehrung-berechnen` | Wenn es um Baurecht Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-079-baurecht-rechtsbeschwerde-pruefen` | Wenn es um Baurecht Rechtsbeschwerde Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-082-strassenverkehr-frist-pruefen` | Wenn es um Strassenverkehr Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-087-strassenverkehr-verjaehrung-berechnen` | Wenn es um Strassenverkehr Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-089-strassenverkehr-rechtsbeschwerde-pruef` | Wenn es um Strassenverkehr Rechtsbeschwerde Pruef in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-091-aussenwirtschaft-tatbestand-zerlegen` | Wenn es um Aussenwirtschaft Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-092-aussenwirtschaft-frist-pruefen` | Wenn es um Aussenwirtschaft Frist Pruefen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-093-aussenwirtschaft-akteneinsicht-schreib` | Wenn es um Aussenwirtschaft Akteneinsicht Schreib in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `owi-094-aussenwirtschaft-einspruch-begruenden` | Wenn es um Aussenwirtschaft Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-095-aussenwirtschaft-einstellung-anregen` | Wenn es um Aussenwirtschaft Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-096-aussenwirtschaft-beweis-ruegen` | Wenn es um Aussenwirtschaft Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-097-aussenwirtschaft-verjaehrung-berechnen` | Wenn es um Aussenwirtschaft Verjaehrung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-098-aussenwirtschaft-gerichtstermin-vorber` | Wenn es um Aussenwirtschaft Gerichtstermin Vorber in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owi-099-aussenwirtschaft-rechtsbeschwerde-prue` | Wenn es um Aussenwirtschaft Rechtsbeschwerde Prue in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `owig-in-einfacher-sprache` | Wenn es um Owig In Einfacher Sprache in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsbeschwerde-pruefen` | Wenn es um Rechtsbeschwerde Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-akteneinsicht-schreibe` | Wenn es um Strassenverkehr Akteneinsicht Schreibe in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `strassenverkehr-beweis-ruegen` | Wenn es um Strassenverkehr Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-einspruch-begruenden` | Wenn es um Strassenverkehr Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-einstellung-ruegen` | Wenn es um Strassenverkehr Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-frist-pruefen` | Wenn es um Strassenverkehr Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-gerichtstermin-vorbere` | Wenn es um Strassenverkehr Gerichtstermin Vorbere in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-mandantenbrief-schreiben` | Wenn es um Strassenverkehr Mandantenbrief Schreib in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `strassenverkehr-rechtsbeschwerde` | Wenn es um Strassenverkehr Rechtsbeschwerde Prüf in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-tatbestand-zerlegen` | Wenn es um Strassenverkehr Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenverkehr-verjaehrung-berechnen` | Wenn es um Strassenverkehr Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tatbestand-fachgesetz-finden` | Wenn es um Tatbestand Fachgesetz Finden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-akteneinsicht-einspruch` | Wenn es um Tierschutz Owi Akteneinsicht Schreiben in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `tierschutz-owi-beweis-ruegen` | Wenn es um Tierschutz Owi Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-einspruch-begruenden` | Wenn es um Tierschutz Owi Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-einstellung-anregen` | Wenn es um Tierschutz Owi Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-frist-pruefen` | Wenn es um Tierschutz Owi Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-gerichtstermin-vorberei` | Wenn es um Tierschutz Owi Gerichtstermin Vorberei in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-mandantenbrief-schreibe` | Wenn es um Tierschutz Owi Mandantenbrief Schreibe in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tierschutz-owi-rechtsbeschwerde-pruefe` | Wenn es um Tierschutz Owi Rechtsbeschwerde Prüfe in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-owi-tatbestand-zerlegen` | Wenn es um Tierschutz Owi Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-verjaehrung-gerichtstermin` | Wenn es um Tierschutz Owi Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-einstellung-ruegen-verjaehrung` | Wenn es um Umwelt Owi Einstellung Anregen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-akteneinsicht-schreiben` | Wenn es um Umwelt Owi Akteneinsicht Schreiben in Ordnungswidrigkeitenrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `umwelt-owi-beweis-ruegen` | Wenn es um Umwelt Owi Beweis Ruegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-einspruch-begruenden` | Wenn es um Umwelt Owi Einspruch Begruenden in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-frist-pruefen` | Wenn es um Umwelt Owi Frist Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-gerichtstermin-vorbereiten` | Wenn es um Umwelt Owi Gerichtstermin Vorbereiten in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-mandantenbrief-schreiben` | Wenn es um Umwelt Owi Mandantenbrief Schreiben in Ordnungswidrigkeitenrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `umwelt-owi-tatbestand-zerlegen` | Wenn es um Umwelt Owi Tatbestand Zerlegen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-owi-verjaehrung-berechnen` | Wenn es um Umwelt Owi Verjährung Berechnen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwelt-rechtsbeschwerde` | Wenn es um Umwelt Owi Rechtsbeschwerde Prüfen in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unternehmen-verbandsgeldbusse` | Wenn es um Unternehmen Und Verbandsgeldbusse in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verjaehrung-und-unterbrechung` | Wenn es um Verjährung Und Unterbrechung in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zustaendige-verwaltungsbehoerde` | Wenn es um Zustaendige Verwaltungsbehoerde in Ordnungswidrigkeitenrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

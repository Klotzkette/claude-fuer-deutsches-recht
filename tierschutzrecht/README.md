# Tierschutzrecht


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`tierschutzrecht`) | [`tierschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tierschutzrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Tierschutzakte Pferdehof Auenwiese** (`tierschutzrecht-veterinaeramt-pferdehof-auenwiese`) | [Gesamt-PDF lesen](../testakten/tierschutzrecht-veterinaeramt-pferdehof-auenwiese/gesamt-pdf/tierschutzrecht-veterinaeramt-pferdehof-auenwiese_gesamt.pdf) | [`testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Tierschutzrecht-Plugin für TierSchG, BGB Paragraf 90a, Haltung, Zucht, Transport, Tierversuche, Behördenverfahren, Strafrecht, Bußgeld und zivilrechtliche Tierfälle.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`tierschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tierschutzrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/tierschutzrecht/tierschutzrecht-werkstatt.md" download><code>tierschutzrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/tierschutzrecht/tierschutzrecht-schnellstart.md" download><code>tierschutzrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Tierschutzakte Pferdehof Auenwiese: [Gesamt-PDF](../testakten/tierschutzrecht-veterinaeramt-pferdehof-auenwiese/gesamt-pdf/tierschutzrecht-veterinaeramt-pferdehof-auenwiese_gesamt.pdf), [`testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese.zip), [`testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-tierschutzrecht-veterinaeramt-pferdehof-auenwiese-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin nimmt Tiere rechtlich ernst: § 90a BGB als Ausgangspunkt, TierSchG als öffentlich-rechtliches und strafrechtliches Schutzregime, dazu Zivilrecht, Behördenaufsicht, Veterinäramt und Vollzug.

## Start

Beginne mit `tierschutzrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| 1. Einstieg und Fallrouting | `kaltstart-tierschutzfall`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `beweisfotos-und-datenschutz`, `gefluegelmast-beweise-sichern`, `haltung-und-betreuung-dokumentieren`, `hundehaltung-beweise-sichern`, `katzenkolonie-beweise-sichern`, `pferdestall-beweise-strafrisiko-bewerten`, `rinderbetrieb-anordnung-beweise-sichern`, `rinderbetrieb-beweise-sichern`, `schlachthof-anordnung-beweise-sichern`, `schlachthof-beweise-sichern`, `schweinehaltung-beweise-sichern`, `tiertransport-beweise-strafrisiko` |
| 3. Prüfung, Anspruch und Subsumtion | `gefluegelmast-strafrisiko-kosten-klaeren`, `hundehaltung-strafrisiko-bewerten`, `katzenkolonie-strafrisiko-kosten-klaeren`, `pferdestall-strafrisiko-bewerten`, `rinderbetrieb-strafrisiko-bewerten`, `schlachthof-strafrisiko-bewerten`, `schweinehaltung-strafrisiko-bewerten`, `tiertransport-strafrisiko-bewerten` |
| 4. Gestaltung, Strategie und Verhandlung | `hundehaltung-vergleich-suchen`, `pferdestall-vergleich-suchen`, `rinderbetrieb-vergleich-suchen`, `schweinehaltung-vergleich-suchen`, `tierheimvertrag-und-kosten`, `tierschutzverein-handlungsoptionen`, `tiertransport-vergleich-suchen` |
| 5. Verfahren, Behörde und Gericht | `bussgeldverfahren-tierschg`, `gefluegelmast-behoerdenantrag-schreibe`, `gefluegelmast-eilantrag-bauen`, `hundehaltung-behoerdenantrag-anordnung`, `hundehaltung-eilantrag-bauen`, `katzenkolonie-behoerdenantrag-schreibe`, `katzenkolonie-eilantrag-bauen`, `pferdestall-behoerdenantrag-schreiben`, `pferdestall-eilantrag-suchen`, `rinderbetrieb-behoerdenantrag-schreibe`, `rinderbetrieb-eilantrag-bauen`, `rinderbetrieb-halterpflichten-eilantrag`, `schlachthof-behoerdenantrag-schreiben`, `schlachthof-eilantrag-bauen`, `schlachthof-halterpflichten-eilantrag`, `schweinehaltung-behoerdenantrag`, `schweinehaltung-eilantrag-bauen`, `tier-022-hundehaltung-behoerdenantrag-schreiben`, ... plus 10 weitere |
| 7. Kontrolle, Qualität und Gegenprüfung | `nutztierhaltung-kontrolle`, `tierarzt-und-behandlungsfehler` |
| 8. Spezialmodule und Schnittstellen | `90a-bgb-richtig-einordnen`, `anordnung-und-wegnahme-pruefen`, `eilrechtsschutz-tierhalter`, `fundtier-und-eigentum`, `gefaehrlicher-hund-zucht-qualzucht`, `gefluegelmast-anordnung-angreifen`, `gefluegelmast-bussgeld-tiertransport`, `gefluegelmast-halterpflichten-erklaere`, `gefluegelmast-kosten-klaeren`, `gefluegelmast-schutzbedarf`, `gefluegelmast-suchen-tiertransport`, `hundehaltung-anordnung-angreifen`, `hundehaltung-bussgeld-verteidigen`, `hundehaltung-halterpflichten-erklaeren`, `hundehaltung-kosten-halterpflichten`, `hundehaltung-schutzbedarf-pruefen`, `katzenkolonie-anordnung-angreifen`, `katzenkolonie-bussgeld-pferdestall`, ... plus 51 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 128 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `90a-bgb-richtig-einordnen` | Wenn es um 90a Bgb Richtig Einordnen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anordnung-und-wegnahme-pruefen` | Wenn es um Anordnung Und Wegnahme Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweisfotos-und-datenschutz` | Wenn es um Beweisfotos Und Datenschutz in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bussgeldverfahren-tierschg` | Wenn es um Bussgeldverfahren Tierschg in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eilrechtsschutz-tierhalter` | Wenn es um Eilrechtsschutz Gegen Haltungsverbot in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fundtier-und-eigentum` | Wenn es um Fundtier Und Eigentum in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefaehrlicher-hund-zucht-qualzucht` | Wenn es um Gefaehrlicher Hund Landesrecht in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-anordnung-angreifen` | Wenn es um Gefluegelmast Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-behoerdenantrag-schreibe` | Wenn es um Gefluegelmast Behördenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `gefluegelmast-beweise-sichern` | Wenn es um Gefluegelmast Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-bussgeld-tiertransport` | Wenn es um Gefluegelmast Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-eilantrag-bauen` | Wenn es um Gefluegelmast Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `gefluegelmast-halterpflichten-erklaere` | Wenn es um Gefluegelmast Halterpflichten Erklaere in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-kosten-klaeren` | Wenn es um Gefluegelmast Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-schutzbedarf` | Wenn es um Gefluegelmast Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-strafrisiko-kosten-klaeren` | Wenn es um Gefluegelmast Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefluegelmast-suchen-tiertransport` | Wenn es um Gefluegelmast Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `haltung-und-betreuung-dokumentieren` | Wenn es um Haltung Und Betreuung Dokumentieren in Tierschutzrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `hundehaltung-anordnung-angreifen` | Wenn es um Hundehaltung Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-behoerdenantrag-anordnung` | Wenn es um Hundehaltung Behördenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `hundehaltung-beweise-sichern` | Wenn es um Hundehaltung Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-bussgeld-verteidigen` | Wenn es um Hundehaltung Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-eilantrag-bauen` | Wenn es um Hundehaltung Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `hundehaltung-halterpflichten-erklaeren` | Wenn es um Hundehaltung Halterpflichten Erklaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-kosten-halterpflichten` | Wenn es um Hundehaltung Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-schutzbedarf-pruefen` | Wenn es um Hundehaltung Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-strafrisiko-bewerten` | Wenn es um Hundehaltung Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hundehaltung-vergleich-suchen` | Wenn es um Hundehaltung Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `kaltstart-tierschutzfall` | Wenn es um Kaltstart Tierschutzfall in Tierschutzrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Tierschutzrecht - Allgemeiner Einstieg in Tierschutzrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-anordnung-angreifen` | Wenn es um Katzenkolonie Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-behoerdenantrag-schreibe` | Wenn es um Katzenkolonie Behördenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `katzenkolonie-beweise-sichern` | Wenn es um Katzenkolonie Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-bussgeld-pferdestall` | Wenn es um Katzenkolonie Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-eilantrag-bauen` | Wenn es um Katzenkolonie Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `katzenkolonie-halterpflichten-erklaere` | Wenn es um Katzenkolonie Halterpflichten Erklaere in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-kosten-klaeren` | Wenn es um Katzenkolonie Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-schutzbedarf` | Wenn es um Katzenkolonie Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-strafrisiko-kosten-klaeren` | Wenn es um Katzenkolonie Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `katzenkolonie-suchen-pferdestall` | Wenn es um Katzenkolonie Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `nutztierhaltung-kontrolle` | Wenn es um Nutztierhaltung Kontrolle in Tierschutzrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-anordnung-angreifen` | Wenn es um Pferdestall Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-behoerdenantrag-schreiben` | Wenn es um Pferdestall Behördenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `pferdestall-beweise-strafrisiko-bewerten` | Wenn es um Pferdestall Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-bussgeld-verteidigen` | Wenn es um Pferdestall Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-eilantrag-suchen` | Wenn es um Pferdestall Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `pferdestall-halterpflichten-erklaeren` | Wenn es um Pferdestall Halterpflichten Erklaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-kosten-klaeren` | Wenn es um Pferdestall Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-schutzbedarf-pruefen` | Wenn es um Pferdestall Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-strafrisiko-bewerten` | Wenn es um Pferdestall Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pferdestall-vergleich-suchen` | Wenn es um Pferdestall Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `rinderbetrieb-anordnung-beweise-sichern` | Wenn es um Rinderbetrieb Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-behoerdenantrag-schreibe` | Wenn es um Rinderbetrieb Behördenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `rinderbetrieb-beweise-sichern` | Wenn es um Rinderbetrieb Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-bussgeld-verteidigen` | Wenn es um Rinderbetrieb Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-eilantrag-bauen` | Wenn es um Rinderbetrieb Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `rinderbetrieb-halterpflichten-eilantrag` | Wenn es um Rinderbetrieb Halterpflichten Erklaere in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `rinderbetrieb-kosten-klaeren` | Wenn es um Rinderbetrieb Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-schutzbedarf-pruefen` | Wenn es um Rinderbetrieb Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-strafrisiko-bewerten` | Wenn es um Rinderbetrieb Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rinderbetrieb-vergleich-suchen` | Wenn es um Rinderbetrieb Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `schlachthof-anordnung-beweise-sichern` | Wenn es um Schlachthof Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlachthof-behoerdenantrag-schreiben` | Wenn es um Schlachthof Behördenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schlachthof-beweise-sichern` | Wenn es um Schlachthof Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlachthof-bussgeld-verteidigen` | Wenn es um Schlachthof Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlachthof-eilantrag-bauen` | Wenn es um Schlachthof Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schlachthof-halterpflichten-eilantrag` | Wenn es um Schlachthof Halterpflichten Erklaeren in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schlachthof-kosten-klaeren` | Wenn es um Schlachthof Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlachthof-schutzbedarf-pruefen` | Wenn es um Schlachthof Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlachthof-strafrisiko-bewerten` | Wenn es um Schlachthof Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-anordnung-angreifen` | Wenn es um Schweinehaltung Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-behoerdenantrag` | Wenn es um Schweinehaltung Behördenantrag Schrei in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schweinehaltung-beweise-sichern` | Wenn es um Schweinehaltung Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-bussgeld-verteidigen` | Wenn es um Schweinehaltung Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-eilantrag-bauen` | Wenn es um Schweinehaltung Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schweinehaltung-halterpflichten-erklae` | Wenn es um Schweinehaltung Halterpflichten Erklae in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-kosten-halterpflichten` | Wenn es um Schweinehaltung Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-schutzbedarf-pruefen` | Wenn es um Schweinehaltung Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-strafrisiko-bewerten` | Wenn es um Schweinehaltung Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schweinehaltung-vergleich-suchen` | Wenn es um Schweinehaltung Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `tier-003-tierschg-grundsatz-und-leiden-pruefen` | Wenn es um Tierschg Grundsatz Und Leiden Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-004-veterinaeramt-zustaendigkeit` | Wenn es um Veterinaeramt Zustaendigkeit in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-006-anordnung-und-wegnahme-pruefen` | Wenn es um Anordnung Und Wegnahme Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-016-tiertransport-pruefen` | Wenn es um Tiertransport Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-021-hundehaltung-schutzbedarf-pruefen` | Wenn es um Hundehaltung Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-022-hundehaltung-behoerdenantrag-schreiben` | Wenn es um Hundehaltung Behoerdenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-027-hundehaltung-kosten-klaeren` | Wenn es um Hundehaltung Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-031-katzenkolonie-schutzbedarf-pruefen` | Wenn es um Katzenkolonie Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-032-katzenkolonie-behoerdenantrag-schreibe` | Wenn es um Katzenkolonie Behoerdenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-037-katzenkolonie-kosten-klaeren` | Wenn es um Katzenkolonie Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-041-pferdestall-schutzbedarf-pruefen` | Wenn es um Pferdestall Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-042-pferdestall-behoerdenantrag-schreiben` | Wenn es um Pferdestall Behoerdenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-047-pferdestall-kosten-klaeren` | Wenn es um Pferdestall Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-051-rinderbetrieb-schutzbedarf-pruefen` | Wenn es um Rinderbetrieb Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-052-rinderbetrieb-behoerdenantrag-schreibe` | Wenn es um Rinderbetrieb Behoerdenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-057-rinderbetrieb-kosten-klaeren` | Wenn es um Rinderbetrieb Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-061-schweinehaltung-schutzbedarf-pruefen` | Wenn es um Schweinehaltung Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-062-schweinehaltung-behoerdenantrag-schrei` | Wenn es um Schweinehaltung Behoerdenantrag Schrei in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-067-schweinehaltung-kosten-klaeren` | Wenn es um Schweinehaltung Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-071-gefluegelmast-schutzbedarf-pruefen` | Wenn es um Gefluegelmast Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-072-gefluegelmast-behoerdenantrag-schreibe` | Wenn es um Gefluegelmast Behoerdenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-077-gefluegelmast-kosten-klaeren` | Wenn es um Gefluegelmast Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-081-tiertransport-schutzbedarf-pruefen` | Wenn es um Tiertransport Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-082-tiertransport-behoerdenantrag-schreibe` | Wenn es um Tiertransport Behoerdenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-087-tiertransport-kosten-klaeren` | Wenn es um Tiertransport Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-091-schlachthof-schutzbedarf-pruefen` | Wenn es um Schlachthof Schutzbedarf Pruefen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tier-092-schlachthof-behoerdenantrag-schreiben` | Wenn es um Schlachthof Behoerdenantrag Schreiben in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tier-097-schlachthof-kosten-klaeren` | Wenn es um Schlachthof Kosten Klaeren in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierarzt-und-behandlungsfehler` | Wenn es um Tierarzt Und Behandlungsfehler in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierhalter-zivilrechtlich-beraten` | Wenn es um Tierhalter Zivilrechtlich Beraten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierheimvertrag-und-kosten` | Wenn es um Tierheimvertrag Und Kosten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschg-grundsatz-haltung-betreuung` | Wenn es um Tierschg Grundsatz Und Leiden Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutz-strafanzeige-vorbereiten` | Wenn es um Tierschutz Strafanzeige Vorbereiten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tierschutzverein-handlungsoptionen` | Wenn es um Tierschutzverein Handlungsoptionen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-anordnung-angreifen` | Wenn es um Tiertransport Anordnung Angreifen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-behoerdenantrag-schreibe` | Wenn es um Tiertransport Behördenantrag Schreibe in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tiertransport-beweise-strafrisiko` | Wenn es um Tiertransport Beweise Sichern in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-bussgeld-verteidigen` | Wenn es um Tiertransport Bussgeld Verteidigen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-eilantrag-suchen` | Wenn es um Tiertransport Eilantrag Bauen in Tierschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tiertransport-halterpflichten-erklaere` | Wenn es um Tiertransport Halterpflichten Erklaere in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-kosten-klaeren` | Wenn es um Tiertransport Kosten Klären in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-pruefen` | Wenn es um Tiertransport Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-schutzbedarf-pruefen` | Wenn es um Tiertransport Schutzbedarf Prüfen in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-strafrisiko-bewerten` | Wenn es um Tiertransport Strafrisiko Bewerten in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tiertransport-vergleich-suchen` | Wenn es um Tiertransport Vergleich Suchen in Tierschutzrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `tierversuch-genehmigung` | Wenn es um Tierversuch Genehmigung in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `veterinaeramt-bussgeldverfahren-tierschg` | Wenn es um Veterinaeramt Zuständigkeit in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zucht-und-qualzucht` | Wenn es um Zucht Und Qualzucht in Tierschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

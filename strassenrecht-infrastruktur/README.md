# Straßenrecht und Infrastruktur


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strassenrecht-infrastruktur`) | [`strassenrecht-infrastruktur.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenrecht-infrastruktur.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Straßenrechtsakte Auenfeld** (`strassenrecht-ortsdurchfahrt-bruecke-auenfeld`) | [Gesamt-PDF lesen](../testakten/strassenrecht-ortsdurchfahrt-bruecke-auenfeld/gesamt-pdf/strassenrecht-ortsdurchfahrt-bruecke-auenfeld_gesamt.pdf) | [`testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Straßenrecht-Plugin für Bundesfernstraßen, Landesstraßen, Gemeindestraßen, Widmung, Planfeststellung, Sondernutzung, Baulast und Erhaltung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strassenrecht-infrastruktur.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenrecht-infrastruktur.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strassenrecht-infrastruktur/strassenrecht-infrastruktur-werkstatt.md" download><code>strassenrecht-infrastruktur-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strassenrecht-infrastruktur/strassenrecht-infrastruktur-schnellstart.md" download><code>strassenrecht-infrastruktur-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Straßenrechtsakte Auenfeld: [Gesamt-PDF](../testakten/strassenrecht-ortsdurchfahrt-bruecke-auenfeld/gesamt-pdf/strassenrecht-ortsdurchfahrt-bruecke-auenfeld_gesamt.pdf), [`testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip), [`testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin trennt Straßenrecht von Straßenverkehrsrecht: Bau, Widmung, Baulast, Unterhaltung, Sondernutzung, Planfeststellung, Anliegerrechte, Kreuzungen, Umstufung und Straßeninfrastruktur.

## Start

Beginne mit `strassenrecht-infrastruktur-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| 1. Einstieg und Fallrouting | `kaltstart-strassenrechtsfall`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `aktenplan-infrastruktur`, `autobahn-dokumente-sortieren`, `bruecke-dokumente-sortieren`, `bundesstrasse-dokumente-sortieren`, `bundesstrasse-unterhaltung-dokumente`, `eilrechtsschutz-aktenplan-infrastruktur`, `gemeindestrasse-dokumente-sortieren`, `kreisstrasse-dokumente-sortieren`, `kreisstrasse-unterhaltung-dokumente`, `landesstrasse-dokumente-sortieren`, `ortsdurchfahrt-dokumente-sortieren`, `ortsdurchfahrt-unterhaltung-dokumente`, `tunnel-dokumente-sortieren`, `tunnel-unterhaltung-dokumente` |
| 3. Prüfung, Anspruch und Subsumtion | `landesstrassengesetz-livecheck` |
| 4. Gestaltung, Strategie und Verhandlung | `autobahn-planrecht-pruefen`, `autobahn-widmung-planrecht-sondernutzung`, `bruecke-planrecht-pruefen`, `bruecke-widmung-planrecht-sondernutzung`, `bundesstrasse-planrecht-pruefen`, `gemeindestrasse-planrecht-pruefen`, `gemeindestrasse-widmung-planrecht`, `kreisstrasse-planrecht-pruefen`, `landesstrasse-planrecht-pruefen`, `landesstrasse-widmung-planrecht`, `ortsdurchfahrt-planrecht-pruefen`, `planfeststellung-strasse-plangenehmigung`, `plangenehmigung-und-uvp`, `str-023-autobahn-planrecht-pruefen`, `str-033-bundesstrasse-planrecht-pruefen`, `str-043-landesstrasse-planrecht-pruefen`, `str-053-kreisstrasse-planrecht-pruefen`, `str-063-gemeindestrasse-planrecht-pruefen`, ... plus 4 weitere |
| 5. Verfahren, Behörde und Gericht | `autobahn-eilantrag-kostenlast`, `bruecke-eilantrag-kostenlast-unterhaltung`, `bundesstrasse-eilantrag-skizzieren`, `gemeindestrasse-eilantrag-kostenlast`, `kreisstrasse-eilantrag-skizzieren`, `landesstrasse-eilantrag-kostenlast`, `ortsdurchfahrt-eilantrag-skizzieren`, `tunnel-eilantrag-skizzieren` |
| 8. Spezialmodule und Schnittstellen | `anliegergebrauch-abgrenzen`, `autobahn-baulast-pruefen`, `autobahn-dashboard-bundesstrasse`, `autobahn-einwendung-bauen`, `autobahn-kostenlast-pruefen`, `autobahn-sondernutzung-formulieren`, `autobahn-unterhaltung-ruegen`, `baustelle-verkehrsfuehrung`, `bruecke-baulast-pruefen`, `bruecke-dashboard-tunnel-baulast-widmung`, `bruecke-einwendung-bauen`, `bruecke-kostenlast-pruefen`, `bruecke-sondernutzung-formulieren`, `bruecke-und-tunnel`, `bruecke-unterhaltung-ruegen`, `bundesfernstrasse-landesstrasse`, `bundesstrasse-baulast-pruefen`, `bundesstrasse-dashboard-erstellen`, ... plus 61 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 126 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenplan-infrastruktur` | Wenn es um Aktenplan Infrastruktur in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anliegergebrauch-abgrenzen` | Wenn es um Anliegergebrauch Abgrenzen in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-baulast-pruefen` | Wenn es um Autobahn Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-dashboard-bundesstrasse` | Wenn es um Autobahn Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-dokumente-sortieren` | Wenn es um Autobahn Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `autobahn-eilantrag-kostenlast` | Wenn es um Autobahn Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `autobahn-einwendung-bauen` | Wenn es um Autobahn Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-kostenlast-pruefen` | Wenn es um Autobahn Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-planrecht-pruefen` | Wenn es um Autobahn Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-sondernutzung-formulieren` | Wenn es um Autobahn Sondernutzung Formulieren in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-unterhaltung-ruegen` | Wenn es um Autobahn Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `autobahn-widmung-planrecht-sondernutzung` | Wenn es um Autobahn Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baustelle-verkehrsfuehrung` | Wenn es um Baustelle Und Verkehrsfuehrung in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-baulast-pruefen` | Wenn es um Bruecke Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-dashboard-tunnel-baulast-widmung` | Wenn es um Bruecke Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-dokumente-sortieren` | Wenn es um Bruecke Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bruecke-eilantrag-kostenlast-unterhaltung` | Wenn es um Bruecke Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `bruecke-einwendung-bauen` | Wenn es um Bruecke Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-kostenlast-pruefen` | Wenn es um Bruecke Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-planrecht-pruefen` | Wenn es um Bruecke Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-sondernutzung-formulieren` | Wenn es um Bruecke Sondernutzung Formulieren in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-und-tunnel` | Wenn es um Bruecke Und Tunnel in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-unterhaltung-ruegen` | Wenn es um Bruecke Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bruecke-widmung-planrecht-sondernutzung` | Wenn es um Bruecke Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesfernstrasse-landesstrasse` | Wenn es um Bundesfernstrasse Oder Landesstrasse in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bundesstrasse-baulast-pruefen` | Wenn es um Bundesstrasse Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-dashboard-erstellen` | Wenn es um Bundesstrasse Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-dokumente-sortieren` | Wenn es um Bundesstrasse Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bundesstrasse-eilantrag-skizzieren` | Wenn es um Bundesstrasse Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `bundesstrasse-einwendung-bauen` | Wenn es um Bundesstrasse Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-kostenlast-pruefen` | Wenn es um Bundesstrasse Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-planrecht-pruefen` | Wenn es um Bundesstrasse Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-sondernutzung-einwendung` | Wenn es um Bundesstrasse Sondernutzung Formuliere in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesstrasse-unterhaltung-dokumente` | Wenn es um Bundesstrasse Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bundesstrasse-widmung-lesen` | Wenn es um Bundesstrasse Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eilrechtsschutz-aktenplan-infrastruktur` | Wenn es um Eilrechtsschutz Gegen Bau in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-baulast-pruefen` | Wenn es um Gemeindestrasse Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-dashboard-ortsdurchfahrt` | Wenn es um Gemeindestrasse Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-dokumente-sortieren` | Wenn es um Gemeindestrasse Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `gemeindestrasse-eilantrag-kostenlast` | Wenn es um Gemeindestrasse Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `gemeindestrasse-einwendung-bauen` | Wenn es um Gemeindestrasse Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-kostenlast-pruefen` | Wenn es um Gemeindestrasse Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-planrecht-pruefen` | Wenn es um Gemeindestrasse Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-sondernutzung-formulie` | Wenn es um Gemeindestrasse Sondernutzung Formulie in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-unterhaltung-ruegen` | Wenn es um Gemeindestrasse Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeindestrasse-widmung-planrecht` | Wenn es um Gemeindestrasse Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-strassenrechtsfall` | Wenn es um Kaltstart Strassenrechtsfall in Straßenrecht und Infrastruktur geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Straßenrecht und Infrastruktur - Allgemeiner Einstieg in Straßenrecht und Infrastruktur geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-baulast-pruefen` | Wenn es um Kreisstrasse Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-dashboard-erstellen` | Wenn es um Kreisstrasse Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-dokumente-sortieren` | Wenn es um Kreisstrasse Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kreisstrasse-eilantrag-skizzieren` | Wenn es um Kreisstrasse Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kreisstrasse-einwendung-bauen` | Wenn es um Kreisstrasse Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-kostenlast-pruefen` | Wenn es um Kreisstrasse Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-planrecht-pruefen` | Wenn es um Kreisstrasse Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-sondernutzung-einwendung` | Wenn es um Kreisstrasse Sondernutzung Formulieren in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreisstrasse-unterhaltung-dokumente` | Wenn es um Kreisstrasse Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kreisstrasse-widmung-lesen` | Wenn es um Kreisstrasse Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreuzungsrecht-strassenausbaubeitrag` | Wenn es um Kreuzungsrecht Bahn Wasser Strasse in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `landesstrasse-baulast-pruefen` | Wenn es um Landesstrasse Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-dashboard` | Wenn es um Landesstrasse Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-dokumente-sortieren` | Wenn es um Landesstrasse Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `landesstrasse-eilantrag-kostenlast` | Wenn es um Landesstrasse Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `landesstrasse-einwendung-bauen` | Wenn es um Landesstrasse Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-kostenlast-pruefen` | Wenn es um Landesstrasse Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-planrecht-pruefen` | Wenn es um Landesstrasse Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-sondernutzung-formuliere` | Wenn es um Landesstrasse Sondernutzung Formuliere in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-unterhaltung-ruegen` | Wenn es um Landesstrasse Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrasse-widmung-planrecht` | Wenn es um Landesstrasse Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landesstrassengesetz-livecheck` | Wenn es um Landesstrassengesetz Livecheck in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-baulast-pruefen` | Wenn es um Ortsdurchfahrt Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-dashboard-erstellen` | Wenn es um Ortsdurchfahrt Dashboard Erstellen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-dokumente-sortieren` | Wenn es um Ortsdurchfahrt Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `ortsdurchfahrt-eilantrag-skizzieren` | Wenn es um Ortsdurchfahrt Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `ortsdurchfahrt-einwendung-bauen` | Wenn es um Ortsdurchfahrt Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-kostenlast-pruefen` | Wenn es um Ortsdurchfahrt Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-planrecht-pruefen` | Wenn es um Ortsdurchfahrt Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-sondernutzung-einwendung` | Wenn es um Ortsdurchfahrt Sondernutzung Formulier in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortsdurchfahrt-unterhaltung-dokumente` | Wenn es um Ortsdurchfahrt Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `ortsdurchfahrt-widmung-lesen` | Wenn es um Ortsdurchfahrt Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `planfeststellung-strasse-plangenehmigung` | Wenn es um Planfeststellung Strasse in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `plangenehmigung-und-uvp` | Wenn es um Plangenehmigung Und Uvp in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rastanlage-und-nebenbetrieb` | Wenn es um Rastanlage Und Nebenbetrieb in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schaeden-durch-strasse` | Wenn es um Schaeden Durch Strasse in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sondernutzungserlaubnis` | Wenn es um Sondernutzungserlaubnis in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-004-widmung-und-einziehung-pruefen` | Wenn es um Widmung Und Einziehung Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-015-strassenausbaubeitrag-pruefen` | Wenn es um Strassenausbaubeitrag Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-021-autobahn-baulast-pruefen` | Wenn es um Autobahn Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-023-autobahn-planrecht-pruefen` | Wenn es um Autobahn Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-027-autobahn-kostenlast-pruefen` | Wenn es um Autobahn Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-031-bundesstrasse-baulast-pruefen` | Wenn es um Bundesstrasse Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-033-bundesstrasse-planrecht-pruefen` | Wenn es um Bundesstrasse Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-037-bundesstrasse-kostenlast-pruefen` | Wenn es um Bundesstrasse Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-041-landesstrasse-baulast-pruefen` | Wenn es um Landesstrasse Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-043-landesstrasse-planrecht-pruefen` | Wenn es um Landesstrasse Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-047-landesstrasse-kostenlast-pruefen` | Wenn es um Landesstrasse Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-051-kreisstrasse-baulast-pruefen` | Wenn es um Kreisstrasse Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-053-kreisstrasse-planrecht-pruefen` | Wenn es um Kreisstrasse Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-057-kreisstrasse-kostenlast-pruefen` | Wenn es um Kreisstrasse Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-061-gemeindestrasse-baulast-pruefen` | Wenn es um Gemeindestrasse Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-063-gemeindestrasse-planrecht-pruefen` | Wenn es um Gemeindestrasse Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-067-gemeindestrasse-kostenlast-pruefen` | Wenn es um Gemeindestrasse Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-071-ortsdurchfahrt-baulast-pruefen` | Wenn es um Ortsdurchfahrt Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-073-ortsdurchfahrt-planrecht-pruefen` | Wenn es um Ortsdurchfahrt Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-077-ortsdurchfahrt-kostenlast-pruefen` | Wenn es um Ortsdurchfahrt Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-081-bruecke-baulast-pruefen` | Wenn es um Bruecke Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-083-bruecke-planrecht-pruefen` | Wenn es um Bruecke Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-087-bruecke-kostenlast-pruefen` | Wenn es um Bruecke Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-091-tunnel-baulast-pruefen` | Wenn es um Tunnel Baulast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-093-tunnel-planrecht-pruefen` | Wenn es um Tunnel Planrecht Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `str-097-tunnel-kostenlast-pruefen` | Wenn es um Tunnel Kostenlast Pruefen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenausbaubeitrag-pruefen` | Wenn es um Strassenausbaubeitrag Prüfen in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenbaulasttraeger-bestimmen` | Wenn es um Strassenbaulasttraeger Bestimmen in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenentwaesserung` | Wenn es um Strassenentwaesserung in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-baulast-pruefen` | Wenn es um Tunnel Baulast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-dokumente-sortieren` | Wenn es um Tunnel Dokumente Sortieren in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `tunnel-eilantrag-skizzieren` | Wenn es um Tunnel Eilantrag Skizzieren in Straßenrecht und Infrastruktur geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tunnel-einwendung-bauen` | Wenn es um Tunnel Einwendung Bauen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-kostenlast-pruefen` | Wenn es um Tunnel Kostenlast Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-planrecht-pruefen` | Wenn es um Tunnel Planrecht Prüfen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-sondernutzung-einwendung-bauen` | Wenn es um Tunnel Sondernutzung Formulieren in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tunnel-unterhaltung-dokumente` | Wenn es um Tunnel Unterhaltung Ruegen in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `tunnel-widmung-lesen` | Wenn es um Tunnel Widmung Lesen in Straßenrecht und Infrastruktur geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umstufung-und-teileinziehung` | Wenn es um Umstufung Und Teileinziehung in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterhaltungspflicht-und-winterdienst` | Wenn es um Unterhaltungspflicht Und Winterdienst in Straßenrecht und Infrastruktur geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `widmung-und-einziehung-pruefen` | Wenn es um Widmung Und Einziehung Prüfen in Straßenrecht und Infrastruktur geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

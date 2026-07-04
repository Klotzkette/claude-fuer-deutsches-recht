# Kommunalrecht der Länder

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kommunalrecht-laender`) | [`kommunalrecht-laender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kommunalrecht-laender.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kommunalakte Morgenfurt** (`kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt`) | [Gesamt-PDF lesen](../testakten/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt/gesamt-pdf/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt_gesamt.pdf) | [`testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Großes Kommunalrecht-Plugin für Gemeinden, Städte, Landkreise, Satzungen, Räte, Bürgerbegehren, Kommunalfinanzen, Aufsicht und Landesrecht.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kommunalrecht-laender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kommunalrecht-laender.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kommunalrecht-laender/kommunalrecht-laender-werkstatt.md" download><code>kommunalrecht-laender-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kommunalrecht-laender/kommunalrecht-laender-schnellstart.md" download><code>kommunalrecht-laender-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Kommunalakte Morgenfurt: [Gesamt-PDF](../testakten/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt/gesamt-pdf/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt_gesamt.pdf), [`testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip), [`testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin ist die Werkbank für kommunale Selbstverwaltung: Rat, Bürgermeister, Landkreis, Satzung, Gebühren, Haushalt, Bürgerbegehren, Kommunalaufsicht, kommunale Unternehmen und Landesrecht.

## Start

Beginne mit `kommunalrecht-laender-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| 1. Einstieg und Fallrouting | `gemeinderat-landesrecht-routen`, `kaltstart-kommunalrechtsfall`, `kaltstart-triage`, `kommunalabgabe-landesrecht-routen`, `kommunalrecht-baden-wuerttemberg-route`, `kommunalrecht-bayern-berlin-routen`, `kommunalrecht-berlin-routen`, `kommunalrecht-brandenburg-routen`, `kommunalrecht-bremen-routen`, `kommunalrecht-hamburg-routen`, `kommunalrecht-hessen-routen`, `kommunalrecht-niedersachsen-routen`, `kommunalrecht-rheinland-pfalz-routen`, `kommunalrecht-saarland-routen`, `kommunalrecht-sachsen-routen`, `kommunalrecht-schleswig-holstein-route`, `kommunalrecht-thueringen-routen`, `kreistag-landesrecht-routen`, ... plus 4 weitere |
| 4. Gestaltung, Strategie und Verhandlung | `ausschuss-beteiligung-planen`, `buergermeister-beteiligung-planen`, `gemeinderat-beteiligung-planen`, `kita-satzung-beteiligung-planen`, `kommunalabgabe-beteiligung-planen`, `kommunalaufsicht-beteiligung-planen`, `kommunaler-finanzausgleich-interkommunale`, `kreistag-beteiligung-planen`, `landrat-beteiligung-planen`, `ortschaftsrat-beteiligung-planen`, `schultraeger-beteiligung-planen`, `stadtrat-beteiligung-planen`, `strassenreinigung-beteiligung-planen` |
| 5. Verfahren, Behörde und Gericht | `ausschuss-beschluss-bauen`, `ausschuss-eilantrag-vorbereiten`, `ausschuss-landesrecht-beschluss-bauen`, `beschluss-und-befangenheit`, `buergermeister-beschluss-bauen`, `buergermeister-eilantrag-vorbereiten`, `buergermeister-landesrecht-beschluss`, `einwohnerantrag-petition-haushalt`, `feuerwehr-beschluss-bauen`, `feuerwehr-landesrecht-beschluss`, `gemeinderat-beschluss-bauen`, `gemeinderat-eilantrag-vorbereiten`, `kita-satzung-beschluss-bauen`, `kita-satzung-beschluss-bauen-redlinen`, `kita-satzung-eilantrag-vorbereiten`, `kommunalabgabe-beschluss-bauen`, `kommunalabgabe-eilantrag-vorbereiten`, `kommunalaufsicht-beschluss-bauen`, ... plus 15 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `kreistag-aufsichtsbeschwerde-schreiben`, `landrat-aufsichtsbeschwerde-schreiben`, `stadtrat-aufsichtsbeschwerde-schreiben` |
| 8. Spezialmodule und Schnittstellen | `ausschuss-aufsichtsbeschwerde-schreibe`, `ausschuss-dashboard-bauen`, `ausschuss-finanzierung-dashboard-bauen`, `ausschuss-gebuehr-kalkulieren`, `ausschuss-satzung-redlinen`, `ausschuss-zustaendigkeit-ortschaftsrat`, `benutzungsordnung`, `buergerbegehren-und-buergerentscheid`, `buergermeister-aufsichtsbeschwerde-sch`, `buergermeister-dashboard-bauen`, `buergermeister-finanzierung-dashboard`, `buergermeister-gebuehr-kalkulieren`, `buergermeister-satzung-redlinen`, `buergermeister-zustaendigkeit-pruefen`, `eilrechtsschutz-kommunalstreit`, `feuerwehr-zustaendigkeit-pruefen`, `gemeinde-stadt-ratssitzung`, `gemeinderat-aufsichtsbeschwerde-schrei`, ... plus 87 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 176 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ausschuss-aufsichtsbeschwerde-schreibe` | Wenn es um Ausschuss Aufsichtsbeschwerde Schreibe in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-beschluss-bauen` | Wenn es um Ausschuss Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-beteiligung-planen` | Wenn es um Ausschuss Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-dashboard-bauen` | Wenn es um Ausschuss Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-eilantrag-vorbereiten` | Wenn es um Ausschuss Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `ausschuss-finanzierung-dashboard-bauen` | Wenn es um Ausschuss Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-gebuehr-kalkulieren` | Wenn es um Ausschuss Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-landesrecht-beschluss-bauen` | Wenn es um Ausschuss Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-satzung-redlinen` | Wenn es um Ausschuss Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausschuss-zustaendigkeit-ortschaftsrat` | Wenn es um Ausschuss Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `benutzungsordnung` | Wenn es um Benutzungsordnung in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beschluss-und-befangenheit` | Wenn es um Beschluss Und Befangenheit in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergerbegehren-und-buergerentscheid` | Wenn es um Buergerbegehren Und Buergerentscheid in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-aufsichtsbeschwerde-sch` | Wenn es um Buergermeister Aufsichtsbeschwerde Sch in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-beschluss-bauen` | Wenn es um Buergermeister Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-beteiligung-planen` | Wenn es um Buergermeister Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-dashboard-bauen` | Wenn es um Buergermeister Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-eilantrag-vorbereiten` | Wenn es um Buergermeister Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `buergermeister-finanzierung-dashboard` | Wenn es um Buergermeister Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-gebuehr-kalkulieren` | Wenn es um Buergermeister Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-landesrecht-beschluss` | Wenn es um Buergermeister Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-satzung-redlinen` | Wenn es um Buergermeister Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buergermeister-zustaendigkeit-pruefen` | Wenn es um Buergermeister Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eilrechtsschutz-kommunalstreit` | Wenn es um Eilrechtsschutz Kommunalstreit in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einwohnerantrag-petition-haushalt` | Wenn es um Einwohnerantrag Und Petition in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `feuerwehr-beschluss-bauen` | Wenn es um Feuerwehr Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `feuerwehr-landesrecht-beschluss` | Wenn es um Feuerwehr Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `feuerwehr-zustaendigkeit-pruefen` | Wenn es um Feuerwehr Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinde-stadt-ratssitzung` | Wenn es um Gemeinde Stadt Landkreis Zuordnen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-aufsichtsbeschwerde-schrei` | Wenn es um Gemeinderat Aufsichtsbeschwerde Schrei in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-beschluss-bauen` | Wenn es um Gemeinderat Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-beteiligung-planen` | Wenn es um Gemeinderat Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-dashboard-bauen` | Wenn es um Gemeinderat Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-eilantrag-vorbereiten` | Wenn es um Gemeinderat Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `gemeinderat-finanzierung-erklaeren` | Wenn es um Gemeinderat Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-gebuehr-aufsichtsbeschwerde` | Wenn es um Gemeinderat Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-landesrecht-routen` | Wenn es um Gemeinderat Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-satzung-redlinen` | Wenn es um Gemeinderat Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gemeinderat-zustaendigkeit-pruefen` | Wenn es um Gemeinderat Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haushalt-und-haushaltssicherung` | Wenn es um Haushalt Und Haushaltssicherung in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `informationsrechte-ratsmitglied` | Wenn es um Informationsrechte Ratsmitglied in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `interkommunale-zusammenarbeit` | Wenn es um Interkommunale Zusammenarbeit in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-kommunalrechtsfall` | Wenn es um Kaltstart Kommunalrechtsfall in Kommunalrecht der Länder geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Kommunalrecht der Länder - Allgemeiner Einstieg in Kommunalrecht der Länder geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-aufsichtsbeschwerde-schre` | Wenn es um Kita Satzung Aufsichtsbeschwerde Schre in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-beschluss-bauen` | Wenn es um Kita Satzung Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-beschluss-bauen-redlinen` | Wenn es um Kita Satzung Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-beteiligung-planen` | Wenn es um Kita Satzung Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-dashboard-bauen` | Wenn es um Kita Satzung Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-dashboard-bauen-beteiligung` | Wenn es um Kita Satzung Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-eilantrag-vorbereiten` | Wenn es um Kita Satzung Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kita-satzung-gebuehr-kalkulieren` | Wenn es um Kita Satzung Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-satzung-redlinen` | Wenn es um Kita Satzung Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kita-satzung-zustaendigkeit-pruefen` | Wenn es um Kita Satzung Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-003-organ-und-zustaendigkeit-pruefen` | Wenn es um Organ Und Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-006-satzung-entwerfen-und-pruefen` | Wenn es um Satzung Entwerfen Und Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-010-kommunalabgaben-pruefen` | Wenn es um Kommunalabgaben Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-038-gemeinderat-zustaendigkeit-pruefen` | Wenn es um Gemeinderat Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-048-stadtrat-zustaendigkeit-pruefen` | Wenn es um Stadtrat Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-058-kreistag-zustaendigkeit-pruefen` | Wenn es um Kreistag Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-068-buergermeister-zustaendigkeit-pruefen` | Wenn es um Buergermeister Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-078-landrat-zustaendigkeit-pruefen` | Wenn es um Landrat Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-088-ausschuss-zustaendigkeit-pruefen` | Wenn es um Ausschuss Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-098-ortschaftsrat-zustaendigkeit-pruefen` | Wenn es um Ortschaftsrat Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-108-kommunalaufsicht-zustaendigkeit-pruefe` | Wenn es um Kommunalaufsicht Zustaendigkeit Pruefe in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-118-kommunalabgabe-zustaendigkeit-pruefen` | Wenn es um Kommunalabgabe Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-128-strassenreinigung-zustaendigkeit-pruef` | Wenn es um Strassenreinigung Zustaendigkeit Pruef in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-138-kita-satzung-zustaendigkeit-pruefen` | Wenn es um Kita Satzung Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-148-schultraeger-zustaendigkeit-pruefen` | Wenn es um Schultraeger Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kom-158-feuerwehr-zustaendigkeit-pruefen` | Wenn es um Feuerwehr Zustaendigkeit Pruefen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-aufsichtsbeschwerde-sch` | Wenn es um Kommunalabgabe Aufsichtsbeschwerde Sch in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-beschluss-bauen` | Wenn es um Kommunalabgabe Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-beteiligung-planen` | Wenn es um Kommunalabgabe Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-dashboard-bauen` | Wenn es um Kommunalabgabe Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-eilantrag-vorbereiten` | Wenn es um Kommunalabgabe Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kommunalabgabe-finanzierung-erklaeren` | Wenn es um Kommunalabgabe Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-gebuehr` | Wenn es um Kommunalabgabe Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-landesrecht-routen` | Wenn es um Kommunalabgabe Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-satzung-redlinen` | Wenn es um Kommunalabgabe Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgabe-zustaendigkeit-pruefen` | Wenn es um Kommunalabgabe Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalabgaben-pruefen` | Wenn es um Kommunalabgaben Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-aufsichtsbeschwerde-s` | Wenn es um Kommunalaufsicht Aufsichtsbeschwerde S in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-beschluss-bauen` | Wenn es um Kommunalaufsicht Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-beteiligung-planen` | Wenn es um Kommunalaufsicht Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-dashboard-bauen` | Wenn es um Kommunalaufsicht Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-eilantrag-vorbereiten` | Wenn es um Kommunalaufsicht Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kommunalaufsicht-einschalten` | Wenn es um Kommunalaufsicht Einschalten in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-finanzierung-dashboard` | Wenn es um Kommunalaufsicht Finanzierung Erklaere in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-gebuehr-kalkulieren` | Wenn es um Kommunalaufsicht Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-landesrecht-beschluss` | Wenn es um Kommunalaufsicht Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-satzung-redlinen` | Wenn es um Kommunalaufsicht Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalaufsicht-zustaendigkeit-pruefe` | Wenn es um Kommunalaufsicht Zuständigkeit Prüfe in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunaler-finanzausgleich-interkommunale` | Wenn es um Kommunaler Finanzausgleich in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunales-unternehmen` | Wenn es um Kommunales Unternehmen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-baden-wuerttemberg-route` | Wenn es um Kommunalrecht Baden Wuerttemberg Route in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-bayern-berlin-routen` | Wenn es um Kommunalrecht Bayern Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-berlin-routen` | Wenn es um Kommunalrecht Berlin Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-brandenburg-routen` | Wenn es um Kommunalrecht Brandenburg Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-bremen-routen` | Wenn es um Kommunalrecht Bremen Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-hamburg-routen` | Wenn es um Kommunalrecht Hamburg Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-hessen-routen` | Wenn es um Kommunalrecht Hessen Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-in-einfacher-sprache` | Wenn es um Kommunalrecht In Einfacher Sprache in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-mecklenburg-niedersachsen` | Wenn es um Kommunalrecht Mecklenburg Vorpommern R in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-niedersachsen-routen` | Wenn es um Kommunalrecht Niedersachsen Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-nordrhein-westfalen-rout` | Wenn es um Kommunalrecht Nordrhein Westfalen Rout in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-rheinland-pfalz-routen` | Wenn es um Kommunalrecht Rheinland Pfalz Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-saarland-routen` | Wenn es um Kommunalrecht Saarland Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-sachsen-routen` | Wenn es um Kommunalrecht Sachsen Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-sachsen-schleswig-holstein` | Wenn es um Kommunalrecht Sachsen Anhalt Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-schleswig-holstein-route` | Wenn es um Kommunalrecht Schleswig Holstein Route in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommunalrecht-thueringen-routen` | Wenn es um Kommunalrecht Thueringen Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-aufsichtsbeschwerde-schreiben` | Wenn es um Kreistag Aufsichtsbeschwerde Schreiben in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-beschluss-bauen` | Wenn es um Kreistag Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-beteiligung-planen` | Wenn es um Kreistag Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-dashboard-bauen` | Wenn es um Kreistag Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-eilantrag-vorbereiten` | Wenn es um Kreistag Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kreistag-finanzierung-erklaeren` | Wenn es um Kreistag Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-gebuehr-aufsichtsbeschwerde` | Wenn es um Kreistag Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-landesrecht-routen` | Wenn es um Kreistag Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-satzung-redlinen` | Wenn es um Kreistag Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kreistag-zustaendigkeit-pruefen` | Wenn es um Kreistag Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-aufsichtsbeschwerde-schreiben` | Wenn es um Landrat Aufsichtsbeschwerde Schreiben in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-beschluss-bauen` | Wenn es um Landrat Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-beteiligung-planen` | Wenn es um Landrat Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-dashboard-bauen` | Wenn es um Landrat Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-eilantrag-vorbereiten` | Wenn es um Landrat Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `landrat-finanzierung-erklaeren` | Wenn es um Landrat Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-gebuehr-aufsichtsbeschwerde` | Wenn es um Landrat Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-landesrecht-routen` | Wenn es um Landrat Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-satzung-redlinen` | Wenn es um Landrat Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landrat-zustaendigkeit-pruefen` | Wenn es um Landrat Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `oeffentliche-einrichtung` | Wenn es um Oeffentliche Einrichtung in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `organ-gemeinderat-stadtrat-kreistag` | Wenn es um Organ Und Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-aufsichtsbeschwerde-schr` | Wenn es um Ortschaftsrat Aufsichtsbeschwerde Schr in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-beschluss-bauen` | Wenn es um Ortschaftsrat Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-beteiligung-planen` | Wenn es um Ortschaftsrat Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-dashboard-bauen` | Wenn es um Ortschaftsrat Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-eilantrag-vorbereiten` | Wenn es um Ortschaftsrat Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `ortschaftsrat-finanzierung-erklaeren` | Wenn es um Ortschaftsrat Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-gebuehr-aufsichtsbeschwerde` | Wenn es um Ortschaftsrat Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-landesrecht-routen` | Wenn es um Ortschaftsrat Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-satzung-redlinen` | Wenn es um Ortschaftsrat Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ortschaftsrat-zustaendigkeit-pruefen` | Wenn es um Ortschaftsrat Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ratssitzung-und-tagesordnung` | Wenn es um Ratssitzung Und Tagesordnung in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `satzung-entwerfen-und-pruefen` | Wenn es um Satzung Entwerfen Und Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-aufsichtsbeschwerde-schre` | Wenn es um Schultraeger Aufsichtsbeschwerde Schre in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-beschluss-bauen` | Wenn es um Schultraeger Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-beteiligung-planen` | Wenn es um Schultraeger Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-dashboard-bauen` | Wenn es um Schultraeger Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-eilantrag-vorbereiten` | Wenn es um Schultraeger Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schultraeger-finanzierung-erklaeren` | Wenn es um Schultraeger Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-gebuehr-aufsichtsbeschwerde` | Wenn es um Schultraeger Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-landesrecht-routen` | Wenn es um Schultraeger Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-satzung-redlinen` | Wenn es um Schultraeger Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schultraeger-zustaendigkeit-feuerwehr` | Wenn es um Schultraeger Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sondernutzung-im-strassenraum` | Wenn es um Sondernutzung Im Strassenraum in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-aufsichtsbeschwerde-schreiben` | Wenn es um Stadtrat Aufsichtsbeschwerde Schreiben in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-beschluss-bauen` | Wenn es um Stadtrat Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-beteiligung-planen` | Wenn es um Stadtrat Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-dashboard-bauen` | Wenn es um Stadtrat Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-eilantrag-vorbereiten` | Wenn es um Stadtrat Eilantrag Vorbereiten in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `stadtrat-finanzierung-dashboard-bauen` | Wenn es um Stadtrat Finanzierung Erklaeren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-gebuehr-kalkulieren` | Wenn es um Stadtrat Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-landesrecht-beschluss-bauen` | Wenn es um Stadtrat Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-satzung-redlinen` | Wenn es um Stadtrat Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stadtrat-zustaendigkeit-pruefen` | Wenn es um Stadtrat Zuständigkeit Prüfen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-aufsichtsbeschwerde` | Wenn es um Strassenreinigung Aufsichtsbeschwerde in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-beschluss-bauen` | Wenn es um Strassenreinigung Beschluss Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-beteiligung-planen` | Wenn es um Strassenreinigung Beteiligung Planen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-dashboard-bauen` | Wenn es um Strassenreinigung Dashboard Bauen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-eilantrag-vorbereite` | Wenn es um Strassenreinigung Eilantrag Vorbereite in Kommunalrecht der Länder geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `strassenreinigung-finanzierung-erklaer` | Wenn es um Strassenreinigung Finanzierung Erklaer in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-gebuehr` | Wenn es um Strassenreinigung Gebuehr Kalkulieren in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-landesrecht-routen` | Wenn es um Strassenreinigung Landesrecht Routen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-satzung-redlinen` | Wenn es um Strassenreinigung Satzung Redlinen in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strassenreinigung-zustaendigkeit-pruef` | Wenn es um Strassenreinigung Zuständigkeit Prüf in Kommunalrecht der Länder geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

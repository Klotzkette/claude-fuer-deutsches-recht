# Straßenrecht und Infrastruktur

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

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 126 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenplan-infrastruktur` | Straßenrecht und Infrastruktur: Aktenplan Infrastruktur. Aktenplan Infrastruktur im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktu... |
| `anliegergebrauch-abgrenzen` | Straßenrecht und Infrastruktur: Anliegergebrauch abgrenzen. Anliegergebrauch abgrenzen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infras... |
| `autobahn-baulast-pruefen` | Autobahn: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-dashboard-bundesstrasse` | Autobahn: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-dokumente-sortieren` | Autobahn: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-eilantrag-kostenlast` | Autobahn: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-einwendung-bauen` | Autobahn: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-kostenlast-pruefen` | Autobahn: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-planrecht-pruefen` | Autobahn: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-sondernutzung-formulieren` | Autobahn: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-unterhaltung-ruegen` | Autobahn: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `autobahn-widmung-planrecht-sondernutzung` | Autobahn: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `baustelle-verkehrsfuehrung` | Straßenrecht und Infrastruktur: Baustelle und Verkehrsführung. Baustelle und Verkehrsführung im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/... |
| `bruecke-baulast-pruefen` | Brücke: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-dashboard-tunnel-baulast-widmung` | Brücke: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-dokumente-sortieren` | Brücke: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-eilantrag-kostenlast-unterhaltung` | Brücke: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-einwendung-bauen` | Brücke: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-kostenlast-pruefen` | Brücke: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-planrecht-pruefen` | Brücke: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-sondernutzung-formulieren` | Brücke: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-und-tunnel` | Straßenrecht und Infrastruktur: Brücke und Tunnel. Brücke und Tunnel im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktur: prüft kon... |
| `bruecke-unterhaltung-ruegen` | Brücke: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bruecke-widmung-planrecht-sondernutzung` | Brücke: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesfernstrasse-landesstrasse` | Straßenrecht und Infrastruktur: Bundesfernstraße oder Landesstraße. Bundesfernstraße oder Landesstraße im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Str... |
| `bundesstrasse-baulast-pruefen` | Bundesstraße: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-dashboard-erstellen` | Bundesstraße: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-dokumente-sortieren` | Bundesstraße: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-eilantrag-skizzieren` | Bundesstraße: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-einwendung-bauen` | Bundesstraße: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-kostenlast-pruefen` | Bundesstraße: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-planrecht-pruefen` | Bundesstraße: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-sondernutzung-einwendung` | Bundesstraße: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-unterhaltung-dokumente` | Bundesstraße: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `bundesstrasse-widmung-lesen` | Bundesstraße: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `eilrechtsschutz-aktenplan-infrastruktur` | Straßenrecht und Infrastruktur: Eilrechtsschutz gegen Bau. Eilrechtsschutz gegen Bau im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastr... |
| `gemeindestrasse-baulast-pruefen` | Gemeindestraße: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-dashboard-ortsdurchfahrt` | Gemeindestraße: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-dokumente-sortieren` | Gemeindestraße: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-eilantrag-kostenlast` | Gemeindestraße: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-einwendung-bauen` | Gemeindestraße: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-kostenlast-pruefen` | Gemeindestraße: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-planrecht-pruefen` | Gemeindestraße: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-sondernutzung-formulie` | Gemeindestraße: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-unterhaltung-ruegen` | Gemeindestraße: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `gemeindestrasse-widmung-planrecht` | Gemeindestraße: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kaltstart-strassenrechtsfall` | Straßenrecht und Infrastruktur: Kaltstart Straßenrechtsfall. Kaltstart Straßenrechtsfall im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `kaltstart-triage` | Straßenrecht und Infrastruktur: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `kreisstrasse-baulast-pruefen` | Kreisstraße: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-dashboard-erstellen` | Kreisstraße: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-dokumente-sortieren` | Kreisstraße: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-eilantrag-skizzieren` | Kreisstraße: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-einwendung-bauen` | Kreisstraße: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-kostenlast-pruefen` | Kreisstraße: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-planrecht-pruefen` | Kreisstraße: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-sondernutzung-einwendung` | Kreisstraße: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-unterhaltung-dokumente` | Kreisstraße: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreisstrasse-widmung-lesen` | Kreisstraße: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kreuzungsrecht-strassenausbaubeitrag` | Straßenrecht und Infrastruktur: Kreuzungsrecht Bahn Wasser Straße. Kreuzungsrecht Bahn Wasser Straße im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straß... |
| `landesstrasse-baulast-pruefen` | Landesstraße: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-dashboard` | Landesstraße: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-dokumente-sortieren` | Landesstraße: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-eilantrag-kostenlast` | Landesstraße: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-einwendung-bauen` | Landesstraße: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-kostenlast-pruefen` | Landesstraße: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-planrecht-pruefen` | Landesstraße: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-sondernutzung-formuliere` | Landesstraße: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-unterhaltung-ruegen` | Landesstraße: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrasse-widmung-planrecht` | Landesstraße: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `landesstrassengesetz-livecheck` | Straßenrecht und Infrastruktur: Landesstraßengesetz-Livecheck. Landesstraßengesetz-Livecheck im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/... |
| `ortsdurchfahrt-baulast-pruefen` | Ortsdurchfahrt: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-dashboard-erstellen` | Ortsdurchfahrt: Dashboard erstellen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-dokumente-sortieren` | Ortsdurchfahrt: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-eilantrag-skizzieren` | Ortsdurchfahrt: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-einwendung-bauen` | Ortsdurchfahrt: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-kostenlast-pruefen` | Ortsdurchfahrt: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-planrecht-pruefen` | Ortsdurchfahrt: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-sondernutzung-einwendung` | Ortsdurchfahrt: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-unterhaltung-dokumente` | Ortsdurchfahrt: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `ortsdurchfahrt-widmung-lesen` | Ortsdurchfahrt: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `planfeststellung-strasse-plangenehmigung` | Straßenrecht und Infrastruktur: Planfeststellung Straße. Planfeststellung Straße im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktu... |
| `plangenehmigung-und-uvp` | Straßenrecht und Infrastruktur: Plangenehmigung und UVP. Plangenehmigung und UVP im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktu... |
| `rastanlage-und-nebenbetrieb` | Straßenrecht und Infrastruktur: Rastanlage und Nebenbetrieb. Rastanlage und Nebenbetrieb im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infr... |
| `schaeden-durch-strasse` | Straßenrecht und Infrastruktur: Schäden durch Straße. Schäden durch Straße im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktur: prü... |
| `sondernutzungserlaubnis` | Straßenrecht und Infrastruktur: Sondernutzungserlaubnis. Sondernutzungserlaubnis im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktu... |
| `str-004-widmung-und-einziehung-pruefen` | Straßenrecht und Infrastruktur: Widmung und Einziehung prüfen. Widmung und Einziehung prüfen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `str-015-strassenausbaubeitrag-pruefen` | Straßenrecht und Infrastruktur: Straßenausbaubeitrag prüfen. Straßenausbaubeitrag prüfen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `str-021-autobahn-baulast-pruefen` | Straßenrecht und Infrastruktur: Autobahn: Baulast prüfen. Baulast prüfen für Autobahn im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-023-autobahn-planrecht-pruefen` | Straßenrecht und Infrastruktur: Autobahn: Planrecht prüfen. Planrecht prüfen für Autobahn im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-027-autobahn-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Autobahn: Kostenlast prüfen. Kostenlast prüfen für Autobahn im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-031-bundesstrasse-baulast-pruefen` | Straßenrecht und Infrastruktur: Bundesstraße: Baulast prüfen. Baulast prüfen für Bundesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-033-bundesstrasse-planrecht-pruefen` | Straßenrecht und Infrastruktur: Bundesstraße: Planrecht prüfen. Planrecht prüfen für Bundesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-037-bundesstrasse-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Bundesstraße: Kostenlast prüfen. Kostenlast prüfen für Bundesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-041-landesstrasse-baulast-pruefen` | Straßenrecht und Infrastruktur: Landesstraße: Baulast prüfen. Baulast prüfen für Landesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-043-landesstrasse-planrecht-pruefen` | Straßenrecht und Infrastruktur: Landesstraße: Planrecht prüfen. Planrecht prüfen für Landesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-047-landesstrasse-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Landesstraße: Kostenlast prüfen. Kostenlast prüfen für Landesstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-051-kreisstrasse-baulast-pruefen` | Straßenrecht und Infrastruktur: Kreisstraße: Baulast prüfen. Baulast prüfen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-053-kreisstrasse-planrecht-pruefen` | Straßenrecht und Infrastruktur: Kreisstraße: Planrecht prüfen. Planrecht prüfen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-057-kreisstrasse-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Kreisstraße: Kostenlast prüfen. Kostenlast prüfen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-061-gemeindestrasse-baulast-pruefen` | Straßenrecht und Infrastruktur: Gemeindestraße: Baulast prüfen. Baulast prüfen für Gemeindestraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-063-gemeindestrasse-planrecht-pruefen` | Straßenrecht und Infrastruktur: Gemeindestraße: Planrecht prüfen. Planrecht prüfen für Gemeindestraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-067-gemeindestrasse-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Gemeindestraße: Kostenlast prüfen. Kostenlast prüfen für Gemeindestraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-071-ortsdurchfahrt-baulast-pruefen` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Baulast prüfen. Baulast prüfen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-073-ortsdurchfahrt-planrecht-pruefen` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Planrecht prüfen. Planrecht prüfen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-077-ortsdurchfahrt-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Kostenlast prüfen. Kostenlast prüfen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-081-bruecke-baulast-pruefen` | Straßenrecht und Infrastruktur: Brücke: Baulast prüfen. Baulast prüfen für Brücke im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-083-bruecke-planrecht-pruefen` | Straßenrecht und Infrastruktur: Brücke: Planrecht prüfen. Planrecht prüfen für Brücke im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-087-bruecke-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Brücke: Kostenlast prüfen. Kostenlast prüfen für Brücke im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-091-tunnel-baulast-pruefen` | Straßenrecht und Infrastruktur: Tunnel: Baulast prüfen. Baulast prüfen für Tunnel im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-093-tunnel-planrecht-pruefen` | Straßenrecht und Infrastruktur: Tunnel: Planrecht prüfen. Planrecht prüfen für Tunnel im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-097-tunnel-kostenlast-pruefen` | Straßenrecht und Infrastruktur: Tunnel: Kostenlast prüfen. Kostenlast prüfen für Tunnel im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `strassenausbaubeitrag-pruefen` | Straßenrecht und Infrastruktur: Straßenausbaubeitrag prüfen. Straßenausbaubeitrag prüfen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infr... |
| `strassenbaulasttraeger-bestimmen` | Straßenrecht und Infrastruktur: Straßenbaulastträger bestimmen. Straßenbaulastträger bestimmen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrech... |
| `strassenentwaesserung` | Straßenrecht und Infrastruktur: Straßenentwässerung. Straßenentwässerung im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/Infrastruktur: prüft... |
| `tunnel-baulast-pruefen` | Tunnel: Baulast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-dokumente-sortieren` | Tunnel: Dokumente sortieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-eilantrag-skizzieren` | Tunnel: Eilantrag skizzieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-einwendung-bauen` | Tunnel: Einwendung bauen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-kostenlast-pruefen` | Tunnel: Kostenlast prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-planrecht-pruefen` | Tunnel: Planrecht prüfen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-sondernutzung-einwendung-bauen` | Tunnel: Sondernutzung formulieren im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-unterhaltung-dokumente` | Tunnel: Unterhaltung rügen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `tunnel-widmung-lesen` | Tunnel: Widmung lesen im Straßenrecht und Infrastruktur: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `umstufung-und-teileinziehung` | Straßenrecht und Infrastruktur: Umstufung und Teileinziehung. Umstufung und Teileinziehung im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/In... |
| `unterhaltungspflicht-und-winterdienst` | Straßenrecht und Infrastruktur: Unterhaltungspflicht und Winterdienst. Unterhaltungspflicht und Winterdienst im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten... |
| `widmung-und-einziehung-pruefen` | Straßenrecht und Infrastruktur: Widmung und Einziehung prüfen. Widmung und Einziehung prüfen im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Straßenrecht/... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

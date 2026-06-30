# Betäubungsmittelrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Betäubungsmittelrecht-Plugin für BtMG, BtMVV, KCanG/MedCanG-Schnittstellen, Strafverfahren, Therapie, ärztliche Praxis, Apotheken und Compliance.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`betaeubungsmittelrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betaeubungsmittelrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/betaeubungsmittelrecht/betaeubungsmittelrecht-werkstatt.md" download><code>betaeubungsmittelrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/betaeubungsmittelrecht/betaeubungsmittelrecht-schnellstart.md" download><code>betaeubungsmittelrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | BtM-Akte: [Gesamt-PDF](../testakten/betaeubungsmittelrecht-apotheke-substitution-festival/gesamt-pdf/betaeubungsmittelrecht-apotheke-substitution-festival_gesamt.pdf), [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip), [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin behandelt BtM nicht nur strafrechtlich: Verkehrsfähigkeit, Verschreibung, Apotheke, ärztliche Praxis, Erlaubnis, Strafverteidigung, Therapie, Cannabis-Schnittstelle und Compliance werden getrennt geführt.

## Start

Beginne mit `betaeubungsmittelrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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

Automatisch generierte Komplett-Liste aller 125 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amphetamin-akteneinsicht-vorbereiten` | Amphetamin: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-bauen-akteneinsicht` | Amphetamin: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-einlassung-planen` | Amphetamin: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-erlaubnis-pruefen` | Amphetamin: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-mandantenbrief-schreiben` | Amphetamin: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-menge-einordnen` | Amphetamin: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-sichern-einlassung-planen` | Amphetamin: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-stoff-pruefen` | Amphetamin: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-strafrahmen-routen` | Amphetamin: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `amphetamin-therapiepfad-pruefen` | Amphetamin: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `apotheke-btm-dokumentation` | Betäubungsmittelrecht: Apotheke BtM-Dokumentation. Apotheke BtM-Dokumentation im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `arztpraxis-compliance` | Betäubungsmittelrecht: Arztpraxis Compliance. Arztpraxis Compliance im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `aufklaerungshilfe-btmg-kcang-medcang-abgrenzen-neue` | Betäubungsmittelrecht: Aufklärungshilfe § 31 BtMG. Aufklärungshilfe § 31 BtMG im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `betriebspruefung-apotheke` | Betäubungsmittelrecht: Betriebsprüfung Apotheke. Betriebsprüfung Apotheke im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `btm-002-stoff-und-anlage-pruefen` | Betäubungsmittelrecht: Stoff und Anlage prüfen. Stoff und Anlage prüfen im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `btm-021-cannabis-stoff-pruefen` | Betäubungsmittelrecht: Cannabis: Stoff prüfen. Stoff prüfen für Cannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-026-cannabis-therapiepfad-pruefen` | Betäubungsmittelrecht: Cannabis: Therapiepfad prüfen. Therapiepfad prüfen für Cannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-027-cannabis-erlaubnis-pruefen` | Betäubungsmittelrecht: Cannabis: Erlaubnis prüfen. Erlaubnis prüfen für Cannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-031-kokain-stoff-pruefen` | Betäubungsmittelrecht: Kokain: Stoff prüfen. Stoff prüfen für Kokain im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-036-kokain-therapiepfad-pruefen` | Betäubungsmittelrecht: Kokain: Therapiepfad prüfen. Therapiepfad prüfen für Kokain im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-037-kokain-erlaubnis-pruefen` | Betäubungsmittelrecht: Kokain: Erlaubnis prüfen. Erlaubnis prüfen für Kokain im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-041-heroin-stoff-pruefen` | Betäubungsmittelrecht: Heroin: Stoff prüfen. Stoff prüfen für Heroin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-046-heroin-therapiepfad-pruefen` | Betäubungsmittelrecht: Heroin: Therapiepfad prüfen. Therapiepfad prüfen für Heroin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-047-heroin-erlaubnis-pruefen` | Betäubungsmittelrecht: Heroin: Erlaubnis prüfen. Erlaubnis prüfen für Heroin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-051-amphetamin-stoff-pruefen` | Betäubungsmittelrecht: Amphetamin: Stoff prüfen. Stoff prüfen für Amphetamin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-056-amphetamin-therapiepfad-pruefen` | Betäubungsmittelrecht: Amphetamin: Therapiepfad prüfen. Therapiepfad prüfen für Amphetamin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-057-amphetamin-erlaubnis-pruefen` | Betäubungsmittelrecht: Amphetamin: Erlaubnis prüfen. Erlaubnis prüfen für Amphetamin im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-061-mdma-stoff-pruefen` | Betäubungsmittelrecht: MDMA: Stoff prüfen. Stoff prüfen für MDMA im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-066-mdma-therapiepfad-pruefen` | Betäubungsmittelrecht: MDMA: Therapiepfad prüfen. Therapiepfad prüfen für MDMA im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-067-mdma-erlaubnis-pruefen` | Betäubungsmittelrecht: MDMA: Erlaubnis prüfen. Erlaubnis prüfen für MDMA im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-071-fentanyl-stoff-pruefen` | Betäubungsmittelrecht: Fentanyl: Stoff prüfen. Stoff prüfen für Fentanyl im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-076-fentanyl-therapiepfad-pruefen` | Betäubungsmittelrecht: Fentanyl: Therapiepfad prüfen. Therapiepfad prüfen für Fentanyl im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-077-fentanyl-erlaubnis-pruefen` | Betäubungsmittelrecht: Fentanyl: Erlaubnis prüfen. Erlaubnis prüfen für Fentanyl im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-081-methadon-stoff-pruefen` | Betäubungsmittelrecht: Methadon: Stoff prüfen. Stoff prüfen für Methadon im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-086-methadon-therapiepfad-pruefen` | Betäubungsmittelrecht: Methadon: Therapiepfad prüfen. Therapiepfad prüfen für Methadon im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-087-methadon-erlaubnis-pruefen` | Betäubungsmittelrecht: Methadon: Erlaubnis prüfen. Erlaubnis prüfen für Methadon im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-091-medizinalcannabis-stoff-pruefen` | Betäubungsmittelrecht: Medizinalcannabis: Stoff prüfen. Stoff prüfen für Medizinalcannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-096-medizinalcannabis-therapiepfad-pruefen` | Betäubungsmittelrecht: Medizinalcannabis: Therapiepfad prüfen. Therapiepfad prüfen für Medizinalcannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-097-medizinalcannabis-erlaubnis-pruefen` | Betäubungsmittelrecht: Medizinalcannabis: Erlaubnis prüfen. Erlaubnis prüfen für Medizinalcannabis im Rahmen von Betäubungsmittelrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `btm-in-einfacher-sprache` | Betäubungsmittelrecht: BtM in einfacher Sprache. BtM in einfacher Sprache im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `cannabis-akteneinsicht-vorbereiten` | Cannabis: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-beweis-sichern` | Cannabis: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-compliance-bauen` | Cannabis: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-einlassung-planen` | Cannabis: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-erlaubnis-pruefen` | Cannabis: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-mandantenbrief-kokain-stoff` | Cannabis: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-menge-strafrahmen-routen-sichern` | Cannabis: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-stoff-pruefen` | Cannabis: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-strafrahmen-routen` | Cannabis: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `cannabis-therapiepfad-erlaubnis-bauen` | Cannabis: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `durchsuchung-und-beschlagnahme` | Betäubungsmittelrecht: Durchsuchung und Beschlagnahme. Durchsuchung und Beschlagnahme im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `einfuhr-ausfuhr-durchfuhr` | Betäubungsmittelrecht: Einfuhr Ausfuhr Durchfuhr. Einfuhr Ausfuhr Durchfuhr im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `einziehung-und-wertersatz` | Betäubungsmittelrecht: Einziehung und Wertersatz. Einziehung und Wertersatz im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `fahrerlaubnis-und-btm` | Betäubungsmittelrecht: Fahrerlaubnis und BtM. Fahrerlaubnis und BtM im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `fentanyl-akteneinsicht-vorbereiten` | Fentanyl: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-bauen-akteneinsicht-vorbereiten` | Fentanyl: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-einlassung-planen` | Fentanyl: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-erlaubnis-pruefen` | Fentanyl: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-mandantenbrief-schreiben` | Fentanyl: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-menge-einordnen` | Fentanyl: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-sichern-einlassung-planen` | Fentanyl: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-stoff-pruefen` | Fentanyl: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-strafrahmen-routen` | Fentanyl: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `fentanyl-therapiepfad-pruefen` | Fentanyl: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `handeltreiben-oder-besitz` | Betäubungsmittelrecht: Handeltreiben oder Besitz. Handeltreiben oder Besitz im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `heroin-akteneinsicht-vorbereiten` | Heroin: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-beweis-sichern` | Heroin: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-compliance-bauen` | Heroin: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-einlassung-planen` | Heroin: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-erlaubnis-pruefen` | Heroin: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-mandantenbrief-amphetamin-stoff` | Heroin: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-menge-strafrahmen-routen-sichern` | Heroin: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-stoff-pruefen` | Heroin: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-strafrahmen-routen` | Heroin: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `heroin-therapiepfad-erlaubnis-bauen` | Heroin: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `internationaler-versand-betriebspruefung-apotheke-einfacher` | Betäubungsmittelrecht: Internationaler Versand. Internationaler Versand im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `jugendliche-und-btm` | Betäubungsmittelrecht: Jugendliche und BtM. Jugendliche und BtM im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `kaltstart-fall` | Betäubungsmittelrecht: Kaltstart BtM-Fall. Kaltstart BtM-Fall im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `kaltstart-triage` | Betäubungsmittelrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `kcang-und-medcang-abgrenzen` | Betäubungsmittelrecht: KCanG und MedCanG abgrenzen. KCanG und MedCanG abgrenzen im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `kokain-akteneinsicht-vorbereiten` | Kokain: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-bauen-akteneinsicht-vorbereiten` | Kokain: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-einlassung-planen` | Kokain: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-erlaubnis-pruefen` | Kokain: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-mandantenbrief-schreiben` | Kokain: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-menge-einordnen` | Kokain: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-sichern-einlassung-planen` | Kokain: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-stoff-pruefen` | Kokain: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-strafrahmen-routen` | Kokain: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `kokain-therapiepfad-pruefen` | Kokain: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-akteneinsicht-vorbereiten` | MDMA: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-beweis-sichern` | MDMA: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-compliance-bauen` | MDMA: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-einlassung-planen` | MDMA: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-erlaubnis-pruefen` | MDMA: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-mandantenbrief-fentanyl-stoff-menge` | MDMA: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-menge-strafrahmen-routen-sichern` | MDMA: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-stoff-pruefen` | MDMA: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-strafrahmen-routen` | MDMA: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `mdma-therapiepfad-erlaubnis-bauen` | MDMA: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-akteneinsicht-vorber` | Medizinalcannabis: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-beweis-sichern-einlassung-planen` | Medizinalcannabis: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-compliance-bauen-akteneinsicht-vorber` | Medizinalcannabis: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-einlassung-planen` | Medizinalcannabis: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-erlaubnis-pruefen` | Medizinalcannabis: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-menge-einordnen` | Medizinalcannabis: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-stoff-pruefen` | Medizinalcannabis: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-strafrahmen-routen` | Medizinalcannabis: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `medizinalcannabis-therapiepfad-pruefen` | Medizinalcannabis: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-akteneinsicht-vorbereiten` | Methadon: Akteneinsicht vorbereiten im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-beweis-sichern` | Methadon: Beweis sichern im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-compliance-bauen` | Methadon: Compliance bauen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-einlassung-planen` | Methadon: Einlassung planen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-erlaubnis-pruefen` | Methadon: Erlaubnis prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-mandantenbrief-medizinalcannabis` | Methadon: Mandantenbrief schreiben im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-menge-strafrahmen-routen-sichern` | Methadon: Menge einordnen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-stoff-pruefen` | Methadon: Stoff prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-strafrahmen-routen` | Methadon: Strafrahmen routen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `methadon-therapiepfad-erlaubnis-bauen` | Methadon: Therapiepfad prüfen im Betäubungsmittelrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung dieses Spezialthemas. |
| `neue-psychoaktive-stoffe` | Betäubungsmittelrecht: Neue psychoaktive Stoffe. Neue psychoaktive Stoffe im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `nicht-geringe-menge-livecheck` | Betäubungsmittelrecht: Nicht geringe Menge Livecheck. Nicht geringe Menge Livecheck im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `rezept-btmvv-arztpraxis-compliance-apotheke-dokumentation` | Betäubungsmittelrecht: BtM-Rezept und BtMVV. BtM-Rezept und BtMVV im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `stoff-und-anlage-pruefen` | Betäubungsmittelrecht: Stoff und Anlage prüfen. Stoff und Anlage prüfen im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `therapie-statt-strafe` | Betäubungsmittelrecht: Therapie statt Strafe. Therapie statt Strafe im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |
| `u-haft-in-btm-sache` | Betäubungsmittelrecht: U-Haft in BtM-Sache. U-Haft in BtM-Sache im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Betäubungsmittelrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

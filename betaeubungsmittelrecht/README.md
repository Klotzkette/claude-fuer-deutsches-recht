# Betäubungsmittelrecht


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`betaeubungsmittelrecht`) | [`betaeubungsmittelrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betaeubungsmittelrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BtM-Akte** (`betaeubungsmittelrecht-apotheke-substitution-festival`) | [Gesamt-PDF lesen](../testakten/betaeubungsmittelrecht-apotheke-substitution-festival/gesamt-pdf/betaeubungsmittelrecht-apotheke-substitution-festival_gesamt.pdf) | [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `amphetamin-strafrahmen-routen`, `cannabis-menge-strafrahmen-routen-sichern`, `cannabis-strafrahmen-routen`, `fentanyl-strafrahmen-routen`, `heroin-menge-strafrahmen-routen-sichern`, `heroin-strafrahmen-routen`, `kaltstart-fall`, `kaltstart-triage`, `kokain-strafrahmen-routen`, `mdma-menge-strafrahmen-routen-sichern`, `mdma-strafrahmen-routen`, `medizinalcannabis-strafrahmen-routen`, `methadon-menge-strafrahmen-routen-sichern`, `methadon-strafrahmen-routen` |
| 2. Unterlagen, Sachverhalt und Quellen | `amphetamin-akteneinsicht-vorbereiten`, `amphetamin-bauen-akteneinsicht`, `apotheke-btm-dokumentation`, `cannabis-akteneinsicht-vorbereiten`, `cannabis-beweis-sichern`, `fentanyl-akteneinsicht-vorbereiten`, `fentanyl-bauen-akteneinsicht-vorbereiten`, `heroin-akteneinsicht-vorbereiten`, `heroin-beweis-sichern`, `kokain-akteneinsicht-vorbereiten`, `kokain-bauen-akteneinsicht-vorbereiten`, `mdma-akteneinsicht-vorbereiten`, `mdma-beweis-sichern`, `medizinalcannabis-akteneinsicht-vorber`, `medizinalcannabis-beweis-sichern-einlassung-planen`, `medizinalcannabis-compliance-bauen-akteneinsicht-vorber`, `methadon-akteneinsicht-vorbereiten`, `methadon-beweis-sichern`, ... plus 1 weitere |
| 3. Prüfung, Anspruch und Subsumtion | `betriebspruefung-apotheke`, `internationaler-versand-betriebspruefung-apotheke-einfacher`, `nicht-geringe-menge-livecheck` |
| 4. Gestaltung, Strategie und Verhandlung | `amphetamin-einlassung-planen`, `amphetamin-sichern-einlassung-planen`, `arztpraxis-compliance`, `cannabis-compliance-bauen`, `cannabis-einlassung-planen`, `fentanyl-einlassung-planen`, `fentanyl-sichern-einlassung-planen`, `heroin-compliance-bauen`, `heroin-einlassung-planen`, `kokain-einlassung-planen`, `kokain-sichern-einlassung-planen`, `mdma-compliance-bauen`, `mdma-einlassung-planen`, `medizinalcannabis-einlassung-planen`, `methadon-compliance-bauen`, `methadon-einlassung-planen` |
| 6. Ergebnis, Schreiben und Kommunikation | `amphetamin-mandantenbrief-schreiben`, `cannabis-mandantenbrief-kokain-stoff`, `fentanyl-mandantenbrief-schreiben`, `heroin-mandantenbrief-amphetamin-stoff`, `kokain-mandantenbrief-schreiben`, `mdma-mandantenbrief-fentanyl-stoff-menge`, `methadon-mandantenbrief-medizinalcannabis` |
| 8. Spezialmodule und Schnittstellen | `amphetamin-erlaubnis-pruefen`, `amphetamin-menge-einordnen`, `amphetamin-stoff-pruefen`, `amphetamin-therapiepfad-pruefen`, `aufklaerungshilfe-btmg-kcang-medcang-abgrenzen-neue`, `btm-002-stoff-und-anlage-pruefen`, `btm-021-cannabis-stoff-pruefen`, `btm-026-cannabis-therapiepfad-pruefen`, `btm-027-cannabis-erlaubnis-pruefen`, `btm-031-kokain-stoff-pruefen`, `btm-036-kokain-therapiepfad-pruefen`, `btm-037-kokain-erlaubnis-pruefen`, `btm-041-heroin-stoff-pruefen`, `btm-046-heroin-therapiepfad-pruefen`, `btm-047-heroin-erlaubnis-pruefen`, `btm-051-amphetamin-stoff-pruefen`, `btm-056-amphetamin-therapiepfad-pruefen`, `btm-057-amphetamin-erlaubnis-pruefen`, ... plus 48 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 125 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amphetamin-akteneinsicht-vorbereiten` | Wenn es um Amphetamin Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `amphetamin-bauen-akteneinsicht` | Wenn es um Amphetamin Compliance Bauen in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `amphetamin-einlassung-planen` | Wenn es um Amphetamin Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-erlaubnis-pruefen` | Wenn es um Amphetamin Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-mandantenbrief-schreiben` | Wenn es um Amphetamin Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `amphetamin-menge-einordnen` | Wenn es um Amphetamin Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-sichern-einlassung-planen` | Wenn es um Amphetamin Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-stoff-pruefen` | Wenn es um Amphetamin Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-strafrahmen-routen` | Wenn es um Amphetamin Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `amphetamin-therapiepfad-pruefen` | Wenn es um Amphetamin Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `apotheke-btm-dokumentation` | Wenn es um Apotheke Btm Dokumentation in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `arztpraxis-compliance` | Wenn es um Arztpraxis Compliance in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufklaerungshilfe-btmg-kcang-medcang-abgrenzen-neue` | Wenn es um Aufklaerungshilfe 31 Btmg in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `betriebspruefung-apotheke` | Wenn es um Betriebspruefung Apotheke in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-002-stoff-und-anlage-pruefen` | Wenn es um Stoff Und Anlage Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-021-cannabis-stoff-pruefen` | Wenn es um Cannabis Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-026-cannabis-therapiepfad-pruefen` | Wenn es um Cannabis Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-027-cannabis-erlaubnis-pruefen` | Wenn es um Cannabis Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-031-kokain-stoff-pruefen` | Wenn es um Kokain Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-036-kokain-therapiepfad-pruefen` | Wenn es um Kokain Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-037-kokain-erlaubnis-pruefen` | Wenn es um Kokain Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-041-heroin-stoff-pruefen` | Wenn es um Heroin Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-046-heroin-therapiepfad-pruefen` | Wenn es um Heroin Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-047-heroin-erlaubnis-pruefen` | Wenn es um Heroin Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-051-amphetamin-stoff-pruefen` | Wenn es um Amphetamin Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-056-amphetamin-therapiepfad-pruefen` | Wenn es um Amphetamin Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-057-amphetamin-erlaubnis-pruefen` | Wenn es um Amphetamin Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-061-mdma-stoff-pruefen` | Wenn es um Mdma Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-066-mdma-therapiepfad-pruefen` | Wenn es um Mdma Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-067-mdma-erlaubnis-pruefen` | Wenn es um Mdma Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-071-fentanyl-stoff-pruefen` | Wenn es um Fentanyl Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-076-fentanyl-therapiepfad-pruefen` | Wenn es um Fentanyl Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-077-fentanyl-erlaubnis-pruefen` | Wenn es um Fentanyl Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-081-methadon-stoff-pruefen` | Wenn es um Methadon Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-086-methadon-therapiepfad-pruefen` | Wenn es um Methadon Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-087-methadon-erlaubnis-pruefen` | Wenn es um Methadon Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-091-medizinalcannabis-stoff-pruefen` | Wenn es um Medizinalcannabis Stoff Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-096-medizinalcannabis-therapiepfad-pruefen` | Wenn es um Medizinalcannabis Therapiepfad Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-097-medizinalcannabis-erlaubnis-pruefen` | Wenn es um Medizinalcannabis Erlaubnis Pruefen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `btm-in-einfacher-sprache` | Wenn es um Btm In Einfacher Sprache in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-akteneinsicht-vorbereiten` | Wenn es um Cannabis Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `cannabis-beweis-sichern` | Wenn es um Cannabis Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-compliance-bauen` | Wenn es um Cannabis Compliance Bauen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-einlassung-planen` | Wenn es um Cannabis Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-erlaubnis-pruefen` | Wenn es um Cannabis Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-mandantenbrief-kokain-stoff` | Wenn es um Cannabis Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `cannabis-menge-strafrahmen-routen-sichern` | Wenn es um Cannabis Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-stoff-pruefen` | Wenn es um Cannabis Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-strafrahmen-routen` | Wenn es um Cannabis Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cannabis-therapiepfad-erlaubnis-bauen` | Wenn es um Cannabis Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `durchsuchung-und-beschlagnahme` | Wenn es um Durchsuchung Und Beschlagnahme in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einfuhr-ausfuhr-durchfuhr` | Wenn es um Einfuhr Ausfuhr Durchfuhr in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einziehung-und-wertersatz` | Wenn es um Einziehung Und Wertersatz in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrerlaubnis-und-btm` | Wenn es um Fahrerlaubnis Und Btm in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-akteneinsicht-vorbereiten` | Wenn es um Fentanyl Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `fentanyl-bauen-akteneinsicht-vorbereiten` | Wenn es um Fentanyl Compliance Bauen in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `fentanyl-einlassung-planen` | Wenn es um Fentanyl Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-erlaubnis-pruefen` | Wenn es um Fentanyl Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-mandantenbrief-schreiben` | Wenn es um Fentanyl Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fentanyl-menge-einordnen` | Wenn es um Fentanyl Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-sichern-einlassung-planen` | Wenn es um Fentanyl Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-stoff-pruefen` | Wenn es um Fentanyl Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-strafrahmen-routen` | Wenn es um Fentanyl Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fentanyl-therapiepfad-pruefen` | Wenn es um Fentanyl Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `handeltreiben-oder-besitz` | Wenn es um Handeltreiben Oder Besitz in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-akteneinsicht-vorbereiten` | Wenn es um Heroin Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `heroin-beweis-sichern` | Wenn es um Heroin Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-compliance-bauen` | Wenn es um Heroin Compliance Bauen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-einlassung-planen` | Wenn es um Heroin Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-erlaubnis-pruefen` | Wenn es um Heroin Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-mandantenbrief-amphetamin-stoff` | Wenn es um Heroin Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `heroin-menge-strafrahmen-routen-sichern` | Wenn es um Heroin Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-stoff-pruefen` | Wenn es um Heroin Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-strafrahmen-routen` | Wenn es um Heroin Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `heroin-therapiepfad-erlaubnis-bauen` | Wenn es um Heroin Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `internationaler-versand-betriebspruefung-apotheke-einfacher` | Wenn es um Internationaler Versand in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `jugendliche-und-btm` | Wenn es um Jugendliche Und Btm in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-fall` | Wenn es um Kaltstart Btm Fall in Betäubungsmittelrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Betäubungsmittelrecht - Allgemeiner Einstieg in Betäubungsmittelrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kcang-und-medcang-abgrenzen` | Wenn es um Kcang Und Medcang Abgrenzen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-akteneinsicht-vorbereiten` | Wenn es um Kokain Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `kokain-bauen-akteneinsicht-vorbereiten` | Wenn es um Kokain Compliance Bauen in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `kokain-einlassung-planen` | Wenn es um Kokain Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-erlaubnis-pruefen` | Wenn es um Kokain Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-mandantenbrief-schreiben` | Wenn es um Kokain Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kokain-menge-einordnen` | Wenn es um Kokain Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-sichern-einlassung-planen` | Wenn es um Kokain Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-stoff-pruefen` | Wenn es um Kokain Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-strafrahmen-routen` | Wenn es um Kokain Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kokain-therapiepfad-pruefen` | Wenn es um Kokain Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-akteneinsicht-vorbereiten` | Wenn es um Mdma Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `mdma-beweis-sichern` | Wenn es um Mdma Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-compliance-bauen` | Wenn es um Mdma Compliance Bauen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-einlassung-planen` | Wenn es um Mdma Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-erlaubnis-pruefen` | Wenn es um Mdma Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-mandantenbrief-fentanyl-stoff-menge` | Wenn es um Mdma Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mdma-menge-strafrahmen-routen-sichern` | Wenn es um Mdma Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-stoff-pruefen` | Wenn es um Mdma Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-strafrahmen-routen` | Wenn es um Mdma Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mdma-therapiepfad-erlaubnis-bauen` | Wenn es um Mdma Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-akteneinsicht-vorber` | Wenn es um Medizinalcannabis Akteneinsicht Vorber in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `medizinalcannabis-beweis-sichern-einlassung-planen` | Wenn es um Medizinalcannabis Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-compliance-bauen-akteneinsicht-vorber` | Wenn es um Medizinalcannabis Compliance Bauen in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `medizinalcannabis-einlassung-planen` | Wenn es um Medizinalcannabis Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-erlaubnis-pruefen` | Wenn es um Medizinalcannabis Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-menge-einordnen` | Wenn es um Medizinalcannabis Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-stoff-pruefen` | Wenn es um Medizinalcannabis Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-strafrahmen-routen` | Wenn es um Medizinalcannabis Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `medizinalcannabis-therapiepfad-pruefen` | Wenn es um Medizinalcannabis Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-akteneinsicht-vorbereiten` | Wenn es um Methadon Akteneinsicht Vorbereiten in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `methadon-beweis-sichern` | Wenn es um Methadon Beweis Sichern in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-compliance-bauen` | Wenn es um Methadon Compliance Bauen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-einlassung-planen` | Wenn es um Methadon Einlassung Planen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-erlaubnis-pruefen` | Wenn es um Methadon Erlaubnis Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-mandantenbrief-medizinalcannabis` | Wenn es um Methadon Mandantenbrief Schreiben in Betäubungsmittelrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `methadon-menge-strafrahmen-routen-sichern` | Wenn es um Methadon Menge Einordnen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-stoff-pruefen` | Wenn es um Methadon Stoff Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-strafrahmen-routen` | Wenn es um Methadon Strafrahmen Routen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methadon-therapiepfad-erlaubnis-bauen` | Wenn es um Methadon Therapiepfad Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `neue-psychoaktive-stoffe` | Wenn es um Neue Psychoaktive Stoffe in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nicht-geringe-menge-livecheck` | Wenn es um Nicht Geringe Menge Livecheck in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rezept-btmvv-arztpraxis-compliance-apotheke-dokumentation` | Wenn es um Btm Rezept Und Btmvv in Betäubungsmittelrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `stoff-und-anlage-pruefen` | Wenn es um Stoff Und Anlage Prüfen in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `therapie-statt-strafe` | Wenn es um Therapie Statt Strafe in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `u-haft-in-btm-sache` | Wenn es um U Haft In Btm Sache in Betäubungsmittelrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

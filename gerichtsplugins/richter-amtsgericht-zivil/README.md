# Richter Amtsgericht Zivilsachen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-amtsgericht-zivil`) | [`richter-amtsgericht-zivil.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`richter-amtsgericht-zivil-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Amtsrichter Zivilsachen: Schlüssigkeit Erheblichkeit Beweis Tenor Kostenentscheidung Streitwertbeschluss vorläufige Vollstreckbarkeit Rechtsmittelbelehrung Versäumnisurteil und Anerkenntnisurteil mit echter Relation und Entscheidungsvorschlag

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-amtsgericht-zivil.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-amtsgericht-zivil/richter-amtsgericht-zivil-werkstatt.md" download><code>richter-amtsgericht-zivil-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-amtsgericht-zivil/richter-amtsgericht-zivil-schnellstart.md" download><code>richter-amtsgericht-zivil-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-amtsgericht-zivil-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil-testakte.zip), [`richter-amtsgericht-zivil-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Amtsrichter in Zivilsachen (Streitwert bis 10.000 Euro, sonstige Zuständigkeiten nach Paragraf 23 GVG)

## Rechtsrahmen

ZPO, BGB, GVG, RPflG, GKG, RVG

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-amtsgericht-zivil-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-amtsgericht-zivil-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eingangspruefung-zuständigkeit** — Prüfung Zuständigkeit (Paragraf 23 GVG sachlich, Paragrafen 12 ff. ZPO örtlich), Klagezustellung, Pflichtangaben Para
- **02-streitwert-und-gerichtskosten** — Streitwertbestimmung Paragrafen 3-9 ZPO, GKG-Anlage 1 (KV 1210, 1211, 1220), vorläufige Streitwertfestsetzung, GKG-Vors
- **03-akte-erstdurchsicht** — Strukturierte Erstdurchsicht: Parteien, Antrag, Lebenssachverhalt, Anspruchsgrundlagen sammeln, Beweismittel listen, Str
- **04-relation-zivilrecht-klein** — Echte Relation: Klägerstation (Schlüssigkeit der Anspruchsgrundlage), Beklagtenstation (Erheblichkeit der Einwendungen
- **05-beweisaufnahme-kleine-zivilkammer** — Beweisbeschluss formulieren (Paragrafen 358-360 ZPO), Zeugenladung, Sachverständigenauswahl, Beweistermin protokolliere
- **06-tenor-und-kostenentscheidung** — Tenor formulieren (Hauptsache, Nebenforderungen, Zinsen, Kosten Paragraf 91 ZPO, vorläufige Vollstreckbarkeit Paragrafe
- **07-urteilsentwurf-paragraf-313** — Urteilsentwurf nach Paragraf 313 ZPO: Rubrum, Tenor, Tatbestand (gestraffter Vortrag), Entscheidungsgründe (Begründeth
- **08-versaeumnisurteil-und-anerkenntnis** — Versaeumnisurteil Paragrafen 330-347 ZPO, Anerkenntnisurteil Paragraf 307 ZPO, Verzichtsurteil Paragraf 306 ZPO, Einspru
- **09-vergleich-und-erledigung** — Prozessvergleich Paragraf 794 Abs. 1 Nr. 1 ZPO, Vergleich im Termin, schriftlicher Vergleich Paragraf 278 Abs. 6 ZPO, Er
- **10-entscheidungsvorschlag-zur-richterlichen-pruefung** — Strukturierter Entscheidungsvorschlag für den Richter: Tenor-Vorschlag, tragende Gründe in Stichpunkten, Risikohinweis

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehoerde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschlaege produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstuetzung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `01-eingangspruefung-zustaendigkeit` |
| 2. Unterlagen, Sachverhalt und Quellen | `03-akte-erstdurchsicht`, `05-beweisaufnahme-kleine-zivilkammer` |
| 3. Prüfung, Anspruch und Subsumtion | `10-entscheidungsvorschlag-zur-richterlichen-pruefung` |
| 4. Gestaltung, Strategie und Verhandlung | `09-vergleich-und-erledigung` |
| 5. Verfahren, Behörde und Gericht | `02-streitwert-und-gerichtskosten`, `07-urteilsentwurf-paragraf-313`, `08-versaeumnisurteil-und-anerkenntnis`, `v392-praxisraster-richter-amtsgericht-zivil` |
| 8. Spezialmodule und Schnittstellen | `04-relation-zivilrecht-klein`, `06-tenor-und-kostenentscheidung`, `99-finale-entscheidung-volltext`, `prozessuale-kniffe-und-rechtsprechungsanker` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-eingangspruefung-zustaendigkeit` | Wenn es um 01 Eingangsprüfung Zuständigkeit in Richter Amtsgericht Zivilsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `02-streitwert-und-gerichtskosten` | Wenn es um 02 Streitwert und Gerichtskosten in Richter Amtsgericht Zivilsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `03-akte-erstdurchsicht` | Wenn es um 03 Akte Erstdurchsicht in Richter Amtsgericht Zivilsachen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `04-relation-zivilrecht-klein` | Wenn es um 04 Relation Zivilrecht Klein in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `05-beweisaufnahme-kleine-zivilkammer` | Wenn es um 05 Beweisaufnahme Kleine Zivilkammer in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `06-tenor-und-kostenentscheidung` | Wenn es um 06 Tenor und Kostenentscheidung in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `07-urteilsentwurf-paragraf-313` | Wenn es um 07 Urteilsentwurf Paragraf 313 in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `08-versaeumnisurteil-und-anerkenntnis` | Wenn es um 08 Versäumnisurteil und Anerkenntnis in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nac... |
| `09-vergleich-und-erledigung` | Wenn es um 09 Vergleich und Erledigung in Richter Amtsgericht Zivilsachen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `10-entscheidungsvorschlag-zur-richterlichen-pruefung` | Wenn es um 10 Entscheidungsvorschlag Zur Richterlichen Prüfung in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung als Volltext (Urteil Amtsgericht Zivil) in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Richter Amtsgericht Zivilsachen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `v392-praxisraster-richter-amtsgericht-zivil` | Wenn es um Praxisraster Amtsgericht Zivil in Richter Amtsgericht Zivilsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Zivilkammer am Landgericht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-landgericht-zivilkammer`) | [`richter-landgericht-zivilkammer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`richter-landgericht-zivilkammer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Zivilkammer LG: erste Instanz und Berufung, große Relation, Schlüssigkeit Erheblichkeit Beweis, Hinweisverfügung Paragraf 139 ZPO, Beweisbeschluss, Sachverständigenbeweis, Urteil Paragraf 313 ZPO, Berufungsentscheidung Paragrafen 522-540 ZPO mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-landgericht-zivilkammer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-zivilkammer/richter-landgericht-zivilkammer-werkstatt.md" download><code>richter-landgericht-zivilkammer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-zivilkammer/richter-landgericht-zivilkammer-schnellstart.md" download><code>richter-landgericht-zivilkammer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-landgericht-zivilkammer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer-testakte.zip), [`richter-landgericht-zivilkammer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Vorsitzender oder Berichterstatter einer Zivilkammer (Paragraf 71 GVG, Streitwert ab 10.001 Euro; auch sonstige Zuständigkeiten Paragrafen 71-74 GVG) sowie zweite Instanz Berufung Paragraf 511 ZPO

## Rechtsrahmen

ZPO, BGB, HGB, GVG, GKG, RVG, EGZPO

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-landgericht-zivilkammer-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-landgericht-zivilkammer-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eingang-und-besetzung** — Eingangsprüfung Paragraf 522 ZPO bei Berufung, sachliche Zuständigkeit Paragraf 71 GVG (Erste Instanz) und Paragraf 11
- **02-große-relation-zivilrecht** — Vollständige zivilrechtliche Relation: Schlüssigkeitsprüfung (Klägerstation), Erheblichkeitsprüfung (Beklagtenstati
- **03-fruehe-erste-verfügung-paragraf-139** — Hinweisverfuegung Paragraf 139 ZPO: Hinweise auf rechtliche Bedenken, Auflagen zur Substantiierung, Ergänzung des Vortr
- **04-beweisbeschluss-und-sachverstaendiger** — Beweisbeschluss Paragrafen 358-360 ZPO: Beweisthema, Beweismittel, Auswahl des Sachverständigen, Sachverständigenfrage
- **05-zeugenbeweis-und-parteivernehmung** — Zeugenbeweis Paragrafen 373-401 ZPO, Beweisaufnahme im Termin, Belehrung, Glaubhaftigkeit, Parteivernehmung Paragrafen 4
- **06-urteil-großes-zivilurteil** — Urteilsentwurf nach Paragraf 313 ZPO bei groesserem Streitwert: ausführlicher Tatbestand, gegliederte Entscheidungsgrue
- **07-berufungsverfahren-paragraf-511-ff** — Berufungsverfahren: Zulässigkeit Paragraf 511, Berufungsbegründung Paragraf 520, Prüfungsumfang Paragraf 529, Zurück
- **08-kostenentscheidung-und-streitwert** — Kostenentscheidung Paragrafen 91-101 ZPO, Streitwertfestsetzung Paragrafen 39-51 GKG, Streitwertbeschluss, Änderung der
- **09-vergleich-und-mediation** — Vergleichsgespraech leiten Paragraf 278 ZPO, Mediation Paragraf 278a ZPO, Prozessvergleich Paragraf 794 Abs. 1 Nr. 1, Vo
- **10-entscheidungsvorschlag-kammer** — Strukturierter Entscheidungsvorschlag für die Kammerberatung: Tenor-Vorschlag, tragende Gründe, Beweiswürdigung, Hilf

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
| 1. Einstieg und Fallrouting | `01-eingang-und-besetzung` |
| 2. Unterlagen, Sachverhalt und Quellen | `04-beweisbeschluss-und-sachverstaendiger`, `05-zeugenbeweis-und-parteivernehmung` |
| 4. Gestaltung, Strategie und Verhandlung | `09-vergleich-und-mediation` |
| 5. Verfahren, Behörde und Gericht | `03-fruehe-erste-verfuegung-paragraf-139`, `06-urteil-grosses-zivilurteil`, `07-berufungsverfahren-paragraf-511-ff`, `v392-praxisraster-richter-landgericht-zivilkammer` |
| 8. Spezialmodule und Schnittstellen | `02-grosse-relation-zivilrecht`, `08-kostenentscheidung-und-streitwert`, `10-entscheidungsvorschlag-kammer`, `99-finale-entscheidung-volltext`, `prozessuale-kniffe-und-rechtsprechungsanker` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-eingang-und-besetzung` | Wenn es um 01 Eingang und Besetzung in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `02-grosse-relation-zivilrecht` | Wenn es um 02 Große Relation Zivilrecht in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `03-fruehe-erste-verfuegung-paragraf-139` | Wenn es um 03 Frühe Erste Verfügung Paragraf 139 in Zivilkammer am Landgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `04-beweisbeschluss-und-sachverstaendiger` | Wenn es um 04 Beweisbeschluss und Sachverständiger in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `05-zeugenbeweis-und-parteivernehmung` | Wenn es um 05 Zeugenbeweis und Parteivernehmung in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `06-urteil-grosses-zivilurteil` | Wenn es um 06 Urteil Großes Zivilurteil in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `07-berufungsverfahren-paragraf-511-ff` | Wenn es um 07 Berufungsverfahren Paragraf 511 Ff in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `08-kostenentscheidung-und-streitwert` | Wenn es um 08 Kostenentscheidung und Streitwert in Zivilkammer am Landgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `09-vergleich-und-mediation` | Wenn es um 09 Vergleich und Mediation in Zivilkammer am Landgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `10-entscheidungsvorschlag-kammer` | Wenn es um 10 Entscheidungsvorschlag Kammer in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung als Volltext (Urteil Zivilkammer) in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigke... |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Zivilkammer am Landgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `v392-praxisraster-richter-landgericht-zivilkammer` | Wenn es um Praxisraster Landgericht Zivilkammer in Zivilkammer am Landgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

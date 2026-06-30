# Strafkammer am Landgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Strafkammer LG: Eröffnungsentscheidung Hauptverhandlung Beweiswürdigung Strafzumessung schwere und mittlere Kriminalitaet Berufung gegen Amtsgerichtsurteil Sicherungsverwahrung und Maßnahmen mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-landgericht-strafkammer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-strafkammer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-strafkammer/richter-landgericht-strafkammer-werkstatt.md" download><code>richter-landgericht-strafkammer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-strafkammer/richter-landgericht-strafkammer-schnellstart.md" download><code>richter-landgericht-strafkammer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-landgericht-strafkammer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-strafkammer-testakte.zip), [`richter-landgericht-strafkammer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-strafkammer-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Tatvorwurf entlang von Beweiswuerdigung und Strafzumessung durchdringen und einen verwertbaren Schriftsatz bauen.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Vorsitzender oder Berichterstatter einer großen oder kleinen Strafkammer (Paragraf 74 GVG, Paragraf 76 GVG); Schwurgericht Paragraf 74 Abs. 2 GVG

## Rechtsrahmen

StGB, StPO, GVG, JGG, BZRG, RVG

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-landgericht-strafkammer-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-landgericht-strafkammer-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eroeffnungsverfahren-strafkammer** — Eröffnungsverfahren Paragrafen 199-203 StPO bei der Strafkammer, hinreichender Tatverdacht, Verlesung der Anklage, Eroe
- **02-hauptverhandlung-große-strafkammer** — Hauptverhandlung mit drei Berufs- und zwei Schöffenrichtern Paragraf 76 GVG, Verhandlungsleitung, Ablauf nach Paragraf - **03-beweisantraege-und-ablehnung** — Beweisantraege Paragraf 244 StPO, Ablehnungsgründe, Wahrunterstellung, Hilfsbeweisantraege, Konnexitaet, Beweisaufnahme
- **04-beweiswuerdigung-strafkammer** — Beweiswürdigung Paragraf 261 StPO bei komplexen Sachverhalten, Aussage gegen Aussage, Indizienprozess, In-dubio-pro-reo
- **05-strafzumessung-große-strafkammer** — Strafzumessung Paragrafen 46-49 StGB: Strafzumessungstatsachen, Strafrahmenverschiebung, besondere gesetzliche Milderung
- **06-maßnahmen-paragraf-61-stgb** — Maßnahmen der Besserung und Sicherung Paragraf 61 StGB: Unterbringung im psychiatrischen Krankenhaus Paragraf 63, Entzi
- **07-urteilsbegruendung-paragraf-267-lg** — Urteilsgründe Paragraf 267 StPO bei umfangreichen Strafverfahren: Persoenliche Verhältnisse, Tatfeststellungen, Beweis
- **08-berufung-strafkammer** — Berufung gegen Amtsgerichtsurteil (Kleine Strafkammer Paragraf 76 GVG), Prüfungsumfang Paragraf 327 StPO, Tatsacheninst
- **09-rechtsmittelbelehrung-strafkammer** — Tenor Strafkammer, Rechtsmittelbelehrung Revision Paragrafen 333 ff. StPO, Annahmeberufung, Frist, Form, Begründungserf
- **10-entscheidungsvorschlag-strafkammer** — Strukturierter Entscheidungsvorschlag für die Kammerberatung: Schuldspruch-Skizze, Strafzumessungs-Skizze, Bewaehrungse

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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-eroeffnungsverfahren-strafkammer` | Eröffnungsverfahren Paragrafen 199-203 StPO bei der Strafkammer, hinreichender Tatverdacht, Verlesung der Anklage, Eröffnungsbeschluss, Zulassung der Anklage |
| `02-hauptverhandlung-grosse-strafkammer` | Hauptverhandlung mit drei Berufs- und zwei Schöffenrichtern Paragraf 76 GVG, Verhandlungsleitung, Ablauf nach Paragraf 243 StPO, Wahrung der Förderungs- und Aufklärungspflicht Paragraf 244 Abs. 2 |
| `03-beweisantraege-und-ablehnung` | Beweisantraege Paragraf 244 StPO, Ablehnungsgründe, Wahrunterstellung, Hilfsbeweisantraege, Konnexitaet, Beweisaufnahme im Selbstleseverfahren Paragraf 249 Abs. 2 |
| `04-beweiswuerdigung-strafkammer` | Beweiswürdigung Paragraf 261 StPO bei komplexen Sachverhalten, Aussage gegen Aussage, Indizienprozess, In-dubio-pro-reo, Behandlung von Sachverständigengutachten, Glaubhaftigkeitsfaktoren |
| `05-strafzumessung-grosse-strafkammer` | Strafzumessung Paragrafen 46-49 StGB: Strafzumessungstatsachen, Strafrahmenverschiebung, besondere gesetzliche Milderungsgründe, Strafaussetzung Paragraf 56 (Bewaehrungsentscheidung), Verwarnung mit Strafvorbehalt Paragraf 59 |
| `06-massnahmen-paragraf-61-stgb` | Maßnahmen der Besserung und Sicherung Paragraf 61 StGB: Unterbringung im psychiatrischen Krankenhaus Paragraf 63, Entziehungsanstalt Paragraf 64, Sicherungsverwahrung Paragraf 66, Fuehrungsaufsicht |
| `07-urteilsbegruendung-paragraf-267-lg` | Urteilsgründe Paragraf 267 StPO bei umfangreichen Strafverfahren: Persoenliche Verhaeltnisse, Tatfeststellungen, Beweiswürdigung, rechtliche Würdigung, Strafzumessung, Maßnahmen |
| `08-berufung-strafkammer` | Berufung gegen Amtsgerichtsurteil (Kleine Strafkammer Paragraf 76 GVG), Prüfungsumfang Paragraf 327 StPO, Tatsacheninstanz, Verbot der Schlechterstellung Paragraf 331 StPO |
| `09-rechtsmittelbelehrung-strafkammer` | Tenor Strafkammer, Rechtsmittelbelehrung Revision Paragrafen 333 ff. StPO, Annahmeberufung, Frist, Form, Begründungserfordernis Paragraf 344 StPO |
| `10-entscheidungsvorschlag-strafkammer` | Strukturierter Entscheidungsvorschlag für die Kammerberatung: Schuldspruch-Skizze, Strafzumessungs-Skizze, Bewaehrungsentscheidung, Maßnahmenkonzept, Risikohinweise, ausdrücklich zur richterlichen Prüfung markiert |
| `99-finale-entscheidung-volltext` | Erzeugt die finale entscheidung als volltext (urteil strafkammer) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Bündelt strafgerichtliche Prozesskniffe zu Beweisaufnahme, Hinweisen, Verständigung, Beweiswürdigung, Strafzumessung, Einziehung und revisionsfestem Urteil. |
| `v392-praxisraster-richter-landgericht-strafkammer` | Praxisraster für Landgericht Strafkammer: Zuständigkeit, Verfahrensstand, Pflichtnormen, Beweisbedarf und passendes Endprodukt werden in der richtigen gerichtlichen oder staatsanwaltschaftlichen Rolle abgearbeitet. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

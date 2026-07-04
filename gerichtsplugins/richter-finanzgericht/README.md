# Finanzgericht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-finanzgericht`) | [`richter-finanzgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`richter-finanzgericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Finanzgericht: Sachprüfung Anfechtungsklage Verpflichtungsklage Aussetzung der Vollziehung Paragraf 69 FGO Beweiswürdigung im Amtsermittlungsgrundsatz und Urteilsentwurf mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-finanzgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-finanzgericht/richter-finanzgericht-werkstatt.md" download><code>richter-finanzgericht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-finanzgericht/richter-finanzgericht-schnellstart.md" download><code>richter-finanzgericht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-finanzgericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht-testakte.zip), [`richter-finanzgericht-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Steuerbescheid prüfen und Einspruch oder Klage tragfaehig begründen.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Finanzrichter als Einzelrichter oder Senat (Paragraf 5 FGO)

## Rechtsrahmen

FGO, AO, EStG, KStG, GewStG, UStG, BewG, FVG, GKG, RVG

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-finanzgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-finanzgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zulässigkeit-finanzgerichtsklage** — Zulässigkeit der Klage Paragrafen 40-65 FGO: Klagearten (Anfechtung Verpflichtung Feststellung Untaetigkeit), Vorverfah
- **02-amtsermittlung-finanzgericht** — Amtsermittlungsgrundsatz Paragraf 76 FGO, Heranziehung der Akten Paragraf 71, Beweismittel, Schätzungsbefugnis Paragraf - **03-aussetzung-der-vollziehung** — Aussetzung der Vollziehung Paragraf 69 FGO bzw. Paragraf 361 AO: ernstliche Zweifel an der Rechtmaessigkeit, unbillige H
- **04-steuerbescheid-prüfen** — Prüfung des angegriffenen Steuerbescheids: formelle Rechtmaessigkeit (Begründung Paragraf 121 AO, Bekanntgabe Paragraf - **05-est-pruefungsschema** — Einkommensteuer-Prüfung: Einkunftsart, Einkunftsermittlung (Paragrafen 4, 5 EStG oder Paragraf 11 EStG), Sonderausgaben
- **06-ust-pruefungsschema** — Umsatzsteuer: Steuerbarkeit Paragraf 1 UStG, Steuerpflicht und Steuerbefreiung Paragraf 4, Bemessungsgrundlage Paragraf - **07-koerperschaft-und-gewerbesteuer** — Körperschaftsteuer: Subjektsteuerpflicht Paragraf 1 KStG, Einkommensermittlung Paragraf 8 KStG i.V.m. EStG, verdeckte G
- **08-schaetzung-und-betriebspruefung** — Schätzung Paragraf 162 AO als Beweismittel: äußere und innere Schätzung, Zeitreihenvergleich, Geldverkehrsrechnung,
- **09-urteil-finanzgericht-und-revision** — Urteil Paragraf 105 FGO: Tatbestand, Entscheidungsgründe, Tenor; Revision Paragraf 115 FGO an BFH (grundsaetzliche Bede
- **10-entscheidungsvorschlag-finanzgericht** — Strukturierter Entscheidungsvorschlag: Tenor, Prüfungsschema Zulässigkeit Begründetheit, materielle Prüfung der Steu

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
| 3. Prüfung, Anspruch und Subsumtion | `05-est-pruefungsschema`, `06-ust-pruefungsschema`, `08-schaetzung-und-betriebspruefung` |
| 5. Verfahren, Behörde und Gericht | `01-zulaessigkeit-finanzgerichtsklage`, `02-amtsermittlung-finanzgericht`, `04-steuerbescheid-pruefen`, `09-urteil-finanzgericht-und-revision`, `10-entscheidungsvorschlag-finanzgericht`, `v392-praxisraster-richter-finanzgericht` |
| 8. Spezialmodule und Schnittstellen | `03-aussetzung-der-vollziehung`, `07-koerperschaft-und-gewerbesteuer`, `99-finale-entscheidung-volltext`, `prozessuale-kniffe-und-rechtsprechungsanker` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-zulaessigkeit-finanzgerichtsklage` | Wenn es um 01 Zulässigkeit Finanzgerichtsklage in Finanzgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `02-amtsermittlung-finanzgericht` | Wenn es um 02 Amtsermittlung Finanzgericht in Finanzgericht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `03-aussetzung-der-vollziehung` | Wenn es um 03 Aussetzung Der Vollziehung in Finanzgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `04-steuerbescheid-pruefen` | Wenn es um 04 Steuerbescheid Prüfen in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `05-est-pruefungsschema` | Wenn es um 05 ESt Prüfungsschema in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `06-ust-pruefungsschema` | Wenn es um 06 USt Prüfungsschema in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `07-koerperschaft-und-gewerbesteuer` | Wenn es um 07 Körperschaft und Gewerbesteuer in Finanzgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `08-schaetzung-und-betriebspruefung` | Wenn es um 08 Schaetzung und Betriebsprüfung in Finanzgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `09-urteil-finanzgericht-und-revision` | Wenn es um 09 Urteil Finanzgericht und Revision in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `10-entscheidungsvorschlag-finanzgericht` | Wenn es um 10 Entscheidungsvorschlag Finanzgericht in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung als Volltext (Urteil Finanzgericht) in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Na... |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Finanzgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `v392-praxisraster-richter-finanzgericht` | Wenn es um Praxisraster Finanzgericht in Finanzgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

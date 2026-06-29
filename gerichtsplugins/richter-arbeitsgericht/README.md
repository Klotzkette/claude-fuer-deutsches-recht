# Arbeitsgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Arbeitsgericht: Gütetermin Kammertermin Kündigungsschutzklage Zahlungsklage einstweilige Verfügung Beschlussverfahren Betriebsverfassung Streitwert mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-arbeitsgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht-werkstatt.md" download><code>richter-arbeitsgericht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht-schnellstart.md" download><code>richter-arbeitsgericht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`richter-arbeitsgericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht-testakte.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Kuendigung rechtssicher angreifen oder aussprechen und die Klagefrist sichern.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Arbeitsrichter als Vorsitzender einer Kammer (mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreis) Paragraf 16 ArbGG

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-arbeitsgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-arbeitsgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zuständigkeit-und-guetetermin** — Sachliche Zuständigkeit Paragraf 2 ArbGG, örtliche Zuständigkeit Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO, Klag
- **02-kuendigungsschutzklage-prüfen** — Kündigungsschutzklage Paragraf 4 KSchG: Klagefrist 3 Wochen, Kündigungsgründe (personenbedingt verhaltensbedingt betr
- **03-zahlungsklage-lohn-und-gehalt** — Zahlungsklage: faelliger Arbeitslohn, Annahmeverzug Paragrafen 615 BGB, Urlaubsabgeltung Paragraf 7 Abs. 4 BUrlG, Entgel
- **04-betriebsuebergang-und-tarif** — Betriebsübergang Paragraf 613a BGB, Eintritt in Arbeitsverhältnisse, Widerspruchsrecht, Informationspflichten Abs. 5;
- **05-befristung-und-teilzeit** — Befristungskontrolle TzBfG: sachgrundlose Befristung Paragraf 14 Abs. 2, Sachgrundbefristung Paragraf 14 Abs. 1, Zweckbe
- **06-agg-diskriminierung** — AGG Paragraf 7: Benachteiligungsverbot, geschuetzte Merkmale Paragraf 1, Beweislastregel Paragraf 22, Entschaedigung und
- **07-einstweilige-verfügung-arbeitsrecht** — Einstweilige Verfügung im Arbeitsrecht: Verfügungsanspruch und -grund Paragraf 940 ZPO, Schutz von Beschaeftigungsansp
- **08-betriebsverfassung-beschlussverfahren** — Beschlussverfahren Paragrafen 80 ff. ArbGG: Beteiligte, Verfahrensgegenstand (Mitbestimmung Paragraf 87 BetrVG, Einigung
- **09-urteil-arbeitsgericht** — Urteil Paragraf 60 ArbGG i.V.m. Paragrafen 313 ZPO, Tenor, Tatbestand, Entscheidungsgründe, Streitwert (3 Bruttomonatsg
- **10-entscheidungsvorschlag-arbeitsgericht** — Strukturierter Entscheidungsvorschlag: Tenor-Skizze, Kündigungsprüfungsschema, Anspruchsprüfung, Vergleichsvorschlag

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
| `01-zustaendigkeit-und-guetetermin` | Sachliche Zuständigkeit Paragraf 2 ArbGG, örtliche Zuständigkeit Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO, Klagezustellung, Anberaumung Guetetermin Paragraf 54 ArbGG |
| `02-kuendigungsschutzklage-pruefen` | Kündigungsschutzklage Paragraf 4 KSchG: Klagefrist 3 Wochen, Kündigungsgründe (personenbedingt verhaltensbedingt betriebsbedingt) Paragraf 1 KSchG, Sozialauswahl Paragraf 1 Abs. 3 KSchG |
| `03-zahlungsklage-lohn-und-gehalt` | Zahlungsklage: faelliger Arbeitslohn, Annahmeverzug Paragrafen 615 BGB, Urlaubsabgeltung Paragraf 7 Abs. 4 BUrlG, Entgeltfortzahlung im Krankheitsfall Paragraf 3 EFZG, Verzugspauschale Paragraf 288 Abs. 5 BGB |
| `04-betriebsuebergang-und-tarif` | Betriebsübergang Paragraf 613a BGB, Eintritt in Arbeitsverhältnisse, Widerspruchsrecht, Informationspflichten Abs. 5; Tarifgebundenheit Paragraf 3 TVG, Tariftreue, Nachwirkung Paragraf 4 Abs. 5 |
| `05-befristung-und-teilzeit` | Befristungskontrolle TzBfG: sachgrundlose Befristung Paragraf 14 Abs. 2, Sachgrundbefristung Paragraf 14 Abs. 1, Zweckbefristung; Teilzeit Paragraf 8 TzBfG (Anspruch auf Verringerung) |
| `06-agg-diskriminierung` | AGG Paragraf 7: Benachteiligungsverbot, geschuetzte Merkmale Paragraf 1, Beweislastregel Paragraf 22, Entschaedigung und Schadensersatz Paragraf 15, Ausschlussfrist Paragraf 15 Abs. 4 |
| `07-einstweilige-verfuegung-arbeitsrecht` | Einstweilige Verfügung im Arbeitsrecht: Verfügungsanspruch und -grund Paragraf 940 ZPO, Schutz von Beschaeftigungsanspruch, Wettbewerbsverbot, Verschwiegenheit; Eilbeschluss |
| `08-betriebsverfassung-beschlussverfahren` | Beschlussverfahren Paragrafen 80 ff. ArbGG: Beteiligte, Verfahrensgegenstand (Mitbestimmung Paragraf 87 BetrVG, Einigungsstelle Paragraf 76 BetrVG), Antrag im Beschlussverfahren |
| `09-urteil-arbeitsgericht` | Urteil Paragraf 60 ArbGG i.V.m. Paragrafen 313 ZPO, Tenor, Tatbestand, Entscheidungsgründe, Streitwert (3 Bruttomonatsgehaelter bei Kündigung), Berufung an LAG Paragraf 64 ArbGG, Revision an BAG Paragraf 72 ArbGG |
| `10-entscheidungsvorschlag-arbeitsgericht` | Strukturierter Entscheidungsvorschlag: Tenor-Skizze, Kündigungsprüfungsschema, Anspruchsprüfung, Vergleichsvorschlag für Guetetermin, Risikohinweise, ausdrücklich zur richterlichen Prüfung markiert |
| `99-finale-entscheidung-volltext` | Erzeugt die finale entscheidung als volltext (urteil arbeitsgericht) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Bündelt arbeitsgerichtliche Prozesskniffe zu Güteverhandlung, Kammertermin, Hinweis, Darlegungslast, Vergleich, Tenor und Vollstreckbarkeit. |
| `v392-praxisraster-richter-arbeitsgericht` | Praxisraster für Arbeitsgericht: Zuständigkeit, Verfahrensstand, Pflichtnormen, Beweisbedarf und passendes Endprodukt werden in der richtigen gerichtlichen oder staatsanwaltschaftlichen Rolle abgearbeitet. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

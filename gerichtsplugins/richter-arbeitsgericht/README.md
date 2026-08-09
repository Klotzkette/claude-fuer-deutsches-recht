# Arbeitsgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Arbeitsgericht: Gütetermin Kammertermin Kündigungsschutzklage Zahlungsklage einstweilige Verfügung Beschlussverfahren Betriebsverfassung Streitwert mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../../SKILLS.md) · [Skills dieses Plugins](../../skills-index/richter-arbeitsgericht.md) · [Plugin-Dateien](.) · [Download-Index](../../ASSET_INDEX.md) · [Testakten](../../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill aus der Skill-Liste wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitsgericht:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet und liefere als Erstes Klageantrag: Es wird festgestellt, dass das Arbeitsverhältnis der Parteien durch die Kündigung vom [Datum] nicht aufgelöst worden ist. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-arbeitsgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-arbeitsgericht/richter-arbeitsgericht-schnellstart.md" download><code>richter-arbeitsgericht-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-arbeitsgericht/richter-arbeitsgericht-werkstatt.md" download><code>richter-arbeitsgericht-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Kündigung rechtssicher angreifen oder aussprechen und die Klagefrist sichern.
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

- **01-zuständigkeit-und-gütetermin** — Sachliche Zuständigkeit Paragraf 2 ArbGG, örtliche Zuständigkeit Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO, Klag
- **02-kündigungsschutzklage-prüfen** — Kündigungsschutzklage Paragraf 4 KSchG: Klagefrist 3 Wochen, Kündigungsgründe (personenbedingt verhaltensbedingt betr
- **03-zahlungsklage-lohn-und-gehalt** — Zahlungsklage: fälliger Arbeitslohn, Annahmeverzug Paragrafen 615 BGB, Urlaubsabgeltung Paragraf 7 Abs. 4 BUrlG, Entgel
- **04-betriebsübergang-und-tarif** — Betriebsübergang Paragraf 613a BGB, Eintritt in Arbeitsverhältnisse, Widerspruchsrecht, Informationspflichten Abs. 5;
- **05-befristung-und-teilzeit** — Befristungskontrolle TzBfG: sachgrundlose Befristung Paragraf 14 Abs. 2, Sachgrundbefristung Paragraf 14 Abs. 1, Zweckbe
- **06-agg-diskriminierung** — AGG Paragraf 7: Benachteiligungsverbot, geschützte Merkmale Paragraf 1, Beweislastregel Paragraf 22, Entschädigung und
- **07-einstweilige-verfügung-arbeitsrecht** — Einstweilige Verfügung im Arbeitsrecht: Verfügungsanspruch und -grund Paragraf 940 ZPO, Schutz von Beschäftigungsansp
- **08-betriebsverfassung-beschlussverfahren** — Beschlussverfahren Paragrafen 80 ff. ArbGG: Beteiligte, Verfahrensgegenstand (Mitbestimmung Paragraf 87 BetrVG, Einigung
- **09-urteil-arbeitsgericht** — Urteil Paragraf 60 ArbGG i.V.m. Paragrafen 313 ZPO, Tenor, Tatbestand, Entscheidungsgründe, Streitwert (3 Bruttomonatsg
- **10-entscheidungsvorschlag-arbeitsgericht** — Strukturierter Entscheidungsvorschlag: Tenor-Skizze, Kündigungsprüfungsschema, Anspruchsprüfung, Vergleichsvorschlag

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehörde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsätzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschläge produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstützung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschläge.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte dürfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewährleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behördlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Sämtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lückenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`02-kuendigungsschutzklage-pruefen`](skills/02-kuendigungsschutzklage-pruefen/SKILL.md), [`03-zahlungsklage-lohn-und-gehalt`](skills/03-zahlungsklage-lohn-und-gehalt/SKILL.md), [`05-befristung-und-teilzeit`](skills/05-befristung-und-teilzeit/SKILL.md), [`07-einstweilige-verfuegung-arbeitsrecht`](skills/07-einstweilige-verfuegung-arbeitsrecht/SKILL.md), [`08-betriebsverfassung-beschlussverfahren`](skills/08-betriebsverfassung-beschlussverfahren/SKILL.md), [`09-urteil-arbeitsgericht`](skills/09-urteil-arbeitsgericht/SKILL.md), [`10-entscheidungsvorschlag-arbeitsgericht`](skills/10-entscheidungsvorschlag-arbeitsgericht/SKILL.md), [`v392-praxisraster-richter-arbeitsgericht`](skills/v392-praxisraster-richter-arbeitsgericht/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`01-zustaendigkeit-und-guetetermin`](skills/01-zustaendigkeit-und-guetetermin/SKILL.md), [`04-betriebsuebergang-und-tarif`](skills/04-betriebsuebergang-und-tarif/SKILL.md), [`06-agg-diskriminierung`](skills/06-agg-diskriminierung/SKILL.md), [`99-finale-entscheidung-volltext`](skills/99-finale-entscheidung-volltext/SKILL.md), [`prozessuale-kniffe-und-rechtsprechungsanker`](skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 14 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`01-zustaendigkeit-und-guetetermin`](skills/01-zustaendigkeit-und-guetetermin/SKILL.md) | Wenn es um 01 Zuständigkeit und Guetetermin in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`02-kuendigungsschutzklage-pruefen`](skills/02-kuendigungsschutzklage-pruefen/SKILL.md) | Wenn es um 02 Kündigungsschutzklage Prüfen in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`03-zahlungsklage-lohn-und-gehalt`](skills/03-zahlungsklage-lohn-und-gehalt/SKILL.md) | Wenn es um 03 Zahlungsklage Lohn und Gehalt in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`04-betriebsuebergang-und-tarif`](skills/04-betriebsuebergang-und-tarif/SKILL.md) | Wenn es um 04 Betriebsübergang und Tarif in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`05-befristung-und-teilzeit`](skills/05-befristung-und-teilzeit/SKILL.md) | Wenn es um 05 Befristung und Teilzeit in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`06-agg-diskriminierung`](skills/06-agg-diskriminierung/SKILL.md) | Wenn es um 06 Agg Diskriminierung in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`07-einstweilige-verfuegung-arbeitsrecht`](skills/07-einstweilige-verfuegung-arbeitsrecht/SKILL.md) | Wenn es um 07 Einstweilige Verfügung Arbeitsrecht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`08-betriebsverfassung-beschlussverfahren`](skills/08-betriebsverfassung-beschlussverfahren/SKILL.md) | Wenn es um 08 Betriebsverfassung Beschlussverfahren in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`09-urteil-arbeitsgericht`](skills/09-urteil-arbeitsgericht/SKILL.md) | Wenn es um 09 Urteil Arbeitsgericht in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`10-entscheidungsvorschlag-arbeitsgericht`](skills/10-entscheidungsvorschlag-arbeitsgericht/SKILL.md) | Wenn es um 10 Entscheidungsvorschlag Arbeitsgericht in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`99-finale-entscheidung-volltext`](skills/99-finale-entscheidung-volltext/SKILL.md) | Wenn es um Finale Entscheidung als Volltext (Urteil Arbeitsgericht) in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Richter Arbeitsgericht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`prozessuale-kniffe-und-rechtsprechungsanker`](skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md) | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`v392-praxisraster-richter-arbeitsgericht`](skills/v392-praxisraster-richter-arbeitsgericht/SKILL.md) | Wenn es um Praxisraster Arbeitsgericht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

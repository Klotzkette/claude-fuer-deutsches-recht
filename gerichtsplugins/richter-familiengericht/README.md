# Familiengericht (großes Familiengericht)

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Familiengericht: Ehesachen Scheidung Versorgungsausgleich Kindschaftssachen elterliche Sorge Umgang Kindesunterhalt Trennungs- und Ehegattenunterhalt Gewaltschutz Adoption Vormundschaft Betreuungsteile mit Verfahrenskostenhilfe und Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../../SKILLS.md) · [Skills dieses Plugins](../../skills-index/richter-familiengericht.md) · [Plugin-Dateien](.) · [Download-Index](../../ASSET_INDEX.md) · [Testakten](../../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../../skills-index/richter-familiengericht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Familiengericht (großes Familiengericht):

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet. Beginne mit folgendem Arbeitsschritt: eine verfahrensleitende Verfügung oder einen belastbaren Entscheidungsentwurf. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-familiengericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-familiengericht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/richter-familiengericht-schnellstart.md" download><code>richter-familiengericht-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/richter-familiengericht-werkstatt.md" download><code>richter-familiengericht-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Familienrecht — Sorge, Umgang und Gewaltschutz in Essen](../../testakten/familienrecht-sorge-umgang-gewaltschutz-essen/README.md) | [Gesamt-PDF](../../testakten/familienrecht-sorge-umgang-gewaltschutz-essen/gesamt-pdf/familienrecht-sorge-umgang-gewaltschutz-essen_gesamt.pdf) | [`testakte-familienrecht-sorge-umgang-gewaltschutz-essen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-familienrecht-sorge-umgang-gewaltschutz-essen.zip) | [`testakte-familienrecht-sorge-umgang-gewaltschutz-essen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-familienrecht-sorge-umgang-gewaltschutz-essen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Familiensache richterlich vorbereiten: Zuständigkeit, Anhörung, Kindeswohl, Unterhalt, Versorgungsausgleich, Zugewinn, Gewaltschutz, Tenor und Beschlussgründe.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Familienrichter am Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG) für Ehe-, Kindschafts-, Unterhalts-, Versorgungsausgleichs-, Gewaltschutz- und sonstige Familiensachen nach FamFG

## Rechtsrahmen

FamFG, BGB (Familienrecht), ZPO (subsidiaer), VersAusglG, GewSchG, KSchG (Kindschaftsrecht), UnterhaltsR (Paragrafen 1601 ff. BGB), FamGKG, RVG, Haager Kinderschutzübereinkommen, EuEheVO, Brüssel IIb

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-familiengericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-familiengericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zuständigkeit-und-zuteilung-familiensache** — Prüfung Zuständigkeit Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG, örtliche Zuständigkeit Paragrafen 122-1
- **02-ehesache-scheidung-paragraf-1565** — Scheidungsverfahren Paragrafen 1564 ff. BGB i.V.m. Paragrafen 121 ff. FamFG: Trennungsjahr Paragraf 1566, Zerruettung Pa
- **03-versorgungsausgleich-vorbereiten** — Versorgungsausgleich nach VersAusglG: Auskünfte der Versorgungsträger einholen, Ehezeit feststellen Paragraf 3 VersAus
- **04-kindschaftssache-elterliche-sorge** — Sorgerechtsverfahren Paragrafen 1626 ff. BGB i.V.m. Paragrafen 151 ff. FamFG: Kindeswohlprüfung (Bindungs-, Förder-, K
- **05-umgangsrecht-paragraf-1684-bgb** — Umgangsverfahren Paragraf 1684 BGB i.V.m. Paragrafen 156 ff. FamFG: Wohl des Kindes, begleiteter Umgang, Umgangspflegsch
- **06-kindesunterhalt-düsseldorfer-tabelle** — Kindesunterhalt Paragrafen 1601 ff. BGB: Bedürftigkeit, Leistungsfähigkeit (Selbstbehalt nach Leitlinien), Düsseldorf
- **07-ehegattenunterhalt-trennung-und-nachehe** — Trennungsunterhalt Paragraf 1361 BGB und nachehelicher Unterhalt Paragrafen 1569 ff. BGB: Anspruchsgrundlagen (Betreuung
- **08-gewaltschutz-und-eilanordnung** — Gewaltschutzverfahren GewSchG: Schutzanordnungen Paragraf 1 (Abstand, Nähe, Kontakt), Wohnungszuweisung Paragraf 2, Eil
- **09-beschluss-familiensache-paragraf-38-famfg** — Beschluss in Familiensache Paragraf 38 FamFG: Tenor, Sachverhalt (knapp), Gründe, Nebenentscheidungen FamGKG-Wert und V
- **10-entscheidungsvorschlag-familienrichter** — Strukturierter Entscheidungsvorschlag für den Familienrichter: Tenor-Skizze (Scheidungsausspruch, Folgesachen, Sorge/Um

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
| 4. Gestaltung, Strategie und Verhandlung | [`03-versorgungsausgleich-vorbereiten`](skills/03-versorgungsausgleich-vorbereiten/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`09-beschluss-familiensache-paragraf-38-famfg`](skills/09-beschluss-familiensache-paragraf-38-famfg/SKILL.md), [`v392-praxisraster-richter-familiengericht`](skills/v392-praxisraster-richter-familiengericht/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`01-zustaendigkeit-und-zuteilung-familiensache`](skills/01-zustaendigkeit-und-zuteilung-familiensache/SKILL.md), [`02-ehesache-scheidung-paragraf-1565`](skills/02-ehesache-scheidung-paragraf-1565/SKILL.md), [`04-kindschaftssache-elterliche-sorge`](skills/04-kindschaftssache-elterliche-sorge/SKILL.md), [`05-umgangsrecht-paragraf-1684-bgb`](skills/05-umgangsrecht-paragraf-1684-bgb/SKILL.md), [`06-kindesunterhalt-duesseldorfer-tabelle`](skills/06-kindesunterhalt-duesseldorfer-tabelle/SKILL.md), [`07-ehegattenunterhalt-trennung-und-nachehe`](skills/07-ehegattenunterhalt-trennung-und-nachehe/SKILL.md), [`08-gewaltschutz-und-eilanordnung`](skills/08-gewaltschutz-und-eilanordnung/SKILL.md), [`10-entscheidungsvorschlag-familienrichter`](skills/10-entscheidungsvorschlag-familienrichter/SKILL.md), [`99-finale-entscheidung-volltext`](skills/99-finale-entscheidung-volltext/SKILL.md), [`prozessuale-kniffe-und-rechtsprechungsanker`](skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 14 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; der Direktdownload lädt dieselbe Datei als Markdown. Beschreibungen stammen aus dem jeweiligen `description`-Feld.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`01-zustaendigkeit-und-zuteilung-familiensache`](skills/01-zustaendigkeit-und-zuteilung-familiensache/SKILL.md) | Wenn es um 01 Zuständigkeit und Zuteilung Familiensache in Familiengericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/01-zustaendigkeit-und-zuteilung-familiensache/SKILL.md" download><code>SKILL.md</code></a> |
| [`02-ehesache-scheidung-paragraf-1565`](skills/02-ehesache-scheidung-paragraf-1565/SKILL.md) | Wenn es um 02 Ehesache Scheidung Paragraf 1565 in Familiengericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/02-ehesache-scheidung-paragraf-1565/SKILL.md" download><code>SKILL.md</code></a> |
| [`03-versorgungsausgleich-vorbereiten`](skills/03-versorgungsausgleich-vorbereiten/SKILL.md) | Wenn es um Versorgungsausgleich vorbereiten in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/03-versorgungsausgleich-vorbereiten/SKILL.md" download><code>SKILL.md</code></a> |
| [`04-kindschaftssache-elterliche-sorge`](skills/04-kindschaftssache-elterliche-sorge/SKILL.md) | Wenn es um 04 Kindschaftssache Elterliche Sorge in Familiengericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/04-kindschaftssache-elterliche-sorge/SKILL.md" download><code>SKILL.md</code></a> |
| [`05-umgangsrecht-paragraf-1684-bgb`](skills/05-umgangsrecht-paragraf-1684-bgb/SKILL.md) | Wenn es um 05 Umgangsrecht Paragraf 1684 Bgb in Familiengericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/05-umgangsrecht-paragraf-1684-bgb/SKILL.md" download><code>SKILL.md</code></a> |
| [`06-kindesunterhalt-duesseldorfer-tabelle`](skills/06-kindesunterhalt-duesseldorfer-tabelle/SKILL.md) | Wenn es um Kindesunterhalt und Düsseldorfer Tabelle in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/06-kindesunterhalt-duesseldorfer-tabelle/SKILL.md" download><code>SKILL.md</code></a> |
| [`07-ehegattenunterhalt-trennung-und-nachehe`](skills/07-ehegattenunterhalt-trennung-und-nachehe/SKILL.md) | Wenn es um 07 Ehegattenunterhalt Trennung und Nachehe in Familiengericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/07-ehegattenunterhalt-trennung-und-nachehe/SKILL.md" download><code>SKILL.md</code></a> |
| [`08-gewaltschutz-und-eilanordnung`](skills/08-gewaltschutz-und-eilanordnung/SKILL.md) | Wenn es um 08 Gewaltschutz und Eilanordnung in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/08-gewaltschutz-und-eilanordnung/SKILL.md" download><code>SKILL.md</code></a> |
| [`09-beschluss-familiensache-paragraf-38-famfg`](skills/09-beschluss-familiensache-paragraf-38-famfg/SKILL.md) | Wenn es um Beschluss in Familiensachen nach Paragraf 38 FamFG in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/09-beschluss-familiensache-paragraf-38-famfg/SKILL.md" download><code>SKILL.md</code></a> |
| [`10-entscheidungsvorschlag-familienrichter`](skills/10-entscheidungsvorschlag-familienrichter/SKILL.md) | Wenn es um 10 Entscheidungsvorschlag Familienrichter in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sc... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/10-entscheidungsvorschlag-familienrichter/SKILL.md" download><code>SKILL.md</code></a> |
| [`99-finale-entscheidung-volltext`](skills/99-finale-entscheidung-volltext/SKILL.md) | Wenn es um Finale Entscheidung als Volltext (Beschluss Familiengericht) in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits-... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/99-finale-entscheidung-volltext/SKILL.md" download><code>SKILL.md</code></a> |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Richter Familiengericht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/juristischer-argumentationskern/SKILL.md" download><code>SKILL.md</code></a> |
| [`prozessuale-kniffe-und-rechtsprechungsanker`](skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md) | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Familiengericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md" download><code>SKILL.md</code></a> |
| [`v392-praxisraster-richter-familiengericht`](skills/v392-praxisraster-richter-familiengericht/SKILL.md) | Wenn es um Praxisraster Familiengericht in Familiengericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-familiengericht/skills/v392-praxisraster-richter-familiengericht/SKILL.md" download><code>SKILL.md</code></a> |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

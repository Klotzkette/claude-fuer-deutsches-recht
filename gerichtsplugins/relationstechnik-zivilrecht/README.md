# Relationstechnik Zivilrecht (Praxis-Werkstatt)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`relationstechnik-zivilrecht`) | [`relationstechnik-zivilrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`relationstechnik-zivilrecht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Relationstechnik Zivilrecht: Klaegerstation, Beklagtenstation, Beweisstation und Entscheidungsstation mit Schlüssigkeit, Erheblichkeit, Beweislast, Hinweisen und Urteilsvotum.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`relationstechnik-zivilrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/relationstechnik-zivilrecht/relationstechnik-zivilrecht-werkstatt.md" download><code>relationstechnik-zivilrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/relationstechnik-zivilrecht/relationstechnik-zivilrecht-schnellstart.md" download><code>relationstechnik-zivilrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`relationstechnik-zivilrecht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht-testakte.zip), [`relationstechnik-zivilrecht-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Jeder Zivilrechtler (Richter, Referendar, Anwalt) der eine große Relation aufbauen will

## Rechtsrahmen

ZPO, BGB, HGB, Methodenlehre des Buergerlichen Rechts (Larenz, Wieacker)

## Inhalt

- **21 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`relationstechnik-zivilrecht-werkstatt.md`)
- **Schnellstart-Prompt** (`relationstechnik-zivilrecht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-akte-erstdurchsicht-zivil** — Strukturierte Erstdurchsicht der Zivilakte: Parteien identifizieren, Antrag isolieren, Lebenssachverhalt extrahieren, be
- **02-parteivortrag-strukturieren** — Kläger- und Beklagtenvortrag in Behauptungen, Bestreiten, Nichtwissen Paragraf 138 Abs. 4 ZPO, Gestaendnis Paragraf 288
- **03-streitstand-erfassen** — Streitiger und unstreitiger Sachverhalt heraussortieren, Geltung von Paragraf 138 Abs. 3 ZPO (Gestaendnisfiktion), Bewei
- **04-klage-antrag-auslegen** — Klageantrag auslegen Paragraf 133 BGB analog, Bestimmtheit Paragraf 253 Abs. 2 Nr. 2 ZPO, Haupt- und Hilfsantraege, Stuf
- **05-anspruchsgrundlagen-identifizieren** — Anspruchsgrundlagen aufstellen: vertraglich, vertragsaehnlich, dinglich, deliktisch, bereicherungsrechtlich; Anspruchssy
- **06-schlüssigkeit-prüfen** — Schlüssigkeitsprüfung (Klägerstation): liegen die Voraussetzungen der Anspruchsgrundlage nach dem Klägervortrag vor?
- **07-klaegerstation-votum** — Schriftliches Votum der Klägerstation: Anspruchsgrundlage, geprüfte Tatbestandsmerkmale, schlüssige Rechtsfolge oder
- **08-beklagtenvortrag-strukturieren** — Beklagtenvortrag ordnen: Bestreiten der Anspruchsvoraussetzungen, Einwendungen (rechtshindernd, rechtsvernichtend), Einr
- **09-einwendungen-einreden-prüfen** — Prüfung der Einwendungen und Einreden: Verjaehrung Paragrafen 194 ff. BGB, Erfuellung Paragrafen 362 ff., Aufrechnung P
- **10-erheblichkeit-prüfen** — Erheblichkeitsprüfung (Beklagtenstation): sind Einwendungen und Einreden rechtlich erheblich? Schlüssigkeit + Erheblic
- **11-beklagtenstation-votum** — Schriftliches Votum der Beklagtenstation: erhebliche Einwendungen und Einreden, unerhebliche Verteidigungsmittel, Beweis
- **12-beweisbeduerftige-tatsachen-isolieren** — Beweisbedürftige Tatsachen isolieren: erhebliche und streitige Tatsachen, Trennung von Rechtsfragen und Tatsachenfragen
- **13-beweislastverteilung-prüfen** — Beweislastverteilung nach allgemeinen Regeln (Rosenberg-Formel) und Sondernormen (Paragraf 280 Abs. 1 S. 2 BGB, Paragraf - **14-beweismittel-wuerdigen** — Beweismittel und ihre Würdigung: Augenschein Paragrafen 371 ff. ZPO, Zeuge Paragrafen 373 ff., Sachverständiger Paragr
- **15-beweisstation-votum** — Schriftliches Votum der Beweisstation: Beweisaufnahmebedarf, Beweisbeschluss-Entwurf Paragraf 358a ZPO, antizipierte Bew
- **16-tenor-formulieren** — Tenor formulieren: Hauptsache (Verurteilung zur Zahlung, Herausgabe, Unterlassung, Feststellung), Nebenforderungen (Zins
- **17-tatbestand-schreiben** — Tatbestand Paragraf 313 Abs. 1 Nr. 5 ZPO: gestraffter unstreitiger Sachverhalt, streitiger Klägervortrag, streitiger Be
- **18-entscheidungsgruende-aufbauen** — Entscheidungsgründe aufbauen: Zulässigkeit, Begründetheit (Anspruchsprüfung Schritt für Schritt), Beweiswürdigung,
- **19-nebenentscheidungen-kosten-vorlaeufige-vollstreckbarkeit** — Nebenentscheidungen: Kosten Paragrafen 91 ff. ZPO, Baumbach'sche Formel bei subjektiver Klagehaeufung, vorläufige Volls
- **20-urteilsentwurf-finalisieren** — Urteilsentwurf finalisieren: Rubrum, Tenor, Tatbestand, Entscheidungsgründe, Nebenentscheidungen, Rechtsmittelbelehrung

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
| 2. Unterlagen, Sachverhalt und Quellen | `01-akte-erstdurchsicht-zivil`, `12-beweisbeduerftige-tatsachen-isolieren`, `13-beweislastverteilung-pruefen`, `14-beweismittel-wuerdigen`, `15-beweisstation-votum` |
| 3. Prüfung, Anspruch und Subsumtion | `05-anspruchsgrundlagen-identifizieren`, `17-tatbestand-schreiben` |
| 4. Gestaltung, Strategie und Verhandlung | `02-parteivortrag-strukturieren`, `08-beklagtenvortrag-strukturieren` |
| 5. Verfahren, Behörde und Gericht | `04-klage-antrag-auslegen`, `20-urteilsentwurf-finalisieren` |
| 8. Spezialmodule und Schnittstellen | `03-streitstand-erfassen`, `06-schluessigkeit-pruefen`, `07-klaegerstation-votum`, `09-einwendungen-einreden-pruefen`, `10-erheblichkeit-pruefen`, `11-beklagtenstation-votum`, `16-tenor-formulieren`, `18-entscheidungsgruende-aufbauen`, `19-nebenentscheidungen-kosten-vorlaeufige-vollstreckbarkeit`, `99-finale-entscheidung-volltext`, `prozessuale-kniffe-und-rechtsprechungsanker` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 22 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-akte-erstdurchsicht-zivil` | Wenn es um 01 Akte Erstdurchsicht Zivil in Relationstechnik Zivilrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `02-parteivortrag-strukturieren` | Wenn es um 02 Parteivortrag Strukturieren in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `03-streitstand-erfassen` | Wenn es um 03 Streitstand Erfassen in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `04-klage-antrag-auslegen` | Wenn es um 04 Klage Antrag Auslegen in Relationstechnik Zivilrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `05-anspruchsgrundlagen-identifizieren` | Wenn es um 05 Anspruchsgrundlagen Identifizieren in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `06-schluessigkeit-pruefen` | Wenn es um 06 Schlüssigkeit Prüfen in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `07-klaegerstation-votum` | Wenn es um 07 Klägerstation Votum in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `08-beklagtenvortrag-strukturieren` | Wenn es um 08 Beklagtenvortrag Strukturieren in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `09-einwendungen-einreden-pruefen` | Wenn es um 09 Einwendungen Einreden Prüfen in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `10-erheblichkeit-pruefen` | Wenn es um 10 Erheblichkeit Prüfen in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `11-beklagtenstation-votum` | Wenn es um 11 Beklagtenstation Votum in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `12-beweisbeduerftige-tatsachen-isolieren` | Wenn es um 12 Beweisbedürftige Tatsachen Isolieren in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `13-beweislastverteilung-pruefen` | Wenn es um 13 Beweislastverteilung Prüfen in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `14-beweismittel-wuerdigen` | Wenn es um 14 Beweismittel Wuerdigen in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `15-beweisstation-votum` | Wenn es um 15 Beweisstation Votum in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `16-tenor-formulieren` | Wenn es um 16 Tenor Formulieren in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `17-tatbestand-schreiben` | Wenn es um 17 Tatbestand Schreiben in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `18-entscheidungsgruende-aufbauen` | Wenn es um 18 Entscheidungsgründe Aufbauen in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `19-nebenentscheidungen-kosten-vorlaeufige-vollstreckbarkeit` | Wenn es um 19 Nebenentscheidungen Kosten Vorläufige Vollstreckbarkeit in Relationstechnik Zivilrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `20-urteilsentwurf-finalisieren` | Wenn es um 20 Urteilsentwurf Finalisieren in Relationstechnik Zivilrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung als Volltext (Urteil oder Beschluss Zivil) in Relationstechnik Zivilrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Z... |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Relationstechnik Zivilrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

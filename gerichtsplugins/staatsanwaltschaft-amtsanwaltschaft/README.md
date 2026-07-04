# Staatsanwaltschaft und Amtsanwaltschaft


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`staatsanwaltschaft-amtsanwaltschaft`) | [`staatsanwaltschaft-amtsanwaltschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`staatsanwaltschaft-amtsanwaltschaft-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Staatsanwaltschaft und Amtsanwaltschaft: Ermittlungsführung, Durchsuchung, Haft, Einstellung, Strafbefehl, Anklage, Einziehung, Plädoyer, Rechtsmittel und Vollstreckung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`staatsanwaltschaft-amtsanwaltschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft/staatsanwaltschaft-amtsanwaltschaft-werkstatt.md" download><code>staatsanwaltschaft-amtsanwaltschaft-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft/staatsanwaltschaft-amtsanwaltschaft-schnellstart.md" download><code>staatsanwaltschaft-amtsanwaltschaft-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`staatsanwaltschaft-amtsanwaltschaft-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft-testakte.zip), [`staatsanwaltschaft-amtsanwaltschaft-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Vorgang aus Sicht der Staatsanwaltschaft oder Amtsanwaltschaft bearbeiten: Tatverdacht, Ermittlungsmaßnahmen, Verfahrensabschluss, Anklage, Strafbefehl, Einstellung und Sitzungsvertretung.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Strafverfolgung und Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 6 (Strafverfolgung) und Nr. 8 Buchstabe a (Justiz) der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die staatsanwaltschaftliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Staatsanwaltschaft oder Amtsanwaltschaft bei Amtsgericht und Landgericht (Paragraf 141 GVG, Paragraf 142 GVG, Paragraf 143 GVG). Das Plugin bildet das Dezernat von der Erstdurchsicht des Ermittlungsvorgangs bis zur Strafvollstreckung ab.

## Rechtsrahmen

StPO, StGB, GVG, JGG, OWiG, RiStBV, OrgStA, StVollstrO, BZRG, RVG

## Inhalt

- **29 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`staatsanwaltschaft-amtsanwaltschaft-werkstatt.md`)
- **Schnellstart-Prompt** (`staatsanwaltschaft-amtsanwaltschaft-schnellstart.md`)
- **Testakten** (`testakte/README.md`) — aus staatsanwaltschaftlicher Sicht

## Skill-Liste

- **01-akte-erstdurchsicht-und-anfangsverdacht** — Erstdurchsicht, Anfangsverdacht (Paragraf 152 Abs. 2 StPO), Verjaehrung, Ermittlungsrichtung
- **02-zuständigkeit-sta-und-amtsanwaltschaft** — Sachliche und oertliche Zuständigkeit, Abgrenzung Staatsanwalt und Amtsanwalt nach OrgStA
- **03-ermittlungsfuehrung-und-ermittlungsanweisung** — Sachleitung (Paragrafen 161, 163 StPO), Ermittlungsanweisung an die Polizei, Ermittlungsplan
- **04-durchsuchung-und-beschlagnahme-antrag** — Antrag Durchsuchung (Paragrafen 102 ff. StPO) und Beschlagnahme (Paragrafen 94 ff. StPO), Richtervorbehalt
- **05-haftbefehlsantrag-und-untersuchungshaft** — Haftbefehlsantrag (Paragrafen 112 ff. StPO), Haftgruende, Verhältnismaessigkeit, Haftverschonung
- **06-vorlaeufige-festnahme-und-eilkompetenz** — Vorlaeufige Festnahme (Paragraf 127 StPO), Eilkompetenz, Vorfuehrung (Paragraf 128 StPO)
- **07-telekommunikationsueberwachung-und-verdeckte-maßnahmen** — TKUe (Paragraf 100a StPO) und verdeckte Maßnahmen, Katalogtat, Subsidiaritaet, Kernbereichsschutz
- **08-beschuldigtenvernehmung-und-belehrung** — Vernehmung (Paragrafen 136, 163a StPO), Belehrung, verbotene Methoden (Paragraf 136a StPO)
- **09-sachverstaendige-und-koerperliche-untersuchung** — Gutachtenauftrag (Paragrafen 73 ff. StPO), koerperliche Untersuchung (Paragraf 81a StPO)
- **10-einstellung-mangels-tatverdacht-paragraf-170** — Einstellung mangels hinreichenden Tatverdachts (Paragraf 170 Abs. 2 StPO), Bescheide
- **11-einstellung-aus-opportunitaet-paragraf-153-und-153a** — Einstellung wegen Geringfuegigkeit und gegen Auflagen (Paragrafen 153, 153a StPO)
- **12-teileinstellung-paragraf-154-und-154a** — Beschraenkung der Verfolgung (Paragrafen 154, 154a StPO)
- **13-strafbefehlsantrag-paragraf-407** — Strafbefehlsantrag (Paragrafen 407 ff. StPO), zulässige Rechtsfolgen, Tatkonkretisierung
- **14-anklageschrift-paragraf-200** — Anklageschrift (Paragraf 200 StPO), Anklagesatz, wesentliches Ermittlungsergebnis, Eroeffnungsantrag
- **15-antrag-beschleunigtes-verfahren-paragraf-417** — Beschleunigtes Verfahren (Paragrafen 417 ff. StPO), Eignung, Rechtsfolgenbegrenzung
- **16-sicherungsverfahren-und-massregeln** — Sicherungsverfahren (Paragrafen 413 ff. StPO), Massregeln (Paragrafen 63, 64 StGB), Gefaehrlichkeitsprognose
- **17-einziehung-und-vermoegensabschoepfung** — Einziehung (Paragrafen 73 ff. StGB), Vermögensarrest (Paragraf 111e StPO), Wertersatz
- **18-jugendsache-und-diversion-paragraf-45-jgg** — Jugendsache, Diversion (Paragraf 45 JGG), Heranwachsende (Paragraf 105 JGG)
- **19-sitzungsdienst-und-fragerecht-hauptverhandlung** — Sitzungsvertretung (Paragraf 226 StPO), Fragerecht (Paragraf 240 StPO), Erklaerungen (Paragraf 257 StPO)
- **20-plaedoyer-und-schlussvortrag-paragraf-258** — Schlussvortrag (Paragraf 258 StPO), Beweiswuerdigung, Strafzumessungsantrag (Paragraf 46 StGB)
- **21-rechtsmittel-der-staatsanwaltschaft** — Berufung, Revision, Beschwerde, zugunsten und zuungunsten (Paragraf 296 Abs. 2 StPO)
- **22-strafvollstreckung-paragraf-451** — Vollstreckung durch die Staatsanwaltschaft (Paragrafen 449 ff. StPO), Ladung, Aufschub
- **23-klageerzwingung-und-beschwerdebescheid-paragraf-172** — Bescheid (Paragraf 171 StPO), Klageerzwingungsverfahren (Paragraf 172 StPO)
- **24-abschlussverfuegung-und-entscheidungsvorschlag** — Abschlussverfuegung, Gesamtwuerdigung, Verfügungstechnik, Markierung als Vorschlag
- **25-adhaesionsverfahren-paragraf-403** — Adhaesionsantrag (Paragrafen 403 ff. StPO), Eignung zur Mitverhandlung, Abtrennung
- **26-opferschutz-nebenklage-und-verletztenrechte** — Opferschutz (Paragrafen 406d ff. StPO), Nebenklage (Paragrafen 395 ff. StPO), psychosoziale Prozessbegleitung
- **27-wiederaufnahme-zuungunsten-paragraf-362** — Wiederaufnahme zuungunsten (Paragraf 362 StPO), formale Anforderungen, ne bis in idem
- **28-internationale-rechtshilfe-und-eu-haftbefehl** — EuHb (Paragrafen 78 ff. IRG), EEA (Paragrafen 91a ff. IRG), klassische Rechtshilfe

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI bei deutschen Strafverfolgungsbehoerden. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 6 KI-VO**: KI-Systeme, die im Bereich **Strafverfolgung** zur Bewertung von Beweismitteln, zur Risikoeinschaetzung oder zur Aufklaerung von Straftaten eingesetzt werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: Soweit das System im Auftrag einer Justizbehoerde bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts** verwendet wird, gilt es ebenfalls als Hochrisiko-KI.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Verfügungsentwuerfen, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Antragsvorschlaege produziert, die Subsumtion vornimmt oder die staatsanwaltschaftliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die staatsanwaltschaftliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine erhebt Anklage, beantragt Haft oder stellt ein.** Diese Skills sind ausschliesslich **Unterstuetzung** der staatsanwaltschaftlichen Arbeit, niemals deren Ersatz. Der Dezernent prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Objektivitaetspflicht

- **Paragraf 160 Abs. 2 StPO**: Die Staatsanwaltschaft hat nicht nur die zur Belastung, sondern auch die zur Entlastung dienenden Umstaende zu ermitteln. Jede KI-Ausgabe ist auf diese Ausgewogenheit zu prüfen; eine einseitig belastende Vorbereitung widerspricht dem gesetzlichen Auftrag.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und die beamtenrechtliche Verschwiegenheitspflicht (**Paragraf 37 BeamtStG** für Landesbeamte, **Paragraf 67 BBG** für Bundesbeamte) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüft an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Weisungsgebundenheit und Revisionssicherheit

- Die Staatsanwaltschaft ist weisungsgebunden (Paragrafen 146, 147 GVG); die KI ersetzt weder Weisung noch dezernatliche Verantwortung.
- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Dezernenten vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die staatsanwaltschaftliche Bearbeitung ist zu dokumentieren.
- Aufbewahrungsfristen nach Aktenordnung und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Behörden werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload, soweit Hausrecht und Datenschutzfreigabe das erlaubt.

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
| 2. Unterlagen, Sachverhalt und Quellen | `01-akte-erstdurchsicht-und-anfangsverdacht` |
| 4. Gestaltung, Strategie und Verhandlung | `19-sitzungsdienst-und-fragerecht-hauptverhandlung` |
| 5. Verfahren, Behörde und Gericht | `04-durchsuchung-und-beschlagnahme-antrag`, `05-haftbefehlsantrag-und-untersuchungshaft`, `13-strafbefehlsantrag-paragraf-407`, `14-anklageschrift-paragraf-200`, `15-antrag-beschleunigtes-verfahren-paragraf-417`, `16-sicherungsverfahren-und-massregeln`, `22-strafvollstreckung-paragraf-451`, `23-klageerzwingung-und-beschwerdebescheid-paragraf-172`, `24-abschlussverfuegung-und-entscheidungsvorschlag`, `25-adhaesionsverfahren-paragraf-403`, `26-opferschutz-nebenklage-und-verletztenrechte` |
| 6. Ergebnis, Schreiben und Kommunikation | `07-telekommunikationsueberwachung-und-verdeckte-massnahmen` |
| 8. Spezialmodule und Schnittstellen | `02-zustaendigkeit-sta-und-amtsanwaltschaft`, `03-ermittlungsfuehrung-und-ermittlungsanweisung`, `06-vorlaeufige-festnahme-und-eilkompetenz`, `08-beschuldigtenvernehmung-und-belehrung`, `09-sachverstaendige-und-koerperliche-untersuchung`, `10-einstellung-mangels-tatverdacht-paragraf-170`, `11-einstellung-aus-opportunitaet-paragraf-153-und-153a`, `12-teileinstellung-paragraf-154-und-154a`, `17-einziehung-und-vermoegensabschoepfung`, `18-jugendsache-und-diversion-paragraf-45-jgg`, `20-plaedoyer-und-schlussvortrag-paragraf-258`, `21-rechtsmittel-der-staatsanwaltschaft`, `27-wiederaufnahme-zuungunsten-paragraf-362`, `28-internationale-rechtshilfe-und-eu-haftbefehl`, `99-finale-entscheidung-volltext`, `prozessuale-kniffe-und-rechtsprechungsanker`, `v392-praxisraster-staatsanwaltschaft-amtsanwaltschaft` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-akte-erstdurchsicht-und-anfangsverdacht` | Wenn es um 01 Akte-Erstdurchsicht und Anfangsverdacht in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `02-zustaendigkeit-sta-und-amtsanwaltschaft` | Wenn es um 02 Zuständigkeit Staatsanwaltschaft und Amtsanwaltschaft in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `03-ermittlungsfuehrung-und-ermittlungsanweisung` | Wenn es um Ermittlungsführung und Ermittlungsanweisung in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `04-durchsuchung-und-beschlagnahme-antrag` | Wenn es um 04 Durchsuchung und Beschlagnahme Antrag in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und... |
| `05-haftbefehlsantrag-und-untersuchungshaft` | Wenn es um 05 Haftbefehlsantrag und Untersuchungshaft in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung u... |
| `06-vorlaeufige-festnahme-und-eilkompetenz` | Wenn es um 06 Vorlaeufige Festnahme und Eilkompetenz in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `07-telekommunikationsueberwachung-und-verdeckte-massnahmen` | Wenn es um 07 Telekommunikationsüberwachung und Verdeckte Maßnahmen in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen... |
| `08-beschuldigtenvernehmung-und-belehrung` | Wenn es um 08 Beschuldigtenvernehmung und Belehrung in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `09-sachverstaendige-und-koerperliche-untersuchung` | Wenn es um 09 Sachverstaendige und Koerperliche Untersuchung in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `10-einstellung-mangels-tatverdacht-paragraf-170` | Wenn es um 10 Einstellung Mangels Tatverdacht Paragraf 170 in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `11-einstellung-aus-opportunitaet-paragraf-153-und-153a` | Wenn es um 11 Einstellung Aus Opportunitaet Paragraf 153 und 153a in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `12-teileinstellung-paragraf-154-und-154a` | Wenn es um 12 Teileinstellung Paragraf 154 und 154a in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `13-strafbefehlsantrag-paragraf-407` | Wenn es um Strafbefehlsantrag nach Paragraf 407 StPO in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| `14-anklageschrift-paragraf-200` | Wenn es um Anklageschrift nach Paragraf 200 StPO in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und An... |
| `15-antrag-beschleunigtes-verfahren-paragraf-417` | Wenn es um 15 Antrag Beschleunigtes Verfahren Paragraf 417 in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründ... |
| `16-sicherungsverfahren-und-massregeln` | Wenn es um 16 Sicherungsverfahren und Maßregeln in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anl... |
| `17-einziehung-und-vermoegensabschoepfung` | Wenn es um 17 Einziehung und Vermoegensabschoepfung in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `18-jugendsache-und-diversion-paragraf-45-jgg` | Wenn es um 18 Jugendsache und Diversion Paragraf 45 JGG in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| `19-sitzungsdienst-und-fragerecht-hauptverhandlung` | Wenn es um 19 Sitzungsdienst und Fragerecht Hauptverhandlung in Staatsanwaltschaft und Amtsanwaltschaft geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `20-plaedoyer-und-schlussvortrag-paragraf-258` | Wenn es um 20 Plaedoyer und Schlussvortrag Paragraf 258 in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| `21-rechtsmittel-der-staatsanwaltschaft` | Wenn es um 21 Rechtsmittel Der Staatsanwaltschaft in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `22-strafvollstreckung-paragraf-451` | Wenn es um 22 Strafvollstreckung Paragraf 451 in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `23-klageerzwingung-und-beschwerdebescheid-paragraf-172` | Wenn es um 23 Klageerzwingung und Beschwerdebescheid Paragraf 172 in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen,... |
| `24-abschlussverfuegung-und-entscheidungsvorschlag` | Wenn es um 24 Abschlussverfuegung und Entscheidungsvorschlag in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrü... |
| `25-adhaesionsverfahren-paragraf-403` | Wenn es um 25 Adhaesionsverfahren Paragraf 403 in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anla... |
| `26-opferschutz-nebenklage-und-verletztenrechte` | Wenn es um 26 Opferschutz Nebenklage und Verletztenrechte in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründu... |
| `27-wiederaufnahme-zuungunsten-paragraf-362` | Wenn es um 27 Wiederaufnahme Zuungunsten Paragraf 362 in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung u... |
| `28-internationale-rechtshilfe-und-eu-haftbefehl` | Wenn es um 28 Internationale Rechtshilfe und EU Haftbefehl in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung Volltext in Staatsanwaltschaft und Amtsanwaltschaft geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Staatsanwaltschaft und Amtsanwaltschaft geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `v392-praxisraster-staatsanwaltschaft-amtsanwaltschaft` | Wenn es um Praxisraster Staatsanwaltschaft und Amtsanwaltschaft in Staatsanwaltschaft und Amtsanwaltschaft geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

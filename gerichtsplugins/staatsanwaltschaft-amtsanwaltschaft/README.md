# Staatsanwaltschaft und Amtsanwaltschaft

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

Wenn du das hier öffnest, willst du einen Tatvorwurf entlang von Beweiswuerdigung und Strafzumessung durchdringen und einen verwertbaren Schriftsatz bauen.
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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-akte-erstdurchsicht-und-anfangsverdacht` | Strukturierte Erstdurchsicht des Ermittlungsvorgangs: Anzeige, Tatvorwurf, Anfangsverdacht, Beschuldigtenstatus, Verjährung, Zuständigkeit und erste Ermittlungsrichtung nach StPO. |
| `02-zustaendigkeit-sta-und-amtsanwaltschaft` | Sachliche und oertliche Zustaendigkeit (Paragrafen 142 und 143 GVG), Abgrenzung Staatsanwalt und Amtsanwalt nach OrgStA, Dezernatszustaendigkeit, Abgabe und Uebernahme, Zustaendigkeit beim Amtsgericht und Landgericht |
| `03-ermittlungsfuehrung-und-ermittlungsanweisung` | Führt Ermittlungen staatsanwaltschaftlich: Anfangsverdacht, Beweisthema, belastende und entlastende Umstände, konkrete Ermittlungsaufträge, Fristen, Verwertbarkeit und nächste Abschlussentscheidung. |
| `04-durchsuchung-und-beschlagnahme-antrag` | Antrag auf richterliche Anordnung der Durchsuchung (Paragrafen 102 bis 105 StPO) und Beschlagnahme (Paragrafen 94 bis 98 StPO), Verhaeltnismaessigkeit, Gefahr im Verzug, Richtervorbehalt |
| `05-haftbefehlsantrag-und-untersuchungshaft` | Antrag auf Erlass eines Haftbefehls (Paragrafen 112 und 112a und 114 StPO), dringender Tatverdacht, Haftgruende, Verhaeltnismaessigkeit (Paragraf 112 Abs. 1 Satz 2), Haftverschonung (Paragraf 116 StPO) |
| `06-vorlaeufige-festnahme-und-eilkompetenz` | Vorlaeufige Festnahme (Paragraf 127 StPO), staatsanwaltschaftliche Eilanordnungskompetenz bei Gefahr im Verzug, Vorfuehrung vor den Richter (Paragraf 128 StPO), Fristen des Paragraf 128 Abs. 1 StPO |
| `07-telekommunikationsueberwachung-und-verdeckte-massnahmen` | Antrag auf Telekommunikationsueberwachung (Paragraf 100a StPO), Online-Durchsuchung (Paragraf 100b StPO), Verkehrsdaten (Paragraf 100g StPO), Katalogtat, Subsidiaritaet, Richtervorbehalt, Kernbereichsschutz |
| `08-beschuldigtenvernehmung-und-belehrung` | Vernehmung des Beschuldigten (Paragrafen 133 und 136 und 163a StPO), Belehrung ueber Schweigerecht und Verteidigerkonsultation, verbotene Vernehmungsmethoden (Paragraf 136a StPO), Verwertungsfragen |
| `09-sachverstaendige-und-koerperliche-untersuchung` | Auswahl und Auftrag an Sachverstaendige (Paragrafen 73 bis 83 StPO), koerperliche Untersuchung und Blutprobe (Paragraf 81a StPO), DNA-Identifizierung (Paragraf 81e StPO), Gutachtenfragen, Verwertung |
| `10-einstellung-mangels-tatverdacht-paragraf-170` | Einstellung des Verfahrens mangels hinreichenden Tatverdachts (Paragraf 170 Abs. 2 StPO), Abschlussverfuegung, Bescheid an Anzeigeerstatter und Beschuldigten, Negativ-Prognose, Wiederaufnahme |
| `11-einstellung-aus-opportunitaet-paragraf-153-und-153a` | Einstellung wegen Geringfuegigkeit (Paragraf 153 StPO) und gegen Auflagen und Weisungen (Paragraf 153a StPO), Zustimmung des Gerichts, geringe Schuld, oeffentliches Interesse, Auflagenkatalog |
| `12-teileinstellung-paragraf-154-und-154a` | Beschraenkung der Verfolgung nach Paragraf 154 StPO (unwesentliche Nebentat) und Paragraf 154a StPO (Beschraenkung auf Tatteile), prozessoekonomische Konzentration, Wiederaufnahmevorbehalt |
| `13-strafbefehlsantrag-paragraf-407` | Erstellt einen Strafbefehlsantrag nach Paragrafen 407 bis 408a StPO mit hinreichendem Tatverdacht, konkretem Tatvorwurf, zulässiger Rechtsfolge, Tagessatzprüfung und Einspruchsrisiko. |
| `14-anklageschrift-paragraf-200` | Erstellt die Anklageschrift nach Paragraf 200 StPO mit Umgrenzungsfunktion, Informationsfunktion, wesentlichem Ermittlungsergebnis, Beweismitteln, Eröffnungsantrag und Zuständigkeitsprüfung. |
| `15-antrag-beschleunigtes-verfahren-paragraf-417` | Antrag im beschleunigten Verfahren (Paragrafen 417 bis 420 StPO), Eignung wegen einfachen Sachverhalts oder klarer Beweislage, Rechtsfolgenbegrenzung (Paragraf 419 StPO), muendlicher oder schriftlicher Antrag |
| `16-sicherungsverfahren-und-massregeln` | Antrag im Sicherungsverfahren (Paragrafen 413 bis 416 StPO), Massregeln der Besserung und Sicherung (Paragrafen 61 ff. StGB), Unterbringung (Paragrafen 63 und 64 StGB), Schuldunfaehigkeit (Paragraf 20 StGB) |
| `17-einziehung-und-vermoegensabschoepfung` | Einziehung von Taterträgen (Paragrafen 73 bis 76b StGB), Vermoegensarrest (Paragraf 111e StPO), selbststaendige Einziehung (Paragraf 76a StGB), Wertersatz, Sicherung im Ermittlungsverfahren |
| `18-jugendsache-und-diversion-paragraf-45-jgg` | Jugendstaatsanwaltschaftliche Bearbeitung, Diversion (Paragraf 45 JGG), Absehen von der Verfolgung, erzieherische Massnahmen, Heranwachsende (Paragraf 105 JGG), Anklage zur Jugendkammer oder zum Jugendrichter |
| `19-sitzungsdienst-und-fragerecht-hauptverhandlung` | Sitzungsvertretung der Staatsanwaltschaft (Paragraf 226 StPO), Fragerecht (Paragraf 240 StPO), Beweisantraege und Erklaerungen (Paragraf 257 StPO), Reaktion auf Antraege der Verteidigung, Vorhalt und Beweisaufnahme |
| `20-plaedoyer-und-schlussvortrag-paragraf-258` | Schlussvortrag der Staatsanwaltschaft (Paragraf 258 StPO), Wuerdigung des Beweisergebnisses, rechtliche Bewertung, konkreter Antrag zu Schuld- und Rechtsfolgenausspruch, Strafzumessungsantrag (Paragraf 46 StGB) |
| `21-rechtsmittel-der-staatsanwaltschaft` | Rechtsmittel der Staatsanwaltschaft: Berufung (Paragrafen 312 ff. StPO), Revision (Paragrafen 333 ff. StPO), Beschwerde (Paragrafen 304 ff. StPO), zugunsten und zuungunsten des Angeklagten (Paragraf 296 Abs. 2 StPO), Fristen und Begruendung |
| `22-strafvollstreckung-paragraf-451` | Strafvollstreckung durch die Staatsanwaltschaft als Vollstreckungsbehoerde (Paragrafen 449 ff. StPO, Paragraf 451 StPO), Vollstreckungsplan, Ladung zum Strafantritt, Vollstreckungsaufschub (Paragraf 456 StPO), StVollstrO |
| `23-klageerzwingung-und-beschwerdebescheid-paragraf-172` | Bescheid auf Beschwerde des Anzeigeerstatters (Paragraf 171 StPO), Vorschaltbeschwerde und Klageerzwingungsverfahren (Paragraf 172 StPO), Begruendungsanforderungen, Vorlage an Generalstaatsanwaltschaft |
| `24-abschlussverfuegung-und-entscheidungsvorschlag` | Strukturierte Abschlussverfuegung des Dezernats: Gesamtwuerdigung des Ermittlungsergebnisses, Entscheidung zwischen Anklage, Strafbefehl, Einstellung und Massregel, Verfuegungstechnik, Risikohinweise, ausdrueckliche Markierung als Vorschlag |
| `25-adhaesionsverfahren-paragraf-403` | Adhaesionsantrag des Verletzten im Strafverfahren (Paragrafen 403 bis 406c StPO), Pruefung der Zulaessigkeit und Eignung zur Mitverhandlung, Abtrennung nach Paragraf 406 Abs. 1 Satz 6 StPO, Schnittstelle zum Opferschutz und zur Verfahren... |
| `26-opferschutz-nebenklage-und-verletztenrechte` | Opferschutzpflichten der Staatsanwaltschaft (Paragrafen 406d bis 406l StPO), Anschluss als Nebenklaeger (Paragrafen 395 bis 402 StPO), opferschutzrechtliche Belehrung, psychosoziale Prozessbegleitung (Paragraf 406g StPO), Akteneinsicht d... |
| `27-wiederaufnahme-zuungunsten-paragraf-362` | Antrag der Staatsanwaltschaft auf Wiederaufnahme zuungunsten des Verurteilten oder Freigesprochenen (Paragraf 362 StPO), Pruefungsschema der Wiederaufnahmegruende, formale Anforderungen (Paragraf 366 StPO), Verfahren nach Paragrafen 367... |
| `28-internationale-rechtshilfe-und-eu-haftbefehl` | Internationale Rechtshilfe in Strafsachen: Europaeischer Haftbefehl (Paragrafen 78 bis 83i IRG), Rechtshilfeersuchen (Paragrafen 59 ff. IRG), Europaeische Ermittlungsanordnung (Paragrafen 91a ff. IRG); Pruefschema fuer Ausstellung und Be... |
| `99-finale-entscheidung-volltext` | Erzeugt Anklageschrift, Strafbefehlsantrag, Einstellungs- oder Abschlussverfügung als zeichnungsreifen staatsanwaltschaftlichen Volltext mit Tatvorwurf, Beweisstand, Verfügungssatz und Rechtsbehelfshinweis. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Stellt staatsanwaltschaftliche Verfahrenskniffe, Rechtsprechungsanker, Eingriffsgrenzen, Abschlussoptionen und Sitzungsdienst-Strategie in eine sofort nutzbare Matrix. |
| `v392-praxisraster-staatsanwaltschaft-amtsanwaltschaft` | Praxisraster für Staatsanwaltschaft und Amtsanwaltschaft: Zuständigkeit, Verfahrensstand, Pflichtnormen, Beweisbedarf und passendes Endprodukt werden in der richtigen gerichtlichen oder staatsanwaltschaftlichen Rolle abgearbeitet. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# GOÄ Gebührenordnung für Ärzte

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`goae-gebuehrenordnung-aerzte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/goae-gebuehrenordnung-aerzte.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/goae-gebuehrenordnung-aerzte-werkstatt.md" download><code>goae-gebuehrenordnung-aerzte-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/goae-gebuehrenordnung-aerzte-schnellstart.md" download><code>goae-gebuehrenordnung-aerzte-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten.

## Wofür dieses Plugin da ist
Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

Das Plugin ist als Arbeitswerkzeug gedacht: Es startet mit einem Kaltstart-Interview, sortiert Unterlagen, prüft Fristen und routet dann in Spezial-Skills. Es soll Anfänger an die Hand nehmen und Profis schnell zu belastbaren Outputs bringen.

## Typischer Workflow
1. **Allgemein-Skill starten:** Rolle, Ziel, Frist, Unterlagen und gewünschtes Ergebnis klären.
2. **Dokumente einlesen:** Verträge, Bescheide, Rechnungen, Tabellen, Registerdaten, Behördenpost oder Screenshots strukturieren.
3. **Spezial-Skill wählen:** Das Plugin schlägt den passenden Skill vor und erklärt, welches Ergebnis damit entsteht.
4. **Live-Quellen prüfen:** Normtext, Behördenseite, EU-Text, Formular oder frei zugängliche Rechtsprechung aktualisieren.
5. **Output erzeugen:** Memo, Antrag, Stellungnahme, Vertragsklausel, Berechnung, Checkliste oder Mandantenbrief.
6. **Red-Team:** Fristen, Zuständigkeit, Zahlen, Quellen und Gegenargumente kontrollieren.

## Quellenanker
- Amtliche Gesetzestexte: gesetze-im-internet.de.
- EU-Recht: EUR-Lex und amtliche Kommissionsseiten.
- Behördenpraxis: zuständige Bundes-/Landesbehörden, Bundesnetzagentur, BaFin, BfArM, G-BA, BKartA oder Länderstellen je nach Thema.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.

## Skill-Schwerpunkte
| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Workflow | Kaltstart, Dokumentenintake, Fristen, Quellencheck, Output-Wahl, Red-Team |
| Materielle Prüfung | Tatbestände, Ausnahmen, Schwellen, Beweislast, Berechnungen, Rechtsfolgen |
| Verfahren und Kommunikation | Anträge, Anhörungen, Beschwerden, Schriftsätze, Behördenkontakt, Mandantenkommunikation |
| Spezialthemen | Branchen-, Vertrags-, Gebühren-, Aufsichts-, EU- und Edge-Case-Prüfungen |

## Quellen- und Halluzinationsschutz
Dieses Plugin soll keine nicht prüfbaren Fundstellen produzieren. Bei unsicherer oder dynamischer Rechtslage wird der Live-Quellencheck ausdrücklich vorgeschaltet.

## Lizenz
Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 65 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `5b-standardtarif-gebuehren-andere-6a` | GOÄ § 5b Standardtarif PKV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Ref... |
| `abrechnung-telemedizin-videosprechstunde-goae` | Abrechnung Telemedizin Videosprechstunde GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht... |
| `abschnitt-a-beratungen-und-untersuchungen` | Abschnitt A Beratungen und Untersuchungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `abschnitt-b-c-abtretung-factoring` | Abschnitt B Grundleistungen Zuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktue... |
| `abschnitt-c-nichtgebietsbezogene-sonderleistungen` | Abschnitt C nichtgebietsbezogene Sonderleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufs... |
| `abtretung-factoring-arzthonorar-datenschutz` | Abtretung Factoring Arzthonorar Datenschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht,... |
| `analogabrechnung-intake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Analogabrechnung Intake § 6 GOÄ im Goae Gebührenordnung Aerzte. |
| `analoge-bewertung-abrechnung-telemedizin` | Analoge Bewertung neue Verfahren Innovation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht,... |
| `anwendungsbereich-berufliche-abweichende` | GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsre... |
| `arbeitsunfaehigkeitsbescheinigung-privatpatient` | Arbeitsunfähigkeitsbescheinigung Privatpatient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrec... |
| `arztbrief-begruendung-nachfordern` | Arztbrief Begründung nachfordern: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle G... |
| `arzthonorarprozess-dokumentenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Arzthonorarprozess Dokumentenplan im Goae Gebührenordnung Aerzte. |
| `auslandsbehandlung-deutsche-goae-anwendung` | Auslandsbehandlung deutsche GOÄ Anwendung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `begruendung-ueber-schwellenwert-redigieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Begründung über Schwellenwert redigieren im Goae Gebührenordnung Aerzte. |
| `beihilfe-einwendungen-belegarzt-konsiliararzt` | Beihilfe Einwendungen und Differenzbetrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `belegarzt-und-konsiliararzt-abrechnung` | Belegarzt und Konsiliararzt Abrechnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktu... |
| `berufsrecht-ueberhoehte-liquidation` | Berufsrecht überhöhte Liquidation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle... |
| `ersatz-auslagen-faelligkeit-rechnungspflicht` | GOÄ § 10 Ersatz von Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-R... |
| `erstattung-pkv-faelligkeit-verzug` | Erstattung PKV vs Honoraranspruch Patient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `faelligkeit-verzug-mahnung-honorarklage` | Fälligkeit Verzug Mahnung Honorarklage: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktu... |
| `gebuehrenrahmen-schwellenwert-ampel` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Gebührenrahmen Schwellenwert Ampel im Goae Gebührenordnung Aerzte. |
| `goae-2-abweichende-vereinbarung-honorarvereinbarung` | GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Ber... |
| `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen` | GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Be... |
| `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` | GOÄ § 5 Bemessung Gebührenrahmen 2 und 3 1 und 8 1 und 15 Schwelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-R... |
| `goae-5a-bemessung-im-basistarif` | GOÄ § 5a Bemessung im Basistarif: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle G... |
| `goae-6-gebuehren-fuer-andere-leistungen-analogbewertung` | GOÄ § 6 Gebühren für andere Leistungen Analogbewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, B... |
| `goae-6a-stationaere-minderung-25-prozent-15-prozent` | GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Beru... |
| `goae-8-wegegeld` | GOÄ § 8 Wegegeld: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweis... |
| `goae-9-reiseentschaedigung` | GOÄ § 9 Reiseentschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Ref... |
| `goae-12-faelligkeit-und-rechnungspflicht` | GOÄ § 12 Fälligkeit und Rechnungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, ak... |
| `goae-14-zahlung-durch-oeffentliche-leistungstraeger` | GOÄ § 14 Zahlung durch öffentliche Leistungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Beruf... |
| `goae-entschaedigungen-wegegeld` | GOÄ § 7 Entschädigungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reform... |
| `goae-reform-referentenentwuerfe-beobachten` | GOÄ Reform Referentenentwürfe beobachten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, ak... |
| `goae-selbstaendige-aerztliche-bemessung` | GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelun... |
| `gutachten-atteste-bescheinigungen` | Gutachten Atteste Bescheinigungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle... |
| `igel-aufklaerung-klageerwiderung` | IGeL Aufklärung Kosteninformation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle... |
| `kaltstart-goae-rechnung-pruefen` | Kaltstart GOÄ Rechnung prüfen: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor. |
| `klageerwiderung-honorarprozess` | Klageerwiderung Honorarprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ... |
| `kosmetische-leistungen-medizinische-indikation` | Kosmetische Leistungen medizinische Indikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrec... |
| `laborleistungen-hoechstsatz-leistungskette` | Laborleistungen und Höchstsatz Besonderheiten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrech... |
| `leistungskette-zielleistung-keine-aufspaltung` | Leistungskette Zielleistung keine Aufspaltung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrech... |
| `livecheck-goae-text-und-reformstand` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck GOÄ Text und Reformstand im Goae Gebührenordnung Aerzte. |
| `m-iii-mandantenmail-patient-materialkosten` | M III M IV Labor Delegation Speziallabor: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, ak... |
| `mandantenmail-patient-freundlich-klar` | Mandantenmail Patient freundlich klar: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktue... |
| `materialkosten-auslagen-abgrenzung-10-goae` | Materialkosten Auslagen Abgrenzung § 10 GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht,... |
| `mehrfachansatz-ausschluesse-minderjaehrige` | Mehrfachansatz Ausschlüsse Nebeneinanderberechnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Beruf... |
| `minderjaehrige-einwilligung-rechnung-schuldner` | Minderjährige Einwilligung Rechnung Schuldner: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrech... |
| `notfall-behandlung-ausserhalb-sprechstunde` | Notfall Behandlung außerhalb Sprechstunde: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `op-komplexe-patientenbrief-einwendung` | OP-Komplexe Narkose Assistenz Zuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, akt... |
| `patientenbrief-und-einwendung-formulieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Patientenbrief und Einwendung formulieren im Goae Gebührenordnung Aerzte. |
| `plausibilitaetscheck-rechnung-mathematisch` | Plausibilitätscheck Rechnung mathematisch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `psychotherapie-psychiatrie-radiologie` | Psychotherapie Psychiatrie Gesprächsleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrec... |
| `radiologie-schnittbild-zielleistung` | Radiologie Schnittbild Zielleistung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuell... |
| `rechnung-pdf-reform-referentenentwuerfe` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema GOÄ Rechnung aus PDF extrahieren im Goae Gebührenordnung Aerzte. |
| `red-team-goae-rechnung-halluzinationscheck` | Red-Team GOÄ Rechnung Halluzinationscheck: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `sachverstaendigenfragen-goae-streit` | Sachverständigenfragen GOÄ Streit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle... |
| `schlichtungsstelle-aerztekammer-stationaere` | Schlichtungsstelle Ärztekammer Honorarstreit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht... |
| `stationaere-privataerztliche-liquidation` | Stationäre privatärztliche Liquidation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktu... |
| `steigerungssatz-begruendung-individuell-patientenbezogen` | Steigerungssatz Begründung individuell patientenbezogen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen,... |
| `tabellenexport-pruefliste-verjaehrung` | Tabellenexport GOÄ Prüfliste: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-R... |
| `verjaehrung-aerztlicher-honoraranspruch` | Verjährung ärztlicher Honoraranspruch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktue... |
| `wahlleistungsvereinbarung-krankenhaus-goae` | Wahlleistungsvereinbarung Krankenhaus GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |
| `wegegeld-besuch-zahnaerztliche-schnittstelle` | Wegegeld Besuch mehrere Patienten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle... |
| `zahnaerztliche-schnittstelle-goz-goae` | Zahnärztliche Schnittstelle GOZ GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuell... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

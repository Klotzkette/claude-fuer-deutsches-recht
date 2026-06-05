---
name: beschwerde-besoldung-zulagen-beurteilung
description: "Beschwerde Besoldung Zulagen Beurteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beschwerde Besoldung Zulagen Beurteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beschwerde Besoldung Zulagen Beurteilung** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beschwerde-gegen-beurteilung-und-laufbahnentscheidung` | Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `besoldung-zulagen-auslandsverwendungszuschlag` | Besoldung, Zulagen, AVZ: prüft BBesG, AVZ-Berechnung, Erschwernis- und Einsatzzulagen sowie Rückforderungen. Norm-/Quellenanker: BBesG §§ 56–58, EZulV, AuslVZV. |
| `beurteilung-konkurrentenstreit-auswahlentscheidung` | Beurteilung, Konkurrentenstreit, Auswahlentscheidung: prüft Beurteilungsfehlerlehre, Bestenauslese, Auswahlvermerk und einstweiligen Rechtsschutz. Norm-/Quellenanker: Art. 33 Abs. 2 GG, § 3 SG, ZDv A-1340/50. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Beschwerde Besoldung Zulagen Beurteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beschwerde-gegen-beurteilung-und-laufbahnentscheidung`

**Fokus:** Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Beschwerde gegen Beurteilung und Laufbahnentscheidung

## Fachkern: Beschwerde gegen Beurteilung und Laufbahnentscheidung
- **Spezialgegenstand:** Beschwerde gegen Beurteilung und Laufbahnentscheidung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Beurteilung (planmäßig oder Anlassbeurteilung) und die darauf gestützte Laufbahnentscheidung (Beförderung, Verwendungsentscheidung, Auswahlentscheidung) sind die Grundlage der Karriere des Soldaten. Beide sind im WBO-Weg anfechtbar (§ 1 WBO). Der Skill ordnet Beurteilungssystematik, Beschwerdegegenstände und Eilrechtsschutz im Konkurrentenstreit.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Beurteilung (planmäßig, Anlass, Probezeit)?
- Welcher Beurteiler (erster, zweiter, Höher- oder Endbeurteiler)?
- Welche konkrete Wertung wird angegriffen (Einzelmerkmale, Gesamtwertung, Verwendungsempfehlung)?
- Wann eröffnet, wann zugegangen (Frist § 6 WBO)?
- Ist parallel ein Konkurrentenstreit anhängig (Beförderung, Dienstposten)?
- Welcher Vergleichsmaßstab steht zur Verfügung (Vergleichsgruppe, Quotenregelung)?

## Rechtlicher Rahmen

- § 27 SG: Beurteilung als dienstliche Bewertung der Eignung, Befähigung und fachlichen Leistung.
- Laufbahnrecht: Soldatenlaufbahnverordnung (SLV) – Voraussetzungen für Beförderung, Verwendung, Wechsel.
- Beurteilungsbestimmungen Bundeswehr – periodisch fortgeschrieben.
- Art. 33 II GG: Bestenauslese – Anspruch auf leistungsbezogene Auswahl.
- § 1 WBO: Beschwerderecht – auch gegen Beurteilung und Auswahlentscheidung.
- § 21 WBO: Erstinstanzliche Zuständigkeit BVerwG bei Maßnahme höherer Vorgesetzter (oft im Konkurrentenstreit).
- BVerwG-Rspr. zu Beurteilungsspielraum und Plausibilitätskontrolle – ständige Rechtsprechung.

## / Schritt für Schritt

1. **Beurteilung und Anlass dokumentieren.** Eröffnungsdatum, Beurteilerkette, Vergleichsgruppe.
2. **Fehler identifizieren.**
 - Formaler Fehler (falsche Beurteilerkette, fehlende Eröffnung),
 - Sachlicher Fehler (Verwertungsverbote, Hörensagen, falsche Tatsachenbasis),
 - Bewertungsfehler (Plausibilitätslücke, Maßstabsverstöße),
 - Quotenfehler (falsche Vergleichsgruppe).
3. **Frist sichern.** § 6 WBO: 1 Monat ab Eröffnung. Fristwahrende Beschwerde mit Vorbehalt der Begründung möglich.
4. **Akteneinsicht.** Personalakte, andere Beurteilungen (anonymisierte Auswertung), Quotenmatrix.
5. **Konkurrentenstreit.**
 - Eilantrag § 21 WBO i.V.m. § 80a VwGO entsprechend, wenn Beförderung anderer droht.
 - Schutzschrift zum BVerwG bei höchstrangiger Auswahl.
6. **Beschwerdeschrift.** Konkrete Rüge der Beurteilungsfehler, Anträge auf Aufhebung und Neubeurteilung.
7. **Mündliche Verhandlung.** Bei Truppendienstgericht häufig; persönliches Erscheinen.

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Klar fehlerhafte Tatsachen | Beweisangebote, Zeugenliste |
| Plausibilitätsfehler | Plausibilitätskontrolle nach BVerwG-Rspr. |
| Drohende Beförderung Mitbewerber | Eilantrag § 21 WBO mit Beförderungsstopp |
| Reine Bemessungsfrage | Beschwerde, ohne Eilrechtsschutz |
| Quotenproblem | Vergleichsgruppe und Maßstab angreifen |

## Praxistipps

- Beurteilungen sind nur eingeschränkt überprüfbar – Spielraum der Beurteiler. Fokus auf formelle und Plausibilitätsfehler.
- Eröffnungstermin Pflicht – ohne Eröffnung läuft die Frist nicht.
- Personalakte spiegelt die Auswahlerwägungen wider – zwingende Einsicht vor Eilrechtsschutz.
- Schutzschrift beim BVerwG vor Beförderungsterminen anderer – häufig nur wenige Wochen Reaktionszeit.
- Maßstabsfragen erfordern Vergleichsgruppe – ohne diese kein Erfolg im Konkurrentenstreit.

## Mustertexte

**Beschwerde gegen Beurteilung:**
"Gegen die mir am [Datum] eröffnete Beurteilung lege ich fristwahrend Beschwerde nach § 1 WBO ein. Ich beantrage: 1. Aufhebung der Beurteilung. 2. Neuerstellung durch [...]. 3. Einsicht in die Vergleichsgruppe und die Quotenmatrix. Begründung folgt nach Akteneinsicht. Rügen u.a.: a) fehlerhafte Tatsachenfeststellung in [...]. b) Plausibilitätslücke zwischen Einzel- und Gesamtwertung. c) Vergleichsgruppe nicht ordnungsgemäß gebildet."

**Eilantrag § 21 WBO Konkurrentenstreit:**
"An das Bundesverwaltungsgericht, Wehrdienstsenat. Es wird beantragt: Im Wege der einstweiligen Anordnung die Antragsgegnerin zu verpflichten, den Dienstposten [Bezeichnung] vorläufig nicht mit Mitbewerber [Name] zu besetzen, bis über die Beschwerde meines Mandanten rechtskräftig entschieden ist. Anordnungsgrund: drohende Beförderung am [Datum]. Anordnungsanspruch: fehlerhafte Auswahlentscheidung."

## Typische Fehler

- Eröffnungsdatum nicht dokumentiert – Frist unsicher.
- Akteneinsicht erst nach Beschwerdeeinlegung – Rügen lückenhaft.
- Schutzschrift im Konkurrentenstreit zu spät – Beförderung erfolgt vor Eilbeschluss.
- Plausibilitätsangriff ohne Vergleichsmaßstab.
- Verwaltungsgerichtsweg gewählt – WBO ist exklusiv.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- eilverfahren-konkurrentenstreit-wehrdienstsenat
- beurteilung-konkurrentenstreit-auswahlentscheidung
- wehrbeschwerdeordnung-beschwerde-frist-form
- personalakte-einsicht-datenschutz
- ernennung-dienstgrad-laufbahnrecht

## Quellen Stand 06/2026

- § 27 SG, Soldatenlaufbahnverordnung – Volltexte gesetze-im-internet.de.
- Beurteilungsbestimmungen Bundeswehr – aktuelle Fassung beim BMVg.
- Art. 33 II GG; BVerfG zu Bestenauslese – ständige Rechtsprechung.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu Beurteilungsspielraum und Plausibilitätskontrolle (Az. nach Verifikation).
- WBO §§ 1, 6, 17, 21 – Volltext gesetze-im-internet.de.

## 2. `besoldung-zulagen-auslandsverwendungszuschlag`

**Fokus:** Besoldung, Zulagen, AVZ: prüft BBesG, AVZ-Berechnung, Erschwernis- und Einsatzzulagen sowie Rückforderungen. Norm-/Quellenanker: BBesG §§ 56–58, EZulV, AuslVZV.

# Besoldung, Zulagen und Auslandsverwendungszuschlag

## Fachkern: Besoldung, Zulagen und Auslandsverwendungszuschlag
- **Spezialgegenstand:** Besoldung, Zulagen und Auslandsverwendungszuschlag. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldaten erhalten Grundgehalt nach BBesG (A-Besoldung) zuzüglich Zulagen. Bei Auslandseinsätzen kommt der AVZ hinzu (§§ 56–58 BBesG), gestaffelt nach Gefährdungsstufen (bis ca. 110 €/Tag).

Häufige Fehler: Fehlberechnungen beim AVZ, nicht ausgezahlte Erschwerniszulagen, Rückforderungen nach fehlerhafter Auszahlung.

## Einschlägige Normen und Quellen

- BBesG — Bundesbesoldungsgesetz
- §§ 56–58 BBesG — Auslandsverwendungszuschlag (AVZ)
- EZulV — Erschwerniszulagenverordnung
- AuslVZV — Auslandsverwendungszulagenverordnung
- § 9a BBesG — Rückforderung
- EinsatzWVG — Einsatzweiterverwendungsgesetz

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Besoldungsgruppe und welcher Dienstgrad?
- Handelt es sich um Auslandseinsatz, und welche Einsatzregion?
- Welche Zulagen werden beansprucht oder sind streitig?
- Liegt ein Rückforderungsbescheid vor?
- Wurden Einsatztage korrekt berechnet?
- Gibt es einen Widerspruch gegen eine Besoldungsmitteilung?

## Prüf- und Arbeitslogik

### Schritt 1 — Grundgehalt und Besoldungsgruppe

Anlage IV BBesG: Grundgehaltstabellen nach Gruppen und Stufen.
Beförderung → sofortiger Gruppenwechsel.
Stufenaufstieg: § 27 BBesG erfahrungsabhängig (2–3 Jahre/Stufe).
Fehler: falsche Stufenzuordnung bei Einstellung prüfen.

### Schritt 2 — Auslandsverwendungszuschlag §§ 56–58 BBesG

Stufen 1–7 nach AuslVZV: abhängig von Gefahrenlage.
Tageweise Berechnung für jeden Einsatztag.
Abgrenzung: AVZ (Einsatz) vs. Auslandsdienstbezüge § 52 BBesG (stationäre Verwendung).
Fehler: falsche Stufenzuordnung → Nachforderung (Ausschlussfrist beachten!).

### Schritt 3 — Erschwernis- und Sonderzulagen EZulV

§§ 47–50 BBesG i.V.m. EZulV: Fallschirmspringer, Kampfschwimmer, ABC, Heeresflugzeugführer.
Voraussetzung: aktive Ausübung der qualifizierten Tätigkeit.
Wegfall bei Verwendungswechsel → sofort, keine Übergangsfrist ohne Rechtsgrundlage.

### Schritt 4 — Rückforderung § 9a BBesG

Überzahlung grundsätzlich rückforderbar.
Gutgläubiger Verbrauch schützt: kein Rückforderungsanspruch.
Bösgläubigkeit: Soldat wusste oder hätte wissen müssen.
Billigkeitserlass § 12 Abs. 2 BBesG: Ratenzahlung, Stundung.

### Schritt 5 — Rechtsbehelfe

Widerspruch gegen Besoldungsbescheid: 1 Monat Zustellung.
Klage: VG (Besoldungsstreitigkeiten).
Verjährung: 3 Jahre, Ausschlussfristen beachten.
Parallel: Billigkeitserlass beantragen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: AVZ-Gefährdungsstufen und Tagessätze (aktuell prüfen)
- Berechnungsschema AVZ für Einsatzzeitraum
- Checkliste: Unterlagen für Besoldungswiderspruch

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — BBesG §§ 56–58
- https://www.gesetze-im-internet.de/ezulv/ — EZulV
- https://www.gesetze-im-internet.de/auslvzv/ — AuslVZV
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `beurteilung-konkurrentenstreit-auswahlentscheidung`

**Fokus:** Beurteilung, Konkurrentenstreit, Auswahlentscheidung: prüft Beurteilungsfehlerlehre, Bestenauslese, Auswahlvermerk und einstweiligen Rechtsschutz. Norm-/Quellenanker: Art. 33 Abs. 2 GG, § 3 SG, ZDv A-1340/50.

# Beurteilung, Konkurrentenstreit und Auswahlentscheidung

## Fachkern: Beurteilung, Konkurrentenstreit und Auswahlentscheidung
- **Spezialgegenstand:** Beurteilung, Konkurrentenstreit und Auswahlentscheidung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Beurteilungen sind Grundlage für Beförderungen und Verwendungsentscheidungen. Fehlerhafte Beurteilungen blockieren Karrieren; unterlegene Bewerber haben Konkurrentenschutzrecht aus Art. 33 Abs. 2 GG.

Typische Fehler: unzuständiger Beurteiler, fehlende Begründung, Nichtberücksichtigung wesentlicher Leistungen, Verstoß gegen ZDv-Maßstäbe. Einstweiliger Rechtsschutz ist oft zeitkritisch.

## Einschlägige Normen und Quellen

- Art. 33 Abs. 2 GG — Bestenauslese
- § 3 SG — Ernennungs- und Verwendungsgrundsätze
- § 23 SG — Personalakte und Beurteilungen
- ZDv A-1340/50 — Beurteilungsbestimmungen
- §§ 6, 17 WBO — Beschwerde und gerichtlicher Antrag
- § 123 VwGO — Einstweiliger Rechtsschutz (analog)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Beurteilung oder Auswahlentscheidung wird angefochten?
- Wann wurde die Beurteilung eröffnet (Fristbeginn!)?
- Welche konkreten Fehler werden gerügt?
- Gibt es Auswahlentscheidung zugunsten eines Konkurrenten?
- Ist die Stelle noch unbesetzt (einstweiliger Rechtsschutz sinnvoll)?
- Soll Besetzungsstopp beantragt werden?

## Prüf- und Arbeitslogik

### Schritt 1 — Beurteilungsfehlerlehre

Dienstherr hat Beurteilungsspielraum: nur Fehler kontrollierbar, nicht Richtigkeit.
Kontrollfähige Fehler: Unzuständigkeit des Beurteilers, Verfahrensfehler, sachfremde Erwägungen, Widerspruch zum Akteninhalt.
Nicht prüfbar: Wertung an sich, solange nachvollziehbar.

### Schritt 2 — Auswahlentscheidung und Bestenauslese

Art. 33 Abs. 2 GG: Eignung, Befähigung, fachliche Leistung.
Aktuelle Beurteilung hat Vorrang vor älteren.
Gleichwertigkeit: Hilfskriterien zulässig (Vorbildung, Einsatzerfahrung).
Auswahlvermerk: muss Bewerbervergleich erkennbar machen.

### Schritt 3 — WBO-Beschwerde gegen Beurteilung

Frist: 1 Monat nach Eröffnung (§ 6 WBO).
Ziel: Aufhebung und Neubeurteilung.
Gleichzeitig: WBO-Beschwerde gegen Auswahlentscheidung (separate Maßnahme!).
Eröffnungsprotokoll aufbewahren.

### Schritt 4 — Einstweiliger Rechtsschutz

Antrag auf gerichtliche Entscheidung § 17 WBO beim TDG.
Besetzungsstopp: TDG kann vorläufig untersagen.
Sofort handeln: Beförderung schafft vollendete Tatsachen!
Akteneinsicht beantragen (Auswahlvermerk, Beurteilungen Mitbewerber).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster-WBO-Beschwerde gegen Beurteilung
- Checkliste: Beurteilungsfehler — Typen und Nachweis
- Prüfschema: Auswahlentscheidung Art. 33 Abs. 2 GG

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — § 3 SG
- https://www.bverwg.de — BVerwG 2 WD Beurteilungsrechtsprechung
- https://dejure.org/gesetze/GG/33.html
- https://openjur.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

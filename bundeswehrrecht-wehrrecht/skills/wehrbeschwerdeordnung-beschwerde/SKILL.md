---
name: wehrbeschwerdeordnung-beschwerde
description: "Wehrbeschwerdeordnung Beschwerde: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wehrbeschwerdeordnung Beschwerde

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Wehrbeschwerdeordnung Beschwerde** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wehrbeschwerdeordnung-beschwerde-frist-form` | Wehrbeschwerdeordnung Beschwerde Frist Form: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `schadenersatz-regress-dienstunfall-material` | Schadensersatz, Regress, Dienstunfall, Materialschäden: prüft SVG, BHO § 59, Regress gegen Soldaten und Haftungsrecht. Norm-/Quellenanker: SVG, SG § 24, BHO, BGB §§ 249 ff. |
| `aerztliche-begutachtung-dienstfaehigkeit` | Ärztliche Begutachtung und Dienstfähigkeit: prüft Begutachtungsverfahren, Tauglichkeitsstufen, Rechtsbehelfe und Versorgungsfolgen. Norm-/Quellenanker: §§ 44–45 SG, SVG, DV 46/1. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Wehrbeschwerdeordnung Beschwerde**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wehrbeschwerdeordnung-beschwerde-frist-form`

**Fokus:** Wehrbeschwerdeordnung Beschwerde Frist Form: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Wehrbeschwerdeordnung – Beschwerde, Frist und Form

## Fachkern: Wehrbeschwerdeordnung – Beschwerde, Frist und Form
- **Spezialgegenstand:** Wehrbeschwerdeordnung – Beschwerde, Frist und Form. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Wehrbeschwerdeordnung (WBO) ist der zentrale Rechtsschutzweg des Soldaten gegen truppendienstliche Maßnahmen, Befehle, Beurteilungen, Versetzungen, Verwendungsentscheidungen und sonstige Beeinträchtigungen seiner Rechtsstellung. Sie ist verbindlich und im Regelfall ausschließlich – ein direkter Verwaltungsgerichtsweg ist gesperrt. Der Skill führt durch Statthaftigkeit, Frist, Form, Zuständigkeit und Stufen der WBO.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Was wird angegriffen (Befehl, Maßnahme, Verhalten, Beurteilung, Versetzung, ablehnende Personalentscheidung)?
- Wann ist die Maßnahme bekannt geworden? Beweis des Zugangsdatums?
- Wer ist Beschwerdegegner – nächster Disziplinarvorgesetzter? Höherer Truppenvorgesetzter?
- Bisheriger Verfahrensstand: bereits Beschwerde eingelegt? Bescheid ergangen? Weitere Beschwerde?
- Eilbedürfnis? Konkurrentenstreit, vorläufige Dienstenthebung, kurzfristige Versetzung?
- Soll Wirkung der Maßnahme einstweilig ausgesetzt werden (§ 3 WBO Aussetzung)?

## Rechtlicher Rahmen

- § 1 WBO: Statthaftigkeit der Beschwerde – gegen Beeinträchtigung in Rechten durch Vorgesetzte oder Dienststelle.
- § 3 WBO: Aufschiebende Wirkung – grundsätzlich keine, Aussetzung der Vollziehung in Ausnahmen.
- § 5 WBO: Beschwerderecht und persönliches Einlegen, Schriftform oder zur Niederschrift.
- § 6 WBO: Beschwerdefrist – 1 Monat ab Kenntnis.
- § 9 WBO: Entscheidung über Beschwerde durch Beschwerdestelle.
- § 16 WBO: Weitere Beschwerde – 2 Wochen ab Zustellung des Beschwerdebescheids.
- § 17 WBO: Antrag auf gerichtliche Entscheidung – Truppendienstgericht.
- § 21 WBO: Antrag auf gerichtliche Entscheidung beim BVerwG (bei truppendienstlicher Erstmaßnahme höherer Vorgesetzter).
- § 22 WBO: Aufschiebende Wirkung der gerichtlichen Anfechtung in eng begrenzten Fällen.
- § 23 WBO: Mündliche Verhandlung beim Truppendienstgericht.

## / Schritt für Schritt

1. **Statthaftigkeit prüfen.** Ist die Maßnahme eine Beschwer iSd § 1 WBO? Befehle, Beurteilungen, ablehnende Personalentscheidungen sind statthafte Beschwerdegegenstände. Disziplinarmaßnahmen einfacher Art werden im WDO-Weg angegriffen.
2. **Frist berechnen.** § 6 WBO: 1 Monat ab Kenntnis. Bei mehrtägiger Maßnahme – Beginn der Frist? Zugang nachweisbar? Schutzschrift mit Vorbehalt der Begründung möglich.
3. **Form wählen.** Schriftlich oder zur Niederschrift bei der nächsten Dienststelle. Per Fax oder elektronisch nach den Maßgaben der jeweiligen Dienststellen-Empfangswege.
4. **Adressat.** Bei einfachen Beschwerden: nächster Disziplinarvorgesetzter des Beschwerdegegners. Bei höhergradigen Vorgesetzten: nächsthöhere Stelle.
5. **Aussetzung beantragen,** wenn Eilbedürfnis besteht (§ 3 II WBO).
6. **Begründung.** Auch nachreichbar; Frist erst durch Begründung gewahrt? Nein – Beschwerde gilt mit Fristwahrung eingelegt, Begründung als Schriftsatz nachreichbar.
7. **Beschwerdebescheid prüfen.** Form, Zustellung, Begründung. Bei Erfolglosigkeit: weitere Beschwerde oder Antrag auf gerichtliche Entscheidung (§§ 16, 17 WBO).
8. **Gerichtliches Verfahren** beim Truppendienstgericht – 2-Wochen-Antragsfrist nach Zustellung des letzten Beschwerdebescheids.

## Trade-off-Matrix

| Konstellation | Sofortige Beschwerde | Beschwerde nach Akteneinsicht |
| --- | --- | --- |
| Klare Frist-Auslaufgefahr | Ja, fristwahrend ohne Begründung | Risiko Fristablauf |
| Komplexer Sachverhalt | Schutzschrift mit Vorbehalt | Begründete Beschwerde |
| Konkurrentenstreit | Eilantrag § 21 WBO | Hauptsacheantrag |
| Vorläufige Dienstenthebung | § 3 II WBO Aussetzung | nur in Ausnahmen sinnvoll |

## Praxistipps

- Beschwerde immer per Schriftstück mit Eingangsbestätigung – formlose mündliche Beschwerde zum Disziplinarvorgesetzten unsicher.
- Postlaufzeiten einkalkulieren. Bei Auslandsverwendung Einlegung über Feldpostadresse oder konsularisch.
- Akteneinsicht (§ 29 SG, § 99 VwGO entsprechend) parallel beantragen.
- Aufschiebende Wirkung der Beschwerde ist Ausnahme; ohne Aussetzungsantrag bleibt die Maßnahme vollziehbar.
- Auch unterhalb der Beschwerdeschwelle: Petition (Art. 17 GG) und Eingabe beim Wehrbeauftragten (Art. 45b GG, WBeauftrG) sind parallele Instrumente.

## Mustertexte

**Fristwahrende WBO-Beschwerde:**
"Hiermit lege ich gegen die [Maßnahme: Versetzung/Befehl/Beurteilung] vom [Datum], zugegangen am [Datum], fristwahrend Beschwerde nach § 1 WBO ein. Die Begründung erfolgt nach Akteneinsicht. Ich beantrage gleichzeitig die Aussetzung der Vollziehung nach § 3 II WBO, weil ein erheblicher Nachteil droht, der nicht mehr rückgängig zu machen ist."

**Antrag auf gerichtliche Entscheidung:**
"Hiermit beantrage ich nach § 17 WBO gerichtliche Entscheidung gegen den Beschwerdebescheid vom [Datum], zugestellt am [Datum]. Ich beantrage,
1. den Beschwerdebescheid sowie die Ausgangsmaßnahme aufzuheben,
2. die Aussetzung der Vollziehung anzuordnen,
3. ein Sachverständigengutachten einzuholen über [...]."

## Typische Fehler

- Frist verpasst, weil Zugang der Maßnahme nicht dokumentiert.
- Beschwerde an die falsche Stelle gerichtet – fristwahrend ist nur die Einlegung bei der zuständigen Stelle; jedoch: jede militärische Dienststelle ist verpflichtet, die Beschwerde weiterzuleiten.
- Aussetzung der Vollziehung nicht beantragt – Maßnahme wird vollzogen, Anliegen erledigt sich faktisch.
- Vermengung von WBO (Maßnahmen) und WDO (Disziplinar) – falscher Rechtsweg.
- Verwaltungsgericht angerufen statt Truppendienstgericht – Klage als unzulässig abzuweisen.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- truppendienstgericht-zustaendigkeit-verfahren
- bundesverwaltungsgericht-wehrdienstsenate
- eilverfahren-konkurrentenstreit-wehrdienstsenat
- weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht
- fristenkalender-bundeswehrrecht

## Quellen Stand 06/2026

- WBO – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zur Auslegung der Beschwer in § 1 WBO und zur Fristberechnung (Az. nur verifiziert zitieren).
- WBeauftrG – Volltext gesetze-im-internet.de, Berichte des Wehrbeauftragten beim Deutschen Bundestag.
- Truppendienstgerichte Süd/Nord – Verfahrensordnung und Geschäftsverteilungspläne (publik bei BVerwG/Truppendienstgerichten).
- Bundeswehrhandbücher und ZDv nur nach Mandantenvorlage zitieren.

## 2. `schadenersatz-regress-dienstunfall-material`

**Fokus:** Schadensersatz, Regress, Dienstunfall, Materialschäden: prüft SVG, BHO § 59, Regress gegen Soldaten und Haftungsrecht. Norm-/Quellenanker: SVG, SG § 24, BHO, BGB §§ 249 ff.

# Schadensersatz, Regress, Dienstunfall und Materialschäden

## Fachkern: Schadensersatz, Regress, Dienstunfall und Materialschäden
- **Spezialgegenstand:** Schadensersatz, Regress, Dienstunfall und Materialschäden. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldaten haften für im Dienst verursachte Schäden eingeschränkt: § 24 SG begründet ein Haftungsprivileg (Haftung nur bei Vorsatz und grober Fahrlässigkeit gegenüber dem Dienstherrn).

Umgekehrt hat der Soldat bei Dienstunfall Versorgungsansprüche nach SVG; der Dienstherr kann Regress gegen Dritte nehmen.

## Einschlägige Normen und Quellen

- SG § 24 — Haftungsprivileg Soldaten
- SVG §§ 27–38 — Versorgung bei Dienstunfall
- BHO § 59 — Regressverzicht
- BGB §§ 249 ff. — Schadensersatz
- § 839 BGB, Art. 34 GG — Amtshaftung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Hat der Soldat einen Schaden verursacht (Material, Ausrüstung, Dritte)?
- Handelt es sich um Vorsatz oder Fahrlässigkeit?
- Liegt ein Dienstunfall vor (Soldat ist Geschädigter)?
- Macht der Dienstherr Regress gegen den Soldaten?
- Drittschäden: Amtshaftung?

## Prüf- und Arbeitslogik

### Schritt 1 — Haftungsprivileg § 24 SG

Soldat haftet dem Dienstherrn gegenüber nur bei Vorsatz oder grober Fahrlässigkeit.
Einfache Fahrlässigkeit: kein Regress des Dienstherrn.
Dritte: Amtshaftung Art. 34 GG gilt; Bundesrepublik haftet, kein direkter Regress gegen Soldaten.
Ausnahme: vorsätzliche Schädigung.

### Schritt 2 — Materialschäden und Regress

Typische Fälle: Fahrzeugschäden, Waffenverlust, Ausrüstungsschäden.
Dienstherr-Regress: nur bei grober Fahrlässigkeit oder Vorsatz (§ 24 SG).
Prüfung: War die grobe Fahrlässigkeit nachweisbar?
Widerspruch gegen Regressbescheid: 1 Monat.

### Schritt 3 — Amtshaftung gegenüber Dritten

Dritter klagt gegen Bundesrepublik (Art. 34 GG, § 839 BGB).
Bundesrepublik kann internen Regress nur bei Vorsatz/grober Fahrlässigkeit nehmen.
Für den Soldaten: erster Schritt WBO, wenn dienstrechtliche Maßnahme.

### Schritt 4 — Dienstunfall und Versorgung

Soldat als Geschädigter: SVG §§ 27 ff. — WDB-Leistungen.
Dienstunfall: unverzügliche Meldung.
Regress des Bundes gegen Drittverursacher (z. B. Kfz-Fahrer).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Prüfschema: Haftungsprivileg § 24 SG
- Tabelle: Haftung Soldat in verschiedenen Schadensszenarien
- Checkliste: Regress-Widerspruch

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — § 24 SG
- https://www.gesetze-im-internet.de/svg/ — SVG §§ 27 ff.
- https://dejure.org/gesetze/SG/24.html
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `aerztliche-begutachtung-dienstfaehigkeit`

**Fokus:** Ärztliche Begutachtung und Dienstfähigkeit: prüft Begutachtungsverfahren, Tauglichkeitsstufen, Rechtsbehelfe und Versorgungsfolgen. Norm-/Quellenanker: §§ 44–45 SG, SVG, DV 46/1.

# Ärztliche Begutachtung und Dienstfähigkeit

## Fachkern: Ärztliche Begutachtung und Dienstfähigkeit
- **Spezialgegenstand:** Ärztliche Begutachtung und Dienstfähigkeit. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die ärztliche Begutachtung entscheidet über Tauglichkeit und Verwendungsfähigkeit (T1 = voll tauglich bis T5 = dauerhaft dienstunfähig). Neben allgemeiner Tauglichkeit bestehen spezifische Eignungsanforderungen (Flieger, Fallschirmjäger, Kampftaucher).

Dauerhafte Dienstunfähigkeit löst bei Berufssoldaten die Zurruhesetzung (§ 45 SG) und bei Soldaten auf Zeit die Entlassung (§ 55 Abs. 2 SG) aus. Die Einstufung hat unmittelbare Versorgungsrelevanz nach SVG (Ruhegehalt, Übergangsgebührnisse, WDB-Ausgleich).

## Einschlägige Normen und Quellen

- § 44 SG — Verwendungsunfähigkeit
- § 45 SG — Zurruhesetzung Berufssoldat bei Dienstunfähigkeit
- § 55 Abs. 2 SG — Entlassung Soldat auf Zeit bei Dienstunfähigkeit
- DV 46/1 — Zentralvorschrift ärztliche Begutachtung Bundeswehr
- §§ 27–38 SVG — Wehrdienstbeschädigung und Versorgungsleistungen
- § 17 SG — Personalakte (Aufnahme Begutachtungsergebnisse)
- §§ 6–11 WBO — Beschwerdeverfahren

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welches Begutachtungsergebnis liegt vor, und in welcher Tauglichkeitsstufe wurde eingestuft?
- Ist die Begutachtung durch Truppenarzt, Sanitätszentrum oder BwKrhs erfolgt?
- Wurde Dienstunfähigkeit festgestellt? Droht Entlassung oder Zurruhesetzung?
- Liegen eigene Gegengutachten oder Facharztberichte vor?
- Besteht ein Zusammenhang mit Dienstunfall oder Auslandseinsatz (WDB)?
- Läuft eine WBO-Beschwerdefrist?

## Prüf- und Arbeitslogik

### Schritt 1 — Begutachtungsgrundlage prüfen

Welches Gutachten liegt vor (Truppenarzt/SanZ/BwKrhs)?
Wurde DV 46/1 eingehalten?
Vollständige Befunderhebung dokumentiert?
Formfehler können zur Aufhebung des Gutachtens führen.

### Schritt 2 — Tauglichkeitsstufe T1–T5

T1 voll tauglich; T2/T3 beschränkt; T4 nur eingeschränkte Verwendung; T5 dauerhaft dienstunfähig.
Sondereignungen gesondert prüfen (fliegerärztlich, ABC, Taucher).
Abgrenzung: vorübergehende Erkrankung (temporäre VE) vs. dauerhafte Dienstunfähigkeit.

### Schritt 3 — Dienstrechtliche Folgen

SaZ § 55 Abs. 2 SG: Entlassung — keine Rückforderung Ausbildungskosten!
BeruSold § 45 SG: Zurruhesetzung; Ruhegehalt nach Dienstzeit.
Frist: Entlassungsverfügung anfechten (WBO § 6, 1 Monat ab Bekanntgabe).

### Schritt 4 — Versorgungsansprüche SVG

§ 27 SVG: Wehrdienstbeschädigung — Kausalität 'hinreichende Wahrscheinlichkeit'.
§ 85 SVG: Ausgleich (Einmalzahlung/Rente nach MdE).
§§ 63a ff. SVG: Einsatzversorgung bei Auslandseinsatz.
Antrag beim BAPersBw, Versorgungsreferat.

### Schritt 5 — Gegengutachten und Rechtsbehelfe

Eigenes Gutachten beauftragen, dem Dienstherrn gegenüberstellen.
WBO-Beschwerde gegen dienstrechtliche Entscheidung (nicht direkt gegen Gutachten).
Klage VG bei Entlassungsverfügung.
WDB-Ansprüche: Sozialgericht (ab SGB XIV 2024).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Tauglichkeitsstufen T1–T5 mit dienstrechtlichen Folgen
- Prüfschema: Wehrdienstbeschädigung § 27 SVG (Schaden → Kausalität → Leistung)
- Checkliste: Gegengutachten beauftragen — notwendige Unterlagen
- Muster-WBO-Beschwerde gegen Entlassungsverfügung wegen Dienstunfähigkeit

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — SG §§ 44–45, 55
- https://www.gesetze-im-internet.de/svg/ — SVG §§ 27–38, 63a ff.
- https://dejure.org/gesetze/SG
- https://www.bverwg.de — BVerwG Wehrdienstsenat
- https://www.bundeswehr.de/de/organisation/personal/bundesamt-fuer-das-personalmanagement

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

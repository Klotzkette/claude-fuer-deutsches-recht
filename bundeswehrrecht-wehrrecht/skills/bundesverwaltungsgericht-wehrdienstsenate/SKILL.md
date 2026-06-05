---
name: bundesverwaltungsgericht-wehrdienstsenate
description: "Bundesverwaltungsgericht Wehrdienstsenate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bundesverwaltungsgericht Wehrdienstsenate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bundesverwaltungsgericht Wehrdienstsenate** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bundesverwaltungsgericht-wehrdienstsenate` | Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `bwbes-neu-001-soldatenbesoldung-grundgehalt-und-dienstgrad` | Soldatenbesoldung Grundgehalt Dienstgrad: prüft BBesG-Gruppen, Stufenaufstieg, Dienstgradkorrelation und Rückwirkungsfragen. Norm-/Quellenanker: BBesG Anlagen I, IV, § 27 BBesG. |
| `bwbes-neu-002-wehrsold-freiwilliger-wehrdienst-und-unterhaltssic` | Wehrsold FWD Unterhaltssicherung: prüft WSG, UhSiG, Höhe, Verfahren und Schnittstellen SGB. Norm-/Quellenanker: WSG, UhSiG, § 58b SG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Bundesverwaltungsgericht Wehrdienstsenate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bundesverwaltungsgericht-wehrdienstsenate`

**Fokus:** Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Bundesverwaltungsgericht – Wehrdienstsenate

## Fachkern: Bundesverwaltungsgericht – Wehrdienstsenate
- **Spezialgegenstand:** Bundesverwaltungsgericht – Wehrdienstsenate. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Wehrdienstsenate des BVerwG (1. und 2. Wehrdienstsenat) entscheiden über Rechtsmittel aus WDO und WBO sowie über erstinstanzliche Anträge in eng begrenzten Fällen (insbesondere Konkurrentenstreit gegen Maßnahmen höherer Vorgesetzter, § 21 WBO). Sie sind die höchste Instanz im Wehrdienstrecht und legen die Auslegung von SG, WBO, WDO maßgebend fest. Der Skill ordnet ein, wann das BVerwG Wehrdienstsenat zuständig ist und wie das Verfahren abläuft.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Liegt eine Entscheidung des Truppendienstgerichts vor? Berufung oder Revision?
- Geht es um eine Maßnahme eines höheren Vorgesetzten (BMVg, Inspekteur, Kommandeur höherer Ebene) – § 21 WBO erste Instanz?
- Welche Frist läuft (1 Monat ab Zustellung des TDG-Urteils; bei § 21 WBO erste Instanz: 1 Monat ab Beschwerdebescheid)?
- Streitwert/Bedeutung der Sache – Revisionszulassungsgründe?
- Eilbedürfnis (vorläufige Maßnahmen § 25 WBO entsprechend)?
- Soll grundsätzliche Rechtsfrage durch BVerwG geklärt werden?

## Rechtlicher Rahmen

- § 21 WBO: Erstinstanzliche Zuständigkeit des BVerwG bei Maßnahmen höherer Vorgesetzter (Bundesminister, Inspekteure).
- § 23a WDO: Berufung gegen TDG-Urteile in disziplinargerichtlichen Sachen.
- §§ 124 ff. VwGO i.V.m. §§ 19 ff. WBO: Verfahren vor dem BVerwG bei wehrbeschwerderechtlichen Streitsachen.
- §§ 132 ff. VwGO: Revisionszulassungsgründe – grundsätzliche Bedeutung, Divergenz, Verfahrensfehler.
- § 80a VwGO: Vorläufige Maßnahmen im Eilrechtsschutz.
- § 50 SG: Verlust der Rechte als Soldat – höchstrichterliche Klärung beim BVerwG.

## / Schritt für Schritt

1. **Rechtsmittelart bestimmen.** Berufung in WDO-Sachen (§ 23a WDO); Antrag auf gerichtliche Entscheidung in § 21 WBO-Sachen; Beschwerde gegen Beschluss des TDG.
2. **Frist sichern.** 1 Monat ab Zustellung des TDG-Urteils bzw. des Beschwerdebescheids.
3. **Anwaltspflicht.** Vor dem BVerwG besteht Vertretungszwang durch Rechtsanwalt nach § 67 IV VwGO entsprechend.
4. **Schriftsatz.** Tatsachenvortrag, rechtliche Würdigung, konkrete Anträge, Beweisangebote (Zeugen, Urkunden, Sachverständige).
5. **Zulassungsgründe.** Bei Revision: grundsätzliche Bedeutung, Divergenz, Verfahrensmangel substantiieren.
6. **Eilantrag prüfen.** Bei drohender Vollziehung – einstweilige Anordnung gegen Versetzung, Konkurrentenstreit, vorläufige Dienstenthebung.
7. **Mündliche Verhandlung** oft erforderlich; schriftliches Verfahren möglich.
8. **Urteil/Beschluss** mit Bindungswirkung; ggf. Verfassungsbeschwerde zum BVerfG (Art. 93 I Nr. 4a GG).

## Trade-off-Matrix

| Ausgangslage | BVerwG erste Instanz § 21 WBO | TDG-Berufungsweg |
| --- | --- | --- |
| Maßnahme BMVg/Inspekteur | Direkt BVerwG | nicht statthaft |
| TDG-Urteil mit Maßnahme | – | Berufung § 23a WDO |
| Konkurrentenstreit höhere Ebene | § 21 WBO + Eilantrag | – |
| Grundsatzfrage | Revision § 132 VwGO | – |

## Praxistipps

- BVerwG entscheidet streng nach Akten – Tatsachenvortrag in den vorinstanzlichen Schriftsätzen muss bereits präzise sein.
- "Ständige Rechtsprechung" der Wehrdienstsenate ist hochrelevant – Auswertung der BVerwG-Datenbank Pflicht. Konkrete Az. nur nach Verifikation zitieren.
- Anwaltspflicht ab BVerwG-Verfahren – Selbstvertretung des Soldaten unzulässig.
- Bei § 21 WBO-Verfahren: keine Vorbefassung des Truppendienstgerichts – Sprung in die Bundesgerichtsbarkeit.
- Eilanträge mit konkreter Glaubhaftmachung der Eilbedürftigkeit (zB Versetzung in zwei Wochen).

## Mustertexte

**Berufungsschrift im disziplinargerichtlichen Verfahren:**
"An das Bundesverwaltungsgericht, Wehrdienstsenat. Gegen das Urteil des Truppendienstgerichts [Süd/Nord], Az. [...], vom [Datum], zugestellt am [Datum], lege ich Berufung nach § 23a WDO ein. Es wird beantragt, das Urteil aufzuheben und [...]. Begründung folgt fristgerecht binnen [Frist]."

**Antrag § 21 WBO erste Instanz:**
"Gegen die Maßnahme des [Bundesministers/Inspekteurs/...] vom [Datum], zugegangen am [Datum], beantrage ich nach § 21 WBO i.V.m. § 17 WBO gerichtliche Entscheidung. Es wird beantragt: 1. Die Maßnahme aufzuheben. 2. Den Antragsgegner zu verpflichten, [...]. 3. Aussetzung der Vollziehung."

## Typische Fehler

- Frist 1 Monat versäumt – Zustellungsdatum ungeprüft.
- Selbstvertretung ohne Anwalt – Schriftsatz wird als unzulässig zurückgewiesen.
- Revisionszulassungsgründe nicht substantiiert.
- Tatsachenvortrag erst beim BVerwG nachgeholt – Präklusion droht.
- Verwechslung von erstinstanzlicher Zuständigkeit nach § 21 WBO und Berufungsweg nach § 23a WDO.

## Querverweise

- truppendienstgericht-zustaendigkeit-verfahren
- wehrbeschwerdeordnung-beschwerde-frist-form
- eilverfahren-konkurrentenstreit-wehrdienstsenat
- weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht
- gerichtliches-disziplinarverfahren-soldat
- rechtsbeistand-im-disziplinarverfahren

## Quellen Stand 06/2026

- WBO §§ 17, 21 – Volltext gesetze-im-internet.de.
- WDO § 23a – Volltext gesetze-im-internet.de.
- VwGO §§ 67, 80a, 124 ff., 132 – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung; Entscheidungsdatenbank des BVerwG (bverwg.de).
- Geschäftsverteilung BVerwG – jährlich publiziert.
- Keine Kommentarstellen aus Modellwissen.

## 2. `bwbes-neu-001-soldatenbesoldung-grundgehalt-und-dienstgrad`

**Fokus:** Soldatenbesoldung Grundgehalt Dienstgrad: prüft BBesG-Gruppen, Stufenaufstieg, Dienstgradkorrelation und Rückwirkungsfragen. Norm-/Quellenanker: BBesG Anlagen I, IV, § 27 BBesG.

# Soldatenbesoldung: Grundgehalt und Dienstgrad

## Fachkern: Soldatenbesoldung: Grundgehalt und Dienstgrad
- **Spezialgegenstand:** Soldatenbesoldung: Grundgehalt und Dienstgrad. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Das Grundgehalt von Berufssoldaten und Soldaten auf Zeit richtet sich nach der Besoldungsgruppe (A-Besoldung), die mit dem Dienstgrad korrespondiert. Der Stufenaufstieg nach § 27 BBesG ist erfahrungsabhängig.

Beförderungen lösen sofortigen Besoldungsgruppenwechsel aus. Fehler bei Stufenzuordnung sind häufig und führen zu Nachzahlungspflichten oder ungerechtfertigten Rückforderungen.

## Einschlägige Normen und Quellen

- §§ 1–3 BBesG — Geltungsbereich und Grundsätze
- §§ 27–28 BBesG — Grundgehalt und Stufen
- Anlage I BBesG — Besoldungsordnung A (Soldaten)
- Anlage IV BBesG — Grundgehaltstabellen
- SG § 3 — Ernennung und Dienstgrad
- § 9a BBesG — Rückforderung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welcher Dienstgrad und welche Besoldungsgruppe?
- Seit wann in dieser Stufe, und war die Stufenzuordnung bei Einstellung/Beförderung korrekt?
- Liegt ein Beförderungsbescheid vor? Rückwirkung?
- Werden Aufwandsentschädigungen oder Stellenzulagen geltend gemacht?
- Streit über Dienstzeitanrechnung für Erfahrungsstufen?

## Prüf- und Arbeitslogik

### Schritt 1 — Besoldungsgruppe nach Dienstgrad

Anlage I BBesG: Mannschaften A4–A6, Unteroffiziere A7–A9, Offiziere A10–A16, Generale B.
Dienstgradkorrelation aktuell in BBesG prüfen.
Statuswechsel SaZ → BeruSold: Besoldungsanpassung ab Ernennungsdatum.

### Schritt 2 — Grundgehaltsstufen § 27 BBesG

Stufen 1–8: zeitgebundener Aufstieg (2–3 Jahre/Stufe).
Anrechnung: frühere Dienstzeiten im öffentl. Dienst, Bundeswehr, Studium § 28 BBesG.
Fehler: falsche Stufenzuordnung bei Einstellung → Nachzahlungsanspruch.

### Schritt 3 — Beförderung und Rückwirkung

Beförderung wirkt ab Ernennungsdatum.
Rechtswidrig verzögerte Beförderung: Schadensersatzanspruch möglich.
Konkurrentenklage: Besetzungsstopp TDG, damit Mitbewerber nicht befördert wird.

### Schritt 4 — Rückforderung § 9a BBesG

Überzahltes Grundgehalt: grundsätzlich rückforderbar.
Gutgläubiger Verbrauch schützt.
Billigkeitserlass § 12 Abs. 2 BBesG beantragen.
Widerspruch 1 Monat nach Bescheid.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Dienstgrad → Besoldungsgruppe aktuell
- Berechnungsbeispiel Stufenaufstieg über 10 Jahre
- Checkliste: Widerspruch gegen Besoldungsmitteilung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — BBesG
- https://dejure.org/gesetze/BBesG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `bwbes-neu-002-wehrsold-freiwilliger-wehrdienst-und-unterhaltssic`

**Fokus:** Wehrsold FWD Unterhaltssicherung: prüft WSG, UhSiG, Höhe, Verfahren und Schnittstellen SGB. Norm-/Quellenanker: WSG, UhSiG, § 58b SG.

# Wehrsold, freiwilliger Wehrdienst und Unterhaltssicherung

## Fachkern: Wehrsold, freiwilliger Wehrdienst und Unterhaltssicherung
- **Spezialgegenstand:** Wehrsold, freiwilliger Wehrdienst und Unterhaltssicherung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Der freiwillige Wehrdienst (FWD, § 58b SG, 7–23 Monate) wurde nach Aussetzung der allgemeinen Wehrpflicht eingeführt. Freiwillige erhalten Wehrsold nach WSG. Das UhSiG sichert den Verdienstausfallausgleich für Arbeitnehmer und Selbstständige.

Schnittstellen mit Sozialrecht (SGB II/III, GRV) sind komplex; FWD-Zeiten zählen als Pflichtbeitragszeiten.

## Einschlägige Normen und Quellen

- WSG — Wehrsoldgesetz
- UhSiG — Unterhaltssicherungsgesetz
- § 58b SG — Freiwilliger Wehrdienst
- SGB VI § 3 — Pflichtbeitragszeiten FWD
- § 3 Nr. 5 EStG — Steuerfreiheit Wehrsold

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- FWD, Reserveübung oder Spannungsfall-Wehrdienst?
- Arbeitnehmer oder Selbstständiger — welche UhSiG-Leistung?
- Wurde Unterhaltssicherung beantragt und in welcher Höhe?
- Streit über Berechnung oder Auszahlung?
- Rentenversicherungszeiten korrekt erfasst?

## Prüf- und Arbeitslogik

### Schritt 1 — Wehrsold WSG

Staffelung nach Dienstgrad und Dienstzeit.
FWD: 7–23 Monate § 58b SG, danach ggf. SaZ.
Sachleistungen: Verpflegung, Unterkunft, Bekleidung.
Steuerfreiheit § 3 Nr. 5 EStG.

### Schritt 2 — Unterhaltssicherung UhSiG

Anspruchsberechtigte: Arbeitnehmer, Selbstständige, Landwirte.
Höhe: Netto-Monatseinkommen abzüglich Wehrsold.
Selbstständige: Einkommensnachweise 3 Jahre.
Antrag: Karrierecenter/BAPersBw.

### Schritt 3 — Sozialrecht-Schnittstellen

SGB VI § 3: FWD als Pflichtbeitragszeiten GRV.
SGB II/III: ALG-Anwartschaft nach FWD prüfen.
Kindergeld: ggf. fortgezahlt während FWD.
Krankenversicherung: Heilfürsorge während FWD, danach PKV-Wechsel.

### Schritt 4 — Rechtsbehelfe

Widerspruch gegen UhSiG-Bescheid: 1 Monat.
Klage: VG (öffentlich-rechtliche Leistung).
WSG-Streit: WBO-Beschwerde oder VwGO?

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Wehrsold-Stufen FWD nach Dienstgrad
- Berechnungsschema UhSiG (Arbeitnehmer/Selbstständiger)
- Checkliste: Unterlagen UhSiG-Antrag

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wsg/ — WSG
- https://www.gesetze-im-internet.de/uhsig/ — UhSiG
- https://www.gesetze-im-internet.de/sg/ — § 58b SG
- https://www.bundeswehr.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

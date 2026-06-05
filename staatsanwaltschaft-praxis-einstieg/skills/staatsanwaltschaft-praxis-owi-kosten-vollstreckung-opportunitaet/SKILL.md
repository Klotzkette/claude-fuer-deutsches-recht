---
name: staatsanwaltschaft-praxis-owi-kosten-vollstreckung-opportunitaet
description: "OWI Kosten Vollstreckung Opportunitaet: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# OWI Kosten Vollstreckung Opportunitaet

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **OWI Kosten Vollstreckung Opportunitaet** im Plugin Staatsanwaltschaft Praxis Einstieg. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `owi-kosten-vollstreckung-und-ruecknahme` | Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-opportunitaet-einstellung-47` | Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-rechtsbeschwerde-79-80` | Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-verbandsgeldbusse-30-130` | Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-verjaehrung-verfolgungsverjaehrung` | Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |

## Arbeitsweg

Im Plugin Staatsanwaltschaft Praxis Einstieg gilt für **OWI Kosten Vollstreckung Opportunitaet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `owi-kosten-vollstreckung-und-ruecknahme`

**Fokus:** Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen

## Fachkern: Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen
- **Spezialgegenstand:** Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 89 ff., 105 ff. OWiG; § 67 OWiG; Kostenrecht live prüfen.

## Fachlicher Fokus

Der Skill erzeugt eine Abschlussverfügung: Rechtskraft, Einspruchsrücknahme, Verwerfung, Kostenfolge, Vollstreckbarkeit, Nebenfolge, Mitteilung an Verwaltungsbehörde und Wiedervorlage. Er verhindert, dass eine scheinbar kleine Bußgeldsache als Aktenrest liegen bleibt.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 2. `owi-opportunitaet-einstellung-47`

**Fokus:** Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren

## Fachkern: Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren
- **Spezialgegenstand:** Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Opportunität im OWi-Verfahren: § 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§ 47 OWiG; § 46 OWiG; RiStBV-Bußgeldteil; Spezialgesetze live prüfen.

## Fachlicher Fokus

Dieser Skill erklärt den wichtigsten Mentalitätswechsel: Ordnungswidrigkeiten werden im pflichtgemäßen Ermessen verfolgt. Er erzeugt eine Einstellungsvorlage mit Verhältnismäßigkeit, Präventionsinteresse, Vorbelastung, Schadensnähe, Verwaltungsaufwand und Zustimmungserfordernissen im gerichtlichen Verfahren.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 3. `owi-rechtsbeschwerde-79-80`

**Fokus:** Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung

## Fachkern: Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung
- **Spezialgegenstand:** Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 79, 80 OWiG; StPO-Rechtsbeschwerdevorschriften sinngemäß; OLG-Zuständigkeit live prüfen.

## Fachlicher Fokus

Der Skill prüft nach Urteil oder § 72-Beschluss, ob die Staatsanwaltschaft Rechtsbeschwerde einlegen oder Zulassung beantragen sollte: Schwellenwerte, Nebenfolge, Fahrverbot, Freispruch/Einstellung, rechtliches Gehör, Fortbildung des Rechts und Sicherung einheitlicher Rechtsprechung.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 4. `owi-verbandsgeldbusse-30-130`

**Fokus:** Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis

## Fachkern: Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis
- **Spezialgegenstand:** Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: §§ 30 und 130 OWiG in der Praxis** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 30, 130 OWiG; Spezialpflichten aus Datenschutz-, Umwelt-, Arbeits-, Produkt- oder Finanzaufsichtsrecht.

## Fachlicher Fokus

Der Skill prüft, ob eine Leitungspersonenhandlung, eine betriebliche Pflichtverletzung oder ein Aufsichtsmangel tragfähig ist. Er erzeugt ein Organigramm, Pflichtenkatalog, Kontrolllücken-Matrix und eine faire Ahndungsempfehlung für Unternehmensbußen.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. `owi-verjaehrung-verfolgungsverjaehrung`

**Fokus:** Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender

## Fachkern: Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender
- **Spezialgegenstand:** Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 31 bis 34 OWiG; Spezialverjährung etwa § 26 StVG; Unterbrechungstatbestände live prüfen.

## Fachlicher Fokus

Der Skill baut einen Fristenkalender für Bußgeldsachen: Tatzeit, Bekanntgabe, Anhörung, Bußgeldbescheid, Zustellung, Einspruch, Unterbrechung und absolute Grenzen. Er warnt davor, strafprozessuale Fristenlogik ungeprüft auf OWi-Sachen zu übertragen.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

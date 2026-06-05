---
name: durchsuchung-beschlagnahme-kanzlei-arzt
description: "Durchsuchung Beschlagnahme Kanzlei Arzt: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Durchsuchung Beschlagnahme Kanzlei Arzt

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Durchsuchung Beschlagnahme Kanzlei Arzt** im Plugin Staatsanwaltschaft Praxis Einstieg. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `durchsuchung-beschlagnahme-antrag` | Durchsuchung und Beschlagnahme: Praxis-Skill für neue Staatsanwälte zu richterlichen Beschluss, Gefahr im Verzug, Verhältnismäßigkeit und Dokumentation sauber vorbereiten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `durchsuchung-kanzlei-arzt-redaktion` | Durchsuchung bei Berufsgeheimnisträgern: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `einstellung-153-153a-auflagen` | Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `einstellung-153-153a-stpo` | Einstellung nach §§ 153 und 153a StPO: Praxis-Skill für neue Staatsanwälte zu Opportunität, Auflagen, Zustimmungserfordernisse, Opferinteressen und Dokumentation handhaben; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `einziehung-drittbetroffene-anhoerung` | Einziehung mit Drittbetroffenen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |

## Arbeitsweg

Im Plugin Staatsanwaltschaft Praxis Einstieg gilt für **Durchsuchung Beschlagnahme Kanzlei Arzt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `durchsuchung-beschlagnahme-antrag`

**Fokus:** Durchsuchung und Beschlagnahme: Praxis-Skill für neue Staatsanwälte zu richterlichen Beschluss, Gefahr im Verzug, Verhältnismäßigkeit und Dokumentation sauber vorbereiten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Durchsuchung und Beschlagnahme

## Fachkern: Durchsuchung und Beschlagnahme
- **Spezialgegenstand:** Durchsuchung und Beschlagnahme wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Durchsuchung und Beschlagnahme** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** richterlichen Beschluss, Gefahr im Verzug, Verhältnismäßigkeit und Dokumentation sauber vorbereiten

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, einschlägiges Nebenstrafrecht und landesrechtliche Verwaltungsvorschriften live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag: Verfügung, Ermittlungsauftrag, Vermerk, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 2. `durchsuchung-kanzlei-arzt-redaktion`

**Fokus:** Durchsuchung bei Berufsgeheimnisträgern: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Durchsuchung bei Berufsgeheimnisträgern

## Fachkern: Durchsuchung bei Berufsgeheimnisträgern
- **Spezialgegenstand:** Durchsuchung bei Berufsgeheimnisträgern wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Durchsuchung bei Berufsgeheimnisträgern** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** §§ 97, 102, 103 StPO, Beschlagnahmeverbote, Trennung und Richtervorbehalt

## Einstieg

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, Nebenstrafrecht und einschlägige Landesvorgaben live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag Vermerk, Ermittlungsauftrag, Verfügung, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 3. `einstellung-153-153a-auflagen`

**Fokus:** Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen

## Fachkern: Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen
- **Spezialgegenstand:** Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Einstellung nach §§ 153/153a StPO: Auflagen sauber begründen** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Geringfügigkeit, öffentliches Interesse, Zustimmung, Auflagenhöhe und Opferinteressen

## Einstieg

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, Nebenstrafrecht und einschlägige Landesvorgaben live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag Vermerk, Ermittlungsauftrag, Verfügung, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 4. `einstellung-153-153a-stpo`

**Fokus:** Einstellung nach §§ 153 und 153a StPO: Praxis-Skill für neue Staatsanwälte zu Opportunität, Auflagen, Zustimmungserfordernisse, Opferinteressen und Dokumentation handhaben; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Einstellung nach §§ 153 und 153a StPO

## Fachkern: Einstellung nach §§ 153 und 153a StPO
- **Spezialgegenstand:** Einstellung nach §§ 153 und 153a StPO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Einstellung nach §§ 153 und 153a StPO** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Opportunität, Auflagen, Zustimmungserfordernisse, Opferinteressen und Dokumentation handhaben

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, einschlägiges Nebenstrafrecht und landesrechtliche Verwaltungsvorschriften live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag: Verfügung, Ermittlungsauftrag, Vermerk, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 5. `einziehung-drittbetroffene-anhoerung`

**Fokus:** Einziehung mit Drittbetroffenen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Einziehung mit Drittbetroffenen

## Fachkern: Einziehung mit Drittbetroffenen
- **Spezialgegenstand:** Einziehung mit Drittbetroffenen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Einziehung mit Drittbetroffenen** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Anhörung, Eigentum, Rechte Dritter, Arrest und gerichtlicher Antrag

## Einstieg

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, Nebenstrafrecht und einschlägige Landesvorgaben live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag Vermerk, Ermittlungsauftrag, Verfügung, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

---
name: quellen-rechtsprechungscheck-anfangsverdacht
description: "Quellen Rechtsprechungscheck Anfangsverdacht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Quellen Rechtsprechungscheck Anfangsverdacht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Quellen Rechtsprechungscheck Anfangsverdacht** im Plugin Staatsanwaltschaft Praxis Einstieg. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `quellen-und-rechtsprechungscheck` | Quellen- und Rechtsprechungscheck: Praxis-Skill für neue Staatsanwälte zu verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `anfangsverdacht-und-verfahrenseinleitung` | Anfangsverdacht und Verfahrenseinleitung: Praxis-Skill für neue Staatsanwälte zu Anfangsverdacht, Anzeige, Strafantrag, Offizialdelikt und erste Verfügung trennen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `beschleunigtes-verfahren-418-stpo` | Beschleunigtes Verfahren nach § 418 StPO: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `frist-und-zustaendigkeit-cockpit` | Fristen- und Zuständigkeitscockpit: Praxis-Skill für neue Staatsanwälte zu macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `fristenkalender-staatsanwaltschaft` | Fristenkalender im Dezernat: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |

## Arbeitsweg

Im Plugin Staatsanwaltschaft Praxis Einstieg gilt für **Quellen Rechtsprechungscheck Anfangsverdacht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `quellen-und-rechtsprechungscheck`

**Fokus:** Quellen- und Rechtsprechungscheck: Praxis-Skill für neue Staatsanwälte zu verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Quellen- und Rechtsprechungscheck

## Fachkern: Quellen- und Rechtsprechungscheck
- **Spezialgegenstand:** Quellen- und Rechtsprechungscheck wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Quellen- und Rechtsprechungscheck** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen

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

## 2. `anfangsverdacht-und-verfahrenseinleitung`

**Fokus:** Anfangsverdacht und Verfahrenseinleitung: Praxis-Skill für neue Staatsanwälte zu Anfangsverdacht, Anzeige, Strafantrag, Offizialdelikt und erste Verfügung trennen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Anfangsverdacht und Verfahrenseinleitung

## Fachkern: Anfangsverdacht und Verfahrenseinleitung
- **Spezialgegenstand:** Anfangsverdacht und Verfahrenseinleitung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Anfangsverdacht und Verfahrenseinleitung** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Anfangsverdacht, Anzeige, Strafantrag, Offizialdelikt und erste Verfügung trennen

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

## 3. `beschleunigtes-verfahren-418-stpo`

**Fokus:** Beschleunigtes Verfahren nach § 418 StPO: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Beschleunigtes Verfahren nach § 418 StPO

## Fachkern: Beschleunigtes Verfahren nach § 418 StPO
- **Spezialgegenstand:** Beschleunigtes Verfahren nach § 418 StPO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Beschleunigtes Verfahren nach § 418 StPO** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** einfacher Sachverhalt, Beweislage, Terminlogik, Verteidigung und Fairness

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

## 4. `frist-und-zustaendigkeit-cockpit`

**Fokus:** Fristen- und Zuständigkeitscockpit: Praxis-Skill für neue Staatsanwälte zu macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Fristen- und Zuständigkeitscockpit

## Fachkern: Fristen- und Zuständigkeitscockpit
- **Spezialgegenstand:** Fristen- und Zuständigkeitscockpit wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Fristen- und Zuständigkeitscockpit** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar

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

## 5. `fristenkalender-staatsanwaltschaft`

**Fokus:** Fristenkalender im Dezernat: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Fristenkalender im Dezernat

## Fachkern: Fristenkalender im Dezernat
- **Spezialgegenstand:** Fristenkalender im Dezernat wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Fristenkalender im Dezernat** im Bereich **Staatsanwaltschaft Praxis-Einstieg**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Haftfristen, Verjährung, Rechtsmittelfristen, Wiedervorlagen und Kontrollvermerke

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

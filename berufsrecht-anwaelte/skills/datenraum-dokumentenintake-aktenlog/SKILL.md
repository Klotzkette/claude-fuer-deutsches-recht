---
name: datenraum-dokumentenintake-aktenlog
description: "Datenraum Dokumentenintake Aktenlog: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Datenraum Dokumentenintake Aktenlog

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Datenraum Dokumentenintake Aktenlog** im Plugin Berufsrecht der Rechtsanwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `datenraum` | Datenraum: vertiefter Berufsrechts-Skill für Anwälte; prüft Datenraum im Berufsrecht für Anwälte, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung. |
| `dokumentenintake-und-aktenlog` | Dokumentenintake und Aktenlog: vertiefter Berufsrechts-Skill für Anwälte; prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung. |
| `entscheidungsvorlage` | Entscheidungsvorlage: vertiefter Berufsrechts-Skill für Anwälte; prüft macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung. |
| `fachbezeichnung` | Fachbezeichnung: vertiefter Berufsrechts-Skill für Anwälte; prüft Fachbezeichnung im Berufsrecht für Anwälte, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung. |

## Arbeitsweg

Im Plugin Berufsrecht der Rechtsanwälte gilt für **Datenraum Dokumentenintake Aktenlog**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `datenraum`

**Fokus:** Datenraum: vertiefter Berufsrechts-Skill für Anwälte; prüft Datenraum im Berufsrecht für Anwälte, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung.

# Datenraum

## Fachkern: Datenraum
- **Spezialgegenstand:** Datenraum; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Datenraum** im Bereich **Berufsrecht Anwälte**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Datenraum im Berufsrecht für Anwälte

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, StPO/ZPO Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge je nach Auftrag: Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 2. `dokumentenintake-und-aktenlog`

**Fokus:** Dokumentenintake und Aktenlog: vertiefter Berufsrechts-Skill für Anwälte; prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung.

# Dokumentenintake und Aktenlog

## Fachkern: Dokumentenintake und Aktenlog
- **Spezialgegenstand:** Dokumentenintake und Aktenlog; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Dokumentenintake und Aktenlog** im Bereich **Berufsrecht Anwälte**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, StPO/ZPO Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge je nach Auftrag: Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 3. `entscheidungsvorlage`

**Fokus:** Entscheidungsvorlage: vertiefter Berufsrechts-Skill für Anwälte; prüft macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung.

# Entscheidungsvorlage

## Fachkern: Entscheidungsvorlage
- **Spezialgegenstand:** Entscheidungsvorlage; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Entscheidungsvorlage** im Bereich **Berufsrecht Anwälte**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, StPO/ZPO Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge je nach Auftrag: Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 4. `fachbezeichnung`

**Fokus:** Fachbezeichnung: vertiefter Berufsrechts-Skill für Anwälte; prüft Fachbezeichnung im Berufsrecht für Anwälte, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung.

# Fachbezeichnung

## Fachkern: Fachbezeichnung
- **Spezialgegenstand:** Fachbezeichnung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Fachbezeichnung** im Bereich **Berufsrecht Anwälte**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Fachbezeichnung im Berufsrecht für Anwälte

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, StPO/ZPO Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge je nach Auftrag: Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

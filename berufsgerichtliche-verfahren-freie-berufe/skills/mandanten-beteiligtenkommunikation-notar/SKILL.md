---
name: mandanten-beteiligtenkommunikation-notar
description: "Mandanten Beteiligtenkommunikation Notar: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandanten Beteiligtenkommunikation Notar

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Mandanten Beteiligtenkommunikation Notar** im Plugin Berufsgerichtliche Verfahren Freie Berufe. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandanten-oder-beteiligtenkommunikation` | Beteiligtenkommunikation: prüft übersetzt das Ergebnis in klare, taktisch sichere Kommunikation in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `notar-disziplinar-bnoto` | Notar Disziplinarverfahren BNotO: prüft Dienstaufsicht, Disziplinarverfahren, Amtsenthebung, Verwahrung und Urkundspflichten in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `patentanwalt-berufsgericht-pao` | Patentanwalt Berufsgericht PAO: prüft PAO-Pflichten, Patentanwaltskammer, berufsgerichtliches Verfahren und Schutzrechtsmandate in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `protokoll-und-nachbereitung` | Protokoll und Nachbereitung: prüft sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |

## Arbeitsweg

Im Plugin Berufsgerichtliche Verfahren Freie Berufe gilt für **Mandanten Beteiligtenkommunikation Notar**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandanten-oder-beteiligtenkommunikation`

**Fokus:** Beteiligtenkommunikation: prüft übersetzt das Ergebnis in klare, taktisch sichere Kommunikation in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur.

# Beteiligtenkommunikation

## Fachkern: Beteiligtenkommunikation
- **Spezialgegenstand:** Beteiligtenkommunikation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Beteiligtenkommunikation** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** übersetzt das Ergebnis in klare, taktisch sichere Kommunikation

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, PAO, StBerG, WPO, BNotO, BORA/BOStB/BS WP/vBP und einschlägige Verfahrensnormen live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Berufsrecht ist häufig existenzgefährdend; Sofortvollzug und Zulassungsfolgen zuerst prüfen.
- Keine Kammer- oder Mandatsgeheimnisse in ungeprüfte Systeme eingeben.
- Rechtsprechung nur frei/amtlich verifiziert ausgeben.

## Output

Erzeuge je nach Auftrag: Verteidigungsvermerk, Kammerantwort, Antrag, Klagebaustein, Fristenblatt oder Vergleichsvorschlag. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 2. `notar-disziplinar-bnoto`

**Fokus:** Notar Disziplinarverfahren BNotO: prüft Dienstaufsicht, Disziplinarverfahren, Amtsenthebung, Verwahrung und Urkundspflichten in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur.

# Notar Disziplinarverfahren BNotO

## Fachkern: Notar Disziplinarverfahren BNotO
- **Spezialgegenstand:** Notar Disziplinarverfahren BNotO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Notar Disziplinarverfahren BNotO** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Dienstaufsicht, Disziplinarverfahren, Amtsenthebung, Verwahrung und Urkundspflichten

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, PAO, StBerG, WPO, BNotO, BORA/BOStB/BS WP/vBP und einschlägige Verfahrensnormen live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Berufsrecht ist häufig existenzgefährdend; Sofortvollzug und Zulassungsfolgen zuerst prüfen.
- Keine Kammer- oder Mandatsgeheimnisse in ungeprüfte Systeme eingeben.
- Rechtsprechung nur frei/amtlich verifiziert ausgeben.

## Output

Erzeuge je nach Auftrag: Verteidigungsvermerk, Kammerantwort, Antrag, Klagebaustein, Fristenblatt oder Vergleichsvorschlag. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 3. `patentanwalt-berufsgericht-pao`

**Fokus:** Patentanwalt Berufsgericht PAO: prüft PAO-Pflichten, Patentanwaltskammer, berufsgerichtliches Verfahren und Schutzrechtsmandate in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur.

# Patentanwalt Berufsgericht PAO

## Fachkern: Patentanwalt Berufsgericht PAO
- **Spezialgegenstand:** Patentanwalt Berufsgericht PAO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Patentanwalt Berufsgericht PAO** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** PAO-Pflichten, Patentanwaltskammer, berufsgerichtliches Verfahren und Schutzrechtsmandate

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, PAO, StBerG, WPO, BNotO, BORA/BOStB/BS WP/vBP und einschlägige Verfahrensnormen live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Berufsrecht ist häufig existenzgefährdend; Sofortvollzug und Zulassungsfolgen zuerst prüfen.
- Keine Kammer- oder Mandatsgeheimnisse in ungeprüfte Systeme eingeben.
- Rechtsprechung nur frei/amtlich verifiziert ausgeben.

## Output

Erzeuge je nach Auftrag: Verteidigungsvermerk, Kammerantwort, Antrag, Klagebaustein, Fristenblatt oder Vergleichsvorschlag. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 4. `protokoll-und-nachbereitung`

**Fokus:** Protokoll und Nachbereitung: prüft sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur.

# Protokoll und Nachbereitung

## Fachkern: Protokoll und Nachbereitung
- **Spezialgegenstand:** Protokoll und Nachbereitung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Protokoll und Nachbereitung** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** BRAO, PAO, StBerG, WPO, BNotO, BORA/BOStB/BS WP/vBP und einschlägige Verfahrensnormen live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Berufsrecht ist häufig existenzgefährdend; Sofortvollzug und Zulassungsfolgen zuerst prüfen.
- Keine Kammer- oder Mandatsgeheimnisse in ungeprüfte Systeme eingeben.
- Rechtsprechung nur frei/amtlich verifiziert ausgeben.

## Output

Erzeuge je nach Auftrag: Verteidigungsvermerk, Kammerantwort, Antrag, Klagebaustein, Fristenblatt oder Vergleichsvorschlag. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

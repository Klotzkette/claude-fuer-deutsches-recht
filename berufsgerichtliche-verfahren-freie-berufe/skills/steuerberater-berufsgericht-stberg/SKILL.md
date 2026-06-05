---
name: steuerberater-berufsgericht-stberg
description: "Steuerberater Berufsgericht Stberg: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuerberater Berufsgericht Stberg

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Steuerberater Berufsgericht Stberg** im Plugin Berufsgerichtliche Verfahren Freie Berufe. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `steuerberater-berufsgericht-stberg` | Steuerberater Berufsgericht StBerG: prüft Warnung, Verweis, Geldbuße, Berufsverbot und Ausschließung nach StBerG in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `steuerberater-unterlagenherausgabe-praevention` | Steuerberater Unterlagenherausgabe (Präventions- und Organisationspaket): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `steuerberater-unterlagenherausgabe-verteidigung` | Steuerberater Unterlagenherausgabe (Verteidigungs- und Kammerantwort): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `steuerberater-vorbehaltsaufgabe-praevention` | Steuerberater Vorbehaltsaufgabe (Präventions- und Organisationspaket): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Berufsgerichtliche Verfahren Freie Berufe gilt für **Steuerberater Berufsgericht Stberg**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `steuerberater-berufsgericht-stberg`

**Fokus:** Steuerberater Berufsgericht StBerG: prüft Warnung, Verweis, Geldbuße, Berufsverbot und Ausschließung nach StBerG in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur.

# Steuerberater Berufsgericht StBerG

## Fachkern: Steuerberater Berufsgericht StBerG
- **Spezialgegenstand:** Steuerberater Berufsgericht StBerG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Steuerberater Berufsgericht StBerG** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Warnung, Verweis, Geldbuße, Berufsverbot und Ausschließung nach StBerG

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

## 2. `steuerberater-unterlagenherausgabe-praevention`

**Fokus:** Steuerberater Unterlagenherausgabe (Präventions- und Organisationspaket): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Steuerberater Unterlagenherausgabe: Präventions- und Organisationspaket

## Fachkern: Steuerberater Unterlagenherausgabe: Präventions- und Organisationspaket
- **Spezialgegenstand:** Steuerberater Unterlagenherausgabe: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Steuerberater Unterlagenherausgabe: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** StBerG, BOStB, BGB, Datenschutz, Auftragsverarbeitung und Kammerhinweise live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Organisationsanweisung, Checkliste, Schulung, Vorlagen, Eskalationslogik und Nachweisordner; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 3. `steuerberater-unterlagenherausgabe-verteidigung`

**Fokus:** Steuerberater Unterlagenherausgabe (Verteidigungs- und Kammerantwort): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Steuerberater Unterlagenherausgabe: Verteidigungs- und Kammerantwort

## Fachkern: Steuerberater Unterlagenherausgabe: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Steuerberater Unterlagenherausgabe: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Steuerberater Unterlagenherausgabe: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** StBerG, BOStB, BGB, Datenschutz, Auftragsverarbeitung und Kammerhinweise live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Stellungnahme, Akteneinsicht, Bestreiten, Einordnung, Entlastung, Wiedergutmachung und Sanktionsabwehr; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 4. `steuerberater-vorbehaltsaufgabe-praevention`

**Fokus:** Steuerberater Vorbehaltsaufgabe (Präventions- und Organisationspaket): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Steuerberater Vorbehaltsaufgabe: Präventions- und Organisationspaket

## Fachkern: Steuerberater Vorbehaltsaufgabe: Präventions- und Organisationspaket
- **Spezialgegenstand:** Steuerberater Vorbehaltsaufgabe: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Steuerberater Vorbehaltsaufgabe: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** StBerG, RDG, BOStB, Berufsrecht und Kammerpraxis live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Organisationsanweisung, Checkliste, Schulung, Vorlagen, Eskalationslogik und Nachweisordner; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

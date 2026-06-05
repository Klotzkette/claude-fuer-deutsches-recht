---
name: steuerberater-vorbehaltsaufgabe-kammer
description: "Steuerberater Vorbehaltsaufgabe Kammer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuerberater Vorbehaltsaufgabe Kammer

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Steuerberater Vorbehaltsaufgabe Kammer** im Plugin Berufsgerichtliche Verfahren Freie Berufe. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `steuerberater-vorbehaltsaufgabe-verteidigung` | Steuerberater Vorbehaltsaufgabe (Verteidigungs- und Kammerantwort): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `vergleich-mit-kammer-praevention` | Vergleich mit Kammer oder Aufsicht (Präventions- und Organisationspaket): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `vergleich-mit-kammer-verteidigung` | Vergleich mit Kammer oder Aufsicht (Verteidigungs- und Kammerantwort): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `vermoegensverfall-zulassungswiderruf-praevention` | Vermögensverfall und Zulassungswiderruf (Präventions- und Organisationspaket): steuert Widerruf der Zulassung wegen Vermögensverfall, Gläubigerschutz, Sofortvollzug und Sanierungsnachweis mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Berufsgerichtliche Verfahren Freie Berufe gilt für **Steuerberater Vorbehaltsaufgabe Kammer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `steuerberater-vorbehaltsaufgabe-verteidigung`

**Fokus:** Steuerberater Vorbehaltsaufgabe (Verteidigungs- und Kammerantwort): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Steuerberater Vorbehaltsaufgabe: Verteidigungs- und Kammerantwort

## Fachkern: Steuerberater Vorbehaltsaufgabe: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Steuerberater Vorbehaltsaufgabe: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Steuerberater Vorbehaltsaufgabe: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung - Verteidigungs- und Kammerantwort

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

Erzeuge Stellungnahme, Akteneinsicht, Bestreiten, Einordnung, Entlastung, Wiedergutmachung und Sanktionsabwehr; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 2. `vergleich-mit-kammer-praevention`

**Fokus:** Vergleich mit Kammer oder Aufsicht (Präventions- und Organisationspaket): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Vergleich mit Kammer oder Aufsicht: Präventions- und Organisationspaket

## Fachkern: Vergleich mit Kammer oder Aufsicht: Präventions- und Organisationspaket
- **Spezialgegenstand:** Vergleich mit Kammer oder Aufsicht: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Vergleich mit Kammer oder Aufsicht: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsrecht, Verwaltungsverfahrensgrundsätze, Sanktionensystem und Verhältnismäßigkeit live prüfen
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

## 3. `vergleich-mit-kammer-verteidigung`

**Fokus:** Vergleich mit Kammer oder Aufsicht (Verteidigungs- und Kammerantwort): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Vergleich mit Kammer oder Aufsicht: Verteidigungs- und Kammerantwort

## Fachkern: Vergleich mit Kammer oder Aufsicht: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Vergleich mit Kammer oder Aufsicht: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Vergleich mit Kammer oder Aufsicht: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsrecht, Verwaltungsverfahrensgrundsätze, Sanktionensystem und Verhältnismäßigkeit live prüfen
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

## 4. `vermoegensverfall-zulassungswiderruf-praevention`

**Fokus:** Vermögensverfall und Zulassungswiderruf (Präventions- und Organisationspaket): steuert Widerruf der Zulassung wegen Vermögensverfall, Gläubigerschutz, Sofortvollzug und Sanierungsnachweis mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Vermögensverfall und Zulassungswiderruf: Präventions- und Organisationspaket

## Fachkern: Vermögensverfall und Zulassungswiderruf: Präventions- und Organisationspaket
- **Spezialgegenstand:** Vermögensverfall und Zulassungswiderruf: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Vermögensverfall und Zulassungswiderruf: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Widerruf der Zulassung wegen Vermögensverfall, Gläubigerschutz, Sofortvollzug und Sanierungsnachweis - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO Zulassungswiderruf, Verwaltungsprozess, Insolvenz-/Schuldnerverzeichnis und anwaltliche Berufsfreiheit live prüfen
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

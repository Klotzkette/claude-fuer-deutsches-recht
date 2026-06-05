---
name: kammeranhoerung-fristverlaengerung
description: "Kammeranhoerung Fristverlaengerung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kammeranhoerung Fristverlaengerung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kammeranhoerung Fristverlaengerung** im Plugin Berufsgerichtliche Verfahren Freie Berufe. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kammeranhoerung-fristverlaengerung-praevention` | Kammeranhörung Fristverlängerung (Präventions- und Organisationspaket): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `kammeranhoerung-fristverlaengerung-verteidigung` | Kammeranhörung Fristverlängerung (Verteidigungs- und Kammerantwort): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `patentanwalt-fristenversaeumnis-epo-dpma-praevention` | Patentanwalt Fristenversäumnis DPMA/EPO (Präventions- und Organisationspaket): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `patentanwalt-fristenversaeumnis-epo-dpma-verteidigung` | Patentanwalt Fristenversäumnis DPMA/EPO (Verteidigungs- und Kammerantwort): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Berufsgerichtliche Verfahren Freie Berufe gilt für **Kammeranhoerung Fristverlaengerung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kammeranhoerung-fristverlaengerung-praevention`

**Fokus:** Kammeranhörung Fristverlängerung (Präventions- und Organisationspaket): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Kammeranhörung Fristverlängerung: Präventions- und Organisationspaket

## Fachkern: Kammeranhörung Fristverlängerung: Präventions- und Organisationspaket
- **Spezialgegenstand:** Kammeranhörung Fristverlängerung: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Kammeranhörung Fristverlängerung: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsrecht des jeweiligen Berufs, Verwaltungsverfahrensgrundsätze und Kammerpraxis live prüfen
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

## 2. `kammeranhoerung-fristverlaengerung-verteidigung`

**Fokus:** Kammeranhörung Fristverlängerung (Verteidigungs- und Kammerantwort): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Kammeranhörung Fristverlängerung: Verteidigungs- und Kammerantwort

## Fachkern: Kammeranhörung Fristverlängerung: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Kammeranhörung Fristverlängerung: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Kammeranhörung Fristverlängerung: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsrecht des jeweiligen Berufs, Verwaltungsverfahrensgrundsätze und Kammerpraxis live prüfen
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

## 3. `patentanwalt-fristenversaeumnis-epo-dpma-praevention`

**Fokus:** Patentanwalt Fristenversäumnis DPMA/EPO (Präventions- und Organisationspaket): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Patentanwalt Fristenversäumnis DPMA/EPO: Präventions- und Organisationspaket

## Fachkern: Patentanwalt Fristenversäumnis DPMA/EPO: Präventions- und Organisationspaket
- **Spezialgegenstand:** Patentanwalt Fristenversäumnis DPMA/EPO: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Patentanwalt Fristenversäumnis DPMA/EPO: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** PAO, DPMA-/EPO-Verfahrensrecht, Haftung und Kammerpflichten live prüfen
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

## 4. `patentanwalt-fristenversaeumnis-epo-dpma-verteidigung`

**Fokus:** Patentanwalt Fristenversäumnis DPMA/EPO (Verteidigungs- und Kammerantwort): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Patentanwalt Fristenversäumnis DPMA/EPO: Verteidigungs- und Kammerantwort

## Fachkern: Patentanwalt Fristenversäumnis DPMA/EPO: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Patentanwalt Fristenversäumnis DPMA/EPO: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Patentanwalt Fristenversäumnis DPMA/EPO: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** PAO, DPMA-/EPO-Verfahrensrecht, Haftung und Kammerpflichten live prüfen
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

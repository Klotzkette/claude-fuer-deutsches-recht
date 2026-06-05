---
name: bea-nicht-berufsgericht
description: "Bea Nicht In Betrieb Praevention, Bea Nicht In Betrieb Verteidigung, Berufsgericht Anschuldigungsschrift Praevention, Berufsgericht Anschuldigungsschrift Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Bea Nicht In Betrieb Praevention, Bea Nicht In Betrieb Verteidigung, Berufsgericht Anschuldigungsschrift Praevention, Berufsgericht Anschuldigungsschrift Verteidigung

## Arbeitsbereich

Dieser Skill bündelt **Bea Nicht In Betrieb Praevention, Bea Nicht In Betrieb Verteidigung, Berufsgericht Anschuldigungsschrift Praevention, Berufsgericht Anschuldigungsschrift Verteidigung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `bea-nicht-in-betrieb-praevention` | beA nicht in Betrieb (Präventions- und Organisationspaket): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `bea-nicht-in-betrieb-verteidigung` | beA nicht in Betrieb (Verteidigungs- und Kammerantwort): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `berufsgericht-anschuldigungsschrift-praevention` | Berufsgericht Anschuldigungsschrift (Präventions- und Organisationspaket): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `berufsgericht-anschuldigungsschrift-verteidigung` | Berufsgericht Anschuldigungsschrift (Verteidigungs- und Kammerantwort): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |

## Arbeitsweg

Für **Bea Nicht In Betrieb Praevention, Bea Nicht In Betrieb Verteidigung, Berufsgericht Anschuldigungsschrift Praevention, Berufsgericht Anschuldigungsschrift Verteidigung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `berufsgerichtliche-verfahren-freie-berufe` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `bea-nicht-in-betrieb-praevention`

**Fokus:** beA nicht in Betrieb (Präventions- und Organisationspaket): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# beA nicht in Betrieb: Präventions- und Organisationspaket

## Fachkern: beA nicht in Betrieb: Präventions- und Organisationspaket
- **Spezialgegenstand:** beA nicht in Betrieb: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Berufsgerichtliche Verfahren Freie Berufe**, wenn genau diese Lage auftaucht oder der Kaltstart dorthin routet. Antworte nicht mit einer allgemeinen Rechtskunde, sondern baue aus den Unterlagen eine handhabbare Fallsteuerung: Was ist sicher, was ist offen, was muss heute getan werden und welche Information darf noch nicht vorschnell preisgegeben werden?

**Fokus:** unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO, ERVV, beA-Regeln, Wiedereinsetzung und Kammerpraxis live prüfen
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

## 2. `bea-nicht-in-betrieb-verteidigung`

**Fokus:** beA nicht in Betrieb (Verteidigungs- und Kammerantwort): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# beA nicht in Betrieb: Verteidigungs- und Kammerantwort

## Fachkern: beA nicht in Betrieb: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** beA nicht in Betrieb: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Berufsgerichtliche Verfahren Freie Berufe**, wenn genau diese Lage auftaucht oder der Kaltstart dorthin routet. Antworte nicht mit einer allgemeinen Rechtskunde, sondern baue aus den Unterlagen eine handhabbare Fallsteuerung: Was ist sicher, was ist offen, was muss heute getan werden und welche Information darf noch nicht vorschnell preisgegeben werden?

**Fokus:** unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO, ERVV, beA-Regeln, Wiedereinsetzung und Kammerpraxis live prüfen
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

## 3. `berufsgericht-anschuldigungsschrift-praevention`

**Fokus:** Berufsgericht Anschuldigungsschrift (Präventions- und Organisationspaket): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufsgericht Anschuldigungsschrift: Präventions- und Organisationspaket

## Fachkern: Berufsgericht Anschuldigungsschrift: Präventions- und Organisationspaket
- **Spezialgegenstand:** Berufsgericht Anschuldigungsschrift: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Berufsgerichtliche Verfahren Freie Berufe**, wenn genau diese Lage auftaucht oder der Kaltstart dorthin routet. Antworte nicht mit einer allgemeinen Rechtskunde, sondern baue aus den Unterlagen eine handhabbare Fallsteuerung: Was ist sicher, was ist offen, was muss heute getan werden und welche Information darf noch nicht vorschnell preisgegeben werden?

**Fokus:** Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO/PAO/StBerG/WPO/BNotO je nach Beruf, Verfahrensrecht und EMRK-Grundsätze live prüfen
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

## 4. `berufsgericht-anschuldigungsschrift-verteidigung`

**Fokus:** Berufsgericht Anschuldigungsschrift (Verteidigungs- und Kammerantwort): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufsgericht Anschuldigungsschrift: Verteidigungs- und Kammerantwort

## Fachkern: Berufsgericht Anschuldigungsschrift: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Berufsgericht Anschuldigungsschrift: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Berufsgerichtliche Verfahren Freie Berufe**, wenn genau diese Lage auftaucht oder der Kaltstart dorthin routet. Antworte nicht mit einer allgemeinen Rechtskunde, sondern baue aus den Unterlagen eine handhabbare Fallsteuerung: Was ist sicher, was ist offen, was muss heute getan werden und welche Information darf noch nicht vorschnell preisgegeben werden?

**Fokus:** Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO/PAO/StBerG/WPO/BNotO je nach Beruf, Verfahrensrecht und EMRK-Grundsätze live prüfen
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

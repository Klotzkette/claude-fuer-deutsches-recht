---
name: epa-befuellpflicht-impfschaden-arzthaftung
description: "EPA Befuellpflicht Impfschaden Arzthaftung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# EPA Befuellpflicht Impfschaden Arzthaftung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **EPA Befuellpflicht Impfschaden Arzthaftung** im Plugin Fachanwalt Medizinrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `epa-befuellpflicht-haftung` | ePA-Befüllpflicht und Haftung: moderner Medizinrechts-Skill für ePA für alle, Befüllungspflichten, Informationspflichten, Widerspruch und Behandlungsfehler durch Datenlücke. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `impfschaden-arzthaftung` | Impfschaden und Arzthaftung: moderner Medizinrechts-Skill für Impfaufklärung, Chargenproblem, Versorgungsanspruch, Kausalität und Pharmakovigilanz. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `medr-arzthaftung-checkliste` | Checkliste Arzthaftung: Behandlungsfehler, grober Behandlungsfehler, Beweislastumkehr § 630h BGB, Befunderhebungsfehler, voll beherrschbares Risiko. Pruefraster Arzt und Patientenanwalt. |
| `palliativmedizin-haftung` | Palliativmedizin Haftung: moderner Medizinrechts-Skill für Symptomkontrolle, Sedierung, Patientenwille, Angehörigenkonflikt und Dokumentation. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |

## Arbeitsweg

Im Plugin Fachanwalt Medizinrecht gilt für **EPA Befuellpflicht Impfschaden Arzthaftung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `epa-befuellpflicht-haftung`

**Fokus:** ePA-Befüllpflicht und Haftung: moderner Medizinrechts-Skill für ePA für alle, Befüllungspflichten, Informationspflichten, Widerspruch und Behandlungsfehler durch Datenlücke. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# ePA-Befüllpflicht und Haftung

## Fachkern: ePA-Befüllpflicht und Haftung
- **Spezialgegenstand:** ePA-Befüllpflicht und Haftung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: ePA-Befüllpflicht und Haftung** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** ePA für alle, Befüllungspflichten, Informationspflichten, Widerspruch und Behandlungsfehler durch Datenlücke.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** SGB V Digitalrecht, BMG-ePA-Hinweise, §§ 630f/h BGB, DSGVO und Berufsrecht.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BMG ePA für alle: https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle
- BfArM DiGA: https://www.bfarm.de/DE/Medizinprodukte/Aufgaben/DiGA-und-DiPA/DiGA/_node.html
- EHDS Regulation EU 2025/327: https://eur-lex.europa.eu/eli/reg/2025/327/oj/
- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 2. `impfschaden-arzthaftung`

**Fokus:** Impfschaden und Arzthaftung: moderner Medizinrechts-Skill für Impfaufklärung, Chargenproblem, Versorgungsanspruch, Kausalität und Pharmakovigilanz. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# Impfschaden und Arzthaftung

## Fachkern: Impfschaden und Arzthaftung
- **Spezialgegenstand:** Impfschaden und Arzthaftung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Impfschaden und Arzthaftung** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Impfaufklärung, Chargenproblem, Versorgungsanspruch, Kausalität und Pharmakovigilanz.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** IfSG, SGB XIV soweit einschlägig, AMG, § 630e BGB und Produkthaftung.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 3. `medr-arzthaftung-checkliste`

**Fokus:** Checkliste Arzthaftung: Behandlungsfehler, grober Behandlungsfehler, Beweislastumkehr § 630h BGB, Befunderhebungsfehler, voll beherrschbares Risiko. Pruefraster Arzt und Patientenanwalt.


# MedR: Arzthaftung Checkliste

## Fachkern: MedR: Arzthaftung Checkliste
- **Spezialgegenstand:** MedR: Arzthaftung Checkliste wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 4. `palliativmedizin-haftung`

**Fokus:** Palliativmedizin Haftung: moderner Medizinrechts-Skill für Symptomkontrolle, Sedierung, Patientenwille, Angehörigenkonflikt und Dokumentation. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# Palliativmedizin Haftung

## Fachkern: Palliativmedizin Haftung
- **Spezialgegenstand:** Palliativmedizin Haftung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Palliativmedizin Haftung** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Symptomkontrolle, Sedierung, Patientenwille, Angehörigenkonflikt und Dokumentation.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** BGB Patientenrechte, Betreuungsrecht, Strafrechtliche Grenzen, Berufsrecht und Leitlinien live prüfen.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

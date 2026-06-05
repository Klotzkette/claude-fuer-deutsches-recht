---
name: energie-regulierungsakte-messstellenbetrieb
description: "Energie Regulierungsakte Messstellenbetrieb: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Energie Regulierungsakte Messstellenbetrieb

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Energie Regulierungsakte Messstellenbetrieb** im Plugin Bundesnetzagentur-Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-rec` | Messstellenbetrieb MsbG Smart Meter: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-ste` | Messstellenbetrieb MsbG Smart Meter: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-unt` | Messstellenbetrieb MsbG Smart Meter: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-nabeg-planfeststellung-rechtsmittel-che` | NABEG Planfeststellung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-nabeg-planfeststellung-stellungnahme-en` | NABEG Planfeststellung: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-nabeg-planfeststellung-unterlagenanford` | NABEG Planfeststellung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-netzanschluss-gas-rechtsmittel-check` | Netzanschluss Gas: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-netzanschluss-gas-unterlagenanforderung` | Netzanschluss Gas: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **Energie Regulierungsakte Messstellenbetrieb**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-rec`

**Fokus:** Messstellenbetrieb MsbG Smart Meter: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Rechtsmittel-Check

## Fachkern: Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Rechtsmittel-Check
- **Spezialgegenstand:** Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 2. `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-ste`

**Fokus:** Messstellenbetrieb MsbG Smart Meter: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Stellungnahme-Entwurf

## Fachkern: Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Stellungnahme-Entwurf
- **Spezialgegenstand:** Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Stellungnahme-Entwurf - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-unt`

**Fokus:** Messstellenbetrieb MsbG Smart Meter: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Unterlagenanforderung

## Fachkern: Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Unterlagenanforderung
- **Spezialgegenstand:** Energie-Regulierungsakte: Messstellenbetrieb MsbG Smart Meter — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 4. `energie-regulierungsakte-nabeg-planfeststellung-rechtsmittel-che`

**Fokus:** NABEG Planfeststellung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: NABEG Planfeststellung — Rechtsmittel-Check

## Fachkern: Energie-Regulierungsakte: NABEG Planfeststellung — Rechtsmittel-Check
- **Spezialgegenstand:** Energie-Regulierungsakte: NABEG Planfeststellung — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 5. `energie-regulierungsakte-nabeg-planfeststellung-stellungnahme-en`

**Fokus:** NABEG Planfeststellung: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: NABEG Planfeststellung — Stellungnahme-Entwurf

## Fachkern: Energie-Regulierungsakte: NABEG Planfeststellung — Stellungnahme-Entwurf
- **Spezialgegenstand:** Energie-Regulierungsakte: NABEG Planfeststellung — Stellungnahme-Entwurf - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 6. `energie-regulierungsakte-nabeg-planfeststellung-unterlagenanford`

**Fokus:** NABEG Planfeststellung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: NABEG Planfeststellung — Unterlagenanforderung

## Fachkern: Energie-Regulierungsakte: NABEG Planfeststellung — Unterlagenanforderung
- **Spezialgegenstand:** Energie-Regulierungsakte: NABEG Planfeststellung — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 7. `energie-regulierungsakte-netzanschluss-gas-rechtsmittel-check`

**Fokus:** Netzanschluss Gas: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: Netzanschluss Gas — Rechtsmittel-Check

## Fachkern: Energie-Regulierungsakte: Netzanschluss Gas — Rechtsmittel-Check
- **Spezialgegenstand:** Energie-Regulierungsakte: Netzanschluss Gas — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 8. `energie-regulierungsakte-netzanschluss-gas-unterlagenanforderung`

**Fokus:** Netzanschluss Gas: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.

# Energie-Regulierungsakte: Netzanschluss Gas — Unterlagenanforderung

## Fachkern: Energie-Regulierungsakte: Netzanschluss Gas — Unterlagenanforderung
- **Spezialgegenstand:** Energie-Regulierungsakte: Netzanschluss Gas — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

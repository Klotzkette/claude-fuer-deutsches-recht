---
name: tk-regulierungsakte-tk-akteneinsicht
description: "TK Regulierungsakte TK Akteneinsicht: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Regulierungsakte TK Akteneinsicht

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **TK Regulierungsakte TK Akteneinsicht** im Plugin Bundesnetzagentur-Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-regulierungsakte-nummernverwaltung-fristen-und-bescheidanalys` | Nummernverwaltung: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-rufnummernmissbrauch-fristen-und-bescheidana` | Rufnummernmissbrauch: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `verfahren-akteneinsicht-drittbeteiligte` | Verfahren / Akteneinsicht Drittbeteiligte: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |
| `verfahren-auskunftsersuchen-bnetza-beantworten` | Verfahren / Auskunftsersuchen BNetzA beantworten: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |
| `verfahren-beschlusskammertermin-muendliche-verhandlung` | Verfahren / Beschlusskammertermin mündliche Verhandlung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |
| `verfahren-bussgeldverfahren-bnetza` | Verfahren / Bußgeldverfahren BNetzA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |
| `verfahren-compliance-monitoring-nach-entscheidung` | Verfahren / Compliance-Monitoring nach Entscheidung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |
| `verfahren-durchsuchung-nachpruefung-dawn-raid` | Verfahren / Durchsuchung Nachprüfung Dawn Raid: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **TK Regulierungsakte TK Akteneinsicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-regulierungsakte-nummernverwaltung-fristen-und-bescheidanalys`

**Fokus:** Nummernverwaltung: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Nummernverwaltung — Fristen- und Bescheidanalyse

## Fachkern: TK-Regulierungsakte: Nummernverwaltung — Fristen- und Bescheidanalyse
- **Spezialgegenstand:** TK-Regulierungsakte: Nummernverwaltung — Fristen- und Bescheidanalyse - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** TKG, TDDDG, EECC-Rahmen, Frequenz-/Rufnummernzuteilung, Universaldienst, Marktregulierung, Missbrauchsaufsicht, Kundenschutz und BNetzA-Schlichtung.
- **Spezifische Weiche:** Prüfe zuerst, ob es um Endkundenrechte, Zugang/Interconnection, Frequenzen, Rufnummern, Sicherheit/Resilienz oder Marktregulierung geht; davon hängen Formular, Beschlusskammer, Beiladung und Rechtsweg ab.
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

## 2. `tk-regulierungsakte-rufnummernmissbrauch-fristen-und-bescheidana`

**Fokus:** Rufnummernmissbrauch: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Rufnummernmissbrauch — Fristen- und Bescheidanalyse

## Fachkern: TK-Regulierungsakte: Rufnummernmissbrauch — Fristen- und Bescheidanalyse
- **Spezialgegenstand:** TK-Regulierungsakte: Rufnummernmissbrauch — Fristen- und Bescheidanalyse - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** TKG, TDDDG, EECC-Rahmen, Frequenz-/Rufnummernzuteilung, Universaldienst, Marktregulierung, Missbrauchsaufsicht, Kundenschutz und BNetzA-Schlichtung.
- **Spezifische Weiche:** Prüfe zuerst, ob es um Endkundenrechte, Zugang/Interconnection, Frequenzen, Rufnummern, Sicherheit/Resilienz oder Marktregulierung geht; davon hängen Formular, Beschlusskammer, Beiladung und Rechtsweg ab.
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

## 3. `verfahren-akteneinsicht-drittbeteiligte`

**Fokus:** Verfahren / Akteneinsicht Drittbeteiligte: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Akteneinsicht Drittbeteiligte

## Fachkern: Verfahren: Akteneinsicht Drittbeteiligte
- **Spezialgegenstand:** Verfahren: Akteneinsicht Drittbeteiligte - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

## 4. `verfahren-auskunftsersuchen-bnetza-beantworten`

**Fokus:** Verfahren / Auskunftsersuchen BNetzA beantworten: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Auskunftsersuchen BNetzA beantworten

## Fachkern: Verfahren: Auskunftsersuchen BNetzA beantworten
- **Spezialgegenstand:** Verfahren: Auskunftsersuchen BNetzA beantworten - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

## 5. `verfahren-beschlusskammertermin-muendliche-verhandlung`

**Fokus:** Verfahren / Beschlusskammertermin mündliche Verhandlung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Beschlusskammertermin mündliche Verhandlung

## Fachkern: Verfahren: Beschlusskammertermin mündliche Verhandlung
- **Spezialgegenstand:** Verfahren: Beschlusskammertermin mündliche Verhandlung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

## 6. `verfahren-bussgeldverfahren-bnetza`

**Fokus:** Verfahren / Bußgeldverfahren BNetzA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Bußgeldverfahren BNetzA

## Fachkern: Verfahren: Bußgeldverfahren BNetzA
- **Spezialgegenstand:** Verfahren: Bußgeldverfahren BNetzA - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

## 7. `verfahren-compliance-monitoring-nach-entscheidung`

**Fokus:** Verfahren / Compliance-Monitoring nach Entscheidung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Compliance-Monitoring nach Entscheidung

## Fachkern: Verfahren: Compliance-Monitoring nach Entscheidung
- **Spezialgegenstand:** Verfahren: Compliance-Monitoring nach Entscheidung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

## 8. `verfahren-durchsuchung-nachpruefung-dawn-raid`

**Fokus:** Verfahren / Durchsuchung Nachprüfung Dawn Raid: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: VwVfG, VwGO, OWiG, Fachgesetze und BNetzA-Beschlusskammerpraxis.

# Verfahren: Durchsuchung Nachprüfung Dawn Raid

## Fachkern: Verfahren: Durchsuchung Nachprüfung Dawn Raid
- **Spezialgegenstand:** Verfahren: Durchsuchung Nachprüfung Dawn Raid - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** VwVfG, VwGO, OWiG, IFG/UIG soweit einschlägig, sektorales Fachgesetz und aktuelle BNetzA-Formulare, Konsultationen und Beschlusskammerhinweise.
- **Spezifische Weiche:** Kläre zuerst Sektor, Beschlusskammer, Verfahrensart, Beteiligtenstellung, Akteneinsicht, Anhörung, Frist, Eilbedarf und ob gerichtlicher Rechtsschutz zum VG/OVG oder über Spezialzuweisung läuft.
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

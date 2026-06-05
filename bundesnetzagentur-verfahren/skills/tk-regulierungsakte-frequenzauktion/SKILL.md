---
name: tk-regulierungsakte-frequenzauktion
description: "TK Regulierungsakte Frequenzauktion: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Regulierungsakte Frequenzauktion

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **TK Regulierungsakte Frequenzauktion** im Plugin Bundesnetzagentur-Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-regulierungsakte-frequenzauktion-unterlagenanforderung` | Frequenzauktion: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-frequenzzuteilung-rechtsmittel-check` | Frequenzzuteilung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-frequenzzuteilung-unterlagenanforderung` | Frequenzzuteilung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-nummernverwaltung-rechtsmittel-check` | Nummernverwaltung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-nummernverwaltung-unterlagenanforderung` | Nummernverwaltung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-rufnummernmissbrauch-rechtsmittel-check` | Rufnummernmissbrauch: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-rufnummernmissbrauch-unterlagenanforderung` | Rufnummernmissbrauch: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-tkg-marktregulierung-betraechtliche-marktm-2` | TKG Marktregulierung beträchtliche Marktmacht: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **TK Regulierungsakte Frequenzauktion**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-regulierungsakte-frequenzauktion-unterlagenanforderung`

**Fokus:** Frequenzauktion: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Frequenzauktion — Unterlagenanforderung

## Fachkern: TK-Regulierungsakte: Frequenzauktion — Unterlagenanforderung
- **Spezialgegenstand:** TK-Regulierungsakte: Frequenzauktion — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 2. `tk-regulierungsakte-frequenzzuteilung-rechtsmittel-check`

**Fokus:** Frequenzzuteilung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Frequenzzuteilung — Rechtsmittel-Check

## Fachkern: TK-Regulierungsakte: Frequenzzuteilung — Rechtsmittel-Check
- **Spezialgegenstand:** TK-Regulierungsakte: Frequenzzuteilung — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 3. `tk-regulierungsakte-frequenzzuteilung-unterlagenanforderung`

**Fokus:** Frequenzzuteilung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Frequenzzuteilung — Unterlagenanforderung

## Fachkern: TK-Regulierungsakte: Frequenzzuteilung — Unterlagenanforderung
- **Spezialgegenstand:** TK-Regulierungsakte: Frequenzzuteilung — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 4. `tk-regulierungsakte-nummernverwaltung-rechtsmittel-check`

**Fokus:** Nummernverwaltung: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Nummernverwaltung — Rechtsmittel-Check

## Fachkern: TK-Regulierungsakte: Nummernverwaltung — Rechtsmittel-Check
- **Spezialgegenstand:** TK-Regulierungsakte: Nummernverwaltung — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 5. `tk-regulierungsakte-nummernverwaltung-unterlagenanforderung`

**Fokus:** Nummernverwaltung: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Nummernverwaltung — Unterlagenanforderung

## Fachkern: TK-Regulierungsakte: Nummernverwaltung — Unterlagenanforderung
- **Spezialgegenstand:** TK-Regulierungsakte: Nummernverwaltung — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 6. `tk-regulierungsakte-rufnummernmissbrauch-rechtsmittel-check`

**Fokus:** Rufnummernmissbrauch: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Rufnummernmissbrauch — Rechtsmittel-Check

## Fachkern: TK-Regulierungsakte: Rufnummernmissbrauch — Rechtsmittel-Check
- **Spezialgegenstand:** TK-Regulierungsakte: Rufnummernmissbrauch — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 7. `tk-regulierungsakte-rufnummernmissbrauch-unterlagenanforderung`

**Fokus:** Rufnummernmissbrauch: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: Rufnummernmissbrauch — Unterlagenanforderung

## Fachkern: TK-Regulierungsakte: Rufnummernmissbrauch — Unterlagenanforderung
- **Spezialgegenstand:** TK-Regulierungsakte: Rufnummernmissbrauch — Unterlagenanforderung - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

## 8. `tk-regulierungsakte-tkg-marktregulierung-betraechtliche-marktm-2`

**Fokus:** TKG Marktregulierung beträchtliche Marktmacht: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.

# TK-Regulierungsakte: TKG Marktregulierung beträchtliche Marktmacht — Rechtsmittel-Check

## Fachkern: TK-Regulierungsakte: TKG Marktregulierung beträchtliche Marktmacht — Rechtsmittel-Check
- **Spezialgegenstand:** TK-Regulierungsakte: TKG Marktregulierung beträchtliche Marktmacht — Rechtsmittel-Check - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
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

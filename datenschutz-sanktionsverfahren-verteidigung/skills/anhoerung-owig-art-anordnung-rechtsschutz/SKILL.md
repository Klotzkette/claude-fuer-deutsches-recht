---
name: anhoerung-owig-art-anordnung-rechtsschutz
description: "Anhoerung 55 Owig, Art 58 Anordnung Verwaltungsakt, Art 78 Rechtsschutz Und Betroffenenbeschwerde, Art 83 Abs 2 Kriterien Einzeln: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anhoerung 55 Owig, Art 58 Anordnung Verwaltungsakt, Art 78 Rechtsschutz Und Betroffenenbeschwerde, Art 83 Abs 2 Kriterien Einzeln

## Arbeitsbereich

Dieser Skill bündelt **Anhoerung 55 Owig, Art 58 Anordnung Verwaltungsakt, Art 78 Rechtsschutz Und Betroffenenbeschwerde, Art 83 Abs 2 Kriterien Einzeln** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `anhoerung-55-owig` | Anhörung nach § 55 OWiG: Reaktion auf Anhörung vorbereiten, Aussagefreiheit wahren und Akteneinsicht anstoßen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `art-58-anordnung-verwaltungsakt` | Art.-58-Anordnung als Verwaltungsakt: Anordnung, Verwarnung, Verbot, Löschung und Transferstopp als verwaltungsgerichtliche Streitigkeit prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `art-78-rechtsschutz-und-betroffenenbeschwerde` | Art. 78 Rechtsschutz: Effektiven Rechtsschutz gegen Aufsichtsentscheidungen und Untätigkeit aus Sicht von Verantwortlichen oder Betroffenen ordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `art-83-abs-2-kriterien-einzeln` | Art. 83 Abs. 2 Kriterien einzeln prüfen: Alle Bußgeldkriterien einzeln mit Tatsachen, Entlastung und Gegenrechnung bearbeiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |

## Arbeitsweg

Für **Anhoerung 55 Owig, Art 58 Anordnung Verwaltungsakt, Art 78 Rechtsschutz Und Betroffenenbeschwerde, Art 83 Abs 2 Kriterien Einzeln** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `datenschutz-sanktionsverfahren-verteidigung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `anhoerung-55-owig`

**Fokus:** Anhörung nach § 55 OWiG: Reaktion auf Anhörung vorbereiten, Aussagefreiheit wahren und Akteneinsicht anstoßen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Anhörung nach § 55 OWiG

## Aufgabe

Reaktion auf Anhörung vorbereiten, Aussagefreiheit wahren und Akteneinsicht anstoßen.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 83 DSGVO
- § 41 BDSG
- §§ 49, 55, 65, 67, 68, 69, 71, 72, 73, 79 OWiG
- § 147 StPO

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Verteidigungsbaustein für OWiG-Verfahren mit Akteneinsicht, Einspruch, Beweisthemen und Terminstrategie.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 2. `art-58-anordnung-verwaltungsakt`

**Fokus:** Art.-58-Anordnung als Verwaltungsakt: Anordnung, Verwarnung, Verbot, Löschung und Transferstopp als verwaltungsgerichtliche Streitigkeit prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Art.-58-Anordnung als Verwaltungsakt

## Aufgabe

Anordnung, Verwarnung, Verbot, Löschung und Transferstopp als verwaltungsgerichtliche Streitigkeit prüfen.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 58 und Art. 78 DSGVO
- § 20 BDSG
- VwGO §§ 42, 80, 123 live prüfen
- Verhältnismäßigkeit und Bestimmtheit

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Klage- oder Eilrechtsschutzgerüst gegen Art.-58-Maßnahme mit Zulässigkeit, Begründetheit und Anlagenplan.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 3. `art-78-rechtsschutz-und-betroffenenbeschwerde`

**Fokus:** Art. 78 Rechtsschutz: Effektiven Rechtsschutz gegen Aufsichtsentscheidungen und Untätigkeit aus Sicht von Verantwortlichen oder Betroffenen ordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Art. 78 Rechtsschutz

## Aufgabe

Effektiven Rechtsschutz gegen Aufsichtsentscheidungen und Untätigkeit aus Sicht von Verantwortlichen oder Betroffenen ordnen.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 58 und Art. 78 DSGVO
- § 20 BDSG
- VwGO §§ 42, 80, 123 live prüfen
- Verhältnismäßigkeit und Bestimmtheit

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Klage- oder Eilrechtsschutzgerüst gegen Art.-58-Maßnahme mit Zulässigkeit, Begründetheit und Anlagenplan.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 4. `art-83-abs-2-kriterien-einzeln`

**Fokus:** Art. 83 Abs. 2 Kriterien einzeln prüfen: Alle Bußgeldkriterien einzeln mit Tatsachen, Entlastung und Gegenrechnung bearbeiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Art. 83 Abs. 2 Kriterien einzeln prüfen

## Aufgabe

Alle Bußgeldkriterien einzeln mit Tatsachen, Entlastung und Gegenrechnung bearbeiten.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 83 Abs. 1 bis 6 DSGVO
- EDPB Guidelines 04/2022
- EuGH C-807/21
- EuGH C-683/21

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Art.-83-Bemessungsmemo mit Behördenkritik, Entlastungsmaterial, Gegenrechnung und Milderungsargumenten.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

---
name: kirchliche-datenschutzaufsicht-massnahmenplan
description: "Kirchliche Datenschutzaufsicht Massnahmenplan: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kirchliche Datenschutzaufsicht Massnahmenplan

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kirchliche Datenschutzaufsicht Massnahmenplan** im Plugin Datenschutz-Sanktionsverfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kirchliche-datenschutzaufsicht-sanktionen` | Kirchliche Datenschutzaufsicht: KDG, DSG-EKD, kirchliche Aufsichten, kirchliche Gerichte und Sanktionslogik einordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `massnahmenplan-als-sanktionsminderung` | Maßnahmenplan als Sanktionsminderung: Root Cause, Sofortmaßnahme, Owner, Budget, Wirksamkeitsmessung und Nachweise bußgeldmindernd aufbereiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `oeffentliche-stellen-bussgeldprivilegien` | Öffentliche Stellen und Bußgeldfähigkeit: Bußgeldfähigkeit öffentlicher Stellen nach Art. 83 Abs. 7 DSGVO, BDSG und Landesrecht prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `sanktionsmandat-schlussprodukt-planen` | Schlussprodukt des Sanktionsmandats planen: Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |

## Arbeitsweg

Im Plugin Datenschutz-Sanktionsverfahren gilt für **Kirchliche Datenschutzaufsicht Massnahmenplan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kirchliche-datenschutzaufsicht-sanktionen`

**Fokus:** Kirchliche Datenschutzaufsicht: KDG, DSG-EKD, kirchliche Aufsichten, kirchliche Gerichte und Sanktionslogik einordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Kirchliche Datenschutzaufsicht

## Aufgabe

KDG, DSG-EKD, kirchliche Aufsichten, kirchliche Gerichte und Sanktionslogik einordnen.

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

## 2. `massnahmenplan-als-sanktionsminderung`

**Fokus:** Maßnahmenplan als Sanktionsminderung: Root Cause, Sofortmaßnahme, Owner, Budget, Wirksamkeitsmessung und Nachweise bußgeldmindernd aufbereiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Maßnahmenplan als Sanktionsminderung

## Aufgabe

Root Cause, Sofortmaßnahme, Owner, Budget, Wirksamkeitsmessung und Nachweise bußgeldmindernd aufbereiten.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 31 und Art. 58 DSGVO
- Art. 83 Abs. 2 DSGVO
- § 55 OWiG
- § 20/§ 41 BDSG je nach Spur

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

Behördenstrategie mit Antwortentwurf, Vorbehalten, Anlagenplan und Schutz vor überschießender Selbstbelastung.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 3. `oeffentliche-stellen-bussgeldprivilegien`

**Fokus:** Öffentliche Stellen und Bußgeldfähigkeit: Bußgeldfähigkeit öffentlicher Stellen nach Art. 83 Abs. 7 DSGVO, BDSG und Landesrecht prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Öffentliche Stellen und Bußgeldfähigkeit

## Aufgabe

Bußgeldfähigkeit öffentlicher Stellen nach Art. 83 Abs. 7 DSGVO, BDSG und Landesrecht prüfen.

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

## 4. `sanktionsmandat-schlussprodukt-planen`

**Fokus:** Schlussprodukt des Sanktionsmandats planen: Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

# Schlussprodukt des Sanktionsmandats planen

## Aufgabe

Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 58, 78, 83 DSGVO
- § 20 BDSG
- § 41 BDSG
- §§ 55, 65, 67 OWiG

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

Mandats-Cockpit mit Verfahrensspur, Fristen, Sofortmaßnahmen, Risikoampel und nächsten Skills.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

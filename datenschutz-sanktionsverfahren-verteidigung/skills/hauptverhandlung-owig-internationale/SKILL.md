---
name: hauptverhandlung-owig-internationale
description: "Hauptverhandlung Owig Internationale im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Hauptverhandlung § 71 OWiG, Internationale Datenpanne und Multi-Notification, Interne Untersuchung und Legal Hold, Irische DPC und deutsche Aufsicht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Hauptverhandlung Owig Internationale

## Arbeitsbereich

**Hauptverhandlung Owig Internationale** ordnet den Fall über die tragenden Prüfungslinien: Hauptverhandlung § 71 OWiG, Internationale Datenpanne und Multi-Notification, Interne Untersuchung und Legal Hold. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `hauptverhandlung-71-owig` | Hauptverhandlung § 71 OWiG: Hauptverhandlung mit StPO-Logik, Beweisaufnahme, Zeugen, Sachverständigen und Anträgen vorbereiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `internationale-datenpanne-und-multi-notification` | Internationale Datenpanne und Multi-Notification: Meldungen in mehreren Jurisdiktionen ohne widersprüchliche Sachverhalte und mit Lead-Authority-Strategie planen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `interne-untersuchung-legal-hold` | Interne Untersuchung und Legal Hold: Dokumentensicherung, E-Mail, Tickets, Logs, Backups, DSB-Hinweise und Vorstandsvorlagen organisieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |
| `irische-dpc-und-deutsche-aufsicht` | Irische DPC und deutsche Aufsicht: Plattform-/SaaS-Fälle mit irischer Hauptniederlassung und deutscher Beschwerde routen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; OWiG; StPO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `hauptverhandlung-71-owig`

**Fokus:** Hauptverhandlung § 71 OWiG: Hauptverhandlung mit StPO-Logik, Beweisaufnahme, Zeugen, Sachverständigen und Anträgen vorbereiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

### Hauptverhandlung § 71 OWiG

## Aufgabe

Hauptverhandlung mit StPO-Logik, Beweisaufnahme, Zeugen, Sachverständigen und Anträgen vorbereiten.

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

## 2. `internationale-datenpanne-und-multi-notification`

**Fokus:** Internationale Datenpanne und Multi-Notification: Meldungen in mehreren Jurisdiktionen ohne widersprüchliche Sachverhalte und mit Lead-Authority-Strategie planen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

### Internationale Datenpanne und Multi-Notification

## Aufgabe

Meldungen in mehreren Jurisdiktionen ohne widersprüchliche Sachverhalte und mit Lead-Authority-Strategie planen.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 56, 60, 65 DSGVO
- Art. 267 AEUV
- Art. 47, 48, 50, 52 GRCh
- CURIA/EDPB live prüfen

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

EU-Verfahrensmemo mit Zuständigkeit, Behördenkoordination, Vorlagefragen und Quellencheck.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 3. `interne-untersuchung-legal-hold`

**Fokus:** Interne Untersuchung und Legal Hold: Dokumentensicherung, E-Mail, Tickets, Logs, Backups, DSB-Hinweise und Vorstandsvorlagen organisieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

### Interne Untersuchung und Legal Hold

## Aufgabe

Dokumentensicherung, E-Mail, Tickets, Logs, Backups, DSB-Hinweise und Vorstandsvorlagen organisieren.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 5 Abs. 2, Art. 24, 32 DSGVO
- § 41 BDSG / OWiG-StPO-Verweise
- § 203 StGB und Mandatsgeheimnis live prüfen
- Technische Beweise verifizieren

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

Beweis- und Untersuchungsplan mit Dokumentensicherung, technischer Plausibilisierung und Vertraulichkeitsschutz.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 4. `irische-dpc-und-deutsche-aufsicht`

**Fokus:** Irische DPC und deutsche Aufsicht: Plattform-/SaaS-Fälle mit irischer Hauptniederlassung und deutscher Beschwerde routen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zuständigkeit, Beweismaßstab und Unternehmensverantwortung fallbezogen prüfen.

### Irische DPC und deutsche Aufsicht

## Aufgabe

Plattform-/SaaS-Fälle mit irischer Hauptniederlassung und deutscher Beschwerde routen.

Dieser Skill arbeitet als präzises Werkzeug für das datenschutzrechtliche Sanktionsverfahren. Er trennt Aufsichtsverfahren, Bußgeldverfahren und Verwaltungsrechtsweg, prüft DSGVO Art. 58/83, BDSG § 41, OWiG und die über § 46 OWiG einbezogene StPO und klärt zuerst Verfahrensstand, Behörde, Zustellung, Frist, Beweisstand und gewünschtes Arbeitsprodukt.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 56, 60, 65 DSGVO
- Art. 267 AEUV
- Art. 47, 48, 50, 52 GRCh
- CURIA/EDPB live prüfen

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

EU-Verfahrensmemo mit Zuständigkeit, Behördenkoordination, Vorlagefragen und Quellencheck.

## Anschlussskills

Je nach Ergebnis weitere Skills ziehen: `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `akteneinsicht-49-owig-147-stpo`, `art-83-abs-2-kriterien-einzeln`, `edpb-04-2022-bemessungsmethodik`, `art-58-anordnung-verwaltungsakt`, `vg-eilrechtsschutz-80-5-vwgo`, `one-stop-shop-art-56-60` oder `red-team-vor-jeder-einreichung`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

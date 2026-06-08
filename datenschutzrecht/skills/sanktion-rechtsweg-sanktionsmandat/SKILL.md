---
name: sanktion-rechtsweg-sanktionsmandat
description: "DSV Sanktion Rechtsweg Sanktionsmandat im Datenschutzrecht: prüft konkret Datenschutzrecht-Brückenskill. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# DSV Sanktion Rechtsweg Sanktionsmandat

## Arbeitsbereich

**DSV Sanktion Rechtsweg Sanktionsmandat** ordnet den Fall über die tragenden Prüfungslinien: Datenschutzrecht-Brückenskill. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `dsv-sanktion-rechtsweg-router` | Datenschutzrecht-Brückenskill: Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren: Geldbuße, Art.-58-Maßnahme, Art.-82-Schadensersatz und Strafrechtsspur aus demselben Vorfall trennen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |
| `dsv-sanktion-sanktionsmandat-schlussprodukt-planen` | Datenschutzrecht-Brückenskill: Schlussprodukt des Sanktionsmandats planen: Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |
| `dsv-sanktion-scope-cut-behoerdenfragen-einhegen` | Datenschutzrecht-Brückenskill: Scope Cut Behördenfragen einhegen: Zu weite Behördenfragen nach Zeitraum, System, Datenart, Gesellschaft und Betroffenenkreis begrenzen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |
| `dsv-sanktion-selbstbelastungsfreiheit-und-mitwirkungspflichten` | Datenschutzrecht-Brückenskill: Selbstbelastung und Mitwirkungspflichten: Auskunftspflichten gegenüber der Aufsicht und Aussagefreiheit im Bußgeldverfahren balancieren. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |
| `dsv-sanktion-staatsanwaltschaft-im-dsgvo-owig` | Datenschutzrecht-Brückenskill: Staatsanwaltschaft im DSGVO-OWiG-Verfahren: Rolle der Staatsanwaltschaft nach Akteneingang und Zustimmungserfordernis der Aufsicht bei Einstellung erklären. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `dsv-sanktion-rechtsweg-router`

**Fokus:** Datenschutzrecht-Brückenskill: Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren: Geldbuße, Art.-58-Maßnahme, Art.-82-Schadensersatz und Strafrechtsspur aus demselben Vorfall trennen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

### Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren

## Aufgabe

Geldbuße, Art.-58-Maßnahme, Art.-82-Schadensersatz und Strafrechtsspur aus demselben Vorfall trennen.

Dieser Skill ist ein konkretes Modul für Datenschutz-Sanktionsverfahren. Starte mit Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtem Arbeitsprodukt; danach wird genau dieses Teilproblem bearbeitet, ohne allgemeine Datenschutzfloskeln vorzuschalten.

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

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 2. `dsv-sanktion-sanktionsmandat-schlussprodukt-planen`

**Fokus:** Datenschutzrecht-Brückenskill: Schlussprodukt des Sanktionsmandats planen: Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

### Schlussprodukt des Sanktionsmandats planen

## Aufgabe

Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren.

Dieser Skill ist ein konkretes Modul für Datenschutz-Sanktionsverfahren. Starte mit Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtem Arbeitsprodukt; danach wird genau dieses Teilproblem bearbeitet, ohne allgemeine Datenschutzfloskeln vorzuschalten.

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

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 3. `dsv-sanktion-scope-cut-behoerdenfragen-einhegen`

**Fokus:** Datenschutzrecht-Brückenskill: Scope Cut Behördenfragen einhegen: Zu weite Behördenfragen nach Zeitraum, System, Datenart, Gesellschaft und Betroffenenkreis begrenzen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

### Scope Cut Behördenfragen einhegen

## Aufgabe

Zu weite Behördenfragen nach Zeitraum, System, Datenart, Gesellschaft und Betroffenenkreis begrenzen.

Dieser Skill ist ein konkretes Modul für Datenschutz-Sanktionsverfahren. Starte mit Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtem Arbeitsprodukt; danach wird genau dieses Teilproblem bearbeitet, ohne allgemeine Datenschutzfloskeln vorzuschalten.

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

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 4. `dsv-sanktion-selbstbelastungsfreiheit-und-mitwirkungspflichten`

**Fokus:** Datenschutzrecht-Brückenskill: Selbstbelastung und Mitwirkungspflichten: Auskunftspflichten gegenüber der Aufsicht und Aussagefreiheit im Bußgeldverfahren balancieren. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

### Selbstbelastung und Mitwirkungspflichten

## Aufgabe

Auskunftspflichten gegenüber der Aufsicht und Aussagefreiheit im Bußgeldverfahren balancieren.

Dieser Skill ist ein konkretes Modul für Datenschutz-Sanktionsverfahren. Starte mit Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtem Arbeitsprodukt; danach wird genau dieses Teilproblem bearbeitet, ohne allgemeine Datenschutzfloskeln vorzuschalten.

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

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

## 5. `dsv-sanktion-staatsanwaltschaft-im-dsgvo-owig`

**Fokus:** Datenschutzrecht-Brückenskill: Staatsanwaltschaft im DSGVO-OWiG-Verfahren: Rolle der Staatsanwaltschaft nach Akteneingang und Zustimmungserfordernis der Aufsicht bei Einstellung erklären. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

### Staatsanwaltschaft im DSGVO-OWiG-Verfahren

## Aufgabe

Rolle der Staatsanwaltschaft nach Akteneingang und Zustimmungserfordernis der Aufsicht bei Einstellung erklären.

Dieser Skill ist ein konkretes Modul für Datenschutz-Sanktionsverfahren. Starte mit Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtem Arbeitsprodukt; danach wird genau dieses Teilproblem bearbeitet, ohne allgemeine Datenschutzfloskeln vorzuschalten.

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

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.

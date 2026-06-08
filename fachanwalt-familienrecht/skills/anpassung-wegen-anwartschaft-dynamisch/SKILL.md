---
name: anpassung-wegen-anwartschaft-dynamisch
description: "Anpassung Wegen Anwartschaft Dynamisch im Plugin Fachanwalt Familienrecht: prüft konkret Anpassung wegen Unterhalt §§ 33 ff VersAusglG, Anwartschaft dynamisch statisch Bewertung, Ausgleich nach der Scheidung §§ 20 ff VersAusglG, Ausländische Anrechte Versorgungsausgleich. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anpassung Wegen Anwartschaft Dynamisch

## Arbeitsbereich

**Anpassung Wegen Anwartschaft Dynamisch** ordnet den Fall über die tragenden Prüfungslinien: Anpassung wegen Unterhalt §§ 33 ff VersAusglG, Anwartschaft dynamisch statisch Bewertung, Ausgleich nach der Scheidung §§ 20 ff VersAusglG. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `anpassung-wegen-unterhalt-33-ff-versausglg` | Anpassung wegen Unterhalt §§ 33 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |
| `anwartschaft-dynamisch-statisch-bewertung` | Anwartschaft dynamisch statisch Bewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |
| `ausgleich-nach-der-scheidung-20-ff-versausglg` | Ausgleich nach der Scheidung §§ 20 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |
| `auslaendische-anrechte-versorgungsausgleich` | Ausländische Anrechte Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |
| `ausschluss-grobe-unbilligkeit-27-versausglg` | Ausschluss grobe Unbilligkeit § 27 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `anpassung-wegen-unterhalt-33-ff-versausglg`

**Fokus:** Anpassung wegen Unterhalt §§ 33 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Anpassung wegen Unterhalt §§ 33 ff VersAusglG

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anpassung wegen Unterhalt §§ 33 ff VersAusglG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Anpassung wegen Unterhalt §§ 33 ff VersAusglG
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 2. `anwartschaft-dynamisch-statisch-bewertung`

**Fokus:** Anwartschaft dynamisch statisch Bewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Anwartschaft dynamisch statisch Bewertung

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anwartschaft dynamisch statisch Bewertung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Anwartschaft dynamisch statisch Bewertung
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `ausgleich-nach-der-scheidung-20-ff-versausglg`

**Fokus:** Ausgleich nach der Scheidung §§ 20 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Ausgleich nach der Scheidung §§ 20 ff VersAusglG

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ausgleich nach der Scheidung §§ 20 ff VersAusglG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Ausgleich nach der Scheidung §§ 20 ff VersAusglG
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 4. `auslaendische-anrechte-versorgungsausgleich`

**Fokus:** Ausländische Anrechte Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Ausländische Anrechte Versorgungsausgleich

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ausländische Anrechte Versorgungsausgleich` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Ausländische Anrechte Versorgungsausgleich
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 5. `ausschluss-grobe-unbilligkeit-27-versausglg`

**Fokus:** Ausschluss grobe Unbilligkeit § 27 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Ausschluss grobe Unbilligkeit § 27 VersAusglG

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ausschluss grobe Unbilligkeit § 27 VersAusglG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Ausschluss grobe Unbilligkeit § 27 VersAusglG
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einsatz
Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 51 VersAusglG
- § 165 FamFG
- § 156 FamFG
- § 89 FamFG
- § 3 VersAusglG
- § 137 FamFG
- § 49 FamFG
- § 18 VersAusglG
- § 63 FamFG
- § 2 SBGG
- § 158 FamFG
- § 1 VersAusglG

### Leitentscheidungen

- BGH XII ZB 186/15
- BGH XII ZR 129/04
- BGH XII ZB 72/19
- BGH XII ZR 181/22


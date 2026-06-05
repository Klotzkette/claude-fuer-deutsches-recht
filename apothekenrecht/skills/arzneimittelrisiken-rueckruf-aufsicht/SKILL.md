---
name: arzneimittelrisiken-rueckruf-aufsicht
description: "Arzneimittelrisiken Rueckruf Aufsicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arzneimittelrisiken Rueckruf Aufsicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Arzneimittelrisiken Rueckruf Aufsicht** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arzneimittelrisiken-rueckruf-chargenrueckverfolgung` | Arzneimittelrisiken Rückruf Chargenrückverfolgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `aufsicht-anhoerung-ordnungswidrigkeit` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aufsicht Anhörung Ordnungswidrigkeit. |
| `beanstandung-durch-aufsichtsbehoerde-anhoerung` | Beanstandung durch Aufsichtsbehörde Anhörung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Arzneimittelrisiken Rueckruf Aufsicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arzneimittelrisiken-rueckruf-chargenrueckverfolgung`

**Fokus:** Arzneimittelrisiken Rückruf Chargenrückverfolgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Arzneimittelrisiken Rückruf Chargenrückverfolgung

## Fachkern: Arzneimittelrisiken Rückruf Chargenrückverfolgung
- **Spezialgegenstand:** Arzneimittelrisiken Rückruf Chargenrückverfolgung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Arzneimittelrisiken Rückruf Chargenrückverfolgung** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 2. `aufsicht-anhoerung-ordnungswidrigkeit`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aufsicht Anhörung Ordnungswidrigkeit.

# Aufsicht Anhörung Ordnungswidrigkeit

## Fachkern: Aufsicht Anhörung Ordnungswidrigkeit
- **Spezialgegenstand:** Aufsicht Anhörung Ordnungswidrigkeit. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Landesaufsichtsbehörden (Regierungspräsidium, Landesamt für Gesundheit, Apothekerkammer) führen Apothekenrevisionen durch und leiten bei Beanstandungen Anhörungs- oder Ordnungswidrigkeitenverfahren ein. Verstösse gegen ApoG, ApBetrO, AMG, BtMG sind teils OWi (§ 97 AMG, § 32 BtMG, § 25 ApoG), teils strafbewehrt. Anhörung nach § 28 VwVfG geht jeder belastenden Massnahme voraus. Ziel des Skills: strukturierte Verteidigung.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Anhörungsschreiben der Landesaufsicht ist eingegangen.
- OWi-Bescheid mit Bussgeldforderung.
- Drohung mit Erlaubniswiderruf nach § 4 ApoG.
- Sofortvollzug nach § 80 Abs. 2 VwGO angeordnet (Schliessungsverfügung).
- Strafrechtliche Nebenfolge erwartet.

Eingaben:
- Anhörungsschreiben / OWi-Bescheid mit Datum, Vorhalten, Frist.
- Apothekenakten zum Vorgang (Rezept, Charge, Beratungsprotokoll, SOP).
- Bisherige Korrespondenz mit Behörde.
- Revisionsbericht (sofern Anlass).
- Berufshaftpflicht-Versicherungsschein zur Schadensmeldung.

## Rechtlicher Rahmen

- **§ 28 VwVfG:** Anhörung vor belastendem VA.
- **§§ 96, 97 AMG:** Straftaten und Ordnungswidrigkeiten.
- **§§ 29 ff. BtMG; § 32 BtMG:** Straftat / OWi BtM-Bereich.
- **§§ 25, 26 ApoG:** OWi Apothekenrecht.
- **§ 4 ApoG:** Widerruf der Erlaubnis (eingriffsintensivste Sanktion).
- **§ 80 VwGO:** Sofortvollzug und Widerspruch.
- **§ 47 VwGO:** Normenkontrolle.
- **OWiG** §§ 17, 47, 65 — Bussgeldverfahren.
- BVerwG, OVG, VGH staend. Rspr. zur Apothekenaufsicht.

## / Schritt für Schritt

1. **Frist ermitteln:** Anhörungsfrist regelmässig zwei Wochen; bei OWi-Bescheid Einspruchsfrist zwei Wochen (§ 67 OWiG).
2. **Akteneinsicht beantragen:** § 29 VwVfG / § 49 OWiG. Verzögernde Wirkung — Antragstellung sofort.
3. **Vorhalte konkret prüfen:**
 - Rechtsgrundlage (Norm korrekt?)
 - Tatsachenstand (was ist gesichert, was ist Behauptung?)
 - Verschuldensform (Vorsatz/Fahrlässigkeit)
 - Wiederholungsrisiko
4. **Stellungnahme strukturieren:**
 - Sachverhalt aus eigener Sicht klarstellen.
 - Rechtliche Würdigung (Tatbestand erfüllt? Rechtfertigung? Schuld?)
 - Verhältnismässigkeit der angedrohten Massnahme.
 - Kooperationsbereitschaft und Abhilfemassnahmen darlegen.
5. **Beweisangebote:** Zeugen (Mitarbeiter), Urkunden (SOP, QM-Handbuch), ggf. Sachverständige.
6. **Sofortvollzug:** Sofort Antrag auf Wiederherstellung der aufschiebenden Wirkung nach § 80 Abs. 5 VwGO ans VG.
7. **OWi-Einspruch:** Form- und fristgerecht bei zuständiger Behörde.
8. **Strafrechtsweg:** Bei §§ 95 AMG, 29 BtMG, 299a StGB sofort Strafverteidiger einbinden.

## Trade-off-Matrix

| Konstellation | Sanktion | Verteidigungslinie | Hinweis |
|---|---|---|---|
| Geringe Beanstandung Revision | mündliche Belehrung | Abhilfe + Schulung | meist erledigt |
| OWi formaler Verstoss | Bussgeld 50–5.000 Euro | § 17 OWiG Verhältnismässigkeit | Einspruch lohnt selten |
| OWi schwerer Verstoss (Beratungspflicht-Mangel) | bis 25.000 Euro | Sachverhaltsverteidigung | Strafrechtsweg vermeiden |
| Erlaubniswiderruf-Drohung | existenzgefährdend | aktive Sanierung, Sanierungsplan | Eilrechtsschutz |
| BtM-Differenz § 29 BtMG | Strafe | Strafverteidiger | Schweigerecht |
| Versorgungsvertrag-Beanstandung | Vertragsanpassung | Korrekturplan | Aufsicht kooperativ |

## Praxistipps

- Niemals impulsiv reagieren — Frist nutzen, Akte studieren.
- Anhörung ist Chance: aktiv Abhilfe darstellen, Schulungspläne vorlegen, SOP-Updates präsentieren — Behörde belohnt Kooperation.
- Bei Sofortvollzug Eilantrag VG **sofort** stellen — sonst Schliessung trotz später Erfolgsaussicht.
- Versicherung informieren (Berufshaftpflicht, Rechtsschutz).
- Schweigerecht im Strafverfahren beachten; Stellungnahme nur mit Strafverteidiger:in.

## Mustertexte

### Stellungnahme zur Anhörung (Auszug)
"Sehr geehrte Damen und Herren, mit Schreiben vom [Datum] (Az [...]) wurden uns folgende Vorhalte gemacht: 1. [Vorhalt 1]; 2. [Vorhalt 2]; 3. [Vorhalt 3]. Hierzu nehmen wir nach Akteneinsicht wie folgt Stellung: Zu 1.: [Sachverhalt klarstellen, Belege beilegen, ggf. Plausibilitätsprüfung-Dokumentation vorzeigen]. Zu 2.: [Tatbestand fehlt, da ...]. Zu 3.: [Erkannter Mangel ist behoben durch [Massnahme]; SOP wurde am [Datum] aktualisiert, Schulung am [Datum] erfolgt]. Eine Wiederholung ist nicht zu erwarten. Wir bitten von einer Sanktion abzusehen oder diese auf das mildeste Mittel zu beschränken (§ 17 OWiG)."

### Einspruch gegen OWi-Bescheid (Auszug)
"Gegen den Bussgeldbescheid vom [Datum] (Az [...]) lege ich form- und fristgerecht Einspruch ein. Begründung: 1. Der Tatbestand ist nicht erfüllt, da [...]. 2. Hilfsweise: Die festgesetzte Geldbusse ist unverhältnismässig (§ 17 OWiG). Erstmaliger Verstoss, geringer Schaden, sofortige Abhilfe (Anlage [Nr.]). Ich beantrage Aufhebung des Bescheides, hilfsweise Reduzierung der Geldbusse auf einen angemessenen Betrag."

### Eilantrag § 80 V VwGO (Auszug)
"In dem Verwaltungsrechtsstreit [...] beantragen wir die Wiederherstellung der aufschiebenden Wirkung unseres Widerspruchs gegen die Verfügung der Behörde vom [Datum] (Schliessung der Apotheke ab [Datum]). Begründung: Der Sofortvollzug ist unverhältnismässig und gefährdet existenziell den Betrieb. Die Erfolgsaussichten im Hauptsacheverfahren sind erheblich [Begründung]. Ein Aufschub ist mit dem öffentlichen Interesse vereinbar, da [...]."

## Typische Fehler

- Fristen versäumt — Bescheid wird bestandskräftig.
- Vorschnell unterzeichneter "Vergleich" mit Behörde — bindet ohne Anwaltsberatung.
- Stellungnahme bei Strafrechtsbezug ohne Strafverteidiger:in.
- Sofortvollzug-Schliessung wird hingenommen ohne Eilantrag VG.
- "Verteidigung mit Selbstvorwürfen" — Schuldeingeständnis ohne Rechtfertigungsversuch.

## Querverweise

- `beanstandung-durch-aufsichtsbehoerde-anhoerung` (Anhörungsablauf)
- `apothekenrevision-vorbereitung-antwort` (Revisionsvorbereitung)
- `widerruf-ruecknahme-ruhen-apothekenerlaubnis` (Widerruf)
- `owi-strafrisiken-apog-amg-btmg` (Strafrisiko)
- `output-behoerdenbrief-sop-mandantenmemo` (Schreibhilfe)
- `apothekenbetriebsordnung-grundpflichten` (Grundpflichten)

## Quellen Stand 06/2026

- ApoG §§ 4, 25, 26; ApBetrO; AMG §§ 95–97; BtMG §§ 29 ff., 32.
- VwVfG § 28; VwGO §§ 80, 47; OWiG §§ 17, 47, 65–67.
- BVerwG / OVG / VGH staend. Rspr. zur Apothekenaufsicht.
- BGH staend. Rspr. zu §§ 299a/b StGB im Apothekenkontext.
- Landesapothekerkammer-Beanstandungsleitfäden (vom Anwender zu verifizieren).

## 3. `beanstandung-durch-aufsichtsbehoerde-anhoerung`

**Fokus:** Beanstandung durch Aufsichtsbehörde Anhörung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Beanstandung durch Aufsichtsbehörde Anhörung

## Fachkern: Beanstandung durch Aufsichtsbehörde Anhörung
- **Spezialgegenstand:** Beanstandung durch Aufsichtsbehörde Anhörung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Beanstandung durch Aufsichtsbehörde Anhörung** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

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
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

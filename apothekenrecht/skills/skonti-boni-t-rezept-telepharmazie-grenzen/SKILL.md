---
name: skonti-boni-t-rezept-telepharmazie-grenzen
description: "Skonti Boni T Rezept Telepharmazie Grenzen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Skonti Boni T Rezept Telepharmazie Grenzen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Skonti Boni T Rezept Telepharmazie Grenzen** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `skonti-boni-rabatte-zuweisungsverbot` | Skonti Boni Rabatte Zuweisungsverbot: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `t-rezept-besondere-arzneimittel` | T-Rezept besondere Arzneimittel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `telepharmazie-grenzen-chancen` | Telepharmazie Grenzen Chancen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Skonti Boni T Rezept Telepharmazie Grenzen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `skonti-boni-rabatte-zuweisungsverbot`

**Fokus:** Skonti Boni Rabatte Zuweisungsverbot: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Skonti Boni Rabatte Zuweisungsverbot

## Fachkern: Skonti Boni Rabatte Zuweisungsverbot
- **Spezialgegenstand:** Skonti Boni Rabatte Zuweisungsverbot. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Skonti, Boni, Rabatte, Gewinnbeteiligungen und Zuweisungspakte sind in der Apothekenbranche stark reguliert. Zentrale Regelungen: AMPreisV (Endpreis-Bindung bei Rx), § 7 HWG (Heilmittelwerbegesetz, Geschenke-Verbot), § 11 ApoG (Zuweisungsverbot Arzt-Apotheke), §§ 299a/b StGB (Korruption im Gesundheitswesen). Skonti zwischen Grosshandel und Apotheke sind ein eigenes Streitfeld (BGH 2024; vom Anwender Aktualität zu verifizieren).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Apotheke plant Rabattaktion, Bonusprogramm, Treuepunkte.
- Arzt schickt Patienten regelmässig in bestimmte Apotheke; Zuweisungsverbot geprüft.
- Grosshandelsangebot mit hohem Skonto, Vereinbarkeit mit BGH-Linie.
- Strafrechtlicher Verdacht §§ 299a/b StGB (Antikorruption Gesundheitswesen).
- Werbeauftritt mit "Vorteil"-Versprechen.

Eingaben:
- Konkretes Bonus-/Skonto-/Rabatt-Modell.
- Lieferantenkonditionen Grosshandel (Skonto-Anteil über üblicher Höhe?).
- Geschäftsbeziehung zu Arzt/Praxis (Mietverhältnis, Räumlichkeiten, Beratungsverträge).
- Werbemittel, Web-Auftritt, Patientenflyer.

## Rechtlicher Rahmen

- **§ 78 AMG i.V.m. AMPreisV:** Preisbindung Rx.
- **§ 7 HWG:** Werbeverbot Zuwendungen — geringwertige Aufmerksamkeiten erlaubt (Wertgrenze in Rspr. um 1 Euro umstritten).
- **§ 11 ApoG:** Zuweisungsverbot — Apotheker dürfen mit Ärzten keine Vereinbarungen zur Patientenzuweisung treffen.
- **§ 31 BO-Ä, § 17 BO-Apo:** Berufsordnung — Verbot Korruption.
- **§§ 299a, 299b StGB:** Bestechlichkeit und Bestechung im Gesundheitswesen.
- **§ 3a UWG:** Verstoss gegen Marktverhaltensregel.
- BGH 14.03.2024, "Skonti im Grosshandel" — Grosshandelszuschlag und Skonti-Höhe (vom Anwender Aktualität zu verifizieren).
- BGH staend. Rspr. zu Boni und Treuepunkten.

## / Schritt für Schritt

1. **Geplante Aktion klassifizieren:**
 - Skonto vom Grosshandel auf HAP — wirtschaftlich, aber Höhe regulierungsrelevant.
 - Bonus an Patient bei Rx — preisbindungsrelevant (siehe AMPreisV).
 - Bonus an Patient bei OTC — zulässig, HWG-Geringwertigkeit beachten.
 - Zuweisungsvereinbarung mit Arzt — generell unzulässig.
2. **Wertgrenze prüfen:** § 7 HWG-Geringwertigkeit — laut Rspr. 1 Euro pro Aktion / pauschal ggf. höher.
3. **Wettbewerbsrechtliche Würdigung:** § 3a UWG i.V.m. AMPreisV, HWG, ApoG.
4. **Strafrechtliche Würdigung:** §§ 299a, 299b StGB — Vorteilsannahme/-gewährung im Verhältnis Apotheker:in zu Arzt/Klinik/Heim.
5. **Vertragsdokumentation:** Schriftliche Verträge mit Marktüblichkeit, ohne Patientenzuweisung.
6. **Werbeprüfung:** Anpassung HWG-konform.

## Trade-off-Matrix

| Aktion | Zulässig | Konflikt | Rspr.-Lage |
|---|---|---|---|
| Patient erhält 1 Euro Gutschein für OTC-Folgekauf | ja (HWG-Geringwertigkeit) | ggf. UWG | Toleranzgrenze |
| Patient erhält 5 Euro Bonus bei E-Rezept-Einlösung (Rx) | nein | AMPreisV | klar unzulässig |
| Grosshandel gewährt 3,15 Prozent Skonto auf HAP | strittig | BGH 2024 | vom Anwender zu verifizieren |
| Arzt erhält Patientenflyer-Gestaltung kostenlos | grenzwertig | § 11 ApoG, § 31 BO-Ä | hoch riskant |
| Apotheke mietet im Ärztehaus | ja, marktüblich | § 11 ApoG bei Umsatzkomponente | strittig |
| Heim erhält "Versorgungspauschale" | je nach Gestaltung | § 11 ApoG, BO | hoch riskant |

## Praxistipps

- Schriftliche Verträge mit klarer Leistung-Gegenleistung-Struktur, ohne Umsatz- oder Verschreibungskomponente.
- Marktüblichkeit dokumentieren (Vergleichsangebote einholen).
- Werbeauftritt rotweiss prüfen lassen — bei Abmahnung kommen schnell Schäden.
- Bei Mietverträgen im Ärztehaus: Festmiete ohne Umsatzbeteiligung, marktüblich; nicht 0 Euro Miete als verdeckte Zuweisung.
- Heimversorgung: Versorgungsvertrag § 12a ApoG separat regeln (siehe `heimversorgung-versorgungsvertrag`).

## Mustertexte

### Internes Memo zur Aktion (Auszug)
"Die geplante Aktion 'Bonus 2 Euro für jede E-Rezept-Einlösung' wurde geprüft. Ergebnis: Bei Rx-Arzneimitteln verstösst die Bonusgewährung gegen § 78 AMG i.V.m. AMPreisV (Endpreisbindung) und § 7 HWG (Zuwendungsverbot). Empfehlung: Aktion ausschliesslich auf apothekenpflichtige OTC und apothekenübliche Waren beschränken; Bonus pro Einkauf maximal 1 Euro im Sinne der HWG-Geringwertigkeit. Bei Rx: Beratungsmehrwerte und kostenfreie Patientenseminare anstelle finanzieller Vorteile."

### Unterlassungserklärung zu Patientenzuweisung (Auszug)
"Ich erkläre, dass die Apotheke keine Vereinbarung mit der Praxis Dr. [Arzt] über die Zuweisung von Patienten getroffen hat und nicht treffen wird. Insbesondere bestehen keine Zahlungen, Sachzuwendungen, Beratungsverträge oder Mietnachlässe zugunsten der Praxis im Zusammenhang mit der Verschreibung von Arzneimitteln, die in unserer Apotheke eingelöst werden. § 11 ApoG, § 31 BO-Ä und §§ 299a/b StGB sind beachtet."

## Typische Fehler

- "Wir geben einen Gutschein für die nächste Bestellung" — bei Rx unzulässig.
- Treuepunktesystem ohne klare Trennung Rx/OTC.
- Mietvertrag mit "Mietzins entsprechend Apothekenumsatz" — verdeckte Zuweisung.
- Arzt-Gewinnbeteiligungsklausel im Praxismiete-Subvertrag.
- Grosshandel-Skonto über üblicher Grenze als "Werbemassnahme" — Steuerproblem zusätzlich.
- Heim erhält "Beratungspauschale" ohne tatsächliche Leistung — § 299a/b StGB-Verdacht.

## Querverweise

- `preisbindung-arzneimittel-ampreisv` (Preisbindung)
- `kooperation-arzt-apotheke-antikorruption` (Kooperation)
- `heimversorgung-versorgungsvertrag` (Heimversorgung)
- `onlinewerbung-hwg-apotheken` (HWG-Werbung)
- `mietvertrag-apothekenstandort-konkurrenzschutz` (Miete)
- `owi-strafrisiken-apog-amg-btmg` (Strafrisiko)

## Quellen Stand 06/2026

- AMG § 78; AMPreisV; HWG § 7; ApoG § 11.
- StGB §§ 299a, 299b.
- UWG § 3a.
- BGH 14.03.2024 zu Grosshandel-Skonti (vom Anwender Aktualität zu verifizieren — Detailregelungen, Folge-Rspr.).
- BGH staend. Rspr. zu Patientenboni und Treuepunkten.
- Berufsordnung Apothekerkammer (vom Anwender zu verifizieren).

## 2. `t-rezept-besondere-arzneimittel`

**Fokus:** T-Rezept besondere Arzneimittel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# T-Rezept besondere Arzneimittel

## Fachkern: T-Rezept besondere Arzneimittel
- **Spezialgegenstand:** T-Rezept besondere Arzneimittel. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: T-Rezept besondere Arzneimittel** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `telepharmazie-grenzen-chancen`

**Fokus:** Telepharmazie Grenzen Chancen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Telepharmazie Grenzen Chancen

## Fachkern: Telepharmazie Grenzen Chancen
- **Spezialgegenstand:** Telepharmazie Grenzen Chancen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Telepharmazie Grenzen Chancen** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

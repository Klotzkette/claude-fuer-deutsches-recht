---
name: beschwerdemanagement-patient-blutprodukte
description: "Beschwerdemanagement Patient Blutprodukte: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beschwerdemanagement Patient Blutprodukte

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beschwerdemanagement Patient Blutprodukte** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beschwerdemanagement-patient-kunden` | Beschwerdemanagement Patient Kunden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `blutprodukte-haemophilie-registerpflicht` | Blutprodukte Hämophilie Registerpflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `btm-rezept-betaeubungsmittel-dokumentation` | BtM-Rezept Betäubungsmittel Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Beschwerdemanagement Patient Blutprodukte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beschwerdemanagement-patient-kunden`

**Fokus:** Beschwerdemanagement Patient Kunden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Beschwerdemanagement Patient Kunden

## Fachkern: Beschwerdemanagement Patient Kunden
- **Spezialgegenstand:** Beschwerdemanagement Patient Kunden. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Beschwerdemanagement Patient Kunden** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 2. `blutprodukte-haemophilie-registerpflicht`

**Fokus:** Blutprodukte Hämophilie Registerpflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Blutprodukte Hämophilie Registerpflicht

## Fachkern: Blutprodukte Hämophilie Registerpflicht
- **Spezialgegenstand:** Blutprodukte Hämophilie Registerpflicht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Blutprodukte Hämophilie Registerpflicht** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `btm-rezept-betaeubungsmittel-dokumentation`

**Fokus:** BtM-Rezept Betäubungsmittel Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# BtM-Rezept Betäubungsmittel Dokumentation

## Fachkern: BtM-Rezept Betäubungsmittel Dokumentation
- **Spezialgegenstand:** BtM-Rezept Betäubungsmittel Dokumentation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Annahme, Prüfung, Abgabe, Lagerung und Dokumentation von Betäubungsmitteln in öffentlichen Apotheken. BtM-Recht ist Sonderrecht mit verschärften Formerfordernissen — BtM-Rezept (rosa, dreiteilig) plus BtM-Buch oder elektronische Aufzeichnung sind Pflicht. Verstösse sind strafbewehrt (§§ 29 ff. BtMG, OWi nach § 32 BtMG, § 13 BtMVV).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Abgabe eines BtM-Rezepts mit formalen Auffälligkeiten (Korrektur, fehlende Angabe, Doppelausstellung).
- Inventurdifferenz im BtM-Buch — Aufklärung gegenüber BfArM / Landesaufsicht.
- Beanstandung der BtM-Lagerung (Tresor, Schlüsselsicherheit).
- Strafrechtlicher Vorwurf nach § 29 BtMG oder § 96 AMG.
- Vorbereitung BtM-Revision.

Eingaben:
- Originale BtM-Rezepte (Teil I bleibt in Apotheke).
- BtM-Buch oder elektronisches BtM-Verzeichnis (Bestandsfortschreibung).
- Inventurprotokolle, Differenzdokumentation.
- Bezugsunterlagen vom Grosshandel (BtM-Anforderungsschein).

## Rechtlicher Rahmen

- **BtMG** §§ 1, 3, 13, 29 ff.: Strafvorschriften, Erlaubnispflicht zur Abgabe.
- **BtMVV (Betäubungsmittel-Verschreibungsverordnung)** insb. §§ 8–13: Rezeptanforderungen, Höchstmengen, Vertretungsausstellung, Dokumentation.
- **§ 8 BtMVV:** Pflichtangaben auf BtM-Rezept — Name Arzt + Anschrift + Tel., Datum, Patient, Arzneimittel, Stärke, Menge, Dosierung oder "gemäss schriftlicher Anweisung", Unterschrift.
- **§ 12 BtMVV:** Vertretungsbefugnis, Notfall-Verschreibung ("Notfall-Verschreibung", separates Rezeptformular).
- **§ 13 BtMVV:** Nachweisführung — BtM-Buch oder gleichwertige Aufzeichnungen; jeder Zu- und Abgang.
- **§ 14 BtMVV:** Aufbewahrung — Rezeptteil I drei Jahre, BtM-Belege zehn Jahre (§ 16 BtMG).
- **ApBetrO § 4:** abschliessbarer BtM-Schrank Pflicht.

## / Schritt für Schritt

1. **Rezeptannahme:** Original (kein Fax!), dreifarbig (T1 Apotheke, T2 Krankenkasse, T3 Arzt).
2. **Formalprüfung:** Arztangaben vollständig, BtM-Nummer des Arztes, Patient, Arzneimittelname, Menge in Wort und Ziffer, Dosierungsanweisung oder "Gemäss schriftlicher Anweisung", Unterschrift.
3. **Höchstmenge:** Pro Patient/Arzneimittel siehe Anlage III BtMG; bei Überschreitung Buchstabe "A" durch Arzt.
4. **Geltungsdauer:** Sieben Tage ab Ausstellungsdatum (§ 12 Abs. 1 BtMVV).
5. **Identitätsprüfung:** Bei Abgabe an Dritte Plausibilität dokumentieren.
6. **Dokumentation BtM-Buch:** Zu- und Abgang lückenlos, fortlaufend, mit Bestandssaldo. Korrekturen nur durch Streichung mit Sichtbarmachung des Ursprungseintrags.
7. **Inventur:** Quartalsweise empfohlen, mindestens einmal jährlich. Differenzen sofort an Landesaufsicht und BfArM melden.
8. **Vernichtung Verfall:** Protokollierte Vernichtung mit Zeugen, Meldung an BfArM.

## Trade-off-Matrix

| Konstellation | Variante A: Vollformal | Variante B: Korrekturbedürftig | Variante C: Notfall §12 BtMVV |
|---|---|---|---|
| Vorlage | Original 3-teilig | Original mit Mängel | Notfall-Verschreibung des Arztes |
| Sofortabgabe | ja | nur nach Korrektur durch Arzt | ja, Folgerezept binnen einer Woche |
| Dokumentation | Standard BtM-Buch | + Korrekturvermerk | + Notfall-Protokoll |
| Risiko | gering | mittel (OWi bei falscher Annahme) | mittel (formale Anforderung Folgerezept) |

## Praxistipps

- BtM-Rezepte nach Eingang sofort in BtM-Buch eintragen, **nicht** am Tagesende — Differenzaufklärung sonst nachträglich kaum möglich.
- Personalwechsel: BtM-Verantwortung schriftlich übergeben (Bestandsaufnahme mit Unterschriften).
- Bei Bestelldifferenz vom Grosshandel sofort schriftlich beanstanden; nicht stillschweigend "korrigieren".
- BtM-Tresor: Schlüsselverwahrung dokumentieren, regelmässig Code wechseln.
- Bei Verdacht auf Rezeptfälschung (Korrektur, ungewöhnliche Schrift): nicht abgeben, sondern Arzt anrufen; bei begründetem Verdacht Polizei informieren.

## Mustertexte

### Eintrag BtM-Buch (Beispielzeile)
"[lfd. Nr.] | [Datum] | Zu-/Abgang | [Arzneimittel + Stärke] | Menge | [Arzt/Patient + Rezeptdatum] | Bestand neu | Handzeichen abgebende Person"

### Differenzmeldung an Aufsicht (Auszug)
"Bei der Inventur am [Datum] wurde eine Differenz von [Anzahl] Einheiten [Arzneimittel] festgestellt. Soll-Bestand laut BtM-Buch: [X], Ist-Bestand: [Y]. Mögliche Ursachen wurden geprüft: [Doppeleintrag / Falschverbuchung / Verlust]. Wir bitten um Kenntnisnahme und stehen für Rückfragen zur Verfügung. Hinweis: § 13 BtMG-Meldung wird parallel an BfArM erfolgen."

### Stellungnahme zur Rezeptbeanstandung (Auszug)
"Das BtM-Rezept vom [Datum] des Herrn/Frau Dr. [Arzt] für [Patient] wies eine Korrektur der Mengenangabe von [X] auf [Y] auf. Die Korrektur war nach § 9 Abs. 2 BtMVV durch eigenhändige Unterschrift des Arztes vor Abgabe bestätigt. Die Abgabe wurde im BtM-Buch unter [lfd. Nr.] dokumentiert, Bestandsfortschreibung erfolgte zeitgleich."

## Typische Fehler

- Faxrezept oder Telekopie BtM angenommen — Original zwingend.
- Höchstmenge überschritten ohne "A"-Vermerk des Arztes — fehlende Plausibilitätsprüfung.
- BtM-Buch wird nur einmal wöchentlich nachgetragen — Differenz wird unauffindbar.
- Vertretungsausstellung ohne Vertretungsvermerk — formale Lücke.
- Vernichtung ohne Zeugen und ohne BfArM-Meldung.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (allgemeiner Abgabevorgang)
- `cannabis-medizinalcannabis-abgabe-dokumentation` (Cannabis BtM oder nicht)
- `t-rezept-besondere-arzneimittel` (Thalidomid-Sonderrecht)
- `securpharm-faelschungsschutz` (Verifikation)
- `apothekenrevision-vorbereitung-antwort` (Revisionspraxis)
- `owi-strafrisiken-apog-amg-btmg` (Strafbarkeit)

## Quellen Stand 06/2026

- BtMG, BtMVV, jeweils aktueller Stand im Bundesgesetzblatt.
- BfArM-Bekanntmachungen Bundesopiumstelle (vom Anwender zu verifizieren).
- Anlage III BtMG für Höchstmengen.
- BGH staend. Rspr. zur Apothekerverantwortung bei BtM-Rezeptannahme.
- Landesaufsicht und Apothekerkammer-Merkblätter zur BtM-Revision (vom Anwender zu verifizieren).

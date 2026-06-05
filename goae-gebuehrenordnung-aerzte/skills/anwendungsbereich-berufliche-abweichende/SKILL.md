---
name: anwendungsbereich-berufliche-abweichende
description: "Anwendungsbereich Berufliche Abweichende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anwendungsbereich Berufliche Abweichende

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anwendungsbereich Berufliche Abweichende** im Plugin Goae Gebuehrenordnung Aerzte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `goae-1-anwendungsbereich-berufliche-leistungen` | GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |
| `goae-2-abweichende-vereinbarung-honorarvereinbarung` | GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |
| `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen` | GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |

## Arbeitsweg

Im Plugin Goae Gebuehrenordnung Aerzte gilt für **Anwendungsbereich Berufliche Abweichende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `goae-1-anwendungsbereich-berufliche-leistungen`

**Fokus:** GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 1 Anwendungsbereich berufliche Leistungen

## Fachkern: GOÄ § 1 Anwendungsbereich berufliche Leistungen
- **Spezialgegenstand:** GOÄ § 1 Anwendungsbereich berufliche Leistungen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

§ 1 GOÄ definiert den Anwendungsbereich der Gebührenordnung für Ärzte: Berufliche Leistungen approbierter Ärzte gegenüber Privatpatienten und Selbstzahlern. GKV-Leistungen sind nicht von der GOÄ erfasst (EBM, § 87 SGB V). Abgrenzung: nichtärztliche Leistungen, IGel, Wahlleistungen Krankenhaus, telemedizinische Leistungen — alle haben ihre eigenen Spezialregeln, gehen aber im Grundsatz auf § 1 GOÄ zurück.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Erstellung einer Privatrechnung — Anwendungsbereich vorab klären.
- Streit, ob eine Leistung überhaupt nach GOÄ abrechenbar ist (z. B. IGel, Wahlleistung, Gutachten).
- Mandant ist nicht Privatversicherter, sondern Beihilfeberechtigter, Selbstzahler oder PKV-Patient.
- Honoraranspruch zu einem Auslandsbehandlungsfall.

Eingaben:
- Approbationsstatus der Ärztin/des Arztes.
- Patientenstatus (PKV, Beihilfe, GKV-Privatabrechnung, Selbstzahler, IGel).
- Behandlungsumfang und -gegenstand.
- Behandlungsvertrag (sofern schriftlich).
- ggf. Wahlleistungsvereinbarung.

## Rechtlicher Rahmen

- **§ 1 GOÄ:** Anwendungsbereich — berufliche Leistungen approbierter Ärzte.
- **§ 1 Abs. 1 GOÄ:** Die GOÄ gilt für die Vergütung beruflicher Leistungen approbierter Ärzte, soweit nicht durch Bundesgesetz andere Regelungen bestehen.
- **§ 2 GOÄ:** Abweichende Honorarvereinbarung — eng begrenzt zulässig.
- **§ 87 SGB V:** EBM für GKV-Vertragsärzte.
- **§§ 630a ff. BGB:** Behandlungsvertrag.
- **§ 12 GOÄ:** Fälligkeit und Rechnungspflicht.
- **Berufsordnung der Ärztekammern** (§ 12 MBO-Ä) — Verbot ungerechtfertigt hoher Liquidationen.
- BGH staend. Rspr. zur Abgrenzung Heilbehandlung / Begutachtung / IGel.

## / Schritt für Schritt

1. **Approbation prüfen:** Approbationsurkunde Ärztin/Arzt vorhanden? Ohne Approbation kein GOÄ-Anwendungsbereich (Berufserlaubnis genügt im Einzelfall).
2. **Patientenstatus klären:**
 - PKV-Privatpatient: GOÄ-Anwendung vollumfänglich.
 - Beihilfeberechtigter: GOÄ + Beihilfeverordnung des Dienstherrn (Bund/Land).
 - GKV-Patient mit Privatbehandlung (z. B. IGel): GOÄ-Anwendung mit Hinweispflicht.
 - Selbstzahler: GOÄ-Anwendung.
 - Auslandsbehandlung: GOÄ-Anwendung nach deutschem Recht.
3. **Leistung klassifizieren:**
 - Heilbehandlung im engeren Sinn: GOÄ direkt.
 - Gutachten/Bescheinigung: GOÄ Abschnitt L (Sonderleistungen).
 - Wahlleistung Krankenhaus: GOÄ § 6a + Wahlleistungsvereinbarung.
 - Telemedizin: GOÄ + spezielle GOÄ-Ziffern (vom Anwender zu verifizieren — laufende Anpassungen).
4. **Abweichende Honorarvereinbarung:** § 2 GOÄ — nur in engen Grenzen zulässig.
5. **Schwellenwert/Höchstsatz:** § 5 GOÄ — Bemessung.
6. **Rechnungserstellung:** § 12 GOÄ — Fälligkeit erst nach formgerechter Rechnung.

## Trade-off-Matrix

| Patientenstatus | GOÄ-Anwendung | Besonderheit |
|---|---|---|
| PKV-Vollprivatpatient | direkt | Erstattung nach Tarif |
| Beihilfe-Berechtigter | direkt | Erstattungsgrenze Beihilfe + ggf. PKV |
| GKV mit IGel | nur für IGel | schriftliche Aufklärung Pflicht |
| GKV mit "Privatbehandlung" (Wunsch des Patienten) | direkt für Privatleistung | Hinweispflicht, dass GKV-Anspruch besteht |
| Selbstzahler ohne Versicherung | direkt | besondere Hinweispflicht Kosten |
| Auslandspatient | direkt nach deutschem Recht | Übersetzung Rechnung empfehlenswert |
| Werksarzt mit Anstellungsverhältnis | nicht GOÄ | Arbeitsrechtsvergütung |

## Praxistipps

- IGel-Aufklärung schriftlich, mit Kostenvoranschlag — sonst keine Anspruchsgrundlage gegen Patient.
- Bei "Privatbehandlung" eines GKV-Patienten: schriftliche Erklärung des Patienten verlangen, dass er Privatleistung wünscht und Kostenpflicht akzeptiert.
- Approbationsurkunde im Praxis-Stammbuch ablegen — bei Streit vorzeigbar.
- Bei Auslandspatient Rechnung in deutscher Sprache mit englischer Kurzfassung; Bezahlung in EUR.
- Wahlleistung Krankenhaus: § 17 KHEntgG i.V.m. § 6a GOÄ; Vereinbarung Wahlleistung notwendig.

## Mustertexte

### IGel-Aufklärung (Auszug)
"Sehr geehrte:r [Patient:in], die von Ihnen gewünschte Leistung [Bezeichnung] ist nicht im Leistungskatalog der gesetzlichen Krankenkasse enthalten. Sie wird als Individuelle Gesundheitsleistung (IGel) abgerechnet. Die Vergütung erfolgt nach der Gebührenordnung für Ärzte (GOÄ). Geschätzte Kosten: [EUR brutto]. Bei Mehrbedarf werden Sie vor Durchführung erneut informiert. Bitte bestätigen Sie nachstehend, dass Sie die Privatbehandlung wünschen und die Kosten selbst tragen."

### Klarstellung Rechnung an Patient (Auszug)
"Die berechnete Leistung [Ziffer] erfolgte als berufliche Leistung im Sinne des § 1 GOÄ. Sie sind als [PKV-Patient / Beihilfeberechtigter / Selbstzahler] Schuldner:in der Vergütung. Die Erstattung durch Ihre Versicherung obliegt Ihnen; wir leisten gerne unterstützend Auskunft."

## Typische Fehler

- GOÄ-Rechnung an GKV-Patienten ohne explizite Privatbehandlung — Forderung nicht durchsetzbar.
- IGel ohne schriftliche Aufklärung; § 630c BGB-Aufklärungspflicht verletzt — keine Vergütung.
- Werksarztleistung wird nach GOÄ abgerechnet — Vergütung über Arbeitsvertrag, nicht GOÄ.
- Bei Beihilfe wird Patient als Vollerstatter behandelt — Beihilfegrenze und PKV-Tarif beachten.
- Auslandspatient wird in dortiger Sprache abgerechnet — Verständnisproblem, Anspruchsdurchsetzung erschwert.

## Querverweise

- `goae-2-abweichende-vereinbarung-honorarvereinbarung` (§ 2 GOÄ)
- `goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip` (Leistung)
- `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` (Bemessung)
- `goae-12-faelligkeit-und-rechnungspflicht` (§ 12)
- `igel-aufklaerung-kosteninformation` (IGel-Workflow)
- `wahlleistungsvereinbarung-krankenhaus-goae` (Wahlleistung)
- `auslandsbehandlung-deutsche-goae-anwendung` (Ausland)

## Quellen Stand 06/2026

- GOÄ §§ 1, 2, 5, 12 — Stand zur Berechnung im amtlichen Bundesgesetzblatt prüfen.
- GOÄ-Reform 2024/2025 — vom Anwender zu verifizieren (laufende politische Anpassungen, ggf. neue Gebührenordnung).
- BGB §§ 630a–630h.
- KHEntgG § 17.
- Berufsordnung Ärztekammer (MBO-Ä § 12).
- BGH staend. Rspr. zur GOÄ-Anwendung.
- PKV-Verband — Erstattungsleitlinien (informativ, nicht verbindlich).

## 2. `goae-2-abweichende-vereinbarung-honorarvereinbarung`

**Fokus:** GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung

## Fachkern: GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung
- **Spezialgegenstand:** GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

§ 2 GOÄ erlaubt eine vom Regelfall abweichende Honorarvereinbarung — typischer Anwendungsfall: Steigerungsfaktor über dem Schwellenwert (3,5-fach für persönliche, 2,5-fach für technische, 1,3-fach für Labor). Strikte Formvorgaben: vor Behandlungsbeginn, schriftlich, persönlich vom Patienten unterzeichnet, mit Hinweis auf abweichende Vereinbarung. Verstösse machen die Vereinbarung unwirksam — Erstattung durch PKV oder Beihilfe meist verweigert.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Praxis will Honorarvereinbarung über Schwellenwert hinaus treffen.
- PKV verweigert Erstattung wegen "fehlender Schriftform" der Vereinbarung.
- Patient widerruft Honorarvereinbarung.
- Streit über Wirksamkeit einer mündlichen Absprache.
- Wahlleistungsvereinbarung Krankenhaus + GOÄ-Honorar (Abgrenzung § 6a GOÄ vs. § 2 GOÄ).

Eingaben:
- Bestehende oder geplante Honorarvereinbarung (Vorlage).
- Datum der Behandlung / Unterzeichnung.
- Korrespondenz Patient–PKV.
- ggf. Aufklärungsdokumentation.

## Rechtlicher Rahmen

- **§ 2 GOÄ:** Abweichende Vereinbarung über die Höhe der Vergütung — Schriftform, vor Erbringung, individuelle Vereinbarung; keine standardisierten Klauseln.
- **§ 2 Abs. 1 S. 2 GOÄ:** Mindestinhalt — Bezeichnung Leistung, abweichender Gebührensatz, Hinweis dass Vereinbarung über den Schwellenwert hinausgeht.
- **§ 2 Abs. 2 GOÄ:** Aushang Möglichkeit der abweichenden Vereinbarung in Praxis (vom Anwender Stand zu verifizieren).
- **§ 305c BGB:** Überraschende Klauseln in AGB unwirksam.
- **§§ 305 ff. BGB:** AGB-Kontrolle — Honorarvereinbarung als Individualabrede einzuordnen.
- **§ 5 GOÄ:** Bemessung — Regelfall innerhalb Schwellenwert.
- BGH staend. Rspr. zur Wirksamkeit § 2-Vereinbarungen, insb. Schriftform und vorheriger Abschluss.

## / Schritt für Schritt

1. **Geplanter Steigerungsfaktor:** Über oder unter Schwellenwert (2,3; 1,8; 1,15)?
2. **Falls darüber — § 2 GOÄ-Vereinbarung nötig.**
3. **Form:** Schriftlich, persönlich unterzeichnet — keine elektronische Signatur ohne qualifizierte Signatur des Patienten (vom Anwender zu verifizieren).
4. **Zeitpunkt:** Vor Erbringung der Leistung. Spätere Vereinbarung ist regelmässig unwirksam.
5. **Inhalt:**
 - Konkrete Leistung (Ziffer, Bezeichnung).
 - Steigerungsfaktor und resultierender Betrag.
 - Hinweis "Diese Vereinbarung weicht von den Gebührensätzen der GOÄ ab".
 - Hinweis auf voraussichtliche fehlende Erstattung durch PKV/Beihilfe oberhalb des Schwellenwerts.
6. **Individualität:** Keine Massentechnik — Patient muss konkret zustimmen.
7. **Erstattungsfähigkeit:** PKV/Beihilfe erstatten regelmässig nur bis Schwellenwert ohne Bedingung; Mehrbetrag oft nicht.
8. **Dokumentation:** Original in Patientenakte.

## Trade-off-Matrix

| Fallgruppe | § 2 GOÄ erforderlich | Erstattung | Risiko |
|---|---|---|---|
| Steigerung bis Schwellenwert (2,3) | nein | regelmässig voll | gering |
| Steigerung über Schwellenwert (3,5-fach) | ja, schriftlich | nur bei besonderer Begründung | hoch ohne Vereinbarung |
| Höchstsatz Labor (1,3) überschritten | ja | meist nicht | hoch |
| Wahlleistung Krankenhaus | gesondert § 6a + Wahlvereinbarung | nach Wahlvereinbarung | mittel |
| Wunschleistung (IGel) | gesondert IGel-Aufklärung | nicht durch Kasse | gering bei Doku |
| Auslandsbehandlung | wie inland | nach Tarif | mittel |

## Praxistipps

- Honorarvereinbarung niemals "blanket" — Patient muss verstehen, was er unterschreibt.
- Standardklauseln in Praxis-AGB sind regelmässig unwirksam (§ 305c BGB).
- Faktorenangabe konkret, keine "bis zu"-Formulierung.
- Patient ausdrücklich auf voraussichtliche fehlende PKV-Erstattung hinweisen (§ 630c BGB-Aufklärungspflicht).
- Kopie an Patient aushändigen, Original Praxis.
- Bei Beihilfe-Berechtigten: Beihilfe-Tarif kennt regelmässig nur den Schwellenwert; Mehrbetrag aus eigener Tasche.

## Mustertexte

### Honorarvereinbarung § 2 GOÄ (Auszug)
"Honorarvereinbarung gemäss § 2 GOÄ. Zwischen [Patient, Anschrift, Geb.-Datum] und [Arzt, Anschrift] wird vereinbart: Die in der Anlage 1 aufgeführten Leistungen werden mit einem Gebührensatz von [Faktor], d. h. [EUR] berechnet. Dies weicht von den Regelsätzen der GOÄ ab (Schwellenwert 2,3 für persönliche, 1,8 für technische, 1,15 für Labor). Ich, der/die Patient:in, bin darüber aufgeklärt, dass meine Krankenversicherung diese erhöhte Vergütung ggf. nicht oder nicht vollständig erstattet. Eine Erstattungs- oder Kostenzusage liegt mir nicht vor. Die Vereinbarung ist vor Beginn der Behandlung individuell abgeschlossen. Ort, Datum, Unterschrift Patient:in / Arzt."

### Hinweis an Patient zur PKV-Erstattung (Auszug)
"Bitte beachten Sie: Die im Folgenden vereinbarten Honorare können den von Ihrer privaten Krankenversicherung erstatteten Betrag übersteigen. Wir empfehlen, die Erstattungsfähigkeit vor Behandlungsbeginn bei Ihrer Versicherung anzufragen. Die Differenz tragen Sie selbst."

## Typische Fehler

- Honorarvereinbarung erst nach Behandlung unterschrieben — unwirksam.
- Standardklausel in Praxis-AGB — Massentechnik, unwirksam.
- "Bis zu 3,5-fach"-Formulierung — nicht hinreichend bestimmt.
- Aufklärung über fehlende Erstattung fehlt — § 630c BGB-Verletzung.
- Vereinbarung ohne konkrete Leistungsangabe — unwirksam.
- Patient unterschreibt unter Zeitdruck im Empfang — Anfechtungsrisiko.

## Querverweise

- `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` (Schwellenwert)
- `steigerungssatz-begruendung-individuell-patientenbezogen` (Begründung)
- `begruendung-ueber-schwellenwert-redigieren` (Begründungstexte)
- `gebuehrenrahmen-schwellenwert-ampel` (Ampel)
- `igel-aufklaerung-kosteninformation` (IGel)
- `wahlleistungsvereinbarung-krankenhaus-goae` (Wahlleistung KH)
- `erstattung-pkv-vs-honoraranspruch-patient` (PKV-Erstattung)

## Quellen Stand 06/2026

- GOÄ § 2, § 5, § 6a.
- BGB §§ 305 ff., 630a–630h.
- BGH staend. Rspr. zur Honorarvereinbarung (Schriftform, vorheriger Abschluss, Individualität).
- Berufsordnung Ärztekammer.
- GOÄ-Reform 2024/2025 — vom Anwender Aktualität zu verifizieren.
- PKV-Verband — Hinweise zur Erstattung von Honorarvereinbarungen (informativ).

## 3. `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen`

**Fokus:** GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen

## Fachkern: GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen
- **Spezialgegenstand:** GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen** im Bereich **GOÄ Gebührenordnung für Ärzte**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

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

---
name: ustva
description: Begleitet Unternehmen und Steuerberater bei der korrekten Abgabe von Umsatzsteuer-Voranmeldungen nach § 18 UStG – von der Bestimmung des Voranmeldungszeitraums über Dauerfristverlängerung bis zur Berichtigung. Lädt bei Fragen zur UStVA, ELSTER, Dauerfristverlängerung und Voranmeldungsberichtigung.
language: de
triggers:
  - "Umsatzsteuervoranmeldung"
  - "UStVA"
  - "§ 18 UStG"
  - "Dauerfristverlängerung"
  - "ELSTER Umsatzsteuer"
  - "Voranmeldungszeitraum"
  - "monatliche UStVA"
  - "quartalsweise Voranmeldung"
  - "Berichtigung UStVA"
---

# Umsatzsteuer-Voranmeldung (§ 18 UStG)

## Zweck

Dieser Skill begleitet die fristgerechte und inhaltlich korrekte Abgabe von Umsatzsteuer-Voranmeldungen (UStVA) nach § 18 UStG. Er deckt die Bestimmung des richtigen Voranmeldungszeitraums, die Dauerfristverlängerung nach § 46 UStDV, die Berichtigung nach §§ 153 AO und 17 UStG sowie die technische Abgabe über ELSTER ab. Anwendungsfälle: monatliche oder quartalsweise UStVA erstellen, Dauerfristverlängerung beantragen, versehentlich falsche UStVA berichtigen, Übergang zwischen Voranmeldungszeiträumen.

## Eingaben

Das Modell benötigt:

- **Voranmeldungszeitraum des Mandanten**: monatlich, quartalsweise oder jährlich (Befreiung)?
- **Vorjahres-Zahllast**: Wie hoch war die USt-Zahllast des Vorjahres? (Maßgeblich für Zeitraum-Bestimmung)
- **Aktueller Zeitraum**: Welcher Monat/welches Quartal wird gemeldet?
- **Abzugebende Daten**: Umsätze (Steuersatz, steuerfreie Umsätze), Vorsteuer, innergemeinschaftliche Erwerbe, Reverse Charge?
- **Dauerfristverlängerung**: Beantragt? Sondervorauszahlung bereits entrichtet?
- **Berichtigungsbedarf**: Liegt ein Fehler in einer bereits abgegebenen UStVA vor? Welcher Art (Betrag, Steuersatz, Vorsteuer)?
- **ELSTER-Zugang**: Besteht ein zertifizierter ELSTER-Zugang (Unternehmen)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 18 Abs. 1 UStG**: Pflicht zur Abgabe der UStVA; Voranmeldungszeitraum grundsätzlich das Kalendervierteljahr; bei Jahres-Zahllast > 7.500 EUR: Kalendermonat (§ 18 Abs. 2 Satz 2 UStG); bei Jahres-Zahllast ≤ 1.000 EUR: Finanzamt kann von monatlicher/quartalsweiser Abgabe befreien (§ 18 Abs. 2 Satz 3 UStG).
- **§ 18 Abs. 1 Satz 4 UStG**: Abgabefrist: 10. Tag nach Ablauf des Voranmeldungszeitraums (10. Folgemonat).
- **§ 18 Abs. 2a UStG**: Neugründer: In den ersten zwei Jahren Monatsmeldung, unabhängig von Zahllast.
- **§ 18 Abs. 9 UStG**: Vergütungsverfahren für ausländische Unternehmer.
- **§ 46 UStDV (Dauerfristverlängerung)**: Verlängerung der Abgabe- und Zahlungsfrist um einen Monat auf Antrag; Voraussetzung für Monatszahler: Sondervorauszahlung i.H.v. 1/11 der Jahresvorauszahlung des Vorjahres bis zum 10. Februar des laufenden Jahres (§ 47 Abs. 1 UStDV); Quartalszahler: kein Sondervorauszahlungserfordernis.
- **§ 153 Abs. 1 AO**: Berichtigungspflicht bei erkanntem Fehler in einer Steuererklärung/-anmeldung; unverzügliche Anzeige beim Finanzamt, kein Verschulden erforderlich; Berichtigung = Selbstanzeige i.S.d. § 371 AO bei vorsätzlicher Verkürzung (Abgrenzung!).
- **§ 17 UStG**: Berichtigung des Steuerbetrags bei nachträglicher Änderung der Bemessungsgrundlage (z.B. Entgeltminderung, Rechnungskorrektur, Uneinbringlichkeit).

### Leitentscheidungen

1. BFH, Urt. v. 24.10.2019 – V R 17/19, BStBl. II 2020, 158 Rn. 22–35: Zur Berichtigungspflicht nach § 153 AO im Umsatzsteuerrecht; der BFH stellt klar, dass nachträglich erkannte Fehler in UStVAs unverzüglich zu berichtigen sind; eine Berichtigung ist keine Selbstanzeige, wenn kein Vorsatz zur Steuerverkürzung vorlag. Maßgeblich für Abgrenzung zwischen § 153 AO und § 371 AO.

2. BFH, Beschl. v. 16.12.2014 – X B 113/14, BFH/NV 2015, 569 Rn. 10–18: Zur Dauerfristverlängerung; der BFH bestätigt, dass die Sondervorauszahlung nach § 47 UStDV rechtmäßige Voraussetzung der Fristverlängerung ist und bei Nichtleistung die Dauerfristverlängerung nicht wirksam ist – Säumnis der regulären Frist folgt.

### Kommentarliteratur

1. Stadie, in: Rau/Dürrwächter, Umsatzsteuergesetz, 183. Lfg. (Stand 04.2024), § 18 UStG Rn. 50–120: Zur systematischen Darstellung der Voranmeldungspflichten; Voranmeldungszeitraum nach Zahllast-Schwellen; Neugründer-Regelung; Abgrenzung der Zeiträume bei unterjährigem Jahreswechsel; ELSTER-Pflicht.

2. Heuermann, in: Sölch/Ringleb, UStG, 96. Lfg. (Stand 02.2025), § 18 UStG Rn. 30–85: Zu Abgabefristen und deren Berechnung; Dauerfristverlängerung und Sondervorauszahlung im Einzelnen; Verhältnis von § 18 UStG zu § 153 AO bei Berichtigungen; Folgen verspäteter Abgabe (Verspätungszuschlag § 152 AO, Schätzung § 162 AO).

## Ablauf

**Schritt 1 – Voranmeldungszeitraum bestimmen**
- Vorjahres-Zahllast ≤ 1.000 EUR: Befreiung möglich (§ 18 Abs. 2 Satz 3 UStG); Finanzamt entscheidet.
- Vorjahres-Zahllast > 1.000 EUR und ≤ 7.500 EUR: Quartalsmeldung (§ 18 Abs. 2 Satz 1 UStG).
- Vorjahres-Zahllast > 7.500 EUR: Monatsmeldung (§ 18 Abs. 2 Satz 2 UStG).
- Neugründer: erste zwei Kalenderjahre stets monatlich (§ 18 Abs. 2a UStG).

**Schritt 2 – Abgabefrist ermitteln**
- Regulär: 10. Tag nach Ablauf des Voranmeldungszeitraums (§ 18 Abs. 1 Satz 4 UStG).
- Beispiel: Januar-UStVA → Abgabe bis 10. Februar.
- Dauerfristverlängerung (§ 46 UStDV): Frist verschiebt sich um einen Monat (Januar → 10. März).
- Samstag/Sonntag/Feiertag: nächster Werktag (§ 108 Abs. 3 AO).

**Schritt 3 – Dauerfristverlängerung beantragen/sichern (§ 46 UStDV)**
- Antrag über ELSTER (Formular „Antrag auf Dauerfristverlängerung/Anmeldung der Sondervorauszahlung").
- Monatszahler: Sondervorauszahlung bis 10. Februar des Jahres entrichten (1/11 der Vorjahres-Zahllast).
- Quartalszahler: Antrag genügt, keine Sondervorauszahlung erforderlich.
- Sondervorauszahlung wird in der Dezember-UStVA/Jahreserklärung angerechnet.

**Schritt 4 – UStVA erstellen und abgeben**
- Ausfüllen über ELSTER (Pflicht zur elektronischen Abgabe, § 18 Abs. 1 Satz 1 UStG i.V.m. § 87a AO).
- Kennzahlen (KZ) korrekt zuordnen: KZ 81 (19 % USt), KZ 86 (7 % USt), KZ 66 (Vorsteuer), KZ 21 (ig Erwerbe), KZ 52 (Reverse Charge).
- Zahlungseingang beim Finanzamt spätestens am Fälligkeitstag (nicht nur Abgabe der Meldung).

**Schritt 5 – Berichtigung einer fehlerhaften UStVA**
- § 153 AO: Erkannter Fehler → unverzügliche Berichtigung, bevor der Fehler dem Finanzamt auffällt.
- Vorgehen: Korrigierte UStVA über ELSTER für den betreffenden Zeitraum einreichen (ersetzt vorherige Anmeldung).
- Abgrenzung § 371 AO: Berichtigung nur als Selbstanzeige wirksam, wenn der Fehler auf Vorsatz zur Steuerverkürzung zurückgeht; bloß fahrlässige Fehler = § 153 AO, keine Selbstanzeige erforderlich.
- § 17 UStG: Bei Änderung der Bemessungsgrundlage (Storno, Rechnungskorrektur, Skonto) Berichtigung in dem UStVA-Zeitraum, in dem die Änderung eingetreten ist (nicht rückwirkend).

**Schritt 6 – Folgen verspäteter oder fehlerhafter Abgabe**
- Verspätungszuschlag: bis zu 10 % der Steuer, max. 25.000 EUR (§ 152 AO); Ermessen des Finanzamts.
- Schätzung: Finanzamt kann Besteuerungsgrundlagen schätzen (§ 162 AO).
- Säumniszuschlag auf verspätete Zahlung: 1 % pro angefangenem Monat (§ 240 AO).

## Ausgabeformat

- **Fristenübersicht** (Tabelle): Voranmeldungszeitraum × Reguläre Frist × Frist mit Dauerfristverlängerung.
- **Checkliste UStVA-Erstellung**: Kennzahlen-Mapping für häufige Geschäftsvorfälle.
- **Berichtigungsanleitung** (Schritt-für-Schritt via ELSTER).
- **Dauerfristverlängerungs-Memo**: Voraussetzungen, Sondervorauszahlungshöhe, ELSTER-Pfad.

## Beispiel

**Sachverhalt**: GmbH G hatte im Jahr 2024 eine USt-Zahllast von 14.000 EUR. G hat keine Dauerfristverlängerung beantragt. Die Januar-2025-UStVA enthält einen Vorsteuerfehler (KZ 66 um 1.200 EUR zu hoch), den G am 15.03.2025 erkennt.

**Gutachtenstil**:

*Voranmeldungszeitraum*: Jahres-Zahllast 2024 = 14.000 EUR > 7.500 EUR → G ist zur monatlichen Voranmeldung verpflichtet (§ 18 Abs. 2 Satz 2 UStG).

*Abgabefrist Januar*: Ohne Dauerfristverlängerung: 10. Februar 2025 (§ 18 Abs. 1 Satz 4 UStG). Frist bereits abgelaufen.

*Berichtigung*: G hat am 15.03.2025 den Fehler erkannt. Berichtigungspflicht nach § 153 Abs. 1 AO besteht; da kein Vorsatz zur Steuerverkürzung vorliegt, ist eine reine Berichtigung (keine Selbstanzeige) ausreichend (BFH, Urt. v. 24.10.2019 – V R 17/19, BStBl. II 2020, 158 Rn. 28). Korrigierte UStVA für Januar ist unverzüglich über ELSTER einzureichen; die sich ergebende Nachzahlung (1.200 EUR × Steuersatz) ist sofort fällig zzgl. Säumniszuschlag (§ 240 AO).

*Dauerfristverlängerung für Zukunft*: G sollte für 2025 Dauerfristverlängerung beantragen (§ 46 UStDV); Sondervorauszahlung = 14.000/11 = 1.272,73 EUR (fällig bis 10.02.2025 – für 2025 ist Frist versäumt; ab 2026 beantragen).

## Risiken und typische Fehler

- **Voranmeldungszeitraum falsch**: Bei Überschreiten der 7.500-EUR-Schwelle im Vorjahr automatischer Wechsel zu monatlicher Meldepflicht – kein gesonderter Bescheid; viele Unternehmen erkennen den Wechsel nicht rechtzeitig.
- **Dauerfristverlängerung ohne Sondervorauszahlung**: Monatszahler, die keine Sondervorauszahlung leisten, haben keine wirksame Dauerfristverlängerung (BFH BFH/NV 2015, 569 Rn. 14); reguläre Frist gilt.
- **§ 153 AO vs. § 371 AO verwechseln**: Irrtümliche Behandlung als Selbstanzeige bei bloß fahrlässigen Fehlern ist unnötig; umgekehrt: bei Vorsatz reicht § 153 AO nicht.
- **§ 17 UStG-Berichtigungszeitpunkt**: Berichtigung bei Änderung der Bemessungsgrundlage gehört in den Zeitraum des Änderungsereignisses, nicht in den Ursprungszeitraum.
- **ELSTER-Pflicht**: Papieranmeldungen sind grundsätzlich nicht zulässig; nur in Härtefällen nach § 150 Abs. 8 AO ausnahmsweise möglich.
- **Zahlung ≠ Abgabe**: Fristwahrung erfordert sowohl rechtzeitige Abgabe der Meldung als auch rechtzeitigen Zahlungseingang beim Finanzamt (§ 18 Abs. 1 Satz 4 UStG).

## Quellenpflicht

Alle Aussagen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rspr.-Belege im BGH-Stil (BFH BStBl. II 2020, 158; BFH/NV 2015, 569) und zwei Kommentarbelege im Bearbeiter-Stil. Änderungen durch Jahressteuergesetze sind am aktuellen Kommentarstand zu überprüfen; bei neueren Rechtsfragen ohne gesicherte BFH-Rspr. ausdrücklich kennzeichnen.

---
name: prognose-stichtag-stundungsanfrage-glaeubiger
description: "Prognose Stichtag Stundungsanfrage Glaeubiger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Prognose Stichtag Stundungsanfrage Glaeubiger

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Prognose Stichtag Stundungsanfrage Glaeubiger** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Geschäftsleiter dass er aktiv geprüft hat (Haftung § 15b InsO § 43 GmbHG) und gegenüber Gläubigern Banken Patron Steuerberater. Wiedervorlage zur Aktualisierung vierteljaehrlich oder bei wesentlicher Aenderung. |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheitsangebot. Pro Gläubiger eigenes Schreiben. Hinweis Steuerstundung § 222 AO (restriktiv) und Sozialversicherung (sehr restriktiv § 76 SGB IV). Schriftliche Stundungszusage erforderlich für Berücksichtigung in der Liquiditaetsplanung. |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Personal) und Risikokategorisierung. Plausibilitaetsband für jede Annahme. Erzeugt Plausibilitaetsprotokoll. Annahmen mit niedriger Belastbarkeit werden als Modellannahme markiert und im Sensitivitaetsszenario gegengerechnet. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **Prognose Stichtag Stundungsanfrage Glaeubiger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `prognose-dokumentation-stichtag`

**Fokus:** Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Geschäftsleiter dass er aktiv geprüft hat (Haftung § 15b InsO § 43 GmbHG) und gegenüber Gläubigern Banken Patron Steuerberater. Wiedervorlage zur Aktualisierung vierteljaehrlich oder bei wesentlicher Aenderung.

# Prognose-Dokumentation Stichtag

## Zweck

Die Fortbestehensprognose ist Beweisstück. Bei späterer Insolvenz wird genau geprüft ob der Geschäftsleiter zum Stichtag der Erstellung **objektiv** eine positive Prognose annehmen durfte. Diese Dokumentation muss als Beweis dienen können.

## Pflichtinhalte

Die Dokumentation enthält:

1. **Stichtag** und Anlass
2. **Bilanzieller Status** zum Stichtag mit Aktiva Passiva Eigenkapital Stillen Reserven Stillen Lasten Rangrücktritt
3. **Insolvenzrechtliche Bilanzbasis** mit Rechnung
4. **Annahmen** im Einzelnen mit Belegen und Plausibilisierung
5. **12-Monats-Liquidität** in Szenarien Basis Negativ Stress
6. **Sanierungsbausteine** mit Status (verbindlich umgesetzt / in Verhandlung / geplant)
7. **Gesamtergebnis** mit Begründung
8. **Wiedervorlage-Termin**

## Dokumenten-Vorlage

```
FORTBESTEHENSPROGNOSE
nach § 19 Abs. 2 InsO

Gesellschaft: [Firma]
HRB: [Nummer], AG [Sitz]
Rechtsform: [GmbH / AG]

Stichtag der Prognose: [Datum]
Erstellt durch: [Geschäftsführer Name]
Prognosehorizont: [Monat plus zwölf Monate]

1. ANLASS

[Aus Skill ausloesendes-ereignis-erfassen — z. B. "Hinweis des Steuerberaters
nach § 102 StaRUG vom [Datum] mit dem Hinweis dass die Bilanz 2025 ein
negatives Eigenkapital von [Betrag] EUR aufweist und eine Fortbestehensprognose
nach § 19 Abs. 2 InsO erstellt werden soll."]

2. BILANZIELLER STATUS

[Aus Skill bilanzieller-status-aufnehmen — als knappe Tabelle mit
Aktiva-Passiva und ausweisbarer bilanzieller Überschuldung.]

3. STILLE RESERVEN UND LASTEN

[Stille Reserven mit Bewertung. Stille Lasten gegengerechnet.]

4. RANGRUECKTRITTE

[Forderungen mit qualifiziertem Rangrücktritt nach § 19 Abs. 2 S. 2 InsO.]

5. INSOLVENZRECHTLICHE BILANZBASIS

[Berechnung Aktiva plus Stille Reserven minus Stille Lasten gegen Passiva
minus Rangrücktritts-Forderungen.]

Ergebnis bilanzielle Prüfung: [positiv / negativ]
Höhe: [Betrag] EUR

6. ANNAHMEN FUER DIE FORTFUEHRUNG

[Aus Skill annahmen-sammeln-fortfuehrung. Pro Annahme:
Bezeichnung — Werte — Begründung — Beleg — Risiko.]

7. PLAUSIBILISIERUNG DER ANNAHMEN

[Aus Skill annahmen-belastbarkeit-plausibilisieren. Pro Annahme:
Band (realistisch / konservativ / ambitioniert / nicht-belastbar) —
Sensitivitaetsszenario.]

8. LIQUIDITAET ZWOELF MONATE

Basis-Szenario: [positiv / negativ / knapp positiv]
Negativ-Szenario: [...]
Stress-Szenario: [...]

[Tabelle mit Monatsendbestaenden je Szenario.]

9. SANIERUNGSBAUSTEINE

[Aus Skill sanierungsbausteine-vorschlagen.
Pro Baustein: Bezeichnung — Höhe — Umsetzungsstatus — Beleg.]

 - Patronatserklärung Hauptgesellschafter 200000 EUR — unterzeichnet
 am [Datum] — Anlage A1
 - Gesellschafterdarlehen 120000 EUR mit qualifiziertem Rangrücktritt —
 notariell beurkundet am [Datum] — Anlage A2
 - Stundungsvereinbarungen 5 Lieferanten — schriftlich vorhanden am
 [Datum] — Anlagen A3 bis A7

10. GESAMTBEWERTUNG

Maßstab: § 19 Abs. 2 InsO — überwiegend wahrscheinlich (mehr als 50 Prozent)
dass das Unternehmen im Prognosezeitraum von zwölf Monaten zahlungsfähig
fortgeführt werden kann.

Ergebnis: [POSITIV / POSITIV MIT MASSNAHMEN / NEGATIV]

Begründung:

[Konkrete Begründung in zwei bis fünf Sätzen. Bei "positiv mit Maßnahmen"
explizit aufzählen welche Maßnahmen umgesetzt sein müssen.]

Folge: [Keine Antragspflicht aus Überschuldung / Antragspflicht ausgeloest]

11. WIEDERVORLAGE

Diese Prognose ist zu aktualisieren:

 - vierteljaehrlich zum [nächster Stichtag]
 - bei jeder wesentlichen Änderung der Annahmen
 - bei Eintritt eines der negativen Ereignisse aus dem Stress-Szenario

12. ABSCHLIESSENDE ERKLAERUNG DES GESCHAEFTSFUEHRERS

Ich erklaere dass ich die obigen Annahmen sorgfaeltig geprüft und mit den
verfügbaren Informationen abgeglichen habe. Die Annahmen entsprechen meiner
objektiven Einschätzung zum Stichtag. Bei wesentlichen Änderungen werde ich
diese Prognose unverzueglich aktualisieren.

[Ort], [Datum]

___________________________
[Geschäftsführer]


ANLAGEN

 A1 Patronatserklärung Hauptgesellschafter
 A2 Gesellschafterdarlehen mit Rangrücktritt notariell
 A3 bis A7 Stundungsvereinbarungen
 A8 Liquiditätsplan 12 Monate (Excel)
 A9 Aktueller BWA SuSa
 A10 Hinweisschreiben Steuerberater § 102 StaRUG
 A11 Bilanz 2025 mit Anhang
```

## Aufbewahrung

- Original mit allen Anlagen in der Geschäftsleitungsakte.
- Kopie an Steuerberater und Insolvenzanwalt (falls eingebunden).
- Aufbewahrung mindestens **zehn Jahre** (Anlehnung an § 257 HGB Buchführungspflicht und ggf. § 147 AO).

## Bei späterer Insolvenz

Diese Dokumentation ist Beweis dass der Geschäftsleiter zum Stichtag eine **objektive** Prognose erstellt hat. Sie schuetzt im Haftungsprozess gegen Vorwuerfe:

- **§ 15a Abs. 4 InsO** Insolvenzverschleppung — wenn die Prognose zum Stichtag positiv war kann nicht angenommen werden dass der Geschäftsleiter den Insolvenzgrund kannte und ignorierte.
- **§ 15b InsO** Zahlungsverbot — wenn der Status zum Stichtag nicht-negativ war waren Zahlungen ab diesem Tag nicht zwingend pflichtwidrig.
- **§ 43 GmbHG** Sorgfaltspflicht — Dokumentation belegt dass der Geschäftsleiter aktiv und mit Sorgfalt geprüft hat.
- **§ 826 BGB** sittenwidrige Schädigung der Gläubiger — nicht erfüllt wenn objektive Prognose vorlag.

## Bei aktualisierter Prognose

Wenn die Prognose vierteljaehrlich aktualisiert wird, alte Prognosen aufheben und mit Stichtag-Vermerk archivieren. Die aktuelle Version bleibt federführend.

## Ausgabe

- `fortbestehensprognose-<datum>.docx` und PDF mit allen Anlagen.
- Sicherer Archivpfad: `fortbestehensprognose/protokolle/<stichtag>.zip` mit Anlagenkonvolut.
- Wiedervorlage-Eintrag im Kalender vierteljaehrlich.
- Bei "negativ" Eskalation an Insolvenzanwalt (Skill `wenn-prognose-negativ-naechste-schritte`).


## Aktuelle Leitentscheidungen — Dokumentation der Prognose (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater haftet bei verfehlter FBP; Dokumentation der Hinweise und der angenommenen Prognoseannahmen ist Pflicht. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung des Beratungsmandats; Dokumentation muss erkennbar machen, dass auch GF angesprochen ist. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Wissentlichkeitsausschluss; lückenlose Dokumentation des Prognose-Prozesses ist entscheidend für die Verteidigung gegen "positive Kenntnis"-Vorwurf.

## Paragrafenkette Dokumentation

§ 15b Abs. 1 InsO (Zahlungsverbot nach Insolvenzreife) → § 43 Abs. 1 GmbHG (Sorgfaltspflicht) → § 93 AktG (Vorstandshaftung) → IDW S 11 (Dokumentationsstandard) → GOBD (Aufbewahrungspflichten digitaler Dokumente)

## Triage — Dokumentations-Checkliste

1. **Stichtag festlegen?** Datum und Uhrzeit der Erstellung dokumentieren.
2. **Unterzeichnung?** Geschaeftsfuehrer unterschreibt Prognose (Beweisstueck bei spaeterer Haftungsfrage).
3. **Anlagen?** Alle Berechnungs-Spreadsheets, Auszuege, IDW S 11-Gutachten als Anlagen beifuegen.
4. **Wiedervorlage?** Naechste Aktualisierung terminieren (spaetestens nach 3 Monaten oder bei wesentlichen Aenderungen).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `stundungsanfrage-glaeubiger`

**Fokus:** Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheitsangebot. Pro Gläubiger eigenes Schreiben. Hinweis Steuerstundung § 222 AO (restriktiv) und Sozialversicherung (sehr restriktiv § 76 SGB IV). Schriftliche Stundungszusage erforderlich für Berücksichtigung in der Liquiditaetsplanung.

# Stundungsanfrage Gläubiger

## Wirkung in der Liquiditätsplanung

Eine Stundung verschiebt die Fälligkeit eines Liquiditätsabflusses nach hinten oder verteilt ihn in Raten. Wirkung:

- **Verbessert** die Liquidität im Stundungszeitraum.
- **Verschlechtert** die Liquidität im Folgezeitraum (es sei denn umgekehrt durch operativ erwirtschaftete Mittel kompensiert).
- **Nur schriftlich** im Liquiditätsplan ansetzen.

Eine muendlich erbetene und nicht schriftlich zugestandene Stundung darf nicht in den Liquiditätsplan eingebaut werden.

## Kategorien der Gläubiger

### 1. Lieferanten

- Regelmäßig **bilateral verhandelbar**.
- Beziehungs-Vorteil: Lieferanten haben Interesse an Fortführung des Kunden.
- Empfehlung: schriftliche Stundungsanfrage mit konkretem Verzugsplan und ggf. **Teilzahlung als Goodwill-Geste**.

### 2. Bank

- Bei bestehenden Darlehen Tilgungspause oder Verlängerung.
- Bei Kreditlinie Erhöhung oder Verlängerung.
- Bank verlangt regelmäßig **Sanierungskonzept** (IDW S 6) oder zumindest die Fortbestehensprognose.
- Verhandlung erfordert Bankgespräch — schriftliche Stundungszusage ggf. erst nach Prüfung.

### 3. Vermieter

- Verhandlung möglich. Mietkündigung gemäß BGB § 543 wegen Zahlungsverzug nicht stundungsfähig — Verzug muss vermieden werden.
- Schriftliche Stundungszusage erforderlich.

### 4. Steueramt (§ 222 AO)

- **Erhebliche Härte** muss vorliegen (§ 222 S. 1 AO).
- Stundung ist **Ermessensentscheidung** der Finanzbehörde.
- Bei drohender Insolvenz oft restriktiv.
- Sicherheitsleistung verlangt (§ 222 S. 2 AO).
- Hinweis: Lohnsteuer kann **nicht** gestundet werden (§ 222 S. 3 AO i.V.m. § 41a EStG).

### 5. Sozialversicherungsträger (§ 76 Abs. 2 SGB IV)

- **Sehr restriktiv** — nur in Ausnahmefällen.
- Sozialversicherungsbeitraege sind treuhaenderisch und Arbeitnehmer-Anteil.
- Nichtabführung kann § 266a StGB auslösen (Vorenthalten Sozialversicherungsbeitraege Arbeitnehmer-Anteil).
- **Pflicht zur Abführung** der Arbeitnehmer-Beitraege bleibt grundsaetzlich auch bei Stundung — daher Stundung praktisch fast unwirksam.

## Mustervorlage Lieferant

```
[Briefkopf der Gesellschaft]

[Datum]

An [Lieferant]
[Anschrift]

Betreff: Stundungsanfrage Rechnungen Nr. [...] vom [...]

Sehr geehrte Damen und Herren,

mit Bezug auf die offenen Rechnungen

 Rechnung Nr. [...] vom [...] in Höhe von [...] EUR (fällig [...])
 Rechnung Nr. [...] vom [...] in Höhe von [...] EUR (fällig [...])
 Gesamt offene Forderung: [...] EUR

bitten wir Sie um Stundung wie folgt:

 - Fälligkeit verschoben auf [neues Datum]
 - alternativ Ratenzahlung in [N] gleichen Monatsraten ab [Datum]
 - Erste Rate in Höhe von [...] EUR überweisen wir bereits am [...]

Hintergrund: Unsere Gesellschaft befindet sich in einer angespannten
wirtschaftlichen Phase die wir aktiv durch Maßnahmen (Standortoptimierung
Patronatserklärung des Hauptgesellschafters Erhöhung der Kreditlinie)
gegensteuern. Eine vollständige Fortbestehensprognose nach § 19 Abs. 2 InsO
liegt unserer Geschäftsführung vor; sie weist mit Maßnahmen positive
Wahrscheinlichkeit aus.

Wir versichern Ihnen dass die Lieferung und Zahlung in der Geschäftsbeziehung
absolute Prioritaet hat. Unsere Beziehung zu Ihnen ist langfristig und wir
sehen unsere Verpflichtung gegenüber Ihnen ausserordentlich.

Eine schriftliche Bestätigung der Stundung erbitten wir bis zum [Datum].

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Mustervorlage Bank

```
[Briefkopf der Gesellschaft]

[Datum]

An [Bank]
[Anschrift]

Betreff: Antrag auf Tilgungspause Darlehen Nr. [...] / Verlängerung
 Kreditlinie

Sehr geehrte Damen und Herren,

mit Verweis auf unsere bestehende Geschäftsbeziehung beantragen wir:

1. Tilgungspause für das Darlehen Nr. [...] in Höhe von [...] EUR für einen
Zeitraum von [...] Monaten (von [...] bis [...]).

2. Verlängerung der Kreditlinie (Linie [...] EUR) bis zum [...].

Hintergrund: Unsere Gesellschaft befindet sich in einer wirtschaftlich
angespannten Phase die wir aktiv durch Maßnahmen gegensteuern. Eine
Fortbestehensprognose nach § 19 Abs. 2 InsO liegt vor und weist mit unseren
laufenden Sanierungsmaßnahmen einschließlich Patronatserklärung des
Hauptgesellschafters in Höhe von [...] EUR positive Wahrscheinlichkeit auf
die Fortfuehrung im Prognosezeitraum von zwölf Monaten.

Wir übersenden Ihnen vorab:

 - Fortbestehensprognose mit Stichtag [...]
 - Patronatserklärung des Hauptgesellschafters vom [...]
 - 12-Monats-Liquiditätsplan einschließlich Sensitivitaetsszenarien

Für ein persoenliches Gespraech sind wir gerne kurzfristig verfügbar.

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Mustervorlage Steueramt (§ 222 AO)

```
[Briefkopf der Gesellschaft]

[Datum]

An das Finanzamt [...]
[Anschrift]

Steuernummer: [...]

Betreff: Antrag auf Stundung gemäß § 222 AO

Sehr geehrte Damen und Herren,

namens und im Auftrag der oben genannten Gesellschaft beantragen wir gemäß
§ 222 AO Stundung der nachstehenden Steuern:

 Koerperschaftsteuer Vorauszahlung Q2/2026, fällig [...]: [...] EUR
 Solidaritaetszuschlag, fällig [...]: [...] EUR
 Gewerbesteuer Vorauszahlung Q2/2026, fällig [...]: [...] EUR

bis zum [neues Datum] beziehungsweise alternativ Ratenzahlung in
[N] Monatsraten ab [...].

Begründung: Die Erhebung der Steuer in der gesetzten Frist würde eine
erhebliche Haerte für die Steuerpflichtige bedeuten. Ihre wirtschaftliche
Lage ist angespannt; eine Fortbestehensprognose mit positiver Wahrscheinlichkeit
ist erstellt. Die laufenden Verhandlungen mit Patronen und Kreditgebern
zeigen positive Entwicklung; mit Vollzug der Sanierungsbausteine ist die
fristgerechte Zahlung gesichert.

Über Sicherheitsleistung ($ 222 S. 2 AO) sind wir gerne im Gespraech
(z. B. Bürgschaft des Patrons Sicherungsuebereignung Maschinen).

Auf Verlangen reichen wir Folgendes nach:

 - Fortbestehensprognose mit Stichtag [...]
 - Aktueller Liquiditätsplan
 - Patronatserklärung des Hauptgesellschafters

Lohnsteuer und Umsatzsteuer (Treuhand-Steuern) sind hiervon ausdrücklich nicht
betroffen. Diese werden weiterhin fristgerecht abgeführt.

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Schriftliche Stundungszusage

Erst nach **schriftlicher** Stundungszusage des Gläubigers darf die Fälligkeit im Liquiditätsplan verschoben werden.

```yaml
stundungen:
 - glaeubiger: Lieferant XYZ GmbH
 offene-forderung: 24000
 urspruengliche-faelligkeit: 2026-06-15
 gestundete-faelligkeit: 2026-09-15
 zusage-vom: 2026-06-05
 zusage-form: E-Mail mit Bestätigung
 bemerkung: Anzahlung 5000 EUR mit Stundungserklärung gezahlt
```

## Ausgabe

- Pro Gläubiger eigenes `stundungsanfrage-<glaeubiger>.docx`.
- Versand per Einschreiben oder über Bank-Portal / E-Mail.
- Wiedervorlage zur Prüfung der Zusage in 14 Tagen.
- Tracker mit Status (versendet / zugesagt / abgelehnt / verhandlung).
- Hinweis: bei Ablehnung Liquiditätsplan-Update mit weiteren Maßnahmen erforderlich.


## Aktuelle Leitentscheidungen — Stundungsanfragen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Stundungsanfragen

§ 271 BGB (Faelligkeit) → § 222 AO (Stundung Steuer) → § 76 SGB IV (Stundung SV-Beitraege) → § 17 InsO (ZU-Beseitigung durch Stundung) → § 130 InsO (Anfechtungsrisiko bei Stundungsvereinbarung)

## Triage — Stundungsanfrage-Strategie

1. **Glaeubiger-Typ?** Lieferant (oft kulant), Bank (meist rigide), FA (sachliche Haerte erforderlich), SV-Traeger (sehr restriktiv).
2. **Stundungszeitraum?** Realistischer Zeitraum bis zur Liquiditaetsverbesserung angeben.
3. **Sicherheitsangebot?** Abtretung Forderungen, Eigentuemervorbehalt-Verlaengerung, persoenliche Buergschaft GF?
4. **Anfechtungsrisiko?** Stundungsvereinbarung in Krisenzeit + spaetere Zahlung = § 130 InsO Risiko; FA-Stundungsantrag schriftlich und mit Liquiditaetsplan belegen.

## Output-Template Stundungsschreiben an Finanzamt

**Adressat:** Finanzamt [ORT] — Tonfall: sachlich-erklaerend

```
Stundungsantrag nach § 222 AO
Steuernummer: [STEUERNUMMER]
Schuldner: [FIRMA]
Datum: [DATUM]

Sehr geehrte Damen und Herren,

wir beantragen Stundung der faelligen Steuerverbindlichkeiten aus [Steuerbescheid vom DATUM, Az. XX]
in Hoehe von EUR [BETRAG] bis zum [DATUM].

Begruendung:
[FIRMA] befindet sich in einer voruibergehenden Liquiditaetsengpass-Situation aufgrund [Ursache].
Eine detaillierte Liquiditaetsplanung liegt als Anlage bei (Anlage 1 — 13-Wochen-Forecast).
Nach aktueller Planung ist die Begleichung der Steuerschuld bis [DATUM] moeglich.

Wir bitten um Stundung ohne Saumniszuschlaege fuer den genannten Zeitraum.

Anlagen: Liquiditaetsplanung (Anlage 1), aktuelle BWA (Anlage 2)
```

## 3. `annahmen-belastbarkeit-plausibilisieren`

**Fokus:** Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Personal) und Risikokategorisierung. Plausibilitaetsband für jede Annahme. Erzeugt Plausibilitaetsprotokoll. Annahmen mit niedriger Belastbarkeit werden als Modellannahme markiert und im Sensitivitaetsszenario gegengerechnet.

# Annahmen plausibilisieren

## Prüfraster pro Annahme

### 1. Vergangenheits-Vergleich

- Stimmt die Annahme mit den **letzten drei Jahren** der BWA / SuSa / Jahresabschluss überein?
- Bei Abweichung: ist die Veränderung **konkret begründet** (neuer Kunde Standortschliessung Tariferhöhung)?
- Bei stark abweichender Optimismus-Annahme **ohne neuen Anlass**: Reduktion auf historisches Niveau im Plausi-Szenario.

### 2. Markt- und Branchenentwicklung

- **Branchenindex** vorhanden? (z. B. ifo Geschäftsklimaindex DESTATIS Branchenkennzahlen).
- **Auftragsbestand der Branche** rückschau.
- **Makro-Indikatoren** Konjunktur Zinsen Energiepreise.

### 3. Interne Konsistenz

- Umsatz steigt, aber Materialkosten bleiben gleich? Konsistenz prüfen.
- Personalkosten steigen, aber Personalstand sinkt? Begründung erforderlich (Tariferhöhung + Reduzierung gleichzeitig).
- Working Capital verbessert sich rapide? Begründung notwendig.

### 4. Belegbarkeit der Maßnahmen

- Sanierungsmaßnahmen mit Effekt — ist der Effekt **belegt** (Vergleichswerte historisch Kostenrechnung)?
- Zeitplan realistisch (z. B. Standortschliessung in 60 Tagen)?
- Einmalkosten realistisch erfasst?

### 5. Drittvereinbarungen

- Patronatserklärungen / Comfortletter: bereits unterzeichnet oder nur in Verhandlung?
- Gesellschafterdarlehen mit Rangrücktritt: notarielle Urkunde vorhanden?
- Bankenzusage: schriftlich oder mundlich?

## Plausibilitätsband pro Annahme

```yaml
plausibilisierung:
 - annahme-id: umsatz-hauptsegment
 band: realistisch # konservativ / realistisch / ambitioniert / nicht-belastbar
 begruendung: |
 Auftragsbestand bis 09/2026 belegt; ab 10/2026 Modellfortschreibung
 auf Basis Vorjahr +3%
 risiko: mittel
 sensitivitaet-szenario:
 negativ: 10% Umsatzrückgang ab 10/2026
 effekt-eur: -190000 (kumuliert)

 - annahme-id: kostensenkung-standort
 band: ambitioniert
 begruendung: |
 Kündigung Standortmietvertrag erfordert 9-Monats-Kündigungsfrist;
 Schliessung bis 08/2026 nur möglich wenn Mieter Aufhebung akzeptiert.
 Aktuell in Verhandlung — nicht belegt.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Schliessung gelingt nicht im Planhorizont
 effekt-eur: 50000 monatliche Mehrkosten

 - annahme-id: bankenzusage-erhöhung-kreditlinie
 band: nicht-belastbar
 begruendung: |
 Verhandlung mit Bank laeuft. Bisher keine schriftliche Zusage.
 Bank verweist auf laufendes Rating-Verfahren.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Kreditlinie wird nicht erhöht
 effekt-eur: keine zusätzliche Liquidität 80000 EUR
```

## Konservativer Maßstab

Eine Fortbestehensprognose ist nicht der Ort für Optimismus. **IDW S 11** und **BGH-Rspr.** verlangen einen vorsichtigen objektiven Maßstab.

- Bei Zweifeln: **konservative** Annahmen wählen.
- Wenn eine Annahme **ambitioniert** oder **nicht-belastbar** ist und entscheidend für das Prognoseergebnis ist: das Ergebnis ist **nicht verwertbar** als positive Fortbestehensprognose. Maßnahme: entweder Belegbarkeit nachholen oder Annahme entfernen.

## Sensitivitätsszenarien

```yaml
szenarien:
 basisszenario:
 annahmen: alle wie in annahmen.yaml
 ergebnis-12-monate-liquiditaet: positiv
 bemerkung: Plan-Szenario

 negativ-szenario:
 annahmen: alle ambitioniert-Annahmen reduziert auf konservativ
 ergebnis-12-monate-liquiditaet: knapp positiv # vor Maßnahmen
 bemerkung: Risiko-Szenario; bei Eintritt sind Zusatzmaßnahmen erforderlich

 stress-szenario:
 annahmen: zusätzlich Wegfall Top-Kunde
 ergebnis-12-monate-liquiditaet: negativ
 bemerkung: Reines Stress-Szenario; in der Plausibilisierung
 als unwahrscheinlich eingeschaetzt
```

## Sonderfälle

### Stille Reserven die zur Plausibilisierung herangezogen werden

Wenn der Status stille Reserven enthält (Skill `bilanzieller-status-aufnehmen`) muss die Liquidität auch realistisch über Verkauf erzielbar sein:

- Verkehrswert-Gutachten vorhanden?
- Realistisch verkaufbar im Planhorizont?
- Auswirkung auf den Betrieb (z. B. Verkauf einer Maschine führt zu Produktionsausfall)?

### Comfortletter

- **Weicher Comfortletter** (Best Effort) ist im Status **nicht** zu berücksichtigen.
- **Harte externe Patronatserklärung** mit Forderungsverzicht im Insolvenzfall ist berücksichtigungsfähig — siehe Skill `patronatserklaerung-extern-hart-erzeugen`.

## Ausgabe

- `plausibilisierung.md` mit jeder Annahme bewertet (Band Risiko Sensitivitaet).
- Drei Szenarien (Basis Negativ Stress) mit Endergebnis.
- Empfehlung: bei mehr als zwei nicht-belastbaren oder ambitionierten Annahmen die das Ergebnis tragen ist die Prognose **nicht positiv** zu werten.
- Liste konkreter Maßnahmen zur Verbesserung der Belastbarkeit (Belegnachholung Verhandlungsabschluss Drittvereinbarung).


## Aktuelle Leitentscheidungen — Annahmen-Plausibilitaet

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Annahmen-Plausibilitaet

§ 19 Abs. 2 InsO (Fortbestehensprognose) → § 15b InsO (Haftung bei fehlerhafter Prognose) → IDW S 11 Rn. 45 ff. (Annahmen-Qualitaet) → IDW S 6 Rn. 90 ff. (Plausibilitaetspruefung Sanierungskonzept)

## Triage — Annahmen-Check

Bevor losgelegt wird, klaere:

1. **Konsistenz-Test:** Passt Umsatzwachstum zu Personalkosten und Material? (Umsatz +10% ohne Personal-Aufstockung bei Vollauslastung → inkonsistent)
2. **Vergangenheits-Abgleich:** Welche Wachstumsraten wurden in den letzten 3 Jahren tatsaechlich erreicht? Neue Annahmen muessen daraus ableitbar sein.
3. **Sensitivity-Test:** Welche Annahme ist am kritischsten? Was passiert wenn Haupt-Kunden 20% weniger abnimmt?
4. **Worst-Case-Szenario:** Prognose auch bei pessimistischsten Annahmen noch positiv?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---
name: negativer-fristennotiz-ausloesendes-ereignis
description: "Negativer Fristennotiz Ausloesendes Ereignis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Negativer Fristennotiz Ausloesendes Ereignis

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Negativer Fristennotiz Ausloesendes Ereignis** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-negativer-fristennotiz-und-naechster-schritt` | Negativer: Fristennotiz und nächster Schritt im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass Gesellschafterhinweis eigene Sorge des Geschäftsführers. Dokumentiert Anlass Datum Hinweisgeber Mitteilungsform. Wichtig für spaeteren Nachweis dass der Geschäftsführer auf Insolvenzanzeichen rechtzeitig reagiert hat (Haftungsfrage § 15b InsO). |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die verzichtete Forderung wird nicht passiviert. Steuerliche Folge beim Schuldner Ertragsbuchung (Sanierungserlös Sanierungsgewinn § 3a EStG bei Sanierungsbedarf). Beim Gläubiger Forderungsausfall ggf abzugsfähig. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **Negativer Fristennotiz Ausloesendes Ereignis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-negativer-fristennotiz-und-naechster-schritt`

**Fokus:** Negativer: Fristennotiz und nächster Schritt im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Negativer: Fristennotiz und nächster Schritt

## Spezialwissen: Negativer: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Negativer: Fristennotiz und nächster Schritt / negativer fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, IDW, StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Negativer** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `ausloesendes-ereignis-erfassen`

**Fokus:** Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass Gesellschafterhinweis eigene Sorge des Geschäftsführers. Dokumentiert Anlass Datum Hinweisgeber Mitteilungsform. Wichtig für spaeteren Nachweis dass der Geschäftsführer auf Insolvenzanzeichen rechtzeitig reagiert hat (Haftungsfrage § 15b InsO).

# Auslösendes Ereignis erfassen

## Zweck

Die Fortbestehensprognose ist kein Selbstzweck — sie ist die Antwort auf einen konkreten Anlass. Der Anlass wird dokumentiert weil **er Beweis ist**: bei späteren Haftungsfragen (§ 15b InsO, § 43 GmbHG, § 826 BGB ggue Gläubigern) zeigt die Dokumentation dass der Geschäftsführer **zeitnah** auf Anzeichen reagiert hat.

## Typische Auslöser

### 1. Hinweis des Steuerberaters nach § 102 StaRUG

Seit 01.01.2021 hat der Steuerberater eine **Hinweispflicht**: wenn ihm bei der Bilanzaufstellung Anhaltspunkte für einen möglichen Insolvenzeröffnungsgrund auffallen muss er den Mandanten darauf hinweisen.

- Datum des Hinweises (schriftlich / mündlich / im Gespräch)
- Wortlaut wenn schriftlich
- Konkrete Anhaltspunkte die der StB genannt hat
- Quittierung des Hinweises durch den Mandanten

### 2. Hinweis des Wirtschaftsprüfers

Bei prüfungspflichtigen Gesellschaften (mittelgroße oder große KapGes nach § 267 HGB) kann der Prüfer im Rahmen des Jahresabschlusses einen **Hinweis zur Going-Concern-Annahme** geben oder den Bestätigungsvermerk einschraenken oder versagen.

### 3. Eigene Feststellung bei der Bilanzaufstellung

- **Eigenkapital negativ** (Aktiva kleiner als Passiva).
- **Wesentliche stille Lasten** im Status (z. B. Pensionsrückstellungen außerbilanziell).
- **Erhebliche außergewöhnliche Verluste** im laufenden Geschäftsjahr.

### 4. Liquiditätsengpass

- Mahnungen Gerichtsbeschlüsse oder Zahlungsverzug bei wesentlichen Gläubigern.
- Kreditlinie ausgeschoepft Kontoüberziehung.
- Lohn- und Gehaltszahlungen knapp.
- Steuer- und Sozialversicherungsabgaben nicht puenktlich.

### 5. Gesellschafterhinweis

- Brief oder E-Mail des Gesellschafters mit Sorge über Lage.
- Gesellschafterbeschluss zur Prüfung der Fortbestehensprognose.

### 6. Eigene Sorge des Geschäftsführers

- Subjektive Wahrnehmung dass die Lage kritisch wird.
- Wichtig: auch ohne externen Hinweis muss der Geschäftsführer aktiv prüfen — Sorgfaltspflicht § 43 GmbHG, § 93 AktG.

### 7. Externes Ereignis

- Wegfall Hauptkunde.
- Kreditlinien-Kündigung der Bank.
- Markteinbruch.
- Insolvenz eines wesentlichen Lieferanten / Abnehmers.

## Dokumentation

```yaml
fall-id: FP-2026-0001
stichtag-pruefung: 2026-05-20
ausloeser:
 typ: hinweis-steuerberater # hinweis-steuerberater / hinweis-wp / eigene-feststellung-bilanz / liquiditätsengpass / gesellschafterhinweis / eigene-sorge / externes-ereignis
 datum: 2026-05-15
 hinweisgeber: Steuerberater Mueller, Kanzlei XYZ
 mitteilungsform: schriftlich # schriftlich / muendlich / e-mail
 wortlaut: |
 "Nach Aufstellung des Jahresabschlusses 2025 ergibt sich ein negatives
 Eigenkapital von 82.000 EUR. Wir weisen Sie nach § 102 StaRUG auf die
 Pflicht zur Prüfung einer Fortbestehensprognose nach § 19 Abs. 2 InsO
 hin."
 konkrete-anhaltspunkte:
 - Eigenkapital negativ 82.000 EUR Stichtag 31.12.2025
 - SuSa weist Lieferantenverbindlichkeiten 410.000 EUR (Vorjahr 180.000)
 - Sozialversicherungsbeitraege drei Monate offen 45.000 EUR
 reaktion-geschaeftsfuehrung:
 erste-reaktion-am: 2026-05-20
 schritte:
 - Beauftragung Erstellung Fortbestehensprognose
 - Aktivierung Plugin fortbestehensprognose
 - Termin mit Insolvenzanwalt vereinbart für 2026-05-27 als Sicherheit
```

## Pflichthinweis Frist

Mit Eintritt der **Insolvenzreife** (Zahlungsunfähigkeit § 17 oder Überschuldung § 19 InsO) beginnen die Antragsfristen des § 15a InsO. **Die Fortbestehensprognose ist nicht zu verwechseln mit dieser Frist** — sie ist die Prüfung **ob** Überschuldung trotz negativen Bilanzbildes verneint werden kann.

- Frist Zahlungsunfähigkeit: **drei Wochen** (§ 15a Abs. 1 S. 2 InsO).
- Frist Überschuldung: **sechs Wochen** (§ 15a Abs. 1 S. 2 InsO seit SanInsFoG 2021).

Im Zweifel **vor Ablauf der Frist** Insolvenzanwalt zu Rate ziehen.

## Ausgabe

- `ausloesendes-ereignis.yaml` mit allen Pflichtfeldern.
- Erste Risikobewertung (grün / gelb / rot).
- Empfehlung: bei rot direkt zu `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einschalten — diese Prüfung kann fortgesetzt werden aber nicht ohne anwaltliche Begleitung.


## Aktuelle Leitentscheidungen — Ausloesende Ereignisse

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Ausloesende Ereignisse

§ 102 StaRUG (Warnpflicht Rechtsberater) → § 19 InsO (Ueberschuldung als Eröffnungsground) → § 15a InsO (Antragspflicht 3/6 Wochen) → § 15b InsO (Haftung GF) → § 43 GmbHG (Sorgfaltspflicht)

## Triage — Ausloesende Ereignisse

1. **Wer hat das Signal gesandt?** Steuerberater (§ 102 StaRUG), Wirtschaftspruefer, eigene Erkenntnis GF, Bank-Gespraech?
2. **Datum des Signals?** Tag-genau dokumentieren → Beginn der Haftungszeit-Uhr.
3. **Schriftliche Dokumentation?** E-Mail, Aktenvermerk, Protokoll vorhanden?
4. **Sofortmassnahmen?** Liquiditaetsplanung starten, Anwalt einschalten, Steuerberater beauftragen?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `forderungsverzicht-besserungsschein`

**Fokus:** Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die verzichtete Forderung wird nicht passiviert. Steuerliche Folge beim Schuldner Ertragsbuchung (Sanierungserlös Sanierungsgewinn § 3a EStG bei Sanierungsbedarf). Beim Gläubiger Forderungsausfall ggf abzugsfähig.

# Forderungsverzicht mit Besserungsschein

## Wirkung

Gläubiger verzichtet auf eine Forderung. Effekt:

- **Im Status**: Forderung entfaellt aus den Passiva. Bilanzbild verbessert sich.
- **Liquidität**: keine direkte Liquiditätszuflussverbesserung (die Forderung war ggf ohnehin nicht in den nächsten 12 Monaten zur Zahlung fällig).
- **Bilanz**: Ertrag (Sanierungserloes).

Mit **Besserungsschein**: Wenn die Schuldnerin später wieder zahlungsfähig wird lebt die Forderung wieder auf. Der Verzicht ist also bedingt.

## Anwendungsfall

- Bank verzichtet auf Teil-Tilgung eines Darlehens.
- Lieferant verzichtet auf Forderung mit Besserungsschein als Sanierungsbeitrag.
- Hauptgesellschafter verzichtet auf Forderung (statt Rangrücktritt).

## Steuerliche Folgen

### Beim Schuldner

Ertragsbuchung Sanierungserloes. **Sanierungsgewinn § 3a EStG** kann steuerbefreit sein wenn die Voraussetzungen (Sanierungsabsicht Sanierungsfähigkeit Sanierungseignung Gläubigergleichbehandlung) erfüllt sind.

Vor Unterzeichnung **steuerliche Beratung** zwingend.

### Beim Gläubiger

Forderungsausfall regelmäßig als Betriebsausgabe abzugsfähig. Bei Banken Wertberichtigung. Steuerlich vor Verzicht prüfen lassen.

## Mustervorlage

```
FORDERUNGSVERZICHTSVEREINBARUNG MIT BESSERUNGSSCHEIN

zwischen

 [Vor- und Nachname Gläubiger]
 [Anschrift]
 - im Folgenden "der Gläubiger" -

und

 [Firma der Schuldnerin]
 vertreten durch [Geschäftsführer]
 [Anschrift]
 HRB [...] AG [...]
 - im Folgenden "die Schuldnerin" -

1. Praeambel

Der Gläubiger ist Inhaber folgender Forderung gegen die Schuldnerin:

 [Bezeichnung der Forderung]
 Hauptforderung [Betrag] EUR
 zuzueglich Zinsen
 zum [Stichtag] insgesamt [Gesamtbetrag] EUR

Die Schuldnerin befindet sich in einer angespannten wirtschaftlichen Lage
und hat eine Fortbestehensprognose nach § 19 Abs. 2 InsO erstellt. Mit
Sanierungsbeitrag durch den Gläubiger ist die Prognose positiv.

2. Verzicht

2.1 Der Gläubiger verzichtet hiermit gegenüber der Schuldnerin auf die
oben bezeichnete Forderung in voller Höhe einschließlich Zinsen und
Nebenforderungen.

2.2 Die Forderung erlischt im Status der Schuldnerin und ist in der
insolvenzrechtlichen Status-Aufstellung nicht mehr zu passivieren.

3. Besserungsschein

3.1 Der Verzicht ist bedingt durch das Wiedererstarken der Zahlungsfähigkeit
der Schuldnerin.

3.2 Die Forderung lebt wieder auf wenn

 a) die Schuldnerin im Jahresabschluss ein positives Eigenkapital aufweist
 oder
 b) die Schuldnerin in einem Geschäftsjahr einen Jahresueberschuss von mehr
 als [X] EUR erwirtschaftet oder
 c) der Gläubiger bei nachhaltiger Verbesserung der wirtschaftlichen Lage
 in Textform die Wiederaufnahme verlangt.

3.3 Der Rückzahlungsbetrag betraegt im Fall des Wiederauflebens

 - höchstens den urspruenglichen Forderungsbetrag,
 - mindestens [X] Prozent des verfügbaren Eigenkapitals des Folgejahres,
 - wird in Raten über [N] Monate getilgt.

3.4 Die Besserungsklausel laeuft für [N] Jahre ab Unterzeichnung. Nach
Ablauf entfaellt die Wiederauflebensmöglichkeit endgültig.

4. Steuerliche Hinweise

Die Parteien sind sich bewusst dass dieser Verzicht beim Schuldner Ertrag
ausloest. Vor Unterzeichnung wurde steuerlicher Rat eingeholt.

5. Form und Wirksamkeit

5.1 Diese Vereinbarung ist beidseitig unterzeichnet wirksam.

5.2 Änderungen und Ergänzungen bedürfen der Schriftform.

5.3 Gerichtsstand: [Sitz der Schuldnerin].

[Ort], [Datum]

___________________________
[Gläubiger]


___________________________
[Geschäftsführer]
für die Schuldnerin
```

## Hinweise

### Echtheit der Sanierungsabsicht

Wird der Forderungsverzicht später als Scheingeschäft angesehen (z. B. weil keine ernsthafte Sanierungsabsicht vorlag) kann er anfechtbar sein.

### Gläubigergleichbehandlung

Bei Sanierungsverzicht ist auf Gläubigergleichbehandlung zu achten. Wenn nur einzelne Gläubiger verzichten und andere nicht ist das in Ordnung — solange der Vorgang nicht als Begueneten-Bezugnahme zu Lasten der nicht-verzichtenden Gläubiger zu werten ist.

### Besserungsschein-Trigger genau definieren

Der Trigger für das Wiederaufleben muss objektiv und nachprüfbar sein. Klauseln wie "wenn es uns wieder besser geht" sind ungeeignet.

## Ausgabe

- `forderungsverzicht-besserungsschein-<glaeubiger>.docx`.
- Steuerliche Prüfer-Flag — Steuerberater einbinden.
- Statusupdate (Skill `bilanzieller-status-aufnehmen`): Forderung entfaellt aus den Passiva.
- Eintrag im Sanierungsbausteine-Tracker.


## Aktuelle Leitentscheidungen — Forderungsverzicht und Besserungsschein

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Forderungsverzicht

§ 19 Abs. 2 InsO (Ueberschuldungsbereinigung) → § 3a EStG (steuerfreier Sanierungsgewinn) → § 397 BGB (Erlass/Verzicht) → § 158 BGB (haengende Bedingung Besserungsschein) → § 133 InsO (Anfechtungsrisiko bei selektivem Verzicht)

## Triage — Forderungsverzicht Check

1. **Glaeubiger und Betrag?** Wer verzichtet auf wie viel?
2. **Steuerliche Folge?** Sanierungsgewinn § 3a EStG: Nachweise Sanierungsplan, Sanierungsabsicht, Sanierungseignung vorbereiten.
3. **Besserungsschein-Formulierung?** Bedingung klar definiert (Wiederherstellung ZF anhand konkreter Liquiditaets-Schwelle).
4. **Anfechtungsschutz?** Verzicht muss Teil eines Gesamtsanierungskonzepts sein (IDW S 6 Qualitaet) um Vorsatzanfechtung § 133 InsO auszuschliessen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

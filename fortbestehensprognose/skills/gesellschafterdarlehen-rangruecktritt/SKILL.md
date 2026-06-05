---
name: gesellschafterdarlehen-rangruecktritt
description: "Gesellschafterdarlehen Rangruecktritt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gesellschafterdarlehen Rangruecktritt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gesellschafterdarlehen Rangruecktritt** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschafterdarlehen-rangruecktritt` | Prüffeld für gesellschafterdarlehen rangruecktritt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `liquiditaet-12-monate` | Prüffeld für liquiditaet 12 monate: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `patronatserklaerung-extern-hart-erzeugen` | Prüffeld für patronatserklaerung extern hart erzeugen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **Gesellschafterdarlehen Rangruecktritt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschafterdarlehen-rangruecktritt`

**Fokus:** Prüffeld für gesellschafterdarlehen rangruecktritt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Gesellschafterdarlehen — qualifizierter Rangrücktritt

## Zweck

Eine bestehende Forderung des Gesellschafters gegen die Gesellschaft (Darlehen Verkaufsforderung Mietforderung) wird mit einem **qualifizierten Rangrücktritt** versehen. Folge:

- Die Forderung wird im insolvenzrechtlichen Status **nicht passiviert** (§ 19 Abs. 2 S. 2 InsO).
- Der Status verbessert sich um den Nennbetrag der Forderung.
- Bei späterer Insolvenz tritt der Gesellschafter hinter alle anderen Gläubiger zurück.

## BGH-Anforderungen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

1. **Insolvenzfall** der Gesellschaft.
2. **Gläubigergleichbehandlung** — Rücktritt hinter alle anderen Gläubiger.
3. **Geschäftsbeendigung und Liquidation** außerhalb der Insolvenz.
4. **Vorinsolvenzliche Krisenlage** — Rückforderung nur nach gleichrangiger Befriedigung aller anderen Gläubiger.

Ohne diese vier Komponenten ist der Rangrücktritt **insolvenzrechtlich unwirksam** und die Forderung muss weiterhin passiviert werden.

## Mustervorlage

```
QUALIFIZIERTER RANGRUECKTRITT

zwischen

 [Vor- und Nachname Gesellschafter]
 [Anschrift]
 - im Folgenden "der Gläubiger" -

und

 [Firma der Gesellschaft]
 vertreten durch [Geschäftsführer]
 [Anschrift]
 HRB [...] AG [...]
 - im Folgenden "die Schuldnerin" -

1. Praeambel

Der Gläubiger ist Inhaber folgender Forderung gegen die Schuldnerin:

 Darlehensvertrag vom [Datum]
 Hauptforderung in Höhe von [Betrag] EUR
 zuzueglich vereinbarter Zinsen
 zum [Stichtag] insgesamt [Gesamtbetrag] EUR.

2. Rangrücktritt

2.1 Der Gläubiger tritt mit der vorgenannten Forderung — einschließlich
samt allen Zinsen Nebenforderungen und sonstigen Anhangs — hinter saemtliche
gegenwaertigen und kuenftigen Forderungen aller anderen Gläubiger der
Schuldnerin im Rang zurück.

2.2 Der Rangrücktritt erstreckt sich auf folgende Fälle:

 a) Insolvenz der Schuldnerin (Eröffnungsverfahren und eroeffnetes Verfahren),
 b) Liquidation der Schuldnerin außerhalb der Insolvenz,
 c) jeden anderen Fall der Geschäftsbeendigung der Schuldnerin,
 d) jede vorinsolvenzliche Krisenlage in der die Schuldnerin nicht
 überwiegend wahrscheinlich zahlungsfähig fortgeführt werden kann.

2.3 Tilgung Zinszahlung oder sonstige Befriedigung der Forderung kann nur
erfolgen wenn

 - alle anderen Gläubiger der Schuldnerin gleichrangig befriedigt sind, ODER
 - die Befriedigung aus dem freien — nicht zur Erfüllung gegenüber Gläubigern
 gleichen oder vorrangigen Ranges erforderlichen — Vermögen der Schuldnerin
 erfolgt.

2.4 Diese Erklärung ist unwiderruflich.

3. Wirkung im Insolvenzstatus

Die Parteien sind sich einig dass aufgrund des Rangrücktritts die Forderung
des Gläubigers im insolvenzrechtlichen Überschuldungsstatus der Schuldnerin
nach § 19 Abs. 2 S. 2 InsO nicht zu passivieren ist.

4. Steuerrechtliche Hinweise

Die Parteien sind sich bewusst dass der Rangrücktritt steuerrechtliche Folgen
ausloesen kann (Ertragsbuchung beim Schuldner bei nachhaltiger Rückzahlungsunfähigkeit
§ 5 Abs. 2a EStG analog). Vor Unterzeichnung wurde steuerlicher Rat eingeholt.

5. Form und Wirksamkeit

5.1 Diese Vereinbarung ist beidseitig unterzeichnet wirksam. Notarielle
Beurkundung wird empfohlen aber ist nicht zwingend.

5.2 Änderungen und Ergänzungen bedürfen der Schriftform.

5.3 Gerichtsstand: [Sitz der Schuldnerin].

[Ort], [Datum]

___________________________
[Gläubiger]


___________________________
[Geschäftsführer]
für die Schuldnerin
```

## Wichtige Hinweise

### Notarielle Beurkundung

Nicht zwingend aber **empfohlen** bei hohen Forderungen — Beweis- und Anfechtungsschutz.

### Anfechtungsrisiko

Bei nachfolgender Insolvenz prüfbar nach § 135 Abs. 1 InsO (Gesellschafterdarlehen — Insolvenzanfechtung). Der Rangrücktritt selbst ist nicht anfechtbar — er konkretisiert die ohnehin nach § 39 Abs. 1 Nr. 5 InsO bestehende Nachrangigkeit.

### Verzicht auf bereits geleistete Zahlungen?

Nicht im Rangrücktritt. Wenn der Gesellschafter Rückzahlungen erhalten hat: prüfen ob diese nach § 135 InsO anfechtbar sind.

### Steuerrechtliche Folge — Buchungsfrage

Wenn nach Bilanzansatz die Forderung dauerhaft nicht mehr werthaltig (kein freies Vermögen jemals zur Tilgung): ggf. Ertragsbuchung beim Schuldner zwingend. Vor Unterzeichnung Steuerberater konsultieren.

### Pflicht zur Anzeige?

Es besteht keine eigenständige Anzeigepflicht. Aber bei Insolvenzantrag ist der Rangrücktritt offen zu legen.

## Ausgabe

- `gesellschafterdarlehen-rangruecktritt.docx` und PDF.
- Hinweis: notariell beurkunden lassen wenn Höhe über 50000 EUR.
- Eintrag im Status (Skill `bilanzieller-status-aufnehmen`) — Forderung wird nicht passiviert.
- Wiedervorlage zur Prüfung Steuerfolge (steuerberatung).


## Aktuelle Leitentscheidungen — Gesellschafterdarlehen und Rangruecktritt

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Gesellschafterdarlehen

§ 19 Abs. 2 S. 2 InsO (qualifizierter Rangruecktritt — Nicht-Passivierung) → § 135 InsO (Anfechtung Gesellschafterdarlehen 1 Jahr) → § 39 Abs. 4 InsO (Sanierungsprivileg) → § 39 Abs. 1 Nr. 5 InsO (Nachrang Gesellschafterdarlehen) → §§ 488 ff. BGB (Darlehensvertrag)

## Triage — Gesellschafterdarlehen Check

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Darlehens-Restlaufzeit?** Innerhalb 1 Jahr → Tilgung anfechtungsgefaehrdet § 135 InsO.
3. **Sanierungskonzept vorhanden?** Ohne IDW S 6 kein Sanierungsprivileg § 39 Abs. 4 InsO.
4. **Zinsen laufen?** Nachrangige Zinsen sollten ebenfalls durch Rangruecktritt erfasst sein.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `liquiditaet-12-monate`

**Fokus:** Prüffeld für liquiditaet 12 monate: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Zwölf-Monats-Liquidität

## Zweck

Die Fortbestehensprognose erfordert dass das Unternehmen über den **Prognosehorizont von zwölf Monaten** zahlungsfähig bleibt. Das bedeutet: in jedem Monat müssen die liquiden Mittel plus Kreditlinien plus Zufluesse die fälligen Verbindlichkeiten decken.

## Drei Schichten

### Schicht 1 — Monatliche Liquiditätsplanung

Aus den Annahmen aus `annahmen-sammeln-fortfuehrung` plus Plausibilisierung:

```yaml
liquiditaet:
 startbestand-2026-05-20: 18000
 kreditlinie-verfuegbar: 12000 # Linie 150000 minus 138000 ausgenutzt

 monatsdaten:
 - monat: 2026-06
 einzahlungen:
 forderungen-laul: 185000
 gesellschafter-darlehen: 0
 sonstige: 0
 summe: 185000
 auszahlungen:
 lieferanten: 130000
 loehne-gehaelter: 78000
 sozialabgaben: 24000
 steuern: 14000
 bank-tilgung: 8000
 miete: 6000
 energie: 9000
 sonstige: 5000
 summe: 274000
 saldo-monat: -89000
 monatsendbestand: -71000 # negativ — Linie reicht nicht
 bemerkung: Liquiditätslücke
```

### Schicht 2 — Detaillierte Wochenplanung

Bei kritischen Phasen (Monaten mit knapp positivem Saldo oder negativem Endbestand) muss die Wochenplanung herangezogen werden:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Plugin `liquiditaetsplanung` enthält die wochenbasierten Vorlagen.

### Schicht 3 — Sensitivitätsszenarien

Drei Szenarien aus `annahmen-belastbarkeit-plausibilisieren` werden in der Liquidität durchgerechnet:

- **Basis-Szenario** — Plan
- **Negativ-Szenario** — ambitionierte Annahmen reduziert
- **Stress-Szenario** — Top-Kunde weg

Bei jedem Szenario die monatlichen Salden über die zwölf Monate.

## Prüfkriterien

### Pro Monat

- **Monatsendbestand mindestens null** (besser kein voll ausgenutzter Kontokorrent).
- **Keine roten Monate** im Plan.

### Über den Horizont

- **Steigender Trend** oder Stabilisierung der Liquidität.
- **Wesentliche Risikoposten** identifiziert.
- **Maßnahmenoptionen** bei Risiko-Eintritt vorhanden.

### Bei Sensitivitaet

- **Negativ-Szenario** Liquidität auch positiv? Wenn nein: dann ist die Prognose **nur** im Basis-Szenario tragfähig. Das ist **nicht** ausreichend für eine positive Fortbestehensprognose.
- **Stress-Szenario** soll mit den Maßnahmen abgefedert werden können — gegebenenfalls Patronatserklärungen Comfortletter Gesellschafterdarlehen.

## Konsolidierung mit dem Plugin `liquiditaetsplanung`

Wenn das Plugin `liquiditaetsplanung` installiert ist:

- Die detaillierte Wochenplanung erfolgt dort (Skill `liquiditaetsvorschau-3-6-12-monate`).
- Hier importieren wir die Monatsaggregate.
- Die Drei-Wochen-Schwelle § 17 InsO wird in `liquiditaetsplanung` separat geprüft.

Wenn nicht installiert: einfache Tabelle hier; bei Bedarf nachinstallieren.

## Beispielergebnis

```
Liquiditätsprüfung Zwölf Monate
Basis-Szenario: positiv (Endbestand jeweils über null)
Negativ-Szenario: kritisch (Monat 11 unter null)
Stress-Szenario: negativ ab Monat 4

Bewertung: ohne Sanierungsmaßnahmen ist die Liquidität im Stress-Szenario
überschritten. Mit Maßnahmen aus Skill sanierungsbausteine-vorschlagen
ist die Liquidität über den Horizont zu sichern.
```

## 90-Prozent-Deckung ist der operative Maßstab

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **In jedem Zeitabschnitt** muss die Deckung der fälligen Verbindlichkeiten mindestens **90 Prozent** betragen (Liquiditätslücke unter zehn Prozent).
- **Eine vorübergehende Lücke** über zehn Prozent darf höchstens **drei Wochen** andauern. Wer laenger als drei Wochen unter 90 Prozent Deckung liegt ist nach BGH zahlungsunfähig — und das ist gerade nicht "fortfuehrbar".
- **Über den vollen Zwölf-Monats-Horizont** muss diese Schwelle eingehalten werden — andernfalls ist die Fortbestehensprognose **negativ**.

Die "mehr als 50 Prozent Wahrscheinlichkeit" der Prognose bezieht sich darauf dass dieses Szenario (Einhaltung der BGH-Schwelle über zwölf Monate) eintritt — also nicht ein abstrakter Erfolgswert sondern die methodische Wahrscheinlichkeit dass das Unternehmen die 90-Prozent-Deckung bzw. die Drei-Wochen-Karenz **über den gesamten Horizont durchhaelt**.

**Konsequenz für die Liquiditätsprognose:**

- Pro Monat (besser pro Woche in kritischen Phasen): Liquiditätsbestand plus Linie / fällige Verbindlichkeiten = Deckungsquote.
- Deckungsquote in jedem Zeitabschnitt mindestens **90 Prozent**.
- Bei Unterschreitung max. drei Wochen — danach muss die Quote zwingend über 90 Prozent zurückkehren.
- Im Negativ- und Stress-Szenario diese Prüfung **wiederholen**. Wenn auch das Negativ-Szenario die Schwelle einhaelt: starke Prognose. Wenn nur das Basis-Szenario einhaelt aber das Negativ-Szenario reisst: knappe Prognose — nur mit zusätzlichen verbindlichen Maßnahmen positiv.

## Ausgabe

- `liquiditaet-12-monate.xlsx` mit monatlichen Werten je Szenario.
- `liquiditaet-monatssalden.md` als menschenlesbare Übersicht.
- Hinweis auf Prüfer-Flag bei roten Monaten.
- Empfehlung auf nächsten Skill `fortbestehensprognose-zusammenfuehren`.


## Aktuelle Leitentscheidungen — 12-Monats-Liquiditaetsplanung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette 12-Monats-Liquiditaet

§ 17 InsO (Zahlungsunfaehigkeit, 10%-Schwelle) → § 19 Abs. 2 InsO (Fortbestehensprognose — Liquiditaet als Kernbestandteil) → IDW S 11 Rn. 50-65 (Liquiditaetsplanung als Prognosebaustein) → § 15a InsO (Antragspflicht bei negativem Forecast)

## Triage — 12-Monats-Forecast Check

1. **Methode?** Direkte Methode (Cash-In/Cash-Out) bevorzugt fuer insolvenzrechtliche Beurteilung.
2. **Periode?** Monatsgranularitaet Minimum; Wochen-Granularitaet wenn ZU-nahe.
3. **Annahmen konsistent?** Mit Umsatz- und Kostenplanung aus `annahmen-sammeln-fortfuehrung` abgestimmt?
4. **Engpaesse sichtbar?** Negative Saldi in einzelnen Monaten klar hervorgehoben und mit Gegenmassnahmen unterlegt?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `patronatserklaerung-extern-hart-erzeugen`

**Fokus:** Prüffeld für patronatserklaerung extern hart erzeugen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Externe harte Patronatserklärung

## Wirkung

Die externe harte Patronatserklärung ist eine **rechtsverbindliche** Zusicherung des Patrons gegenüber dem Begueneten (typisch der Gesellschaft selbst oder ihren Gläubigern) finanzielle Mittel zur Verfügung zu stellen damit die Begueneten ihren Verpflichtungen nachkommen kann.

Im Gegensatz zur **internen** und zur **weichen** Patronatserklärung ist sie:

- **Schriftlich** und rechtsverbindlich.
- **Mit konkretem Inhalt** (Höhe Bedingungen Laufzeit).
- **Direkt durchsetzbar** durch die Gesellschaft (oder ihre Gläubiger als Drittberechtigte wenn vereinbart).
- **Insolvenzfest** — die Verpflichtung des Patrons bleibt auch im Insolvenzfall der Gesellschaft bestehen.

## Voraussetzungen für Berücksichtigung im Status

- **Höhe** des Verpflichtungsumfangs konkret beziffert.
- **Bonität** des Patrons (er muss leistungsfähig sein — Bonitätsnachweis erforderlich).
- **Insolvenzfeste Klausel**: der Patron verzichtet darauf seine Forderung gegen die Gesellschaft im Insolvenzfall geltend zu machen.
- **Unwiderruflichkeit** während der Laufzeit der Prognose.

## Mustervorlage

```
PATRONATSERKLAERUNG

zwischen

 [Vor- und Nachname Patron]
 [Anschrift]
 - im Folgenden "der Patron" -

und

 [Firma der Gesellschaft]
 vertreten durch ihre(n) Geschäftsführer(in)
 [Name]
 [Anschrift]
 Handelsregister AG [...] HRB [...]
 - im Folgenden "die Gesellschaft" -

1. Praeambel

Die Gesellschaft befindet sich in einer wirtschaftlich angespannten Lage.
Die Geschäftsführung hat eine Fortbestehensprognose nach § 19 Abs. 2 InsO
erstellt aus der sich ergibt dass die Gesellschaft für die nächsten zwölf
Monate eine überwiegende Wahrscheinlichkeit zur Fortfuehrung nur unter
Inanspruchnahme dieser Patronatserklärung aufweist.

Der Patron wünscht die Fortfuehrung der Gesellschaft zu unterstützen.

2. Erklärung des Patrons

2.1 Der Patron verpflichtet sich gegenüber der Gesellschaft auf erstes
schriftliches Anfordern hin saemtliche Mittel zur Verfügung zu stellen die
zur Erfüllung der gesetzlichen Verpflichtungen der Gesellschaft erforderlich
sind soweit diese aus eigenen Mitteln nicht aufgebracht werden können.

2.2 Die Verpflichtung gilt bis zu einem Höchstbetrag von

 [Betrag in EUR] EUR (in Worten ___________________)

2.3 Die Verpflichtung gilt für den Zeitraum vom [Beginn] bis zum [Ende].
Die Mindestlaufzeit betraegt zwölf Monate ab Unterzeichnung; sie verlängert
sich automatisch um jeweils sechs Monate sofern nicht spaetestens drei Monate
vor Ablauf schriftlich gekündigt wird.

3. Insolvenzfestigkeit

3.1 Der Patron verzichtet darauf Forderungen die ihm gegen die Gesellschaft
aus der Erfüllung dieser Patronatserklärung zustehen sollten im Fall einer
Insolvenz der Gesellschaft als Insolvenzforderung anzumelden.

3.2 Der Patron erklärt hilfsweise dass solche Forderungen — sollten sie
entstehen — den Forderungen aller anderen Gläubiger der Gesellschaft im
Range nachgehen (qualifizierter Rangrücktritt im Sinne von § 19 Abs. 2 S. 2
InsO).

3.3 Diese Verzichtserklärung ist unwiderruflich.

4. Bonitätsnachweis

Der Patron weist seine Leistungsfähigkeit durch folgende beigefuegte
Unterlagen nach:

 - Aktueller Vermögensstatus zum [Datum]
 - Bonitätsbescheinigung der Hausbank vom [Datum]
 - [weitere Belege]

5. Direktdurchgriff für Gläubiger der Gesellschaft

5.1 Die Gesellschaft kann diese Patronatserklärung Gläubigern und
Lieferanten gegenüber offenlegen und als Sicherheit benennen.

5.2 [optional] Gläubiger der Gesellschaft können unmittelbar Erfüllung
vom Patron verlangen wenn die Gesellschaft ihrer Verpflichtung nicht
nachkommt.

6. Form und Wirksamkeit

6.1 Schriftform ist Wirksamkeitsvoraussetzung.

6.2 Änderungen Ergänzungen und Aufhebungen bedürfen der Schriftform.

6.3 Gerichtsstand: [Sitz der Gesellschaft].

[Ort], [Datum]

___________________________
[Patron]


___________________________
[Geschäftsführer]
für die Gesellschaft
```

## Wichtige Hinweise

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Eine harte externe Patronatserklärung wirkt als **eigene Verpflichtung** des Patrons gegenüber der Gesellschaft oder ggue Gläubigern. Sie ist im Status der Gesellschaft als **Aktivposten** (Forderung gegen den Patron) zu berücksichtigen.

### Insolvenzanfechtung

Wenn der Patron später selbst in Insolvenz gerät kann die Patronatserklärung als **anfechtbar** behandelt werden wenn sie kurz vor seiner Insolvenz erfolgt ist. Daher Bonität des Patrons kritisch.

### Steuerrechtliche Folge beim Patron

Die Patronatszahlung an die Gesellschaft ist beim Patron regelmäßig **nicht abzugsfähig** als Einkommensteuer-Aufwand — sondern oft als verdeckte Einlage zu betrachten (verlangt Bewertung prüfen mit Steuerberater).

### Comfortletter NICHT ausreichend

Eine **weiche** Patronatserklärung (Comfortletter, "Best Effort"-Erklärung) genügt **nicht** für die Berücksichtigung im Status. Sie wirkt nur reputationell.

## Ausgabe

- `patronatserklaerung-extern-hart.docx` und PDF.
- Hinweis Patron Bonität prüfen.
- Eintragung im Sanierungsbausteine-Tracker mit Status: zur Unterschrift bereitgestellt.
- Wiedervorlage in einer Woche zur Prüfung ob unterschrieben.


## Aktuelle Leitentscheidungen — Patronatserklaerung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Patronatserklaerung

§ 19 Abs. 2 InsO (Fortbestehensprognose — externe Unternehmenssiherung) → § 311 BGB (Schuldrechtlicher Vertrag Patronatserklaerung) → § 241 Abs. 2 BGB (Schutzpflichten) → § 765 BGB analog (Buergschaft-Aspekte)

## Triage — Patronatserklaerung-Pruefung

1. **Hard oder soft?** Harte externe Patronatserklaerung = klagbarer Anspruch; weiche = kein Status-Effekt.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Unwiderruflich?** Widerrufliche Erklaerung reicht nicht fuer Ueberschuldungsstatus.
4. **Patron bonitaer?** Aktuelle Bonitats-Pruefung des Patrons erforderlich.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

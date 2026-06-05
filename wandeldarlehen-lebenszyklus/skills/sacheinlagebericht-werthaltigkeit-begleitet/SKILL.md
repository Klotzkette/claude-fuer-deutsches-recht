---
name: sacheinlagebericht-werthaltigkeit-begleitet
description: "Sacheinlagebericht Werthaltigkeit Begleitet: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sacheinlagebericht Werthaltigkeit Begleitet

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Sacheinlagebericht Werthaltigkeit Begleitet** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `sacheinlagebericht-werthaltigkeit` | Sacheinlagebericht für Sachkapitalerhohung durch Wandeldarlehen erstellen und Werthaltigkeit prufen. § 56 GmbHG Sacheinlage §§ 19 8 GmbHG Einlageverpflichtung. Prüfraster: Sacheinlagegegenstand Bewertung Werthaltigkeit Bericht Unterschrift. Output: Sacheinlagebericht Bewertungsgrundlage. Abgrenzung: nicht für Beurkundungsfragen (beurkundungserfordernis-prüfung). |
| `spezial-begleitet-erstpruefung-und-mandatsziel` | Begleitet: Erstprüfung, Rollenklärung und Mandatsziel im Plugin wandeldarlehen lebenszyklus; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Sacheinlagebericht Werthaltigkeit Begleitet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `sacheinlagebericht-werthaltigkeit`

**Fokus:** Sacheinlagebericht für Sachkapitalerhohung durch Wandeldarlehen erstellen und Werthaltigkeit prufen. § 56 GmbHG Sacheinlage §§ 19 8 GmbHG Einlageverpflichtung. Prüfraster: Sacheinlagegegenstand Bewertung Werthaltigkeit Bericht Unterschrift. Output: Sacheinlagebericht Bewertungsgrundlage. Abgrenzung: nicht für Beurkundungsfragen (beurkundungserfordernis-prüfung).

# Sacheinlagebericht und Werthaltigkeit der Forderung

## Zweck

Dieser Skill erstellt den Sacheinlagebericht und prüft die Werthaltigkeit der als Sacheinlage einzubringenden Forderung aus dem Wandeldarlehen (Darlehen + aufgelaufene Zinsen). Phase D des Lebenszyklus.

## Eingaben

- Wandlungssumme (Darlehensbetrag + aufgelaufene Zinsen)
- Aktuelle Bilanz der Gesellschaft (letzte Jahresabschluss oder aktuelle BWA)
- Zahlungsfähigkeit der Gesellschaft (Liquiditätsstand)
- Forderungsbewertung: Ist die Forderung des Lenders werthaltig (d.h. nicht ausfallgefährdet)?
- Steuerberater: bereits mit Werthaltigkeitsprüfung beauftragt?
- Qualifizierter Rangrücktritt: gilt er weiterhin bis zur Eintragung?

## Rechtlicher Rahmen

### Primärnormen
- § 9 GmbHG (Differenzhaftung Gesellschafter bei Überbewertung der Sacheinlage)
- § 57 Abs. 2 Satz 1 GmbHG i.V.m. § 8 Abs. 2 Satz 1 GmbHG (Versicherung der Geschäftsführer in der HR-Anmeldung der Kapitalerhöhung, dass die Einlagen ordnungsgemäß bewirkt und endgültig zur freien Verfügung der Geschäftsführer stehen)
- § 9a GmbHG i.V.m. § 57 Abs. 4 GmbHG analog (Schadensersatzpflicht der Geschäftsführer gegenüber der Gesellschaft bei falschen Angaben oder verschwiegenen Tatsachen im Rahmen der Anmeldung)
- § 57a GmbHG i.V.m. § 9c GmbHG (Prüfungsrecht des Registergerichts; Eintragung darf bei nicht unwesentlich überbewerteter Sacheinlage versagt werden)
- § 56 GmbHG (Sacheinlage: Leistung muss vor Anmeldung erbracht/gesichert sein)
- § 56a GmbHG (Sacheinlagebericht analog Sachgründungsbericht § 5 Abs. 4 GmbHG bei Kapitalerhöhung gegen Sacheinlage)
- § 82 GmbHG (Strafbarkeit falscher Angaben in HR-Anmeldung)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage)
- IDW RS HFA 42 (Werthaltigkeit von Forderungen als Sacheinlage)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Forderungsbewertung
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 2. Konfusions-Argument
Bei der Einbringung der Forderung als Sacheinlage geht die Forderung auf die Gesellschaft über (Konfusion, § 1976 BGB analog). Die Forderung erlischt, gleichzeitig entsteht das neue Eigenkapital. Werthaltigkeitsfrage: War die Forderung gegen die Gesellschaft vor Konfusion vollwertig?

### 3. Rangrücktritt und Werthaltigkeit
Hinweis: Der qualifizierte Rangrücktritt schränkt die Durchsetzbarkeit der Forderung ein. Dies könnte die Werthaltigkeit reduzieren. Gegenargument: Durch die Wandlung / Einbringung als Eigenkapital wird der Rangrücktritt gerade aufgehoben – der Wert ist der Nennwert der Forderung.

### 4. Sacheinlagebericht erstellen
Inhalt: (a) Beschreibung der Sacheinlage (Art der Forderung, Betrag, Fälligkeit), (b) Bewertungsgrundlagen (Buchwert, Marktwert, Plausibilisierung), (c) Ergebnis der Werthaltigkeitsprüfung, (d) Unterschrift Geschäftsführerin und ggf. Steuerberater.

### 5. Differenzhaftungs- und Geschäftsführer-Haftungsrisiko
Falls Forderung überbewertet eingebracht wird (z. B. Buchwert EUR 275694, tatsächlicher Wert EUR 200000 wegen Ausfallrisiko): Differenzhaftung der einbringenden Gesellschafterin / des Lenders i.H.d. Differenz (§ 9 GmbHG). Zusätzlich Geschäftsführer-Eigenhaftung aus **§ 9a GmbHG i.V.m. § 57 Abs. 4 GmbHG** analog, wenn die in der HR-Anmeldung nach **§ 57 Abs. 2 i.V.m. § 8 Abs. 2 GmbHG** abzugebende Versicherung (Einlagen bewirkt und zur freien Verfügung der Geschäftsführung) wahrheitswidrig oder unter Verschweigung wesentlicher Umstände erfolgt; strafrechtlich flankiert durch § 82 GmbHG (falsche Angaben). Registergericht prüft Werthaltigkeit nach § 57a i.V.m. § 9c GmbHG. Gegenstrategie: konservative Bewertung, dokumentierte Bewertungsgrundlage (Bilanz, BWA, Liquiditätsstatus), externe Plausibilisierung durch Steuerberater oder Wirtschaftsprüfer.

### 6. Vorlage beim Notar
Sacheinlagebericht wird dem Kapitalerhöhungsbeschluss als Anlage beigefügt und dem Handelsregister übermittelt.

## Muster-Sacheinlagebericht (Auszug)

```
SACHEINLAGEBERICHT
zur Kapitalerhöhung der Sonnenglas Solartechnologie UG (haftungsbeschränkt)

Einzubringende Sacheinlage:
Forderung der Northstar Pre-Seed Partners GmbH & Co. KG gegen die Gesellschaft
aus dem Wandeldarlehensvertrag vom [Datum] in Höhe von EUR 275694
(Darlehensbetrag EUR 250000 zuzüglich aufgelaufener Zinsen EUR 25694).

Bewertung:
Die Forderung ist werthaltig. Die Gesellschaft verfügt gemäß BWA vom [Datum]
über liquide Mittel in Höhe von EUR [●] und ist zahlungsfähig. Die Forderung
entspricht ihrem Nennwert von EUR 275694. Eine Überbewertung liegt nicht vor.

[Ort, Datum]
[Unterschrift Geschäftsführerin Dr. Mira Schoeneck]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Gesellschaft überschuldet oder zahlungsunfähig | Werthaltigkeit der Forderung fraglich, Differenzhaftung § 9 GmbHG | Liquidität knapp | Gesellschaft klar zahlungsfähig |
| Kein Sacheinlagebericht | HR-Eintragung scheitert | Bericht unvollständig | Vollständiger Bericht |
| Rangrücktritt noch aktiv bei Einbringung | Werthaltigkeit strittig | Rangrücktritt wird zeitgleich aufgehoben | Klar aufgehoben |
| Differenzhaftungsrisiko ignoriert | Persönliche Haftung Lender/Gesellschafterinnen | Risiko bekannt aber nicht quantifiziert | Konservative Bewertung |
| GF-Versicherung in HR-Anmeldung ohne Plausibilisierung | § 9a i.V.m. § 57 IV GmbHG-Haftung GF, § 82 GmbHG strafrechtlich | Versicherung dünn dokumentiert | Plausibilisierung durch StB/WP dokumentiert |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/rangruecktritt-formulieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen und Updates

Stand: 05/2026.
- § 9 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__9.html
- § 9a GmbHG: https://www.gesetze-im-internet.de/gmbhg/__9a.html
- § 19 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__19.html
- § 56 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__56.html
- § 56a GmbHG: https://www.gesetze-im-internet.de/gmbhg/__56a.html
- § 57 GmbHG (Anmeldung Kapitalerhoehung): https://www.gesetze-im-internet.de/gmbhg/__57.html
- § 57a GmbHG iVm § 9c GmbHG (Pruefungspflicht Registergericht): https://www.gesetze-im-internet.de/gmbhg/__9c.html
- § 82 GmbHG (Strafbarkeit falscher Angaben): https://www.gesetze-im-internet.de/gmbhg/__82.html
- § 272 II Nr. 4 HGB (Kapitalruecklage): https://www.gesetze-im-internet.de/hgb/__272.html
- IDW S 1 / IDW RS HFA 42 (Werthaltigkeit von Forderungen): https://www.idw.de/idw/idw-verlautbarungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `spezial-begleitet-erstpruefung-und-mandatsziel`

**Fokus:** Begleitet: Erstprüfung, Rollenklärung und Mandatsziel im Plugin wandeldarlehen lebenszyklus; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Begleitet: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Begleitet: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Begleitet: Erstprüfung, Rollenklärung und Mandatsziel / begleitet erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UG/GmbH ist Gesellschaftsform, keine Einzelquelle. Prüfe GmbHG §§ 5a, 7, 8, 16, 19, 55 ff.; BGB §§ 488 ff. und 311; ggf. WpPG/VermAnlG/KAGB, GwG, Steuerrecht und notarielle/registerrechtliche Anforderungen live.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Begleitet** prüfen.
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

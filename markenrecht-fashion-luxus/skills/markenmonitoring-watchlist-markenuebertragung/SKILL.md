---
name: markenmonitoring-watchlist-markenuebertragung
description: "Markenmonitoring Watchlist Markenuebertragung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Markenmonitoring Watchlist Markenuebertragung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Markenmonitoring Watchlist Markenuebertragung** im Plugin Markenrecht Fashion/Luxus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `markenmonitoring-und-watchlist` | Markenmonitoring und Watchlist-Dienste einrichten: Modehaus will Fruehwarnung bei Trittbrettfahrer-Anmeldungen. Normen: § 14 MarkenG (Verletzungsschutz), Art. 9 UMV, Madrid-Monitor WIPO. Prüfraster: DPMA/EUIPO/WIPO-Watch-Konfiguration, Alert-Parameter (Klassen, Aehnlichkeitsgrad), ROMARIN-Datenbank. Output Watchlist-Konfigurationsempfehlung, Monitoring-Service-Auswahl, Alert-Workflow. Abgrenzung: Widerspruch nach Alert siehe dpma-widerspruch-und-löschung, euipo-widerspruchsverfahren; Konkurrenten-Monitoring Patent siehe ueberwachung-konkurrenten. |
| `markenuebertragung-chain-of-title` | Markenübertragung und Chain-of-Title prüfen: Asset Deal, Share Deal, Konzernumhängung, Registerumschreibung, Vollmachten, Prioritätsrechte, Lizenzen, Sicherheiten und internationale Portfolios. |
| `marketplace-notice-action-dsa` | Marketplace-Enforcement nach MarkenG und Digital Services Act: Notice-and-Action, Trusted Flagger, Plattformhaftung, Wiederholungstäter, Belegpaket, Gegenanzeige und Eskalation gegen Online-Marktplätze. |
| `messe-verletzung-und-gv-einsatz` | Markenverletzung auf Messen (Pitti Uomo, Berlin Fashion Week) schnell unterbinden: Eilantrag und Gerichtsvollzieher-Einsatz vorbereiten. Normen: §§ 935 und 940 ZPO (einstweilige Verfuegung), § 19 MarkenG (Auskunftsanspruch), § 18 MarkenG (Vernichtungsanspruch), § 14 MarkenG. Prüfraster: Dringlichkeit, Schutzschrift einreichen, GV-Sicherstellung, Auskunfts-Durchsetzung. Output Antrag auf einstweilige Verfuegung, Schutzschrift, GV-Beauftragungsschreiben. Abgrenzung: Außergerichtliche Abmahnung siehe abmahnung-markenrecht-uwg; Plattform-Verletzung siehe plattform-piraterie-donauzon. |

## Arbeitsweg

Im Plugin Markenrecht Fashion/Luxus gilt für **Markenmonitoring Watchlist Markenuebertragung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `markenmonitoring-und-watchlist`

**Fokus:** Markenmonitoring und Watchlist-Dienste einrichten: Modehaus will Fruehwarnung bei Trittbrettfahrer-Anmeldungen. Normen: § 14 MarkenG (Verletzungsschutz), Art. 9 UMV, Madrid-Monitor WIPO. Prüfraster: DPMA/EUIPO/WIPO-Watch-Konfiguration, Alert-Parameter (Klassen, Aehnlichkeitsgrad), ROMARIN-Datenbank. Output Watchlist-Konfigurationsempfehlung, Monitoring-Service-Auswahl, Alert-Workflow. Abgrenzung: Widerspruch nach Alert siehe dpma-widerspruch-und-löschung, euipo-widerspruchsverfahren; Konkurrenten-Monitoring Patent siehe ueberwachung-konkurrenten.

# Markenmonitoring und Watchlist-Dienste

## Fachkern: Markenmonitoring und Watchlist-Dienste
- **Spezialgegenstand:** Markenmonitoring und Watchlist-Dienste; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Eine eingetragene Marke, die nicht überwacht wird, ist wie ein Schloss ohne Wächter. Für klôtzzkètté SA habe ich ein mehrschichtiges Monitoring-System aufgebaut: tägliche Alerts für DPMA und EUIPO, wöchentliche WIPO-Scans, monatliche Domain-Monitoring und quartalsweise Social-Media-Screenings.

Die Widerspruchsfrist beträgt nur 3 Monate (EUIPO) bzw. 3 Monate (DPMA) ab Veröffentlichung. Wer diese Frist verpasst, verliert die Chance auf das effizienteste Abwehrinstrument.

## Rechtsrahmen

- **§ 42 MarkenG:** Widerspruchsfrist 3 Monate ab Veröffentlichung (DPMA) — MONITORING PFLICHT
- **Art. 46 UMV:** Widerspruchsfrist 3 Monate ab Veröffentlichung im EUIPO-Bulletin — MONITORING PFLICHT
- **Art. 5 PMMA:** Madrid-Protokoll Widerspruchsfrist je nach Bestimmungsland (US: 30 Tage nach Publication in OG für Opposition)
- **§ 49 MarkenG:** Beobachtung fremder Marken auf Verfallsreife (5-Jahres-Benutzungspflicht)
- **§ 12 BGB:** Namensrecht — Monitoring für Unternehmens-/Personennamen
- **DSA Art. 16 ff. VO (EU) 2022/2065:** Online-Monitoring auf Plattformen (vgl. Skill `plattform-piraterie-donauzon`)

## Monitoring-Ebenen

### Ebene 1: Markenanmeldungs-Monitoring (Kern-Monitoring)

**DPMA:**
- DPMA-Markenblatt: wöchentlich, Klassen 3/14/18/25/35 (Kern-Überwachungsklassen klôtzzkètté)
- DPMA-Newsletter: kostenfrei, E-Mail-Benachrichtigung bei neuen Veröffentlichungen
- DPMAregister: manuelle Suche nach phonetischen Ähnlichkeiten
- Professioneller Watch-Dienst (z.B. Dennemeyer Watch, Brand Monitor, MARKIFY): tägliche Alerts

**EUIPO:**
- EUIPO TMview Watch: kostenpflichtige Überwachung; automatische Alerts bei ähnlichen Anmeldungen
- EUIPO eWatch: EU-spezifisch, nach Nizza-Klassen und Suchbegriffen konfigurierbar
- BoA-Datenbank: Verfolgen von Beschwerden mit klôtzzkètté-Relevanz

**WIPO/Madrid:**
- WIPO Global Brand Database: Suche nach phonetischen/visuellen Ähnlichkeiten
- WIPO ROMARIN (Replace by Madrid Monitor): Verfolgen aller Madrid-IR-Anmeldungen
- Madrid Monitor: Statusverfolgung eigener IR-Marken

### Ebene 2: Domain-Monitoring

- Dienste: MarkMonitor, CSC Digital Brand Services, Clarabridge Domain Watch
- Überwachung: "klotzkette*" / "klotzzkette*" / "klôtzzkètté*" in allen TLDs (.de/.com/.eu/.fr/.it/.shop)
- Typosquatting-Varianten: klotzzkette, klotzkette, klotz-kette, klotz-kett etc.
- Reaktion bei Verletzung: UDRP-Beschwerde (für .com) oder DENIC-Dispute (für .de)

### Ebene 3: Social Media Monitoring

- Tools: Brandwatch, Mention, Talkwalker, Meltwater
- Überwachung: Markenname + Varianten, Hashtags, Influencer-Nutzung
- Fokus: Fälschungsverkäufe (Instagram Shops, TikTok Shop), irreführende Inhalte
- Reaktion: DSA-Notice (vgl. Skill `plattform-piraterie-donauzon`)

### Ebene 4: Zoll und Online-Marktplätze

- CBP IPR Center (US): eigene Marken in US CBP Recordation-Datenbank registriert? (vgl. `us-counterfeit-und-customs-cbp`)
- EUIPO-IP Enforcement Database: Zollbehörden-Interface mit AWA-Anträgen
- Donauzon Brand Registry: Markenverwaltung bei Donauzon (falls Kooperation möglich)
- Amazon Brand Registry: bei US/EU-Amazon-Präsenz

### Ebene 5: Wettbewerber-Beobachtung

- Regelmäßige Recherche nach neuen Anmeldungen von bekannten Gegenparteien (Brezelmann, Donauzon)
- Zeitschriften-Scan: Fashion Law publications, Markenanmeldungsstatistiken
- Messen: Berlin Fashion Week, Pitti Uomo, Paris Fashion Week — physisches Screening

## Prüfungsschritte

1. **Erstkonfiguration Watch-System:**
 - Alle eigenen Marken in Watch-Dienst eingeben
 - Suchbegriffe definieren: exakte Schreibweise + phonetische Varianten + visuelle Ähnlichkeiten
 - Klassen: Kernklassen 3/14/18/25/35 + erweiterte Klassen 9/41/42 (KI-Kontext)
 - Territorien: DE/AT/CH/FR/IT/ES/GB/US/JP/CN als Mindestdeckung

2. **Alert-Bearbeitung:**
 - Tägliche Alert-Prüfung (automatisch + manuell bei Unsicherheit)
 - Priorisierung: (a) identische Zeichen = sofort prüfen; (b) ähnliche Zeichen = innerhalb 48h; (c) entfernte Ähnlichkeit = wöchentlich
 - Widerspruchsentscheidung: spätestens in Monat 2 der 3-monatigen Frist

3. **Dokumentation:**
 - Alert-Log: Datum, gefundene Marke, Bewertung, Entscheidung
 - Widerspruchs-Tracking: Aktenzeichen, Fristen, Status
 - Jahresbericht an klôtzzkètté SA: Zusammenfassung Monitoring-Ergebnisse

4. **Kostenkontrolle:**
 - Professioneller Watch-Dienst: EUR 800-3.000/Jahr je nach Umfang
 - EUIPO eWatch: ab EUR 200/Jahr
 - DPMA-Newsletter: kostenfrei
 - Gesamtbudget Monitoring: ca. EUR 2.500-5.000/Jahr für umfassendes System

## Falltypische Konstellationen

### Konstellation 1: Alert "KLÖTZE-KETTÉ" in Klasse 25
Watch-Dienst meldet am 15.01.2025: Neue DPMA-Anmeldung "KLÖTZE-KETTÉ" durch Brezelmann Discount KG für Klasse 25. Sofortige Kollisionsanalyse: klanglich hoch ähnlich zu klôtzzkètté; Warenidentität. Widerspruch empfohlen, Frist: bis 15.04.2025. Sofortige Mandantenkommunikation und Widerspruchsvorbereitung.

### Konstellation 2: Madrid IR-Anmeldung "KLOTZETTE" für US-Markt
WIPO-Alert: Neue Madrid IR-Anmeldung mit Designation USA. US-Notifikation an USPTO. Koordination mit Whitman Brennan Forsythe NYC für US-Opposition beim TTAB (vgl. Skill `ttab-opposition-und-cancellation`).

### Konstellation 3: Domain "klotzkette.shop" registriert
Domain-Monitor meldet: "klotzkette.shop" soeben registriert, Inhaber anonym (Privacy Shield). Sofortiger UDRP-Antrag bei WIPO (für .shop-Domain): klôtzzkètté hat ältere Marke, Domain ist verwechslungsfähig, bösgläubige Registrierung vermutet.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Aktuelle Rechtsprechung zum Markenmonitoring

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Templates

### Watchlist-Konfigurationsdatei (intern)
```
KLÔTZZKÈTTÉ SA — WATCHLIST-KONFIGURATION

Eigene Zeichen (überwacht):
- klôtzzkètté (Wortmarke)
- klotzkette / klotzzkette (ASCII-Varianten)
- Doppel-K-Signet (Bildmarke — Visuell-Watch)

Such-Algorithmus-Parameter:
- Phonetisch ähnlich: max. Levenshtein-Distanz 3
- Visuell ähnlich: Logo-Ähnlichkeit > 70 %
- Klassen: 3/14/18/25/35 (primär); 9/41/42 (sekundär)

Territorien: DE/EU/US/JP/CN/GB/CH/FR/IT/AE

Reaktions-SLA:
- Identisch: 24h
- Sehr ähnlich: 48h
- Ähnlich: 7 Tage
- Entfernt ähnlich: monatliche Batchbeurteilung
```

## Verweise auf andere Skills

- `dpma-widerspruch-und-loeschung` — Reaktion auf neue DPMA-Anmeldungen
- `euipo-widerspruchsverfahren` — Reaktion auf neue EUIPO-Anmeldungen
- `ttab-opposition-und-cancellation` — Reaktion auf US-Anmeldungen
- `fashion-luxus-kaltstart-interview` — Monitoring als Teil des IP-Audits

## Risiken & Stolperfallen

- **Versäumte Widerspruchsfrist:** Das größte Risiko im Monitoring — kein Monitoring = verpasster Widerspruch = dauerhafter Rechtsverlust
- **False Positives:** Zu breite Suchparameter generieren zu viele Alerts → Fatigue; sorgfältige Kalibrierung
- **Domain-Privacy-Shields:** Anonyme Domainhaber erschweren UDRP — WHOIS-Lookup + UDRP-Registrar-Daten oft der einzige Weg
- **Monitoring ≠ Registrierung:** Monitoring ersetzt keine Markenanmeldung in neuen Märkten — beide müssen parallel laufen

## 2. `markenuebertragung-chain-of-title`

**Fokus:** Markenübertragung und Chain-of-Title prüfen: Asset Deal, Share Deal, Konzernumhängung, Registerumschreibung, Vollmachten, Prioritätsrechte, Lizenzen, Sicherheiten und internationale Portfolios.

# Markenübertragung und Chain of Title

## Fachkern: Markenübertragung und Chain of Title
- **Spezialgegenstand:** Markenübertragung und Chain of Title; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Aufgabe

Prüfe, ob Markenrechte wirksam übertragen wurden und ob Register, Verträge und tatsächliche Nutzung zusammenpassen.

## Normanker

- MarkenG §§ 27, 28 für Übertragung, Rechtsübergang und Registervermutung.
- MarkenG § 30 für Lizenzen; bestehende Lizenzrechte können den wirtschaftlichen Wert und die Durchsetzung prägen.
- UmwG/InsO/BGB je nach Transaktionsgrund: Verschmelzung, Spaltung, Asset Deal, Insolvenzverkauf, Sicherheitenfreigabe.
- Internationale Register (EUIPO, WIPO Madrid, nationale Ämter) live prüfen; Umschreibungsformalien unterscheiden sich.

## Pflichtfragen

- Welche Marken, Register, Länder, Klassen und Inhaber?
- Asset Deal, Share Deal, Verschmelzung, Umwandlung, Insolvenz, Sicherheit oder Konzernreorganisation?
- Übertragungsvertrag, Anlagen, Vollmachten, Registeranträge, Gebühren?
- Bestehende Lizenzen, Sicherheiten, Streitigkeiten, Widersprüche?

## Prüfprogramm

1. **Rechtsinhaber feststellen:** Registerstand vs. Vertrag vs. tatsächliche Brand-Nutzung.
2. **Übertragungsgegenstand:** Marke, Anmeldungen, Prioritäten, Domains, Designs, Copyright, Know-how, Goodwill.
3. **Formalia:** Schriftform/Unterschrift, Vertretungsmacht, Apostille/Legalisation, Übersetzungen, Registerumschreibung.
4. **Lücken suchen:** Falsche Inhaberin, alte Umfirmierung, fehlende Anlage, vergessene IR-Benennung, Lizenzbindung.
5. **Closingfähigkeit:** Conditions precedent, Bring-down, Vollmachten, Post-Closing-Registerplan.
6. **Vertretungsmacht:** Geschäftsführer, Insolvenzverwalter, Liquidator, Trustee, Notarvollmacht, Apostille/Legalisation und Registerfähigkeit gesondert sichern.
7. **Nebenassets:** Domains, Social Handles, Produktdesigns, Werbematerial, Datenbanken und Goodwill nicht stillschweigend als "Marke" behandeln.

## Output

- Chain-of-Title-Memo.
- Register-Umschreibungsplan.
- Closing-Checkliste.
- Red-Flag-Liste.

## Qualitätsregeln

Registerdaten live prüfen. Keine Annahme, dass Registerumschreibung materiellrechtliche Übertragung ersetzt oder umgekehrt.

## 3. `marketplace-notice-action-dsa`

**Fokus:** Marketplace-Enforcement nach MarkenG und Digital Services Act: Notice-and-Action, Trusted Flagger, Plattformhaftung, Wiederholungstäter, Belegpaket, Gegenanzeige und Eskalation gegen Online-Marktplätze.

# Marketplace Notice-and-Action

## Fachkern: Marketplace Notice-and-Action
- **Spezialgegenstand:** Marketplace Notice-and-Action; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Aufgabe

Führe Markeninhaber durch Plattformmeldungen gegen Fälschungen, Trittbrettfahrer-Angebote und rechtsverletzende Listings.

## Norm- und Plattformanker

- MarkenG §§ 14, 15, 18, 19 für Verletzung, Entfernung/Rückruf und Auskunft.
- Digital Services Act (VO (EU) 2022/2065), besonders Art. 16 Notice-and-Action, Art. 20 Beschwerdemanagement und Art. 22 Trusted Flagger.
- Produktsicherheits-/Zollrecht nur ziehen, wenn Fälschung, gefährliches Produkt oder Grenzbeschlagnahme betroffen ist.
- Plattformregeln live prüfen: Amazon Brand Registry, eBay VeRO, Meta/TikTok/Google IP-Formulare, Marketplace-Policy, Counter-Notice.

## Pflichtfragen

- Plattform, Listing-URL, Verkäufer, Land, Waren, Screenshots, Testkauf?
- Eingetragenes Recht mit Registerauszug und Markeninhaber?
- Welche Verletzung: Counterfeit, identisches Zeichen, Verwechslungsgefahr, Rufausbeutung, Irreführung?
- Vorherige Meldungen, Reaktion, Wiederholungstäter, Eilbedarf?

## Prüfprogramm

1. **Belegpaket bauen:** Registerauszug, Vollmacht, Screenshots, Produktvergleich, Testkauf, Seriennummern.
2. **DSA-Notice:** Präzise Rechtsverletzung, URL, Erklärung der Gutgläubigkeit, Kontakt, gewünschte Maßnahme.
3. **Plattformprozess:** Brand Registry, IP-Portal, DSA-Meldung, Trusted Flagger, Beschwerde gegen Ablehnung.
4. **Gegenschlag einplanen:** Counter-Notice, Account-Sperre des Mandanten, unberechtigte Schutzrechtsverwarnung.
5. **Eskalation:** Abmahnung Verkäufer, Auskunft, einstweilige Verfügung, Plattform als Störer/Intermediär nur quellengeprüft bewerten.
6. **Overblocking vermeiden:** Nur konkrete Listings/Verkäufer melden, keine pauschale Marktbereinigung ohne Schutzrechts- und Belegbasis.
7. **Wiederholungstäter:** Verkäufer-ID, USt-ID, Impressum, Lieferadresse, Zahlungsdaten, verbundene Shops und Testkäufe zusammenführen.

## Output

- DSA-/Plattformmeldung.
- Belegmatrix.
- Eskalationsplan.
- Risikoanalyse für Overblocking.

## Qualitätsgate

DSA und Plattformregeln live prüfen; keine Plattformformulare aus Gedächtnis behaupten.

## 4. `messe-verletzung-und-gv-einsatz`

**Fokus:** Markenverletzung auf Messen (Pitti Uomo, Berlin Fashion Week) schnell unterbinden: Eilantrag und Gerichtsvollzieher-Einsatz vorbereiten. Normen: §§ 935 und 940 ZPO (einstweilige Verfuegung), § 19 MarkenG (Auskunftsanspruch), § 18 MarkenG (Vernichtungsanspruch), § 14 MarkenG. Prüfraster: Dringlichkeit, Schutzschrift einreichen, GV-Sicherstellung, Auskunfts-Durchsetzung. Output Antrag auf einstweilige Verfuegung, Schutzschrift, GV-Beauftragungsschreiben. Abgrenzung: Außergerichtliche Abmahnung siehe abmahnung-markenrecht-uwg; Plattform-Verletzung siehe plattform-piraterie-donauzon.

# Markenverletzung auf Messen und Gerichtsvollzieher-Einsatz

## Fachkern: Markenverletzung auf Messen und Gerichtsvollzieher-Einsatz
- **Spezialgegenstand:** Markenverletzung auf Messen und Gerichtsvollzieher-Einsatz; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Auf der Berlin Fashion Week 2024: Ein Stand von Donauzon Marketplace GmbH zeigt gefälschte klôtzzkètté-Taschen, Schal-Kollektionen mit dem Doppel-K-Signet und Parfumflakons, die dem K°°-Flakon täuschend ähnlich sehen. Die Comtesse Beatrice de Klotzzkettie ruft mich um 8:00 Uhr morgens an. Um 11:00 Uhr liegt der Eilantrag beim LG Berlin vor.

Messe-Verletzungen erfordern blitzschnelles Handeln: Die Ware verschwindet nach der Messe — und der Beweis mit ihr.

## Rechtsrahmen

- **§ 14 II/V MarkenG:** Verletzungsverbotstatbestand; Unterlassungsanspruch
- **§ 18 MarkenG:** Vernichtungsanspruch (Ware vernichten oder aussondern)
- **§ 19 MarkenG:** Auskunftsanspruch (Lieferkette, Mengen, Bezugsquellen)
- **§ 19a MarkenG:** Vorlage- und Besichtigungsanspruch (Sicherungszwecke)
- **§§ 935/940 ZPO:** Einstweilige Verfügung (Verfügungsgrund: Eilbedürftigkeit; Verfügungsanspruch: glaubhafter Verletzungstatbestand)
- **§§ 916/917 ZPO:** Arrest (Sicherungsarrest für Schadensersatzansprüche)
- **§§ 753/759 ZPO:** Gerichtsvollzieher-Vollstreckung/Sicherstellung
- **Schutzschrift (§ 945a ZPO / Schutzschriftenregister):** Präventive Eingabe des Beklagten bei Gericht vor Erlass einer einstweiligen Verfügung
- **Messeprivileg:** Bei ausländischen Messegästen: Internationale Zuständigkeit nach EuGVVO Art. 7 Nr. 2 (Tatortprinzip), Durchführungsverordnung zu §§ 110/111 MarkenG (Schutz ausländischer Staatsangehöriger auf deutschen Messen)

## Prüfungsschritte

### Phase 1: Sofortmaßnahmen vor Ort (Messe-Tag)

1. **Beweissicherung:**
 - Fotos und Videos der verletzenden Waren (Zeitstempel!)
 - Testkauf (Kaufbeleg aufbewahren)
 - Visitenkarte / Aussteller-Daten vom Messekatalog
 - Zeugen benennen (Messepersonal, Mitarbeiter klôtzzkètté)

2. **Verständigung der Messe-Sicherheit:**
 - Messe-Direktion informieren (meist sofortige Unterstützung bei nachgewiesener Markenverletzung)
 - Ausstellerregistrierung: Stand-Inhaber und Verantwortlicher identifizieren

3. **Sofortige Unterrichtung der Kanzlei:**
 - Bilder, Kaufbeleg, Ausstellerdaten sofort übermitteln
 - Parallele Prüfung: Schutzschriften-Register (zentrale Schutzschriften-Datenbank ZSSR) auf Schutzschrift des Gegners prüfen

### Phase 2: Eilantrag (innerhalb von Stunden)

4. **Abwägung: Abmahnung zuerst oder direkt zum Gericht?**
 - Bei klarer Fälschung (Produktpiraterie): direkt einstweilige Verfügung ohne Abmahnung
 - Begründung Eilbedürftigkeit: Messeende droht; Ware verlässt nach Messe das Land

5. **Antrag auf Erlass einstweiliger Verfügung (§§ 935/940 ZPO):**
 - Verfügungsanspruch: § 14 V MarkenG (Unterlassung)
 - Verfügungsgrund: Eilbedürftigkeit — Messe endet in 2/3 Tagen
 - Glaubhaftmachung durch Anwaltseidesstattliche Versicherung + Fotos + Kaufbeleg
 - Beantragung beim zuständigen LG (Messestadt: LG Berlin / LG Frankfurt / LG München I)

6. **Gerichtsvollzieher-Beauftragung (§§ 753/759 ZPO):**
 - Nach Erlass der einstweiligen Verfügung: GV-Beauftragung mit Vollstreckungsauftrag
 - Messestand aufsuchen, Waren sicherstellen
 - GV-Protokoll = gesicherter Beweis

7. **Ordnungsmittelantrag (§ 890 ZPO):**
 - Bei Zuwiderhandlung nach Zustellung der einstweiligen Verfügung
 - Ordnungsgeld bis EUR 250.000 oder Ordnungshaft

### Phase 3: Hauptsacheverfahren und Abwicklung

8. **Auskunftsklage (§ 19 MarkenG):**
 - Lieferkette: Hersteller, Importeure, Vorbesitzer
 - Mengen: Stückzahlen produzierten und gelieferten Ware
 - Grundlage für Schadensersatz

9. **Vernichtung (§ 18 MarkenG):**
 - Gefälschte Ware vernichten oder unbrauchbar machen
 - Gerichtliche Anordnung erforderlich (kein Selbstvollzug!)

## Falltypische Konstellationen

### Konstellation 1: Donauzon-Stand auf der Berlin Fashion Week
Donauzon Marketplace GmbH präsentiert auf der Berlin Fashion Week in Halle 2 gefälschte klôtzzkètté-Handtaschen. Testkauf à EUR 89 (Original: EUR 2.400). Eilantrag LG Berlin um 11:00 Uhr; Erlass Verfügung noch am Nachmittag; GV-Einsatz nächsten Morgen. Ergebnis: 847 Stück gefälschte Ware sichergestellt.

### Konstellation 2: Brezelmann auf der Düsseldorf Neonyt
Brezelmann Discount KG präsentiert auf einer Düsseldorfer Modemesse Schal-Kollektion mit dem klôtzzkètté-ähnlichen Muster. Nicht Produktpiraterie, sondern Markenverletzung durch ähnliches Zeichen. Strategie: Abmahnung vor Ort, strafbewehrte Unterlassungserklärung — wenn verweigert: einstweilige Verfügung LG Düsseldorf.

### Konstellation 3: Ausländischer Aussteller auf Pitti Uomo Florenz
Chinesischer Hersteller zeigt auf der Pitti Uomo in Florenz klôtzzkètté-Kopien. Zuständigkeit: Tribunale di Firenze (italienische Zuständigkeit). Abstimmung mit Whitman Brennan Forsythe NYC für US-Parallelvorgehen; Kooperation mit Mailänder Korrespondenzkanzlei für IT-Enforcement.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### Antragsschrift einstweilige Verfügung (Messe)
```
An das Landgericht [Berlin/Frankfurt/München I]
Kammer für Handelssachen / Zivilkammer

Antrag auf Erlass einer einstweiligen Verfügung
Antragstellerin: klôtzzkètté SA, Paris, vertr. durch RA'in [Name]
Antragsgegnerin: [Donauzon/Brezelmann], [Adresse Messestand]

I. ANTRAG
Es wird beantragt, der Antragsgegnerin im Wege der einstweiligen
Verfügung zu untersagen, im geschäftlichen Verkehr Waren mit dem
Zeichen [KLOTZ-KETTEN / Abbildung] anzubieten, zu vertreiben oder
zu bewerben, insbesondere auf der [Messe], [Datum], Stand [Nr.].

II. VERFÜGUNGSANSPRUCH (§ 14 V MarkenG)
[...]

III. VERFÜGUNGSGRUND (§§ 935/940 ZPO)
Messeende: [Datum]. Nach Messeende verlassen die Waren die
Bundesrepublik und sind für Vollstreckungsmaßnahmen nicht mehr
erreichbar. Eilbedürftigkeit liegt auf der Hand.

IV. GLAUBHAFTMACHUNG
- Eidesstattliche Versicherung RA'in [Name] (Anlage 1)
- Fotografische Beweise (Anlage 2-7)
- Testkauf-Quittung (Anlage 8)
- Auszug Markenregister DPMA/EUIPO (Anlage 9-10)
```

## Verweise auf andere Skills

- `abmahnung-markenrecht-uwg` — Wenn Abmahnung vor Gericht möglich und sinnvoll
- `produktpiraterie-und-zoll` — Parallelmaßnahmen Zollrecht
- `plattform-piraterie-donauzon` — Online-Verletzungen durch Donauzon

## Risiken & Stolperfallen

- **Beweissicherung SOFORT:** Fotos/Video unmittelbar nach Entdeckung — keine stundenlange Abwartehaltung
- **Dringlichkeitsfrist:** Nach BGH gilt: Wer mit Verletzung länger als 4-6 Wochen zuwartet, verwirkt die Eilbedürftigkeit (sog. Dringlichkeitsschädlichkeit). Bei Messeverletzung: Keine Duldung, sofort handeln
- **Schutzschrift des Gegners:** Donauzon könnte vorab Schutzschrift hinterlegt haben → ZSSR prüfen
- **GV-Zugang Messestand:** Gerichtsvollzieher braucht Zugang; Messe-Direktion vorab einbinden
- **Internationale Aussteller:** EuGVVO-Zuständigkeit bei EU-Ausländern; außerhalb EU: Haager Zustellungsübereinkommen beachten

## Triage-Fragen bei Messeverletzung

Bevor der Eilantrag gestellt wird, klaere:
1. Ist die Beweissicherung vollstaendig (Fotos mit Zeitstempel, Testkauf, Ausstellerdaten)?
2. Ist das Gericht des Messeorts zustaendig (LG Berlin/Frankfurt/Duesseldorf/Muenchen I)?
3. Wann endet die Messe — genuegt die Zeit fuer Antrag und Erlass noch am Messtag?
4. Hat der Verletzer moglicherweise bereits eine Schutzschrift im ZSSR hinterlegt?
5. Handelt es sich um Produktpiraterie (direkte einstweilige Verfuegung) oder Zeichenaehnlichkeit (zuerst Abmahnung pruefe)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---
<!-- AUDIT 27.05.2026 | bundle_037 | task 1/5
Massnahme: Beide Vorkommen (Belege-Liste und Aktuelle-Rechtsprechung-Block) geloescht.
-->

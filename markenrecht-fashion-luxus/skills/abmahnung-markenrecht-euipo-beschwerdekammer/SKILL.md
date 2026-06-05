---
name: abmahnung-markenrecht-euipo-beschwerdekammer
description: "Abmahnung Markenrecht Euipo Beschwerdekammer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Abmahnung Markenrecht Euipo Beschwerdekammer

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Abmahnung Markenrecht Euipo Beschwerdekammer** im Plugin Markenrecht Fashion/Luxus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `abmahnung-markenrecht-uwg` | Markenrechtliche Abmahnung mit strafbewehrter Unterlassungserklärung erstellen: Mandant hat Markenverletzung entdeckt und will Abmahnung aussprechen oder hat Abmahnung erhalten und muss reagieren. Normen: § 14 MarkenG (Verletzungsansprüche), § 8 UWG (Unterlassung), § 14 Abs. 1 UWG n.F. 2021 (Kostenersatz). Prüfraster: Verletzungstatbestand, Hamburger Brauch Vertragsstrafe, Berechnung Abmahnkosten, Frist zur Abgabe. Output Abmahnung mit Unterlassungserklärung und Vertragsstrafe oder Gegenstellungnahme/modifizierte UE. Abgrenzung: Kein Eilantrag siehe messe-verletzung-und-gv-einsatz; kein DPMA-Widerspruch siehe dpma-widerspruch-und-löschung. |
| `euipo-beschwerdekammer-eu-gerichte` | EUIPO-Rechtsmittelroute steuern: Beschwerdekammer, Begründung, Belege, Fristen, Amtssprache, Vergleich, Gericht der EU, EuGH-Rechtsmittel und nationale Parallelverfahren. |
| `absolute-schutzhindernisse-8-markeng-art7-umv` | Absolute Schutzhindernisse bei DPMA- und EUIPO-Anmeldungen prüfen: Unterscheidungskraft, beschreibende Angaben, Freihaltebedürfnis, Täuschung, Sittenverstoß, Hoheitszeichen, Form- und Funktionsausschlüsse, Verkehrsdurchsetzung und Beanstandungsantwort. |
| `anmeldung-strategie-portfolio` | Strategische Markenportfolio-Planung für Luxus-Modehaeuser: Mandant will Marken in DE/EU/international schützen oder Portfolio optimieren. Normen: §§ 32 ff. MarkenG, Art. 32 ff. UMV (EU) 2017/1001, Madrid-Protokoll (WIPO). Prüfraster: Nizza-Klassen (3/14/18/25/35), Multi-Class-Strategie, Prioritaets-Kaskade, Kostenoptimierung, Anmeldezeitpunkt. Output Marken-Portfolio-Plan, Anmelde-Empfehlung je Territorium, Kostenprojektion. Abgrenzung: Einzelne Anmeldung DPMA siehe wortmarke-anmeldung-dpma; Madrid-Protokoll Details siehe madrid-protokoll-und-internationale-registrierung. |

## Arbeitsweg

Im Plugin Markenrecht Fashion/Luxus gilt für **Abmahnung Markenrecht Euipo Beschwerdekammer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `abmahnung-markenrecht-uwg`

**Fokus:** Markenrechtliche Abmahnung mit strafbewehrter Unterlassungserklärung erstellen: Mandant hat Markenverletzung entdeckt und will Abmahnung aussprechen oder hat Abmahnung erhalten und muss reagieren. Normen: § 14 MarkenG (Verletzungsansprüche), § 8 UWG (Unterlassung), § 14 Abs. 1 UWG n.F. 2021 (Kostenersatz). Prüfraster: Verletzungstatbestand, Hamburger Brauch Vertragsstrafe, Berechnung Abmahnkosten, Frist zur Abgabe. Output Abmahnung mit Unterlassungserklärung und Vertragsstrafe oder Gegenstellungnahme/modifizierte UE. Abgrenzung: Kein Eilantrag siehe messe-verletzung-und-gv-einsatz; kein DPMA-Widerspruch siehe dpma-widerspruch-und-löschung.

# Markenrechtliche Abmahnung und Unterlassungserklärung

## Fachkern: Markenrechtliche Abmahnung und Unterlassungserklärung
- **Spezialgegenstand:** Markenrechtliche Abmahnung und Unterlassungserklärung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Die Abmahnung ist das erste Durchsetzungsinstrument im markenrechtlichen Werkzeugkasten. Für klôtzzkètté SA ist sie das Signal an Verletzer: Wir kennen die Verletzung, wir verfolgen sie, und wir geben Gelegenheit zur außergerichtlichen Bereinigung — bevor das Gericht entscheidet.

Eine rechtssichere Abmahnung spart Gerichtskosten und schafft vollstreckbare Unterlassungsansprüche. Eine fehlerhafte Abmahnung kostet den Mandanten Geld und das Verfahren.

## Rechtsrahmen

- **§ 14 V MarkenG:** Unterlassungsanspruch bei Markenverletzung
- **§ 14 VI MarkenG:** Schadensersatz bei schuldhafter Verletzung (dreifache Berechnungsmethode: entgangener Gewinn, Verletzergewinn, Lizenzanalogie)
- **§ 19 MarkenG:** Auskunftsanspruch als Vorstufe zum Schadensersatz
- **§ 97a UrhG (analog):** Abmahnungserfordernis als Obliegenheit vor Klage (auch im Markenrecht üblicher Usus)
- **§ 13 UWG n.F. (seit 12.2021):** Abmahnkosten-Regulation im UWG — beachte: im reinen Markenrecht gilt das UWG-Abmahnkostenrecht nicht unmittelbar, ist aber Maßstab
- **Hamburger Brauch:** Richterrechtliche Vertragsstrafe-Klausel bei unklarer Verletzungsart — Verletzer unterwirft sich einer Vertragsstrafe "nach billigem Ermessen der Gläubigerin, im Streitfall durch Gericht überprüfbar"
- **Neue Hamburger Formel:** Alternativ: Feste Vertragsstrafe ab EUR 5.000 je Verletzungshandlung (planungssicherer, aber weniger flexibel)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 8 IV UWG:** Missbrauchsverbot bei UWG-Abmahnungen (beschränkt auf UWG-Ansprüche)
- **§ 12 UWG:** Prozessuale Absicherung (Unterlassungsklage nach erfolgloser Abmahnung)

## Prüfungsschritte

1. **Vorprüfung:**
 - Ist die klôtzzkètté-Marke eingetragen und in Kraft? (DPMA/EUIPO-Auszug)
 - Liegt eine schützbare Verletzungshandlung vor? (§ 14 II Nr. 1/2/3 MarkenG)
 - Wer ist der Verletzer (natürl./jurist. Person)? Identifizierung Impressum/Handelsregister
 - Zuständiges Gericht im Streitfall (Markenrechtliche Spezialspruchkörper: LG Berlin, LG Hamburg, LG München I, LG Frankfurt, LG Köln, LG Düsseldorf)

2. **Abmahnschreiben formulieren:**
 - Genaue Beschreibung der Verletzungshandlung (Datum, URL/Ort, Verletzungszeichen)
 - Markenrechtliche Grundlage: § 14 II Nr. [1/2/3] MarkenG
 - Forderungen: (a) Unterlassung + Unterlassungserklärung mit Vertragsstrafe, (b) Auskunft (§ 19 MarkenG), (c) Schadensersatz dem Grunde nach, (d) Kostenersatz
 - Fristsetzung: in der Regel 7-14 Tage (bei offensichtlicher Verletzung kürzer möglich)

3. **Unterlassungserklärung — Vertragsstrafe:**
 - Hamburger Brauch: "…bei jeder schuldhaften Zuwiderhandlung eine von der klôtzzkètté SA nach billigem Ermessen festzusetzende, im Streitfall durch das zuständige Gericht zu überprüfende Vertragsstrafe zu zahlen."
 - Alternative: Feste Vertragsstrafe EUR 10.000 je Verletzungshandlung (für Serienverletzer empfehlenswert)
 - Klausel: Kein Abstrich (kein "mindestens EUR 1") — Erstunterwerfung muss Wiederholungsgefahr beseitigen

4. **Reaktionsmöglichkeiten des Verletzers:**
 - Unterlassungserklärung abgegeben: Wiederholungsgefahr entfallen → kein Eilantrag mehr nötig
 - Modifizierte Unterlassungserklärung: Prüfen ob ausreichend (meist nicht)
 - Keine Reaktion: Eilantrag §§ 935/940 ZPO

5. **Kostenrechnung:**
 - Anwaltsgebühren nach RVG, Gegenstandswert (GW) bei Markenabmahnung: EUR 50.000-250.000 (je nach Bedeutung und Verletzungsumfang)
 - GW EUR 100.000: 1,3 Geschäftsgebühr = EUR 2.019,50 + USt = ca. EUR 2.403
 - Kostenerstattungspflicht des Verletzers: § 14 VI MarkenG (Ersatz der erforderlichen Kosten)

## Falltypische Konstellationen

### Konstellation 1: Brezelmann Online-Shop "klotzkette-discount.de"
Brezelmann betreibt Website, die unter dem Keyword "klôtzzkètté" günstige Nachahmungen bewirbt. Abmahnung wegen § 14 II Nr. 2 MarkenG (Verwechslungsgefahr) und §§ 5/6 UWG (irreführende/vergleichende Werbung). Frist: 10 Tage. Vertragsstrafe: EUR 15.000 je Handlung (Wiederholungsgefahr bereits belegt durch frühere Abmahnung).

### Konstellation 2: Influencer trägt gefälschtes klôtzzkètté-Stück auf Instagram
Micro-Influencer (200k Follower) trägt offensichtliche Fälschung und taggt "@klotzkette_official" (fake Account). Abmahnung gegen Influencer auf § 14 II Nr. 1 (Identität) oder Nr. 2 (Verwechslungsgefahr). Separate Notice-and-Action gegen Instagram/Meta nach DSA (vgl. Skill `plattform-piraterie-donauzon`).

### Konstellation 3: Wiederholungstäter Brezelmann
Brezelmann hat bereits eine Unterlassungserklärung abgegeben (Hamburger Brauch), verwendet das Zeichen erneut. Vertragsstrafe-Klage: Quantifizierung der Zuwiderhandlungen, EUR 5.000-15.000 je Fall. Parallele neue Abmahnung für neue Verletzungshandlungen.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### Abmahnschreiben (Wortmarke DE, Standard)
```
ABMAHNUNG — VERTRAULICH

An: [Verletzer GmbH], [Adresse]

Unsere Mandantin: klôtzzkètté SA, 23 Rue Saint-Honoré, Paris
Unser Zeichen: [Az.], Datum: [...]

Sehr geehrte Damen und Herren,

wir vertreten die klôtzzkètté SA, Inhaberin der deutschen Wortmarke
"klôtzzkètté" (DPMA-Reg.-Nr. [...], Klassen 14/18/25/35).

Sie verwenden das Zeichen "[Verletzungszeichen]" im geschäftlichen
Verkehr für [Waren/Dienstleistungen], was die Markenrechte unserer
Mandantin verletzt (§ 14 II Nr. 2 MarkenG).

Wir fordern Sie auf, bis [Frist, 10 Tage] die beiliegende
strafbewehrte Unterlassungserklärung zu unterzeichnen sowie
unsere Anwaltskosten in Höhe von EUR [X] zu erstatten.

Bei Fristversäumnis werden wir ohne weitere Ankündigung gerichtliche
Eilmaßnahmen beantragen.

RA'in [Name], Partnerin
```

## Verweise auf andere Skills

- `messe-verletzung-und-gv-einsatz` — Bei Eilbedürftigkeit direkt Gericht
- `plattform-piraterie-donauzon` — Online-Verletzungen
- `produktpiraterie-und-zoll` — Schwerere Verletzungsfälle

## Risiken & Stolperfallen

- **Rechtsmissbrauch:** Zu weitgehende Abmahnungen (z.B. wegen Bagatellverletzungen mit hohem GW) können als rechtsmissbräuchlich gewertet werden (§ 8 IV UWG analog)
- **Fehlende Markenrecherche vor Abmahnung:** Eigene Marke muss eingetragen und in Kraft sein — Abmahnung auf Basis einer inzwischen verfallenen Marke ist unwirksam
- **Unterlassungserklärung mit Abstrich:** Enthält die Erklärung des Verletzers eine Einschränkung, ist Wiederholungsgefahr nicht beseitigt — nicht blind annehmen
- **Fristlauf Vertragsstrafe:** Vertragsstrafe entsteht erst bei schuldhafter Zuwiderhandlung — bei sofortiger Unterwerfung kein automatisches Recht auf Zahlung

## Triage-Fragen vor Abmahnung

Bevor die Abmahnung abgeschickt wird, kläre:
1. Ist die eigene Marke eingetragen, in Kraft und nicht im Verfall (§§ 26/49 MarkenG)?
2. Handelt es sich um eine gewerbliche oder private Nutzung?
3. Welche Verletzungshandlung genau — § 14 II Nr. 1 (Doppelidentität), Nr. 2 (Verwechslungsgefahr) oder Nr. 3 (Bekanntheitsschutz)?
4. Ist der Verletzer im Inland greifbar (Impressum, HReg-Auszug)?
5. Liegt Wiederholungsgefahr oder (erst) Erstbegehungsgefahr vor?
6. Ist eine Abmahnung sinnvoll oder besteht Missbrauchsrisiko (§ 8 IV UWG analog)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `euipo-beschwerdekammer-eu-gerichte`

**Fokus:** EUIPO-Rechtsmittelroute steuern: Beschwerdekammer, Begründung, Belege, Fristen, Amtssprache, Vergleich, Gericht der EU, EuGH-Rechtsmittel und nationale Parallelverfahren.

# EUIPO-Beschwerde und EU-Gerichte

## Fachkern: EUIPO-Beschwerde und EU-Gerichte
- **Spezialgegenstand:** EUIPO-Beschwerde und EU-Gerichte; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Aufgabe

Führe eine EUIPO-Entscheidung in die richtige Rechtsmittel- oder Vergleichsroute.

## Pflichtfragen

- Entscheidung: absolute Hindernisse, Widerspruch, Nichtigkeit, Verfall?
- Zustellung, Frist, Sprache, Aktenzeichen, Parteien.
- Neue Belege oder nur Rechtsfehler?
- Parallelverfahren vor nationalen Gerichten?

## Prüfprogramm

1. **Fristen:** Beschwerde und Begründung strikt trennen und live prüfen.
2. **Angriffsziel:** Tatsachenwürdigung, Rechtsfehler, Verfahrensfehler, Beweiswürdigung.
3. **Belege:** Zulässigkeit neuer Belege und strategische Nachreichung prüfen.
4. **Vergleichsfenster:** Einschränkung, Koexistenz, Rücknahme, Kosten.
5. **Weitere Route:** Gericht der EU und EuGH nicht als zweite Tatsacheninstanz missverstehen.
6. **Parallelität:** Nationale Verletzungsverfahren und EUIPO-Bestandsverfahren synchronisieren.

## Output

- Rechtsmittel-Fahrplan.
- Beschwerdebegründungsstruktur.
- Beleg- und Fristenmatrix.

## Quellen

UMV, Verfahrensordnung, EUIPO Guidelines und konkrete Entscheidung live prüfen.

## 3. `absolute-schutzhindernisse-8-markeng-art7-umv`

**Fokus:** Absolute Schutzhindernisse bei DPMA- und EUIPO-Anmeldungen prüfen: Unterscheidungskraft, beschreibende Angaben, Freihaltebedürfnis, Täuschung, Sittenverstoß, Hoheitszeichen, Form- und Funktionsausschlüsse, Verkehrsdurchsetzung und Beanstandungsantwort.

# Absolute Schutzhindernisse

## Fachkern: Absolute Schutzhindernisse
- **Spezialgegenstand:** Absolute Schutzhindernisse; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Aufgabe

Prüfe, ob ein Zeichen an § 8 MarkenG oder Art. 7 UMV scheitert und wie man den Anmeldegegenstand, das Waren- und Dienstleistungsverzeichnis oder die Argumentation retten kann.

## Pflichtfragen

- DPMA, EUIPO oder internationale Registrierung mit Schutzgesuch für Deutschland oder EU?
- Zeichenform: Wort, Bild, Wort-Bild, 3D, Farbe, Klang, Position, Bewegung oder sonstige Marke?
- Waren und Dienstleistungen mit Klassen und konkreten Begriffen?
- Liegt bereits ein Beanstandungsbescheid vor, mit Frist und Begründung?
- Gibt es Benutzungsnachweise für Verkehrsdurchsetzung?

## Prüfprogramm

1. **Zeichen sauber lesen:** Schreibweise, Sprache, Bestandteile, grafische Elemente, Aussprache, Übersetzungen und Branchenverständnis trennen.
2. **Unterscheidungskraft prüfen:** Kann das Zeichen betriebliche Herkunft anzeigen oder bleibt es nur Werbespruch, Sachhinweis, Qualitätshinweis, Form, Dekor oder Preisversprechen?
3. **Freihaltebedürfnis prüfen:** Brauchen Wettbewerber die Angabe zur Beschreibung von Art, Qualität, Menge, Bestimmung, Wert, geografischer Herkunft oder sonstigen Merkmalen?
4. **Sonderhindernisse prüfen:** Täuschungsgefahr, öffentliche Ordnung, Hoheitszeichen, geschützte geografische Angaben, Sortenbezeichnungen, religiöse/politische Sensibilität.
5. **Formmarken-Falle:** Wesentliche Form durch Art der Ware, technische Wirkung oder wesentlichen Wert der Ware prüfen; kein Schutzrechts-Hopping durch Marke.
6. **Rettungsoptionen:** Waren-/Dienstleistungsverzeichnis verengen, Bildbestandteile stärken, Priorität ändern, Benutzungsdurchsetzung belegen, Design/UWG/GeschGehG als Alternative prüfen.

## Output

- Risikoampel pro Schutzhindernis.
- Beanstandungsantwort oder interne Go/No-Go-Notiz.
- Liste der Belege für Verkehrsdurchsetzung.
- Vorschlag für alternative Zeichenfassung.

## Quellen-Hardening

Normtext und Behördenpraxis live prüfen: MarkenG, UMV, DPMA-Hinweise, EUIPO Guidelines. Rechtsprechung nur mit verifizierter Quelle ausgeben.

## 4. `anmeldung-strategie-portfolio`

**Fokus:** Strategische Markenportfolio-Planung für Luxus-Modehaeuser: Mandant will Marken in DE/EU/international schützen oder Portfolio optimieren. Normen: §§ 32 ff. MarkenG, Art. 32 ff. UMV (EU) 2017/1001, Madrid-Protokoll (WIPO). Prüfraster: Nizza-Klassen (3/14/18/25/35), Multi-Class-Strategie, Prioritaets-Kaskade, Kostenoptimierung, Anmeldezeitpunkt. Output Marken-Portfolio-Plan, Anmelde-Empfehlung je Territorium, Kostenprojektion. Abgrenzung: Einzelne Anmeldung DPMA siehe wortmarke-anmeldung-dpma; Madrid-Protokoll Details siehe madrid-protokoll-und-internationale-registrierung.

# Anmeldestrategie & Markenportfolio für Luxus-Modehäuser

## Fachkern: Anmeldestrategie & Markenportfolio für Luxus-Modehäuser
- **Spezialgegenstand:** Anmeldestrategie & Markenportfolio für Luxus-Modehäuser; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Als Partnerin bei einer der führenden deutschen Markenboutiquen betreue ich das gesamte IP-Portfolio der klôtzzkètté SA, Paris/Mailand. Die Anmeldestrategie für ein Haute-Couture-Label erfordert eine durchdachte Kaskade aus nationalen, europäischen und internationalen Schutzrechten — kein Stein darf unbeachtet bleiben.

Das Portfolio von klôtzzkètté umfasst Wortmarken, Bild- und Wort-Bild-Marken, Slogan-, Sound-, Positions- und 3D-Marken sowie neue Kennzeichenformate für die Post-KI-Ära. Die Comtesse Beatrice de Klotzzkettie erwartet lückenlose Schutzabdeckung.

## Rechtsrahmen

- **Nationales Recht DE:** §§ 3/4/32 ff. MarkenG, DPMA-Anmeldegebühren nach PatKostG Anlage (je Klasse ab Klasse 4: EUR 100 Zuschlag)
- **Unionsmarke:** VO (EU) 2017/1001 (UMV), Art. 33 UMV (Nizza-Klassifikation), EUIPO e-Filing
- **Internationales Recht:** Madrider Abkommen (MMA) und Protokoll (PMMA), Regel 9 PMMA-Ausführungsordnung, Basismarken-Anforderungen
- **Nizza-Klassifikation:** 12. Ausgabe (NCL 12-2023), WIPO-Datenbank
- **Priorität:** Art. 4 PVÜ (6-Monats-Frist), Art. 35 UMV

## Prüfungsschritte

1. **Bestandsaufnahme:** Vollständige IP-Inventur aller bestehenden Zeichen, Verfallsdaten, Klassenbelegungen — vgl. Skill `fashion-luxus-kaltstart-interview`
2. **Territoriale Schutzstrategie:**
 - DE-Basismarke beim DPMA als Anker (schneller, günstiger, solide Basis)
 - EU-Unionsmarke (UM) für einheitlichen EU-Schutz via EUIPO
 - Internationale Registrierung via Madrid-Protokoll für Drittstaaten (CH, UK, US, JP, CN, AE)
3. **Klassenstrategie für Mode-Luxus:**
 - Klasse 3: Parfums, Kosmetika, Pflegeprodukte (klôtzzkètté Parfum "Abîme Dorée")
 - Klasse 14: Schmuck, Uhren, Edelmetalle (klôtzzkètté Bijou)
 - Klasse 18: Leder, Reiseartikel, Handtaschen (klôtzzkètté Sac)
 - Klasse 25: Bekleidung, Schuhwerk, Kopfbedeckungen (Kernklasse)
 - Klasse 35: Einzelhandelsdienstleistungen, Online-Shops (klôtzzkètté.com)
 - Klasse 40: Schneiderarbeiten, Maßanfertigung (optional, Couture-Atelier)
 - Klasse 41: Mode-Events, Schauen (Paris Fashion Week)
4. **Kollisionsrecherche:** DPMA-Markenrecherche, EUIPO eSearch plus, WIPO Global Brand Database — vor jeder Anmeldung obligatorisch
5. **Prioritätskaskade:**
 - Tag 0: DPMA-Anmeldung Wortmarke + Wort-Bild-Marke
 - Tag +30: EUIPO-Anmeldung mit Prioritätsanspruch auf DE-Anmeldung (Art. 35 UMV)
 - Tag +150: Madrid-Protokoll-Anmeldung mit Priorität aus DE- oder EU-Basismarke
6. **Kostenoptimierung:**
 - Multi-Class-Bundles beim EUIPO (1. Klasse: EUR 850; 2. Klasse: EUR 50 Zuschlag; ab 3. Klasse: EUR 150 je Klasse)
 - DPMA: EUR 300 für 3 Klassen, je weitere Klasse EUR 100
 - Vermeidung unnötiger Klassen (Benutzungsnachweis nach 5 Jahren!)

## Falltypische Konstellationen

### Konstellation 1: Erstanmeldung "klôtzzkètté" als Wortmarke
klôtzzkètté SA plant die Markteinführung in DE/EU. Strategie: Gleichzeitige DPMA-Anmeldung (Klassen 14/18/25/35) und EUIPO-Anmeldung mit 6-Monats-Priorität. Sonderzeichen ô/è im Markenwort sind zulässig (Art. 26 I lit. b UMV), erfordern aber eine phonetische Entsprechung in der Beschreibung.

### Konstellation 2: Erweiterung nach Asien
Nach 3 Jahren Markterfolg plant die Comtesse Expansion nach CN/JP/KR. Lösung: Madrid-Protokoll-Anmeldung auf Basis der bestehenden EUIPO-Registrierung. WIPO-Gebühren variieren je Bestimmungsland (CN-Zuschlag besonders hoch für Klasse 25).

### Konstellation 3: Neue Produktlinie "klôtzzkètté Maison"
Haushaltstextilien (Klasse 24), Möbel (Klasse 20), Innenausstattung (Klasse 42 Designdienstleistungen). Eigenständige Unter-Marke oder Erweiterung der bestehenden Registrierungen? Bei über 5 Jahren Benutzungsnachweis in Klasse 25 können neue Klassen via DPMA-Einzel-Anmeldung hinzugefügt werden (keine Zusammenlegung möglich — neue Aktenzeichen).

### Konstellation 4: Reaktive Verteidigung gegen Brezelmann Discount
Brezelmann Discount KG (Bad Mergentheim) hat "KLÖTZ-KETTE" in Klasse 25 beim DPMA angemeldet. Prioritätslücke! Sofortiger Widerspruch §§ 42 ff. MarkenG — vgl. Skill `dpma-widerspruch-und-loeschung`.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### Checkliste Anmeldung DPMA (Wortmarke)
```
[ ] Markenbezeichnung (max. 250 Zeichen für Wortmarke)
[ ] Nizza-Klassen und Warenverzeichnis (Entwurf)
[ ] Inhaberangaben (klôtzzkètté SA, Adresse, ggf. Vertreter)
[ ] Prioritätsangaben (falls beansprucht)
[ ] Anmeldegebühr überweisen: EUR 300 (bis 3 Klassen)
[ ] DPMA-Onlineformular DPMAonline oder DPMAdirekt
[ ] Ggf. Vertretervollmacht (Form 3.1)
```

### Warenverzeichnis-Muster Klasse 25
> Bekleidungsstücke, insbesondere Oberbekleidung, Unterbekleidung, Kleider, Röcke, Blusen, Jacken, Mäntel und Pelzwaren; Schuhwaren; Kopfbedeckungen; Handschuhe [Bekleidung]; Gürtel [Bekleidung]; Strümpfe und Strumpfwaren; Badebekleidung; Abendgarderobe; Haute-Couture-Erzeugnisse.

### Madrid-Protokoll — Checkliste Basismarken-Anforderungen
```
[ ] Basismarke eingetragen (DE oder EU) oder angemeldet
[ ] Identische Waren/Dienstleistungen in Bestimmungsländern
[ ] WIPO-Formular MM2 (elektronisch)
[ ] Liechtenstein/CH als Basisamt (DPMA) oder EUIPO
[ ] Grundgebühr WIPO: CHF 653 + Länderzuschläge
```

## Verweise auf andere Skills

- `wortmarke-anmeldung-dpma` — DPMA-Verfahren im Detail
- `unionsmarken-anmeldung-euipo` — EUIPO-Anmeldeverfahren
- `bildmarke-und-wort-bild` — Bildmarken-Anmeldung
- `fashion-luxus-kaltstart-interview` — IP-Audit als Ausgangspunkt
- `markenmonitoring-und-watchlist` — Überwachung nach Eintragung

## Risiken & Stolperfallen

- **Benutzungszwang:** §§ 26/49 MarkenG, Art. 58 UMV — nach 5 Jahren droht Verfall bei Nichtbenutzung; jede Klasse einzeln prüfen
- **Zu weites Warenverzeichnis:** Angreifbar durch Brezelmann & Co. via Teillöschungsantrag; nur realistische Waren eintragen
- **Sonderzeichen:** Prüfen, ob das DPMA-System ô/è korrekt kodiert (UTF-8); im Zweifel auch vereinfachte ASCII-Schreibweise parallel anmelden
- **Madrid-Transformation:** Bei Angriff auf die Basismarke innerhalb von 5 Jahren droht Transformation aller abhängigen internationalen Registrierungen (zentrale Angriffsfläche!)
- **Klassenerweiterung unmöglich:** DPMA lässt keine nachträgliche Klassenerweiterung zu — zu enge Erstanmeldung ist kaum heilbar

## Triage-Fragen vor Anmeldestrategie

Bevor die Anmeldekaskade gestartet wird, kläre:
1. Ist das Zeichen bereits irgendwo angemeldet oder benutzt (unregistrierte Marke, §§ 4 Nr. 2/3 MarkenG)?
2. Welche Märkte sind innerhalb der nächsten 3 Jahre kommerziell realistisch?
3. Bestehen bekannte Kollisionsrisiken durch Drittmarken in Zielklassen?
4. Wurde die 5-Jahres-Benutzungspflicht für bestehende Eintragungen beachtet?
5. Ist eine Madrid-IR-Basismarke bereits konsolidiert und Central-Attack-resistent?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

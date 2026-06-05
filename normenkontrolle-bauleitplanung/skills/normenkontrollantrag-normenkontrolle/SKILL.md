---
name: normenkontrollantrag-normenkontrolle
description: "Normenkontrollantrag Normenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Normenkontrollantrag Normenkontrolle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Normenkontrollantrag Normenkontrolle** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erforderlichkeit Abwaegungsfehler Vorgang und Ergebnis Hilfsantrag Teilunwirksamkeit. Anlagen Plan-Unterlagen Bekanntmachung Begründung Schriftverkehr. Output: vollständiger Normenkontrollantrag-Schriftsatz. Abgrenzung zu einstweilige-anordnung-47-abs-6-vwgo (Eilantrag) und mandat-erstgespraech-normenkontrolle. |
| `normenkontrolle-oder-inzidentkontrolle` | Normenkontrolle oder Inzidentkontrolle: wann § 47 VwGO, wann Anfechtung/Verpflichtung/Feststellung gegen Einzelakt.; Normanker: VwGO §§ 42 und 43 und 47; Rechtsschutzbedürfnis; Bestandskraft; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar. |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche Fehler § 215 BauGB Ruegefrist ein Jahr ab Bekanntmachung schriftliche Ruege an Gemeinde ergaenzendes Verfahren § 214 Abs. 4. Ergebnisfehler immer beachtlich. Output: Fehler-Relevanztabelle Planerhalten vs. Unwirksam. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Fehlertypen) und jahresfrist-47-abs-2-vwgo. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Normenkontrollantrag Normenkontrolle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `normenkontrollantrag-schriftsatz`

**Fokus:** Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erforderlichkeit Abwaegungsfehler Vorgang und Ergebnis Hilfsantrag Teilunwirksamkeit. Anlagen Plan-Unterlagen Bekanntmachung Begründung Schriftverkehr. Output: vollständiger Normenkontrollantrag-Schriftsatz. Abgrenzung zu einstweilige-anordnung-47-abs-6-vwgo (Eilantrag) und mandat-erstgespraech-normenkontrolle.

# Normenkontrollantrag — Schriftsatz

## Zweck

Der Normenkontrollantrag ist das Kernstück der Mandatsbearbeitung. Er muss in der Begründung die formellen und materiellen Fehler so darstellen, dass der Senat die Unwirksamkeit erkennen muss.

## Schritt 1 — Rubrum

### Bestandteile
- An den Bayerischen Verwaltungsgerichtshof
- Senatsgeschäftsstelle München
- Antragstellerin: vollständiger Name, Anschrift
- Verfahrensbevollmächtigte: Anwältin, Kanzlei, Adresse, beA-SAFE-ID
- Antragsgegnerin: Stadt / Gemeinde, Anschrift
- Beigeladene: ggf. Vorhabenträger, Eisenbahn-Bundesamt, Eigentümer

### Bezeichnung des Verfahrens
- "wegen Normenkontrolle nach § 47 VwGO gegen den Bebauungsplan Nr. X 'Name' der Stadt Y"

## Schritt 2 — Antrag

### Hauptantrag
- "Der Bebauungsplan Nr. X 'Name' der Stadt Y, bekannt gemacht im Amtsblatt der Stadt Y Nr. A vom B, wird für unwirksam erklärt."

### Hilfsantrag Teilunwirksamkeit
- "Hilfsweise: Der Bebauungsplan Nr. X 'Name' der Stadt Y wird in Bezug auf die textliche Festsetzung Nr. Y / die zeichnerische Festsetzung Z für unwirksam erklärt."

### Kosten
- "Die Antragsgegnerin und die Beigeladene tragen die Kosten des Verfahrens als Gesamtschuldner."

### Vorläufige Vollstreckbarkeit
- "Das Urteil ist hinsichtlich der Kosten vorläufig vollstreckbar."

## Schritt 3 — Sachverhalt

### Aufbau
1. Mandantenstellung und Eigentum (Grundbuchauszug Anlage)
2. Räumliche Lage zum Plangebiet (Lageplan Anlage)
3. Plan-Identifikation (Bekanntmachung Anlage)
4. Verfahrensablauf des Plans chronologisch
5. Beteiligung der Mandantin (Einwendungen Anlage)
6. Bekanntmachung (Bekanntmachungstext Anlage)
7. Aktueller Stand (Genehmigung bereits beantragt?)

### Stil
- Tatsachenangaben sachlich
- Bezugnahmen mit Aktenseiten / Anlagen-Nummer
- Keine Rechtsausführungen im Sachverhalt

## Schritt 4 — Zulässigkeit

### Aufbau
1. **Statthaftigkeit** § 47 Abs. 1 Nr. 1 VwGO — B-Plan als Satzung
2. **Antragsbefugnis** § 47 Abs. 2 S. 1 VwGO — Eigentum + Belang
3. **Antragsfrist** § 47 Abs. 2 S. 1 VwGO — Eingang innerhalb Jahresfrist
4. **Rechtsschutzbedürfnis** — gegeben

### Substanziierung
- Belang konkret benennen: Verschattung, Lärm, Wertminderung, Stellplatzdruck
- Verweis auf Einwendungen im Aufstellungsverfahren

## Schritt 5 — Begründetheit-Aufbau

### Empfohlene Reihenfolge
A. Formelle Mängel
1. Bekanntmachungsfehler (Anstoßfunktion)
2. Auslegungsfehler (Dauer, Identität)
3. Beteiligungsfehler (frühe Beteiligung, erneute Auslegung)
4. Umweltbericht-Mängel
5. Beschlussfassungsmängel

B. Materielle Mängel
1. § 1 Abs. 3 BauGB Erforderlichkeit / Planrechtfertigung / Gefälligkeitsplanung
2. § 8 Abs. 2 BauGB Anpassungsgebot
3. § 1 Abs. 7 BauGB Abwägung
 3.1 Abwägungsausfall (Vorfestlegung)
 3.2 Abwägungsdefizit (übersehene Belange)
 3.3 Abwägungsfehleinschätzung (falsche Gewichtung)
 3.4 Abwägungsdisproportionalität (Ergebnis)
4. § 1a Abs. 3 BauGB Eingriffsregelung
5. § 44 BNatSchG Artenschutz
6. § 50 BImSchG Trennungsgrundsatz / Lärm
7. Art. 47 BayBO Stellplatzfragen

C. Beachtlichkeit / Rüge
- Subsumtion unter § 214 BauGB
- Verweis auf erfolgte Rüge § 215 BauGB

## Schritt 6 — Anlagen

### Pflicht-Anlagen
- Vollmacht
- Grundbuchauszug
- Bekanntmachung B-Plan
- Planurkunde (zeichnerisch)
- Textliche Festsetzungen
- Begründung mit Umweltbericht
- Eigene Einwendungen Mandantin mit Eingangsbestätigung
- Rügeschreiben § 215 BauGB
- Lageplan-Übersicht

### Beweis-Anlagen
- Schallschutzgutachten Stadt
- Eigenes Gegen-Gutachten (sofern vorhanden)
- Verkehrsgutachten
- Artenschutz-Gutachten
- Mandanten-Chronologie / Notizen
- Eidesstattliche Versicherungen Zeugen Bürgerversammlung
- Sitzungsprotokolle Stadtrat (falls beschafft)
- E-Mail-Korrespondenz Stadt-Investor (falls IFG)

## Schritt 7 — Streitwert

### Streitwertkatalog Verwaltungsgerichtsbarkeit Nr. 9.8.1
- Im Regelfall 60.000 EUR
- Bei Mehrfach-Antragstellern jeweils eigener Wert
- Bei wirtschaftlich besonders bedeutendem Plan höher

### Streitwertangabe
- Im Schriftsatz: "Der Streitwert wird mit 60.000 EUR angegeben."
- Endgültige Festsetzung durch Senat

## Schritt 8 — Einreichung

### Form
- elektronisch über beA gemäß § 55a VwGO
- Empfangsbekenntnis sichern
- bei mehreren Antragstellern Einzelvollmachten oder Sammelvollmacht

### Frist
- Eingang spätestens am letzten Tag der Jahresfrist
- Eingangsbestätigung Senatsgeschäftsstelle abwarten

### Kostenvorschuss
- Anforderungsbescheid abwarten
- Streitwertgrundlage 60.000 EUR — Gebühren nach GKG-Tabelle

## Schritt 9 — Strategische Hinweise

### Reihenfolge und Gewichtung
- Stärkste Fehler an den Anfang
- Ergebnisfehler (Disproportionalität, § 1 Abs. 3 BauGB) prominent
- Vorgangsfehler mit Beachtlichkeits-Subsumtion abgesichert
- Hilfsweise Teilunwirksamkeit anbieten

### Mündliche Verhandlung
- In der Regel wird mündlich verhandelt
- Schriftsatz nicht zu lang — Senat liest nicht endlos
- Klare Struktur mit Zwischen-Überschriften
- Tabellen / Aufzählungen bei Komplexität

### Beweisanträge vorbereiten
- Sachverständigengutachten zu Lärm, Verkehr, Artenschutz
- Zeugen für Bürgerversammlung
- Augenscheinseinnahme vor Ort

## Schritt 10 — Häufige Fehler

- Antrags-Formulierung zu unkonkret
- Antragsbefugnis nicht substantiell begründet
- Anlagen unvollständig
- Streitwert zu niedrig
- Rügeschreiben § 215 BauGB nicht beigefügt
- Materielle Fehler ohne Subsumtion auf § 214 Abs. 3 BauGB
- Schriftsatz zu lang ohne Struktur

## Quellen

- VwGO §§ 47 55a 154 167
- BauGB §§ 1 1a 2 3 4 4a 8 9 10 13a 214 215
- BImSchG § 50
- BNatSchG § 44
- BayBO Art. 47 81
- Streitwertkatalog Verwaltungsgerichtsbarkeit Nr. 9.8.1

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `normenkontrolle-oder-inzidentkontrolle`

**Fokus:** Normenkontrolle oder Inzidentkontrolle: wann § 47 VwGO, wann Anfechtung/Verpflichtung/Feststellung gegen Einzelakt.; Normanker: VwGO §§ 42 und 43 und 47; Rechtsschutzbedürfnis; Bestandskraft; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar.

# Normenkontrolle oder Inzidentkontrolle: wann § 47 VwGO, wann Anfechtung/Verpflichtung/Feststellung gegen Einzelakt.

## Auftrag

Dieser Skill löst § 47 VwGO aus der reinen Bauleitplanung. Er prüft, ob eine im Rang unter dem Landesgesetz stehende Rechtsvorschrift direkt vor dem OVG/VGH überprüft werden kann oder ob nur eine Inzidentkontrolle im Verfahren gegen einen Einzelakt passt.

## Normanker

VwGO §§ 42, 43, 47; Rechtsschutzbedürfnis; Bestandskraft. Vor jeder Ausgabe muss das jeweilige Landesrecht geprüft werden, weil § 47 Abs. 1 Nr. 2 VwGO die Normenkontrolle außerhalb der BauGB-Fälle nur eröffnet, soweit Landesrecht dies bestimmt.

## Prüfprogramm

1. Normtyp: Satzung, Rechtsverordnung, Bebauungsplan, Polizeiverordnung, Benutzungssatzung oder bloßer Verwaltungsakt?
2. Statthaftigkeit: § 47 Abs. 1 Nr. 1 oder Nr. 2 VwGO, Landesrechtseröffnung, Rang unter Landesgesetz.
3. Antragsteller: mögliche Rechtsverletzung, Adressat, Eigentümer, Nutzer, Gemeinde, Verband oder Konkurrent.
4. Frist und Rechtsschutzbedürfnis: Jahresfrist, fortbestehende Beschwer, Parallelverfahren.
5. Materielle Kontrolle: Ermächtigung, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.
6. Rechtsfolge: Unwirksamkeit, Bekanntmachung der Entscheidung, Wirkung auf Folgebescheide, neue Satzung.

## Ausgabe

Erzeuge eine Statthaftigkeitsskizze, Satzungs-Red-Team, Eilantragsskizze, Schriftsatzgliederung oder Bürger-/Mandantenbrief.

## 3. `planerhaltung-214-215-baugb`

**Fokus:** Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche Fehler § 215 BauGB Ruegefrist ein Jahr ab Bekanntmachung schriftliche Ruege an Gemeinde ergaenzendes Verfahren § 214 Abs. 4. Ergebnisfehler immer beachtlich. Output: Fehler-Relevanztabelle Planerhalten vs. Unwirksam. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Fehlertypen) und jahresfrist-47-abs-2-vwgo.

# Planerhaltung — § 214/215 BauGB

## Zweck

§§ 214 und 215 BauGB filtern Fehler heraus, die nicht durchschlagen. Sie sind zentrale Verteidigungs-Argumente der Gemeinde. Anwältin der Antragstellerseite muss sie umgekehrt aushebeln: durch Subsumtion auf "beachtlich" und durch fristgerechte Rüge.

## Schritt 1 — § 214 Abs. 1 BauGB Verfahrens- und Formfehler


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Abschließende Liste beachtlicher Fehler
- Verletzung Vorschriften über die Beteiligung (§§ 3 Abs. 2, 4 Abs. 2 BauGB) — nur wenn nach den Umständen offenkundig und Auswirkung
- Verletzung Vorschriften über die Begründung — nur wenn fehlend in wesentlichen Punkten
- Verletzung des Beschlusses — beachtlich
- Verletzung der Bekanntmachung — wenn nicht offenkundig (Anstoßfunktion)

### Subsumtion Anwältin
- Konkret darlegen, dass der Mangel "offenkundig" und "auf das Ergebnis Auswirkung" hatte
- Bei Beteiligungsfehler: hätte die fehlende Auslegung andere Stellungnahmen erbracht?
- Bei Bekanntmachungsfehler: hätte ein anderer Adressatenkreis erreicht werden müssen?

## Schritt 2 — § 214 Abs. 2 BauGB Erweiterung Form

### Form-Verstöße
- Erweiterung beachtlicher Form-Fehler in besonderen Konstellationen
- Praxisrelevanz geringer als Abs. 1
- Häufig kombiniert mit Abs. 1 geprüft

## Schritt 3 — § 214 Abs. 3 BauGB Abwägungsfehler

### Voraussetzung Beachtlichkeit
- Mängel im Abwägungsvorgang sind nur beachtlich, wenn sie offensichtlich sind
- Und auf das Abwägungsergebnis von Einfluss gewesen sind
- Beide Voraussetzungen kumulativ

### Abgrenzung Vorgang/Ergebnis
- Abwägungsvorgangsfehler: Belange übersehen, falsch gewichtet, miteinander unausgeglichen behandelt
- Abwägungsergebnisfehler: das Ergebnis selbst sprengt den Abwägungsspielraum (Disproportionalität)
- § 214 Abs. 3 BauGB filtert nur Vorgangsfehler — Ergebnisfehler bleiben stets beachtlich

### "Offensichtlich"
- Aus dem Aktenstand erkennbar
- Aus der Begründung erkennbar
- Nicht: erst durch Sachverständigengutachten zu klären

### "Auf das Ergebnis von Einfluss"
- Konkrete Möglichkeit, dass ohne den Fehler anders entschieden worden wäre
- Keine bloße abstrakte Möglichkeit

## Schritt 4 — § 214 Abs. 4 BauGB Ergänzendes Verfahren

### Heilung
- Mängel können durch ergänzendes Verfahren behoben werden
- Erneute Auslegung, erneuter Beschluss, erneute Bekanntmachung
- Rückwirkung möglich

### Strategie Anwältin
- Wenn Stadt während des Normenkontrollverfahrens "heilen" will:
 - Prüfen ob das ergänzende Verfahren methodisch korrekt
 - Prüfen ob der bestehende Mangel heilungsfähig ist (Ergebnis-Fehler nicht)
 - Prüfen ob Rückwirkung legitim
- Häufig bricht "Heilung" an formellen Folgemängeln

## Schritt 5 — § 215 Abs. 1 BauGB Rügefrist

### Frist
- Ein Jahr ab Bekanntmachung der Satzung
- Schriftliche Rüge gegenüber der Gemeinde
- Konkrete Bezeichnung des Mangels mit Begründung

### Erfasste Fehler
- Nr. 1: Beachtliche Verfahrens- und Formvorschriften
- Nr. 2: Vorschriften über Begründungspflicht (Verstoß)
- Nr. 3: Mängel im Abwägungsvorgang

### Nicht erfasste Fehler
- Mängel der Erforderlichkeit § 1 Abs. 3 BauGB
- Abwägungsergebnis-Mängel (Disproportionalität, Gleichheitssatz-Verletzung)
- Verstoß gegen höherrangiges Recht (Bundesrecht, EU-Recht)

## Schritt 6 — § 215 Abs. 2 BauGB Hinweis-Erfordernis

### Pflicht
- Beim Erlass der Satzung ist auf die Folgen der Nichtrüge hinzuweisen
- Hinweis in Bekanntmachung erforderlich

### Folge fehlenden Hinweises
- Rügefrist läuft nicht
- Auch nicht-gerügte Verfahrensfehler bleiben beachtlich
- Häufiger Treffer in Praxis

### Hinweis-Inhalt
- Hinweis auf einjährige Frist
- Hinweis auf Erfordernis schriftlicher Rüge
- Hinweis auf Inhalt der Rüge (konkrete Bezeichnung)
- Hinweis an wen (Gemeinde)

## Schritt 7 — Rügeschreiben § 215 BauGB praktisch

### Form
- Schriftform
- Adressat: Gemeinde / Stadtverwaltung
- Bezeichnung des Plans (Nummer, Name, Bekanntmachungsdatum)
- Konkrete Bezeichnung des Mangels
- Begründung

### Zeitpunkt
- So früh wie möglich nach Bekanntmachung
- Spätestens 4 Wochen vor Ablauf Jahresfrist
- Per Einschreiben mit Rückschein

### Inhalt
- Alle erkannten Verfahrens- und Form-Fehler aufzählen
- Alle erkannten Abwägungsvorgangs-Fehler aufzählen
- Vorsorglich: Hinweis dass nicht abschließend
- Vorbehalt weiterer Rügen

### Strategische Pflicht
- "Schrotschuss"-Rüge: alle theoretisch denkbaren Mängel sicherheitshalber benennen
- Aber Substanziierung erforderlich — bloße Floskeln genügen nicht

## Schritt 8 — Verhältnis zur Normenkontrolle

### Zeitliche Abfolge
- Tag 0: Bekanntmachung
- Bis Tag 365: Rüge § 215 BauGB und Antrag § 47 VwGO einreichen
- Rüge ist Voraussetzung für materielle Berücksichtigung der Verfahrensfehler im Verfahren

### Bei Verspätung
- Verspätete Rüge bleibt zwar als Beweismittel relevant, aber die Fehler werden unbeachtlich
- Materielle Ergebnisfehler bleiben angreifbar
- § 1 Abs. 3 BauGB und Disproportionalität bleiben angreifbar

## Schritt 9 — Audit-Tabelle

| Fehlerart | § 214 BauGB beachtlich? | § 215 BauGB rügepflichtig? |
|---|---|---|
| Bekanntmachung Anstoßfunktion verletzt | ja (Abs. 1 Nr. 4) | ja |
| Auslegung nicht 1 Monat | ja (Abs. 1 Nr. 2) | ja |
| Online-Veröffentlichung fehlt | ja | ja |
| Erneute Auslegung versäumt | ja | ja |
| Umweltbericht fehlt | ja | ja |
| Abwägungsausfall (Belang nicht erkannt) | ja (Abs. 3) | ja |
| Abwägungsdefizit | ja | ja |
| Disproportionalität (Ergebnis) | stets beachtlich | nein |
| Erforderlichkeit § 1 Abs. 3 BauGB | stets beachtlich | nein |
| Verstoß höherrangiges Recht | stets beachtlich | nein |

## Quellen

- BauGB §§ 1 1a 2 2a 3 4 4a 10 214 215
- BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10 (Präklusion)
- BVerwG, Urteil vom 22.9.2010 – 4 CN 2.10 (Heilung)
- BVerwG, Urteil vom 9.4.2008 – 4 CN 1.07 (Abwägungsvorgang)
- BVerwG, Urteil vom 27.10.1999 – 11 A 31.98 (Offensichtlichkeit)

## Aktuelle Rechtsprechung (Stand 05/2026, verifiziert bverwg.de)

- BVerwG 23.06.2020, 9 A 22.19 — Klimaschutz als Abwaegungsbelang; uebertragbar auf Bauleitplanung (bverwg.de)
- BVerwG 11.04.2024, 4 BN 50.23 — Klimaschutz § 1 Abs. 5 S. 2 BauGB Abwaegungsmaengel (bverwg.de)
- BVerwG 04.05.2022, 4 CN 2.21 — Konzentrationszonen-Planung Wind/Solar (bverwg.de)
- BVerwG 17.06.2020, 4 CN 6.18 — Bekanntmachung B-Plan und Anstossfunktion (bverwg.de)

Weitere Aktenzeichen vor Ausgabe per bverwg.de und OVG/VGH-Datenbanken verifizieren.

## Paragrafenkette Planerhaltung

§ 214 Abs. 1 BauGB (beachtliche Verfahrensfehler) → § 214 Abs. 2a BauGB (§ 13a-Verfahren) → § 214 Abs. 3 BauGB (beachtliche Abwägungsfehler) → § 214 Abs. 4 BauGB (ergänzendes Verfahren) → § 215 Abs. 1 BauGB (Rügefrist 1 Jahr) → § 215 Abs. 2 BauGB (Hinweispflicht) → § 233 BauGB (Übergangsrecht)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Bearbeitung

Kläre nach Mandatsübernahme:
1. Datum der Bekanntmachung der Satzung? (Rügefrist läuft ab diesem Tag)
2. Enthält die Bekanntmachung den Hinweis auf § 215 BauGB-Rügefrist und Rechtsfolgen?
3. Welche Fehler wurden im Aufstellungsverfahren erkannt? (Verfahren/Form/Abwägungsvorgang)
4. Liegt ein Ergebnisfehler vor? (keine Rüge nötig, immer beachtlich)
5. Wurde bereits eine § 215-Rüge erstattet? (Inhalt prüfen auf Konkretheit)
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Fehler-Ruege nach § 215 BauGB fristwahrend stellen | Ruegeschreiben nach Schema; Template unten |
| Variante A — Frist nach § 215 Abs. 1 BauGB bereits abgelaufen | Verfahrensfehler-Heilung pruefen; keine Ruege mehr moeglich |
| Variante B — Fehler nicht ruegefahig weil Materialfehler | § 214 Abs. 1 BauGB Verfahrensfehler vs Materialfehler abgrenzen |
| Variante C — Plan noch nicht in Kraft getreten Ruege praematuer | Abwarten; Ruege erst nach Bekanntmachung des Plans |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template § 215 BauGB Rügeschreiben

**Adressat:** Gemeinde/Stadtverwaltung — Tonfall formell-juristisch, fristwahrend

```
An die Gemeinde/Stadt [NAME]
Rechtsamt
[ANSCHRIFT]

Einschreiben mit Rückschein
[ORT], [DATUM]

Bebauungsplan Nr. [X] "[NAME]" der [GEMEINDE]
Bekanntmachung im Amtsblatt vom [DATUM]
Unser Zeichen: [AZ]

Sehr geehrte Damen und Herren,

im Namen unserer Mandantschaft [NAME] rügen wir gemäß § 215 Abs. 1 BauGB
fristgerecht innerhalb der Jahresfrist ab Bekanntmachung folgende Mängel:

1. Verletzung von § 3 Abs. 2 BauGB — Öffentlichkeitsbeteiligung
 [KONKRETE BEZEICHNUNG DES MANGELS]

2. Verletzung von § 4 Abs. 2 BauGB — Behördenbeteiligung
 [KONKRETE BEZEICHNUNG]

3. Abwägungsdefizit § 1 Abs. 7 i.V.m. § 2 Abs. 3 BauGB
 [KONKRETE BEZEICHNUNG: welcher Belang übersehen / falsch gewichtet]

Wir behalten uns weitere Rügen ausdrücklich vor, soweit uns weiteres
Akten- und Begründungsmaterial zugänglich wird.

[UNTERSCHRIFT]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

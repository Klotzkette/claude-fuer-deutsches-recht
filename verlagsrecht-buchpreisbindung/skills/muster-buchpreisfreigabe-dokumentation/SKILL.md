---
name: muster-buchpreisfreigabe-dokumentation
description: "Buchpreisfreigabe-Dokumentation nach BuchPrG: korrekte Preisfestsetzung und -aufhebung gemäß §§ 3 und 7 BuchPrG, VLB-Protokoll, Ausnahmenbelege nach § 6 BuchPrG im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung."
---

# Muster-Buchpreisfreigabe-Dokumentation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Dieser Skill erstellt und prüft die vollständige **Preisbindungs-Dokumentation** eines Verlags für ein konkretes Buch oder eine Titelgruppe. Die Dokumentation umfasst den gesamten Lebenszyklus des gebundenen Ladenpreises: von der Erstfestsetzung über erlaubte Aktionspreise und Sonderkonditionen bis hin zur rechtssicheren Aufhebung der Preisbindung.

Korrekte Dokumentation ist nicht nur eine rechtliche Pflicht nach **BuchPrG §§ 3 und 7**, sondern dient auch als Beweismittel im Streitfall. Behörden (Kartellamt), der Börsenverein und klagebefugte Verbände können jederzeit Nachweis verlangen. Fehlt die Dokumentation, drohen Bußgelder nach **BuchPrG § 13** und zivilrechtliche Unterlassungsansprüche.

Der Skill richtet sich an Verlagscontrolling, Vertriebsleiter und Rechtsabteilungen, die Preisbindungsvorgänge rechtssicher nachweisen wollen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle (URL) |
|------|--------|-------------|
| BuchPrG § 3 | Preisbindungspflicht; Festsetzung des Ladenpreises durch Verleger | https://www.gesetze-im-internet.de/buchprg/__3.html |
| BuchPrG § 4 | Bindung des Letztabnehmers | https://www.gesetze-im-internet.de/buchprg/__4.html |
| BuchPrG § 5 | Ausnahmen für Letztabnehmer | https://www.gesetze-im-internet.de/buchprg/__5.html |
| BuchPrG § 6 | Ausnahmen von der Preisbindung | https://www.gesetze-im-internet.de/buchprg/__6.html |
| BuchPrG § 7 | Aufhebung der Preisbindung | https://www.gesetze-im-internet.de/buchprg/__7.html |
| BuchPrG § 9 | Durchsetzung; Klagebefugnis | https://www.gesetze-im-internet.de/buchprg/__9.html |
| BuchPrG § 13 | Bußgeld | https://www.gesetze-im-internet.de/buchprg/__13.html |
| MwStG / UStG | Mehrwertsteuer auf Bücher (7 % ermäßigt) | https://www.gesetze-im-internet.de/ustg_1980/__12.html |

## Dokumentationsstruktur: Lebenszyklus eines Ladenpreises

### Phase 1: Erstfestsetzung des Ladenpreises

#### Pflichtinhalt der Preisfestsetzungs-Dokumentation

| Dokument-Element | Inhalt | Pflichtfeld? |
|-----------------|--------|-------------|
| Titel / ISBN-13 | Eindeutige Werkidentifikation | Ja |
| Verlag (Name, Adresse) | Rechtsträger der Preisbindung | Ja |
| Festgesetzter Ladenpreis (brutto) | Inkl. 7 % MwSt. | Ja |
| Nettopreis (netto) | Ladenpreis ÷ 1,07 | Ja |
| Gültig ab (Datum) | Datum der Preisbindungswirkung | Ja |
| Erscheinungsdatum | Datum der Erstauslieferung | Ja |
| VLB-Meldung | Datum und Bestätigungsnummer | Empfohlen |
| Zuständige Person | Unterzeichner im Verlag | Empfohlen |

#### VLB-Meldeprozess

```
Schritt 1: Titeldaten im VLB/Midas eingeben (ISBN, Titel, Preis, Erscheinungsdatum)
Schritt 2: Preis als "Ladenpreis DE" mit Mehrwertsteuersatz 7 % anlegen
Schritt 3: Auslieferungsanweisung an Auslieferung: Ladenpreis = EUR [X,XX] ab [Datum]
Schritt 4: Bestätigung der Meldung archivieren (VLB-Datenbankstand mit Zeitstempel)
Schritt 5: Sicherungskopie der Preismeldung in Verlagsakte
```

### Phase 2: Preisänderungen während der Bindungsdauer

#### Zulässige Preisänderungen

| Art der Änderung | Zulässig? | Dokumentationspflicht |
|-----------------|----------|----------------------|
| Reguläre Preiserhöhung | Ja | Neue VLB-Meldung mit Datum; alte Preisbindung bis Datum X, neue ab Datum Y |
| Preissenkung (dauerhafte) | Ja | Neue VLB-Meldung |
| Zeitlich befristete Aktion (§ 6 Abs. 1 Nr. 1 BuchPrG) | Ja, max. 3 Jahre nach Erscheinen | Aktionsdokument: Titel, Aktionspreis, Laufzeit (von–bis), Begründung |
| Mängelexemplar-Preis (§ 6 Abs. 1 Nr. 2 BuchPrG) | Ja | Mängelnachweis: Art des Mangels, Exemplar-Menge, Neuer Preis |
| Subskriptionspreis | Ja, vor Erscheinen | Subskriptionsangebot dokumentieren |

#### Mängelexemplar-Dokumentation (§ 6 Abs. 1 Nr. 2 BuchPrG)

```
Datum: [TT.MM.JJJJ]
ISBN: [978-3-XXXXX-XXX-X]
Exemplar-Anzahl: [Anzahl]
Art des Mangels: □ Druckfehler (Seite ___) □ Beschädigung □ Vergilbung □ Sonstiges: ___
Mängelpreis: EUR [X,XX] (entspricht [XX] % Nachlass auf Ladenpreis)
Gültig ab: [Datum]
Verantwortlicher: [Name, Funktion]
Unterschrift: ___________________
```

### Phase 3: Ausnahmen nach § 6 BuchPrG

#### Vollständige Ausnahmen-Übersicht

| Ausnahme | Norm | Bedingung | Dokumentation |
|----------|------|-----------|---------------|
| Bücher außerhalb des Anwendungsbereichs | § 1 BuchPrG | Nicht in DE/AT erschienen und nicht in DE/AT angeboten | Nachweis: Erscheinungsland, kein Angebot in DE |
| Mängelexemplare | § 6 Abs. 1 Nr. 2 | Sichtbarer Mangel, übliche Verkaufsbezeichnung erkennbar | Mängelprotokoll |
| Bücher aus Bibliotheken und Restbuchhandlungen | § 6 Abs. 1 Nr. 3 | Bibliothek/Restbuchhandlung verkauft eigenen Bestand | Nachweis: Herkunft aus eigener Bibliothek |
| Export ins Ausland | § 6 Abs. 1 Nr. 4 | Letztabnehmer außerhalb Deutschlands | Nachweis: Lieferadresse außerhalb DE |
| Zeitlich begrenzte Sonderaktion bei Neuerscheinungen | § 6 Abs. 2 | Maximal 3 Jahre nach Ersterscheinen | Aktionsdokument (s.o.) |
| Schulbücher (öffentliche Beschaffung) | § 5 Abs. 2 | Kauf durch Schule/Behörde | Bestellnachweis Schule/Behörde |

### Phase 4: Aufhebung der Preisbindung (§ 7 BuchPrG)

#### Aufhebungs-Pflichtdokument

```
BUCHPREISFREIGABE-DOKUMENT
==========================
Datum der Aufhebung: [TT.MM.JJJJ]
ISBN-13: [978-3-XXXXX-XXX-X]
Titel: [Werktitel]
Bisheriger Ladenpreis: EUR [X,XX] (brutto, 7 % MwSt.)
Grund der Aufhebung: □ Vergriffenheit (§ 17 VerlG / keine Lieferbarkeit mehr)
 □ Ablauf der geplanten Lieferbarkeit
 □ Verlagsauflösung/-verkauf
 □ Sonstiger Grund: ___________________________
Lagerbestand bei Aufhebung: [Anzahl] Exemplare
Verbleib Restbestand: □ Veräußerung ohne Preisbindung □ Einmakulierung □ Weitergabe an Restbuchhandlung
VLB-Abmeldung: □ Erfolgt am [Datum] □ Bestätigung Nr. [___]
Auslieferungs-Information: □ Informiert am [Datum] per [E-Mail/Schreiben]
Buchhandels-Information: □ Informiert am [Datum] per [E-Mail/Schreiben]
Verantwortlicher: [Name, Funktion]
Unterschrift: ___________________
```

#### Fristen und Pflichten bei Aufhebung

| Schritt | Inhalt | Frist |
|---------|--------|-------|
| VLB-Abmeldung | Preis als aufgehoben melden; Lieferstatus auf „vergriffen" | Unverzüglich |
| Auslieferungs-Information | Auslieferung über Preisaufhebung informieren | Gleichzeitig mit VLB |
| Buchhandels-Information | Sofern Restexemplare noch im Buchhandel | Unverzüglich |
| Interne Archivierung | Aufhebungs-Dokument in Verlagsakte | Dauerhaft (10 Jahre empfohlen) |
| Steuerliche Behandlung | MwSt.-Anpassung prüfen bei Restverkauf unter bisherigem Preis | Mit Aufhebung |

## Dokumentation für digitale Produkte (E-Books)

E-Books unterliegen nach deutschem Recht ebenfalls der **Buchpreisbindung** (BGH, Urt. v. 20.05.2021 — I ZR 136/20). Für digitale Produkte gelten besondere Dokumentationspflichten:

| Dokument-Element | E-Book | Print |
|-----------------|--------|-------|
| Preis-Dokumentation | Ja, pro Plattform | Ja |
| Plattform-Rabatte | Gesondert dokumentieren | n/a |
| MwSt. | 7 % (ab 2020) | 7 % |
| Aufhebung bei Rückzug von Plattform | Plattformvertrag kündigen + Preisaufhebungsdokument | VLB-Abmeldung |

### Plattform-Preisbindungs-Protokoll (E-Book)

```
Plattform: [Amazon KDP / Tolino / Apple Books / ...]
ASIN/EAN: [Kennung auf Plattform]
Festgesetzter Preis: EUR [X,XX] (inkl. 7 % MwSt.)
Plattform-Rabatt: [XX] % (nach Plattformvertrag)
Nettoerlös Verlag: EUR [X,XX]
Datum Einstellung auf Plattform: [TT.MM.JJJJ]
Datum Preisänderung: [TT.MM.JJJJ] → Neuer Preis: EUR [X,XX]
Datum Rückzug von Plattform: [TT.MM.JJJJ]
Preisaufhebung erklärt: □ Ja, Datum: [___] □ Nein, weiter auf anderer Plattform verfügbar
```

## Revisionssichere Archivierung

### Aufbewahrungsfristen

| Dokument | Aufbewahrungsfrist | Basis |
|----------|--------------------|-------|
| Preisfestsetzungs-Dokument | Mindestens 10 Jahre nach Aufhebung | Handelsrechtliche Grundsätze |
| VLB-Meldungsbelege | Mindestens 10 Jahre | Handelsrechtliche Grundsätze |
| Mängelexemplar-Protokolle | 5 Jahre nach Verkauf | Verjährungsrecht |
| Aufhebungs-Dokumentation | Dauerhaft (Empfehlung) | Beweis im Streitfall |
| Ausnahmen-Belege (§ 6) | 5 Jahre nach Vorgang | Verjährungsrecht |

## Typische Fallen

- **VLB nicht aktualisiert**: Preis im VLB weicht von tatsächlichem Ladenpreis ab → Preisbindungsverletzung durch Buchhandel möglich.
- **Mängelexemplar ohne Kennzeichnung**: „Als Mängelexemplar gekennzeichnet" muss sichtbar auf dem Buch stehen (Klebeband oder Stempel) — fehlt die Kennzeichnung, greift § 6 Abs. 1 Nr. 2 nicht.
- **Exportnachweis lückenhaft**: Verlag behauptet Export ins Ausland, kann aber Lieferadresse nicht nachweisen → Preisbindungsverstoß.
- **E-Book-Plattformrabatt nicht dokumentiert**: Plattform gewährt eigenmächtig Rabatt → Verlag muss widersprechen und dokumentieren.
- **Aufhebung nicht kommuniziert**: Buchhandel verkauft Restexemplare weiter zum alten Preis, obwohl Preisbindung aufgehoben → Verwirrung; Verlag muss proaktiv informieren.

## Checkliste Buchpreisfreigabe-Dokumentation

- [ ] Preisfestsetzungs-Dokument für jede ISBN vorhanden
- [ ] VLB-Meldung mit Zeitstempel archiviert
- [ ] Alle Preisänderungen chronologisch dokumentiert
- [ ] Mängelexemplar-Protokolle für Preisreduzierungen vorhanden
- [ ] Ausnahmen nach § 6 BuchPrG mit Belegen versehen
- [ ] E-Book-Plattformpreise pro Plattform dokumentiert
- [ ] Aufhebungs-Dokument bei Vergriffenheit erstellt
- [ ] VLB bei Aufhebung aktualisiert
- [ ] Auslieferung und Buchhandel informiert
- [ ] Aufbewahrungsfristen eingehalten (mind. 10 Jahre)
- [ ] Steuerliche Behandlung (MwSt.) bei Aufhebung geprüft

## Quellenreferenzen

- BuchPrG § 3: https://www.gesetze-im-internet.de/buchprg/__3.html
- BuchPrG § 6: https://www.gesetze-im-internet.de/buchprg/__6.html
- BuchPrG § 7: https://www.gesetze-im-internet.de/buchprg/__7.html
- BuchPrG § 13: https://www.gesetze-im-internet.de/buchprg/__13.html
- BGH I ZR 136/20 (E-Book-Preisbindung): https://www.bgh.de/
- dejure.org BuchPrG: https://dejure.org/gesetze/BuchPrG
- UStG § 12 (ermäßigter Steuersatz): https://www.gesetze-im-internet.de/ustg_1980/__12.html

## Output-Formate

- Preisfestsetzungs-Vorlage (ausfüllbares Formular)
- Mängelexemplar-Protokoll-Vorlage
- Aufhebungs-Dokument-Vorlage (§ 7 BuchPrG)
- E-Book-Plattform-Preisbindungsprotokoll
- Checkliste Preisbindungs-Compliance (jährliche Revisionskontrolle)
- Ausnahmen-Belegliste nach § 6 BuchPrG


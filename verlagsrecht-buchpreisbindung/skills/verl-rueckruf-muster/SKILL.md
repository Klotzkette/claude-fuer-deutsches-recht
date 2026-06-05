---
name: verl-rueckruf-muster
description: "Verl 046 Rueckruf Vergriffenes Werk Und Neuauflage, Verl 049 Muster Buchpreisfreigabe Dokumentation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 046 Rueckruf Vergriffenes Werk Und Neuauflage, Verl 049 Muster Buchpreisfreigabe Dokumentation

## Arbeitsbereich

Dieser Skill bündelt **Verl 046 Rueckruf Vergriffenes Werk Und Neuauflage, Verl 049 Muster Buchpreisfreigabe Dokumentation** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-046-rueckruf-vergriffenes-werk-und-neuauflage` | Rückruf bei Vergriffenheit eines Werkes nach VerlG § 17 und UrhG § 41: Voraussetzungen, Verfahren, Preisaufhebung nach BuchPrG § 7 und Neuauflage bei anderem Verlag. |
| `verl-049-muster-buchpreisfreigabe-dokumentation` | Buchpreisfreigabe-Dokumentation nach BuchPrG: korrekte Preisfestsetzung und -aufhebung gemäß §§ 3 und 7 BuchPrG, VLB-Protokoll, Ausnahmenbelege nach § 6 BuchPrG. |

## Arbeitsweg

Für **Verl 046 Rueckruf Vergriffenes Werk Und Neuauflage, Verl 049 Muster Buchpreisfreigabe Dokumentation** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-046-rueckruf-vergriffenes-werk-und-neuauflage`

**Fokus:** Rückruf bei Vergriffenheit eines Werkes nach VerlG § 17 und UrhG § 41: Voraussetzungen, Verfahren, Preisaufhebung nach BuchPrG § 7 und Neuauflage bei anderem Verlag.

# Rückruf vergriffenes Werk und Neuauflage

## Zweck dieses Skills

Dieser Skill begleitet Autoren und Verlage bei der rechtlich korrekten Abwicklung von Vergriffenheit und dem daraus folgenden Rückruf von Nutzungsrechten. Wenn ein Verlag ein Werk nicht mehr lieferfähig hält und keine Neuauflage plant, eröffnet das Gesetz dem Urheber spezifische Rückrufmechanismen.

Zentral sind zwei Normen: **VerlG § 17** (Rücktrittrecht des Verlegers und Rückgabe bei Untergang des Werkes) sowie **UrhG § 41** (Rückruf wegen Nichtausübung des Nutzungsrechts). Hinzu kommt die Frage, wann die Buchpreisbindung nach BuchPrG endet und wie ein Neustart beim selben oder einem anderen Verlag rechtssicher gestaltet wird.

Die praktische Bedeutung wächst, da viele Backlist-Titel in Print vergriffen sind, gleichzeitig aber digitale Verwertung (E-Book, Hörbuch, Datenbank) fortbesteht. Autoren müssen verstehen, wann „vergriffen" im Sinne des Gesetzes vorliegt und wann das Rückrufrecht tatsächlich ausgeübt werden kann.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle (URL) |
|------|--------|-------------|
| VerlG § 17 | Vergriffenheit; Recht des Verlegers zum Rücktritt | https://www.gesetze-im-internet.de/verlg/__17.html |
| VerlG § 7 | Pflicht des Verlegers zur Vervielfältigung und Verbreitung | https://www.gesetze-im-internet.de/verlg/__7.html |
| VerlG § 30 | Kündigung bei wesentlicher Vertragsverletzung | https://www.gesetze-im-internet.de/verlg/__30.html |
| UrhG § 41 | Rückruf wegen Nichtausübung des Nutzungsrechts | https://www.gesetze-im-internet.de/urhg/__41.html |
| UrhG § 42 | Rückruf wegen gewandelter Überzeugung | https://www.gesetze-im-internet.de/urhg/__42.html |
| UrhG § 31 | Einräumung von Nutzungsrechten | https://www.gesetze-im-internet.de/urhg/__31.html |
| BuchPrG § 3 | Preisbindungspflicht des Verlegers | https://www.gesetze-im-internet.de/buchprg/__3.html |
| BuchPrG § 7 | Aufhebung der Preisbindung | https://www.gesetze-im-internet.de/buchprg/__7.html |
| DSM-RL Art. 8–11 | Vergriffene Werke und kollektive Lizenzen | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790 |

## Begriff der Vergriffenheit

### Gesetzliche Definition (VerlG § 17)

VerlG § 17 spricht von Vergriffenheit, wenn der Verlag den Titel nicht mehr auf Lager hat und **keine Neuauflage** innerhalb angemessener Frist plant. Es reicht nicht, dass einzelne Exemplare beim Handel vergriffen sind — entscheidend ist, ob der Verlag die **Lieferfähigkeit vollständig eingestellt** hat.

### Kriterien in der Praxis

| Kriterium | Vergriffenheit liegt vor | Vergriffenheit liegt nicht vor |
|-----------|--------------------------|-------------------------------|
| Lagerbestand Verlag | 0 Exemplare | ≥ 1 Exemplar vorrätig |
| Nachdruckankündigung | Keine Planung | Ankündigung innerhalb 12 Monate |
| E-Book verfügbar | Irrelevant für Print-Vergriffenheit | Digitale Ausgabe ≠ Print-Lieferbarkeit |
| BoD-Ausgabe | Kommt auf Vertragsklausel an | Ausdrückliche BoD-Klausel = lieferbar |

### E-Book-Sonderfall

Ein weiterhin lieferbares E-Book verhindert grundsätzlich nicht den Rückruf der **Print-Nutzungsrechte**, wenn der Verlagsvertrag Druck- und Digitalrechte getrennt einräumt. Bei pauschaler Rechteübertragung (alle Nutzungsarten) blockiert ein noch genutztes E-Book den Rückruf nach § 41 UrhG.

## UrhG § 41: Rückruf wegen Nichtausübung

### Voraussetzungen

1. **Nutzungsrecht wurde eingeräumt** (§ 31 UrhG) — Verlagsvertrag muss wirksam bestehen.
2. **Keine angemessene Ausübung** — Der Verlag verwertet das Werk nicht oder erheblich zu wenig.
3. **Fristablauf**: Nach § 41 Abs. 2 UrhG kann der Rückruf frühestens **zwei Jahre nach Einräumung** (bei Filmwerken fünf Jahre) erklärt werden. Bei Verlagsverträgen gilt zusätzlich eine **Frist von einem Jahr nach Ablieferung** des Manuskripts.
4. **Vorherige Abmahnung**: Vor dem Rückruf ist dem Verleger eine **angemessene Nachfrist** zur Aufnahme der Nutzung zu setzen. Erst nach fruchtlosem Ablauf kann der Rückruf erklärt werden.
5. **Verschulden irrelevant**: § 41 UrhG ist verschuldensunabhängig. Selbst unverschuldete Nichtausübung (z. B. wegen Papiermangels) kann den Rückruf auslösen.

### Ausschluss und Verwirkung

- Der Rückruf ist **ausgeschlossen**, wenn der Urheber selbst die Nichtausübung zu vertreten hat (§ 41 Abs. 4 UrhG).
- Er ist **verwirkt**, wenn der Autor jahrelang schweigt und dem Anschein nach duldet.

### Ausübung des Rückrufs

```
Formerfordernis: Schriftform empfohlen (str. str., keine gesetzliche Form vorgeschrieben)
Adressat: Verlagsleitung (Geschäftsführer/Vorstand)
Inhalt: Bezeichnung des Werkes, konkreter Verstoß (Vergriffenheit seit [Datum]),
 Nachfrist (§ 41 Abs. 3: angemessen, i.d.R. 6 Monate),
 Ankündigung des Rückrufs nach Fristablauf
```

## VerlG § 17: Spezifisches Verlagsrecht

VerlG § 17 gibt **dem Verleger** das Recht zurückzutreten, wenn das Werk durch äußere Umstände vernichtet oder unverkäuflich wird (z. B. Veralterung). Für den Autor hat § 17 VerlG dagegen eher beschränkte Bedeutung; sein Hauptinstrument bleibt § 41 UrhG.

Gleichwohl ist § 17 VerlG relevant, wenn der Verlag aktiv vom Vertrag zurücktreten will (z. B. wegen drastisch gesunkenem Absatz) — dann fallen die Nutzungsrechte kraft Gesetzes zurück.

## Buchpreisbindung bei Vergriffenheit

### Automatisches Erlöschen nach BuchPrG § 7

Nach **BuchPrG § 7** ist der Verleger berechtigt, die Preisbindung aufzuheben. Bei faktischer Vergriffenheit (keine Lieferfähigkeit mehr) läuft die Preisbindung ins Leere. Der Buchhandel ist dann nicht mehr zur Einhaltung des bisherigen Ladenpreises verpflichtet, weil keine Exemplare mehr gehandelt werden.

### Pflichten des Verlegers bei Aufhebung

| Schritt | Inhalt | Frist |
|---------|--------|-------|
| 1. VLB-Meldung | Titel als „vergriffen" melden, Preisbindung aufheben | Unverzüglich |
| 2. Benachrichtigung Buchhandel | Mitteilung an Auslieferung und Großhandel | Unverzüglich nach VLB-Meldung |
| 3. Restbestand-Abverkauf | Restexemplare können nun unter bisherigem Ladenpreis verkauft werden | Nach Aufhebung |
| 4. Dokumentation | Nachweis Datum der Aufhebung in Verlagsakte | Dauerhaft |

## Rückgabe der Rechte und Neuauflage

### Rechtslage nach erfolgreichem Rückruf

Nach Wirksamwerden des Rückrufs (§ 41 Abs. 1 UrhG) fallen die eingeräumten Nutzungsrechte an den Urheber zurück. Der Verlag ist fortan **nicht mehr berechtigt**, das Werk zu verbreiten, zu vervielfältigen oder digital anzubieten.

### Checkliste für den Autor nach Rückruf

- [ ] Schriftliche Bestätigung des Rückrufs vom Verlag einholen
- [ ] Lagerbestand beim Verlag prüfen (VerlG § 17: Was geschieht mit Restexemplaren?)
- [ ] VLB-Meldung auf Vergriffenheit kontrollieren
- [ ] ISBN-Rechte klären (ISBN verbleibt beim bisherigen Verlag)
- [ ] Neue ISBN für Neuauflage beantragen
- [ ] Druckdaten/Satz: Gehören Druckdateien dem Verlag oder dem Autor? (Vertragsklausel prüfen)
- [ ] Schutzfristende beachten: Liegt das Werk im gemeinfrei-nahen Bereich?

### Neuauflage beim neuen Verlag

```
Schritt 1: Rechterückfall bestätigen (Rückruf-Bestätigung oder Urteil)
Schritt 2: Neuen Verlagsvertrag schließen — alle Nutzungsarten explizit regeln
Schritt 3: Neue ISBN beantragen (beim neuen Verlag als ISBN-Inhaber)
Schritt 4: Preisbindung neu festsetzen (BuchPrG § 3) und VLB melden
Schritt 5: Ggf. Mängelexemplar-Klausel prüfen (Restexemplare alter Verlag)
```

### Überarbeitete Neuauflage vs. unveränderter Nachdruck

| Variante | Urheberrechtlich | Preisbindung |
|----------|-----------------|--------------|
| Unveränderte Neuauflage | Gleicher Schutz, neuer Verlagsvertrag nötig | Neue Preisfestsetzung nötig |
| Überarbeitete Fassung | Ggf. neues Werk (§ 3 UrhG: Bearbeitung) | Neue ISBN, neue Preisbindung |
| Lizenzausgabe | Lizenznehmer setzt eigenen Preis | Neue Preisbindungsdokumentation |

## DSM-Richtlinie: Vergriffene Werke und kollektive Lizenzen

DSM-RL Art. 8–11 (Richtlinie 2019/790/EU) ermöglicht Verwertungsgesellschaften, **kollektive Lizenzen für vergriffene Werke** zu erteilen. In Deutschland umgesetzt durch **§§ 61–61c UrhG** (verwaiste Werke) und die VG-Wort-Regelungen zum Kulturerbe-Digitalisierungsprogramm.

Praktische Relevanz: Bibliotheken und Archive können vergriffene Werke digital zugänglich machen, wenn der Rechteinhaber nicht mehr auffindbar oder unbekannt ist. Für aktive Rechteinhaber ist diese Regelung nur dann anwendbar, wenn sie ausdrücklich **keine gegenteilige Erklärung** abgegeben haben.

## Typische Fallen

- **Zu früher Rückruf**: Nachfrist nach § 41 Abs. 3 UrhG nicht gesetzt → Rückruf unwirksam.
- **Digitale Verwertung übersehen**: E-Book noch lieferbar → Rückruf der Print-Rechte ggf. nur teilweise möglich.
- **Druckdaten-Eigentum nicht geregelt**: Autor hat nach Rückruf keine Druckdateien → teurer Neusatz nötig.
- **ISBN-Irrtum**: Alte ISBN kann nicht vom neuen Verlag übernommen werden → VLB-Verwirrung.
- **Restbestand nicht abgeklärt**: Alter Verlag verkauft noch vorhandene Lagerexemplare ohne Preisbindung weiter.
- **Schutzfristen-Fehler bei Gemeinfreiheit**: Autor verwechselt eigene Rechte mit gemeinfreiem Inhalt im Werk.

## Checkliste Rückruf vergriffenes Werk

- [ ] Vergriffenheit dokumentieren (VLB-Auszug, Schreiben an Verlag)
- [ ] Verlagsvertrag auf Vergriffenheitsklausel prüfen
- [ ] Zweijahresfrist nach § 41 Abs. 2 UrhG geprüft
- [ ] Nachfristschreiben an Verlag versandt
- [ ] Nachfrist abgelaufen (i.d.R. 6 Monate)
- [ ] Rückruferklärung schriftlich übermittelt
- [ ] Bestätigung des Rechtsfalls erhalten
- [ ] VLB-Meldung Vergriffenheit geprüft
- [ ] Neue Verlagsoptionen evaluiert
- [ ] Druckdaten und Satzrechte geklärt
- [ ] Neue ISBN beantragt
- [ ] Neue Preisbindung nach BuchPrG § 3 festgesetzt

## Quellenreferenzen

- VerlG § 17: https://www.gesetze-im-internet.de/verlg/__17.html
- UrhG § 41: https://www.gesetze-im-internet.de/urhg/__41.html
- UrhG § 42: https://www.gesetze-im-internet.de/urhg/__42.html
- BuchPrG § 7: https://www.gesetze-im-internet.de/buchprg/__7.html
- DSM-RL 2019/790 Art. 8–11: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790
- UrhG §§ 61–61c (verwaiste Werke): https://www.gesetze-im-internet.de/urhg/__61.html
- dejure.org VerlG: https://dejure.org/gesetze/VerlG

## Output-Formate

- Rückruf-Musterbrief (Schritt-für-Schritt mit Nachfristformel)
- Checkliste Rechterückfall nach § 41 UrhG
- Vergleichstabelle: Vergriffenheit Print vs. Digital
- Ablaufdiagramm: Rückruf → Neuauflage → Neue Preisbindung
- Muster-Übersicht: Klauseln im neuen Verlagsvertrag (Druckdaten, ISBN, Restbestand)

## 2. `verl-049-muster-buchpreisfreigabe-dokumentation`

**Fokus:** Buchpreisfreigabe-Dokumentation nach BuchPrG: korrekte Preisfestsetzung und -aufhebung gemäß §§ 3 und 7 BuchPrG, VLB-Protokoll, Ausnahmenbelege nach § 6 BuchPrG.

# Muster-Buchpreisfreigabe-Dokumentation

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

---
name: zvg-berichtswesen-besitzuebernahme-bestellung
description: "Berichtswesen Besitzuebernahme Bestellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Berichtswesen Besitzuebernahme Bestellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Berichtswesen Besitzuebernahme Bestellung** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-berichtswesen-gericht` | Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben § 161 ZVG Rechnungslegung. Prüfraster Besitzerlangung Sachstand Einnahmen Ausgaben Mieter offene Fragen Gerichtsbeschluss-Bedarf. Output Gerichtskonformer Bericht mit Darstellung Einnahmen Ausgaben Mietsituation und Handlungsempfehlungen. Abgrenzung zu zvg-rechnungslegung (Jahresrechnung) und zvg-gläubiger-schuldner-kommunikation. |
| `zvg-besitzuebernahme` | Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhältnisse. Prüfraster Vor-Ort-Termin Objektbeschreibung Nutzungen Rechte Mobilien Forderungen Lasten Ausgaben Schluessel. Output Besitzerlangungsbericht mit Objektprotokoll Fotodokumentation Schluesselliste und Meldung ans Gericht. Abgrenzung zu zvg-aktenanlage-objektcockpit und zvg-berichtswesen-gericht. |
| `zvg-bestellung-beschlagnahme` | Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prüfraster Beschluss Bestallung Objekt Schuldner Gläubiger Rang Umfang Weisungen des Gerichts. Output Prüfliste Beschluss mit Vollständigkeitsvermerk und naechsten Schritten für Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Berichtswesen Besitzuebernahme Bestellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-berichtswesen-gericht`

**Fokus:** Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben § 161 ZVG Rechnungslegung. Prüfraster Besitzerlangung Sachstand Einnahmen Ausgaben Mieter offene Fragen Gerichtsbeschluss-Bedarf. Output Gerichtskonformer Bericht mit Darstellung Einnahmen Ausgaben Mietsituation und Handlungsempfehlungen. Abgrenzung zu zvg-rechnungslegung (Jahresrechnung) und zvg-gläubiger-schuldner-kommunikation.

# Berichtswesen an das Vollstreckungsgericht

## Aufgabe

Erstellt klare, vollständige und belegbare Berichte an das Vollstreckungsgericht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Besitzerlangungsbericht fällig ist
- Gericht Sachstand oder Entscheidungsvorlage verlangt
- wesentliche Ereignisse im Objekt auftreten

## Eingaben

- Objektkarte, Besitzprotokoll, Rent Roll
- Kontostand, Rückstände, Maßnahmen, Risiken
- gerichtliche Verfügung

## Workflow

1. **Adressat und Anlass** - Berichtstyp, Zeitraum und konkrete gerichtliche Frage bestimmen.
2. **Faktenblock** - Objekt, Nutzung, Mieten, Lasten, Maßnahmen, Konto und Risiken aktualisieren.
3. **Entscheidungsbedarf** - Zustimmung, Vorschuss, Maßnahme oder Verteilung klar herausstellen.
4. **Anlagen** - Fotos, Konto, Belege und Tabellen referenzieren.

## Ausgabe

- Besitzerlangungsbericht
- Sachstandsbericht
- Gerichtliche Entscheidungsvorlage

## Qualitätsgates

- § 3 ZwVwV-Bericht vollständig
- Zahlen mit Anlagen
- offene Ermittlungen benannt

## Rote Schwellen

- Gefahr oder Versicherungslücke nicht gemeldet
- Vorschussbedarf verschwiegen
- Bericht ohne Kontostand

## Interne Vorlagen

- assets/templates/monatsbericht-gericht.md
- assets/templates/besitzuebernahme-protokoll.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Berichtswesen

§ 153 ZVG (Pflichten laufende Verwaltung) → § 154 ZVG (Gerichtliche Aufsicht) → § 3 ZwVwV (Besitzerlangungsbericht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 20 ZwVwV (Vergütung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Berichtswesen

1. Wann war der Besitzerlangungstermin? (2-Wochen-Frist für Besitzerlangungsbericht)
2. Welche Berichtsfrequenz hat das Gericht vorgegeben? (Monatlich / Quartalsweise / Jährlich)
3. Sind alle Mieter und Nutzungseinheiten im Bericht vollständig erfasst?
4. Wurden wesentliche Veränderungen (Leerstand Kündigung Mietausfall) zeitnah gemeldet?

## Output-Template Besitzerlangungsbericht (Auszug)

**Adressat:** Amtsgericht / Vollstreckungsgericht — Tonfall formell-berichtend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
Aktenzeichen: [AZ]

Besitzerlangungsbericht
Zwangsverwaltung [ADRESSE]

Sehr geehrte Damen und Herren,

gemäß § 3 ZwVwV erstattet der Unterzeichner Bericht über die Besitzerlangung
am [DATUM]:

1. Zustand des Objekts: [BESCHREIBUNG]
2. Nutzungseinheiten: [TABELLE MIETER/EINHEITEN]
3. Vorgefundene Mängel/Sofortmaßnahmen: [LISTE]
4. Laufende Verträge (Versicherung Dienstleister): [LISTE]
5. Besondere Vorkommnisse: [GGFS. SCHULDNER ANWESEND / ZUGANG VERWEIGERT]
6. Treuhandkonto: Eröffnet bei [BANK], IBAN [X].

[DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```

## 2. `zvg-besitzuebernahme`

**Fokus:** Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhältnisse. Prüfraster Vor-Ort-Termin Objektbeschreibung Nutzungen Rechte Mobilien Forderungen Lasten Ausgaben Schluessel. Output Besitzerlangungsbericht mit Objektprotokoll Fotodokumentation Schluesselliste und Meldung ans Gericht. Abgrenzung zu zvg-aktenanlage-objektcockpit und zvg-berichtswesen-gericht.

# Besitzerlangung und Objektaufnahme

## Aufgabe

Führt durch den Vor-Ort-Termin zur Besitzergreifung mit Bericht nach ZwVwV.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Objekt erstmals betreten oder übernommen wird
- Schlüssel, Zustand und Mieter zu erfassen sind
- Sofortmaßnahmen wegen Gefahr oder Versicherung nötig sind

## Eingaben

- Bestallung, Objektadresse, Schlüsselinfo
- Mieter- und Pächterdaten
- Fotos, Zählerstände, Versicherungen, Dienstleister

## Workflow

1. **Termin vorbereiten** - Beteiligte informieren, Zutritt, Zeugen, Kamera und Checkliste sichern.
2. **Objekt aufnehmen** - Nutzungsart, Zustand, Drittrechte, Mobilien, Forderungen, Lasten und Ausgaben protokollieren.
3. **Gefahren sichern** - Versicherung, Wasser, Strom, Brand, Verkehrssicherung und Notdienst prüfen.
4. **Bericht einreichen** - Besitzerlangungsbericht ans Gericht und Nachermittlungen vormerken.

## Ausgabe

- Besitzübernahmeprotokoll
- Objektzustandsbericht
- Sofortmaßnahmenliste

## Qualitätsgates

- § 3 ZwVwV-Punkte vollständig abgefragt
- Fotos/Belege referenziert
- Nachermittlungen terminiert

## Rote Schwellen

- akute Gefahrenstelle
- fehlende Gebäudeversicherung
- Schuldner verweigert Zugang

## Interne Vorlagen

- assets/templates/besitzuebernahme-protokoll.md
- assets/templates/instandhaltung-gefahrensicherung.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Besitzübernahme

§ 150 ZVG (Besitzeinweisung durch Gericht) → § 152 ZVG (Rechte und Pflichten ab Besitzerlangung) → § 3 ZwVwV (Besitzerlangung und Bericht) → § 858 BGB (verbotene Eigenmacht) → § 869 BGB (Besitzschutz Zwangsverwalter) → § 154 ZVG (Gerichtshilfe bei Verweigerung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Besitzübernahme

1. Liegt die Bestallungsurkunde des Gerichts vor? (Legitimation für Vor-Ort-Termin)
2. Sind alle Mieter vorab informiert worden? (Schreiben mind. 3 Tage vorher)
3. Wer begleitet den Termin? (Zeuge empfohlen bei unklarer Situation, ggf. Schlüsseldienst)
4. Sind Versicherungsnachweise bereits angefordert? (Gebäudeversicherung Pflicht ab Besitzerlangung)
5. Fotodokumentation vorbereitet? (Zustands-Beweis für spätere Haftungsfragen)

## Output-Template Besitzübernahmeprotokoll (Auszug)

```
Besitzübernahmeprotokoll
Zwangsverwaltung [ADRESSE]
Aktenzeichen: [AZ]
Datum/Uhrzeit des Termins: [DATUM] [UHRZEIT]
Anwesende: [ZWANGSVERWALTER, ZEUGE, ggf. SCHULDNER, MIETER]

1. Schlüsselübergabe: [JA/NEIN, wer übergeben, Anzahl Schlüsselsätze]
2. Zählerstände: Strom [X], Gas [Y], Wasser [Z]
3. Vorgefundene Schäden (Fotos als Anhang): [LISTE]
4. Mieter angetroffen: [JA/NEIN, Name, Einheit]
5. Sofortmaßnahmen erforderlich: [LISTE]
6. Schuldner anwesend: [JA/NEIN, Reaktion]

Unterschrift Zwangsverwalter: ___________________
Unterschrift Zeuge: ___________________
```

## 3. `zvg-bestellung-beschlagnahme`

**Fokus:** Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prüfraster Beschluss Bestallung Objekt Schuldner Gläubiger Rang Umfang Weisungen des Gerichts. Output Prüfliste Beschluss mit Vollständigkeitsvermerk und naechsten Schritten für Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit.

# Bestellung und Beschlagnahme

## Aufgabe

Prüft die gerichtliche Grundlage der Zwangsverwaltung und den Umfang der Beschlagnahme.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anordnungs- oder Beitrittsbeschluss eingeht
- Bestallungsurkunde ausgestellt wurde
- unklar ist, welche Rechte und Forderungen erfasst sind

## Eingaben

- Anordnungsbeschluss, Beitritte, Bestallung
- Grundbuch, Forderungsaufstellung, Gläubigerangaben
- gerichtliche Weisungen

## Workflow

1. **Beschlussdaten** - Gericht, Aktenzeichen, Objekt, Schuldner, Gläubiger und Forderung erfassen.
2. **Umfang** - Grundstück, Zubehör, Nutzungen, Forderungen und Rechte bestimmen.
3. **Rang und Beitritt** - betreibende Gläubiger und spätere Beitritte dokumentieren.
4. **Weisungen** - gerichtliche Weisungen und Zustimmungsvorbehalte vormerken.

## Ausgabe

- Beschlussprüfvermerk
- Beschlagnahmeumfang
- Rang- und Gläubigerliste

## Qualitätsgates

- Objektbezeichnung stimmt mit Grundbuch
- Bestellung nicht überdehnt
- Beitritte separat geführt

## Rote Schwellen

- falsches Objekt
- unklare Ranglage
- fehlende Bestallung

## Interne Vorlagen

- assets/templates/bestellungs-und-beschlagnahmecheck.md
- assets/templates/zvg-objektkarte.md

## Amtliche Erstquellen

- § 150 ZVG
- § 2 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bestellung/Beschlagnahme

§ 146 ZVG (Anordnung Zwangsverwaltung) → § 147 ZVG (Beschlagnahme) → § 148 ZVG (Wirkung Beschlagnahme) → § 150 ZVG (Besitzeinweisung) → § 20 ZVG (Wirkung auf Verfügungen) → § 23 ZVG (Beschlagnahme Früchte) → § 57 ZVG (Mieterschutz bei Beschlagnahme)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Bestellung/Beschlagnahme

1. Datum des Zustellungsbeschlusses und Datum der Zustellung an Schuldner? (Beschlagnahme ab Zustellung)
2. Wurden Mieter über die Beschlagnahme informiert? (Zahlungspflicht Miete an Zwangsverwalter)
3. Hat Schuldner vor Beschlagnahme Mieten im Voraus vereinnahmt? (§ 153 ZVG Rückforderung prüfen)
4. Liegt eine eingetragene Grundschuld oder Hypothek vor? (Gläubiger-Rang für Ausschüttungen)

## Output-Template Mieter-Benachrichtigung nach Beschlagnahme

**Adressat:** Mieter — Tonfall sachlich-erklärend

```
[ZWANGSVERWALTER, ADRESSE]

An [MIETER NAME]
[ADRESSE MIETWOHNUNG]

[ORT], [DATUM]

Betreff: Zwangsverwaltung — Zahlungsanweisung für Miete

Sehr geehrte/r Herr/Frau [NAME],

über das Grundstück [ADRESSE, GRUNDBUCHBEZEICHNUNG] wurde durch Beschluss
des Amtsgerichts [ORT] vom [DATUM] (AZ [X]) die Zwangsverwaltung angeordnet.
Ich wurde zum Zwangsverwalter bestellt.

Ab sofort ist die monatliche Miete von [BETRAG] EUR ausschließlich auf
folgendes Treuhandkonto zu zahlen:
IBAN: [X], BIC: [Y], Bank: [Z], Verwendungszweck: [AZ + IHRE EINHEIT]

Zahlungen an den Eigentümer haben nach Beschlagnahme keine schuldbefreiende
Wirkung mehr (§ 148 ZVG).

Mit freundlichen Grüßen
[ZWANGSVERWALTER]
```

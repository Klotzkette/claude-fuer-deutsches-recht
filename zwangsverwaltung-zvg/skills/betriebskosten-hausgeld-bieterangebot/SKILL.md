---
name: betriebskosten-hausgeld-bieterangebot
description: "Betriebskosten Hausgeld Bieterangebot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Betriebskosten Hausgeld Bieterangebot

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Betriebskosten Hausgeld Bieterangebot** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-betriebskosten-hausgeld` | Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld BetrKV Betriebskostenarten. Prüfraster Nebenkosten Dienstleister WEG-Hausgeld Versorger Wirtschaftlichkeit Abrechnung Zahlungsplan Belegpflicht. Output Betriebskosten-Übersicht mit Abrechnungsprotokoll und Zahlungsplan für Gericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung. |
| `zvg-bieterangebot-bewertung` | Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung §§ 44 ff. ZVG bestehenbleibende Rechte. Prüfraster Verkehrswert geringstes Gebot Sicherheitsleistung bestehenbleibende Rechte Mietlage Sanierungsrisiko Bietlimit. Output Investoren-Bewertungsreport mit empfohlenem Bietlimit Risikoeinschaetzung und Finanzierungsgrundlage. Abgrenzung zu zvg-versteigerungsteilnahme und zvg-verkauf-versteigerung-schnittstelle. |
| `zvg-glaeubiger-schuldner-kommunikation` | Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kündigung § 535 BGB Mietrecht. Prüfraster Adressat Anlass Normbezug Ton Fristen Dokumentation. Output Schreibenpaket mit Vorlagen für alle typischen Kommunikationsanlaesse in der Zwangsverwaltung. Abgrenzung zu zvg-berichtswesen-gericht (nur Gericht) und zvg-miet-und-pachtverwaltung. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Betriebskosten Hausgeld Bieterangebot**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zvg-betriebskosten-hausgeld`

**Fokus:** Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld BetrKV Betriebskostenarten. Prüfraster Nebenkosten Dienstleister WEG-Hausgeld Versorger Wirtschaftlichkeit Abrechnung Zahlungsplan Belegpflicht. Output Betriebskosten-Übersicht mit Abrechnungsprotokoll und Zahlungsplan für Gericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung.

# Betriebskosten, Hausgeld und laufende Objektkosten

## Aufgabe

Verhindert, dass laufende Objektkosten, Hausgeld und Versorgerleistungen die Verwaltung destabilisieren.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- WEG-Hausgeld, Betriebskosten oder Versorgerrechnungen eingehen
- Abrechnungen erstellt oder geprüft werden müssen
- Liquiditätsengpass bei laufender Verwaltung entsteht

## Eingaben

- Hausgeldabrechnung, Wirtschaftsplan, Versorgerverträge
- Betriebskostenbelege, Dienstleisterrechnungen
- Mieter-Vorauszahlungen und Leerstände

## Workflow

1. **Kosten erfassen** - laufende Kosten, öffentliche Lasten, Hausgeld, Dienstleister und Versorger trennen.
2. **Umlage prüfen** - umlagefähige und nicht umlagefähige Positionen markieren.
3. **Liquidität** - Fälligkeiten mit Mieten und Vorschussbedarf abgleichen.
4. **Abrechnung** - Betriebskosten- oder WEG-Schnittstellen für Bericht vorbereiten.

## Ausgabe

- Kostenmatrix
- Zahlungsplan
- Abrechnungsvorbereitung

## Qualitätsgates

- öffentliche Lasten separat
- Umlagefähigkeit geprüft
- Fälligkeit belegt

## Rote Schwellen

- Versorgungssperre
- Hausgeldrückstand mit Verwalterdruck
- unwirtschaftlicher Dienstleister

## Interne Vorlagen

- assets/templates/betriebskosten-hausgeld.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- §§ 9, 13, 15 ZwVwV
- § 155 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Betriebskosten/Hausgeld

§ 153 ZVG (laufende Ausgaben) → § 155 ZVG (Verteilungsplan) → § 10 Abs. 1 Nr. 2 ZVG (Rangklasse Hausgeld) → §§ 8-10 ZwVwV (Ausgaben Verwaltung) → § 16 Abs. 2 WEG (Kostentragung Wohnungseigentuemer) → §§ 556-556d BGB (Betriebskosten Mietverhältnis)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Betriebskosten/Hausgeld

1. Handelt es sich um eine WEG-Einheit? (Hausgeld-Rückstände haben Vorrang in § 10 ZVG)
2. Sind laufende Betriebskostenvorauszahlungen in den Mietverträgen ausgewiesen?
3. Welche Betriebskosten zahlt der Zwangsverwalter direkt? (Versicherung Grundsteuer Energie)
4. Liegen Hausgeld-Rückstände aus der Zeit vor Beschlagnahme vor?

## Schritt-für-Schritt-Betriebskostenabrechnung ZVG

1. Alle Kostenpositionen mit Belegen erfassen (Heizung Wasser Müll Hausmeister)
2. Umlageschlüssel aus Mietverträgen und WEG-Beschlüssen prüfen
3. Abrechnungszeitraum festlegen (Kalenderjahr oder Verwaltungszeitraum)
4. Soll-Vorauszahlungen der Mieter gegen tatsächliche Kosten abgleichen
5. Nachzahlungen oder Guthaben berechnen und Mieter informieren
6. Überschüsse in Verteilungsplan nach § 155 ZVG einbeziehen

## 2. `zvg-bieterangebot-bewertung`

**Fokus:** Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung §§ 44 ff. ZVG bestehenbleibende Rechte. Prüfraster Verkehrswert geringstes Gebot Sicherheitsleistung bestehenbleibende Rechte Mietlage Sanierungsrisiko Bietlimit. Output Investoren-Bewertungsreport mit empfohlenem Bietlimit Risikoeinschaetzung und Finanzierungsgrundlage. Abgrenzung zu zvg-versteigerungsteilnahme und zvg-verkauf-versteigerung-schnittstelle.

# Bieterangebot Bewerten

## Aufgabe

Bewertet ein Objekt aus der Zwangsversteigerung oder ein vor-/außerterminliches Angebot. Der Skill ersetzt keine Finanzierung, Besichtigung oder anwaltliche Endprüfung; er macht die Risiken entscheidungsfähig.

## Startet bei

- "Ist dieses Versteigerungsangebot attraktiv?"
- "Welches Bietlimit ist plausibel?"
- "Was bedeutet Mindestgebot?"
- "Wie bewerte ich Gutachten, Grundbuch und Mietvertrag?"

## Workflow

1. **Unterlagen inventarisieren**: Bekanntmachung, Gutachten, Grundbuch, Teilungserklärung, Mietvertrag, Hausgeld, Protokolle, Baulasten, Energie, Versicherungen.
2. **Rechtsbegriffe sauberziehen**: Umgangssprachlich "Mindestgebot" meist vom rechtlichen "geringsten Gebot" unterscheiden.
3. **Wertbasis prüfen**: Verkehrswert, Stichtag, Innen-/Außenbesichtigung, Bewertungsverfahren, Abschläge, Vergleichsdaten, Marktrisiko.
4. **Lasten prüfen**: Abteilung II, Abteilung III soweit bekannt, bestehenbleibende Rechte, Rückstände, öffentliche Lasten, WEG-Hausgeld, Sonderumlagen.
5. **Nutzung prüfen**: Mietvertrag, tatsächliche Nutzung, Klingel-/Briefkasten-Abweichungen, Renovierungsabreden, Kündigungs-/Räumungsrisiko.
6. **Bietlimit rechnen**: Maximalbudget minus Sicherheitsabschlag, Erwerbsnebenkosten, Sanierung, Leerstand, Prozesskosten, Finanzierungspuffer und bestehenbleibende Rechte.
7. **Ampel ausgeben**: GRÜN nur bei belegtem Wert, klaren Lasten und ausreichendem Puffer; sonst GELB/ROT mit Nachforderungen.

## Ausgabe

- Bieterangebots-Matrix
- Bietlimit mit Annahmen
- offene Fragen an Gericht, Verwalter, WEG-Verwaltung, Bank oder Sachverständigen
- Entscheidung: beobachten, nachrecherchieren, bieten, nicht bieten

## Qualitätsgates

- Keine Gewährleistungsannahmen: ZVG-Erwerb ist kein normaler Kaufvertrag.
- Geringstes Gebot und 5/10-/7/10-Grenzen werden getrennt erläutert.
- Sicherheitsleistung wird auf Basis des Verkehrswerts geprüft.
- Bietlimit enthält Finanzierung und Liquidität, nicht nur Kaufpreis.

## Rote Schwellen

- Nur Außenbesichtigung und zugleich hoher Sanierungshebel
- unklare tatsächliche Nutzung oder gewerbliche Hinweise in Wohnraum
- bestehenbleibende Rechte nicht verstanden
- Angebot drängt zu schneller Zahlung außerhalb klarer Gerichts-/Notarstruktur

## Interne Vorlage

- `assets/templates/bieterangebot-bewertung.md`

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bieterangebot/Versteigerungsschnittstelle

§ 152 ZVG (Verwalterpflichten) → § 56 ZVG (Übergabe an Ersteher) → § 57 ZVG (Mieterschutz bei Eigentumsübergang) → § 57a ZVG (Sonderkündigungsrecht Ersteher) → §§ 566-566e BGB (Kauf bricht nicht Miete) → § 155 ZVG (Verteilungsplan bis Versteigerung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Bieterangebot/Versteigerung

1. Ist ein Versteigerungstermin angesetzt? (Auftrag des Gerichts, Mieterliste und Zustands-Bericht vorzubereiten)
2. Sind alle Mietverhältnisse vollständig dokumentiert? (Laufzeit Miete Rückstände)
3. Gibt es Anhaltspunkte für Mietrechte die dem Bieter nicht bekannt sein könnten?
4. Plant der Ersteher eine Eigennutzung? (Sonderkündigungsrecht § 57a ZVG prüfen)

## Output-Template Versteigerungsinfo-Bericht (Auszug)

```
Information für Bieter im Versteigerungsverfahren
AZ: [X]
Objekt: [ADRESSE]
Stand: [DATUM]

Vermietungsstand:
Nr. | Mieter | Einheit | Nettomiete | NK-VZ | Vertragsende | Rückstände
1 | [...] | [...] | [...] | [...] | [unbefristet] | [BETRAG]

Sonderrechte: [Vorkaufsrechte Vormerkungen etc.]
Technischer Zustand: [ZUSAMMENFASSUNG]
Zu beachten für Ersteher: Mietverhältnisse gehen gem. §§ 566 BGB über;
Sonderkündigungsrecht § 57a ZVG nur innerhalb von 2 Wochen nach Zuschlag.
```

## 3. `zvg-glaeubiger-schuldner-kommunikation`

**Fokus:** Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kündigung § 535 BGB Mietrecht. Prüfraster Adressat Anlass Normbezug Ton Fristen Dokumentation. Output Schreibenpaket mit Vorlagen für alle typischen Kommunikationsanlaesse in der Zwangsverwaltung. Abgrenzung zu zvg-berichtswesen-gericht (nur Gericht) und zvg-miet-und-pachtverwaltung.

# Gläubiger-, Schuldner- und Drittschuldnerkommunikation

## Aufgabe

Erstellt klare, rollenrichtige Schreiben in der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieter, Schuldner, Gläubiger oder Behörden informiert werden müssen
- Konflikte über Zutritt, Mieten oder Maßnahmen entstehen
- Gerichtskommunikation vorbereitet wird

## Eingaben

- Rolle und Adressat
- Beschluss, Objekt, Anlass, gewünschte Reaktion
- Frist, Belege und Tonalität

## Workflow

1. **Adressat klären** - Rolle, Rechte, Pflichten und Zustellweg bestimmen.
2. **Kernbotschaft** - Was ist passiert, was wird verlangt, bis wann, mit welcher Folge.
3. **Belege** - Beschluss, Bestallung, Konto, Fotos oder Tabellen beifügen.
4. **Nachhalten** - Wiedervorlage, Antwortauswertung und Eskalation setzen.

## Ausgabe

- Schreibenentwurf
- Anlagenliste
- Wiedervorlage

## Qualitätsgates

- keine Drohung ohne Grundlage
- Zahlstelle eindeutig
- Adressat nicht verwechselt

## Rote Schwellen

- Schuldner blockiert Objektzugang
- Mieter zahlen falsch
- Gläubiger drängt auf unzulässige Sonderzahlung

## Interne Vorlagen

- assets/templates/schuldner-glaeubiger-kommunikation.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 4 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Gläubiger-Schuldner-Kommunikation

§ 154 ZVG (Aufsicht durch Gericht) → § 153 Abs. 2 ZVG (Auskunftspflicht) → §§ 13-15 ZwVwV (Buchführung Rechnungslegung) → § 20 ZwVwV (Vergütung und Rechenschaft) → § 242 BGB (Treu und Glauben, Auskunftsanspruch analog)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Kommunikation

1. Wer ist betreibender Gläubiger? (Alle Gläubiger in Rangklassen nach § 10 ZVG erfassen)
2. Liegt eine Bevollmächtigung des Gläubigers vor? (Ansprechpartner/Kanzlei)
3. Kommuniziert der Schuldner kooperativ? (Verweigerung → Gerichtsantrag)
4. Haben weitere Gläubiger beigetreten?

## Output-Template Gläubigerinfo-Schreiben (Auszug)

**Adressat:** Betreibender Gläubiger — Tonfall formell-berichtend

```
An [GLÄUBIGER / BEVOLLMÄCHTIGTE KANZLEI]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]
Quartalsbericht [QUARTAL/JAHR]

Sehr geehrte Damen und Herren,

zum Stand der Zwangsverwaltung berichte ich:

Einnahmen [QUARTAL]: [BETRAG]
Ausgaben [QUARTAL]: [BETRAG]
Kontostand per [DATUM]: [BETRAG]
Ausschüttungsfähiger Betrag nach Rücklage: [BETRAG]

Besondere Vorkommnisse: [LEERSTAND REPARATUR RECHTSTREIT]

Nächster Auszahlungsantrag: [DATUM]

[UNTERSCHRIFT ZWANGSVERWALTER]
```

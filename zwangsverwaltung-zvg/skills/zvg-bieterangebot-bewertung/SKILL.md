---
name: zvg-bieterangebot-bewertung
description: "Bewertet Zwangsversteigerungsobjekte aus Investorensicht fuer Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung §§ 44 ff. ZVG bestehenbleibende Rechte. Pruefraster Verkehrswert geringstes Gebot Sicherheitsleistung bestehenbleibende Rechte Mietlage Sanierungsrisiko Bietlimit. Output Investoren-Bewertungsreport mit empfohlenem Bietlimit Risikoeinschaetzung und Finanzierungsgrundlage. Abgrenzung zu zvg-versteigerungsteilnahme und zvg-verkauf-versteigerung-schnittstelle."
---

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

- BGH, Beschl. v. 05.11.2004 - IX ZB 183/03, NZI 2005, 108 Rn. 14 — Der Zwangsverwalter ist nicht berechtigt, das verwaltete Grundstück zu veräußern; er kann jedoch Mietrechte begründen und ist verpflichtet, unberechtigte Nutzungen zu beenden, wenn sie den Grundstückswert gefährden.
- BGH, Beschl. v. 18.05.2006 - IX ZB 25/05, NZI 2006, 531 — Wenn in der Zwangsverwaltung ein Versteigerungstermin ansteht, hat der Zwangsverwalter das Gericht über den Objektzustand und bestehende Mietverhältnisse zu unterrichten; er muss sicherstellen, dass Bieter über die tatsächliche Vermietungssituation informiert werden können.

## Paragrafenkette Bieterangebot/Versteigerungsschnittstelle

§ 152 ZVG (Verwalterpflichten) → § 56 ZVG (Übergabe an Ersteher) → § 57 ZVG (Mieterschutz bei Eigentumsübergang) → § 57a ZVG (Sonderkündigungsrecht Ersteher) → §§ 566-566e BGB (Kauf bricht nicht Miete) → § 155 ZVG (Verteilungsplan bis Versteigerung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., §§ 56-57a Rn. 1-40 (Übergang auf Ersteher Mietrecht)
- Böttcher ZVG 6. Aufl., § 56 Rn. 10-30 (Übergabepflicht Zwangsverwalter)

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
1   | [...]  | [...]   | [...]      | [...]  | [unbefristet] | [BETRAG]

Sonderrechte: [Vorkaufsrechte Vormerkungen etc.]
Technischer Zustand: [ZUSAMMENFASSUNG]
Zu beachten für Ersteher: Mietverhältnisse gehen gem. §§ 566 BGB über;
Sonderkündigungsrecht § 57a ZVG nur innerhalb von 2 Wochen nach Zuschlag.
```

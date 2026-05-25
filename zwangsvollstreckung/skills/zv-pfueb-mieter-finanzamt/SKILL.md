---
name: zv-pfueb-mieter-finanzamt
description: "PfÜB gegen sonstige Drittschuldner: Mieter (Mietzinsforderung), Finanzamt (Steuererstattung, Kindergeld nur eingeschränkt), Krankenkassen (Krankengeld), Versicherungen (Rückkaufswert), Geschäftspartner (offene Rechnungen). Beachtet § 851 ZPO Unübertragbarkeit, § 850b ZPO bedingt pfändbare Bezüge, § 46 AO Steueranspruchsabtretung. Lädt, wenn weder Bank noch Arbeitgeber Drittschuldner ist."
---

# PfÜB Mieter, Finanzamt, sonstige Drittschuldner

## Aufgabe

Pfändung beweglicher Forderungen jenseits von Bank und Arbeitgeber. Häufigste Fälle: Mietzins (Vermieter ist Schuldner, Mieter ist Drittschuldner), Steuererstattung gegen Finanzamt, Versicherungsleistungen, B2B-Forderungen.

## Startet bei

- Titel + Klausel + Zustellung grün
- Drittschuldner identifizierbar (Person, Sitz)
- Forderung nicht nach § 851 ZPO unpfändbar

## Rechtsgrundlagen

- §§ 829, 835 ZPO – allgemeine Forderungspfändung
- § 851 ZPO – unpfändbare Forderungen
- § 851a ZPO – Pfändungsschutz Landwirt
- § 851b ZPO – Pfändungsschutz Miete (Mieterperspektive – hier umgekehrt)
- § 850b ZPO – bedingt pfändbare Bezüge (Renten aus Versicherung, Schmerzensgeld)
- § 46 AO – Steueranspruchsabtretung und -pfändung
- § 54 SGB I – Pfändbarkeit Sozialleistungen
- §§ 21, 22 EStG mittelbar (Mietzins als Forderung)

## Workflow

1. **Drei-Säulen-Prüfung**.
2. **Drittschuldner exakt bezeichnen**: Mieter (Vor- und Nachname), Finanzamt mit zuständiger Behörde, Versicherungs-AG mit Sitz.
3. **Forderung definieren**:
   - Mietzins: laufender Anspruch des Vermieters gegen den Mieter aus Mietvertrag vom DD.MM.JJJJ, einschließlich Nebenkostennachzahlungen, einschließlich künftiger Mieten.
   - Finanzamt: alle Einkommensteuer-Erstattungsansprüche des Schuldners für VZ x ff., einschließlich Solidaritätszuschlag.
   - Versicherung: Rückkaufswert oder fällige Leistungen aus Police Nr. x.
4. **Pfändungsverbote prüfen**:
   - § 851 ZPO: unübertragbare Forderungen
   - § 850b ZPO: Sterbegeld, Schmerzensgeld – nur eingeschränkt pfändbar
   - § 54 SGB I: Kindergeld nur für Unterhalt des Kindes pfändbar
5. **Vollstreckungsgericht**: Wohnsitz Schuldner (§ 828 Abs. 2 ZPO).
6. **Antrag** auf ZVFV-Formular, ab 1.10.2026 XML-Antrag.
7. **Zustellung** an Drittschuldner durch GV oder ab 1.10.2027 elektronisch (sofern Behörde/Unternehmen Postfach eröffnet).
8. **Drittschuldnererklärung § 840 ZPO** abwarten.
9. **Bei Finanzamt-Pfändung**: parallele Abtretungsanzeige nach § 46 AO ist verfahrensmäßig oft schneller, aber rechtlich anders zu bewerten – Mandanten beraten.

## Sonderfall Mieter als Drittschuldner

Pfändung der Mietforderung. Wichtige Punkte:

- Der Mieter darf nach Pfändung nur noch an den Gläubiger zahlen.
- Der Mieter kann mit eigenen Gegenforderungen gegen den Vermieter aufrechnen, soweit § 392 BGB nichts entgegensteht.
- Mietminderung bleibt möglich, Pfändung erfasst nur den tatsächlich geschuldeten Betrag.
- BGH 6.7.2005 – VIII ZR 209/04: Mieter zahlt schuldbefreiend an Gläubiger nach Zustellung.

## Sonderfall Steuererstattung

- § 46 AO regelt Abtretung und Pfändung. Anzeige beim Finanzamt zwingend.
- Erfasst werden Erstattungsansprüche für laufenden VZ und künftige – soweit hinreichend bestimmt.
- Vorauszahlungen sind keine Erstattung, sondern Vorleistung.
- BFH 21.3.2014 – VII R 28/13: Pfändung künftiger Erstattungsansprüche zulässig, wenn Veranlagungszeiträume bezeichnet.

## Leitentscheidungen

- BGH 6.7.2005 – VIII ZR 209/04 (Mieter zahlt schuldbefreiend nach Pfändung)
- BFH 21.3.2014 – VII R 28/13 (Pfändung künftiger Steuererstattung)
- BGH 19.3.2004 – IXa ZB 321/03 (Pfändung Lebensversicherung-Rückkaufswert)
- BGH 4.10.2018 – IX ZB 7/18 (Reichweite bei Dauerschuldverhältnissen)

## Ausgabeformat

```
PFÜB SONSTIGER DRITTSCHULDNER [Mandant] / [Schuldner]

Titel:                 [Art, Datum, Aussteller]
Forderung Schuldner:   EUR Haupt + EUR Zinsen + EUR Kosten
Drittschuldner:        [Mieter / Finanzamt / Versicherung / Geschäftspartner]
Gepfändete Forderung:  [genaue Bezeichnung mit Rechtsgrund und Zeitraum]
Pfändungsverbote:      [§ 851 / § 850b / § 54 SGB I geprüft]
Zustellungsweg:        GV Papier / eBO / ab 1.10.2027 ggf. elektronisch

NÄCHSTER SCHRITT:      Drittschuldnererklärung
WIEDERVORLAGE:         DD.MM.JJJJ
```

## Qualitätsgates

- Niemals unpfändbare Forderungen pfänden (§ 851 ZPO – Sozialhilfe nicht abgrenzbar).
- Niemals Kindergeld pfänden, außer für privilegierte Unterhaltsforderung.
- Bei Steuererstattung: Zeitraum konkret nennen, sonst Pfändung zu unbestimmt.
- Bei Mietzins: Mieter darf nicht doppelt zahlen – schriftliche Aufforderung an Mieter zur Zahlung an Gläubiger.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-elektronische-zustellung-2027`
- `zv-vermoegensauskunft-gv` – wenn Forderungen unbekannt
- `zv-kontensuche-drittschuldner`

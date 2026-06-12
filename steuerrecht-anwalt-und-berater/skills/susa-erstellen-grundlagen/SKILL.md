---
name: susa-erstellen-grundlagen
description: "Summen- und Saldenliste SuSa erstellen Grundlagen. Anwendungsfall monatliche Erstellung aus Finanzbuchhaltung Hauptbuchkonten Personenkonten Erfolgskonten Bestandsbuchungen. Methodik Aufbau Prüfung Verwendung. Output SuSa-Datei als Excel oder PDF mit Sollsalden Habensalden."
---

# Summen- und Saldenliste — Erstellung und Grundlagen

## Fachlicher Anker

- **Normen:** § 6a, § 238 HGB, § 239 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Summen- und Saldenliste (SuSa) ist die periodengerecht aufbereitete Auflistung aller Sachkonten mit Soll- und Habensummen sowie Saldo. Sie ist die unmittelbare Grundlage der BWA, der USt-Voranmeldung und des Jahresabschlusses. Der Steuerberater stellt sie monatlich aus der Finanzbuchhaltung her und nutzt sie für Buchungspruefung, Salden-Konsistenz und steuerliche Auswertungen.

## Kaltstart-Rueckfragen

1. Welche Periode — Monat, Quartal, kumuliert seit Jahresbeginn?
2. Welcher Kontenrahmen — SKR 03, SKR 04, individuell?
3. Welche Detailtiefe — Hauptbuchkonten allein oder mit Personenkonten?
4. Welche Filter — Konten ohne Saldo ausblenden, nur bestimmte Klassen?
5. Welche Vergleichsspalten — Vormonat, kumuliert, Vorjahr?
6. Welche Ausgabeform — Bildschirm, PDF, Excel-Export?
7. Wird die SuSa intern oder extern verwendet (Prüfer, Bank)?
8. Welche Sondereffekte sind zu kennzeichnen?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 239 HGB** — Form und Inhalt der Buchfuehrung; vollstaendige Erfassung.

**§ 146 AO** — Zeitgerechtigkeit der Buchungen; Vollstaendigkeit.

**§ 257 HGB / § 147 AO** — Aufbewahrungsfristen 10 Jahre.

**§ 33 StBerG** — StB-Aufgabenkreis (Buchfuehrungshilfe).

### Standards

- BMF v. 28.11.2019 zu GoBD (BStBl I 2019, 1269).
- DATEV/Addison/Sage Standardformate.
- IDW PS 480.

## Workflow

### Phase 1 — Datenbasis sichern

- Vollstaendigkeit der Buchungen: Bank, Kasse, Eingangs- und Ausgangsrechnungen, Lohnbuchung.
- Periodenabgrenzung (RAP) durchgefuehrt.
- Verrechnungskonten 1590/1599 (SKR 03) bzw. entsprechende SKR-04-Konten geklaert.
- USt-Voranmeldungs-Buchungen integriert.

### Phase 2 — SuSa-Aufbau

Aufbau-Beispiel (Kontennummern beispielhaft im SKR 03; im konkreten Mandat mit aktueller DATEV-Kontenrahmenfassung abgleichen — SKR 04 nutzt eine andere Nummernlogik):

```
SUMMEN- UND SALDENLISTE
Mandant: [Firma]
Periode: [Monat / Quartal / YTD]

Konto Bezeichnung Soll-Summe Haben-Summe Saldo Soll Saldo Haben
0440 GWG [X] [X] [X] [X]
0670 Bauten/Grundstuecke [X] [X] [X] [X]
...
1000 Kasse [X] [X] [X] [X]
1200 Bank [X] [X] [X] [X]
1400 Forderungen LuL [X] [X] [X] [X]
1576 Vorsteuer 19 Prozent [X] [X] [X] [X]
1700 Verb. LuL [X] [X] [X] [X]
1776 USt 19 Prozent [X] [X] [X] [X]
2000 Eroeffnungsbilanz [X] [X] [X] [X]
...
3400 Wareneingang 19 Pr. [X] [X] [X] [X]
4120 Loehne [X] [X] [X] [X]
8400 Erloese 19 Prozent [X] [X] [X] [X]
...
```

### Phase 3 — Filter und Strukturierung

- Konten ohne Saldo ausblenden (Default in DATEV).
- Reihenfolge nach Kontonummer (Bilanzgliederung implizit).
- Separate Ausweisung Bestandskonten (Klassen 0-2 SKR 03; Klassen 0-3 SKR 04) und Erfolgskonten (Klassen 4-8 SKR 03; Klassen 4-7 SKR 04).
- Personenkonten nur auf Wunsch (separate OPOS-Liste).

### Phase 4 — Plausibilitaetspruefung

- Summe Soll = Summe Haben (Prüfsumme; doppelte Buchfuehrung).
- USt-Saldo plausibel mit USt-Voranmeldung.
- Verrechnungskonten auf null.
- Erfolgskonten-Saldo = Jahresergebnis-Roh (vor Periodenabgrenzung).

### Phase 5 — Sondereffekte und Hinweise

- Bei Buchungsfehlern: Korrektur vor SuSa-Versand.
- Schaetzungen klar gekennzeichnet (Bestand, Rueckstellungen).
- Bei Vorperiodenkorrekturen: Hinweis im Begleitschreiben.

### Phase 6 — Versand und Archivierung

- SuSa als PDF mit Mandantenkopf.
- Excel-Export für Sachbearbeiter (optional).
- Archivierung GoBD-konform 10 Jahre.
- Versand an Mandant über DATEV Unternehmen Online oder verschluesseltes Portal.

## Strategie und Praxis-Tipps

- SuSa ist NICHT direkt für den Mandanten — meist interne Auswertung; bei externem Bedarf BWA bevorzugen.
- Externer Prüfer (Wirtschaftspruefer, Aussenprueferin Finanzamt) bekommt SuSa direkt.
- Prüfsumme Soll = Haben ist Grundpruefung; Abweichung = Fehler im System (selten, aber kommt vor).
- Bei Mandanten mit grossem Belegvolumen: SuSa kann mehrere Hundert Konten umfassen — Filter und Sortierung wichtig.
- StBVV: SuSa-Erstellung pauschaliert in der Buchfuehrungspauschale.
- DATEV-Tipp: SuSa per "Sachkontenauswertung" mit Filter "nur saldierte Konten" anfordern.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239, 257.
- AO §§ 146, 147.
- StBerG § 33.
- BMF v. 28.11.2019, BStBl I 2019, 1269.
- IDW PS 480.

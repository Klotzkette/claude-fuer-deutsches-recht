---
name: stb-pruefliste-belegabgabe-monatlich
description: "Pruefliste monatliche Belegabgabe. Anwendungsfall standardisierte Belegabgabe-Kontrolle Mandant Vollstaendigkeit Bankauszuege Kasse Eingangsrechnungen Ausgangsrechnungen Lohnauswertung. Methodik Pruefliste Eingangskontrolle Mahnung. Output Pruefprotokoll Belegmahnung."
---

# Pruefliste monatliche Belegabgabe

## Kernsachverhalt

Die Belegabgabe-Disziplin des Mandanten ist Erfolgsfaktor der Monatsabschluss-Routine. Fehlt ein Beleg, verzoegert sich die BWA, die USt-VA wird ungenau, der Jahresabschluss bekommt Probleme. Der Steuerberater fuehrt eine Pruefliste, prueft die Vollstaendigkeit eingegangener Belege und mahnt bei Verzoegerungen. Bei wiederholten Verspaetungen Honoraranknuepfung oder Eskalation.

## Kaltstart-Rueckfragen

1. Welche Belegart wird abgegeben (Papier, DUO, scan-zentrum)?
2. Welche Frequenz vereinbart (taeglich, woechentlich, monatlich)?
3. Welche Mandantenbranche und Belegvolumen?
4. Welche Sondervorgaenge in der Periode (Reisekosten, Geschenke)?
5. Welche Frist fuer Belegabgabe?
6. Welche Eskalation bei Verspaetung?
7. Welche Wiederkehrenden Belegart (Mieten, Versicherungen)?
8. Welcher Eskalationsstand?

## Rechtlicher Rahmen

### Primaernormen

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit.

**§ 147 AO** — Aufbewahrung.

**§ 90 AO** — Mitwirkungspflicht Mandant.

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 4 StBVV** — Honorarvereinbarung.

## Workflow

### Phase 1 — Standard-Pruefliste

```
BELEGABGABE-PRUEFLISTE
Mandant: [Firma]
Monat: [Monat]

A. BANK
[ ] Alle Bankauszuege fuer den Monat
[ ] PSD2-Online-Banking-Anbindung funktioniert
[ ] Ueberweisungen mit Verwendungszweck

B. KASSE
[ ] Kassenbuch komplett
[ ] Z-Bons taeglich
[ ] Tageseinnahmen-Aufzeichnung GoBD-konform

C. EINGANGSRECHNUNGEN
[ ] Lieferantenrechnungen alle erfasst
[ ] eRechnungen empfangen
[ ] Beleg-Pruefung (USt-Pflichtangaben)

D. AUSGANGSRECHNUNGEN
[ ] Kundenrechnungen alle erfasst
[ ] eRechnungs-Versand (B2B Pflicht seit 01.01.2025)
[ ] Skonti-Belege

E. LOHN
[ ] Lohnauswertung aus Lohnprogramm
[ ] SV-Beitragsbescheide
[ ] Sondervergueteungen, Boni

F. SONSTIGE
[ ] Reisekosten-Belege
[ ] Bewirtungsbelege
[ ] Geschenk-Belege
[ ] Kfz-Belege
[ ] Versicherungs-Bescheide
[ ] FA-Bescheide

G. SONDERVORGAENGE
[ ] Anlagenkauf/-verkauf
[ ] Darlehensvereinbarungen
[ ] Gesellschaftervereinbarungen

H. STATUS
Belege vollstaendig: [Ja/Nein]
Fehlende Belege: [Liste]
Mahnstand: [keine / 1. / 2. Mahnung]
```

### Phase 2 — Eingangskontrolle

- Mandant uebermittelt Belege.
- Sachbearbeiter laed in DATEV.
- Vollstaendigkeit pruefen (Bank-Cut-off, Lohn-Synchronizitaet).

### Phase 3 — Mahnung bei Verspaetung

- Stufe 1: telefonische Nachfrage.
- Stufe 2: schriftliche Erinnerung (E-Mail).
- Stufe 3: Mandantenakte mit Vermerk; ggf. Honorar-Aufschlag.
- Stufe 4: Mandantenniederlegung (§ 627 BGB) im Extremfall.

### Phase 4 — Belege fuer Wiederkehrende Vorgaenge

- Miet-, Pacht-, Leasing-Vertraege als Stamm.
- Versicherungs-Bescheide jaehrlich.
- Daueraufgaben Strom, Heizung, Wasser.

### Phase 5 — Bei Verlust eines Beleges

- Mandant um Ersatzbeleg bitten.
- Schaetzung (mit Vermerk) als letzte Option.
- Bei wiederholten Verlusten: GoBD-Risiko.

### Phase 6 — Reporting an Mandant

- Bei jedem Monatsabschluss: Pruefprotokoll mit Status.
- Bei wesentlichen Maengeln: Mandantengespraech.

## Output

- Pruefprotokoll Belegabgabe.
- Mahnung bei Verspaetung.
- Mandantenakte aktualisiert.

## Strategie und Praxis-Tipps

- Pruefliste konsequent durchgehen — fehlende Belege sind haeufige Ursache von Buchungsfehlern.
- Bei wiederholten Verzoegerungen: Honorar-Aufschlag (z.B. 25 Prozent Eilzuschlag) abrechnen.
- DATEV-DUO ist Einaffacheb-Hebel — Mandanten zu nutzen ermutigen.
- StBVV: in Pauschal; Eilbearbeitung Sonderhonorar.
- DATEV-Tipp: DATEV DUO Belegfluss-Statistik nutzen.

## Querverweise

- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-mandantenanfrage-reaktion-frist-laufend` — Mandantenanfragen.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 90, 146, 147.
- StBerG § 33.
- StBVV § 4.
- BMF v. 28.11.2019 zu GoBD.

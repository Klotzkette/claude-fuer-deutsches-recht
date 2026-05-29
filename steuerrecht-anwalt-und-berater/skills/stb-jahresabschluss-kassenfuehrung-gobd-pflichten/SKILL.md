---
name: stb-jahresabschluss-kassenfuehrung-gobd-pflichten
description: "Kassenführung GoBD-Pflichten. Anwendungsfall Mandanten mit Bargeschäft Kasse Aufzeichnungspflichten Kassenbuch elektronische Aufzeichnungssysteme TSE technische Sicherheitseinrichtung. Methodik Prüfung Sorgfalt. Output GoBD-konforme Kassenführung."
---

# Kassenfuehrung — GoBD-Pflichten

## Kernsachverhalt

Bei Mandanten mit Bargeschaeft (Gastronomie, Einzelhandel) ist die Kassenfuehrung ein sensibler Pruefpunkt. § 146 AO verlangt Zeitgerechtigkeit und Vollstaendigkeit; § 146a AO erfordert seit 01.01.2020 (BMF-Nichtbeanstandungsregelung bis 30.09.2020) eine zertifizierte Technische Sicherheitseinrichtung (TSE) bei elektronischen Aufzeichnungssystemen. Seit 01.01.2020 besteht zudem die Belegausgabepflicht nach § 146a Abs. 2 AO. Verstoesse koennen zur Schaetzungsbefugnis (§ 162 AO), Bussgeld (§ 379 AO) bzw. zu steuerstrafrechtlicher Bewertung als Steuerhinterziehung fuehren.

## Kaltstart-Rueckfragen

1. Welche Kassenart — offene Ladenkasse, elektronische Kasse, mobile Kasse?
2. TSE eingebaut?
3. Welches Kassensystem (Hersteller, Modell)?
4. Wer fuehrt Kassenbuch (Mandant, StB)?
5. Welche Sondersituation (Trinkgeld, Wechselgeld, Skontoabzug)?
6. Welche Pruefungen Vergangenheit (Kassenpruefung, Aussenpruefung)?
7. Welche Belegpflicht-Vorgaben?
8. Welche taegliche Z-Bon-Routine?

## Rechtlicher Rahmen

### Primaernormen

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit.

**§ 146a AO** — Aufzeichnungspflicht elektronische Aufzeichnungssysteme; TSE.

**§ 146b AO** — Belegausgabepflicht.

**§ 379 AO** — Bussgeld bei Verstoss.

**§ 162 AO** — Schaetzung bei Maengeln.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 zu GoBD.
- BMF v. 17.06.2019 zu § 146a AO (TSE).
- BMF v. 11.06.2020 zur Kassennachschau § 146b AO.

## Workflow

### Phase 1 — Kassensystem pruefen

| System | TSE-Pflicht | Anforderungen |
|---|---|---|
| Offene Ladenkasse (Geldkasten) | Keine TSE; aber tagliche Aufzeichnung in Kassenbericht | Manuelle Kassenfuehrung |
| Elektronische Kasse / Registrierkasse | TSE seit 01.01.2020 | Zertifizierte TSE eingebaut |
| Cloud-Kassensystem | TSE | Auch Cloud-Loesungen brauchen TSE |
| App-Kasse | TSE | Bei elektronischer Speicherung |

### Phase 2 — TSE-Pruefung

- TSE-Modul muss zertifiziert sein (BSI).
- TSE-Daten werden mit jeder Buchung erstellt (Signatur, Zeitstempel).
- Speicherung 10 Jahre.

### Phase 3 — Tagliche Routine

- Z-Bon (Tagesabschluss): am Tagesende ausdrucken.
- Kassensturz: Soll-Bestand vs. Ist-Bestand.
- Differenzen klaeren.
- Kassenbericht oder elektronisch.

### Phase 4 — Belegpflicht § 146b AO

- Seit 01.01.2020: jeder Verkauf Beleg.
- Beleg kann Papier oder elektronisch sein.
- Verstoss: § 379 AO Bussgeld.

### Phase 5 — Bei Pruefung

- Kassennachschau § 146b AO: unangemeldet moeglich.
- Aussenpruefer: Kassenfuehrung vorlegen.
- Bei wesentlichen Maengeln: Schaetzung § 162 AO.

### Phase 6 — Verfahrensdokumentation

- Verfahrensdokumentation des Kassensystems (Pflicht).
- Bedienungsanleitung TSE.
- Beleg-Archivierung GoBD-konform 10 Jahre.

## Output

- GoBD-konforme Kassenfuehrung.
- Verfahrensdokumentation.
- Belegarchiv.

## Strategie und Praxis-Tipps

- Die TSE-Pflicht ist hart durchgesetzt; der Bussgeldrahmen reicht nach § 379 Abs. 6 AO bis 25.000 EUR pro Verstoss.
- Die Verfahrensdokumentation (Konfiguration, Bedienungsanleitung, Aenderungsprotokoll) ist haeufig vernachlaessigt, aber ausdruecklich Pflichtbestandteil nach GoBD (BMF v. 28.11.2019, Rz. 153 ff.).
- Bei Mandanten mit hohem Bargeschaeft ist eine kontinuierliche StB-Begleitung sinnvoll; bei Verdacht auf Manipulation der Aufzeichnungen ist der Mandant nachweisbar (Aktenvermerk, schriftliche Belehrung) auf die Sanktionsrisiken nach § 379 AO bzw. § 370 AO hinzuweisen — vgl. die Eskalations-Routine in `stb-mandantenanfrage-reaktion-frist-laufend` und die berufsrechtliche Hinweispflicht aus § 102 StaRUG bei drohender Insolvenz.
- Die Kassennachschau nach § 146b AO erfolgt unangekuendigt — auch zu Beginn der Geschaeftsoeffnung; Mandanten sollten auf den Umgang mit dem Pruefer (Vorlage Kassen-Z-Bons, TSE-DSFinV-K-Daten) geschult werden.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-fehlerquellen-haeufig` — Fehlerquellen.
- `stb-susa-erstellen-grundlagen` — SuSa.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 146a, 146b, 162, 379.
- BMF v. 28.11.2019 zu GoBD.
- BMF v. 17.06.2019 (TSE).
- BMF v. 11.06.2020 (Kassennachschau).

---
name: mandat-triage-bank-kapitalmarktrecht
description: Strukturierte Eingangs-Abfrage fuer bank- und kapitalmarktrechtliche Mandate. Klaert Sachgebiet (Anlageberatungsfehler Kapitalmarktinformationshaftung Prospekthaftung Kreditfinanzierung Verbraucherkredit Bauerfinanzierung Bank-AGB Konto-Sperre Kontopfaendung Bankenrettung BaFin-Aufsicht Geldwaesche § 261 StGB AGB-Banken-Kunde Sparbuch Schwarzgeld) Mandantenrolle (Anleger Kreditnehmer Verbraucher Bank Vorstand Compliance Beauftragter) Sofort-Fristen-Check Verjaehrung drei Jahre § 195 BGB Hoechstfrist zehn Jahre § 199 Abs. 3 BGB. Eskalation Telefon-Sofort bei Kontosperrung BaFin-Anordnung. Routing zu anlageberatungsfehler-pruefen.
---

# Mandat-Triage Bank- und Kapitalmarktrecht

## Zweck

Bank- und Kapitalmarktrecht ist heterogen — Anlegerschaden Konsumentenkredit Sicherheiten Insolvenz Aufsichtsrecht. Triage stellt richtige Spur.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Anleger / Sparer
- Kreditnehmer (Verbraucher / Unternehmer)
- Sicherheitengeber (Bürge Grundschuldgeber)
- Bank / Sparkasse
- Vorstand / Geschäftsleiter Bank
- Compliance Geldwäschebeauftragter
- Aufsicht (BaFin)

### Frage 2 — Sachgebiet?

- Anlageberatungsfehler
- Kapitalmarktinformationshaftung (Falschangaben Ad-hoc)
- Prospekthaftung
- Verbraucherkredit Widerruf § 495 ff. BGB Widerrufsjoker
- Immobilienfinanzierungs-Beratung
- Bank-AGB Kontoführung Kontosperre
- Kontopfändung Pfändungsschutz P-Konto §§ 850k 899 ff. ZPO (Pfändungsschutzkonto seit PKoFoG 01.12.2021 in §§ 899-910 ZPO)
- Kreditsicherheiten Grundschuld Bürgschaft Sicherungsabtretung
- Geldwäsche § 261 StGB AMLA
- BaFin-Aufsicht Sanktionen
- Banken-Restrukturierung / Sanierungsmaßnahmen
- Crypto-Asset MiCAR

### Frage 3 — Akute Eilbedürftigkeit?

- Kontosperre (Geldwäsche-Verdacht oder AGB-Kündigung)
- Kreditkündigung — Verwertung droht
- BaFin-Anordnung sofortige Vollziehung
- Vorlaeufige Untersagung Geschäftsbetrieb
- Pfändung-Konto wirtschaftliche Existenz
- Klage-Fristablauf Hauptsachefrist nach Schiedsspruch

### Frage 4 — Stand?

- Beratung vor Vertragsschluss
- Vertrag läuft Streit ueber Leistung
- Außergerichtlicher Schriftwechsel
- Ombudsstelle der Banken läuft (Hemmung Verjährung)
- Klage erhoben
- BaFin-Verfahren
- Strafverfahren Geldwäsche

### Frage 5 — Produktart bei Anlageberatung?

- Aktie Fonds (offen geschlossen)
- Anleihe Zertifikat strukturiertes Produkt
- Schiffsfonds Immobilienfonds Filmfonds
- Lebensversicherung als Anlage
- Swap-Geschäfte
- Crypto-Asset

### Frage 6 — Vertragsbasis?

- Beratungsvertrag konkludent
- Vermögensverwaltungs-Vertrag
- Bank-AGB der konkreten Bank
- Prospekt
- WpHG-Bestätigungen

### Frage 7 — Frist?

- **Verjährung Anlageberatung** drei Jahre Kenntnis / zehn Jahre Beratung § 195 199 BGB
- **Widerrufsjoker** Verbraucherkredit Immobiliendarlehen-Widerruf — Bei fehlerhafter Belehrung verlängerter Widerruf
- **Ombudsstelle** Hemmung Verjährung
- **Strafverfahren Geldwäsche** Verjährung je nach Strafmaß

### Frage 8 — Wirtschaftliche Verhältnisse?

- Hohes Anlagevolumen (Schadenshöhe)
- Berufshaftpflicht Anlageberater
- Versicherer für Bank?
- Rechtsschutz Anleger?

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Anlageberatungsfehler | `anlageberatungsfehler-pruefen` |
| Prospekthaftung | `anlageberatungsfehler-pruefen` plus Prospektfokus |
| Verbraucherkredit Widerruf | (Skill verbraucherkredit-widerruf — perspektivisch) |
| Immobilienkredit | (Skill immobilienkredit-pruefen — perspektivisch) |
| Bank-AGB-Klauselstreit | (Skill agb-banken-pruefen — perspektivisch) |
| Kontosperre | (Skill kontosperre-pruefen — perspektivisch) |
| Geldwäsche-Strafverfahren | weiter an `mandat-triage-strafrecht` plus Spezial |
| BaFin-Aufsichtsverfahren | weiter an `mandat-triage-verwaltungsrecht` |
| Pfändung P-Konto | weiter an `forderungsmanagement-klagewerkstatt` |
| Crypto / MiCAR | (Skill micar-compliance — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Bank/Kunde
- **Streitwert** Anlageverlust voll oder Differenzhypothese
- **Sachverständigen-Bedarf** Wertentwicklung Marktwert
- **Versicherungs-Deckung** Anleger-Rechtsschutz

## Eskalation

- **Telefon-Sofort** Kontosperre BaFin Hausdurchsuchung Bank-Mitarbeiter
- **Binnen einer Stunde** Widerrufs-Schreiben bei Fristablauf
- **Heute** Ombudsstellen-Antrag Verzugsschreiben
- **Diese Woche** Klage-Erstentwurf Schadensberechnung

## Ausgabe

- `triage-protokoll-bank-kapital.md`
- Aktenanlage
- Frist im Fristenbuch
- Ombudsstellen-Antrag oder Klage-Empfehlung
- Mandatsvereinbarung
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 195 199 280 311 488 ff. 495 ff. 765 ff.
- WpHG MiFID-II
- VermAnlG WpPG
- StGB § 261
- KWG
- ZPO §§ 850k 899-910 (PKoFoG)
- BGH XI. Zivilsenat — Bond Lehman Ille Kickback

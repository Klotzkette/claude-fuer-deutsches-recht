---
name: mandat-triage-bank-kapitalmarktrecht
description: "Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-Fristen. Verjährung §§ 195 199 Abs. 3 BGB 3 Jahre / 10 Jahre. Normen je nach Routing. Prüfraster Sachgebiets-Zuordnung Fristen-Sofort-Check Eskalation Kontosperrung BaFin-Anordnung. Output Mandat-Karte Routing-Empfehlung Handlungsweichen. Abgrenzung zu erstgespraech-mandatsannahme (Vollaufnahme) und fachanwalt-bank-kapitalmarktrecht-orientierung (Überblick)."
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
- Vorläufige Untersagung Geschäftsbetrieb
- Pfändung-Konto wirtschaftliche Existenz
- Klage-Fristablauf Hauptsachefrist nach Schiedsspruch

### Frage 4 — Stand?

- Beratung vor Vertragsschluss
- Vertrag läuft Streit über Leistung
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
| Immobilienkredit | (Skill immobilienkredit-prüfen — perspektivisch) |
| Bank-AGB-Klauselstreit | (Skill agb-banken-pruefen — perspektivisch) |
| Kontosperre | (Skill kontosperre-prüfen — perspektivisch) |
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

## Vertiefung: Rechtsprechung und erweiterte Triage

### Schluessel-Leitsaetze fuer Triage Bank-/Kapitalmarktrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Erweiterte Triage-Matrix

| Konstellation | Sofortmassnahme | Folge-Skill |
|---|---|---|
| Widerruf Immobiliendarlehen, Frist laeuft | SOFORT Widerruf erklaeren | `widerrufsjoker-immobiliendarlehen` |
| Anlageberatung, Verjaebrung naht | Ombudsmann SOFORT (hemmt Verjaebrung) | `anlageberatungsfehler-pruefen` |
| Kreditkuendigung ohne § 498-Voraussetzungen | Widerspruch + Feststellungsklage | `fachanwalt-bank-kapitalmarktrecht-kreditkuendigung` |
| SCHUFA-Eintrag rechtswidrig | Loeschungsverlangen Art. 17 DSGVO | `fachanwalt-bank-kapitalmarktrecht-schufa-eintrag` |
| Cybertrading-Betrug, < 8 Wochen | SEPA-Recall SOFORT | `fachanwalt-bank-kapitalmarktrecht-cybertrading-anlagebetrug` |
| MiCA-Stablecoin BaFin-Lizenz | Whitepaper + Antrag vorbereiten | `fachanwalt-bank-kapitalmarktrecht-mica-stablecoin-art-16-bafin` |
| Negativzins-Klausel AGB | AGB-Kontrolle § 307 BGB + Rueckforderung | `anlageberatungsfehler-pruefen` |

### Entscheidungsbaum Verjaebrung

Ist die Verjaebrungsfrist bekannt?
→ NEIN: Datum der Beratung/Schaden + 3 Jahre = § 195 BGB; aber max. 10 Jahre ab Entstehung § 199 Abs. 3 BGB
→ JA und < 6 Monate: Ombudsmann-Antrag zur Hemmung SOFORT; parallel Klageschrift vorbereiten
→ JA und > 10 Jahre: Verjaebrung eingetreten; Sonderfall Arglist § 199 Abs. 3 Nr. 2 BGB pruefen

### Output-Template Triage-Protokoll
**Adressat:** Intern — Tonfall: schnell, strukturiert

```
TRIAGE-PROTOKOLL Bank-/Kapitalmarktrecht
=========================================
Eingangsdatum:       [TT.MM.JJJJ]
Mandant:             [NAME]
Sachgebiet:          [Anlageberatung / Verbraucherkredit / Kreditkuendigung ...]
Sofortfrist:         [DATUM + RECHTSGRUNDLAGE]
Verjaebrung:         [3 Jahre ab XX.XX.XXXX]
Streitwert:          EUR [BETRAG]
Prioritaet:          [ROT / GELB / GRUEN]
Folge-Skill:         [SKILL-NAME]
Naechster Schritt:   [MASSNAHME] bis [DATUM] durch [PERSON]
=========================================
```

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

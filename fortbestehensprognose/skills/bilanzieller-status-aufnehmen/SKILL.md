---
name: bilanzieller-status-aufnehmen
description: Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Pruefraster bilanzielle Ueberschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und ausserbilanzielle Verpflichtungen (Pensionsrueckstellungen Buergschaften Comfortletter). Erzeugt Insolvenzstatus als Vorstufe zur Fortbestehensprognose. Wichtig — bilanzielle Ueberschuldung ist nicht automatisch insolvenzrechtliche Ueberschuldung (§ 19 Abs. 2 InsO Fortbestehensprognose).
---

# Bilanzieller Status aufnehmen

## Zweck

Der **bilanzielle** Überschuldungsstatus ist die Voraussetzung um in die Prüfung der **insolvenzrechtlichen** Überschuldung nach § 19 Abs. 2 InsO einzusteigen. Beide Schritte sind zu trennen:

1. **Bilanzieller Überschuldungsstatus** (Stichtagsbetrachtung). Aktiva kleiner als Passiva?
2. **Insolvenzrechtliche Überschuldung** (§ 19 InsO). Nur wenn bilanzielle Überschuldung vorliegt UND keine positive Fortbestehensprognose.

## Stichtagsbilanz

```yaml
stichtag: 2026-05-20  # oder Bilanzstichtag des letzten Jahresabschlusses
bilanzansatz: hgb  # hgb / ifrs / mischung

aktiva:
  a-anlagevermoegen:
    immaterielle: 50000
    sachanlagen: 320000
    finanzanlagen: 0
  b-umlaufvermoegen:
    vorraete: 180000
    forderungen-laul: 120000
    sonstige-forderungen: 15000
    fluessige-mittel: 18000
  c-rechnungsabgrenzung: 5000
  aktiva-summe: 708000

passiva:
  a-eigenkapital:
    gezeichnetes-kapital: 25000
    kapitalruecklage: 0
    gewinnruecklagen: 0
    bilanzergebnis: -107000  # negativ
    eigenkapital-summe: -82000  # negativ
  b-rueckstellungen:
    pensionen: 0
    sonstige: 22000
  c-verbindlichkeiten:
    banken: 250000
    lieferanten: 410000
    sonstige: 38000
    steuern: 25000
    sozialversicherung: 45000
  d-rechnungsabgrenzung: 0
  passiva-summe: 708000

bilanzielle-ueberschuldung: ja  # Aktiva = Passiva aber EK negativ = bilanzielle Überschuldung
hoehe-bilanzielle-ueberschuldung: 82000
```

## Stille Reserven

Vermögenswerte deren Buchwert geringer ist als der Verkehrswert. Im Status zu addieren (heben die bilanzielle Überschuldung).

```yaml
stille-reserven:
  - position: CNC-Anlage
    buchwert: 95000
    verkehrswert: 180000
    stille-reserve: 85000
  - position: Betriebsgrundstueck
    buchwert: 120000
    verkehrswert: 210000
    stille-reserve: 90000
summe-stille-reserven: 175000
```

## Stille Lasten

Verpflichtungen die in der Handelsbilanz nicht oder zu niedrig passiviert sind. Im Status zu addieren (verschärfen die bilanzielle Überschuldung).

```yaml
stille-lasten:
  - position: Drohende Inanspruchnahme aus Bürgschaft
    bilanziell: 0
    insolvenzrechtlich: 50000
  - position: Pensionsrückstellung Erfüllungsbetrag versus Bilanzwert
    bilanziell: 0
    insolvenzrechtlich: 30000
summe-stille-lasten: 80000
```

## Bereits qualifizierter Rangrücktritt

Forderungen mit qualifiziertem Rangrücktritt (§ 19 Abs. 2 S. 2 InsO) werden im Überschuldungsstatus **nicht passiviert**.

```yaml
qualifizierter-rangruecktritt:
  - glaeubiger: Hauptgesellschafter Karl Mueller
    forderung: Gesellschafterdarlehen vom 15.03.2024
    nennbetrag: 120000
    rangruecktritt-erklaert-am: 2026-05-22
    rangruecktritt-form: notarielle Urkunde  # idealtypisch
    bgh-konform: ja  # siehe Skill gesellschafterdarlehen-rangrücktritt
```

## Insolvenzrechtlicher Überschuldungsstatus

```
Aktiva (Handelsbilanz)          708.000 EUR
+ stille Reserven               175.000 EUR
- stille Lasten                 -80.000 EUR
= Insolvenzrechtliche Aktiva    803.000 EUR

Passiva (Handelsbilanz)         790.000 EUR  (Aktiva minus EK)
- qualifizierter Rangrücktritt -120.000 EUR
= Insolvenzrechtliche Passiva   670.000 EUR

Differenz                       133.000 EUR positiv
```

Ergebnis: trotz **bilanzieller Überschuldung von 82.000 EUR** ist die **insolvenzrechtliche Bilanzbasis positiv** weil stille Reserven und Rangrücktritt dies neutralisieren. Reine Vermögensbilanz **ist nicht ausreichend** — die Fortbestehensprognose ist zusätzlich erforderlich (Skill `annahmen-sammeln-fortfuehrung`).

## Wichtige Hinweise

- Bei **Personengesellschaften ohne natürlich-personige Vollhafter** (z. B. GmbH und Co. KG mit ausschließlich Komplementär-GmbH) gilt § 19 InsO entsprechend.
- Bei **Einzelkaufmann** oder Personengesellschaft mit natürlich-personiger Vollhafter ist § 19 InsO **nicht anwendbar** — Insolvenzantragspflicht ergibt sich nur aus Zahlungsunfähigkeit § 17 InsO.
- Die Erstellung des Status ist **Geschäftsleiter-Pflicht**. Bei Buchführungsmängeln (kein aktueller Stand kein Status möglich) kommt **Bankrott** § 283b StGB in Betracht.

## Rechtsprechung

- BGH, Urt. v. 13.07.2017 — IX ZR 290/14, NJW 2017, 3373: Insolvenzrechtliche Überschuldung Anwendung des § 19 InsO neu (seit MoMiG 2008).
- BGH, Urt. v. 18.10.2010 — II ZR 151/09, NZG 2010, 1393: Überschuldungsprognose.

## Ausgabe

- `bilanzieller-status.yaml` mit Stichtag Bilanzwerten stillen Reserven Lasten Rangrücktritt und insolvenzrechtlicher Bilanzbasis.
- Erste Ergebnisaussage (insolvenzrechtliche Bilanzbasis positiv / negativ).
- Empfehlung: bei negativer Bilanzbasis ohne Aussicht auf Fortbestehensprognose **sofort** Insolvenzanwalt — § 15a InsO Sechs-Wochen-Frist beginnt zu laufen.

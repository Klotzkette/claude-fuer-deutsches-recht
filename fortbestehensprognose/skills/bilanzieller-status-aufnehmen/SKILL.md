---
name: bilanzieller-status-aufnehmen
description: "Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle Verpflichtungen (Pensionsrückstellungen Buergschaften Comfortletter). Erzeugt Insolvenzstatus als Vorstufe zur Fortbestehensprognose. Wichtig — bilanzielle Überschuldung ist nicht automatisch insolvenzrechtliche Überschuldung (§ 19 Abs. 2 InsO Fortbestehensprognose) im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Bilanzieller Status aufnehmen

## Arbeitsbereich

Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle Verpflichtungen (Pensionsrückstellungen Buergschaften Comfortletter). Erzeugt Insolvenzstatus als Vorstufe zur Fortbestehensprognose. Wichtig — bilanzielle Überschuldung ist nicht automatisch insolvenzrechtliche Überschuldung (§ 19 Abs. 2 InsO Fortbestehensprognose). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Der **bilanzielle** Überschuldungsstatus ist die Voraussetzung um in die Prüfung der **insolvenzrechtlichen** Überschuldung nach § 19 Abs. 2 InsO einzusteigen. Beide Schritte sind zu trennen:

1. **Bilanzieller Überschuldungsstatus** (Stichtagsbetrachtung). Aktiva kleiner als Passiva?
2. **Insolvenzrechtliche Überschuldung** (§ 19 InsO). Nur wenn bilanzielle Überschuldung vorliegt UND keine positive Fortbestehensprognose.

## Stichtagsbilanz

```yaml
stichtag: 2026-05-20 # oder Bilanzstichtag des letzten Jahresabschlusses
bilanzansatz: hgb # hgb / ifrs / mischung

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
 bilanzergebnis: -107000 # negativ
 eigenkapital-summe: -82000 # negativ
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

bilanzielle-ueberschuldung: ja # Aktiva = Passiva aber EK negativ = bilanzielle Überschuldung
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
 rangruecktritt-form: notarielle Urkunde # idealtypisch
 bgh-konform: ja # siehe Skill gesellschafterdarlehen-rangrücktritt
```

## Insolvenzrechtlicher Überschuldungsstatus

```
Aktiva (Handelsbilanz) 708.000 EUR
+ stille Reserven 175.000 EUR
- stille Lasten -80.000 EUR
= Insolvenzrechtliche Aktiva 803.000 EUR

Passiva (Handelsbilanz) 790.000 EUR (Aktiva minus EK)
- qualifizierter Rangrücktritt -120.000 EUR
= Insolvenzrechtliche Passiva 670.000 EUR

Differenz 133.000 EUR positiv
```

Ergebnis: trotz **bilanzieller Überschuldung von 82.000 EUR** ist die **insolvenzrechtliche Bilanzbasis positiv** weil stille Reserven und Rangrücktritt dies neutralisieren. Reine Vermögensbilanz **ist nicht ausreichend** — die Fortbestehensprognose ist zusätzlich erforderlich (Skill `annahmen-sammeln-fortfuehrung`).

## Wichtige Hinweise

- Bei **Personengesellschaften ohne natürlich-personige Vollhafter** (z. B. GmbH und Co. KG mit ausschließlich Komplementär-GmbH) gilt § 19 InsO entsprechend.
- Bei **Einzelkaufmann** oder Personengesellschaft mit natürlich-personiger Vollhafter ist § 19 InsO **nicht anwendbar** — Insolvenzantragspflicht ergibt sich nur aus Zahlungsunfähigkeit § 17 InsO.
- Die Erstellung des Status ist **Geschäftsleiter-Pflicht**. Bei Buchführungsmängeln (kein aktueller Stand kein Status möglich) kommt **Bankrott** § 283b StGB in Betracht.

## Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

- `bilanzieller-status.yaml` mit Stichtag Bilanzwerten stillen Reserven Lasten Rangrücktritt und insolvenzrechtlicher Bilanzbasis.
- Erste Ergebnisaussage (insolvenzrechtliche Bilanzbasis positiv / negativ).
- Empfehlung: bei negativer Bilanzbasis ohne Aussicht auf Fortbestehensprognose **sofort** Insolvenzanwalt — § 15a InsO Sechs-Wochen-Frist beginnt zu laufen.

## Aktuelle Leitentscheidungen — Bilanzieller Status

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bilanzieller Status

§ 19 Abs. 2 InsO (Ueberschuldungsbegriff) → § 19 Abs. 2 S. 2 InsO (qualifizierter Rangruecktritt) → § 35 Abs. 1 InsO (Massebegriff stille Reserven) → HGB §§ 252-255 (Bewertungsgrundsaetze) → IDW S 11 Rn. 20-42 (Status-Ermittlung)

## Triage — Bilanzieller Status

1. **Stichtag festlegen:** Welches Datum hat der Status? (aktuellstes Datum mit verlaesslichen Daten)
2. **Stille Reserven identifizieren:** Grundstuecke zum Buchwert vs. Verkehrswert; Forderungen vs. Marktpreis; Beteiligungen.
3. **Ausserbilanzielle Verpflichtungen:** Pensionen, Buergschaften, noch nicht ausgewiesene Verluste aus schwebenden Geschaeften.
4. **Sanierungsmassnahmen einbeziehen?** Gesellschafterdarlehen mit Rangruecktritt, Patronatserklaerung, Kapitalzufuhr — bereits vorhanden oder noch planerisch?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

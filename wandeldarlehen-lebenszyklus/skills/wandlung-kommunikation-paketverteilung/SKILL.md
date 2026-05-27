---
name: wandlung-kommunikation-paketverteilung
description: "Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Pruefraster: Empfaengerliste Dokumente Zugang Fristen Bestaetigung. Output: Kommunikationsplan Versandprotokoll. Abgrenzung: nicht fuer inhaltliche Pruefung der Wandlung (wandelereignis-eingang)."
---

# Wandlung – Kommunikation und Paketverteilung

## Zweck

Dieser Skill koordiniert alle Kommunikationsmaßnahmen nach der Wandlungsentscheidung: Bestätigungsschreiben, Mitwirkungsaufforderungen und Buchungsanweisungen an alle beteiligten Stellen. Phase C des Lebenszyklus.

## Eingaben

- Bestätigte Wandlungsberechnung (aus `wandlungspreis-berechnung`)
- Adressen aller Parteien (Lender, Gesellschaft, Gesellschafterinnen, Steuerberater, Buchhaltung)
- Datum der Wandlungserklärung und der Bestätigung
- Cap-Table Post-Money (aus `cap-table-update-pre-post`)
- Buchungsanweisungen: Ausbuchung Verbindlichkeit (Darlehensbetrag + Zinsen), Einbuchung Eigenkapital

## Rechtlicher Rahmen

### Primärnormen
- § 4.9 Wandeldarlehensvertrag (Gesellschaft beruft unverzüglich Gesellschafterversammlung ein)
- § 5 Wandeldarlehensvertrag (Mitwirkungspflichten Gesellschafterinnen)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage nach Einlage der Forderung)
- § 246 HGB (Vollständigkeit der Buchführung)
- § 8 Wandeldarlehensvertrag (Vertraulichkeit – an wen darf kommuniziert werden?)

### Rechtsprechung
- BGH, Urt. v. 29. April 2002 – II ZR 330/00 (Mitwirkungspflicht Gesellschafterinnen bei Kapitalerhöhung)

## Vorgehen

### 1. Bestätigungsschreiben an Lender
Inhalt: Bestätigung der Wandlungserklärung, Wandlungssumme (Darlehen + Zinsen), berechnete neue Anteile (Zahl, Nennwert), vorgesehener Termin Kapitalerhöhungsbeschluss, vorgesehener Notar.

### 2. Aufforderungsschreiben an Gesellschaft (Geschäftsführerin)
Inhalt: Einberufungspflicht gemäß § 4.9, Frist (unverzüglich, spätestens innerhalb zwei Wochen), Tagesordnungspunkte (Kapitalerhöhung gegen Sacheinlage, Bezugsrechtsverzicht, Aufnahme Lender), Notar-Beauftragung.

### 3. Schreiben an Gesellschafterinnen (Mitwirkungspflicht)
Inhalt: Hinweis auf § 5 des Wandeldarlehensvertrags (Mitwirkungspflicht), Einladung zur Gesellschafterversammlung, Beschlussthemen, Bitte um Anwesenheitsbestätigung oder Vollmacht.

### 4. Mitteilung an Steuerberater
Inhalt: Wandlungsdaten (Betrag, Datum, neue Gesellschafterstruktur), neue Cap-Table als Anlage, Bitte um steuerliche Würdigung (Wandlung als Tausch nach § 20 UmwStG analog?).

### 5. Buchungsanweisung an Buchhaltung
Soll-Buchung: Verbindlichkeit Wandeldarlehen (Darlehen + aufgelaufene Zinsen) auflösen. Haben-Buchung: Stammkapital (Nennbetrag neue Anteile) und Kapitalrücklage (Rest) erhöhen. Buchungssatz: per Verbindlichkeit Wandeldarlehen an Gezeichnetes Kapital und Kapitalrücklage.

### 6. Dokumentation und Archivierung
Alle Schreiben mit Sendenachweis archivieren (Textform-Anforderung). Kommunikationsstatus im Aktenstammblatt vermerken.

## Beispiel-Buchungssatz

```
Buchungstag: [Eintragungsdatum Handelsregister]

Soll:
  Verbindlichkeit Wandeldarlehen Northstar:     EUR 275694

Haben:
  Gezeichnetes Kapital (§ 272 Abs. 1 HGB):     EUR 7
  Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB):    EUR 275687
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Buchhaltung bucht Darlehen erst nach Fälligkeit aus | Bilanzunklarheit | Buchung verzögert | Buchung zeitnah mit Eintragung |
| Steuerberater nicht informiert | Steuerliche Risiken unerkannt | Informiert nach HR-Eintragung | Sofort informiert |
| Gesellschafterinnen nicht eingeladen | Mitwirkungspflicht verletzt | Einladung verspätet | Rechtzeitige Einladung |
| Kommunikation gegen Vertraulichkeitsklausel | § 8-Verstoß | Empfänger nicht § 8-berechtigt | Alle Empfänger § 8 lit. a berechtigt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterversammlung-einberufen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung HGB § 272 oder UmwStG § 20 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 17.07.2012 — **II ZR 244/07**, BGHZ 194, 132 Rn. 18: Kommunikation nach vollzogener Wandlung muss alle relevanten Parteien gleichzeitig und vollständig informieren; asynchrone Information kann als Insiderinformation-Problem qualifiziert werden, wenn das Unternehmen auf Wertpapiermärkten aktiv ist; bei GmbH ist die Gesellschafterliste das maßgebliche öffentliche Instrument.

BGH, Urt. v. 12.03.2007 — **II ZR 256/08** (Wandeldarlehen zweistufige Konstruktion), BGHZ 182, 272 Rn. 28: Alle beteiligten Gesellschafter müssen über die Wandlung informiert werden; ihre Zustimmung zum Bezugsrechtsverzicht muss dokumentiert sein; fehlt die Information oder Zustimmung, können sie den Kapitalerhöhungsbeschluss anfechten.

### Normen-Ergänzung

§ 47 Abs. 4 GmbHG (Stimmverbot eigene Sache) → § 40 GmbHG (Gesellschafterliste nach Wandlung) → § 53 Abs. 1 GmbHG (Zustimmung Gesellschafter zur Satzungsänderung) → § 16 GmbHG (Legitimationswirkung) → §§ 130, 132 BGB (Zugang Erklärungen)

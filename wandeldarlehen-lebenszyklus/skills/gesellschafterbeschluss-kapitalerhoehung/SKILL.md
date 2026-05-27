---
name: gesellschafterbeschluss-kapitalerhoehung
description: "Gesellschafterbeschluss fuer Kapitalerhohung nach Wandlung vorbereiten. §§ 53 55 56 GmbHG Kapitalerhohung. Pruefraster: Beschlussinhalt Mehrheitserfordernisse notarielle Form neues Stammkapital Einlagepflicht Handelsregistereintrag. Output: Beschlussentwurf Ladungsunterlagen. Abgrenzung: nicht fuer allgemeine Gesellschafterversammlung (gesellschafterversammlung-einberufen)."
---

# Gesellschafterbeschluss – Kapitalerhöhung gegen Sacheinlage

## Zweck

Dieser Skill erstellt den notariell beurkundungspflichtigen Gesellschafterbeschluss über die Kapitalerhöhung gegen Sacheinlage (Wandlung des Wandeldarlehens). Phase D des Lebenszyklus.

## Eingaben

- Wandlungsberechnung (neue Anteile, Nennbetrag, Wandlungssumme) aus `wandlungspreis-berechnung`
- Lender (Name, Anschrift, Vertreter)
- Stammkapital vor und nach Kapitalerhöhung
- Sacheinlage: Forderung aus Wandeldarlehen (Betrag gesamt)
- Notar: Name, Amtssitz
- Sacheinlagebericht (Entwurf, aus `sacheinlagebericht-werthaltigkeit`)

## Rechtlicher Rahmen

### Primärnormen
- § 53 Abs. 2 GmbHG (Satzungsänderung durch Gesellschafterbeschluss – drei Viertel-Mehrheit, notarielle Beurkundung)
- § 55 Abs. 1 GmbHG (Kapitalerhöhungsbeschluss – Zulassung neuer Gesellschafter)
- § 55 Abs. 2 GmbHG (Übernahmeerklärung des neuen Gesellschafters – notarielle Beurkundung)
- § 56 GmbHG (Sacheinlage: Leistung vor Anmeldung zum Handelsregister)
- § 56a GmbHG (Sachgründungsbericht / Sacheinlagebericht)
- § 9 GmbHG (Differenzhaftung bei Überbewertung)

### Rechtsprechung
- BGH, Urt. v. 24. Oktober 2005 – II ZR 179/03 (Sacheinlage – Werthaltigkeit und Differenzhaftung)
- BGH, Urt. v. 6. Dezember 2010 – II ZR 14/09 (Einbringung von Forderungen als Sacheinlage – Werthaltigkeitsnachweis)

## Vorgehen

### 1. Beschlussstruktur festlegen
Notarielle Beurkundung (§ 53 Abs. 2 GmbHG) zwingend. Beschlussinhalt: (a) Kapitalerhöhung, (b) Ausschluss Bezugsrecht, (c) Zulassung Lender, (d) Satzungsänderung. Gleichzeitig: Übernahmeerklärung des Lenders (§ 55 Abs. 2 GmbHG) – auch notariell.

### 2. Beschlusstext ausarbeiten
„Die Gesellschafterinnen beschließen mit der erforderlichen Mehrheit von drei Vierteln der abgegebenen Stimmen die Erhöhung des Stammkapitals der Gesellschaft von EUR [alt] um EUR [Erhöhungsbetrag] auf EUR [neu] durch Ausgabe von [Anzahl] neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00 gegen Einbringung der Forderung aus dem Wandeldarlehensvertrag vom [Datum] in Höhe von EUR [Wandlungssumme] als Sacheinlage."

### 3. Bezugsrechtsverzicht formulieren
„Die Altgesellschafterinnen verzichten hiermit auf ihr Bezugsrecht an den neuen Geschäftsanteilen und stimmen der Zulassung von [Lender] zur Übernahme der neuen Geschäftsanteile zu."

### 4. Übernahmeerklärung Lender (§ 55 Abs. 2 GmbHG)
Lender erklärt notariell die Übernahme der neuen Geschäftsanteile gegen Einbringung der Forderung. Gleichzeitig: Abtretung der Forderung an die Gesellschaft (Konfusion) oder Verzicht (§ 4.8 WDV).

### 5. Sacheinlagebericht beifügen
Werthaltigkeitsnachweis der einzubringenden Forderung (aus `sacheinlagebericht-werthaltigkeit`). Bewertungsgrundlage, Bilanzwert, ggf. Gutachten.

### 6. Anmeldung zum Handelsregister vorbereiten
Notar erstellt Anmeldung der Kapitalerhöhung (§ 57 GmbHG). Unterlagen: Beschluss, Übernahmeerklärung, Sacheinlagebericht, neue Gesellschafterliste, Leistungsnachweis (§ 56 GmbHG).

## Muster-Beschluss (Kern)

```
TOP 1: Kapitalerhöhung gegen Sacheinlage

Die Gesellschafterversammlung der Sonnenglas Solartechnologie UG (haftungsbeschränkt)
beschließt einstimmig:

1. Das Stammkapital der Gesellschaft wird von EUR 100 um EUR 7 auf EUR 107 erhöht
   durch Ausgabe von 7 neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00.

2. Die neuen Geschäftsanteile werden gegen Einbringung der Forderung der Northstar
   Pre-Seed Partners GmbH & Co. KG aus dem Wandeldarlehensvertrag vom [Datum]
   in Höhe von EUR 275694 als Sacheinlage ausgegeben.

3. Die Altgesellschafterinnen verzichten auf ihr Bezugsrecht.

4. Northstar Pre-Seed Partners GmbH & Co. KG wird zur Übernahme der 7 neuen
   Geschäftsanteile zugelassen.

[Notarielle Beurkundung durch Notar [●], [Datum]]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine notarielle Beurkundung | Beschluss unwirksam, HR-Eintragung scheitert | Notar noch nicht beauftragt | Notar bestätigt Beurkundung |
| Bezugsrechtsverzicht fehlt | Altgesellschafterinnen könnten neue Anteile beanspruchen | Verzicht nachzureichen | Verzicht im Beschluss |
| Sacheinlagebericht fehlt | Differenzhaftungsrisiko § 9 GmbHG | Bericht in Erarbeitung | Bericht vollständig |
| Wandlungssumme fehlerhaft | Beschluss und Kapitalerhöhung inkonsistent | Kleiner Rechenfehler | Exakter Betrag |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/sacheinlagebericht-werthaltigkeit/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 53 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 15.01.2013 — **II ZR 235/11**, BGHZ 196, 195 Rn. 20: Kapitalerhöhungsbeschluss der Gesellschafterversammlung muss notariell beurkundet werden (§ 53 Abs. 2 GmbHG); der Beschluss muss die wesentlichen Eckdaten enthalten (Erhöhungsbetrag, neuer Nennbetrag, Übernahmebefugnis); Mängel in der Beurkundung führen zur Nichtigkeit des Beschlusses.

BGH, Urt. v. 24.10.2005 — **II ZR 179/03**, BGHZ 165, 6 Rn. 16: Bei Sachkapitalerhöhung (Wandlung Darlehen → Anteile) muss der Kapitalerhöhungsbeschluss die Sacheinlage genau bezeichnen (Forderung aus Wandeldarlehen, Betrag, Fälligkeit); fehlende oder unklare Bezeichnung führt zur Anfechtbarkeit des Beschlusses und zur Differenzhaftung.

BGH, Urt. v. 20.09.2011 — **II ZR 234/09**, NJW 2012, 301 Rn. 18: Bezugsrechtsverzicht der übrigen Gesellschafter kann durch ausdrückliche Erklärung in der notariellen Urkunde oder durch entsprechende Satzungsklausel erfolgen; bei Fehlen des Verzichts bleibt das Bezugsrecht der Altgesellschafter erhalten.

### Normen-Ergänzung

§§ 53, 54 GmbHG (Satzungsänderung, notarielle Beurkundung) → § 55 GmbHG (Kapitalerhöhung durch Gesellschafterbeschluss) → § 56 GmbHG (Sacheinlage, Werthaltigkeitsprüfung) → § 57 GmbHG (Anmeldung zum Handelsregister) → § 57a GmbHG (vereinfachte Kapitalerhöhung) → § 47 GmbHG (Mehrheitserfordernisse, Stimmverbote)

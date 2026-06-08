---
name: sanierungsbausteine-vorschlagen-annahmen
description: "Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinbarungen Forderungsverzichte mit Besserungsschein Eigenkapitalmassnahme StaRUG-Restrukturierungsplan. Empfehlungsmatrix nach Effekt und Umsetzungszeit. Empfiehlt konkret welche Dokumente erzeugt werden sollten (Skills patronatserklärung-extern-hart-erzeugen gesellschafterdarlehen-rangrücktritt stundungsanfrage-gläubiger) im Fortbestehensprognose."
---

# Sanierungsbausteine vorschlagen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Auswahlmatrix

Aus der Zusammenführung (Skill `fortbestehensprognose-zusammenfuehren`) ergibt sich die Lücke zwischen aktueller Liquidität / Bilanzbasis und der Schwelle zur positiven Fortbestehensprognose. Die Bausteine sind nach Effekt und Umsetzungszeit zu wählen.

| Baustein | Effekt | Umsetzungszeit | Skill |
|---|---|---|---|
| Externe harte Patronatserklärung | Liquiditäts- und Bilanzeffekt sofort | 1 bis 2 Tage | patronatserklaerung-extern-hart-erzeugen |
| Comfortletter (intern/weich) | Symbolisch / Reputation; kein Bilanzeffekt | 1 Tag | comfortletter-weich-erzeugen |
| Gesellschafterdarlehen mit Rangrücktritt | Bilanzeffekt sofort; Liquidität bei Auszahlung | 3 bis 7 Tage notariell | gesellschafterdarlehen-rangrücktritt |
| Forderungsverzicht mit Besserungsschein | Bilanzeffekt sofort | 5 bis 14 Tage | forderungsverzicht-besserungsschein |
| Stundung Forderung (Lieferant Bank) | Liquiditätseffekt sofort | 5 bis 10 Tage | stundungsanfrage-gläubiger |
| Kapitalerhöhung Gesellschafter | Bilanz- und Liquiditätseffekt | 14 bis 28 Tage notariell | (Plugin gesellschaftsrecht) |
| Sale-and-Lease-back | Liquidität einmalig | 14 bis 30 Tage | externe Bank |
| Kreditlinienerhöhung | Liquidität sofort wenn zugesagt | je nach Bank | externe Bank |
| StaRUG-Restrukturierungsplan | Vielschichtig — bei drohender Zahlungsunfähigkeit | mehrere Wochen | Plugin insolvenzrecht / StaRUG-Berater |

## Prüfraster pro Baustein

### Externe harte Patronatserklärung

- **Patron** muss bonitaer sein und sich gegenüber dem Begueneten **direkt** verpflichten.
- Patronatserklärung **schriftlich** mit **klarem Verzicht auf Insolvenzanforderung** im Insolvenzfall.
- Mehrwert: Forderung des Patrons gegen sich selbst (im Insolvenzfall) entlastet den Status.
- Skill `patronatserklaerung-extern-hart-erzeugen` mit Mustervorlage.

### Comfortletter (weich)

- **Nicht** ausreichend für die Fortbestehensprognose-Bilanzentlastung.
- Kann aber **Liquiditätsunterstützung** signalisieren (z. B. an Bank).
- Skill `comfortletter-weich-erzeugen`.

### Gesellschafterdarlehen mit qualifiziertem Rangrücktritt

- Bestehendes Gesellschafterdarlehen wird mit **qualifiziertem Rangrücktritt** versehen.
- Im Status nicht passiviert (§ 19 Abs. 2 S. 2 InsO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Form: **notariell oder mit Schriftform unterzeichnet von beiden Parteien**.
- Skill `gesellschafterdarlehen-rangruecktritt`.

### Forderungsverzicht mit Besserungsschein

- Gläubiger verzichtet auf Forderung — im Insolvenzfall waere er ohnehin Auseinandersetzungsgläubiger.
- **Besserungsschein** lebt die Forderung wieder auf wenn das Unternehmen wieder zahlungsfähig.
- Steuerliche Folgen prüfen (Ertrag aus Forderungsverzicht — Sanierungsklausel § 3a EStG).
- Skill `forderungsverzicht-besserungsschein`.

### Stundungen

- Lieferanten Bank Steuern (Achtung: Steuerstundung § 222 AO) Sozialversicherung (sehr restriktiv).
- **Schriftlich** und mit **klarem Termin**.
- Skill `stundungsanfrage-glaeubiger`.

### Kapitalerhöhung

- Bareinlage durch Gesellschafter oder Sacheinlage (mit Sachgründungsbericht).
- Notarurkunde Handelsregistereintragung.
- Plugin `gesellschaftsrecht` (Skill kapitalerhöhung).

### Sale-and-Lease-back

- Verkauf eines Vermögenswerts (Maschine Grundstück) an Leasing-Geber mit anschließendem Leasing.
- Liquiditätseffekt einmalig.
- Folgekosten (Leasingraten) im Liquiditätsplan berücksichtigen.

### StaRUG-Restrukturierungsplan

- Nur bei **drohender** Zahlungsunfähigkeit (§ 18 InsO mit Prognose 24 Monate) — nicht bei akuter Zahlungsunfähigkeit oder Überschuldung.
- Restrukturierungsbeauftragter wird vom Gericht bestellt.
- Plan kann **mit Mehrheit der Gläubiger** durchgesetzt werden.
- Externe Begleitung durch StaRUG-Anwalt notwendig.

## Empfehlungslogik

```yaml
empfehlungen:
 zur-erreichung-positive-prognose:
 pflicht:
 - baustein: patronatserklaerung-extern-hart
 umfang: 200000 EUR
 patron: Hauptgesellschafter
 skill: patronatserklaerung-extern-hart-erzeugen
 prioritaet: kritisch
 umsetzung-bis: 2026-05-27

 empfohlen:
 - baustein: stundungsanfrage-glaeubiger
 anzahl: 5 Lieferanten
 skill: stundungsanfrage-glaeubiger
 prioritaet: hoch
 umsetzung-bis: 2026-06-15

 - baustein: gesellschafterdarlehen-rangruecktritt
 umfang: 120000 EUR bestehend
 skill: gesellschafterdarlehen-rangruecktritt
 prioritaet: hoch
 umsetzung-bis: 2026-05-25 notariell

 optional-bei-eskalation:
 - baustein: forderungsverzicht-besserungsschein
 umfang: 50000 EUR Bank
 skill: forderungsverzicht-besserungsschein
 prioritaet: mittel
 umsetzung-bis: 2026-06-30

 ergebnis-nach-massnahmen:
 bilanzbasis-vorher: positiv 133000 EUR
 bilanzbasis-nach-massnahmen: positiv 333000 EUR (zusätzlich Patronage 200000)
 liquiditaet-vorher-stress: negativ
 liquiditaet-nach-massnahmen-stress: positiv
 gesamtprognose: positiv mit Maßnahmen
```

## Zeitliche Reihenfolge

- **Sofort** (binnen Tagen): Patronatserklärung Rangrücktritt
- **Innerhalb Wochen** (drei Wochen Frist § 15a InsO bei Zahlungsunfähigkeit beachten): Stundungen Forderungsverzichte
- **Innerhalb Frist § 15a InsO Sechs Wochen**: alle Maßnahmen verbindlich
- **Bei Frist-Überschreitung**: keine zusätzliche Maßnahme mehr ausreichend — sofort Insolvenzantrag (Skill `wenn-prognose-negativ-naechste-schritte`).

## Ausgabe

- `sanierungsbausteine-empfehlung.md` mit konkreter Maßnahmenliste je Prioritaet.
- Nächste Skill-Verlinkungen je Maßnahme.
- Eintrag in Tagesnotizen zur Umsetzungskontrolle.
- Stichtag-Wiedervorlage in zwei Wochen zur Prüfung der tatsächlichen Umsetzung.

## Aktuelle Leitentscheidungen — Sanierungsbausteine

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Sanierungsbausteine

§ 19 Abs. 2 InsO (Fortbestehensprognose) → §§ 29 ff. StaRUG (vorinsolvenzliche Sanierung) → § 39 Abs. 4 InsO (Sanierungsprivileg Gesellschafterdarlehen) → § 3a EStG (steuerfreier Sanierungserloes) → § 133 InsO (Anfechtungsschutz bei echtem Sanierungskonzept)

## Triage — Sanierungsbaustein-Auswahl

1. **Zeitbedarf?** Patronatserklaerung/Rangruecktritt: 1-2 Tage. StaRUG-Plan: 4-8 Wochen. Kapitalerhöhung: 4-12 Wochen.
2. **Glaeubiger-Einbindung noetig?** Stundungsanfragen, Verzichte — Zustimmung einholen.
3. **Steuerliche Wirkung?** Sanierungserloes § 3a EStG: Voraussetzungen pruefen; Steuerberater einbinden.
4. **Gesamtkonzept?** Alle Bausteine zusammen muessen eine positive Prognose tragen (IDW S 11 Konformitaet).


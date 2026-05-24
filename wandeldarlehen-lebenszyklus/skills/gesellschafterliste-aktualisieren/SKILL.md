---
name: gesellschafterliste-aktualisieren
description: "Aktualisierte Gesellschafterliste nach § 40 GmbHG mit fortlaufenden Nummern, neuem Lender-Eintrag nach Kapitalerhoehung, Bestaetigung Geschaeftsfuehrung, Notar-Bestaetigung. Gutglaubenswirkung nach § 16 GmbHG und Frist zur Einreichung beim Handelsregister. Transparenzregister-Meldepflicht § 19 GwG."
---

# Gesellschafterliste aktualisieren (§ 40 GmbHG)

## Zweck

Dieser Skill erstellt die aktualisierte Gesellschafterliste nach der Kapitalerhöhung und dem Eintritt des Lenders als neuer Gesellschafter. Die Liste wird beim Handelsregister eingereicht. Phase D des Lebenszyklus.

## Eingaben

- Vorherige Gesellschafterliste (aus dem Handelsregister)
- Ergebnis der Kapitalerhöhung (neue Anteile, Nennwert, Gesellschafternummer)
- Vollständige Daten Lender (Name, Geburtsdatum, Anschrift oder Sitz und Vertreter)
- Notar (hat Kapitalerhöhung beurkundet und überreicht normalerweise aktualisierte Liste)
- Datum der Beurkundung und des vorgesehenen Einreichungsdatums

## Rechtlicher Rahmen

### Primärnormen
- § 40 Abs. 1 GmbHG (Geschäftsführerin reicht neue Gesellschafterliste bei Änderung ein)
- § 40 Abs. 2 GmbHG (Mitwirkung eines Notars: Notar reicht Liste ein, wenn er an Änderung mitgewirkt hat)
- § 16 GmbHG (Gutglaubenswirkung der Gesellschafterliste: nur als Gesellschafter gilt, wer eingetragen ist)
- § 15 GmbHG (Anteilsübertragung – Vollwirkung erst mit Eintragung)
- § 19 GwG (Transparenzregister – wirtschaftlich Berechtigte nach Änderung melden)

### Rechtsprechung
- BGH, Urt. v. 17. November 2008 – II ZR 244/07 (Gutglaubenswirkung § 16 GmbHG – nur eingetragene Gesellschafter)
- BGH, Urt. v. 20. September 2011 – II ZR 234/09 (Gesellschafterliste und unrichtige Angaben)

## Vorgehen

### 1. Listenentwurf erstellen
Alle Gesellschafterinnen und neuer Lender mit vollständigen Angaben:
- Laufende Nummer (fortlaufend, keine Lücken)
- Gesellschaftername (Vor- und Nachname oder Firma)
- Geburtsdatum (natürliche Person) oder HRB + Amtsgericht (juristische Person)
- Anschrift (Wohnanschrift oder Geschäftsanschrift Sitz)
- Anzahl der Geschäftsanteile und Nennwert (in EUR)
- Datum des Erwerbs (Beurkundungsdatum Kapitalerhöhung)

### 2. Vollständigkeitsprüfung
Alle alten Gesellschafterinnen unverändert übernehmen (Anteile, Nennwert). Neuen Lender-Eintrag hinzufügen. Gesamtstammkapital prüfen: Summe aller Nennwerte = neues Stammkapital.

### 3. Einreichung durch Notar (§ 40 Abs. 2 GmbHG)
Da Notar an Kapitalerhöhung mitgewirkt hat, reicht er die neue Liste ein. Frist: unverzüglich nach Beurkundung.

### 4. Gutglaubenswirkung beachten
Ab Einreichung der neuen Liste gilt der Lender als Gesellschafter (§ 16 Abs. 1 GmbHG). Vor Einreichung: kein Stimmrecht, kein Gewinnbezugsrecht, keine HR-Legitimation.

### 5. Transparenzregister aktualisieren (§ 19 GwG)
Falls Lender nach Kapitalerhöhung wirtschaftlich Berechtigter (mehr als 25 %) wird: Meldung an Transparenzregister unverzüglich nach Eintragung ins Handelsregister.

### 6. Kopie an alle Parteien
Aktuelle Gesellschafterliste (nach HR-Eintragung) an Geschäftsführerin, alle Gesellschafterinnen, Lender, Steuerberater. Ablage in Gesellschaftsakte.

## Muster-Gesellschafterliste (Auszug)

```
Gesellschafterliste der Sonnenglas Solartechnologie UG (haftungsbeschränkt)
Berlin, HRB 123456 B, Amtsgericht Charlottenburg
Stand: [Datum nach Kapitalerhöhung]

Nr. | Name | Geburtsdatum / HRB | Anschrift | Anteile | Nennwert EUR | Erwerb
1   | Dr. Mira Schoeneck | [Datum] | [Anschrift] | 40 | 40 | [Gründungsdatum]
2   | Lina Habersaat | [Datum] | [Anschrift] | 35 | 35 | [Gründungsdatum]
3   | [Treasury GmbH] | HRB ●, AG ● | [Anschrift] | 25 | 25 | [Datum]
4   | Northstar Pre-Seed Partners GmbH & Co. KG | HRA 99999, AG Frankfurt | [Anschrift] | 7 | 7 | [Beurkundungsdatum KE]

Gesamt: 107 Anteile, Stammkapital EUR 107
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Liste nicht eingereicht | Lender hat keine Gutglaubensposition | Liste in Erarbeitung | Notar reicht sofort ein |
| Fehlerhafte Anteilszahl | HR-Liste und tatsächliche Beteiligung weichen ab | Kleiner Tippfehler | Exakt korrekt |
| Transparenzregister nicht aktualisiert | GwG-Bußgeld (§ 56 GwG) | Frist läuft | Aktualisierung bestätigt |
| Lender als Gesellschafter ohne HR-Eintragung | Stimmrechte, Gewinnrechte blockiert | Eintragung beantragt | Eintragung erfolgt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/handelsregisteranmeldung-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40/§ 16 aktualisieren.

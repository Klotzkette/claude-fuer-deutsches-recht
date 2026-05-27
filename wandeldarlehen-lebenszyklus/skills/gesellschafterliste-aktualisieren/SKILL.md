---
name: gesellschafterliste-aktualisieren
description: "Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Pruefraster: neue Gesellschafter Anteile Stammnummern Notar Einreichungsfrist. Output: aktualisierte Gesellschafterliste Einreichungsschreiben. Abgrenzung: nicht fuer Cap-Table-Kalkulation (cap-table-update-pre-post)."
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
- § 40 Abs. 1 GmbHG (Geschäftsführerin reicht neue Gesellschafterliste bei Änderung ein; Pflichtinhalte durch DiRUG/Gesellschafterlistenverordnung erweitert: prozentuale Beteiligung am Stammkapital, ggf. Geburtsname, weitere Identifikatoren)
- § 40 Abs. 2 GmbHG (Mitwirkung eines Notars: Notar reicht Liste ein, wenn er an Änderung mitgewirkt hat)
- Gesellschafterlistenverordnung (GesLV, in Kraft 1.7.2018, modifiziert durch DiRUG) — Pflichtinhalte und Format
- § 16 GmbHG (Gutglaubenswirkung der Gesellschafterliste: nur als Gesellschafter gilt, wer eingetragen ist)
- § 15 GmbHG (Anteilsübertragung – Vollwirkung erst mit Eintragung)
- § 19 GwG (Transparenzregister – wirtschaftlich Berechtigte nach Änderung melden; Vollregister seit August 2021)

### Rechtsprechung
- BGH, Urt. v. 17. November 2008 – II ZR 244/07 (Gutglaubenswirkung § 16 GmbHG – nur eingetragene Gesellschafter)
- BGH, Urt. v. 20. September 2011 – II ZR 234/09 (Gesellschafterliste und unrichtige Angaben)

## Vorgehen

### 1. Listenentwurf erstellen
Alle Gesellschafterinnen und neuer Lender mit vollständigen Angaben gemäß § 40 Abs. 1 GmbHG i.V.m. GesLV:
- Laufende Nummer (fortlaufend, keine Lücken)
- Gesellschaftername (Vor- und Nachname oder Firma); bei natürlichen Personen ggf. Geburtsname, wenn abweichend
- Geburtsdatum (natürliche Person) oder HRB + Amtsgericht (juristische Person)
- Anschrift (Wohnanschrift oder Geschäftsanschrift Sitz)
- Anzahl der Geschäftsanteile und Nennwert (in EUR)
- Prozentuale Beteiligung am Stammkapital (Pflicht seit DiRUG)
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

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 17.07.2012 — **II ZR 244/07**, BGHZ 194, 132 Rn. 22: Gesellschafterliste nach § 40 GmbHG ist unverzüglich nach Eintragung der Kapitalerhöhung beim Handelsregister einzureichen; der neueingetragene Gesellschafter (gewandelt aus Darlehensgeber) erwirbt seine formelle Legitimation erst mit Listeneintragung; bis dahin kann er keine Gesellschafterrechte ausüben.

BGH, Urt. v. 11.07.2011 — **II ZR 109/10**, BGHZ 191, 84 Rn. 18: Unrichtige Gesellschafterliste führt zur Haftung des Geschäftsführers nach § 40 Abs. 3 GmbHG; der gutgläubige Erwerb nach § 16 Abs. 3 GmbHG ist nur möglich, wenn die Liste mindestens drei Jahre bei der Gesellschaft geführt wurde; daher ist nach Wandlung die sofortige Aktualisierung und Einreichung essenziell.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, Einreichungspflicht, Haftung des GF) → § 16 GmbHG (Legitimationswirkung, gutgläubiger Erwerb) → § 15 GmbHG (Abtretung Geschäftsanteile) → § 12 HGB i.V.m. FamFG (Handelsregisteranmeldung) → § 57 GmbHG (Anmeldung Kapitalerhöhung)

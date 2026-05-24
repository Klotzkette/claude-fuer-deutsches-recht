---
name: notar-paket-uebermittlung
description: "Erstellung des vollstaendigen Notar-Pakets zur Handelsregister-Anmeldung der Kapitalerhoehung: Kapitalerhöhungsbeschluss, Sacheinlagebericht, Anmeldung Handelsregister nach § 57 GmbHG, neue Gesellschafterliste nach § 40 GmbHG, Liste Geschaeftsanteile, Anschrift Notar, Terminbuchung und Checkliste einzureichender Dokumente."
---

# Notar-Paket zur Handelsregister-Anmeldung

## Zweck

Dieser Skill stellt das vollständige Paket für den Notar zusammen, der die Kapitalerhöhung beim Handelsregister anmeldet. Phase D des Lebenszyklus.

## Eingaben

- Notariell beurkundeter Kapitalerhöhungsbeschluss (aus `gesellschafterbeschluss-kapitalerhoehung`)
- Sacheinlagebericht (aus `sacheinlagebericht-werthaltigkeit`)
- Aktuelle Gesellschafterliste (§ 40 GmbHG, aus `gesellschafterliste-aktualisieren`)
- Name und Anschrift des zuständigen Notars
- Handelsregisternummer und zuständiges Amtsgericht

## Rechtlicher Rahmen

### Primärnormen
- § 57 GmbHG (Anmeldung der Kapitalerhöhung – durch Geschäftsführerin beim Registergericht)
- § 57a GmbHG (Inhalt der Anmeldung: Betrag der Kapitalerhöhung, neue Gesellschafterliste)
- § 40 GmbHG (Gesellschafterliste – nach Kapitalerhöhung neue Liste beim Handelsregister)
- § 78 GmbHG (Notarielle Beglaubigung der Anmeldung)
- § 8 GmbHG (Inhalt der Anmeldung allgemein)

### Rechtsprechung
- BGH, Urt. v. 17. November 2008 – II ZR 244/07 (Gesellschafterliste und Gutglaubenswirkung § 16 GmbHG)
- OLG Düsseldorf, Beschl. v. 10. April 2019 – 3 Wx 228/18 (Anforderungen Sacheinlagebericht bei Kapitalerhöhung)

## Vorgehen

### 1. Vollständigkeitsprüfung des Notar-Pakets

| Dokument | Status |
|---|---|
| Notariell beurkundeter Kapitalerhöhungsbeschluss | [ ] |
| Notariell beurkundete Übernahmeerklärung Lender | [ ] |
| Sacheinlagebericht (unterschrieben) | [ ] |
| Neue Gesellschafterliste (§ 40 GmbHG) | [ ] |
| Anmeldung Kapitalerhöhung (§ 57 GmbHG, von Notar vorbereitet) | [ ] |
| Nachweis Leistung Sacheinlage (Forderungsabtretung oder Konfusionsnachweis) | [ ] |

### 2. Gesellschafterliste vorbereiten (§ 40 GmbHG)
Nach Kapitalerhöhung neue Liste mit: fortlaufender Nummer, Name, Geburtsdatum, Wohnanschrift, Anteilszahl, Nennwert, Datum Erwerb. Alle Gesellschafterinnen plus neuer Lender. Unterschrift: Notar (§ 40 Abs. 2 GmbHG nach Kapitalerhöhung bei Notar-Mitwirkung) oder Geschäftsführerin.

### 3. Anmeldungstext § 57 GmbHG
„Die Geschäftsführerin der Sonnenglas Solartechnologie UG (haftungsbeschränkt) meldet zur Eintragung in das Handelsregister an: Die Kapitalerhöhung vom [Datum] in Höhe von EUR [Betrag] durch Ausgabe von [Anzahl] neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00 gegen Sacheinlage ist vollzogen. Der neue Gesellschafter hat die Sacheinlage vollständig erbracht." Notarielle Beglaubigung der Anmeldung.

### 4. Notar-Briefing
E-Mail an Notar mit: Kurzdarstellung des Vorgangs, Anlagen (Beschluss, Sacheinlagebericht, neue Gesellschafterliste), gewünschtes Datum der Einreichung, Kontakt für Rückfragen.

### 5. Bearbeitungsdauer abschätzen
Handelsregistereintragung in der Regel zwei bis acht Wochen nach Einreichung. Beschleunigte Eintragung auf Antrag in dringlichen Fällen möglich.

### 6. Transparenzregister-Folge-Anmeldung
Nach Kapitalerhöhung: Pflicht zur Aktualisierung des Transparenzregisters nach § 19 GwG (wirtschaftlich Berechtigte). Frist: unverzüglich. Notar erledigt dies regelmäßig mit.

## Inhaltsverzeichnis Notar-Paket

```
1. Beurkundetes Protokoll der außerordentlichen Gesellschafterversammlung
   vom [Datum], Urk.-Nr. [●] des Notars [●]
2. Beurkundete Übernahmeerklärung Northstar Pre-Seed Partners GmbH & Co. KG
   vom [Datum], Urk.-Nr. [●]
3. Sacheinlagebericht vom [Datum]
4. Neue Gesellschafterliste nach § 40 GmbHG
5. Anmeldung Kapitalerhöhung nach § 57 GmbHG
6. Nachweis Einbringung Sacheinlage (Forderungsabtretung)
[Gesamt: 6 Positionen]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sacheinlage vor Anmeldung nicht erbracht | § 57 GmbHG-Voraussetzung fehlt | Einbringungsnachweis unvollständig | Einbringung vollständig belegt |
| Gesellschafterliste nicht aktualisiert | § 16 GmbHG-Gutglaubenswirkung gefährdet | Liste in Erarbeitung | Aktuelle Liste beigefügt |
| Notar nicht in Beurkundungsbezirk | Zuständigkeitsproblem | Notar außerhalb prüfen | Zuständiger Notar |
| Transparenzregister nicht aktualisiert | GwG-Verstoß, Bußgeld | Frist läuft | Aktualisierung beauftragt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/handelsregisteranmeldung-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 57 ff. oder GwG § 19 aktualisieren.

---
name: arbeitsblatt-perspektiven-definieren
description: "Definiert die dritte Wuerfel-Achse — Arbeitsblaetter als Perspektiven die ueber denselben Dokumentenstapel laufen aber jeweils eine andere Brille aufsetzen. Typische Perspektiven: Recht (Anwalt) Steuer (Steuerberater) Wirtschaft (Buyside-Analyst) Datenschutz (DSGVO-Beauftragter) IT (Architekt) Betrieb (Operations) Compliance (GwG / Lieferkettengesetz). Pro Arbeitsblatt: eigene Zusatzspalten Auslassungen Sonderprompts Ampelregeln. Erzeugt `arbeitsblaetter.yaml`. Erlaubt Kreuzblatt-Konsistenzpruefung."
---

# /tabellenreview-3d:arbeitsblatt-perspektiven-definieren

## Zweck

Excel kann mehrere Tabellenblaetter nebeneinander. Der 3D-Würfel übernimmt dieses Bild: dieselben Dokumente (Zeilen) werden mehrfach geprüft, jedes Mal aus einer anderen Perspektive (Arbeitsblatt). Die Spalten sind je Arbeitsblatt zum Teil deckungsgleich (vergleichbare Datenpunkte) und zum Teil arbeitsblattspezifisch.

## Standard-Perspektiven

### Recht (Anwaltsperspektive)

- Spalten: AGB-Wirksamkeit Haftungsregime Verjährungsverkürzung Gerichtsstand Schiedsklausel Schriftformklausel
- Materialität: rot bei Klauseln die nach BGB Paragraph 307 unwirksam sind
- Prüfer: zugelassener Rechtsanwalt

### Steuer (Steuerberater)

- Spalten: Umsatzsteuer-Behandlung Rechnungspflichtangaben UStG Paragraph 14 grenzüberschreitend ja / nein Reverse-Charge ja / nein
- Materialität: rot bei UStG-Compliance-Risiken
- Prüfer: Steuerberater oder Wirtschaftsprüfer

### Wirtschaft (Buyside-Analyst)

- Spalten: Vertragsvolumen Laufzeit Kündigungsdatum Preisanpassungsmechanik Working-Capital-Effekt
- Materialität: rot bei Top-5-Kunden-Konzentration über 60 Prozent
- Prüfer: Deal-Lead / Corp-Dev

### Datenschutz (DSGVO-Beauftragter)

- Spalten: Datenkategorien Rechtsgrundlage Auftragsverarbeitung-Pflicht AVV vorhanden Drittlandtransfer SCC vorhanden
- Materialität: rot bei fehlender AVV trotz Auftragsverarbeitung (DSGVO Artikel 28)
- Prüfer: Datenschutzbeauftragter

### IT (Architekt)

- Spalten: Hosting-Modell Verschlüsselungs-Standard Lock-in-Risiko Schnittstellen-Dokumentation Exit-Daten-Format
- Materialität: rot bei nicht standardisierten Datenformaten ohne Exit-Pflicht
- Prüfer: IT-Architekt

### Betrieb (Operations)

- Spalten: Service-Level Reaktionszeit Wiederherstellungszeit Eskalationsstufen Vertretungsregelung
- Materialität: rot bei SLA-Reaktionszeit über 4 Stunden bei produktionskritischen Services
- Prüfer: Operations-Lead

### Compliance (GwG / LkSG)

- Spalten: Wirtschaftlich Berechtigter bekannt Sanktionslisten-Prüfung Lieferketten-Risiko-Region nach LkSG
- Materialität: rot bei Sanktionslisten-Treffer
- Prüfer: Compliance-Officer

## Pflichtfelder pro Arbeitsblatt

```yaml
- id: recht
  titel: "Rechtliche Perspektive"
  perspektive: "anwalt"
  pruefer-rolle: "rechtsanwalt"
  eigene-spalten-zusaetze:
    - id: agb-wirksamkeit
      prompt: "Sind die AGB-Klauseln nach BGB Paragraph 305 ff. wirksam?"
  auslassungen:
    - umsatzsteuer  # Steuerblatt; hier nicht zuständig
  ampel-regel:
    rot: "Unwirksame Klausel BGB Paragraph 307"
    gelb: "AGB-Wirksamkeit zweifelhaft"
    gruen: "Wirksam oder Individualvereinbarung"
```

## Stapelung

Die Arbeitsblätter werden in der Excel-Ausgabe als Tabellenreiter nebeneinander dargestellt. Im PDF-Bericht erscheinen sie als aufeinanderfolgende Abschnitte. In `kreuzblatt-konsistenzpruefung` werden Widersprüche zwischen Arbeitsblättern gefunden (z. B. ein Vertrag der rechtlich grün aber wirtschaftlich rot ist — das ist legitim und soll markiert werden).

## Ausgabe

- `arbeitsblaetter.yaml` mit allen Arbeitsblättern, deren Spaltenzusätze, Auslassungen und Prüfer-Rollen
- `arbeitsblatt-matrix.md` als menschenlesbare Übersicht

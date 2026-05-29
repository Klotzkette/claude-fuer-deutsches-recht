---
name: arbeitsblatt-perspektiven-definieren
description: "Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster, Gläubigerstellung. Output: Perspektivendefinition als Grundlage für Wuerfel-Aufbau. Abgrenzung: nicht Prüfungsdurchführung."
---

# /tabellenreview-3d:arbeitsblatt-perspektiven-definieren

## Zweck

Excel kann mehrere Tabellenblaetter nebeneinander. Der 3D-Würfel übernimmt dieses Bild: dieselben Dokumente (Zeilen) werden mehrfach geprüft, jedes Mal aus einer anderen Perspektive (Arbeitsblatt). Die Spalten sind je Arbeitsblatt zum Teil deckungsgleich (vergleichbare Datenpunkte) und zum Teil arbeitsblattspezifisch.

## Triage zu Beginn

1. Wie viele Perspektiven sind erforderlich? (Recht / Steuer / Wirtschaft / Datenschutz / IT)
2. Muss jede Perspektive von einem anderen Pruefer verantwortet werden?
3. Gibt es GwG-Compliance-Anforderungen? → Separate Compliance-Perspektive (LkSG / GwG / IDW PS 980)
4. Ist ein M&A-Closing-Datum bekannt? → Fristen der Arbeitsblaetter entsprechend konfigurieren

## Rechtliche Grundlagen fuer Pruefer-Perspektiven

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

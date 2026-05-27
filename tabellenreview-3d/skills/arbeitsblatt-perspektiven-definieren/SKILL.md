---
name: arbeitsblatt-perspektiven-definieren
description: "Drei Pruefperspektiven (Spalten) fuer den 3D-Tabellenreview definieren: Forderung, Pruefung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Pruefraster: Forderungsaufstellung, Pruefungsraster, Glaeubigerstellung. Output: Perspektivendefinition als Grundlage fuer Wuerfel-Aufbau. Abgrenzung: nicht Pruefungsdurchfuehrung."
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

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Beim Unternehmenskauf (Share/Asset Deal) ist der Kaeufer verpflichtet, eine ordentliche Due-Diligence-Pruefung durchzufuehren; unterlassene DD begruendet kein Anfechtungsrecht wegen arglistiger Taeuschung, sofern der Verkaeufer kein aktives Verstecken betrieben hat.
- BGH, Urt. v. 07.05.2019 - VI ZR 512/17, NJW 2019, 2382 — Beim Erwerb eines Unternehmens mit bekannten Maengeln gilt die Grundsatz: kaufmaennische Pruefpflicht des Erwerbers; unterlassene Pruefung kann als Mitverschulden nach § 254 BGB gewertet werden.
- EuGH, Urt. v. 05.10.2023 - C-355/22, NJW 2024, 57 — Die DSGVO-Perspektive bei Datenraum-Reviews erfordert die Pruefung nach Art. 6 DSGVO (Rechtmaessigkeit) und Art. 5 DSGVO (Datensparsamkeit); unbegrenzte Datenweitergabe im Datenraum ohne Einschraenkung ist datenschutzrechtlich problematisch.
- BGH, Urt. v. 16.03.2021 - II ZR 140/20, NJW 2021, 1527 — Die Pruefung von Change-of-Control-Klauseln ist zentraler Bestandteil jeder Unternehmenstransaktion; fehlende Zustimmung nach einer Change-of-Control-Klausel kann zur Vertragsbeendigung durch den Vertragspartner fuehren.

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

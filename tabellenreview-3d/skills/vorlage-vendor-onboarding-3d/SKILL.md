---
name: vorlage-vendor-onboarding-3d
description: "Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output: Vendor-Onboarding-Prüftabelle. Abgrenzung: nicht allgemeine Vertragsprüfung."
---

# /tabellenreview-3d:vorlage-vendor-onboarding-3d

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Spalten (17 Datenpunkte)

### Stammdaten

1. Vendor-Name und Rechtsform
2. Branche und Hauptleistung
3. Sitz und Lieferketten-Region

### Datenschutz

4. AVV-Pflicht (DSGVO Artikel 28)
5. AVV-vorhanden und aktuelle Fassung
6. Drittlandtransfer (USA UK CH andere)
7. SCC vorhanden (Standardvertragsklauseln)

### IT und SLA

8. Verschlüsselung in Transit und at Rest
9. SLA-Reaktionszeit
10. SLA-Verfügbarkeit (Prozent / Jahr)
11. Subunternehmer-Liste vollständig

### Exit und Daten

12. Exit-Klausel (Vertragsende Pflichten)
13. Datenherausgabe-Format und Frist

### Compliance

14. Sanktionsliste gefiltert (EU US OFAC)
15. GwG-Prüfung wirtschaftlich Berechtigter
16. Lieferketten-Risiko nach LkSG (Branchen und Region)

### Wirtschaft

17. Versicherungssumme und Haftungsbegrenzung

## Arbeitsblatt-Perspektiven (5)

### Vertrag

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Gerichtsstand / Vertragsstrafe
- Prüfer: Vertragsanwalt
- Materialität rot: Haftungsausschluss für Vorsatz / grobe Fahrlaessigkeit

### Datenschutz

- Zusatzspalten: TIA (Transfer Impact Assessment) / Datenschutz-Folgenabschätzung-Pflicht / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV; Drittlandtransfer ohne SCC + TIA

### IT-Sicherheit

- Zusatzspalten: ISO-27001-Zertifikat / SOC-2-Bericht / Penetrationstest-Bericht / Vulnerability-Disclosure-Policy
- Prüfer: CISO / IT-Sicherheit
- Materialität rot: keine ISO-27001 UND keine SOC-2 UND Verarbeitung sensibler Daten

### Compliance (GwG / LkSG)

- Zusatzspalten: GwG-Transparenzregister / Sanktionslisten-Treffer / Risiko nach LkSG Paragraph 5 / Beschwerdeverfahren-Anbindung
- Prüfer: Compliance-Officer
- Materialität rot: Sanktionslisten-Treffer; LkSG-Hochrisiko-Region ohne Prüfkette

### Wirtschaft

- Zusatzspalten: Vendor-Volumen / Lock-in-Risiko / Wechselkosten / Konzentrations-Risiko
- Prüfer: Einkauf / Risikomanagement
- Materialität rot: Vendor-Lock-in ohne Exit-Daten-Standard UND mehr als 30 Prozent Anteil an kritischer Leistung

## Normenrahmen

- **DSGVO** — Artikel 28 (Auftragsverarbeitung) Artikel 35 (DSFA) Artikel 44 ff. (Drittlandtransfer)
- **BDSG** — Beschäftigtendatenschutz
- **GwG** — Paragraph 10 Sorgfaltspflichten Paragraph 20 Transparenzregister
- **LkSG** — Paragraph 5 Risikoanalyse Paragraph 6 Präventionsmaßnahmen
- **BGB** — Paragraph 305 ff. AGB-Kontrolle
- **TKG / NIS2** — bei TK-/Cyber-bezogenen Vendoren

## Ausgabe

Würfel-Schema fix und fertig. Direkt einsatzbereit.

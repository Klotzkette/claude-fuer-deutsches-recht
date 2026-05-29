---
name: vorlage-ma-due-diligence
description: "Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A-Skill."
---

# /tabellenreview-3d:vorlage-ma-due-diligence

## Zweck

M&A-DD bei einem Vertragsstapel der Zielgesellschaft. Die Standardfragen sind bekannt — diese Vorlage liefert sie fix und fertig: Spaltenprompts mit BGH-Verankerung, vier Arbeitsblatt-Perspektiven, Ampel-Schwellen praxisbewährt.

## Spalten (18 Datenpunkte)

1. **Vertragsart** — Rahmenvertrag / Einzelvertrag / NDA / Lizenz / Lieferung / Werk
2. **Laufzeit und Beginn** — Vertragsdatum + Festlaufzeit / unbefristet
3. **Kündigungsfrist** — ordentliche / außerordentliche / Sondertatbestände
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **MAC-Klausel** — Wesentlichkeitsdefinition / Rechtsfolge (BGB Paragraph 313 / 314)
6. **Abtretungsverbot** — BGB Paragraph 399 / HGB Paragraph 354a / Vertragsübernahme
7. **Haftungsbegrenzung** — pro Fall / pro Jahr / Ausschluss Vorsatz und grobe Fahrlaessigkeit
8. **Garantien** — beschaffenheitsbezogen / verschuldensunabhängig / Haftungsausschluss BGB Paragraph 444
9. **Vertragsstrafe** — Höhe / Deckelung / Verschuldensanknuepfung
10. **Service-Level** — Reaktionszeit / Verfügbarkeit / Wiederherstellungszeit
11. **Datenschutz-AVV** — DSGVO Artikel 28 / Drittlandtransfer / SCC / TIA
12. **Geheimhaltung** — Dauer / Carve-Outs / Rückgabe / Sanktionen
13. **Vergütung** — Festpreis / Stundensatz / Erfolg / Schwellen
14. **Preisanpassung** — Indexbindung / Schwellen / Kündigungsrecht der Gegenseite
15. **Schriftform** — Änderungsvorbehalt / Sprengsatz (BGB Paragraph 125 Satz 2)
16. **Gerichtsstand** — vereinbarter Gerichtsstand / Kaufmannsklausel (ZPO Paragraph 38)
17. **Schiedsklausel** — Schiedsgericht / Sitz / Sprache / Verfahrensordnung
18. **Anwendbares Recht** — Rechtswahl / kollisionsrechtliche Wirkungen

## Arbeitsblatt-Perspektiven (4)

### Recht (Anwaltsperspektive)

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Klauselverbote (BGB Paragraph 308 / Paragraph 309) / Verjährungsverkürzung
- Prüfer: M&A-Lead-Counsel
- Materialität rot: unwirksame Klausel mit Hauptleistungsbezug

### Steuer (Steuerberater)

- Zusatzspalten: Umsatzsteuer-Behandlung / Reverse-Charge / verdeckte Gewinnausschuettung bei Konzernverträgen (KStG)
- Prüfer: Steuerberater
- Materialität rot: USt-Risiko mehr als 100k EUR

### Wirtschaft (Buyside)

- Zusatzspalten: Vertragsvolumen pro Jahr / Top-Kunde-Konzentration / Working-Capital-Effekt / Verlängerungsoption
- Prüfer: Deal-Lead
- Materialität rot: Vertrag > 10 Prozent Umsatz UND Kündigungsrecht der Gegenseite < 12 Monate

### Datenschutz (DSGVO)

- Zusatzspalten: Datenkategorien / Rechtsgrundlage Artikel 6 / Drittlandtransfer / Auftragsverarbeitung / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV oder Drittlandtransfer ohne SCC

## BGH-Leitsätze (Auswahl)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

Würfel-Schema fix und fertig in `wuerfel-schema.yaml` mit allen drei Achsen. Direkt einsatzbereit für `review-durchfuehren`.

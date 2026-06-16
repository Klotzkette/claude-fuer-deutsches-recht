---
name: vorlage-ma-arbeitsblatt-perspektiven-audit
description: "Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A"
---

# /tabellenreview-3d:vorlage-ma-due-diligence

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->


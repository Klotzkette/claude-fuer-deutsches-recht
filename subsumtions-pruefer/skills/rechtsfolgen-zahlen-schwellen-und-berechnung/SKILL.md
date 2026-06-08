---
name: rechtsfolgen-zahlen-schwellen-und-berechnung
description: "Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung im Subsumtions Pruefer."
---

# Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wichtige Schwellenwerte und gesetzliche Beträge (Stand: Modellwissen; live prüfen)

| Bereich | Schwelle / Betrag | Norm | Quelle |
|---|---|---|---|
| Zuständigkeit AG / LG | bis EUR 5.000 AG; ab EUR 5.000 LG | §§ 23, 71 GVG | gesetze-im-internet.de |
| Berufungssumme | EUR 600 | § 511 Abs. 2 Nr. 1 ZPO | gesetze-im-internet.de |
| Kleinstunternehmer USt | EUR 22.000 (ab 2025: EUR 25.000) | § 19 UStG | live prüfen; gesetze-im-internet.de |
| DSGVO-Bußgeld max. | EUR 20 Mio. oder EUR 4% Jahresumsatz | Art. 83 Abs. 5 DSGVO | eur-lex.europa.eu |
| Verzugszins | Basiszinssatz + 5 PP (§ 288 Abs. 1 BGB); + 9 PP bei B2B (§ 288 Abs. 2 BGB) | §§ 288, 247 BGB | gesetze-im-internet.de; Bundesbank.de (Basiszinssatz) |
| Mietkaution max. | 3 Nettokaltmieten | § 551 BGB | gesetze-im-internet.de |
| Abfindung | Kein gesetzlicher Betrag; § 1a KSchG: 0,5 Monatsverdienst/Jahr | § 1a KSchG | live prüfen |
| Schmerzensgeld | Kein Schematismus; nach Billigkeitsgesichtspunkten | § 253 Abs. 2 BGB | BGH-Rechtsprechung live prüfen |

## Berechnungsschemata

### Schema 1 — Verzugszinsen

```
Hauptforderung: EUR X
Fälligkeit: TT.MM.JJJJ (bei Mahnung oder vertraglicher Bestimmung)
Verzugsbeginn: Mahnung (§ 286 Abs. 1 BGB) oder 30 Tage nach Fälligkeit (§ 286 Abs. 3 BGB)
Zinssatz: Basiszinssatz (Bundesbank.de, aktuell prüfen) + 5 PP (B2C) / + 9 PP (B2B)
Zinsen pro Tag: Hauptforderung × Zinssatz / 365
Gesamtzinsen: Zinsen pro Tag × Anzahl Tage Verzug
```

### Schema 2 — Schadensersatz § 249 BGB

```
Naturalrestitution (§ 249 Abs. 1 BGB): Zustand wie ohne schädigendes Ereignis
Differenzschaden: Vermögen mit schädigendem Ereignis vs. ohne
Positiver Schaden (damnum emergens): tatsächlich entstandene Kosten
Entgangener Gewinn (lucrum cessans): § 252 BGB; üblicher Gewinn oder wahrscheinliche Entwicklung
Abzug: Mitverschulden § 254 BGB; Vorteilsausgleichung
```

### Schema 3 — RVG-Gebühren (Anwalt; live prüfen)

```
Streitwert (§ 2 RVG) → Gebührentabelle (Anlage 2 RVG)
Geschäftsgebühr (Nr. 2300 RVG VV): 0,5–2,5; Regelgebühr 1,3
Verfahrensgebühr (Nr. 3100 RVG VV): 1,3
Terminsgebühr (Nr. 3104 RVG VV): 1,2
Einigungsgebühr (Nr. 1000, 1003 RVG VV): 1,5
Hinweis: RVG-Tabellen und Gebührensätze live prüfen unter gesetze-im-internet.de (RVG Anlage 2)
```

## Streitwertberechnung

- Leistungsklage: Streitwert = Klageforderung
- Feststellungsklage: Abschlag (BGH: ca. 20–80% des bezifferbaren Hauptanspruchs; live prüfen)
- Räumungsklage: Jahresmiete (§ 9 ZPO)
- Unterlassungsklage: Gesamtinteresse des Klägers; kein starrer Schematismus

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rechtsfolge soll berechnet werden (Schadensersatz, Zinsen, Bußgeld, Gebühren)?
2. Welche Zahlen und Daten liegen vor (Hauptforderung, Frist, Basiszinssatz)?
3. Gibt es behördliche Festsetzungen oder Schätzgrundlagen?
4. Welche Dokumente, Rechnungen oder Tabellen belegen die Zahlen?
5. Welcher Output wird gebraucht: Berechnung im Schriftsatz, Mandanteninfo, Tabelle?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Zahlen-Grundlage in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen für Rechtsfolge und Berechnung prüfen.
3. **Prüfpunkte abarbeiten:** Welche Beträge sind gesichert? Welche müssen live geprüft werden?
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.


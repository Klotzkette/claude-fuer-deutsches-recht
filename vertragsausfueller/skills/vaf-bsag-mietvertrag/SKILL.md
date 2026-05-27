---
name: vaf-bsag-mietvertrag
description: "BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB Schriftformerfordernis. Pruefraster BSAG-Handelsregisterpruefung, Term Sheet vollständig Fläche Nutzungsart Miete Laufzeit, USt-Option Vorsteuerabzug, Konkurrenzschutzklausel. Output ausgefüllter BSAG-Mietvertragsentwurf mit Lückenmarkierung und Klauselentscheidungen. Abgrenzung zu allgemeinem Kommandocenter und zu Template-Erkennung."
---

# BSAG-Mietvertrag


## Triage zu Beginn

1. Ist die BSAG als Vermieterin im Handelsregister eingetragen und ist die Vertretung aktuell?
2. Liegt das Term Sheet Huckelriede vollständig vor (Fläche, Nutzungsart, Miete, Laufzeit)?
3. Gibt es USt-Option (§ 9 UStG) — ist BSAG als Vermieter zum Vorsteuerabzug berechtigt?
4. Soll eine Konkurrenzschutzklausel aufgenommen werden und welchen Umfang?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 03.03.2010 - XII ZR 131/08, NJW 2010, 1663 — Gewerbemiete Konkurrenzschutz: Vermieter schuldet im Gewerbemietvertrag ohne ausdrückliche Klausel nur eingeschränkten Konkurrenzschutz; eindeutige Vereinbarung nötig.
- BGH, Urt. v. 02.11.2005 - XII ZR 233/03, NJW 2006, 1198 — Betriebspflicht in Gewerbemietverträgen: ausdrückliche Vereinbarung nötig; stillschweigende Betriebspflicht nur in Ausnahmefällen.
- BGH, Urt. v. 25.04.2018 - VIII ZR 176/17, NJW 2018, 2113 — Indexklausel muss transparenten Berechnungsmaßstab enthalten; Verweis auf VPI ausreichend.
- BGH, Urt. v. 18.09.2013 - XII ZR 58/11, NJW 2014, 54 — Schriftformheilung nach § 550 BGB: Nachtrags-Vereinbarungen ohne Schriftform können bei langfristigen Verträgen zur Kündbarkeit führen.

## Zentrale Normen

- § 535, 536 BGB — Miete und Mängelgewährleistung
- § 550 BGB — Schriftformerfordernis bei Mietdauer > 1 Jahr
- § 578 BGB — Gewerbemietrecht (entsprechende Anwendung)
- § 9 UStG — Option zur Umsatzsteuer (wichtig für BSAG-Mietvertrag)
- § 305 ff. BGB — AGB-Kontrolle gewerblicher Klauseln

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. 2022, § 535 Rn. 50-100 (Gewerbemietvertrag)
- Staudinger/Emmerich, BGB, 2021, § 550 Rn. 1-30 (Schriftformheilung)
- MüKo-BGB/Häublein, 9. Aufl. 2022, § 578 Rn. 1-20 (Gewerberaum)

## Aufgabe

Der Skill setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. BSAG-Stammdaten als feste Vermieterdaten übernehmen.
2. Mieter, Mietobjekt, Fläche, Nutzung, Miete, Nebenkosten, Kaution, Laufzeit, Option, Indexierung, Öffnungszeiten und Sonderbedingungen mappen.
3. Sonderpunkte wie Konkurrenzschutz, Fettabscheider, Sauberhaltung, Sortiment, Werbung und Rückbau als Klauselentscheidungen abfragen.
4. Clean-Entwurf, Ausfüllprotokoll und auf Wunsch nach Rückfrage Redline-Fassung vorbereiten.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

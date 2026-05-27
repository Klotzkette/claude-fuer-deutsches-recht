---
name: vaf-feldinventar
description: "Feldinventar für Vertragsgenerator erstellen: Anwendungsfall Anwalt oder Mandant will wissen welche Felder im Vertrag auszufüllen sind bevor Rückfrageninterview startet. §§ 550 BGB Schriftformerfordernis Mietvertrag, § 2 NachwG Arbeitsvertrag Pflichtfelder. Pruefraster Pflichtfelder nach Gesetz, optionale Felder, Quellen für Werte, bedingte Felder für Sonderoptionen, Risikofelder ohne Default. Output Feldinventar-Tabelle mit Feldname, Pflicht/Optional, Quelle und Risikohinweis. Abgrenzung zu Template-Erkennung und zu Rückfrageninterview."
---

# Feldinventar


## Triage zu Beginn

1. Welcher Vertragstyp liegt vor — Kauf, Miete, Werk, Dienstleistung, Lizenz?
2. Gibt es Pflichtfelder nach Gesetz (z.B. § 550 BGB Schriftform, § 2 NachwG bei Arbeitsvertrag)?
3. Welche Felder kommen aus dem Term Sheet direkt — welche müssen erfragt werden?
4. Sind Felder vorhanden, die nur bei bestimmten Vertragsoptionen relevant sind (bedingte Felder)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 14.07.2004 - VIII ZR 163/03, NJW 2004, 2884 — Wesentliche Vertragsbestandteile (essentialia negotii): Vertrag kommt nur zustande, wenn Parteien, Gegenstand und Entgelt hinreichend bestimmt sind.
- BGH, Urt. v. 08.03.1994 - VI ZR 16/93, NJW 1994, 1529 — Formerfordernisse: Fehlen gesetzlich vorgeschriebener Formfelder (z.B. Schriftform § 126 BGB) führt zur Nichtigkeit.
- BGH, Urt. v. 15.10.2008 - VIII ZR 235/07, NJW 2009, 575 — AGB: Blankofelder im Vertragsformular sind kein Hindernis für die Wirksamkeit des Vertrags, wenn der ausgefüllte Teil eindeutig ist.
- BGH, Urt. v. 29.10.2019 - II ZR 211/18, NJW 2020, 461 — Bestimmtheitsgrundsatz: Gesellschaftsvertragsklauseln müssen so bestimmt sein, dass die Rechtsfolge ohne weiteres Ermessen feststellbar ist.

## Zentrale Normen

- §§ 145, 150 BGB — Angebot und Annahme (essentialia negotii)
- § 126 BGB — Schriftform
- § 550 BGB — Schriftform bei langfristiger Miete
- § 2 NachwG — Mindestinhalt Arbeitsvertrag
- § 481 ff. BGB — Verbrauchsgüterkauf (Pflichtangaben)

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, §§ 145-150 Rn. 1-30 (Vertragsschluss)
- MüKo-BGB/Armbrüster, 9. Aufl. 2022, § 126 Rn. 1-25 (Schriftform)

## Aufgabe

Der Skill baut die zentrale Datenmatrix für den Vertrag. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Alle Platzhalter und erkannten Variablen als Tabelle erfassen.
2. Pflichtfelder, optionale Felder, abgeleitete Werte und juristische Prüfwerte trennen.
3. Konflikte zwischen Vorlage, Altvertrag und Term Sheet markieren.
4. Ein Feld erst als freigegeben behandeln, wenn Wert, Quelle und Plausibilität klar sind.

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

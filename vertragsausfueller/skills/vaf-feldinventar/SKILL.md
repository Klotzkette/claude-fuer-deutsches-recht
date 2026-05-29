---
name: vaf-feldinventar
description: "Feldinventar für Vertragsgenerator erstellen: Anwendungsfall Anwalt oder Mandant will wissen welche Felder im Vertrag auszufüllen sind bevor Rückfrageninterview startet. §§ 550 BGB Schriftformerfordernis Mietvertrag, § 2 NachwG Arbeitsvertrag Pflichtfelder. Prüfraster Pflichtfelder nach Gesetz, optionale Felder, Quellen für Werte, bedingte Felder für Sonderoptionen, Risikofelder ohne Default. Output Feldinventar-Tabelle mit Feldname, Pflicht/Optional, Quelle und Risikohinweis. Abgrenzung zu Template-Erkennung und zu Rückfrageninterview."
---

# Feldinventar


## Triage zu Beginn

1. Welcher Vertragstyp liegt vor — Kauf, Miete, Werk, Dienstleistung, Lizenz?
2. Gibt es Pflichtfelder nach Gesetz (z.B. § 550 BGB Schriftform, § 2 NachwG bei Arbeitsvertrag)?
3. Welche Felder kommen aus dem Term Sheet direkt — welche müssen erfragt werden?
4. Sind Felder vorhanden, die nur bei bestimmten Vertragsoptionen relevant sind (bedingte Felder)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 145, 150 BGB — Angebot und Annahme (essentialia negotii)
- § 126 BGB — Schriftform
- § 550 BGB — Schriftform bei langfristiger Miete
- § 2 NachwG — Mindestinhalt Arbeitsvertrag
- § 481 ff. BGB — Verbrauchsgüterkauf (Pflichtangaben)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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


---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

Dieser Skill wurde im Rahmen von Bundle 046 auf halluzinierte Rechtsprechungsnachweise geprüft und korrigiert.
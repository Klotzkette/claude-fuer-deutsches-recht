---
name: vaf-rueckfrageninterview
description: "Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene Pflichtfelder nach Priorität sortieren, Freitext oder Tabellen-Eingabe anbieten, Platzhalter-Schnellversion bei Zeitdruck, Teilantworten aus vorhandenen Dokumenten verwerten. Output vollständig ausgefülltes Feldinventar oder Schnell-Entwurf mit markierten Platzhaltern. Abgrenzung zu Feldinventar für Vorbereitung und zu Kommandocenter."
---

# Rückfrageninterview


## Triage zu Beginn

1. Welche Felder sind noch offen — Pflichtfelder oder optionale Felder?
2. Sind die Rückfragen nach Priorität geordnet (Parteien, Gegenstand, Preis, Frist, Risiko)?
3. Hat der Mandant Zeit für ein ausführliches Interview oder soll ein Schnell-Entwurf mit Platzhaltern erstellt werden?
4. Gibt es bereits Dokumente (E-Mail, Term Sheet) die Teilantworten enthalten?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 280 BGB — Schadensersatz wegen Pflichtverletzung (Beratungshaftung)
- §§ 675, 611 BGB — Anwaltsvertrag (Dienstvertrag mit Geschäftsbesorgung)
- § 3 BRAO — Anwalt als unabhängiger Berater

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill füllt Datenlücken ohne den Nutzer zu überfordern. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Maximal zehn wichtigste Rückfragen zuerst stellen.
2. Fragen nach Parteien, Gegenstand, Geld, Frist, Risiko und Anlagen gruppieren.
3. Unbekannte Werte als Platzhalter mit Warnung stehen lassen, wenn der Nutzer schnell einen Entwurf will.
4. Nach jeder Antwort aktualisieren, welche Felder nun freigegeben sind.

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

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 394/12 (claimed: Verlaesslichkeit von Auskuenften, NJW 2014, 2360): NOT_FOUND auf dejure.org. NJW 2014, 2360 gehoert zu BGH I ZR 169/12 (BearShare – Filesharing-Stoererhaftung) – thematisch unverwandt. Eintrag geloescht. -->

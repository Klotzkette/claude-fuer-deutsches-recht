---
name: vaf-rueckfrageninterview
description: "Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Pruefraster offene Pflichtfelder nach Priorität sortieren, Freitext oder Tabellen-Eingabe anbieten, Platzhalter-Schnellversion bei Zeitdruck, Teilantworten aus vorhandenen Dokumenten verwerten. Output vollständig ausgefülltes Feldinventar oder Schnell-Entwurf mit markierten Platzhaltern. Abgrenzung zu Feldinventar fuer Vorbereitung und zu Kommandocenter."
---

# Rückfrageninterview


## Triage zu Beginn

1. Welche Felder sind noch offen — Pflichtfelder oder optionale Felder?
2. Sind die Rückfragen nach Priorität geordnet (Parteien, Gegenstand, Preis, Frist, Risiko)?
3. Hat der Mandant Zeit für ein ausführliches Interview oder soll ein Schnell-Entwurf mit Platzhaltern erstellt werden?
4. Gibt es bereits Dokumente (E-Mail, Term Sheet) die Teilantworten enthalten?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 21.02.2017 - XI ZR 185/16, NJW 2017, 1823 — Aufklärungspflicht des Beraters: fehlende Information über wesentliche Vertragsbestandteile kann Schadensersatzpflicht auslösen (§ 280 Abs. 1 BGB).
- BGH, Urt. v. 15.04.2010 - IX ZR 189/09, NJW 2010, 1830 — Anwaltliche Beratungspflicht: Anwalt muss alle Informationen einholen, die für eine korrekte rechtliche Beratung erforderlich sind; andernfalls Haftung nach § 280 BGB.
- BGH, Urt. v. 03.06.2014 - VI ZR 394/12, NJW 2014, 2360 — Verlässlichkeit von Auskünften: Bei unvollständigen Angaben des Mandanten kann Berater nicht haftbar sein, wenn er auf Grundlage der gegebenen Informationen korrekt gehandelt hat.
- BGH, Urt. v. 13.03.2008 - IX ZR 136/07, NJW 2008, 2037 — Dokumentation der Beratung: Rückfragen und Antworten müssen für Haftungszwecke dokumentiert werden.

## Zentrale Normen

- § 280 BGB — Schadensersatz wegen Pflichtverletzung (Beratungshaftung)
- §§ 675, 611 BGB — Anwaltsvertrag (Dienstvertrag mit Geschäftsbesorgung)
- § 3 BRAO — Anwalt als unabhängiger Berater

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 280 Rn. 1-30 (Schadensersatz Beraterhaftung)
- Henssler/Prütting, BRAO, 5. Aufl. 2019, § 3 Rn. 1-20 (anwaltliche Pflichten)

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

---
name: vaf-kommandocenter
description: "Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen Workflow. Vertragsrecht §§ 145 ff. BGB, § 3a RVG Vergütung. Pruefraster Eingabedokument-Typ erkennen, Ausgabeziel Clean-Entwurf oder Redline klären, Track-Changes-Bestätigung einholen, Vertragstyp bestimmen. Output Deal-Start-Karte mit Weiterleitung zum Spezial-Skill. Abgrenzung zu Template-Erkennung fuer Vorlage-Analyse und zu Rückfrageninterview."
---

# Kommandocenter


## Triage zu Beginn

1. Was ist das Eingabedokument — Word-Vorlage, Altvertrag, Term Sheet, E-Mail oder Freitext?
2. Was ist das Ausgabeziel — Clean-Entwurf, Redline, Track Changes oder nur Ausfüllprotokoll?
3. Soll ein bestehender Vertrag ergänzt oder ein neuer erstellt werden?
4. Welche Parteien und welcher Vertragstyp (Kauf, Miete, Werk, Dienstleistung)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 07.06.1978 - VIII ZR 84/77, NJW 1978, 1858 — Vertragsabschluss durch konkludentes Handeln: Kontrolle über den Vertragsinhalt beginnt mit dem ersten Austausch von Klauseln.
- BGH, Urt. v. 20.01.1983 - VII ZR 105/81, NJW 1985, 1838 — Knock-out-Doktrin bei kollidierenden AGB: dispositives Recht tritt an die Stelle weggefallener Klauseln.
- BGH, Urt. v. 25.09.2018 - VIII ZR 36/17, NJW 2019, 434 — Vertragsschluss per E-Mail mit AGB-Bezugnahme: wirksam, wenn Empfänger hinreichend auf AGB hingewiesen wurde und Kenntnisnahme möglich war.
- BGH, Urt. v. 14.04.2005 - IX ZR 148/03, NJW 2005, 2086 — Vollmacht zur Vertragsunterzeichnung muss vor Unterzeichnung vorliegen; nachträgliche Genehmigung nach § 177 BGB möglich.

## Zentrale Normen

- §§ 145 ff. BGB — Vertragsschluss (Angebot und Annahme)
- § 167 ff. BGB — Vollmacht (Vertretungsbefugnis prüfen)
- § 305 BGB — AGB-Einbeziehung
- § 177 BGB — Genehmigung schwebend unwirksamer Verträge

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, §§ 145-157 Rn. 1-50 (Vertragsschluss und Auslegung)
- MüKo-BGB/Schubert, 9. Aufl. 2022, § 167 Rn. 1-40 (Vollmacht)

## Aufgabe

Der Skill steuert den gesamten Workflow von Upload bis neuem Vertragsentwurf. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Eingänge trennen: Vorlage, Altvertrag, Term Sheet, handschriftliche Notizen, E-Mail und Datenliste.
2. Ausgabeziel klären: neuer Clean-Vertrag, Ausfüllprotokoll, Rückfragenliste, Redline oder Track-Changes-Fassung.
3. Vor jeder Redline- oder Track-Changes-Ausgabe ausdrücklich fragen und ohne Bestätigung nur Clean-Entwurf oder Änderungsprotokoll erstellen.
4. Nächste Schritte nach Risiko, Datenlücken und Dokumentqualität priorisieren.

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

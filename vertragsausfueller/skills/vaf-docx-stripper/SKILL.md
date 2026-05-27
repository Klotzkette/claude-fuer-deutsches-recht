---
name: vaf-docx-stripper
description: "DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstruktur, Schriftform-Erfordernisse. Pruefraster DOCX-Zustand prüfen passwortgeschützt oder beschädigt, Track-Changes sichtbar machen, Platzhalter-Typen erkennen, Tabellenstruktur extrahieren. Output strukturiertes Dokumentinventar mit Klausel-Index und Platzhalter-Liste. Abgrenzung zu Template-Erkennung fuer Vertragstyp-Erkennung und zu Feldinventar."
---

# DOCX-Stripper


## Triage zu Beginn

1. Ist das DOCX vollständig abrufbar oder beschädigt/passwortgeschützt?
2. Enthält das Dokument Track-Changes-Markierungen die berücksichtigt werden müssen?
3. Gibt es strukturierte Platzhalter (eckige Klammern, XXX, TBD) oder nur unstrukturierte Freitextfelder?
4. Sind Tabellen vorhanden die als Feldinventar extrahiert werden sollen?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 15.11.2006 - VIII ZR 166/06, NJW 2007, 674 — Vertragsinhalt bestimmt sich nach dem Wortlaut der schriftlichen Urkunde; bei Widersprüchen zwischen Text und Anlagen gilt der Haupttext.
- BGH, Urt. v. 14.01.2010 - VII ZR 213/07, NJW 2010, 1283 — Urkunde ist auszulegen nach ihrem objektiven Erklärungsinhalt; späteres Verhalten der Parteien als Auslegungshilfe.
- BGH, Urt. v. 22.02.2018 - VII ZR 46/17, NJW 2018, 1706 — Vertragsauslegung bei widersprüchlichen AGB-Klauseln: Spezialklausel geht Generalklausel vor.
- BGH, Urt. v. 05.12.2019 - IX ZR 189/18, NJW 2020, 673 — Integrationsklausel ("dieser Vertrag enthält alle Vereinbarungen") schließt Einbeziehung vorvertraglicher E-Mails aus.

## Zentrale Normen

- §§ 133, 157 BGB — Vertragsauslegung (Auslegung nach Treu und Glauben)
- § 305c Abs. 2 BGB — Unklarheitenregel (gilt für Platzhalter-Auslegung)
- § 416 ZPO — Beweiskraft von Privaturkunden

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 133 Rn. 1-30 (Auslegung)
- MüKo-BGB/Busche, 9. Aufl. 2022, § 157 Rn. 1-40 (Vertragsauslegung)

## Aufgabe

Der Skill macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Absätze, Überschriften, Listen, Tabellen, Fußnoten, Platzhalter und Anlagenhinweise extrahieren.
2. Platzhalter in eckigen Klammern, leere Linien, wiederkehrende Begriffe und Optionsklauseln erkennen.
3. Originaldatei unangetastet lassen und jeden Extrakt mit Dateiname, Stand und Quelle kennzeichnen.
4. Bei beschädigten oder gescannten Dateien einen OCR- oder manuellen Nachfasspfad anbieten.

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

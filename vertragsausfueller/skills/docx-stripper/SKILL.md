---
name: docx-stripper
description: "DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstruktur, Schriftform-Erfordernisse. Prüfraster DOCX-Zustand pr..."
---

# DOCX-Stripper

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Ist das DOCX vollständig abrufbar oder beschädigt/passwortgeschützt?
2. Enthält das Dokument Track-Changes-Markierungen die berücksichtigt werden müssen?
3. Gibt es strukturierte Platzhalter (eckige Klammern, XXX, TBD) oder nur unstrukturierte Freitextfelder?
4. Sind Tabellen vorhanden die als Feldinventar extrahiert werden sollen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 133, 157 BGB — Vertragsauslegung (Auslegung nach Treu und Glauben)
- § 305c Abs. 2 BGB — Unklarheitenregel (gilt für Platzhalter-Auslegung)
- § 416 ZPO — Beweiskraft von Privaturkunden

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

<!-- AUDIT 27.05.2026: BGH VII ZR 213/07 (14.01.2010) WRONG_TOPIC – tatsächliches Thema ist Verjährung der Rückforderung von Mangelbeseitigungsvorschüssen, NJW 2010, 1195 (nicht Urkundenauslegung, nicht NJW 2010, 1283). Verifiziert auf dejure.org (https://dejure.org/2010,781). Eintrag korrigiert. -->

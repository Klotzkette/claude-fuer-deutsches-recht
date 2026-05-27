---
name: vaf-redline-qa
description: "Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollstaendigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft werden. §§ 145 ff. BGB Vertragsänderungen, §§ 305 ff. BGB AGB-Änderungskontrolle. Pruefraster Ausgangsfassung und überarbeitete Fassung identifiziert, alle Track-Changes-Status klar, materielle Änderungen gegen Freigaben geprüft. Output QA-Protokoll mit Änderungsübersicht und offenen Klauselentscheidungen. Abgrenzung zu Clean-Output und zu Klauselentscheidung."
---

# Redline-QA


## Triage zu Beginn

1. Welche Fassung ist Ausgangsdokument und welche ist die überarbeitete Fassung?
2. Sind alle Track-Changes-Markierungen angenommen oder abgelehnt oder noch ausstehend?
3. Entsprechen alle materiellen Änderungen freigegebenen Klauselentscheidungen?
4. Hat der Mandant die Herausgabe der Redline ausdrücklich bestätigt?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 19.07.2018 - I ZR 268/15, NJW 2018, 3178 — Vertragsverhandlungen per Redline begründen grundsätzlich kein culpa in contrahendo; aber verdeckte Änderungen können Pflichtverletzung nach § 280 Abs. 1 BGB sein.
- BGH, Urt. v. 18.09.2019 - VIII ZR 188/18, NJW 2020, 142 — Änderungsvorbehalt: Klausel die einseitige Änderungen erlaubt, muss transparent sein (§ 307 BGB); stillen Änderungen fehlt die Grundlage.
- BGH, Urt. v. 07.11.2017 - KZR 38/16, NJW 2018, 1461 — Gegenseite muss über wesentliche Vertragsänderungen in Kenntnis gesetzt werden; andernfalls kann das Vertragsverhältnis nach § 122 BGB anfechtbar sein.
- BGH, Urt. v. 10.12.2008 - XII ZR 22/07, NJW 2009, 1272 — Bei Formularverträgen sind alle Seiten einzubeziehen, die übergebenen Anlagen gelten als Teil des Vertrags.

## Zentrale Normen

- § 119 ff. BGB — Anfechtung (bei verdeckten Änderungen im Redline-Prozess)
- § 241 Abs. 2 BGB — Nebenpflicht zur Rücksichtnahme (kein Einbringen unbesprochener Änderungen)
- § 307 BGB — Transparenzgebot (bei Änderungen per AGB)

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 241 Rn. 5-15 (Nebenpflichten)
- MüKo-BGB/Roth, 9. Aufl. 2022, § 119 Rn. 1-30 (Anfechtung wegen Irrtums)

## Aufgabe

Der Skill kontrolliert Änderungsfassungen vor Herausgabe. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Jede Änderung einem Feld, einer Rückfrage oder einer Klauselentscheidung zuordnen.
2. Formatbrüche, doppelte Leerzeichen, zerstörte Nummerierung und Anlagenverweise prüfen.
3. Materielle Abweichungen vom Term Sheet separat hervorheben.
4. Freigabe erst empfehlen, wenn Clean- und Redline-Fassung denselben Stand haben.

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

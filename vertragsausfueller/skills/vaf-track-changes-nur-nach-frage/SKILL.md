---
name: vaf-track-changes-nur-nach-frage
description: "Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhandlung, §§ 305 ff. BGB AGB-Transparenz. Pruefraster ausdrückliche Bestätigung vorhanden, saubere Ausgangsfassung nach Quality Gate vorhanden, Ausgangspunkt für Änderungsmarkierung definiert, Kommentierung materiell relevanter Änderungen. Output Track-Changes-Fassung oder ablehnende Weiterleitung zu Clean-Output. Abgrenzung zu Redline-QA fuer Prüfung und zu Clean-Output."
---

# Track Changes nur nach Frage


## Triage zu Beginn

1. Hat der Nutzer ausdrücklich (und mit "Ja" bestätigt) eine Track-Changes- oder Redline-Fassung gewünscht?
2. Liegt eine saubere Ausgangsfassung vor (Clean-Entwurf nach Quality Gate)?
3. Ist klar, welche Version als Ausgangspunkt für die Änderungsmarkierungen dient?
4. Sollen alle Änderungen kommentiert werden oder nur materiell relevante?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 19.07.2018 - I ZR 268/15, NJW 2018, 3178 — Verdeckte Änderungen in Vertragsverhandlungen können Pflichtverletzung nach § 241 Abs. 2 BGB darstellen; Transparenzpflicht bei Änderungen.
- BGH, Urt. v. 07.11.2017 - KZR 38/16, NJW 2018, 1461 — Pflicht zur Offenlegung wesentlicher Änderungen; Schweigen über materiell bedeutsame Änderungen kann arglistig im Sinne des § 123 BGB sein.
- BGH, Urt. v. 10.12.2008 - XII ZR 22/07, NJW 2009, 1272 — Vollständigkeit der Vertragsdokumentation: alle Anlagen und Änderungen müssen dem finalen Vertrag klar zugeordnet sein.
- BVerfG, Beschl. v. 12.05.2010 - 1 BvR 1098/09, NJW 2010, 2194 — Anwaltliches Berufsrecht: Anwalt muss Mandanten vollständig und wahrheitsgemäß über den Vertragsinhalt informieren.

## Zentrale Normen

- § 241 Abs. 2 BGB — Rücksichtnahmepflicht (Transparenz in Vertragsverhandlungen)
- § 123 BGB — Anfechtung wegen Täuschung (bei verdeckten Änderungen)
- § 3 BRAO — anwaltliche Sorgfaltspflicht

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 241 Rn. 5-15 (Nebenpflichten im Schuldverhältnis)
- Henssler/Prütting, BRAO, 5. Aufl. 2019, § 3 Rn. 1-20 (anwaltliche Pflichten)

## Aufgabe

Der Skill setzt die ausdrückliche Nachfragepflicht durch. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Immer fragen: Soll ich zusätzlich eine Track-Changes- oder Redline-Fassung erstellen?
2. Ohne Ja keine Änderungsfassung erzeugen.
3. Bei Ja Ausgangsdokument, Zielentwurf und Änderungslog trennen.
4. Änderungen erklärbar halten und keine verdeckten materiellen Änderungen einbauen.

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

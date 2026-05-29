---
name: vaf-track-changes-nur-nach-frage
description: "Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhandlung, §§ 305 ff. BGB AGB-Transparenz. Prüfraster ausdrückliche Bestätigung vorhanden, saubere Ausgangsfassung nach Quality Gate vorhanden, Ausgangspunkt für Änderungsmarkierung definiert, Kommentierung materiell relevanter Änderungen. Output Track-Changes-Fassung oder ablehnende Weiterleitung zu Clean-Output. Abgrenzung zu Redline-QA für Prüfung und zu Clean-Output."
---

# Track Changes nur nach Frage


## Triage zu Beginn

1. Hat der Nutzer ausdrücklich (und mit "Ja" bestätigt) eine Track-Changes- oder Redline-Fassung gewünscht?
2. Liegt eine saubere Ausgangsfassung vor (Clean-Entwurf nach Quality Gate)?
3. Ist klar, welche Version als Ausgangspunkt für die Änderungsmarkierungen dient?
4. Sollen alle Änderungen kommentiert werden oder nur materiell relevante?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 241 Abs. 2 BGB — Rücksichtnahmepflicht (Transparenz in Vertragsverhandlungen)
- § 123 BGB — Anfechtung wegen Täuschung (bei verdeckten Änderungen)
- § 3 BRAO — anwaltliche Sorgfaltspflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

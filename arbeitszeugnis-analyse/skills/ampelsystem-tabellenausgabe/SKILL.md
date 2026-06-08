---
name: ampelsystem-tabellenausgabe
description: "Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und Begründung dargestellt werden. Vereinheitlicht Output aller Analyse-Skills für Mandantenbericht und Klagebegründung. Output strukturierte Ampeltabelle als Grundlage für mandantenbericht-zeugnisanalyse und klage-strategie-zeugnisberichtigung."
---

# Ampelsystem-Tabellenausgabe

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Element | Ampel-Zuordnung |
|---|---|
| Note 1-Formel vorhanden | Grün |
| Note 2-Formel vorhanden | Grün |
| Note 3-Formel vorhanden | Orange |
| Note 4-Formel vorhanden | Rot |
| Note 5-Formel vorhanden | Rot |
| Gemischter Satz (grün + orange) | Orange gesamt |
| Gemischter Satz (grün + rot) | Rot gesamt |
| Fehlende Pflichtaussage | Rot |

## Beispiele

**Beispiel 1 – Ausgabe für Note-1-Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "stets zur vollsten Zufriedenheit" | Grün | Note 1 | Stabil | Vollständige Maximalformel |
| "stets einwandfrei" (Verhalten) | Grün | Note 1 | Stabil | Maximale Verhaltensformel |
| Vollständige Schlussformel | Grün | Note 1-2 | Stabil | Alle drei Elemente vorhanden |

**Beispiel 2 – Ausgabe für gemischtes Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "zur vollen Zufriedenheit" | Orange | Note 3 | Abschwächend | Fehlendes "stets" |
| "bemüht" (Leistungsaussage) | Rot | Note 4 | Abwärts | Rotes Signal durch "bemüht" |
| Schlussformel ohne Bedauern | Orange | Note 3 | Abschwächend | Fehlendes Bedauern |

**Beispiel 3 – Gesamtzusammenfassung:** Grüne Sätze: 4 / Orange Sätze: 2 / Rote Sätze: 1 → Gewichtete Gesamtnote: Note 2 bis 3. Empfehlung: Nachverhandlung des roten Satzes und eines orangen Satzes sinnvoll.

## Ausgabeformat

Die Ausgabe umfasst: (1) Übersichtstabelle aller Sätze mit Ampelzuordnung, (2) separate Tabelle der Auslassungen, (3) Ampel-Zusammenfassung (Anzahl je Farbe), (4) Gesamtnoten-Spanne, (5) Handlungsempfehlung (Zeugnis akzeptieren / Nachverhandlung empfehlen / Klage prüfen).

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes Zeugnis; Wohlwollensgebot und Wahrheitspflicht
- **§ 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich formuliert sein; Codierungen, die Fortkommen erschweren, verstoßen gegen Wohlwollensgebot

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — vor der Tabellenausgabe klären

1. Welche Analyse-Skills wurden bereits ausgeführt? (Leistungsbeurteilung, Verhaltensbeurteilung, Schlussformel)
2. Liegt ein vollständiges Zeugnisdokument vor oder nur Auszüge?
3. Ist das Ziel: Mandantenbericht, Klageantrag-Vorbereitung oder interne Einschätzung?

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 16 BBiG
- § 46 ArbGG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG
- § 2 NachwG
- § 42 GKG
- § 29 VwVfG
- § 11 ArbGG
- § 13 BBiG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)


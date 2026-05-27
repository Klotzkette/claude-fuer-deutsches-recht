---
name: notenrelevante-saetze-identifizieren
description: "Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss fuer Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollstaendigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe fuer satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und zeugnisart-erkennung."
---

# Notenrelevante Sätze identifizieren

Nicht jeder Satz in einem Arbeitszeugnis ist für die Benotung relevant. Die Aufgabenbeschreibung — also die Schilderung dessen, womit der Arbeitnehmer befasst war — enthält keine Bewertung und ist für die Notenbildung neutral. Erst wenn ein Satz eine Aussage über die Qualität der Aufgabenerfüllung trifft, wird er notenrelevant.

Die vier Hauptkategorien sind: (1) Aufgabenbeschreibung (neutral, deskriptiv), (2) Leistungsbeurteilung (Arbeitsqualität, Arbeitsbereitschaft, Arbeitstempo, Arbeitsmenge, Fachkenntnisse), (3) Verhaltensbeurteilung (soziales Verhalten zu Vorgesetzten, Kollegen, Kunden, Lieferanten) und (4) Schlussformel (Bedauern, Dank, Zukunftswünsche). Die Kategorien (2) bis (4) sind notenrelevant und werden im Ampelsystem bewertet.

Ein besonderer Grenzfall ist die verkürzte Aufgabenbeschreibung: Wenn ein Zeugnis die Aufgaben sehr kurz beschreibt und damit signalisiert, dass der Arbeitnehmer nur geringe Verantwortung hatte — obwohl seine tatsächliche Stellung höher war — kann das ein implizites Abwertungssignal sein. Ebenso ist eine übertrieben lange Aufgabenbeschreibung bei gleichzeitig knapper Leistungsbeurteilung ein Hinweis darauf, dass der Aussteller das Positive bewusst minimiert.

Besondere Aufmerksamkeit verdienen Sätze, die scheinbar deskriptiv sind, aber Bewertungen einschließen. „Er war stets bereit, Überstunden zu leisten" klingt nach Beschreibung, ist aber eine Leistungsaussage über Einsatzbereitschaft. „Sie bearbeitete sämtliche Aufgaben eigenverantwortlich" beschreibt Arbeitsweise und ist eine verdeckte Leistungsbeurteilung.

## Geheimcode-Regeln

| Satztyp | Notenrelevant? | Ampel-Analyse |
|---|---|---|
| Aufgabenbeschreibung (rein deskriptiv) | Nein | Keine Ampelzuordnung |
| Leistungsaussage mit Qualitätsmerkmal | Ja | Ampel nach Formulierung |
| Verhaltensaussage zu Dritten | Ja | Ampel nach Formulierung und Reihenfolge |
| Schlussformel (Dank, Bedauern, Wünsche) | Ja | Ampel nach Vollständigkeit |
| Satz mit impliziter Bewertung | Ja | Ampel nach Gesamttendenz |
| Kurze Aufgabenbeschreibung trotz hoher Stellung | Grenzfall | Orange |

## Beispiele

**Beispiel 1 – Rein deskriptiv (nicht notenrelevant):** „Frau Weber war in unserem Haus als Projektmanagerin tätig und verantwortete die Koordination externer Dienstleister." — Keine Qualitätsaussage.

**Beispiel 2 – Leistungsbeurteilung (notenrelevant):** „Sie erledigte alle ihr übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit." — Kernbeurteilungssatz, Note 1, Grün.

**Beispiel 3 – Verhaltensbeurteilung (notenrelevant):** „Ihr Verhalten gegenüber Vorgesetzten und Kollegen war einwandfrei." — Reihenfolge und Qualifikationswort bestimmen Ampelfarbe.

**Beispiel 4 – Implizite Bewertung (notenrelevant):** „Herr Schmidt war stets bemüht, seine Aufgaben pünktlich abzuliefern." — Scheinbar positiv, tatsächlich rotes Signal durch „bemüht".

**Beispiel 5 – Schlussformel (notenrelevant):** Fehlen des Bedauerns über das Ausscheiden — rotes Signal trotz positiver Leistungsformulierungen.

## Ausgabeformat

Jeder Satz des Zeugnisses wird in einer Tabelle klassifiziert: Satz (Kurzform) | Kategorie (Aufgabe/Leistung/Verhalten/Schluss) | Notenrelevant (Ja/Nein) | Weitergeleitet an Skill (z. B. leistungsbeurteilung-analyse). Notenrelevante Sätze werden im Anschluss an die zuständigen Analyse-Skills weitergegeben.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- **BAG, Urt. v. 18.11.2014 — 9 AZR 584/13**, NZA 2015, 345 — Beweislastverteilung: Note schlechter als befriedigend beweist Arbeitgeber; Note besser als befriedigend beweist Arbeitnehmer; diese Verteilung gilt für alle notenrelevanten Bestandteile.
- **BAG, Urt. v. 12.08.2008 — 9 AZR 632/07**, BAGE 127, 232 — Wohlwollensgebot: Arbeitgeber muss Formulierungen wählen, die Fortkommen nicht unnötig erschweren; Berichtigungsanspruch bei Verstoß.

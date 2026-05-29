---
name: notenrelevante-saetze-identifizieren
description: "Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollständigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe für satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und zeugnisart-erkennung."
---

# Notenrelevante Sätze identifizieren

Nicht jeder Satz in einem Arbeitszeugnis ist für die Benotung relevant. Die Aufgabenbeschreibung — also die Schilderung dessen, womit der Arbeitnehmer befasst war — enthält keine Bewertung und ist für die Notenbildung neutral. Erst wenn ein Satz eine Aussage über die Qualität der Aufgabenerfüllung trifft, wird er notenrelevant.

Die vier Hauptkategorien sind: (1) Aufgabenbeschreibung (neutral, deskriptiv), (2) Leistungsbeurteilung (Arbeitsqualität, Arbeitsbereitschaft, Arbeitstempo, Arbeitsmenge, Fachkenntnisse), (3) Verhaltensbeurteilung (soziales Verhalten zu Vorgesetzten, Kollegen, Kunden, Lieferanten) und (4) Schlussformel (Bedauern, Dank, Zukunftswünsche). Leistungs- und Verhaltenssätze sind regelmäßig notenrelevant. Die Schlussformel wird als Signal bewertet, rechtlich aber gesondert behandelt.

Ein besonderer Grenzfall ist die verkürzte Aufgabenbeschreibung: Wenn ein Zeugnis die Aufgaben sehr kurz beschreibt und damit signalisiert, dass der Arbeitnehmer nur geringe Verantwortung hatte — obwohl seine tatsächliche Stellung höher war — kann das ein implizites Abwertungssignal sein. Ebenso ist eine übertrieben lange Aufgabenbeschreibung bei gleichzeitig knapper Leistungsbeurteilung ein Hinweis darauf, dass der Aussteller das Positive bewusst minimiert.

Besondere Aufmerksamkeit verdienen Sätze, die scheinbar deskriptiv sind, aber Bewertungen einschließen. "Er war stets bereit, Überstunden zu leisten" klingt nach Beschreibung, ist aber eine Leistungsaussage über Einsatzbereitschaft. "Sie bearbeitete sämtliche Aufgaben eigenverantwortlich" beschreibt Arbeitsweise und ist eine verdeckte Leistungsbeurteilung.

## Geheimcode-Regeln

| Satztyp | Notenrelevant? | Ampel-Analyse |
|---|---|---|
| Aufgabenbeschreibung (rein deskriptiv) | Nein | Keine Ampelzuordnung |
| Leistungsaussage mit Qualitätsmerkmal | Ja | Ampel nach Formulierung |
| Verhaltensaussage zu Dritten | Ja | Ampel nach Formulierung und Reihenfolge |
| Schlussformel (Dank, Bedauern, Wünsche) | Signalrelevant | Ampel nach Ton; Anspruch gesondert prüfen |
| Satz mit impliziter Bewertung | Ja | Ampel nach Gesamttendenz |
| Kurze Aufgabenbeschreibung trotz hoher Stellung | Grenzfall | Orange |

## Beispiele

**Beispiel 1 – Rein deskriptiv (nicht notenrelevant):** "Frau Weber war in unserem Haus als Projektmanagerin tätig und verantwortete die Koordination externer Dienstleister." — Keine Qualitätsaussage.

**Beispiel 2 – Leistungsbeurteilung (notenrelevant):** "Sie erledigte alle ihr übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit." — Kernbeurteilungssatz, Note 1, Grün.

**Beispiel 3 – Verhaltensbeurteilung (notenrelevant):** "Ihr Verhalten gegenüber Vorgesetzten und Kollegen war einwandfrei." — Reihenfolge und Qualifikationswort bestimmen Ampelfarbe.

**Beispiel 4 – Implizite Bewertung (notenrelevant):** "Herr Schmidt war stets bemüht, seine Aufgaben pünktlich abzuliefern." — Scheinbar positiv, tatsächlich rotes Signal durch "bemüht".

**Beispiel 5 – Schlussformel (signalrelevant):** Fehlen des Bedauerns über das Ausscheiden — mögliches Distanzsignal trotz positiver Leistungsformulierungen; rechtlich nicht automatisch einklagbar.

## Ausgabeformat

Jeder Satz des Zeugnisses wird in einer Tabelle klassifiziert: Satz (Kurzform) | Kategorie (Aufgabe/Leistung/Verhalten/Schluss) | Notenrelevant (Ja/Nein) | Weitergeleitet an Skill (z. B. leistungsbeurteilung-analyse). Notenrelevante Sätze werden im Anschluss an die zuständigen Analyse-Skills weitergegeben.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---
name: notenrelevante-saetze-identifizieren
description: "Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollständigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe für satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-überblick-extraktion (Kopfdaten) und zeugnisart-erkennung."
---

# Notenrelevante Sätze identifizieren

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


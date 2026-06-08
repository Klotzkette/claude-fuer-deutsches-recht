---
name: steigerungsadverbien-katalog
description: "Vollständige Referenzliste aller Steigerungsadverbien der Zeugnissprache mit Notenwert. Ein Adverb fehlt, eine Note faellt. Trennt echte Steigerer (stets, jederzeit, vollkommen, hoechst) von scheinbaren Steigerern (regelmäßig, ueberwiegend, weitgehend) und Frequenzadverbien (oft, meist, gelegentlich) und ordnet jede Kombination einer Schulnote zu."
---

# Steigerungsadverbien-Katalog

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

### Echte Maximalsteigerer (Note 1)

| Adverb | Wirkung |
|---|---|
| stets vollster | Maximalformel, Note 1 |
| jederzeit aeusserst | Maximalformel, Note 1 |
| vollkommen | Maximalsteigerer, Note 1 |
| aeusserst | Maximalsteigerer, Note 1 |
| in hoechstem Masse | Maximalsteigerer, Note 1 |
| uneingeschraenkt | Maximalsteigerer, Note 1 |
| absolut | Maximalsteigerer, Note 1 |
| in allen Belangen | Bereichssteigerer, Note 1 |

### Echte Standardsteigerer (Note 1 bis 2)

| Adverb | Wirkung |
|---|---|
| stets | Standardsteigerer, hebt um eine Note |
| jederzeit | Standardsteigerer, hebt um eine Note |
| immer | Standardsteigerer, hebt um eine Note |
| durchgehend | Standardsteigerer, hebt um eine Note |
| zu jeder Zeit | Standardsteigerer, hebt um eine Note |
| ohne Ausnahme | Bereichssteigerer, Note 1 |

### Scheinsteigerer (Note 2 bis 3)

| Adverb | Wirkung |
|---|---|
| regelmaessig | Haeufigkeit, keine Qualitaet, Note 3 |
| im Allgemeinen | Standardlage, Note 3 |
| zumeist | Mehrzahl der Faelle, Note 3 |

### Abschwaecher (Note 3 bis 4)

| Adverb | Wirkung |
|---|---|
| ueberwiegend | Ausnahmen mitgedacht, Note 3 bis 4 |
| weitgehend | Ausnahmen mitgedacht, Note 3 bis 4 |
| grundsaetzlich | Ausnahmen mitgedacht, Note 3 bis 4 |

### Starke Negativsteigerer (Note 4 bis 5)

| Adverb | Wirkung |
|---|---|
| im Wesentlichen | Erhebliche Maengel, Note 4 |
| im Grossen und Ganzen | Erhebliche Maengel, Note 4 |
| bei guten Tagen | Schwankende Leistung, Note 4 bis 5 |

### Frequenzadverbien

| Adverb | Wirkung |
|---|---|
| oft | Haeufig, Note 2 bis 3 |
| meist | Mehrheit, Note 3 |
| haeufig | Wiederholung, Note 3 |
| gelegentlich | Selten, Note 4 |
| bisweilen | Selten, Note 4 bis 5 |

### Auslassungsregel

| Befund | Wirkung |
|---|---|
| Steigerer "stets" im Zeugnis durchgaengig, fehlt an einer Stelle | Punktuelle Abwertung, Drift-Signal |
| Steigerer fehlt vollstaendig im ganzen Zeugnis | Maximalnote nicht erreichbar, Note 2 oder schlechter |

## Beispiele

**Beispiel 1 – Maximalformel:** "Er erledigte alle Aufgaben jederzeit zu unserer vollsten Zufriedenheit" → drei Steigerer ("jederzeit", "vollsten", implizites "alle"), Note 1.

**Beispiel 2 – Standardformel:** "Sie erledigte ihre Aufgaben stets zu unserer Zufriedenheit" → ein Standardsteigerer ohne Maximalsteigerer, Note 2.

**Beispiel 3 – Abgestufte Formel:** "Er erledigte seine Aufgaben zur Zufriedenheit" → kein Steigerer, Note 3.

**Beispiel 4 – Scheinsteigerer:** "Sie nahm regelmaessig erfolgreich an Weiterbildungsseminaren teil" → "regelmaessig" ist Haeufigkeit, kein Qualitaetssteigerer; ohne "stets" oder "mit grossem Erfolg" bleibt die Aussage Note 3.

**Beispiel 5 – Abschwaecher:** "Sein Verhalten war ueberwiegend korrekt" → "ueberwiegend" denkt Ausnahmen mit, "korrekt" ohne Steigerer, Note 4.

**Beispiel 6 – Auslassung als Signal:** Zeugnis enthaelt zehnmal "stets", einmal aber "Sein Verhalten war einwandfrei" ohne "stets" → punktuelle Drift, Sozialverhalten-Note rutscht von 1 auf 2 bis 3.

## Ausgabeformat

Der Skill kann zweifach eingesetzt werden. Erstens als Nachschlagewerk: Eingabe eines Adverbs liefert Notenwirkung und Kategorie (Maximalsteigerer, Standardsteigerer, Scheinsteigerer, Abschwaecher, Negativsteigerer, Frequenzadverb). Zweitens als Analysator: Eingabe eines vollstaendigen Zeugnistexts liefert eine Tabelle mit allen erkannten Adverbien, ihren Positionen, ihren Notenwirkungen und besonderen Auslassungen. Die Ausgabe ist Eingangsbasis für satzweise-notenmatrix und bereichs-drift-detektor.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

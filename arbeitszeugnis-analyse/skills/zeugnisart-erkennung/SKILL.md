---
name: zeugnisart-erkennung
description: "Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen § 109 GewO qualifiziertes vs. einfaches Zeugnis § 16 BBiG Ausbildungszeugnis. Prüfraster Inhalt Zeitbezug Position Stichtag Ausstellungsanlass. Output Zeugnisart-Klassifikation mit Erlauterungen zu Inhalt Erwartungshaltung und Interpretationsrahmen für alle Folge-Skills. Abgrenzung zu zeugnis-überblick-extraktion (Kopfdaten) und notenrelevante-saetze-identifizieren."
---

# Zeugnisart-Erkennung

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Zeugnisart | Mindest- und Erwartungsbausteine | Fehlende Bausteine |
|---|---|---|
| Einfaches Zeugnis | Art und Dauer der Tätigkeit | Keine Leistungsaussage erwartet |
| Qualifiziertes Endzeugnis | Art, Dauer, Leistung, Verhalten, Schlussformel | Rotes Signal |
| Zwischenzeugnis | Art, Dauer, Leistung, Verhalten (Präsens) | Kein Enddatum, keine Verabschiedung OK |
| Ausbildungszeugnis | Lernleistung, Berufsschule, Verhalten, Praxis | Nach BBiG-Maßstab |
| Führungskraft (qualifiziert) | Plus Führung, Strategie, Repräsentation | Fehlen = Orange/Rot |

## Beispiele

**Beispiel 1 – Korrekte Zeugnisart-Erkennung:** "Wir stellen dieses Zeugnis auf eigenen Wunsch aus" + kein Enddatum → Zwischenzeugnis auf Wunsch des Arbeitnehmers.

**Beispiel 2 – Einfaches Zeugnis korrekt interpretiert:** Zeugnis ohne jede Leistungsbeurteilung und ohne Verhaltensabschnitt, aber mit explizitem Hinweis "einfaches Zeugnis" oder keine Bewertungsformulierungen — nicht als Abwertung zu lesen.

**Beispiel 3 – Fehlendes Verhalten bei Endzeugnis (Orange):** Qualifiziertes Zeugnis mit Leistungsbeurteilung, aber ohne Verhaltensabschnitt gegenüber Kollegen/Kunden — Auslassung ist auffällig.

**Beispiel 4 – Ausbildungszeugnis ohne Berufsschulangabe (Orange):** Bei einem BBiG-Zeugnis fehlt die Beurteilung des schulischen Teils komplett, obwohl Schule und Betrieb im Sachverhalt eine tragende Rolle spielen — erwarteter Baustein fehlt.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


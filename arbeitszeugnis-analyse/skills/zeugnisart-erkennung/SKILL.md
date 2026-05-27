---
name: zeugnisart-erkennung
description: "Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen § 109 GewO qualifiziertes vs. einfaches Zeugnis § 16 BBiG Ausbildungszeugnis. Pruefraster Inhalt Zeitbezug Position Stichtag Ausstellungsanlass. Output Zeugnisart-Klassifikation mit Erlauterungen zu Inhalt Erwartungshaltung und Interpretationsrahmen fuer alle Folge-Skills. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und notenrelevante-saetze-identifizieren."
---

# Zeugnisart-Erkennung

Die Art des Zeugnisses bestimmt grundlegend, welche Formulierungen erwartet werden, welche Aussagen fehlen dürfen und wie Auslassungen zu interpretieren sind. Ein einfaches Zeugnis enthält per Definition keine Leistungsbeurteilung — das Fehlen dieser Passage ist kein negatives Signal. Ein qualifiziertes Zeugnis hingegen muss Leistung und Verhalten beurteilen; fehlt eine dieser Komponenten, ist das auffällig.

Das Zwischenzeugnis wird ausgestellt, während das Arbeitsverhältnis noch besteht — etwa bei Vorgesetztenwechsel, Versetzung, Elternzeit oder auf ausdrücklichen Wunsch. Es enthält kein Enddatum und keine Schlussformel mit Verabschiedung. Die Formulierungen sind typischerweise im Präsens oder im Perfekt gehalten. Fehlt bei einem Zwischenzeugnis die Zukunftswunschformel, ist das kein Fehler; einige Zeugnisersteller fügen gleichwohl Formulierungen wie „Wir wünschen ihr weiterhin viel Erfolg" ein.

Das Ausbildungszeugnis beurteilt Auszubildende nach BBiG (§ 16 BBiG). Es enthält besondere Abschnitte zu Lernfortschritten, Verhalten im Ausbildungsbetrieb und in der Berufsschule sowie zur praktischen Ausbildungsleistung. Der Bewertungsrahmen ist eigenständig und nicht mit dem von Arbeitnehmer-Zeugnissen identisch.

Führungskräfte-Zeugnisse (leitende Angestellte) haben zusätzliche Erwartungen an Abschnitte zur Mitarbeiterführung, strategischen Verantwortung und Repräsentation des Unternehmens. Fehlen diese Abschnitte bei einer Führungskraft, ist das ein orangefarbenes oder rotes Signal.

## Geheimcode-Regeln

| Zeugnisart | Pflichtbausteine | Fehlende Bausteine |
|---|---|---|
| Einfaches Zeugnis | Art und Dauer der Tätigkeit | Keine Leistungsaussage erwartet |
| Qualifiziertes Endzeugnis | Art, Dauer, Leistung, Verhalten, Schlussformel | Rotes Signal |
| Zwischenzeugnis | Art, Dauer, Leistung, Verhalten (Präsens) | Kein Enddatum, keine Verabschiedung OK |
| Ausbildungszeugnis | Lernleistung, Berufsschule, Verhalten, Praxis | Nach BBiG-Maßstab |
| Führungskraft (qualifiziert) | Plus Führung, Strategie, Repräsentation | Fehlen = Orange/Rot |

## Beispiele

**Beispiel 1 – Korrekte Zeugnisart-Erkennung:** „Wir stellen dieses Zeugnis auf eigenen Wunsch aus" + kein Enddatum → Zwischenzeugnis auf Wunsch des Arbeitnehmers.

**Beispiel 2 – Einfaches Zeugnis korrekt interpretiert:** Zeugnis ohne jede Leistungsbeurteilung und ohne Verhaltensabschnitt, aber mit explizitem Hinweis „einfaches Zeugnis" oder keine Bewertungsformulierungen — nicht als Abwertung zu lesen.

**Beispiel 3 – Fehlendes Verhalten bei Endzeugnis (Orange):** Qualifiziertes Zeugnis mit Leistungsbeurteilung, aber ohne Verhaltensabschnitt gegenüber Kollegen/Kunden — Auslassung ist auffällig.

**Beispiel 4 – Ausbildungszeugnis ohne Berufsschulangabe (Orange):** Bei BBiG-Zeugnis fehlt die Beurteilung des schulischen Teils komplett — Pflichtbaustein fehlt.

## Ausgabeformat

Der Skill gibt zunächst die erkannte Zeugnisart aus (mit Begründung) und listet dann die erwarteten Bausteine mit dem Status „vorhanden / fehlend / unerwartet". Auf dieser Basis justiert er den Interpretationsrahmen für alle nachgelagerten Analyse-Skills.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- **BAG, Urt. v. 18.11.2014 — 9 AZR 584/13**, NZA 2015, 345 — Beweislastverteilung: Note schlechter als befriedigend beweist Arbeitgeber; Note besser als befriedigend beweist Arbeitnehmer; diese Verteilung gilt für alle notenrelevanten Bestandteile.
- **BAG, Urt. v. 12.08.2008 — 9 AZR 632/07**, BAGE 127, 232 — Wohlwollensgebot: Arbeitgeber muss Formulierungen wählen, die Fortkommen nicht unnötig erschweren; Berichtigungsanspruch bei Verstoß.

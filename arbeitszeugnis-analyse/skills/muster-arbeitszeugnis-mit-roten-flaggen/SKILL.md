---
name: muster-arbeitszeugnis-mit-roten-flaggen
description: "Anonymisiertes Beispielzeugnis mit roten orangen und gruenen Bewertungen als Schulungsmaterial. Anwendungsfall Training fuer Zeugnissprache und Geheimcode-Erkennung. Enthalt gemischte Ampelsignale mit vollstaendiger Analysetabelle. Output Ampel-Analysetabelle als kommentiertes Lernbeispiel mit Note-4- und Note-5-Signalen. Abgrenzung zu muster-arbeitszeugnis-gemischte-noten (Drift-Schwerpunkt) und muster-arbeitszeugnis-note-1 (Positivreferenz)."
---

# Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial)

Dieses anonymisierte Musterzeugnis zeigt ein real vorkommendes Mischbild: ein Zeugnis, das auf den ersten Blick positiv erscheint, aber bei näherer Analyse mehrere rote und orange Signale enthält. Es dient ausschließlich als Schulungsmaterial zur Übung der Geheimcode-Erkennung. Alle Namen und Daten sind fiktiv.

Dieses Zeugnis entspricht in der Gesamtbewertung der Note 3 bis 4. Die Signale verteilen sich: Leistungsbeurteilung enthält das klassische „bemüht"-Signal (Rot), die Verhaltensbeurteilung hat eine falsche Reihenfolge (Orange) und eine fragwürdige Formulierung (Orange), und die Schlussformel ist unvollständig — das Bedauern fehlt (Orange bis Rot).

## Geheimcode-Regeln

| Satz | Signal | Ampel | Note |
|---|---|---|---|
| „zur vollen Zufriedenheit" ohne „stets" | Fehlende Steigerung | Orange | Note 3 |
| „war stets bemüht" | Klassisches Note-4-Signal | Rot | Note 4 |
| „Kollegen und Vorgesetzte" (Reihenfolge) | Falsche Reihenfolge | Orange | Note 3 |
| „direkte Kommunikationsweise" | Euphemismus für schwieriges Verhalten | Rot | Note 4-5 |
| Schlussformel ohne Bedauern | Fehlender Pflichtbaustein | Orange-Rot | Note 3-4 |

## Beispiele

### Vollständiges Muster-Zeugnis mit roten Flaggen

---

**[Briefkopf]**
Beispiel GmbH | Beispielstraße 5 | 20000 Beispielstadt

**Arbeitszeugnis**

Herr Thomas Beispiel, geboren am 15. Juni 1980, war vom 1. Januar 2020 bis zum 30. Juni 2024 in unserem Unternehmen als Vertriebsmitarbeiter beschäftigt.

**Aufgaben:**
Herr Beispiel war im Außendienst tätig und betreute einen definierten Kundenkreis im Bereich Industriebedarf. Er war für die regelmäßige Kundenbesuche, die Angebotserstellung und die Bearbeitung von Reklamationen zuständig.

**Leistungsbeurteilung:**
Herr Beispiel verfügt über ausreichende Fachkenntnisse für seinen Aufgabenbereich. Er war stets bemüht, die ihm übertragenen Aufgaben zur vollen Zufriedenheit zu erledigen, und zeigte dabei durchgehend guten Willen. Seine Arbeitsweise war im Wesentlichen strukturiert.

*(Analyse: „bemüht" = Rot/Note 4; „zur vollen Zufriedenheit" ohne „stets" = Orange/Note 3; „im Wesentlichen" = Rot/Note 4; Gesamttendenz Leistung: Note 4)*

**Verhaltensbeurteilung:**
Gegenüber Kollegen und Vorgesetzten verhielt sich Herr Beispiel korrekt. Er zeichnete sich durch eine direkte Kommunikationsweise aus.

*(Analyse: Reihenfolge falsch — Kollegen vor Vorgesetzten = Orange; „korrekt" statt „einwandfrei" = Orange/Note 3; „direkte Kommunikationsweise" = Rot/Note 4-5; Kein Wort zu Kunden trotz Kundenjob = Rot)*

**Schlussformel:**
Wir danken Herrn Beispiel für seine Mitarbeit und wünschen ihm für die Zukunft alles Gute.

*(Analyse: Kein Bedauern = Orange-Rot; Dank ohne Adjektiv = Orange; Wunsch schwach formuliert = Orange; Gesamtnote Schlussformel: Note 3-4)*

---

### Gesamtbewertung des Schulungsbeispiels

| Bereich | Ampel | Note |
|---|---|---|
| Leistungsbeurteilung | Rot | Note 4 |
| Verhaltensbeurteilung | Rot | Note 4 |
| Schlussformel | Orange | Note 3-4 |
| **Gesamtnote** | **Rot** | **Note 4** |

**Handlungsempfehlung:** Nachverhandlung aller Leistungs- und Verhaltensformulierungen sowie vollständige Neufassung der Schlussformel empfohlen. Bei Weigerung: Klage auf Zeugnisberichtigung prüfen.

## Ausgabeformat

Der Skill gibt das Muster-Zeugnis mit eingebetteten Analyse-Kommentaren aus (wie im Beispiel oben), gefolgt von der vollständigen Ampeltabelle und der Gesamtbewertung. Einsatz als Schulungsmaterial für Mitarbeitende, Personalverantwortliche und Rechtsanwälte.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- **BAG, Urt. v. 18.11.2014 — 9 AZR 584/13**, NZA 2015, 345 — Beweislastverteilung: Note schlechter als befriedigend beweist Arbeitgeber; Note besser als befriedigend beweist Arbeitnehmer; diese Verteilung gilt für alle notenrelevanten Bestandteile.
- **BAG, Urt. v. 12.08.2008 — 9 AZR 632/07**, BAGE 127, 232 — Wohlwollensgebot: Arbeitgeber muss Formulierungen wählen, die Fortkommen nicht unnötig erschweren; Berichtigungsanspruch bei Verstoß.

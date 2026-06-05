---
name: hoai-baubesprechung-protokoll-baugrund
description: "Baubesprechung Protokoll Baugrund: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Baubesprechung Protokoll Baugrund

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Baubesprechung Protokoll Baugrund** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-baubesprechung-protokoll` | HOAI-Praxis: erstellt präzises Protokoll mit Verantwortlichen, Fristen und Beweiswert; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-baugrund-altlasten-untersuchungsbedarf` | HOAI-Fachfrage: Baugrund, Altlasten, Schadstoffe, Bestandserkundung, Untersuchungsbedarf, besondere Leistungen und Haftungs-/Nachtragsfolgen im Planungsprozess prüfen. |
| `hoai-bauherrnentscheidung-matrix` | HOAI-Praxis: macht Entscheidungen beweisbar, datiert und kostenbewusst; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-bauunternehmen-perspektive` | HOAI-Praxis: übersetzt HOAI-Planungsstand in Ausführungsrisiko und Nachtragschance; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-bim-cde-planmanagement` | HOAI-Praxis: ordnet BIM, CDE, Modellstände, Planfreigabe und Datenhoheit; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **Baubesprechung Protokoll Baugrund**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-baubesprechung-protokoll`

**Fokus:** HOAI-Praxis: erstellt präzises Protokoll mit Verantwortlichen, Fristen und Beweiswert; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Erstellt präzises protokoll mit verantwortlichen

## Einsatz

Dieser Querschnitts-Skill bearbeitet **erstellt präzises Protokoll mit Verantwortlichen, Fristen und Beweiswert** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 2. `hoai-baugrund-altlasten-untersuchungsbedarf`

**Fokus:** HOAI-Fachfrage: Baugrund, Altlasten, Schadstoffe, Bestandserkundung, Untersuchungsbedarf, besondere Leistungen und Haftungs-/Nachtragsfolgen im Planungsprozess prüfen.

# Baugrund, Altlasten Und Untersuchungsbedarf

## Einsatz

Dieses Fachmodul greift, wenn Baugrundgutachten fehlt, Schadstoffe im Bestand auftauchen, Altlasten Kosten sprengen oder der Planer Untersuchungsbedarf übersehen haben soll.

## Normanker

- Anlage 10 HOAI LPH 1/2: Untersuchungsbedarf und Auswahl fachlich Beteiligter.
- Besondere Leistungen nach Anlage 10 prüfen.
- Bauordnungs-, Umwelt- und Arbeitsschutzrecht live prüfen.

## Prüfung

1. Welche Hinweise gab es: Lage, Nutzungshistorie, Bestandspläne, Risse, Feuchte, Schadstoffe?
2. War ein Gutachten erforderlich oder nur zweckmäßig?
3. Wer musste es beauftragen und wer musste warnen?
4. Wie wirken neue Erkenntnisse auf Kosten, Termine und Planung?
5. Sind Zusatzleistungen vergütbar oder Fehlerbeseitigung?

## Output

Untersuchungsbedarf-Vermerk mit Warnpflicht, Fachgutachterauftrag, Kostenfolge und Beweisunterlagen.

## 3. `hoai-bauherrnentscheidung-matrix`

**Fokus:** HOAI-Praxis: macht Entscheidungen beweisbar, datiert und kostenbewusst; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Macht entscheidungen beweisbar

## Einsatz

Dieser Querschnitts-Skill bearbeitet **macht Entscheidungen beweisbar, datiert und kostenbewusst** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 4. `hoai-bauunternehmen-perspektive`

**Fokus:** HOAI-Praxis: übersetzt HOAI-Planungsstand in Ausführungsrisiko und Nachtragschance; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Übersetzt hoai-planungsstand in ausführungsrisiko und nachtragschance

## Einsatz

Dieser Querschnitts-Skill bearbeitet **übersetzt HOAI-Planungsstand in Ausführungsrisiko und Nachtragschance** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 5. `hoai-bim-cde-planmanagement`

**Fokus:** HOAI-Praxis: ordnet BIM, CDE, Modellstände, Planfreigabe und Datenhoheit; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Ordnet bim

## Einsatz

Dieser Querschnitts-Skill bearbeitet **ordnet BIM, CDE, Modellstände, Planfreigabe und Datenhoheit** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

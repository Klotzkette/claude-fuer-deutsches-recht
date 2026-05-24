---
name: legistik-auftragsaufnahme
description: "Strukturierte Aufnahme eines legistischen Auftrags. Nimmt eine politische Vorgabe entgegen Koalitionsvertrag Beschluss Bundeskabinett Landtagsantrag Buergermeisterbeschluss Aufsichtsweisung. Bricht sie herunter in operationalisierbare Regelungsziele. Klaert Adressaten Buerger Unternehmen Verwaltung Gerichte. Klaert Eingriffstiefe deklaratorisch konstitutiv. Klaert Dringlichkeit Eckpunktepapier Referentenentwurf Formulierungshilfe Kabinettsentwurf. Erzeugt Auftragsblatt mit zehn Fragen Regelungsziel Adressat Eingriff Norm-Ebene Vorrang anderer Normen EU-Bezug Verfassungsbezug Folgen Zeitplan Beteiligte. Anschluss `normhierarchie-routing`."
---

# Legistik-Auftragsaufnahme

> Erster Skill bei jedem neuen legistischen Vorhaben. Vor Normwahl, vor Entwurf, vor allem.

## Eingaben

- politische Vorgabe (Koalitionsvertrag, Kabinettsbeschluss, Landtagsantrag, Bürgermeisterbeschluss, Aufsichtsweisung)
- Auftraggeber (Hausleitung, Fachreferat, Land, Kommune)
- Adressat der Vorgabe (Bundestag, Bundesrat, Landtag, Stadtrat, Kammer-Vollversammlung)

## Vorgehen

### Schritt 1 - Was ist das politische Ziel?

Wer soll wozu verpflichtet oder ermaechtigt werden? Was soll verboten, was erlaubt werden?

### Schritt 2 - Wer ist Adressat der neuen Regel?

- Bürger (Grundrechtseingriff bedacht?)
- Unternehmen (Erfüllungsaufwand bedacht?)
- Verwaltung (Vollzugsaufwand bedacht?)
- Gerichte (gerichtliche Pruefbarkeit klar?)

### Schritt 3 - Wie tief greift die Regel ein?

- deklaratorisch (nur klarstellend, keine neuen Pflichten)
- konstitutiv (begründet neue Rechte oder Pflichten)
- modifizierend (aendert bestehende Pflichten)

### Schritt 4 - Wie eilig ist die Vorgabe?

- Eckpunktepapier (Phase 1) - politische Klärung
- Referentenentwurf (Phase 2) - mit Begründung, Verbändeanhörung
- Kabinettsentwurf (Phase 3) - nach Ressortabstimmung
- Formulierungshilfe (Phase 4) - aus der Mitte des Bundestages/Landtags (umgeht Ressortabstimmung und NKR-Prüfung)
- Eilgesetzgebung (Phase 5) - Fristverkürzungen

### Schritt 5 - Was ist die Norm-Ebene? Vorab-Routing

Welche Stufe ist plausibel? Bundesgesetz, Landesgesetz, Rechtsverordnung Bund, Rechtsverordnung Land, Satzung. Endgültige Antwort gibt Skill `normhierarchie-routing`.

### Schritt 6 - Auftragsblatt

| Feld | Inhalt |
|---|---|
| Aktenzeichen | (intern) |
| Bezeichnung des Vorhabens | |
| Politisches Ziel in einem Satz | |
| Adressat der Regelung | |
| Eingriffstiefe | |
| Norm-Ebene erste Einschätzung | |
| EU-Bezug ja/nein/unsicher | |
| Verfassungsbezug ja/nein/unsicher | |
| Folgen Bürger/Wirtschaft/Verwaltung | |
| Beteiligte Stellen | |
| Zeitplan | |

## Ausgabe

Strukturiertes Auftragsblatt als Markdown, das durch alle weiteren Skills mitgeführt wird.

## Anschluss

- `normhierarchie-routing` - welche Norm-Ebene ist richtig
- `gesetzgebungskompetenz-pruefen` falls Gesetz
- `verordnungsermaechtigung-art80` falls VO
- `satzungskompetenz-pruefen` falls Satzung

## Stolperfallen

1. Politische Vorgaben sind oft unscharf - Legist muss klären, nicht erfinden, sondern beim Auftraggeber nachfragen
2. Politik will manchmal nicht eine Norm, sondern eine Geste - dann ist ein Schreiben oder Erlass besser als ein Gesetz
3. Zeitvorgabe prüfen - oft ist eine Formulierungshilfe schneller als ein Referentenentwurf

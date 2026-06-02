---
name: legistik-auftragsaufnahme
description: "Legistischen Auftrag strukturiert aufnehmen und in operationale Regelungsziele umwandeln. Anwendungsfall Erstkontakt zu einem neuen Vorhaben aus Bundesministerium, Bundestag, Fraktion, Landesministerium, Landtag, Kommune, Kammer oder Hochschule. Klaert Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Adressaten, Eingriffstiefe, Dringlichkeit, Eckpunktepapier, Referentenentwurf, Formulierungshilfe, Gesetzentwurf aus der Mitte, Aenderungsantrag, Antrag, Kabinettsentwurf, Norm-Ebene, Verfassungs- und EU-Bezug, Zeitplan und Beteiligte. Output Auftragsblatt mit Startbahn und zehn Kernfragen. Anschluss normhierarchie-routing. Abgrenzung zu normenkartierung bestehende Normen kartieren."
---

# Legistik-Auftragsaufnahme

> Erster Skill bei jedem neuen legistischen Vorhaben. Vor Normwahl, vor Entwurf, vor allem.

## Eingaben

- politische Vorgabe (Koalitionsvertrag, Kabinettsbeschluss, Landtagsantrag, Bürgermeisterbeschluss, Aufsichtsweisung)
- Auftraggeber oder fachlicher Zulieferer (Hausleitung, Fachreferat, Fraktion, Gruppe, Abgeordnete, Land, Kommune, Kammer, Hochschule)
- formaler Initiator und Adressat der Vorgabe (Bundestag, Bundesrat, Landtag, Stadtrat, Kammer-Vollversammlung, Landesregierung, Gemeinderat)
- Bundesland und einschlägige Geschäftsordnung, wenn es kein reines Bundesvorhaben ist

## Vorgehen

### Schritt 0 - Startbahn und Verantwortung klären

Vor der inhaltlichen Zielbeschreibung ist die Startbahn zu dokumentieren:

| Startbahn | Klärfrage | Warum wichtig? |
|---|---|---|
| Bundesministerium / Bundesregierung | Welches Ressort, welches Referat, welche Hausleitung, welche Mitzeichner? | GGO, HdR, Ressortabstimmung, NKR und Kabinettspfad hängen daran. |
| Bundestag / Fraktion / Abgeordnete | Welche Fraktion, Gruppe oder Abgeordnetenzahl, welcher Ausschuss, welche Drucksache? | Art. 76 GG und GO-BT unterscheiden formale Initiative und fachliche Zulieferung. |
| Landesministerium / Landesregierung | Welches Bundesland, welches Ressort, welches Kabinetts- und Beteiligungsverfahren? | Landesverfassung, Landesgeschäftsordnung und Verkündung sind landesspezifisch. |
| Landtag / Landtagsfraktion | Welcher Landtag, welche Fraktion, welcher Verfahrensstand, welches Format? | Landtags-Geschäftsordnungen regeln Einbringung, Ausschuss und Änderungsanträge unterschiedlich. |
| Sonstiger Normgeber | Welche Körperschaft, welches Organ, welche Aufsicht und Bekanntmachungsform? | Satzungs- und Verordnungsbefugnis muss tragfähig belegt werden. |

Immer trennen:

- **Fachlicher Verfasser**: Wer liefert den Text?
- **Formaler Initiator**: Wer bringt die Vorlage ein?
- **Politischer Auftraggeber**: Wer trägt das Vorhaben?
- **Verantwortlicher Prüfpfad**: Regierungsintern, parlamentarisch, landesspezifisch oder satzungsrechtlich?

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

### Schritt 4 - Wie eilig ist die Vorgabe und welches Format passt?

- Eckpunktepapier (Phase 1) - politische Klärung
- Referentenentwurf (Phase 2) - mit Begründung, Verbändeanhörung
- Kabinettsentwurf (Phase 3) - nach Ressortabstimmung
- Formulierungshilfe oder Änderungsantrag (Phase 4) - fachliche Zulieferung für ein laufendes parlamentarisches Verfahren; formaler Initiator bleibt die parlamentarische Seite
- Gesetzentwurf aus der Mitte des Bundestages oder Landtages (Phase 4a) - parlamentarischer Vollentwurf, auch für Opposition oder Gruppen/Abgeordnete in der erforderlichen Stärke
- Antrag oder Entschließungsantrag (Phase 4b) - politischer Beschlussvorschlag ohne oder mit nur mittelbarem Normtext
- Eilgesetzgebung (Phase 5) - Fristverkürzungen

### Schritt 5 - Was ist die Norm-Ebene? Vorab-Routing

Welche Stufe ist plausibel? Bundesgesetz, Landesgesetz, Rechtsverordnung Bund, Rechtsverordnung Land, Satzung. Endgültige Antwort gibt Skill `normhierarchie-routing`.

### Schritt 6 - Auftragsblatt

| Feld | Inhalt |
|---|---|
| Aktenzeichen | (intern) |
| Bezeichnung des Vorhabens | |
| Startbahn | Bundesressort / Bundestag / Landesressort / Landtag / sonstiger Normgeber |
| Bund oder Bundesland | |
| Ressort / Fraktion / Organ | |
| Fachlicher Verfasser | |
| Formaler Initiator | |
| Regierungs-, Koalitions- oder Oppositionsrolle | |
| Verfahrensstand / Drucksache / Ausschuss | |
| Politisches Ziel in einem Satz | |
| Adressat der Regelung | |
| Eingriffstiefe | |
| Norm-Ebene erste Einschätzung | |
| EU-Bezug ja/nein/unsicher | |
| Verfassungsbezug ja/nein/unsicher | |
| Folgen Bürger/Wirtschaft/Verwaltung | |
| Beteiligte Stellen | |
| Maßgebliche Geschäftsordnung / Rechtsförmlichkeitsvorgaben | |
| Zeitplan | |

## Arbeitsgrundlagen

- Art. 76 Abs. 1 GG: Gesetzesvorlagen können durch Bundesregierung, aus der Mitte des Bundestages oder durch den Bundesrat eingebracht werden.
- Geschäftsordnung des Deutschen Bundestages, insbesondere Vorlagen von Mitgliedern des Bundestages und parlamentarische Antragsformen.
- GGO: Regierungsinterne Vorbereitung, Ressortbeteiligung, Rechtsprüfung, Kabinettsvorlagen und Umgang mit Vorlagen aus dem Bundestag/Bundesrat.
- Handbuch der Rechtsförmlichkeit des BMJ: Form, Sprache und Struktur von Gesetzes- und Verordnungsentwürfen der Bundesministerien.
- Landesverfassung, Geschäftsordnung der Landesregierung, Geschäftsordnung des Landtags und Verkündungsrecht des jeweiligen Bundeslandes.
- Gemeindeordnung, Kammergesetz, Hochschulgesetz oder Fachgesetz, wenn der Normgeber nicht Parlament oder Regierung ist.

## Zentrale Normen (Paragrafenkette)

Art. 76 Abs. 1 GG (Initiativrecht Bundesregierung, Bundestag, Bundesrat) — Art. 70-74 GG (Gesetzgebungskompetenz) — Art. 80 GG (Rechtsverordnung) — Art. 28 Abs. 2 GG (kommunale Selbstverwaltung) — GGO (ministerieller Regierungsweg) — GO-BT und Landtags-Geschäftsordnungen (parlamentarischer Weg) — Landesverfassungen und Verkündungsrecht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
4. Bei parlamentarischen Vorhaben nicht Ministerium und Parlament verschmelzen: Formale Initiative, fachliche Zuarbeit und politische Verantwortung getrennt dokumentieren
5. Bei Ländern nie mit Bundes-GGO allein arbeiten: Bundesland, Landesverfassung, Landtags-GO und Verkündungsblatt ausdrücklich abfragen

## Anschluss an Ressort-Router

Nach Aufnahme von Startbahn; Zielen und Eckdaten unmittelbar weiter zu **`legw-ressort-router`**.
Dieser leitet auf den fachlich richtigen Heranfuehrungs-Skill `legw-ressort-<kuerzel>` und die
ressorteigene Aufgaben- und Spezialkette. Ohne Ressort-Router bleibt die Materie ein blinder Fleck;
Politikwissenschaftler bekommen erst dort das Sachfeld-Verstaendnis fuer Landwirtschaft; Chemie;
Bauwesen; Verkehr und Co.

Wenn das Vorhaben digital-tauglich werden soll (Rulemap; BMJ-Initiative; SPRIND), zusaetzlich
Anschluss an **`legw-rmap-einstieg-und-eignung`**.


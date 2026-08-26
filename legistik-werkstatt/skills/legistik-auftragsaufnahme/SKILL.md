---
name: legistik-auftragsaufnahme
description: "Für Legistik-Auftragsaufnahme: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Legistik-Auftragsaufnahme

> Erster Skill bei jedem neuen legistischen Vorhaben. Vor Normwahl, vor Entwurf, vor allem.

## Eingaben

- politische Vorgabe (Koalitionsvertrag, Kabinettsbeschluss, Landtagsantrag, Bürgermeisterbeschluss, Aufsichtsweisung)
- Auftraggeber oder fachlicher Zulieferer (Hausleitung, Fachreferat, Fraktion, Gruppe, Abgeordnete, Land, Kommune, Kammer, Hochschule)
- formaler Initiator und Adressat der Vorgabe (Bundestag, Bundesrat, Landtag, Stadtrat, Kammer-Vollversammlung, Landesregierung, Gemeinderat)
- Bundesland und einschlägige Geschäftsordnung, wenn es kein reines Bundesvorhaben ist

## Arbeitsgrundlagen

- Art. 76 Abs. 1 GG: Gesetzesvorlagen können durch Bundesregierung, aus der Mitte des Bundestages oder durch den Bundesrat eingebracht werden.
- Geschäftsordnung des Deutschen Bundestages, insbesondere Vorlagen von Mitgliedern des Bundestages und parlamentarische Antragsformen.
- GGO: Regierungsinterne Vorbereitung, Ressortbeteiligung, Rechtsprüfung, Kabinettsvorlagen und Umgang mit Vorlagen aus dem Bundestag/Bundesrat.
- Handbuch der Rechtsförmlichkeit des BMJ: Form, Sprache und Struktur von Gesetzes- und Verordnungsentwürfen der Bundesministerien.
- Landesverfassung, Geschäftsordnung der Landesregierung, Geschäftsordnung des Landtags und Verkündungsrecht des jeweiligen Bundeslandes.
- Gemeindeordnung, Kammergesetz, Hochschulgesetz oder Fachgesetz, wenn der Normgeber nicht Parlament oder Regierung ist.

## Zentrale Normen (Paragrafenkette)

Art. 76 Abs. 1 GG (Initiativrecht Bundesregierung, Bundestag, Bundesrat) — Art. 70-74 GG (Gesetzgebungskompetenz) — Art. 80 GG (Rechtsverordnung) — Art. 28 Abs. 2 GG (kommunale Selbstverwaltung) — GGO (ministerieller Regierungsweg) — GO-BT und Landtags-Geschäftsordnungen (parlamentarischer Weg) — Landesverfassungen und Verkündungsrecht

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
Politikwissenschaftler bekommen erst dort das Sachfeld-Verstaendnis für Landwirtschaft; Chemie;
Bauwesen; Verkehr und Co.

Wenn das Vorhaben digital-tauglich werden soll (Rulemap; BMJ-Initiative; SPRIND), zusaetzlich
Anschluss an **`legw-rmap-grundlagen`** (didaktischer Einstieg in 10 RuleMapping-Skills, abschliessend `legw-rmap-anschluss-an-legw` als Rueckkopplung).

---
name: orientierung-triage-paragraph-stgb-besonders
description: "Einstieg und Triage. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe), erkennt Eilfristen, schlaegt passende Fachmodule aus diesem Plugin vor u..."
---

# Strafzumessung — Orientierung und Triage

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es?

Strafzumessung ist die richterliche Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens. Grundlage ist die Schuld des Taeters (§ 46 Abs. 1 Satz 1 StGB). Dieser Allgemein-Skill ist der Eingang in das Plugin: er ordnet den Stand des Verfahrens, identifiziert Fristen und schlaegt den passenden Fachmodul vor.

## Wann brauchen Sie diese Skill?

- Mandant hat Strafbefehl erhalten, Strafzumessung soll angegriffen oder beschraenkter Einspruch erwogen werden.
- Anklageschrift liegt vor, Strafzumessungs-Verteidigung in der Hauptverhandlung wird vorbereitet.
- Verstaendigungs-Gespraech (§ 257c StPO) mit Gericht und Staatsanwaltschaft steht an, Strafrahmen wird sondiert.
- Urteil ist ergangen, Strafzumessungsruege wird vorbereitet (§ 267 Abs. 3 StPO).
- Mehrere Verurteilungen liegen vor, nachtraegliche Gesamtstrafenbildung (§ 55 StGB) oder Haerteausgleich prüfen.

## Rolle abklaeren (Pflicht)

| Rolle | Typischer Fokus |
|---|---|
| Strafverteidiger | Strafmilderung, Bewaehrung, TOA, Verstaendigung, Strafzumessungsruege |
| Staatsanwaltschaft | Antragsstrafe, Strafzumessungsrichtlinien, Schwere-Argumente |
| Mandant / Betroffener (mit Anwalt) | Verstaendnis der Strafzumessungslogik; Tagessatzpruefung |
| Nebenklaegervertreter | Strafzumessungs-Aspekte zugunsten des Opfers |

Wenn die Rolle unklar ist, **frage zuerst** — die Argumentationsrichtung haengt davon ab.

## Verfahrensstadium-Triage

| Stadium | Primaerer Skill |
|---|---|
| Strafbefehl liegt vor | `strafbefehl-strafzumessung-407-stpo`, ggf. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` |
| Einstellungsangebot § 153a StPO | `153a-stpo-einstellung-gegen-auflage` |
| Anklage liegt vor, Hauptverhandlung vorbereiten | `strafrahmen-und-strafzumessungsstufen`, dann `paragraph-46-stgb-grundsatz-strafzumessung` |
| Verstaendigung steht an | `verstaendigung-257c-stpo-strafzumessung` |
| TOA mit dem Opfer möglich | `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` |
| Mehrere Taten in einem Verfahren | `gesamtstrafenbildung-53-54-stgb-erste-instanz` |
| Mehrere Verurteilungen, eine Anlasstat | `nachtraegliche-gesamtstrafenbildung-55-stgb`, ggf. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` |
| Urteil liegt vor, Strafzumessungsruege | `267-iii-stpo-begruendungsanforderungen-strafurteil` |
| Mandant unter 21 Jahren | `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` |

## Schritt-für-Schritt-Anleitung

1. Rolle und Verfahrensstadium erfragen oder aus Material erkennen.
2. Eilfristen prüfen (Einspruchsfrist § 410 StPO, Revisionsbegruendung § 345 StPO, Bewaehrungsstellungnahme).
3. Strafrahmen-Frage stellen: Welche Norm, welcher Strafrahmen, gibt es Regelbeispiele oder minder schweren Fall?
4. Strafzumessungs-Tatsachen sammeln (§ 46 Abs. 2 StGB): Vorleben, Tat, Nachtatverhalten.
5. Passenden Fachmodul auswaehlen; bei klarer Faktenlage sofort ersten Entwurf mit Platzhaltern liefern.
6. Quellenpflicht beachten: § 46 StGB, einschlaegige Spezialnormen, BGH-Linie nur mit verifiziertem Aktenzeichen.

## Typische Fehler

- Strafzumessung wird ohne Sortierung des Strafrahmens diskutiert: erst Strafrahmen prüfen, dann konkretisieren.
- Verstaendigung wird abgeschlossen, bevor die Belehrungspflicht (§ 257c Abs. 4 und 5 StPO) sauber gepruefte ist.
- TOA wird als reine Schadenswiedergutmachung verstanden; nach BGH ist ein friedensstiftender kommunikativer Prozess noetig.
- Tagessatzhoehe wird ohne Einkommensnachweis akzeptiert; Gericht schaetzt sonst zu Lasten des Mandanten.
- Nachtraegliche Gesamtstrafe wird vergessen; Haerteausgleich nicht thematisiert.

## Quellen und Stand 05/2026

- StGB §§ 38 ff. (Strafarten, Strafrahmen), § 46 (Grundsatz), §§ 47, 49, 56, 56b–f, 53–55 StGB.
- StPO §§ 153, 153a, 257c, 267 Abs. 3, 407 ff., 460 StPO.
- JGG §§ 5 ff., 17, 18, 105.
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; vgl. `references/zitierweise.md`.

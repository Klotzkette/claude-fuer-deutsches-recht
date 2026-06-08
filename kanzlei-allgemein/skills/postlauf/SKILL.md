---
name: postlauf
description: "Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen Output Zeit und Rechnung im Kanzlei Allgemein."
---

# Postlauf um 11 Uhr

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Sind neue Eingaenge seit dem letzten Postlauf zu verarbeiten (Brief, beA, E-Mail, Fax, Messenger)?
2. Gibt es fristwaehrende Dokumente im Posteingang (Klageschrift, Bescheide, Urteile mit EB-Pflicht)?
3. Muss das beA-Journal aktualisiert werden (neue Nachrichten, ZIP-Export, EB-Entscheidungen)?
4. Welche offenen Action-Items aus dem letzten Postlauf sind noch ausstehend?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 173 ZPO — Zeitpunkt der beA-Zustellung: Eingang im Empfangspostfach
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Datum massgebend für Fristbeginn
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion seit 01.01.2025
- § 51 BRAO — Haftung bei Organisationspflichtverletzung im Postlauf

## Ablauf

1. Neue Eingänge seit dem letzten Postlauf erfassen.
2. Bei beA-Connect das Nachrichtenjournal öffnen, einsehen, Screenshot sichern und `kanzlei-allgemein-bea-journal` starten.
3. Jede neue beA-Nachricht als ZIP-Archiv exportieren oder herunterladen, entpacken und der Akte zuordnen.
4. Jede seit dem letzten Lauf versandte beA-Nachricht im Journal prüfen, als ZIP sichern und entpacken.
5. Elektronische Empfangsbekenntnisse erkennen und EB-anbieten.
6. Nicht zugeordnete Eingänge an `kanzlei-allgemein-intake` geben.
7. Fristen heute, morgen und diese Woche anzeigen.
8. Action-Items nach Verantwortlichen gruppieren.
9. Versandbedarf prüfen.
10. Rückfragen an Mandant, Gericht, Gegner oder intern sammeln.
11. Zeiteinträge für Postbearbeitung vorschlagen.

## Ausgabe

`assets/templates/postlauf-journal.md` verwenden.

## Automationshinweis

Wenn die Umgebung Automationen unterstützt, den Nutzer fragen:

> Soll ich eine tägliche Erinnerung um 11 Uhr für den Postlauf einrichten?

Ohne Automationsunterstützung eine manuelle Checkliste erzeugen.


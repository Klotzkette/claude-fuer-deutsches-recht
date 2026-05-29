---
name: kanzlei-allgemein-postlauf
description: "Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen Output Zeit und Rechnung."
---

# Postlauf um 11 Uhr


## Triage zu Beginn
1. Sind neue Eingaenge seit dem letzten Postlauf zu verarbeiten (Brief, beA, E-Mail, Fax, Messenger)?
2. Gibt es fristwaehrende Dokumente im Posteingang (Klageschrift, Bescheide, Urteile mit EB-Pflicht)?
3. Muss das beA-Journal aktualisiert werden (neue Nachrichten, ZIP-Export, EB-Entscheidungen)?
4. Welche offenen Action-Items aus dem letzten Postlauf sind noch ausstehend?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 173 ZPO — Zeitpunkt der beA-Zustellung: Eingang im Empfangspostfach
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Datum massgebend fuer Fristbeginn
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion seit 01.01.2025
- § 51 BRAO — Haftung bei Organisationspflichtverletzung im Postlauf

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bildet die tägliche Kanzleipost ab. Er ist für den manuellen Aufruf oder für eine Umgebung mit Automationen gedacht.

## Ablauf

1. Neue Eingänge seit dem letzten Postlauf erfassen.
2. Bei beA-Connect das Nachrichtenjournal öffnen, einsehen, Screenshot sichern und `kanzlei-allgemein-bea-journal` starten.
3. Jede neue beA-Nachricht als ZIP-Archiv exportieren oder herunterladen, entpacken und der Akte zuordnen.
4. Jede seit dem letzten Lauf versandte beA-Nachricht im Journal prüfen, als ZIP sichern und entpacken.
5. Elektronische Empfangsbekenntnisse erkennen und EB-Workflow anbieten.
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

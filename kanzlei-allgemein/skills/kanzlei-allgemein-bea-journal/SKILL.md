---
name: kanzlei-allgemein-bea-journal
description: "Dokumentation von beA-Verbindungen Nachrichten Versand und Empfangsbekenntnissen. Anwendungsfall beA-Eingang oder Versand muss nachvollziehbar protokolliert werden mit Screenshot ZIP-Export und EB-Workflow. Normen § 130a ZPO § 31a BRAO § 12 ERVV. Prüfraster Nachrichtenjournal Screenshots ZIP-Export eingegangene und versandte Nachrichten EB-Status Freigabe vor Versand. Output Versandjournal EB-Dokumentation ZIP-Archiv Screenshot-Ablage. Abgrenzung zu bea-versand-prüfen (Prüfung Versandweg) und kanzlei-allgemein-output-versand."
---

# beA-Nachrichtenjournal und EB-Workflow


## Triage zu Beginn
1. Liegt ein frischer beA-Zugriff oder ein archivierter ZIP-Export vor?
2. Welche Nachrichten muessen der Akte zugeordnet werden (Eingang und Ausgang)?
3. Gibt es Empfangsbekenntnisse (EB), die aktuell zur Entscheidung anstehen?
4. Sind fristwahrende Dokumente dabei, die sofort ins Fristenbuch muessen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 173 Abs. 2 ZPO — Zustellung per beA: Zustelldatum ist der Tag des EB-Klicks
- § 31a BRAO — Pflicht zur Einrichtung und Nutzung des beA
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Formerfordernis und Fristausloesung
- § 130a ZPO — Anforderungen an elektronische Dokumente und Uebermittlung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill wird genutzt, sobald eine technische beA-Verbindung, ein beA-Export oder ein beA-Screenshot vorliegt. Er macht aus beA-Zugriffen einen nachvollziehbaren Kanzleivorgang: Journal sichern, Nachrichten archivieren, Eingänge und Ausgänge der Akte zuordnen, Fristen erkennen und elektronische Empfangsbekenntnisse nur nach ausdrücklicher Freigabe vorbereiten oder abgeben.

## Sicherheitsstart

Vor jedem beA-Zugriff ausgeben:

> beA-Sicherheitswarnung: Software-Token, Zertifikatsdatei, PIN und Passwörter nicht in den Chat eingeben und nicht speichern. PIN nur in der lokalen beA-Komponente eingeben. Dieser Lauf dokumentiert Nachrichten, Archive, Screenshots und EB-Entscheidungen, ersetzt aber keine anwaltliche Fristen- und Versandkontrolle.

## Scope klären

1. Welches beA-Postfach wird bearbeitet?
2. Welcher Zeitraum wird geprüft?
3. Welche Akten oder Aktenzeichen sind umfasst?
4. Soll nur gelesen und archiviert oder auch ein Versand vorbereitet werden?
5. Wer ist berufsträgerseitig verantwortlich?
6. Wo sollen Journal, Screenshots, ZIP-Archive und entpackte Nachrichten abgelegt werden?

## Pflichtablauf bei beA-Verbindung

Wenn ein beA-Connect technisch möglich ist:

1. Nachrichtenjournal öffnen und einsehen.
2. Nachrichtenjournal mit Zeitpunkt, Postfach, Filter und Bearbeiter protokollieren.
3. Screenshot des Nachrichtenjournals erstellen oder anfordern.
4. Wenn technisch möglich, Journal zusätzlich als PDF, HTML oder Exportdatei speichern.
5. Jede eingegangene beA-Nachricht als ZIP-Archiv herunterladen oder exportieren.
6. Jedes eingegangene ZIP-Archiv entpacken und die entpackten Dateien der Akte zuordnen.
7. Jede versandte beA-Nachricht nach Versand im Ausgangs- oder Gesendet-Journal öffnen.
8. Jede versandte beA-Nachricht als ZIP-Archiv herunterladen oder exportieren.
9. Jedes versandte ZIP-Archiv entpacken und Versandnachweis, Anlagen und Metadaten prüfen.
10. Für jede Nachricht Fristen, EB, Antwortbedarf und Ablageentscheidung an `kanzlei-allgemein-fristen-monitor` übergeben.

## Eingegangene Nachrichten

Für jeden Eingang erfassen:

- Empfangsdatum und Uhrzeit.
- Absender und SAFE-ID, soweit sichtbar.
- Betreff, Geschäftszeichen, Aktenzeichen, Gericht oder Behörde.
- Zustellart und Zustellnachweis.
- Anlagenliste.
- ZIP-Archivpfad.
- Entpackter Ablagepfad.
- Screenshot- oder Journalnachweis.
- Fristen und Action-Items.
- Ob ein elektronisches Empfangsbekenntnis verlangt oder sinnvoll ist.

## Versandte Nachrichten

Nach jedem beA-Versand:

1. Gesendet- oder Ausgangsjournal öffnen.
2. Versandstatus, Empfänger, Zeitpunkt, Nachrichtentyp, Aktenzeichen und Anlagen kontrollieren.
3. Screenshot des Versandstatus oder Nachrichtenjournals erstellen.
4. Versandte Nachricht als ZIP-Archiv herunterladen oder exportieren.
5. ZIP entpacken.
6. Versandnachweis, Prüfprotokoll, Schriftsatzfassung und Anlagen mit dem Versandauftrag abgleichen.
7. Ergebnis in `assets/templates/bea-nachrichtenjournal.md` und `assets/templates/output-versandprotokoll.md` dokumentieren.

## Elektronisches Empfangsbekenntnis

Wenn eine Nachricht ein EB verlangt oder nahelegt:

1. EB-Anforderung erkennen und Quelle zitieren.
2. Zustellungsdatum, Fristbeginn, Dokumentumfang und Akte prüfen.
3. Berufsträger fragen:

   > Soll ich für diese beA-Nachricht ein elektronisches Empfangsbekenntnis vorbereiten oder abgeben?

4. Vor Abgabe zusätzlich warnen:

   > EB-Abgabe bestätigt den Empfang und kann Fristen auslösen. Bitte erst nach Prüfung von Akte, Nachricht, Anlagen, Zustellungsdatum, Fristfolgen und Berufsträgerzuständigkeit freigeben.

5. Ohne ausdrückliche Einzelbestätigung kein EB abgeben.
6. Nach EB-Abgabe Journal erneut öffnen, Screenshot erstellen, EB-Nachweis speichern, ZIP-Export sichern und Fristenmonitor aktualisieren.

## Fallback ohne technische beA-Steuerung

Wenn das System beA nicht selbst bedienen kann:

- Schritt-für-Schritt-Checkliste für den Nutzer ausgeben.
- Den Nutzer bitten, Journal-Screenshot, Nachrichten-ZIP, Versand-ZIP oder EB-Nachweis hochzuladen.
- Keine Behauptung aufstellen, dass ein Versand, Download oder EB erfolgt sei.

## Ausgabe

`assets/templates/bea-nachrichtenjournal.md` verwenden.

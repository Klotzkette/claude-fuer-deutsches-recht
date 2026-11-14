---
name: bea-journal
description: "Für beA-Nachrichtenjournal und EB-Workflow: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# beA-Nachrichtenjournal und EB-Workflow

## Arbeitsbereich

Dokumentation von beA-Verbindungen, Nachrichten, Versand und Empfangsbekenntnissen. Ein beA-Eingang oder Versand muss mit Exportnachricht, Prüfvermerk, gerichtlicher Eingangsbestätigung und EB-Status nachvollziehbar protokolliert werden. Normenanker sind ZPO Paragraf 130a, BRAO Paragraf 31a, ERVV und die aktuelle ERVB. Der Skill liefert Versandjournal, EB-Dokumentation, Exportarchiv und Screenshot-Ablage und grenzt sich von `bea-versand-pruefen` als Form- und Eingangskontrolle ab.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Liegt ein frischer beA-Zugriff oder ein archivierter ZIP-Export vor?
2. Welche Nachrichten müssen der Akte zugeordnet werden (Eingang und Ausgang)?
3. Gibt es Empfangsbekenntnisse (EB), die aktuell zur Entscheidung anstehen?
4. Sind fristwahrende Dokumente dabei, die sofort ins Fristenbuch müssen?

## Zentrale Normen
- § 173 Abs. 2 ZPO — Zustellung per beA: Zustelldatum ist der Tag des EB-Klicks
- § 31a BRAO — Pflicht zur Einrichtung und Nutzung des beA
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Formerfordernis und Fristausloesung
- § 130a ZPO — Anforderungen an elektronische Dokumente und Uebermittlung

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

---
name: handelsregisterabruf
description: "Handelsregisterabruf über offizielle Quellen für Unternehmensprüfung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprüft werden. Normen §§ 15 17 HGB Registerrecht § 10 GwG wirtschaftlich Berechtigte. Prüfraster Firma Sitz..."
---

# Handelsregisterabruf

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Was ist der Zweck des Abrufs: Vertretungspruefung, KYC/GwG, Zustellungsanschrift, Vertragspartei-Identifikation?
2. Ist der Eintrag beim Handelsregister aktuell (letzter Abruf-Zeitstempel noetig für Nachweis)?
3. Gibt es Verdachtsmomente für Sitzverlegung, Geschäftsführeraenderung oder Insolvenzen?
4. Ist eine Gesellschafterliste (GmbH) oder Prokura-Eintragung relevant?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 15 HGB — Registerpublizitaet: Eintragungen und deren Wirkung
- § 8 HGB — Inhalt und Pflichtangaben des Handelsregisters
- § 40 GmbHG — Gesellschafterliste: Hinterlegung und Wirkung als Nachweis der Mitgliedschaft
- § 3 GwG — Sorgfaltspflichten für risikobasierte KYC-Prüfung (Handelsregister als Beleg)

## Offizielle Quellen

- Gemeinsames Registerportal der Länder: `https://www.handelsregister.de`.
- Unternehmensregister: `https://www.unternehmensregister.de`.
- Nicht auf Drittanbieter verlassen, wenn es um Vertretung, Registerstand oder aktuelle Dokumente geht.

Wenn kein Browser- oder Registerzugang vorhanden ist, einen Simulationsmodus anbieten. Im Simulationsmodus müssen alle Registerdaten als fiktiv oder ungeprüft gekennzeichnet werden.

## Abrufziel klären

1. Firma oder Name.
2. Rechtsform.
3. Sitz.
4. Registergericht.
5. Registernummer.
6. Zweck: Klage, Zustellung, Vertrag, Vollmacht, Rechnung, KYC, Due Diligence.
7. Benötigte Dokumente: aktueller Abdruck, chronologischer Abdruck, Gesellschafterliste, Gesellschaftsvertrag, Registerbekanntmachung.

## Prüfprogramm

- Firma exakt übernehmen.
- Rechtsform und Sitz prüfen.
- Registergericht und Registernummer festhalten.
- Vertretungsberechtigung prüfen.
- Einzel- oder Gesamtvertretung prüfen.
- Prokura prüfen.
- Liquidation, Insolvenz, Löschung oder Umwandlung prüfen.
- Zustellfähige Anschrift nicht blind aus Handelsregister ableiten, wenn Zustellung kritisch ist.
- Dokumentdatum und Abrufzeitpunkt protokollieren.

## Such- und Trefferlogik

- Schreibvarianten, alte Firma, Sitzverlegung und Rechtsformzusatz prüfen.
- Mehrere Treffer nicht zusammenführen, sondern getrennt darstellen.
- Bei UG, GmbH, AG, KG, OHG, PartG und e. K. Rechtsform exakt übernehmen.
- Bei Zweigniederlassungen Hauptniederlassung und Vertretung gesondert prüfen.
- Bei Konzernnamen nicht automatisch die richtige Vertragspartnerin annehmen.

## Verwendung

Für Klage:

- Parteibezeichnung und Vertretung prüfen.
- Zustelladresse gesondert validieren.
- Anlagenbezeichnung für Registerauszug vergeben.

Für Vertrag:

- Parteibezeichnung.
- Vertretung und Zeichnungsberechtigung.
- Handelsregisterdaten in Rubrum oder Präambel.

Für Rechnung und Buchhaltung:

- Rechnungsempfänger mit Firma, Rechtsform und Anschrift abgleichen.
- Debitorenstamm aktualisieren.
- Zahlungszuordnung nicht allein aus Registerdaten ableiten.

## Warnlogik

`STOPP` ausgeben, wenn:

- Firma oder Rechtsform unklar ist.
- Vertretung nicht geprüft ist.
- der Registerstatus Liquidation, Löschung, Insolvenz oder Umwandlung nahelegt.
- die Anschrift für Zustellung oder Vertrag nicht belastbar ist.

`WARNUNG` ausgeben, wenn:

- nur eine Simulation vorliegt.
- Dokumente älter sind als der aktuelle Entscheidungsbedarf.
- Gesellschafterliste, Satzung oder Prokura relevant sein könnten, aber fehlen.

## Ausgabe

`assets/templates/handelsregisterabruf-protokoll.md` verwenden.

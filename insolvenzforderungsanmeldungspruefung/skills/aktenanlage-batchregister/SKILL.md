---
name: aktenanlage-batchregister
description: "Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubigerstamm, Prüfnummern, Status je Forderung, Wiedervorlagen, Audit-Trail, Fristen. Output Batchregister mit Eingangsprotokoll, Statusuebersicht und Fristenliste. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Kommandocenter im Insolvenzforderungsanmeldungspruefung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Aktenanlage und Batchregister

## Arbeitsbereich

Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubigerstamm, Prüfnummern, Status je Forderung, Wiedervorlagen, Audit-Trail, Fristen. Output Batchregister mit Eingangsprotokoll, Statusuebersicht und Fristenliste. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Kommandocenter. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aktenanlage und Batchregister` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe

Baut die Arbeitsakte für große Forderungsstapel und hält Status, Zuständigkeit und Nachlauf zusammen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- mehr als fünf Forderungen
- Tabellenimport soll vorbereitet werden
- Prüfteam braucht Statusübersicht

## Workflow

1. Einheitliche Prüfnummern bilden und jeder Anmeldung genau eine Arbeitsakte geben.
2. Gläubigerstamm normalisieren: Name, Rechtsform, Anschrift, Vertreter, Konto, E-Mail, Registerdaten.
3. Statusspalten anlegen: neu, formal geprüft, Nachforderung, materiell geprüft, festgestellt, bestritten, erledigt.
4. Wiedervorlagen für Belege, Prüfungstermin, Feststellungsklage und § 189-Nachweis setzen.
5. Audit-Trail mit Bearbeiter, Datum, Quelle und Entscheidung anlegen.

## Ausgabe

- Batchregister als CSV-Struktur
- Statusdashboard
- Wiedervorlagenliste
- Bearbeitungsprotokoll

## Qualitätsgates

- Eine Forderung kann mehrere Teilbeträge haben, aber nur eine eindeutige Prüfnummernfamilie.
- Gläubigerstamm und Forderungspositionen bleiben getrennt.
- Bearbeitungsstände sind rückverfolgbar.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.

## Rechtliche Grundlagen und Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aktenanlage

§ 174 InsO (Anmeldeform) → § 175 InsO (Eintragung Tabelle) → § 176 InsO (Pruefungstermin) → § 66 InsO (Rechnungslegung und Dokumentation) → § 60 InsO (Verwalterhaftung) → § 61 InsO (persoenliche Haftung IV)

## Triage — Batchregister-Kaltstart

1. **Wieviele Anmeldungen erwartet?** Mittel- bis Grossverfahren (>20 Glaeubiger) → Batch-System zwingend.
2. **Digitale Einreichung?** § 174 Abs. 4 InsO Erleichterungen beachten; E-Mail vs. beA.
3. **Fristen?** Pruefungstermin § 176 InsO: Ladungsfrist 7 Tage; Tabelle muss vorher vollstaendig sein.
4. **Dubletten-Risiko?** Gleicher Glaeubiger mehrfach (z.B. Abtretung) → Deduplication-Logik einbauen.

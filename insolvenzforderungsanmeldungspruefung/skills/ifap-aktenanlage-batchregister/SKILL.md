---
name: ifap-aktenanlage-batchregister
description: "Batchregister fuer Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Pruefungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. § 175 InsO Tabelle, § 176 InsO Pruefungstermin. Pruefraster Glaeubigerstamm, Prüfnummern, Status je Forderung, Wiedervorlagen, Audit-Trail, Fristen. Output Batchregister mit Eingangsprotokoll, Statusuebersicht und Fristenliste. Abgrenzung zu Intake-Kanalcheck fuer Eingangserfassung und zu Kommandocenter."
---

# Aktenanlage und Batchregister

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

- BGH, Urt. v. 19.02.2009 — IX ZR 2/08, NZI 2009, 389 — Insolvenzverwalter-Pflicht zur ordnungsgemaessen Fuehrung der Insolvenztabelle: Fehler bei Tabellenanlage und Aktenregistrierung begruenden persoenliche Haftung des IV; Sorgfaltsmassstab wie ein ordentlicher Kaufmann.
- BGH, Urt. v. 25.09.2014 — IX ZR 252/13, NZI 2015, 31 — Verwalterhaftung bei Verlust von Forderungsanmeldungen: IV haftet wenn Anmeldungen verloren gehen und Glaeubiger Rechte verlieren; Dokumentationspflicht aus § 66 InsO.
- BGH, Urt. v. 22.09.2005 — IX ZB 55/04 — Pruefungstermin § 176 InsO: IV muss Tabelle vollstaendig und richtig fuehren; falsche Eintragungen koennen Schadensersatz des Glaeubiger-Ausschusses begruenden.

## Paragrafenkette Aktenanlage

§ 174 InsO (Anmeldeform) → § 175 InsO (Eintragung Tabelle) → § 176 InsO (Pruefungstermin) → § 66 InsO (Rechnungslegung und Dokumentation) → § 60 InsO (Verwalterhaftung) → § 61 InsO (persoenliche Haftung IV)

## Triage — Batchregister-Kaltstart

1. **Wieviele Anmeldungen erwartet?** Mittel- bis Grossverfahren (>20 Glaeubiger) → Batch-System zwingend.
2. **Digitale Einreichung?** § 174 Abs. 4 InsO Erleichterungen beachten; E-Mail vs. beA.
3. **Fristen?** Pruefungstermin § 176 InsO: Ladungsfrist 7 Tage; Tabelle muss vorher vollstaendig sein.
4. **Dubletten-Risiko?** Gleicher Glaeubiger mehrfach (z.B. Abtretung) → Deduplication-Logik einbauen.

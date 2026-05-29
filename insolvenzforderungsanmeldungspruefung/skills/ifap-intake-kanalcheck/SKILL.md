---
name: ifap-intake-kanalcheck
description: "Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsanmeldung, § 177 InsO Nachtragsanmeldung. Prüfraster Kanal-Identifikation, Metadaten-Erfassung, Eingangs-Zeitstempel, Dubletten-Vorabcheck, Prioritaet bei Fristnaehe. Output strukturiertes Eingangsbuch mit Kanal, Datum, Gläubiger und Status. Abgrenzung zu Aktenanlage-Batchregister für Massenerfassung und zu Formalprüfung."
---

# Intake und Kanalcheck

## Aufgabe

Erfasst eingehende Forderungsanmeldungen kanalneutral und bildet ein belastbares Eingangsbuch.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Posteingang liegt vor
- Portalexport oder CSV liegt vor
- Gläubiger sendet Nachtrag
- mehrere Kanäle enthalten dieselbe Forderung

## Workflow

1. Eingangskanal, Eingangsdatum, Dateiname, Absender, Vertreter und Gläubiger-ID erfassen.
2. Anmeldung von Begleitschreiben, Anlagen, Rechnungspaketen, Titeln und Zahlungsnachweisen trennen.
3. Fristlage prüfen: rechtzeitig, verspätet, geändert oder offensichtlich nur Ergänzung.
4. Dublettenindizien markieren: gleicher Gläubiger, gleiche Rechnung, gleicher Betrag, gleicher Zeitraum, gleicher Titel.
5. Eingangsbuch und Prüfnummer vergeben, ohne materiell zu entscheiden.

## Ausgabe

- Intake-Register
- Dublettenhinweise
- fehlende Mindestdaten
- Zuordnung zu bestehender Prüfnummer

## Qualitätsgates

- Nachträge werden an die ursprüngliche Anmeldung geklebt.
- E-Mail-Text und Anlagen werden getrennt ausgewertet.
- Unlesbare Dateien werden nicht stillschweigend ignoriert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
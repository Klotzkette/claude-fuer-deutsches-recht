---
name: ifap-nachtraegliche-anmeldung-177
description: "Verspätete und nachträgliche Forderungsanmeldungen nach § 177 InsO: Anwendungsfall Gläubiger meldet Forderung nach Ablauf der Anmeldefrist an oder ändert bereits angemeldete Forderung. § 177 InsO Nachtragsanmeldung, § 176 InsO Pruefungstermin, § 5 InsO Sondertermin. Pruefraster Fristablauf feststellen, Kostenpflicht bei Verspätung, Einordnung in Sondertermin oder schriftliches Verfahren. Output Verfahrensprotokoll mit Kostenbescheid und Terminzuordnung. Abgrenzung zu Formalprüfung-174 fuer rechtzeitige Anmeldungen und zu Pruefungstermin-176."
---

# Nachträgliche Anmeldung nach § 177 InsO

## Aufgabe

Ordnet späte und geänderte Anmeldungen in Prüfungstermin, Sondertermin oder schriftliches Verfahren ein.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung kommt nach Fristablauf
- Anmeldung wird geändert
- Prüfungstermin ist vorbei

## Workflow

1. Zeitpunkt der Anmeldung gegenüber Anmeldefrist und Prüfungstermin feststellen.
2. Prüfen, ob Prüfung im bestehenden Termin möglich ist oder besonderer Termin/schriftliches Verfahren nötig wird.
3. Kostenfolge und Säumigenhinweis als organisatorischen Punkt markieren.
4. Änderung von neuer Forderung unterscheiden.
5. Nachträgliche Prüfung in Tabellenstand und Wiedervorlagen einbauen.

## Ausgabe

- Nachtragsvermerk
- Termin-/Schriftverfahrensvorschlag
- Kostenhinweis
- aktualisierter Tabellenstatus

## Qualitätsgates

- Nachtrag wird nicht als neue Dublette behandelt, wenn er dieselbe Forderung ergänzt.
- Fristlage wird mit konkretem Datum ausgegeben.
- Alte und neue Beträge bleiben nachvollziehbar.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- BGH, Urt. v. 19.02.2009 — IX ZR 2/08, NZI 2009, 389 — Verwalterhaftung bei Tabellenfehlern: Pruefungsfehler begruenden persoenliche Haftung des IV aus § 60 InsO; Massstab ordentlicher Kaufmann; Glaeubiger-Schadensersatz wenn Forderung zu Unrecht nicht festgestellt.
- BGH, Urt. v. 22.09.2005 — IX ZB 55/04 — Pruefungstermin § 176 InsO: vollstaendige und richtige Tabelle Pflicht; Versaeumnis des IV kann Verzug-Schadensersatz ausloesen.
- BGH, Urt. v. 25.01.2007 — IX ZR 120/04, NZI 2007, 281 — Bestreiten im Pruefungstermin: Bestreiten durch IV muss begruendet sein; pauschales Bestreiten reicht nicht; IV muss konkrete Einwendungen erheben.
- BGH, Urt. v. 14.07.2016 — IX ZR 188/15, NZI 2016, 857 — Feststellungsklage § 180 InsO nach Bestreiten: Klagefrist und Zustaendigkeit; Verjaehrung gehemmt solange Prüfungstermin noch aussteht.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Bestreiten begruendet?** Konkrete Einwendungen formulieren (BGH IX ZR 120/04).

## Kommentarliteratur

- MüKo InsO/Riedel §§ 174-189 InsO Rn. 1 ff. — Forderungsanmeldung und Tabellenpruefung.
- Uhlenbruck/Sinz §§ 174-178 InsO Rn. 1 ff. — Tabellenwirkung und Feststellungsklage.
- Jaeger/Gerhardt § 178 InsO — Tabellenwirkung und Rechtskraft.

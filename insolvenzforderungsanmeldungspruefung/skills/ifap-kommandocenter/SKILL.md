---
name: ifap-kommandocenter
description: "Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen Prüfschritt finden. §§ 174-189 InsO Forderungsanmeldung und Pruefung. Pruefraster Verfahrensstand und Rolle erkennen, naechsten sicheren Schritt bestimmen, Fristen und Risiken anzeigen. Output Deal-Ampel mit Weiterleitung zum richtigen Spezial-Skill. Abgrenzung zu Intake-Kanalcheck fuer Eingangserfassung und zu Quality-Gate fuer Endkontrolle."
---

# Kommandocenter für die Forderungsprüfung

## Aufgabe

Steuert den gesamten Prüfpfad von Eingangsstapel bis Tabellen- und Streitnachlauf.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- neuer Eingangsstapel
- unklare Forderungsanmeldung
- Prüfungstermin steht bevor
- Tabelle muss bereinigt werden

## Workflow

1. Verfahrensdaten aufnehmen: Gericht, Aktenzeichen, Eröffnungsdatum, Anmeldefrist, Prüfungstermin, schriftliches Verfahren.
2. Material sortieren: Eingangskanal, Gläubiger, Forderungsart, Betrag, Rang, Belege, Titel und Nachträge.
3. Arbeitsmodus wählen: Einzelprüfung, Batchprüfung, Nachforderung, Tabellenimport, Prüfungstermin oder Streitnachlauf.
4. Rote Schwellen markieren: vbuH, Titel, Nachrang, Absonderung, Masseforderung, Arbeitnehmerforderung, Steuer/SV, Dublette.
5. Konkrete nächste Ausgabe erzeugen: Prüfplan, Rückfragenliste, Tabellenzeilen oder Entscheidungsvermerk.

## Ausgabe

- Prüfpfad mit Prioritäten
- offene Rückfragen
- nächster Skill-Vorschlag
- Risikoampel je Forderung

## Qualitätsgates

- Keine Feststellung ohne Belegkette.
- Jede streitige Forderung erhält einen Nachlaufvermerk.
- Fristen und Prüfungstermin werden sichtbar gemacht.

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

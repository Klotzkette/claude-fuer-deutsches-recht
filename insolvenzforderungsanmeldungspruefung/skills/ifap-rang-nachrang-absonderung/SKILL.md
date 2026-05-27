---
name: ifap-rang-nachrang-absonderung
description: "Rang Nachrang Absonderung und Aussonderung bei Insolvenzforderungen prüfen: Anwendungsfall Glaeubiger behauptet Sonderrechte wie Absonderungsrecht aus Sicherungsuebereignung oder Nachrang. §§ 38-39 InsO Insolvenzforderungen und Nachrang, §§ 49-51 InsO Absonderungsrecht, §§ 47-48 InsO Aussonderungsrecht. Pruefraster einfache Insolvenzforderung vs. Nachrang vs. Absonderung, Glaubhaftmachung Sicherheitsrecht, Ausfallforderung nach Verwertung. Output Rang-Klassifizierungsprotokoll mit Begruendung und Tabellenposition. Abgrenzung zu Formalprüfung und zu Pruefentscheidung."
---

# Rang, Nachrang und Sicherungsrechte

## Aufgabe

Prüft die insolvenzrechtliche Einordnung der Forderung und alle behaupteten Sonderrechte.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Nachrang ist angemeldet
- Sicherheit wird behauptet
- Ausfallforderung unklar
- Eigentumsvorbehalt steht im Raum

## Workflow

1. Regelrang nach § 38 InsO, Nachrang nach § 39 InsO und sonstige Rangangaben trennen.
2. Prüfen, ob Nachrang überhaupt zur Anmeldung aufgefordert wurde.
3. Absonderungsrechte erfassen: Sicherungsübereignung, Pfand, Grundpfandrecht, Forderungsabtretung, Eigentumsvorbehalt.
4. Ausfallforderung und Verwertungslage abfragen, wenn Sicherheit vorhanden ist.
5. Aussonderung von Forderungsanmeldung trennen, wenn Eigentum oder Herausgabe statt Quote gemeint ist.
6. Tabellenrang und Sonderrechtsvermerk getrennt formulieren.

## Ausgabe

- Rangmatrix
- Sicherheitenvermerk
- Ausfallstatus
- Rangkorrekturvorschlag

## Qualitätsgates

- Sicherungsrechte werden nicht allein aus Selbstauskunft festgestellt.
- Nachrang wird ausdrücklich bezeichnet.
- Aussonderung führt nicht automatisch zu einer Tabellenforderung.

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

---
name: ifap-formalpruefung-174
description: "Formalprüfung Forderungsanmeldung nach § 174 InsO: Anwendungsfall Insolvenzverwalter oder Pruefungsstelle prüft ob eingegangene Anmeldung Mindestangaben hat und tabellenfähig ist. § 174 InsO Pflichtinhalt, § 175 InsO Tabelle, § 176 InsO Pruefungstermin. Pruefraster Glaeubiger mit Anschrift, Forderungsgrund, Betrag, Nachrang, Urkundenvorlage, elektronische Einreichung EGVP. Output Formalprüfungsprotokoll mit gruener oder roter Ampel und Maengelschreiben-Vorlage. Abgrenzung zu Grund-Betrag-Zinsen fuer inhaltliche Pruefung und zu Intake-Kanalcheck."
---

# Formalprüfung nach § 174 InsO

## Aufgabe

Prüft, ob eine Forderungsanmeldung formal tabellenfähig ist oder gezielte Ergänzung braucht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung soll in die Tabelle
- Grund oder Betrag fehlen
- vbuH oder Nachrang ist angekreuzt

## Workflow

1. Prüfen, ob eine Anmeldung beim Verwalter vorliegt und welcher Gläubiger sie trägt.
2. Grund und Betrag isoliert erfassen, nicht aus Anlagen erraten, wenn die Anmeldung selbst leer bleibt.
3. Urkundenstatus prüfen: beigefügt, elektronisch, nachzureichen, unlesbar, nicht passend.
4. Nachranghinweis und Rangstelle prüfen, wenn nachrangige Forderung angemeldet ist.
5. vbuH, Unterhalt oder Steuerstraftat nur mit konkreten Tatsachen erfassen.
6. Mangelkategorie vergeben: heilbar, substanziell unklar, offensichtlich falscher Weg, Nachforderung erforderlich.

## Ausgabe

- § 174-Checkliste
- Mängelliste
- Nachforderungsvorschlag
- Status für Tabellenimport

## Qualitätsgates

- Grund und Betrag sind Pflichtachsen.
- Urkundenmangel wird nicht mit materiellem Bestreiten verwechselt.
- Elektronische Rechnung kann Urkunde sein, muss aber lesbar zuordenbar bleiben.

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

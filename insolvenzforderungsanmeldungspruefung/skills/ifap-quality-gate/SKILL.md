---
name: ifap-quality-gate
description: "Qualitätsgate vor Tabelleneintrag Prüfungstermin und Verteilung: Anwendungsfall alle Prüfschritte wurden durchgeführt und jetzt muss vor Versand oder Eintrag nochmals Vollstaendigkeit Plausibilitaet und Risiken geprüft werden. § 175 InsO Tabelle, § 176 InsO Pruefungstermin, § 189 InsO Verteilung. Pruefraster alle Pflichtfelder befüllt, Berechnungen plausibel, rote Risiken identifiziert, Quellen belegt. Output Qualitaetsprotokoll mit Ampelstatus und Freigabeentscheidung. Abgrenzung zu Kommandocenter als Einstieg und zu Pruefentscheidung."
---

# Qualitätsgate und Plausibilitätskontrolle

## Aufgabe

Stoppt unvollständige, unplausible oder zu riskante Ausgaben vor Import, Versand und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- vor Import
- vor Prüfungstermin
- vor Versand
- vor Verteilung
- bei hohem Risiko

## Workflow

1. Vollständigkeit prüfen: Anmeldung, Belege, Betrag, Rang, Status, Entscheidung, Bearbeiter, Datum.
2. Plausibilität prüfen: Summen, Zinsen, Dubletten, Titel, OPOS, Nachträge, Nachrang, vbuH, Masseabgrenzung.
3. Rechtsquellencheck: Normen nur aus aktueller amtlicher Quelle oder geprüfter Kanzleiquelle verwenden.
4. Ausgabecheck: verständlich, tabellentauglich, keine überschießende Rechtsberatung, keine geheimen internen Notizen im Außenbrief.
5. Freigabe verlangen, wenn rote Schwellen berührt sind.

## Ausgabe

- QA-Protokoll
- Korrekturliste
- Freigabevermerk
- Rest-Risiko-Liste

## Qualitätsgates

- Rote Schwellen stoppen den Automatismus.
- Jede Zahl muss aus Quelle oder Rechnung herleitbar sein.
- Außenkommunikation und interne Bewertung bleiben getrennt.

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

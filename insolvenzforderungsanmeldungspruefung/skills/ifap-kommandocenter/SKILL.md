---
name: ifap-kommandocenter
description: "Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen Prüfschritt finden. §§ 174-189 InsO Forderungsanmeldung und Prüfung. Prüfraster Verfahrensstand und Rolle erkennen, naechsten sicheren Schritt bestimmen, Fristen und Risiken anzeigen. Output Deal-Ampel mit Weiterleitung zum richtigen Spezial-Skill. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Quality-Gate für Endkontrolle."
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
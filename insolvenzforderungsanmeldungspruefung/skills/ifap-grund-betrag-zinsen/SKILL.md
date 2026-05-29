---
name: ifap-grund-betrag-zinsen
description: "Anspruchsgrund Betrag und Zinsen der Insolvenzforderung prüfen: Anwendungsfall Insolvenzverwalter prüft ob angemeldeter Betrag rechnerisch korrekt und durch Anspruchsgrundlage gedeckt ist. § 174 InsO Forderungsanmeldung, §§ 38-39 InsO Insolvenzforderungen, BGB Verzugszinsen § 288. Prüfraster Hauptforderung aufschlüsseln, Teilzahlungen und Gutschriften abziehen, Zinsberechnung prüfen, Kostenpositionen prüfen. Output Berechnungsprotokoll mit Sollbetrag, Abweichungsampel und Korrekturbedarf. Abgrenzung zu Formalprüfung-174 und zu Beleg-Urkundencheck."
---

# Grund, Betrag und Zinsen

## Aufgabe

Zerlegt die angemeldete Forderung in prüfbare Teilpositionen und macht Rechenfehler sichtbar.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Betrag passt nicht zu Belegen
- Zinsen sind angemeldet
- Teilzahlungen oder Gutschriften stehen im Raum

## Workflow

1. Anspruchsgrund konkretisieren: Vertrag, Lieferung, Dienstleistung, Darlehen, Steuer, Lohn, Schaden, Kosten, Titel.
2. Hauptforderung aus Anmeldung und Belegen in Teilpositionen zerlegen.
3. Teilzahlungen, Gutschriften, Aufrechnungen, Skonto, Storno und Sicherheiten abziehen oder als ungeklärt markieren.
4. Zinsen prüfen: Beginn, Zinssatz, Zeitraum bis Eröffnung, Rechtsgrund, Verzugsnachweis, titulierte Zinsen.
5. Kosten prüfen: Mahnkosten, Rechtsverfolgungskosten, Gerichtskosten, Inkasso, tituliert oder nicht tituliert.
6. Feststellbarer und zu bestreitender Betrag getrennt ausgeben.

## Ausgabe

- Betragsrechnung
- Zinsrechnung
- Teilbestreitensvorschlag
- Rechenprotokoll

## Qualitätsgates

- Zinsen nach Verfahrenseröffnung werden nicht blind als Insolvenzforderung übernommen.
- Teilzahlungen werden quellenbezogen dokumentiert.
- Rundungs- und Währungsfragen werden offengelegt.

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
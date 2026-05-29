---
name: ifap-dubletten-serienforderungen
description: "Dubletten und Serienforderungen in Insolvenzanmeldungen erkennen: Anwendungsfall mehrere Gläubiger melden gleichartige oder identische Forderungen an; Inkassounternehmen und Originalgläubiger reichen parallel ein. § 174 InsO Forderungsanmeldung, § 178 InsO Tabelle Bestreiten. Prüfraster Doppelerfassung gleicher Rechnung, Serienrechnungen mit laufenden Nummern, Konzernforderungen und Vertreterwechsel, mehrfach eingereichte Titel. Output Dublettenprotokoll mit Unterscheidung echte Dublette vs. Serienforderung. Abgrenzung zu Aktenanlage-Batchregister und zu Formalprüfung."
---

# Dubletten und Serienforderungen

## Aufgabe

Findet Mehrfachanmeldungen und trennt echte Dubletten von ähnlichen Serienforderungen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- gleiche Rechnung mehrfach
- Inkasso und Gläubiger melden parallel
- Konzernmeldungen überschneiden sich

## Workflow

1. Vergleichsschlüssel bilden: Gläubiger, Schuldnerkonto, Rechnungsnummer, Betrag, Zeitraum, Titel, Vertragsnummer.
2. Exakte Dubletten, wahrscheinliche Dubletten und bloß ähnliche Serienforderungen unterscheiden.
3. Vertreterwechsel und Inkasso-Zessionen prüfen: Forderungsinhaber, Vollmacht, Abtretung, Prozessstandschaft.
4. Bei Teilabtretungen und Konsortialforderungen Quoten und Teilbeträge trennen.
5. Entscheidung vorschlagen: zusammenführen, Nachweis verlangen, teilweise bestreiten, Doppelanmeldung bestreiten.

## Ausgabe

- Dublettenreport
- Zusammenführungsplan
- Zessions-/Vertretercheck
- Bestreitensvermerk

## Qualitätsgates

- Ähnliche Beträge sind nicht automatisch Dubletten.
- Inkassovertretung ist nicht Forderungsinhaberschaft.
- Zusammenführung bleibt im Audit-Trail nachvollziehbar.

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
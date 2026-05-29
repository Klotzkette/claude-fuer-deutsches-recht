---
name: ifap-tabellenimport-175
description: "Tabelleneintrag und Tabellenimport nach § 175 InsO: Anwendungsfall Forderungen sind geprüft und muessen in gerichtliche Tabelle überführt werden oder CSV-Import in Verwaltungssoftware vorbereitet werden. § 175 InsO Tabelle, § 176 InsO Prüfungstermin, Inso-Table-Standard. Prüfraster Gläubiger Anspruchsgrund Betrag Rang vbuH Widerspruch Prüfstatus vollständig. Output tabellenfähige Ausgabe mit Import-Format und Prüfprotokoll. Abgrenzung zu Prüfentscheidung und zu Tabellenauszug-178."
---

# Tabellenimport nach § 175 InsO

## Aufgabe

Überführt geprüfte Forderungen in eine saubere Tabellenstruktur.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Tabelle soll angelegt werden
- CSV-Import wird gebraucht
- gerichtlicher Arbeitsstand ist zu liefern

## Workflow

1. Pflichtspalten aus Verfahrenspraxis definieren: laufende Nummer, Gläubiger, Vertreter, Grund, Betrag, Rang, Status.
2. § 174-Angaben in Tabellenlogik übertragen, ohne Begründungen zu verlieren.
3. vbuH, Unterhalt, Steuerstraftat und Schuldnerhinweis gesondert kennzeichnen.
4. Bestreiten von Verwalter, Schuldner oder Gläubiger getrennt abbilden.
5. Exportformat als CSV und menschenlesbare Prüfliste ausgeben.

## Ausgabe

- Tabellenimport.csv
- Tabellenarbeitsstand
- Fehlerliste
- Importnotiz

## Qualitätsgates

- Keine Tabellenzeile ohne Prüfnummer.
- Widerspruchsperson wird getrennt vom Forderungsstatus erfasst.
- Sonderzeichen und Dezimalformate werden vor Import kontrolliert.

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
---
name: ifap-beleg-und-urkundencheck
description: "Belege und Urkunden bei Insolvenzforderungsanmeldung prüfen: Anwendungsfall Gläubiger legt Rechnungen Verträge Titel Lieferscheine Kontoauszüge vor; Insolvenzverwalter oder Prüfungsstelle muss Belegkette aufbauen und Beweiswert einordnen. § 174 InsO Anmeldepflicht Urkunden, § 180 InsO streitige Forderung. Prüfraster vollständige Belegkette prüfen, Originale vs. Kopien, Lesbarkeit, Titel-Nachweis, Zuordnung zur Forderungssumme. Output Belegcheckliste mit Beweiswert-Ampel und Nachforderungsbedarf. Abgrenzung zu Formalprüfung-174 und zu Grund-Betrag-Zinsen."
---

# Beleg- und Urkundencheck

## Aufgabe

Bildet die Belegkette der Anmeldung und trennt belastbare Nachweise von bloßem Vortrag.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anlagenstapel ist unübersichtlich
- Rechnungen fehlen
- Titel wird behauptet
- Buchhaltung widerspricht

## Workflow

1. Alle Belege inventarisieren: Typ, Datum, Nummer, Parteien, Betrag, Zeitraum, Datei, Lesbarkeit.
2. Belege der konkreten Forderungsposition zuordnen und Fremdbelege aussortieren.
3. Titelstatus prüfen: vollstreckbarer Titel, Endurteil, Mahnbescheid, Vergleich, Kostenfestsetzung, bloße Rechnung.
4. Schuldnerbuchhaltung und OPOS abgleichen: gebucht, bestritten, bezahlt, storniert, Gegenforderung, Skonto.
5. Lücken markieren und konkrete Nachforderung formulieren.

## Ausgabe

- Belegkettenmatrix
- Titelvermerk
- OPOS-Abgleich
- fehlende Urkunden

## Qualitätsgates

- Ein Titel ersetzt nicht automatisch die Rangprüfung.
- Ein OPOS-Eintrag ersetzt nicht automatisch den Rechtsgrund.
- Unlesbare oder fremdsprachige Belege erhalten eigenen Prüfstatus.

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
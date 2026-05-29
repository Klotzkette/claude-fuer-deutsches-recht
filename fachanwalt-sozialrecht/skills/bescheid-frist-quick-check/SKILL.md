---
name: bescheid-frist-quick-check
description: "60-Sekunden-Sofortprüfung der Frist eines sozialrechtlichen Bescheids. Eingabe Datum der Bekanntgabe (Zugang) und Datum des Bescheids und Status der Rechtsbehelfsbelehrung. Berechnung Widerspruchsfrist § 84 SGG ein Monat ab Bekanntgabe. Bei fehlender oder unrichtiger Rechtsbehelfsbelehrung ein Jahr ab Bekanntgabe nach § 66 Abs. 2 SGG. Bekanntgabe-Fiktion bei einfachem Brief vier Tage ab Aufgabe zur Post § 37 Abs. 2 SGB X n.F. (seit 1.1.2025 PostModG; davor drei Tage). Endet mit Ampel rot (verstrichen) gelb (knapp unter zwei Wochen) gruen (komfortabel) plus Frist-Datum und Vorfrist-Datum. Vorschalt-Skill für alles weitere. Prüfung Wiedereinsetzung § 67 SGG bei roter Ampel. Prüfung § 44 SGB X Überprüfungsantrag wenn Wiedereinsetzung ausgeschlossen."
---

# Frist-Quick-Check

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Sofort-Eingangstür zu jedem Bescheid. Vor Bescheidanalyse, vor Widerspruchsentwurf. **Nichts** vorher tun.

## Eingabe

- Datum auf dem Bescheid
- Datum der Bekanntgabe (Zugang, Posteingang)
- Hat der Bescheid eine **Rechtsbehelfsbelehrung**? (ja / nein / unklar / nur teilweise)
- Versandweg (einfacher Brief / Postzustellungsurkunde PZU / Einschreiben mit Rueckschein / elektronisch)

## Rechtsgrundlagen — Kompakt

| Norm | Inhalt |
|---|---|
| § 84 Abs. 1 SGG | Widerspruchsfrist ein Monat ab Bekanntgabe |
| § 66 Abs. 1 SGG | Frist läuft nur bei korrekter Rechtsbehelfsbelehrung |
| § 66 Abs. 2 SGG | Bei fehlender / unrichtiger Belehrung ein Jahr ab Bekanntgabe |
| § 37 Abs. 2 SGB X n.F. | Bekanntgabe-Fiktion einfacher Brief — am vierten Tag nach Aufgabe zur Post (seit 1.1.2025 PostModG; bei Aufgabe vor dem 1.1.2025: dritter Tag a.F.) |
| § 87 SGG | Klagefrist ein Monat nach Zustellung Widerspruchsbescheid |
| § 67 SGG | Wiedereinsetzung in den vorigen Stand bei unverschuldeter Versaeumung |
| § 44 SGB X | Überprüfungsantrag — auch nach Bestandskraft |
| § 86b SGG | Eilrechtsschutz beim Sozialgericht |

## Algorithmus

Schritt 1 — Bekanntgabe bestimmen:
- PZU oder Einschreiben mit Rueckschein → Datum auf Urkunde
- Einfacher Brief → drei Tage nach Aufgabe zur Post (Datum auf Bescheid plus drei Tage, sofern nicht Mandant früheres Zugangsdatum angibt)
- Elektronisch über Postfach → tatsächliches Abrufdatum, spaetestens drei Tage

Schritt 2 — Fristbeginn ist der Tag nach Bekanntgabe (§ 26 Abs. 1 SGB X iVm § 187 Abs. 1 BGB).

Schritt 3 — Fristende ist eine Monat später, abends 24 Uhr, ggf. mit § 26 Abs. 3 SGB X (Wochenende, Feiertag).

Schritt 4 — Falls Rechtsbehelfsbelehrung fehlt oder fehlerhaft: Frist ist ein Jahr.

## Ampel

| Status | Verbleibende Tage | Sofortaktion |
|---|---|---|
| GRUEN | mehr als 14 | normale Bearbeitung, Akteneinsicht parallel |
| GELB | 4 bis 14 | Vorrang Widerspruch heute oder morgen, Begründung nachreichen § 84 Abs. 1 SGG |
| ROT | weniger als 4 | sofort Widerspruchsschreiben "dem Grunde nach" — Begründung folgt |
| VERSTRICHEN | minus | Wiedereinsetzung § 67 SGG prüfen, ggf. § 44 SGB X |
| EILBEDARF | egal | parallel `eilantrag-sozialrecht` |

## Output-Format

Liefere immer diese genau drei Zeilen plus Aktion:

```
FRIST-QUICK-CHECK [Mandant] — [Az]

Bekanntgabe: [TT.MM.JJJJ] (Grundlage: [PZU / Brief plus vier Tage § 37 Abs. 2 SGB X n.F. / Mandantenangabe])
Frist Widerspruch: [TT.MM.JJJJ] — verbleibend [N Tage]
Belehrung: [korrekt / fehlt / unrichtig — Konsequenz: Frist Monat / Jahr]
Ampel: [GRUEN / GELB / ROT / VERSTRICHEN / EILBEDARF]
Sofort: [konkrete erste Handlung heute]
```

## Wiedereinsetzung § 67 SGG — Kurzprüfung

Voraussetzungen alle:
- Frist unverschuldet versäumt (Krankheit, Naturkatastrophe, kein Verschulden der Anwaltschaft auf den Mandanten zugerechnet § 73 Abs. 6 SGG iVm § 85 ZPO)
- Antrag binnen zwei Wochen nach Wegfall des Hindernisses
- Glaubhaftmachung (Attest, Bestätigung)
- Nachholung der versäumten Handlung im selben Schriftsatz

Wenn nicht alle erfüllt → kein Wiedereinsetzungsantrag, stattdessen `§ 44 SGB X` Überprüfungsantrag prüfen.

## Faustregel Bestandskraft und § 44

§ 44 Abs. 1 SGB X greift, wenn der Bescheid **rechtswidrig** war und der Mandant deshalb zu wenig oder gar keine Leistung erhalten hat. Rueckwirkung max. vier Jahre § 44 Abs. 4 SGB X. Antragsstellung jederzeit möglich.

## Anschluss-Skills

| Ergebnis | Nächster Skill |
|---|---|
| Ampel grün oder gelb | `bescheidanalyse` |
| Ampel rot | `widerspruch-formulieren` (Kurzfassung dem Grunde nach) |
| Ampel verstrichen, Wiedereinsetzung möglich | `widerspruch-formulieren` mit Antrag § 67 SGG |
| Ampel verstrichen, keine Wiedereinsetzung | Prüfung § 44 SGB X (eigenständiger Pfad) |
| Eilbedarf | `eilantrag-sozialrecht` parallel |

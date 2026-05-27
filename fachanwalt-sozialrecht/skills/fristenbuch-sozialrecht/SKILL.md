---
name: fristenbuch-sozialrecht
description: "Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und ueberwachen. Fristenbuch Sozialrecht. Standardfristen: § 84 SGG Widerspruch 1 Monat § 87 SGG Klage 1 Monat § 173 SGG Beschwerde 1 Monat Untaetigkeit § 88 SGG 6 Monate. Berechnung nach § 37 SGB X (Vier-Tage-Fiktion seit 1.1.2025 PostModG) und § 26 SGB X. Output: Fristenbuch-Eintrag mit Hauptfrist und Vorfristen. Abgrenzung zu bescheid-frist-quick-check (Schnellpruefung Einzelfall) und widerspruchsfrist-und-zustellung-sgb (Detailpruefung Zustellung)."
---

# Fristenbuch Sozialrecht

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/fristenbuch.yaml`

Pro Eintrag:

```yaml
- mandat-az: SR-2026-0042
  mandant: Mueller, Hans
  vorgang: Bürgergeld-Bescheid 12.03.2026
  fristart: widerspruchsfrist
  rechtsgrundlage: "§ 84 Abs. 1 SGG"
  fristbeginn: 2026-03-16  # Zugang nach Vier-Tages-Fiktion § 37 Abs. 2 SGB X n.F. (PostModG, seit 1.1.2025): Aufgabe zur Post 12.03.2026 + 4 Tage = 16.03.2026
  hauptfrist: 2026-04-16
  vorfrist-tage: 5
  vorfrist: 2026-04-11
  zustaendig: RA Mueller
  status: offen
  bemerkung: Widerspruchsbegründung benoetigt Akteneinsicht
```

## Standardfristen

### SGG

| Frist | Norm | Dauer |
|---|---|---|
| Widerspruchsfrist | § 84 Abs. 1 SGG | ein Monat ab Bekanntgabe; ein Jahr bei fehlender Rechtsbehelfsbelehrung § 66 Abs. 2 SGG |
| Klagefrist nach Widerspruchsbescheid | § 87 Abs. 1 SGG | ein Monat |
| Untätigkeitsklage | § 88 SGG | drei Monate Untätigkeit der Behörde |
| Beschwerde gegen Beschlüsse des SG | § 173 SGG | ein Monat |
| Berufung gegen Urteile des SG | § 151 SGG | ein Monat |
| Revisionsfrist | § 164 SGG | ein Monat |
| Wiedereinsetzung | § 67 SGG | zwei Wochen ab Wegfall des Hindernisses |

### SGB X / SGB V

| Frist | Norm | Bedeutung |
|---|---|---|
| Vier-Tages-Fiktion Zustellung (seit 1.1.2025) | § 37 Abs. 2 SGB X n.F. | Bekanntgabe vier Tage nach Aufgabe zur Post (PostModG; bis 31.12.2024: drei Tage) |
| Genehmigungsfiktion Krankenkasse | § 13 Abs. 3a SGB V | drei Wochen (fünf Wochen bei MDK) |
| Entscheidungsfrist Reha-Antrag | § 18 SGB IX | zwei Monate |
| Überprüfungsantrag | § 44 SGB X | keine eigentliche Frist aber Wirkung nur für Vergangenheit |

## Berechnung Fristbeginn

- **Postzustellung** vier Tage nach Aufgabe (§ 37 Abs. 2 SGB X n.F., seit 1.1.2025 PostModG). Wenn nachweislich früherer Zugang: Zugang maßgeblich. Für Verwaltungsakte mit Aufgabe zur Post vor dem 1.1.2025 gilt die alte Drei-Tages-Frist.
- **EGVP / beA** Tag der erfolgreichen Übertragung.
- **Bekanntgabe durch Aushaendigung** Tag der Aushaendigung.
- **Fristberechnung** § 26 SGB X iVm §§ 187 ff. BGB — Beginn des Folgetages; Ende mit Ablauf des entsprechenden Tages des letzten Monats; bei Wochenende / Feiertag auf nächsten Werktag.

## Vorfristen

- Standard fünf Werktage vor Hauptfrist.
- Bei Klagefristen Vorfrist mindestens sieben Tage (Akteneinsicht beA-Versand Anlagenkonvolut).
- Eskalation bei Vorfrist-Erreichung an zuständigen Anwalt.

## Pflege

- Bei Eingang Bescheid: sofort Eintrag im Fristenbuch.
- Bei Eingang Widerspruchsbescheid: Eintrag Klagefrist.
- Bei Untätigkeit der Behörde: Eintrag Drei-Monats-Frist Untätigkeitsklage.
- Bei Bewilligung mit Änderungsvorbehalt: ggf. Wiedervorlage.

## Ausgabe

- `fristenbuch.yaml` aktualisiert
- `fristen-uebersicht.md` als Sekretariats-Bericht (Tagesbericht nächste sieben Tage)
- Bei Vorfristerreichung: Erinnerungs-Eintrag im Sekretariats-Tagesbrief (Plugin `kanzlei-allgemein`)

## Sicherheit

- Niemals Fristen ändern ohne dokumentierte Begründung.
- Audit-Trail in der Aktenchronik.
- Sekretariat und Anwalt gegenseitig prüfen.

## Triage — kläre bei jedem neuen Fristeneintrag

1. Versanddatum des Bescheids auf dem Dokument angegeben? — Vier-Tages-Fiktion § 37 Abs. 2 SGB X n.F. ab Aufgabedatum
2. Nachweislich früherer Zugang beim Mandanten? — dann Zugangsdatum maßgeblich, Fiktion weicht zurück
3. Rechtsbehelfsbelehrung vorhanden und korrekt? — bei Fehler Jahresfrist § 66 Abs. 2 SGG
4. Feiertag oder Wochenende am Fristende? — Verlängerung auf nächsten Werktag § 26 SGB X iVm § 193 BGB analog
5. Sekretariat und verantwortlicher Anwalt im Fristenbuch eingetragen? — Vier-Augen-Prinzip für Kanzleisicherung

## Aktuelle Rechtsprechung

- BSG, Urt. v. 06.05.2010 - B 14 AS 12/09 R, SozR 4-1300 § 37 Nr. 1 Rn. 15 — Die Drei-Tages-Fiktion (jetzt vier Tage nach PostModG) des § 37 Abs. 2 SGB X gilt auch dann, wenn der Bescheid tatsächlich früher zuging; maßgeblich ist der fingierte Zeitpunkt, sofern kein abweichender Zugang beweisbar ist.
- BSG, Urt. v. 26.05.2011 - B 14 AS 54/10 R, SozR 4-1500 § 84 Nr. 4 Rn. 17 — Bei fehlender oder fehlerhafter Rechtsbehelfsbelehrung beginnt die Jahresfrist des § 66 Abs. 2 SGG mit der Bekanntgabe des Bescheids; ein erneutes Jahr läuft ab dem Zeitpunkt der Heilung durch nachträgliche Belehrung.
- BSG, Urt. v. 17.07.2014 - B 14 AS 25/13 R, SozR 4-1500 § 67 Nr. 3 Rn. 21 — Wiedereinsetzung in den vorigen Stand nach § 67 SGG setzt unverschuldetes Hindernis und unverzüglichen Antrag (zwei Wochen ab Wegfall) voraus; Verschulden des Prozessbevollmächtigten wird dem Mandanten zugerechnet.
- BSG, Urt. v. 29.11.2012 - B 14 AS 196/11 R, SozR 4-1300 § 26 Nr. 2 Rn. 12 — Die Fristberechnung nach § 26 SGB X folgt den §§ 187 ff. BGB; fällt das Ende einer Frist auf einen Sonnabend, Sonntag oder gesetzlichen Feiertag, endet sie am nächsten Werktag.

## Kommentarliteratur

- Kasseler Kommentar Sozialversicherungsrecht, Steinwedel § 37 SGB X Rn. 1 ff. (Bekanntgabe, Zugangsfiktionen)
- Krasney/Udsching, Handbuch des Sozialgerichtsprozesses, Kap. IV Rn. 60 ff. (Fristen, Wiedereinsetzung)

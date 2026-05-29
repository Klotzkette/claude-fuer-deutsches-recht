---
name: fristenbuch-sozialrecht
description: "Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und ueberwachen. Fristenbuch Sozialrecht. Standardfristen: § 84 SGG Widerspruch 1 Monat § 87 SGG Klage 1 Monat § 173 SGG Beschwerde 1 Monat Untätigkeit § 88 SGG 6 Monate. Berechnung nach § 37 SGB X (Vier-Tage-Fiktion seit 1.1.2025 PostModG) und § 26 SGB X. Output: Fristenbuch-Eintrag mit Hauptfrist und Vorfristen. Abgrenzung zu bescheid-frist-quick-check (Schnellprüfung Einzelfall) und widerspruchsfrist-und-zustellung-sgb (Detailprüfung Zustellung)."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
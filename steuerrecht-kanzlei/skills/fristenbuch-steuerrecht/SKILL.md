---
name: fristenbuch-steuerrecht
description: Fristenbuch fuer steuerrechtliche Verfahren — pflegt zentrale Datei mit Hauptfristen und Vorfristen. Standardfristen AO (§ 355 Einspruch ein Monat / § 356 ein Jahr bei fehlender Rechtsbehelfsbelehrung) FGO (§ 47 Klage ein Monat / § 116 Nichtzulassungsbeschwerde ein Monat / § 120 Revisionsbegruendung zwei Monate). Berechnet Fristbeginn nach § 122 Abs. 2 AO Drei-Tages-Fiktion und § 108 AO Fristberechnung. Vorfristen typisch fuenf Tage vor Hauptfrist.
---

# Fristenbuch Steuerrecht

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-kanzlei/fristenbuch.yaml`

```yaml
- mandat-az: ST-2026-0042
  mandant: Mueller GmbH
  vorgang: USt-Bescheid 2024 vom 12.03.2026
  fristart: einspruchsfrist
  rechtsgrundlage: "§ 355 Abs. 1 AO"
  fristbeginn: 2026-03-15
  hauptfrist: 2026-04-15
  vorfrist-tage: 5
  vorfrist: 2026-04-10
  zustaendig: RA Mueller
  status: offen
  bemerkung: AdV-Antrag separat einreichen
```

## Standardfristen

### AO

| Frist | Norm | Dauer |
|---|---|---|
| Einspruchsfrist | § 355 Abs. 1 AO | ein Monat ab Bekanntgabe; ein Jahr bei fehlender Rechtsbehelfsbelehrung § 356 AO |
| Antragsfrist auf schlichte Änderung | § 172 Abs. 1 Nr. 2 AO | ein Monat |
| Festsetzungsverjährung regelmäßig | § 169 Abs. 2 Nr. 2 AO | vier Jahre |
| Festsetzungsverjährung bei Hinterziehung | § 169 Abs. 2 Satz 2 AO | zehn Jahre |
| Festsetzungsverjährung bei Leichtfertigkeit | § 169 Abs. 2 Satz 2 AO | fünf Jahre |
| Antrag auf Stundung / Erlass | §§ 222 227 AO | keine Frist; Fälligkeit beobachten |
| Wiedereinsetzung | § 110 AO | ein Monat nach Wegfall des Hindernisses |

### FGO

| Frist | Norm | Dauer |
|---|---|---|
| Klagefrist | § 47 Abs. 1 FGO | ein Monat ab Bekanntgabe Einspruchsentscheidung |
| Untätigkeitsklage möglich | § 46 FGO | nach sechs Monaten ohne Einspruchsentscheidung |
| AdV-Antrag an FG | § 69 FGO | keine eigene Frist |
| Nichtzulassungsbeschwerde | § 116 Abs. 2 FGO | ein Monat |
| Revisionsbegründung | § 120 Abs. 2 FGO | zwei Monate |
| Aussetzungszinsen | § 237 AO | bei Verlust 0,15 Prozent pro Monat |

## Bekanntgabe (§ 122 AO)

- **Schriftliche Bescheide per Post** drei Tage nach Aufgabe zur Post (§ 122 Abs. 2 Nr. 1 AO).
- **Elektronische Bescheide** drei Tage nach Absendung (§ 122a AO).
- Beweispflicht der Behörde wenn Zugang bestritten.

## Fristberechnung § 108 AO

- Beginn am Folgetag der Bekanntgabe (§ 187 BGB analog).
- Ende mit Ablauf des entsprechenden Tages des letzten Monats (§ 188 BGB analog).
- Bei Wochenende / Feiertag auf nächsten Werktag.

## Vorfristen

- Standard fünf Werktage vor Hauptfrist.
- Bei Klagefristen Vorfrist sieben Tage (Akteneinsicht beA-Versand Anlagen).
- Eskalation bei Vorfrist an zuständigen Anwalt und Sekretariat.

## Sondere Fristen

### Steuererklärungspflicht (§ 149 AO)

- **Pflichtveranlagung** sieben Monate nach Ablauf des Kalenderjahrs (§ 149 Abs. 2 AO).
- **Bei steuerlicher Vertretung** durch Steuerberater Verlängerung bis Ende Februar des übernächsten Jahres (§ 149 Abs. 3 AO).

### USt-Voranmeldung (§ 18 UStG)

- **Monatlich** wenn Steuer im Vorjahr über 7500 EUR; **vierteljaehrlich** sonst.
- Frist bis zum 10. des Folgemonats Quartals.
- Dauerfristverlängerung um einen Monat möglich (§ 18 Abs. 6 UStG).

### Lohnsteueranmeldung (§ 41a EStG)

- **Monatlich** wenn LSt mehr als 5000 EUR; **vierteljaehrlich** zwischen 1080 und 5000 EUR; **jaehrlich** bis 1080 EUR.
- Frist bis zum 10. des Folgemonats / Folgequartals.

## Pflege und Audit

- Sofortige Eintragung bei Bescheideingang.
- Sekretariat und Anwalt gegenseitig prüfen.
- Audit-Trail bei jeder Friständerung.

## Ausgabe

- `fristenbuch.yaml` aktualisiert
- `fristen-uebersicht.md` Tagesbericht nächste sieben Tage
- Vorfristen-Erinnerung in Sekretariats-Tagesbrief (Plugin `kanzlei-cowork`)

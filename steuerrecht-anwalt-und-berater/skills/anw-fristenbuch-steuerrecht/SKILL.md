---
name: anw-fristenbuch-steuerrecht
description: "Fristenbuch für steuerrechtliche Verfahren pflegen und Fristen berechnen. Anwendungsfall neue Bescheide oder Entscheidungen eingegangen Fristen muessen sofort eingetragen und ueberwacht werden. Standardfristen Einspruch § 355 AO ein Monat fehlende Belehrung § 356 AO ein Jahr FG-Klage § 47 FGO ein Monat Nichtzulassungsbeschwerde § 116 FGO ein Monat Revisionsbegründung § 120 FGO zwei Monate. Berechnung Fristbeginn § 122 Abs. 2 AO Vier-Tages-Fiktion seit 01.01.2025 PostModG Fristberechnung § 108 AO. Vorfristen fuenf Tage vor Hauptfrist. Output strukturierte Fristentabelle mit Haupt- und Vorfristen."
---

# Fristenbuch Steuerrecht

## Triage — Sofortprüfung bei jedem neuen Mandat

1. Liegt ein Steuerbescheid vor? → Einspruchsfrist ein Monat (§ 355 Abs. 1 AO) sofort eintragen
2. Liegt eine Einspruchsentscheidung vor? → Klagefrist ein Monat (§ 47 Abs. 1 FGO) sofort eintragen
3. Fehlt die Rechtsbehelfsbelehrung oder ist sie fehlerhaft? → Jahresfrist (§ 356 AO), aber nicht warten — so früh wie möglich handeln
4. Liegt bereits Fristversäumnis vor? → Wiedereinsetzung § 110 AO prüfen (Frist ein Monat nach Wegfall des Hindernisses)
5. Besteht Festsetzungsverjährungs-Problematik (§ 169 AO)? → Ablaufhemmung prüfen (§ 171 AO)

## Aktuelle Rechtsprechung (Fristen)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/fristenbuch.yaml`

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
| Aussetzungszinsen | § 237 AO | bei Verlust 0.15 Prozent pro Monat |

## Bekanntgabe (§ 122 AO)

- **Schriftliche Bescheide per Post** vier Tage nach Aufgabe zur Post (§ 122 Abs. 2 Nr. 1 AO n.F., seit 1.1.2025; davor drei Tage).
- **Elektronische Bescheide** vier Tage nach Absendung (§ 122 Abs. 2a / § 122a Abs. 4 AO n.F., seit 1.1.2025; davor drei Tage).
- **Bekanntgabe von Verwaltungsakten mit Aufgabe zur Post vor dem 1.1.2025**: weiterhin Drei-Tages-Fiktion alter Fassung.
- Beweispflicht der Behörde wenn Zugang bestritten.

## Fristberechnung § 108 AO

- Beginn am Folgetag der Bekanntgabe (§ 187 BGB analog).
- Ende mit Ablauf des entsprechenden Tages des letzten Monats (§ 188 BGB analog).
- Bei Wochenende / Feiertag auf nächsten Werktag.

## Vorfristen

- Standard fünf Werktage vor Hauptfrist.
- Bei Klagefristen zum Finanzgericht Vorfrist sieben Tage (Akteneinsicht beA-Versand Anlagen — zum Gericht weiterhin über beA, § 52d FGO).
- Bei Einspruchs- und sonstigen Antragsfristen zum Finanzamt Vorfrist drei Werktage (Versand über ELSTER/ERiC, Brief oder Fax; **kein beA** an Finanzamt seit 6.12.2024, § 87a Abs. 1 S. 2 AO n.F.).
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
- Vorfristen-Erinnerung in Sekretariats-Tagesbrief (Plugin `kanzlei-allgemein`)

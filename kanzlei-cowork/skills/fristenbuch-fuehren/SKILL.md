---
name: fristenbuch-fuehren
description: Zentrales Fristenbuch fuer die Kanzlei mit Haupt- und Vorfristen ueber alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG seit 1.1.2025; bis 31.12.2024 drei Tage). Trennt Notfristen (BRAO-Haftungsrisiko) von Beobachtungsfristen. Setzt Vorfristen typisch fuenf Werktage vor Hauptfrist; bei BRAO-relevanten Notfristen sieben Werktage. Eskalation an Sekretariat und zustaendigen Anwalt bei Vorfristerreichung. Audit-Trail jeder Fristaenderung.
---

# Zentrales Fristenbuch der Kanzlei

## Pflicht

Jede Kanzlei muss ein Fristenbuch führen — die Versäumung einer Notfrist ist anwaltliche Pflichtverletzung mit Haftungsrisiko (§ 51 BRAO).

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-cowork/fristenbuch.yaml`

```yaml
- mandat-az: 2026/0042
  mandant: Mueller GmbH
  vorgang: Kundenklage
  fristart: berufungsfrist
  rechtsgrundlage: "§ 517 ZPO"
  fristbeginn: 2026-03-15
  hauptfrist: 2026-04-15
  vorfrist-tage: 7
  vorfrist: 2026-04-06
  zustaendig: RA Mueller
  status: offen
  bemerkung: Berufungsbegründung gemäß § 520 ZPO innerhalb von zwei Monaten
```

## Fristarten und Standardfristen

### Zivilprozess (ZPO)

| Frist | Norm | Dauer |
|---|---|---|
| Klageerwiderung | § 276 ZPO | nach gerichtlicher Setzung (regelmäßig zwei Wochen Notfrist plus zwei Wochen weitere Frist) |
| Berufung | § 517 ZPO | ein Monat ab Zustellung |
| Berufungsbegründung | § 520 ZPO | zwei Monate ab Zustellung |
| Revision | § 548 ZPO | ein Monat |
| Revisionsbegründung | § 551 ZPO | zwei Monate |
| Sofortige Beschwerde | § 569 ZPO | zwei Wochen Notfrist |
| Einspruch Versäumnisurteil | § 339 ZPO | zwei Wochen Notfrist |

### Arbeitsgericht (ArbGG)

| Frist | Norm | Dauer |
|---|---|---|
| Kündigungsschutzklage | § 4 KSchG | drei Wochen Notfrist |
| Berufung | § 66 ArbGG | ein Monat |

### Strafprozess (StPO)

| Frist | Norm | Dauer |
|---|---|---|
| Berufung | § 314 StPO | eine Woche Notfrist |
| Revision | § 341 StPO | eine Woche Notfrist |
| Revisionsbegründung | § 345 StPO | ein Monat |
| Beschwerde | § 311 StPO | eine Woche |

### Verwaltungsgericht (VwGO)

| Frist | Norm | Dauer |
|---|---|---|
| Widerspruchsfrist | § 70 VwGO | ein Monat |
| Klagefrist | § 74 VwGO | ein Monat |
| Berufungsantrag | § 124a VwGO | ein Monat (Zulassungsbeschwerde) |
| Eilrechtsschutz | § 80 Abs. 5 VwGO | keine eigene Antragsfrist |

### Sozialgericht (SGG) — siehe Plugin `sozialrecht-kanzlei`

### Finanzgericht (FGO) — siehe Plugin `steuerrecht-anwalt-und-berater`

### Familiengericht (FamFG)

| Frist | Norm | Dauer |
|---|---|---|
| Beschwerde | § 63 FamFG | ein Monat |
| Sofortige Beschwerde | § 64 FamFG | zwei Wochen |

## Notfrist vs Beobachtungsfrist

- **Notfristen** (Versäumnis = Verlust): Berufung Revision Kündigungsschutzklage. Vorfrist sieben Werktage.
- **Beobachtungsfristen** (z. B. Vorlauf zur Stellungnahme): Vorfrist drei bis fünf Werktage.

## Vier-Tages-Fiktionen (PostModG, seit 1.1.2025)

Durch das Postrechtsmodernisierungsgesetz (BGBl. 2024 I Nr. 236) wurden alle Bekanntgabe-Fiktionen einheitlich von drei auf vier Tage verlängert:

- **§ 270 ZPO n.F.** Schriftsatzzustellung
- **§ 122 Abs. 2 Nr. 1 AO n.F.** Steuerbescheid (auch § 122 Abs. 2a / § 122a Abs. 4 AO bei elektronischer Übermittlung)
- **§ 41 Abs. 2 VwVfG n.F.** Verwaltungsakt
- **§ 37 Abs. 2 SGB X n.F.** Sozialleistungsbescheid
- **§ 4 Abs. 2 VwZG n.F.** Zustellung gegen Empfangsbekenntnis (Verwaltungszustellung)

Beim Eintragen automatisch berücksichtigen — bei nachweislich früherem Zugang Zugang maßgeblich. Für Verwaltungsakte / Schriftstücke mit Aufgabe zur Post **vor dem 1.1.2025** gilt weiterhin die alte Drei-Tages-Fiktion.

## Vorfristen

- **Standard** fünf Werktage vor Hauptfrist.
- **Notfristen** sieben Werktage.
- **Berufungs-/Revisionsbegründung** zehn Werktage (zwei-Monats-Fristen).

## Workflow

1. **Eintragen** sofort bei Posteingang Bescheid Urteil Zustellung.
2. **Kontrolle** durch Sekretariat **und** zuständigen Anwalt (Vier-Augen-Prinzip).
3. **Vorfrist** loest Eintrag im Tagesbrief aus (Skill `sekretariats-tagesbrief`).
4. **Erledigung** mit Datum und Unterschrift / Initial.
5. **Audit** bei jeder Änderung Eintrag in Audit-Trail.

## Ausgabe

- `fristenbuch.yaml` aktualisiert
- `fristen-uebersicht.md` Tagesbericht nächste sieben und nächste vierzehn Tage
- Vorfristen-Erinnerung in `sekretariats-tagesbrief`
- Audit-Eintrag bei Änderungen

## Haftungshinweis

Das Fristenbuch ist nur so gut wie seine Pflege. Die Letztverantwortung liegt beim Anwalt. Bei Versäumnis Wiedereinsetzung prüfen (jeweilige Verfahrensordnung).

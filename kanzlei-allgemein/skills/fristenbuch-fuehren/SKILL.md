---
name: fristenbuch-fuehren
description: "Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG seit 1.1.2025; bis 31.12.2024 drei Tage). Trennt Notfristen (BRAO-Haftungsrisiko) von Beobachtungsfristen. Setzt Vorfristen typisch fuenf Werktage vor Hauptfrist; bei BRAO-relevanten Notfristen sieben Werktage. Eskalation an Sekretariat und zuständigen Anwalt bei Vorfristerreichung. Audit-Trail jeder Fristaenderung im Kanzlei Allgemein: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Zentrales Fristenbuch der Kanzlei

## Arbeitsbereich

Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG seit 1.1.2025; bis 31.12.2024 drei Tage). Trennt Notfristen (BRAO-Haftungsrisiko) von Beobachtungsfristen. Setzt Vorfristen typisch fuenf Werktage vor Hauptfrist; bei BRAO-relevanten Notfristen sieben Werktage. Eskalation an Sekretariat und zuständigen Anwalt bei Vorfristerreichung. Audit-Trail jeder Fristaenderung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um eine Notfrist (absolut haftungsrelevant: Rechtsmittelfristen) oder eine einfache gesetzliche Frist?
2. Nach welcher Verfahrensordnung laeuft die Frist (ZPO, StPO, VwGO, SGG, FGO, FamFG, AO)?
3. Gilt die neue Vier-Tages-Fiktion nach PostModG (ab 01.01.2025) oder noch die Drei-Tages-Fiktion?
4. Wer ist verantwortlicher Anwalt und wer ist Vertretung bei Abwesenheit?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung nach dem Zivilprozessrecht
- § 517 ZPO — Berufungsfrist ein Monat ab Zustellung des Urteils (Notfrist)
- § 548 ZPO — Revisionsfrist ein Monat ab Zustellung (Notfrist)
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion fuer Postsendungen ab 01.01.2025

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflicht

Jede Kanzlei muss ein Fristenbuch führen — die Versäumung einer Notfrist ist anwaltliche Pflichtverletzung mit Haftungsrisiko (§ 51 BRAO).

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/fristenbuch.yaml`

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

### Sozialgericht (SGG) — siehe Plugin `fachanwalt-sozialrecht`

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

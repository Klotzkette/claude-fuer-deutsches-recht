---
name: workflow-fristen-und-risikoampel
description: "Fristenund Risikoampel für das Plugin gewerblicher-rechtsschutz: strukturierte Fristenerfassung, Risikobewertung Grün/Gelb/Rot und sofortige Handlungsempfehlung. Für alle IP-Verfahren vom Erstgespräch bis zur Vollstreckung im Gewerblicher Rechtsschutz: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Workflow: Fristen und Risikoampel

## Arbeitsbereich

Fristenund Risikoampel für das Plugin gewerblicher-rechtsschutz: strukturierte Fristenerfassung, Risikobewertung Grün/Gelb/Rot und sofortige Handlungsempfehlung. Für alle IP-Verfahren vom Erstgespräch bis zur Vollstreckung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill erstellt eine **vollständige Fristenübersicht mit Risikoampel** für ein laufendes IP-Mandat. Er ist kein vollständiges Fristenbuch (s. `spezial-fristen-abschlussprodukt-und-uebergabe`), sondern das operative Werkzeug für die laufende Fristenkontrolle und Risikobewertung im Mandatsalltag.

Mandatsbezug: Wöchentlicher Fristencheck in der Kanzlei; Übergabe eines Mandats an Urlaubsvertretung; schnelle Lageeinschätzung bei einem parallelen Mandat-Portfolio.

## Risikoampel-System

### Ampelfarben und Bedeutung

| Ampel | Kriterien | Handlungspflicht |
|---|---|---|
| 🔴 ROT – Sofort | Frist in < 5 Werktagen; kritischer Tatbestand ohne Beleg | Sofortige Mandatsbearbeitung; ggf. Notfallroutine |
| 🟡 GELB – Diese Woche | Frist in 5–14 Tagen; Belege unvollständig; offene Mandantenentscheidung | Frist vorbereiten; Mandant kontaktieren |
| 🟢 GRÜN – Komfortabel | Frist > 14 Tage; alle Belege vorhanden; Mandat vorbereitet | Planmäßige Bearbeitung |
| ⚫ OFFEN | Frist nicht ermittelbar; weitere Klärung nötig | Klärung bis Ende des Tages |

## Standard-Fristencheck: Zehn Kategorien

### Kategorie 1 – EV-Vollziehungsfrist

```
Frist: § 929 Abs. 2 ZPO
Auslöser: Zustellung EV an Antragsteller
Dauer: 1 Monat
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
Nächster Schritt: _______________
```

### Kategorie 2 – Abmahnreaktionsfrist (gesetzt durch Abmahner)

```
Frist: Gesetzt im Abmahnschreiben
Auslöser: Datum Zustellung Abmahnung
Gesetzt auf: _______________ (Datum)
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
Nächster Schritt: _______________
```

### Kategorie 3 – DPMA-Widerspruchsfrist

```
Frist: § 42 Abs. 1 MarkenG
Auslöser: Veröffentlichung im Markenblatt
Dauer: 3 Monate
Veröffentlichungsdatum: _______________
Fristende: _______________
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 4 – EUIPO-Widerspruchsfrist

```
Frist: Art. 46 EUTMR
Dauer: 3 Monate ab Veröffentlichung
Veröffentlichungsdatum: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 5 – Patent-Einspruchsfrist

```
Frist: § 59 PatG / Art. 99 EPÜ
Dauer: 3 Monate (DPMA) / 9 Monate (EPA)
Erteilungsveröffentlichung: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 6 – Berufungs-/Rechtsmittelfrist

```
Frist: § 517 ZPO (Berufung) / § 548 ZPO (Revision)
Dauer: 1 Monat
Urteilszustellung: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 7 – Patent-Jahresgebühr

```
Frist: § 17 PatG
Fälligkeitsdatum: _______________
Mahngebühren-Frist (Nachzahlung): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 8 – Marken-Verlängerungsfrist

```
Frist: § 47 MarkenG / Art. 53 EUTMR
Ablauf Schutzperiode: _______________
Nachzahlungsfrist (6 Monate): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 9 – Verjährungsfrist

```
Frist: § 11 UWG / § 20 MarkenG / § 102 UrhG
Kenntnis-Datum: _______________
Fristende (3 Jahre): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 10 – Dringlichkeitsfrist EV

```
Frist: Gerichtspraxis (4–8 Wochen nach Erstkenntnis)
Erstkenntnis-Datum: _______________
Kritische Schwelle: _______________
Status: Dringlichkeit noch gegeben? [Ja / Grenzwertig / Nein]
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

## Fristenübersicht-Vorlage (Mandatsübergabe)

```
FRISTENÜBERSICHT – [Mandat]
Stand: [Datum]
Verantwortlich: [Anwalt]

| # | Fristart | Auslöser | Fristende | Restzeit | Ampel | Nächster Schritt |
|---|---|---|---|---|---|---|
| 1 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |
| 2 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |
| 3 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |

SOFORTMASSNAHMEN (ROT):
1. _______________
2. _______________

DIESE WOCHE (GELB):
1. _______________

OFFENE KLÄRUNGSPUNKTE:
1. _______________
```

## Notfallroutine bei roter Ampel

1. Anwalt sofort informieren.
2. Mandant sofort informieren.
3. Nächste Handlung identifizieren und delegieren.
4. Prüfen: Ist Fristverlängerung möglich? (z.B. § 929 Abs. 2 Satz 2 ZPO; EUIPO-Verlängerungsantrag)
5. Dokumentation: Alle Schritte in Akte festhalten.

## Quellenregel

- Fristen nur aus aktuellen Normen; gesetze-im-internet.de und dejure.org.
- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- [§ 42 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/42.html)
- Keine Pauschalangaben; Fristberechnungen immer im konkreten Fall prüfen.

## Anschluss-Skills

- `spezial-fristen-abschlussprodukt-und-uebergabe` – Vollständige Fristenmatrix
- `spezial-schutzrechts-fristennotiz-und-naechster-schritt` – Sofort-Fristennotiz
- `workflow-dokumentenintake` – Frist-Auslöser aus Dokumenten
- `evvollzug-neu-001` – EV-Vollziehungsfrist im Detail

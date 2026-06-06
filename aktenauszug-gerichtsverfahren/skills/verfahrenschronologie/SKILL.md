---
name: verfahrenschronologie
description: "Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben. Normen §§ 222 517 520 ZPO Fristberechnung im Aktenauszug Gerichtsverfahren: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Verfahrenschronologie

## Arbeitsbereich

Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben. Normen §§ 222 517 520 ZPO Fristberechnung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Die Verfahrenschronologie erfasst alle prozessualen Schritte in zeitlicher Reihenfolge. Sie unterscheidet sich von der Sachverhaltschronologie dadurch, dass sie ausschließlich innerhalb des Verfahrens liegende Handlungen und Ereignisse abbildet.

## Triage — kläre vor Erstellung

1. Liegt die Zustellungsurkunde der Klageschrift vor? (Fristbeginn für Klageerwiderung)
2. Wurden alle Urteile zugestellt? (Berufungsfrist läuft ab Zustellung!)
3. Haben beide Parteien Schriftsätze vorgelegt? Welche?
4. Sind Vollstreckungsmaßnahmen eingeleitet? (Pfändungsbeschluss, Zwangshypothek)

## Zentrale Normen (Verfahrensrecht)

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung im Verfahren
- §§ 517-520 ZPO — Berufung und Begründung (Fristen: 1 Monat / 2 Monate)
- §§ 548-551 ZPO — Revision (Fristen: 1 Monat / 2 Monate)
- § 329 ZPO — Verkündung von Beschlüssen
- § 310 ZPO — Verkündung des Urteils
- § 929 Abs. 2 ZPO — Vollziehungsfrist bei einstweiliger Verfügung (1 Monat)
- §§ 704-945 ZPO — Zwangsvollstreckung

## Rechtsprechung zu Verfahrensfristen und Zustellung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Was gehört hinein

- Klageeingang / Antragseingang beim Gericht
- Zahlung des Gerichtskostenvorschusses
- Zustellung der Klageschrift / des Arrestgesuchs
- Klageerwiderung und alle weiteren Schriftsätze (mit Datum)
- Richterliche Verfügungen und Hinweisbeschlüsse
- Beweisbeschlüsse
- Terminsladungen
- Mündliche Verhandlungen (mit Ergebnis / Protokollvermerk)
- Beweisaufnahme (Zeugenvernehmung, Sachverständigengutachten)
- Eingang von Gutachten
- Urteile und Beschlüsse (mit Tenor)
- Rechtsmittelfristen und Einlegung von Rechtsmitteln
- Vollstreckungsmaßnahmen

## Was nicht hinein gehört

- Außerprozessuale Ereignisse (→ Sachverhaltschronologie)
- Rechtliche Bewertungen der Schriftsätze

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des prozessualen Schritts] (Fundstelle: [Blatt])
- ** TT.MM.JJJJ — FRIST:** [Fristbezeichnung — z. B. Berufungsfrist] (Fundstelle: [Blatt])
```

## Hervorhebung von Fristen

Jede prozessrelevante Frist wird hervorgehoben und ans Ende der Chronologie als eigener Block wiederholt:

```
## Fristen und Termine (Übersicht)

| Frist / Termin | Datum | Status |
|---|---|---|
| Berufungsfrist (§ 517 ZPO) | TT.MM.JJJJ | laeuft |
| Begründungsfrist (§ 520 ZPO) | TT.MM.JJJJ | laeuft |
| Nächste mündliche Verhandlung | TT.MM.JJJJ | angesetzt |
```

## Beispiele

```
- **08.02.2023** Eingang der Klageschrift beim Landgericht Frankfurt am Main (Bl. 1)
- **15.02.2023** Anforderung des Gerichtskostenvorschusses (Bl. 5)
- **22.02.2023** Einzahlung des Gerichtskostenvorschusses durch Klägerin (Bl. 7)
- **03.03.2023** Zustellung der Klageschrift an Beklagte (Bl. 9)
- **14.04.2023** Eingang der Klageerwiderung (Bl. 12-45)
- **20.06.2023** Terminsladung zur mündlichen Verhandlung am 15.09.2023 (Bl. 48)
- **15.09.2023** Mündliche Verhandlung; Beweisbeschluss über Einholung Sachverständigengutachten (Bl. 60-62)
- **10.01.2024** Eingang des Sachverständigengutachtens (Bl. 80-140)
- **05.04.2024** Verkündung des Urteils; Klage abgewiesen (Bl. 200-215)
- **05.05.2024 — FRIST:** Berufungsfrist gemäß § 517 ZPO (einen Monat ab Zustellung)
```

## Besonderheiten nach Verfahrensart

**Eilverfahren:** Vollziehungsfrist des § 929 Abs. 2 ZPO besonders hervorheben.

**Strafverfahren:** Eröffnungsbeschluss, Ladungen, Hauptverhandlungstermine, Einlegung von Rechtsmitteln nach § 333 ff. StPO.

**Verwaltungsverfahren:** Widerspruchsverfahren als vorgelagerte Phase einschließen; Klagefrist des § 74 VwGO.

## Qualitätscheck

- [ ] Alle prozessualen Schritte erfasst?
- [ ] Chronologisch sortiert?
- [ ] Fristen hervorgehoben?
- [ ] Fristentabelle vorhanden?
- [ ] Keine außerprozessualen Ereignisse enthalten?
- [ ] Zustellungsdaten als Grundlage der Fristberechnung angegeben?

---

---
name: strafbefehl-tagessaetze-geldstrafe
description: "Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenzahlungsantrag § 42 StGB. Ersatzfreiheitsstrafe § 43 StGB im Strafbefehl Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Tagessaetze und Geldstrafe — §§ 40 bis 43 StGB

## Arbeitsbereich

Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenzahlungsantrag § 42 StGB. Ersatzfreiheitsstrafe § 43 StGB. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. **Wie viele Tagessaetze sind im Strafbefehl festgesetzt?** — Anzahl bestimmt Schuldgewicht, Hoehe das Nettoeinkommen.
2. **Tagessatzhoehe korrekt?** — Nettoeinkommen / 30 = Tagessatz (§ 40 Abs. 2 StGB); zu hoch wenn Einkommen ueberschaetzt.
3. **Liegt Einkommensnachweis vor?** — Lohnabrechnung, Steuerbescheid, BWA bei Selbststaendigen.
4. **Ratenzahlung noetig?** — § 42 StGB: Gericht kann Ratenzahlung gestatten; Antrag bei Zahlungsunfaehigkeit.
5. **Kann Geldstrafe nicht bezahlt werden?** — Ersatzfreiheitsstrafe droht (§ 43 StGB: 1 Tag Freiheitsstrafe pro uneinbringlichem Tagessatz).

## Zentrale Normen

- **§ 40 Abs. 1 StGB** — Geldstrafe: 5 bis 360 Tagessaetze (bei Mehrfachverstoss bis 720)
- **§ 40 Abs. 2 StGB** — Tagessatz: Dreissigstel des monatlichen Nettoeinkommens; Mindest 1 EUR
- **§ 40 Abs. 2 Satz 3 StGB** — Schaetzungsrecht des Gerichts wenn genaues Einkommen nicht feststellbar
- **§ 41 StGB** — Geldstrafe neben Freiheitsstrafe moeglich
- **§ 42 StGB** — Zahlungserleichterungen, Ratenzahlung
- **§ 43 StGB** — Ersatzfreiheitsstrafe: 1 Tag pro Tagessatz, mind. 1 Tag
- **§ 459d StPO** — Uneinbringlichkeit der Geldstrafe: Vollstreckungsgericht entscheidet

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BGH 15.07.2025 — 2 StR 644/24: KCanG-Strafzumessung — die gesetzliche Wertung des § 1 Nr. 8 ff. KCanG ist als bestimmender Strafzumessungsgrund zu beruecksichtigen; das wirkt auch auf die Tagessatzhoehe und die Anzahl der Tagessaetze bei Cannabisvorwurf. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- BGH (GSSt) 03.02.2025 — GSSt 1/24: Sanktionsfreie Eigenkonsummengen sind aus der Einziehung herauszunehmen — relevant für die Bemessung in KCanG-Strafbefehlen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Hinweis: Eine aktuelle BGH-Leitentscheidung 2025/2026 zu § 40 StGB / Tagessatzbemessung im Strafbefehl ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 40 StGB Tagessatzhoehe Nettoeinkommen" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berechnungsschema Tagessatz

```
1. Bruttoeinkommen monatlich: [BETRAG] EUR
2. Abzuege (Lohnsteuer, SV-Beitraege): [BETRAG] EUR
3. Nettoeinkommen: [BETRAG] EUR
4. Tagessatz (Netto / 30): [BETRAG] EUR

Besonderheiten:
- Fahrtkosten / Werbungskosten: koennen abgezogen werden
- Unterhaltspflichten: mindern verfuegbares Einkommen (§ 40 Abs. 2 Satz 2)
- Schulden / Verbindlichkeiten: einzelfallabhaengig, kein automatischer Abzug
- Selbststaendige: Gewinn lt. Steuerbescheid / 12 als Monats-"Netto"
```

## Einkommensnachweise-Checkliste

```
□ Lohnabrechnung letzter 3 Monate
□ Steuerbescheid letztes Jahr
□ Rentennachweis (bei Rentnern)
□ Buchfuehrungs-Zusammenfassung / BWA (bei Selbststaendigen)
□ ALG-II-/Buergergeld-Bescheid (bei ALG-II-Empfaengern: ca. 1-2 EUR Tagessatz)
□ Unterhaltsnachweis (belegt Verbindlichkeiten)
□ Kreditvertraege (monatliche Belastungen)
```

## Antrag auf Ratenzahlung — Template

**Adressat:** Vollstreckungsgericht / Staatsanwaltschaft — Tonfall: sachlich, Daten belegt

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Zahlungserleichterung nach § 42 StGB

Mein Mandant ist verurteilt zu [X] Tagessaetzen a [Y] EUR,
gesamt [X*Y] EUR Geldstrafe.

Er ist aufgrund [Einkommensverhaeltnisse beschreiben] derzeit nicht in
der Lage, den Gesamtbetrag in einer Summe zu zahlen.

Wir beantragen Ratenzahlung von [RATE] EUR monatlich beginnend
ab [DATUM].

Anlage: Einkommensnachweis / Kontoauszug
```

## Harte Leitplanken

- Tagessatz nie ohne Einkommensnachweis bestimmen — Schaetzung zu Mandantenungunsten moglich.
- Ratenzahlungsantrag fruehzeitig stellen — vor Vollstreckungsbeginn.
- Ersatzfreiheitsstrafe (§ 43 StGB) dem Mandanten klar erklaeren.
- Anwaltliche Endkontrolle bei Berechnungen.

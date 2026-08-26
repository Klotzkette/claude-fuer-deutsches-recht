---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Strafrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Strafrecht

> Vorladung, Durchsuchung, U-Haft, Anklage, Revision — Verfahrensphase entscheidet alles. Identität des Beschuldigten zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 311 II StPO: 1 Woche** sofortige Beschwerde. § 314 StPO: Berufung 1 Woche ab Verkündung. § 341 StPO: Revision 1 Woche ab Verkündung; § 345 StPO: Begründung 1 Monat ab Zustellung. § 33a StPO (Haftprüfung jederzeit). § 67 OWiG: Einspruch Bußgeld 2 Wochen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Hier kein klassischer Anspruch: Tatvorwurf benennen (Norm + StGB- bzw. Nebenstrafrechts-§). Mitwirkung: Akteneinsicht § 147 StPO, Beweisantrag § 244 StPO, Verteidigerwahl § 137 StPO, Pflichtverteidigung § 140 StPO. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | AG Strafrichter / Schöffengericht (§§ 24 ff. GVG), LG große Strafkammer (§ 74 GVG), OLG (Staatsschutz, § 120 GVG). Bei Jugendlichen: JGG-Spruchkörper. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Sofortige Beschwerde (1 Woche), Revisionsfrist (1 Woche / 1 Monat) tickt ab Verkündung/Zustellung. 🟠 Hauptverhandlung in 30 Tagen — Beweisanträge vorbereiten.
- **Beweislage:** 🟠 Beschuldigtenaussage NIE ohne Akteneinsicht. 🔴 Belastungszeugen: Konfrontationsrecht Art. 6 III d EMRK ausnutzen. 🟢 Selbstanzeige § 371 AO nur nach umfassender Aktenlage.
- **Wirtschaftlich:** 🔴 Berufstauglichkeit gefährdet (Beamte, Heilberufe, Approbation): parallel berufsrechtliche Schiene mitdenken. 🟠 Vermögensabschöpfung §§ 73 ff. StGB im Blick.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Untersuchungshaft / Haftbefehl** | `strafr-haftpruefung-haftbeschwerde-workflow` | Haftbeschwerde § 304 StPO, Haftprüfung § 117 StPO, mündliche Verhandlung erzwingen |
| Akteneinsicht & Strategie | `akteneinsicht-beantragen` | Antrag § 147 StPO, Wahl Verfahrensschiene, ggf. Schweigen / Einlassungsmemo |
| Beweisantrag vorbereiten | `strafr-dysfunk-beweisantrag-fundament` | Substantiierte Tatsachenbehauptung, Beweismittel, Konnexität |
| Revision prüfen | `revisionsbegruendung-paragraf-344-stpo` | Sach- vs. Verfahrensrüge, absolute Revisionsgründe § 338 StPO |
| Wirtschafts-/Vermögensabschöpfung | `strafr-vermoegensabschoepfung-spezial` | Einziehung §§ 73 ff. StGB, vermögenssichernde Maßnahmen § 111b StPO |

## Norm-Radar (live verifizieren)

- **§ 147 StPO** — Akteneinsicht des Verteidigers
- **§ 137 StPO** — Recht auf Verteidiger jederzeit
- **§ 244 StPO** — Beweisantragsrecht
- **§ 117 StPO** — Haftprüfung
- **§ 341 StPO** — Revisions-Einlegungsfrist (1 Woche)
- **§ 73 StGB** — Einziehung von Taterträgen

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Verfahrensphase** läuft (Ermittlung · Anklage · Hauptverhandlung · Rechtsmittel · Vollstreckung), und sitzt der Mandant **in Haft**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verständigung § 257c StPO; Mitteilungspflichten** — BVerfG 2. Senat; BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`
- **Beweisantragsrecht § 244 StPO; Konnexität** — BGH-Strafsenate — *live verifizieren auf* `bundesgerichtshof.de`
- **Faires Verfahren / Konfrontationsrecht Art. 6 III d EMRK** — EGMR — *live verifizieren auf* `hudoc.echr.coe.int`
- **Einziehung §§ 73 ff. StGB; verfassungsrechtliche Grenzen** — BVerfG / BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

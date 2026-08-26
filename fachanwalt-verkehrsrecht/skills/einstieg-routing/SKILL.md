---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Verkehrsrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Verkehrsrecht

> Bußgeld, Fahrerlaubnis, Unfallregulierung, Trunkenheitsfahrt — drei Aktenbündel, oft parallel: OWi/Straf, FE-Behörde, Versicherer.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 67 OWiG: 2 Wochen** Einspruch Bußgeldbescheid ab Zustellung. § 80 III VwGO: Widerspruch gegen FE-Entzug 1 Monat. § 41 RL 2009/103/EG / § 115 VVG: Direktanspruch Versicherer (keine Verjährungsfalle, aber Verzug nach 6 Wochen). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | OWi-Verteidigung (§§ 66, 67 OWiG), Straffahrlässigkeit/Vorsatz (§§ 315c, 316 StGB, § 21 StVG, § 24a StVG), Schadensersatz aus Unfall §§ 7 StVG, 18 StVG, 17 StVG (Quote), §§ 823, 249 BGB, 253 II BGB (Schmerzensgeld), Direktanspruch § 115 VVG. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | OWi: AG am Tatort (§ 68 OWiG). Strafsachen: AG/LG nach §§ 24 ff. GVG. FE-Sache: Verwaltungsbehörde + VG. Zivilrechtlich: Wahlrecht §§ 17, 32 ZPO, AG/LG je Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Bußgeld-Einspruch (2 Wochen) tickt ab Zustellung; Datum aus Akte verifizieren. 🟠 Verjährung OWi: 3 Monate bis Anhörung, 6 Monate gesamt (§ 26 III StVG für StVO-Verstöße).
- **Beweislage:** 🟠 Messverfahren: Eichschein, Bauartzulassung, Toleranzabzug. 🔴 Trunkenheit: BAK-Analyse, Blutprobenrichter (§ 81a StPO!).
- **Wirtschaftlich:** 🟠 1-Monats-Fahrverbot: Schonfrist § 25 IIa StVG (Beruf!). 🔴 FE-Entzug: MPU-Risiko und 6-Monats-Wiedererteilungssperre § 69a StGB.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Bußgeldbescheid eingegangen** | `bussgeld-einspruch-pruefen` | Einspruch fristgerecht, Akteneinsicht, Messverfahren-Check |
| Fahrerlaubnis-Entzug droht | `fahrerlaubnis-entzug` | MPU-Anordnung prüfen, vorläufige Entziehung § 111a StPO |
| MPU steht an | `mpu-vorbereitung` | Begutachtungsanlass, Abstinenzbelege, Vorbereitungsphase |
| Unfallregulierung Versicherer | `verk-unfallregulierung-workflow` | Haftungsquote, Schadensersatzpositionen, Anlagensatz § 287 ZPO |
| Trunkenheits-/Drogenfahrt | `verk-trunkenheit-drogenfahrt-spezial` | BAK/AAK-Bewertung, § 316 StGB vs. § 24a StVG, FE-Folgen |

## Norm-Radar (live verifizieren)

- **§ 67 OWiG** — Einspruchsfrist 2 Wochen Bußgeld
- **§ 25 StVG** — Fahrverbot; Schonfrist Abs. 2a
- **§ 69 StGB** — Entziehung Fahrerlaubnis; Wiedererteilungssperre § 69a
- **§ 316 StGB** — Trunkenheit im Verkehr
- **§ 7 StVG** — Halterhaftung Unfall
- **§ 115 VVG** — Direktanspruch gegen KH-Versicherer

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Schiene** dominiert (OWi/Straf · FE-Behörde · Versicherer-Regulierung) — und welche Frist tickt zuerst?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Standardisiertes Messverfahren** — BGH 4. Strafsenat (Linie seit 1997) — *live verifizieren auf* `bundesgerichtshof.de`
- **Akteneinsicht in Rohmessdaten (OWi)** — BVerfG 2. Senat (Beschluss v. 12.11.2020) — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Halterhaftung § 7 StVG; Höhere Gewalt** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Direktanspruch § 115 VVG gegen KH-Versicherer** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

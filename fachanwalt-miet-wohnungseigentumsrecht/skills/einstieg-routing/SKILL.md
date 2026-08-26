---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Miet- und Wohnungseigentumsrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Miet- und Wohnungseigentumsrecht

> Kündigung, Mieterhöhung, Betriebskosten, Mietminderung, WEG-Beschlussanfechtung — Vertragstyp und Zeitpunkt bestimmen die Schiene.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 45 WEG / § 46 WEG: 1 Monat** Beschlussanfechtungsklage. § 558b BGB: Zustimmungsverlangen Mieterhöhung 2 Monate. § 559 BGB: Modernisierungs-Ankündigung 3 Monate vor Beginn. § 574 BGB: Sozialklausel-Widerspruch 2 Monate vor Beendigung. § 573 III BGB: Schriftform Kündigung. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Räumung §§ 546, 985 BGB · Zahlungsklage (Miete, Betriebskosten) §§ 535 II, 556 BGB · Mietminderung § 536 BGB · Mängelbeseitigung § 535 I 2 BGB · WEG-Anfechtung § 44 ff. WEG · Hausgeld §§ 16 II, 28 WEG. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Wohnraummietsachen: Amtsgericht am belegenen Ort, ausschließlich und streitwertunabhängig nach Paragraf 23 Nummer 2a GVG und Paragraf 29a ZPO; in erster Instanz kein Anwaltszwang nach Paragraf 78 Absatz 1 Satz 1 ZPO im Umkehrschluss. Gewerberaummiete: bis einschließlich zehntausend Euro Amtsgericht, darüber Landgericht mit Anwaltszwang. WEG-Streitigkeiten: Amtsgericht am belegenen Ort nach Paragraf 43 WEG. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 WEG-Anfechtung: 1 Monat ab Beschlussfassung, NICHT ab Protokoll. 🟠 Mieterhöhung Zustimmungsklage § 558b II BGB. 🟠 Räumungsklage nach Kündigung — Widerspruchsfrist § 574b BGB.
- **Beweislage:** 🟠 Zugang der Kündigung: § 130 BGB beim Empfänger. 🔴 Mietminderung: Mangelanzeige § 536c BGB lückenlos, sonst Schadensersatzpflicht.
- **Wirtschaftlich:** 🔴 Räumung: Vollstreckungsschutz § 765a ZPO (Härtefall). 🟠 Betriebskostennachforderung > 1.000 €: Belegeinsicht und materielle Prüfung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Eigenbedarfskündigung erhalten** | `kuendigung-eigenbedarf-bgb-viii-zr-21-19` | Substantiierung Bedarf, Härtefall § 574 BGB, Sozialklausel |
| Mietminderung wegen Mangel | `mietminderung-paragraf-536-bgb` | Quote, Anzeigeobliegenheit § 536c BGB, Zurückbehaltungsrecht |
| Betriebskostenabrechnung prüfen | `miet-betriebskostenabrechnung-checkliste` | Formelle und materielle Prüfung, Abrechnungsfrist § 556 III BGB |
| Mietpreisbremse / Rüge | `mietpreisbremse-paragraf-556d-bgb-bgh-viii-zr-25-22` | Rüge, Auskunft Vormiete, Rückforderung |
| WEG-Beschlussanfechtung | `beschlussanfechtung-spezial-fristen` | 1-Monatsfrist § 45 WEG, Begründung 2 Monate, Form |

## Norm-Radar (live verifizieren)

- **§ 573 BGB** — ordentliche Kündigung Wohnraum; berechtigtes Interesse
- **§ 574 BGB** — Sozialklausel / Härtefall-Widerspruch
- **§ 536 BGB** — Mietminderung wegen Mangel
- **§ 556 BGB** — Betriebskosten; Abrechnungsfrist III
- **§ 558 BGB** — Mieterhöhung bis ortsübliche Vergleichsmiete
- **§ 45 WEG** — Anfechtungsklage 1-Monatsfrist

## Genau eine Rückfrage (nur wenn nötig)

> Geht es um **Wohnraummiete · Gewerbemiete · WEG-Beschluss** — und steht eine **Beendigung** (Kündigung, Räumung) oder eine **Zahlungs-/Mängel-Frage** im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Eigenbedarfskündigung § 573 II Nr. 2 BGB; Vortäuschung** — BGH VIII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Sozialklausel § 574 BGB; Härtefall-Abwägung** — BGH VIII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Mietpreisbremse §§ 556d ff. BGB; Rüge und Auskunft** — BGH VIII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **WEG-Beschlussanfechtung § 44 WEG (n. F.); Fristen** — BGH V. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

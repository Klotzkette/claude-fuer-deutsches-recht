---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht

> Gesellschafterstreit, Geschäftsführerhaftung, Anfechtungsklage, M&A, Handelsvertreterausgleich — Beteiligungsverhältnisse und Beschlüsse zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 246 AktG: 1 Monat** Anfechtungsklage Hauptversammlungsbeschluss. § 256 AktG (Nichtigkeitsklage). GmbH-Beschlüsse: analog 1 Monat (h. M., kein gesetzlicher Frist, vertragliche Regelungen prüfen). § 89b HGB: Ausgleichsanspruch Handelsvertreter 1 Jahr nach Ende. § 161 II AktG: Erklärung Corporate Governance jährlich. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Anfechtung Beschluss § 243 AktG · Nichtigkeit § 241 AktG · GF-Haftung §§ 43 GmbHG, 93 AktG · Treuepflicht (st. Rspr.) · Wettbewerbsverbot § 88 AktG · Auskunft § 51a GmbHG · Handelsvertreterausgleich § 89b HGB · Einsicht Kommanditist § 166 HGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | LG Kammer für Handelssachen (§§ 95, 96 GVG) — auf Antrag (§ 98 GVG). Schiedsklauseln verbreitet → vorab Schiedsvereinbarung prüfen (§ 1029 ZPO). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Anfechtungsklage Hauptversammlungsbeschluss § 246 AktG (1 Monat ab Beschlussfassung). 🟠 Ausgleichsanspruch HV § 89b III HGB Geltendmachung 1 Jahr nach Vertragsbeendigung.
- **Beweislage:** 🟠 Beschlussfassung: Protokoll, Versammlungsleitung, Beschlussverfahren. 🔴 GF-Haftung: Geschäftsvorfall, Vorteilsabsicht, Kausalität — Buchhaltung sichern.
- **Wirtschaftlich:** 🔴 Insolvenzantragspflicht § 15a InsO (3 Wochen ab Eintritt Zahlungsunfähigkeit) — parallel zur Geschäftsführerhaftung mitdenken. 🟠 M&A: Due-Diligence-Findings als Verhandlungsmasse.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Geschäftsführerhaftung im Raum** | `gmbh-gf-haftung-paragraf-43-gmbhg` | Pflichtverstoß, Schaden, Verschulden, Entlastung § 46 Nr. 5 GmbHG |
| Hauptversammlungsbeschluss anfechten | `aktionaersklage-anfechtung-paragraf-243-aktg` | 1-Monatsfrist § 246 AktG, Anfechtungsbefugnis |
| Gesellschafterstreit GmbH | `gesellschafterstreit` | Ausschluss, Einziehung, Treuepflichtklage |
| Handelsvertreterausgleich § 89b HGB | `handelsvertreterausgleich` | Voraussetzungen, Berechnung, Geltendmachungs-Frist |
| M&A Due-Diligence Befunde | `ma-due-diligence-findings` | Risikoclustering, SPA-Anpassungen, Earn-out-/MAC-Klauseln |

## Norm-Radar (live verifizieren)

- **§ 243 AktG** — Anfechtbarkeit Hauptversammlungsbeschluss
- **§ 246 AktG** — 1-Monatsfrist Anfechtungsklage
- **§ 43 GmbHG** — Geschäftsführerhaftung
- **§ 51a GmbHG** — Auskunftsrecht des GmbH-Gesellschafters
- **§ 89b HGB** — Handelsvertreterausgleich
- **§ 15a InsO** — Insolvenzantragspflicht

## Genau eine Rückfrage (nur wenn nötig)

> Steht ein **Beschluss zur Anfechtung** im Raum, **Haftung eines Organs** oder ein **Vertragsstreit** (Handelsvertreter, M&A) im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **GmbH-Geschäftsführerhaftung § 43 GmbHG; Business Judgement Rule** — BGH II. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Hauptversammlungsbeschluss-Anfechtung § 243 AktG; 1-Monats-Frist § 246 AktG** — BGH II. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Handelsvertreterausgleich § 89b HGB; Berechnung** — BGH VII./VIII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Grenzüberschreitender Formwechsel** - EuGH, Urteil vom 25.10.2017 - C-106/16 (Polbud): Die Niederlassungsfreiheit kann auch die Umwandlung in eine Gesellschaft nach dem Recht eines anderen Mitgliedstaats schützen, ohne dass die Gesellschaft dort ihre tatsächliche wirtschaftliche Tätigkeit ausüben muss; Missbrauchsprüfung und inzwischen harmonisiertes Umwandlungsrecht getrennt anwenden.

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

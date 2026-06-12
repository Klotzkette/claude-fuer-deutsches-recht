---
name: einstieg-routing
description: "Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat."
---

# Anwalts-Dashboard Fachanwalt Arbeitsrecht

> Kündigung, Aufhebungsvertrag, Befristung, Betriebsrat, Betriebsübergang — sieben Eilfristen, ein Klagestrang.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 4 KSchG: 3 Wochen** ab Zugang Kündigung. Daneben § 626 II BGB (außerordentlich, 2 Wochen ab Kenntnis), § 15 IV AGG (2 Monate Geltendmachung), § 17 KSchG (Massenentlassungsanzeige), § 9 MuSchG, § 613a VI BGB (1 Monat Widerspruch). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Kündigungsschutz §§ 1, 4, 7 KSchG · Lohn §§ 611a, 614, 615 BGB (Annahmeverzug) · Schadensersatz §§ 280 I, 823 BGB · AGG-Entschädigung §§ 7, 15 AGG · Betriebsübergang § 613a BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Arbeitsgericht am Arbeitsort (§ 48 ArbGG, § 17 ZPO). Streitwert KSchG-Klage: 1/4 Bruttojahresgehalt (§ 42 II GKG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kündigung mit laufender 3-Wochen-Frist: heute Klageschrift. 🟠 Aufhebungsvertrag mit Widerrufsoption: 14 Tage prüfen. 🟢 Lohnklage ohne Verfallsklausel.
- **Beweislage:** 🟠 Zugang der Kündigung trägt der Arbeitgeber (§ 130 BGB); Zustellungsnachweis sichern. 🔴 Bei mündlicher Kündigung: Zeugen organisieren.
- **Wirtschaftlich:** 🔴 Lohnverlust > 3 Monate + Verlust SV-Pflicht: Eilantrag Weiterbeschäftigung (§ 102 V BetrVG) prüfen. 🟠 Abfindung ≈ 0,5 Monatsgehälter pro BJ als Verhandlungsstart.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Kündigung erhalten — Schutzklage prüfen** | `ar-kuendigungspruefung-workflow` | Klageschrift mit Anträgen, Streitwertangabe, Antrag auf vorläufige Weiterbeschäftigung |
| Aufhebungsvertrag angeboten | `ar-aufhebungsvertrag-praxis` | Risikomatrix, Abfindungs-Range, Sperrzeit § 159 SGB III |
| Befristung soll geprüft werden | `befristung-tzbfg` | Sachgrund- vs. sachgrundlose Befristung, Anschlussverbot § 14 II 2 TzBfG |
| Betriebsrats-Beteiligung streitig | `beteiligung-betriebsrat-102-betrvg` | Anhörungsfehler, Heilung, Folge der Unwirksamkeit |
| Betriebsübergang im Raum | `ar-betriebsuebergang-spezial` | Widerspruchsfrist § 613a VI BGB (1 Monat), Informationsanspruch |

## Norm-Radar (live verifizieren)

- **§ 4 KSchG** — 3-Wochen-Frist Kündigungsschutzklage
- **§ 626 BGB** — außerordentliche Kündigung, 2-Wochen-Frist Abs. 2
- **§ 1 KSchG** — Sozialwidrigkeit; KSchG-Anwendung ab 10 AN (Kleinbetrieb)
- **§§ 611a, 615 BGB** — Arbeitsvertrag, Annahmeverzug
- **§ 613a BGB** — Betriebsübergang; Widerspruchsrecht Abs. 6
- **§ 102 BetrVG** — Anhörung Betriebsrat; Folge der Unwirksamkeit

## Genau eine Rückfrage (nur wenn nötig)

> Liegt eine **Kündigung mit Zugangsdatum** vor — oder ist der Triggerpunkt ein anderer (Befristung, Lohn, Aufhebungsvertrag, AGG)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Kündigungsschutz § 1 KSchG; Sozialwidrigkeit** — BAG 2. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`
- **Betriebsübergang § 613a BGB; Identitätswahrung** — BAG 8. Senat (Spijkers-/Süzen-Linie) — *live verifizieren auf* `bundesarbeitsgericht.de + EuGH curia.europa.eu`
- **Befristung ohne Sachgrund; Vorbeschäftigung § 14 II 2 TzBfG** — BAG 7. Senat; BVerfG 1. Senat — *live verifizieren auf* `bundesarbeitsgericht.de + bundesverfassungsgericht.de`
- **AGG-Entschädigung § 15 II; 2-Monats-Frist** — BAG 8. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die über das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des $ 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschließlich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis können Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln müssen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschäftigte nach Kuendigung unter Fortzahlung der Vergütung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall möglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Prüfschemata, Klagebausteine und Verteidigungsmuster.

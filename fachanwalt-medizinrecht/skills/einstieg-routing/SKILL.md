---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Medizinrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Medizinrecht

> Behandlungsfehler, Aufklärungsmangel, Approbation, MVZ, Apothekenrecht — drei Welten: Haftung, Berufsrecht, Vergütung.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine klassische 2-Wochen-Frist im Patientenrecht, aber: § 199 BGB Verjährung 3 Jahre ab Kenntnis (regelmäßig). § 41 BÄO i. V. m. VwGO: 1 Monat Widerspruch gegen Approbationsbescheid. § 80 V VwGO: Eilantrag bei Ruhensanordnung. § 287 ZPO/§ 287a ZPO Beweismaßerleichterung Patientenseite. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Behandlungsvertrag § 630a BGB · Aufklärung § 630e BGB · Dokumentation § 630f BGB · Beweisrechtsumkehr § 630h BGB · Schmerzensgeld § 253 II BGB · Schadensersatz §§ 280, 823 BGB · Approbation §§ 3, 5 BÄO · Verträge mit Krankenkassen § 75 SGB V. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Zivilklage Patient ↔ Arzt: LG (regelmäßig Spezialkammer Arzthaftung). Berufsrechtliche Sache: VG / OVG (§ 40 VwGO). Schlichtungsstelle Ärztekammer fakultativ. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🟠 Verjährung Patientenanspruch tickt ab Kenntnis (§ 199 BGB) — Schweigen der Klinik schiebt die Frist NICHT hinaus. 🔴 Approbationswiderruf: 1 Monat Widerspruch + Aufschiebenhebungsantrag § 80 V VwGO.
- **Beweislage:** 🔴 Dokumentationslücke § 630h III BGB: Beweisrechtsumkehr zugunsten Patient. 🟠 Aufklärungsbeweis trägt der Arzt (§ 630h II BGB) — Aufklärungsbogen lückenlos prüfen.
- **Wirtschaftlich:** 🔴 Approbationsentzug = Berufsende — Eilrechtsschutz und parallel Strafverteidigung (z. B. § 95 BtMG, § 263 StGB). 🟠 MVZ-Anstellung: Wettbewerbsverbot und Übergangsversorgung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Behandlungsfehler-Verdacht prüfen** | `behandlungsfehler-anspruch-pruefen` | Anspruchsgrundlagen § 630a/h BGB, Beweisrechtsumkehr, Sachverständige |
| Aufklärungspflichtverletzung | `aufklaerungspflicht-paragraf-630e-bgb` | Aufklärungsumfang, Zeitpunkt, Beweislast § 630h II BGB |
| Schlichtungsstelle prüfen | `gutachterkommission-aek-schlichtung` | Verfahrensvorteile, Hemmung der Verjährung § 204 I Nr. 4 BGB |
| Approbationsbescheid angreifen | `approbations-widerspruch` | Widerspruch 1 Monat, Aufschubantrag § 80 V VwGO, Berufseingriffsabwehr |
| Akteneinsicht / Befundherausgabe | `befundherausgabe-epa-akte` | Anspruch § 630g BGB, ePA-Spezifika, Verweigerung Vermerkbarkeit |

## Norm-Radar (live verifizieren)

- **§ 630a BGB** — Behandlungsvertrag
- **§ 630e BGB** — Aufklärungspflicht
- **§ 630f BGB** — Dokumentationspflicht
- **§ 630h BGB** — Beweislast bei Behandlungsfehler
- **§ 3 BÄO** — Approbation; Voraussetzungen und Widerruf
- **§ 199 BGB** — Verjährungsbeginn

## Genau eine Rückfrage (nur wenn nötig)

> Geht es um **Patient ↔ Behandler (Haftung)**, **Arzt/MVZ ↔ Behörde (Berufsrecht)** oder um **Vergütung / Kassenzulassung**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Aufklärungspflicht § 630e BGB; Beweislast § 630h II BGB** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Grober Behandlungsfehler; Beweislastumkehr § 630h V BGB** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Dokumentationspflicht § 630f BGB; Folgen Lücken** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Recht auf selbstbestimmtes Sterben** — BVerfG 2. Senat (Urteil v. 26.02.2020, 2 BvR 2347/15) — *live verifizieren auf* `bundesverfassungsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Medizin- und Gesundheitsrecht:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->

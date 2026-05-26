---
name: digitalregulierung-pyramide-check
description: "Einstiegsskill EU-Digitalregulierung. Ordnet einen Sachverhalt den passenden Rechtsakten zu: DSA DMA Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Prüfreihenfolge: Akteurstyp; Dienst-Typ (Vermittlungsdienst Hosting Online-Plattform VLOP Kernplattformdienst Gatekeeper); Datentyp; Risikoklasse. Liefert Kurzprüfschema mit Verweis auf Spezialskills im Plugin."
---

# Digitalregulierung — Pyramiden-Check

## Zweck

Bei jedem digitalrechtlichen Mandat zuerst klären: **Welcher Rechtsakt greift überhaupt?** Die EU-Digitalregulierung ist geschichtet und überlappt — derselbe Sachverhalt kann gleichzeitig DSA, DSGVO und nationales Wettbewerbsrecht auslösen.

## Erstprüfung in vier Schritten

### Schritt 1 — Akteurstyp bestimmen

| Akteur | Mögliche Rechtsakte |
|---|---|
| Online-Vermittlungsdienst (Hosting, Marktplatz, soziales Netzwerk) | DSA, P2B-VO, DDG |
| Sehr große Online-Plattform (VLOP) oder Suchmaschine (VLOSE) | DSA Kapitel III Abschnitt 5 (Art. 33 ff.) |
| Gatekeeper iSd Art. 3 DMA | DMA |
| Anbieter von KI-Systemen | AI Act |
| Anbieter eines Datenvermittlungsdienstes | DGA |
| Hersteller eines IoT-Produkts | Data Act, CRA |
| Anbieter qualifizierter Vertrauensdienste | eIDAS 2.0 |
| Betreiber wesentlicher/wichtiger Einrichtungen | NIS-2 |
| Finanzunternehmen / IKT-Drittdienstleister | DORA |
| Marktbeherrschendes oder marktübergreifend bedeutendes Digitalunternehmen | § 19a GWB |

### Schritt 2 — Dienst-Typ einordnen (DSA-Hierarchie)

DSA arbeitet mit einer Hierarchie aufsteigender Pflichten:

1. **Reiner Durchleitungsdienst** (Art. 4) — minimale Pflichten, Haftungsprivileg
2. **Caching** (Art. 5)
3. **Hosting-Dienst** (Art. 6) — Notice-and-Action, Art. 16
4. **Online-Plattform** (Art. 19 ff.) — interne Beschwerdeverfahren, trusted flaggers, Transparenzberichte
5. **VLOP / VLOSE** ab 45 Mio. monatlich aktiven Nutzern in der EU (Art. 33) — Systemrisiko, Audits, Forschungsdatenzugang
6. **Online-Marktplatz** — zusätzlich Art. 30 ff. (Händler-Identifikation)

Kleinunternehmen sind teilweise befreit (Art. 19 für kleine/Kleinst-Unternehmen).

### Schritt 3 — Datentyp prüfen

- **Personenbezogene Daten** → DSGVO gilt zusätzlich (Art. 2 Abs. 4 DSA, kein lex specialis)
- **Nicht-personenbezogene maschinengenerierte Daten (IoT)** → Data Act
- **Daten der öffentlichen Hand für Weiterverwendung** → DGA, Open-Data-RL
- **Geschäftsgeheimnisse** → GeschGehG bleibt anwendbar

### Schritt 4 — Risiko- und Inhaltsklasse

- **Illegale Inhalte** → DSA Art. 16
- **Schädliche aber legale Inhalte (Desinformation, Wahlen)** → DSA Art. 34/35 systemische Risiken
- **KI-System mit hohem Risiko** → AI Act Anhang III
- **Kritische Infrastruktur** → NIS-2 / CRA

## Anwendungsverhältnis

- **Lex specialis derogat legi generali** gilt nur eingeschränkt: DSA, DSGVO und Wettbewerbsrecht laufen oft parallel
- **DMA verdrängt nicht das allgemeine Kartellrecht** (Art. 1 Abs. 6 DMA): Art. 102 AEUV und § 19a GWB bleiben anwendbar
- **§ 19a GWB ist enger gefasst als DMA**, kann aber Sachverhalte erfassen, die unterhalb der DMA-Schwellen liegen
- **DDG ersetzt NetzDG und Teile des TMG** und implementiert DSA in Deutschland — Aufsicht: BNetzA als Digital Services Coordinator (DSC)

## Weiterleitung an Spezialskills

| Anliegen | Skill |
|---|---|
| VLOP-Designation prüfen | `dsa-vlop-vlose-einordnung-und-pflichten` |
| Gatekeeper-Schwellen | `dma-gatekeeper-schwellen-und-kernplattformdienste` |
| Systemische Risikobewertung | `dsa-art-34-systemische-risikobewertung` |
| Algorithmen-Zugang für Forschung | `dsa-art-40-forschungsdatenzugang-algorithmen` |
| Account-Sperre Mandant | `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` |
| Schnittstellen DSGVO/P2B/GWB | `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` |
| Zustellung an Auslandsplattform | `zustellung-und-vertreter-art-13-dsa-art-37-dma` |
| Klage gegen VLOP-Bescheid | `klage-gegen-vlop-einordnung-art-263-aeuv` |

## Mandantenfrage zuerst klären

Wer hat das Anliegen?

- **Plattform / Unternehmen selbst** → Pflichten-Compliance, ggf. Klage gegen Designation
- **Nutzer / Verbraucher** → Beschwerde, ADR, einstweilige Verfügung, Schadensersatz
- **Wettbewerber** → DMA-Beschwerde bei Kommission, kartellrechtliche Schritte
- **Forscher / Behörde** → Art. 40 DSA, Auskunftsverlangen
- **Geschäftlicher Nutzer (Händler auf Marktplatz)** → P2B-VO, DMA Art. 5/6

---
name: mittelstand-corporate-ma-vertragsmarkup-key-issues
description: "Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschlaege nach Parteiperspektive."
---

# Markup und Key Issues

## Zweck

Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive.

## Arbeitsmodus

- Änderungen nach wirtschaftlicher Relevanz und Rechtsrisiko clustern.
- Position Buy-side/Sell-side transparent halten.
- Rote Linien, Konzessionen und Verhandlungsstrategie trennen.
- Gegenentwurf nur als Vorschlag mit Review-Status ausgeben.

## Rote Schwellen

- Gegenseitenmarkup falsch gelesen.
- Marktüblichkeit ohne eigene Präzedenz- oder Quellenbasis behauptet.
- Risk shift ohne Mandantenentscheidung.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/key-issues-list.md
- assets/templates/markup-response-sheet.md

## Triage

1. Welches Dokument wird markiert — SPA, APA, NDA, Shareholders Agreement, Process Letter?
2. Welche Parteiperspektive — Kaeufer (Buy-side) oder Verkaeufer (Sell-side)?
3. Welche Klauseln sind vorrangig — Garantien, Haftungsbeschraenkungen (Cap, Basket), MAC, Earn-Out, CPs?
4. Liegt ein aktueller Term Sheet vor, auf den sich das Markup stuetzt?

## Zentrale Rechtsgrundlagen

- §§ 305-310 BGB — AGB-Inhaltskontrolle: Haftungsausschluesse und ungewoehnliche Klauseln koennen unwirksam sein
- §§ 443, 311 BGB — Garantievereinbarung: Formulierung entscheidet ueber Haftungsumfang; "Best Knowledge" vs. "actual knowledge" hat unterschiedliche Rechtsfolgen
- §§ 195, 199 BGB — Verjaehrungsfristen: vertragliche Abkuerzung auf 18-24 Monate ueblich; laengere Fristen bei Tax und Title

## Aktuelle Rechtsprechung

- BGH, Urt. v. 29.10.2020 - I ZR 153/17, NJW 2021, 780 — Haftungscap: Cap begraenzt Ansprueche; aber: Cap gilt nicht fuer arglistige Taeusching; ist separat zu klauseln
- BGH, Urt. v. 24.11.2010 - VIII ZR 235/09, NJW 2011, 594 — Kaeuferwissen: "Best Knowledge" Klausel schliesst Ansprueche aus bei Kaeuferwissen; "Actual Knowledge" ist enger; Formulierung ist entscheidend

## Kommentarliteratur

- Beisel/Klumpp, Unternehmenskauf, Kapitel 5 (SPA-Verhandlung, Markup, Key Issues), 8. Auflage
- Picot, Unternehmenskauf, Kapitel 4 (Vertragsgestaltung, Markup)

## Schritt-fuer-Schritt-Workflow

1. **Key Issues List erstellen:** alle nicht geklarten Punkte aus Term Sheet extrahieren; Prioritaet festlegen
2. **Markup nach Parteiperspektive erstellen:** Buy-side: staerkere Garantien, laengere Fristen, hoehere Caps; Sell-side: Beschraenkungen, kurze Fristen, Caps
3. **Redlines dokumentieren:** je Klausel: aktuelle Fassung, Markup, Begruendung, Kompromissvorschlag
4. **Human-in-the-loop:** alle Deal-Breaker-Markups → Partner-Freigabe vor Uebersendung

## Rote Schwellen

- Arglist-Ausnahme nicht geklauselt: Cap ggf. unwirksam fuer arglistige Taeusching
- Verjaehrung nicht abgegrenzt: Tax Warranties koennen unter kurzfristiger Gewaehrleistung fallen

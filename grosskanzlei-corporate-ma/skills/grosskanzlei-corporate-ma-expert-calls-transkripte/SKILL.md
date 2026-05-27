---
name: grosskanzlei-corporate-ma-expert-calls-transkripte
description: "Expert Calls und Transkript-Auswertung fuer M&A Due Diligence: Anwendungsfall Deal-Team hat Experteninterviews oder Management-Presentations transkribiert und muss Kernaussagen strukturiert extrahieren. MAR Vertraulichkeit, §§ 433 ff. BGB DD-Pflichten. Pruefraster Kerninformationen extrahieren, Widersprueche zu Datenraum-Unterlagen markieren, Red Flags identifizieren, Zitate fuer DD-Report verwertbar machen. Output strukturierte Transkript-Zusammenfassung mit Kernaussagen und Red-Flag-Liste. Abgrenzung zu DD-Reporting und zu QA-Information-Requests."
---

# Expert Calls und Transkripte

## Zweck

Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf.

## Arbeitsmodus

- Einwilligung und Vertraulichkeit vor Transkription prüfen.
- Call-Notizen nach Workstream und Quelle strukturieren.
- Mundliche Aussagen mit Datenraumbelegen verknuepfen.
- Unbelegte Aussagen als Follow-up in Q&A überführen.

## Rote Schwellen

- Keine Zustimmung zur Aufzeichnung.
- Geschäftsgeheimnisse in falschem Kanal.
- Mundliche Aussage wird ohne Verifikation als Tatsache genutzt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/expert-call-note.md
- assets/templates/transcript-consent-log.md

## Triage

1. Handelt es sich um eine Management Presentation, einen Expert Call mit Sachverstaendigem oder ein Kunden-Interview?
2. Ist das Transkript fuer SPA-Garantien oder fuer Disclosure-Zwecke relevant?
3. Liegt eine Vertraulichkeitsvereinbarung (NDA) fuer den Expert Call vor?
4. Handelt es sich um einen Expert Call mit Personen, die moeglicherweise Insiderinformationen haben (boersennotiertes Unternehmen)?

## Zentrale Rechtsgrundlagen

- §§ 17-18 GeschGehG — Vertraulichkeit in Expert Calls: Informationen sind Geschaeftsgeheimnisse; Grundlage muss NDA sein
- Art. 7, 10 MAR — Expert Calls mit Management boersennotierter Zielgesellschaft: koennen Insiderinformationen uebertragen; Expert muss auf MAR-Pflichten hingewiesen werden
- § 101 UrhG — Transkription: urheberrechtliche Fragen bei automatisierter Transkription
- §§ 201 StGB — unbefugte Tonbandaufnahmen im Gespraech sind strafbar; Einwilligung aller Teilnehmer erforderlich

## Aktuelle Rechtsprechung

- BGH, Urt. v. 13.05.2015 - XII ZB 503/13, NJW 2015, 3032 — Tonbandaufnahme: heimliche Aufzeichnung eines Gespraechs ohne Einwilligung ist nach § 201 StGB strafbar und als Beweismittel unverwertbar; schriftliche Einwilligung aller Teilnehmer erforderlich
- EuGH, Urt. v. 11.03.2015 - C-628/13, NJW 2015, 1716 — MAR: Management-Interviews koennen Insiderinformationen uebertragen; Expert-Call-Teilnehmer sind in Insiderliste aufzunehmen

## Kommentarliteratur

- Assmann/Poetzsch/Schneider, WpUEG, Art. 18 MAR Rn. 1-40 (Insiderliste bei Expert Calls)

## Schritt-fuer-Schritt-Workflow

1. **Einwilligung sichern:** alle Teilnehmer muessen Aufzeichnung genehmigen; bei boersennotierten Gesellschaften: MAR-Hinweis
2. **Expert Call vorbereiten:** Frageliste, Due-Diligence-Scope, Vertraulichkeitsstufe
3. **Transkription und Zusammenfassung:** Key Statements extrahieren; Material-Statements fuer SPA-Garantien oder Disclosure kennzeichnen
4. **Insiderliste pruefen:** bei boersennotiertem Zielobjekt: Teilnehmer in Insiderliste (Art. 18 MAR) eintragen
5. **Integration in DD-Report:** Key Findings aus Expert Call in Workstream-Findings einpflegen

## Rote Schwellen

- Aufzeichnung ohne Einwilligung: § 201 StGB strafbar; Beweismittel unverwertbar
- Expert Call mit Insider ohne MAR-Protokoll: Aufsichtsrisiko

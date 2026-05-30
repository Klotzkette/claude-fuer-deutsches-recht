---
name: corporate-kanzlei-kaltstart
description: "Kaltstart Corporate-Kanzlei: Strukturiert den Einstieg in ein neues Corporate/M&A-Mandat mit Schnellerfassung von Parteien, Dealtyp, Phase, ersten Risiken und naechsten Schritten. Normen: BRAO §§ 43a und 49b; GwG § 10 (KYC); MAR Insider-Abgrenzung. Prüfraster: Mandantenrolle (Kaeufer/Verkaeufer/Target), Dealtyp (Share/Asset/Merger/Distressed), Phase, Konflikt-Check, Fristen-Sofortcheck. Output Deal-Kurzkarte mit Ampel, Routing-Empfehlung an Spezialskills. Abgrenzung: Detailarbeit siehe kommandocenter; Deal-Intake siehe deal-intake-skill."
---

# Kaltstart Corporate-Kanzlei

## Zweck

Strukturiert den Einstieg in ein neues Corporate/M&A-Mandat aus beliebiger Quelle: E-Mail, Call, Teams-Message, NDA-Anfrage, Term Sheet oder Teaser.

## Triage-Fragen beim Kaltstart

1. Was ist die Transaktion? (M&A Share Deal, Asset Deal, Squeeze-Out, IPO, Restrukturierung)
2. Wer ist unser Mandant? (Kaeufer / Verkaefer / Target-Management / Finanzinvestor)
3. Was ist die Zielgesellschaft? (Rechtsform, Sitz, Branche, Jahresumsatz-Groessenordnung)
4. Gibt es bekannte Konflikte? (§ 43a BRAO — sofort pruefen)
5. Sind Insiderinformationen im Spiel? (Art. 18 MAR — Insider-Log anlegen)
6. Was wird als naechstes erwartet? (NDA, IRL, Kick-Off-Meeting, Regulatory-Check)

## Routing-Logik: Welcher Skill als naechstes?

| Situation | Naechster Skill |
|---|---|
| Neues Transaktionsmandat eingehend | `corporate-kanzlei-deal-intake` |
| Datenraum-Einladung erhalten | `corporate-kanzlei-datenraum-aufbau` |
| Due-Diligence-Phase | `corporate-kanzlei-due-diligence-legal` |
| SPA-Entwurf erhalten | `corporate-kanzlei-spa-apa-entwurf` + `corporate-kanzlei-vertragsmarkup-key-issues` |
| Kartell-/FDI-Fragen | `corporate-kanzlei-regulatory-fdi-merger-control` |
| Signing-Vorbereitung | `corporate-kanzlei-signing-closing-conditions` |
| Closing und Archiv | `corporate-kanzlei-closing-bible-archiv` |
| W&I-Versicherung | `corporate-kanzlei-wi-insurance` |
| Umwandlungsrecht | `corporate-kanzlei-umwandlungsrecht` |
| Post-Closing | `corporate-kanzlei-post-closing-integration` |

## Schnell-Output: Deal-Karte

```
DEAL-KARTE (KALTSTART)
Datum: [HEUTE]
Matter-Nr.: [VERGEBEN]
Deal-Codename: [GENERIERT]

Mandant: [NAME, Funktion (Kaeufer/Verkaefer)]
Zielgesellschaft: [NAME, Rechtsform, Sitz]
Deal-Typ: [Share Deal / Asset Deal / Merger / IPO]
Phase: [Vorfeldgespraech / DD / SPA-Verhandlung / Signing / Closing]

Compliance-Sofort-Check:
[ ] Konfliktpruefung durchgefuehrt — Ergebnis: [Frei]
[ ] Insider-Log angelegt — [Ja / Nein]
[ ] GwG-CDD angestossen — [Ja / Nein]

Naechste Aktion: [TODO mit Datum und Owner]
Eskalation: [Falls Konflikt oder Insider-Verdacht → Partner sofort]
```

## Rechtlicher Rahmen

- **§ 43a BRAO** — Interessenwiderstreit; sofortiger Check vor jedem Mandat
- **Art. 18 MAR** — Insider-Liste; bei borsennotierten Targets sofort anlegen
- **§§ 2-10 GwG** — CDD; wirtschaftlich Berechtigter; PEP; Sanktionen
- **§§ 311 II, 241 II BGB** — vorvertragliche Pflichten ab dem ersten Kontakt

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rote Schwellen

- Kein Konflikt-Check vor dem ersten Beratungsschritt → § 43a BRAO-Risiko
- Keine Insider-Log-Anlage bei borsennotierten Targets → Art. 18 MAR
- GwG-CDD verzögert → vor jeder mandatsbezogenen Tätigkeit durchführen

## Quellen

- § 43a BRAO; Art. 18 MAR; §§ 2-10 GwG; §§ 311 II BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

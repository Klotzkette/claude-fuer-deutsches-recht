---
name: corporate-kanzlei-kommandocenter
description: "Deal-Kommandocenter Corporate/M&A: Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Spezialskill (SPA, DD, StaRUG, Kapitalmarkt, Register)."
---

# Deal-Kommandocenter — Corporate/M&A

## Triage — kläre beim Mandatseingang

1. Dealtyp: Share Deal, Asset Deal, Kapitalerhöhung, Umwandlung, Distressed M&A, StaRUG/Insolvenz, Registervorgang?
2. Parteiperspektive: Buy-side, Sell-side, Target-Management, W&I-Versicherer, Finanzierungsbank, Aufsichtsrat?
3. Deal-Phase: Origination, Vorbereitung/NDA, Datenraum-Aufbau, Due Diligence, Vertragsverhandlung, Signing, Closing, Post-Merger-Integration, Streit/Restrukturierung?
4. Zeitkritisch? Signing-/Closing-Datum, behördliche Fristen (Fusionskontrolle, FDI), Insolvenzantragspflicht §§ 15a, 15b InsO?
5. Besondere Sensibilität: Clean-Room-Anforderung, Insiderinformation (MAR), Sanktionsrecht, Mandatsgeheimnis?

## Zentrale Normen

- **§ 15a InsO** — Insolvenzantragspflicht; Frist 6 Wochen (Überschuldung) / 3 Wochen (Zahlungsunfähigkeit).
- **§§ 17-19 InsO** — Insolvenztatbestände; Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung.
- **Art. 7 ECMR / § 36 GWB** — Fusionskontrolle; Vollzugsverbot vor Freigabe.
- **§ 40 AWG / §§ 55 ff. AWV** — Außenwirtschaftsrechtliche Investitionsprüfung (FDI); Vollzugsverbote.
- **Art. 17 MAR / § 26 WpHG** — Ad-hoc-Pflicht; Insiderinformation im M&A-Prozess.
- **§§ 2 ff. StaRUG** — Restrukturierungsrahmen; Anzeigepflicht und Planverfahren bei drohender Zahlungsunfähigkeit.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Deal-Routing-Matrix

| Dealtyp / Thema | Primärer Spezialskill | Sekundärer Spezialskill |
|---|---|---|
| SPA / APA Entwurf und Verhandlung | `corporate-kanzlei-spa-apa-entwurf` | `corporate-kanzlei-vertragsmarkup-key-issues` |
| Legal Due Diligence | `corporate-kanzlei-due-diligence-legal` | `corporate-kanzlei-due-diligence-reporting` |
| Datenraum Aufbau | `corporate-kanzlei-datenraum-aufbau` | `corporate-kanzlei-datenraum-gap-clean-room` |
| Transaktionsstruktur | `corporate-kanzlei-transaktionsstruktur` | `corporate-kanzlei-umwandlungsrecht` |
| Signing und Closing | `corporate-kanzlei-signing-closing-conditions` | `corporate-kanzlei-output-versand-signing` |
| W&I-Versicherung | `corporate-kanzlei-wi-insurance` | `corporate-kanzlei-disclosure-schedules` |
| Public M&A / Kapitalmarkt | `corporate-kanzlei-public-ma-kapitalmarkt-mar` | `corporate-kanzlei-regulatory-fdi-merger-control` |
| Restrukturierung / StaRUG | `corporate-kanzlei-restructuring-starug-insolvenzplan` | `corporate-kanzlei-distressed-ma` |
| KG / Personengesellschaft | `corporate-kanzlei-kg-personengesellschaften` | — |
| Umwandlungssteuerrecht | `corporate-kanzlei-umwandlungssteuerrecht` | `corporate-kanzlei-transaktionsstruktur` |
| Handelsregister / Register | `corporate-kanzlei-handelsregisterabruf` | `corporate-kanzlei-gesellschaftsrecht-register` |
| Konflikt / GwG / Sanktionen | `corporate-kanzlei-conflict-gwg-sanctions` | — |
| Datenqualität | `corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle` | — |
| Billing / Narratives | `corporate-kanzlei-billing-narratives` | — |

## Schritt-für-Schritt-Workflow

1. **Dealtyp erkennen** — aus Eingabetext (Term Sheet, NDA, Markup, Sachverhaltsangabe) den primären Dealtyp bestimmen.
2. **Parteiperspektive klären** — Buy-side oder Sell-side; Target-Management, Aufsichtsrat oder Finanzierungspartei?
3. **Deal-Phase bestimmen** — welche Phase ist aktiv; was ist die unmittelbare nächste Aktion?
4. **Zeitkritische Elemente identifizieren** — Signing/Closing-Datum, behördliche Fristläufe, Insolvenzantragspflicht?
5. **Routing-Entscheidung** — passenden Spezialskill aus Deal-Routing-Matrix auswählen.
6. **Deal-Karte erstellen** — Standardausgabe mit Ampel, Rollen, Owner, Deadline, Risiko, Freigabegrad.
7. **Rote Schwellen prüfen** — Stop bei Insiderinformation, Clean-Room-Problem, unklarem Closing-Datum oder Insolvenzantragspflicht.
8. **An Spezialskill übergeben** — Deal-Karte und Sachverhalt weitergeben; offene Punkte als TODO mit Owner und Frist.

## Output-Template Deal-Karte

**Adressat:** Deal-Team intern — Tonfall sachlich-präzise
```
DEAL-KARTE
Mandat: [Mandatsname / Kürzel]
Datum: [Datum]
Ersteller: [Name, Funktion]

ÜBERSICHT
Dealtyp:          [Share Deal / Asset Deal / Umwandlung / Distressed / Kapitalerhöhung]
Parteiperspektive:[Buy-side / Sell-side / Target-Management / W&I / Financing]
Deal-Phase:       [Origination / Vorbereitung / DD / Verhandlung / Signing / Closing / PMI]
Signing:          [Datum oder "ausstehend"]
Closing:          [Datum oder "ausstehend — Bedingungen offen"]

AMPELSTATUS
| Workstream | Status | Owner | Nächste Aktion | Deadline |
|-----------|--------|-------|----------------|---------|
| Legal DD  | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| SPA Verh. | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| Regulatory| 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| Closing   | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| PMI       | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |

ROTE SCHWELLEN (aktiv)
[ ] Frist oder Closing-Datum unklar
[ ] Insiderinformation / Clean-Room-Problem
[ ] Insolvenzantragspflicht möglicherweise ausgelöst
[ ] Fusionskontrolle / FDI-Freigabe ausstehend

ROUTING
Primärer Spezialskill: [Skill-Name]
Sekundärer Skill:      [Skill-Name oder —]

OFFENE PUNKTE (TODO)
| Nr. | Punkt | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1  | [Punkt] | [Name] | [Datum] | [Stufe] |

FREIGABEGRAD: [Entwurf / Freigegeben durch Partner / Vertraulich — nur intern]
```

## Rote Schwellen

- Signing- oder Closing-Datum unklar → Deal-Karte unvollständig; Datum klären bevor Routing.
- Insiderinformation oder Clean-Room-Anforderung erkannt → Stop; Informationsbarriere aufbauen; Compliance informieren.
- Insolvenzantragspflicht (§ 15a InsO) möglicherweise ausgelöst → sofort Eskalation an Partner; keine unkoordinierten Handlungen.
- Analytisches Ergebnis soll ungeprüft in Board Paper oder DD-Bericht einfließen → Qualitätskontrolle (`corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle`) vorschalten.
- Fusionskontrolle oder FDI-Freigabe ausstehend, Deal-Vollzug geplant → Gun-Jumping-Risiko; Regulatory-Skill einschalten.

## Quellen und Vertiefung

- §§ 15a, 15b, 17-19 InsO (Insolvenzantragspflicht und -tatbestände)
- Art. 7 ECMR; § 36 GWB (Fusionskontrolle)
- § 40 AWG; §§ 55 ff. AWV (FDI-Investitionsprüfung)
- Art. 17 MAR; § 26 WpHG (Insiderinformation)
- §§ 2 ff. StaRUG (Restrukturierungsanzeige)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

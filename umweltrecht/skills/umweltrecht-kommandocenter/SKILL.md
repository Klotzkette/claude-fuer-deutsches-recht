---
name: umweltrecht-kommandocenter
description: "Umweltmandat-Einstieg: Intake Anlagenkarte Behoerdenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Routing Triage-Matrix. Output Mandat-Karte Routing-Empfehlung Naechste-Schritte-Plan. Abgrenzung zu allen Fach-Skills (nur Master-Routing)."
---

# Umweltrecht-Kommandocenter

## Triage-Matrix — welcher Spezial-Skill?

| Sachverhalt | Spezial-Skill |
|---|---|
| BImSchG-Genehmigung beantragen oder anfechten | `umweltrecht-immissionsschutz-bimschg` |
| Emissionshandel TEHG, BEHG, DEHSt | `umweltrecht-emissionshandel-tehg` |
| Abfallstatus, KrWG, Nebenprodukt, Circular Economy | `umweltrecht-abfall-circular-economy` |
| Naturschutz, FFH, Artenschutz § 44 BNatSchG | `umweltrecht-naturschutz-artenschutz` |
| Stoerfall-Anlage, 12. BImSchV, Seveso | `umweltrecht-stoerfall-anlagen` |
| Wasser-Erlaubnis, Altlasten, BBodSchG | `umweltrecht-wasser-bodenschutz` |
| M&A-Transaktion, Umwelt-DD, Red Flags | `umweltrecht-transaktionen-dd` |
| UIG/IFG-Informationsantrag, Ablehnung | `umweltrecht-umweltinformation-uig-ifg` |
| VG-Klage, Eilantrag, Beschwerde OVG | `umweltrecht-verfahren` |
| Bussgeld-Bescheid, Anhoerung, Sanktionen | `umweltrecht-bussgeld-sanktionen` |
| Compliance, Beauftragte, Schulungsplan | `umweltrecht-compliance-schulung` |
| ESG, CSRD, Greenwashing | `esg-greenwashing-csrd` |
| Klimaklage, Verbandsklage UmwRG | `klimaklagen-verbandsklage-umwrg` |
| Lieferkette, LkSG, CSDDD | `lksg-csddd-lieferkettensorgfalt` |

## Intake-Fragen (fuer jeden Mandat)

1. **Mandantenrolle**: Betreiber, Investor, Betroffener Dritter, Umweltverband, Behoerde?
2. **Rechtsgebiet**: BImSchG, KrWG, WHG, BBodSchG, TEHG, BNatSchG — oder mehrere?
3. **Verfahrensstand**: Noch kein Verfahren / Antragsverfahren laufend / Bescheid ergangen / Klage anhangig?
4. **Fristen akut**: Widerspruch 1 Monat, Klage 1 Monat, Eilantrag unverzueglich — Eingang Bescheid?
5. **Beweismaterial**: Welche Dokumente — Genehmigung, Gutachten, Behoerdenkorrespondenz, Fotos?
6. **Wirtschaftliches Ziel**: Betrieb sichern, Anlage verhindern, Entschaedigung, Informationszugang, Reputationsschutz?

## Zentrale Querschnitts-Normen Umweltrecht

- **§§ 3-10 BImSchG** — Grundpflichten Emissionsschutz
- **§§ 4 9 10 BBodSchG** — Altlasten-Verantwortung und Sanierung
- **§§ 8 9 10 WHG** — Wasserrechtliche Erlaubnisse
- **§§ 14 15 34 44 BNatSchG** — Eingriff, FFH, Artenschutz
- **§ 2 UmwRG** — Verbandsklage-Befugnis
- **§ 4 UmwRG** — Verfahrensfehler als Aufhebungsgrund
- **§ 80 Abs. 5 VwGO** — Eilrechtsschutz gegen vollziehbare Genehmigung

## Leitentscheidungen (Ueberblick)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ampelmatrix Risikobewertung (Standard-Output)

| Risiko | Ampel | Fristen | Verantwortlich | Naechste Handlung |
|---|---|---|---|---|
| [THEMA 1] | ROT | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 2] | ORANGE | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 3] | GRUEN | — | [PERSON] | Monitoring |

## Output-Template: Mandatskarte Umweltrecht

**Adressat:** Akte / Interne Notiz — Tonfall: strukturiert, stichwortartig

```
MANDATSKARTE UMWELTRECHT
Stand: [DATUM]
Akte: [AKTENZEICHEN]

MANDANT: [NAME], [ROLLE: Betreiber/Nachbar/Verband]
GEGNER/BEHOERDE: [NAME/STELLE]
ANLAGE: [BEZEICHNUNG], [ORT], [TYP]

RECHTSRAHMEN:
- Hauptnorm: § [X] [GESETZ]
- Nebenrecht: [weitere Normen]

VERFAHRENSSTAND:
- [DATUM]: Genehmigung erteilt / Antrag gestellt / Bescheid erhalten
- [DATUM]: Widerspruch eingelegt / Klage erhoben
- [DATUM]: Naechster Termin [Erörterungstermin / VG / OVG]

FRISTEN:
- [DATUM]: Klagefrist / Einwendungsfrist / TEHG-Abgabe

RISIKEN:
- ROT: [Konkrete Gefahr, z.B. Praeklusion mangels Einwendung]
- ORANGE: [Risiko mit Einschaetzung Wahrscheinlichkeit]

NAECHSTE HANDLUNG:
1. [Konkrete Massnahme, Verantwortlich, Deadline]
2. [Weitere Massnahme]

OFFENE FRAGEN / BENOETIGT:
- [Dokument / Information]
```

## Schnittstellen-Skills

- `fachanwalt-verwaltungsrecht-orientierung` — allgemeine Verwaltungsrechtspruefung
- `energieanlagen-bimschg-genehmigung-verfahren` — Energie-Spezial-BImSchG
- `energietrassen-planfeststellung-rechtsschutz` — Energie-Planfeststellung
- `esg-greenwashing-csrd` — Nachhaltigkeitsberichte
- `klimaklagen-verbandsklage-umwrg` — Klimaklagen

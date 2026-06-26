---
name: signing-closing-conditions-cp-tracker
description: Baut einen belastbaren Tracker für Closing Conditions, Zustimmungen, Registerhandlungen, Waiver und Long-Stop-Risiken im Unternehmenskauf.
---
# Signing-Closing-Conditions und CP-Tracker

Nutze diesen Skill, wenn Signing und Closing auseinanderfallen und die Bedingungen bis zur Vollziehung geführt werden müssen. Der Skill macht aus Klauseln, Nebenabreden und Zuständigkeiten einen arbeitsfähigen Tracker.

## Kaltstartfragen

1. Welche Conditions Precedent sind im SPA vorgesehen?
2. Gibt es kartellrechtliche, außenwirtschaftsrechtliche oder sektorale Freigaben?
3. Welche Third-Party-Consents, Bankfreigaben oder Change-of-Control-Zustimmungen fehlen?
4. Wer liefert welche Nachweise bis wann?
5. Welche CPs sind objektiv, welche können verzichtet werden?
6. Gibt es Long-Stop Date, Break Fee oder Closing-by-Escrow?

## Tracker-Logik

| CP | Quelle | Owner | Nachweis | Fällig | Status | Eskalation |
| --- | --- | --- | --- | --- | --- | --- |
| Freigabe | SPA, Behörde | Käufer | Bescheid | | offen | Long-Stop prüfen |
| Consent | Vertrag | Verkäufer | Zustimmung | | offen | Waiver möglich |
| Register | GmbHG, Notar | Notar | Liste, Anmeldung | | offen | Closing Deliverables |

## Prüfraster

1. Bedingungstyp klären: rechtlich zwingend, vertraglich frei, nur Closing Deliverable.
2. Waiver-Fähigkeit prüfen: einseitig, gegenseitig, notariell, dokumentationspflichtig.
3. Closing-Fähigkeit trennen von Post-Closing-Covenants.
4. Evidenz definieren: Bescheid, E-Mail-Zustimmung, Board Approval, Registerauszug, Legal Opinion.
5. Ampellogik setzen: grün erledigt, gelb mit Restpunkt, rot Closing-Blocker.

## Rechtsprechungs- und Normanker

- Paragraf 158 BGB: Bedingungsmechanik als Grundmodell für CPs.
- Paragraf 41 GWB: Vollzugsverbot bei anmeldepflichtigen Zusammenschlüssen.
- Paragraf 15 und 16 sowie Paragraf 40 GmbHG: Anteilserwerb, Wirksamkeit gegenüber Gesellschaft und Gesellschafterliste.
- BGH, 21.04.1997 - II ZR 175/95: Entscheidungsvorbereitung muss Risiken und Alternativen sichtbar machen.

## Visualisierung

Signing -> CP-Tracker -> Freigaben und Consents -> Closing Call -> Closing Deliverables -> Post-Closing-Liste

## Output

Gib einen CP-Tracker, eine Closing-Agenda und eine kurze Waiver-Notiz aus. Markiere jede echte Vollziehungssperre ausdrücklich.

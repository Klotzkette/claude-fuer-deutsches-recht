---
name: sofortmassnahmen-checkliste
description: "Für Sofortmaßnahmen-Checkliste nach Datenschutzvorfall: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Sofortmaßnahmen-Checkliste nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Ist der Angriff oder das Leck noch aktiv oder bereits gestoppt?
2. Sind Backups intakt und vom kompromittierten System getrennt?
3. Gibt es Hinweise auf einen Innentäter — dann besondere Vorsicht bei Account-Sperrungen wegen Beweismittelvernichtung?
4. Greift eine Strafanzeigepflicht oder ein Strafanzeigeinteresse?
5. Welche Verträge mit Auftragsverarbeitern oder Cyberversicherern verlangen Sofortmeldungen?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; Beweissicherung; Compliance-Dokumentation)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Pflicht zu angemessenen technischen und organisatorischen Maßnahmen einschließlich Wiederherstellungsfähigkeit.
- **Art. 33 Abs. 3 lit. c DSGVO** Angabe der ergriffenen oder vorgeschlagenen Maßnahmen in der Meldung.
- **Art. 5 Abs. 1 lit. f DSGVO** Integrität und Vertraulichkeit.
- **§ 42 BDSG** Strafvorschriften.
- **§ 274 StGB** Urkundenunterdrückung; **§ 303a StGB** Datenveränderung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zu Beweisverwertungsverboten bei eilig getroffenen Maßnahmen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. f; Art. 32; Art. 33 Abs. 3 lit. c DSGVO; § 42 BDSG; §§ 274; 303a StGB.

## Praxisformulierung — Sofortmaßnahmen Priorität 1 bis 4

Priorität 1 (sofort, 0-1 h):
- Eindämmung — System isolieren oder Account sperren ohne Beweisvernichtung.
- Beweissicherung — Logs einfrieren; Speicherabbild ziehen lassen.
- Interner Alarm — DSB, Geschäftsleitung, IT-Sicherheit.
- Versicherer kontaktieren falls Cyberpolice vorhanden.

Priorität 2 (1-6 h):
- Forensiker beauftragen.
- Passwort- und Token-Reset für betroffene Konten.
- Backups vom Netz trennen.
- Kommunikationssperre bis zur Lagebeurteilung.

Priorität 3 (6-24 h):
- Detaillierte Bestandsaufnahme der betroffenen Verarbeitungen.
- Auftragsverarbeiter informieren.
- Risikoabwägung Art. 33 / Art. 34 DSGVO einleiten.

Priorität 4 (24-72 h):
- Meldung an Aufsichtsbehörde vorbereiten und absenden.
- Strafanzeige bei Insider-Verdacht prüfen.
- Pressemitteilung und Kundenkommunikation vorbereiten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## Vertiefung bei Bedarf

- Bei `dsv-sofortmassnahmen-checkliste` beziehungsweise Generiert eine priorisierte Sofortmaßnahmen-Checkliste innerhalb der ersten Stunden nach Bekanntwerden eines Datenschutzvorfalls: [die zusätzliche Vertiefung laden](./references/vertiefung-dsv-sofortmassnahmen-checkliste.md).

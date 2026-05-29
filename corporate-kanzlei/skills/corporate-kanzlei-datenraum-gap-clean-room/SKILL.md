---
name: corporate-kanzlei-datenraum-gap-clean-room
description: "Gap-Analyse des Datenraums und Clean-Room-Protokoll für M&A-Transaktionen: Identifiziert fehlende Dokumente, verwaltet IRL-Status (Information Request List), trennt sensible Wettbewerberdaten. Normen: DSGVO, GWB Clean-Team-Grundsaetze, MAR. Prüfraster: je Workstream fehlende Belege, IRL-Antwortstand, Clean-Room-Zugangsliste. Output Gap-Tabelle mit Priorisierung, IRL-Update, Clean-Room-Protokoll. Abgrenzung: Aufbau des DR siehe datenraum-aufbau; inhaltliche Vertragsprüfung siehe due-diligence-commercial-contracts."
---

# Datenraum Gap-Analyse und Clean Room

## Triage — klaere vor Beginn

1. Welche Datenraum-Plattform? Welche Dokument-Kategorien fehlen noch?
2. Wie weit ist die IRL (Information Request List) abgearbeitet? Quantifizieren.
3. Welche Workstreams sind zeitkritisch (z.B. Steuer vor DD-Abschluss)?
4. Gibt es kartellrechtliche Clean-Room-Anforderungen (GWB Clean Team fuer Wettbewerber)?
5. Welche sensiblen Daten (HR, Kunden-Namen, Betriebsgeheimnisse) brauchen eingeschraenkten Zugang?
6. Sind W&I-Underwriter im Prozess? (Underwriter-Zugriffsrechte separat regeln)

## Zentrale Normen

- **Art. 5, 28 DSGVO** — Datensparsamkeit; Auftragsverarbeitung; keine unnoetigen Personal-Daten im DR
- **§§ 1, 19 GWB** — kartellrechtliche Clean-Room-Anforderung bei Wettbewerber-Transaktionen; Informationsaustausch verboten bis Freigabe
- **§ 17 UWG** — Geschaeftsgeheimnis; Schutz sensibler Informationen auch im DD-Prozess
- **Art. 18 MAR** — Insider-Log fuer jeden mit Datenraum-Zugang bei borsennotierten Zielgesellschaften

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bundeskartellamt, Leitfaden Clean Team 2019 — kartellrechtlicher Clean Team-Betrieb; nur ausgewaehlte, operativ unabhaengige Personen erhalten Zugang zu wettbewerbssensiblen Informationen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Gap-Analyse: Bewertungsmatrix

| Status | Bedeutung | Handlung |
|---|---|---|
| Vorhanden und vollstaendig | Dokument hochgeladen, aktuell, vollstaendig | Keine Aktion |
| Vorhanden, unvollstaendig | Nur Teilversion; fehlende Anlagen | IRL-Frage; Nachforderung |
| Angekuendigt aber ausstehend | Verkaefer hat Lieferung zugesagt | Follow-up; Eskalation wenn > 48h |
| Nicht vorhanden | Existenz unbekannt | Direkte IRL-Frage; ggf. Alternative anfordern |
| Verweigert | Verkaefer lehnt Offenlegung ab | Begrenzung des Disclosure Letter; Risiko im DD-Report |

## Clean-Room-Protokoll: Kartellrechtliche Anforderungen

Bei Transaktionen zwischen Wettbewerbern prueft das Bundeskartellamt den Informationsaustausch. Ein Clean Room beschraenkt sensible Informationen (Preise, Kunden, Produktionskapazitaeten) auf ein separates Team.

**Clean-Team-Anforderungen:**
1. Mitglieder operativ unabhaengig vom Wettbewerbsbetrieb (keine Einkauf, Vertrieb, Pricing)
2. Schriftliche Verpflichtung jedes Clean-Team-Mitglieds
3. Separate Raeumlichkeiten oder locked-down IT-Umgebung
4. Ergebnisse nur in aggregierter/anonymisierter Form an das Verhandlungsteam
5. Protokollierung aller Clean-Team-Aktivitaeten

## Schritt-fuer-Schritt-Workflow

1. **Ausgangsstatus erfassen** — Datenraum-Index gegen IRL spiegeln; fehlende Positionen markieren
2. **Prioritaeten festlegen** — kritische Pfade (Tax, Litigation, wesentliche Vertraege) zuerst
3. **Follow-up-IRL** — priorisierte Nachforderung; kurze Fristen; klare Formulierung
4. **Kartellrechtliche Pruefung** — Clean-Room-Erfordernis bei Wettbewerber-Transaktionen?
5. **Clean-Team einrichten** — Mitglieder benennen; Verpflichtung unterschreiben lassen
6. **Zugriffsebenen anpassen** — Clean-Room-Ordner im DR separat; keine Cross-Contamination
7. **DSGVO-Massnahmen** — Personaldaten anonymisieren; AVV mit Plattformanbieter pruefen
8. **Gap-Report erstellen** — Statusbericht an Deal-Team; kritische Luecken hervorheben

## Output-Template IRL-Tracker (Ausschnitt)

**Adressat:** Deal-Team / DD-Koordinator — Tonfall strukturiert, actionable

```
IRL-TRACKER (INFORMATION REQUEST LIST)
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Nr. | Workstream | Dokument | Erwartet von | Faellig | Status | Datenraum-ID |
|-----|-----------|---------|-------------|---------|--------|-------------|
| 1.1 | Corporate | Aktuelle Gesellschafterliste | [Verkaefer] | [Datum] | Offen | — |
| 1.2 | Corporate | Satzung (aktuell) | [Verkaefer] | [Datum] | Vorhanden | Tab 1.1 |
| 2.1 | Finanzen | JA 2022 geprueft | [Verkaefer] | [Datum] | Ausstehend | — |
| 3.1 | Vertraege | Top-10-Kundenvertraege | [Verkaefer] | [Datum] | Teilw. vorhanden | Tab 3.1-3.7 |
| 6.1 | Litigation | Klage LG Frankfurt Az. X | [Verkaefer] | [Datum] | Verweigert | — |

KRITISCHE LUECKEN:
- [Nr.]: [Beschreibung] — Eskalation an [NAME] bis [Datum]

CLEAN-ROOM-STATUS:
Team: [NAMEN]
Zugriffsrechte seit: [Datum]
Verpflichtungen unterschrieben: [Ja/Nein]
```

## Rote Schwellen

- Clean-Room-Verletzung (Wettbewerbsinfo ohne Clean-Team) → § 1 GWB; Kartellbusse moeglich
- Personaldaten ungeschwetzt im Datenraum → DSGVO-Bussgeld; Betriebsrat-Rechte verletzt
- Wesentliche Dokumente nicht hochgeladen bis DD-Deadline → DD-Report-Luecken; Seller-Haftungsrisiko
- Keine Download-Protokollierung → kein Nachweis Kaeufer-Kenntnis bei spaeterem Streit

## Quellen

- Art. 5, 28 DSGVO; §§ 1, 19 GWB; § 17 UWG; Art. 18 MAR
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 5

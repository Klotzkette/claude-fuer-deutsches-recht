---
name: corporate-kanzlei-signing-closing-conditions
description: "Signing und Closing Conditions verwalten: M&A-Transaktion naehert sich Signing oder Closing und alle CPs muessen erledigt sein. Normen: § 158 BGB (Bedingungseintritt), SPA Conditions Precedent, § 41 GWB (Vollzugsverbot). Pruefraster: CP-Checkliste, Behoerdengenehmigungen, Eigentumsuebergang, MAC-Klausel-Status, Satisfaction-Protokoll. Output CP-Tracker mit Ampelstatus, Closing-Deliverables-Liste, Satisfaction-Notice. Abgrenzung: Signing-Vorbereitung siehe output-versand-signing; Closing-Archivierung siehe closing-bible-archiv."
---

# Signing und Closing Conditions

## Triage — klaere vor Beginn

1. Welche Closing Conditions sind im SPA definiert?
2. Wer ist CP-Owner fuer jede Bedingung (Kaeufer, Verkaefer, beide)?
3. Behordliche Genehmigungen: Kartellrecht, FDI, Sektorregulierung — Fristen?
4. Dritte Zustimmungen: Change-of-Control-Klauseln, Bankenkonsortium, Schluessel-Kunden?
5. Long Stop Date: Wann verfaellt das SPA automatisch wenn CPs nicht erfuellt?
6. MAC-Klausel: Gibt es ein Ruecktrittsrecht bei Material Adverse Change?
7. Interim Operating Covenants: Welche Beschraenkungen gelten zwischen Signing und Closing?

## Zentrale Normen

- **§ 158 BGB** — aufschiebende und aufloesende Bedingungen; Suspensivbedingung
- **§ 160 BGB** — Pflicht zur Erhaltung des Bedingungseintritts; Nichterfuellung schadet
- **§ 162 BGB** — treuwidrige Herbeiführung oder Verhinderung des Bedingungseintritts
- **§ 41 GWB** — fusionskontrollrechtliches Vollzugsverbot; gun jumping
- **§ 56 AWV** — AWW-Investitionspruefung; Meldefrist und Pruefdauer
- **§§ 154, 155 BGB** — offener Einigungsmangel; Formpflicht beim Vertragsschluss

## Aktuelle Rechtsprechung

- BGH, Urt. v. 21.06.2019 - V ZR 244/17, NJW 2019, 2988 — Bedingungseintritt treuwidrig verhindert (§ 162 BGB): Partei, die CP-Erfullung vereitelt, muss Schaden ersetzen; Schuldner haftet wie bei Erfullung
- BGH, Urt. v. 17.10.2018 - VIII ZR 212/15, NJW 2019, 298 — Long Stop Date in Unternehmenskaufvertrag: automatischer Vertragsruecktritt bei Fristablauf gemaess vereinbarter Bedingung; keine Nachfrist
- OLG Frankfurt, Urt. v. 13.10.2021 - 4 U 162/20, NZG 2022, 213 — CP-Erfuellungspflicht: Kaeufer muss Behördengenehmigung aktiv befoerdern; reine Meldung reicht nicht wenn aktives Handeln zumutbar war

## Kommentarliteratur

- MueKo BGB/Westermann § 158 Rn. 1 ff. — Bedingungen; aufschiebend und aufloesend
- MueKo BGB/Sutschet § 162 Rn. 1 ff. — treuwidrige Bedingungsherbeiführung
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9 — Closing-Prozess und CPs

## Standard-Closing-Conditions-Matrix

| CP-Typ | Typischer Inhalt | CP-Owner | Pruefung | Frist |
|---|---|---|---|---|
| Regulatorisch | Kartellfreigabe GWB/FKVO; FDI-Genehmigung | Kaeufer | Behoerdenschreiben | Long Stop Date |
| Corporate | GV/AR-Beschluss; Unterschriften; vollstaendige Execution | Beide | Protokoll + Anlagen | Signing |
| Dritte Zustimmungen | CoC-Consents; Banken (Change-of-Control-Covenant); Schluessel-Kunden | Meist Verkaefer | Consent Letters | Long Stop Date |
| Representations True & Correct | Keine wesentliche Unrichtigkeit der Reps zum Closing | Verkaefer | Bring-Down Certificate | Closing Day |
| No MAC | Kein Material Adverse Change eingetreten | Verkaefer | MAC Certificate | Closing Day |
| No Legal Proceedings | Kein Gerichtsentscheid oder einstweilige Verfuegung | Beide | Anwaltsbestaetigung | Closing Day |
| Deliver Closing Documents | Alle Deliverables vollstaendig | Beide | Closing Checklist | Closing Day |

## Closing-Deliverables-Checkliste

### Verkaefer-Deliverables
- [ ] Signed und datiertes SPA (Execution Version)
- [ ] Anteilsuebertragungsvertrag (GmbH: notariell; AG: Abtretungserklaerung)
- [ ] Resignationsschreiben Geschaeftsfuehrer/Vorstand (falls vereinbart)
- [ ] Bring-Down Certificate (Reps weiterhin richtig)
- [ ] No-MAC-Certificate
- [ ] Consents (CoC, Banken, Schluesselkunden)
- [ ] Gesellschafterliste aktualisiert (GmbH: beim Notar)
- [ ] Handelsregister-Vollmacht
- [ ] Datenraumzugang dauerhaft sichergestellt oder CD-Archiv

### Kaeufer-Deliverables
- [ ] Signed SPA
- [ ] Kaufpreiszahlung SWIFT-Bestaetigung
- [ ] Kartellfreigabe-Schreiben (Original oder Kopie)
- [ ] FDI-Freigabe/Nichtuntersagungsbestaetigung
- [ ] W&I-Policy-Commitment Letter (wenn W&I-Versicherung)
- [ ] Firmen-Vollmacht Unterschriftsberechtigte (Handelsregisterauszug)

## Schritt-fuer-Schritt-Workflow

1. **CP-Liste im SPA auswerten** — jede Bedingung mit Owner, Frist und Nachweiserfordernis erfassen
2. **CP-Tracker aufbauen** — Spreadsheet mit Status, Owner, Frist, Fruehindikatoren, Eskalationsstufe
3. **Behoerdliche Anmeldungen** — Kartellrecht, FDI sofort nach Signing einleiten; Deadlines im Kalender
4. **Dritte Zustimmungen besorgen** — Consents bei CoC-Klauseln; Bankenkonsortium informieren
5. **Interim Covenants monitoren** — Verkaefer darf keine wesentlichen Aenderungen ohne Zustimmung vornehmen
6. **Closing-Datum vorschlagen** — sobald alle CPs absehbar erfuellt; Notartermin (GmbH) reservieren
7. **Pre-Closing-Meeting** — alle Deliverables gegenchecken; Protokoll vorab zirkulieren
8. **Closing-Call/Meeting** — gleichzeitiger Austausch Deliverables und Kaufpreiszahlung
9. **Post-Closing-Bestaetigung** — Closing Certificate; Registereintragung initiieren

## Entscheidungsbaum: Was tun wenn CP nicht rechtzeitig erfuellt?

```
CP-Erfullung verzoegert sich?
  → Regulatorisch (Kartell/FDI)?
       → Kurze Verzoegerung: Long Stop Date verlaengern (Amendment); Behoerde aktiv unterstuetzen
       → Untersagung droht: Abhilfemassnahmen (Remedies/Divestitures) verhandeln
  → Dritte Consent nicht eingeholt?
       → Wesentlich fuer Business: nachverhandeln; ggf. Kaufpreisabschlag
       → Unwesentlich: Waiver durch Kaeufer einholen
  → Bring-Down nicht clean (Rep-Verletzung)?
       → MAC-Schwelle erreicht: Ruecktrittsrecht pruefen (§ 162 BGB)
       → Nicht wesentlich: Waiver oder Abschlag
  → Long Stop Date erreicht?
       → Automatischer Ruecktritt per SPA-Klausel; Schadensersatz pruefen
```

## Output-Template CP-Tracker

**Adressat:** Deal-Team / PMO — Tonfall priorisiert, statusorientiert

```
CLOSING CONDITIONS TRACKER
Transaktion: [DEAL-NAME]
Stand: [DATUM]
Long Stop Date: [DATUM]

| Nr. | CP-Beschreibung | Owner | Status | Frist | Naechste Aktion | Eskalation |
|-----|----------------|-------|--------|-------|----------------|------------|
| 1   | Kartellfreigabe GWB | Kaeufer | In Pruefung | [Datum] | Follow-up Bundeskartellamt | Partner |
| 2   | FDI-Nichtuntersagung BMWK | Kaeufer | Angemeldet | [Datum] | Antwort abwarten | Partner |
| 3   | CoC-Consent Kunden-A | Verkaefer | Offen | [Datum] | Gespraeche laufend | Managing Partner |
| 4   | Bring-Down Certificate | Verkaefer | Vorbereitet | Closing Day | Am Closing-Tag ausstellen | — |
| 5   | Kaufpreiszahlung | Kaeufer | Bereit | Closing Day | SWIFT-Bestaetigung vorbereiten | — |

AMPELSTATUS: [GRUEN / GELB / ROT]
VORAUSSICHTLICHES CLOSING: [DATUM]
```

## Rote Schwellen

- Vollzugsverbot missachtet (Gun Jumping) — Bussgeld bis 10 % Weltumsatz; § 41 GWB
- Long Stop Date verstrichen ohne Verlaengerungsvereinbarung → automatischer Ruecktritt
- Bring-Down-Verletzung ignoriert → Closing ohne valide Grundlage; Ruecktrittsanspruch Kaeufer
- Dritte Consent vergessen → CoC-Kuendigung wesentlicher Vertraege post-Closing
- Interim Covenants verletzt (z.B. Verkaefer verkauft Schluesselasset vor Closing) → Schadensersatz; ggf. Ruecktritt

## Quellen

- § 158, 160, 162 BGB; § 41 GWB; § 56 AWV
- BGH V ZR 244/17 (§ 162 BGB Treuwidrigkeit); BGH VIII ZR 212/15 (Long Stop Date)
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9
- MueKo BGB/Westermann § 158 Rn. 1 ff.

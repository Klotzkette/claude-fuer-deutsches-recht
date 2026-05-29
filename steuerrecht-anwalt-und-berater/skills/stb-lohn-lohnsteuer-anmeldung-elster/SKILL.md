---
name: stb-lohn-lohnsteuer-anmeldung-elster
description: "Elektronische Lohnsteuer-Anmeldung über ELSTER. Anwendungsfall monatliche oder vierteljaehrliche LSt-Anmeldung KiSt SolZ Pauschalierung Anmeldungs-Schema technische Übermittlung. Methodik Daten aus Lohnabrechnung ELSTER-Formular Prüfen Senden. Output ELSTER-Quittung."
---

# Lohnsteuer-Anmeldung ueber ELSTER

## Kernsachverhalt

Die Lohnsteuer-Anmeldung wird elektronisch ueber ELSTER an das Finanzamt uebermittelt — Pflicht seit Jahren. Der Steuerberater nutzt entweder DATEV-ELSTER-Modul oder ELSTER-Online direkt. Die Anmeldung enthaelt: LSt, KiSt, SolZ, ggf. pauschalierte Loehne. Frist: 10. des Folgemonats (monatlich) bzw. 10. des dem Quartal folgenden Monats (vierteljaehrlich).

## Kaltstart-Rueckfragen

1. Welcher Anmeldungszeitraum — monatlich, vierteljaehrlich, jaehrlich?
2. Liegen alle Lohnabrechnungen vor?
3. Sind pauschalierte Loehne (Minijob, § 37b, § 40a) zu beruecksichtigen?
4. Welches Finanzamt ist zustaendig?
5. Steuer-Nr des AG aktuell?
6. Liegen Sondervergueteungen mit eigener Steuerklasse vor?
7. Welche Korrekturen aus Vormonat (Berichtigung § 153 AO)?
8. ELSTER-Zugang funktioniert (Zertifikat, Passwort)?

## Rechtlicher Rahmen

### Primaernormen

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 41b EStG** — Lohnsteuerbescheinigung.

**§ 40 EStG, § 40a EStG, § 37b EStG** — Pauschalierungen.

**§ 240 AO** — Saeumniszuschlag.

**§ 152 AO** — Verspaetungszuschlag.

**§ 39e EStG** — ELStAM.

### Verwaltungsanweisungen

- BMF zu ELSTER-Verfahren.
- LStR.

## Workflow

### Phase 1 — Daten zusammenstellen

- Bruttoloehne aller AN.
- LSt insgesamt.
- KiSt insgesamt (Konfession der einzelnen AN).
- SolZ insgesamt (SolZ entfaellt fuer Lohnsteuerpflichtige unterhalb der Freigrenze § 3 Abs. 3 SolZG seit 01.01.2021; ab 2025 Freigrenze 18.130 EUR ESt (Einzel) / 36.260 EUR (Zusammenveranlagung); Milderungszone bis Voll-SolZ; aktuelle Grenzen ueber SolZG-Fassung pruefen).
- Pauschal versteuerte Betraege (§ 40 Abs. 1 / Abs. 2 EStG, § 40a EStG, § 37b EStG).
- KSt-Pauschalierung Aushilfen (§ 40a EStG): 25 Prozent (kurzfristig) oder 2 Prozent (Minijob, geht direkt an Knappschaft, nicht ueber LSt-Anmeldung).

### Phase 2 — ELSTER-Formular

| Feld | Inhalt |
|---|---|
| Steuer-Nr | AG-Steuer-Nr |
| Anmeldungszeitraum | Monat/Quartal |
| Bruttoloehne insgesamt | Summe aller Brutto |
| Einbehaltene LSt | Summe LSt |
| KiSt evang/kath | Konfession |
| SolZ | Stand 2026 ggf. 0 |
| Pauschal versteuerte Betraege | § 40, § 40a, § 37b |
| Erstattungsantraege | Lohnsteuer-Ueberzahlung |

### Phase 3 — Pruefung vor Senden

- Plausibilitaet Bruttolohnsumme mit BWA/SuSa (Konto 4120/4130 SKR 03).
- LSt-Summe plausibel zur Bruttolohnsumme (ca. 15-25 Prozent je nach Steuerklassen-Mix).
- SV-Beitraege im Mandantenbericht separat dokumentiert.

### Phase 4 — Sendung und Quittung

- ELSTER-Senden ueber DATEV LODAS Schnittstelle oder ELSTER-Online.
- Sendebestaetigung mit Transaktions-Nummer archivieren.
- FA-Bescheid abwarten (in der Regel automatische Verarbeitung, kein gesonderter Bescheid).

### Phase 5 — Zahlung

- LSt-Faelligkeit: 10. des Folgemonats.
- Ueberweisung an FA-Konto.
- Verspaetungszuschlag § 152 AO: bis 10 Prozent der Anmeldung, max. 25.000 EUR.
- Saeumniszuschlag § 240 AO: 1 Prozent pro Monat.

### Phase 6 — Korrekturen

- Bei spaeter erkanntem Fehler: Berichtigung § 153 AO.
- Berichtigte Anmeldung mit Vermerk "Berichtigung".
- Bei wesentlicher Steuerverkuerzung: ggf. Selbstanzeige § 371 AO.

## Output

- ELSTER-Quittung mit Transaktions-Nummer.
- Lohnsteuer-Anmeldung-Dokumentation in Mandantenakte.
- Buchungssatz (Konto LSt-Verbindlichkeit).

## Strategie und Praxis-Tipps

- Frist 10. des Folgemonats hart — bei wiederholten Verspaetungen Verspaetungszuschlag.
- Pauschalierungs-Optionen pruefen (Minijob 2 Prozent vs. reguläre Lohnsteuer).
- Bei Sondervergueteungen Fuenftel-Regelung § 34 EStG pruefen.
- Bei Mehrfachbeschaeftigung des AN: Steuerklasse 6 fuer Folge-AG.
- StBVV: ELSTER-Anmeldung in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS hat direkte ELSTER-Schnittstelle; bei Sicherheits-Zertifikaten regelmaessige Erneuerung.

## Querverweise

- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 37b, 39e, 40, 40a, 41a, 41b.
- AO §§ 152, 153, 240, 371.
- BMF zu ELSTER-Verfahren.
- LStR.
- SolZ-Freigrenze 2025: 18.130 EUR ESt (Einzel); Milderungszone § 3 Abs. 3 SolZG; aktuelle Freigrenze jaehrlich pruefen (SolZG).

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (SolZ-Freigrenze 2025 eingesetzt) -->

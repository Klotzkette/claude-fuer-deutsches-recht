---
name: stb-lohn-lohnsteuer-monatsabschluss
description: "Monatlicher Lohnsteuer-Monatsabschluss. Anwendungsfall regulaere Lohnabrechnung Bruttolohn LSt KiSt SolZ pauschalierte Loehne SV-Abrechnung Auszahlung Anmeldung. Methodik Standard-Workflow Abrechnungsschritte 39e Tabelle. Output Lohnabrechnungen LSt-Anmeldung Bankueberweisung."
---

# Lohnsteuer-Monatsabschluss

## Kernsachverhalt

Der monatliche Lohnsteuer-Abschluss ist die Hauptarbeit der Lohnbuchhaltung: Bruttolohnermittlung, LSt-Berechnung (Steuerklasse, KiFB, KKB), KiSt, SolZ, pauschalierte Loehne, SV-Beitraege, Auszahlung netto, Buchung im Hauptbuch, Anmeldung LSt beim FA. Der Steuerberater erledigt das mit DATEV LODAS oder Lohn und Gehalt — aber die fachliche Pruefung bleibt seine Verantwortung.

## Kaltstart-Rueckfragen

1. Welcher Abrechnungsmonat?
2. Welche Aenderungen gegenueber Vormonat (Eintritte, Austritte, Gehaltsaenderungen, Sonderzahlungen)?
3. Liegen alle ELStAM-Daten aktuell vor?
4. Liegen Krankheitstage / Urlaubstage vor?
5. Sind Sondervergueteungen (Tantieme, Boni) abzurechnen?
6. Liegen Sachbezuege oder geldwerte Vorteile vor?
7. Sind pauschal versteuerte Loehne (Minijob, Aushilfen) abzurechnen?
8. Welcher LSt-Anmeldungs-Zeitraum (monatlich, vierteljaehrlich, jaehrlich)?

## Rechtlicher Rahmen

### Primaernormen

**§ 38 EStG** — Lohnsteuer-Abzug Pflicht AG.

**§ 39b EStG** — Einbehaltung Lohnsteuer.

**§ 40 EStG** — Pauschalierung in besonderen Faellen.

**§ 40a EStG** — Pauschalierung Aushilfskraefte.

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 3 EStG** — steuerfreie Einnahmen (Kataloge); insbesondere § 3 Nr. 16, 24, 26, 33, 39, 51, 63.

**§ 3b EStG** — Zuschlaege Sonntag, Feiertag, Nacht.

**§ 8 Abs. 2 EStG** — Sachbezuege.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**SGB IV §§ 14, 28d, 28e** — SV-Beitraege.

### Verwaltungsanweisungen

- LStR (Lohnsteuer-Richtlinien).
- LStDV.
- BMF-Schreiben zu Reisekosten, Sachbezuegen.

## Workflow

### Phase 1 — Datenuebernahme

- Stammdaten aus DATEV LODAS/Lohn und Gehalt.
- Aenderungsdaten aus Mandant (Eintritte, Krankheitstage, Sonderzahlungen).
- ELStAM aktuell abrufen.

### Phase 2 — Bruttolohnermittlung

- Grundgehalt aus Stammdatum.
- Stundenlohn bei Stunden-AN.
- Mehrarbeit, Ueberstunden, Schichtzuschlaege.
- Sonn-/Feiertag-/Nachtzuschlaege § 3b EStG (LSt-frei und SV-frei in bestimmten Grenzen).
- Sondervergueteungen: 13. Monatsgehalt, Tantieme, Sonderzahlung.
- Sachbezuege (Verpflegung, Unterkunft mit SvEV-Werten 2026 verifizieren).

### Phase 3 — Lohnsteuer-Berechnung

- LSt-Tabelle automatisch in DATEV LODAS.
- Steuerklasse, KiFB, KKB aus ELStAM.
- Pauschalierung Aushilfen (§ 40a EStG): 2 Prozent (Minijob) oder 25 Prozent (kurzfristig).
- Pauschalierung Sachzuwendungen (§ 37b EStG): 30 Prozent (mit Zuschlag).
- KiSt nach AN-Konfession.
- SolZ aktuell (Stand 2026): SolZ entfaellt fuer den Grossteil der AN; verifizieren bei hoeheren Einkommen.

### Phase 4 — SV-Beitraege

- Beitragsbemessungsgrenzen (BBG) 2026 verifizieren:
  - RV (West): aktueller Wert 2026 ueber DRV/BMAS verifizieren.
  - KV/PV: aktueller Wert 2026 verifizieren (JAEG).
- Beitragssaetze (Stand 2026): RV, AV, KV, PV; aktuelle Saetze ueber GKV-Spitzenverband verifizieren.
- Zusatzbeitrag KV individuell je Kasse.
- Beitragsverteilung AG-/AN-Anteile (jeweils ca. halftig; Ausnahmen PV-Kinderlose, Insolvenzgeld-Umlage).

### Phase 5 — Auszahlung und Buchung

- Nettolohn = Brutto minus LSt/KiSt/SolZ minus SV-AN-Anteile (- Pfaendung, - VL, - Sonderabzug).
- Ueberweisung an AN-Konto.
- Buchung im Hauptbuch (Loehne, SV-AG, LSt-Verbindlichkeit, KK-Verbindlichkeit).

### Phase 6 — Anmeldung Lohnsteuer

- LSt-Anmeldung beim FA ueber ELSTER bis 10. des Folgemonats.
- LSt-Faelligkeit: 10. des Folgemonats; Sofortverfuegung Saeumniszuschlag § 240 AO.
- KiSt parallel angemeldet.
- SolZ ggf. parallel.

## Output

- Lohnabrechnungen aller AN.
- LSt-Anmeldung an FA.
- SV-Beitragsabrechnung an Krankenkassen.
- Buchungssatz fuer Hauptbuch.

## Strategie und Praxis-Tipps

- Frist 10. des Folgemonats fuer LSt-Anmeldung — bei Verspaetung Verspaetungszuschlag.
- BBG und Beitragssaetze 2026 jaehrlich verifizieren (Stand 01.01.2026).
- Bei pauschal versteuerten Loehnen (Minijob 2 Prozent): Buchung separat.
- Sonn-/Feiertag-/Nacht-Zuschlaege § 3b EStG nur LSt- und SV-frei in bestimmten Grenzen; ueber die Grenze normal versteuert/verbeitragt.
- StBVV: Monatsabschluss in Lohnpauschale; Sondertaetigkeiten (Mehrarbeit-Berechnung mit komplexer Schichten-Logik) Zeithonorar.
- DATEV-Tipp: DATEV LODAS Monatsabschluss-Pruefliste vor Anmeldung; Plausibilitaetspruefung Bruttolohnsumme.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-meldungen-sv-elstam-zugang` — ELStAM/SV-Meldungen.
- `stb-lohn-lohnsteuer-anmeldung-elster` — ELSTER-Anmeldung.
- `stb-lohn-sv-beitraege-grundlagen` — SV-Beitraege.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3, 3b, 8, 19, 38, 39b, 40, 40a, 41a; LStR.
- SGB IV §§ 14, 28d, 28e.
- LStDV.
- Verifikations-Hinweis: BBG 2026 RV/KV/PV und Beitragssaetze ueber DRV/BMAS jaehrlich aktualisieren.
- Verifikations-Hinweis: Sachbezugswerte SvEV 2026 (Verpflegung, Unterkunft) verifizieren.

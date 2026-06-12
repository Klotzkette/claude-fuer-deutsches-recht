---
name: lohn-meldungen-sv-elstam-zugang
description: "SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschäftigungsbeginn und Beendigung Anmeldung Abmeldung Änderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik DEUEV-Verfahren ELStAM Prüfung. Output gemeldete Vorgaenge Quittungen."
---

# SV-Meldungen und ELStAM-Verfahren

## Fachlicher Anker

- **Normen:** § 6a, § 28a SGB IV, § 28e SGB IV.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Bei Beschäftigungsbeginn ist der Arbeitnehmer zur Sozialversicherung anzumelden, bei Ende abzumelden. Änderungen (Krankenkasse-Wechsel, Adresse, Steuerklasse) sind zu melden. Parallel erfolgt der elektronische Abruf der Lohnsteuer-Abzugsmerkmale (ELStAM). Das DEUEV-Verfahren (Datenerfassungs- und -uebermittlungsverordnung) steuert die SV-Meldungen, das ELStAM-Verfahren die LSt-Abzugsmerkmale. Beide müssen rechtzeitig und korrekt erfolgen.

## Kaltstart-Rueckfragen

1. Beschäftigungsbeginn — wann, regulaer oder Sofortmeldungspflicht (Bau, Gaststaette, Fleisch, ...)?
2. Steuer-Id des AN vorhanden?
3. Krankenkassen-Wahl bekannt?
4. SV-Status — versicherungspflichtig, geringfuegig, kurzfristig, Werkstudent?
5. AN-Vorbeschaeftigung in laufender Periode (Mehrfachbeschaeftigung)?
6. Liegt Änderungs-Anlass vor (Steuerklasse, Adresse, Kinderfreibetrag)?
7. Bei Beendigung: ordentliche Kuendigung, fristlos, Aufhebungsvertrag?
8. Liegt ELStAM-Sperre vor (Mehrfacharbeitgeber-Konflikt)?

## Rechtlicher Rahmen

### Primaernormen

**§ 28a SGB IV** — Meldepflichten Arbeitgeber.

**§ 28e SGB IV** — Arbeitgeber-Beitragspflicht.

**§ 28f SGB IV** — Aufzeichnungs- und Aufbewahrungspflicht.

**DEUEV** — Verordnung; konkretisiert die Meldepflichten.

**§ 39e EStG** — ELStAM-Verfahren.

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 41b EStG** — elektronische Lohnsteuerbescheinigung.

### Verwaltungsanweisungen

- BMF und BMAS Rundschreiben.
- Gemeinsame Rundschreiben Spitzenverbaende Krankenkassen.
- ITSG (IT-Sicherheitsgesellschaft) — technische Spezifikation.

## Workflow

### Phase 1 — Beschäftigungsbeginn-Anmeldung

| Meldungsart | Inhalt | Frist |
|---|---|---|
| Anmeldung | Beschäftigungsbeginn, AN-Daten | Mit der ersten naechsten Lohnabrechnung, spaetestens 6 Wochen nach Beschäftigungsbeginn |
| Sofortmeldung (Sonderbranchen) | Vor Beschäftigungsbeginn | Spaetestens bei Aufnahme der Beschäftigung |
| Minijob-Anmeldung | Bei Minijob-Zentrale (Knappschaft) | Mit erster Abrechnung |

### Phase 2 — DEUEV-Abgabegruende (Auszug)

- Anmeldung (Grund 10).
- Abmeldung (Grund 30).
- Jahresmeldung (Grund 50).
- Unterbrechungsmeldung (Grund 51).
- Änderung Beitragsgruppe (Grund 11).
- Änderung Personalien (Grund 12).
- Sofortmeldung (Grund 20).

### Phase 3 — ELStAM-Abruf

- Anmeldung beim ELStAM-Verfahren über das BZSt (Bundeszentralamt für Steuern).
- Voraussetzungen: AN-Steuer-ID (11-stellig nach § 139b AO), AG-Steuer-Nr (oder AG-Identifikationsnummer), AG-Betriebsstaetten-Nummer der BA.
- Standard-Abrufintervall: monatlich vor der Lohnabrechnung; in DATEV LODAS automatisiert.
- Bei Änderungen (Steuerklasse, Kinderfreibetrag, Konfession): automatische Aktualisierung durch FA; das AG-System aktualisiert ELStAM beim naechsten Abruf.

### Phase 4 — ELStAM-Sonderfaelle

- Erster Arbeitgeber (Steuerklasse 1-5): Hauptbeschaeftigung.
- Weiterer Arbeitgeber (Steuerklasse 6): hoechste LSt-Belastung.
- Änderung Hauptbeschaeftigung: AN muss FA informieren.
- Bei ELStAM-Sperre durch Konflikt: Sperrgrund prüfen, AN-Aufklaerung.

### Phase 5 — Abmeldung

- Bei Beschäftigungsende: Abmeldung in der naechsten Entgeltabrechnung.
- Grund 30 (regulaer), 34 (Tod), 36 (Renteneintritt).
- ELStAM-Abmeldung automatisch.

### Phase 6 — Dokumentation und Quittungen

- DEUEV-Quittungen archivieren (10 Jahre).
- ELStAM-Quittungen.
- DATEV-Mandantenakte Lohn.

## Strategie und Praxis-Tipps

- Anmeldung rechtzeitig — Sofortmeldungspflicht-Branchen vor Beschäftigungsbeginn melden.
- Bei Sofortmeldungs-Branchen Verspaetung: Bussgelder erheblich (bis 25.000 EUR für den AG).
- ELStAM-Abruf jeden Monat — Änderungen durch FA (KiFB, KKB) werden automatisch wirksam.
- Bei Mehrfachbeschaeftigung: AN muss FA bzgl. Hauptarbeitgeber informieren.
- StBVV: SV/ELStAM-Meldungen pauschal in Lohnabrechnungsentgelt.
- DATEV-Tipp: DATEV LODAS DEUEV-Modul und ELStAM-Schnittstelle automatisiert.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28e, 28f.
- DEUEV.
- EStG §§ 39e, 41a, 41b.
- BMF-Rundschreiben ELStAM.
- ITSG-Spezifikation.

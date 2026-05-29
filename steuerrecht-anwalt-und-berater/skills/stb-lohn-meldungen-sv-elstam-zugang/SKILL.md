---
name: stb-lohn-meldungen-sv-elstam-zugang
description: "SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschaeftigungsbeginn und Beendigung Anmeldung Abmeldung Aenderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik DEUEV-Verfahren ELStAM Prüfung. Output gemeldete Vorgaenge Quittungen."
---

# SV-Meldungen und ELStAM-Verfahren

## Kernsachverhalt

Bei Beschaeftigungsbeginn ist der Arbeitnehmer zur Sozialversicherung anzumelden, bei Ende abzumelden. Aenderungen (Krankenkasse-Wechsel, Adresse, Steuerklasse) sind zu melden. Parallel erfolgt der elektronische Abruf der Lohnsteuer-Abzugsmerkmale (ELStAM). Das DEUEV-Verfahren (Datenerfassungs- und -uebermittlungsverordnung) steuert die SV-Meldungen, das ELStAM-Verfahren die LSt-Abzugsmerkmale. Beide muessen rechtzeitig und korrekt erfolgen.

## Kaltstart-Rueckfragen

1. Beschaeftigungsbeginn — wann, regulaer oder Sofortmeldungspflicht (Bau, Gaststaette, Fleisch, ...)?
2. Steuer-Id des AN vorhanden?
3. Krankenkassen-Wahl bekannt?
4. SV-Status — versicherungspflichtig, geringfuegig, kurzfristig, Werkstudent?
5. AN-Vorbeschaeftigung in laufender Periode (Mehrfachbeschaeftigung)?
6. Liegt Aenderungs-Anlass vor (Steuerklasse, Adresse, Kinderfreibetrag)?
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

### Phase 1 — Beschaeftigungsbeginn-Anmeldung

| Meldungsart | Inhalt | Frist |
|---|---|---|
| Anmeldung | Beschaeftigungsbeginn, AN-Daten | Mit der ersten naechsten Lohnabrechnung, spaetestens 6 Wochen nach Beschaeftigungsbeginn |
| Sofortmeldung (Sonderbranchen) | Vor Beschaeftigungsbeginn | Spaetestens bei Aufnahme der Beschaeftigung |
| Minijob-Anmeldung | Bei Minijob-Zentrale (Knappschaft) | Mit erster Abrechnung |

### Phase 2 — DEUEV-Abgabegruende (Auszug)

- Anmeldung (Grund 10).
- Abmeldung (Grund 30).
- Jahresmeldung (Grund 50).
- Unterbrechungsmeldung (Grund 51).
- Aenderung Beitragsgruppe (Grund 11).
- Aenderung Personalien (Grund 12).
- Sofortmeldung (Grund 20).

### Phase 3 — ELStAM-Abruf

- Anmeldung beim ELStAM-Verfahren ueber das BZSt (Bundeszentralamt fuer Steuern).
- Voraussetzungen: AN-Steuer-ID (11-stellig nach § 139b AO), AG-Steuer-Nr (oder AG-Identifikationsnummer), AG-Betriebsstaetten-Nummer der BA.
- Standard-Abrufintervall: monatlich vor der Lohnabrechnung; in DATEV LODAS automatisiert.
- Bei Aenderungen (Steuerklasse, Kinderfreibetrag, Konfession): automatische Aktualisierung durch FA; das AG-System aktualisiert ELStAM beim naechsten Abruf.

### Phase 4 — ELStAM-Sonderfaelle

- Erster Arbeitgeber (Steuerklasse 1-5): Hauptbeschaeftigung.
- Weiterer Arbeitgeber (Steuerklasse 6): hoechste LSt-Belastung.
- Aenderung Hauptbeschaeftigung: AN muss FA informieren.
- Bei ELStAM-Sperre durch Konflikt: Sperrgrund pruefen, AN-Aufklaerung.

### Phase 5 — Abmeldung

- Bei Beschaeftigungsende: Abmeldung in der naechsten Entgeltabrechnung.
- Grund 30 (regulaer), 34 (Tod), 36 (Renteneintritt).
- ELStAM-Abmeldung automatisch.

### Phase 6 — Dokumentation und Quittungen

- DEUEV-Quittungen archivieren (10 Jahre).
- ELStAM-Quittungen.
- DATEV-Mandantenakte Lohn.

## Output

- DEUEV-Anmeldung/Abmeldung verschickt.
- ELStAM-Abruf erfolgreich (Steuerklasse, KiFB, KV-Status).
- Quittungen in Mandantenakte.

## Strategie und Praxis-Tipps

- Anmeldung rechtzeitig — Sofortmeldungspflicht-Branchen vor Beschaeftigungsbeginn melden.
- Bei Sofortmeldungs-Branchen Verspaetung: Bussgelder erheblich (bis 25.000 EUR fuer den AG).
- ELStAM-Abruf jeden Monat — Aenderungen durch FA (KiFB, KKB) werden automatisch wirksam.
- Bei Mehrfachbeschaeftigung: AN muss FA bzgl. Hauptarbeitgeber informieren.
- StBVV: SV/ELStAM-Meldungen pauschal in Lohnabrechnungsentgelt.
- DATEV-Tipp: DATEV LODAS DEUEV-Modul und ELStAM-Schnittstelle automatisiert.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-lohnsteuer-monatsabschluss` — LSt-Anmeldung.
- `stb-lohn-sv-beitraege-grundlagen` — SV-Beitraege.
- `stb-lohn-sv-meldungen-dakota-svnet` — DAKOTA/sv.net.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28e, 28f.
- DEUEV.
- EStG §§ 39e, 41a, 41b.
- BMF-Rundschreiben ELStAM.
- ITSG-Spezifikation.

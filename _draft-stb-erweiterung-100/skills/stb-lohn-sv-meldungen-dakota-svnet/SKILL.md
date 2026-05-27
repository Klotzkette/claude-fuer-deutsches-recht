---
name: stb-lohn-sv-meldungen-dakota-svnet
description: "SV-Meldungen ueber sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Uebermittlung Pruefung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen."
---

# SV-Meldungen ueber sv.net oder DAKOTA

## Kernsachverhalt

SV-Beitragsnachweise und DEUEV-Meldungen werden elektronisch an die Krankenkassen uebermittelt. Zwei Hauptverfahren: sv.net (kostenfrei, ueber GKV-Spitzenverband) oder DATEV-DAKOTA (kostenpflichtig, mit DATEV-Integration). Der Steuerberater waehlt das passende System, konfiguriert Zugaenge und versendet die Meldungen.

## Kaltstart-Rueckfragen

1. Welches System ist aktuell in Verwendung — sv.net, DAKOTA, anderes?
2. Welche Mandantenzahl rechtfertigt welches System?
3. Welche Krankenkassen sind vertreten?
4. Sind alle ITSG-Zertifikate gueltig?
5. Welche Meldearten sind regelmaessig (Standard, Sondermeldungen)?
6. Welche Sonderaufnahme (Sofortmeldung)?
7. Liegen Erstattungsantraege (U1/U2) vor?
8. Welche Ueberwachung der Quittungen?

## Rechtlicher Rahmen

### Primaernormen

**§ 28a SGB IV** — Meldepflichten elektronisch.

**§ 28b SGB IV** — Form der Meldungen.

**§ 95 SGB IV** — Datenuebermittlungs-Verordnung.

**DEUEV** — Datenerfassungs- und -uebermittlungsverordnung.

### Verwaltungsanweisungen

- ITSG-Spezifikation.
- GKV-Spitzenverband Rundschreiben.

## Workflow

### Phase 1 — System-Wahl

| System | Vorteile | Nachteile |
|---|---|---|
| sv.net (ITSG) | Kostenfrei; Standard GKV-Spitzenverband; sv.net classic ist 2023/2024 abgeloest durch sv.net Online und sv.net Comfort — Stand 2026 Migration ueber ITSG verifizieren | Beschraenkter Funktionsumfang; nicht mandantenoptimal bei vielen AN |
| DATEV DAKOTA | Integriert in DATEV LODAS / Lohn und Gehalt; mandantenoptimiert; jaehrliches Zertifikat ueber DATEV-eService | Kostenpflichtig |
| ITSG-Software anderer Anbieter (z.B. Lexware, Addison) | Mandanten-spezifisch | Pruefung Kosten/Nutzen |

### Phase 2 — Zugang und Zertifikate

- ITSG-Zertifikat pro Mandant erforderlich.
- Erneuerung jaehrlich (oder 3-Jahres-Zertifikat).
- Sicherheitspasswort.

### Phase 3 — Meldungs-Typen

| Meldungsart | Inhalt | Zeitpunkt |
|---|---|---|
| Beitragsnachweis | Voraus-Beitrag laufender Monat | Bis drittletzter Bankarbeitstag |
| Korrigierter Beitragsnachweis | Ist-Beitrag nach Abrechnung | Bis 15. Folgemonat |
| DEUEV-Anmeldung | Beschaeftigungsbeginn AN | Mit naechster Lohnabrechnung |
| DEUEV-Abmeldung | Beschaeftigungsende | Mit naechster Abrechnung |
| Unterbrechungsmeldung | Krankheit > 6 Wochen | Bei Beginn Krankengeld |
| Jahresmeldung | Jahreslohnsumme je AN | Bis 15. Februar Folgejahr |
| Sofortmeldung | Beschaeftigungsbeginn in § 28a Abs 4-Branche | Vor Aufnahme |
| U1/U2-Erstattungsantrag | Krankheits-/Mutterschaftserstattung | Spaetestens 3 Monate nach Ereignis |

### Phase 4 — Sendung

- sv.net oder DAKOTA Sendung.
- Empfangsquittung.
- Bei Fehler: Korrektur und erneute Sendung.

### Phase 5 — Pruefung Quittungen

- Eingehende Quittung vom Server.
- Bei Fehler: Pruefung Stammdaten.
- Bestaetigungsmeldung von der Krankenkasse.

### Phase 6 — Archivierung

- Quittungen 10 Jahre aufbewahren (§ 28f SGB IV).
- Elektronisch in DATEV LODAS oder Mandantenakte.

## Output

- Versendete Meldungen.
- Empfangsquittungen.
- Beleg in Mandantenakte.

## Strategie und Praxis-Tipps

- Bei vielen Mandanten DATEV DAKOTA wirtschaftlich; bei wenigen sv.net ausreichend.
- ITSG-Zertifikate rechtzeitig erneuern — bei Ablauf keine Uebermittlung mehr moeglich.
- Bei Sofortmeldungspflicht-Branchen sofort am Tag der Beschaeftigungsaufnahme.
- Wiederholte Fehlermeldungen (z.B. SV-Nummer nicht erkannt) deuten auf Stammdaten-Fehler hin.
- StBVV: Standardmeldungen in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS automatische ITSG-Zertifikats-Erinnerung.

## Querverweise

- `stb-lohn-meldungen-sv-elstam-zugang` — ELStAM/SV-Meldungen.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-jahresmeldungen-ahn-asn-besondere` — Jahresmeldungen.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28b, 28f, 95.
- DEUEV.
- ITSG-Spezifikation.

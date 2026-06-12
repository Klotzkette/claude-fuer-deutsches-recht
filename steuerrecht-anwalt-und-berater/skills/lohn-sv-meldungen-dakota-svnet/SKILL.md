---
name: lohn-sv-meldungen-dakota-svnet
description: "SV-Meldungen über sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Übermittlung Prüfung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen."
---

# SV-Meldungen über sv.net oder DAKOTA

## Fachlicher Anker

- **Normen:** § 6a, § 28a SGB IV, § 28b SGB IV.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

SV-Beitragsnachweise und DEUEV-Meldungen werden elektronisch an die Krankenkassen uebermittelt. Zwei Hauptverfahren: sv.net (kostenfrei, über GKV-Spitzenverband) oder DATEV-DAKOTA (kostenpflichtig, mit DATEV-Integration). Der Steuerberater waehlt das passende System, konfiguriert Zugaenge und versendet die Meldungen.

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
| sv.net (ITSG) | Kostenfrei; Standard GKV-Spitzenverband; sv.net classic wurde 2024 abgeloest durch sv.net online (Browser) und sv.net comfort (Lokalinstallation); aktuelle Verfuegbarkeit über ITSG.de prüfen | Beschraenkter Funktionsumfang; nicht mandantenoptimal bei vielen AN |
| DATEV DAKOTA | Integriert in DATEV LODAS / Lohn und Gehalt; mandantenoptimiert; jaehrliches Zertifikat über DATEV-eService | Kostenpflichtig |
| ITSG-Software anderer Anbieter (z.B. Lexware, Addison) | Mandanten-spezifisch | Prüfung Kosten/Nutzen |

### Phase 2 — Zugang und Zertifikate

- ITSG-Zertifikat pro Mandant erforderlich.
- Erneuerung jaehrlich (oder 3-Jahres-Zertifikat).
- Sicherheitspasswort.

### Phase 3 — Meldungs-Typen

| Meldungsart | Inhalt | Zeitpunkt |
|---|---|---|
| Beitragsnachweis | Voraus-Beitrag laufender Monat | Bis drittletzter Bankarbeitstag |
| Korrigierter Beitragsnachweis | Ist-Beitrag nach Abrechnung | Bis 15. Folgemonat |
| DEUEV-Anmeldung | Beschäftigungsbeginn AN | Mit naechster Lohnabrechnung |
| DEUEV-Abmeldung | Beschäftigungsende | Mit naechster Abrechnung |
| Unterbrechungsmeldung | Krankheit > 6 Wochen | Bei Beginn Krankengeld |
| Jahresmeldung | Jahreslohnsumme je AN | Bis 15. Februar Folgejahr |
| Sofortmeldung | Beschäftigungsbeginn in § 28a Abs 4-Branche | Vor Aufnahme |
| U1/U2-Erstattungsantrag | Krankheits-/Mutterschaftserstattung | Spaetestens 3 Monate nach Ereignis |

### Phase 4 — Sendung

- sv.net oder DAKOTA Sendung.
- Empfangsquittung.
- Bei Fehler: Korrektur und erneute Sendung.

### Phase 5 — Prüfung Quittungen

- Eingehende Quittung vom Server.
- Bei Fehler: Prüfung Stammdaten.
- Bestaetigungsmeldung von der Krankenkasse.

### Phase 6 — Archivierung

- Quittungen 10 Jahre aufbewahren (§ 28f SGB IV).
- Elektronisch in DATEV LODAS oder Mandantenakte.

## Strategie und Praxis-Tipps

- Bei vielen Mandanten DATEV DAKOTA wirtschaftlich; bei wenigen sv.net ausreichend.
- ITSG-Zertifikate rechtzeitig erneuern — bei Ablauf keine Uebermittlung mehr möglich.
- Bei Sofortmeldungspflicht-Branchen sofort am Tag der Beschäftigungsaufnahme.
- Wiederholte Fehlermeldungen (z.B. SV-Nummer nicht erkannt) deuten auf Stammdaten-Fehler hin.
- StBVV: Standardmeldungen in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS automatische ITSG-Zertifikats-Erinnerung.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28b, 28f, 95.
- DEUEV.
- ITSG-Spezifikation.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (sv.net-Verfuegbarkeit Prüfhinweis ohne Marker) -->

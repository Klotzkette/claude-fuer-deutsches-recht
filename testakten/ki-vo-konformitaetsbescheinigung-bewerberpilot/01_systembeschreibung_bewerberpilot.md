# Systembeschreibung BewerberPilot TalentRank 2.4

Hersteller/Anbieter: BewerberPilot Score GmbH, Köln
Produkt: BewerberPilot TalentRank 2.4
Stand: 13.05.2026
Pilotkundin: Elbtal Klinikservice gGmbH, Dresden

## 1. Zweckbestimmung

BewerberPilot TalentRank unterstützt Recruitingteams bei der Sichtung eingehender Bewerbungen. Das System extrahiert aus Lebensläufen, Anschreiben und Zeugnissen strukturierte Merkmale, vergleicht diese mit Stellenanforderungen und erzeugt eine priorisierte Prüfliste. Es trifft nach Produktbeschreibung keine finale Einstellungsentscheidung und darf nicht ohne menschliche Prüfung zur Ablehnung verwendet werden.

Bestimmungsgemäße Nutzung:

- Sortierung eingehender Bewerbungen nach fachlicher Passung.
- Hervorhebung fehlender Muss-Anforderungen.
- Vorschlag von Interviewfragen.
- Zusammenfassung von Qualifikationen für Recruitingteams.

Nicht bestimmungsgemäße Nutzung:

- Automatisierte Absage ohne menschliche Prüfung.
- Bewertung von Krankheit, Schwangerschaft, Gewerkschaft, Religion, politischer Haltung oder Herkunft.
- Einsatz für Beschäftigtenüberwachung.
- Einsatz zur Leistungs- oder Verhaltensbewertung bestehender Mitarbeitender.

## 2. Rollen

| Akteur | Rolle nach KI-VO | Begründung |
|---|---|---|
| BewerberPilot Score GmbH | Anbieter | Entwickelt und bringt TalentRank unter eigenem Namen in Verkehr |
| Elbtal Klinikservice gGmbH | Betreiber | Nutzt das System in eigener Recruitingorganisation |
| LexiCore Systems Inc. | Komponentenlieferant/GPAI-Anbieter | Liefert allgemeines Sprachmodell für Textzusammenfassung |
| MedData Hosting GmbH | Auftragsverarbeiter/Hosting | Betreibt EU-Hosting in Nürnberg |

## 3. Architektur

1. Upload von Bewerbungsunterlagen in EU-Hosting.
2. Dokumentklassifikation und OCR.
3. Extraktion von Qualifikationen, Berufserfahrung, Zertifikaten.
4. Abgleich mit Stellenprofil.
5. Score zwischen 0 und 100, zusätzlich Muss-Kriterium-Flag.
6. Zusammenfassung und Interviewfragen durch GPAI-Komponente.
7. Anzeige im Recruiter-Dashboard.
8. Menschliche Entscheidung und Protokollierung.

## 4. Daten

- Lebenslauf, Anschreiben, Zeugnisse, Zertifikate.
- Kontaktdaten.
- Berufserfahrung, Ausbildung, Sprachkenntnisse.
- Bewerbungsstatus.
- Manuelle Recruiterkommentare.
- Systemscore und Erklärmerkmale.

Besondere Kategorien personenbezogener Daten sollen technisch nicht ausgewertet werden. Das System kann solche Angaben aber in Bewerbungsunterlagen erkennen; sie werden maskiert und nicht als positives oder negatives Bewertungskriterium verwendet.

## 5. Freigabestand

TalentRank 2.4 ist intern als Release Candidate freigegeben. Der Pilot bei Elbtal soll am 01.08.2026 beginnen. Die Anbieterin möchte vorher keine finale Konformitätsbehauptung abgeben, solange Lücken in Datenherkunft, Human-Oversight-Test und Lieferantennachweisen bestehen.

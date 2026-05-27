---
name: stb-eau-elektronische-arbeitsunfaehigkeit-2023
description: "eAU elektronische Arbeitsunfaehigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration."
---

# eAU — Elektronische Arbeitsunfaehigkeitsbescheinigung

## Kernsachverhalt

Seit 01.01.2023 (mit Uebergangsphase) ist die elektronische Arbeitsunfaehigkeitsbescheinigung (eAU) verpflichtend. AN informiert AG ueber Krankheit; AG ruft eAU-Daten bei der Krankenkasse ueber Schnittstelle ab. Die "gelbe Bescheinigung" auf Papier entfaellt. Voraussetzungen: AG-System mit eAU-Schnittstelle, AN mit GKV (PKV-Versicherte aktuell nicht im eAU-Verfahren).

## Kaltstart-Rueckfragen

1. Hat der AG eAU-Schnittstelle eingerichtet?
2. Welches Lohnprogramm (DATEV LODAS, Lohn und Gehalt)?
3. Welche Krankenkassen sind vertreten?
4. Welche AN sind in PKV (Privat-KV; Ausnahme von eAU)?
5. Welche Mandanten-Schulung der HR-Abteilung erfolgt?
6. Welche Fallback bei Schnittstellen-Stoerung?
7. Welche Konsistenz von Krankheits-Zeiten und Entgeltfortzahlung?
8. Welche § 109 SGB IV-Konformitaet?

## Rechtlicher Rahmen

### Primaernormen

**§ 109 SGB IV** — Elektronisches Verfahren bei Arbeitsunfaehigkeit.

**§ 5 EFZG** — AU-Anzeige- und Nachweispflicht.

**§ 3 EFZG** — Entgeltfortzahlung.

**EFZG, § 5 Abs. 1a (durch eAU-Reform)** — Anpassung Nachweisweg.

### Verwaltungsanweisungen

- BMAS zum eAU-Verfahren.
- GKV-Spitzenverband Rundschreiben.

## Workflow

### Phase 1 — Anmeldung des AG zum eAU-Verfahren

- Schnittstelle ueber DATEV LODAS / Lohn und Gehalt einrichten.
- ITSG-Zertifikat erforderlich.
- Anmeldung beim ITSG-Verfahren.

### Phase 2 — Krankmeldungs-Prozess

```
AN meldet sich krank (Telefon, Mail)
   ↓
AG erfaesst Krankheitsbeginn in Lohnprogramm
   ↓
AG-System ruft automatisch eAU-Daten ab
   ↓
Krankenkasse liefert Diagnose-Codes und Dauer
   ↓
Lohnabrechnung mit Entgeltfortzahlung-Anteil
```

### Phase 3 — Datenruckmeldung

- Krankenkasse liefert: Anfangs-/Enddatum, Diagnose-Code, fortdauernd ja/nein.
- AG-Pflicht: Daten in Lohnabrechnung integrieren.

### Phase 4 — Fallback-Verfahren

- Bei Schnittstellen-Stoerung: traditionelle gelbe Bescheinigung.
- PKV-Versicherte: traditionelle Bescheinigung (eAU bisher nicht).

### Phase 5 — Datenschutz

- Diagnose-Codes werden zwischen Krankenkassen und AG ausgetauscht.
- AG-Geheimhaltungspflicht.
- Kein Weitergabe an Dritte.

### Phase 6 — Mandantenkommunikation

- HR-Abteilung schulen.
- Schnittstellen-Wartung.

## Output

- eAU-Schnittstelle aktiv.
- Krankheits-Lohnabrechnung automatisch.

## Strategie und Praxis-Tipps

- eAU ist Effizienz-Vorteil — keine Papierabholung mehr.
- Bei PKV-Versicherten: traditionelles Verfahren parallel.
- Schnittstellen-Stoerungen: rechtzeitig Test (insbesondere zum Jahreswechsel).
- DATEV-Tipp: DATEV LODAS eAU-Modul mit automatischem Abruf.

## Querverweise

- `stb-lohn-krankheit-entgeltfortzahlung-efzg` — Krankheit.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.
- `stb-lohn-meldungen-sv-elstam-zugang` — SV-Meldungen.

## Quellen und Updates

Stand: 05/2026.

- SGB IV § 109.
- EFZG §§ 3, 5.
- BMAS zum eAU-Verfahren.
- GKV-Spitzenverband Rundschreiben.

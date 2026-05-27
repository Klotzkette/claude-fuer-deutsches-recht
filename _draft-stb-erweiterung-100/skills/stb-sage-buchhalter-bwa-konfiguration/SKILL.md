---
name: stb-sage-buchhalter-bwa-konfiguration
description: "Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage."
---

# Sage Buchhalter BWA

## Kernsachverhalt

Sage ist eine internationale ERP- und Buchhaltungsplattform, in Deutschland mit Sage 100, Sage 50 fuer KMU. Insbesondere bei mittelstaendischen Mandanten haeufig im Einsatz. BWA-Module sind aequivalent zu DATEV/Addison, aber mit anderer Bedienlogik. Steuerberater, die mit Sage-Mandanten arbeiten, brauchen Schnittstellen oder Datenuebernahme.

## Kaltstart-Rueckfragen

1. Welche Sage-Version (Sage 100, Sage 50, Sage Office Line)?
2. Wer betreibt Sage — Mandant selbst oder StB?
3. Welche BWA-Form ist konfiguriert?
4. Welcher Kontenrahmen (SKR 03, SKR 04, individuell)?
5. Welche Schnittstellen zu DATEV (falls vorhanden)?
6. Welche Module aktiv?
7. Welche Mandantenbeguenstigung?
8. Welcher Updates-Stand?

## Workflow

### Phase 1 — System-Setup

- Mandant betreibt Sage selbst; StB hat Lese-Zugriff.
- Oder: StB betreibt Sage als Service.
- Konten-Konfiguration.

### Phase 2 — BWA-Konfiguration

- Sage-Standard-BWA mit fuenf Bloecken.
- Vorjahresvergleich und Plan-Werte.

### Phase 3 — Schnittstellen

- Sage-eRechnung-Modul.
- Bank-Anbindung.
- Datenexport DATEV-Format moeglich (CSV).

### Phase 4 — Datenaustausch mit StB

- Sage-Datenexport monatlich an StB.
- StB importiert in DATEV (DATEV-CSV-Format).
- Alternative: StB hat Sage-Lese-Zugang.

### Phase 5 — Lohn

- Sage HR / Lohn separat (oder externes Lohnprogramm).
- Schnittstelle zu Hauptbuch.

### Phase 6 — Updates

- Jaehrlich; oft cloud-basiert.

## Output

- Konfigurierte Sage-BWA.

## Strategie und Praxis-Tipps

- Bei Sage-Mandanten Datenaustausch standardisieren — CSV-Export ist Standard.
- Datenuebernahme Sage zu DATEV ist Aufwand — Mandantenwechsel sorgfaeltig planen.
- Sage-Schulung ueber Sage-Akademie.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.
- `stb-addison-bwa-konfiguration-tipps` — Addison.

## Quellen und Updates

Stand: 05/2026.

- Sage Dokumentation.

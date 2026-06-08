---
name: eau-elektronische-arbeitsunfaehigkeit
description: "eAU elektronische Arbeitsunfähigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration."
---

# eAU — Elektronische Arbeitsunfaehigkeitsbescheinigung

## Fachlicher Anker

- **Normen:** § 6a, § 109 SGB IV, § 5.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

- Schnittstelle im Lohnprogramm einrichten (DATEV LODAS / Lohn und Gehalt, Sage HR, eGecko, sage Lohn). Konkrete Programmpfade je Lohnprogramm-Version in der Programm-Onlinehilfe oder Dokumentation nachschlagen.
- ITSG-Zertifikat erforderlich (Sicherheitszertifikat für SV-Datenuebermittlung); Verlaengerung jaehrlich.
- Anmeldung des AG zum eAU-Abrufverfahren ueber den GKV-Datenaustausch-Standard (Verfahren der GKV-Spitzenverbaende auf Basis § 109 SGB IV); konkrete technische Konfiguration in der Lohnprogramm-Dokumentation pruefen.

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

### Phase 3 — Datenrueckmeldung

- Krankenkasse liefert: Anfangs- und Enddatum der AU, fortdauernd ja/nein.
- Hinweis: Diagnose-Codes werden seit der eAU-Reform regelmaessig **nicht** mehr an den AG uebermittelt (Datenschutz-Aspekt); konkrete Daten-Felder gemaess GKV-Datenuebermittlungs-Standard pruefen.
- AG-Pflicht: AU-Zeiten in Lohnabrechnung integrieren, Entgeltfortzahlung gemaess § 3 EFZG (bis 6 Wochen).

### Phase 4 — Fallback-Verfahren

- Bei Schnittstellen-Stoerung: traditionelle gelbe Bescheinigung.
- PKV-Versicherte: traditionelle Bescheinigung (eAU bisher nicht).

### Phase 5 — Datenschutz

- Im eAU-Verfahren erhaelt der AG nach geltender Praxis grundsaetzlich nur AU-Beginn, AU-Ende und Information ueber Folgebescheinigung — Diagnose-Codes verbleiben bei der Krankenkasse (DSGVO-konform).
- AG unterliegt Geheimhaltungspflicht hinsichtlich aller AU-bezogenen Daten.
- Keine Weitergabe an Dritte (Ausnahme: gesetzliche Meldungen).

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

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (generischer Programmpfad-Hinweis, nicht versionsspezifisch belegbar, Verweis auf Onlinehilfe) -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

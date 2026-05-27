---
name: stb-belegtransfer-datev-unternehmen-online
description: "Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard."
---

# Belegtransfer ueber DATEV Unternehmen Online

## Kernsachverhalt

DATEV Unternehmen Online (DUO) ist die Standardplattform fuer Belegtransfer zwischen Mandant und StB. Mandant erfasst Belege ueber Smartphone-App, Scanner oder Mailpostfach; StB greift in DATEV Kanzlei-Rechnungswesen direkt zu. Dieser Skill konkretisiert den Belegfluss und die Standard-Workflow-Konfiguration.

## Kaltstart-Rueckfragen

1. Welche Mandanten arbeiten bereits mit DUO?
2. Welche Belegart wird transferiert?
3. Welche Erfassungs-Kanaele (App, Mail, Scanner)?
4. Welche OCR-Qualitaet erforderlich?
5. Welche Bank-Anbindung?
6. Welche eRechnung-Empfaenger?
7. Welche Mandantenfreigabe-Workflow?
8. Welche Archivierung GoBD-konform?

## Workflow

### Phase 1 — Belegerfassung

| Kanal | Anwendung |
|---|---|
| DATEV Upload Online (Mobile App) | Belege per Smartphone scannen |
| Mailpostfach | E-Mail-Rechnungen direkt an DUO-Postfach |
| Scanner | Buero-Scanner mit Standard-PDF |
| eRechnung | XRechnung/ZUGFeRD direkt empfangen |
| Bank-Online | PSD2-Anbindung; Bankbewegungen automatisch |

### Phase 2 — OCR und Beleg-Klassifizierung

- OCR-Erkennung des Beleg-Inhalts (Lieferant, Betrag, Datum, USt).
- Automatische Klassifizierung in DATEV-Konten-Vorschlag.
- Mandantenfreigabe oder direkte Verbuchung.

### Phase 3 — Buchungs-Vorschlag

- DATEV Belegcockpit zeigt Beleg + Buchungsvorschlag.
- Sachbearbeiter prueft und gibt frei.
- Bei manueller Klaerung: Mandantenanfrage.

### Phase 4 — Bank-Anbindung

- Bank-Online ueber PSD2.
- Bankbewegungen automatisch.
- Zuordnung zu Belegen ueber Verwendungszweck.

### Phase 5 — eRechnungs-Empfang

- DUO mit eRechnungs-Postfach.
- XRechnung/ZUGFeRD-Auswertung.
- Automatische Verbuchung moeglich.

### Phase 6 — Archivierung

- GoBD-konform im Originalformat.
- 10 Jahre Aufbewahrung.
- Belege im Mandanten-Online-Postfach.

## Output

- Konfigurierter Belegfluss DUO.
- Buchungen mit Belegverknuepfung.
- GoBD-konforme Archivierung.

## Strategie und Praxis-Tipps

- DUO + DATEV Upload Online = Killer-Kombination fuer effizienten Belegfluss.
- OCR-Qualitaet variabel — Kontrolle durch Sachbearbeiter bleibt Pflicht.
- Bei vielen kleinen Belegen: Mandant taeglich scannen, Sachbearbeiter woechentlich pruefen.
- Bei eRechnungs-Empfang: Automatisierung Hebel.
- DATEV-Tipp: DATEV Upload Online mit GoBD-konformer Mandanten-Schulung.

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-erechnung-pflicht-b2b-2025-2026` — eRechnung.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 147.
- BMF v. 28.11.2019 zu GoBD.
- DATEV DUO Dokumentation.

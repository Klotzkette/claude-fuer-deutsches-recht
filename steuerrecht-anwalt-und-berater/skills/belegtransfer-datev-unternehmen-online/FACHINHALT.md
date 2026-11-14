---
name: belegtransfer-datev-unternehmen-online
description: "Für Belegtransfer über DATEV Unternehmen Online: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Steuerrecht – Steuerberater und Anwälte. Route: belegtransfer-datev-unternehmen-online."
---

# Belegtransfer über DATEV Unternehmen Online

## Fachlicher Anker

- **Normen:** § 6a, §§ 146.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

DATEV Unternehmen Online (DUO) ist die Standardplattform für Belegtransfer zwischen Mandant und StB. Mandant erfasst Belege über Smartphone-App, Scanner oder Mailpostfach; StB greift in DATEV Kanzlei-Rechnungswesen direkt zu. Dieser Skill konkretisiert den Belegfluss und die Standard-Workflow-Konfiguration.

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

- DATEV "Belege Online" / Belegcockpit zeigt Beleg-Bild und Buchungsvorschlag (Konto, USt-Schlüssel, Buchungstext) nebeneinander an.
- Sachbearbeiter prüft den Vorschlag, korrigiert ggf. die Kontierung und gibt frei.
- Bei manueller Klärung wird die Mandantenanfrage über das DUO-Postfach gestellt (revisionssichere Dokumentation).
- Konkrete Menue-Pfade in der aktuellen DATEV-Programmversion ggf. abweichend.

### Phase 4 — Bank-Anbindung

- Bank-Online über PSD2.
- Bankbewegungen automatisch.
- Zuordnung zu Belegen über Verwendungszweck.

### Phase 5 — eRechnungs-Empfang

- DUO mit eRechnungs-Postfach.
- XRechnung/ZUGFeRD-Auswertung.
- Automatische Verbuchung möglich.

### Phase 6 — Archivierung

- GoBD-konform im Originalformat.
- 10 Jahre Aufbewahrung.
- Belege im Mandanten-Online-Postfach.

## Strategie und Praxis-Tipps

- DUO + DATEV Upload Online = Killer-Kombination für effizienten Belegfluss.
- OCR-Qualitaet variabel — Kontrolle durch Sachbearbeiter bleibt Pflicht.
- Bei vielen kleinen Belegen: Mandant taeglich scannen, Sachbearbeiter woechentlich prüfen.
- Bei eRechnungs-Empfang: Automatisierung Hebel.
- DATEV-Tipp: DATEV Upload Online mit GoBD-konformer Mandanten-Schulung.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 147.
- BMF v. 28.11.2019 zu GoBD.
- DATEV Unternehmen Online und "Belege Online" Dokumentation (aktuelle Version prüfen).
- Verifikations-Hinweis: konkrete Programmpfade und Modul-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.
